'''
python3 classify_capture.py \
  --model test_data/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite  \
  --labels test_data/inat_bird_labels.txt
'''


import argparse
import cv2
import numpy as np

from pycoral.adapters.common import input_size
from pycoral.adapters import common
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.adapters import classify


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='.tflite model path')
    parser.add_argument('--labels', help='label file path')
    parser.add_argument('--top_k', type=int, default=1,
                        help='number of categories with highest score to display')
    parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default=0)
    parser.add_argument('--threshold', type=float, default=0.1,
                        help='classifier score threshold')
    parser.add_argument(
        '-a', '--input_mean', type=float, default=128.0,
        help='Mean value for input normalization')
    parser.add_argument(
        '-s', '--input_std', type=float, default=128.0,
        help='STD value for input normalization')
    args = parser.parse_args()

    print('Loading {} with {} labels.'.format(args.model, args.labels))
    interpreter = make_interpreter(args.model)
    interpreter.allocate_tensors()
    labels = read_label_file(args.labels)
    inference_size = input_size(interpreter)

    cap = cv2.VideoCapture(args.camera_idx)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2_im = frame
        cv2_im_rgb = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
        cv2_im_rgb = cv2.resize(cv2_im_rgb, inference_size)
        params = common.input_details(interpreter, 'quantization_parameters')
        scale = params['scales']
        zero_point = params['zero_points']
        mean = args.input_mean
        std = args.input_std
        if abs(scale * std - 1) < 1e-5 and abs(mean - zero_point) < 1e-5:
            # Input data does not require preprocessing.
            common.set_input(interpreter, cv2_im_rgb)
        else:
            # Input data requires preprocessing
            normalized_input = (np.asarray(cv2_im_rgb) - mean) / (std * scale) + zero_point
            np.clip(normalized_input, 0, 255, out=normalized_input)
            common.set_input(interpreter, normalized_input.astype(np.uint8))
        interpreter.invoke()
        classes = classify.get_classes(interpreter, args.top_k, args.threshold)
        cv2_im = add_labels_to_img(cv2_im,  classes, labels)

        cv2.imshow('frame', cv2_im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def add_labels_to_img(cv2_im, classes, labels):
    for c in classes:
        label = '%s: %.5f' % (labels.get(c.id, c.id), c.score)
        print(label)
        cv2_im = cv2.putText(cv2_im, label, (0, 0 + 30),
                             cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
    return cv2_im


if __name__ == '__main__':
    main()
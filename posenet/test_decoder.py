from pose_engine import PoseEngine
import argparse
import cv2
import numpy as np

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

    engine = PoseEngine(
        'models/mobilenet/posenet_mobilenet_v1_075_481_641_quant_decoder_edgetpu.tflite')

    cap = cv2.VideoCapture(args.camera_idx)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2_im = frame
        input_shape = engine.get_input_tensor_shape()
        inference_size = (input_shape[2], input_shape[1])
        cv2_im_rgb = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
        cv2_im_rgb = cv2.resize(cv2_im_rgb, inference_size)
        resized_image = cv2_im_rgb
        input_data = np.asarray(resized_image)
        engine.run_inference(input_data.flatten())
        poses, inference_time = engine.ParseOutput()
        if len(poses)>0:
            print(str(poses[0])[0:60], inference_time)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
import numpy as np
import tflite_runtime.interpreter as tflite
from PIL import Image
from pycoral.adapters import common
import time

def run_tflite_model(tflite_file, input_data):
    # Initialize the interpreter
    interpreter = tflite.Interpreter(model_path=str(tflite_file), experimental_delegates=[tflite.load_delegate('libedgetpu.so.1',  {})])
    interpreter.allocate_tensors()
    image = input_data
    _, scale = common.set_resized_input(
        interpreter, image.size, lambda size: image.resize(size, Image.ANTIALIAS))
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # input_shape = input_details[0]['shape']

    # input_data = np.asarray(input_data).reshape(1, 401, 401, 3)
    # interpreter.set_tensor(input_details[0]['index'], input_data)
    start = time.perf_counter()
    interpreter.invoke()
    inference_time = time.perf_counter() - start
    print('%.2f ms' % (inference_time *1000))
    kp_maps = interpreter.get_tensor(output_details[0]['index'])
    short_offsets = interpreter.get_tensor(output_details[1]['index'])
    # mid_offsets = interpreter.get_tensor(output_details[2]['index'])

    print(np.shape(kp_maps), np.shape(short_offsets))
    return [kp_maps, short_offsets]


input_data = Image.open('couple.jpg')
output_file = 'kp_short_edgetpu.tflite'
predictions = run_tflite_model(output_file, input_data)

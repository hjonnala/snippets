import numpy as np
import tflite_runtime.interpreter as tflite
import os

import time

# Load TFLite model and allocate tensors.
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, 'models', 'mobilenet')
models = [model for model in os.listdir(models_dir) if model.endswith('edgetpu.tflite')]

POSENET_SHARED_LIB = os.path.join(
    'posenet_lib', os.uname().machine, 'macos_posenet_decoder.so')
for model_name in models:
    print(model_name)
    model_path = os.path.join(models_dir, model_name)
    if '_edgetpu' in model_name:
        interpreter = tflite.Interpreter(
            model_path=model_path, experimental_delegates=[tflite.load_delegate('libedgetpu.1.dylib', {}), tflite.load_delegate(POSENET_SHARED_LIB)])
    else:
        interpreter = tflite.Interpreter(model_path=model_path)

    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=input_details[0]['dtype'])
    interpreter.set_tensor(input_details[0]['index'], input_data)
    for i in range(1):
        start = time.perf_counter()
        interpreter.invoke()
        inference_time = time.perf_counter() - start
        print('%.2f ms' % (inference_time * 1000))
    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    for output in output_details:
        print(output['quantization'])
    print(model_path, len(output_data))

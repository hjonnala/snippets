import numpy as np
import tflite_runtime.interpreter as tflite
import os
import time
import platform

_EDGETPU_SHARED_LIB = {
  'Linux': 'libedgetpu.so.1',
  'Darwin': 'libedgetpu.1.dylib',
  'Windows': 'edgetpu.dll'
}[platform.system()]

base_dir = '/home/Downloads/'
model_name = 'deeplabv3_mnv2_pascal_quant_edgetpu.tflite'

model_path = os.path.join(base_dir, model_name)

if 'edgetpu.tflite'  in model_name:
    interpreter = tflite.Interpreter(
        model_path=model_path, experimental_delegates=[tflite.load_delegate(_EDGETPU_SHARED_LIB,  {})])
else:
    interpreter = tflite.Interpreter(model_path=model_path)

interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=input_details[0]['dtype'])
interpreter.set_tensor(input_details[0]['index'], input_data)

inference_time = 0
count = 100
for i in range(count):
    start = time.perf_counter()
    interpreter.invoke()
    inference_time += time.perf_counter() - start
print('%.2f ms' % (inference_time * 1000/count))

output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)

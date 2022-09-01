#!/usr/bin/env python
# coding: utf-8

import numpy as np
import tflite_runtime.interpreter as tflite
import os
import time
import platform
import argparse

_EDGETPU_SHARED_LIB = {
  'Linux': 'libedgetpu.so.1',
  'Darwin': 'libedgetpu.1.dylib',
  'Windows': 'edgetpu.dll'
}[platform.system()]

parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
      '-m', '--model', required=True, help='File path of .tflite file.')

args = parser.parse_args()

model_path = args.model

if 'edgetpu.tflite'  in model_path:
    interpreter = tflite.Interpreter(
        model_path=model_path, experimental_delegates=[tflite.load_delegate(_EDGETPU_SHARED_LIB,  {})])
else:
    interpreter = tflite.Interpreter(model_path=model_path)

interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# input_shape = input_details[0]['shape']
# input_data = np.array(np.random.random_sample(input_shape), dtype=input_details[0]['dtype'])
# interpreter.set_tensor(input_details[0]['index'], input_data)


model_input = np.fromfile('model_input', dtype=np.float32)

interpreter.set_tensor(input_details[0]['index'], model_input.reshape(1, 320, 160, 6))
interpreter.set_tensor(input_details[1]['index'], np.zeros((1, 3), dtype=np.float32))
inference_time = 0
count = 1
for i in range(count):
    start = time.perf_counter()
    interpreter.invoke()
    inference_time += time.perf_counter() - start
print('%.2f ms' % (inference_time * 1000/count))

output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data[0])
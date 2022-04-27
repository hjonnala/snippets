
Coral Dev board 
```
mendel@deft-jet:~$ ./single_model_benchmark --model movenet_single_pose_thunder_ptq_edgetpu.tflite 
2022-04-27 19:09:03
Running ./single_model_benchmark
Run on (4 X 1500 MHz CPU s)
Load Average: 0.00, 0.00, 0.00
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
-----------------------------------------------------
Benchmark           Time             CPU   Iterations
-----------------------------------------------------
BM_Model         44.9 ms         21.8 ms           31 movenet_single_pose_thunder_ptq_edgetpu.tflite

mendel@deft-jet:~$ ./single_model_benchmark --model movenet_single_pose_lightning_ptq_edgetpu.tflite 
2022-04-27 19:09:20
Running ./single_model_benchmark
Run on (4 X 1500 MHz CPU s)
Load Average: 0.00, 0.00, 0.00
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
-----------------------------------------------------
Benchmark           Time             CPU   Iterations
-----------------------------------------------------
BM_Model         26.2 ms         15.2 ms           48 movenet_single_pose_lightning_ptq_edgetpu.tflite
```
Linux Machine with USB accelrator
```
glaptop:~/libcoral/out/k8/benchmarks/coral$ ./single_model_benchmark --model movenet_single_pose_lightning_ptq_edgetpu.tflite
2022-04-27 12:10:56
Running ./single_model_benchmark
Run on (4 X 3900 MHz CPU s)
CPU Caches:
  L1 Data 32K (x2)
  L1 Instruction 32K (x2)
  L2 Unified 256K (x2)
  L3 Unified 4096K (x1)
Load Average: 1.62, 1.17, 0.95
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
-----------------------------------------------------
Benchmark           Time             CPU   Iterations
-----------------------------------------------------
BM_Model         8.08 ms         2.71 ms          262 movenet_single_pose_lightning_ptq_edgetpu.tflite

glaptop:~/libcoral/out/k8/benchmarks/coral$ ./single_model_benchmark --model movenet_single_pose_thunder_ptq_edgetpu.tflite 
2022-04-27 12:11:23
Running ./single_model_benchmark
Run on (4 X 3900 MHz CPU s)
CPU Caches:
  L1 Data 32K (x2)
  L1 Instruction 32K (x2)
  L2 Unified 256K (x2)
  L3 Unified 4096K (x1)
Load Average: 1.61, 1.21, 0.97
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
-----------------------------------------------------
Benchmark           Time             CPU   Iterations
-----------------------------------------------------
BM_Model         16.3 ms         5.29 ms          149 movenet_single_pose_thunder_ptq_edgetpu.tflite
```



Dev Board mini:
```
mendel@undefined-calf:~$ ./single_model_benchmark -model ssdlite_mobiledet_coco_qat_postprocess_edgetpu.tflite
2021-12-10 16:37:16
Running ./single_model_benchmark
Run on (4 X 1300 MHz CPU s)
Load Average: 0.80, 0.26, 0.09
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
-----------------------------------------------------
Benchmark           Time             CPU   Iterations
-----------------------------------------------------
BM_Model         78.2 ms         21.3 ms           32 ssdlite_mobiledet_coco_qat_postprocess_edgetpu.tflite
```

Dev Board:
```
mendel@orange-horse:~$ ./single_model_benchmark -model ssdlite_mobiledet_coco_qat_postprocess_edgetpu.tflite
2021-12-10 16:35:13
Running ./single_model_benchmark
Run on (4 X 1500 MHz CPU s)
Load Average: 0.04, 0.11, 0.06
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
-----------------------------------------------------
Benchmark           Time             CPU   Iterations
-----------------------------------------------------
BM_Model         28.8 ms         19.8 ms           32 ssdlite_mobiledet_coco_qat_postprocess_edgetpu.tflite

```
USB accelerator:
```
hemanthr@hemanth-glaptop:~/libcoral/out/k8/benchmarks/coral$ ./single_model_benchmark -model ssdlite_mobiledet_coco_qat_postprocess_edgetpu.tflite
2021-12-10 08:30:12
Running ./single_model_benchmark
Run on (4 X 3900 MHz CPU s)
CPU Caches:
  L1 Data 32K (x2)
  L1 Instruction 32K (x2)
  L2 Unified 256K (x2)
  L3 Unified 4096K (x1)
Load Average: 1.07, 1.04, 1.00
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
-----------------------------------------------------
Benchmark           Time             CPU   Iterations
-----------------------------------------------------
BM_Model         11.7 ms         4.16 ms          131 ssdlite_mobiledet_coco_qat_postprocess_edgetpu.tflite
```

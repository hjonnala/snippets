```
root@root ~# python3
Python 3.7.3 (default, Jan 22 2021, 20:04:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pycoral.pybind._pywrap_coral import ListEdgeTpus as list_edge_tpus
>>> list_edge_tpus()
[{'type': 'pci', 'path': '/dev/apex_0'}]

```

```
mog@random:~$ python3 -c 'from pycoral.utils.edgetpu import get_runtime_version; print(get_runtime_version())'
BuildLabel(COMPILER=6.3.0 20170516,DATE=redacted,TIME=redacted), RuntimeVersion(14)
```
```
Python 3.9.7 (default, Sep  3 2021, 06:18:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> import tflite_runtime as tflite
>>> import pycoral
>>> from pycoral.utils.edgetpu import get_runtime_version
>>> get_runtime_version()
'BuildLabel(COMPILER=6.3.0 20170516,DATE=redacted,TIME=redacted), RuntimeVersion(14)'
>>> numpy.__version__
'1.19.5'
>>> tflite.__version__
'2.5.0.post1'
>>> pycoral.__version__
'2.0.0'
>>> 
```
```
bash enable_lk_fastboot.sh
**********************************************************************
Unable to connect to debug board, check connection or manually toggle GPIO.
**********************************************************************
/tmp/tmp.A2frymb1B7 ~/Downloads/excelsior-eagle-20201210233645
INFO: pySerial version: (3.5)
INFO: Use config file: /tmp/tmp.A2frymb1B7/dl_addr.ini
INFO: Waiting to connect platform...
INFO: Got /dev/ttyACM0
INFO: Connect brom
INFO: Loading file: lk.bin
INFO: Send lk.bin
INFO: Jump da
```

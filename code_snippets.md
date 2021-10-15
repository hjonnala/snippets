```
root@root ~# python3
Python 3.7.3 (default, Jan 22 2021, 20:04:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pycoral.pybind._pywrap_coral import ListEdgeTpus as list_edge_tpus
>>> list_edge_tpus()
[{'type': 'pci', 'path': '/dev/apex_0'}]

```

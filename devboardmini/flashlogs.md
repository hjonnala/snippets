```
hemanth:~/Downloads/excelsior-eagle-20201210233645$ bash enable_lk_fastboot.sh 
**********************************************************************
Unable to connect to debug board, check connection or manually toggle GPIO.
**********************************************************************
/tmp/tmp.QbpOLX6s7i ~/Downloads/excelsior-eagle-20201210233645
INFO: pySerial version: (3.5)
INFO: Use config file: /tmp/tmp.QbpOLX6s7i/dl_addr.ini
INFO: Waiting to connect platform...
INFO: Got /dev/ttyACM0
INFO: Connect brom
INFO: Loading file: lk.bin
INFO: Send lk.bin
INFO: Jump da
~/Downloads/excelsior-eagle-20201210233645
```
```
hemanth:~/Downloads/excelsior-eagle-20201210233645$ fastboot devices
0123456789ABCDEF        fastboot
```

```
hemanth:~/Downloads/excelsior-eagle-20201210233645$ bash flash.sh
Sending 'mmc0' (33 KB)                             OKAY [  0.003s]
Writing 'mmc0'                                     OKAY [  0.016s]
Finished. Total time: 0.025s
Sending 'mmc0boot0' (87 KB)                        OKAY [  0.005s]
Writing 'mmc0boot0'                                OKAY [  0.135s]
Finished. Total time: 0.146s
Sending 'mmc0boot1' (4 KB)                         OKAY [  0.002s]
Writing 'mmc0boot1'                                OKAY [  0.069s]
Finished. Total time: 0.076s
Sending 'bootloaders' (791 KB)                     OKAY [  0.032s]
Writing 'bootloaders'                              OKAY [  0.026s]
Finished. Total time: 0.065s
Invalid sparse file format at header magic
Sending sparse 'boot' 1/1 (26509 KB)               OKAY [  1.042s]
Writing 'boot'                                     OKAY [  0.694s]
Finished. Total time: 1.919s
Sending sparse 'rootfs' 1/25 (64326 KB)            OKAY [  2.508s]
Writing 'rootfs'                                   OKAY [  1.603s]
Sending sparse 'rootfs' 2/25 (65520 KB)            OKAY [  2.601s]
Writing 'rootfs'                                   OKAY [  1.670s]
Sending sparse 'rootfs' 3/25 (61040 KB)            OKAY [  2.554s]
Writing 'rootfs'                                   OKAY [  1.819s]
Sending sparse 'rootfs' 4/25 (65533 KB)            OKAY [  2.611s]
Writing 'rootfs'                                   OKAY [  1.635s]
Sending sparse 'rootfs' 5/25 (65532 KB)            OKAY [  2.594s]
Writing 'rootfs'                                   OKAY [  1.555s]
Sending sparse 'rootfs' 6/25 (65532 KB)            OKAY [  2.525s]
Writing 'rootfs'                                   OKAY [  1.592s]
Sending sparse 'rootfs' 7/25 (65532 KB)            OKAY [  2.253s]
Writing 'rootfs'                                   OKAY [  1.576s]
Sending sparse 'rootfs' 8/25 (60836 KB)            OKAY [  2.672s]
Writing 'rootfs'                                   OKAY [  1.486s]
Sending sparse 'rootfs' 9/25 (64976 KB)            OKAY [  2.454s]
Writing 'rootfs'                                   OKAY [  1.567s]
Sending sparse 'rootfs' 10/25 (64996 KB)           OKAY [  2.690s]
Writing 'rootfs'                                   OKAY [  1.584s]
Sending sparse 'rootfs' 11/25 (65532 KB)           OKAY [  2.513s]
Writing 'rootfs'                                   OKAY [  1.574s]
Sending sparse 'rootfs' 12/25 (65077 KB)           OKAY [  2.489s]
Writing 'rootfs'                                   OKAY [  1.627s]
Sending sparse 'rootfs' 13/25 (64981 KB)           OKAY [  2.675s]
Writing 'rootfs'                                   OKAY [  1.603s]
Sending sparse 'rootfs' 14/25 (63390 KB)           OKAY [  2.701s]
Writing 'rootfs'                                   OKAY [  1.605s]
Sending sparse 'rootfs' 15/25 (65508 KB)           OKAY [  2.685s]
Writing 'rootfs'                                   OKAY [  1.866s]
Sending sparse 'rootfs' 16/25 (65531 KB)           OKAY [  2.646s]
Writing 'rootfs'                                   OKAY [  1.681s]
Sending sparse 'rootfs' 17/25 (65532 KB)           OKAY [  2.698s]
Writing 'rootfs'                                   OKAY [  1.581s]
Sending sparse 'rootfs' 18/25 (65532 KB)           OKAY [  2.567s]
Writing 'rootfs'                                   OKAY [  1.628s]
Sending sparse 'rootfs' 19/25 (65168 KB)           OKAY [  2.589s]
Writing 'rootfs'                                   OKAY [  1.572s]
Sending sparse 'rootfs' 20/25 (59394 KB)           OKAY [  2.420s]
Writing 'rootfs'                                   OKAY [  1.521s]
Sending sparse 'rootfs' 21/25 (65532 KB)           OKAY [  2.621s]
Writing 'rootfs'                                   OKAY [  1.588s]
Sending sparse 'rootfs' 22/25 (63540 KB)           OKAY [  2.546s]
Writing 'rootfs'                                   OKAY [  1.525s]
Sending sparse 'rootfs' 23/25 (65532 KB)           OKAY [  2.674s]
Writing 'rootfs'                                   OKAY [  1.586s]
Sending sparse 'rootfs' 24/25 (65532 KB)           OKAY [  2.648s]
Writing 'rootfs'                                   OKAY [  1.589s]
Sending sparse 'rootfs' 25/25 (14560 KB)           OKAY [  0.591s]
Writing 'rootfs'                                   OKAY [  0.356s]
Finished. Total time: 101.863s
Rebooting                                          OKAY [  0.002s]
Finished. Total time: 0.052s
Flash completed.
hemanth:~/Downloads/excelsior-eagle-20201210233645$ 
```

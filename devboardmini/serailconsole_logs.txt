[  166.215903] configfs-gadget gadget: high-speed config #1: c
[  166.221492] gs_console_connect: port num [0] is not support console

F0: 102B 0000
F3: 0000 0000
V0: 0000 0000 [0001]
00: 0000 0000
BP: 0400 0041 [0000]
G0: 1190 0000
EC: 0000 1000 [0001]
T0: 0000 0212 [000F]
Jump to BL

NOTICE:  BL2: v2.3():c1984dc174fa
NOTICE:  BL2: Built : 08:07:51, Oct  2 2020
NOTICE:  CHIPSET: MT8167
[PWRAP] pmic ID: 2092.
[EMI] MDL number = 0 
[EMI] LPDDR3
Vcore HV NV LV, Vdram HV NV LV
0x5f 0x48 0x3f, 0xb 0x0 0x3
[EMI] Use default emigen emi settings 
[EMI] Config emi settings:
EMI_CONA=0x2a052,   EMI_CONH=0x3
EMI_RAMK0=0x40000000, EMI_RAMK1=0x40000000
EMI_CONA=0x2a052
EMI_CONF=0x4210000
EMI_CONH=0x3

[DramcSwImpedanceCal] FINAL: DRVP=8, DRVN=7

LPDDR3 Pinmux 2
SSC OFF
DRAM Clock: 1584MHz

[Write Leveling]
WriteLevelingMoveDQSInsteadOfCLK
===============================================================================
Dram Type= 3, Freqency= 1600, rank 1
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
WL Clk delay = 0, CA CLK delay = 0
No need to update CA/CS delay because the CLK delay is small than CA training.
Final Clk output delay = 0
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS0 delay =  27
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS1 delay =  27
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS2 delay =  26
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS3 delay =  26
[DramcWriteLeveling] ====Done====
[DramRankNumberDetection] 2, 0x0
LPDDR3 Pinmux 2
SSC OFF
DRAM Clock: 1584MHz

[CATrainingLP3]
FINAL: CA0  (1~32) 16
FINAL: CA1  (0~30) 15
FINAL: CA2  (1~31) 16
FINAL: CA3  (0~30) 15
FINAL: CA5  (1~31) 16
FINAL: CA6  (1~31) 16
FINAL: CA7  (1~31) 16
FINAL: CA8  (2~32) 17
FINAL: CA4  (1~32) 16
FINAL: CA9  (1~32) 16
=========================================
u4GoldenPattern 0xrank0:
Macro0 Clk Dealy is 0, CA delay is 15
rank1:
Macro0 Clk Dealy is 0, CA delay is 15
[CATrainingLP3] ====Done====


[Write Leveling]
WriteLevelingMoveDQSInsteadOfCLK
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
WL Clk delay = 0, CA CLK delay = 0
No need to update CA/CS delay because the CLK delay is small than CA training.
Final Clk output delay = 0
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS0 delay =  29
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS1 delay =  29
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS2 delay =  27
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS3 delay =  27
[DramcWriteLeveling] ====Done====

[Gating]
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
[Byte 0]First pass (1, 6, 12)
[Byte 1]First pass (1, 6, 12)
[Byte 2]First pass (1, 6, 12)
[Byte 3]First pass (1, 6, 12)
[Byte 3]Bigger pass win(2, 0, 3)  Pass tap=55
[Byte 0]Bigger pass win(2, 0, 4)  Pass tap=56
[Byte 1]Bigger pass win(2, 0, 4)  Pass tap=56
[Byte 2]Bigger pass win(2, 0, 4)  Pass tap=56
===============================================================================
    dqs input gating widnow, final delay value
    Frequency=1600  rank=0
===============================================================================
R0 FINAL: GW best DQS0 P0 delay(2T, 0.5T, PI) = (1, 7, 8) [tap = 56]
R0 FINAL: GW best DQS1 P0 delay(2T, 0.5T, PI) = (1, 7, 8) [tap = 56]
R0 FINAL: GW best DQS2 P0 delay(2T, 0.5T, PI) = (1, 7, 8) [tap = 56]
R0 FINAL: GW best DQS3 P0 delay(2T, 0.5T, PI) = (1, 7, 7) [tap = 55]
R0 FINAL: GW best DQS0 P1 delay(2T, 0.5T, PI) = (2, 1, 8)
R0 FINAL: GW best DQS1 P1 delay(2T, 0.5T, PI) = (2, 1, 8)
R0 FINAL: GW best DQS2 P1 delay(2T, 0.5T, PI) = (2, 1, 8)
R0 FINAL: GW best DQS3 P1 delay(2T, 0.5T, PI) = (2, 1, 7)
[DramcRxdqsGatingCal] ====Done====

[DATLAT]
DATLAT Default value = 0x10
5, 0x6, 0x7, 0x8, 0x9, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0xpattern=5 first_step=15 total pass=6 best_step=17
R0 FINAL: DATLAT = 17 [15 ~ 20]
[DramcRxdatlatCal] ====Done====

[RX]
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
RX Window Sum 765
R0 FINAL: RX Bit 0, 16 (5 ~ 27) 23
R0 FINAL: RX Bit 1, 14 (2 ~ 26) 25
R0 FINAL: RX Bit 2, 13 (0 ~ 26) 27
R0 FINAL: RX Bit 3, 13 (3 ~ 24) 22
R0 FINAL: RX Bit 4, 18 (7 ~ 29) 23
R0 FINAL: RX Bit 5, 16 (3 ~ 30) 28
R0 FINAL: RX Bit 6, 17 (6 ~ 29) 24
R0 FINAL: RX Bit 7, 17 (5 ~ 30) 26
R0 FINAL: RX Bit 8, 17 (5 ~ 29) 25
R0 FINAL: RX Bit 9, 17 (5 ~ 29) 25
R0 FINAL: RX Bit 10, 15 (2 ~ 29) 28
R0 FINAL: RX Bit 11, 18 (7 ~ 29) 23
R0 FINAL: RX Bit 12, 18 (8 ~ 29) 22
R0 FINAL: RX Bit 13, 18 (6 ~ 30) 25
R0 FINAL: RX Bit 14, 18 (8 ~ 29) 22
R0 FINAL: RX Bit 15, 17 (3 ~ 31) 29
R0 FINAL: RX Bit 16, 18 (4 ~ 32) 29
R0 FINAL: RX Bit 17, 18 (5 ~ 32) 28
R0 FINAL: RX Bit 18, 16 (2 ~ 30) 29
R0 FINAL: RX Bit 19, 17 (4 ~ 30) 27
R0 FINAL: RX Bit 20, 14 (2 ~ 26) 25
R0 FINAL: RX Bit 21, 15 (3 ~ 27) 25
R0 FINAL: RX Bit 22, 13 (2 ~ 25) 24
R0 FINAL: RX Bit 23, 14 (2 ~ 27) 26
R0 FINAL: RX Bit 24, 18 (7 ~ 30) 24
R0 FINAL: RX Bit 25, 19 (8 ~ 30) 23
R0 FINAL: RX Bit 26, 18 (5 ~ 32) 28
R0 FINAL: RX Bit 27, 20 (8 ~ 33) 26
R0 FINAL: RX Bit 28, 19 (9 ~ 30) 22
R0 FINAL: RX Bit 29, 19 (8 ~ 30) 23
R0 FINAL: RX Bit 30, 18 (9 ~ 28) 20
R0 FINAL: RX Bit 31, 17 (7 ~ 27) 21
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
DQS Delay :
DQS0 = 0, DQS1 = 0, DQS2 = 0, DQS3 = 0
DQM Delay :
DQM0 = 15, DQM1 = 17, DQM2 = 15, DQM3 = 18
DQ Delay :
DQ0 =16, DQ1 =14, DQ2 =13, DQ3 =13 
DQ4 =18, DQ5 =16, DQ6 =17, DQ7 =17 
DQ8 =17, DQ9 =17, DQ10 =15, DQ11 =18 
DQ12 =18, DQ13 =18, DQ14 =18, DQ15 =17 
DQ16 =18, DQ17 =18, DQ18 =16, DQ19 =17 
DQ20 =14, DQ21 =15, DQ22 =13, DQ23 =14 
DQ24 =18, DQ25 =19, DQ26 =18, DQ27 =20 
DQ28 =19, DQ29 =19, DQ30 =18, DQ31 =17 
________________________________________________________________________
[DramcRxWindowPerbitCal] ====Done====

[TX]
[DramcTxWindowPerbitCal] Frequency=1600, Rank=0, calType=2
[DramcTxWindowPerbitCal] Begin, TX DQ(2, 2),  DQ OEN(2, 0)
TX Window Sum 737
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
R0 FINAL: TX Bit0 (34~56) 23 45,   Bit8 (37~58) 22 47,  Bit16 (33~53) 21 43,   Bit24 (36~57) 22 46
R0 FINAL: TX Bit1 (30~54) 25 42,   Bit9 (35~58) 24 46,  Bit17 (32~53) 22 42,   Bit25 (35~57) 23 46
R0 FINAL: TX Bit2 (32~55) 24 43,   Bit10 (35~58) 24 46,  Bit18 (32~53) 22 42,   Bit26 (34~57) 24 45
R0 FINAL: TX Bit3 (34~54) 21 44,   Bit11 (36~60) 25 48,  Bit19 (32~53) 22 42,   Bit27 (36~57) 22 46
R0 FINAL: TX Bit4 (36~57) 22 46,   Bit12 (36~60) 25 48,  Bit20 (29~51) 23 40,   Bit28 (35~56) 22 45
R0 FINAL: TX Bit5 (36~57) 22 46,   Bit13 (36~59) 24 47,  Bit21 (31~53) 23 42,   Bit29 (33~57) 25 45
R0 FINAL: TX Bit6 (35~57) 23 46,   Bit14 (35~59) 25 47,  Bit22 (30~51) 22 40,   Bit30 (33~55) 23 44
R0 FINAL: TX Bit7 (35~57) 23 46,   Bit15 (38~59) 22 48,  Bit23 (31~53) 23 42,   Bit31 (33~56) 24 44

==================================================================
Byte0, PI DQ Delay 44 Delay2 45
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 45)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 45)

Byte1, PI DQ Delay 47 Delay2 48
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 48)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 48)

Byte2, PI DQ Delay 41 Delay2 42
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 42)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 42)

Byte3, PI DQ Delay 45 Delay2 45
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 45)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 45)

[DramcTxWindowPerbitCal] ====Done====

[Gating]
===============================================================================
Dram Type= 3, Freqency= 1600, rank 1
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
[Byte 0]First pass (1, 6, 8)
[Byte 1]First pass (1, 6, 8)
[Byte 2]First pass (1, 6, 8)
[Byte 3]First pass (1, 6, 8)
[Byte 0]Bigger pass win(2, 0, 0)  Pass tap=56
[Byte 1]Bigger pass win(2, 0, 0)  Pass tap=56
[Byte 2]Bigger pass win(2, 0, 0)  Pass tap=56
[Byte 3]Bigger pass win(2, 0, 0)  Pass tap=56
===============================================================================
    dqs input gating widnow, final delay value
    Frequency=1600  rank=1
===============================================================================
R1 FINAL: GW best DQS0 P0 delay(2T, 0.5T, PI) = (1, 7, 4) [tap = 56]
R1 FINAL: GW best DQS1 P0 delay(2T, 0.5T, PI) = (1, 7, 4) [tap = 56]
R1 FINAL: GW best DQS2 P0 delay(2T, 0.5T, PI) = (1, 7, 4) [tap = 56]
R1 FINAL: GW best DQS3 P0 delay(2T, 0.5T, PI) = (1, 7, 4) [tap = 56]
R1 FINAL: GW best DQS0 P1 delay(2T, 0.5T, PI) = (2, 1, 4)
R1 FINAL: GW best DQS1 P1 delay(2T, 0.5T, PI) = (2, 1, 4)
R1 FINAL: GW best DQS2 P1 delay(2T, 0.5T, PI) = (2, 1, 4)
R1 FINAL: GW best DQS3 P1 delay(2T, 0.5T, PI) = (2, 1, 4)
[DramcRxdqsGatingCal] ====Done====

[DATLAT]
DATLAT Default value = 0x11
5, 0x6, 0x7, 0x8, 0x9, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0xpattern=5 first_step=15 total pass=6 best_step=17
R1 FINAL: DATLAT = 17 [15 ~ 20]
[DramcRxdatlatCal] ====Done====
[DramcRxdqsGatingPostProcess] p->frequency 1600
[DramcRxdqsGatingPostProcess] s1ChangeDQSINCTL 0, reg_TX_dly_DQSgated_min 3, u1TXDLY_Cal_min 3
[DramcDualRankRxdatlatCal] RANK0: 17, RANK1: 17, Final_Datlat 17
[Get MRR] Vendor 5.
[Get MRR] MR8 1f1f.
[Get MRR] Rank 0, u1DieNumber 1, Desity 0x40000000.
[Get MRR] MR8 1f1f.
[Get MRR] Rank 1, u1DieNumber 1, Desity 0x40000000.
[vDramcUpdateEmiSetting] EMI_CONA 0x2a052, EMI_CONH 0x3
[vDramcACTimingOptimize] Density 7, u1TRFC 73, u1TRFCpb 25, u1TRFC_05T 0, u1TXREFCNT 86

Settings after calibration ...
=== [DramcRunTimeConfig] ===
HW_GATING: ON
DUMMY_READ_FOR_TRACKING: ON
DFS_HW_SYNC_GATING_TRACKING: OFF
ZQCS_ENABLE: ON
LOWPOWER_GOLDEN_SETTINGS(DCM): ON
SPM_CONTROL_AFTERK: ON
TEMP_SENSOR_ENABLE: OFF
ENABLE_PER_BANK_REFRESH: OFF
HW_SAVE_FOR_SR: OFF
=========================
[MEM] complex R/W mem test pass
NOTICE:  BL2: Booting BL31


U-Boot 2019.10 (Dec 09 2020 - 23:51:30 +0000), Build: jenkins-excelsior.excelsior-bootloader-2

CPU:   MediaTek MT8516
DRAM:  512 MiB
WDT:   Started with servicing (60s timeout)
MMC:   mmc@11120000: 0
Loading Environment from MMC... OK
In:    serial@11005000
Out:   serial@11005000
Err:   serial@11005000
8GB mmc detected
Hit any key to stop autoboot:  0 
gpio: pin 42 (gpio 42) value is 1
switch to partitions #0, OK
mmc0(part 0) is current device
1420 bytes read in 0 ms
## Executing script at 4c000000
Loading image...
6747990 bytes read in 86 ms (74.8 MiB/s)
Loading device tree...
42834 bytes read in 2 ms (20.4 MiB/s)
104 bytes read in 1 ms (101.6 KiB/s)
## Loading kernel from FIT Image at 4a000000 ...
   Using 'conf@1' configuration
   Trying 'kernel@1' kernel subimage
     Description:  Linux kernel
     Type:         Kernel Image
     Compression:  gzip compressed
     Data Start:   0x4a0000e4
     Data Size:    6746273 Bytes = 6.4 MiB
     Architecture: AArch64
     OS:           Linux
     Load Address: 0x40080000
     Entry Point:  0x40080000
     Hash algo:    sha256
     Hash value:   0470380bb98e5f4131f5dec4c7721e059de557065168fa7ba4ad6ad0caa94b65
   Verifying Hash Integrity ... sha256+ OK
## Flattened Device Tree blob at 42000000
   Booting using the fdt blob at 0x42000000
   Uncompressing Kernel Image
   Loading Device Tree to 000000005fb7e000, end 000000005fb8bfff ... OK

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd041]
[    0.000000] Linux version 4.19.125-mtk (pbuilder@linux-mtk-44a92093-5a4b-410b-8ad5-805072874b42-7qs4k-8xlpx) (gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP PREEMPT Thu Dec 10 02:36:13 UTC 2020
[    0.000000] Machine model: Google Coral MT8167
[    0.000000] efi: Getting EFI parameters from FDT:
[    0.000000] efi: UEFI not found.
[    0.000000] cma: Reserved 64 MiB at 0x00000000bc000000
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv1.1 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: Trusted OS migration not required
[    0.000000] psci: SMC Calling Convention v1.1
[    0.000000] random: get_random_bytes called from start_kernel+0x98/0x44c with crng_init=0
[    0.000000] percpu: Embedded 22 pages/cpu s53144 r8192 d28776 u90112
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] Speculative Store Bypass Disable mitigation not required
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 516064
[    0.000000] Kernel command line: root=PARTUUID=02f36a4f-4562-46b2-bbec-bfc1682f9e92 rootwait
[    0.000000] Dentry cache hash table entries: 262144 (order: 9, 2097152 bytes)
[    0.000000] Inode-cache hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.000000] Memory: 1978928K/2097024K available (9788K kernel code, 1086K rwdata, 3104K rodata, 832K init, 978K bss, 52560K reserved, 65536K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=64 to nr_cpu_ids=4.
[    0.000000]  Tasks RCU enabled.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: GICv2 detected, but range too small and irqchip.gicv2_force_probe not set
[    0.000000] arch_timer: cp15 timer(s) running at 13.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x2ff89eacb, max_idle_ns: 440795202429 ns
[    0.000004] sched_clock: 56 bits at 13MHz, resolution 76ns, wraps every 4398046511101ns
[    0.000106] clocksource: timer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 147020034397 ns
[    0.000117] sched_clock: 32 bits at 13MHz, resolution 76ns, wraps every 165191050201ns
[    0.000548] Console: colour dummy device 80x25
[    0.000909] console [tty0] enabled
[    0.000938] Calibrating delay loop (skipped), value calculated using timer frequency.. 26.00 BogoMIPS (lpj=52000)
[    0.000963] pid_max: default: 32768 minimum: 301
[    0.001061] Security Framework initialized
[    0.001078] SELinux:  Initializing.
[    0.001176] Mount-cache hash table entries: 4096 (order: 3, 32768 bytes)
[    0.001201] Mountpoint-cache hash table entries: 4096 (order: 3, 32768 bytes)
[    0.023967] ASID allocator initialised with 32768 entries
[    0.031961] rcu: Hierarchical SRCU implementation.
[    0.040295] EFI services will not be available.
[    0.048014] smp: Bringing up secondary CPUs ...
[    0.080201] Detected VIPT I-cache on CPU1
[    0.080251] CPU1: Booted secondary processor 0x0000000001 [0x410fd041]
[    0.112278] Detected VIPT I-cache on CPU2
[    0.112320] CPU2: Booted secondary processor 0x0000000002 [0x410fd041]
[    0.144361] Detected VIPT I-cache on CPU3
[    0.144402] CPU3: Booted secondary processor 0x0000000003 [0x410fd041]
[    0.144502] smp: Brought up 1 node, 4 CPUs
[    0.144584] SMP: Total of 4 processors activated.
[    0.144600] CPU features: detected: 32-bit EL0 Support
[    0.144652] CPU: All CPU(s) started at EL2
[    0.144679] alternatives: patching kernel code
[    0.145565] devtmpfs: initialized
[    0.152939] Registered cp15_barrier emulation handler
[    0.152973] Registered setend emulation handler
[    0.153350] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.153386] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.154917] pinctrl core: initialized pinctrl subsystem
[    0.155508] DMI not present or invalid.
[    0.155744] NET: Registered protocol family 16
[    0.156093] audit: initializing netlink subsys (disabled)
[    0.156276] audit: type=2000 audit(0.152:1): state=initialized audit_enabled=0 res=1
[    0.157016] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.161562] DMA: preallocated 256 KiB pool for atomic allocations
[    0.186427] cryptd: max_cpu_qlen set to 1000
[    0.189571] PVR_K:(Error):     1: mtk_mfg_async_init: Enable power domain failed
[    0.189772] PVR_K:(Error):     1: mtk_mfg_2d_init: Enable power domain failed
[    0.190020] SCSI subsystem initialized
[    0.190155] usbcore: registered new interface driver usbfs
[    0.190206] usbcore: registered new interface driver hub
[    0.190332] usbcore: registered new device driver usb
[    0.190994] i2c-gpio 1100b000.i2c: using lines 447 (SDA) and 448 (SCL)
[    0.191153] videodev: Linux video capture interface: v2.00
[    0.192427] Advanced Linux Sound Architecture Driver Initialized.
[    0.192987] Bluetooth: Core ver 2.22
[    0.193050] NET: Registered protocol family 31
[    0.193065] Bluetooth: HCI device and connection manager initialized
[    0.193087] Bluetooth: HCI socket layer initialized
[    0.193104] Bluetooth: L2CAP socket layer initialized
[    0.193149] Bluetooth: SCO socket layer initialized
[    0.193641] clocksource: Switched to clocksource arch_sys_counter
[    0.251208] VFS: Disk quotas dquot_6.6.0
[    0.251290] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.259603] NET: Registered protocol family 2
[    0.260166] tcp_listen_portaddr_hash hash table entries: 1024 (order: 2, 16384 bytes)
[    0.260214] TCP established hash table entries: 16384 (order: 5, 131072 bytes)
[    0.260353] TCP bind hash table entries: 16384 (order: 6, 262144 bytes)
[    0.260561] TCP: Hash tables configured (established 16384 bind 16384)
[    0.260697] UDP hash table entries: 1024 (order: 3, 32768 bytes)
[    0.260754] UDP-Lite hash table entries: 1024 (order: 3, 32768 bytes)
[    0.260960] NET: Registered protocol family 1
[    0.262386] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    0.265674] Initialise system trusted keyrings
[    0.265885] workingset: timestamp_bits=62 max_order=19 bucket_order=0
[    0.270517] fuse init (API version 7.27)
[    0.275103] Key type asymmetric registered
[    0.275131] Asymmetric key parser 'x509' registered
[    0.275162] io scheduler noop registered
[    0.275176] io scheduler deadline registered
[    0.275323] io scheduler cfq registered (default)
[    0.275341] io scheduler mq-deadline registered
[    0.275355] io scheduler kyber registered
[    0.284060] Serial: 8250/16550 driver, 3 ports, IRQ sharing disabled
[    0.285485] mt-pmic-pwrap 1000f000.pwrap: unexpected interrupt int=0x1
[    0.305870] 11005000.serial: ttyS0 at MMIO 0x11005000 (irq = 183, base_baud = 1625000) is a ST16650V2
[    0.931364] console [ttyS0] enabled
[    0.956148] 11006000.serial: ttyS1 at MMIO 0x11006000 (irq = 184, base_baud = 1625000) is a ST16650V2
[    0.966263] mtk_rng 1020c000.rng: registered RNG driver
[    0.966637] random: fast init done
[    0.972881] iommu: Adding device 14007000.disp_ovl0 to group 0
[    0.975284] random: crng init done
[    0.981386] iommu: Adding device 1400a000.rdma1 to group 0
[    0.989846] iommu: Adding device 14009000.disp_rdma0 to group 0
[    0.997472] mediatek-drm 14000000.mmsys2: Adding component match for /soc/dpi1@14019000
[    1.005609] mediatek-drm 14000000.mmsys2: Adding component match for /soc/rdma1@1400a000
[    1.013725] mediatek-drm 14000000.mmsys2: Adding component match for /soc/disp_ovl0@14007000
[    1.022138] mediatek-drm 14000000.mmsys2: Adding component match for /soc/disp_rdma0@14009000
[    1.030635] mediatek-drm 14000000.mmsys2: Adding component match for /soc/disp_color@1400c000
[    1.040461] mediatek-hdmi-phy 10018300.hdmi-phy: Using default TX DRV impedance: 4.2k/36
[    1.050231] [drm] hdmi-audio-codec driver bound to HDMI
[    1.055780] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    1.069039] brd: module loaded
[    1.080360] loop: module loaded
[    1.083949] zram: Added device: zram0
[    1.087875] [xo] dts default cap code: 0x0
[    1.092060] [xo] default cap_code: 0x30
[    1.095883] [xo] get xo efuse: a4000000
[    1.120133] [xo] set cap_code: 0x24
[    1.123619] [xo] current cap_code: 0x24
[    1.127459] [Preloader] BSI read: [0x25] = 0x6aab
[    1.132154] [Preloader] BSI read: [0x29] = 0x1
[    1.136690] [Preloader] BSI read: [0x29] = 0x0
[    1.141116] [xo] status: 0xf
[    1.144011] [xo] current cap code: 0x24
[    1.148876] mt6392-regulator mt6392-regulator: Chip ID = 0x2092
[    1.161351] ldo_vgp2: Bringing 2800000uV into 3300000-3300000uV
[    1.173532] tun: Universal TUN/TAP device driver, 1.6
[    1.179067] PPP generic driver version 2.4.2
[    1.183484] PPP BSD Compression module registered
[    1.188173] PPP Deflate Compression module registered
[    1.193215] PPP MPPE Compression module registered
[    1.197993] NET: Registered protocol family 24
[    1.202750] usbcore: registered new interface driver usb-storage
[    1.208766] usbcore: registered new interface driver ums-alauda
[    1.214681] usbcore: registered new interface driver ums-cypress
[    1.220680] usbcore: registered new interface driver ums-datafab
[    1.226678] usbcore: registered new interface driver ums-freecom
[    1.232676] usbcore: registered new interface driver ums-isd200
[    1.238588] usbcore: registered new interface driver ums-jumpshot
[    1.244676] usbcore: registered new interface driver ums-karma
[    1.250504] usbcore: registered new interface driver ums-onetouch
[    1.256588] usbcore: registered new interface driver ums-sddr09
[    1.262500] usbcore: registered new interface driver ums-sddr55
[    1.268413] usbcore: registered new interface driver ums-usbat
[    1.274291] usbcore: registered new interface driver option
[    1.279860] usbserial: USB Serial support registered for GSM modem (1-port)
[    1.287209] usb_phy_generic usb_phy_generic.1.auto: usb_phy_generic.1.auto supply vcc not found, using dummy regulator
[    1.297939] usb_phy_generic usb_phy_generic.1.auto: Linked as a consumer to regulator.0
[    1.306027] musb-mtk 11100000.usb: Linked as a consumer to regulator.1
[    1.313137] musb-hdrc musb-hdrc.2.auto: MUSB HDRC host driver
[    1.318891] musb-hdrc musb-hdrc.2.auto: new USB bus registered, assigned bus number 1
[    1.327343] hub 1-0:1.0: USB hub found
[    1.331116] hub 1-0:1.0: 1 port detected
[    1.336895] input: mtk-pmic-keys as /devices/platform/soc/1000f000.pwrap/1000f000.pwrap:pmic/mtk-pmic-keys/input/input0
[    1.348744] mt6397-rtc mt6397-rtc: registered as rtc0
[    1.353847] i2c /dev entries driver
[    1.359595] iommu: Adding device 16000000.vcu to group 0
[    1.365221] iommu: Adding device soc:vcu@1 to group 0
[    1.370862] iommu: Adding device 16000000.codec to group 0
[    1.377856] iommu: Adding device 14001000.rdma to group 0
[    1.384077] iommu: Adding device d5af20.wdma to group 0
[    1.389445] iommu: Adding device d5b308.wrot to group 0
[    1.395214] mtk-mdp 14001000.rdma: driver registered as /dev/video2
[    1.395934] iommu: Adding device 10011800.mipicsi to group 0
[    1.407893] mtk-mipicsi 10011800.mipicsi: Waiting for larb device larb@15001000
[    1.415698] ov5645_mipi 2-003c: Linked as a consumer to regulator.27
[    1.422515] ov5645_mipi 2-003c: Linked as a consumer to regulator.26
[    1.429314] ov5645_mipi 2-003c: Linked as a consumer to regulator.11
[    1.505876] ov5645_read_reg:write reg error:reg=300a
[    1.510819] camera ov5645_mipi is not found
[    1.515108] ov5645_mipi 2-003c: Dropping the link to regulator.11
[    1.521257] ov5645_mipi 2-003c: Dropping the link to regulator.26
[    1.527403] ov5645_mipi 2-003c: Dropping the link to regulator.27
[    1.534121] mtk-thermal 1100d000.thermal: Calibration data: buf[0]:0x29c0e25d, buf[1]:0x82e336d9, buf[2]:0x702ae600
[    1.544557] mtk-thermal 1100d000.thermal: Calibration data: adc_ge:523, vts1:224, vts2:226, vts3:224, degc_cali:46, o_slope:10
[    1.556586] mtk-wdt 10007000.toprgu: Watchdog enabled (timeout=31 sec, nowayout=0)
[    1.564543] device-mapper: uevent: version 1.0.3
[    1.569426] device-mapper: ioctl: 4.39.0-ioctl (2018-04-03) initialised: dm-devel@redhat.com
[    1.578025] Bluetooth: Generic Bluetooth SDIO driver ver 0.1
[    1.584199] cpu cpu0: Linked as a consumer to regulator.6
[    1.589639] cpu cpu0: dummy supplies not allowed for exclusive requests
[    1.598760] mtk-msdc 11120000.mmc: Linked as a consumer to regulator.19
[    1.605461] mtk-msdc 11120000.mmc: Linked as a consumer to regulator.25
[    1.640266] mtk-msdc 11130000.mmc: Linked as a consumer to regulator.19
[    1.647409] mtk-msdc 11130000.mmc: Linked as a consumer to regulator.25
[    1.679058] mtk-msdc 11170000.mmc: Linked as a consumer to regulator.18
[    1.685959] mtk-msdc 11170000.mmc: Linked as a consumer to regulator.17
[    1.719575] hidraw: raw HID events driver (C) Jiri Kosina
[    1.726924] usbcore: registered new interface driver usbhid
[    1.732534] usbhid: USB HID core driver
[    1.737836] mtk-msdc 11120000.mmc: phase: [map:ffff003f] [maxlen:16] [final:24]
[    1.738502] mtk-msdc 11130000.mmc: phase: [map:f0ffffff] [maxlen:24] [final:8]
[    1.745467] mmc0: new HS200 MMC card at address 0001
[    1.745702] mtk-iommu 10203000.m4u: bound 14016000.larb (ops 0xffffff8008af6a38)
[    1.745712] mtk-iommu 10203000.m4u: bound 15001000.larb (ops 0xffffff8008af6a38)
[    1.745721] mtk-iommu 10203000.m4u: bound 16010000.larb (ops 0xffffff8008af6a38)
[    1.746031] optee: probing for conduit method from DT.
[    1.746052] optee: revision 3.8
[    1.746459] optee: initialized driver
[    1.746873] usbcore: registered new interface driver snd-usb-audio
[    1.749853] mtk-afe-pcm 11140000.audio-controller: MTK AFE driver initialized.
[    1.750455] mt8167-excelsior sound: mt8167_excelsior_gpio_probe Set pinctrl state default 0
[    1.750886] mtk-afe-pcm 11140000.audio-controller: ASoC: Failed to create component debugfs directory
[    1.751118] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mt8167-codec node
[    1.751127] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mediatek,afe-regmap
[    1.751152] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found platform device of mediatek,afe-regmap
[    1.751161] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found regmap of mediatek,afe-regmap
[    1.751244] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mt8167-codec node
[    1.751252] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mediatek,pwrap-regmap
[    1.751264] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found platform device of mediatek,pwrap-regmap
[    1.751271] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found regmap of mediatek,pwrap-regmap
[    1.754642] mmc1: new ultra high speed SDR104 SDIO card at address 0001
[    1.759523] mmcblk0: mmc0:0001 MB2908 7.28 GiB 
[    1.909931] mmcblk0boot0: mmc0:0001 MB2908 partition 1 4.00 MiB
[    1.917588] mmcblk0boot1: mmc0:0001 MB2908 partition 2 4.00 MiB
[    1.923738] mmcblk0rpmb: mmc0:0001 MB2908 partition 3 4.00 MiB, chardev (247:0)
[    1.923835] mt8167-excelsior sound: snd-soc-dummy-dai <-> DL1 mapping ok
[    1.938248] mt8167-excelsior sound: snd-soc-dummy-dai <-> VUL mapping ok
[    1.943117] Alternate GPT is invalid, using primary GPT.
[    1.945191] mt8167-excelsior sound: snd-soc-dummy-dai <-> AWB mapping ok
[    1.950250]  mmcblk0: p1 p2 p3 p4
[    1.961086] mt8167-excelsior sound: snd-soc-dummy-dai <-> DL2 mapping ok
[    1.967879] mt8167-excelsior sound: mt8167-codec <-> INT ADDA mapping ok
[    1.974679] mt8167-excelsior sound: ASoC: no DMI vendor name!
[    1.983171] input: excelsior-card Headset Jack as /devices/platform/sound/sound/card0/input1
[    1.992219] drop_monitor: Initializing network drop monitor service
[    1.998537] Mirror/redirect action on
[    2.002227] u32 classifier
[    2.004914]     Performance counters on
[    2.008731]     input device check on
[    2.012392]     Actions configured
[    2.016431] xt_time: kernel timezone is -0000
[    2.020917] ipip: IPv4 and MPLS over IPv4 tunneling driver
[    2.027026] Initializing XFRM netlink socket
[    2.031760] NET: Registered protocol family 10
[    2.037254] Segment Routing with IPv6
[    2.041054] mip6: Mobile IPv6
[    2.044220] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.051152] NET: Registered protocol family 17
[    2.055639] NET: Registered protocol family 15
[    2.060166] Bridge firewalling registered
[    2.064309] Bluetooth: RFCOMM TTY layer initialized
[    2.069317] Bluetooth: RFCOMM socket layer initialized
[    2.074474] Bluetooth: RFCOMM ver 1.11
[    2.078322] 8021q: 802.1Q VLAN Support v1.8
[    2.083187] Loading compiled-in X.509 certificates
[    2.111841] mediatek-dpi 14019000.dpi1: Found bridge node: /soc/hdmi@1401b000
[    2.119205] mediatek-drm 14000000.mmsys2: bound 14019000.dpi1 (ops 0xffffff8008aaeff0)
[    2.127104] mediatek-drm 14000000.mmsys2: bound 1400a000.rdma1 (ops 0xffffff8008aaa728)
[    2.135077] mediatek-drm 14000000.mmsys2: bound 14007000.disp_ovl0 (ops 0xffffff8008aaa1b8)
[    2.143390] mediatek-drm 14000000.mmsys2: bound 14009000.disp_rdma0 (ops 0xffffff8008aaa728)
[    2.151789] mediatek-drm 14000000.mmsys2: bound 1400c000.disp_color (ops 0xffffff8008aa9e10)
[    2.160183] mediatek-drm 14000000.mmsys2: Not creating crtc 0 because component 9 is disabled or missing
[    2.169676] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    2.176254] [drm] No driver support for vblank timestamp query.
[    2.182664] [drm] Initialized mediatek 1.0.0 20150513 for 14000000.mmsys2 on minor 0
[    2.190415] [drm] Cannot find any crtc or sizes
[    2.195713] mtk-mipicsi 10011800.mipicsi: not set mediatek,mipicsi_max_vc, use default value 1
[    2.204295] mtk-mipicsi 10011800.mipicsi: not set mediatek,serdes_link_reg, can't read subdev link number
[    2.213820] mtk-mipicsi 10011800.mipicsi: there are 1 camsv node
[    2.220522] mtk-mipicsi 10011800.mipicsi: seninf_mux_camsv@15004000 parse done
[    2.228025] mtk-mipicsi 10011800.mipicsi: mipicsi@15008000 parse done
[    2.234459] mtk-mipicsi 10011800.mipicsi: mipicsi node parse done
[    2.240580] mtk-mipicsi 10011800.mipicsi: probe done
[    2.245649] [drm] Cannot find any crtc or sizes
[    2.247612] PVR_K:  1: irq_res = 0xca
[    2.253956] PVR_K:  1: reg_res = 0x13000000, 0x80000
[    2.259281] PVR_K:  1: Read BVNC 22.40.54.30 from HW device registers
[    2.265940] PVR_K:  1: RGX Device registered with BVNC 22.40.54.30
[    2.272918] [drm] Initialized pvr 1.11.5516664 20170530 for 13000000.clark on minor 1
[    2.281280] mt6397-rtc mt6397-rtc: hctosys: unable to read the hardware clock
[    2.288599] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    2.298065] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    2.304719] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    2.306029] [MUSBFSH] musbfsh_init 1859: MUSBFSH is enabled
[    2.313312] cfg80211: failed to load regulatory.db
[    2.319936] musbfsh-hdrc musbfsh-hdrc.0: Linked as a consumer to regulator.4
[    2.330634] [MUSBFSH] musbfsh_init_controller 1372: vbus registered
[    2.338605] [MUSBFSH] musbfsh_core_init 894: musbfsh-hdrc: ConfigData=0x1f (UTMI-16, dyn FIFOs, HB-ISO Rx, HB-ISO Tx, SoftConn)
[    2.353176] musbfsh-hdrc musbfsh-hdrc.0: MUSBFSH HDRC host driver
[    2.359299] musbfsh-hdrc musbfsh-hdrc.0: new USB bus registered, assigned bus number 2
[    2.367919] hub 2-0:1.0: USB hub found
[    2.371699] hub 2-0:1.0: 1 port detected
[    2.375769] [MUSBFSH] musbfsh_start 581: <== devctl 0x98
[    2.381057] [MUSBFSH] mt_usb11_set_vbus 455: Enable VBUS
[    2.437815] musbfsh-hdrc musbfsh-hdrc.0: USB controller at 00000000c9fb0e12 using DMA, IRQ 193
[    2.446528] [MUSBFSH] musbfsh_init_enable_pin 1310: ERROR: Cannot find musbfsh_pinctrl!
[    2.454573] ALSA device list:
[    2.457518]   #0: excelsior-card
[    2.466824] EXT4-fs (mmcblk0p4): INFO: recovery required on readonly filesystem
[    2.474266] EXT4-fs (mmcblk0p4): write access will be enabled during recovery
[    2.537724] [MUSBFSH] musbfsh_hub_control 565: port status 00000100,devctl=0x19
[    2.545275] [MUSBFSH] musbfsh_bus_suspend 2806: musbfsh_bus_suspend++,power=0x61
[    2.623983] [MUSBFSH] musbfsh_stage0_irq 532: CONNECT ! devctl 0x5d
[    2.630231] [MUSBFSH] musbfsh_bus_resume 2852: musbfsh_bus_resume++,power=0x61
[    2.637516] [MUSBFSH] musbfsh_hub_control 565: port status 00010101,devctl=0x5d
[    2.670418] EXT4-fs (mmcblk0p4): orphan cleanup on readonly fs
[    2.676697] EXT4-fs (mmcblk0p4): 1 orphan inode deleted
[    2.682107] EXT4-fs (mmcblk0p4): recovery complete
[    2.696729] EXT4-fs (mmcblk0p4): mounted filesystem with ordered data mode. Opts: (null)
[    2.704902] VFS: Mounted root (ext4 filesystem) readonly on device 179:4.
[    2.712232] devtmpfs: mounted
[    2.715683] Freeing unused kernel memory: 832K
[    2.720213] Run /sbin/init as init process
[    2.749750] [MUSBFSH] musbfsh_hub_control 565: port status 00000101,devctl=0x5d
[    2.757233] [MUSBFSH] musbfsh_port_reset 261: reset=1 power=0x61
[    2.829728] [MUSBFSH] musbfsh_port_reset 261: reset=0 power=0x78
[    2.835738] [MUSBFSH] musbfsh_hub_control 565: port status 00120503,devctl=0x5d
[    2.901729] usb 2-1: new high-speed USB device number 2 using musbfsh-hdrc
[    2.908810] [MUSBFSH] musbfsh_port_reset 261: reset=1 power=0x70
SELinux:  Could not open policy file <= /etc/selinux/targeted/po[    2.949611] systemd[1]: System time before build time, advancing clock.
licy/policy.31:  No such file or directory
[    2.981692] [MUSBFSH] musbfsh_port_reset 261: reset=0 power=0x78
[    2.987687] [MUSBFSH] musbfsh_hub_control 565: port status 00120503,devctl=0x5d
[    2.999466] systemd[1]: Failed to find module 'autofs4'
[    3.020003] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    3.041855] systemd[1]: Detected architecture arm64.

Welcome to Mendel GNU/Linux 5 (Eagle)![    3.053769] [MUSBFSH] musbfsh_h_disable 2655: musbfsh_h_disable++: ep: 0x0


[    3.061239] MTK_ICUSB [DBG], <musbfsh_h_disable(), 2660> qh == NULL
[    3.068117] [MUSBFSH] musbfsh_h_disable 2655: musbfsh_h_disable++: ep: 0x0
[    3.075407] MTK_ICUSB [DBG], <musbfsh_h_disable(), 2660> qh == NULL
[    3.081817] systemd[1]: Set hostname to <neat-calf>.
[    3.103246] [MUSBFSH] musbfsh_hub_control 565: port status 00020503,devctl=0x5d
[    3.280063] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
[    3.297292] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
[    3.411140] systemd[1]: /lib/systemd/system/vitalsd.service:3: Failed to add dependency on usb-gadget, ignoring: Unknown error -22
[    3.423029] systemd[1]: /lib/systemd/system/vitalsd.service:5: Unknown lvalue 'Exec' in section 'Service', ignoring
[    3.433760] systemd[1]: vitalsd.service: Service has no ExecStart=, ExecStop=, or SuccessAction=. Refusing.
[    3.535292] systemd[1]: /lib/systemd/system/usb-gadget-getty-ttyGS0.service:21: Unknown lvalue 'TTYDisallocate' in section 'Service', ignoring
[    3.590006] systemd[1]: vitalsd.service: Cannot add dependency job, ignoring: Unit vitalsd.service has a bad unit file setting.
[  OK  ] Created slice system-systemd\x2dmkfs.slice.
[  OK  ] Listening on Journal Socket.
[  OK  ] Started Forward Password R…uests to Wall Directory Watch.
[  OK  ] Listening on fsck to fsckd communication Socket.
[  OK  ] Reached target Remote File Systems.
[  OK  ] Created slice User and Session Slice.
         Mounting POSIX Message Queue File System...
[  OK  ] Created slice system-getty.slice.
[  OK  ] Listening on udev Kernel Socket.
[  OK  ] Listening on Syslog Socket.
[  OK  ] Listening on Journal Socket (/dev/log).
[  OK  ] Reached target Slices.
         Mounting Kernel Debug File System...
[  OK  ] Listening on initctl Compatibility Named Pipe.
[  OK  ] Created slice system-systemd\x2dfsck.slice.
[  OK  ] Started Dispatch Password …ts to Console Directory Watch.
[  OK  ] Reached target Swap.
         Starting File System Check on Root Device...
         Starting Load Kernel Modules...
[  OK  ] Listening on udev Control Socket.
         Starting udev Coldplug all Devices...
[  OK  ] Reached target Local Encrypted Volumes.
[  OK  ] Listening on Journal Audit Socket.
         Starting Journal Service...
[  OK  ] Created slice system-serial\x2dgetty.slice.
[  OK  ] Mounted POSIX Message Queue File System.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Started File System Check on Root Device.
[  OK  ] Started Load Kernel Modules.
[  OK  ] Started File System Check Daemon to report status.
         Mounting FUSE Control File System...
         Mounting Kernel Configuration File System...
         Starting Apply Kernel Variables...
         Starting Remount Root and Kernel File Systems...
[  OK  ] Started Journal Service.
[  OK  ] Mounted FUSE Control File System.
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Started Apply Kernel Variables.
[    4.299957] EXT4-fs (mmcblk0p4): re-mounted. Opts: (null)
[  OK  ] Started Remount Root and Kernel File Systems.
         Starting Load/Save Random Seed...
         Starting Create System Users...
[  OK  ] Started Load/Save Random Seed.
[  OK  ] Started Create System Users.
[  OK  ] Started udev Coldplug all Devices.
         Starting Helper to synchronize boot up for ifupdown...
         Starting Create Static Device Nodes in /dev...
[  OK  ] Started Helper to synchronize boot up for ifupdown.
[  OK  ] Started Create Static Device Nodes in /dev.
         Starting udev Kernel Device Manager...
[  OK  ] Reached target Local File Systems (Pre).
         Mounting /var/log...
[  OK  ] Mounted /var/log.
         Starting Flush Journal to Persistent Storage...
[  OK  ] Started udev Kernel Device Manager.
[  OK  ] Started VPU Daemon.
[  OK  ] Started MDP Daemon.
[    4.674434] systemd-journald[155]: Received request to flush runtime journal from PID 1
remap_shmem,line:311 vpud: shmem_length=1089536, shmem=0x7fb80a0000

[Info]vpud_init,line:343 share_obj:56,1024,24, set:40387600,mva:c0187601,free:c0187602,flush:c0187603,get:c0387604,log:7f44007605,cache:c0187606
vdec_codec_service_init() block mode
venc_codec_service_init()
The firmware version is 0.2.14
mdpd without fuse
mdpd: shmem_length=1212416, shmem=0x7fa0270000
[  OK  ] Started Flush Journal to Persistent Storage.
The firmware version is 0.2.13
--[mdp] create_rt_thread,line:217
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Found device /dev/disk/by-…9-3004-4e30-87dc-ed33fbf4dbfd.
[    5.388611] wlan_mt7668_sdio: loading out-of-tree module taints kernel.
[  OK  ] Found device /dev/disk/by-…b-1d90-492f-ab86-6952303b214e.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Starting File System Check…1d90-492f-ab86-6952303b214e...
         Starting Make File System …3004-4e30-87dc-ed33fbf4dbfd...
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Started Make File System o…9-3004-4e30-87dc-ed33fbf4dbfd.
         Starting File System Check…3004-4e30-87dc-ed33fbf4dbfd...
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Started File System Check …9-3004-4e30-87dc-ed33fbf4dbfd.
         Mounting /home...disk (26.2% complete)
[    6.064152] EXT4-fs (mmcblk0p3): mounted filesystem with ordered data mode. Opts: (null)
[  OK  ] Mounted /home. 1 disk (39.4% complete)
Checking in progress [    6.175161] EXT4-fs (mmcblk0p2): mounting ext2 file system using the ext4 subsystem
Chec[    6.186411] EXT4-fs (mmcblk0p2): mounted filesystem without journal. Opts: (null)
[  OK  ] Started File System Check …b-1d90-492f-ab86-6952303b214e.
         M[    6.311422] net lo: No handler found (wireless_process_ioctl)
ounting /boot...
[  OK  ] Mounted /boot.
[  OK  ] Reached target Local File Systems.
         Starting Create Volatile Files and Directories...
         Starting Raise network interfaces...
[  OK  ] Started Create Volatile Files and Directories.
         Starting Network Time Synchronization...
[  OK  ] Started Entropy daemon using the HAVEGE algorithm.
         Starting Update UTMP about Sys[    6.365664] [XO] xocap_timer_func
tem Boot/Shutdow[    6.370016] [XO] xocap_work_func
n...
[    6.374596] [MT6620][nvram_read] : failed to open!!
2m  OK  ] Started Update UTMP about System Boot/Shu[    6.385168]  ret is -1!
tdown.
[  OK  ] Started Raise network interfaces.
[    6.409350] current cap code(after nvram):0x24
[  OK  ] Started Network Time Synchronization.
[  OK  ] Reached target System Initialization.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Started Restart mdt-keymas… when authorized_keys changes.
[  OK  ] Reached target Paths.
         Starting Scripts that should be run only once...
[  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
[  OK  ] Reached target Sockets.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Started Daily apt download activities.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Started Daily man-db regeneration.
[  OK  ] Started Daily rotation of log files.
[  OK  ] Reached target Timers.
[  OK  ] Started Scripts that should be run only once.
[  OK  ] Reached target Basic System.
[  OK  ] Started Regular background program processing daemon.
[  OK  ] Started D-Bus System Message Bus.
         Starting Login Service...
         Starting WPA supplicant...
         Starting Avahi mDNS/DNS-SD Stack...
[  OK  ] Started Manage Sound Card State (restore and store).
         Starting Save/Restore Sound Card State...
         Starting Network Manager...
         Starting USB Gadget...
         Starting Initialize hardware monitoring sensors...
[  OK  ] Started Excelsior bootloader install service.
         Starting System Logging Service...
[  OK  ] Started System Logging Service.
[  OK  ] Started Save/Restore Sound Card State.
[  OK  ] Started Avahi mDNS/DNS-SD Stack.
[  OK  ] Reached target Sound Card.
[  OK  ] Started WPA supplicant.
[  OK  ] Started Initialize hardware monitoring sensors.
[  OK  ] Started Login Service.
[  OK  ] Started Network Manager.
         Starting Hostname Service...
[  OK  ] Started Hostname Service.
         Starting Network Manager Script Dispatcher Service...
[  OK  ] Started Network Manager Script Dispatcher Service.
         Starting Authorization Manager...
[  OK  ] Started Authorization Manager.
[    7.800337] using random self ethernet address
[    7.804819] using random host ethernet address
[    7.820260] using random self ethernet address
[    7.824818] using random host ethernet address
[    8.196643] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
[    8.270352] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
[  OK  ] Started Excelsior B[    8.282225] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
luetooth Module.
[    8.404417] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
[    8.487332] BTMTK_init
[    8.489748] proc initialized
[    8.489790] major number:244
[    8.495555] BT_majorfwlog number: 243
[    8.499249] BT_chrdev driver(major 244) installed.
[    8.504039] BT_chrdevfwlog driver(major 243) installed.
[    8.509792] BTMTK_init: BT_major 244, BT_majorfwlog 243
[    8.515032] BTMTK_init: devID 255852544, devIDfwlog 254803968
[    8.520940] btmtk_sdio_probe Mediatek Bluetooth driver Version=v0.0.0.53_2018072701_YOCTO
[    8.529149] vendor=0x37a, device=0x7668, class=255, fn=2, support func_num 2
[    8.536198] btmtk_sdio_probe chip_id is 7668
[    8.540566] before claim irq read SDIO_CCCR_IENx 0, func num 2
[    8.546467] sdio_claim_irq success: ret=0
[    8.550520] after claim irq read SDIO_CCCR_IENx 0
[    8.555350] SDIO FUNC2 IO port: 0xf07668
[    8.559383] btmtk_sdio_enable_host_int read CSDIOCSR is 0x1
[    8.565035] btmtk_sdio_enable_host_int write CSDIOCSR is 0x5
[    8.570698] btmtk_sdio_download_fw begin
[    8.574817] btmtk_sdio_send_wohci retrun  0x0
[    8.579296] btmtk_sdio_bt_memRegister_read: read cr 80000000
[    8.600268] btmtk_sdio_bt_memRegister_read: retrytime 299
[    8.605684] btmtk_sdio_bt_memRegister_read: ger cr 0x80000000 value 0x8b11
[    8.612694] btmtk_sdio_download_rom_patch uhwversion 0x8b11
[    8.618273] btmtk_sdio_download_rom_patch request_firmware(firmware name mt7668_patch_e2_hdr.bin)
[    8.627510] btmtk_sdio_download_rom_patch patch is ready no need load patch again
[    8.635061] btmtk_sdio_download_rom_patch read chipid =  f07668
[    8.641119] btmtk_sdio_bt_set_power: onoff 1
[    8.749938] btmtk_eeprom_bin_file: 7668 series
[    8.880877] usb0: HOST MAC d6:57:7d:e9:cd:b4
[    8.882004] net usb0: No handler found (wireless_process_ioctl)
[    8.891498] usb0: MAC 02:22:78:0d:f6:df
[    8.893949] btmtk_set_eeprom2ctrler: set BDAddress(F4-F5-E8-EC-AF-E8) OK
[    8.896508] usb1: HOST MAC 02:22:78:0d:f6:dd
[    8.904971] net usb1: No handler found (wireless_process_ioctl)
[    8.912449] usb1: MAC 02:22:78:0d:f6:de
[    9.017822] btmtk_set_eeprom2ctrler: set radio(BT/BLE default power: 5/5 MAX power: 5) OK
[    9.146120] btmtk_sdio_recv_rx_data: retry_count = 0,timeout
[    9.177926] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.184257] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.199838] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.221998] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.257855] btmtk_set_eeprom2ctrler: set power offset(FE FD FD FD FC FB) OK
[    9.369838] btmtk_set_eeprom2ctrler: set XTAL(0xAB 00) OK
[    9.375345] btmtk_sdio_set_sleep begin
[    9.382487] btmtk_sdio_set_write_clear write CHCR 0x00000002
[    9.388539] btmtk_sdio_set_write_clear read CHCR 0x00000002
[    9.394176] btmtk_sdio_set_write_clear write clear
[    9.399299] btmtk_sdio_set_i2s_slave
[    9.403700] configfs-gadget gadget: high-speed config #1: c
[    9.409305] gs_console_connect: port num [0] is not support console
[    9.415987] btmtk_sdio_read_pin_mux_setting
[    9.417875] IPv6: ADDRCONF(NETDEV_CHANGE): usb0: link becomes ready
[    9.427305] btmtk_sdio_write_pin_mux_setting begin
[    9.435606] btmtk_sdio_read_pin_mux_setting
[    9.443163] confirm pinmux 22220000
[    9.446776] btmtk_add_card begin
[    9.450096] Starting kthread...
[    9.453378] main_thread begin 50
[    9.456734] btmtk_service_main_thread probe_ready 0 delay 10ms~15ms
[    9.458407] btmtk_sdio_probe normal end
[    9.467713] SDIO Driver Registration Success
[    9.478272] Bluetooth: hci0: unexpected event for opcode 0xfcd1
         Starting Bluetooth service...
[  OK  ] Started Bluetooth service.
[  OK  ] Reached target Bluetooth.
[    9.775302] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[    9.781981] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[    9.797412] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[    9.819104] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[  OK  ] Started USB Gadget.
[  OK  ] Reached target Network.
[  OK  ] Started MDT public key management service.
         Starting Permit User Sessions...
         Starting dnsmasq - A light…DHCP and caching DNS server...
[  OK  ] Started Unattended Upgrades Shutdown.
         Starting OpenBSD Secure Shell server...
[  OK  ] Started Permit User Sessions.
[  OK  ] Started Getty on ttyGS0.
         Starting Weston Wayland Compositor (on tty7)...
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Started Getty on tty1.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started Update LED behavior after boot.
[  OK  ] Started Weston Wayland Compositor (on tty7).
[  OK  ] Started OpenBSD Secure Shell server.
[  OK  ] Started dnsmasq - A lightw…t DHCP and caching DNS server.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.
         Starting Update UTMP about System Runlevel Changes...
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Created slice User Slice of UID 1000.
         Starting User Runtime Directory /run/user/1000...
[  OK  ] Started Update UTMP about System Runlevel Changes.
[  OK  ] Started User Runtime Directory /run/user/1000.
         Starting User Manager for UID 1000...
[  OK  ] Started User Manager for UID 1000.
[  OK  ] Started    11.093706] PVR_K:  707: RGX Firmware image 'rgx.fw.22.40.54.30' loaded

Mendel GNU/Linux (eagle) neat-calf ttyS0

neat-calf login: [   33.757738] usb0_vbus: disabling
[   33.760964] usb0_vbus_old: disabling
[   33.764590] backlight_vbus: disabling
[   33.768310] ldo_vm25: disabling
                                                   
hemanthreddyj@hemanthreddyj-glaptop:~$ [  OK  ] Started Getty on tty1.
bash: [: missing `]'
hemanthreddyj@hemanthreddyj-glaptop:~$ screen /dev/ttyUSB0 115200































                                                      
hemanthreddyj@hemanthreddyj-glaptop:~$ [  OK  ] Started Getty on tty1.
bash: [: missing `]'
hemanthreddyj@hemanthreddyj-glaptop:~$ screen /dev/ttyUSB0 115200
hemanthreddyj@hemanthreddyj-glaptop:~$ screen /dev/ttyUSB0 115200

F0: 102B 0000
F3: 0000 0000
V0: 0000 0000 [0001]
00: 0000 0000
BP: 0400 0041 [0000]
G0: 1190 0000
EC: 0000 1000 [0001]
T0: 0000 0212 [000F]
Jump to BL

NOTICE:  BL2: v2.3():c1984dc174fa
NOTICE:  BL2: Built : 08:07:51, Oct  2 2020
NOTICE:  CHIPSET: MT8167
[PWRAP] pmic ID: 2092.
[EMI] MDL number = 0 
[EMI] LPDDR3
Vcore HV NV LV, Vdram HV NV LV
0x5f 0x48 0x3f, 0xb 0x0 0x3
[EMI] Use default emigen emi settings 
[EMI] Config emi settings:
EMI_CONA=0x2a052,   EMI_CONH=0x3
EMI_RAMK0=0x40000000, EMI_RAMK1=0x40000000
EMI_CONA=0x2a052
EMI_CONF=0x4210000
EMI_CONH=0x3

[DramcSwImpedanceCal] FINAL: DRVP=8, DRVN=7

LPDDR3 Pinmux 2
SSC OFF
DRAM Clock: 1584MHz

[Write Leveling]
WriteLevelingMoveDQSInsteadOfCLK
===============================================================================
Dram Type= 3, Freqency= 1600, rank 1
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
WL Clk delay = 0, CA CLK delay = 0
No need to update CA/CS delay because the CLK delay is small than CA training.
Final Clk output delay = 0
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS0 delay =  27
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS1 delay =  27
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS2 delay =  26
R1 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS3 delay =  26
[DramcWriteLeveling] ====Done====
[DramRankNumberDetection] 2, 0x0
LPDDR3 Pinmux 2
SSC OFF
DRAM Clock: 1584MHz

[CATrainingLP3]
FINAL: CA0  (1~32) 16
FINAL: CA1  (0~30) 15
FINAL: CA2  (1~31) 16
FINAL: CA3  (0~31) 15
FINAL: CA5  (1~31) 16
FINAL: CA6  (1~31) 16
FINAL: CA7  (1~31) 16
FINAL: CA8  (2~32) 17
FINAL: CA4  (1~32) 16
FINAL: CA9  (1~32) 16
=========================================
u4GoldenPattern 0xrank0:
Macro0 Clk Dealy is 0, CA delay is 15
rank1:
Macro0 Clk Dealy is 0, CA delay is 15
[CATrainingLP3] ====Done====


[Write Leveling]
WriteLevelingMoveDQSInsteadOfCLK
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
WL Clk delay = 0, CA CLK delay = 0
No need to update CA/CS delay because the CLK delay is small than CA training.
Final Clk output delay = 0
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS0 delay =  28
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS1 delay =  28
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS2 delay =  26
R0 FINAL: WriteLeveling DQS:(2, 2) OEN:(2, 0) DQS3 delay =  25
[DramcWriteLeveling] ====Done====

[Gating]
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
[Byte 0]First pass (1, 6, 12)
[Byte 1]First pass (1, 6, 12)
[Byte 2]First pass (1, 6, 12)
[Byte 3]First pass (1, 6, 12)
[Byte 0]Bigger pass win(2, 0, 3)  Pass tap=55
[Byte 1]Bigger pass win(2, 0, 3)  Pass tap=55
[Byte 3]Bigger pass win(2, 0, 3)  Pass tap=55
[Byte 2]Bigger pass win(2, 0, 4)  Pass tap=56
===============================================================================
    dqs input gating widnow, final delay value
    Frequency=1600  rank=0
===============================================================================
R0 FINAL: GW best DQS0 P0 delay(2T, 0.5T, PI) = (1, 7, 7) [tap = 55]
R0 FINAL: GW best DQS1 P0 delay(2T, 0.5T, PI) = (1, 7, 7) [tap = 55]
R0 FINAL: GW best DQS2 P0 delay(2T, 0.5T, PI) = (1, 7, 8) [tap = 56]
R0 FINAL: GW best DQS3 P0 delay(2T, 0.5T, PI) = (1, 7, 7) [tap = 55]
R0 FINAL: GW best DQS0 P1 delay(2T, 0.5T, PI) = (2, 1, 7)
R0 FINAL: GW best DQS1 P1 delay(2T, 0.5T, PI) = (2, 1, 7)
R0 FINAL: GW best DQS2 P1 delay(2T, 0.5T, PI) = (2, 1, 8)
R0 FINAL: GW best DQS3 P1 delay(2T, 0.5T, PI) = (2, 1, 7)
[DramcRxdqsGatingCal] ====Done====

[DATLAT]
DATLAT Default value = 0x10
5, 0x6, 0x7, 0x8, 0x9, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0xpattern=5 first_step=15 total pass=6 best_step=17
R0 FINAL: DATLAT = 17 [15 ~ 20]
[DramcRxdatlatCal] ====Done====

[RX]
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
RX Window Sum 764
R0 FINAL: RX Bit 0, 16 (5 ~ 27) 23
R0 FINAL: RX Bit 1, 14 (2 ~ 26) 25
R0 FINAL: RX Bit 2, 13 (1 ~ 26) 26
R0 FINAL: RX Bit 3, 14 (3 ~ 25) 23
R0 FINAL: RX Bit 4, 18 (7 ~ 29) 23
R0 FINAL: RX Bit 5, 16 (3 ~ 30) 28
R0 FINAL: RX Bit 6, 17 (6 ~ 29) 24
R0 FINAL: RX Bit 7, 18 (6 ~ 31) 26
R0 FINAL: RX Bit 8, 17 (6 ~ 29) 24
R0 FINAL: RX Bit 9, 17 (6 ~ 29) 24
R0 FINAL: RX Bit 10, 15 (2 ~ 29) 28
R0 FINAL: RX Bit 11, 17 (6 ~ 29) 24
R0 FINAL: RX Bit 12, 18 (7 ~ 29) 23
R0 FINAL: RX Bit 13, 18 (6 ~ 30) 25
R0 FINAL: RX Bit 14, 18 (8 ~ 29) 22
R0 FINAL: RX Bit 15, 17 (4 ~ 31) 28
R0 FINAL: RX Bit 16, 18 (4 ~ 32) 29
R0 FINAL: RX Bit 17, 19 (6 ~ 32) 27
R0 FINAL: RX Bit 18, 16 (2 ~ 30) 29
R0 FINAL: RX Bit 19, 18 (5 ~ 31) 27
R0 FINAL: RX Bit 20, 14 (2 ~ 26) 25
R0 FINAL: RX Bit 21, 15 (3 ~ 27) 25
R0 FINAL: RX Bit 22, 14 (3 ~ 26) 24
R0 FINAL: RX Bit 23, 14 (2 ~ 27) 26
R0 FINAL: RX Bit 24, 18 (7 ~ 30) 24
R0 FINAL: RX Bit 25, 19 (8 ~ 30) 23
R0 FINAL: RX Bit 26, 19 (6 ~ 32) 27
R0 FINAL: RX Bit 27, 20 (8 ~ 33) 26
R0 FINAL: RX Bit 28, 19 (9 ~ 30) 22
R0 FINAL: RX Bit 29, 18 (7 ~ 30) 24
R0 FINAL: RX Bit 30, 18 (9 ~ 28) 20
R0 FINAL: RX Bit 31, 16 (6 ~ 27) 22
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
DQS Delay :
DQS0 = 0, DQS1 = 0, DQS2 = 0, DQS3 = 0
DQM Delay :
DQM0 = 15, DQM1 = 17, DQM2 = 16, DQM3 = 18
DQ Delay :
DQ0 =16, DQ1 =14, DQ2 =13, DQ3 =14 
DQ4 =18, DQ5 =16, DQ6 =17, DQ7 =18 
DQ8 =17, DQ9 =17, DQ10 =15, DQ11 =17 
DQ12 =18, DQ13 =18, DQ14 =18, DQ15 =17 
DQ16 =18, DQ17 =19, DQ18 =16, DQ19 =18 
DQ20 =14, DQ21 =15, DQ22 =14, DQ23 =14 
DQ24 =18, DQ25 =19, DQ26 =19, DQ27 =20 
DQ28 =19, DQ29 =18, DQ30 =18, DQ31 =16 
________________________________________________________________________
[DramcRxWindowPerbitCal] ====Done====

[TX]
[DramcTxWindowPerbitCal] Frequency=1600, Rank=0, calType=2
[DramcTxWindowPerbitCal] Begin, TX DQ(2, 2),  DQ OEN(2, 0)
TX Window Sum 741
===============================================================================
Dram Type= 3, Freqency= 1600, rank 0
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
R0 FINAL: TX Bit0 (34~56) 23 45,   Bit8 (36~58) 23 47,  Bit16 (32~53) 22 42,   Bit24 (33~55) 23 44
R0 FINAL: TX Bit1 (29~53) 25 41,   Bit9 (35~58) 24 46,  Bit17 (31~53) 23 42,   Bit25 (33~55) 23 44
R0 FINAL: TX Bit2 (32~55) 24 43,   Bit10 (34~58) 25 46,  Bit18 (31~53) 23 42,   Bit26 (33~55) 23 44
R0 FINAL: TX Bit3 (32~53) 22 42,   Bit11 (36~58) 23 47,  Bit19 (32~53) 22 42,   Bit27 (34~55) 22 44
R0 FINAL: TX Bit4 (36~56) 21 46,   Bit12 (36~59) 24 47,  Bit20 (28~50) 23 39,   Bit28 (33~55) 23 44
R0 FINAL: TX Bit5 (35~57) 23 46,   Bit13 (35~59) 25 47,  Bit21 (30~52) 23 41,   Bit29 (33~55) 23 44
R0 FINAL: TX Bit6 (35~57) 23 46,   Bit14 (35~58) 24 46,  Bit22 (28~50) 23 39,   Bit30 (32~54) 23 43
R0 FINAL: TX Bit7 (34~57) 24 45,   Bit15 (37~59) 23 48,  Bit23 (30~52) 23 41,   Bit31 (32~54) 23 43

==================================================================
Byte0, PI DQ Delay 43 Delay2 44
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 44)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 44)

Byte1, PI DQ Delay 47 Delay2 47
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 47)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 47)

Byte2, PI DQ Delay 40 Delay2 41
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 41)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 41)

Byte3, PI DQ Delay 43 Delay2 44
Final DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,2, 44)
OEN DQ PI Delay(LargeUI, SmallUI, PI) =(2 ,0, 44)

[DramcTxWindowPerbitCal] ====Done====

[Gating]
===============================================================================
Dram Type= 3, Freqency= 1600, rank 1
odt_onoff= 0, Byte mode= 0, Read_DBI= 0, Write DBI= 0 
===============================================================================
[Byte 3]First pass (1, 6, 4)
[Byte 0]First pass (1, 6, 5)
[Byte 2]First pass (1, 6, 5)
[Byte 1]First pass (1, 6, 6)
[Byte 0]Bigger pass win(2, 0, 0)  Pass tap=59
[Byte 1]Bigger pass win(2, 0, 0)  Pass tap=58
[Byte 2]Bigger pass win(2, 0, 0)  Pass tap=59
[Byte 3]Bigger pass win(2, 0, 0)  Pass tap=60
===============================================================================
    dqs input gating widnow, final delay value
    Frequency=1600  rank=1
===============================================================================
R1 FINAL: GW best DQS0 P0 delay(2T, 0.5T, PI) = (1, 7, 2) [tap = 59]
R1 FINAL: GW best DQS1 P0 delay(2T, 0.5T, PI) = (1, 7, 3) [tap = 58]
R1 FINAL: GW best DQS2 P0 delay(2T, 0.5T, PI) = (1, 7, 2) [tap = 59]
R1 FINAL: GW best DQS3 P0 delay(2T, 0.5T, PI) = (1, 7, 2) [tap = 60]
R1 FINAL: GW best DQS0 P1 delay(2T, 0.5T, PI) = (2, 1, 2)
R1 FINAL: GW best DQS1 P1 delay(2T, 0.5T, PI) = (2, 1, 3)
R1 FINAL: GW best DQS2 P1 delay(2T, 0.5T, PI) = (2, 1, 2)
R1 FINAL: GW best DQS3 P1 delay(2T, 0.5T, PI) = (2, 1, 2)
[DramcRxdqsGatingCal] ====Done====

[DATLAT]
DATLAT Default value = 0x11
5, 0x6, 0x7, 0x8, 0x9, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0xpattern=5 first_step=15 total pass=6 best_step=17
R1 FINAL: DATLAT = 17 [15 ~ 20]
[DramcRxdatlatCal] ====Done====
[DramcRxdqsGatingPostProcess] p->frequency 1600
[DramcRxdqsGatingPostProcess] s1ChangeDQSINCTL 0, reg_TX_dly_DQSgated_min 3, u1TXDLY_Cal_min 3
[DramcDualRankRxdatlatCal] RANK0: 17, RANK1: 17, Final_Datlat 17
[Get MRR] Vendor 5.
[Get MRR] MR8 1f1f.
[Get MRR] Rank 0, u1DieNumber 1, Desity 0x40000000.
[Get MRR] MR8 1f1f.
[Get MRR] Rank 1, u1DieNumber 1, Desity 0x40000000.
[vDramcUpdateEmiSetting] EMI_CONA 0x2a052, EMI_CONH 0x3
[vDramcACTimingOptimize] Density 7, u1TRFC 73, u1TRFCpb 25, u1TRFC_05T 0, u1TXREFCNT 86

Settings after calibration ...
=== [DramcRunTimeConfig] ===
HW_GATING: ON
DUMMY_READ_FOR_TRACKING: ON
DFS_HW_SYNC_GATING_TRACKING: OFF
ZQCS_ENABLE: ON
LOWPOWER_GOLDEN_SETTINGS(DCM): ON
SPM_CONTROL_AFTERK: ON
TEMP_SENSOR_ENABLE: OFF
ENABLE_PER_BANK_REFRESH: OFF
HW_SAVE_FOR_SR: OFF
=========================
[MEM] complex R/W mem test pass
NOTICE:  BL2: Booting BL31


U-Boot 2019.10 (Dec 09 2020 - 23:51:30 +0000), Build: jenkins-excelsior.excelsior-bootloader-2

CPU:   MediaTek MT8516
DRAM:  512 MiB
WDT:   Started with servicing (60s timeout)
MMC:   mmc@11120000: 0
Loading Environment from MMC... OK
In:    serial@11005000
Out:   serial@11005000
Err:   serial@11005000
8GB mmc detected
Hit any key to stop autoboot:  0 
gpio: pin 42 (gpio 42) value is 1
switch to partitions #0, OK
mmc0(part 0) is current device
1420 bytes read in 0 ms
## Executing script at 4c000000
Loading image...
6747990 bytes read in 86 ms (74.8 MiB/s)
Loading device tree...
42834 bytes read in 2 ms (20.4 MiB/s)
104 bytes read in 0 ms
## Loading kernel from FIT Image at 4a000000 ...
   Using 'conf@1' configuration
   Trying 'kernel@1' kernel subimage
     Description:  Linux kernel
     Type:         Kernel Image
     Compression:  gzip compressed
     Data Start:   0x4a0000e4
     Data Size:    6746273 Bytes = 6.4 MiB
     Architecture: AArch64
     OS:           Linux
     Load Address: 0x40080000
     Entry Point:  0x40080000
     Hash algo:    sha256
     Hash value:   0470380bb98e5f4131f5dec4c7721e059de557065168fa7ba4ad6ad0caa94b65
   Verifying Hash Integrity ... sha256+ OK
## Flattened Device Tree blob at 42000000
   Booting using the fdt blob at 0x42000000
   Uncompressing Kernel Image
   Loading Device Tree to 000000005fb7e000, end 000000005fb8bfff ... OK

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd041]
[    0.000000] Linux version 4.19.125-mtk (pbuilder@linux-mtk-44a92093-5a4b-410b-8ad5-805072874b42-7qs4k-8xlpx) (gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP PREEMPT Thu Dec 10 02:36:13 UTC 2020
[    0.000000] Machine model: Google Coral MT8167
[    0.000000] efi: Getting EFI parameters from FDT:
[    0.000000] efi: UEFI not found.
[    0.000000] cma: Reserved 64 MiB at 0x00000000bc000000
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv1.1 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: Trusted OS migration not required
[    0.000000] psci: SMC Calling Convention v1.1
[    0.000000] random: get_random_bytes called from start_kernel+0x98/0x44c with crng_init=0
[    0.000000] percpu: Embedded 22 pages/cpu s53144 r8192 d28776 u90112
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] Speculative Store Bypass Disable mitigation not required
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 516064
[    0.000000] Kernel command line: root=PARTUUID=02f36a4f-4562-46b2-bbec-bfc1682f9e92 rootwait
[    0.000000] Dentry cache hash table entries: 262144 (order: 9, 2097152 bytes)
[    0.000000] Inode-cache hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.000000] Memory: 1978928K/2097024K available (9788K kernel code, 1086K rwdata, 3104K rodata, 832K init, 978K bss, 52560K reserved, 65536K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=64 to nr_cpu_ids=4.
[    0.000000]  Tasks RCU enabled.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: GICv2 detected, but range too small and irqchip.gicv2_force_probe not set
[    0.000000] arch_timer: cp15 timer(s) running at 13.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x2ff89eacb, max_idle_ns: 440795202429 ns
[    0.000004] sched_clock: 56 bits at 13MHz, resolution 76ns, wraps every 4398046511101ns
[    0.000105] clocksource: timer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 147020034397 ns
[    0.000115] sched_clock: 32 bits at 13MHz, resolution 76ns, wraps every 165191050201ns
[    0.000546] Console: colour dummy device 80x25
[    0.000908] console [tty0] enabled
[    0.000938] Calibrating delay loop (skipped), value calculated using timer frequency.. 26.00 BogoMIPS (lpj=52000)
[    0.000963] pid_max: default: 32768 minimum: 301
[    0.001063] Security Framework initialized
[    0.001081] SELinux:  Initializing.
[    0.001178] Mount-cache hash table entries: 4096 (order: 3, 32768 bytes)
[    0.001204] Mountpoint-cache hash table entries: 4096 (order: 3, 32768 bytes)
[    0.023968] ASID allocator initialised with 32768 entries
[    0.031961] rcu: Hierarchical SRCU implementation.
[    0.040295] EFI services will not be available.
[    0.048017] smp: Bringing up secondary CPUs ...
[    0.080207] Detected VIPT I-cache on CPU1
[    0.080256] CPU1: Booted secondary processor 0x0000000001 [0x410fd041]
[    0.112283] Detected VIPT I-cache on CPU2
[    0.112325] CPU2: Booted secondary processor 0x0000000002 [0x410fd041]
[    0.144366] Detected VIPT I-cache on CPU3
[    0.144406] CPU3: Booted secondary processor 0x0000000003 [0x410fd041]
[    0.144513] smp: Brought up 1 node, 4 CPUs
[    0.144595] SMP: Total of 4 processors activated.
[    0.144612] CPU features: detected: 32-bit EL0 Support
[    0.144663] CPU: All CPU(s) started at EL2
[    0.144691] alternatives: patching kernel code
[    0.145580] devtmpfs: initialized
[    0.152954] Registered cp15_barrier emulation handler
[    0.152988] Registered setend emulation handler
[    0.153366] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.153402] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.154918] pinctrl core: initialized pinctrl subsystem
[    0.155508] DMI not present or invalid.
[    0.155744] NET: Registered protocol family 16
[    0.156093] audit: initializing netlink subsys (disabled)
[    0.156276] audit: type=2000 audit(0.152:1): state=initialized audit_enabled=0 res=1
[    0.157015] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.161562] DMA: preallocated 256 KiB pool for atomic allocations
[    0.186378] cryptd: max_cpu_qlen set to 1000
[    0.189585] PVR_K:(Error):     1: mtk_mfg_async_init: Enable power domain failed
[    0.189788] PVR_K:(Error):     1: mtk_mfg_2d_init: Enable power domain failed
[    0.190034] SCSI subsystem initialized
[    0.190169] usbcore: registered new interface driver usbfs
[    0.190221] usbcore: registered new interface driver hub
[    0.190350] usbcore: registered new device driver usb
[    0.191014] i2c-gpio 1100b000.i2c: using lines 447 (SDA) and 448 (SCL)
[    0.191172] videodev: Linux video capture interface: v2.00
[    0.192448] Advanced Linux Sound Architecture Driver Initialized.
[    0.193009] Bluetooth: Core ver 2.22
[    0.193073] NET: Registered protocol family 31
[    0.193088] Bluetooth: HCI device and connection manager initialized
[    0.193109] Bluetooth: HCI socket layer initialized
[    0.193127] Bluetooth: L2CAP socket layer initialized
[    0.193171] Bluetooth: SCO socket layer initialized
[    0.193662] clocksource: Switched to clocksource arch_sys_counter
[    0.251183] VFS: Disk quotas dquot_6.6.0
[    0.251264] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.259567] NET: Registered protocol family 2
[    0.260125] tcp_listen_portaddr_hash hash table entries: 1024 (order: 2, 16384 bytes)
[    0.260174] TCP established hash table entries: 16384 (order: 5, 131072 bytes)
[    0.260312] TCP bind hash table entries: 16384 (order: 6, 262144 bytes)
[    0.260521] TCP: Hash tables configured (established 16384 bind 16384)
[    0.260659] UDP hash table entries: 1024 (order: 3, 32768 bytes)
[    0.260716] UDP-Lite hash table entries: 1024 (order: 3, 32768 bytes)
[    0.260922] NET: Registered protocol family 1
[    0.262344] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    0.265591] Initialise system trusted keyrings
[    0.265823] workingset: timestamp_bits=62 max_order=19 bucket_order=0
[    0.270470] fuse init (API version 7.27)
[    0.275040] Key type asymmetric registered
[    0.275068] Asymmetric key parser 'x509' registered
[    0.275098] io scheduler noop registered
[    0.275112] io scheduler deadline registered
[    0.275259] io scheduler cfq registered (default)
[    0.275277] io scheduler mq-deadline registered
[    0.275292] io scheduler kyber registered
[    0.284009] Serial: 8250/16550 driver, 3 ports, IRQ sharing disabled
[    0.285432] mt-pmic-pwrap 1000f000.pwrap: unexpected interrupt int=0x1
[    0.305814] 11005000.serial: ttyS0 at MMIO 0x11005000 (irq = 183, base_baud = 1625000) is a ST16650V2
[    0.931290] console [ttyS0] enabled
[    0.956069] 11006000.serial: ttyS1 at MMIO 0x11006000 (irq = 184, base_baud = 1625000) is a ST16650V2
[    0.966164] mtk_rng 1020c000.rng: registered RNG driver
[    0.966537] random: fast init done
[    0.972787] iommu: Adding device 14007000.disp_ovl0 to group 0
[    0.975192] random: crng init done
[    0.981298] iommu: Adding device 1400a000.rdma1 to group 0
[    0.989740] iommu: Adding device 14009000.disp_rdma0 to group 0
[    0.997359] mediatek-drm 14000000.mmsys2: Adding component match for /soc/dpi1@14019000
[    1.005495] mediatek-drm 14000000.mmsys2: Adding component match for /soc/rdma1@1400a000
[    1.013612] mediatek-drm 14000000.mmsys2: Adding component match for /soc/disp_ovl0@14007000
[    1.022025] mediatek-drm 14000000.mmsys2: Adding component match for /soc/disp_rdma0@14009000
[    1.030522] mediatek-drm 14000000.mmsys2: Adding component match for /soc/disp_color@1400c000
[    1.040352] mediatek-hdmi-phy 10018300.hdmi-phy: Using default TX DRV impedance: 4.2k/36
[    1.050114] [drm] hdmi-audio-codec driver bound to HDMI
[    1.055660] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    1.068997] brd: module loaded
[    1.080308] loop: module loaded
[    1.083905] zram: Added device: zram0
[    1.087818] [xo] dts default cap code: 0x0
[    1.092008] [xo] default cap_code: 0x30
[    1.095830] [xo] get xo efuse: a4000000
[    1.120077] [xo] set cap_code: 0x24
[    1.123563] [xo] current cap_code: 0x24
[    1.127403] [Preloader] BSI read: [0x25] = 0x6aab
[    1.132098] [Preloader] BSI read: [0x29] = 0x1
[    1.136633] [Preloader] BSI read: [0x29] = 0x0
[    1.141059] [xo] status: 0xf
[    1.143955] [xo] current cap code: 0x24
[    1.148819] mt6392-regulator mt6392-regulator: Chip ID = 0x2092
[    1.161291] ldo_vgp2: Bringing 2800000uV into 3300000-3300000uV
[    1.173463] tun: Universal TUN/TAP device driver, 1.6
[    1.179002] PPP generic driver version 2.4.2
[    1.183417] PPP BSD Compression module registered
[    1.188105] PPP Deflate Compression module registered
[    1.193146] PPP MPPE Compression module registered
[    1.197924] NET: Registered protocol family 24
[    1.202683] usbcore: registered new interface driver usb-storage
[    1.208700] usbcore: registered new interface driver ums-alauda
[    1.214615] usbcore: registered new interface driver ums-cypress
[    1.220614] usbcore: registered new interface driver ums-datafab
[    1.226613] usbcore: registered new interface driver ums-freecom
[    1.232611] usbcore: registered new interface driver ums-isd200
[    1.238523] usbcore: registered new interface driver ums-jumpshot
[    1.244612] usbcore: registered new interface driver ums-karma
[    1.250440] usbcore: registered new interface driver ums-onetouch
[    1.256525] usbcore: registered new interface driver ums-sddr09
[    1.262437] usbcore: registered new interface driver ums-sddr55
[    1.268350] usbcore: registered new interface driver ums-usbat
[    1.274227] usbcore: registered new interface driver option
[    1.279795] usbserial: USB Serial support registered for GSM modem (1-port)
[    1.287141] usb_phy_generic usb_phy_generic.1.auto: usb_phy_generic.1.auto supply vcc not found, using dummy regulator
[    1.297874] usb_phy_generic usb_phy_generic.1.auto: Linked as a consumer to regulator.0
[    1.305949] musb-mtk 11100000.usb: Linked as a consumer to regulator.1
[    1.313054] musb-hdrc musb-hdrc.2.auto: MUSB HDRC host driver
[    1.318808] musb-hdrc musb-hdrc.2.auto: new USB bus registered, assigned bus number 1
[    1.327257] hub 1-0:1.0: USB hub found
[    1.331034] hub 1-0:1.0: 1 port detected
[    1.336811] input: mtk-pmic-keys as /devices/platform/soc/1000f000.pwrap/1000f000.pwrap:pmic/mtk-pmic-keys/input/input0
[    1.348659] mt6397-rtc mt6397-rtc: registered as rtc0
[    1.353761] i2c /dev entries driver
[    1.359522] iommu: Adding device 16000000.vcu to group 0
[    1.365148] iommu: Adding device soc:vcu@1 to group 0
[    1.370795] iommu: Adding device 16000000.codec to group 0
[    1.377779] iommu: Adding device 14001000.rdma to group 0
[    1.383996] iommu: Adding device d5af20.wdma to group 0
[    1.389370] iommu: Adding device d5b308.wrot to group 0
[    1.395139] mtk-mdp 14001000.rdma: driver registered as /dev/video2
[    1.395860] iommu: Adding device 10011800.mipicsi to group 0
[    1.407823] mtk-mipicsi 10011800.mipicsi: Waiting for larb device larb@15001000
[    1.415628] ov5645_mipi 2-003c: Linked as a consumer to regulator.27
[    1.422443] ov5645_mipi 2-003c: Linked as a consumer to regulator.26
[    1.429241] ov5645_mipi 2-003c: Linked as a consumer to regulator.11
[    1.505896] ov5645_read_reg:write reg error:reg=300a
[    1.510840] camera ov5645_mipi is not found
[    1.515128] ov5645_mipi 2-003c: Dropping the link to regulator.11
[    1.521276] ov5645_mipi 2-003c: Dropping the link to regulator.26
[    1.527422] ov5645_mipi 2-003c: Dropping the link to regulator.27
[    1.534142] mtk-thermal 1100d000.thermal: Calibration data: buf[0]:0x29c0e25d, buf[1]:0x82e336d9, buf[2]:0x702ae600
[    1.544580] mtk-thermal 1100d000.thermal: Calibration data: adc_ge:523, vts1:224, vts2:226, vts3:224, degc_cali:46, o_slope:10
[    1.556609] mtk-wdt 10007000.toprgu: Watchdog enabled (timeout=31 sec, nowayout=0)
[    1.564568] device-mapper: uevent: version 1.0.3
[    1.569445] device-mapper: ioctl: 4.39.0-ioctl (2018-04-03) initialised: dm-devel@redhat.com
[    1.578041] Bluetooth: Generic Bluetooth SDIO driver ver 0.1
[    1.584212] cpu cpu0: Linked as a consumer to regulator.6
[    1.589641] cpu cpu0: dummy supplies not allowed for exclusive requests
[    1.598770] mtk-msdc 11120000.mmc: Linked as a consumer to regulator.19
[    1.605471] mtk-msdc 11120000.mmc: Linked as a consumer to regulator.25
[    1.640271] mtk-msdc 11130000.mmc: Linked as a consumer to regulator.19
[    1.647418] mtk-msdc 11130000.mmc: Linked as a consumer to regulator.25
[    1.679062] mtk-msdc 11170000.mmc: Linked as a consumer to regulator.18
[    1.685961] mtk-msdc 11170000.mmc: Linked as a consumer to regulator.17
[    1.719581] hidraw: raw HID events driver (C) Jiri Kosina
[    1.726943] usbcore: registered new interface driver usbhid
[    1.732552] usbhid: USB HID core driver
[    1.737825] mtk-msdc 11120000.mmc: phase: [map:ffff803f] [maxlen:17] [final:23]
[    1.738503] mtk-msdc 11130000.mmc: phase: [map:f07fffff] [maxlen:23] [final:7]
[    1.745486] mmc0: new HS200 MMC card at address 0001
[    1.745719] mtk-iommu 10203000.m4u: bound 14016000.larb (ops 0xffffff8008af6a38)
[    1.745729] mtk-iommu 10203000.m4u: bound 15001000.larb (ops 0xffffff8008af6a38)
[    1.745738] mtk-iommu 10203000.m4u: bound 16010000.larb (ops 0xffffff8008af6a38)
[    1.746048] optee: probing for conduit method from DT.
[    1.746069] optee: revision 3.8
[    1.746473] optee: initialized driver
[    1.746888] usbcore: registered new interface driver snd-usb-audio
[    1.749863] mtk-afe-pcm 11140000.audio-controller: MTK AFE driver initialized.
[    1.750463] mt8167-excelsior sound: mt8167_excelsior_gpio_probe Set pinctrl state default 0
[    1.750897] mtk-afe-pcm 11140000.audio-controller: ASoC: Failed to create component debugfs directory
[    1.751131] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mt8167-codec node
[    1.751140] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mediatek,afe-regmap
[    1.751165] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found platform device of mediatek,afe-regmap
[    1.751174] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found regmap of mediatek,afe-regmap
[    1.751257] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mt8167-codec node
[    1.751265] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found mediatek,pwrap-regmap
[    1.751277] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found platform device of mediatek,pwrap-regmap
[    1.751283] mt8167-codec mt8167-codec: mt8167_codec_get_regmap_from_dt found regmap of mediatek,pwrap-regmap
[    1.754622] mmc1: new ultra high speed SDR104 SDIO card at address 0001
[    1.759495] mmcblk0: mmc0:0001 MB2908 7.28 GiB 
[    1.909916] mmcblk0boot0: mmc0:0001 MB2908 partition 1 4.00 MiB
[    1.917583] mmcblk0boot1: mmc0:0001 MB2908 partition 2 4.00 MiB
[    1.923736] mmcblk0rpmb: mmc0:0001 MB2908 partition 3 4.00 MiB, chardev (247:0)
[    1.923831] mt8167-excelsior sound: snd-soc-dummy-dai <-> DL1 mapping ok
[    1.938247] mt8167-excelsior sound: snd-soc-dummy-dai <-> VUL mapping ok
[    1.943116] Alternate GPT is invalid, using primary GPT.
[    1.945193] mt8167-excelsior sound: snd-soc-dummy-dai <-> AWB mapping ok
[    1.950249]  mmcblk0: p1 p2 p3 p4
[    1.961081] mt8167-excelsior sound: snd-soc-dummy-dai <-> DL2 mapping ok
[    1.967873] mt8167-excelsior sound: mt8167-codec <-> INT ADDA mapping ok
[    1.974674] mt8167-excelsior sound: ASoC: no DMI vendor name!
[    1.983159] input: excelsior-card Headset Jack as /devices/platform/sound/sound/card0/input1
[    1.992210] drop_monitor: Initializing network drop monitor service
[    1.998529] Mirror/redirect action on
[    2.002220] u32 classifier
[    2.004906]     Performance counters on
[    2.008724]     input device check on
[    2.012385]     Actions configured
[    2.016427] xt_time: kernel timezone is -0000
[    2.020910] ipip: IPv4 and MPLS over IPv4 tunneling driver
[    2.027019] Initializing XFRM netlink socket
[    2.031749] NET: Registered protocol family 10
[    2.037238] Segment Routing with IPv6
[    2.041036] mip6: Mobile IPv6
[    2.044206] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.051131] NET: Registered protocol family 17
[    2.055618] NET: Registered protocol family 15
[    2.060143] Bridge firewalling registered
[    2.064287] Bluetooth: RFCOMM TTY layer initialized
[    2.069296] Bluetooth: RFCOMM socket layer initialized
[    2.074454] Bluetooth: RFCOMM ver 1.11
[    2.078206] 8021q: 802.1Q VLAN Support v1.8
[    2.083070] Loading compiled-in X.509 certificates
[    2.111782] mediatek-dpi 14019000.dpi1: Found bridge node: /soc/hdmi@1401b000
[    2.119164] mediatek-drm 14000000.mmsys2: bound 14019000.dpi1 (ops 0xffffff8008aaeff0)
[    2.127062] mediatek-drm 14000000.mmsys2: bound 1400a000.rdma1 (ops 0xffffff8008aaa728)
[    2.135035] mediatek-drm 14000000.mmsys2: bound 14007000.disp_ovl0 (ops 0xffffff8008aaa1b8)
[    2.143348] mediatek-drm 14000000.mmsys2: bound 14009000.disp_rdma0 (ops 0xffffff8008aaa728)
[    2.151746] mediatek-drm 14000000.mmsys2: bound 1400c000.disp_color (ops 0xffffff8008aa9e10)
[    2.160142] mediatek-drm 14000000.mmsys2: Not creating crtc 0 because component 9 is disabled or missing
[    2.169625] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    2.176204] [drm] No driver support for vblank timestamp query.
[    2.182611] [drm] Initialized mediatek 1.0.0 20150513 for 14000000.mmsys2 on minor 0
[    2.190363] [drm] Cannot find any crtc or sizes
[    2.195663] mtk-mipicsi 10011800.mipicsi: not set mediatek,mipicsi_max_vc, use default value 1
[    2.204247] mtk-mipicsi 10011800.mipicsi: not set mediatek,serdes_link_reg, can't read subdev link number
[    2.213774] mtk-mipicsi 10011800.mipicsi: there are 1 camsv node
[    2.220473] mtk-mipicsi 10011800.mipicsi: seninf_mux_camsv@15004000 parse done
[    2.227975] mtk-mipicsi 10011800.mipicsi: mipicsi@15008000 parse done
[    2.234409] mtk-mipicsi 10011800.mipicsi: mipicsi node parse done
[    2.240533] mtk-mipicsi 10011800.mipicsi: probe done
[    2.245589] [drm] Cannot find any crtc or sizes
[    2.247581] PVR_K:  1: irq_res = 0xca
[    2.253900] PVR_K:  1: reg_res = 0x13000000, 0x80000
[    2.259222] PVR_K:  1: Read BVNC 22.40.54.30 from HW device registers
[    2.265898] PVR_K:  1: RGX Device registered with BVNC 22.40.54.30
[    2.272871] [drm] Initialized pvr 1.11.5516664 20170530 for 13000000.clark on minor 1
[    2.281235] mt6397-rtc mt6397-rtc: hctosys: unable to read the hardware clock
[    2.288557] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    2.298030] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    2.304688] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    2.306047] [MUSBFSH] musbfsh_init 1859: MUSBFSH is enabled
[    2.313282] cfg80211: failed to load regulatory.db
[    2.319899] musbfsh-hdrc musbfsh-hdrc.0: Linked as a consumer to regulator.4
[    2.330610] [MUSBFSH] musbfsh_init_controller 1372: vbus registered
[    2.338584] [MUSBFSH] musbfsh_core_init 894: musbfsh-hdrc: ConfigData=0x1f (UTMI-16, dyn FIFOs, HB-ISO Rx, HB-ISO Tx, SoftConn)
[    2.353076] musbfsh-hdrc musbfsh-hdrc.0: MUSBFSH HDRC host driver
[    2.359194] musbfsh-hdrc musbfsh-hdrc.0: new USB bus registered, assigned bus number 2
[    2.367814] hub 2-0:1.0: USB hub found
[    2.371602] hub 2-0:1.0: 1 port detected
[    2.375681] [MUSBFSH] musbfsh_start 581: <== devctl 0x98
[    2.380968] [MUSBFSH] mt_usb11_set_vbus 455: Enable VBUS
[    2.437770] musbfsh-hdrc musbfsh-hdrc.0: USB controller at 0000000027cdd5a2 using DMA, IRQ 193
[    2.446465] [MUSBFSH] musbfsh_init_enable_pin 1310: ERROR: Cannot find musbfsh_pinctrl!
[    2.454516] ALSA device list:
[    2.457462]   #0: excelsior-card
[    2.466690] EXT4-fs (mmcblk0p4): INFO: recovery required on readonly filesystem
[    2.474131] EXT4-fs (mmcblk0p4): write access will be enabled during recovery
[    2.537746] [MUSBFSH] musbfsh_hub_control 565: port status 00000100,devctl=0x19
[    2.545169] [MUSBFSH] musbfsh_bus_suspend 2806: musbfsh_bus_suspend++,power=0x61
[    2.623869] [MUSBFSH] musbfsh_stage0_irq 532: CONNECT ! devctl 0x5d
[    2.630117] [MUSBFSH] musbfsh_bus_resume 2852: musbfsh_bus_resume++,power=0x61
[    2.637409] [MUSBFSH] musbfsh_hub_control 565: port status 00010101,devctl=0x5d
[    2.749701] [MUSBFSH] musbfsh_hub_control 565: port status 00000101,devctl=0x5d
[    2.757074] [MUSBFSH] musbfsh_port_reset 261: reset=1 power=0x61
[    2.769087] EXT4-fs (mmcblk0p4): orphan cleanup on readonly fs
[    2.775234] EXT4-fs (mmcblk0p4): 1 orphan inode deleted
[    2.780468] EXT4-fs (mmcblk0p4): recovery complete
[    2.794972] EXT4-fs (mmcblk0p4): mounted filesystem with ordered data mode. Opts: (null)
[    2.803106] VFS: Mounted root (ext4 filesystem) readonly on device 179:4.
[    2.810507] devtmpfs: mounted
[    2.813868] Freeing unused kernel memory: 832K
[    2.818440] Run /sbin/init as init process
[    2.829723] [MUSBFSH] musbfsh_port_reset 261: reset=0 power=0x78
[    2.835721] [MUSBFSH] musbfsh_hub_control 565: port status 00120503,devctl=0x5d
[    2.901781] usb 2-1: new high-speed USB device number 2 using musbfsh-hdrc
[    2.908887] [MUSBFSH] musbfsh_port_reset 261: reset=1 power=0x70
[    2.981717] [MUSBFSH] musbfsh_port_reset 261: reset=0 power=0x78
[    2.987720] [MUSBFSH] musbfsh_hub_control 565: port status 00120503,devctl=0x5d
SELinux:  Could not open policy file <= /etc/selinux/targeted/po[    3.050174] systemd[1]: System time before build time, advancing clock.
licy/policy.31: [    3.057834] [MUSBFSH] musbfsh_h_disable 2655: musbfsh_h_disable++: ep: 0x0
 No such file or[    3.065584] MTK_ICUSB [DBG], <musbfsh_h_disable(), 2660> qh == NULL
 directory
[    3.073518] [MUSBFSH] musbfsh_h_disable 2655: musbfsh_h_disable++: ep: 0x0
[    3.081459] MTK_ICUSB [DBG], <musbfsh_h_disable(), 2660> qh == NULL
[    3.103619] systemd[1]: Failed to find module 'autofs4'
[    3.111310] [MUSBFSH] musbfsh_hub_control 565: port status 00020503,devctl=0x5d
[    3.127054] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    3.148929] systemd[1]: Detected architecture arm64.

Welcome to Mendel GNU/Linux 5 (Eagle)!

[    3.170512] systemd[1]: Set hostname to <neat-calf>.
[    3.363706] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
[    3.380942] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
[    3.494367] systemd[1]: /lib/systemd/system/vitalsd.service:3: Failed to add dependency on usb-gadget, ignoring: Unknown error -22
[    3.506303] systemd[1]: /lib/systemd/system/vitalsd.service:5: Unknown lvalue 'Exec' in section 'Service', ignoring
[    3.517015] systemd[1]: vitalsd.service: Service has no ExecStart=, ExecStop=, or SuccessAction=. Refusing.
[    3.618152] systemd[1]: /lib/systemd/system/usb-gadget-getty-ttyGS0.service:21: Unknown lvalue 'TTYDisallocate' in section 'Service', ignoring
[    3.673042] systemd[1]: vitalsd.service: Cannot add dependency job, ignoring: Unit vitalsd.service has a bad unit file setting.
[  OK  ] Created slice system-systemd\x2dmkfs.slice.
[  OK  ] Listening on fsck to fsckd communication Socket.
[  OK  ] Listening on udev Control Socket.
[  OK  ] Started Dispatch Password …ts to Console Directory Watch.
[  OK  ] Created slice system-systemd\x2dfsck.slice.
[  OK  ] Listening on Journal Audit Socket.
[  OK  ] Reached target Swap.
[  OK  ] Started Forward Password R…uests to Wall Directory Watch.
[  OK  ] Listening on udev Kernel Socket.
[  OK  ] Listening on Syslog Socket.
[  OK  ] Listening on Journal Socket.
         Starting Load Kernel Modules...
         Mounting Kernel Debug File System...
         Starting udev Coldplug all Devices...
         Mounting POSIX Message Queue File System...
         Starting File System Check on Root Device...
[  OK  ] Reached target Remote File Systems.
[  OK  ] Created slice User and Session Slice.
[  OK  ] Reached target Slices.
[  OK  ] Listening on Journal Socket (/dev/log).
         Starting Journal Service...
[  OK  ] Created slice system-serial\x2dgetty.slice.
[  OK  ] Reached target Local Encrypted Volumes.
[  OK  ] Listening on initctl Compatibility Named Pipe.
[  OK  ] Created slice system-getty.slice.
[  OK  ] Started Load Kernel Modules.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Mounted POSIX Message Queue File System.
[  OK  ] Started File System Check on Root Device.
[  OK  ] Started Journal Service.
[  OK  ] Started File System Check Daemon to report status.
         Starting Remount Root and Kernel File Systems...
         Mounting Kernel Configuration File System...
         Mounting FUSE Control File System...
         Starting Apply Kernel Variables...
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Mounted FUSE Control File System.
[    4.377831] EXT4-fs (mmcblk0p4): re-mounted. Opts: (null)
[  OK  ] Started Apply Kernel Variables.
[  OK  ] Started Remount Root and Kernel File Systems.
         Starting Create System Users...
         Starting Load/Save Random Seed...
[  OK  ] Started udev Coldplug all Devices.
[  OK  ] Started Create System Users.
[  OK  ] Started Load/Save Random Seed.
         Starting Create Static Device Nodes in /dev...
         Starting Helper to synchronize boot up for ifupdown...
[  OK  ] Started Helper to synchronize boot up for ifupdown.
[  OK  ] Started Create Static Device Nodes in /dev.
[  OK  ] Reached target Local File Systems (Pre).
         Mounting /var/log...
         Starting udev Kernel Device Manager...
[  OK  ] Mounted /var/log.
         Starting Flush Journal to Persistent Storage...
[    4.705496] systemd-journald[155]: Received request to flush runtime journal from PID 1
[  OK  ] Started udev Kernel Device Manager.
[  OK  ] Started Flush Journal to Persistent Storage.
[  OK  ] Started MDP Daemon.
[  OK  ] Started VPU Daemon.
mdpd without fuse
mdpd: shmem_length=1212416, shmem=0x7f9d931000
remap_shmem,line:311 vpud: shmem_length=1089536, shmem=0x7fb5007000

[Info]vpud_init,line:343 share_obj:56,1024,24, set:40387600,mva:c0187601,free:c0187602,flush:c0187603,get:c0387604,log:7f44007605,cache:c0187606
vdec_codec_service_init() block mode
venc_codec_service_init()
The firmware version is 0.2.14
The firmware version is 0.2.13
--[mdp] create_rt_thread,line:217
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Found device /dev/disk/by-…b-1d90-492f-ab86-6952303b214e.
[    5.453752] wlan_mt7668_sdio: loading out-of-tree module taints kernel.
[  OK  ] Found device /dev/disk/by-…9-3004-4e30-87dc-ed33fbf4dbfd.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Starting File System Check…1d90-492f-ab86-6952303b214e...
         Starting Make File System …3004-4e30-87dc-ed33fbf4dbfd...
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Started Make File System o…9-3004-4e30-87dc-ed33fbf4dbfd.
         Starting File System Check…3004-4e30-87dc-ed33fbf4dbfd...
[  OK  ] Started File System Check …9-3004-4e30-87dc-ed33fbf4dbfd.
         Mounting /home...
Checking in progress on 1 disk [    6.333857] EXT4-fs (mmcblk0p3): mounted filesystem with ordered data mode. Opts: (null)
[  OK  ] Mounted /home. 1 disk (56.9% complete)
[    6.369678] [XO] xocap_timer_func% complete)
[    6.373035] [XO] xocap_work_func
[    6.376352] [MT6620][nvram_read] : failed to open!!
[    6.381279]  ret is -1!
Checking i[    6.404831] current cap code(after nvram):0x24
Checking in progress on 1 disk (98.1% com[    6.416561] EXT4-fs (mmcblk0p2): mounting ext2 file system using the ext4 subsystem
Checking in progress on [    6.427327] EXT4-fs (mmcblk0p2): mounted filesystem without journal. Opts: (null)
[  OK  ] Started File System Check …b-1d90-492f-ab86-6952303b214e.
         Mounting /boot...
[  OK  ] Mounted /boot.
[  OK  ] Reached target Local File Systems.
         Starting Create Volatile Files and Directories...
         Starting Raise network interfaces...
[  OK  ] Started Create Volatile Files and Directories.
         Starting Update UTMP about System Boot/Shutdown...
[  OK  ] Started Entropy daemon using the HAVEGE algorithm.
         Starting Network Time Synchronization...
[    6.552391] net lo: No handler found (wireless_process_ioctl)
[  OK  ] Started Update UTMP about System Boot/Shutdown.
[  OK  ] Started Raise network interfaces.
[  OK  ] Started Network Time Synchronization.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Daily man-db regeneration.
[  OK  ] Started Daily rotation of log files.
[  OK  ] Started Restart mdt-keymas… when authorized_keys changes.
[  OK  ] Reached target Paths.
[  OK  ] Started Daily Cleanup of Temporary Directories.
         Starting Scripts that should be run only once...
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Started Daily apt download activities.
[  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
[  OK  ] Reached target Sockets.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Reached target Timers.
[  OK  ] Started Scripts that should be run only once.
[  OK  ] Reached target Basic System.
         Starting Initialize hardware monitoring sensors...
[  OK  ] Started Regular background program processing daemon.
         Starting Login Service...
[  OK  ] Started D-Bus System Message Bus.
         Starting Network Manager...
[  OK  ] Started Excelsior bootloader install service.
[  OK  ] Started Manage Sound Card State (restore and store).
         Starting Save/Restore Sound Card State...
         Starting System Logging Service...
         Starting WPA supplicant...
         Starting USB Gadget...
         Starting Avahi mDNS/DNS-SD Stack...
[  OK  ] Started System Logging Service.
[  OK  ] Started Initialize hardware monitoring sensors.
[  OK  ] Started Avahi mDNS/DNS-SD Stack.
[  OK  ] Started Save/Restore Sound Card State.
[  OK  ] Reached target Sound Card.
[  OK  ] Started WPA supplicant.
[  OK  ] Started Login Service.
[  OK  ] Started Network Manager.
         Starting Hostname Service...
[  OK  ] Started Hostname Service.
         Starting Network Manager Script Dispatcher Service...
[  OK  ] Started Network Manager Script Dispatcher Service.
         Starting Authorization Manager...
[  OK  ] Started Authorization Manager.
[    7.952939] using random self ethernet address
[    7.957455] using random host ethernet address
[    7.974201] using random self ethernet address
[    7.978838] using random host ethernet address
[    8.266856] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
[    8.338381] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
[  OK  ] Started Excelsior Bluetooth Module    8.348842] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
0m.
[    8.455234] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
[    8.559956] BTMTK_init
[    8.562372] proc initialized
[    8.562398] major number:244
[    8.568160] BT_majorfwlog number: 243
[    8.571847] BT_chrdev driver(major 244) installed.
[    8.576643] BT_chrdevfwlog driver(major 243) installed.
[    8.582316] BTMTK_init: BT_major 244, BT_majorfwlog 243
[    8.587569] BTMTK_init: devID 255852544, devIDfwlog 254803968
[    8.593523] btmtk_sdio_probe Mediatek Bluetooth driver Version=v0.0.0.53_2018072701_YOCTO
[    8.601733] vendor=0x37a, device=0x7668, class=255, fn=2, support func_num 2
[    8.608786] btmtk_sdio_probe chip_id is 7668
[    8.613186] before claim irq read SDIO_CCCR_IENx 0, func num 2
[    8.619082] sdio_claim_irq success: ret=0
[    8.623133] after claim irq read SDIO_CCCR_IENx 0
[    8.627937] SDIO FUNC2 IO port: 0xf07668
[    8.631964] btmtk_sdio_enable_host_int read CSDIOCSR is 0x1
[    8.637581] btmtk_sdio_enable_host_int write CSDIOCSR is 0x5
[    8.643240] btmtk_sdio_download_fw begin
[    8.647335] btmtk_sdio_send_wohci retrun  0x0
[    8.651810] btmtk_sdio_bt_memRegister_read: read cr 80000000
[    8.672690] btmtk_sdio_bt_memRegister_read: retrytime 299
[    8.678101] btmtk_sdio_bt_memRegister_read: ger cr 0x80000000 value 0x8b11
[    8.684962] btmtk_sdio_download_rom_patch uhwversion 0x8b11
[    8.690529] btmtk_sdio_download_rom_patch request_firmware(firmware name mt7668_patch_e2_hdr.bin)
[    8.699797] btmtk_sdio_download_rom_patch patch is ready no need load patch again
[    8.707354] btmtk_sdio_download_rom_patch read chipid =  f07668
[    8.713377] btmtk_sdio_bt_set_power: onoff 1
[    8.825969] btmtk_eeprom_bin_file: 7668 series
[    8.965896] btmtk_set_eeprom2ctrler: set BDAddress(F4-F5-E8-EC-AF-E8) OK
[    9.032952] usb0: HOST MAC a6:e9:32:87:6d:79
[    9.034208] net usb0: No handler found (wireless_process_ioctl)
[    9.046019] usb0: MAC 02:22:78:0d:f6:df
[    9.050957] usb1: HOST MAC 02:22:78:0d:f6:dd
[    9.056045] usb1: MAC 02:22:78:0d:f6:de
[    9.058643] net usb1: No handler found (wireless_process_ioctl)
[    9.077886] btmtk_set_eeprom2ctrler: set radio(BT/BLE default power: 5/5 MAX power: 5) OK
[    9.206144] btmtk_sdio_recv_rx_data: retry_count = 0,timeout
[    9.317854] btmtk_set_eeprom2ctrler: set power offset(FE FD FD FD FC FB) OK
[    9.318239] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.331186] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.346579] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.369475] IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
[    9.433870] btmtk_set_eeprom2ctrler: set XTAL(0xAB 00) OK
[    9.439360] btmtk_sdio_set_sleep begin
[    9.446742] btmtk_sdio_set_write_clear write CHCR 0x00000002
[    9.452483] btmtk_sdio_set_write_clear read CHCR 0x00000002
[    9.458077] btmtk_sdio_set_write_clear write clear
[    9.463114] btmtk_sdio_set_i2s_slave
[    9.470180] btmtk_sdio_read_pin_mux_setting
[    9.477825] btmtk_sdio_write_pin_mux_setting begin
[    9.486001] btmtk_sdio_read_pin_mux_setting
[    9.493547] confirm pinmux 22220000
[    9.497135] btmtk_add_card begin
[    9.500438] Starting kthread...
[    9.503945] main_thread begin 50
[    9.507277] btmtk_service_main_thread probe_ready 0 delay 10ms~15ms
[    9.508767] btmtk_sdio_probe normal end
[    9.521906] SDIO Driver Registration Success
[    9.530699] Bluetooth: hci0: unexpected event for opcode 0xfcd1
[    9.542382] configfs-gadget gadget: high-speed config #1: c
[    9.547989] gs_console_connect: port num [0] is not support console
[    9.555766] IPv6: ADDRCONF(NETDEV_CHANGE): usb0: link becomes ready
         Starting Bluetooth service...
[  OK  ] Started Bluetooth service.
[  OK  ] Reached target Bluetooth.
[    9.968694] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[    9.975082] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[    9.990680] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[   10.011627] IPv6: ADDRCONF(NETDEV_UP): usb1: link is not ready
[  OK  ] Started USB Gadget.
[  OK  ] Reached target Network.
[  OK  ] Started MDT public key management service.
         Starting OpenBSD Secure Shell server...
         Starting Permit User Sessions...
         Starting dnsmasq - A light…DHCP and caching DNS server...
[  OK  ] Started Unattended Upgrades Shutdown.
[  OK  ] Started Permit User Sessions.
[  OK  ] Started Getty on tty1.
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Started Getty on ttyGS0.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started Update LED behavior after boot.
         Starting Weston Wayland Compositor (on tty7)...
[  OK  ] Started Weston Wayland Compositor (on tty7).
[  OK  ] Started OpenBSD Secure Shell server.
[  OK  ] Created slice User Slice of UID 1000.
         Starting User Runtime Directory /run/user/1000...
[  OK  ] Started dnsmasq - A lightw…t DHCP and caching DNS server.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.
         Starting Update UTMP about System Runlevel Changes...
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Started Update UTMP about System Runlevel Changes.
[  OK  ] Started User Runtime Directory /run/user/1000.
         Starting User Manager for UID 1000...
[  OK  ] Started User Manager for UID 1000.
[  OK  ] Started    11.289478] PVR_K:  706: RGX Firmware image 'rgx.fw.22.40.54.30' loaded

Mendel GNU/Linux (eagle) neat-calf ttyS0

neat-calf login: [   33.761780] usb0_vbus: disabling
[   33.765004] usb0_vbus_old: disabling
[   33.768609] backlight_vbus: disabling
[   33.772363] ldo_vm25: disabling
                                                   




[15168] Failed to execute script 'flashtool' due to unhandled exception!
Traceback (most recent call last):
  File "flashtool.py", line 16, in <module>
ModuleNotFoundError: No module named 'progress'
Failed uploading: uploading error: exit status 1

## fix1 (ModuleNotFoundError: No module named 'progress'):

cd C:/Users/heman/coralmicro/scripts

pyinstaller -F --paths=C:/heman/python39/Lib/site-packages flashtool.py

cp C:/Users/heman/coralmicro/scripts/dist/flashtool.exe C:\Users\heman\AppData\Local\Arduino15\packages\coral\tools\flashtool\1.0.0



## fix2(C:\Users\heman\AppData\Local\Temp\_MEI134082\third_party\nxp\elftosb\win\elftosb.exe does not exist):
To resolve it:
1. Modified flashtoll script root_dir to get  C:\Users\heman\AppData\Local\Temp instead C:\Users\heman\AppData\Local\Temp\_MEI134082 
2. copiled third_party directory from coaralmicro to C:\Users\heman\AppData\Local\Temp


## fix3(isuue with libusb as libusb-1.0.dll is not added to flashtoo.exe):

To resolve it:
generated the flashtool.exe with below command:

pyinstaller flashtool.spec

flashtool.spec file content:

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

binaries = [
   ('C:\WINDOWS\system32\libusb-1.0.dll', '.'),
]


a = Analysis(
    ['flashtool.py'],
    pathex=[],
    binaries=binaries,
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='flashtool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


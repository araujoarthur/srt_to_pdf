# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        ('C:/msys64/mingw64/bin/libgobject-2.0-0.dll', '.'), 
        ('C:/msys64/mingw64/bin/libglib-2.0-0.dll','.'), 
        ('C:/msys64/mingw64/bin/libpango-1.0-0.dll','.'), 
        ('C:/msys64/mingw64/bin/libfontconfig-1.dll','.'),
        ('C:/msys64/mingw64/bin/libpangoft2-1.0-0.dll','.')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='s2p-x64',
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
    onefile=True,
    distpath="dist/x64"
)

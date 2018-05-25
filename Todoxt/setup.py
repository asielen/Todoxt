# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'



data_files = [('',['config.ini','view-refresh.png','preferences-system.png','icon.png'])]

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Todoxt",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]\Todoxt.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     "TARGETDIR",               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}


##executables = [
##    Executable('Todoxt.py', base=base)
##]

executables = [Executable(
    "Todoxt.py",
    base="Win32GUI",
    icon="icon.ico"
    )]

options = {
    'build_exe': {
        'includes': 'atexit'
    },"bdist_msi": bdist_msi_options
}

setup(name='Todoxt',
      shortcutName="Todoxt",
      shortcutDir="DesktopFolder",
      version='0.12',
      description='Todoxt GUI application',
      options=options,
      executables=executables,
      data_files = data_files
)

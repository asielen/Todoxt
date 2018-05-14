# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

data_files = [('',['config.ini'])]

##executables = [
##    Executable('Todoxt.py', base=base)
##]

executables = [Executable(
    "Todoxt.py",
    base="Win32GUI",
    icon="icon.ico"
    )]

setup(name='Todoxt',
      version='0.1',
      description='Todo.xtx GUI application',
      options=options,
      executables=executables,
      data_files = data_files
)

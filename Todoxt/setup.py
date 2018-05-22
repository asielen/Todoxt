# -*- coding: utf-8 -*-
#!/usr/bin/python3

import sys
import cx_Freeze

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

executables = [cx_Freeze.Executable(
    "Todoxt.py",
    base="Win32GUI",
    icon="icon.ico"
    )]

cx_Freeze.setup(name='Todoxt',
                version='0.1',
                description='Todo.xtx GUI application',
                options=options,
                executables=executables,
                data_files = data_files
                )

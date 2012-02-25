#! /usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from glob import glob
from shutil import rmtree
import os, sys

# Remove the build folder
rmtree("build", ignore_errors=True)

# Note that for distutils functions all supplied pathnames should
# be written using the Unix convention, i.e. slash-separated.
# The distutils will take care about conversion.
# For standard functions like glob.glob() or os.listdir() use
# os.path.join() to stay portable among platforms.

my_data_files = []
# we use package_data, but data_files is needed for py2exe
# adjust ../path/to/gdiplus.dll (must be a relaitve path)
if "py2exe" in sys.argv:
    import py2exe
    my_data_files = [
                    ('icons', glob(os.path.join('icons', '*'))),
                    ('',      ['readme.md', 'CHANGELOG.TXT',
                               '../../../programming/python27/lib/site-packages/wx-2.8-msw-unicode/wx/gdiplus.dll'
                              ]
                    )]
## this is only needed if you don't want to install Side by Side (SxS)
## assemblies via the inno setup script, but prefer private assemblies:
## adjust the path to redistributables shared among your projects
#    my_data_files += [
#        ('', ['../shared/Microsoft.VC90.CRT/Microsoft.VC90.CRT.manifest',
#              '../shared/Microsoft.VC90.CRT/msvcp90.dll',
#              '../shared/Microsoft.VC90.CRT/msvcr90.dll'
#             ]
#        )]

my_console_opts = {
    "script": "molcalc.py",
    }

my_windows_opts = {
    "script": "wxMol.py",
    "icon_resources": [(1, "icons/benzol.ico")]
    }

my_excludes = [
    '_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
    'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
    'threading', 'Tkconstants', 'Tkinter', 'doctest',
    'subprocess'
    ]

## note the exclusion of msvcp90.dll to fix an error in py2exe
my_dll_excludes = [
    'libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
    'tk84.dll', 'msvcp90.dll'
    ]

setup(
    name='wxMol',
    version='0.85',
    description='Stoichiometric Calculator',
    long_description ='wrapper for eval() function '
        'that recognizes element symbols and '
        'formula notation',
    author='Ing. Hubert Hanghofer',
    author_email='hubert@netbeer.org',
    copyright='2010, Hubert Hanghofer',
    url='http://hubert.hanghofer.net/',
    license='GPL version 3',
    platforms=['any'],
    package_dir={'wxMol': ''},
    packages=['wxMol'],
    package_data={'wxMol': ['icons/*']},
    data_files=my_data_files,
    console=[my_console_opts],
    windows=[my_windows_opts],
    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "bundle_files": 1,
                          "excludes": my_excludes,
                          "dll_excludes": my_dll_excludes,
                          "dist_dir": "dist.w32",
                          "skip_archive": False,
                          "ascii": True,
                         }
               },
    requires=['wx'],
    zipfile = r'library.zip',
    )

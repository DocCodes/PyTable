#!/usr/bin/env python3
from distutils.core import setup

setup(
   name = 'PyTable',
   packages = ['table'],
   version = '0.1.25',
   description = 'A table module for python',
   author = 'Evan Young',
   url = 'https://github.com/DocCodes/PyTable',
   download_url = 'https://github.com/DocCodes/PyTable/archive/master.tar.gz',
   keywords = ['chart', 'table'],
   classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Steam User API',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Programming Language :: Python :: 3.6',
      'Natural Language :: English'
   ],
   install_requires = [
      'pytest'
   ],
   python_requires = '~=3.6'
)
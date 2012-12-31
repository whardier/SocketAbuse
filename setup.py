#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

import socketabuse

with open('README.md') as stream:
  long_desc = stream.read()

setup(
    name = socketabuse.__name__,
    version = socketabuse.__version__,
    author = socketabuse.__author__,
    author_email = socketabuse.__email__,
    packages = ['socketabuse'],
    url='https://github.com/whardier/SocketAbuse',
    license = socketabuse.__license__,
    description = socketabuse.__description__,
    long_description = long_desc,
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Communications',
    ],
    entry_points={
        'console_scripts': [
            'socketabuse = socketabuse.__main__:main',
        ],
    }
)



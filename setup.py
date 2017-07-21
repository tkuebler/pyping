#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
	name='pyping',
	version='0.0.6',
	description='A pure python ICMP ping implementation for python3 using raw sockets',
	long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.rst').read(),
	license=open("LICENSE").read(),
	author="Todd Kuebler",
	author_email="todd@kuebler.org",
	url='https://github.com/tkuebler/pyping',
	keywords="ping icmp network latency",
	packages = ['pyping'],
	scripts=["bin/pyping"]
)

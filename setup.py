#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup


# Package meta-data.
NAME = 'roman_numerals'
DESCRIPTION = 'Function to convert decimals to roman literals'
URL = 'https://github.com/imanhodjaev/roman_numerals'
EMAIL = 'sultan.imanhodjaev@gmail.com'
AUTHOR = 'Awesome Soul'

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
__version__ = '0.0.1'

setup(
    name=NAME,
    version='__version__',
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),

    py_modules=[NAME],

    entry_points={
         'console_scripts': ['roman_numerals=roman_numerals:main'],
    },

    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)

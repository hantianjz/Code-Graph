#!/usr/bin/bash

# Setup VENV

# Run pytests
python setup.py test

# Run pylint

# Build package
python setup.py build

# generate distribute wheel
python -m build

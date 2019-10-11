#!/bin/bash

virtualenv venv
source venv/bin/activate

python -m unittest test_strmatch.py

# File: _init_path.py 
# Author: Abinash Mohanty
# Date: 02/28/2017
# Arizona State University
# Adds the lib folder to python path 

import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = osp.dirname(__file__)

# Add lib to PYTHONPATH
lib_path = osp.join(this_dir)
add_path(lib_path)

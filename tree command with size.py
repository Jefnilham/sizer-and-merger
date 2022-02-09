# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:36:18 2022

@author: jefni
"""

import os
from os.path import getsize

for root, dirs, files in os.walk(r""):
    offset = len(root.split(os.path.sep))
    print("    " * (offset - 1), root, sep="|––––")
    
    file_by_size_bytes = []
    file_by_size_names = files
    for file in files:
        file_by_size_bytes.append(getsize(os.path.join(root, file)))        
        print("    " * offset, file, str(getsize(os.path.join(root, file))) + ' Bytes', sep="|––––")

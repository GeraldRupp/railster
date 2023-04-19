# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:04:37 2023

@author: ruppg
"""

import multiprocessing

def multiply_by_2(x):
    return x * 2

values = [1, 2, 3, 4, 5]
with multiprocessing.Pool() as pool:
    result = pool.map(multiply_by_2, values)
print(result)
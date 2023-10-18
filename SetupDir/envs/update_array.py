# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:46:48 2023

@author: Ritwik-Ghosh
"""

import numpy as np

def update_array(array, update_element):
    updated_array = np.append(array, update_element)
    updated_array = np.delete(updated_array, 0)
    
    return updated_array


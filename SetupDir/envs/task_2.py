# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 05:51:03 2023

@author: Ritwik-Ghosh
"""

'task_2: 1. advancing the time, 2. update Open price'

import numpy as np
from SetupDir.envs.update_array import update_array

def task_2(self):
    
    'Advance the time'
    'self.present_index_in_int is the current time index in int value'
    'The int index value is then advances by 1'
    'self.df.index[] get the datetime index value'
    self.present_index_in_int += 1   
    self.time = self.df.index[(self.present_index_in_int)]
    
    'Update the Open Price parameter in observation'
    self.open_price = update_array(self.open_price, self.df.loc[self.time, 'open'])
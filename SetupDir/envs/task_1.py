# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 04:46:26 2023

@author: Ritwik-Ghosh
"""

import random
from SetupDir.envs.update_array import update_array

''' task_1: update the following parameters, 1. Action Taken, 2. High Price
3. Low Price, 4. Volume, 5. Execution Price'''

def task_1(self):

    'Updating the action in observation space'
    self.action_taken = update_array(self.action_taken, self.action)
    
    'Updating the High Price parameter in observation'
    self.high_price = update_array(self.high_price, self.df.loc[self.time, 'high'])
    
    'Update the Low Price parameter in observation'
    self.low_price = update_array(self.low_price, self.df.loc[self.time, 'low'])
    
    'Updating the Close Price parameter in observation'
    self.close_price = update_array(self.close_price, self.df.loc[self.time, 'close'])

    'Updating the volume parameter in observation'
    self.volumes = update_array(self.volumes, self.df.loc[self.time, 'volume'])

    'Calculate the execution price'
    self.execution_price = random.uniform(self.low_price[-1], self.high_price[-1])
    
    #print('\n The execution price:', self.execution_price)
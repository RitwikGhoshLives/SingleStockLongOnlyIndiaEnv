# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:20:31 2023

@author: Ritwik-Ghosh
"""

from gym.envs.registration import register

# Register the environment
register(id='SingleStockLongOnlyIndiaEnv',
         entry_point='SetupDir.envs.env:Env')
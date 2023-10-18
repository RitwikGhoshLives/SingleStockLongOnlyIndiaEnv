# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 01:41:00 2023

@author: Ritwik-Ghosh
"""
import numpy as np

def update_observation(self):
    self.observation = [self.open_price,
                        self.high_price,
                        self.low_price,
                        self.close_price,
                        self.volumes,
                        self.money_reserve,
                        self.stock_holdings_in_num,
                        self.action_taken]
    
    self.observation = np.array(self.observation)
    
    return self.observation
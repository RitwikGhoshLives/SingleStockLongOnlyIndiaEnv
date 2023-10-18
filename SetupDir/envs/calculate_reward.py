# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 05:36:04 2023

@author: Ritwik-Ghosh
"""

def calculate_reward(self):
    
    self.reward = 0
    
    '1. At everystep the infletion create a negative reward.'
    self.reward = self.reward - self.negative_reward_per_step_by_inflation
    
    '2.Reward by the net worth groth'
    self.reward = self.reward + ((self.net_worth - self.old_net_worth)/self.initial_fund_in_money) 
        
    #print('Reward at the step:', self.reward)
    


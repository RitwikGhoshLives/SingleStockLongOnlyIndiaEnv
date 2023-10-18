# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:26:49 2023

@author: Ritwik-Ghosh
"""

import gym
from gym import spaces
import numpy as np
from SetupDir.envs.update_observation import update_observation
from SetupDir.envs.reset_all_parameters import reset_all_parameters
from SetupDir.envs.task_1 import task_1
from SetupDir.envs.execute_trading import execute_trading
from SetupDir.envs.calculate_reward import calculate_reward
from SetupDir.envs.task_2 import task_2

'Defining the class of the environmentas gym.Env'
class Env(gym.Env):
    
    def __init__(self, list_of_stock, data_dir, episode_length_in_steps,
                 time_stamp_in_min, look_back_window, initial_fund_in_money,
                 fee_percentage, max_fee, inflation_percentage_per_year, 
                 max_acceptable_drop_down_percentage_episode_stopping):
        
        'The list of stocks. At each episode one random stock is selected.'
        self.list_of_stock = list_of_stock
        'The directory where all the stocks data are kept'
        self.data_dir = data_dir
        'Length of one episode in number of steps'
        self.episode_length_in_steps = episode_length_in_steps
        'How many time steps (int) the agent looking back at every step.'
        self.look_back_window = look_back_window
        'The time frame or interval of the input dataframe e.g., 15 min, 5 min'
        self.time_stamp_in_min = time_stamp_in_min
        'Initial fund in money'
        self.initial_fund_in_money = initial_fund_in_money
        'The action is represented as a int in range of [-100,100].'
        self.action_space = spaces.Discrete(201, start=-100)
        '''The observation space have the following 8 parameters 1. Open prices,
        2. High prices 3. Low prices, 4. Close prices, 5. Volume, 6. Money reserve,
        7. Stock holding, 8. Action taken'''
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf,
                                            shape=(8,self.look_back_window),
                                            dtype=np.float64)
        'Trading fee'
        self.fee_percentage = fee_percentage
        self.max_fee = max_fee
        
        'Lowest acceptable net worth'
        self.lowest_acceptabl_net_worth = self.initial_fund_in_money * (1 - (max_acceptable_drop_down_percentage_episode_stopping/100))
        self.target_net_worth = 1.02 * self.initial_fund_in_money
        
        'Inflation percentage per year'
        self.inflation_percentage_per_year = inflation_percentage_per_year
        self.total_steps_per_year = (260*6*60)/self.time_stamp_in_min
        self.negative_reward_per_step_by_inflation = (self.inflation_percentage_per_year/100)/self.total_steps_per_year
        
        
    def reset(self):        
        # print('\nStarting a reset for a new episode...')
        
        'Reseting time and all the 8 parameters of the observation space'
        reset_all_parameters(self)
        
        'Creating the initial observation by combining all the arrays defined before'
        self.observation = update_observation(self)
        #print('\nObservation After Reset:\n', self.observation)
        
        'Initialize the "done" status as False'
        self.done = False        
        #print('\nDone Status after the reset:', self.done)
        
        #print('\nThe reset is completed')
        return self.observation
    
    
    def step(self, action):
        
        'Action taken by the agent'
        self.action = action
        #print('\nThe action, applied to the env by the agent:', self.action)
        
        ''' task_1: update the following parameters, 1. Action Taken, 2. High Price
        3. Low Price, 4. Volume. Also calculate Execution Price'''
        task_1(self)  
        ''' execute_trading: According to the action the update the money_reserve,
        stock_holdings. Also calculate net_worth_in_money '''
        execute_trading(self)
        
        ''' *** This is the instant when one time stamp just ends. At this instant all
        the parameter of the instant including the reward is available. However, the
        observation for next instant is not ready yet. But this instant is useful for 
        rendering.*** '''
        
        'Calculate the continuous inflation using Eular formula'
        self.old_net_worth = self.net_worth
        self.net_worth = self.money_reserve[-1] + (self.stock_holdings_in_num[-1] * self.close_price[-1])
        
        'Episode stopping criteria'
        if ((self.time>=self.end_time) or
            (self.net_worth <= self.lowest_acceptabl_net_worth)):
            #(self.money_reserve[-1] >= self.target_net_worth)):
            self.done = True # Ending the episode
            print('\nThe net Worth at the end of the episode:', self.net_worth)
            #print('\n The episode length was:', (self.present_index_in_int - self.start_time_index_in_int))
            
        'Calculate reward'
        calculate_reward(self)
            
        'task_2: 1. advancing the time, 2. update Open price'
        task_2(self)
        'Updating the Observation'
        self.observation = update_observation(self)
        'Need to explore more'
        info = {}
        
        #print('\nTime and done status at the end of the step:', self.time, self.done)
        #print('The updated observation at the end of the step:\n', self.observation)
        
        #print('self observation after the step', self.observation)
        return self.observation, self.reward, self.done, info
    

    def render(self, mode='human'):
        pass
    
    
    def close (self):
        pass
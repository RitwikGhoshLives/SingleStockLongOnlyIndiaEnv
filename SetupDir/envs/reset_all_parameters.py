# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 02:04:49 2023

@author: Ritwik-Ghosh
"""

import numpy as np
import pandas as pd
import random

def reset_all_parameters(self):
    
    'Select a stock from the list'
    selected_stock = random.choice(self.list_of_stock)    
    print('\nThe selected stock for the episode:', selected_stock)
    
    'Select the data frame from the dir'
    df = pd.read_csv(self.data_dir + '/' + selected_stock + '.csv', index_col=0)
    df.index = pd.to_datetime(df.index) # Ensuring the index is in datetime format
    self.df = df
    #print('\nThe dataframe containing historical data of the selected stock:\n', self.df)
    
    'End time of the episode'
    end_time_int_index_lower_bound = self.look_back_window + self.episode_length_in_steps + 1
    end_time_int_index_upper_bound = len(self.df)-1
    end_time_int_index = random.randint(end_time_int_index_lower_bound, end_time_int_index_upper_bound)
    self.end_time = self.df.index[end_time_int_index] # Index value of the last row of the data frame
    #print('\nThe End Time:', self.end_time)
    
    'Present time'
    present_time_int_index = end_time_int_index - self.episode_length_in_steps + 1
    self.start_time_index_in_int = present_time_int_index
    self.time = self.df.index[present_time_int_index]
    #print('\nTime current time after the reseet', self.time)
    
    'Present index value in int'
    self.present_index_in_int = self.df.index.get_loc(self.time)
    
    'Starting and ending index for resetting parameters, 1. Open Time'
    starting_int_index = present_time_int_index - self.look_back_window + 1
    starting_index = self.df.index[starting_int_index]
    ending_int_index = present_time_int_index
    ending_index = self.df.index[ending_int_index] 
    
    'Filling the array that stores open prices of last n time stamps at reset'
    self.open_price = self.df.loc[starting_index:ending_index, 'open'].values
    #print('\nThe open_prices array after the reset:', self.open_price)
    
    'Starting and ending time index for all parameters other than Open Price'
    starting_int_index = starting_int_index - 1
    starting_index = self.df.index[starting_int_index]    
    ending_int_index = ending_int_index - 1
    ending_index = self.df.index[ending_int_index]
        
    'Filling the array that stores all the parameters other than Open Prices'
    self.high_price = self.df.loc[starting_index:ending_index, 'high'].values
    self.low_price = self.df.loc[starting_index:ending_index, 'low'].values       
    self.close_price = self.df.loc[starting_index:ending_index, 'close'].values
    self.volumes = self.df.loc[starting_index:ending_index, 'volume'].values
    self.money_reserve = np.full((self.look_back_window,), self.initial_fund_in_money,dtype=np.float64)
    self.stock_holdings_in_num = np.full((self.look_back_window,), 0,dtype=np.float64)
    self.action_taken = np.full((self.look_back_window,), 0,dtype=np.int64)
    
    #print('\nThe high_prices array after the reset:', self.high_price)
    #print('\nThe low_prices array after the reset:', self.low_price)
    #print('\nThe close_prices array after the reset:', self.close_price)
    #print('\nThe volumes array after the reset:', self.volumes)
    #print('\nThe money_reserve array after the reset:', self.money_reserve)
    #print('\nThe action_taken array after the reset:', self.action_taken)
    
    'Initial Net Worth'
    self.net_worth = self.initial_fund_in_money
    
    
    'Avarage buy price'
    'n1, n2, n3 numbers of stock is bought at p1, p2, p3 price.'
    'The avarage price p_avg = (p1 + p2 + p3)/(n1 + n2 + n3)'
    'Now additional n4 stocks are bought at p4 price'
    'New avg price, p_avg_new = ((p_avg * (n1+n2+n3)) + p4) / (n1+n2+n3+n4)'
    self.avg_buy_price = 0 # initilize the price to 0
    #print('Average buy price after reset:', self.avg_buy_price)
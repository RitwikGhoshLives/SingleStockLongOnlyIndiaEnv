# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 05:20:53 2023

@author: Ritwik-Ghosh
"""

'This function execute trading according to the action taken by the agent'

from SetupDir.envs.update_array import update_array

def execute_trading(self):
    
    'Execute hold action'
    if (self.action==0):
        
        'The money_reserve remains the same'
        self.money_reserve = update_array(self.money_reserve, self.money_reserve[-1])
        
        'The stock_holdings remains the same'
        self.stock_holdings_in_num = update_array(self.stock_holdings_in_num, self.stock_holdings_in_num[-1])
        
        'No fee for holding'
        total_fee = 0
        

    'Execute buy operation'
    if (self.action > 0):
        
        'Target position'
        target_position_in_money = self.money_reserve[-1] * (1 - (self.fee_percentage/100)) * (self.action*0.01)
        #print('\nTarget position to buy in money:', target_position_in_money)
        
        'Calculate the stock quantity that can be bought'      
        stock_buy_in_quantity = target_position_in_money//self.execution_price        
        #print('\nActual stock quantity bought:', stock_buy_in_quantity)
        
        'Update the stock holdings'        
        new_stock_holdings_in_num = self.stock_holdings_in_num[-1] + stock_buy_in_quantity
        self.stock_holdings_in_num = update_array(self.stock_holdings_in_num, new_stock_holdings_in_num)
        
        'Actual money spent to buy the stocks'
        actual_money_spent = stock_buy_in_quantity * self.execution_price        
        #print('\nThe actual money spent to purchase stock:', actual_money_spent)
        
        'Trading Fee calculation'
        total_fee = actual_money_spent * (self.fee_percentage/100)
        total_fee = max(total_fee, self.max_fee)       
        #print('\nThe total fee to be paid', total_fee)
        
        'Update the money_reserve after the sell'
        new_money_in_reserve = self.money_reserve[-1] - actual_money_spent - total_fee
        self.money_reserve = update_array(self.money_reserve, new_money_in_reserve)
        
        'Update the average buy price'
        'n1, n2, n3 numbers of stock is bought at p1, p2, p3 price.'
        'The avarage price p_avg = (p1 + p2 + p3)/(n1 + n2 + n3)'
        'Now additional n4 stocks are bought at p4 price'
        'New avg price, p_avg_new = ((p_avg * (n1+n2+n3)) + p4) / (n1+n2+n3+n4)'
        total_money_spent_for_all_buy = (self.avg_buy_price * self.stock_holdings_in_num[-2]) + actual_money_spent
        self.avg_buy_price = total_money_spent_for_all_buy / self.stock_holdings_in_num[-1]
        
        #print('\nThe average buy price is:', self.avg_buy_price)
        

    'Execute sell operation'
    if (self.action < 0):
        
        'Calculate the stock quantity that can be sold'
        stock_sell_in_quantity = int(self.stock_holdings_in_num[-1] * (-self.action*0.01))
        #print('\nActual stock quantity to be sold', stock_sell_in_quantity)
        
        'Calculate the new stock holdings'        
        new_stock_holdings_in_num = self.stock_holdings_in_num[-1] - stock_sell_in_quantity
        
        'Update the new stock holdings in the self.stock_holdings_in_num array'
        self.stock_holdings_in_num = update_array(self.stock_holdings_in_num, new_stock_holdings_in_num)
        
        'Calculate the money earned by the sell'       
        money_earn = stock_sell_in_quantity * self.execution_price   
        #print('\nActual money earned in the stock selling:', money_earn)
        
        'Fee calculation'
        total_fee = money_earn * (self.fee_percentage/100)
        total_fee = max(total_fee, self.max_fee)
        #print('\nThe total fee to be paid', total_fee)
        
        'Update the money_reserve after the sell'
        new_money_in_reserve = self.money_reserve[-1] + money_earn - total_fee
        self.money_reserve = update_array(self.money_reserve, new_money_in_reserve)
        
    
    'Making the total_fee a global variable to use it in the reward calculation'
    self.total_fee = total_fee
    #print('\nStock holding before trade execution:', self.stock_holdings_in_num[-2])
    #print('\nStock holding after trade execution:', self.stock_holdings_in_num[-1])
        
        
    
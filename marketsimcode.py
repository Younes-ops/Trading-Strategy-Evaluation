""""""  		  	   		  	  			  		 			     			  	 
"""MC2-P1: Market simulator.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		  	  			  		 			     			  	 
All Rights Reserved  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Template code for CS 4646/7646  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  	  			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		  	  			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  	  			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  			  		 			     			  	 
or edited.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  	  			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		  	  			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  			  		 			     			  	 
GT honor code violation.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
-----do not edit anything above this line---  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Student Name: Younes EL BOUZEKRAOUI   		  	  			  		 			     			  	 
GT User ID: ybouzekraoui3   		  	   		  	  			  		 			     			  	 
GT ID: 903738099 			  	   		  	  			  		 			     			  	 
"""  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import datetime as dt  		  	   		  	  			  		 			     			  	 
import os  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import numpy as np  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import pandas as pd  		  	   		  	  			  		 			     			  	 
from util import get_data, plot_data  
 	   		  	  			  		 			     			  	 
  		  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
def compute_portvals(  		  	   		  	  			  		 			     			  	 
    orders,
    symbol, 		  	   		  	  			  		 			     			  	 
    start_val=100000,  		  	   		  	  			  		 			     			  	 
    commission=0,  		  	   		  	  			  		 			     			  	 
    impact=0
    ):  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    Computes the portfolio values.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
    :param orders: orders dataframe  		  	   		  	  			  		 			     			  	 
    :type orders: dataframe 		  	   		  	  			  		 			     			  	 
    :param start_val: The starting value of the portfolio  		  	   		  	  			  		 			     			  	 
    :type start_val: int  		  	   		  	  			  		 			     			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  	  			  		 			     			  	 
    :type commission: float  		  	   		  	  			  		 			     			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  	  			  		 			     			  	 
    :type impact: float  		  	   		  	  			  		 			     			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  	  			  		 			     			  	 
    :rtype: pandas.DataFrame  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
	  	   		  	  			  		 			     			  	 
    # extracting start date
    start_date = orders.index[0]
    # extracting end date 
    end_date = orders.index[-1]

    dates = pd.date_range(start_date, end_date)

    # getting prices data using get_data function from utils.py 
    prices = get_data([symbol], dates)
    prices = prices.drop(columns=['SPY'])
    # creating the a new column 'cash' and filling it with ones
    prices['cash']=np.ones(prices.shape[0])
    # print('prices : ',prices)

    trades=prices.copy()
    trades[:]=0

    # trades dataframe contains all the trades of each stock and also their equivalent change in cach for each day
    for index, row in orders.iterrows():
        if row.Shares > 0 :
            trades.loc[index,symbol] += row.Shares
            trades.loc[index,'cash'] += -(row.Shares * prices.loc[index,symbol]) * (1+impact) - commission
        if row.Shares < 0 :
            trades.loc[index,symbol] += row.Shares
            trades.loc[index,'cash'] += - (row.Shares * prices.loc[index,symbol]) * (1 - impact) - commission
            
    

    # holdings is a dataframe containing what the protfolio holds in each day
    holdings = trades.cumsum()
    holdings.cash += start_val
    # print('holdings :' ,holdings)
    # values is dataframe containing the equivalent values of the holdings in each day
    values = prices * holdings
    # print(values.iloc[250:300])
    # provals is just the sum of the porfolio value in each day
    portvals =pd.DataFrame(values.sum(axis=1),columns=['portval'])
    # print('portvals : ',portvals.iloc[200:270])
    return portvals  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 

def get_statistics(df):
    daily_returns = df.copy()
    daily_returns = (df / df.shift(1)) - 1
    daily_returns = daily_returns[1:]

    cr= (df.iloc[-1]/df.iloc[0]) -1
    adr=daily_returns.mean()
    sddr=daily_returns.std()

    sr=np.sqrt(252) * (daily_returns - 0).mean() / (daily_returns.std())

    return cr,adr,sddr,sr

def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3"
 		  	   		  	  			  		 			     			  	 	  	   		  	  			  		 			     			  	 



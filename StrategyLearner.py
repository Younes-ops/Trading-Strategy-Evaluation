""""""  		  	   		  	  			  		 			     			  	 
"""  		  	   		  	  			  		 			     			  	 
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
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
import random  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import pandas as pd  		  	   		  	  			  		 			     			  	 
import util as ut  	
from indicators import *	 
import QLearner as QL 	 
import marketsimcode   
import itertools
import time

  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
class StrategyLearner(object):  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  	  			  		 			     			  	 
        If verbose = False your code should not generate ANY output.  		  	   		  	  			  		 			     			  	 
    :type verbose: bool  		  	   		  	  			  		 			     			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		  	  			  		 			     			  	 
    :type impact: float  		  	   		  	  			  		 			     			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		  	  			  		 			     			  	 
    :type commission: float  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    # constructor  		  	   		  	  			  		 			     			  	 
    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Constructor method  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        self.verbose = verbose  		  	   		  	  			  		 			     			  	 
        self.impact = impact  		  	   		  	  			  		 			     			  	 
        self.commission = commission  		  	   		  	  			  		 			     			  	 
                                                      		     			  	 
    # this method should create a QLearner, and train it for trading  		  	   		  	  			  		 			     			  	 
    def add_evidence(  		  	   		  	  			  		 			     			  	 
        self,  		  	   		  	  			  		 			     			  	 
        symbol="IBM",  		  	   		  	  			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		  	  			  		 			     			  	 
        ed=dt.datetime(2009, 1, 1),  		  	   		  	  			  		 			     			  	 
        sv=10000,  	
        	  	   		  	  			  		 			     			  	 
    ):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Trains your strategy learner over a given time frame.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        :param symbol: The stock symbol to train on  		  	   		  	  			  		 			     			  	 
        :type symbol: str  		  	   		  	  			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  	  			  		 			     			  	 
        :type sd: datetime  		  	   		  	  			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  	  			  		 			     			  	 
        :type ed: datetime  		  	   		  	  			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		  	  			  		 			     			  	 
        :type sv: int  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        self.tradecount = 0

        dates = pd.date_range(sd, ed)  		  	   		  	  			  		 			     			  	 
        prices_all = ut.get_data([symbol], dates)  # automatically adds SPY  		  	   		  	  			  		 			     			  	 
        prices = prices_all[[symbol,]]  # only portfolio symbols  		  	   		  	  			  		 			     			  	 
        prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  
        trades=	prices.copy()	  
        trades_SPY=	prices.copy()	   		  	  			  		 			     			  	 
        trades.values[:, :] = 0  # set them all to nothing  	
        trades.columns=['Shares']	  	   	

        sma,sma_by_price = SMA([symbol],sd , ed, rolling_window = 20)
        upperBB,lowerBB,BBP = BollingerBands([symbol], sd, ed, rolling_window = 20)
        macd,macd_signal = MACD([symbol], sd , ed, rolling_window = 20)
        momentum = Momentum([symbol], sd , ed, days = 20)
        K_percent,D_percent=Stochastic_Oscillator([symbol], sd , ed)	




        steps = 10

        used_indicator1 = self.discretize( BBP , steps)
        used_indicator2 = self.discretize(sma_by_price, steps)
        used_indicator3 = self.discretize(momentum, steps)
        # used_indicator4 = self.discretize(momentum, steps)
        # used_indicator5 = self.discretize(K_percent, steps)

        # print(np.count_nonzero(np.isnan(used_indicator2)))

        self.learner = QL.QLearner(num_states=steps**3, \
        num_actions = 3, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.9, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False)

        daily_returns = prices.copy()
        daily_returns = (prices / prices.shift(1)) - 1
        daily_returns.iloc[0] = 0

        max_episodes=150
        for episode in range(max_episodes):
            previous_order = 0
            # print(np.count_nonzero(np.isnan(self.learner.Q)))
            for i in range(trades.shape[0]):
                state1 = used_indicator1[i][0]
                state2 = used_indicator2[i][0]
                state3 = used_indicator3[i][0]
                # state4 = used_indicator4[i][0]
                # state5 = used_indicator5[i][0]
                # state = state1 + (state2-1)*steps + (state3-1)*steps**2 + (state4-1)*steps**3 + (state5-1)*steps**4
                state = state1 + (state2-1)*steps  + (state3-1)*steps**2 
                reward_component = daily_returns.iloc[i][0] * previous_order
                reward = reward_component - self.impact*reward_component -self.commission
                
                action = self.learner.query(state,reward)

                if action == 2 :
                    trades.iloc[i] = 1000 - previous_order
                    previous_order = 1000
                elif action == 1 :
                    trades.iloc[i] = -1000 - previous_order
                    previous_order = -1000
                elif action == 0:
                    trades.iloc[i] = 0
                # print(self.learner.Q[state])  
        # print(np.nansum(self.learner.Q))             
            
                

        # print(self.learner.Q)
        return trades



  		  	   		  	  			  		 			     			  	 
    # this method should use the existing policy and test it against new data  		  	   		  	  			  		 			     			  	 
    def testPolicy(  		  	   		  	  			  		 			     			  	 
        self,  		  	   		  	  			  		 			     			  	 
        symbol="IBM",  		  	   		  	  			  		 			     			  	 
        sd=dt.datetime(2009, 1, 1),  		  	   		  	  			  		 			     			  	 
        ed=dt.datetime(2010, 1, 1),  		  	   		  	  			  		 			     			  	 
        sv=10000,  		  	   		  	  			  		 			     			  	 
    ):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Tests your learner using data outside of the training data  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        :param symbol: The stock symbol that you trained on on  		  	   		  	  			  		 			     			  	 
        :type symbol: str  		  	   		  	  			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  	  			  		 			     			  	 
        :type sd: datetime  		  	   		  	  			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  	  			  		 			     			  	 
        :type ed: datetime  		  	   		  	  			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		  	  			  		 			     			  	 
        :type sv: int  		  	   		  	  			  		 			     			  	 
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		  	  			  		 			     			  	 
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		  	  			  		 			     			  	 
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		  	  			  		 			     			  	 
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		  	  			  		 			     			  	 
        :rtype: pandas.DataFrame  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        dates = pd.date_range(sd, ed)  		  	   		  	  			  		 			     			  	 
        prices_all = ut.get_data([symbol], dates)  # automatically adds SPY  		  	   		  	  			  		 			     			  	 
        prices = prices_all[[symbol,]]  # only portfolio symbols  		  	   		  	  			  		 			     			  	 
        prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  
        trades=	prices.copy()	  
        trades_SPY=	prices.copy()	   		  	  			  		 			     			  	 
        trades.values[:, :] = 0  # set them all to nothing  	
        trades.columns=['Shares']	  	   	

        sma,sma_by_price = SMA([symbol],sd , ed, rolling_window = 20)
        upperBB,lowerBB,BBP = BollingerBands([symbol], sd, ed, rolling_window = 20)
        macd,macd_signal = MACD([symbol], sd , ed, rolling_window = 20)
        momentum = Momentum([symbol], sd , ed, days = 20)
        K_percent,D_percent=Stochastic_Oscillator([symbol], sd , ed)	


    



        steps = 10



        used_indicator = self.discretize( BBP , steps)

        used_indicator1 = self.discretize(BBP, steps)
        used_indicator2 = self.discretize(sma_by_price, steps)
        used_indicator3 = self.discretize(momentum, steps)
        # used_indicator4 = self.discretize(momentum, steps)
        # used_indicator5 = self.discretize(K_percent, steps)

        daily_returns = prices.copy()
        daily_returns = (prices / prices.shift(1)) - 1
        daily_returns = daily_returns  
        daily_returns.iloc[0]=0

        previous_order = 0
        # print(np.nansum(self.learner.Q))
        for i in range(trades.shape[0]-1):
            state1 = used_indicator1[i][0]
            state2 = used_indicator2[i][0]
            state3 = used_indicator3[i][0]
            # state4 = used_indicator4[i][0]
            # state5 = used_indicator5[i][0]
            # state = state1 + (state2-1)*steps + (state3-1)*steps**2 + (state4-1)*steps**3 + (state5-1)*steps**4
            state = state1 + (state2-1)*steps + (state3-1)*steps**2 
            action = self.learner.querysetstate(state)
            if action == 2 :
                trades.iloc[i] = 1000 - previous_order
                previous_order = 1000
            elif action == 1 :
                trades.iloc[i] = -1000 - previous_order
                previous_order = -1000
            elif action == 0:
                trades.iloc[i] = 0
            # print(action)

        

        return trades	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	
    def discretize(self,indicator, steps):
        stepsize = indicator.shape[0]/steps 
        sorted= indicator.sort_values(indicator.columns[0])
        thresholds=[]
        for i in range(0,steps-1):
            thresholds.append(sorted.iloc[int((i+1)*stepsize)][0])
        indicator_discretized = np.digitize(indicator,thresholds)
        return indicator_discretized      

def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3"

if __name__ == "__main__":  		
                         	  		 			     			  	 
    print("One does not simply think up a strategy")  	
    sd = dt.datetime(2010,1,1)
    ed = dt.datetime(2010,12,31)

    learner = StrategyLearner(impact=0.005)
    tmp = time.time() 
    learner.add_evidence('JPM',dt.datetime(2008,1,1),dt.datetime(2009,12,31),100000)
    train_t = time.time() - tmp 

    print('Train Time :' , train_t)
    q_trades = learner.testPolicy('JPM',sd,ed,100000)
    # manual_trades = testPolicy()
    holdings = q_trades.cumsum()
    # print(q_trades)
    

    Benchmark_orders = q_trades.copy()
    Benchmark_orders[:]=0
    Benchmark_orders.iloc[0]=1000

    Benchmark_port_vals = marketsimcode.compute_portvals(Benchmark_orders,'JPM',100000,0,0)
    q_port_vals = marketsimcode.compute_portvals(q_trades,'JPM',100000,0,0)
    # print('_________ Benchmark _________')
    # print(Benchmark_port_vals)
    # print('_________ Man Strat _________')
    # print(compute_portvals(manual_trades,100000,9.95,0.005))
    # print('_________ Q Learner _________')
    # print(q_port_vals)

    cr_bench,adr_bench,sddr_bench,sr_bench = marketsimcode.get_statistics(Benchmark_port_vals) 
    Benchmark_port_vals_normed=Benchmark_port_vals/Benchmark_port_vals.iloc[0,:]

    cr,adr,sddr,sr = marketsimcode.get_statistics(q_port_vals) 
    port_vals_normed=q_port_vals/q_port_vals.iloc[0,:]
    #sys.stdout = open("p6_results.txt", "w")
    print()
    print(f"Date Range: {sd} to {ed}") 
    print('--------------------------------------------------------------------------')	
    print('                               Q Learner             Benshmark       ')
    print('--------------------------------------------------------------------------')	  	   		  	  			  		 			     			  	   		  	   		  	  			  		 			     			  	 
    print(f"Sharpe Ratio                    {round(sr[0],6)}               {round(sr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')			  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
    print(f"Cumulative Return               {round(cr[0],6)}               {round(cr_bench[0],6)}")  		  	   		  	  			  		 			     			  	 
    print('--------------------------------------------------------------------------')		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
    print(f"Standard Deviation              {round(sddr[0],6)}               {round(sddr_bench[0],6)}")
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Average Daily Return            {round(adr[0],6)}                  {round(adr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Final Portfolio Value:          {round(q_port_vals.iloc[-1][0],6)}          {round(Benchmark_port_vals.iloc[-1][0],6)}")
    print('--------------------------------------------------------------------------')	
  	  	   		  	  			  		 			     			  	 
    df_temp = pd.concat(  		  	   		  	  			  		 			     			  	 
            [port_vals_normed, Benchmark_port_vals_normed], keys=["Portfolio", "Benchmark"], axis=1  		  	   		  	  			  		 			     			  	 
        )  		  	   		  	  			  		 			     			  	 
    ax = df_temp.plot(title="Strategy Learner vs Benchmark OUT OF SAMPLE ",color=['r','purple'], grid=True, fontsize=12)
    ax.legend(['Strategy Learner strategy','Benchmark strategy'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized daily portfolio value")
    fig = ax.get_figure()
    fig.savefig('images/Strategy_LearnervsBenchmark.png')
    plt.close()

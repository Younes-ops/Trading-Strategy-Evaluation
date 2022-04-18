import datetime as dt  		  	   		  	  			  		 			     			  	 
import random  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import pandas as pd  		  	   		  	  			  		 			     			  	 
import util as ut  
import marketsimcode
import sys
from indicators import *

class ManualStrategy(object):

    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Constructor method  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        self.verbose = verbose  		  	   		  	  			  		 			     			  	 
        self.impact = impact  		  	   		  	  			  		 			     			  	 
        self.commission = commission  


    def testPolicy(self,symbol='JPM', sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000) :
        


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

        previous_order=0
        for i in range(trades.shape[0]-1):
            # print((momentum.iloc[i] < -0.05) & (BBP.iloc[i] < 0.2))
            # print(D_percent.iloc[i][symbol])
            # if (D_percent.iloc[i][symbol] < 20)  :
            if (sma_by_price.iloc[i][symbol] > 1.05) & (BBP.iloc[i][symbol] < 0.2) & (momentum.iloc[i][symbol] < -0.05):
                trades.iloc[i] = 1000 - previous_order
                previous_order = 1000
            # elif (D_percent.iloc[i][symbol] > 80)  :
            elif (sma_by_price.iloc[i][symbol]< 0.95) & (BBP.iloc[i][symbol] > 0.8) & (momentum.iloc[i][symbol] > 0.05) :
                trades.iloc[i] = -1000 - previous_order
                previous_order = -1000
            else:
                trades.iloc[i] = 0
                # previous_order=0



        # trades.values[0, :] = 1000  # add a BUY at the start  		  	   		  	  			  		 			     			  	 
        # trades.values[2, :] = -1000  # add a SELL  		  	   		  	  			  		 			     			  	 
        # trades.values[41, :] = 1000  # add a BUY  		  	   		  	  			  		 			     			  	 
        # trades.values[60, :] = -2000  # go short from long  		  	   		  	  			  		 			     			  	 
        # trades.values[61, :] = 2000  # go long from short  		  	   		  	  			  		 			     			  	 
        # trades.values[-1, :] = -1000  # exit on the last day 



        return trades

def in_sample():
    sd=dt.datetime(2008, 1, 1)
    ed=dt.datetime(2009,12,31)
    sv = 100000
    manual_learner = ManualStrategy(impact=0.005,commission=9.95)
    trades=manual_learner.testPolicy('JPM',sd,ed,sv)
    # print(trades)
    port_vals=marketsimcode.compute_portvals(trades,symbol='JPM')
    cr,adr,sddr,sr = marketsimcode.get_statistics(port_vals) 



    port_vals_normed=port_vals/port_vals.iloc[0,:]

    Benchmark_trades = trades.copy()
    Benchmark_trades[:]=0
    Benchmark_trades.iloc[0]=1000
    Benchmark_port_vals=marketsimcode.compute_portvals(Benchmark_trades,symbol='JPM')
    cr_bench,adr_bench,sddr_bench,sr_bench = marketsimcode.get_statistics(Benchmark_port_vals) 

    Benchmark_port_vals_normed=Benchmark_port_vals/Benchmark_port_vals.iloc[0,:]
    #sys.stdout = open("p6_results.txt", "w")
    print()
    print(f"Date Range: {sd} to {ed}") 
    print('--------------------------------------------------------------------------')	
    print('                              Manual Strategy         Benshmark       ')
    print('--------------------------------------------------------------------------')	  	   		  	  			  		 			     			  	   		  	   		  	  			  		 			     			  	 
    print(f"Sharpe Ratio                    {round(sr[0],6)}               {round(sr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')			  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
    print(f"Cumulative Return               {round(cr[0],6)}                 {round(cr_bench[0],6)}")  		  	   		  	  			  		 			     			  	 
    print('--------------------------------------------------------------------------')		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
    print(f"Standard Deviation              {round(sddr[0],6)}               {round(sddr_bench[0],6)}")
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Average Daily Return            {round(adr[0],6)}               {round(adr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Final Portfolio Value:          {round(port_vals.iloc[-1][0],6)}               {round(Benchmark_port_vals.iloc[-1][0],6)}")
    print('--------------------------------------------------------------------------')		
    # print(port_vals.iloc[250:300])


    df_temp = pd.concat(  		  	   		  	  			  		 			     			  	 
            [port_vals_normed, Benchmark_port_vals_normed], keys=["Portfolio", "Benchmark"], axis=1  		  	   		  	  			  		 			     			  	 
        )  		  	   		  	  			  		 			     			  	 
    ax = df_temp.plot(title="Manual_Strategy vs Benchmark IN SAMPLE",color=['r','purple'], grid=True, fontsize=12)
    ax.legend(['Manual_Strategy','Benchmark strategy'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized daily portfolio value")



    for index, row in trades.iterrows():
        if trades.loc[index]['Shares'] > 0:
            ax.axvline(x=index, color='blue', linestyle='--',lw=0.8)
        elif trades.loc[index]['Shares'] < 0:
            ax.axvline(x=index, color='black', linestyle='--',lw=0.8)
    fig = ax.get_figure()
    fig.savefig('images/Manual_StrategyVsBenchmark_in_sample.png')
    plt.close()
    
def out_of_sample():
    sd=dt.datetime(2010, 1, 1)
    ed=dt.datetime(2010,12,31)
    sv = 100000
    manual_learner = ManualStrategy(impact=0.005,commission=9.95)
    trades=manual_learner.testPolicy('JPM',sd,ed,sv)
    # print(trades)
    port_vals=marketsimcode.compute_portvals(trades,symbol='JPM')
    cr,adr,sddr,sr = marketsimcode.get_statistics(port_vals) 



    port_vals_normed=port_vals/port_vals.iloc[0,:]

    Benchmark_trades = trades.copy()
    Benchmark_trades[:]=0
    Benchmark_trades.iloc[0]=1000
    Benchmark_port_vals=marketsimcode.compute_portvals(Benchmark_trades,symbol='JPM')
    cr_bench,adr_bench,sddr_bench,sr_bench = marketsimcode.get_statistics(Benchmark_port_vals) 

    Benchmark_port_vals_normed=Benchmark_port_vals/Benchmark_port_vals.iloc[0,:]
    #sys.stdout = open("p6_results.txt", "w")
    print()
    print(f"Date Range: {sd} to {ed}") 
    print('--------------------------------------------------------------------------')	
    print('                              Manual Strategy          Benshmark       ')
    print('--------------------------------------------------------------------------')	  	   		  	  			  		 			     			  	   		  	   		  	  			  		 			     			  	 
    print(f"Sharpe Ratio                    {round(sr[0],6)}               {round(sr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')			  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
    print(f"Cumulative Return               {round(cr[0],6)}                 {round(cr_bench[0],6)}")  		  	   		  	  			  		 			     			  	 
    print('--------------------------------------------------------------------------')		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
    print(f"Standard Deviation              {round(sddr[0],6)}               {round(sddr_bench[0],6)}")
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Average Daily Return            {round(adr[0],6)}               {round(adr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Final Portfolio Value:          {round(port_vals.iloc[-1][0],6)}               {round(Benchmark_port_vals.iloc[-1][0],6)}")
    print('--------------------------------------------------------------------------')		
    # print(port_vals.iloc[250:300])


    df_temp = pd.concat(  		  	   		  	  			  		 			     			  	 
            [port_vals_normed, Benchmark_port_vals_normed], keys=["Portfolio", "Benchmark"], axis=1  		  	   		  	  			  		 			     			  	 
        )  		  	   		  	  			  		 			     			  	 
    ax = df_temp.plot(title="Manual_Strategy vs Benchmark OUT OF SAMPLE ",color=['r','purple'], grid=True, fontsize=12)
    ax.legend(['Manual_Strategy','Benchmark strategy'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized daily portfolio value")



    for index, row in trades.iterrows():
        if trades.loc[index]['Shares'] > 0:
            ax.axvline(x=index, color='blue', linestyle='--',lw=0.8)
        elif trades.loc[index]['Shares'] < 0:
            ax.axvline(x=index, color='black', linestyle='--',lw=0.8)
    fig = ax.get_figure()
    fig.savefig('images/Manual_StrategyVsBenchmark_out_of_sample.png')
    plt.close()
    

def test_code(): 
    print('********************** Manual Strategy Vs Benshmark **********************')	
    print()
    print()
    print('********************** In sample **********************')
    in_sample()
    print()
    print()
    print('********************** Out of Sample **********************')
    out_of_sample()
    print()
    print()
    print('**************************************************************************')	
def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3"	
    
if __name__ == "__main__":  
    	  	   
    test_code()
    
  		  	   		  	  
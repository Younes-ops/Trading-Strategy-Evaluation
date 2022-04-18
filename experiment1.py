from pytz import common_timezones_set
import StrategyLearner
import ManualStrategy  
import datetime as dt 
import time
import marketsimcode
import pandas as pd
import matplotlib.pyplot as plt 
import sys	
import random

def run_in_sample():  

    print('********************** In Sample **********************')
    sd = dt.datetime(2008,1,1)
    ed = dt.datetime(2009,12,31)
    sv = 100000
    
    manual_learner = ManualStrategy.ManualStrategy(impact=0.005,commission=9.95)
    manual_trades=manual_learner.testPolicy('JPM',sd,ed,sv)

    q_learner = StrategyLearner.StrategyLearner(impact=0.005, commission=9.95)

    tmp = time.time() 
    q_learner.add_evidence('JPM',dt.datetime(2008,1,1),dt.datetime(2009,12,31),sv)
    train_t = time.time() - tmp 
    print('StrategyLearner Train Time :' , train_t)
    q_trades = q_learner.testPolicy('JPM',sd,ed,sv)
    


    

    Benchmark_orders = q_trades.copy()
    Benchmark_orders[:]=0
    Benchmark_orders.iloc[0]=1000

    
    Benchmark_port_vals = marketsimcode.compute_portvals(Benchmark_orders,'JPM',sv,9.95,0.005)
    q_port_vals = marketsimcode.compute_portvals(q_trades,'JPM',sv,9.95,0.005)
    manual_port_vals = marketsimcode.compute_portvals(manual_trades,'JPM',sv,9.95,0.005)


    cr_bench,adr_bench,sddr_bench,sr_bench = marketsimcode.get_statistics(Benchmark_port_vals) 
    Benchmark_port_vals_normed=Benchmark_port_vals/Benchmark_port_vals.iloc[0,:]


    q_cr,q_adr,q_sddr,q_sr = marketsimcode.get_statistics(q_port_vals) 
    q_port_vals_normed=q_port_vals/q_port_vals.iloc[0,:]

    manual_cr,manual_adr,manual_sddr,manual_sr = marketsimcode.get_statistics(manual_port_vals) 
    manual_port_vals_normed=manual_port_vals/manual_port_vals.iloc[0,:]

    #sys.stdout = open("p6_results.txt", "w")
    print()
    print(f" IN SAMPLE  Date Range: {sd} to {ed}") 
    print('------------------------------------------------------------------------------------------------------')	
    print('                               Q Learner             Benshmark                    Manual Strategy')
    print('------------------------------------------------------------------------------------------------------')	  	   		  	  			  		 			     			  	   		  	   		  	  			  		 			     			  	 
    print(f"Sharpe Ratio                    {'%08.6f'%q_sr[0]}               {'%08.6f'%sr_bench[0]}               {'%08.6f'%manual_sr[0]}") 
    print('------------------------------------------------------------------------------------------------------')			  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
    print(f"Cumulative Return               {'%08.6f'%q_cr[0]}               {'%08.6f'%cr_bench[0]}               {'%08.6f'%manual_cr[0]}")  		  	   		  	  			  		 			     			  	 
    print('------------------------------------------------------------------------------------------------------')		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
    print(f"Standard Deviation              {'%08.6f'%q_sddr[0]}               {'%08.6f'%sddr_bench[0]}               {'%08.6f'%manual_sddr[0]}")
    print('------------------------------------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Average Daily Return            {'%08.6f'%q_adr[0]}               {'%08.6f'%adr_bench[0]}               {'%08.6f'%manual_adr[0]}") 
    print('------------------------------------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Final Portfolio Value:          {'%09.2f'%q_port_vals.iloc[-1][0]}              {'%09.2f'%Benchmark_port_vals.iloc[-1][0]}              {'%09.2f'%manual_port_vals.iloc[-1][0]}")
    print('------------------------------------------------------------------------------------------------------')	
  	  	   		  	  			  		 			     			  	 
    df_temp = pd.concat(  		  	   		  	  			  		 			     			  	 
            [q_port_vals_normed,manual_port_vals_normed, Benchmark_port_vals_normed], keys=["Strategy Learner","Manual Strategy", "Benchmark"], axis=1  		  	   		  	  			  		 			     			  	 
        )  		  	   		  	  			  		 			     			  	 
    ax = df_temp.plot(title="Strategy Learner vs Manual Strategy vs Benchmark In Sample  ",color=['y','r','purple'], grid=True, fontsize=12)
    ax.legend(['Strategy Learner',"Manual Strategy",'Benchmark strategy'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized daily portfolio value")
    fig = ax.get_figure()
    fig.savefig('images/in_sample.png')
    plt.close()

def run_out_of_sample():  

    print('********************** Out Of Sample **********************')
    sd = dt.datetime(2010,1,1)
    ed = dt.datetime(2010,12,31)
    sv = 100000
    
    manual_learner = ManualStrategy.ManualStrategy(impact=0.005,commission=9.95)
    manual_trades=manual_learner.testPolicy('JPM',sd,ed,sv)

    q_learner = StrategyLearner.StrategyLearner(impact=0.005, commission=9.95)

    tmp = time.time() 
    q_learner.add_evidence('JPM',dt.datetime(2008,1,1),dt.datetime(2009,12,31),sv)
    train_t = time.time() - tmp 
    print('StrategyLearner Train Time :' , train_t)
    q_trades = q_learner.testPolicy('JPM',sd,ed,sv)
    


    

    Benchmark_orders = q_trades.copy()
    Benchmark_orders[:]=0
    Benchmark_orders.iloc[0]=1000

    
    Benchmark_port_vals = marketsimcode.compute_portvals(Benchmark_orders,'JPM',sv,9.95,0.005)
    q_port_vals = marketsimcode.compute_portvals(q_trades,'JPM',sv,9.95,0.005)
    manual_port_vals = marketsimcode.compute_portvals(manual_trades,'JPM',sv,9.95,0.005)


    cr_bench,adr_bench,sddr_bench,sr_bench = marketsimcode.get_statistics(Benchmark_port_vals) 
    Benchmark_port_vals_normed=Benchmark_port_vals/Benchmark_port_vals.iloc[0,:]


    q_cr,q_adr,q_sddr,q_sr = marketsimcode.get_statistics(q_port_vals) 
    q_port_vals_normed=q_port_vals/q_port_vals.iloc[0,:]

    manual_cr,manual_adr,manual_sddr,manual_sr = marketsimcode.get_statistics(manual_port_vals) 
    manual_port_vals_normed=manual_port_vals/manual_port_vals.iloc[0,:]

    #sys.stdout = open("p6_results.txt", "w")
    print()
    print(f" Out Of Sample  Date Range: {sd} to {ed}") 
    print('------------------------------------------------------------------------------------------------------')	
    print('                               Q Learner             Benshmark                    Manual Strategy')
    print('------------------------------------------------------------------------------------------------------')	  	   		  	  			  		 			     			  	   		  	   		  	  			  		 			     			  	 
    print(f"Sharpe Ratio                    {'%08.6f'%q_sr[0]}               {'%08.6f'%sr_bench[0]}               {'%08.6f'%manual_sr[0]}") 
    print('------------------------------------------------------------------------------------------------------')			  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
    print(f"Cumulative Return               {'%08.6f'%q_cr[0]}               {'%08.6f'%cr_bench[0]}               {'%08.6f'%manual_cr[0]}")  		  	   		  	  			  		 			     			  	 
    print('------------------------------------------------------------------------------------------------------')		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
    print(f"Standard Deviation              {'%08.6f'%q_sddr[0]}               {'%08.6f'%sddr_bench[0]}               {'%08.6f'%manual_sddr[0]}")
    print('------------------------------------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Average Daily Return            {'%08.6f'%q_adr[0]}               {'%08.6f'%adr_bench[0]}               {'%08.6f'%manual_adr[0]}") 
    print('------------------------------------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Final Portfolio Value:          {'%09.2f'%q_port_vals.iloc[-1][0]}              {'%09.2f'%Benchmark_port_vals.iloc[-1][0]}              {'%09.2f'%manual_port_vals.iloc[-1][0]}")
    print('------------------------------------------------------------------------------------------------------')	
  	  	   		  	  			  		 			     			  	 
    df_temp = pd.concat(  		  	   		  	  			  		 			     			  	 
            [q_port_vals_normed,manual_port_vals_normed, Benchmark_port_vals_normed], keys=["Strategy Learner","Manual Strategy", "Benchmark"], axis=1  		  	   		  	  			  		 			     			  	 
        )  		  	   		  	  			  		 			     			  	 
    ax = df_temp.plot(title="Strategy Learner vs Manual Strategy vs Benchmark In Sample  ",color=['y','r','purple'], grid=True, fontsize=12)
    ax.legend(['Strategy Learner',"Manual Strategy",'Benchmark strategy'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized daily portfolio value")
    fig = ax.get_figure()
    fig.savefig('images/out_of_sample.png')
    plt.close()



def test():
    random.seed(183278)
    print()
    print()
    print('********************** Starting Experiment 1 **********************')     
    run_in_sample()
    print()
    run_out_of_sample()
    print('********************** End of Experiment 1 **********************')
    print()
    print()

def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3"

if __name__ == "__main__":
    test()

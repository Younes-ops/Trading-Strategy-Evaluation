from pytz import common_timezones_set
import StrategyLearner
import ManualStrategy  
import datetime as dt 
import time
import marketsimcode
import pandas as pd
import matplotlib.pyplot as plt 	

def run_experiment():  

    
    sd = dt.datetime(2008,1,1)
    ed = dt.datetime(2009,12,31)
    sv = 100000

    # Strategy Learner - impact = 0.0005
    qlearner = StrategyLearner.StrategyLearner(verbose = False, impact=0.0005)
    qlearner.add_evidence(symbol="JPM",sd=dt.datetime(2008,1,1),ed=dt.datetime(2009,12,31),sv=100000)
    q_trades = qlearner.testPolicy(symbol="JPM",sd=dt.datetime(2008,1,1),ed=dt.datetime(2009,12,31),sv=100000)
    q_port_vals1 = marketsimcode.compute_portvals(q_trades,'JPM',sv,0,0.0005)
    q_port_vals_normed1=q_port_vals1/q_port_vals1.iloc[0,:]


    # Strategy Learner - impact = 0.005
    qlearner = StrategyLearner.StrategyLearner(verbose = False, impact=0.005)
    qlearner.add_evidence(symbol="JPM",sd=dt.datetime(2008,1,1),ed=dt.datetime(2009,12,31),sv=100000)
    q_trades = qlearner.testPolicy(symbol="JPM",sd=dt.datetime(2008,1,1),ed=dt.datetime(2009,12,31),sv=100000)
    q_port_vals2 = marketsimcode.compute_portvals(q_trades,'JPM',sv,0,0.005)
    q_port_vals_normed2=q_port_vals2/q_port_vals2.iloc[0,:]

    # Strategy Learner - impact = 0.05
    qlearner = StrategyLearner.StrategyLearner(verbose = False, impact=0.05)
    qlearner.add_evidence(symbol="JPM",sd=dt.datetime(2008,1,1),ed=dt.datetime(2009,12,31),sv=100000)
    q_trades = qlearner.testPolicy(symbol="JPM",sd=dt.datetime(2008,1,1),ed=dt.datetime(2009,12,31),sv=100000)
    q_port_vals3 = marketsimcode.compute_portvals(q_trades,'JPM',sv,0,0.05)
    q_port_vals_normed3=q_port_vals3/q_port_vals3.iloc[0,:]


    
    


    

    # Benchmark_orders = q_trades.copy()
    # Benchmark_orders[:]=0
    # Benchmark_orders.iloc[0]=1000

    
    # Benchmark_port_vals = marketsimcode.compute_portvals(Benchmark_orders,'JPM',sv,9.95,0.005)
    # q_port_vals = marketsimcode.compute_portvals(q_trades,'JPM',sv,9.95,0.005)
    # manual_port_vals = marketsimcode.compute_portvals(manual_trades,'JPM',sv,9.95,0.005)


    q_cr1,q_adr1,q_sddr1,q_sr1 = marketsimcode.get_statistics(q_port_vals1) 
    q_port_vals_normed1=q_port_vals1/q_port_vals1.iloc[0,:]

    q_cr2,q_adr2,q_sddr2,q_sr2 = marketsimcode.get_statistics(q_port_vals2) 
    q_port_vals_normed2=q_port_vals2/q_port_vals2.iloc[0,:]

    q_cr3, q_adr3,q_sddr3,q_sr3 = marketsimcode.get_statistics(q_port_vals3) 
    q_port_vals_normed3=q_port_vals3/q_port_vals3.iloc[0,:]

  
    #sys.stdout = open("p6_results.txt", "w")
    print()
    print(f" IN SAMPLE  Date Range: {sd} to {ed}") 
    print('------------------------------------------------------------------------------------------------------')	
    print(' Startegy Learner Impact         0.0005             0.005                    0.05')
    print('------------------------------------------------------------------------------------------------------')	  	   		  	  			  		 			     			  	   		  	   		  	  			  		 			     			  	 
    print(f"Sharpe Ratio                    {'%08.6f'%q_sr1[0]}               {'%08.6f'%q_sr2[0]}               {'%08.6f'%q_sr3[0]}") 
    print('------------------------------------------------------------------------------------------------------')			  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
    print(f"Cumulative Return               {'%08.6f'%q_cr1[0]}               {'%08.6f'%q_cr2[0]}               {'%08.6f'%q_cr3[0]}")  		  	   		  	  			  		 			     			  	 
    print('------------------------------------------------------------------------------------------------------')		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
    print(f"Standard Deviation              {'%08.6f'%q_sddr1[0]}               {'%08.6f'%q_sddr2[0]}               {'%08.6f'%q_sddr3[0]}")
    print('------------------------------------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Average Daily Return            {'%08.6f'%q_adr1[0]}               {'%08.6f'%q_adr2[0]}               {'%08.6f'%q_adr3[0]}") 
    print('------------------------------------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Final Portfolio Value:          {'%09.2f'%q_port_vals1.iloc[-1][0]}              {'%09.2f'%q_port_vals2.iloc[-1][0]}              {'%09.2f'%q_port_vals3.iloc[-1][0]}")
    print('------------------------------------------------------------------------------------------------------')	
  	  	   		  	  			  		 			     			  	 
    df_temp = pd.concat(  		  	   		  	  			  		 			     			  	 
            [q_port_vals_normed1,q_port_vals_normed2, q_port_vals_normed3], keys=["Strategy Learner","Manual Strategy", "Benchmark"], axis=1  		  	   		  	  			  		 			     			  	 
        )  		  	   		  	  			  		 			     			  	 
    ax = df_temp.plot(title="Strategy Learner vs Impact  ",color=['y','r','purple'], grid=True, fontsize=12)
    ax.legend(['Impact = 0.0005',"Impact = 0.005",'Impact = 0.05'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized daily portfolio value")
    fig = ax.get_figure()
    fig.savefig('images/impact.png')
    plt.close()
    

def test():
    print()
    print()
    print('********************** Starting Experiment 2 **********************')
    run_experiment()
    print('********************** End of Experiment 2 **********************')
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

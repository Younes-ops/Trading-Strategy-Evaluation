import StrategyLearner
import ManualStrategy  
import datetime as dt 
import time
import marketsimcode
import pandas as pd
import matplotlib.pyplot as plt 
import sys	
import random
import experiment1
import experiment2
import os


def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3"

if __name__ == "__main__":  
    isExist = os.path.exists('images')
    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs('images')	

    random.seed(183278)
    sys.stdout = open("p8_results.txt", "w")
    experiment1.test()
    experiment2.test()
    ManualStrategy.test_code()
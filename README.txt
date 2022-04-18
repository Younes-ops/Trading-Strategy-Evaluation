# Project 8: Strategy Evaluation

#### Author: Younes EL BOUZEKRAOUI

#### Author Email: ybouzekraoui3@gatech.edu


### Instruction :
To run the code reproduce the results and the figures:

-Put all the files in the same directory.

-Only run the file testproject.py on the ML4T environement using : PYTHONPATH=../:. python testproject.py 

When you run this file it will create a directory 'images' it it does not already exist and where all the chart will be stored
It will create also  a file p8_results.txt where all the results will be printed.
No other file needs to be run , the file testproject.py calls all the other files run all the experiments, save the figures in /images and print the results in p8_results.txt

#### Note that it might take few minutes to run and  get the results

### Repository Structure:



```
|-- indicators.py
|-- experiment1.py
|-- experiment2.py
|-- ManualStrategy.py
|-- marketsimcode.py
|-- QLearner.py
|-- StrategyLearner.py
|-- testproject.py
|-- README.txt
```


### Files Description:

```
|-- indicators.py : Contains the implementation of each indicator we used in this project and the project 6

|-- experiment1.py : Contains a function test() that run the experiment 1 saves the figures in the folder images and print the statitics table in p8_results.txt

|-- experiment2.py : Contains also a function test() that run the experiment 2 saves the figures in the folder images and print the statitics table in p8_results.txt
|-- ManualStrategy.py : Contain the code implementation of the Manual strategy with the function testPolicy , it contains also a function test_code() that runs in sample and out of sample comparizon between the benchmark and the Manual Strategy, the figures are saved in /images and the statistics tables are printed in p8_results.txt .
|-- marketsimcode.py : Contains the necessary function the simulate a market : Computeportvals() get_statistics() ..
|-- QLearner.py : The Q Learning that we implemented in a previous project 
|-- StrategyLearner.py : A Strategy Learner that uses the Q Learner, the function add_evidence() trains the model and testPolicy() that tests the model
|-- testproject.pdf : This is the main entry for this project , it calls all the other files run all the experiment, save the figures in /images and print the results in p8_results.txt


```



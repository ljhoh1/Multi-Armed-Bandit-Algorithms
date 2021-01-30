# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:49:14 2021

@author: ljhoh
"""
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def reward(mu, sd):
    '''
    generate reward from a Gaussian dist.
    
    Inputs: 
        - mu (float) = the mean of normal
        - sd (float) = the sd of normal
    Output:
        - reward (float) = random sample from normal
    '''
    rng = np.random.default_rng()
    reward = rng.normal(mu, sd)
    
    return reward

#def eval():
    

def eval_select(narms, steps, means, egreed = 0):
    '''
    Find the q function, and choose an action (arm to pull) sample from.
    
    Inputs: 
        - narms (int) = number of arms
        - steps (int) = the number of steps performed
    Outputs: 
        - arms (list) = final value estimate for each arm
        - selection (list) = for each step, the chosen action is appended 
    '''
    rng = np.random.default_rng()
    arms = [0] * narms  
    
    selection = [0] * narms
        
           
    for step in range(1, steps):
        # generate uniform variable for egreedy            
        u = rng.uniform(0, 1) 
       
        if u > egreed:  
            maxRew = max(arms)
            ids = [i for i, j in enumerate(arms) if j == maxRew]
            if len(ids) > 1:
                id = rng.choice(ids)
            
            else:
                id = ids[0]               
            
        elif u <= egreed:               
            arm_option = np.arange(10)
            id = rng.choice(arm_option)
          
          
        old = arms[id]            
        selection[id] += 1         
        rew =  reward(means[id], 1)
        arms[id] = old + 1/selection[id] * (rew - old)
    
    return arms, selection

means = np.arange(10)
est, sel = eval_select(narms = 10, means = means, steps = 100_000, egreed = 0.1)


x = np.arange(len(sel))
plt.bar(x, sel)

sns.lineplot(x, sel)

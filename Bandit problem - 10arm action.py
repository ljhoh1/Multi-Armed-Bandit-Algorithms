# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:49:14 2021

@author: ljhoh
"""
import numpy as np
import seaborn as sns

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

def eval():
    

def eval_select(narms, steps):
    '''
    Find the q function, and choose an action
    '''
    rng = np.random.default_rng()
    arms = [0] * narms
    
    for arm in range(len(arms)):
        arms[arm] = reward(5, 1)
    
    selection = []
    
    for step in range(1, steps):
        
        id = arms.index(max(arms))
        old = arms[id]
        
        selection.append(id)
        
        reward =  reward(5, 1)
        arms[id] = old + 1/step * (reward - old)
    
    return arms, selection


est, sel = eval_select(narms = 10, steps = 10000)

sns.histplot(sel)

selection = []
selection.append(7)

for arm in range(len(arms)):
        arms[arm] = rng.normal(5, 1)
        
id = arms.index(max(arms))

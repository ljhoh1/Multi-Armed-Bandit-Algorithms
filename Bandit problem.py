# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:57:56 2021

@author: ljhoh
"""

import numpy as np
import seaborn as sns

def generate_arm(steps):
    '''
    
    '''
    
    rng = np.random.default_rng()
    values = np.zeros(steps)
    ests = np.zeros(steps)
    
    values[0] = rng.normal(5, 1)
    ests[0] 
    
    for step in range(1, steps):
        
        #inc = rng.normal(0, 0.01)
        reward =  rng.normal(5, 1)
        
        qfun = ests[step-1] + 1/step * (reward - ests[step - 1])
        ests[step] = qfun
        
        #value = values[step-1]+inc
        if np.abs(ests[step] - ests[step - 1]) < np.exp(-10):
            break
        
        #values[step] = value
    
    return values, ests

arm1 = generate_arm(10000)

xseq = np.arange(10000)
sns.lineplot(xseq, arm1)


def estimate():
    '''
    Find the q function, and choose an action
    '''
    
    
    
    rng = np.random.default_rng()
    ests = rng.normal(5, 1)
    n = 0
    old = -100
    #values[0] = rng.normal(5, 1)
    #ests[0] 
    
    while np.abs(ests - old) > 0.001:
        
        
        
        n += 1
        
        reward =  rng.normal(5, 1)
        old = ests
        
        ests = old + 1/n * (reward - old)
        
        
    
    return ests, n


est, n = estimate()


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:49:14 2021

@author: ljhoh
"""

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
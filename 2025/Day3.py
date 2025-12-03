# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 08:44:08 2025

@author: marco
"""

#%% Intro

import numpy as np

with open('Day3.txt','r') as f:
    data = f.read().splitlines()
    
#%% Part 1 & 2

def findNum(d,n):
    num = []
    idx = 0
    N = len(d)
    for i in range(n):
        idx += np.argmax(d[idx:N-(n-i)+1]) 
        num.append(d[idx])
        idx += 1
    return sum([num[i]*10**(n-i-1) for i in range(n)])

data = [[int(i) for i in d] for d in data]

sol1 = sum([findNum(d, 2) for d in data])
sol2 = sum([findNum(d, 12) for d in data])

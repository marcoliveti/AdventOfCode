# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 08:44:35 2025

@author: marco
"""

#%% Intro

import numpy as np

with open('Day2.txt', 'r') as f:
    data = f.read().split(',')
    
data = [[int(d.split('-')[0]), int(d.split('-')[1])] for d in data]

#%% Part 1

sol1 = 0

for d in data:
    power = np.ceil(len(str(d[0]))/2) 
    num = 10**power + 1        
    mul = np.arange(max(np.ceil(d[0]/num),10**(power-1)), min(10**(power)-1, np.floor(d[1]/num))+1)
    sol1 += int(sum(num*mul))

#%% Part 2

def findMuls(d, p):
    muls = set()
    if p > 1:
        for n in range(1,p):
            if p%n == 0:
                num = sum([10**k for k in range(0,p,n)])
                muls.update(list(num*np.arange(int(np.ceil(d[0]/num)), int(np.floor(d[1]/num)+1))))
    return int(sum(muls))

sol2 = 0

for d in data:
    power = [int(len(str(d[0]))), int(len(str(d[1])))]
    if power[0] == power[1]:
        sol2 += findMuls(d,power[0])
    else:
        sol2 += findMuls((d[0], 10**power[0]-1),power[0]) + findMuls((10**power[0], d[1]), power[1])

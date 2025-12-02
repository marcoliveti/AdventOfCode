# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 07:21:07 2025

@author: marco
"""

#%% Intro

with open('Day1.txt','r') as f:
    data = f.read().splitlines()

#%% Part 1 & 2

inst = [int(d[1:]) if d[0] == 'R' else -int(d[1:]) for d in data]
steps = [50]
passes = []
for i in inst:
    s = steps[-1] + i
    if steps[-1] > 0 and s <= 0:
        p = 1
    else:
        p = 0
    p += int(abs(s)/100) 
    steps.append(s%100)
    passes.append(p)
    
sol1 = steps.count(0)
sol2 = sum(passes)


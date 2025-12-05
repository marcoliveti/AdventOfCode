# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 08:40:48 2025

@author: marco
"""

#%% Intro

with open('Day5.txt','r') as f:
    data = f.read().splitlines()
    
rngs = sorted([(int(i.split('-')[0]),int(i.split('-')[1])) for i in data[:data.index('')]], key = lambda x: x[0]) 
ids = [int(i) for i in data[data.index('')+1:]]

#%% Part 1

sol1 = 0
for i in ids:
    for r in rngs:
        if r[0] <= i <= r[1]:
            sol1 += 1
            break

#%% Part 2

i = 0
while i < len(rngs)-1:
    if rngs[i+1][0] > rngs[i][1]:
        i += 1
    elif rngs[i+1][0] <= rngs[i][1] <= rngs[i+1][1]:
        rngs[i] = (rngs[i][0],rngs[i+1][1])
        del rngs[i+1]
    elif  rngs[i][1] > rngs[i+1][1]:
        del rngs[i+1]

sol2 = sum([i[1]-i[0]+1 for i in rngs])    
    
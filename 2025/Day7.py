# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 10:10:41 2025

@author: marco
"""

#%% Intro

import numpy as np

with open('Day7.txt','r') as f:
    data = [list(i) for i in f.read().split()]

#%% Part 1

pos = [{data[0].index('S')}]
sol1 = 0
for i,d in enumerate(data[1:]):
    if '^' not in d:
        pos.append(pos[i])
    else:
        idx = [i for i, val in enumerate(d) if val == '^']
        newPos = set()
        for p in pos[i-1]:
            if p in idx:
                newPos.update([p-1,p+1])
                sol1 += 1
            else:
                newPos.update([p])
        pos.append(newPos)

#%% Part 2

data = np.array(data)
countPart = np.zeros((len(data),len(data[0])))
countPart[data == 'S'] = 1
for i in range(1,data.shape[1]):
    if '^' not in data[i]:
        countPart[i] += countPart[i-1]
    else:
        idxMf = np.argwhere(data[i] == '^')
        countPart[i] += countPart[i-1]
        countPart[i,idxMf-1] += countPart[i,idxMf]
        countPart[i,idxMf+1] += countPart[i,idxMf]
        countPart[i,idxMf] = 0
sol2 = int(sum(countPart[-2]))     

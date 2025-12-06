# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 09:48:03 2025

@author: marco
"""

#%% Intro

import numpy as np

with open('Day6.txt','r') as f:
    data = f.read().splitlines()

#%% Part 1

prob = [d.split() for d in data]
prob[:-1] = [[int(i) for i in d] for d in prob[:-1]]
prob = [[d[i] for d in prob] for i in range(len(prob[0]))]
sol1 = int(sum([sum(d[:-1]) if d[-1] == '+' else np.prod(d[:-1]) for d in prob]))

#%% Part 2

num = []
oper = data[-1].split()
sol2 = 0
for i in range(len(data[0])-1,-1,-1):
    temp = ''.join([d[i] for d in data[:-1]])
    if temp.isspace() or i == 0:
        if i == 0:
            num.append(int(temp))
        if oper[-1] == '+':
            sol2 += sum(num)
        else:
            sol2 += int(np.prod(num))
        num = []
        oper.pop()
    else:
        num.append(int(temp))

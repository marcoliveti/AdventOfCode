# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 12:23:57 2025

@author: marco
"""

#%% Intro

import numpy as np
from itertools import combinations_with_replacement

with open('Day10.txt', 'r') as f:
    data = f.read().splitlines()

#%% Part 1

pattern = [d.split(' ')[0][1:-1] for d in data]
pattern = [np.array([0 if i == '.' else 1 for i in p]) for p in pattern]

inst = []
for i,d in enumerate(data):
    temp = d.split(' ')[1:-1]
    inst.append([np.array([1 if str(n) in t else 0 for n in range(len(pattern[i]))]) for t in temp])

sol1 = 0
for i,p in enumerate(pattern):
    presses = 1
    sent = False
    while not sent:
        comb = combinations_with_replacement(range(len(inst[i])), presses)
        for c in comb:
            test = np.sum(np.array([inst[i][k] for k in c]),axis = 0)%2
            if (test == pattern[i]).all():
                sol1 += presses
                sent = True
                break
        if not sent:
            presses += 1

#%% Part 2

joltage = [d.split(' ')[-1][1:-1] for d in data]
joltage = [[int(i) for i in p.split(',')] for p in joltage]

from scipy.optimize import milp
from scipy.optimize import LinearConstraint

sol2 = 0
for i,d in enumerate(data):
    temp = d.split(' ')[1:-1]
    buttons = [np.array([int(i) for i in t[1:-1].split(',')]) for t in temp]
    buttons = [np.array([1 if n in b else 0 for n in range(len(joltage[i]))]) for b in buttons]
    
    c = np.ones(len(buttons))
    A = np.array(buttons).T
    b_u = np.array(joltage[i])
    b_l = b_u

    constraints = LinearConstraint(A, b_l, b_u)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraints, integrality=integrality)
    sol2 += int(sum(res.x))




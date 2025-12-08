# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 20:35:17 2025

@author: marco
"""

#%% Intro 

import numpy as np

with open('Day8.txt','r') as f:
    data = [np.array([int(k) for k in i.split(',')]) for i in f.read().splitlines()]

#%% Part 1

def junction():
    idx = np.unravel_index(dist.argmin(), dist.shape)
    dist[idx[0],idx[1]] = 1e9
    dist[idx[1],idx[0]] = 1e9
    j1 = data[idx[0]]
    j2 = data[idx[1]]
    idxC1, idxC2 = -1, -1
    for i,c in enumerate(circuits):
        if j1 in c:
            idxC1 = i
        if j2 in c:
            idxC2 = i
    if idxC1 == -1 and idxC2 == -1:
        circuits.append(set([j1,j2]))
    elif idxC2 == -1:
        circuits[idxC1].update([j2])
    elif idxC1 == -1:
        circuits[idxC2].update([j1])
    elif idxC1 != idxC2:
        circuits[idxC1].update(circuits[idxC2])
        circuits.pop(idxC2)
    return j1,j2

dist = np.zeros((len(data),len(data)))
for i,d in enumerate(data):
    dist[i] = [np.linalg.norm(d-f) for f in data]
dist[np.diag_indices_from(dist)] = 1e9
data = [tuple([int(n) for n in i]) for i in data]

circuits = []
for connection in range(10):
    junction()
    
sol1 = np.prod(sorted([len(c) for c in circuits])[-3:])    

#%% Part 2

while len(circuits[0]) < len(data):
    j1,j2 = junction()

sol2 = j1[0] * j2[0]

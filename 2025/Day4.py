# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 08:07:41 2025

@author: marco
"""

#%% Intro

import numpy as np

with open('Day4.txt','r') as f:
    data = np.array([list(i) for i in f.read().splitlines()])
    
#%% Part 1

data = np.vstack((np.array(['.']*len(data)), data, np.array(['.']*len(data))))
data = np.hstack((np.atleast_2d(np.array(['.']*data.shape[0])).T, data, 
                  np.atleast_2d(np.array(['.']*data.shape[0])).T))

idxRolls = np.argwhere(data == '@')
sol1 = 0
for i in idxRolls:
    if np.sum(data[i[0]-1:i[0]+2,i[1]-1:i[1]+2] == '@') <= 4:
        sol1 += 1

#%% Part 2

sent = True
newData = np.copy(data)
sol2 = np.sum(newData == '@')
while sent:
    sent = False
    idxRolls = np.argwhere(data == '@')
    for i in idxRolls:
        if np.sum(data[i[0]-1:i[0]+2,i[1]-1:i[1]+2] == '@') <= 4:
            newData[i[0],i[1]] = '.'
            sent = True
    data = np.copy(newData)
sol2 -= np.sum(newData == '@')

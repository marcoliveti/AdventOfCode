# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:32:51 2025

@author: marco
"""

#%% Intro

import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

start = perf_counter()
with open('Day9.txt', 'r') as f:
    data = [np.array([int(i) for i in d.split(',')]) for d in f.read().splitlines()]
    
#%% Part 1

rect = []
idx = []
for i in range(len(data)):
    rect += [(abs(data[i][0]-data[k][0])+1) * (abs(data[i][1]-data[k][1])+1) for k in range(i,len(data))]
    idx += [(i,k) for k in range(i,len(data))]
sol1 = int(max(rect))

#%% Part 2

plt.close('all')
fig, ax = plt.subplots(num = 'Tiles')
for d in range(len(data)-1):
    plt.plot([data[d][0],data[d+1][0]],[data[d][1],data[d+1][1]],'k')
    plt.axis('equal')

from copy import copy 

temp = np.array(data)
ysort = temp[np.lexsort((temp[:,0],temp[:,1]))]
yvalid = [[ysort[0,1], [(ysort[0,0], ysort[1,0])]]]
for i in range(2,len(ysort),2):
    y = ysort[i,1]
    rngs = copy(yvalid[-1][1])
    n0,n1 = ysort[i,0], ysort[i+1,0]
    sent = False
    k = 0
    while k < len(rngs) and sent == False:
        sent = True
        if n0 == rngs[k][0] and n1 == rngs[k][1]:
            y += 1
            del rngs[k]
        elif n0 == rngs[k][1]:
            rngs[k] = (rngs[k][0], n1)
            if k < (len(rngs)-1) and n1 == rngs[k+1][0]:
                rngs[k] = (rngs[k][0], rngs[k+1][1])
                del rngs[k+1]
        elif n1 == rngs[k][0]:
            rngs[k] = (n0, rngs[k][1])
        elif n0 == rngs[k][0]:
            rngs[k] = (n1, rngs[k][1])
            y += 1
        elif n1 == rngs[k][1]:
            rngs[k] = (rngs[k][0], n0)
            y += 1
        elif rngs[k][0] < n0 < n1 < rngs[k][1]:
            rngs.append((n1,rngs[k][1]))
            rngs[k] = (rngs[k][0], n0)
        else:
            sent = False
            k += 1
    if sent == False:
        rngs.append((n0,n1))
    yvalid.append([y,sorted(rngs)]) 

for y in yvalid:
    for r in y[1]:
        plt.plot([r[0],r[1]], [y[0],y[0]], 'r-x', lw = 0.2)

temp = np.array(data)
xsort = temp[np.lexsort((temp[:,1],temp[:,0]))]
xvalid = [[xsort[0,0], [(xsort[0,1], xsort[1,1])]]]
for i in range(2,len(xsort),2):
    x = xsort[i,0]
    rngs = copy(xvalid[-1][1])
    n0,n1 = xsort[i,1], xsort[i+1,1]
    sent = False
    k = 0
    while k < len(rngs) and sent == False:
        sent = True
        if n0 == rngs[k][0] and n1 == rngs[k][1]:
            x += 1
            del rngs[k]
        elif n0 == rngs[k][1]:
            rngs[k] = (rngs[k][0], n1)
            if k < (len(rngs)-1) and n1 == rngs[k+1][0]:
                rngs[k] = (rngs[k][0], rngs[k+1][1])
                del rngs[k+1]
        elif n1 == rngs[k][0]:
            rngs[k] = (n0, rngs[k][1])
        elif n0 == rngs[k][0]:
            rngs[k] = (n1, rngs[k][1])
            x += 1
        elif n1 == rngs[k][1]:
            rngs[k] = (rngs[k][0], n0)
            x += 1
        elif rngs[k][0] < n0 < n1 < rngs[k][1]:
            rngs.append((n1,rngs[k][1]))
            rngs[k] = (rngs[k][0], n0)
        else:
            sent = False
            k += 1
    if sent == False:
        rngs.append((n0,n1))
    xvalid.append([x,sorted(rngs)])

for x in xvalid:
    for r in x[1]:
        plt.plot([x[0],x[0]],[r[0],r[1]], 'b-x', lw = 0.2)

xcheck = np.array([x[0] for x in xvalid])
ycheck = np.array([y[0] for y in yvalid])
order = np.flip(np.argsort(rect))
sent = False
k = 0
while sent == False:
    p1 = data[idx[order[k]][0]]
    p3 = data[idx[order[k]][1]]
    p2 = np.array([p1[0],p3[1]])
    p4 = np.array([p3[0],p1[1]])
    rngs = yvalid[np.argmin(ycheck - p1[1] <= 0)-1][1]
    inRange = False
    for r in rngs:
        if r[0] <= p1[0] <= r[1] and r[0] <= p4[0] <= r[1]:
            inRange = True
    if inRange:
        inRange = False
        rngs = yvalid[np.argmin(ycheck - p3[1] <= 0)-1][1]
        for r in rngs:
            if r[0] <= p3[0] <= r[1] and r[0] <= p2[0] <= r[1]:
                inRange = True
    if inRange:
        inRange = False
        rngs = xvalid[np.argmin(xcheck - p1[0] <= 0)-1][1]
        for r in rngs:
            if r[0] <= p1[1] <= r[1] and r[0] <= p2[1] <= r[1]:
                inRange = True
    if inRange:
        inRange = False
        rngs = xvalid[np.argmin(xcheck - p3[0] <= 0)-1][1]
        for r in rngs:
            if r[0] <= p3[1] <= r[1] and r[0] <= p4[1] <= r[1]:
                inRange = True
    if inRange:
        sent = True
        sol2 = int(rect[order[k]])
        plt.plot([p1[0],p2[0],p3[0],p4[0],p1[0]],[p1[1],p2[1],p3[1],p4[1],p1[1]], 'o-')
    else:
        k += 1

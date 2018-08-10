# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 08:35:17 2018

@author: Aman Dubey
"""

def swap(a,b):
    return b,a

def partition(x,p,start,end):
    pindex = start
    pivot = p[end]
    for i in range(start,end):
        if p[i] < pivot:
            p[i],p[pindex] = swap(p[i],p[pindex])
            x[i],x[pindex] = swap(x[i],x[pindex])
            pindex += 1
    p[end],p[pindex] = swap(p[end],p[pindex])
    x[end],x[pindex] = swap(x[end],x[pindex])
    return pindex

def sort(x,p,start,end):
    if start < end:
        pindex = partition(x,p,start,end)
        sort(x,p,start,pindex-1)
        sort(x,p,pindex+1,end)

import random

x = [5,2,1,8,4,7,10,9,3,6]
n = len(x)

P = []

for i in range(n):
    P.append(random.randint(1, n**3))

print("ORIGINAL ARRAY X and P")
print(x)
print(P)

start = 0
end = len(P) - 1
sort(x, P, start, end)
print("ARRAY X and P SORTED ACCORDING to P(PRIORITY)")
print(x)
print(P)


best = 0
m = len(x)

hiring_cost = 0
index = 0
for i in range(m):    
    if x[i] > best:
        index = i
        best = x[i]
        hiring_cost += 1
    
print(best,"found at",index + 1,"round")
print(hiring_cost)
    
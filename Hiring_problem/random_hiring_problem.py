# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 08:00:41 2018

@author: Aman Dubey
"""
import random

x = [5,2,1,8,4,7,10,9,3,6]

best = 0

m = len(x)
random.shuffle(x)
print(x)

hiring_cost = 0
index = 0
for i in range(m):    
    if x[i] > best:
        index = i
        best = x[i]
        hiring_cost += 1
    
print(best,"found at",index + 1,"round")
print(hiring_cost)
    
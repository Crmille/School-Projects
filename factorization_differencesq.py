# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:35:52 2015

@author: Chad-PC
"""
from math import sqrt
from math import floor
import numpy as np

def factorize(n, base):
    def is_square(n):
        return sqrt(n).is_integer()
    
    a, b = 0, 0
    for i in range(1,base+1):
        r = n + i**2
        if is_square(r) == True:
            a,b = i,sqrt(r)
            break
    
    x = b**2 - a**2    
    return x
        
def find_ab(n):
    x = []
    limit = int(n)    
    for i in range(0,limit):
        r = n % i
        if r == 0 and i != 1:
            x.append(i)
    return x
      
      
      
if __name__=="__main__":
    givenN = np.array([53357, 34571, 25777, 64213])
    x = np.zeros(len(givenN))
    for i in range(0,len(givenN)):
        x[i] = factorize(givenN[i], 200)
        prod1 = find_ab(x[i])
        print(i,x[i],":",prod1)
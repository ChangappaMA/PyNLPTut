# -*- coding: utf-8 -*-
"""Machinelearning

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hjw8L2y31KZiXGXNaW22tZ_GV--HTu3g
"""

print("Hello World")

L1 =[2,4,6,8,10]
L2 =[1,3,5,7,9]

Sum = []
mul = []

for i in range(0,5):
  Sum.append(L1[i]+L2[i])
  mul.append(L2[i]*2)

print (Sum)
print (mul)

angles = []
subangles=[]



for i in range(0, 390, 30):
  angles.append(i)
  
subangles = angles[:].reverse()

print(angles)
print(subangles)
i1 = angles.index(90)
i2 = angles.index(270)
print(i1,i2)

lenangles = len(angles)
print(lenangles)

i1_rev = lenangles - i1
i2_rev = lenangles - i2
print(i1_rev, i2_rev)

L1 = [2,4,6,8,10]

L2 = L1
L3 = L1.copy()

del L3[2]

print(L1)
print(L3)

import numpy as py
import tensorflow as tf
#import pytorch

examTuple = (1,2,3)

examTuple += (4,)
del examTuple[2]
print(examTuple)

States = {'Andhra Pradesh' : [4900000, 'Hydrabad', True], 'Assam' : [50000, 'Dispur', False], 'Bihar': [600000, 'Patna', True]}

print(States['Bihar'])

States['Telangana'] = [500000, 'Hydrabad', False]

print(States)

def deg_rad(angle):
  radians = (angle * 3.14) / 180
  return (radians)



print(deg_rad(360))

deg_rad_inline = lambda angle,rotate: angle/180*3.14+rotate

deg_rad_inline(30, deg_rad(90))
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:09:55 2020

@author: Piravin KCM
"""


import numpy
from time import sleep
x,y=numpy.loadtxt("ffaxis.csv",unpack=True,delimiter=',')
a = numpy.column_stack([x,y])
print(a[:,0])
numpy.savetxt("ff.csv",a,delimiter=',')
sleep(100)
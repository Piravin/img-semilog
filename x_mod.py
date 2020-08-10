# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:41:32 2020

@author: Piravin KCM
"""


import numpy
from time import sleep
from matplotlib import pyplot
x=numpy.loadtxt('xv.csv',unpack=True,delimiter=',')
col=[]
dif=[]
global s
s = 2
xval=[]
x=x.tolist()
for r in range(1,len(x)):
    
    co=x[r]-x[r-1]
    col.append(co)
    if r<9:
        dif.append(1000)
        xval.append(dif[r-1]*s)
        s=s+1
    if r>=9 and r<18:
        if r==9:
            
            s=1
        dif.append(10000)
        xval.append(dif[r-1]*s)
        s=s+1
    if r>=18 and r<27:
        if r==18:
            
            s=1
        dif.append(100000)
        xval.append(dif[r-1]*s)
        s=s+1
    if r>=27 and r<36:
        if r==27:
            
            s=1
        dif.append(1000000)
        xval.append(dif[r-1]*s)
        s=s+1
    if r>=36 and r<40:
        if r==36:
            
            s=1
        dif.append(10000000)
        xval.append(dif[r-1]*s)
        s=s+1
rx=[]
ry=[]
poy,pos = numpy.loadtxt('ff.csv',unpack=True,delimiter=',')
for v in range(0,len(pos)):
    for g in range(0,len(x)-1):
        if x[g]<pos[v] and x[g+1]>pos[v]:
            rpos=(dif[g]/col[g]*(pos[v]-x[g]))+xval[g]
            rx.append(rpos)
        elif pos[v]==x[g]:
            rpos=xval[g]
            rx.append(rpos)
      #  else :
#            rp.append(pos[v])
yax = [486,14]
for h in range(0,len(poy)):
    rpoy = ((900/(yax[0]-yax[1]))*(yax[0]-poy[h]))+100
    ry.append(rpoy)
print(len(ry))
print(len(dif))
print(len(x))
print(xval)
print(len(rx),len(ry))
pyplot.semilogx(rx,ry)
pyplot.xlim(2000,50000000)
pyplot.ylim(100,900)
pyplot.grid(True,which="both")
pyplot.show()
e=numpy.column_stack([rx,ry])
numpy.savetxt("55%.csv",e,delimiter=',')
#sleep(100)
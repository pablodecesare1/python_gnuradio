#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:31:37 2020

@author: pablo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

plt.close()
t=np.linspace(0,np.pi*2,1000)
y=np.sin(5*t,dtype="float32")
#plt.plot(t,y)

f=open("onda.dat",'wb')
np.ndarray.tofile(y,f,sep="",format="%f")
f.close()

a=sc.fromfile(open("onda.dat"),dtype=sc.float32)
plt.figure()
#plt.plot(a)


c=np.exp(5j*t,dtype="complex64")
plt.plot(t,c.real,t,c.imag)


f=open("onda_complex","wb")
np.ndarray.tofile(c,f,sep="",format="%f")
f.close()

a=sc.fromfile(open("onda.dat"),dtype=sc.complex64)
plt.figure()
plt.plot(a)
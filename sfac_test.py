import os
import sys
import math
import numpy
from numpy import *
ifile = open("temp1","r")
n = input("enter no of r bins:")
qbin = input("enter no of q bins:")
maxq = input("input max q:")
rmax = 39.9333
dr = 39.9333/n
dq = (maxq - 0.0)/qbin
gr = zeros(n,float)
r = zeros(n,float)
q = zeros(qbin,float)
rho = 57915.0/(81.8258419513**3.0)
sq = zeros(qbin,float)
k = 0
for line in ifile:
    items = str.split(line)
    gr[k] = float(items[2])
    r[k] = float(items[1])
    k = k + 1
for i in range(qbin):
    q[i] = (i+0.5)*dq
    sq[i] = 0.0
    for j in range(n):
        sq[i] += r[j]*(gr[j]-1.0)*math.sin(q[i]*r[j])/q[i]
    sq[i] *= dr*rho*math.pi*4.0
    sq[i] += 1.0
ofile = open("sfac_test_total.txt", "w")
for i in range(qbin):
    file.write(ofile, str(q[i]) + '  ' + str(sq[i]) + '\n')
file.close(ifile)
file.close(ofile)

import os
import sys
import math
import numpy
from numpy import *
import string
ifile = open("temp","r")
natom = input("enter no of atoms:")
nframe = input("enter no of frames:")
ofile = open("temp1","w")
ofile1 = open("temp2","w")
#k = 0
for i in range(nframe):
    for j in range(natom):
        lines = ifile.readline()
        if j == 0:
            items = str.split(lines)
            nstep = int(items[2])
            print nstep
        if i != 0 and nstep == k:
            file.write(ofile1,lines)
#            break
        if i == 0 or nstep != k:
            file.write(ofile, lines)
    k = nstep
file.close(ifile)
file.close(ofile)

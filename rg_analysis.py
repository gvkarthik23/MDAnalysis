import os
import sys
import math
import numpy
from numpy import *
ifile = open("temp","r")
n1 = input("enter no of anions:")
n2 = input("enter no of cations:")
rg_anion = zeros(n1,float)
rg_cation = zeros(n2,float)
k1 = 0
k2 = 0
for line in ifile:
    items = str.split(line)
    if int(items[2]) == 18:
        rg_anion[k1] = float(items[1])
        k1 = k1 + 1
    if int(items[2]) == 131:
        rg_cation[k2] = float(items[1])
        k2 = k2 + 1
print numpy.max(rg_anion), numpy.min(rg_anion)
print numpy.max(rg_cation), numpy.min(rg_cation)
nbin = input("enter no of bins:")
d1 = (numpy.max(rg_anion) - numpy.min(rg_anion))/nbin
d2 = (numpy.max(rg_cation) - numpy.min(rg_cation))/nbin
count_cat = zeros(nbin,int)
count_anion = zeros(nbin,int)
for i in range(nbin):
    for j in range(n1):
        if rg_anion[j] <= (numpy.min(rg_anion)+(d1*(i+1.))) and rg_anion[j] >= (numpy.min(rg_anion)+(d1*(i))):
            count_anion[i] += 1
print sum(count_anion)
print count_anion
for i in range(nbin):
    for j in range(n2):
        if rg_cation[j] <= (numpy.min(rg_cation)+(d2*(i+1.))) and rg_cation[j] >= (numpy.min(rg_cation)+(d2*(i))):
            count_cat[i] += 1
print sum(count_cat)
print count_cat
ofile = open("rg_dist_cation_300k.txt","w")
for i in range(nbin):
    file.write(ofile, str((numpy.min(rg_cation)+(d2*(i+1.)))) + '  ' + str((numpy.min(rg_cation)+(d2*(i)))) + '  ' + str(count_cat[i]) + '\n')
ofile1 = open("rg_dist_anion_300k.txt","w")
for i in range(nbin):
    file.write(ofile1, str((numpy.min(rg_anion)+(d1*(i+1.)))) + '  ' + str((numpy.min(rg_anion)+(d1*(i)))) + '  ' + str(count_anion[i]) + '\n')
file.close(ifile)
file.close(ofile)
file.close(ofile1)

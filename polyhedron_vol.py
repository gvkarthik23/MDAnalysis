##Calculate the volume of any polyhedron formed by a collection of points
import numpy as np
from numpy import zeros
from scipy.spatial import Delaunay
def tetrahedron_volume(a, b, c, d):
    return np.abs(np.einsum('ij,ij->i', a-d, np.cross(b-d, c-d))) / 6
pts = np.random.rand(10, 3)
#print pts
pts1 = zeros([6,3],float)
ifile = open("temp","r")
k = 0
for line in ifile:
    items = str.split(line)
    if items[0] == "O":
        pts1[k][0] = float(items[1])
        pts1[k][1] = float(items[2])
        pts1[k][2] = float(items[3])
        k = k + 1
print pts1
dt = Delaunay(pts1)
#print dt
tets = dt.points[dt.simplices]
#print tets
vol = np.sum(tetrahedron_volume(tets[:, 0], tets[:, 1], tets[:, 2], tets[:, 3]))
print vol

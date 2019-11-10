import numpy as np
import scipy as sp
from scipy import spatial
import matplotlib.pyplot as plt


origin = [0], [0] # origin point
originCoord=np.array([0,0])
V = np.array([[1,1],[-1,-1],[2,-7]])

for x in np.arange(0, 1, 0.1):
    for y in np.arange(0, 1, 0.1):
        pointTemp=np.array(x,y)
        if(sp.spatial.distance.cosine(originCoord,pointTemp)==1):
            print(x,y)
    



plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)

# plt.
plt.show()
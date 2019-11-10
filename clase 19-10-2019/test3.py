import numpy as np
import scipy as sp

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import spatial


def cos(x,y):
	return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

# Projection of th evector 'y' onto the vector 'x' is the vector
def projection(x,y):
    return (np.dot(x,y)/(np.linalg.norm(x)**2))*x
 


w=np.array(
	[2, 1, -1, 2]
)

# print(cos(a,b))
# Similarty is 1-distance beetwhen vectors.
#print(1-spatial.distance.cosine(a,b))


## Check if are independet, if are different 0 is depedent
# A = np.row_stack([x, y, z, w])
# # Singular value decomposition
# U, s, V=np.linalg.svd(A)
# print(s)
# # print(np.dot(a,a))



# xeq=np.array([[0,1,2,0],[1,0,1,1],[-1,2,0,1],[2,1,-1,2]])
# xb=np.array([0,0,0,0])
# print(np.linalg.lstsq(xeq, xb))



# lambdas, V =  np.linalg.eig(xeq.T)
# print(xeq[lambdas == 0,:])

# origin = [0], [0] # origin point
# V = np.array([x,y])
# print(x,y,z)
# plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)

# origin = y[0], y[1]
# V = np.array([z])
# print(*origin)
# plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)

# plt.show()

x=np.array(
	[1, 0, 0, 1, 1, 1]
)

y=np.array(
	[0,1,0, 1, 1, 1]
)

z=projection(x,y)

soa = np.array([x,y,z])
print([x,y,z])
X, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W)
ax.set_xlim([-5, 10])
ax.set_ylim([-5, 10])
ax.set_zlim([-5, 8])
plt.show()



print(np.dot(x,y))
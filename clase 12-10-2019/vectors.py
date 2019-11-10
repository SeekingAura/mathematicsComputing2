import numpy as np
import scipy as sp

from scipy import spatial


def cos(x,y):
	return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

 
 
x=np.array(
	[0, 1, -1, 2]
)

y=np.array(
	[1,0,1,1]
)

z=np.array(
	[-1, 2, 0, 1]
)

w=np.array(
	[2, 1, -1, 2]
)

# print(cos(a,b))
# Similarty is 1-distance beetwhen vectors.
#print(1-spatial.distance.cosine(a,b))


## Check if are independet, if are different 0 is depedent
A = np.row_stack([x, y, z, w])
# Singular value decomposition
U, s, V=np.linalg.svd(A)
print(s)
# print(np.dot(a,a))



xeq=np.array([[0,1,2,0],[1,0,1,1],[-1,2,0,1],[2,1,-1,2]])
xb=np.array([0,0,0,0])
print(np.linalg.lstsq(xeq, xb))



lambdas, V =  np.linalg.eig(xeq.T)
print(xeq[lambdas == 0,:])
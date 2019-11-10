import numpy as np
import scipy as sp


def cos(x,y):
	return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

 
 
a=np.array(
	[1,2,3]
)

b=np.array(
	[2,1,-1]
)

print(cos(a,b))
# Similarty is 1-distance beetwhen vectors.
print(1-sp.spatial.distance.cosine(a,b))
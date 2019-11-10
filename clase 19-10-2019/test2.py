import numpy as np
import matplotlib.pyplot as plt 
import math



valuesX=[i*math.pi for i in np.arange(0, 4, 0.5)]

plt.plot(valuesX, [math.sin(i) for i in valuesX])
plt.plot(valuesX, [math.cos(i) for i in valuesX])

plt.show()
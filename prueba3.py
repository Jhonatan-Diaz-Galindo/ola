import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,40)
y = 1/x
plt.plot(x,y,"gd--")
plt.show()
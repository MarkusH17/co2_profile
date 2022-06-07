#import directories
import numpy as np
import matplotlib.pyplot as plt

num = np.exp(3)
print(num)
xs = np.linspace(0,100,101)
ys = xs**2
plt.plot(xs,ys)
plt.show()
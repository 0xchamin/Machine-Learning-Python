 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mglearn

#generate data set
X,y = mglearn.datasets.make_wave(n_samples = 40)

#plot dataset 
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()
print("X.shape:{}".format(X.shape))


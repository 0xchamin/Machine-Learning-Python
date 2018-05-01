import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mglearn

#generate data set
X,y = mglearn.datasets.make_forge()

#plot dataset 
mglearn.discrete_scatter(X[:,0], X[:,1], y)
plt.legend(["Class 0", "Class 1"], loc =4)
plt.xlabel("First Feature")
plt.ylabel("Second Feature")
plt.show()
print("X.shape:{}".format(X.shape))


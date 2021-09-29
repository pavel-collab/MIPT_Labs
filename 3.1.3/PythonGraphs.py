import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd

from scipy.interpolate import interp1d
import seaborn as sns

import PythonGraphMod

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

x_arr = np.array(x)
y_arr = np.array(y)


fig, ax = PythonGraphMod.CreateSimpleGraph()

ax.plot(x_arr, y_arr)
ax.grid(color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.75)
plt.show()
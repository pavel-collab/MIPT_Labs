import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd

from scipy.interpolate import interp1d
import seaborn as sns

import PythonGraphMod

# выкинули 4ю точку
n = [1,   2,   3,   5,   6,   7,   8]
B = [232, 314, 349, 362, 363, 364, 369]

n_arr = np.array(n)
B_arr = np.array(B)

fig, ax = PythonGraphMod.CreateSimpleGraph()

n_dence, B_dence = PythonGraphMod.InterpolateSet(n, B, 'cubic', 1, 8)
ax.plot(n_dence, B_dence, color='blue', alpha=.75, lw=1, ls='-.')

ax.scatter(n_arr, B_arr)
PythonGraphMod.AddGreed(ax)
plt.show()
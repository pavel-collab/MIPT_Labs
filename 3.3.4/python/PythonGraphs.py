import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd

from scipy.interpolate import interp1d
import seaborn as sns

import PythonGraphMod

current = [2, 1.8, 1.4, 1.2, 1, 0.8, 0.6, 0.4]        # А
B       = [1057, 1032, 935, 845, 730, 611, 491, 338]  # мТл

cur_arr = np.array(current)
B_arr = np.array(B)

fig, ax = PythonGraphMod.CreateSimpleGraph()

cur_dence, B_dence = PythonGraphMod.InterpolateSet(current, B, 'cubic', 0.4, 2)
# ax.plot(cur_dence, B_dence, color='blue', alpha=.75, lw=1, ls='-.')

ax.scatter(cur_arr, B_arr)

plt.title('Градуирование мангита B(I)')
plt.xlabel('I, А')
plt.ylabel('B, мТл')
PythonGraphMod.AddGreed(ax)
plt.show()

fig.savefig('../images/solenoid.png')
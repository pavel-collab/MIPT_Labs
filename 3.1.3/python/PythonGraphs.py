import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd

from scipy.interpolate import interp1d
import seaborn as sns

import PythonGraphMod

# выкинули 4ю и 8ю точку
n = [1,   2,   3,   5,   6,   7]
B = [232, 314, 349, 362, 363, 364]

n_arr = np.array(n)
B_arr = np.array(B)

fig, ax = PythonGraphMod.CreateSimpleGraph()

n_dence, B_dence = PythonGraphMod.InterpolateSet(n, B, 'cubic', 1, 7)
ax.plot(n_dence, B_dence, color='blue', alpha=.75, lw=1, ls='-.')

ax.scatter(n_arr, B_arr)

ax.text(x = 3, y = 300, 
        s = r'$\lim_{h \rightarrow \infty} \frac{\mu_0}{2} P_m \frac{h}{\sqrt{R^2 + h^2}} = \frac{\mu_0}{2} P_m$', 
        fontsize = 20)
plt.title('График зависимости B(n)')
plt.xlabel('n')
plt.ylabel('B, мкТл')
PythonGraphMod.AddGreed(ax)
plt.show()

fig.savefig('../images/solenoid.png')
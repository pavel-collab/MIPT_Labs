import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import seaborn as sns
from scipy.stats import linregress

import PythonGraphMod

fig1, ax1 = PythonGraphMod.CreateSimpleGraph()

h = np.array([5, 10, 20]) # размер диафрагмы в мм
delta = np.array([0.3, 0.6, 2.3]) # мм

lin = linregress(h**2, delta)

ax1.scatter(h**2, delta, color='black', marker='o', alpha=1)
ax1.plot(h**2, lin.intercept + lin.slope * (h**2), color='red', alpha=0.75, lw=1.5, ls='--')

# сетка
ax1.minorticks_on()
ax1.grid(which = 'major', color = 'black', linewidth = 1, linestyle = '-', alpha = 0.75)
ax1.grid(which = 'minor', color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.5)

# оформление
plt.ylabel(r'$\delta$, мм')
plt.xlabel('h, мм')
ax1.text(20, 2.33, 'y(x) = %0.3f x + %0.3f' %(lin.slope, lin.intercept))
ax1.text(20, 2.23, 'slope_err = %f' %lin.stderr)
ax1.text(20, 2.13, 'intercept_err = %f' %lin.intercept_stderr)
ax1.text(20, 2.03, 'y(625) = %0.2f' %(lin.intercept + lin.slope * 625))

plt.show()
fig1.savefig("../images/spheric_aberration.pdf")
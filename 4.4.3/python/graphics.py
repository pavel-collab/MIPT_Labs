import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import seaborn as sns
from scipy.stats import linregress

import PythonGraphMod

n = np.array([1.6484, 1.6544, 1.6583, 1.6584, 1.6617, 1.6693, 1.6806, 1.6898])
lambd = np.array([690.7, 623.4, 597.1, 577.0, 546.1, 491.6, 435.8, 404.7])

fig1, ax1 = PythonGraphMod.CreateSimpleGraph()

# наносим точки эксперементальных данных
ax1.scatter(lambd, n, color='black', s=8, marker='o', alpha=1)

# исключим выбившуюся точку
lambd = np.delete(lambd, 2)
n = np.delete(n, 2)

lambd_dence, n_dence = PythonGraphMod.InterpolateSet(lambd, n, 'quadratic', min(lambd), max(lambd))
# строим аппроксимирующую кривую
ax1.plot(lambd_dence, n_dence, color='red', alpha=0.75, lw=1.5, ls='--', label='lense')
ax1.plot(lambd_dence[0:143000], -0.000296*lambd_dence[0:143000] + 1.8095)

# отметим тички nD, nF и nC
lD = 589.3   # нм -- среднее значение длин волн желтогодублета натрия
nD = 1.6572  # 
lF = 486.1   # нм -- голубая линия водорода
nF = 1.6700  # 
lC = 656.3   # нм -- красная линия водорода
nC = 1.6513  # 

# изабразим положения точек на пересечении горизонтальних и вертикальных линий
ax1.vlines(lD, min(n), nD, ls='--', color='yellow')
ax1.vlines(lF, min(n), nF, ls='--', color='blue')
ax1.vlines(lC, min(n), nC, ls='--', color='red')
ax1.hlines(nD, min(lambd), lD, ls='--', color='yellow')
ax1.hlines(nF, min(lambd), lF, ls='--', color='blue')
ax1.hlines(nC, min(lambd), lC, ls='--', color='red')
# отметим точки на графике
ax1.scatter(lD, nD, color='yellow', s=25, marker='o', alpha=1)
ax1.scatter(lF, nF, color='blue', s=25, marker='o', alpha=1)
ax1.scatter(lC, nC, color='red', s=25, marker='o', alpha=1)

# сетка
ax1.minorticks_on()
ax1.grid(which = 'major', color = 'black', linewidth = 1, linestyle = '-', alpha = 0.75)
ax1.grid(which = 'minor', color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.5)

# оформление
plt.ylabel('n')
plt.xlabel(r'$\lambda$, нм')
ax1.text(560, 1.6875, r'$n_D$ = ' + str(nD) + r' ($\lambda$ = ' + str(lD) + ' нм)')
ax1.text(560, 1.6850, r'$n_F$ = ' + str(nF) + r' ($\lambda$ = ' + str(lF) + ' нм)')
ax1.text(560, 1.6825, r'$n_C$ = ' + str(nC) + r' ($\lambda$ = ' + str(lC) + ' нм)')

plt.show()
fig1.savefig("../images/n_lambda.pdf")
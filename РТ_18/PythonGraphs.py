import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import PythonGraphMod
from scipy.interpolate import interp1d

df_Data_intgrt = pd.read_excel("integrating.ods")
df_Data_dfntg  = pd.read_excel("differentiating.ods")

# данные для интегрирующей цепочки
K_intgrt   = np.array(df_Data_intgrt['K'])     # коэф. усиления
f_intgrt   = np.array(df_Data_intgrt['f'])     # частота f = 2^n f_0
n_intgrt   = np.array(df_Data_intgrt['n'])     # n
lgK_intgrt = np.array(df_Data_intgrt['lgK20']) # логарифм коэф-та усиления

# данные для дифференцирующей цепочки
K_dfntg   = np.array(df_Data_dfntg['K'])      # коэф. усиления
f_dfntg   = np.array(df_Data_dfntg['f'])      # частота f = 2^n f_0
n_dfntg   = np.array(df_Data_dfntg['n'])      # n
lgK_dfntg = np.array(df_Data_dfntg['lgK20'])  # логарифм коэф-та усиления

fig1, ax1_intgrt, ax2_intgrt = PythonGraphMod.CreateDoubleGraph()
fig2, ax1_dfntg, ax2_dfntg   = PythonGraphMod.CreateDoubleGraph()

#----------------------------------------------------------------------------------------------

#! поиграться с размерами фигуры
aprx_func1 = interp1d(f_intgrt, K_intgrt, 'quadratic')

f_intgrt_dence = np.linspace(0.4, 24, 1000)
K_intgrt_dence = aprx_func1(f_intgrt_dence)
ax1_intgrt.plot(f_intgrt_dence, K_intgrt_dence, color='blue', alpha=.75, lw=1, ls='-.')

aprx_func2 = interp1d(f_dfntg, K_dfntg, 'quadratic')

f_dfntg_dence = np.linspace(119, 7590, 1000)
K_dfntg_dence = aprx_func2(f_dfntg_dence)
ax1_dfntg.plot(f_dfntg_dence, K_dfntg_dence, color='blue', alpha=.75, lw=1, ls='-.')

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#! написать интерполирующую функцию
aprx_func3 = interp1d(n_intgrt, lgK_intgrt, 'cubic')

n_intgrt_dence = np.linspace(-2, 4, 1000)
lgK_intgrt_dence = aprx_func3(n_intgrt_dence)
ax2_intgrt.plot(n_intgrt_dence, lgK_intgrt_dence, color='red', alpha=.75, lw=1, ls='-.')

# aprx_func4 = interp1d(n_dfntg, lgK_dfntg, 'cubic')

# n_dfntg_dence = np.linspace(-4, 2, 1000)
# lgK_dfntg_dence = aprx_func4(n_dfntg_dence)

n_dfntg_dence, lgK_dfntg_dence = PythonGraphMod.InterpolateSet(n_dfntg, lgK_dfntg, 'cubic', -4, 2)

ax2_dfntg.plot(n_dfntg_dence, lgK_dfntg_dence, color='red', alpha=.75, lw=1, ls='-.')

#----------------------------------------------------------------------------------------------

ax1_intgrt.scatter(f_intgrt, K_intgrt)
ax2_intgrt.scatter(n_intgrt, lgK_intgrt)
ax1_dfntg.scatter(f_dfntg, K_dfntg)
ax2_dfntg.scatter(n_dfntg, lgK_dfntg)

ax1_intgrt.grid(color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.75)
ax2_intgrt.grid(color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.75)
ax1_dfntg.grid(color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.75)
ax2_dfntg.grid(color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.75)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import PythonGraphMod
from scipy.interpolate import interp1d

# инпортируем данные из таблиц
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

#! поиграться с размерами фигуры
fig1, ax1_intgrt, ax2_intgrt = PythonGraphMod.CreateDoubleGraph()
fig2, ax1_dfntg, ax2_dfntg   = PythonGraphMod.CreateDoubleGraph()

#----------------------------------------------------------------------------------------------

# строим графики коэффициента услинения от частоты
f_intgrt_dence, K_intgrt_dence = PythonGraphMod.InterpolateSet(f_intgrt, K_intgrt, 'quadratic', 0.4, 24)
ax1_intgrt.plot(f_intgrt_dence, K_intgrt_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

f_dfntg_dence, K_dfntg_dence = PythonGraphMod.InterpolateSet(f_dfntg, K_dfntg, 'quadratic', 119, 7590)
ax1_dfntg.plot(f_dfntg_dence, K_dfntg_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

# строим графы Боде
n_intgrt_dence, lgK_intgrt_dence = PythonGraphMod.InterpolateSet(n_intgrt, lgK_intgrt, 'cubic', -2, 4)
ax2_intgrt.plot(n_intgrt_dence, lgK_intgrt_dence, color='red', alpha=.75, lw=1.5, ls='-.')

n_dfntg_dence, lgK_dfntg_dence = PythonGraphMod.InterpolateSet(n_dfntg, lgK_dfntg, 'cubic', -4, 2)
ax2_dfntg.plot(n_dfntg_dence, lgK_dfntg_dence, color='red', alpha=.75, lw=1.5, ls='-.')

#----------------------------------------------------------------------------------------------

# наносим на графики матки (эксперементыльные точки)
ax1_intgrt.scatter(f_intgrt, K_intgrt)
ax2_intgrt.scatter(n_intgrt, lgK_intgrt)
ax1_dfntg.scatter(f_dfntg, K_dfntg)
ax2_dfntg.scatter(n_dfntg, lgK_dfntg)

PythonGraphMod.AddGreed(ax1_intgrt)
PythonGraphMod.AddGreed(ax2_intgrt)
PythonGraphMod.AddGreed(ax1_dfntg)
PythonGraphMod.AddGreed(ax2_dfntg)

fig1.suptitle('Интегрирующая схема')
ax1_intgrt.set_title('График зависимости K(f)')
ax2_intgrt.set_title('Граф Боде')
# ax1_intgrt.set_xlabel('f, кГц')
# ax1_intgrt.set_ylabel('K')

fig2.suptitle('Дифференцирующая схема')
ax1_dfntg.set_title('График зависимости K(f)')
ax2_dfntg.set_title('Граф Боде')
plt.show()
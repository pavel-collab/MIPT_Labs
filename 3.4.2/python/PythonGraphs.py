import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.interpolate import interp1d
import seaborn as sns

from scipy.stats import linregress

import PythonGraphMod

# =================================================================================================
# graphic 1/x(T)

# import data
df_Data_exp_1xT = pd.read_excel("../data/1x(T).ods")

T = np.array(df_Data_exp_1xT['T'])
x1 = np.array(df_Data_exp_1xT['1/x'])

# create figure and graph
fig1, ax1 = PythonGraphMod.CreateSimpleGraph()

T_dence, x1_dence = PythonGraphMod.InterpolateSet(T, x1, 'quadratic', 284, 303)

# построение наилучшей прямой
'''
struct result:
    slopefloat       -- slope of the regression line
    intercept        -- Intercept of the regression line
    rvalue           -- Correlation coefficient
    pvalue
    stderr           -- Standard error of the estimated slope (gradient), under the assumption of residual normality
    intercept_stderr -- Standard error of the estimated intercept, under the assumption of residual normality
'''
res = linregress(T[:5:-1], x1[:5:-1])

intersection_point = -res.intercept/res.slope

print("======================================")
print("Diagram 1")
print("Temperature dependence of the inverse magnetic susceptibility")
print()
print('intersection point : (%i, 0)' %intersection_point)
print("======================================")


ax1.scatter(T, x1, c = 'black', marker = 'o')

plt.plot(T, res.intercept + res.slope * T, color='red', alpha=.75, lw=1.5, ls='--')
plt.plot(intersection_point, 0, 'ro')
ax1.plot(T_dence, x1_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

plt.title (r'Зависимость $1/\chi$(T)')
plt.xlabel('T, K')
plt.ylabel(r'$1/\chi$')
plt.ylim([-5, 20])
PythonGraphMod.AddGreed(ax1)

# =================================================================================================
# graphic x(T)

# import data
df_Data_exp_xT = pd.read_excel("../data/x(T).ods")

x = np.array(df_Data_exp_xT['x'])

# create figure and graph
fig2, ax2 = PythonGraphMod.CreateSimpleGraph()

T_dence, x_dence = PythonGraphMod.InterpolateSet(T, x, 'quadratic', 284, 303)

ax2.scatter(T, x, c = 'black', marker = 'o')
ax2.plot(T_dence, x_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

plt.title (r'Зависимость $\chi$(T)')
plt.xlabel('T, K')
plt.ylabel(r'$\chi$')
# plt.ylim([-5, 20])
PythonGraphMod.AddGreed(ax2)

# =================================================================================================
# graphic mu(T)

# import data
df_Data_exp_muT = pd.read_excel("../data/mu(T).ods")

mu = np.array(df_Data_exp_muT['mu'])

# create figure and graph
fig3, ax3 = PythonGraphMod.CreateSimpleGraph()

T_dence, mu_dence = PythonGraphMod.InterpolateSet(T, mu, 'quadratic', 284, 303)

ax3.scatter(T, mu, c = 'black', marker = 'o')
ax3.plot(T_dence, mu_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

plt.title (r'Зависимость $\mu$(T)')
plt.xlabel('T, K')
plt.ylabel(r'$\mu$')
# plt.ylim([-5, 20])
PythonGraphMod.AddGreed(ax3)

# =================================================================================================
# graphic L(T)

# import data
df_Data_exp_LT = pd.read_excel("../data/L(T).ods")

L = np.array(df_Data_exp_LT['L'])

# create figure and graph
fig4, ax4 = PythonGraphMod.CreateSimpleGraph()

T_dence, L_dence = PythonGraphMod.InterpolateSet(T, L, 'quadratic', 284, 303)

ax4.scatter(T, L, c = 'black', marker = 'o')
ax4.plot(T_dence, L_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

plt.title ('Зависимость L(T)')
plt.xlabel('T, K')
plt.ylabel('L, мкГн')
# plt.ylim([-5, 20])
PythonGraphMod.AddGreed(ax4)

plt.show()

# fig1.savefig('../images/graph_1x(T).png')
# fig2.savefig('../images/graph_x(T).png')
# fig3.savefig('../images/graph_mu(T).png')
# fig4.savefig('../images/graph_L(T).png')
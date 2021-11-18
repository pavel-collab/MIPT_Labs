import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.interpolate import interp1d
import seaborn as sns

from scipy.stats import linregress

import PythonGraphMod

def PrintParams(up_intercept, down_intercept, mid_slope) :
    print("======================================")
    print()
    print('saturation current +: (0, %.3f)' %up_intercept)
    print('saturation current -: (0, %.3f)' %down_intercept)
    print('avarege current : %.3f' %((up_intercept + abs(down_intercept))/2))
    print('midle slope : %.3f' %mid_slope)
    print("======================================")

# =================================================================================================
# VAC1

# import data file
df_Data_exp_VAC1 = pd.read_excel("../data/VAC1.ods")

# import data from data file (.ods)
I = np.array(df_Data_exp_VAC1['I'])
U = np.array(df_Data_exp_VAC1['U'])

# create figure and graph
fig1, ax1 = PythonGraphMod.CreateSimpleGraph()
# create linspace for interpolate plot
U_dence, I_dence = PythonGraphMod.InterpolateSet(U, I, 'cubic', 130.55, 232.19)

# create diagrams
ax1.scatter(U, I, c = 'black', marker = 'o')
ax1.plot(U_dence, I_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ разряда в Неоне')
plt.xlabel('U, В')
plt.ylabel('I, мА')
PythonGraphMod.AddGreed(ax1)

# =================================================================================================
# VAC2

# import data file
df_Data_exp_VAC2 = pd.read_excel("../data/VAC2.ods")

# import data from data file (.ods)
I = np.array(df_Data_exp_VAC2['I'])
U = np.array(df_Data_exp_VAC2['U'])

# create figure and graph
fig2, ax2 = PythonGraphMod.CreateSimpleGraph()

# calculate a params of tangents
res_up = linregress(U[:10:1], I[:10:1])
res_down = linregress(U[:-7:-1], I[:-7:-1])
mid_slope = linregress(U[13:42], I[13:42])

# print information to consol (for developer)
# PrintParams(res_up.intercept, res_down.intercept, mid_slope.slope)

# create linspace for interpolate plot
U_dence1, I_dence1 = PythonGraphMod.InterpolateSet(U, I, 'quadratic', 0.3, 31.61)
U_dence2, I_dence2 = PythonGraphMod.InterpolateSet(U, I, 'cubic', -31.61, -0.008)

# create diagrams
plt.plot(U, res_up.intercept + res_up.slope * U, color='red', alpha=.75, lw=1.5, ls='--')
plt.plot(U, res_down.intercept + res_down.slope * U, color='red', alpha=.75, lw=1.5, ls='--')

plt.plot(U, mid_slope.slope * U, color='green', alpha=.75, lw=1.5, ls='--')

plt.plot(0, res_up.intercept, 'ro')
plt.plot(0, res_down.intercept, 'ro')

ax2.scatter(U, I, c = 'black', marker = 'o')
ax2.plot(U_dence1, I_dence1, color='blue', alpha=.75, lw=1.5, ls='-.')
ax2.plot(U_dence2, I_dence2, color='blue', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ двойного зонда')
ax2.text(0, res_up.intercept+5, r'$I_{i}$', size = 15)
ax2.text(0, res_down.intercept+5, r'$-I_{i}$', size = 15)
ax2.text(3, -10, 'slope = ' + str(round(mid_slope.slope, 3)) + ' мкА/В', size = 15)
ax2.text(-30, 90, r'$\left<I_{i} \right> = $' + str(round((res_up.intercept + abs(res_down.intercept))/2, 3)) + ' мкА', size = 15)
plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.ylim([-135, 110])
PythonGraphMod.AddGreed(ax2)

# =================================================================================================
# VAC3

# import data file
df_Data_exp_VAC3 = pd.read_excel("../data/VAC3.ods")

# import data from data file (.ods)
I = np.array(df_Data_exp_VAC3['I'])
U = np.array(df_Data_exp_VAC3['U'])

# create figure and graph
fig3, ax3 = PythonGraphMod.CreateSimpleGraph()

# calculate a params of tangents
res_up = linregress(U[:12:1], I[:12:1])
res_down = linregress(U[:-8:-1], I[:-8:-1])
mid_slope = linregress(U[15:38], I[15:38])

# print information to consol (for developer)
# PrintParams(res_up.intercept, res_down.intercept, mid_slope.slope)

# create linspace for interpolate plot
U_dence1, I_dence1 = PythonGraphMod.InterpolateSet(U, I, 'quadratic', 0.045, 31.61)
U_dence2, I_dence2 = PythonGraphMod.InterpolateSet(U, I, 'cubic', -31.61, -0.019)

# create diagrams
plt.plot(U, res_up.intercept + res_up.slope * U, color='red', alpha=.75, lw=1.5, ls='--')
plt.plot(U, res_down.intercept + res_down.slope * U, color='red', alpha=.75, lw=1.5, ls='--')

plt.plot(U, mid_slope.slope * U, color='green', alpha=.75, lw=1.5, ls='--')

plt.plot(0, res_up.intercept, 'ro')
plt.plot(0, res_down.intercept, 'ro')

ax3.scatter(U, I, c = 'black', marker = 'o')
ax3.plot(U_dence1, I_dence1, color='blue', alpha=.75, lw=1.5, ls='-.')
ax3.plot(U_dence2, I_dence2, color='blue', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ двойного зонда')
ax3.text(0, res_up.intercept+5, r'$I_{i}$', size = 15)
ax3.text(0, res_down.intercept+5, r'$-I_{i}$', size = 15)
ax3.text(3, -10, 'slope = ' + str(round(mid_slope.slope, 3)) + ' мкА/В', size = 15)
ax3.text(-30, 50, r'$\left<I_{i} \right> = $' + str(round((res_up.intercept + abs(res_down.intercept))/2, 3)) + ' мкА', size = 15)
plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.ylim([-70, 70])
PythonGraphMod.AddGreed(ax3)

# =================================================================================================
# VAC4

# import data file
df_Data_exp_VAC4 = pd.read_excel("../data/VAC4.ods")

# import data from data file (.ods)
I = np.array(df_Data_exp_VAC4['I'])
U = np.array(df_Data_exp_VAC4['U'])

# create figure and graph
fig4, ax4 = PythonGraphMod.CreateSimpleGraph()

# calculate a params of tangents
res_up = linregress(U[:10:1], I[:10:1])
res_down = linregress(U[:-9:-1], I[:-9:-1])
mid_slope = linregress(U[12:35], I[12:35])

# print information to consol (for developer)
# PrintParams(res_up.intercept, res_down.intercept, mid_slope.slope)

# create linspace for interpolate plot
U_dence1, I_dence1 = PythonGraphMod.InterpolateSet(U, I, 'quadratic', 0.005, 31.6)
U_dence2, I_dence2 = PythonGraphMod.InterpolateSet(U, I, 'cubic', -31.6, -0.0086)

# create diagrams
plt.plot(U, res_up.intercept + res_up.slope * U, color='red', alpha=.75, lw=1.5, ls='--')
plt.plot(U, res_down.intercept + res_down.slope * U, color='red', alpha=.75, lw=1.5, ls='--')

plt.plot(U, mid_slope.slope * U, color='green', alpha=.75, lw=1.5, ls='--')

plt.plot(0, res_up.intercept, 'ro')
plt.plot(0, res_down.intercept, 'ro')

ax4.scatter(U, I, c = 'black', marker = 'o')
ax4.plot(U_dence1, I_dence1, color='blue', alpha=.75, lw=1.5, ls='-.')
ax4.plot(U_dence2, I_dence2, color='blue', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ двойного зонда')
ax4.text(0, res_up.intercept+3, r'$I_{i}$', size = 15)
ax4.text(0, res_down.intercept+3, r'$-I_{i}$', size = 15)
ax4.text(3, -5, 'slope = ' + str(round(mid_slope.slope, 3)) + ' мкА/В', size = 15)
ax4.text(-30, 25, r'$\left<I_{i} \right> = $' + str(round((res_up.intercept + abs(res_down.intercept))/2, 3)) + ' мкА', size = 15)
plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.ylim([-35, 35])
PythonGraphMod.AddGreed(ax4)

# =================================================================================================

plt.show()

# safing figures
# fig1.savefig('../images/VAC1.png')
# fig2.savefig('../images/VAC2.png')
# fig3.savefig('../images/VAC3.png')
# fig4.savefig('../images/VAC4.png')
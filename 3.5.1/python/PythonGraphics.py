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
I1 = np.array(df_Data_exp_VAC1['I'])
U1 = np.array(df_Data_exp_VAC1['U'])

# calculate a params of tangents
res = linregress(U1[2:4:1], I1[2:4:1])

# create figure and graph
fig1, ax1 = PythonGraphMod.CreateSimpleGraph()
# create linspace for interpolate plot
U_dence, I_dence = PythonGraphMod.InterpolateSet(U1, I1, 'cubic', 130.55, 232.19)

# create diagrams
ax1.scatter(U1, I1, c = 'black', marker = 'o')
ax1.plot(U_dence, I_dence, color='blue', alpha=.75, lw=1.5, ls='-.')
ax1.plot(U1, res.intercept + res.slope * U1, color='green', alpha=.75, lw=1.5, ls='--')

# diagram desing
plt.title ('ВАХ разряда в Неоне')
plt.xlabel('U, В')
plt.ylabel('I, мА')
ax1.text(180, 3, 'dI/dU = ' + str(round(res.slope, 3)), size = 15)
ax1.text(180, 2.5, r'$R_{диф} = $' + str(round(abs(1000/res.slope), 3)) + ' Ом', size = 15)
plt.ylim([0, 6])
PythonGraphMod.AddGreed(ax1)

# =================================================================================================
# VAC2

# import data file
df_Data_exp_VAC2 = pd.read_excel("../data/VAC2.ods")

# import data from data file (.ods)
I2 = np.array(df_Data_exp_VAC2['I'])
U2 = np.array(df_Data_exp_VAC2['U'])

# create figure and graph
fig2, ax2 = PythonGraphMod.CreateSimpleGraph()

# calculate a params of tangents
res_up2 = linregress(U2[:10:1], I2[:10:1])
res_down2 = linregress(U2[:-7:-1], I2[:-7:-1])
mid_slope2 = linregress(U2[13:42], I2[13:42])

# print information to consol (for developer)
# PrintParams(res_up.intercept, res_down.intercept, mid_slope.slope)

# create linspace for interpolate plot
U_dence1_V2, I_dence1_V2 = PythonGraphMod.InterpolateSet(U2, I2, 'quadratic', 0.3, 31.61)
U_dence2_V2, I_dence2_V2 = PythonGraphMod.InterpolateSet(U2, I2, 'cubic', -31.61, -0.008)

# create diagrams
plt.plot(U2, res_up2.intercept + res_up2.slope * U2, color='red', alpha=.75, lw=1.5, ls='--')
plt.plot(U2, res_down2.intercept + res_down2.slope * U2, color='red', alpha=.75, lw=1.5, ls='--')

plt.plot(U2, mid_slope2.slope * U2, color='green', alpha=.75, lw=1.5, ls='--')

plt.plot(0, res_up2.intercept, 'ro')
plt.plot(0, res_down2.intercept, 'ro')

ax2.scatter(U2, I2, c = 'black', marker = 'o')
ax2.plot(U_dence1_V2, I_dence1_V2, color='blue', alpha=.75, lw=1.5, ls='-.')
ax2.plot(U_dence2_V2, I_dence2_V2, color='blue', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ двойного зонда')
ax2.text(0, res_up2.intercept+5, r'$I_{i}$', size = 15)
ax2.text(0, res_down2.intercept+5, r'$-I_{i}$', size = 15)
ax2.text(3, -10, 'slope = ' + str(round(mid_slope2.slope, 3)) + ' мкА/В', size = 15)
ax2.text(-30, 90, r'$\left<I_{i} \right> = $' + str(round((res_up2.intercept + abs(res_down2.intercept))/2, 3)) + ' мкА', size = 15)
plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.ylim([-135, 110])
PythonGraphMod.AddGreed(ax2)

# =================================================================================================
# VAC3

# import data file
df_Data_exp_VAC3 = pd.read_excel("../data/VAC3.ods")

# import data from data file (.ods)
I3 = np.array(df_Data_exp_VAC3['I'])
U3 = np.array(df_Data_exp_VAC3['U'])

# create figure and graph
fig3, ax3 = PythonGraphMod.CreateSimpleGraph()

# calculate a params of tangents
res_up3 = linregress(U3[:12:1], I3[:12:1])
res_down3 = linregress(U3[:-8:-1], I3[:-8:-1])
mid_slope3 = linregress(U3[15:38], I3[15:38])

# print information to consol (for developer)
# PrintParams(res_up.intercept, res_down.intercept, mid_slope.slope)

# create linspace for interpolate plot
U_dence1_V3, I_dence1_V3 = PythonGraphMod.InterpolateSet(U3, I3, 'quadratic', 0.045, 31.61)
U_dence2_V3, I_dence2_V3 = PythonGraphMod.InterpolateSet(U3, I3, 'cubic', -31.61, -0.019)

# create diagrams
plt.plot(U3, res_up3.intercept + res_up3.slope * U3, color='red', alpha=.75, lw=1.5, ls='--')
plt.plot(U3, res_down3.intercept + res_down3.slope * U3, color='red', alpha=.75, lw=1.5, ls='--')

plt.plot(U3, mid_slope3.slope * U3, color='green', alpha=.75, lw=1.5, ls='--')

plt.plot(0, res_up3.intercept, 'ro')
plt.plot(0, res_down3.intercept, 'ro')

ax3.scatter(U3, I3, c = 'black', marker = 'o')
ax3.plot(U_dence1_V3, I_dence1_V3, color='blue', alpha=.75, lw=1.5, ls='-.')
ax3.plot(U_dence2_V3, I_dence2_V3, color='blue', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ двойного зонда')
ax3.text(0, res_up3.intercept+5, r'$I_{i}$', size = 15)
ax3.text(0, res_down3.intercept+5, r'$-I_{i}$', size = 15)
ax3.text(3, -10, 'slope = ' + str(round(mid_slope3.slope, 3)) + ' мкА/В', size = 15)
ax3.text(-30, 50, r'$\left<I_{i} \right> = $' + str(round((res_up3.intercept + abs(res_down3.intercept))/2, 3)) + ' мкА', size = 15)
plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.ylim([-70, 70])
PythonGraphMod.AddGreed(ax3)

# =================================================================================================
# VAC4

# import data file
df_Data_exp_VAC4 = pd.read_excel("../data/VAC4.ods")

# import data from data file (.ods)
I4 = np.array(df_Data_exp_VAC4['I'])
U4 = np.array(df_Data_exp_VAC4['U'])

# create figure and graph
fig4, ax4 = PythonGraphMod.CreateSimpleGraph()

# calculate a params of tangents
res_up4 = linregress(U4[:10:1], I4[:10:1])
res_down4 = linregress(U4[:-9:-1], I4[:-9:-1])
mid_slope4 = linregress(U4[12:35], I4[12:35])

# print information to consol (for developer)
# PrintParams(res_up.intercept, res_down.intercept, mid_slope.slope)

# create linspace for interpolate plot
U_dence1_V4, I_dence1_V4 = PythonGraphMod.InterpolateSet(U4, I4, 'quadratic', 0.005, 31.6)
U_dence2_V4, I_dence2_V4 = PythonGraphMod.InterpolateSet(U4, I4, 'cubic', -31.6, -0.0086)

# create diagrams
plt.plot(U4, res_up4.intercept + res_up4.slope * U4, color='red', alpha=.75, lw=1.5, ls='--')
plt.plot(U4, res_down4.intercept + res_down4.slope * U4, color='red', alpha=.75, lw=1.5, ls='--')

plt.plot(U4, mid_slope4.slope * U4, color='green', alpha=.75, lw=1.5, ls='--')

plt.plot(0, res_up4.intercept, 'ro')
plt.plot(0, res_down4.intercept, 'ro')

ax4.scatter(U4, I4, c = 'black', marker = 'o')
ax4.plot(U_dence1_V4, I_dence1_V4, color='blue', alpha=.75, lw=1.5, ls='-.')
ax4.plot(U_dence2_V4, I_dence2_V4, color='blue', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ двойного зонда')
ax4.text(0, res_up4.intercept+3, r'$I_{i}$', size = 15)
ax4.text(0, res_down4.intercept+3, r'$-I_{i}$', size = 15)
ax4.text(3, -5, 'slope = ' + str(round(mid_slope4.slope, 3)) + ' мкА/В', size = 15)
ax4.text(-30, 25, r'$\left<I_{i} \right> = $' + str(round((res_up4.intercept + abs(res_down4.intercept))/2, 3)) + ' мкА', size = 15)
plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.ylim([-35, 35])
PythonGraphMod.AddGreed(ax4)

# =================================================================================================
# one graphic for all VAC

# create figure and graph
fig5, ax5 = PythonGraphMod.CreateSimpleGraph()

# create diagrams
ax5.scatter(U2, I2, c = 'black', marker = 's', s = 10)
ax5.plot(U_dence1_V2, I_dence1_V2, color='blue', alpha=.75, lw=1.5, ls='-.', label = r'$I_p = 4.8$ мА')
ax5.plot(U_dence2_V2, I_dence2_V2, color='blue', alpha=.75, lw=1.5, ls='-.')
ax5.scatter(U3, I3, c = 'black', marker = 's', s = 10)
ax5.plot(U_dence1_V3, I_dence1_V3, color='red', alpha=.75, lw=1.5, ls='-.', label = r'$I_p = 3$ мА')
ax5.plot(U_dence2_V3, I_dence2_V3, color='red', alpha=.75, lw=1.5, ls='-.')
ax5.scatter(U4, I4, c = 'black', marker = 's', s = 10)
ax5.plot(U_dence1_V4, I_dence1_V4, color='green', alpha=.75, lw=1.5, ls='-.', label = r'$I_p = 1.5$ мА')
ax5.plot(U_dence2_V4, I_dence2_V4, color='green', alpha=.75, lw=1.5, ls='-.')

# diagram desing
plt.title ('ВАХ двойного зонда')
plt.legend(loc="upper left")
plt.xlabel('U, В')
plt.ylabel('I, мкА')
# plt.ylim([-135, 110])
PythonGraphMod.AddGreed(ax5)

# =================================================================================================

plt.show()

# safing figures
fig1.savefig('../images/VAC1.png')
# fig2.savefig('../images/VAC2.png')
# fig3.savefig('../images/VAC3.png')
# fig4.savefig('../images/VAC4.png')
# fig5.savefig('../images/all_VAC.png')
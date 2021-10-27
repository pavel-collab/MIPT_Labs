import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.interpolate import interp1d
import seaborn as sns

import PythonGraphMod

# =================================================================================================
# first sample graphics B(H)

# import data
df_Data_experiment_1_table_1 = pd.read_excel("../data/first_sample_B(H).ods")

# get data arrays H and B
H = np.array(df_Data_experiment_1_table_1['H'])
B = np.array(df_Data_experiment_1_table_1['B'])

# create figure and graph
fig1, ax1 = PythonGraphMod.CreateSimpleGraph()

H_dence, B_dence = PythonGraphMod.InterpolateSet(H, B, 'cubic', 5, 32)

ax1.scatter(H, B, c = 'black', marker = 's')
ax1.plot(H_dence, B_dence, color='blue', alpha=.75, lw=1.5, ls='-.')

plt.title ('Феррит B(H)')
plt.xlabel('H, А/м')
plt.ylabel('B, Тл')
PythonGraphMod.AddGreed(ax1)

# fig1.savefig('../images/sample1_B(H)Python.png')

# =================================================================================================
# first sample graphics mu(H)

df_Data_experiment_1_table_2 = pd.read_excel("../data/first_sample_mu(H).ods")

H = np.array(df_Data_experiment_1_table_2['H'])
mu = np.array(df_Data_experiment_1_table_2['mu'])

fig2, ax2 = PythonGraphMod.CreateSimpleGraph()

H_dence, mu_dence = PythonGraphMod.InterpolateSet(H, mu, 'cubic', 4.8, 32)

ax2.scatter(H, mu, c = 'black', marker = 's')
ax2.plot(H_dence, mu_dence, color='green', alpha=.75, lw=1.5, ls='-.')

plt.title (r'Феррит $\mu(H)$')
plt.xlabel('H, А/м')
plt.ylabel(r'$\mu$')
PythonGraphMod.AddGreed(ax2)

# fig2.savefig('../images/sample1_mu(H)Python.png')

# =================================================================================================
# second sample graphics B(H)

df_Data_experiment_2_table_1 = pd.read_excel("../data/second_sample_B(H).ods")

H = np.array(df_Data_experiment_2_table_1['H'])
B = np.array(df_Data_experiment_2_table_1['B'])

fig3, ax3 = PythonGraphMod.CreateSimpleGraph()

H_dence, B_dence = PythonGraphMod.InterpolateSet(H, B, 'cubic', 15.3, 50.9)

ax3.scatter(H, B, c = 'black', s = 20, marker = 's')
ax3.plot(H_dence, B_dence, color='deeppink', lw=1.5, ls='-.')

plt.title ('Пермаллой B(H)')
plt.xlabel('H, А/м')
plt.ylabel('B, Тл')
PythonGraphMod.AddGreed(ax3)

# fig3.savefig('../images/sample2_B(H)Python.png')

# =================================================================================================
# second sample graphics mu(H)

df_Data_experiment_2_table_2 = pd.read_excel("../data/second_sample_mu(H).ods")

H = np.array(df_Data_experiment_2_table_2['H'])
mu = np.array(df_Data_experiment_2_table_2['mu'])

fig4, ax4 = PythonGraphMod.CreateSimpleGraph()

H_dence, mu_dence = PythonGraphMod.InterpolateSet(H, mu, 'cubic', 15.3, 50.9)

ax4.scatter(H, mu, c = 'black', s = 20, marker = 's')
ax4.plot(H_dence, mu_dence, color='orange', lw=1.5, ls='-.')

plt.title (r'Пермаллой $\mu(H)$')
plt.xlabel('H, А/м')
plt.ylabel(r'$\mu$')
PythonGraphMod.AddGreed(ax4)

# fig4.savefig('../images/sample2_mu(H)Python.png')

# =================================================================================================
plt.show()
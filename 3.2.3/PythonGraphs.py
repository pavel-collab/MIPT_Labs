from math import sqrt

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import PythonGraphMod
from scipy.interpolate import interp1d

df_Data_res1 = pd.read_excel("Data_res1.ods")
df_Data_res2 = pd.read_excel("Data_res2.ods")

f1 = np.array(df_Data_res1['f'])
A1 = np.array(df_Data_res1['A'])
f2 = np.array(df_Data_res2['f1'])
A2 = np.array(df_Data_res2['A1'])

fig, ax = PythonGraphMod.CreateSimpleGraph()

aprx_f1 = interp1d(f1, A1, 'cubic')

f1_dence = np.linspace(14.5, 31.0, 1000)
A1_dence = aprx_f1(f1_dence)

aprx_f2 = interp1d(f2, A2, 'cubic')

f2_dence = np.linspace(11.0, 21.0, 1000)
A2_dence = aprx_f2(f2_dence)

ax.scatter(f1, A1)
ax.scatter(f2, A2)
ax.plot(f1_dence, A1_dence, color='blue', alpha=.75, lw=1, ls='-.')
ax.plot(f2_dence, A2_dence, color='red', alpha=.75, lw=1, ls='-.')

#----------------------------------------------------------------------------------------------
# горизонтальная линия
# параметры: координата по y, x_min, x_max
ax.hlines(286, 10.0, 35.0, ls='--')
# вертикальная линия
# параметры: координата по x, y_min, y_max
ax.vlines(23.56, 0, 400, ls='--')

ax.hlines(99.6, 10.0, 35.0,'red', ls='--')
ax.vlines(17.8 , 0  , 141,'red', ls='--')
#----------------------------------------------------------------------------------------------

plt.title ('amplitude-frequency characteristic')
plt.xlabel('frequency')
plt.ylabel('amplitude')

ax.grid(color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.75)
plt.show()
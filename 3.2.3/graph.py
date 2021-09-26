#import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.interpolate import interp1d
import seaborn as sns

'''
MODUL:
    from scipy.interpolate import interp1d

INTERP1D
    f = interp1d(x, y, kind='<kind of interpolate curved line>')

    x and y are np arrays

DESCRIPTION:
    This funcsion is used, when you have a set of date (x, y),
    you don't know the mathematical relationshipt between the measures
    'x' and 'y' and you need to interpolate it by the smooth curved line. 

EXAMPLE:
'''
# x = np.linspace(0, 10, 10)
# y = x**2 * np.sin(x)

# plt.scatter(x, y)
# plt.show()

# f = interp1d(x, y, kind='cubic')

# x_dence = np.linspace(0, 10, 100)
# y_dence = f(x_dence)

# plt.plot(x_dence, y_dence)
# plt.show()

#===============================================================================================

# variants to build a linear regretion
#   polyfit() and poly1d()
#   sns.lmplot()
#   seaborn.regplot()

#===============================================================================================

data_frame = pd.read_excel('Data.ods')

# plt.figure(figsize=(12, 7))
fig, ax = plt.subplots()

ax.scatter(data_frame['f'], data_frame['A'], c = 'black')
ax.scatter(data_frame['f1'], data_frame['A1'], c = 'red')

f1 = interp1d(data_frame['f'], data_frame['A'], kind='cubic')

x_dence1 = np.linspace(150, 300, 1000)
y_dence1 = f1(x_dence1)

ax.plot(x_dence1, y_dence1)

# linear regression
sns.lmplot(x = 'C_par', y = '(T/2pi)^2', data = data_frame)

plt.grid()
plt.show()
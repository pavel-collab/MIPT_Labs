import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d

def CreateSimpleGraph():
    figure, axes = plt.subplots()
    return figure, axes

def CreateDoubleGraph():
    figure = plt.figure(figsize=(5,4), dpi=100)

    axes1 = figure.add_subplot(2, 1, 1)
    axes2 = figure.add_subplot(2, 1, 2)
    return figure, axes1, axes2

def InterpolateSet(x, y, mode, x_min, x_max):
    ApproximateFunction = interp1d(x, y, mode)

    x_dence = np.linspace(x_min, x_max, 1000)
    y_dence = ApproximateFunction(x_dence)
    return x_dence, y_dence

#==============================================================================================

'''
Createa figure and an axes on it
'''

# fig, ax = plt.subplots()

#----------------------------------------------------------------------------------------------

'''
Createa figure and add two axes on it
Define figure size and resolution
'''

# figure = plt.figure(figsize=(5,4), dpi=100)

# ax1 = figure.add_subplot(2, 1, 1)
# ax2 = figure.add_subplot(2, 1, 2)

#----------------------------------------------------------------------------------------------

#==============================================================================================

'''
Set an x and y ticks
'''

# ax.set_xticks(np.arange(0, 5, 0.5))
# ax.set_yticks(np.arange(0, 5, 0.5))

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

'''
plot grid params, plot background color and show the plot
'''

# ax.set_facecolor('deeppink')
# ax.grid(color = 'grey', linewidth = 1, linestyle = '--', alpha = 0.75)
# plt.show()

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

'''
Tatle and labels
'''

# plt.title('Plot title')
# plt.xlabel('x label')
# plt.ylabel('y label')

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

'''
Plot params
color       -- цвет графика 
alpha       -- прозрачность
lw          -- толщина линии
ls          -- стиль линии
marker      -- стиль маркеров точек
markersize  -- размер маркеров
markercolor -- цвет маркеров
'''

# ax.plot(x, y, color='blue', alpha=.75, lw=1, ls='--', marker='o',
#                             markersize = 3, markercolor = 'yellow')

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

'''
горизонтальная линия
параметры: координата по y, x_min, x_max
'''
# ax.hlines(286, 100, 350, ls='--')

'''
вертикальная линия
параметры: координата по x, y_min, y_max
'''
# ax.vlines(235.6, 0, 400, ls='--')

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

'''
Tex Markup

0,23 -- location on the axes
'''

# ax.text(0, 23, 
#         r'$\frac{1}{2} S = \pi R^2$)

#==============================================================================================
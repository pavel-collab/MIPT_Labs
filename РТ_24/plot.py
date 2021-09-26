import os
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [0, 1, 2, 3, 4, 8, 13, 15]
plt.figure(figsize=(12, 7))

fig, ax = plt.subplots()

#plt.plot(x, y1, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
ax.scatter(x, y1, marker = 'o', linewidths = 4, c = 'black')
ax.set_facecolor('deeppink')     #  цвет области Axes
ax.set_title('My Plot.')
#plt.legend()
plt.grid(True)

plt.savefig('saved_figure.png')
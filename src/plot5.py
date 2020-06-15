import matplotlib.pyplot as plt
import numpy as np

# setting the axes 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# squaring in red
x = np.linspace(0,2,100)
y1 = x**2
plt.plot(x,y1, 'r')

# square root in bliue
x = np.linspace(0,4,100)
y2 = x**0.5
plt.plot(x,y2,'b')

# show plot
plt.xticks(range(1, 5))
plt.yticks(range(1, 5))
plt.show()


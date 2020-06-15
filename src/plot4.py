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
y = x**2
plt.plot(x,y, 'r')

# square root in blue
plt.plot(y,x,'b')

# show plot
plt.xticks(range(1, 5))
plt.yticks(range(1, 5))
plt.show()


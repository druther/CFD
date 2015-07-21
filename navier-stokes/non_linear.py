''' Program to plot non-linear convection using Python '''

import numpy as np
import matplotlib.pyplot as plt

# Initail Parameters
nx = 41
dx = 2./(nx-1)
nt = 20
dt = .25
c = 2

u = np.ones(nx)          # Creates array with number of elements equal to nx
u[.5/dx : 1/dx+1] = 2   # Change value of some of the array elements
un = u.copy()
print u

for n in range (0,nt):
  un = u.copy()
  for i in range (1,nx):
    u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])

plt.plot(np.linspace(0,2,nx),u)       # First two parameters just give scale of the graph
plt.savefig('plot_6')

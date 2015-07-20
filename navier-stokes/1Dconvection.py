# My implementation for solving the navier stokes equations using Python

import numpy
import mathplotlib.pyplot
import time, sys

print 'Hello'

#%matplotlib inline # for avoiding a new window

numx = 41  # Number of grid points
distx = float(4./(numx-1))
numt = 25
deltat = 0.25
c = 1 # wavenumber

u = numpy.ones(nx)
u[.5/distx : 1/distx +1]=2
print u
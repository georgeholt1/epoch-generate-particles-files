# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

This file should contain a 3-dimensional particle number density distribution as
a Python function called number_density_3d. 
"""
import numpy as np

def gaussian(x, x0, w):
    '''A simple Gaussian function centred on x0 with waist w.'''
    return np.exp(-(x - x0) ** 2 / (w ** 2))

def number_density_3d(x, y, z):
    '''Return particle number density for given x-y-z-coordinate.'''
    return 1e25 * gaussian(x, 0.2e-6, 1e-6) * gaussian(y, -0.1e-6, 0.5e-6) * \
           gaussian(z, 0.3e-6, 0.7e-6)
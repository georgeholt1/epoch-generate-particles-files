# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

This file should contain a 1-dimensional particle number density distribution as
a Python function called number_density_1d. 
"""
import numpy as np

def number_density_1d(x):
    '''Return particle number density for a value of x-position.'''
    return 1e25 * np.exp(-(x ** 2) / (1e-6) ** 2)
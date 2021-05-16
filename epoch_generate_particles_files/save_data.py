# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

Functions to save the generated data.
"""
import numpy as np
import os

def save_1d(x_list, w_list, out_dir):
    '''Save 1D particle data.
    
    Parameters
    ----------
    x_list : list
        List of x-coordinate values.
    w_list : list
        List of weight values.
    out_dir : str
        Path to output directory.
    '''
    with open(os.path.join(out_dir, 'x_data.dat'), 'wb') as f:
        f.write(np.array(x_list).tobytes())
    with open(os.path.join(out_dir, 'w_data.dat'), 'wb') as f:
        f.write(np.array(w_list).tobytes())
        
        
def save_2d(x_list, y_list, w_list, out_dir):
    '''Save 2D particle data.
    
    Parameters
    ----------
    x_list : list
        List of x-coordinate values.
    y_list : list
        List of y-coordinate values.
    w_list : list
        List of weight values.
    out_dir : str
        Path to output directory.
    '''
    with open(os.path.join(out_dir, 'x_data.dat'), 'wb') as f:
        f.write(np.array(x_list).tobytes())
    with open(os.path.join(out_dir, 'y_data.dat'), 'wb') as f:
        f.write(np.array(y_list).tobytes())
    with open(os.path.join(out_dir, 'w_data.dat'), 'wb') as f:
        f.write(np.array(w_list).tobytes())


def save_3d(x_list, y_list, z_list, w_list, out_dir):
    '''Save 3D particle data.
    
    Parameters
    ----------
    x_list : list
        List of x-coordinate values.
    y_list : list
        List of y-coordinate values.
    z_list : list
        List of z-coordinate values.
    w_list : list
        List of weight values.
    out_dir : str
        Path to output directory.
    '''
    with open(os.path.join(out_dir, 'x_data.dat'), 'wb') as f:
        f.write(np.array(x_list).tobytes())
    with open(os.path.join(out_dir, 'y_data.dat'), 'wb') as f:
        f.write(np.array(y_list).tobytes())
    with open(os.path.join(out_dir, 'z_data.dat'), 'wb') as f:
        f.write(np.array(z_list).tobytes())
    with open(os.path.join(out_dir, 'w_data.dat'), 'wb') as f:
        f.write(np.array(w_list).tobytes())
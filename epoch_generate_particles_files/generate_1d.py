# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

This generates particle data by sampling a 1-dimensional number density
distribution.
"""
import numpy as np

try:
    from distributions.d1 import number_density_1d
except ImportError:
    raise SystemExit("Failed to import number density distribution function.")



def generate_1d(xmin, xmax, nx, ppc, progress=False, n_min=0, vis_samples=1000):
    '''Generate particles in 1D space.
    
    Parameters
    ----------
    xmin, xmax : float
        Boundaries in the x-direction.
    nx : int
        Number of cells in the x-direction.
    ppc : int
        Number of particles per cell.
    progress : bool, optional
        Whether or not to print a progress bar with tqdm. Defaults to False.
    n_min : float, optional
        Minimum number density value. Particles are not generated if the number
        density at the sample point is lower than this threshold. Defaults to
        zero (i.e. particles are created at all sample positions; even ones
        with zero weight).
    vis_samples : int, optional
        How many data points to use to plot the number density distribution.
        Defaults to 1000.
    '''
    # generate visualisation
    x_vis = np.linspace(xmin, xmax, vis_samples)
    n_vis = number_density_1d(x_vis)
    
    cell_size_x = (xmax - xmin) / nx
    cell_vol = cell_size_x

    # initialise lists to be populated
    x_list = []  # x-positions
    n_list = []  # number density values
    w_list = []  # weights
    
    # start at the lower boundary
    x_current = xmin
    
    # sample the cells
    if progress:
        try: 
            from tqdm import tqdm
        except ImportError:
            print("No tqdm found.")
            progress = False
    if progress:
        pbar = tqdm(total=np.ceil((xmax-xmin)/cell_size_x))
    while x_current < xmax:
        # randomly sample cell space
        x_rands = np.random.uniform(0, cell_size_x, ppc)
        x_rands += x_current
        
        # get number density values
        n_samp = number_density_1d(x_rands)
        
        # add particles to list if they exceed the minimum n
        for i in range(ppc):
            if n_samp[i] >= n_min:
                x_list.append(x_rands[i])
                n_list.append(n_samp[i])
                w_list.append(n_samp[i] * cell_vol / ppc)
        
        x_current += cell_size_x
        
        if progress:
            pbar.update(1)

    return x_vis, n_vis, x_list, n_list, w_list
# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

This generates particle data by sampling a 2-dimensional number density
distribution.
"""
import numpy as np

try:
    from distributions.d2 import number_density_2d
except ImportError:
    raise SystemExit("Failed to import number density distribution function.")

def generate_2d(xmin, xmax, ymin, ymax, nx, ny, ppc, progress=False, n_min=0,
                vis_samples_x=1000, vis_samples_y=1000):
    '''Generate particles in 2D space.
    
    Parameters
    ----------
    xmin, xmax : float
        Boundaries in the x-direction.
    ymin, ymax : float
        Boundaries in the y-direction.
    nx, ny : int
        Number of cells in the x- and y-direction.
    ppc : int
        Number of particles per cell.
    progress : bool, optional
        Whether or not to print a progress bar with tqdm. Defaults to False.
    n_min : float, optional
        Minimum number density value. Particles are not generated if the number
        density at the sample point is lower than this threshold. Defaults to
        zero (i.e. particles are created at all sample positions; even ones
        with zero weight).
    vis_samples_x, vis_samples_y : int, optional
        How many data points to use to plot the number density distribution in
        the x- and y-direction. Defaults to 1000.
    '''
    # generate visualisation
    x_vis = np.linspace(xmin, xmax, vis_samples_x).reshape((1, vis_samples_x))
    y_vis = np.linspace(ymin, ymax, vis_samples_y).reshape((vis_samples_y, 1))
    n_vis = number_density_2d(x_vis, y_vis)
    
    cell_size_x = (xmax - xmin) / nx
    cell_size_y = (ymax - ymin) / ny
    cell_vol = cell_size_x * cell_size_y

    # initialise lists to be populated
    x_list = []
    y_list = []
    n_list = []
    w_list = []
    
    # start at lower boundary
    x_current = xmin
    y_current = ymin

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
        while y_current < ymax:
            # randomly sample cell space
            x_rands = np.random.uniform(0, cell_size_x, ppc)
            x_rands += x_current
            y_rands = np.random.uniform(0, cell_size_y, ppc)
            y_rands += y_current
            
            # get number density values
            n_samp = number_density_2d(x_rands, y_rands)
            
            # add particles to list if they exceed the minimum n
            for i in range(ppc):
                if n_samp[i] >= n_min:
                    x_list.append(x_rands[i])
                    y_list.append(y_rands[i])
                    n_list.append(n_samp[i])
                    w_list.append(n_samp[i] * cell_vol / ppc)
            
            y_current += cell_size_y
        y_current = ymin
        x_current += cell_size_x
        
        if progress:
            pbar.update(1)
        
    return x_vis, y_vis, n_vis, x_list, y_list, n_list, w_list
# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

This generates particle data by sampling a 3-dimensional number density
distribution.
"""
import numpy as np

try:
    from distributions.d3 import number_density_3d
except ImportError:
    raise SystemExit("Failed to import number density distribution funciton.")

def generate_3d(xmin, xmax, ymin, ymax, zmin, zmax, nx, ny, nz, ppc,
                progress=False, n_min=0):
    '''Generate particles in 3D space.
    
    Parameters
    ----------
    xmin, xmax : float
        Boundaries in the x-direction.
    ymin, ymax : float
        Boundaries in the y-direction.
    zmin, zmax : float
        Boundaries in the z-direction.
    nx, ny, nz : int
        Number of cell in the x-, y- and z-directions.
    ppc : int
        Number of particles per cell.
    progress : bool, optional
        Whether or not to print a progress bar with tqdm. Defaults to False.
    n_min : float, optional
        Minimum number density value. Particles are not generated if the number
        density at the sample point is lower than this threshold. Defaults to
        zero (i.e. particles are created at all sample positions; even ones
        with zero weight).
    '''
    cell_size_x = (xmax - xmin) / nx
    cell_size_y = (ymax - ymin) / ny
    cell_size_z = (zmax - zmin) / nz
    cell_vol = cell_size_x * cell_size_y * cell_size_z

    # initialise lists to be populated
    x_list = []
    y_list = []
    z_list = []
    n_list = []
    w_list = []
    
    # start at lower boundary
    x_current = xmin
    y_current = ymin
    z_current = zmin    
    
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
            while z_current < zmax:
                # randomly sample cell space
                x_rands = np.random.uniform(0, cell_size_x, ppc)
                x_rands += x_current
                y_rands = np.random.uniform(0, cell_size_y, ppc)
                y_rands += y_current
                z_rands = np.random.uniform(0, cell_size_z, ppc)
                z_rands += z_current

                # get number density values
                n_samp = number_density_3d(x_rands, y_rands, z_rands)
                
                # add particles to list if they exceed the minimum n
                for i in range(ppc):
                    if n_samp[i] >= n_min:
                        x_list.append(x_rands[i])
                        y_list.append(y_rands[i])
                        z_list.append(z_rands[i])
                        n_list.append(n_samp[i])
                        w_list.append(n_samp[i] * cell_vol / ppc)
                        
                z_current += cell_size_y
            z_current = zmin
            y_current += cell_size_y
        y_current = ymin
        x_current += cell_size_x

        if progress:
            pbar.update(1)
    
    return x_list, y_list, z_list, n_list, w_list
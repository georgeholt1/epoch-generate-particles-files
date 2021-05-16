# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

Functions to plot distributions and samples.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os


def plot_1d(x_vis, n_vis, x_list, n_list, out_dir):
    '''Plot the distribution and sampled number density values.
    
    Parameters
    ----------
    x_vis : list
        List of x-coordinate values for the distribution.
    n_vis : list
        List of number density values corresponding to x_vis.
    x_list : list
        List of sampled x-coordinate values.
    n_list : list
        List of number density values corresponding to x_list.
    out_dir : str
        Path to output directory.
    '''
    fig, ax = plt.subplots()
    ax.plot(x_vis, n_vis, '-', label='Distribution')
    ax.plot(x_list, n_list, 'o', alpha=0.5, label='Samples')
    ax.legend()
    ax.grid()
    ax.set_xlabel('$x$ (m)')
    ax.set_ylabel('$n$ $m^{-3}$')
    ax.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, 'dist-1D.png'))
    plt.close('all')
    
    
def plot_2d(x_vis, y_vis, n_vis, x_list, y_list, n_list, out_dir):
    '''Plot the distribution and sampled number density values.
    
    Parameters
    ----------
    x_vis, y_vis : list
        List of x- and y-coordinate values for the distribution.
    n_vis : list
        List of number density values corresponding to x_vis and y_vis.
    x_list, y_list : list
        List of sample x- and y-coordinate values.
    n_list : list
        List of number density values corresponding to x_list and y_list.
    out_dir : str
        Path to output directory.
    '''
    fig, (ax1, ax2) = plt.subplots(1, 2)
    divider = make_axes_locatable(ax1)
    cax1 = divider.append_axes('right', size='5%', pad=0.06)
    divider = make_axes_locatable(ax2)
    cax2 = divider.append_axes('right', size='5%', pad=0.06)
    
    im = ax1.pcolormesh(x_vis, y_vis, n_vis)
    ax1.set_xlabel('$x$ (m)')
    ax1.set_ylabel('$y$ (m)')
    cbar1 = fig.colorbar(im, cax=cax1, orientation='vertical')
    cbar1.set_label('$n$ (m$^{-3}$)')
    
    sc = ax2.scatter(x_list, y_list, c=n_list)
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_ylim(ax1.get_ylim())
    ax2.set_xlabel('$x$ (m)')
    ax2.set_ylabel('$y$ (m)')
    cbar2 = fig.colorbar(sc, cax=cax2, orientation='vertical')
    cbar2.set_label('$n$ (m$^{-3}$)')
    
    ax1.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
    ax2.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
    
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, 'dist-2D.png'))
    plt.close('all')
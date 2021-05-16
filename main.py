# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

This is the main file, used to generate the particles binary files to be passed
to EPOCH.
"""
import numpy as np
import matplotlib.pyplot as plt

from epoch_generate_particles_files.parse_args import (
    create_parser, check_valid_args)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    valid, err_msg = check_valid_args(args)
    if not valid:
        raise SystemExit(err_msg)
    
    # generate, save, and (optionally) plot the distributions.
    if args.dimensions == 1:
        print("Generating 1D particle distribution.")
        
        from epoch_generate_particles_files.generate_1d import generate_1d
        from epoch_generate_particles_files.save_data import save_1d
        
        x_vis, n_vis, x_list, n_list, w_list = generate_1d(
            args.xmin, args.xmax, args.nx, args.ppc, args.progress, args.nmin,
            args.visx
        )
        
        save_1d(x_list, w_list, args.outdir)
        
        if args.plot:
            from epoch_generate_particles_files.plot_distributions import plot_1d
            plot_1d(x_vis, n_vis, x_list, n_list, args.outdir)
        
    elif args.dimensions == 2:
        print("Generating 2D particle distribution.")
        
        from epoch_generate_particles_files.generate_2d import generate_2d
        from epoch_generate_particles_files.save_data import save_2d
        
        x_vis, y_vis, n_vis, x_list, y_list, n_list, w_list = generate_2d(
            args.xmin, args.xmax, args.ymin, args.ymax, args.nx, args.ny,
            args.ppc, args.progress, args.nmin, args.visx, args.visy
        )
        
        save_2d(x_list, y_list, w_list, args.outdir)
        
        if args.plot:
            print("Plotting.")
            from epoch_generate_particles_files.plot_distributions import plot_2d
            plot_2d(x_vis, y_vis, n_vis, x_list, y_list, n_list, args.outdir)
            
    else:
        print("Generating 3D particle distribution.")
        
        from epoch_generate_particles_files.generate_3d import generate_3d
        from epoch_generate_particles_files.save_data import save_3d
        
        x_list, y_list, z_list, n_list, w_list = generate_3d(
            args.xmin, args.xmax, args.ymin, args.ymax, args.zmin, args.zmax,
            args.nx, args.ny, args.nz, args.ppc, args.progress, args.nmin
        )
        
        save_3d(x_list, y_list, z_list, w_list, args.outdir)
        
        if args.plot:
            print("Visualisation not currently implemented for 3D.")
    
    print("Done.")
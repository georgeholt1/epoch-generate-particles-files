# Author: George K. Holt
# License: MIT
# Version: 0.1
"""
Part of EPOCH Generate Particles Files.

Contains a function to parse arguments passed to the executable.
"""
import argparse
import os

def create_parser():
    '''Create argparse parser.'''
    parser = argparse.ArgumentParser(
        prog='EPOCH Generate Particles Files',
        description="Generate binary files of particles to be passed to EPOCH."
    )
    parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s 0.1'
    )
    parser.add_argument(
        '-d', '--dimensions', required=True, choices=[1, 2, 3], type=int,
        help="Dimensionality of the simulation. Required."
    )
    parser.add_argument(
        '-o', '--outdir', default=os.getcwd(),
        help="Directory in which to write the files. Defaults to current directory."
    )
    parser.add_argument(
        '--xmin', required=True, type=float,
        help="Minimum x-coordinate. Required."
    )
    parser.add_argument(
        '--xmax', required=True, type=float,
        help="Maximum x-coordinate. Required."
    )
    parser.add_argument(
        '--ymin', type=float,
        help="Minimum y-coordinate. Required if d={2|3}."
    )
    parser.add_argument(
        '--ymax', type=float,
        help="Maximum y-coordinate. Required if d={2|3}."
    )
    parser.add_argument(
        '--zmin', type=float,
        help="Minimum z-coordinate. Required if d=3."
    )
    parser.add_argument(
        '--zmax', type=float,
        help="Maximum z-coordinate. Required if d=3."
    )
    parser.add_argument(
        '--ppc', type=int, required=True,
        help="Particles per cell. Required."
    )
    parser.add_argument(
        '--nx', type=int, required=True,
        help="Number of cells in the x-direction. Required."
    )
    parser.add_argument(
        '--ny', type=int,
        help="Number of cells in the y-direction. Required if d={2|3}."
    )
    parser.add_argument(
        '--nz', type=int,
        help="Number of cells in the z-direction. Required if d=3."
    )
    parser.add_argument(
        '--nmin', type=float, default=0,
        help="Minimum number density to generate particles."
    )
    parser.add_argument(
        '-p', '--plot', dest='plot', action='store_true',
        help="Plot the generated distribution."
    )
    parser.add_argument(
        '--visx', type=int, default=1000,
        help="Points to plot in x."
    )
    parser.add_argument(
        '--visy', type=int, default=1000,
        help="Points to plot in y."
    )
    parser.add_argument(
        '-P', '--progress', dest='progress', action='store_true',
        help="Print a progress bar. Requires tqdm."
    )
    parser.set_defaults(plot=False, progress=False)
    
    return parser



def check_valid_args(args):
    '''Perform some checks on argument validity.
    
    Returns
    -------
    True/False for valid/invalid and error string (if applicable).
    '''
    if args.dimensions == 2 and (not args.ymin or not args.ymax):
        return (False, "2D but missing ymin and/or ymax.")
    elif args.dimensions == 3 and (not args.ymin or not args.ymax or
                                   not args.zmin or not args.zmax):
        return (False, "3D but missing ymin, ymax, zmin and/or zmax.")
    elif args.dimensions == 2 and not args.ny:
        return (False, "2D but missing ny.")
    elif args.dimensions == 3 and (not args.ny or not args.nz):
        return (False, "3D but missing ny or nz.")
    elif not os.path.isdir(args.outdir):
        return(
            False,
            f"Proposed output directory '{args.outdir}' does not exist."
        )
    else:
        return (True, None)
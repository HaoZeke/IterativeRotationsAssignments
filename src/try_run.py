#!/usr/bin/env python3
from pprint import pprint as pp
import numpy as np
from bbdir import irasort
from pathlib import Path
import ase.io as aseio


def read_xyz(fname):
    typ = np.genfromtxt(fname, skip_header=2, usecols=[0], dtype=None, encoding=None)
    coords = np.genfromtxt(fname, skip_header=2, usecols=[1, 2, 3], dtype=np.float64)
    nat = len(typ)
    return nat, typ, coords.T


ROOT = Path("/home/rgoswami/Git/Github/Fortran/IterativeRotationsAssignments/")
nat1, typ1, coords1 = read_xyz(ROOT / "examples/IRA/example_inputs/s1.xyz")
nat2, typ2, coords2 = read_xyz(ROOT / "examples/IRA/example_inputs/s2.xyz")
# print(coords1.shape)
# atm1 = aseio.read(ROOT / "examples/IRA/example_inputs/s1.xyz")
# atm2 = aseio.read(ROOT / "examples/IRA/example_inputs/s2.xyz")
# print(atm1.positions)
# print(coords1)

pp(
    irasort.cshda(
        [1] * 13,
        coords1.T.reshape(3, -1),
        [1] * 13,
        coords2.T.reshape(3, -1),
        99.9,
    )
)

#!/usr/bin/env python

import numpy as np
import parmed as pmd
from tabulate import tabulate
from pybel import readstring
from lj_parspace import PostgWrapper, units
import click_spinner
import click

@click.command()
@click.argument('wfn_file', type=click.Path(exists=True))
@click.argument('topology_file', type=click.Path(exists=True))
def main(wfn_file, topology_file):
    with click_spinner.spinner():
        postg_wrapper = PostgWrapper()
        p = postg_wrapper.execute(wfn=wfn_file)

    c6 = p.coefficients.c6.diagonal()
    c6 = np.squeeze(np.asarray(c6))

    molecule = readstring('xyz', p.molecule.write(format='xyz'))

    atom_types = {}

    top = pmd.load_file(topology_file)

    if len(top.atoms) != len(molecule.atoms):
        raise AssertionError('The number of atoms in the given topology file doesn\'t match that of the wave function')

    for index, atom in enumerate(molecule):
        top_atom = top.atoms[index]
        atom_type = top_atom.type

        if atom_type not in atom_types:
            c6_ff = 4 * top_atom.epsilon * (top_atom.sigma ** 6)
            atom_types[atom_type] = {
                'XDM': [],
                'FF': units.dispersion_coefficient_au(c6_ff)
            }

        atom_types[atom_type]['XDM'].append(c6[index] * 2)

    headers = ['AtomType', 'C6 XDM (a.u.)', 'C6 FF (a.u.)', 'STD']
    table = []

    for atom_type in atom_types:
        table.append(
            [
                atom_type,
                np.mean(atom_types[atom_type]['XDM']),
                np.mean(atom_types[atom_type]['FF']),
                np.std(atom_types[atom_type]['XDM'])
            ]
        )

    print tabulate(table, headers, tablefmt='pipe')


if __name__ == '__main__':
    main()

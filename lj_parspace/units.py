from parmed.unit import *

bohr_base_unit = BaseUnit(length_dimension, 'bohr', 'bp')
bohr_base_unit.define_conversion_factor_to(meter_base_unit, 5.29177249e-11)
bohrs = bohr = Unit({bohr_base_unit: 1.0})

hartree_base_unit = ScaledUnit(43.60e-19, joule, 'hartree', 'ha')
hartree = Unit({hartree_base_unit: 1.0})
avogadro = 6.022e23

def dispersion_coefficient_au(value):
    return (value / avogadro * md_kilocalorie * angstrom ** 6).value_in_unit( hartree * bohr ** 6)

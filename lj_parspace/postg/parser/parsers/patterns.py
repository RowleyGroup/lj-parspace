sci_number_pattern = '[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?'
atomic_symbol_pattern = '[A-Z][a-z]?'

def create_named_pattern(name, pattern):
    return '(?P<' + name + '>' + pattern + ')'

def create_sci_number_pattern(name):
    return create_named_pattern(name, sci_number_pattern)

# Regex for parsing a line of the coefficients part
coefficients_pattern = '\s*' \
                     + create_named_pattern('i', '\d+') + '\s+' \
                     + create_named_pattern('j', '\d+') + '\s+' \
                     + create_sci_number_pattern('dij') + '\s+' \
                     + create_sci_number_pattern('C6') + '\s+' \
                     + create_sci_number_pattern('C8') + '\s+' \
                     + create_sci_number_pattern('C10') + '\s+' \
                     + create_sci_number_pattern('Rc') + '\s+' \
                     + create_sci_number_pattern('Rvdw')

# Regex for parsing a line of the atoms and respective positions part
atoms_positions_pattern = '\s*' \
    + create_named_pattern('n', '\d+') + '\s+' \
    + create_named_pattern('atom', atomic_symbol_pattern) + '\s+' \
    + create_sci_number_pattern('x') + '\s+' \
    + create_sci_number_pattern('y') + '\s+' \
    + create_sci_number_pattern('z') + '\s+' \
    + create_named_pattern('nr', '\d+') + '\s+' \
    + create_named_pattern('nl', '\d+')

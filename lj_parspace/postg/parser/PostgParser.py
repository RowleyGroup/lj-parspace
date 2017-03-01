import parsers.parsers

atoms_part_header = '# n  At           x               y               z         nr    nl\n'
coefficients_part_header = '# i  j       dij            C6               C8               C10              Rc           Rvdw\n'
end_sign = '\n#\n'


def get_middle_string(string, start, end):
    return string.split(start, 1)[1].split(end)[0]


class PostgParser():
    def __init__(self, string):
        """

        :type string: str
        """
        self.string = string
        self.parse()

    def parse(self):
        self.molecule = parsers.atoms_positions_parser(self.get_atoms_part())
        self.coefficients = parsers.coefficients_parser(self.get_coefficients_part())

    def get_atoms_part(self):
        return get_middle_string(self.string, atoms_part_header, end_sign)

    def get_coefficients_part(self):
        return get_middle_string(self.string, coefficients_part_header, end_sign)

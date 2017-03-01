from subprocess import Popen, PIPE
from ..config import Config
from .parser import PostgParser

class PostgWrapper:
    def execute(self, **kwargs):
        """
        Executes postg calculation on the given wfn

        :param kwargs:

        :return: PostgParser
        """
        config = kwargs.get('config', Config())
        postg_executable = config.get('postg_path')
        chf = kwargs.get('chf', 'pbe0')
        a1 = kwargs.get('a1', '0.754')
        a2 = kwargs.get('a2', '1.102')
        file = kwargs.get('wfn')

        process = Popen([postg_executable, a1, a2, file, chf], stdout=PIPE)
        process.wait()
        output = process.communicate()[0]
        parser = PostgParser(output)
        return parser

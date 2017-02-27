import unittest
from lj_parspace.config import Config, defaults


class TestUtils(unittest.TestCase):
    """
    Test config.
    """

    def setUp(self):
        pass

    def test_default_config(self):
        """
        It should return all the default values for each available default config
        """
        config = Config()
        for default in defaults:
            self.assertEqual(
                defaults[default],
                config.get(default)
            )

import os
from ConfigParser import SafeConfigParser

DEFAULT_CONFIG_FILE = os.path.expanduser(os.path.join("~", ".ljparspace.cfg"))

defaults = {
    'postg_path': '/usr/bin/postg'
}


class Config:
    def __init__(self, **kwargs):
        self.file = kwargs.get('filename', DEFAULT_CONFIG_FILE)

    def setup(self):
        config = SafeConfigParser(defaults)

        with open(self.file, 'wb') as configfile:
            config.write(configfile)

    def get(self, key):
        """
        Get configuration by the given value

        :param key: The key (e.g. postg_path)
        :type key: str
        :return:
        """
        config = SafeConfigParser(defaults)
        config.read(self.file)

        return config.get('DEFAULT', key)

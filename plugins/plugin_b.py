import plugins
import os


class Plugin(plugins.Base):

    def __init__(self):
        self.name = os.path.basename(__file__)
        pass

    def start(self):
        print(f"Plugin {self.name}")

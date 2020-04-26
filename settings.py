from configparser import ConfigParser


class Settings:
    config = ConfigParser()
    file = "settings/config.ini"

    def __init__(self):
        self.settings = self.config.read(self.file)
        if len(self.settings) == 0:
            self.initialize_default_settings()

    def initialize_default_settings(self):
        self.config.read(self.file)
        self.config.add_section("Sound")
        self.config.set("Sound", "volume", "1.0")
        self.config.set("Sound", "speech rate", "120")
        with open(self.file, "w") as f:
            self.config.write(f)

    def getVolume(self):
        return self.config.getfloat("Sound", "volume")

    def getRate(self):
        return self.config.getint("Sound", "speech rate")




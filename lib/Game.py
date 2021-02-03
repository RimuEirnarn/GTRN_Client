"""Game Module"""
from os.path import exists, realpath
from json import loads, dumps


def install():
    if exists(realpath("settings.json")):
        return True
    else:
        data = {"Level": 1, "UseGTRNServer": False, "Port": 7880, "Version": "1.0.0"}
        open(realpath("settings.json"), "w").write(dumps(data, indent=4))


class Settings:
    def __init__(self):
        install()
        self.__dict__.update(loads(open(realpath("settings.json")).read()))
        self.raw_data = loads(open(realpath("settings.json")).read())
        if "Port" not in self.__dict__:
            self.__dict__["Port"] = 7880
            self.raw_data["Port"] = 7880

    def write(self):
        open("settings.json", "w").write(dumps(self.raw_data, indent=4))

    def __getitem__(self, item):
        """Get a raw item from raw data"""
        return self.raw_data[item]

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __repr__(self):
        return 'Settings()'

    def contains(self, item):
        return item in self.raw_data

    def put(self, key, content):
        self.__dict__[key] = content

    def remove(self, key):
        del self.__dict__[key]

    def items(self):
        return self.raw_data.items()

    @classmethod
    def read(cls):
        return loads(open(realpath("settings.json")).read())


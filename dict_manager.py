import json
import pathlib

class DictManager:
    def __init__(self):
        self.__path
        self.__config
        self.__load_config()

    def __load_config(self):
        my_file = pathlib.Path("/Documents")
        if my_file.is_file():
            my_file = json.load()
            return my_file

        return []

    def __save_config(self):
        with open("config.json", "w") as outfile:
            json_dump = json.dumps(self.config)
            outfile.write(json_dump)
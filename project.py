import sys
import argparse
import yaml # Might use for config?
from pathlib import Path # Might use for file operations?

class Morse:
    def __init__(self, database:str = 'morse.yaml'):
        # Import YAML file with morse data
        with open(database) as file:
            self.lookup = yaml.load(file, Loader=yaml.BaseLoader)
            if not all(len(c) == 1 and isinstance(c) == str for c in self.lookup):
                raise ValueError('All keys in .yaml file must be a char.')

        # If exists, import profile defaults from the correct directory.    
        self.dot = '.'
        self.dash= '-'




        # default_file will be a 
    def txt_to_morse(self, txt: str):
        to_return = ''
        for c in txt:
            if c in self.lookup:
                to_return += self.lookup[c]

        return to_return

    def morse_to_txt(self, morse: str):
        ...

    @classmethod
    def touch_config():
        # Create config file if it doesn't exist
        ...




def main():
    m = Morse()


if __name__ == '__main__':
    main()

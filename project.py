#import sys
#import argparse
import yaml # Might use for config?
#from pathlib import Path # Might use for file operations?

class Morse:
    def __init__(self, db:str = 'morse.yaml'):
        '''Initialize Morse class.
        Takes in a reference to a .yaml file or dictionary of single character keys.'''
        # Import YAML file with morse data
        with open(db, mode='r') as file:
            self.lookup = yaml.load(file, Loader=yaml.BaseLoader)
            if not all(len(ch) == 1 and isinstance(ch) == str for ch in self.lookup):
                raise ValueError('All keys in .yaml file must be a char.')

        # If exists, import profile defaults from the correct directory.
        self.dot = '.'
        self.dash= '-'

    def txt_to_morse(self, txt: str) -> str:
        '''Given a string of text, use lookup array to generate morse code equivalent of text.'''
        to_return = ''
        for c in txt:
            if c in self.lookup:
                to_return += self.lookup[c] 

        return to_return

    def morse_to_txt(self, morse: str) -> str:
        '''Given a string of morse, use lookup array to generate text equivalent.'''
        ...

    @classmethod
    def touch_config():
        '''Creates configuration file and prints its location on disk.
        May remove.'''
        # Create config file if it doesn't exist
        ...


def main():
    morse = Morse()


if __name__ == '__main__':
    main()

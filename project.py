'''Morse Code converter.
Given a text file or string with text or morse,
the user is returned a string of the opposite type.'''
#import sys
#import argparse
import yaml # Might use for config?
#from pathlib import Path # Might use for file operations?

class Morse:
    '''Functional component of project.py.
        txt_to_morse: given text, return morse code equivalent.
        morse_to_txt: given morse, return text equivalent.
        @class touch_config: creates config file if it doesn\'t exist.'''
    def __init__(self, data:str = 'morse.yaml'):
        # Import YAML file with morse data
        with open(data, mode='r', encoding='utf-8') as file:
            self.lookup = yaml.load(file, Loader=yaml.BaseLoader)
            if not all(len(ch) == 1 and isinstance(ch) == str for ch in self.lookup):
                raise ValueError('All keys in .yaml file must be a char.')

        # If exists, import profile defaults from the correct directory.
        self.dot = '.'
        self.dash= '-'

    def txt_to_morse(self, txt: str) -> str:
        '''Given a string of text, use lookup array to generate morse code equivalent of text.'''
        to_return = ''
        for char in txt:
            if char in self.lookup:
                to_return += self.lookup[char]

        return to_return

    def morse_to_txt(self, morse: str) -> str:
        '''Given a string of morse, use lookup array to generate text equivalent.'''

    @classmethod
    def touch_config(cls):
        '''Creates configuration file and prints its location on disk.
        May remove.'''
        # Create config file if it doesn't exist


def main():
    '''Called on program start.'''
    morse = Morse()
    morse.txt_to_morse("SOS")


if __name__ == '__main__':
    main()

"""Morse Code converter.
Given a text file or string with text or morse,
the user is returned a string of the opposite type."""
# import sys
import argparse
import yaml  # Might use for config?

class Morse:
    '''Functional component of project.py.
    txt_to_morse: given text, return morse code equivalent.
    morse_to_txt: given morse, return text equivalent.
    @class touch_config: creates config file if it doesn\'t exist.'''

    # TODO: Import dict separate from .yaml 
    def __init__(self, data: str = "morse.yaml"):
        with open(data, mode="r", encoding="utf-8") as file:
            self.lookup = yaml.load(file, Loader=yaml.BaseLoader)
            if not all(len(ch) == 1 and isinstance(ch, str) for ch in self.lookup):
                raise ValueError("All keys in .yaml file must be a char.")

    def txt_to_morse(self, txt: str) -> str:
        '''Given a string of text, use lookup array to generate morse code equivalent of text.'''
        to_return = ''
        for char in txt.upper():
            if char in self.lookup:
                to_return += self.lookup[char] + ' '
            else:
                to_return += char

        return to_return.rstrip('/ ')

    # TODO: Future refactor
    def morse_to_txt(self, morse: str) -> str:
        '''Given a string of morse, use lookup array to generate text equivalent.'''
        # May change this
        if len(morse) == 0:
            return ''
        morse_chars = morse.split(" ")
        to_return = str()
        for char in morse_chars:
            try:
                to_return += next(
                    key for key, value in self.lookup.items() if value == char
                )
            except StopIteration:
                to_return += '�'

        return to_return

    def auto_conv(self, string: str) -> str:
        # Take in a string, determine the type if possible
        # Assume 
        ...

def main():
    parser = make_parser()
    args = parser.parse_args()
    words = ' '.join(args.words)

    morse = Morse()
    if args.text:
        print(morse.morse_to_txt(words))
    elif args.morse:
        print(morse.txt_to_morse(words))
    else:
        print(morse.auto_conv(words))


def make_parser():
    '''Called on program start.'''
    # Convert multiple arguments into single string
    parser = argparse.ArgumentParser(
        description='Convert between morse and text. Will automatically guess the input type, but can be overridden.'
    )
    parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')
    # Verbose
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='increase output verbosity'
    )
    # Type Hint
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--text', action='store_true', help='source is text. Convert to morse')
    group.add_argument('-m', '--morse', action='store_true', help='source is morse. Convert to text')
    # String input
    parser.add_argument('words', type=str, nargs='+', help='morse or txt source to convert')

    # TODO: What to do with errors? Pass, Print, Raise? Default: Print invalid char

    return parser


def touch_config():
    '''Creates configuration file and prints its location on disk.
    May remove.'''
    ...

if __name__ == '__main__':
    main()

"""Morse Code converter.
Given a text file or string with text or morse,
the user is returned a string of the opposite type."""
# import sys
import argparse
import yaml  # Might use for config?

# from pathlib import Path # Might use for file operations?


class Morse:
    """Functional component of project.py.
    txt_to_morse: given text, return morse code equivalent.
    morse_to_txt: given morse, return text equivalent.
    @class touch_config: creates config file if it doesn\'t exist."""

    # TODO: make setter for dot and dash, data is a dictionary.
    # Type parameter with 'auto', 'a' 'text', 't' and 'file', 'f' selectable modes.
    def __init__(self, data: str = "morse.yaml"):
        with open(data, mode="r", encoding="utf-8") as file:
            self.lookup = yaml.load(file, Loader=yaml.BaseLoader)
            if not all(len(ch) == 1 and isinstance(ch, str) for ch in self.lookup):
                raise ValueError("All keys in .yaml file must be a char.")

    def txt_to_morse(self, txt: str) -> str:
        """Given a string of text, use lookup array to generate morse code equivalent of text."""
        to_return = ""
        for char in txt.upper():
            if char in self.lookup:
                to_return += self.lookup[char] + " "
            else:
                to_return += char

        return to_return.rstrip("/ ")

    # TODO: Future refactor
    def morse_to_txt(self, morse: str) -> str:
        """Given a string of morse, use lookup array to generate text equivalent."""
        # May change this
        if len(morse) == 0:
            return ''
        morse_chars = morse.split(" ")
        to_return = ""
        for char in morse_chars:
            try:
                to_return += next(
                    key for key, value in self.lookup.items() if value == char
                )
            except StopIteration:
                to_return += "�"

        return to_return

    @classmethod
    def touch_config(cls):
        """Creates configuration file and prints its location on disk.
        May remove."""
        # Create config file if it doesn't exist


def main():
    """Called on program start."""
    parser = argparse.ArgumentParser(description="Convert between morse and text.")
    parser.add_argument("input", help="Text to convert")
    parser.add_argument("-d", "--dot")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="increase output verbosity"
    )
    morse = Morse()
    # args = parser.parse_args()

    # print(morse.txt_to_morse(args.input))

    print(morse.txt_to_morse("SOS uh sos"))
    print(morse.morse_to_txt(""))


if __name__ == "__main__":
    main()

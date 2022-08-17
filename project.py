"""Morse Code converter.
Given a text file or string with text or morse,
the user is returned a string of the opposite type."""
# import sys
import argparse
import yaml  # Might use for config?

LOOKUP_DIR = 'morse.yaml'


class Morse:
    """Functional component of project.py.
    txt_to_morse: given text, return morse code equivalent.
    morse_to_txt: given morse, return text equivalent.
    """

    def __init__(self, data: dict, err_mode: str = "p"):
        self.lookup = data

    @property
    def lookup(self):
        """Stores a dictionary of key-value pairs.
        all keys must be a single character."""
        return self._lookup

    @lookup.setter
    def lookup(self, l):
        if not all(len(ch) == 1 and isinstance(ch, str) for ch in l):
            raise ValueError("All keys must be a char.")
        self._lookup = l

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
            return ""
        morse_chars = morse.split(" ")
        to_return = str()
        for char in morse_chars:
            try:
                to_return += next(
                    key for key, value in self.lookup.items() if value == char
                )
            except StopIteration:
                to_return += "�"

        return to_return

    def auto_conv(self, inp: str) -> str:
        """Take in a string, determine the type if possible"""
        res = all(char in " /-." for char in inp)
        return self.morse_to_txt(inp) if res else self.txt_to_morse(inp)


def main():
    parser = make_parser()
    args = parser.parse_args()
    words = " ".join(args.words)

    with open(LOOKUP_DIR, mode="r", encoding="utf-8") as file:
        lookup = yaml.load(file, Loader=yaml.BaseLoader)

    print (args.errmode)
    morse = Morse(lookup)
    if args.morse:
        print(morse.morse_to_txt(words))
    elif args.text:
        print(morse.txt_to_morse(words))
    else:
        print(morse.auto_conv(words))


def make_parser():
    """Called on program start."""
    # Convert multiple arguments into single string
    parser = argparse.ArgumentParser(
        description="Convert automatically between morse and text."
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    # Input Hint
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-t", "--text", action="store_true", help="source is text. Convert to morse"
    )
    group.add_argument(
        "-m", "--morse", action="store_true", help="source is morse. Convert to text"
    )
    # String input
    parser.add_argument(
        "words", type=str, nargs="+", help="morse or txt source to convert"
    )

    parser.add_argument("-e", "--errmode", default="print", choices=["ignore","print", "raw" ,"err"])

    return parser


if __name__ == "__main__":
    main()

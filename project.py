"""Morse Code converter.
Given a text file or string with text or morse,
the user is returned a string of the opposite type."""
# import sys
import argparse
import yaml  # Might use for config?

LOOKUP_DIR = "morse.yaml"
ERR_OPTIONS = ["pass", "print", "raw", "err"]


class Morse:
    """Functional component of project.py.
    txt_to_morse: given text, return morse code equivalent.
    morse_to_txt: given morse, return text equivalent.
    """

    def __init__(self, data: dict, err_mode: str = "print"):
        self.lookup = data
        self.err_mode = err_mode

    def txt_to_morse(self, txt: str) -> str:
        """Given a string of text, use lookup array to generate morse code equivalent."""
        to_return = ""
        for char in txt.upper():
            if char in self.lookup:
                to_return += self.lookup[char] + " "
            else:
                to_return += self.err_handle(char)

        return to_return.rstrip("/ ")

    def morse_to_txt(self, morse: str) -> str:
        """Given a string of morse, use lookup array to generate text equivalent."""
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
                to_return += self.err_handle(char)

        return to_return

    def err_handle(self, txt: str) -> str:
        """Based on self.error_mode, will return a string handling the input text."""
        match self.err_mode:
            case "pass":
                return str()
            case "print":
                return "�"
            case "raw":
                return f"{{{txt}}}"
            case "err":
                raise ValueError(f"input: {txt} is not valid.")
            case _:
                raise SyntaxError

    def auto_conv(self, inp: str) -> str:
        """Take in a string, determine the type if possible"""
        res = all(char in " /-." for char in inp)
        return self.morse_to_txt(inp) if res else self.txt_to_morse(inp)

    # Class Methods
    @classmethod
    def load_yaml(cls, yaml_dir: str) -> dict:
        """Given a .yaml file location, will generate a"""
        with open(yaml_dir, mode="r", encoding="utf-8") as file:
            lookup = yaml.load(file, Loader=yaml.BaseLoader)

        return lookup

    # Setters and getters
    @property
    def err_mode(self) -> str:
        """Stores mode used for input operations"""
        return self._err_mode

    @err_mode.setter
    def err_mode(self, mode: str):
        if mode not in ERR_OPTIONS:
            raise ValueError("Invalid error parameter.")
        self._err_mode = mode

    @property
    def lookup(self) -> str:
        """Stores a dictionary of key-value pairs.
        all keys must be a single character."""
        return self._lookup

    @lookup.setter
    def lookup(self, lookup: str):
        if not all(len(ch) == 1 and isinstance(ch, str) for ch in lookup):
            raise ValueError("All keys must be a char.")
        self._lookup = lookup


def main():
    """Code introduction, run when project called directly."""
    parser = make_parser()
    args = parser.parse_args()
    words = args.words

    morse = Morse(Morse.load_yaml(LOOKUP_DIR), err_mode=args.err_handle)
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
    group_hint = parser.add_mutually_exclusive_group()
    group_hint.add_argument(
        "-t", "--text", action="store_true", help="source is text. Convert to morse"
    )
    group_hint.add_argument(
        "-m", "--morse", action="store_true", help="source is morse. Convert to text"
    )
    # String input
    parser.add_argument("words", type=str, help="morse or txt source to convert")
    # Alternative:
    # -r        --raw
    # -e        --err
    # -i        --ignore
    # -p        --print (default)
    parser.add_argument(
        "-e",
        "--err_handle",
        default="print",
        choices=ERR_OPTIONS,
        help="change invalid character handler.",
    )

    return parser


if __name__ == "__main__":
    main()

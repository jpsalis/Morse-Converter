"""Tests project.py file in same directory"""
from project import Morse

LOOKUP_DIR = "morse.yaml"


def test_txt_to_morse():
    """tests txt_to_morse function from project file"""
    morse = Morse(Morse.load_yaml(LOOKUP_DIR))
    assert morse.txt_to_morse("SOS") == "... --- ..."
    assert morse.txt_to_morse("") == ""
    assert morse.txt_to_morse("SOS SOS") == "... --- ... / ... --- ..."
    assert morse.txt_to_morse("TEST SENTENCE") == "- . ... - / ... . -. - . -. -.-. ."


def test_morse_to_txt():
    """tests morse_to_txt function from project file"""
    morse = Morse(Morse.load_yaml(LOOKUP_DIR))
    assert morse.morse_to_txt("... --- ...") == "SOS"
    assert morse.morse_to_txt("") == ""
    assert morse.morse_to_txt("- . ... - / ... . -. - . -. -.-. .") == "TEST SENTENCE"
    assert morse.morse_to_txt("--.--..-.") == "�"
    assert morse.morse_to_txt("abc abcde") == "��"

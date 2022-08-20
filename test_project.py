"""Tests project.py file in same directory"""
import pytest
from project import Morse

LOOKUP_DIR = "morse.yaml"

morse = Morse(Morse.load_yaml(LOOKUP_DIR))


def test_txt_to_morse():
    """tests txt_to_morse function from project file for improper assertion"""
    assert morse.txt_to_morse("SOS") == "... --- ..."
    assert morse.txt_to_morse("") == ""
    assert morse.txt_to_morse("SOS SOS") == "... --- ... / ... --- ..."
    assert morse.txt_to_morse("TEST SENTENCE") == "- . ... - / ... . -. - . -. -.-. ."


def test_morse_to_txt():
    """tests morse_to_txt function from project file for improper assertion"""
    assert morse.morse_to_txt("... --- ...") == "SOS"
    assert morse.morse_to_txt("") == ""
    assert morse.morse_to_txt("- . ... - / ... . -. - . -. -.-. .") == "TEST SENTENCE"
    assert morse.morse_to_txt("--.--..-.") == "�"
    assert morse.morse_to_txt("abc abcde") == "��"


def test_err_handle():
    """tests err_handle from project file for improper assertion"""
    err = Morse(Morse.load_yaml(LOOKUP_DIR))
    err.err_mode = "print"
    assert err.morse_to_txt("--.--..-.") == "�"
    assert err.morse_to_txt("abc abcde") == "��"

    err.err_mode = "pass"
    assert err.morse_to_txt("--.--..-.") == ""
    assert err.morse_to_txt("abc abcde") == ""

    err.err_mode = "raw"
    assert err.morse_to_txt("--.--..-.") == r"{--.--..-.}"
    assert err.morse_to_txt("abc abcde") == r"{abc}{abcde}"

    err.err_mode = "err"
    with pytest.raises(ValueError):
        err.morse_to_txt("--.--..-.")
    with pytest.raises(ValueError):
        err.morse_to_txt("abc abcde")

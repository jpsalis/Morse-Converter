'''Tests project.py file in same directory'''
import project

def test_txt_to_morse():
    '''tests txt_to_morse function from project file'''
    morse = project.Morse()
    assert morse.txt_to_morse('SOS') == '... --- ...'
    assert morse.txt_to_morse('') == ''
    assert morse.txt_to_morse('SOS SOS') == '... --- ... / ... --- ...'
    assert morse.txt_to_morse('TEST SENTENCE') == '- . ... - / ... . -. - . -. -.-. .'

def test_morse_to_txt():
    '''tests morse_to_txt function from project file'''
    morse = project.Morse()
    assert morse.morse_to_txt('... --- ...') == 'SOS'
    assert morse.morse_to_txt('') == ''
    assert morse.morse_to_txt('- . ... - / ... . -. - . -. -.-. .') == 'TEST SENTENCE'

'''Tests project.py file in same directory for accurate output.'''
import project

def test_txt_to_morse():
    '''tests txt_to_morse function from project file'''
    morse = project()


    assert morse.txt_to_morse('--- ... ---') == 'SOS'
    assert morse.txt_to_morse('') == ''

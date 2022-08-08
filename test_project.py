import morse as m

def test_txt_to_morse():
    assert m.txt_to_morse('--- ... ---') == 'SOS'
    assert m.txt_to_morse('') == ''


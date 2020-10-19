from dotsplit import __version__, dotsplit

def test_dotsplit_version():
    assert __version__ == '0.2.1'

def test_dotsplit_splits():
    assert dotsplit('group.0.section.a.seat.3') == ['group', '0', 'section', 'a', 'seat', '3'], 'splits dot delimited strings'

def test_dotsplit_empty_given_none():
    assert dotsplit(None) == ['None'], 'returns single element array of "None" given None'

def test_dotsplit_empty_given_false():
    assert dotsplit(False) == ['False'], 'returns single element array of "False" given False'



# Generated at 2022-06-14 01:06:53.751227
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    code = rnd.custom_code(mask='@###')
    assert code[0] in string.ascii_uppercase
    assert code[1] in string.digits
    assert code[2] in string.digits
    assert code[3] in string.digits



# Generated at 2022-06-14 01:07:02.227166
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    code = rnd.custom_code(mask='@###')
    assert len(code) == 4
    assert code[0].isalpha()
    assert code[1:].isdigit()
    code = rnd.custom_code(mask='@@@@@')
    assert len(code) == 5
    assert code[0].isalpha()
    assert code[1:].isalpha()
    code = rnd.custom_code(mask='@@@@@@')
    assert len(code) == 6
    assert code[0].isalpha()
    assert code[1:].isalpha()


# Generated at 2022-06-14 01:07:07.282549
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random_ = Random()
    result = random_.custom_code()
    assert result == random_.custom_code() and ''.join(
            random_.custom_code(mask='@###').split('@')) == ''.join(
            result.split('@'))

# Generated at 2022-06-14 01:07:17.569497
# Unit test for method custom_code of class Random
def test_Random_custom_code():

    rnd = Random()
    rnd.seed(42)

    # Test with default values
    mask = rnd.custom_code()
    assert len(mask) == 4
    assert mask.isupper()
    assert not mask.islower()
    assert not mask.isdigit()

    # Test with placeholder for characters
    mask = rnd.custom_code(char='#')
    assert not mask.isupper()
    assert not mask.islower()
    assert len(mask) == 4
    assert mask.isdigit()

    # Test with placeholder for digits
    mask = rnd.custom_code(digit='#')
    assert not mask.isupper()
    assert not mask.islower()
    assert len(mask) == 4
    assert mask == '@@##'

    # Test with custom length

# Generated at 2022-06-14 01:07:27.099851
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method ``custom_code()`` of class ``Random``."""
    c = random.custom_code()
    assert len(c) == 10 and c.isalnum() is True

    c = random.custom_code(mask='####')
    assert len(c) == 4 and c.isdigit() is True

    c = random.custom_code(mask='@@@@')
    assert len(c) == 4 and c.isalpha() is True

    c = random.custom_code(mask='A@@@')
    assert len(c) == 4 and c[2:].isdigit() is True and c[:2].isalpha() is True

    c = random.custom_code(mask='A@@@', char='A', digit='#')
    assert len(c) == 4 and c[2:].isdigit

# Generated at 2022-06-14 01:07:29.025888
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    result = Random().custom_code(mask='@###')
    assert type(result) == str



# Generated at 2022-06-14 01:07:34.397806
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    _custom_code = random.custom_code(mask='@###-##')
    assert isinstance(_custom_code, str), 'Expected {}, got {}'.format(
        str, type(_custom_code))

    _custom_code = random.custom_code(mask='###')
    assert isinstance(_custom_code, str), 'Expected {}, got {}'.format(
        str, type(_custom_code))

    _custom_code = random.custom_code(mask='@###-##-##', char='$', digit='#')
    assert isinstance(_custom_code, str), 'Expected {}, got {}'.format(
        str, type(_custom_code))

# Generated at 2022-06-14 01:07:43.006674
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code(mask='@###', char='@', digit='#') != ''
    assert Random().custom_code(mask='@###', char='@', digit='#').isdigit() is False
    assert Random().custom_code(mask='@###', char='@', digit='#').isalpha() is False
    assert Random().custom_code(mask='@###', char='@', digit='#').isalnum() is True
    assert len(Random().custom_code(mask='@###', char='@', digit='#')) == 4
    assert len(Random().custom_code(mask='######', char='@', digit='#')) == 6
    assert len(Random().custom_code(mask='############', char='@', digit='#')) == 12

# Generated at 2022-06-14 01:07:44.217115
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random = Random()
    
    assert type(random.custom_code()) is str

# Generated at 2022-06-14 01:07:49.926692
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    custom_code_example = random.custom_code(mask='@###', char='@', digit='#')
    assert len(custom_code_example) == 4 and custom_code_example[0].isalpha() and custom_code_example[1:].isdigit()

# Generated at 2022-06-14 01:08:06.617100
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method ``custom_code()`` of class ``Random()``.

    The test checks if the method generates code,
    which consists of letters and digits and has fixed length.
    """
    # Test for wrong case
    try:
        assert random.custom_code('@###', '@', '@') is not None
    except ValueError:
        pass
    # Test for correct case
    assert random.custom_code('@###', '@', '#') is not None

# Generated at 2022-06-14 01:08:07.856282
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code() == '@QGC'

# Generated at 2022-06-14 01:08:13.641743
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """ Test method custom_code of class Random """
    mask = '@@@@-@@@@'
    code = random.custom_code(mask)
    assert isinstance(code, str)
    assert len(code) == len(mask)
    for i in code:
        assert 65 <= ord(i) <= 91

# Generated at 2022-06-14 01:08:20.908974
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert random.custom_code('vv#vv')[0:3] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert random.custom_code('vv#vv')[3].isdigit()
    assert random.custom_code('vv#vv')[4:] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert random.custom_code('vv#vv')[3].isdigit()

# Generated at 2022-06-14 01:08:29.880557
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    assert r.custom_code() == r.custom_code(), 'Code is unique'
    assert r.custom_code('@###') == r.custom_code(mask='@###'), 'Code is unique'
    assert r.custom_code('@###') != r.custom_code(mask='@@##'), 'Code is unique'
    try:
        r.custom_code(char='#', digit='#')
    except ValueError:
        raise ValueError('Error handling is incorrect!')
    try:
        r.custom_code(char='#', digit='$')
    except ValueError:
        raise ValueError('Error handling is incorrect!')

# Generated at 2022-06-14 01:08:39.024824
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    a = Random()
    mask = '@###'
    char = '@'
    digit = '#'
    b = a.custom_code(mask, char, digit)
    assert b[0] != b[1]
    assert b[2] != b[3]
    assert b[3] != b[4]
    assert b[4] != b[5]
    assert b[0].isalpha()
    assert b[0].isupper()
    assert b[1].isalpha()
    assert b[1].isupper()
    assert b[2].isdigit()
    assert b[3].isdigit()
    assert b[4].isdigit()
    assert b[5].isdigit()

# Generated at 2022-06-14 01:08:51.262303
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Test with default mask
    res = Random().custom_code()
    assert len(res) == 4
    assert res[0].isalpha()
    assert res[1:].isdigit()

    # Test with custom mask
    res = Random().custom_code(mask='@####')
    assert len(res) == 5
    assert res[0].isalpha()
    assert res[1:].isdigit()

    # Test with custom placeholders
    res = Random().custom_code(mask='@@@###', char='@', digit='#')
    assert len(res) == 6
    assert res[:3].isalpha()
    assert res[3:].isdigit()

    # Test with custom placeholders, which have the same value

# Generated at 2022-06-14 01:08:54.286090
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    a = random.custom_code()
    b = random.custom_code()
    assert a != b
    assert len(a) == len(b)

# Generated at 2022-06-14 01:09:01.545852
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code of class Random."""
    random = Random()
    random.seed(a=1)
    code = random.custom_code(mask='@@####', char='@',  digit='#')
    random.seed(a=1)
    code2 = random.custom_code(mask='@@####', char='@',  digit='#')
    assert code == code2
    # Test that all letters are uppercase
    assert all(c.isupper() for c in code)
    # Test that all places with # are digits
    assert all(c.isdigit() for c in code if c != '@')

# Generated at 2022-06-14 01:09:07.107518
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    print(Random().randstr(length=None))


if __name__ == '__main__':
    test_Random_custom_code()
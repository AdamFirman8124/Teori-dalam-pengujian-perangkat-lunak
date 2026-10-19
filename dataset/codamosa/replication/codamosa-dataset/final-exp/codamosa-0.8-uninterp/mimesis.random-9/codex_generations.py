

# Generated at 2022-06-14 01:07:05.786441
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code of class Random.

    This test generates a code that begins with a character and ends with a number.

    """
    assert random.custom_code().startswith(
        random.choice(string.ascii_uppercase)
    )
    assert random.custom_code().endswith(str(random.random()))


if __name__ == '__main__':
    test_Random_custom_code()

# Generated at 2022-06-14 01:07:17.074295
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    # mask where character and digit "mask" are the same
    mask = 'q###'
    _mask = mask.encode()
    assert len(_mask) == 4
    char = 'q'
    char_code = ord(char)
    digit = '#'
    digit_code = ord(digit)
    assert char_code == digit_code

    # mask where character and digit "mask" are different
    mask = 'q###'
    _mask = mask.encode()
    assert len(_mask) == 4
    char = 'q'
    char_code = ord(char)
    digit = '#'
    digit_code = ord(digit)
    assert char_code != digit_code

    # Length of mask not equal to 4

# Generated at 2022-06-14 01:07:19.378100
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Initialize random
    rnd = Random()
    # Generate code
    code = rnd.custom_code()
    # Test
    assert code is not None and code != ''

# Generated at 2022-06-14 01:07:31.934887
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # noinspection PyAttributeOutsideInit
    self = Random()

    self.custom_code("@@@@-###-##") == "PRZA-948-83"

    self.custom_code("@@@-@@@-####") == "HVV-LWI-4557"

    self.custom_code("@##-@##") == "P8O-W3N"

    self.custom_code("@##-@##", digit="#", char="!") == "P8O-W3N"

    self.custom_code("@##-@##", digit="!", char="!") == "P8O-W3N"

    import pytest

    with pytest.raises(ValueError):
        self.custom_code("@##-@##", digit="@", char="@")

# Generated at 2022-06-14 01:07:34.709725
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code('@###') == 'A123'
    assert Random().custom_code('@###', '$', '#') == 'A123'

# Generated at 2022-06-14 01:07:37.639184
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    a = random.custom_code('ABC###')
    assert 1 <= len(a) <= 5
    assert a[0] == 'A'
    assert a[1] == 'B'
    assert a[2] == 'C'

# Generated at 2022-06-14 01:07:41.493052
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    mask = '@###'
    char = '@'
    digit = '#'
    string = random.custom_code(mask, char, digit)
    assert len(string) == len(mask)

# Generated at 2022-06-14 01:07:44.366979
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    mask = 'A###C'
    char = 'A'
    digit = '#'

    assert len(random.custom_code(mask, char, digit)) == len(mask)

# Generated at 2022-06-14 01:07:55.904047
# Unit test for method custom_code of class Random

# Generated at 2022-06-14 01:08:09.253506
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    code = r.custom_code('###-@#')
    assert isinstance(code, str)
    assert len(code) == 6
    # Test mask
    assert code[3] == '-'
    # Test char
    assert (ord('A') <= ord(code[4]) <= ord('Z')) or \
           (ord('a') <= ord(code[4]) <= ord('z'))
    # Test digit
    assert ord('0') <= ord(code[0]) <= ord('9')
    assert ord('0') <= ord(code[1]) <= ord('9')
    assert ord('0') <= ord(code[2]) <= ord('9')
    assert ord('0') <= ord(code[5]) <= ord('9')

    r1 = Random()
    code1 = r1.custom_
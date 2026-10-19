

# Generated at 2022-06-14 01:06:54.926273
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    for _ in range(1000):
        code = rnd.custom_code('AA##')
        assert code[:2] in string.ascii_uppercase
        assert code[2:].isdigit()

# Generated at 2022-06-14 01:07:03.015633
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for ``Random.custom_code()`` method."""
    assert random.custom_code() == random.custom_code()
    assert random.custom_code(mask='@@###') == random.custom_code(mask='@@###')
    assert random.custom_code(mask='@@###', char='@') != \
           random.custom_code(mask='@@###', char='#')
    assert random.custom_code(mask='@@###', digit='#') != \
           random.custom_code(mask='@@###', digit='@')



# Generated at 2022-06-14 01:07:14.897479
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test the method custom_code of class Random."""
    # Mask with one placeholder
    assert Random().custom_code('@') == 'A'

    # Mask with identical placeholders
    with pytest.raises(ValueError):
        Random().custom_code('@##@')

    # Mask with two placeholders
    assert Random().custom_code('##') == '10'

    # Mask with three placeholders and custom placeholder for chars
    assert Random().custom_code('@@@', char='F') == 'AAA'

    # Mask with three placeholders and custom placeholder for digits
    assert Random().custom_code('@@@', digit='C') == '000'

    # Mask with three placeholders and custom placeholders for chars and digits
    assert Random().custom_code('@CC', char='F', digit='C') == 'ACC'

# Generated at 2022-06-14 01:07:27.444469
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code of class Random."""

    random_string = Random().custom_code()

    assert len(random_string) == 4
    assert random_string.isupper()

    # Test for custom placeholders
    random_string = Random().custom_code(mask='###@@', char='@', digit='%')
    assert len(random_string) == 4
    assert random_string.isupper()

    # Test for changing mask
    random_string = Random().custom_code(mask='@@@####')
    assert len(random_string) == 7

    # Exception in case of the same placeholder for both chars and digits
    try:
        Random().custom_code(char='@', digit='@')
    except ValueError:
        pass

# Generated at 2022-06-14 01:07:31.326056
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random.custom_code.__doc__
    assert isinstance(Random.custom_code(), str)

    # Test with the same placeholder
    with pytest.raises(ValueError):
        assert Random.custom_code('@###', '@', '@')



# Generated at 2022-06-14 01:07:36.356190
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    result = random.custom_code('@###')
    assert len(result) == 4
    assert result[0] in string.ascii_uppercase
    assert result[1] in string.ascii_uppercase
    assert result[2] in string.digits
    assert result[3] in string.digits


# Generated at 2022-06-14 01:07:47.782003
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Testing for method ``custom_code()``.

    :return: Nothing.
    """

    def test_is_upper(value: str) -> None:
        """Test if value of custom code is uppercase string.

        :param value: Custom code.
        """
        assert value.isupper()

    def test_not_contains_digit(value: str) -> None:
        """Test if value of custom code doesn't contain digits.

        :param value: Custom code.
        """
        assert not any(c.isdigit() for c in value)

    def test_not_contains_char(value: str) -> None:
        """Test if value of custom code doesn't contain characters.

        :param value: Custom code.
        """
        assert not any(c.isalpha() for c in value)


# Generated at 2022-06-14 01:07:51.726279
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rand_obj = Random()
    rand_obj.seed(0)
    assert rand_obj.custom_code() == 'G3U0'
    assert rand_obj.custom_code(mask='@@####') == 'QE5433'



# Generated at 2022-06-14 01:07:55.003915
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    expected_result = 'A555'
    count = 0
    for _ in range(1000):
        random_code = random.custom_code()
        if random_code == expected_result:
            count += 1
    assert count < 200

# Generated at 2022-06-14 01:08:06.585153
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code of class Random."""
    # List of masks to generate custom codes
    i = [
        ('@###', '@AA9'),
        ('@###', '@I2A'),
        ('@###', '@FUF'),
        ('@###-@###-@###', '@KP6-@ZDA-@GJ5'),
    ]
    # Generate random codes
    codes = [Random.custom_code(mask=e[0]) for e in i]

    assert len(codes) == len(i)

    for code in codes:
        assert isinstance(code, str) and code.isalnum()

# Generated at 2022-06-14 01:08:17.383872
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()

    assert r.custom_code(mask=('##@###@##')) == '20FOQL65TE'
    assert r.custom_code(mask=('@###')) == 'OR49'
    assert r.custom_code(mask=('##@@##@@')) == '40YF40YF'

# Generated at 2022-06-14 01:08:19.126184
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    object_Random = Random()
    object_Random.custom_code()

# Generated at 2022-06-14 01:08:29.954214
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code()
    assert Random().custom_code('A@@@')
    assert Random().custom_code('@@@-@@@')
    assert Random().custom_code('123456789')
    assert Random().custom_code(mask='@###', char='@', digit='#')
    assert Random().custom_code(mask='A@@@', char='A', digit='@')
    assert Random().custom_code(mask='@@@-@@@', char='@', digit='-')
    assert Random().custom_code(mask='123456789', char='1', digit='2')
    assert Random().custom_code()
    assert Random().custom_code('A@@@')
    assert Random().custom_code('@@@-@@@')
    assert Random().custom_code('123456789')
    assert Random

# Generated at 2022-06-14 01:08:37.272702
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert random.custom_code(mask='@@###') == 'F0011'
    assert random.custom_code(mask='@@@###', char='@', digit='#') == 'A00137'
    assert random.custom_code(mask='@@@###', char='@', digit='#') != 'A00137'
    assert len(random.custom_code(mask='@@@###', char='@', digit='#')) == 6

# Generated at 2022-06-14 01:08:39.193309
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code for class Random."""
    u = Random()
    r = u.custom_code()
    assert r

# Generated at 2022-06-14 01:08:47.022902
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code of class Random."""
    _random = random
    mask = '@#@####@'
    pattern = 'T[A-Z][0-9]{2}[A-Z]{4}T'
    c = 0
    while c < 100:
        _code = _random.custom_code(mask)

        import re
        assert re.match(pattern, _code) is not None

        c += 1

# Generated at 2022-06-14 01:08:55.427922
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert len(random.custom_code()) == 4
    assert len(random.custom_code('@')) == 1
    assert len(random.custom_code('@###')) == 4
    assert len(random.custom_code('@###', '#', '@')) == 1
    assert len(random.custom_code('@###', '#', '@')) == 1
    assert len(random.custom_code('####@####')) == 8
    assert random.custom_code('@###') != random.custom_code('@###')

# Generated at 2022-06-14 01:08:59.535774
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    rnd.seed(0)
    code = rnd.custom_code('@###-##-###')
    assert code == 'B063-00-847'

# Generated at 2022-06-14 01:09:02.087810
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    code = rnd.custom_code()
    assert isinstance(code, str)

# Generated at 2022-06-14 01:09:12.373680
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    assert Random.custom_code('', '@', '#') == ''
    assert Random.custom_code('A###', '@', '#') == 'A###'
    assert Random.custom_code('A###P#', '@', '#') == 'A###P#'
    assert Random.custom_code('A###P#', 'w', '#') == 'A###P#'
    assert Random.custom_code('A###P#', 'w', 'w') == 'A###P#'
    assert Random.custom_code('P#A###', '@', '#') == 'P#A###'
    assert Random.custom_code('P#A###', 'w', '#') == 'P#A###'
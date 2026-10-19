

# Generated at 2022-06-14 01:07:00.007370
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method ``_custom_code()`` of class ``Random()``.

    :return: True if test fails, otherwise False.
    """
    def test_case(pattern: str,
                  mask: str = '@####',
                  char: str = '@',
                  digit: str = '#') -> bool:
        """Test case helper.

        :param pattern: Pattern of string. It can be letters, digits or combination.
        :param mask: Mask of string. Default is '@####'.
        :param char: Placeholder for characters. Default is '@'.
        :param digit: Placeholder for digits. Default is '#'.
        :return: True if test fails, otherwise False.
        """
        value = random.custom_code(mask, char, digit)

# Generated at 2022-06-14 01:07:05.147287
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    code = r.custom_code()

    # assert it has only uppercase letters and digits
    assert all(i.isupper() or i.isdigit() for i in code)


# Generated at 2022-06-14 01:07:14.133590
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    r = Random()
    r_code = r.custom_code(mask='AB12', char='A', digit='B')
    if not (r_code[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and
            r_code[1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and
            r_code[2] in '0123456789' and
            r_code[3] in '0123456789'):
        raise AssertionError('Not correct random code.')

# Generated at 2022-06-14 01:07:24.639150
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    rnd = Random(3)
    assert rnd.custom_code(mask='@####') == 'J9701'
    assert rnd.custom_code(mask='@##@') == 'ULK7'
    assert rnd.custom_code(mask='##@@') == '13KF'
    assert rnd.custom_code(mask='###@') == '627L'
    assert rnd.custom_code(mask='##@') == '60K'
    assert rnd.custom_code(mask='#@#', char='#', digit='@') == '6H4'
    assert rnd.custom_code(mask='#@#', char='#') == '2I9'

# Generated at 2022-06-14 01:07:31.781398
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    print(rnd.custom_code())
    print(rnd.custom_code(mask='#-#-@'))
    print(rnd.custom_code('@@@@@@#'))
    print(rnd.custom_code('@@@@@@#', char='@', digit='#'))
    print(rnd.custom_code('@@@@@@', char='@', digit='#'))
    print(rnd.custom_code('@@@@@@', char='*', digit='#'))

# Generated at 2022-06-14 01:07:34.662231
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Expected result
    expected = 'qWD2'

    # Check that the result is equal to the expected
    assert Random().custom_code(mask='@###') == expected

# Generated at 2022-06-14 01:07:43.137268
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method generate_custom_code."""
    random_object = Random()
    custom_code = random_object.custom_code()

    for i in custom_code:
        assert i.isdigit()

    custom_code = random_object.custom_code('@@@##')
    custom_code = random_object.custom_code('@@@##', '@', '#')
    custom_code = random_object.custom_code('@@@##', digit='#', char='@')
    custom_code = random_object.custom_code(digit='#', char='@', mask='@@@##')

    mask = '@###'
    original = mask
    mask = mask.replace('@', 'A')
    mask = mask.replace('#', '0')
    custom_code = random_object.custom_code

# Generated at 2022-06-14 01:07:46.507421
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Check that the mask is too short
    try:
        r = Random()
        r.custom_code(mask='@')
    except ValueError:
        return
    raise ValueError('Mask is too short!')



# Generated at 2022-06-14 01:07:56.322578
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert len(Random().custom_code()) == 4, "Expected 4 characters got %d." % len(Random().custom_code())
    assert len(Random().custom_code(mask='@##')) == 3, "Expected 3 characters got %d." % len(Random().custom_code(mask='@##'))
    assert len(Random().custom_code(mask='@@@#')) == 4, "Expected 4 characters got %d." % len(Random().custom_code(mask='@@@#'))
    assert len(Random().custom_code(mask='@@@#')) == 4, "Expected 4 characters got %d." % len(Random().custom_code(mask='@@@#'))

    for i in range(100):
        string = Random().custom_code("@@@")

# Generated at 2022-06-14 01:07:59.476329
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    i = int(random.random() * 10)
    str_custom_code = random.custom_code()
    assert len(str_custom_code) == 5
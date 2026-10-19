

# Generated at 2022-06-14 01:06:57.439771
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Check the generating of custom_code."""
    custom_code = random.custom_code(mask='AAA#', char='A', digit='#')
    assert custom_code in ['AAA0', 'AAA1', 'AAA2', 'AAA3', 'AAA4',
                           'AAA5', 'AAA6', 'AAA7', 'AAA8', 'AAA9']

# Generated at 2022-06-14 01:07:05.727456
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Given
    mask = '@###'
    char = '@'
    digit = '#'
    first_regex = 'ABC\d\d\d'
    second_regex = 'DEF\d\d\d'

    # When
    first_code = random.custom_code(mask, char, digit)
    second_code = random.custom_code(mask, char, digit)

    # Then
    assert first_code != second_code
    assert first_code != second_regex
    assert second_code != first_regex
    assert first_regex != second_regex
    assert first_code[0] in ('A', 'B', 'C')
    assert second_code[0] in ('D', 'E', 'F')

# Generated at 2022-06-14 01:07:14.272674
# Unit test for method custom_code of class Random
def test_Random_custom_code():

    code = random.custom_code()
    print('Random code: {}'.format(code))

    code2 = random.custom_code(mask='#@@#@@#@@#@@#@@')
    print('Random code: {}'.format(code2))

    code3 = random.custom_code(mask='@#######')
    print('Random code: {}'.format(code3))

    code4 = random.custom_code(mask='#@@#@@#@@#@@#@@##@@#@@#@@#@@#@@#@@@@#')
    print('Random code: {}'.format(code4))

# Generated at 2022-06-14 01:07:24.797353
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for custom_code method."""
    assert len(Random().custom_code()) == 4
    assert len(Random().custom_code('@1##')) == 4
    assert len(Random().custom_code('@1##', '@', '1')) == 4
    assert len(Random().custom_code('@1##', '1', '@')) == 4
    assert len(Random().custom_code('@1##', '1', '1')) == 4
    assert len(Random().custom_code('@###')) == 4
    assert len(Random().custom_code('@1##', '#', '#')) == 4

# Generated at 2022-06-14 01:07:32.415533
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    random_obj = Random()

    # Test when placeholders are the same
    with pytest.raises(TypeError):
        random_obj.custom_code(mask='@###', char='@', digit='@')

    # Generate code with a custom mask
    assert random_obj.custom_code('@###') == 'AF93'
    assert random_obj.custom_code(digit=0, char=1) == '123'

# Generated at 2022-06-14 01:07:39.910205
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method generate_custom_code of class Random."""
    _random = Random()
    num = 0
    for _ in range(500):
        code = _random.custom_code()
        assert len(code) == 4
        if not code.isdigit():
            num += 1
    assert num != 0

# Generated at 2022-06-14 01:07:44.866533
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test the method custom_code of the class Random."""
    r = Random()
    code = r.custom_code('AAAA', 'A', '0')
    assert all(map(lambda x: x in string.ascii_uppercase, code))

# Generated at 2022-06-14 01:07:56.151983
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    assert rnd.custom_code()
    assert rnd.custom_code('@###', '@', '#')
    assert rnd.custom_code('###', '@', '#')
    assert rnd.custom_code('@@', '@', '#')
    assert rnd.custom_code('####', '@', '#')
    assert rnd.custom_code('@@@@', '@', '#')
    assert rnd.custom_code('@@##', '@', '#')
    assert rnd.custom_code('@#@#', '@', '#')
    assert rnd.custom_code('@###', '@', '#')
    assert rnd.custom_code('@###', '@', '#')

# Generated at 2022-06-14 01:08:03.693113
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code = random.custom_code('@### @###')
    assert isinstance(code, str)
    assert len(code) == 10
    assert code[4] == ' '
    for letter in [code[5], code[6], code[7]]:
        assert letter.isdigit()
    for letter in [code[0], code[1], code[2], code[3], code[8], code[9]]:
        assert letter.isupper()


# Generated at 2022-06-14 01:08:10.258466
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    rnd.seed(15)
    assert rnd.custom_code(mask='@###', char='@', digit='#') == '@4H4'
    assert rnd.custom_code(mask='@@@##', char='@', digit='#') == '@@@44'
    assert rnd.custom_code(mask='@##-@##', char='@', digit='#') == '@44-@44'
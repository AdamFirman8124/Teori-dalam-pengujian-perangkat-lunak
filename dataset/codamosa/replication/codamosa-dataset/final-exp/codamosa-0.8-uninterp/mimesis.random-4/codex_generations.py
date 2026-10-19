

# Generated at 2022-06-14 01:07:14.689172
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    assert rnd.custom_code() in ['@###', '#@@@', '@@@#', '###@', '#@##', '@##@']
    assert rnd.custom_code(mask='#@@@') in ['#@@@', '@@@#', '@##@']
    assert rnd.custom_code(mask='##@@') in ['##@@', '@@##', '@@@#']
    assert rnd.custom_code(mask='###') in ['###', '@@@', '@#@', '##@']
    assert rnd.custom_code(mask='###@') in ['###@', '@@@@', '@#@@', '##@@']
    assert rnd.custom_code(mask='@###', char='#', digit='@') in ['@@@']
   

# Generated at 2022-06-14 01:07:21.722683
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    assert random.custom_code()
    assert random.custom_code('@AAA')
    assert random.custom_code('@@')
    assert random.custom_code('AAA')
    assert random.custom_code('#')
    assert random.custom_code(char='$')
    assert random.custom_code(char='$', digit='%')
    assert random.custom_code(digit='%')

# Generated at 2022-06-14 01:07:24.334787
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code = random.custom_code()
    assert isinstance(code, str)
    assert len(code) == 4



# Generated at 2022-06-14 01:07:29.966902
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test for the method custom_code of class Random()."""
    r = random.Random()
    assert len(r.custom_code('@##')) == 4
    assert len(r.custom_code('@###', digit='$')) == 4
    assert len(r.custom_code('@###', char='$')) == 4
    assert len(r.custom_code()) == 10



# Generated at 2022-06-14 01:07:37.787691
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random = Random()
    # с @ не должно быть
    assert random.custom_code() == random.custom_code('@###', '@')
    # только 1 подстрока, не должно быть ошибки
    assert random.custom_code('@###@', '@')
    # должна быть ошибка
    try:
        random.custom_code('@###@', '@', '@')
    except ValueError:
        print('\nОшибка на строке 21')

# Generated at 2022-06-14 01:07:45.360087
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method ``Random.custom_code()``."""
    code_sample = '@###'
    for i in range(100):
        code = Random().custom_code(code_sample)
        assert len(code) == len(code_sample)
        for c in code:
            if c != '@' and c != '#':
                assert not '@' in code
                assert not '#' in code
                assert c in string.ascii_uppercase

# Generated at 2022-06-14 01:07:54.536812
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random.
    Args:
        mask (str): Mask of code.
        char (str): Placeholder for characters.
        digit (str): Placeholder for digits.
    Return: Return a Custom code
    """
    mask = '####'
    char = '@'
    digit = '#'
    code = random.custom_code(mask,char,digit)
    if len(code) != len(mask):
        raise ValueError('length of code and mask are not equal')
    for char in code:
        if char not in ('@','#'):
            raise ValueError('the mask contains characters other than @ and #')

# Generated at 2022-06-14 01:08:00.260845
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    assert rnd.custom_code('@###')
    assert rnd.custom_code('@###-##-##')
    assert rnd.custom_code('@###-##-##', char='*', digit='%')
    assert rnd.custom_code('@###-##-##', char='@', digit='@')

# Generated at 2022-06-14 01:08:07.845520
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random = Random()
    random_code = random.custom_code()
    print(random_code)
    assert isinstance(random_code, str)

    random_code = random.custom_code('######')
    print(random_code)
    assert isinstance(random_code, str)

    random_code = random.custom_code('######', '#', '*')
    print(random_code)
    assert isinstance(random_code, str)


test_Random_custom_code()

# Generated at 2022-06-14 01:08:11.261016
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    coded = random.custom_code(mask='@##-@@@')
    length = len(coded)

    assert length == 7
    assert '-' not in coded[:3]
    assert '-' not in coded[4:]
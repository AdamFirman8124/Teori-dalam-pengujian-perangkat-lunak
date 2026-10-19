

# Generated at 2022-06-14 01:09:37.286539
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random_code = Random().custom_code(mask='@###', char='@', digit='#')
    assert isinstance(random_code, str)
    assert len(random_code) == 4
    assert random_code.isalnum()
    assert random_code.isupper()

# Generated at 2022-06-14 01:09:51.234675
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    _mask = '@###'
    _char = '@'
    _digit = '#'
    _code = Random.custom_code(_mask, _char, _digit)
    _code = ''.join([char for char in _code])
    _char = ''.join([char for char in _char])
    _digit = ''.join([digit for digit in _digit])
    _chars = string.ascii_letters
    _digits = string.digits

    # Check if description of code is the same as mask
    assert len(_mask) == len(_code)

    for char in _code:
        # Check the code is letter or digit
        assert char in _chars or char in _digits

        if _char in char:
            # Check the code is letter
            assert char in _chars

# Generated at 2022-06-14 01:10:00.704152
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Case 1
    assert random.custom_code(mask='@@##') == 'EF82'
    # Case 2
    assert random.custom_code(mask='@@@@##') == 'CWYF05'
    # Case 3
    assert random.custom_code(mask='@') == 'P'
    # Case 4
    assert random.custom_code(mask='@@') == 'UX'
    # Case 5
    assert random.custom_code(mask='@@@') == 'FAU'
    # Case 6
    assert random.custom_code(mask='@@@@') == 'VQXD'
    # Case 7
    assert random.custom_code(mask='@@@@@') == 'LHEHJ'
    # Case 8
    assert random.custom_code(mask='@@@@@@') == 'SQKWVS'
    #

# Generated at 2022-06-14 01:10:03.903935
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    res1 = 'AA1'
    res2 = 'BBC123'
    assert Random().custom_code() == res1
    assert Random().custom_code('@@##') == res2

# Generated at 2022-06-14 01:10:09.219533
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # It will pass.
    Random(78).custom_code('@###', '@', '#')
    # It will fail.
    try:
        Random(78).custom_code('@@@', '@', '@')
    except ValueError:
        pass

# Generated at 2022-06-14 01:10:18.843679
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Ensures that Random().custom_code is working properly."""
    from mimesis.constants import DATA_DIR
    from mimesis.exceptions import NonEnumerableError

    mask = '@###'
    char = '@'
    digits = '#'
    _random = Random()
    code = _random.custom_code(mask)

    assert isinstance(code, str)
    assert len(code) == len(mask)

    # Check only digits
    mask = '###'
    code = _random.custom_code(mask)
    assert isinstance(code, str)
    assert code.isdigit() is True

    # Check only characters
    mask = '@@@'
    code = _random.custom_code(mask)
    assert isinstance(code, str)
    assert code.isalpha()

# Generated at 2022-06-14 01:10:31.135860
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    from mimesis.exceptions import NullObject
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    import random
    import pytest

    for i in range(5):
        print(Random().custom_code())

    for i in range(5):
        print(Random().custom_code(char='#'))

    for i in range(5):
        print(Random().custom_code(digit='@'))

    for i in range(5):
        print(Random().custom_code(char='#', digit='@'))

    for i in range(5):
        print(Random().custom_code(char='#', digit='@', mask='#######@#@#@#@#@#@#@#@#@#@#@#@#'))

    person = Person('en')

# Generated at 2022-06-14 01:10:34.487036
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random_custom = Random()
    random_custom.seed(1)
    random_custom.custom_code('@###', '@', '#')



# Generated at 2022-06-14 01:10:40.233032
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    result = random.custom_code('AA@@##@@', '@', '#')
    assert result == 'AAYQQ13YQ' or result == 'AABPQ22BP'
    result = random.custom_code('AA@###@@@', '@', '#')
    assert result == 'AAK016AJE' or result == 'AAP068AOD'

# Generated at 2022-06-14 01:10:50.005015
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random.

    :return: None.
    """
    random_instance = Random()
    mask = '@@##'
    char = '@'
    digit = '#'
    code = random_instance.custom_code(mask, char, digit)
    assert len(code) == len(mask)
    assert code[0].isalpha() and code[1].isalpha()
    assert code[2].isdigit() and code[3].isdigit()
    mask = 'abcd'
    char = '#'
    digit = '*'
    code = random_instance.custom_code(mask, char, digit)
    assert code == 'abcd'
    mask = '@@##'
    char = '@'
    digit = '@'
    random_instance.custom
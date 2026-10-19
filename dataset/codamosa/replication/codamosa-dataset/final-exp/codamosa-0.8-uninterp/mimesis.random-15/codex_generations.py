

# Generated at 2022-06-14 01:14:33.881156
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test for the method ``custom_code()`` of class ``Random()``."""
    my_random = Random()
    assert my_random.custom_code() == 'R8C8'
    assert my_random.custom_code('@##') == 'L79'
    assert my_random.custom_code('AA@@##') == 'JQFQ24'
    assert my_random.custom_code('@@##@@') == 'KI39KI'
    assert my_random.custom_code(digit='@', char='#') == 'P#27#'



# Generated at 2022-06-14 01:14:39.322853
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rand = Random()
    rand.seed(1)

    mask = '@@##@@'
    char = '@'
    digit = '#'
    result = rand.custom_code(mask, char, digit)
    assert result == 'PH91PH'
    assert isinstance(result, str)



# Generated at 2022-06-14 01:14:46.675390
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test Random.custom_code()."""
    length = random.randint(1, 20)
    mask = '#' * length
    code = random.custom_code(mask)
    assert len(code) == length, f'{len(code)} != {length}'
    assert code.isalnum(), f'{len(code)} is not alphanumeric'



# Generated at 2022-06-14 01:14:57.902630
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code_mask = '@@##@@'
    char = '@'
    digit = '#'
    custom_code = Random().custom_code(code_mask, char, digit)
    assert len(custom_code) == 6
    assert custom_code[0].isupper()
    assert custom_code[1].isupper()
    assert custom_code[2].isdigit()
    assert custom_code[3].isdigit()
    assert custom_code[4].isupper()
    assert custom_code[5].isupper()

# Generated at 2022-06-14 01:15:04.330079
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random.

    Assertion:
         - Function must return a result that is a string.
         - Function must return a result whose length matches the length of the mask.
    """
    result = random.custom_code()
    flag = isinstance(result, str)
    length = len(result) == len('@###')
    assert flag and length



# Generated at 2022-06-14 01:15:15.345595
# Unit test for method custom_code of class Random

# Generated at 2022-06-14 01:15:19.601572
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test unit for method custom_code of class Random."""
    print(random.custom_code('@@@-@@@', '@', '#'))


# Generated at 2022-06-14 01:15:23.239886
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    print(Random().custom_code())

if __name__ == '__main__':
    test_Random_custom_code()

# Generated at 2022-06-14 01:15:28.943110
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code('@@') == 'AA'
    assert Random().custom_code('@@@') == 'AAa'
    assert Random().custom_code(mask='@@@', char='@', digit='#') == 'AA0'


# Generated at 2022-06-14 01:15:35.206367
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random"""
    part_of_code = random.custom_code()
    code = part_of_code
    for i in range(3):
        part_of_code = random.custom_code()
        code = code + part_of_code
    assert len(code) == (len(part_of_code) * 4)
    assert type(code) == str


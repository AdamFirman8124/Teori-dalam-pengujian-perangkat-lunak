

# Generated at 2022-06-14 01:11:39.632191
# Unit test for method custom_code of class Random
def test_Random_custom_code():

    r = Random()
    res = r.custom_code(mask='@###', char='@', digit='#')
    assert len(res) == 4
    assert res[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM'
    assert res[1] in 'QWERTYUIOPASDFGHJKLZXCVBNM'
    assert res[2] in 'QWERTYUIOPASDFGHJKLZXCVBNM'
    assert res[3] in '0123456789'

    res = r.custom_code(mask='@@@@@@###', char='@', digit='#')
    assert len(res) == 9
    assert res[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM'

# Generated at 2022-06-14 01:11:42.101524
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code(mask='@', char='@', digit='#') == 'B'

# Generated at 2022-06-14 01:11:45.838584
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert 'A1A1' == random.custom_code('@@@@')
    assert 'A1A1.1' == random.custom_code('@@@@.#')

# Generated at 2022-06-14 01:11:50.946643
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    mask = '@@@###'
    char = '@'
    digit = '#'
    char_code = ord(char)
    digit_code = ord(digit)
    assert char_code != digit_code

# Generated at 2022-06-14 01:12:00.165708
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for ``Random.custom_code()``."""
    rnd = Random()
    code = rnd.custom_code()
    assert len(code) == 4
    for letter in code:
        assert letter.isdigit()

    rnd = Random()
    code = rnd.custom_code('@@@')
    assert len(code) == 3
    assert code[0].isdigit()
    assert code[1].isalpha()
    assert code[2].isalpha()

    rnd = Random()
    code = rnd.custom_code('###')
    assert len(code) == 3
    assert code[0].isdigit()
    assert code[1].isdigit()
    assert code[2].isdigit()

    rnd = Random()

# Generated at 2022-06-14 01:12:04.948155
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    code = r.custom_code()
    assert isinstance(code, str), "The code must be a string."
    assert len(code) == 4, "The length of code must be 4 symbols."

# Generated at 2022-06-14 01:12:09.930958
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for custom_code method of the Random class."""
    result = random.custom_code()
    assert isinstance(result, str)



# Generated at 2022-06-14 01:12:12.298653
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    result = rnd.custom_code()
    print(result)
    assert(len(result) == 4)

# Generated at 2022-06-14 01:12:14.777428
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code of class Random."""
    assert Random().custom_code() == 'A0Z9'



# Generated at 2022-06-14 01:12:17.977983
# Unit test for method custom_code of class Random
def test_Random_custom_code():
        r = Random()
        assert r.custom_code() == 'F38S'
        assert r.custom_code(mask='@##') == 'E04'

# Generated at 2022-06-14 01:12:45.368200
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Test for "@" used for letters and "#" used for digits:
    my_code = random.custom_code()

    assert len(my_code) == 4
    assert my_code[0].isalpha()
    assert my_code[1].isdigit()
    assert my_code[2].isdigit()
    assert my_code[3].isdigit()

    my_code = random.custom_code('@###')

    assert len(my_code) == 4
    assert my_code[0].isalpha()
    assert my_code[1].isdigit()
    assert my_code[2].isdigit()
    assert my_code[3].isdigit()

    # Test for "@" used for digits and "#" used for letters:

# Generated at 2022-06-14 01:12:48.602977
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    for _ in range(10):
        code = random.custom_code(mask='@@@@@')
        assert isinstance(code, str) and len(code) == 5 and code.isupper()



# Generated at 2022-06-14 01:12:55.480420
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert random.custom_code(mask='########') == 'QO98OI9X'
    assert random.custom_code(mask='@#@#@#@#') == 'JG44AJKL'
    assert random.custom_code(mask='@###') == 'R234'
    assert random.custom_code(mask='####@####') == '2557MJ959'



# Generated at 2022-06-14 01:13:05.474199
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = random.custom_code()
    assert isinstance(r, str)
    assert len(r) == 4

    r = random.custom_code(mask='@###-@###')
    assert isinstance(r, str)
    assert len(r) == 9

    r = random.custom_code(mask='@###@@@')
    assert isinstance(r, str)
    assert len(r) == 7

    r = random.custom_code(mask='@###@@@##-')
    assert isinstance(r, str)
    assert len(r) == 10

    r = random.custom_code(mask='@###@@@$$$')
    assert isinstance(r, str)
    assert len(r) == 10


# Generated at 2022-06-14 01:13:19.264772
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for custom method of class Random.

    Check the Random.custom_code which is used to create the unique
    code using ascii uppercase and random integers.
    """
    # Test 1 
    s = ''
    for i in range(100):
        s = Random.custom_code('###')
    # Test 2
    s = Random.custom_code('###')
    assert len(s) == 3
    # Test 3
    assert Random.custom_code('@@') != Random.custom_code('@@')
    # Test 4
    assert len(Random.custom_code('#'*10)) == 10
    # Test 5
    random_code = Random.custom_code('##')
    assert isinstance(random_code, str)

test_Random_custom_code()

# Generated at 2022-06-14 01:13:31.520592
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    print(rnd.custom_code('@#A#'))
    print(rnd.custom_code('@#A#', '@', '#'))
    print(rnd.custom_code('A@A@', '@', 'A'))
    print(rnd.custom_code('@@@@'))
    print(rnd.custom_code('@@@@', '@', 'A'))
    print(rnd.custom_code('@@'), rnd.custom_code('AA'), rnd.custom_code('##'))
    print(rnd.custom_code('AA'), rnd.custom_code('AA'), rnd.custom_code('##'))
    print(rnd.custom_code('11'), rnd.custom_code('11'), rnd.custom_code('##'))
   

# Generated at 2022-06-14 01:13:34.471283
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code = random.custom_code('@@##')  # noqa

# Generated at 2022-06-14 01:13:39.278419
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    res = random.custom_code('@####')
    assert isinstance(res, str)
    assert len(res) == 5
    res = random.custom_code('@@####')
    assert isinstance(res, str)
    assert len(res) == 6

# Generated at 2022-06-14 01:13:51.774826
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random(3)
    assert rnd.custom_code('##-@###') == '16-LHGFD'
    assert rnd.custom_code('##-@###', '@', '#') == '16-KJNHB'
    assert rnd.custom_code('##-@###', '#', '@') == '16-LHGFD'
    assert rnd.custom_code('@@@-#@###') == 'LBF-3KHGFD'
    assert rnd.custom_code('@@-#@###') == 'LB-3KHGFD'
    assert rnd.custom_code('@@-##@###') == 'LB-16KHGFD'
    assert rnd.custom_code('@-##@###') == 'L-16KHGFD'


# Generated at 2022-06-14 01:14:01.605213
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    result = random.custom_code(mask='@@##', char='@', digit='#')

    assert result is not None
    assert len(result) == 5
    assert result[0] in string.ascii_uppercase
    assert result[1] in string.ascii_uppercase
    assert result[2] in string.digits
    assert result[3] in string.digits
    assert result[4] not in string.digits and result[4] not in string.ascii_uppercase
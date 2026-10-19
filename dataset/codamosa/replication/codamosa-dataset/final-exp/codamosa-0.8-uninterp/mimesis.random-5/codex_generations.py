

# Generated at 2022-06-14 01:07:06.719739
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    d = []
    for i in range(0, 10000):
        s = rnd.custom_code()
        d.append(s)
    assert len(d) == len(set(d))
    assert len(d) == 10000

# Generated at 2022-06-14 01:07:11.273887
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code() == Random().custom_code()
    assert Random().custom_code('@AA') == Random().custom_code('@AA')
    assert Random().custom_code('###-@@@') == '834-JAS'

# Generated at 2022-06-14 01:07:18.702256
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random_code = Random().custom_code(mask="@###")
    assert random_code is not None
    assert len(random_code) == 4
    assert random_code.islower()
    # assert custom_code in all(map(lambda x: isinstance(x, str), random_code))
    # assert '@' not in random_code
    del random_code


test_Random_custom_code()

# Generated at 2022-06-14 01:07:23.398240
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert random.custom_code('@@@ ### ####', '@', '#') in ('A21 456 6890', 'D14 276 8390', 'B23 123 7890')

# Generated at 2022-06-14 01:07:27.487511
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    mask = '@@##'
    char = '@'
    digit = '#'
    r = Random()
    assert len(r.custom_code(mask=mask, char=char, digit=digit)) == len(mask)

# Generated at 2022-06-14 01:07:30.165247
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code = Random().custom_code(mask='@@@@@@Z##')
    assert isinstance(code, str)
    assert len(code) == len('@@@@@@Z##')

# Generated at 2022-06-14 01:07:37.864512
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    def create_data():
        char_code = ord('@')
        digit_code = ord('#')

# Generated at 2022-06-14 01:07:43.831669
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    assert rnd.custom_code() in [
        '@AFE', '@CAK', '@BEC', '@EAC', '@CIF', '@HAB',
        '@GFK', '@GJE', '@DIE', '@EJL', '@DFL'
    ]

# Generated at 2022-06-14 01:07:55.831386
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test for method custom_code of class Random"""
    from string import ascii_uppercase
    from itertools import product

    _mask = '@### ##@@'
    _char = '@'
    _digit = '#'

    rnd = Random()

    for _ in range(40):
        code = rnd.custom_code(_mask, _char, _digit)
        assert len(code) == len(_mask)

        for char in code:
            if char in ascii_uppercase:
                assert _mask[code.index(char)] == _char
            elif char in set(map(lambda x: str(x), range(10))):
                assert _mask[code.index(char)] == _digit
            else:
                assert char == _mask[code.index(char)]


# Generated at 2022-06-14 01:08:09.263890
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert random.custom_code('AB@#') == 'AB10'
    assert random.custom_code('#AB#') == '40AB'
    assert random.custom_code('AB#') == 'AB3'
    assert random.custom_code('AB#XA') == 'AB3XA'
    assert random.custom_code('01AB#XA') == '01AB3XA'
    assert random.custom_code('A###') == 'A025'
    assert random.custom_code('@###') == '@065'
    assert random.custom_code('@###', 'A', 'B') == '@065'
    assert random.custom_code('@###', 'B', 'A') == '@065'
    assert random.custom_code('##AB') == '79AB'
    assert random

# Generated at 2022-06-14 01:08:23.144958
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # prepare data
    mask = '@###'
    char = '@'
    digit = '#'
    char_code = ord(char)
    digit_code = ord(digit)

    # prepare methods
    rnd = Random()

    code = rnd.custom_code(mask, char, digit)
    code_bytes = code.encode()
    for i, p in enumerate(code_bytes):
        if mask[i] == char:
            assert char_code == p
        elif mask[i] == digit:
            assert digit_code == p
        else:
            assert mask[i] == p


# Generated at 2022-06-14 01:08:27.352240
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method custom_code of class Random."""
    r = Random()
    result = r.custom_code("@@@", '@', '#')
    assert result.isalnum()

# Generated at 2022-06-14 01:08:39.098707
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    '''The method custom_code of class Random should return random code.
    '''
    res = random.custom_code()
    assert isinstance(res, str)
    assert not res.isdigit()
    assert res.isupper()
    assert len(res) == 4
    res = random.custom_code('@##', '@', '#')
    assert isinstance(res, str)
    assert not res.isdigit()
    assert res.isupper()
    assert len(res) == 3
    res = random.custom_code('@@####', '@', '#')
    assert isinstance(res, str)
    assert not res.isdigit()
    assert res.isupper()
    assert len(res) == 6


# Generated at 2022-06-14 01:08:51.356407
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test class Random."""
    for _ in range(100):
        rand = Random()
        assert rand.custom_code() in ['P324', 'E038', 'U611', 'O876', 'K935',
                                      'B348', 'H325', 'E010', 'B805', 'F673']
        assert len(rand.custom_code()) == 4

        assert rand.custom_code('@###-@###') in ['K645-P746', 'P948-K650',
                                                 'U196-G141', 'I739-P058',
                                                 'I931-J003']
        assert len(rand.custom_code('@###-@###')) == 9


# Generated at 2022-06-14 01:08:52.198167
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    pass

# Generated at 2022-06-14 01:08:58.444988
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    for _ in range(100):
        assert len(rnd.custom_code()) == 4
    for _ in range(100):
        assert len(rnd.custom_code(mask='@#', digit='#', char='@')) == 2
    for _ in range(100):
        assert len(rnd.custom_code(mask='#@#@')) == 4

# Generated at 2022-06-14 01:09:10.755177
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method ``custom_code()`` of class ``Random()``.
    """
    the_random = Random()
    code = the_random.custom_code(mask='@###-##-#', char='@', digit='#')
    assert code != the_random.custom_code()
    assert code.startswith('@')
    assert code.endswith('-')
    assert code[4] == '-'
    assert code[7] == '-'
    assert code[9] == '-'
    assert code[-1].isdigit()
    assert code[-2].isdigit()
    assert code[-3].isdigit()
    assert code[-4].isalpha()
    assert code[-5].isalpha()
    assert code[-6].isalpha()

# Generated at 2022-06-14 01:09:12.801386
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code('@@@###') == 'LKH789'

# Generated at 2022-06-14 01:09:17.871119
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    custom_code= '@@###'
    assert Random.custom_code(Random(), mask=custom_code, char='@', digit='#') != custom_code

# Generated at 2022-06-14 01:09:22.114760
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    _ = r.custom_code(mask='# ###', char='#', digit=' ')
    assert _ is not None
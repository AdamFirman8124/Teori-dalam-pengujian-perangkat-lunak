

# Generated at 2022-06-14 01:07:09.226638
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    res = r.custom_code(mask='@###', char='@')
    assert len(res) == 4
    assert res[-1].isdigit()
    assert res[0].isupper()

# Generated at 2022-06-14 01:07:12.474392
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert Random().custom_code()
    assert Random().custom_code(mask='@###')
    assert Random().custom_code(mask='@###', char='@', digit='#')

# Generated at 2022-06-14 01:07:17.587162
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    from mimesis.compatibility import pick_random_module

    if pick_random_module() == random_module:
        assert random.custom_code() is not None
        assert random.custom_code() == random.custom_code()
        assert random.custom_code('@#@#@#@#') is not None



# Generated at 2022-06-14 01:07:25.452037
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test ``custom_code()`` method of class ``Random``.

    The test checks whether the method
    generates the code specified in the mask.

    """

    mask = '@###'
    _random = Random()
    _custom_code = _random.custom_code(mask=mask)

    assert isinstance(_custom_code, str)
    assert len(_custom_code) == len(mask)

    if _custom_code[0].isupper():
        assert True
    else:
        assert False

    if _custom_code[1:].isdigit():
        assert True
    else:
        assert False



# Generated at 2022-06-14 01:07:35.000468
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test method ``custom_code()`` of class ``Random``."""
    rnd = Random()
    assert isinstance(rnd.custom_code(), str)
    assert rnd.custom_code() == rnd.custom_code()
    assert rnd.custom_code('AAA') != rnd.custom_code('AAA')
    assert len(rnd.custom_code()) == len(rnd.custom_code('AAA'))

# Generated at 2022-06-14 01:07:43.365286
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Testing generator of custom code.

    Two placeholders can be used in a mask:
        - @ for chars;
        - # for digits.
    """

    r = Random()
    assert r.custom_code() == r.custom_code('@#@#')
    assert r.custom_code('@@###') == r.custom_code('@@###')
    assert r.custom_code('@@###', char='@', digit='@') == 'AA###'
    assert r.custom_code('@@###', char='@', digit='#') == 'AA###'
    assert r.custom_code('@@###', char='@', digit='@') == 'AA###'
    assert r.custom_code('@@###', char='@', digit='#') == 'AA###'

# Generated at 2022-06-14 01:07:47.782191
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    from mimesis.providers.environments import Environment
    r = random
    a = Environment().custom_code('@###')
    b = r.custom_code('@###')
    c = r.custom_code('@@##')
    assert len(a) == len(b) == len(c) == 4
    assert a != b != c

# Generated at 2022-06-14 01:08:00.632817
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    import string
    assert Random.custom_code() == "S851"
    assert Random.custom_code(mask="##") == "12"
    assert Random.custom_code(mask="@") == "N"
    assert Random.custom_code(mask="@", char="!") == "!"
    assert Random.custom_code(mask="@@@") == "VFS"
    assert Random.custom_code(mask="@@@", char="#") == "857"
    assert Random.custom_code(mask="###") == "234"
    assert Random.custom_code(mask="###", char="&") == "926"
    assert Random.custom_code(mask="###", digit="@") == "@@@"
    assert Random.custom_code(mask="###", digit="&") == "378"
    assert Random

# Generated at 2022-06-14 01:08:14.091111
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random.

    :return:
    """
    rnd = Random()
    print(rnd.custom_code())  # @4C4

    print(rnd.custom_code(mask='@@#'))  # UZ4

    print(rnd.custom_code(mask='@@#', char='@'))  # UZ4

    print(rnd.custom_code(mask='@@#', digit='#'))  # UZ4

    print(rnd.custom_code(char='@', digit='#'))  # @4C4

    print(rnd.custom_code(mask='@@#', char='@', digit='#'))  # UZ4

    print(rnd.custom_code(char='@'))  # @4C4

   

# Generated at 2022-06-14 01:08:17.968758
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code = random.custom_code()
    assert code
    assert len(code) == 4

    code = random.custom_code('@###')
    assert code
    assert len(code) == 4
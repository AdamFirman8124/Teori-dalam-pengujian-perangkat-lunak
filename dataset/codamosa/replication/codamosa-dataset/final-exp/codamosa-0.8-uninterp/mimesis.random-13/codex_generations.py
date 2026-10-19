

# Generated at 2022-06-14 01:06:57.687798
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    codes = set()
    for _ in range(10):
        code = Random().custom_code()
        if code in codes:
            print('fails')
        codes.add(code)

# Generated at 2022-06-14 01:06:59.360849
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    assert rnd.custom_code(mask='@@@###') == rnd.custom_code()

# Generated at 2022-06-14 01:07:09.601457
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    import re
    pattern = r'[A-Z]\d{3}'
    for _ in range(100):
        result = random.custom_code('@###')
        assert re.fullmatch(pattern, result) is not None
        result = random.custom_code('#@##')
        assert re.fullmatch(pattern, result) is not None
        result = random.custom_code('##@#')
        assert re.fullmatch(pattern, result) is not None
        result = random.custom_code('###@')
        assert re.fullmatch(pattern, result) is not None
    assert re.fullmatch(pattern, random.custom_code('@###', '*', '*')) is not None

# Generated at 2022-06-14 01:07:13.913066
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random(123456)
    mask = '@###'
    assert rnd.custom_code(mask, '@', '#') == 'U147'

# Generated at 2022-06-14 01:07:18.929941
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    _person = Person('en')
    _gender = _person.gender()
    _code = random.custom_code()

    if _gender == Gender.MALE:
        assert len(_code) == 4
    else:
        assert len(_code) == 5

# Generated at 2022-06-14 01:07:31.641797
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    assert random.custom_code(mask='ABC', char='A', digit='B') \
           .isupper() and random.custom_code(mask='000', char='0', digit='1') \
           .isdigit()
    assert len(random.custom_code(mask='ABC000')) == 6
    assert len(random.custom_code(mask='ABC000', char='0', digit='A')) == 6
    assert random.custom_code(mask='0000000') == '0000000'
    assert random.custom_code(mask='0000000', char='0', digit='0') == '0000000'
    assert random.custom_code(mask='AAAAAAA') == 'AAAAAAA'
    assert random.custom_code(mask='AAAAAAA', char='A', digit='A') == 'AAAAAAA'

# Generated at 2022-06-14 01:07:41.146261
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    for _ in range(100):
        assert len(random.custom_code()) == 4
        assert len(random.custom_code(mask='@@##', char='@', digit='#')) == 4
        assert len(random.custom_code(mask='@@###', char='@', digit='#')) == 5
        assert len(random.custom_code(mask='@@####', char='@', digit='#')) == 6
        assert len(random.custom_code(mask='@@@@', char='@', digit='#')) == 4
        assert len(random.custom_code(mask='@@@@@', char='@', digit='#')) == 5
        assert len(random.custom_code(mask='@@@@@@', char='@', digit='#')) == 6

# Generated at 2022-06-14 01:07:49.319686
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Должен вернуть числа и буквы в верхнем регистре
    assert re.match("^[0-9A-Z]{4}$", random.custom_code("####"))

    # Должен вернуть буквы в верхнем регистре
    assert re.match("^[A-Z]{4}$", random.custom_code("@@@@"))

    # Должен вернуть буквы и цифры в верхн

# Generated at 2022-06-14 01:07:57.669258
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    code = rnd.custom_code()
    assert isinstance(code, str)
    assert len(code) == 4
    code = rnd.custom_code(mask='ABC')
    assert isinstance(code, str)
    assert len(code) == 3
    code = rnd.custom_code(mask='ABC', char=':', digit='%')
    assert isinstance(code, str)
    assert len(code) == 3


# Generated at 2022-06-14 01:08:02.435392
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    c = Random().custom_code()
    assert c[0].isalpha()
    assert c[1].isdigit()
    assert c[2].isdigit()
    assert c[3].isdigit()




# Generated at 2022-06-14 01:07:05.108744
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    for i in range(100):
        assert Random().custom_code('@###') == Random().custom_code('@###')
        assert Random().custom_code('@@##') == Random().custom_code('@@##')
        assert Random().custom_code('@@##', char='#') == Random().custom_code('@@##', char='#')
        assert Random().custom_code('@@##', digit='#') == Random().custom_code('@@##', digit='#')
        assert Random().custom_code('@@##', char='@', digit='@') == Random().custom_code('@@##', char='@', digit='@')
        assert Random().custom_code('@@##', char='#', digit='#') == Random().custom_code('@@##', char='#', digit='#')

# Generated at 2022-06-14 01:07:07.296335
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    codes = Random().custom_code()
    assert isinstance(codes, str)
    assert len(codes) == 4

# Generated at 2022-06-14 01:07:12.473560
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code = random.custom_code(mask = '@#@#@#@#@#', digit = '#', char = '@')
    assert len(code) == 10
    for i in code:
        assert i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Generated at 2022-06-14 01:07:15.873103
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    code = rnd.custom_code()
    assert isinstance(code, str), 'Type error'
    assert len(code) == 4, 'Length code error'

# Generated at 2022-06-14 01:07:22.132185
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    code = Random().custom_code()
    assert len(code) == 4
    assert code[0] in string.ascii_uppercase
    assert code[1] in string.ascii_uppercase
    assert code[2] in string.digits
    assert code[3] in string.digits



# Generated at 2022-06-14 01:07:28.028991
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    random = Random()
    assert random.custom_code(mask='@###') == 'AAA1'
    assert random.custom_code(mask='@@###', char='a') == 'aH068'
    assert random.custom_code() == 'A001'
    assert random.custom_code(mask='@@##', char='a') == 'aE03'
    assert random.custom_code(mask='@@##', char='a', digit='$') == 'aE02'

# Generated at 2022-06-14 01:07:30.758613
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    codes = set()

    for _ in range(3):
        code = random.custom_code()
        codes.add(code)

    assert len(codes) == 3

# Generated at 2022-06-14 01:07:37.679416
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # TODO (lk-geimfari): more tests
    rnd = Random()
    assert rnd.custom_code()
    assert rnd.custom_code('@###/@###')
    assert rnd.custom_code('@###/@###', char='@', digit='#')
    assert rnd.custom_code('@@@-###')
    assert rnd.custom_code('@@@-!@#')
    assert rnd.custom_code('@@@-###', char='@', digit='#')
    assert rnd.custom_code('@@@-###', char='!', digit='#')
    assert rnd.custom_code('@@@-###', char='@', digit='!')

# Generated at 2022-06-14 01:07:42.921793
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    result = r.custom_code(mask='@@@', char='@')
    assert isinstance(result, str)
    assert len(result) == 3
    assert result.isupper()

# Generated at 2022-06-14 01:07:49.801162
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    # One char placeholder
    code = r.custom_code('@#1')
    print(code)
    assert code == 'A#1'

    # Two chars placeholder
    code = r.custom_code('@##')
    print(code)
    assert code == 'A#1'

    # Three chars placeholder
    code = r.custom_code('@###')
    print(code)
    assert code == 'A#1#'

    # Four chars placeholder
    code = r.custom_code('@####')
    print(code)
    assert code == 'A#1##'

    # Five chars placeholder
    code = r.custom_code('@#####')
    print(code)
    assert code == 'A#1###'

    # Six chars placeholder
    code = r.custom_code
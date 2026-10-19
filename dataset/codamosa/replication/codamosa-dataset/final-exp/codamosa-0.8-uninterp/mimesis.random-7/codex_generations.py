

# Generated at 2022-06-14 01:15:59.206769
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    import random
    import string
    random.seed(0)
    test = random.custom_code('#@####')
    # random.seed(0)
    # test2 = random.custom_code('#@####')
    string.ascii_letters
    assert test == '89YGQ'

# Generated at 2022-06-14 01:16:05.358325
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    from mimesis.providers.datetime import Datetime
    datetime = Datetime('en')
    datetime_format = '%Y%m%d'
    code = '@###'
    print(datetime.date(code, '.'))

# Generated at 2022-06-14 01:16:12.046645
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method custom_code of class Random."""
    # Test of incorrect param
    try:
        random.custom_code('@#@#@#@#@#@#', '@', '#')
    except ValueError as err:
        assert str(err) == 'You cannot use the same ' \
                           'placeholder for digits and chars!'

# Generated at 2022-06-14 01:16:15.169487
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    # Expected is @b68
    assert random.custom_code() == '@B68'

# Generated at 2022-06-14 01:16:21.746986
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    custom_code = random.custom_code('a@@@b')
    assert isinstance(custom_code, str)
    assert len(custom_code) == 5
    assert custom_code[0] == 'a'
    assert custom_code[4] == 'b'
    assert custom_code[3].isdigit()
    
test_Random_custom_code()
 

# Generated at 2022-06-14 01:16:32.775001
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Test ``custom_code()`` of class ``Random()``.

    :return:
    """
    r = Random()
    r.seed(0)

    mask_str = r.custom_code(mask='@###')
    assert mask_str in [
        'V719', 'H039', 'U569', 'O937', 'N564', 'E774', 'Q825', 'B253',
        'J961', 'M831', 'X918', 'Z988', 'T859', 'F030', 'I111', 'D196',
        'G237', 'C958', 'P100', 'S844', 'L338', 'K494', 'R655',
    ]

    # Test if method raises exception if you use
    # the same placeholder for digits and characters
   

# Generated at 2022-06-14 01:16:37.045209
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    _rnd = Random()
    for _ in range(10000):
        _code = _rnd.custom_code()
        assert _code.startswith('@')


if __name__ == "__main__":
    test_Random_custom_code()

# Generated at 2022-06-14 01:16:49.322872
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Check if all values created in the loop without exceptions."""
    for _ in range(100):
        s = random.custom_code('@###-##-###')
        assert isinstance(s, str)
        assert s.count('@') == 3
        assert s.count('#') == 3
        assert '-' in s
        assert len(s) == 11
    for _ in range(100):
        s = random.custom_code('@###-###')
        assert isinstance(s, str)
        assert s.count('@') == 1
        assert s.count('#') == 5
        assert '-' in s
        assert len(s) == 8

# Generated at 2022-06-14 01:17:02.820902
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    rnd.seed(0)
    assert rnd.custom_code() == 'Z2QH'
    assert rnd.custom_code('@###') == 'I461'
    assert rnd.custom_code('##-#-#') == '61-2-2'
    assert rnd.custom_code('###@###') == '618A618'
    assert rnd.custom_code('@#@#@#@#@#@#@#@#') == 'A1B1C1D1E1F1G1H1'
    assert rnd.custom_code('###-#-###', '#', '-') == '402-8-476'


# Generated at 2022-06-14 01:07:05.658085
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    rnd = Random()
    assert rnd.custom_code(mask='@@@') in ['@A@', '@B@', '@C@']



# Generated at 2022-06-14 01:07:08.187963
# Unit test for function get_random_item
def test_get_random_item():
    """Unit test for function get_random_item."""
    from mimesis.enums import Gender

    assert get_random_item(Gender) in Gender

# Generated at 2022-06-14 01:07:10.575430
# Unit test for function get_random_item
def test_get_random_item():
    from mimesis.enums import Gender
    assert Gender.MALE == get_random_item(Gender)
    assert Gender.FEMALE == get_random_item(Gender, Random(0))

# Generated at 2022-06-14 01:07:23.015732
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    _random = Random()
    _str = _random.custom_code()
    assert all([c.isupper() or c.isdigit() for c in _str])
    assert len(_str) == 4

    _str = _random.custom_code(mask='AA#')
    assert all([c.isupper() or c.isdigit() for c in _str])
    assert len(_str) == 3

    _str = _random.custom_code(mask='AA#', char='A', digit='#')
    assert all([c.isupper() or c.isdigit() for c in _str])
    assert len(_str) == 3

    _str = _random.custom_code(mask='AA#', char='.', digit='#')

# Generated at 2022-06-14 01:07:29.228297
# Unit test for function get_random_item
def test_get_random_item():
    """Test for function get_random_item."""
    from mimesis.enums import DayOfWeek
    from mimesis.schema import Field, Schema

    field = Field('day', DayOfWeek)
    schema = Schema(field)
    day = schema.create(1)[0]
    for _ in range(10):
        random_day = schema.create(1)[0]
        assert day != random_day


# Generated at 2022-06-14 01:07:37.411020
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    """Unit test for method ``custom_code()``.

    The method returns a custom code, which can then be used for
    generation verification codes.
    """
    assert '@WZ6' == random.custom_code('@###')
    assert 'ZZL90' == random.custom_code('@@###')
    assert '@A2@' == random.custom_code('@##@')
    assert '4B4' == random.custom_code('###', char='#')
    assert 'BJL@' == random.custom_code('@@@?', char='@', digit='?')
    assert 'A1@B2@' == random.custom_code('@?@?#?#')
    assert '1A2@' == random.custom_code('1A2@')

# Generated at 2022-06-14 01:07:40.097033
# Unit test for function get_random_item
def test_get_random_item():
    eg = get_random_item('foo', 'bar', 'baz')
    assert eg in ('foo', 'bar', 'baz')

# Generated at 2022-06-14 01:07:44.879383
# Unit test for function get_random_item
def test_get_random_item():
    """Unit test for function get_random_item."""
    from mimesis.enums import Browser, BrowserVersion

    browser_v = get_random_item(BrowserVersion)
    browser = get_random_item(Browser)
    assert browser_v in BrowserVersion
    assert browser in Browser

# Generated at 2022-06-14 01:07:51.472356
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random()
    for _ in range(20):
        assert r.uniform(-10, 10)
        assert r.uniform(-10, 10, 3)
        assert r.uniform(-10, 10, 6)
        assert r.uniform(-10, 10, 12)
        assert r.custom_code()
        assert r.custom_code('####')



# Generated at 2022-06-14 01:08:04.103950
# Unit test for method custom_code of class Random
def test_Random_custom_code():
    r = Random(3)
    code = r.custom_code(mask='@@###@@')
    assert len(code) == 6

    code = r.custom_code(mask='@###@')
    assert len(code) == 5

    code = r.custom_code(mask='@@###@@')
    assert len(code) == 6

    code = r.custom_code(mask='@@###@@')
    assert len(code) == 6

    code = r.custom_code(mask='@@###@@')
    assert len(code) == 6

    code = r.custom_code(mask='@@###@@')
    assert len(code) == 6

    code = r.custom_code(mask='A###A')
    assert len(code) == 5

    code = r.custom_code(mask='@@###@@')

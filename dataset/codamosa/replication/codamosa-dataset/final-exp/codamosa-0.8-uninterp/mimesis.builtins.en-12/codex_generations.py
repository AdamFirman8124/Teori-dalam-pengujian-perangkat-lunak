

# Generated at 2022-06-13 23:13:00.191163
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    a = USASpecProvider()
    b = USASpecProvider()
    assert a.personality() in b.personality()

    assert type(a.personality('rheti')) == int
    assert type(b.personality('rheti')) == int


# Generated at 2022-06-13 23:13:04.108063
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    us1 = USASpecProvider(seed=123)
    us2 = USASpecProvider(seed=123)

    assert us1.personality() == 'ESFJ'
    assert us2.personality(category='rheti') == 6


# Generated at 2022-06-13 23:13:10.720293
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    # category = 'mbti'
    my_personality = usa.personality()
    assert my_personality == 'ISTJ'
    my_personality = usa.personality(category='mbti')
    assert my_personality == 'INTJ'
    # category = 'rheti'
    my_personality = usa.personality(category='rheti')
    assert my_personality == 8


# Generated at 2022-06-13 23:13:12.918711
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    x  = USASpecProvider().personality(category = "rheti")
    print(x)


# Generated at 2022-06-13 23:13:18.174281
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality("mbti") in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
                                                     'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

# Generated at 2022-06-13 23:13:25.096647
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    from pprint import pprint

    from mimesis.builtins.usa import USASpecProvider

    usa_sp_1 = USASpecProvider(seed=12345678)

    result = usa_sp_1.personality(category='rheti')
    print('rheti personality:', result)
    assert result == 4

    pprint(vars(usa_sp_1))

    result = usa_sp_1.personality()
    print('mbti personality:', result)
    assert result == 'ISTJ'



# Generated at 2022-06-13 23:13:32.236294
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_spec = USASpecProvider()
    for _ in range(100):
        result = usa_spec.personality("mbti")
        assert isinstance(result, str)
        assert len(result) == 4
        result = usa_spec.personality("rheti")
        assert isinstance(result, int)
        assert result in range(1, 11)


# Generated at 2022-06-13 23:13:40.877997
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # Discovered
    usa_provider = USASpecProvider().personality(category='rheti')
    assert isinstance(usa_provider, int)  # type: ignore
    # Discovered
    usa_provider = USASpecProvider().personality(category='mbti')
    assert isinstance(usa_provider, str)  # type: ignore
    # Discovered
    usa_provider = USASpecProvider().personality()
    assert isinstance(usa_provider, str)  # type: ignore
    usa_provider = USASpecProvider().personality(category='mbti')
    assert ' ' not in usa_provider



# Generated at 2022-06-13 23:13:44.217628
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usaspec = USASpecProvider()
    assert usaspec.personality('MBTI') != 'ISFJ'


# Generated at 2022-06-13 23:13:48.361553
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    expected = 'ISFJ'
    actual = USASpecProvider().personality('mbti')
    assert actual == expected, 'Failed to create a valid mbti type'

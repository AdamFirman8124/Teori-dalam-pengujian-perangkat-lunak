

# Generated at 2022-06-13 23:13:04.815819
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    a = USASpecProvider()
    mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
             'ISTP', 'ISFP', 'INFP', 'INTP',
             'ESTP', 'ESFP', 'ENFP', 'ENTP',
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert a.personality(category='mbti') in mbtis
    assert 1 <= a.personality(category='rheti') <= 10

# Generated at 2022-06-13 23:13:09.774478
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_sp = USASpecProvider(seed=123)
    assert usa_sp.personality(category='mbti') == 'ENFJ'
    assert usa_sp.personality(category='rheti') == 3
    assert usa_sp.personality(category='show') == 'ISFP'


# Generated at 2022-06-13 23:13:13.077475
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    a1 = USASpecProvider().personality(category='rheti')
    print('a1:', a1)
    assert a1 != a1


# Generated at 2022-06-13 23:13:22.514435
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    from mimesis.providers.usa.usa_provider import USASpecProvider
    
    us_sp = USASpecProvider()

    mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
             'ISTP', 'ISFP', 'INFP', 'INTP',
             'ESTP', 'ESFP', 'ENFP', 'ENTP',
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

    assert us_sp.personality() in mbtis
    assert 1 <= us_sp.personality(category='rheti') <= 10



# Generated at 2022-06-13 23:13:32.018247
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    USASpecProvider = USASpecProvider(seed=12345)

    assert USASpecProvider.personality(category='rheti') in range(1,11)
    assert USASpecProvider.personality(category='mbti') in {'ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'}


# Generated at 2022-06-13 23:13:37.385730
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Test that the method personality of class USASpecProvider return a correct value."""
    import re

    provider = USASpecProvider()
    mbtis = re.compile('(\w?\w?\w?\w?)')
    assert re.match(mbtis, provider.personality())


# Generated at 2022-06-13 23:13:39.535036
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Test method personality of class USASpecProvider."""
    usa = USASpecProvider()
    print(usa.personality())

# Generated at 2022-06-13 23:13:46.608451
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert(USASpecProvider().personality().upper() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ') )

# Generated at 2022-06-13 23:13:52.824331
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usProvider = USASpecProvider()
    assert usProvider.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                        'ISTP', 'ISFP', 'INFP', 'INTP',
                                        'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert 1 <= usProvider.personality('rheti') <= 10


# Generated at 2022-06-13 23:14:00.225393
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Tests a method that generates a type of personality"""
    from mimesis.enums import Personality

    provider = USASpecProvider()
    mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
             'ISTP', 'ISFP', 'INFP', 'INTP',
             'ESTP', 'ESFP', 'ENFP', 'ENTP',
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert provider.personality() in mbtis
    assert provider.personality(category=Personality.MBTI) in mbtis
    assert provider.personality(category='rheti') in range(1, 10)
    assert provider.personality(category=Personality.RHETI) in range(1, 10)

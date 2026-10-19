

# Generated at 2022-06-13 23:13:01.313964
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality() in (
        'ISFJ', 'ISTJ', 'INFJ', 'INTJ',
        'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP',
        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')



# Generated at 2022-06-13 23:13:11.825734
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # Test character
    personality_1 = USASpecProvider().personality(category='mbti')
    personality_2 = USASpecProvider().personality(category='mbti')
    personality_3 = USASpecProvider().personality(category='mbti')
    assert personality_1 == personality_2
    assert personality_1 == personality_3
    assert isinstance(personality_1, str)

    # Test numeric
    personality_1 = USASpecProvider().personality(category='rheti')
    personality_2 = USASpecProvider().personality(category='rheti')
    personality_3 = USASpecProvider().personality(category='rheti')
    assert personality_1 == personality_2
    assert personality_1 == personality_3
    assert isinstance(personality_1, int)


# Generated at 2022-06-13 23:13:15.507899
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usprovider = USASpecProvider()
    assert isinstance(usprovider.personality(), str)
    assert isinstance(usprovider.personality('rheti'), int)
    


# Generated at 2022-06-13 23:13:23.381561
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_sp = USASpecProvider()
    type_of_personality = usa_sp.personality()
    assert type_of_personality in [
        'ISFJ',
        'ISTJ',
        'INFJ',
        'INTJ',
        'ISTP',
        'ISFP',
        'INFP',
        'INTP',
        'ESTP',
        'ESFP',
        'ENFP',
        'ENTP',
        'ESTJ',
        'ESFJ',
        'ENFJ',
        'ENTJ'
    ]

# Generated at 2022-06-13 23:13:30.129378
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_provider = USASpecProvider()
    personality = usa_provider.personality()
    assert personality in ('ISFJ','ISTJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ','ENTJ')


# Generated at 2022-06-13 23:13:31.429560
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    for i in range(10):
        result = provider.personality('rheti')
        print(result)

# Generated at 2022-06-13 23:13:33.508405
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    up = USASpecProvider()
    assert type(up.personality() == str)

# Generated at 2022-06-13 23:13:40.109947
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Unit test for method personality of class USASpecProvider."""
    provider = USASpecProvider()
    result = provider.personality()
    assert result in \
        ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
         'ISTP', 'ISFP', 'INFP', 'INTP',
         'ESTP', 'ESFP', 'ENFP', 'ENTP',
         'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')



# Generated at 2022-06-13 23:13:43.243713
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert isinstance(usa.personality(), str)
    assert isinstance(usa.personality(category='rheti'), int)


# Generated at 2022-06-13 23:13:51.404895
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    p = USASpecProvider()
    assert p.personality('mbti') in ('ISFJ','ISTJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ','ENTJ')
    assert isinstance(p.personality('rheti'), int)
    assert 0 <= p.personality('rheti') <= 10

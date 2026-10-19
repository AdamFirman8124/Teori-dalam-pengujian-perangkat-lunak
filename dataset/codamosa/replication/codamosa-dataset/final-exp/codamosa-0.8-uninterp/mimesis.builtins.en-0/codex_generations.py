

# Generated at 2022-06-13 23:12:58.419115
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Test the method personality."""
    assert USASpecProvider().personality('rheti') in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert USASpecProvider().personality('mbti') in ['ISFJ', 'ISTP', 'INFJ', 'INTJ',
                                                     'ISTJ', 'ISFP', 'INFP', 'INTP',
                                                     'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                                     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']


# Generated at 2022-06-13 23:13:01.434703
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    assert len(provider.personality()) == 4
    assert provider.personality(category='rheti') in range(1, 10)

# Generated at 2022-06-13 23:13:04.662427
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    data = {
        'mbti': 'ISFJ',
        'rheti': 9,
    }
    assert USASpecProvider().personality(category='mbti') in data.values()


# Generated at 2022-06-13 23:13:11.779341
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    spec_provider = USASpecProvider()
    assert spec_provider.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                           'ISTP', 'ISFP', 'INFP', 'INTP',
                                           'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                           'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert spec_provider.personality('rheti') in range(1, 11)


# Generated at 2022-06-13 23:13:20.115991
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Test method."""
    usa = USASpecProvider()
    assert isinstance(usa.personality(), str)
    assert isinstance(usa.personality(), str)
    assert isinstance(usa.personality('rheti'), int)
    assert isinstance(usa.personality('rheti'), int)
    assert isinstance(usa.personality('rheti'), int)
    assert isinstance(usa.personality('rheti'), int)
    assert isinstance(usa.personality('rheti'), int)


# Generated at 2022-06-13 23:13:28.397464
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()

# Generated at 2022-06-13 23:13:31.316790
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Test personality of USASpecProvider."""
    provider = USASpecProvider()
    x = provider.personality()


# Generated at 2022-06-13 23:13:39.428944
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    assert provider.personality(category='mbti') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP',
                                                     'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ',
                                                     'ENFJ', 'ENTJ')
    assert provider.personality(category='rheti') in range(1, 10)



# Generated at 2022-06-13 23:13:43.137435
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    p = USASpecProvider(seed=0)
    assert p.personality(category='mbti') == 'ISTJ'
    assert p.personality(category='rheti') == 9


# Generated at 2022-06-13 23:13:47.712178
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    category = 'mbti'
    personality = provider.personality(category)
    assert(personality is not None)

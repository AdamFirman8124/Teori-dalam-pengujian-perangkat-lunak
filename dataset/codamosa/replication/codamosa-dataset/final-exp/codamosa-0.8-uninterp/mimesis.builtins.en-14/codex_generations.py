

# Generated at 2022-06-13 23:12:58.979422
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality() != None


# Generated at 2022-06-13 23:13:01.103947
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    assert isinstance(provider.personality(), str)


# Generated at 2022-06-13 23:13:07.862537
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    tmp = USASpecProvider()
    assert tmp.personality(category='rheti') in list(range(1, 10+1))
    assert tmp.personality(category='mbti') in ['ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

# Generated at 2022-06-13 23:13:12.657980
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    data_provider = USASpecProvider()
    assert data_provider.personality() in (
        'ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP',
        'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ',
        'ESFJ', 'ENFJ', 'ENTJ'
    )

# Generated at 2022-06-13 23:13:21.761811
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()

    for _ in range(0, 100):
        assert provider.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                          'ISTP', 'ISFP', 'INFP', 'INTP',
                                          'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                          'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

    for _ in range(0, 100):
        assert provider.personality('rheti') in range(1, 11)


# Generated at 2022-06-13 23:13:31.026750
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Method for unit testing."""
    provider = USASpecProvider()
    assert provider.personality('mbti') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                            'ISTP', 'ISFP', 'INFP', 'INTP',
                                            'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                            'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

    assert 1 <= provider.personality('rheti') <= 10

# Generated at 2022-06-13 23:13:34.616982
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert len(USASpecProvider().personality()) == 4
    assert len(USASpecProvider().personality(category='rheti')) == 1


# Generated at 2022-06-13 23:13:38.358624
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Create provider and get personality."""
    u = USASpecProvider()
    assert len(u.personality('rheti')) == 1
    assert len(u.personality()) == 4


# Generated at 2022-06-13 23:13:39.609367
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    tmp = USASpecProvider()
    print(tmp.personality())

# Generated at 2022-06-13 23:13:47.175012
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    print("Begin test_USASpecProvider_personality")
    provider = USASpecProvider()
    assert provider.personality() == 'ISFJ'
    assert provider.personality('mbti') == 'ISFP'
    assert provider.personality('rheti') == 1
    print("End test_USASpecProvider_personality")

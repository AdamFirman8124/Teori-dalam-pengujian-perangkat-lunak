

# Generated at 2022-06-13 23:13:05.220324
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    for _ in range(100):
        assert provider.personality() in ('ISFJ', 'ISTJ', 'INFJ',
                                          'INTJ', 'ISTP', 'ISFP',
                                          'INFP', 'INTP', 'ESTP',
                                          'ESFP', 'ENFP', 'ENTP',
                                          'ESTJ', 'ESFJ', 'ENFJ',
                                          'ENTJ')
        assert provider.personality('rheti') in range(1, 11)


# Generated at 2022-06-13 23:13:10.589755
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # initialize provider
    usa = USASpecProvider()
    assert usa.personality()

    # set variable to person
    person = usa.personality()
    assert isinstance(person, str)

    # unit test for method personality of class USASpecProvider
    assert usa.personality() == person


# Initialize negative unit test for method personality of class USASpecProvider

# Generated at 2022-06-13 23:13:22.429055
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    for i in range(100):
        assert provider.personality(category='mbti') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                                         'ISTP', 'ISFP', 'INFP', 'INTP',
                                                         'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                                         'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    for i in range(100):
        assert provider.personality(category='rheti') in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Generated at 2022-06-13 23:13:31.086426
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # arrange
    provider = USASpecProvider()

    samples = ['ISFJ', 'ISTJ', 'INFJ', 'INTJ',
               'ISTP', 'ISFP', 'INFP', 'INTP',
               'ESTP', 'ESFP', 'ENFP', 'ENTP',
               'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

    # act
    res = provider.personality(category='mbti')

    # assert
    assert res in samples

# Generated at 2022-06-13 23:13:40.281065
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Unit test for method personality of class USASpecProvider"""
    usa = USASpecProvider()
    assert usa.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                 'ISTP', 'ISFP', 'INFP', 'INTP',
                                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert (1 <= usa.personality(category='rheti') <= 10)
    assert usa.personality(category='tyu') is None


# Generated at 2022-06-13 23:13:50.263378
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
             'ISTP', 'ISFP', 'INFP', 'INTP',
             'ESTP', 'ESFP', 'ENFP', 'ENTP',
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    from mimesis.providers.usa import USASpecProvider
    us_obj = USASpecProvider()
    for _ in range(0, 1000):
        assert us_obj.personality(category='mbti') in mbtis



# Generated at 2022-06-13 23:13:56.611307
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # Unit test for method personality of class USASpecProvider
    usa = USASpecProvider()
    assert usa.personality(category='') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                            'ISTP', 'ISFP', 'INFP', 'INTP',
                                            'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                            'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert 1 <= usa.personality(category='rheti') <= 10


# Generated at 2022-06-13 23:13:59.920837
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider(seed=2)
    response = provider.personality()
    assert response == 'INFJ'


# Generated at 2022-06-13 23:14:03.024356
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert usa.personality() in usa.personality('mbti').split()
    assert usa.personality(category='rheti') in usa.personality('rheti').split()



# Generated at 2022-06-13 23:14:04.319992
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert usa.personality() in usa.mbtis
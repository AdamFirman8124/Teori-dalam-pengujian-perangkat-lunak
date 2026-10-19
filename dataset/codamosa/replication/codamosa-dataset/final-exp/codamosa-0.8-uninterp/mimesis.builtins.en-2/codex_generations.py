

# Generated at 2022-06-13 23:13:03.334394
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usaSpecProvider = USASpecProvider()
    assert usaSpecProvider.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                             'ISTP', 'ISFP', 'INFP', 'INTP',
                                             'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert 1 <= usaSpecProvider.personality(category='rheti') <= 10



# Generated at 2022-06-13 23:13:12.110599
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
             'ISTP', 'ISFP', 'INFP', 'INTP',
             'ESTP', 'ESFP', 'ENFP', 'ENTP',
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

    usa_spec_provider = USASpecProvider()
    mbti = usa_spec_provider.personality(category='mbti')

    assert mbti in mbtis

    mbti = usa_spec_provider.personality(category='rheti')

    assert 1 <= mbti <= 10

# Generated at 2022-06-13 23:13:15.299722
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    test_instance = USASpecProvider()
    result = test_instance.personality('mbti')
    assert 4 <= len(result) <= 5



# Generated at 2022-06-13 23:13:25.452123
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert(USASpecProvider().personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                               'ISTP', 'ISFP', 'INFP', 'INTP',
                                               'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                               'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'))
    assert(USASpecProvider().personality(category='random') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                                                'ISTP', 'ISFP', 'INFP', 'INTP',
                                                                'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                                                'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'))

# Generated at 2022-06-13 23:13:36.186065
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    from mimesis.providers.personality.us import USASpecProvider

    usa_provider = USASpecProvider()
    personality = usa_provider.personality()
    assert personality in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) or \
        personality in (
            'ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
            'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
        )

# Generated at 2022-06-13 23:13:42.435324
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert usa.personality() in ['ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                 'ISTP', 'ISFP', 'INFP', 'INTP',
                                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
    assert isinstance(usa.personality('Rheti'), int)
    assert usa.personality('Rheti') in range(1, 11)



# Generated at 2022-06-13 23:13:52.175801
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():

    # Initialization of the class object
    provider = USASpecProvider()

    #  Entering an incorrect category
    assert provider.personality('rheti') in range(1, 10)

    # Entering an incorrect category
    assert provider.personality('mbti') in ['ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                            'ISTP', 'ISFP', 'INFP', 'INTP',
                                            'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                            'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

# Generated at 2022-06-13 23:13:54.475230
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # Call method under test
    provider = USASpecProvider()
    result = provider.personality(category="rheti")

    assert 1 <= result <= 10


# Generated at 2022-06-13 23:14:00.068246
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    from mimesis.providers.usa import USASpecProvider
    from mimesis.enums import PersonalityCategory

    USASpecProvider().personality(category=PersonalityCategory.MBTI)
    USASpecProvider().personality(category=PersonalityCategory.RHETI)


# Generated at 2022-06-13 23:14:09.521233
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert usa.personality(category='mbti') in [
        'ISFJ', 'ISTJ', 'INFJ', 'INTJ',
        'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP',
        'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
    ]
    assert isinstance(usa.personality(category='rheti'), int)


#Unit test for method tracking_number of class USASpecProvider
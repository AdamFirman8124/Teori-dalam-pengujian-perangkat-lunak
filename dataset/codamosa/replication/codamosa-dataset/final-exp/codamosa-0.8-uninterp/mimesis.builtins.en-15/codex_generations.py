

# Generated at 2022-06-13 23:12:58.444275
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # test with category: mbti
    assert USASpecProvider().personality('mbti') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                                     'ISTP', 'ISFP', 'INFP', 'INTP',
                                                     'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                                     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    # test with category: Rheti
    assert isinstance(USASpecProvider().personality('Rheti'), int)

# Generated at 2022-06-13 23:13:01.053136
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    y = USASpecProvider()
    x = y.personality(category='rheti')
    assert isinstance(x,int)

# Generated at 2022-06-13 23:13:06.637011
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usaProvider = USASpecProvider()
    assert usaProvider.personality().upper() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                 'ISTP', 'ISFP', 'INFP', 'INTP',
                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

# Generated at 2022-06-13 23:13:10.367016
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():

    # Get the result of method personality of class USASpecProvider
    result = USASpecProvider.personality()
    # print("Test_1: result=", result)

    # Assert the result
    assert True


# Generated at 2022-06-13 23:13:21.554566
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    #test if result is string
    result = USASpecProvider.personality(USASpecProvider(), "mbti")
    assert isinstance(result, str)
    #test result is one of the elements
    mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
             'ISTP', 'ISFP', 'INFP', 'INTP',
             'ESTP', 'ESFP', 'ENFP', 'ENTP',
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert result in mbtis
    #test result is a integer
    result = USASpecProvider.personality(USASpecProvider(), "rheti")
    assert isinstance(result, int)


# Generated at 2022-06-13 23:13:35.901830
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    mbtis = ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
             'ISTP', 'ISFP', 'INFP', 'INTP',
             'ESTP', 'ESFP', 'ENFP', 'ENTP',
             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

    test = USASpecProvider()

    def check_mbti_type(t):  # type: (str) -> bool
        return t in mbtis

    assert test.personality('mbti') in mbtis
    assert test.personality('rheti') in range(1, 11)

    personality = test.personality()
    assert personality in mbtis or (isinstance(personality, int) and personality in range(1, 11))


# Generated at 2022-06-13 23:13:40.609650
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_spec_provider = USASpecProvider()
    assert usa_spec_provider.personality('MBTI') in ('ISFJ', 'ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

# Generated at 2022-06-13 23:13:47.664181
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_spec_provider = USASpecProvider()
    assert(len(usa_spec_provider.personality())==4)
    assert(isinstance(usa_spec_provider.personality(category='rheti'), int))
    assert(usa_spec_provider.personality(category='rheti') in range(1,11))

# Generated at 2022-06-13 23:13:56.791308
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    assert provider.personality('mbti') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                            'ISTP', 'ISFP', 'INFP', 'INTP',
                                            'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                            'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert provider.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                       'ISTP', 'ISFP', 'INFP', 'INTP',
                                       'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                       'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

# Generated at 2022-06-13 23:14:00.055107
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                             'ISTP', 'ISFP', 'INFP', 'INTP',
                             'ESTP', 'ESFP', 'ENFP', 'ENTP',
                             'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
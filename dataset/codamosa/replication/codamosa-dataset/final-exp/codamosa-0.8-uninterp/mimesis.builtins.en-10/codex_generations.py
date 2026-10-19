

# Generated at 2022-06-13 23:13:04.364657
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
	personality1 = USASpecProvider().personality(category='mbti')
	assert personality1 in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                 'ISTP', 'ISFP', 'INFP', 'INTP',
                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')


# Generated at 2022-06-13 23:13:10.888959
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    us = USASpecProvider()
    assert us.personality(category='mbti') in ['ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                'ISTP', 'ISFP', 'INFP', 'INTP',
                'ESTP', 'ESFP', 'ENFP', 'ENTP',
                'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
    assert us.personality(category='rheti') in range(1, 10)

# Generated at 2022-06-13 23:13:20.171764
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Tests for USASpecProvider."""
    personality = USASpecProvider().personality()

    # Test: personality() method is working without raising exceptions
    assert isinstance(personality, str)

    # Test: personality() method is using correct types of answer
    assert personality in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                           'ISTP', 'ISFP', 'INFP', 'INTP',
                           'ESTP', 'ESFP', 'ENFP', 'ENTP',
                           'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')



# Generated at 2022-06-13 23:13:26.741461
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert usa.personality(category='mbti') in ['ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                                'ISTP', 'ISFP', 'INFP', 'INTP',
                                                'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                                'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
    assert usa.personality(category='rheti') in [i for i in range(1, 11)]

# Generated at 2022-06-13 23:13:36.442458
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    us = USASpecProvider()
    assert us.personality(category="mbti") in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                       'ISTP', 'ISFP', 'INFP', 'INTP',
                                       'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                       'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert us.personality(category="rheti") in  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Generated at 2022-06-13 23:13:42.522163
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    print()
    print(USASpecProvider(seed=4321).personality())
    print(USASpecProvider(seed=4321).personality(category='rheti'))
    print(USASpecProvider(seed=4321).personality(category='mbti'))
    print(USASpecProvider(seed=4321).personality())
    print(USASpecProvider(seed=4321).personality(category='rheti'))
    print(USASpecProvider(seed=4321).personality(category='mbti'))


# Generated at 2022-06-13 23:13:53.034768
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    p = USASpecProvider()
    # This is a demo test, the returned value may change in the future
    assert p.personality() in (
        'ISFJ', 'ISTJ', 'INFJ', 'INTJ',
        'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP',
        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
    )
    assert p.personality(category='Rheti') in range(1, 10)
    assert p.personality('Rheti') in range(1, 10)



# Generated at 2022-06-13 23:13:55.665437
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    from mimesis.providers.us_provider import USASpecProvider
    us = USASpecProvider(seed=1)
    assert us.personality() == 'ESFJ'
    assert us.personality(category='rheti') == 8

# Generated at 2022-06-13 23:14:03.334613
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Test function, which test method personality of class USASpecProvider."""
    from mimesis.enums import DataCategory
    from mimesis.providers.usa import USASpecProvider

    personality = USASpecProvider('en')
    personality.seed(42)

    res_1 = personality.personality(DataCategory.RHETI)
    res_2 = personality.personality(DataCategory.MYERS_BRIGGS)

    assert res_1 == 2
    assert res_2 == 'ENTJ'

# Generated at 2022-06-13 23:14:10.330515
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # arrange
    result = USASpecProvider().personality()
    expected = result in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                          'ISTP', 'ISFP', 'INFP', 'INTP',
                          'ESTP', 'ESFP', 'ENFP', 'ENTP',
                          'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

    # assert
    assert expected

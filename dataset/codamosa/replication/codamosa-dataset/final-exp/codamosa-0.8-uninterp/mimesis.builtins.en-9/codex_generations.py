

# Generated at 2022-06-13 23:13:04.311225
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_provider = USASpecProvider()
    assert usa_provider.personality() == 'ESFP' or 'ENFP' or 'ISFP' or 'ISFJ' or 'ENTP' or 'ENTJ' or 'ENFJ' or 'ESTP'\
                                          or 'ISTP' or 'INFP' or 'INFJ' or 'INTP' or 'ISTJ' or 'ESFJ' or 'ESTJ'\
                                          or 'INTJ'


# Generated at 2022-06-13 23:13:12.657224
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """ Unit test for USASpecProvider class method personality """
    instance_1 = USASpecProvider()
    assert instance_1.personality() in ['ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                        'ISTP', 'ISFP', 'INFP', 'INTP',
                                        'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
    assert isinstance(instance_1.personality('rheti'), int)
    assert instance_1.personality('rheti') > 0
    assert instance_1.personality('rheti') < 11

# Generated at 2022-06-13 23:13:22.884287
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """
    Purpose:
        Unit tests for USASpecProvider class. Given a category, it should return a valid
        personality type.
    Args:
        N/A
    Returns:
        N/A
    Raises:
        N/A
    """
    usaspp = USASpecProvider()
    personality = usaspp.personality()
    assert personality in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                           'ISTP', 'ISFP', 'INFP', 'INTP',
                           'ESTP', 'ESFP', 'ENFP', 'ENTP',
                           'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')



# Generated at 2022-06-13 23:13:33.729944
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
	"""
	Test case for method personality of class USASpecProvider
	"""
	test_mbti = USASpecProvider().personality()
	assert test_mbti in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                 'ISTP', 'ISFP', 'INFP', 'INTP',
                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
	test_rheti = USASpecProvider().personality(category='rheti')
	assert test_rheti in range(1,11)


# Generated at 2022-06-13 23:13:34.534316
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
	# Passed
	pass

# Generated at 2022-06-13 23:13:38.300147
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    a = usa.personality('mbti')
    a_check = 'ISFJ'
    assert (a == a_check)


# Generated at 2022-06-13 23:13:41.514916
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    assert provider.personality() in {'ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                      'ISTP', 'ISFP', 'INFP', 'INTP',
                                      'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                      'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'}


# Generated at 2022-06-13 23:13:46.608824
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider(seed=12345).personality(category='mbti') == 'ENTP'
    assert USASpecProvider(seed=12345).personality(category='rheti') == 8


# Generated at 2022-06-13 23:13:51.145026
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    temp = USASpecProvider()
    assert temp.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                  'ISTP', 'ISFP', 'INFP', 'INTP',
                                  'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                  'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert 1 <= temp.personality('rheti') <= 10


# Generated at 2022-06-13 23:13:55.810348
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    import random
    from mimesis.builtins.usa import USASpecProvider
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r = random.Random()
    r.choice = lambda x: choices[9]
    usaSpecProvider = USASpecProvider(seed=r)
    assert usaSpecProvider.personality(category='rheti') == 10
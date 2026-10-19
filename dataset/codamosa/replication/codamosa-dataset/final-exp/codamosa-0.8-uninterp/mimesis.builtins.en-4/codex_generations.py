

# Generated at 2022-06-13 23:12:56.329440
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Unit test for method personality."""
    usa = USASpecProvider()
    assert usa.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                 'ISTP', 'ISFP', 'INFP', 'INTP',
                                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')


# Generated at 2022-06-13 23:13:06.183505
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Unit test for method personality of class USASpecProvider"""
    spec = USASpecProvider()
    personality = spec.personality()
    assert personality in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP',
                           'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                           'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

    personality = spec.personality(category='rheti')
    assert personality in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



# Generated at 2022-06-13 23:13:13.996372
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    USASpecProvider_personality_v1 = USASpecProvider().personality(category='rheti')
    assert USASpecProvider_personality_v1 <=10 and USASpecProvider_personality_v1 >=1

    USASpecProvider_personality_v2 = USASpecProvider().personality(category='mbti')
    assert USASpecProvider_personality_v2 in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')


# Generated at 2022-06-13 23:13:24.375329
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    data = []
    for i in range(100):
        p1 = USASpecProvider(seed=i).personality(category='mbti')
        p2 = USASpecProvider(seed=i).personality(category='rheti')
        data.append((p1, p2))


# Generated at 2022-06-13 23:13:31.124813
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    ups = USASpecProvider()
    dict_personality = dict()
    for i in range(100):
        p = ups.personality()
        print(p)
        if p not in dict_personality:
            dict_personality[p] = 1
        else:
            dict_personality[p] += 1
    print(dict_personality)


# Generated at 2022-06-13 23:13:37.073619
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Tests for USASpecProvider().personality()."""
    us = USASpecProvider()
    assert us.personality() not in ('', None)
    assert us.personality('rheti') != ''
    assert type(us.personality()) == str
    assert type(us.personality('rheti')) == int


# Generated at 2022-06-13 23:13:42.647202
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                               'ISTP', 'ISFP', 'INFP', 'INTP',
                                               'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                               'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert type(USASpecProvider().personality(category='rheti')) == int
    assert 0 < USASpecProvider().personality(category='rheti') < 11
    assert -1 < USASpecProvider().personality(category='rheti') < 10
    assert -1 < USASpecProvider().personality(category='rheti') < 10

# Generated at 2022-06-13 23:13:48.452993
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    # print('Executing function USASpecProvider_personality')
    provider = USASpecProvider()
    assert type(provider.personality('mbti')) is str
    assert type(provider.personality('rheti')) is int


# Generated at 2022-06-13 23:13:50.358382
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert isinstance(
        usa.personality(),
        str
    )

# Generated at 2022-06-13 23:13:56.387188
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    p = provider.personality()
    assert p in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                 'ISTP', 'ISFP', 'INFP', 'INTP',
                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    p = provider.personality(category='R')
    assert isinstance(p, int)
    assert p in range(1, 11)
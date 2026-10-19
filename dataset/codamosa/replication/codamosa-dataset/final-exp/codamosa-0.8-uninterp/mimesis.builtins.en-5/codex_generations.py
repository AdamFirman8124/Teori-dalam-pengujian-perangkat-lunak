

# Generated at 2022-06-13 23:13:01.154659
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_provider = USASpecProvider()

    assert isinstance(usa_provider.personality(), str)
    assert isinstance(usa_provider.personality(category='rheti'), int)


# Generated at 2022-06-13 23:13:06.335818
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality("rheti") == 3
    assert USASpecProvider().personality("rheti") != 4
    assert USASpecProvider().personality("rheti") != 2
    assert USASpecProvider().personality() == "INFJ"
    assert USASpecProvider().personality() != "Rheti"


# Generated at 2022-06-13 23:13:14.664470
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    from mimesis.enums import Category
    from mimesis.providers.usa.usa import USASpecProvider
    sp = USASpecProvider()
    print('test for method personality of class USASpecProvider')
    print(f'\t{sp.personality(category=Category.RHETI)}')
    print(f'\t{sp.personality(category=Category.RHETI)}')
    print(f'\t{sp.personality(category=Category.RHETI)}')
    print(f'\t{sp.personality(category=Category.MBTI)}')
    print(f'\t{sp.personality(category=Category.MBTI)}')
    print(f'\t{sp.personality(category=Category.MBTI)}')

# Generated at 2022-06-13 23:13:21.709211
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    import random
    
    assert len(random.choice(mbtis)) == 4
    assert isinstance(random.randint(1,10),int)
    return 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

test_USASpecProvider_personality()

# Generated at 2022-06-13 23:13:27.476653
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    a = USASpecProvider()
    for x in range(100):
        assert len(a.personality(category='mbti')) in range(2, 5)
        assert a.personality(category='rheti') in range(1, 11)


# Generated at 2022-06-13 23:13:37.137731
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    up = USASpecProvider()
    result = up.personality()
    assert result in ("ISFJ", "ISTJ", "INFJ", "INTJ", "ISTP",
                      "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP",
                      "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ")
    result = up.personality(category='rheti')
    assert result in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Generated at 2022-06-13 23:13:41.777740
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    tmp = USASpecProvider()
    assert tmp.personality() in ['ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                 'ISTP', 'ISFP', 'INFP', 'INTP',
                                 'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
    assert tmp.personality('rheti') in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generated at 2022-06-13 23:13:50.627744
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_spec_provider = USASpecProvider()
    mbti_type_list = [i for i in range(1, 17)]
    for i in range(100):
        assert usa_spec_provider.personality(category='mbti') in mbti_type_list
    assert usa_spec_provider.personality(category='rheti') in mbti_type_list
    assert usa_spec_provider.personality(category='dummy') is None


# Generated at 2022-06-13 23:13:54.062824
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa = USASpecProvider()
    assert isinstance(usa.personality('mbti'), str)
    assert isinstance(usa.personality('rheti'), int)

if __name__ == "__main__":
    test_USASpecProvider_personality()

# Generated at 2022-06-13 23:14:01.394822
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                  'ISTP', 'ISFP', 'INFP', 'INTP',
                                  'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                  'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert isinstance(USASpecProvider().personality(category='rheti'), int)

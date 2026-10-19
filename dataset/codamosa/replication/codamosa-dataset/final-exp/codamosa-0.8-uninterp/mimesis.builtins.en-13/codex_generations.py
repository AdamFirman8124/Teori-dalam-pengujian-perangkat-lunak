

# Generated at 2022-06-13 23:12:53.621672
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    p = USASpecProvider()
    assert isinstance(p.personality(), str)
    assert len(p.personality()) == 4
    assert p.personality(category='rheti') in range(1, 11)

# Generated at 2022-06-13 23:12:59.611305
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    new_usaspecprovider = USASpecProvider()
    print(new_usaspecprovider.personality())

    # ISFJ
    print(new_usaspecprovider.personality())
    # ISTJ
    print(new_usaspecprovider.personality())
    # INFJ
    print(new_usaspecprovider.personality())
    # INTJ
    print(new_usaspecprovider.personality())
    # ESTP
    print(new_usaspecprovider.personality())
    # ESFP
    print(new_usaspecprovider.personality())
    # ENFP
    print(new_usaspecprovider.personality())
    # ENTP
    print(new_usaspecprovider.personality())
    # ESTJ

# Generated at 2022-06-13 23:13:07.967269
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    us_provider = USASpecProvider()

    assert us_provider.personality(category='rheti') >= 1
    assert us_provider.personality(category='rheti') <= 10
    assert us_provider.personality(category='mbti') in (
        'ISFJ', 'ISTJ', 'INFJ', 'INTJ',
        'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP',
        'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
    )

# Generated at 2022-06-13 23:13:11.271718
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_personality = USASpecProvider()
    assert isinstance(usa_personality.personality(category='mbti'), str)
    assert isinstance(usa_personality.personality(category='rheti'), int)


# Generated at 2022-06-13 23:13:18.671441
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    print("\nStart test_USASpecProvider_personality")
    usa = USASpecProvider()
    assert usa.personality("mbti") in (
        "ISFJ", "ISTJ", "INFJ", "INTJ",
        "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP",
        "ESTJ", "ESFJ", "ENFJ", "ENTJ")

# Generated at 2022-06-13 23:13:25.229308
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    e_rheti = USASpecProvider().personality(category='rheti')
    assert 1 <= e_rheti <= 10

    e_mbti = USASpecProvider().personality(category='mbti')
    assert e_mbti in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

# Generated at 2022-06-13 23:13:35.514364
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()

    # 'mbti' is the same as 'MBTI' or 'MBT' or 'mbt'.
    assert provider.personality(category='mbt') in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                                    'ISTP', 'ISFP', 'INFP', 'INTP',
                                                    'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                                    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert provider.personality(category='rheti') in range(1, 11)

# Generated at 2022-06-13 23:13:42.147825
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Unit test for method personality of class USASpecProvider."""

    us_en = USASpecProvider()
    assert us_en.personality() in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                                   'ISTP', 'ISFP', 'INFP', 'INTP',
                                   'ESTP', 'ESFP', 'ENFP', 'ENTP',
                                   'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')
    assert isinstance(us_en.personality(category='rheti'), int)  # type: ignore

# Generated at 2022-06-13 23:13:49.735327
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality() in ("ISFJ", "ISTJ", "INFJ", "INTJ",
                                               "ISTP", "ISFP", "INFP", "INTP",
                                               "ESTP", "ESFP", "ENFP", "ENTP",
                                               "ESTJ", "ESFJ", "ENFJ", "ENTJ")


# Generated at 2022-06-13 23:13:52.175639
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    us = USASpecProvider()
    assert len(us.personality()) is len('ISFJ')
    assert isinstance(us.personality(category='rheti'), int)
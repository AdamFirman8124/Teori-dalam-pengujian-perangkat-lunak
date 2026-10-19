

# Generated at 2022-06-13 23:13:01.001446
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    """Check the function of the method personality.

    :returns: No return.
    :rtype: None
    """
    provider = USASpecProvider()
    p = provider.personality()
    assert type(p) == str

    p1 = provider.personality('rheti')
    assert type(p1) == int



# Generated at 2022-06-13 23:13:03.229589
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    us = USASpecProvider()
    result = us.personality('rheti')
    assert result in range(1, 11)

# Generated at 2022-06-13 23:13:05.981398
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    provider = USASpecProvider()
    provider.personality() # Test for mbti list
    provider.personality('rheti') # Test for Rheti list


# Generated at 2022-06-13 23:13:09.332516
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    usa_provider = USASpecProvider()
    assert usa_provider.personality().isalpha()
    assert usa_provider.personality('rheti').isnumeric()


# Generated at 2022-06-13 23:13:10.718337
# Unit test for method ssn of class USASpecProvider
def test_USASpecProvider_ssn():
    assert USASpecProvider().ssn() == '048-67-4612'

# Generated at 2022-06-13 23:13:13.811103
# Unit test for method ssn of class USASpecProvider
def test_USASpecProvider_ssn():
    usa_spec_provider = USASpecProvider(seed=1)
    assert usa_spec_provider.ssn() == '416-50-9591'



# Generated at 2022-06-13 23:13:21.911203
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    from mimesis.enums import Category

    usa = USASpecProvider()
    assert usa.personality() in Category.MBTI
    assert isinstance(usa.personality(category="rheti"), int)
    assert usa.personality(category="") in Category.MBTI
    assert isinstance(usa.personality(category="rheti"), int)
    assert isinstance(usa.personality(category="rheti"), int)
    assert usa.personality(category="rheti") in range(1, 10)

# Generated at 2022-06-13 23:13:24.820085
# Unit test for method ssn of class USASpecProvider
def test_USASpecProvider_ssn():
    provider = USASpecProvider()

    # Exercise the API and test
    assert len(provider.ssn()) == 11

# Generated at 2022-06-13 23:13:27.739251
# Unit test for method personality of class USASpecProvider
def test_USASpecProvider_personality():
    assert USASpecProvider().personality().endswith(("F", "J", "P", "T"))


# Generated at 2022-06-13 23:13:32.760315
# Unit test for method ssn of class USASpecProvider
def test_USASpecProvider_ssn():
    assert USASpecProvider().ssn() in ['321-23-7716', '321-78-1620',
                                       '321-78-1621', '321-62-9018',
                                       '321-78-1623', '321-62-9019']
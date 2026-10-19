

# Generated at 2022-06-13 23:28:34.949660
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    print()
    print("Unit test for method snils of class RussiaSpecProvider")
    print()
    rus = RussiaSpecProvider()
    print(rus.snils())

# Generated at 2022-06-13 23:28:42.749453
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Test case for method snils of class RussiaSpecProvider.
    """
    russian_provider = RussiaSpecProvider() # Create a RussiaSpecProvider object
    generated_snils = russian_provider.snils() # Generate a snils string
    print(generated_snils) # Print the snils string to console
    assert len(generated_snils) == 11 # Assert the length of the generated string is 11

# Generated at 2022-06-13 23:28:45.946536
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert isinstance(snils, str)
    assert len(snils) == 11
    assert snils.isdigit()


# Generated at 2022-06-13 23:28:49.839838
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    print('\nUnit test for method snils of class RussiaSpecProvider\n')
    provider = RussiaSpecProvider()
    snils = RussiaSpecProvider.snils(provider)
    print('Random snils: {}'.format(snils))


# Generated at 2022-06-13 23:28:53.245503
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    mysnils = ''
    while mysnils.endswith('00'):
        mysnils = rsp.snils()
    print(mysnils)
    assert len(mysnils) == 11

# Generated at 2022-06-13 23:28:55.537236
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert type(result) == str
    assert len(result) == 11


# Generated at 2022-06-13 23:28:57.635289
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert len(result) == 11
    assert result.isdigit()


# Generated at 2022-06-13 23:29:02.735816
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rp = RussiaSpecProvider(seed = '12345')
    snils = rp.snils()
    assert isinstance(snils, str)
    assert snils == '41917492600'


# Generated at 2022-06-13 23:29:04.081947
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    print(provider.snils())

# Generated at 2022-06-13 23:29:12.247394
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils()

    # tm = RussiaSpecProvider()
    # seeds = []
    # results = []
    # for i in range(0, 1000000):
    #     seeds.append(i)
    #     results.append(tm.snils())
    #     tm.seed(seeds[i])
    #
    # for i in range(0, len(results) - 1):
    #     assert results[i] != results[i + 1]



# Generated at 2022-06-13 23:29:35.400499
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    sp = RussiaSpecProvider()
    nums = []
    for i in range(0, 10):
        nums.append(sp.random.randint(0, 9))
    s = (''.join(str(i) for i in nums))
    assert sp.snils() == s

# Generated at 2022-06-13 23:29:42.889012
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import unittest
    from mimesis.providers.russia import RussiaSpecProvider

    class RussiaSpecProviderTestCase(unittest.TestCase):
        def setUp(self):
            self.provider = RussiaSpecProvider()

        def test_snils(self):
            result = self.provider.snils()
            self.assertTrue(
                result.isnumeric() and len(result) == 11)

    unittest.main()

# Generated at 2022-06-13 23:29:49.323172
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    s = ['54323587900', '24323587900', '76323587900', '58503380900', '85294639600', '06485629400', '13676950900',
         '70592423000', '58503380900', '05492717200']
    prov = RussiaSpecProvider()
    for _ in range(0, 10):
        assert prov.snils() in s

# Generated at 2022-06-13 23:29:51.233114
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test = RussiaSpecProvider()
    assert test.snils() == '41917492600'

# Generated at 2022-06-13 23:29:53.990500
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins.russia_provider import RussiaSpecProvider
    rus = RussiaSpecProvider()
    print(rus.snils())
    #41917492600


# Generated at 2022-06-13 23:30:05.169258
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person import Person
    from mimesis.enums import Gender
    import re
    import sys
    if sys.version_info >= (3, 7):
        person = Person('en')
        person.gender = Gender.MALE
        patronymic = person.patronymic(gender=Gender.MALE)
        last_name = person.last_name()
        snils_pattern = r'41917492600'
        snils = re.findall(snils_pattern, person.snils())
        assert snils == snils_pattern
        assert patronymic == 'Алексеевич' or 'Алексеевна'
        assert last_name == 'Смирнов'
        # print(person.

# Generated at 2022-06-13 23:30:08.210286
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    for i in range(0,10):
        print(provider.snils())

test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:30:11.094492
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    actual = provider.snils()
    print(actual)
    expected = 41917492600
    assert actual == expected


# Generated at 2022-06-13 23:30:14.078768
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    tester = RussiaSpecProvider(seed=42)
    assert tester.snils() == "02792652300"


# Generated at 2022-06-13 23:30:17.325575
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert int(snils) > 0 and int(snils) < 10000000000
    assert len(snils) == 11


# Generated at 2022-06-13 23:30:58.013309
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # If you have correct ssn, then you can use it for testing
    valid_snils = '94539034958 % 9453903'
    provider = RussiaSpecProvider()
    assert provider.snils() == valid_snils, 'Bad snils'


# Generated at 2022-06-13 23:31:03.504563
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Проведем тестирование метода с использованием UnitTest библиотеки Python
    import unittest
    class RussiaSpecProviderTestCase(unittest.TestCase):
        def test_snils(self):
            r = RussiaSpecProvider()
            snils_1 = r.snils()
            snils_2 = r.snils()
            self.assertTrue(snils_1 != snils_2)

    unittest.main()


# Generated at 2022-06-13 23:31:06.140651
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    rus_snils = provider.snils()
    assert isinstance(rus_snils, str)
    assert len(rus_snils) == 11


# Generated at 2022-06-13 23:31:09.269347
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    assert len(snils) == 11
    assert isinstance(snils, str)


# Generated at 2022-06-13 23:31:11.061376
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RussiaSpecProvider.snils()


# Generated at 2022-06-13 23:31:13.031282
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    print(provider.snils())


# Generated at 2022-06-13 23:31:17.264649
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    for i in range(0, 1000):
        assert provider.snils() == provider.snils()

# Unit tests for method inn of class RussiaSpecProvider

# Generated at 2022-06-13 23:31:21.363351
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    pr = RussiaSpecProvider()
    assert len(pr.snils()) == 11
    assert pr.snils().isdigit()
    for i in range(0, 100):
        assert pr.snils()

# Generated at 2022-06-13 23:31:25.971344
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    sm = RussiaSpecProvider()
    sm.random.reseed(1)
    import sys
    print(sys.version)
    print(sm.snils())

test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:31:29.051257
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    for _ in range(100):
        snils = provider.snils()
        assert type(snils) == str


# Generated at 2022-06-13 23:32:58.150520
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    obj = RussiaSpecProvider()
    snils = obj.snils()
    assert len(snils) == 11

# Generated at 2022-06-13 23:33:01.463528
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils of class RussiaSpecProvider.
    :return:
    """
    assert RussiaSpecProvider().snils() == '41917492600'

# Generated at 2022-06-13 23:33:07.893249
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test_object = RussiaSpecProvider(seed=1234)
    for _ in range(0, 10):
        assert test_object.snils() in ('61263234581', '76111572600'),\
            "Method RussiaSpecProvider.snils() doesn't work correctly"


# Generated at 2022-06-13 23:33:11.593965
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Create RussiaSpecProvider() object
    rusprovider = RussiaSpecProvider()
    snils = rusprovider.snils()
    # Check if snils is valid
    assert len(snils) == 11

# Generated at 2022-06-13 23:33:23.826856
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.providers.ru.person import Person
    p = Person('ru')
    s = p.snils()
    assert s not in ('00000000000', '99999999999', '12345678901')
    assert len(s) == 11
    assert s == p.snils()
    p = Person('ru', gender=Gender.FEMALE)
    s = p.snils()
    assert s == p.snils(Gender.FEMALE)
    p = Person('ru', gender=Gender.MALE)
    s = p.snils()
    assert s == p.snils(Gender.MALE)
    p = Person('ru', gender=Gender.NOT_SURE)
    s = p.snils()

# Generated at 2022-06-13 23:33:33.670097
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import pytest
    from mimesis.enums import Gender
    from mimesis.exceptions import FieldValueError
    from mimesis.providers.person.rus import snils

    rus = RussiaSpecProvider()

    with pytest.raises(FieldValueError):
        rus.snils()
    with pytest.raises(FieldValueError):
        rus.snils(gender=Gender.MALE)
    with pytest.raises(FieldValueError):
        rus.snils(gender=Gender.FEMALE)

    assert len(rus.snils()) == 11
    assert len(snils(person_=rus, gender=Gender.MALE)) == 11
    assert len(snils(person_=rus, gender=Gender.FEMALE)) == 11

# Generated at 2022-06-13 23:33:37.233797
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test_class = RussiaSpecProvider()
    assert len(str(test_class.snils())) == 11


# Generated at 2022-06-13 23:33:38.019943
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert len(r.snils()) == 11


# Generated at 2022-06-13 23:33:41.998656
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rp = RussiaSpecProvider()
    snils = rp.snils()
    assert len(snils) == 11
    assert snils.isnumeric()
    assert isinstance(snils, str)


# Generated at 2022-06-13 23:33:44.237171
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    sn = RussiaSpecProvider().snils()
    print(sn)

# Generated at 2022-06-13 23:37:41.799743
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider(seed=1)
    assert rsp.snils() == '63652957200'



# Generated at 2022-06-13 23:37:49.508941
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    russia_spec_provider = RussiaSpecProvider()
    snils = russia_spec_provider.snils()
    try:
        int(snils)
    except ValueError:
        raise AssertionError('Incorrect type of value.')
    try:
        assert len(snils) == 11
    except AssertionError:
        raise AssertionError('Incorrect length of value.')



# Generated at 2022-06-13 23:37:51.727596
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for RussiaSpecProvider.snils"""
    t = RussiaSpecProvider()
    assert len(t.snils()) == 11
    assert t.snils().isdigit()

# Generated at 2022-06-13 23:37:57.123572
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method ``snils`` of class ``RussiaSpecProvider``."""
    random_snils = RussiaSpecProvider().snils()
    assert len(str(random_snils)) == 11

# Generated at 2022-06-13 23:38:03.984309
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Check for method snils of class RussiaSpecProvider."""
    # Init provider, method will generate random SNILS
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11


# Generated at 2022-06-13 23:38:05.462708
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    spec = RussiaSpecProvider()
    spec.set_seed('mimesis')
    assert spec.snils() == '41917492600'

# Generated at 2022-06-13 23:38:07.094206
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    seed = 'сброшен'
    rus = RussiaSpecProvider(seed=seed)
    assert rus.snils() == '84914731100', "fail with seed '%s'" % seed


# Generated at 2022-06-13 23:38:11.789701
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Method test_RussiaSpecProvider_snils tests snils method."""
    test_provider_snils = RussiaSpecProvider()
    count = 0
    while (count < 1000):
        result_snils = test_provider_snils.snils()
        assert len(result_snils) == 11
        count += 1


# Generated at 2022-06-13 23:38:14.381569
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils method of class RussiaSpecProvider."""
    data = RussiaSpecProvider(seed=42)
    assert data.snils() == '41917492600'

# Generated at 2022-06-13 23:38:15.843732
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    print(r.snils())

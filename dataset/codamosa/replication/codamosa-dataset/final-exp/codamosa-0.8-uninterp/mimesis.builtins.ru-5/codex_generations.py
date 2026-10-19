

# Generated at 2022-06-13 23:28:43.777613
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    test_list = []
    for i in range(0, 10):
        test_list.append(RussiaSpecProvider().snils())
    test_list2 = []
    for i in range(0, 10):
        test_list2.append(RussiaSpecProvider().snils())
    assert len(test_list) == len(test_list2)
    assert isinstance(test_list[0], str)

# Generated at 2022-06-13 23:28:46.610060
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    instance = RussiaSpecProvider()
    for i in range(100):
        assert len(instance.snils()) == 11

# Generated at 2022-06-13 23:28:49.442215
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a = RussiaSpecProvider()
    snils = a.snils()
    assert snils == '41917492600' or snils == '4191692600' or \
        snils == '4191749260'

# Generated at 2022-06-13 23:28:51.430384
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert len(result) == 11


# Generated at 2022-06-13 23:28:53.466108
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert len(RussiaSpecProvider().snils()) == 11
    assert RussiaSpecProvider().snils().isdigit()


# Generated at 2022-06-13 23:29:01.191572
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    from mimesis import Person

    rus = Person('ru')

    # create a dict for testing a snils
    snils_dict = {
        '41917492600': 0,
        '20353806475': 0,
        '74703106657': 0,
        '56416489370': 0,
        '18162302712': 0,
        '24105416895': 0,
        '39121607959': 0,
        '24625671935': 0,
        '00293179953': 0,
        '99989898982': 0,
    }

    snils_counter = 0
    while snils_counter < 1000000:
        random_snils = rus.snils()

# Generated at 2022-06-13 23:29:12.570846
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Проверка работы метода snils"""

    inst_ru = RussiaSpecProvider()
    d = {}
    snils = inst_ru.snils()
    d[snils] = None
    print("SNILS={0}".format(snils))
    while len(d)<10000:
        snils = inst_ru.snils()
        d[snils] = None
    print("Проверка прошла успешно. Сгенерировано 10000 разных номеров.")

# test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:29:17.546501
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person.ru import RussiaSpecProvider
    russia_spec_provider = RussiaSpecProvider()
    for _ in range(0, 10):
        print(russia_spec_provider.inn())


# Generated at 2022-06-13 23:29:28.661719
# Unit test for method snils of class RussiaSpecProvider

# Generated at 2022-06-13 23:29:31.019711
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    r.snils()

# Generated at 2022-06-13 23:29:51.454702
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    d = RussiaSpecProvider()
    snils = d.snils()
    assert int(snils) % 11 <= 101
    assert len(snils) == 11

# Generated at 2022-06-13 23:29:53.860190
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert len(r.snils()) == 11
    assert r.snils().isdigit()
    assert type(r.snils()) == str


# Generated at 2022-06-13 23:29:57.590263
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    snils = rus.snils()
    assert rus.calculate_checksum(snils) == rus.snils_checksum(snils)


# Generated at 2022-06-13 23:30:05.373665
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider().snils()
    if not snils.isdigit():
        test_RussiaSpecProvider_snils()
    else:
        snils = int(snils)
        if snils < 10019980000:
            test_RussiaSpecProvider_snils()
        elif snils > 99999999999:
            test_RussiaSpecProvider_snils()



# Generated at 2022-06-13 23:30:09.712530
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    r = RussiaSpecProvider()
    snils = r.snils()
    assert len(snils) == 11
    assert snils[9] == snils[10]
    assert r.snils() != r.snils()

# Generated at 2022-06-13 23:30:13.664975
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    print("\n\ntest for snils\n")
    instance = RussiaSpecProvider()
    snils = instance.snils()
    print(snils)

    assert len(snils) == 11


# Generated at 2022-06-13 23:30:25.659242
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11
    assert provider.snils() == '41917492600'
    assert provider.snils() == '29805744300'
    assert provider.snils() == '97785975400'
    assert provider.snils() == '67995435500'
    assert provider.snils() == '94820494800'
    assert provider.snils() == '62046530200'
    assert provider.snils() == '96881213200'
    assert provider.snils() == '57804444100'
    assert provider.snils() == '90818536400'
    assert provider.snils() == '09457712800'
    assert provider.snils() == '05813371400'

# Generated at 2022-06-13 23:30:27.297394
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    result = r.snils()
    print(result)


# Generated at 2022-06-13 23:30:36.347266
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    # Test: check that field 'snils' is added to the class
    assert hasattr(RussiaSpecProvider, 'snils')
    # Test: check that result of method snils is not empty
    assert provider.snils() != ''

    # Test: check that method snils generate a result with length 11
    assert len(provider.snils()) == 11

    # Test: check that method snils generate a result of type string
    assert type(provider.snils()) == str

    # Test: check that method snils generate a result without a slash
    assert provider.snils().find('/') == -1



# Generated at 2022-06-13 23:30:43.571978
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils."""
    seed = "5f5e5d5c5b5a595857565554535251504f4e4d4c4b4a494847464544434241403f3e3d3c3b3a393837363534333231302f2e2d2c2b2a292827262524232221201f1e1d1c1b1a191817161514131211100f0e0d0c0b0a09080706050403020100"
    rsp = RussiaSpecProvider(seed)
    snils_expected = "41917492600"
    snils_generated = rsp.snils()
    assert snils_expected == snils_generated

# Generated at 2022-06-13 23:31:23.012951
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    sp = RussiaSpecProvider()
    snils = sp.snils()
    assert type(snils) == str
    assert len(snils) == 11
    print(snils)


# Generated at 2022-06-13 23:31:28.661666
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method `RussiaSpecProvider.snils`."""
    from mimesis.providers import RussiaSpecProvider

    r = RussiaSpecProvider()
    snils = r.snils()
    assert isinstance(snils, str)
    assert len(snils) == 11



# Generated at 2022-06-13 23:31:31.937499
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert len(result) == 11
    assert result.isnumeric()


# Generated at 2022-06-13 23:31:36.963938
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person.enums import Gender
    provider = RussiaSpecProvider()
    assert provider.snils()
    assert provider.snils(gender=Gender.MALE)
    assert provider.snils(gender=Gender.FEMALE)


# Generated at 2022-06-13 23:31:42.759022
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test method snils of class RussiaSpecProvider."""
    import random
    import re
    snils_provider = RussiaSpecProvider(random.randint(0, 100))
    snils = snils_provider.snils()
    assert re.match(r'\d{9}', snils)


# Generated at 2022-06-13 23:31:46.477931
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert len(result) == 11
    assert result.count('9') == 3


# Generated at 2022-06-13 23:31:50.128055
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rs = RussiaSpecProvider()
    for _ in range(1000):
        snils = rs.snils()
        assert(len(snils) == 11)
        assert(snils != '00000000000')


# Generated at 2022-06-13 23:32:01.153346
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Проверка сгенерированных снилсов на корректность в тестовом модуле
    # из библиотеки python-snils версии 1.0.3.1
    from snils import is_valid
    import pytest

    def check_snils():
        test_snils = s.snils()
        assert is_valid(test_snils) == True

    s = RussiaSpecProvider()
    check_snils()
    s = RussiaSpecProvider(seed=1)
    check_snils()

# Generated at 2022-06-13 23:32:02.390906
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
  provider = RussiaSpecProvider()
  data = provider.snils()
  assert len(data) == 11


# Generated at 2022-06-13 23:32:03.996655
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert (len(RussiaSpecProvider().snils()) == 11)


# Generated at 2022-06-13 23:33:31.924771
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    assert ru.snils() == ru.snils()



# Generated at 2022-06-13 23:33:34.935628
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == '41917492600'


# Generated at 2022-06-13 23:33:44.342817
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider
    rsp = RussiaSpecProvider()
    for _ in range(0, 200):
        snils = rsp.snils()
        if snils.endswith('00'):
            print('{}: {} is correct'.format('snils', snils))
        else:
            numbers = []
            control_codes = []
            for i in range(0, 9):
                numbers.append(int(snils[i]))
            for i in range(9, 0, -1):
                control_codes.append(numbers[9 - i] * i)
            control_code = sum(control_codes)
            if (control_code % 101) == int(snils[9:11]):
                print('{}: {} is correct'.format('snils', snils))


# Generated at 2022-06-13 23:33:47.306348
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a = RussiaSpecProvider()
    b = a.snils()
    # print(b)
    assert b


# Generated at 2022-06-13 23:33:50.629343
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
	provider = RussiaSpecProvider()
	snils_str=provider.snils()
	snils=int(snils_str)
	assert snils < 10000000000


# Generated at 2022-06-13 23:33:55.092689
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    with open('snils.txt', 'r') as f:
        for number in f:
            assert provider.snils() == number.replace('\n', '')

# Generated at 2022-06-13 23:33:58.332808
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Test args
    provider = RussiaSpecProvider()
    # Test method
    snils = provider.snils()
    assert isinstance(snils, str)

# Generated at 2022-06-13 23:34:01.859518
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider

    snils = RussiaSpecProvider()

    for i in range(0, 10):
        result = snils.snils()
        print("snils", result)
        assert len(result) == 11



# Generated at 2022-06-13 23:34:02.783391
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    print(RussiaSpecProvider.snils())


# Generated at 2022-06-13 23:34:04.862410
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider('seed').snils() == '41917492600'


# Generated at 2022-06-13 23:38:06.734348
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person import Person
    from mimesis.enums import Gender

    rus_provider = RussiaSpecProvider()
    rus_person = Person('ru')
    rus_person.seed(3)
    snils = rus_provider.snils()
    print(snils)

    # Test the length of SNILS
    assert len(snils) == 11

    # Test the random generation of SNILS
    snils2 = rus_provider.snils()
    assert snils != snils2

    # Test the reproducibility of data generation
    snils2 = rus_provider.snils()
    assert snils == snils2

    # Test the generation of a SNILS with a set gender

# Generated at 2022-06-13 23:38:16.602291
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils_provider = RussiaSpecProvider()

    for index in range(1, 11):
        snils = snils_provider.snils()
        snils_int = int(snils)
        snils_arr = [snils_int // 100000000 % 10 ** 9, snils_int // 10 ** 9 % 10 ** 8, snils_int // 10 ** 8 % 10 ** 7, snils_int // 10 ** 7 % 10 ** 6, snils_int // 10 ** 6 % 10 ** 5, snils_int // 10 ** 5 % 10 ** 4, snils_int // 10 ** 4 % 10 ** 3, snils_int // 10 ** 3 % 10 ** 2, snils_int // 10 ** 2 % 10 ** 1]

# Generated at 2022-06-13 23:38:18.154741
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == '41917492600'

# Generated at 2022-06-13 23:38:22.400549
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    data = []
    for ind in range(0, 10):
        data.append(provider.snils())
    assert len(data) == 10
    assert len(data[0]) == 11

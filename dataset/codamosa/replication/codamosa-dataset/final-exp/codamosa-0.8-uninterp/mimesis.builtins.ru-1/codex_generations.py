

# Generated at 2022-06-13 23:28:38.631489
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Tests for method snils of class RussiaSpecProvider"""
    # TODO: write unit tests
    pass


# Generated at 2022-06-13 23:28:44.300511
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # INITIALIZATION
    RussiaSpecProvider_data = RussiaSpecProvider()
    # TEST
    RussiaSpecProvider_data_snils = RussiaSpecProvider_data.snils()
    assert RussiaSpecProvider_data_snils != None
    assert type(RussiaSpecProvider_data_snils) == str
    assert len(RussiaSpecProvider_data_snils) == 11



# Generated at 2022-06-13 23:28:47.064140
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    print(snils)
    assert snils == "41917492600"


# Generated at 2022-06-13 23:28:48.875754
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'

# Generated at 2022-06-13 23:28:51.619095
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for snils method of class RussiaSpecProvider."""
    rsp = RussiaSpecProvider()
    assert len(str(rsp.snils())) == 11

# Generated at 2022-06-13 23:28:53.635684
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600', 'AssertionError: test_RussiaSpecProvider_snils'

# Generated at 2022-06-13 23:28:55.252391
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russia = RussiaSpecProvider()
    assert russia.snils() != '41917492600'

# Generated at 2022-06-13 23:29:05.671587
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person import Person
    from mimesis.providers.date import DateTime
    ru_provider = RussiaSpecProvider()
    ru_person = Person('ru')
    ru_date = DateTime('ru')
    actual_snils = ru_provider.snils()
    actual_date = ru_date.date(start=1940, end=2003, fmt='%Y-%m-%d').split('-')
    year = actual_date[0]
    month = actual_date[1]
    day = actual_date[2]
    actual_male_name = ru_person.full_name(gender=Gender.MALE)
    actual_female_name = ru_person.full_name(gender=Gender.FEMALE)
    actual_female_patronymic = ru_

# Generated at 2022-06-13 23:29:06.478745
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11
    assert provider.snils() != 0

# Generated at 2022-06-13 23:29:16.211312
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    def control_sum(nums: list, t: str) -> int:
        digits_dict = {
            'n2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        }
        number = 0
        digits = digits_dict[t]

        for i, _ in enumerate(digits, start=0):
            number += nums[i] * digits[i]
        return number % 11 % 10

    def snils_check(number: str) -> bool:
        if len(number) != 11:
            return False

        if not number.isdigit():
            return False

        num = [int(x) for x in list(number)]
       

# Generated at 2022-06-13 23:29:35.513910
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider(seed='1')
    assert r.snils() == '41917492600'


# Generated at 2022-06-13 23:29:39.486562
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person.ru import RussiaSpecProvider
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11


# Generated at 2022-06-13 23:29:42.767816
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russian_provider = RussiaSpecProvider(seed=42)
    snils = russian_provider.snils()
    assert snils == '43882414600'

# Generated at 2022-06-13 23:29:46.552731
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    snils = r.snils()
    assert len(snils) == 11
    assert snils in ['41917492600', '41835718993']

# Generated at 2022-06-13 23:29:49.202063
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils method of RussiaSpecProvider class."""
    p = RussiaSpecProvider(seed=101)
    r = p.snils()
    assert r == '41917492600'


# Generated at 2022-06-13 23:29:59.375731
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import pytest

    @pytest.fixture(scope='session', autouse=True)
    def _init_tester():
        class Tester(RussiaSpecProvider):
            def __init__(self, seed):
                super().__init__(seed=seed)

        return Tester


# Generated at 2022-06-13 23:30:02.800356
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russia = RussiaSpecProvider()
    snils = russia.snils()
    print(snils)
    assert len(snils) == 11


# Generated at 2022-06-13 23:30:09.423549
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.providers import RussiaSpecProvider
    from mimesis.providers.helpers import calculate_control_code

    rsp = RussiaSpecProvider()

    for _ in range(0, 1000):
        snils = rsp.snils()
        m = int(snils[-2:])
        n = int(snils[:-2])
        assert m == calculate_control_code(n)



# Generated at 2022-06-13 23:30:13.411720
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()

    for _ in range(0, 100):
        with r.snils() as s:
            s = int(s)
            assert len(str(s)) == 11
            assert s != 0
            assert s >= 1001998 and s <= 88888888888

# Generated at 2022-06-13 23:30:19.729503
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    seed = "TestSeed"
    # test for seed = "TestSeed"
    result = "41917492600"
    assert(RussiaSpecProvider(seed).snils() == result)

    # test for seed = "TestSeed2"
    result = "89869233021"
    assert(RussiaSpecProvider("TestSeed2").snils() == result)



# Generated at 2022-06-13 23:30:57.675836
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert provider.snils() == provider.snils()


# Generated at 2022-06-13 23:30:58.800581
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'

# Generated at 2022-06-13 23:31:03.103194
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test_value = RussiaSpecProvider().snils()
    assert len(test_value) == 11
    assert(test_value[-2:].isdecimal())
    assert(test_value[:9].isdecimal())

# Generated at 2022-06-13 23:31:07.667003
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person import Person
    from mimesis.enums import Gender
    from mimesis.builtins.russia import RussiaSpecProvider

    for _ in range(10):
        p = Person('ru')
        name = p.full_name(gender=Gender.FEMALE)
        snils = RussiaSpecProvider().snils()
        print(snils)


# Generated at 2022-06-13 23:31:13.042447
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    res = r.snils()
    assert len(res) == 11
    assert res.isdigit()
    assert int(res[-2:]) == r.control_sum_snils(int(res[:-2]))


# Generated at 2022-06-13 23:31:14.320078
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    pass


# Generated at 2022-06-13 23:31:17.570613
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    ru = RussiaSpecProvider()
    t = ru.snils()
    print(t)
    assert len(str(t)) == 11

# Generated at 2022-06-13 23:31:21.110152
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    if len(snils) != 11:
        raise Exception("Wrong snils length")


# Generated at 2022-06-13 23:31:22.785805
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RSP = RussiaSpecProvider()
    assert RSP.snils() == '41917492600'


# Generated at 2022-06-13 23:31:27.444087
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    provider = RussiaSpecProvider(seed=None)
    snils_str = provider.snils()
    #print(snils_str, type(snils_str))
    assert("41917492600" != snils_str)


# Generated at 2022-06-13 23:32:52.475531
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    r = RussiaSpecProvider(seed=0)

    for i in range(0, 100):
        snils = r.snils()
        print(snils)
        numbers = []
        for i in range(0, 9):
            numbers.append(int(snils[i]))

        control_codes = []
        for i in range(9, 0, -1):
            control_codes.append(numbers[9 - i] * i)

        control_code = sum(control_codes)

        if control_code in (100, 101):
            control_code = 0
        elif control_code > 101:
            control_code = control_code % 101
            if control_code == 100:
                control_code = 0


# Generated at 2022-06-13 23:32:54.849868
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person.russia import RussiaSpecProvider
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert(len(snils) == 11)


# Generated at 2022-06-13 23:33:00.132034
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Initialization
    RussiaSpecProvider.seed(453)
    provider = RussiaSpecProvider()
    # Testing
    assert provider.snils() == '41917492600'

# Generated at 2022-06-13 23:33:05.625131
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test = RussiaSpecProvider()
    series_and_numbers = dict()
    for i in range(1, 2000):
        snils = test.snils()
        series_and_numbers[snils] = snils
    assert len(series_and_numbers) == 2000

# Generated at 2022-06-13 23:33:11.785418
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method test_RussiaSpecProvider_snils()."""
    russiaSpecProvider = RussiaSpecProvider()
    assert len(russiaSpecProvider.snils()) == 11
    assert isinstance(russiaSpecProvider.snils(), str)
    assert russiaSpecProvider.snils() == "04381524459"


# Generated at 2022-06-13 23:33:15.987039
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru_spec_provider = RussiaSpecProvider(seed = 12345)
    snils = ru_spec_provider.snils()
    assert(snils == '9877252880')


# Generated at 2022-06-13 23:33:22.595759
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    # Initialization of object
    rsp = RussiaSpecProvider()
    # Generate snils
    snils_1 = rsp.snils()
    assert snils_1 != rsp.snils()
    assert len(snils_1) == 11
    assert snils_1
    assert snils_1.isdigit()

# Generated at 2022-06-13 23:33:26.703331
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert snils != None
    assert len(snils) == 11
    assert snils.isnumeric() == True

# Generated at 2022-06-13 23:33:30.797067
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils1 = provider.snils()
    snils2 = provider.snils()
    assert snils1 != snils2



# Generated at 2022-06-13 23:33:37.495936
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import random
    import pytest
    from custom.data.providers import RussiaSpecProvider
    ru = RussiaSpecProvider(random.random)

    snils = ru.snils()

    assert len(snils) == 11
    assert isinstance(snils, str)


# Generated at 2022-06-13 23:37:22.717758
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    print(provider.snils())

# Generated at 2022-06-13 23:37:24.962772
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11

    for i in range(0, 1000):
        assert len(provider.snils()) == 11


# Generated at 2022-06-13 23:37:30.866856
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Create an instance of RussiaSpecProvider
    provider = RussiaSpecProvider(seed=None)

    # Call the method snils of class RussiaSpecProvider
    result = provider.snils()

    # Verify the result
    assert(len(result) == 11)
    assert(int(result) < 10000000000)
    assert(int(result) > 999999999)

# Generated at 2022-06-13 23:37:35.058388
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""

    for item in range(10):

        result = RussiaSpecProvider().snils()
        assert len(result) == 11
        assert result.isdigit() == True
        assert result.startswith('419') == True


if __name__ == '__main__':
    test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:37:37.882115
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for RussiaSpecProvider"""
    russ = RussiaSpecProvider()
    snils = russ.snils()
    a = False
    if snils:
        a = True
    assert a

# Generated at 2022-06-13 23:37:47.464990
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11

    # Test for checksum
    snils = snils[:9]
    control_codes = []
    for i in range(9, 0, -1):
        control_codes.append(int(snils[9 - i]) * i)

    control_code = sum(control_codes)

    if control_code < 100:
        assert control_code == int(snils[9:11])
    else:
        assert (control_code % 101) % 100 == int(snils[9:11])

# Generated at 2022-06-13 23:37:49.181368
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert len(RussiaSpecProvider().snils()) == 11



# Generated at 2022-06-13 23:37:51.304346
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russian_provider = RussiaSpecProvider()
    series = russian_provider.snils()
    assert len(series) == 11


# Generated at 2022-06-13 23:38:03.984278
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils method of Russia provider."""
    russian_provider = RussiaSpecProvider()
    result = russian_provider.snils()
    assert isinstance(result, str)
    assert len(result) == 11
    assert not result.startswith('0')
    assert not result.startswith('00')
    assert not result.endswith('00')




# Generated at 2022-06-13 23:38:05.464090
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    p = RussiaSpecProvider(seed=42)
    for i in range(10):
        print(i, p.snils())



# Generated at 2022-06-13 23:28:39.749185
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Sentence: Я программист, документы в порядке, прошу выдать визу."""
    gender = Gender.FEMALE
    result = RussiaSpecProvider(seed=0).snils()
    assert result == '41917492600'

# Generated at 2022-06-13 23:28:48.919830
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.identification import Identification

    ru = Identification('ru')
    russian_snils = ru.rus_spec.snils()
    print(russian_snils)

    # Select five random snils numbers
    random_snils = ru.rus_spec.snils()
    print(random_snils)

    random_snils = ru.rus_spec.snils()
    print(random_snils)

    random_snils = ru.rus_spec.snils()
    print(random_snils)

    random_snils = ru.rus_spec.snils()
    print(random_snils)


# Generated at 2022-06-13 23:28:55.214439
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.providers.utils import calculate_control_code
    from mimesis.typing import Seed

    seed("Hello World!")
    rup = RussiaSpecProvider("ru")
    snils = rup.snils()
    assert len(snils) == 11
    assert snils.isdigit()
    assert calculate_control_code(snils) == snils[-2:]


# Generated at 2022-06-13 23:28:56.993521
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=1234)
    x = provider.snils()
    assert x == '42917492600'

# Generated at 2022-06-13 23:29:00.680432
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert (snils=='41917492600')

# Generated at 2022-06-13 23:29:03.898138
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    if snils.isdigit():
        assert len(snils)==11
    else:
        assert False


# Generated at 2022-06-13 23:29:09.066721
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    obj = RussiaSpecProvider()
    assert len(obj.snils()) == 11
    sel_obj = RussiaSpecProvider(seed=123)
    res_1 = sel_obj.snils()
    res_2 = sel_obj.snils()
    assert res_1 == res_2


# Generated at 2022-06-13 23:29:12.884288
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider
    Checks that the generated SNILS number is correct
    """
    r = RussiaSpecProvider()
    assert r._validate_snils(r.snils())


# Generated at 2022-06-13 23:29:15.845146
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert isinstance(provider.snils(), str) == True


# Generated at 2022-06-13 23:29:27.930280
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # создаем экземпляр класса
    rus = RussiaSpecProvider()
    # генерируем случайное значение через метод snils
    test_snils = rus.snils()
    # получаем значения для проверки контрольной суммы
    numbers = [int(i) for i in test_snils[:9]]
    control_codes = []
    # генерируем

# Generated at 2022-06-13 23:29:45.601729
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == '41917492600'


# Generated at 2022-06-13 23:29:47.568356
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    number = RussiaSpecProvider.snils()
    print(number)


# Generated at 2022-06-13 23:29:53.804891
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Testing method snils of class RussiaSpecProvider for correct values."""
    rp = RussiaSpecProvider()
    snils = rp.snils()
    assert len(snils) == 11 or len(snils) == 2
    assert isinstance(snils, str) == True


# Generated at 2022-06-13 23:29:59.680876
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider
    from mimesis.enums import Gender

    check_list = []
    r = RussiaSpecProvider('en')
    for i in range(1, 10):
        check_list.append(r.snils())
    for x in check_list:
        if len(str(x)) != 11:
            raise AssertionError("Length of SNILS should be equal to 11.")


# Generated at 2022-06-13 23:30:07.825635
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for The method snils of class RussiaSpecProvider."""
    # snils is correct
    assert len(str(RussiaSpecProvider().snils())) == 11

    # snils is uncorrect
    with pytest.raises(ValueError):
        assert len(str(RussiaSpecProvider().snils())) < 11

    # snils is uncorrect
    with pytest.raises(ValueError):
        assert len(str(RussiaSpecProvider().snils())) > 11


# Generated at 2022-06-13 23:30:09.424964
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru_provider = RussiaSpecProvider()
    ru_provider.snils() == '41917492600'

# Generated at 2022-06-13 23:30:17.535952
# Unit test for method snils of class RussiaSpecProvider

# Generated at 2022-06-13 23:30:28.285195
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # YYYY-MM-DD
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person
    from mimesis.providers.russia import RussiaSpecProvider
    
    r = RussiaSpecProvider(seed = '2020-07-01')
    a = Address('ru')
    

# Generated at 2022-06-13 23:30:31.204881
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.rus_provider import RussiaSpecProvider

    assert RussiaSpecProvider('ru').snils() == '41917492600'

# Generated at 2022-06-13 23:30:36.340581
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender

    r = RussiaSpecProvider()
    for i in range(0, 50):
        assert r.snils =="41917492600"
        assert len(r.snils) == 11


# Generated at 2022-06-13 23:31:13.438984
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11

# Generated at 2022-06-13 23:31:23.086233
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rs = RussiaSpecProvider()
    # не должно падать
    # и не должно возвращать всегда один и тот же результат
    # что в примере
    x1 = rs.snils()
    x2 = rs.snils()
    print(f'{x1} {x2}')
    assert x1 != x2



# Generated at 2022-06-13 23:31:28.726787
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russ = RussiaSpecProvider()
    assert russ.snils() == "34038712300" # проверка выдачи форматированного результата

# Generated at 2022-06-13 23:31:31.463331
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=None)
    snils = provider.snils()
    assert isinstance(snils, str)


# Generated at 2022-06-13 23:31:36.488519
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test function snils."""
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert snils in provider.snils.__doc__
    assert len(snils) == 11
    assert snils.isdigit()



# Generated at 2022-06-13 23:31:40.294266
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test that method generates the correct snils."""
    rus = RussiaSpecProvider()
    assert rus.snils() == '14255646582'

# Generated at 2022-06-13 23:31:42.605646
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russiaspecprovider = RussiaSpecProvider()
    snils = russiaspecprovider.snils()
    assert len(snils) == 11
    assert ' ' not in snils

# Generated at 2022-06-13 23:31:55.712083
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit-test for RussiaSpecProvider.snils()."""
    rus = RussiaSpecProvider()
    # create SNILS and seperate it into 3 parts for testing
    snils_test = rus.snils()
    snils_part1 = snils_test[0:3]
    snils_part2 = snils_test[3:6]
    snils_part3 = snils_test[6:9]
    # check if SNILS doesn't have zeroes in its first part
    assert len(snils_part1) == 3
    assert snils_part1[0] != '0'
    # check if SNILS doesn't have zero's in its second part
    assert len(snils_part2) == 3
    assert snils_part2[0] != '0'
    # check if SNILS

# Generated at 2022-06-13 23:31:58.105912
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert r.snils() == '41917492600'


# Generated at 2022-06-13 23:32:01.890062
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Test for method snils of class RussiaSpecProvider
    """

    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert(snils.find("00") == -1)

# Generated at 2022-06-13 23:33:32.147274
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    snils1 = provider.snils()
    snils2 = provider.snils()
    assert snils1 != snils2
    assert len(snils1) == 11
    assert len(snils2) == 11


# Generated at 2022-06-13 23:33:36.403499
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import timeit
    print(timeit.timeit('RussiaSpecProvider().snils()', number=1000, globals=globals()))


# Generated at 2022-06-13 23:33:42.041691
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    assert len(snils) == 11
    assert int(snils) % 111 % 101 != 0

# unit test for method inn of class RussiaSpecProvider

# Generated at 2022-06-13 23:33:46.452497
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    _ob = RussiaSpecProvider(seed=0)
    for _ in range(10):
        print(_ob.snils())

if __name__ == '__main__':
    test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:33:52.752194
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider
    
    rs = RussiaSpecProvider()

    for i in range(0, 10):
        assert rs.snils() == rs.snils()
    try : 
        assert rs.snils() == rs.snils()
    except AssertionError:
        return True
    # False case
    return False


# Generated at 2022-06-13 23:33:55.972757
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    instance = RussiaSpecProvider()
    snils = instance.snils()
    print(snils)
    assert len(snils) == 11


# Generated at 2022-06-13 23:33:59.282974
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    num = provider.snils()
    assert isinstance(num, str)
    assert len(num) == 11


# Generated at 2022-06-13 23:34:04.009231
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider
    rus = RussiaSpecProvider()
    snils = rus.snils()
    if (snils == "41917492600") : #snils if it's not change
        print("Unit test passed\n")
        return True
    else:
        print("Unit test failed\n")
        return False

#Unit test for method patronymic of class RussiaSpecProvider

# Generated at 2022-06-13 23:34:16.456606
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    r = RussiaSpecProvider('ru')
    snils = r.snils()
    print(snils)

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

    numbers = [int(char) for char in list(str(snils))[:9]]

# Generated at 2022-06-13 23:34:24.802220
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""

    provider = RussiaSpecProvider()

    for _ in range(100):
        snils = provider.snils()
        data = snils.split('.')
        number = data[0]

        numbers = []
        for i in number:
            numbers.append(int(i))

        sum = 0
        for i in range(9, 0, -1):
            sum += numbers[9 - i] * i

        if sum % 101 % 100 == int(data[1]):
            assert True
        else:
            assert False

# Generated at 2022-06-13 23:38:12.148443
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11


# Generated at 2022-06-13 23:38:15.786853
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test_provider = RussiaSpecProvider()
    res = test_provider.snils()
    if not res:
        raise Exception("snils not generate")
    if not isinstance(res, str):
        raise Exception("snils return not str")


# Generated at 2022-06-13 23:38:17.372767
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    assert ru.snils()[-2:] != '00'



# Generated at 2022-06-13 23:38:19.645181
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Запускает метод snils класса RussiaSpecProvider
    """
    print(RussiaSpecProvider().snils())


# Generated at 2022-06-13 23:38:22.507541
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Checking snils method of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    assert 9 == len(provider.snils())


# Generated at 2022-06-13 23:38:24.765520
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider_test = RussiaSpecProvider()
    assert provider_test.snils() == "71901485400"
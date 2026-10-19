

# Generated at 2022-06-13 23:28:39.783469
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider"""
    assert RussiaSpecProvider().snils() == '41917492600'

# Generated at 2022-06-13 23:28:42.801610
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider
    spec = RussiaSpecProvider(seed=5)
    res = spec.snils()
    assert res == '42968231800'


# Generated at 2022-06-13 23:28:44.589221
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    print(snils)
    assert(len(snils) == 11 and snils.isdigit())

# Generated at 2022-06-13 23:28:46.562628
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=123)
    assert provider.snils() == '418749264'

# Generated at 2022-06-13 23:28:48.000973
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    p = RussiaSpecProvider()
    print(p.snils())

# Generated at 2022-06-13 23:28:55.962446
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Модуль тестирования метода snils класса RussiaSpecProvider
    # Выборка данных для теста
    data_test = [
        '40516378844',
        '15092458356',
        '44817456591',
        '00164847863',
        '21757084223',
        '32613646272',
        '08297874980',
        '27474695567',
        '41894399342',
        '73330367035',
    ]
    for snils in data_test:
        assert RussiaSpecProvider(seed=snils).snils() == snils

# Generated at 2022-06-13 23:28:57.748664
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    print(rsp.snils())
    #assert rsp.snils()


# Generated at 2022-06-13 23:28:59.689319
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    seed = 12
    random.seed(seed)
    cls = RussiaSpecProvider(seed=seed)
    assert cls.snils() == '41917492600'

# Generated at 2022-06-13 23:29:02.936525
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russia = RussiaSpecProvider()
    assert isinstance(russia.snils(), str)
    assert len(russia.snils()) == 11


# Generated at 2022-06-13 23:29:03.898057
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test."""
    pass

# Generated at 2022-06-13 23:29:29.445190
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    # check 1
    result = provider.snils()
    assert len(result) == 11
    # check 2
    result = provider.snils()
    assert len(result) == 11
    # check 3
    result = provider.snils()
    assert len(result) == 11
    # check 4
    result = provider.snils()
    assert len(result) == 11
    # check 5
    result = provider.snils()
    assert len(result) == 11
    # check 6
    result = provider.snils()
    assert len(result) == 11
    # check 7
    result = provider.snils()
    assert len(result) == 11
    # check 8
    result = provider.snils()
    assert len(result) == 11
    # check 9
    result

# Generated at 2022-06-13 23:29:43.684980
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    def assert_snils():
        r_gen = RussiaSpecProvider()
        generated_snils = r_gen.snils()
        generated_snils_int = int(generated_snils)
        prev_generated_snils_int = generated_snils_int
        for i in range(0, 9999):
            generated_snils = r_gen.snils()
            generated_snils_int = int(generated_snils)
            assert prev_generated_snils_int != generated_snils_int
            prev_generated_snils_int = generated_snils_int

    def assert_snils_with_seed(seed):
        r_gen = RussiaSpecProvider(seed=seed)
        generated_snils = r_gen.snils()
        generated_snils_int = int(generated_snils)

# Generated at 2022-06-13 23:29:46.595395
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    rsp = RussiaSpecProvider()
    print(rsp.snils())



# Generated at 2022-06-13 23:29:48.594091
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru_sp = RussiaSpecProvider()
    assert ru_sp.snils() != ru_sp.snils()



# Generated at 2022-06-13 23:29:56.148623
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider().snils()

    snils_list = list(snils)
    snils_list.pop(-1)
    nums = [int(d) for d in snils_list]

    control_codes = []

    for i in range(9, 0, -1):
        control_codes.append(nums[9 - i] * i)

    control_code = sum(control_codes)
    if control_code % 101 == int(snils[-2:]):
        return True
    return False


# Generated at 2022-06-13 23:30:01.731185
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    rsp = RussiaSpecProvider()

    assert len(rsp.snils()) == 11
    assert rsp.snils().isdigit()


# Generated at 2022-06-13 23:30:13.080586
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    # Проверка на корректность генерации СНИЛС
    snils = provider.snils()
    snils = list(map(int, snils))
    # Вычисление контрольной суммы
    control_codes = []
    for i in range(9, 0, -1):
        control_codes.append(snils[9 - i] * i)
    control_code = sum(control_codes)
    # Проверка на корректность

# Generated at 2022-06-13 23:30:25.302196
# Unit test for method snils of class RussiaSpecProvider

# Generated at 2022-06-13 23:30:27.631235
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    snils = RussiaSpecProvider(seed = '7').snils()
    assert snils == "39817862300"

# Generated at 2022-06-13 23:30:29.740703
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russia = RussiaSpecProvider()
    # Test
    assert len(russia.snils()) == 11
    assert isinstance(russia.snils(), str)

# Generated at 2022-06-13 23:31:06.674796
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method ``snils()`` of class ``RussiaSpecProvider``."""
    # Create instance of class
    spec_provider = RussiaSpecProvider()

    # Check type of result
    assert isinstance(spec_provider.snils(), str)

# Generated at 2022-06-13 23:31:09.406774
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils."""
    rssp = RussiaSpecProvider()
    assert rssp.snils() == '41917492600'

# Generated at 2022-06-13 23:31:22.721653
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""

# Generated at 2022-06-13 23:31:36.317061
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider()
    snils_list = []
    for i in range(100):
        snils_list.append(int(ru.snils()))


# Generated at 2022-06-13 23:31:38.979424
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    assert len(rsp.snils()) == 11

# Generated at 2022-06-13 23:31:44.924363
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import os
    import csv
    d = os.getcwd() + '/tests/data/data.csv'

    with open(d, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        dataset = [dict(row) for row in reader]

    for x in dataset:
        assert RussiaSpecProvider(seed=x['snils']).snils() == x['snils']

# Generated at 2022-06-13 23:31:49.232958
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
  class O:
    pass
  
  setattr(O, 'random', random.Random())
  assert(RussiaSpecProvider.snils(O) != '')



#  Unit test for method bic of class RussiaSpecProvider

# Generated at 2022-06-13 23:31:54.594247
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    ru = RussiaSpecProvider(seed=12345)
    snils_1 = ru.snils()
    snils_2 = ru.snils()
    assert snils_1 == '41917492600'
    assert snils_2 == '41917492600'


# Generated at 2022-06-13 23:32:03.462490
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Test for:
    #     41917492600
    #     48350979524
    #     14188231381
    #     52766378841
    #     91086589171
    #     61461956286
    #     88989860951
    #     04722395211
    #     51383601218
    #     51585110615
    assert RussiaSpecProvider(seed=12345).snils() == "41917492600"
    assert RussiaSpecProvider(seed=123456).snils() == "48350979524"
    assert RussiaSpecProvider(seed=1234567).snils() == "14188231381"
    assert RussiaSpecProvider(seed=12345678).snils() == "52766378841"

# Generated at 2022-06-13 23:32:05.083092
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    print(r.snils())


# Generated at 2022-06-13 23:33:33.171031
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    a = RussiaSpecProvider()
    print(a.snils())
    print(a.inn())
    print(a.ogrn())

test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:33:36.818617
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # code of the unit test
    p = RussiaSpecProvider()
    for _ in range(1000):
        print(p.snils())

# Generated at 2022-06-13 23:33:39.868386
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    pr = RussiaSpecProvider()
    assert str(pr.snils()).count('41917492600') == 1

# Generated at 2022-06-13 23:33:41.117466
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    print (rsp.snils())

# Generated at 2022-06-13 23:33:53.538773
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test the snils generation method"""
    r = RussiaSpecProvider()
    result = r.snils()
    assert len(result) == 11
    assert result.isdigit()
    assert result != '12345678900'
    assert result != '12345678910'
    assert result != '12345678911'
    assert result != '12345678912'
    assert result != '12345678913'
    assert result != '12345678914'
    assert result != '12345678915'
    assert result != '12345678916'
    assert result != '12345678917'
    assert result != '12345678918'
    assert result != '12345678919'
    assert result != '12345678920'

# Generated at 2022-06-13 23:33:58.941099
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Test for method snils of class RussiaSpecProvider
    The function to test the method snils of class RussiaSpecProvider
    """
    provider = RussiaSpecProvider()
    assert type(provider.snils()) == str



# Generated at 2022-06-13 23:34:00.688839
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    print(rsp.snils())



# Generated at 2022-06-13 23:34:05.641959
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.providers import RussiaSpecProvider

    provider = RussiaSpecProvider()
    assert len(str(provider.snils())) == 11

    number_of_tests = 100

    for _ in range(number_of_tests):
        control_codes = []
        numbers = []
        snils = provider.snils()

        for i in range(0, 9):
            numbers.append(int(snils[i]))

        for i in range(9, 0, -1):
            control_codes.append(numbers[9 - i] * i)

        control_code = sum(control_codes)
        assert snils[9:11] == '00' or control_code % 101 == int(snils[9:11])


# Generated at 2022-06-13 23:34:09.813421
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:34:10.855553
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    pass



# Generated at 2022-06-13 23:38:03.984328
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    ru = RussiaSpecProvider()
    snils = ru.snils()
    assert len(snils) == 11
    assert snils[9:] == str(int(snils) % 101 % 100)
    assert snils[:9] != str(int(snils[9:])).zfill(9)


# Generated at 2022-06-13 23:38:06.968692
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    test_obj = RussiaSpecProvider()
    test_seed = '9db2e7bb-5c5d-5739-80d5-8eec9ce38f1b'
    test_obj.seed(test_seed)
    assert test_obj.snils() == '12444444785'


# Generated at 2022-06-13 23:38:10.829764
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert len(result) == 11 # Небольшой тест для метода snils(self)


# Generated at 2022-06-13 23:38:14.605853
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit tests for method snils of class RussiaSpecProvider."""
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    assert (type(snils) == str) and snils.isalnum() and len(snils) == 11


# Generated at 2022-06-13 23:38:16.559635
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils"""
    rsp = RussiaSpecProvider()
    assert rsp.snils() == '41917492600'

# Generated at 2022-06-13 23:38:19.273991
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    def print_snils(s):
        print(s)

    provider = RussiaSpecProvider()
    for _ in range(0, 10):
        print_snils(provider.snils())


test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:38:25.915700
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider(seed=666) # Initialize
    print(rsp.inn()) # Check if the method works
    print(rsp.ogrn()) # Check if the method works
    print(rsp.bic()) # Check if the method works
    print(rsp.kpp()) # Check if the method works
    assert True # It does

# Run test_RussiaSpecProvider_snils
test_RussiaSpecProvider_snils()
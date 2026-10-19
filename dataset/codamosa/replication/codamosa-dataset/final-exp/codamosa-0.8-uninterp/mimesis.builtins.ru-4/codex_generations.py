

# Generated at 2022-06-13 23:28:34.911238
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import doctest
    doctest.testmod(extraglobs={"instance":RussiaSpecProvider()})

# Generated at 2022-06-13 23:28:39.155736
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.person.russia import RussiaSpecProvider  # noqa
    randomiser = RussiaSpecProvider()
    randomiser.seed(1234)
    snils_1 = randomiser.snils()
    randomiser.seed(1235)
    snils_2 = randomiser.snils()
    assert (snils_1 == snils_2)
# end test_RussiaSpecProvider_snils


# Generated at 2022-06-13 23:28:41.055233
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert provider.snils() == '41917492600'

# Generated at 2022-06-13 23:28:51.318099
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Тест создаёт экземпляр класса RussiaSpecProvider для дальнейшего генератора случайных значений в виде СНИЛС
    rs = RussiaSpecProvider()
    # Тест создаёт переменную snils, в которую записывает первые 9 случайных чис

# Generated at 2022-06-13 23:28:53.465202
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    result = r.snils()
    assert len(result) == 11
    assert result.isdigit()



# Generated at 2022-06-13 23:28:55.159209
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    result = RussiaSpecProvider().snils()
    assert (len(result) == 11 and result.isnumeric())


# Generated at 2022-06-13 23:28:56.644886
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    assert(len(rsp.snils()) == 11)


# Generated at 2022-06-13 23:29:03.111441
# Unit test for method snils of class RussiaSpecProvider

# Generated at 2022-06-13 23:29:06.639843
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    spec = RussiaSpecProvider()
    result = spec.snils()
    assert result == '41917492600'
    assert result.isdecimal() is True


# Generated at 2022-06-13 23:29:07.928063
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    snils = r.snils()
    assert snils is not None, "Method snils does not work correctly"


# Generated at 2022-06-13 23:29:29.490672
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils() of class RussiaSpecProvider:

    Check the method returns a string of 9 digits
    """

    ru = RussiaSpecProvider()
    snils = ru.snils()

    assert snils.isdigit()
    assert len(snils) == 9



# Generated at 2022-06-13 23:29:32.199174
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Method that tests function who generates SNILS"""
    russiaprovider = RussiaSpecProvider(0)
    snils = russiaprovider.snils()
    assert len(snils) == 11, 'Error in method snils, not len(snils) == 11'


# Generated at 2022-06-13 23:29:45.206049
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

    def get_nums(snils: str) -> list:
        return [int(x) for x in snils]

    snils = RussiaSpecProvider().snils()
    n1 = get_nums(snils)[-2]
    n

# Generated at 2022-06-13 23:29:48.283934
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    local_test_RussiaSpecProvider = RussiaSpecProvider()
    assert len(local_test_RussiaSpecProvider.snils()) == 11


# Generated at 2022-06-13 23:29:52.801516
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils = RussiaSpecProvider().snils()
    assert len(snils) == 11, 'Result must be 11 digits!'
    assert snils.isdigit(), 'Result must be only digits!'


# Generated at 2022-06-13 23:29:57.058441
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider"""
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11  # SNILS is 11 digits
    assert (snils != None)  # result is not None



# Generated at 2022-06-13 23:29:59.962017
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """."""
    ru = RussiaSpecProvider()
    assert ru.snils() == '41917492600'

# Generated at 2022-06-13 23:30:04.945767
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    def test_RussiaSpecProvider_snils():
        provider = RussiaSpecProvider()
        for _ in range(10):
            res = provider.snils()
            assert len(res) == 11, 'Size of SNILS is valid'

# Generated at 2022-06-13 23:30:07.720859
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rs = RussiaSpecProvider()

    assert len(rs.snils()) == 11
    assert type(rs.snils()) is str



# Generated at 2022-06-13 23:30:11.447538
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    #default - no params
    a = int(rsp.snils())
    print(a)
    #assert snils > 1000000 and snils < 9999999
    assert 1000000 <= a and a <= 9999999

# Generated at 2022-06-13 23:30:48.729555
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Initialize class
    rus = RussiaSpecProvider()

    # Call method
    result = rus.snils()

    # Test
    assert len(result) == 11


# Generated at 2022-06-13 23:30:50.590268
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rpc = RussiaSpecProvider()
    assert len(rpc.snils()) == 11


# Generated at 2022-06-13 23:30:53.714649
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.rus.rus import RussiaSpecProvider
    provider = RussiaSpecProvider()
    snils = provider.snils()
    print(snils)


# Generated at 2022-06-13 23:31:01.795173
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    q = RussiaSpecProvider()
    for i in range(0, 100):
        num = q.snils()
        snils_list = list(str(num))
        snils_list.pop(9)
        snils_list.pop(9)
        snils_list1 = [int(i) for i in snils_list]
        snils_list1.reverse()
        n1_sum = 0
        n2_sum = 0

        for j in range(0, 9):
            n1_sum += snils_list1[j] * (j + 1)
            n2_sum += snils_list1[j] * (9 - j)

        if n1_sum % 101 == 100:
            n1_sum = 0

        if n2_sum % 101 == 100:
            n2_

# Generated at 2022-06-13 23:31:06.419416
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """ Unit test for method snils of class RussiaSpecProvider
        The test is passed if the calculated snils is equal to the expected one
    """
    seed = 'tests'
    rsp = RussiaSpecProvider(seed)
    snils = rsp.snils()
    assert snils == '94526796900'


# Generated at 2022-06-13 23:31:08.108343
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RussiaSpecProvider().snils()
    '41917492600'


# Generated at 2022-06-13 23:31:12.445280
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Initialize object
    r = RussiaSpecProvider()

    # Get snils
    snils = r.snils()

    # Asserting
    assert len(snils) == 11


# Generated at 2022-06-13 23:31:14.257888
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '41917492600'


# Generated at 2022-06-13 23:31:24.318452
# Unit test for method snils of class RussiaSpecProvider

# Generated at 2022-06-13 23:31:27.905851
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test = RussiaSpecProvider()
    test.seed(0)
    sn = test.snils()
    assert sn == '41917492600'


# Generated at 2022-06-13 23:32:44.889132
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for RussiaSpecProvider."""
    rus = RussiaSpecProvider()
    assert isinstance(rus.snils(), str)



# Generated at 2022-06-13 23:32:48.057318
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider"""
    assert RussiaSpecProvider().snils() is not None



# Generated at 2022-06-13 23:32:50.631042
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert snils('41917492600') is True
    assert snils('41917492601') is False

# Generated at 2022-06-13 23:32:53.787411
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11 and int(snils)


# Generated at 2022-06-13 23:32:59.720632
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()

    assert type(snils) is str
    assert re.match(r'\d{11}', snils) is not None


# Generated at 2022-06-13 23:33:01.006020
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert len(RussiaSpecProvider().snils()) == 11


# Generated at 2022-06-13 23:33:11.468293
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    snils_obj = RussiaSpecProvider(seed=123456789)
    snils_obj.random.seed(123456789)
    assert [snils_obj.snils() for i in range(0,10)] == [
        '41917492600', '13913808389', '56424352227', '40994744334', '83028832477',
        '50500236214', '81578602443', '27447603090', '93375246042', '86907739791'
    ]

# Generated at 2022-06-13 23:33:23.476964
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    print('=====Unit test for RussiaSpecProvider.snils()=====')
    rp = RussiaSpecProvider()
    rp.seed(10)
    print('Should be 98177528600:', rp.snils())
    rp.seed(10)
    print('Should be 98177528600:', rp.snils())
    rp.seed(50)
    print('Should be 84042753700:', rp.snils())
    rp.seed(99999)
    print('Should be 00091868600:', rp.snils())
    rp.seed(99999)
    print('Should be 00091868600:', rp.snils())
    print('Unit test passed!')
    print(' ')


# Generated at 2022-06-13 23:33:27.243716
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for RussiaSpecProvider.snils()."""
    rsp = RussiaSpecProvider()
    snils1 = rsp.snils()
    snils2 = rsp.snils()
    assert snils1 != snils2


# Generated at 2022-06-13 23:33:28.797962
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    oid = RussiaSpecProvider()
    snils = oid.snils()
    assert len(snils) == 11

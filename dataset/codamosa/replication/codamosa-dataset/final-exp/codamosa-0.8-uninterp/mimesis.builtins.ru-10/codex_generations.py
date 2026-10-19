

# Generated at 2022-06-13 23:28:33.954249
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    d = RussiaSpecProvider()
    assert len(d.snils()) == 11

# Generated at 2022-06-13 23:28:34.985027
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RSP = RussiaSpecProvider()
    print(RSP.snils())

# Generated at 2022-06-13 23:28:40.479784
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test that returns valid and existent snils."""
    data_provider = RussiaSpecProvider()
    assert len(data_provider.snils()) == 11
    assert isinstance(data_provider.snils(), str)


# Generated at 2022-06-13 23:28:46.563020
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test snils method of RussiaSpecProvider class."""
    provider = RussiaSpecProvider()

    snils = provider.snils()
    assert snils

    # Test uniqueness
    snils_list = [provider.snils() for x in range(0, 10)]
    snils_set = set(snils_list)
    assert len(snils_set) == len(snils_list)

# Generated at 2022-06-13 23:28:55.059626
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    code = rus.snils()

    numbers = [int(code[0:1]), int(code[1:2]), int(code[2:3]), int(code[3:4]),
               int(code[4:5]), int(code[5:6]), int(code[6:7]), int(code[7:8]),
               int(code[8:9])]

    control_codes = [int(code[9:10]), int(code[10:11])]

    control_code = 0
    for i in range(0,9):
        control_code += numbers[i] * (9 - i)

    if control_code < 100:
        control_code = control_code
    elif control_code == 100:
        control_code = 0

# Generated at 2022-06-13 23:28:59.284415
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Check snils
    snils_is_str = ''
    RSP = RussiaSpecProvider()
    snils_is_str = RSP.snils()
    assert isinstance(snils_is_str, str)
    assert len(snils_is_str) == 11

    snils_is_int = int(snils_is_str)
    assert isinstance(snils_is_int, int)
    assert isinstance(snils_is_str, str)
    assert len(snils_is_str) == 11


# Generated at 2022-06-13 23:29:12.001881
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Generate snils
    gen_snils = RussiaSpecProvider().snils()
    # Last 3 digits of generated snils
    last_digits = int(gen_snils[-3:])
    # First 9 digits of generated snils
    first_digits = [int(gen_snils[i:i+1]) for i in range(0, 9)]
    # List of weights
    weights = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # Calculate sum of numbers
    check_sum = sum([first_digits[i]*weights[i] for i in range(0, 9)])
    # Last digit of the calculated sum
    check_sum_last_digit = check_sum % 101
    # Check

# Generated at 2022-06-13 23:29:15.783798
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    for _ in range(10):
        spec = RussiaSpecProvider()
        snils = spec.snils()
        print(snils)



# Generated at 2022-06-13 23:29:24.716204
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Function for unit test RussiaSpecProvider.snils(self)

    :return: test result
    """
    from mimesis.providers.person.ru import RussiaSpecProvider
    count_error = 0
    for i in range(1000):
        count_error += RussiaSpecProvider(seed=i).snils() == check_snils(RussiaSpecProvider(seed=i).snils())
    if (count_error == 1000):
        return True
    else:
        return False


# Generated at 2022-06-13 23:29:30.019068
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Unit test for method 'snils' of class 'RussiaSpecProvider'
    """
    print('\nTest for method "snils" of class "RussiaSpecProvider"')
    rsp = RussiaSpecProvider()
    for _ in range(0, 2000):
        print(rsp.snils())
        assert len(rsp.snils()) == 11


# Generated at 2022-06-13 23:29:50.567378
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert len(r.snils()) == 11


# Generated at 2022-06-13 23:29:52.664754
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    print('snils = ', snils)


# Generated at 2022-06-13 23:29:55.680806
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    test_instance = RussiaSpecProvider()
    print(test_instance.snils())


# Generated at 2022-06-13 23:30:05.911200
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    '''
    Function test snils method of RussiaSpecProvider class
    '''
    from mimesis.builtins import RussiaSpecProvider
    rsp = RussiaSpecProvider()
    snils_list = []
    for i in range(0, 5):
        snils_list.append(rsp.snils())
    if len(snils_list) == len(set(snils_list)):
        print('test_RussiaSpecProvider_snils: OK')
    else:
        print('test_RussiaSpecProvider_snils: NO')


# Generated at 2022-06-13 23:30:09.075358
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    ru = RussiaSpecProvider()
    ru.seed(130)
    assert ru.snils() == "41917492600"



# Generated at 2022-06-13 23:30:12.126833
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=314)
    snils = provider.snils()
    test_snils = provider.snils()

    assert snils == test_snils

# Generated at 2022-06-13 23:30:17.008035
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    print('Проверка корректности генерации СНИЛС')
    rp = RussiaSpecProvider()
    snils = rp.snils()
    print(snils)
    assert snils[8] == str(int(snils[0:8]) % 101 % 100 // 10)
    assert snils[9] == str(int(snils[0:8]) % 101 % 10)
        # break

# Generated at 2022-06-13 23:30:22.157593
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    print('\n' + 'Unit test for method \"snils\" of class RussiaSpecProvider:' + '\n')
    data = RussiaSpecProvider()
    for i in range(10):
        print(data.snils())


# Generated at 2022-06-13 23:30:27.828224
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rs = RussiaSpecProvider.__new__(RussiaSpecProvider)
    test_dict = {}
    for i in range(0, 10000):
        snils = rs.snils()
        if snils not in test_dict:
            test_dict[snils] = 1
        else:
            test_dict[snils] = test_dict.get(snils) + 1
    print(test_dict)

# if __name__ == "__main__":
#     test_RussiaSpecProvider_snils()

# Generated at 2022-06-13 23:30:31.018118
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    test_snils = RussiaSpecProvider()
    snils = test_snils.snils()

    if len(snils) != 11:
        raise Exception('Test Failed.')



# Generated at 2022-06-13 23:31:15.866238
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp1 = RussiaSpecProvider()
    snils = rsp1.snils()
    print(snils)
    rsp2 = RussiaSpecProvider(seed=snils)
    snils2 = rsp2.snils()
    print(snils2)
    assert snils == snils2

# Generated at 2022-06-13 23:31:22.814841
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    seed = 'test'
    russiaspecp = RussiaSpecProvider(seed)
    snils = russiaspecp.snils()
    if snils != '41917492600':
        raise AssertionError()

    russiaspecp = RussiaSpecProvider('test')
    snils = russiaspecp.snils()
    if snils != '41917492600':
        raise AssertionError()


# Generated at 2022-06-13 23:31:24.906007
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert len(r.snils()) == 11

# Generated at 2022-06-13 23:31:27.251004
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    print(snils)

# Generated at 2022-06-13 23:31:30.107763
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert len(r.snils()) == 11
    assert int(r.snils()) % 101 % 100 % 10 == 0

# Generated at 2022-06-13 23:31:36.669203
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    assert type(provider.snils()) is str
    assert len(provider.snils()) is 11
    assert ' ' not in provider.snils()
    assert int(provider.snils()) % 100 == int(provider.snils()[-2:])


# Generated at 2022-06-13 23:31:40.003806
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    result = provider.snils()
    assert len(result) == 11

# Generated at 2022-06-13 23:31:42.057071
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russiaspecprovider = RussiaSpecProvider(seed=0)
    assert russiaspecprovider.snils() == '63350726312'

# Generated at 2022-06-13 23:31:43.671771
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert provider.snils() == '41917492600'
# End of test for method snils
    

# Generated at 2022-06-13 23:31:46.906780
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider

    rus = RussiaSpecProvider()
    assert len(rus.snils()) == 11


# Generated at 2022-06-13 23:33:20.284949
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider(seed=0)
    assert r.snils() == '41917492600'

# Generated at 2022-06-13 23:33:24.642343
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.providers.numbers import Numbers
    provider = RussiaSpecProvider()
    numbers = Numbers()
    assert numbers.validate('snils', provider.snils()) == True



# Generated at 2022-06-13 23:33:27.489064
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import doctest
    doctest.testmod(RussiaSpecProvider.snils)


# Generated at 2022-06-13 23:33:30.865738
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Tests RussiaSpecProvider.snils method."""
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11
    for x in snils:
        assert (x >= '0' and x <= '9')


# Generated at 2022-06-13 23:33:43.026974
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    result = RussiaSpecProvider().snils()
    assert result != None, "Не определился результат вызова функции"
    assert isinstance(result, str), "Результат вызова функции не строка"
    assert len(result) == 11, "Результат не является 11-ти значным числом"


# Generated at 2022-06-13 23:33:46.781491
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russia = RussiaSpecProvider()
    snils = russia.snils()
    assert len(snils) == 11
    assert snils.isdigit() is True


# Generated at 2022-06-13 23:33:50.141731
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins.russia import RussiaSpecProvider
    r = RussiaSpecProvider()
    for i in range(20):
        r.snils()

# Generated at 2022-06-13 23:33:51.902209
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert len(provider.snils()) == 11

# Generated at 2022-06-13 23:33:54.536046
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for the RussiaSpecProvider.snils method."""
    provider = RussiaSpecProvider()
    assert provider.snils() == '41917492600'

# Generated at 2022-06-13 23:34:04.738999
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    class Dummy:
        pass

    dummy = Dummy()
    russia_spec_provider = RussiaSpecProvider()
    dummy.snils = russia_spec_provider.snils()
    print(dummy.snils)
    assert dummy.snils != '00000000099'
    assert dummy.snils != '12345678932'
    assert dummy.snils != '23456789012'
    assert dummy.snils != '34567890123'
    assert dummy.snils != '45678901234'
    assert dummy.snils != '56789012345'
    assert dummy.snils != '67890123456'
    assert dummy.snils != '78901234567'
    assert dummy.snils != '89012345678'
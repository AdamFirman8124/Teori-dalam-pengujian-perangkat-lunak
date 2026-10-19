

# Generated at 2022-06-13 23:28:38.492453
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """
    Unit test for method cpf of class BrazilSpecProvider

    :Example:
        001.137.297-40
    """
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14, "Length of cpf is not right"
    assert cpf[3] == '.', "3rd char of cpf is not right"
    assert cpf[7] == '.', "7th char of cpf is not right"
    assert cpf[11] == '-', "10th char of cpf is not right"


# Generated at 2022-06-13 23:28:47.951831
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()

    assert cnpj[:2] in [str(i) for i in range(0, 99)]
    assert cnpj[2:5] in [str(i).zfill(3) for i in range(0, 999)]
    assert cnpj[5:8] in [str(i).zfill(3) for i in range(0, 999)]
    assert cnpj[8:12] in [str(i).zfill(4) for i in range(0, 9999)]
    assert cnpj[12:] in [str(i) for i in range(0, 100)]

# Generated at 2022-06-13 23:28:49.519383
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '962.788.302-72'


# Generated at 2022-06-13 23:28:53.290850
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of BrazilSpecProvider."""
    cnpj_provider = BrazilSpecProvider()
    cnpj = cnpj_provider.cnpj(with_mask=False)
    assert len(cnpj) == 14


# Generated at 2022-06-13 23:28:55.575821
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Given
    provider = BrazilSpecProvider()
    # When
    cpf = provider.cpf()
    # Then
    assert len(cpf) == 14


# Generated at 2022-06-13 23:28:57.410900
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert cpf == '134.822.478-92'



# Generated at 2022-06-13 23:29:03.194033
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    test = BrazilSpecProvider()
    test.seed(1)
    assert test.cpf() == "922.927.843-70"
    assert test.cpf(with_mask=False) == "92292784370"


# Generated at 2022-06-13 23:29:05.528403
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj(False) == '36233407000140'


# Generated at 2022-06-13 23:29:08.841920
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Receiving a list of cpf
    provider = BrazilSpecProvider()
    for _ in range(5):
        assert provider.cpf() not in provider.cpf()



# Generated at 2022-06-13 23:29:10.928030
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj(True)


# Generated at 2022-06-13 23:29:28.767614
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    from mimesis.enums import Gender
    provider = BrazilSpecProvider()
    pattern = re.compile('^(?:\d{3}\.){2}\d{3}-\d{2}$')
    cpf = provider.cpf()
    assert pattern.fullmatch(cpf) is not None
    cpf = provider.cpf(with_mask=False)
    assert len(cpf) == 11
    # Test with gender
    cpf = provider.cpf(gender=Gender.FEMALE)
    assert pattern.fullmatch(cpf) is not None
    cpf = provider.cpf(gender=Gender.MALE, with_mask=False)
    assert len(cpf) == 11


# Generated at 2022-06-13 23:29:32.274621
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert len(b.cpf()) == 14


# Generated at 2022-06-13 23:29:36.927338
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    result = provider.cpf()
    assert len(result) == 14
    result2 = provider.cpf(True)
    assert len(result2) == 14
    assert result == result2


# Generated at 2022-06-13 23:29:41.406281
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test BrazilSpecProvider.cnpj."""
    brazil = BrazilSpecProvider()
    cnpj = brazil.cnpj()
    assert len(cnpj) == 18
    assert isinstance(cnpj, str)


# Generated at 2022-06-13 23:29:46.011360
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    br = BrazilSpecProvider()
    cpf = br.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:29:50.810519
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Testing BrazilSpecProvider_cpf."""
    bzp = BrazilSpecProvider()

    assert len(bzp.cpf()) == 14
    assert len(bzp.cpf(with_mask=False)) == 11

    assert bzp.cpf().startswith('000.000') is False
    assert bzp.cpf(with_mask=False).startswith('000000') is False


# Generated at 2022-06-13 23:29:53.250804
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider.
    """
    a = BrazilSpecProvider()
    c = a.cpf()
    assert len(c) == 14

# Generated at 2022-06-13 23:30:00.950765
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Get the random value and check if it is valid."""
    obj = BrazilSpecProvider()
    cnpj = obj.cnpj(with_mask=False)
    assert list(map(int, cnpj))[12] == int(cnpj[12])
    assert list(map(int, cnpj))[13] == int(cnpj[13])

# Generated at 2022-06-13 23:30:04.407609
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    a = BrazilSpecProvider()
    cpf = a.cpf(False)
    assert len(cpf) == 11


# Generated at 2022-06-13 23:30:06.038872
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider"""
    pass



# Generated at 2022-06-13 23:30:28.812060
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.internet import Internet

    cpf = BrazilSpecProvider()
    internet = Internet()

    random = cpf.random
    random.seed(0)


# Generated at 2022-06-13 23:30:32.488929
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    print(cpf)
    assert len(cpf) == 14
    assert not cpf[0].isdigit()


# Generated at 2022-06-13 23:30:41.896017
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Test with default mask
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert cnpj.count('.', 0, 1) == 0
    assert cnpj.count('/', 0, 1) == 0
    assert cnpj.count('-', 0, 1) == 0
    assert cnpj.count('.', 2, 3) == 0
    assert cnpj.count('/', 2, 3) == 0
    assert cnpj.count('-', 2, 3) == 0
    assert cnpj.count('.', 4, 5) == 0
    assert cnpj.count('/', 4, 5) == 0
    assert cnpj.count('-', 4, 5) == 0
    assert cnpj.count('/', 6, 7) == 1

# Generated at 2022-06-13 23:30:45.336889
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Method that test cpf."""
    brazil = BrazilSpecProvider(seed=123)
    assert brazil.cpf(with_mask=False) == '00074999427'



# Generated at 2022-06-13 23:30:51.325822
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider"""
    from mimesis.providers.brazil import BrazilSpecProvider
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj(with_mask=True)
    assert cnpj.count('.') == 2 and cnpj.count('-') == 1 and cnpj.count('/') ==1

# Generated at 2022-06-13 23:30:53.106240
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import Faker
    obj1 = Faker.Faker('pt_BR')
    sample_cnpj = obj1.cnpj()
    brazil = BrazilSpecProvider(seed = 907)
    cnpj = brazil.cnpj()
    assert cnpj in sample_cnpj


# Generated at 2022-06-13 23:31:01.487355
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    
    def assert_cnpj_validity(cnpj, expected_result):
        print('CNPJ: {}'.format(cnpj))
        result = cnpj[12:] == str(digit([int(i) for i in cnpj[:12]]))
        print('Result: {}'.format(result))
        print('Expected Result: {}'.format(expected_result))
        assert result == expected_result
        print()
    
    def digit(cnpj):
        cnpj = cnpj[:12]
        aux = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        new_cnpj = cnpj[:12]

# Generated at 2022-06-13 23:31:07.573290
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bprovider = BrazilSpecProvider()
    assert bprovider.cpf(False) == bprovider.cpf()[:9]
    assert bprovider.cpf(False) != bprovider.cpf()
    assert bprovider.cpf(True) == bprovider.cpf()
    assert bprovider.cpf() != bprovider.cpf()


# Generated at 2022-06-13 23:31:21.198482
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """This function tests the brazilian CPF methos cpf() of the BrazilSpecProvider class"""
    # Initialize a BrazilSpecProvider instance
    brazilSpecProvider = BrazilSpecProvider()
    
    # Get a random CPF
    cpf = brazilSpecProvider.cpf()
    
    # Get a random CPF with mask
    cpfWithMask = brazilSpecProvider.cpf(True)

    # Verify if the format is correct

# Generated at 2022-06-13 23:31:34.753995
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj() in ['13.619.741/0001-50',
                                           '02.043.677/0001-98',
                                           '00.524.597/0001-15',
                                           '93.833.242/0001-85',
                                           '67.826.146/0001-08',
                                           '80.650.842/0001-51',
                                           '44.380.538/0001-31',
                                           '82.736.093/0001-31',
                                           '36.808.475/0001-60',
                                           '87.580.516/0001-59',
                                           '51.743.317/0001-07',
                                           '42.748.981/0001-17']

# Unit test

# Generated at 2022-06-13 23:32:05.368142
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil_provider import BrazilSpecProvider

    cpf = BrazilSpecProvider().cpf()
    assert type(cpf) is str
    assert len(cpf) == 14

# Generated at 2022-06-13 23:32:07.987139
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj() == '23.449.255/0001-72'


# Generated at 2022-06-13 23:32:16.025902
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """
    Validate cpf method of BrazilSpecProvider class
    """
    # Prepare data
    raw_cpf = BrazilSpecProvider().cpf(with_mask=False)
    
    # Execute method under test
    cpf = BrazilSpecProvider().cpf(with_mask=True)

    # Validate the result
    assert cpf == raw_cpf[:3] + '.' + raw_cpf[3:6] + '.' + raw_cpf[6:9] + '-' + raw_cpf[9:]


# Generated at 2022-06-13 23:32:21.036418
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    instance = BrazilSpecProvider()
    result = instance.cnpj()
    assert result is not None, ("test_BrazilSpecProvider_cnpj: "
                                "result is null")
    assert len(result) == 18, ("test_BrazilSpecProvider_cnpj: "
                               "not the size of result")


# Generated at 2022-06-13 23:32:28.505363
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import unittest
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    brazilianProvider = BrazilSpecProvider()
    cpf = brazilianProvider.cpf()
    cpf_list = cpf.split('.')
    mask_cpf = '###.###.###-##'
    mask_cpf_list = mask_cpf.split('.')
    assert len(cpf_list) == len(mask_cpf_list)
    for i in range(0, len(cpf_list)):
        assert len(cpf_list[i]) == len(mask_cpf_list[i])
    cpf = brazilianProvider.cpf(with_mask=False)
    assert brazilianProvider.regex.cpf().match(cpf) is not None


# Generated at 2022-06-13 23:32:37.103526
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print("Testing BrazilSpecProvider method cpf without mask")
    bsp = BrazilSpecProvider()
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    print(bsp.cpf(with_mask=False))
    
    

# Generated at 2022-06-13 23:32:40.767727
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert cpf != "", "BrazilSpecProvider.cpf() should not return empty string."
    assert len(cpf) == 14, "BrazilSpecProvider.cpf() should return string with 14 characters."


# Generated at 2022-06-13 23:32:42.124105
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)


# Generated at 2022-06-13 23:32:44.752679
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert len(b.cpf()) == 14


# Generated at 2022-06-13 23:32:47.916553
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    result = BrazilSpecProvider().cnpj(True)
    assert isinstance(result, str) == True
    

# Generated at 2022-06-13 23:33:54.652502
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj(True)
    print(cnpj)


# Generated at 2022-06-13 23:33:59.163446
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    test_method_result = BrazilSpecProvider().cnpj(with_mask=True)
    expected_result = "77.732.230/0001-70"
    assert test_method_result == expected_result
    return expected_result


# Generated at 2022-06-13 23:34:05.558361
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    IS_VALID_CNPJ = re.compile(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}')

    def assert_cnpj_matches_regex(cnpj, regex):
        assert bool(regex.search(cnpj)) == True, "The CNPJ %s did not match the regular expression" % cnpj

    provider = BrazilSpecProvider()

    for i in range(100):
        cnpj = provider.cnpj()
        assert_cnpj_matches_regex(cnpj, IS_VALID_CNPJ)


# Generated at 2022-06-13 23:34:10.904345
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert isinstance(cpf, str)
    assert len(cpf) == 14
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1


# Generated at 2022-06-13 23:34:16.723148
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    print(provider.cnpj(with_mask=False))
    # provider.reset_seed()
    # print(provider.cnpj(with_mask=False))
    # provider.reset_seed()
    # print(provider.cnpj(with_mask=False))
    # provider.reset_seed()
    # print(provider.cnpj(with_mask=False))

# Generated at 2022-06-13 23:34:18.971247
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test cpf method for BrazilSpecProvider class."""
    assert BrazilSpecProvider().cpf() != ''


# Generated at 2022-06-13 23:34:22.349865
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.builtins import BrazilSpecProvider
    my_BrazilSpecProvider = BrazilSpecProvider()
    for _ in range(0, 100):
        assert len(my_BrazilSpecProvider.cnpj(with_mask = False)) == 14


# Generated at 2022-06-13 23:34:27.494693
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf)==14
    assert type(cpf) == str
    provider = BrazilSpecProvider()
    cpf_without_mask = provider.cpf(with_mask=False)
    assert len(cpf_without_mask)==11
    assert type(cpf_without_mask) == str


# Generated at 2022-06-13 23:34:33.250940
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider(seed='Mimesis')
    cpf = brazil.cpf(with_mask=False)
    cpf_mask = brazil.cpf(with_mask=True)
    assert cpf == '49352305830'
    assert cpf_mask == '493.523.058-30'


# Generated at 2022-06-13 23:34:37.060687
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    spec_provider = BrazilSpecProvider()
    cpf = spec_provider.cpf(False)

    assert len(cpf) == 11


# Generated at 2022-06-13 23:37:55.120173
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert '001.137.297-40' == BrazilSpecProvider().cpf()


# Generated at 2022-06-13 23:38:03.984185
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Arrange
    provider = BrazilSpecProvider()
    is_with_mask = True
    # Act
    actual = provider.cpf(is_with_mask)
    # Assert
    assert len(actual) == 14


# Generated at 2022-06-13 23:38:07.748634
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    cpf = brazil.cpf(with_mask=False)
    print(cpf)
    assert len(cpf) == 11
    assert cpf != brazil.cpf(with_mask=False)


# Generated at 2022-06-13 23:38:10.176772
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider(Seed.random())
    assert provider.cnpj() != provider.cnpj()


# Generated at 2022-06-13 23:38:12.885987
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    assert isinstance(cnpj, str)
    assert len(cnpj) == 18
    cnpj = BrazilSpecProvider().cnpj(with_mask=False)
    assert isinstance(cnpj, str)
    assert len(cnpj) == 14


# Generated at 2022-06-13 23:38:20.907943
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis import BrazilSpecProvider
    from copy import copy
    from random import seed
    from re import compile

    sep = compile('[./\-]')
    from sys import maxsize as MAX_INT
    from sys import float_info
    from sys import int_info

    FLAG_1 = 1
    FLAG_2 = 2
    FLAG_3 = 3
    FLAG_4 = 4
    FLAG_5 = 5
    FLAG_6 = 6
    FLAG_7 = 7
    FLAG_8 = 8

    seed_gen = seed
    seed_gen(1)
    spec_provider = BrazilSpecProvider(seed=1)

    cnpj_1 = spec_provider.cnpj(with_mask=False)
    assert cnpj_1 == '7773223000197'
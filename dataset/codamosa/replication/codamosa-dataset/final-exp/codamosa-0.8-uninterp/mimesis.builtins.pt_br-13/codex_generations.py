

# Generated at 2022-06-13 23:28:34.598017
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    assert bsp.cnpj() == '77.732.230/0001-70'

# Generated at 2022-06-13 23:28:41.106410
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Test with mask
    b = BrazilSpecProvider()
    assert b.cpf(with_mask=True) == '936.264.929-00'
    # Test without mask
    b = BrazilSpecProvider()
    assert b.cpf(with_mask=False) == '93626492900'


# Generated at 2022-06-13 23:28:43.882211
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    result = BrazilSpecProvider().cpf()
    assert len(result) == 14
    assert result[:3] == '000'
    assert result[4:7] == '000'
    assert result[8:11] == '000'


# Generated at 2022-06-13 23:28:47.448556
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj."""
    bsp = BrazilSpecProvider(seed=10)
    cnpj = bsp.cnpj()
    assert cnpj == '77.732.230/0001-70'


# Generated at 2022-06-13 23:28:50.580368
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert(len(cpf) == 14)
    assert(cpf.count('.') == 2)
    assert(cpf.count('-') == 1)


# Generated at 2022-06-13 23:28:52.301973
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    print(brazil.cpf())


# Generated at 2022-06-13 23:28:55.973718
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.data import BRAZIL_PROVIDER

    cpf = BRAZIL_PROVIDER.cpf()
    assert len(cpf) == 14

    cpf = BRAZIL_PROVIDER.cpf(with_mask=False)
    assert len(cpf) == 11



# Generated at 2022-06-13 23:29:01.381894
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.person.brazil import BrazilSpecProvider
    brazil_spec = BrazilSpecProvider()
    cpf_1 = brazil_spec.cpf(False)
    cpf_2 = brazil_spec.cpf(False)
    assert cpf_1 != cpf_2


# Generated at 2022-06-13 23:29:12.995924
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.base import BaseSpecProvider
    from mimesis.builtins.brazil_provider import BrazilSpecProvider
    import math

    custom_provider = BaseSpecProvider(seed=1002)
    base_provider = BaseSpecProvider()
    br_provider = BrazilSpecProvider(seed=1002)

    assert br_provider.cpf() == '430.339.632-00'
    assert br_provider.cpf() == base_provider.cpf(seed=1002)
    assert br_provider.cpf(
        with_mask=False) == '43033963200'

    assert custom_provider.cpf() == base_provider.cpf(seed=1002)
    assert br_provider.cpf() == custom_provider.cpf()

# Generated at 2022-06-13 23:29:16.849802
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    expected = '049.974.750-53'
    assert provider.cpf() == expected


# Generated at 2022-06-13 23:29:28.871567
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_specProvider = BrazilSpecProvider()
    cpf = brazil_specProvider.cpf(with_mask=False)
    return len(cpf) == 11 and len(set(cpf)) == 11


# Generated at 2022-06-13 23:29:38.778473
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brlsp = BrazilSpecProvider()
    cnpj = brlsp.cnpj(with_mask=False)
    cnpj_without_mask = cnpj
    cnpj_with_mask = brlsp.cnpj(with_mask=True)
    assert len(cnpj_without_mask) == 14
    assert len(cnpj_with_mask) == 18
    print("CNPJ: " + cnpj_with_mask)


# Generated at 2022-06-13 23:29:43.684885
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider()
    cpf_method = cpf.cpf(False)
    assert type(cpf_method) == str
    assert len(cpf_method) == 11
    assert type(cpf.cpf(True)) == str


# Generated at 2022-06-13 23:29:52.309095
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
  from string import digits
  from mimesis.enums import Gender
  from mimesis.providers.person import Person
  from mimesis.providers.address import Address
  from mimesis.builtins import BrazilSpecProvider
  
  bsp = BrazilSpecProvider()
  #### CPF validation
  # Test 1: cpf with mask
  # Assert that this cpf is valid and each character is a digit
  for item in bsp.cpf():
    assert item.isdigit()
  
  # Test 2: cpf without mask
  # Assert that this cpf is valid and each character is a digit
  for item in bsp.cpf(False):
    assert item.isdigit()
  ####
  
  #### Rg validation
  # Test 1: rg 
  # Assert that this

# Generated at 2022-06-13 23:29:53.599344
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj()
    

# Generated at 2022-06-13 23:29:56.769218
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bt = BrazilSpecProvider()

    assert bt.cnpj(with_mask=True)
    assert bt.cnpj(with_mask=False)

# Generated at 2022-06-13 23:30:01.648136
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Initialize BrazilSpecProvider
    bsp = BrazilSpecProvider()
    # Generate a random CNPJ
    bsp.cnpj()  # 70555340000198


# Generated at 2022-06-13 23:30:05.569736
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test method cpf on class BrazilSpecProvider."""
    assert len(BrazilSpecProvider().cpf()) == 14
    assert len(BrazilSpecProvider().cpf(with_mask=False)) == 11



# Generated at 2022-06-13 23:30:11.955427
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """
    Unit test for method cpf of class BrazilSpecProvider
    """
    import mimesis
    bsp = mimesis.BrazilSpecProvider()
    cpf1 = bsp.cpf(with_mask=True)
    cpf2 = bsp.cpf(with_mask=False)
    assert len(cpf1) == 14
    assert len(cpf2) == 11
    assert cpf1 != cpf2


# Generated at 2022-06-13 23:30:18.497530
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    b.cpf()

# Generated at 2022-06-13 23:30:27.594912
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    result = provider.cpf()
    print(result)
    assert len(result) == 14


# Generated at 2022-06-13 23:30:29.327814
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    cpf = br.cpf()

    assert len(cpf) == 14


# Generated at 2022-06-13 23:30:32.300725
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider  = BrazilSpecProvider()
    assert provider.cpf() == '008.782.276-07'


# Generated at 2022-06-13 23:30:35.614598
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()

    assert cpf == '652.947.345-34'


# Generated at 2022-06-13 23:30:40.928961
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import BrazilSpecProvider
    bsp = BrazilSpecProvider()
    for _ in range(100):
        cpf = bsp.cpf()
        assert len(cpf) == 14
    for _ in range(100):
        cpf = bsp.cpf(True)
        assert len(cpf) == 14
    for _ in range(100):
        cpf = bsp.cpf(False)
        assert len(cpf) == 11


# Generated at 2022-06-13 23:30:47.687134
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins import BrazilSpecProvider
    br = BrazilSpecProvider()
    cpf_without_mask = '00113729740'
    cpf_with_mask = '001.137.297-40'
    assert br.cpf() == cpf_with_mask
    assert br.cpf(with_mask=False) == cpf_without_mask


# Generated at 2022-06-13 23:30:56.789276
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Arrange
    bsp = BrazilSpecProvider()
    cnpj_mock_with_mask = "12.345.678/9123-45"
    cnpj_mock_without_mask = "12345678912345"

    # Act
    cnpj = bsp.cnpj(with_mask=False)

    # Assert
    assert len(cnpj) == 14 and cnpj == cnpj_mock_without_mask

    # Arrange
    cnpj = bsp.cnpj(with_mask=True)

    # Assert
    assert len(cnpj) == 18 and cnpj == cnpj_mock_with_mask


# Generated at 2022-06-13 23:31:04.251034
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.finance import Finance

    p = Person('pt-br')
    finance = Finance('pt-br')

    cpf = finance.cpf(with_mask=False)
    assert len(cpf) == 11, 'Not a valid CPF'
    assert isinstance(p.cpf(with_mask=True), str), \
            'Should be a valid CPF'

# Generated at 2022-06-13 23:31:12.585369
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """This is a test function to validate if the CNPJ is valid when using
    the CNPJ generators in the BrazilSpecProvider class.
    """
    result = BrazilSpecProvider().cnpj(with_mask=False)
    if result == '7773223000170':
        print('test_BrazilSpecProvider_cnpj: Test passed!')
    else:
        print('test_BrazilSpecProvider_cnpj: Test failed!')


# Generated at 2022-06-13 23:31:19.607301
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf[12].isdigit()
    assert cpf[13].isdigit()

# Generated at 2022-06-13 23:31:37.709399
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    spec_bp = BrazilSpecProvider()
    assert spec_bp.cpf() == '052.824.759-25'
    assert isinstance(spec_bp.cpf(), str)


# Generated at 2022-06-13 23:31:42.494956
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Tests BrazilSpecProvider.cnpj() method"""
    cnpj = BrazilSpecProvider().cnpj()
    assert re.search(r'^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}$', cnpj) is not None

# Generated at 2022-06-13 23:31:48.143291
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf[-2:] != '00'


# Generated at 2022-06-13 23:31:51.181597
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """
    Unit test method BrazilSpecProvider.cpf
    """
    provider = BrazilSpecProvider()
    if len(provider.cpf()) != 14:
        print("Test with error!")
    else:
        print("Test Success!")


# Generated at 2022-06-13 23:31:59.714547
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test cnpj method of class BrazilSpecProvider."""
    bsp = BrazilSpecProvider()
    # Document with correct digit verifier
    document = bsp.cnpj(with_mask=False)
    assert len(document) == 14
    assert get_verifying_digit_cnpj(list(map(int, document[:-2])), 5) == int(document[12])
    assert get_verifying_digit_cnpj(list(map(int, document[:-1])), 6) == int(document[13])


# Generated at 2022-06-13 23:32:04.973141
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import re
    x = BrazilSpecProvider().cnpj()
    pattern = re.compile(r'([\d]{2})([\d]{3})([\d]{3})([\d]{4})([\d]{2})')
    assert re.search(pattern, x)


# Generated at 2022-06-13 23:32:17.043338
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import mimesis
    brazil = mimesis.BrazilSpecProvider()
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())
    print(brazil.cnpj())

# Generated at 2022-06-13 23:32:22.374862
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
    cpf_example = brazil_provider.cpf()
    assert(len(cpf_example) == 14)
    assert(cpf_example[3] == '.')
    assert(cpf_example[7] == '.')
    assert(cpf_example[11] == '-')
    

# Generated at 2022-06-13 23:32:24.122572
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    result = BrazilSpecProvider(seed=0).cnpj()
    assert result == "64.965.856/0001-27"


# Generated at 2022-06-13 23:32:28.504193
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
  provider = BrazilSpecProvider()

  # It is validating the generated cpf
  assert provider.cpf(with_mask=False) == provider.cpf(with_mask=False)


# Generated at 2022-06-13 23:33:15.544276
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print(BrazilSpecProvider().cpf())
    print(BrazilSpecProvider().cpf())
    print(BrazilSpecProvider().cpf())
    print(BrazilSpecProvider().cpf())
    print(BrazilSpecProvider().cpf())
    print(BrazilSpecProvider().cpf())
    

# Generated at 2022-06-13 23:33:23.260440
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b1 = BrazilSpecProvider()
    b2 = BrazilSpecProvider()

    cnpj1 = b1.cnpj()
    cnpj2 = b2.cnpj()

    cnpj_masked1 = b1.cnpj(True)
    cnpj_masked2 = b2.cnpj(True)

    print(cnpj1, cnpj2)
    print(cnpj_masked1, cnpj_masked2)



# Generated at 2022-06-13 23:33:33.299439
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    provider = BrazilSpecProvider()
    v1 = provider.cnpj()
    v2 = provider.cnpj()
    assert len(v1) == 18
    assert len(v2) == 18
    assert v1 != v2
    assert v1[0].isdigit()
    assert v1[1].isdigit()
    assert v1[2] == "."
    assert v1[3].isdigit()
    assert v1[4].isdigit()
    assert v1[5].isdigit()
    assert v1[6] == "."
    assert v1[7].isdigit()
    assert v1[8].isdigit()
    assert v1[9].isdigit()

# Generated at 2022-06-13 23:33:36.242169
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    assert type(cnpj) == str


# Generated at 2022-06-13 23:33:41.099190
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    result = provider.cnpj(with_mask = False)
    if (len(result) != 14):
        print("CNPJ must have 14 numbers without mask.")
        

# Generated at 2022-06-13 23:33:53.973529
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test for BrazilSpecProvider.cpf."""
    provider = BrazilSpecProvider()
    cpf_1 = provider.cpf(with_mask=True)
    cpf_2 = provider.cpf(with_mask=True)
    assert isinstance(cpf_1, str)
    assert isinstance(cpf_2, str)
    assert cmp(cpf_1, cpf_2) != 0

    cpf_3 = provider.cpf(with_mask=False)
    cpf_4 = provider.cpf(with_mask=False)
    assert isinstance(cpf_3, str)
    assert isinstance(cpf_4, str)
    assert cmp(cpf_3, cpf_4) != 0


# Generated at 2022-06-13 23:33:59.338170
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins.brazil import BrazilSpecProvider
    # initialise BrazilSpecProvider
    brazil_provider = BrazilSpecProvider()
    # get cpf
    brazil_provider.cpf()


# Generated at 2022-06-13 23:34:00.944066
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    p = BrazilSpecProvider()

    for _ in range(1000):
        cnpj = p.cnpj()
        print(cnpj)


# Generated at 2022-06-13 23:34:02.403547
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf(): 
    brazil = BrazilSpecProvider()
    t = brazil.cpf()
    print(t)
    assert len(t) == 14


# Generated at 2022-06-13 23:34:10.152827
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf[3] == "."
    assert cpf[7] == "."
    assert cpf[11] == "-"
    assert cpf.isnumeric() == True
    assert cpf != provider.cpf()


# Generated at 2022-06-13 23:36:00.823215
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('pt-br')
    gender = Gender.FEMALE

    # this is a valid cpf
    cpf = '578.310.507-34'
    assert cpf == person.cpf(gender=gender)

    # this is a valid cpf, with mask
    cpf_with_mask = '073.809.444-85'
    assert cpf_with_mask == person.cpf(gender=gender, with_mask=True)



# Generated at 2022-06-13 23:36:02.153806
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider.cpf(with_mask=True)


# Generated at 2022-06-13 23:36:04.784721
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:36:13.375362
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method BrazilSpecProvider.cnpj.
    """
    provider = BrazilSpecProvider(seed=0)
    """
    Runs tests for method BrazilSpecProvider.cnpj
    """
    for _ in range(1000):
        assert len(provider.cnpj()) == 14
        assert len(provider.cnpj(with_mask=False)) == 14
        assert provider.cnpj() != provider.cnpj()


# Generated at 2022-06-13 23:36:16.598341
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj(with_mask=False)
    assert (len(cnpj) == 14)

# Generated at 2022-06-13 23:36:21.005617
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    print('Test method BrazilSpecProvider.cpf')
    print(bsp.cpf())
    print(bsp.cpf(False))
    print('Test end')


# Generated at 2022-06-13 23:36:23.967020
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    return BrazilSpecProvider().cnpj()


# Generated at 2022-06-13 23:36:31.555160
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():

    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'


# Generated at 2022-06-13 23:36:40.879921
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    br = BrazilSpecProvider()
    assert br.cnpj(with_mask=True) == '77.732.230/0001-70'


# Generated at 2022-06-13 23:36:47.526772
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'
    assert cnpj[12:] == cnpj[:13:-1]
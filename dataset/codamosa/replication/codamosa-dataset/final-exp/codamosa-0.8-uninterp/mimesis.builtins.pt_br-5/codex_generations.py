

# Generated at 2022-06-13 23:28:40.908997
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from re import match
    prov = BrazilSpecProvider()
    cnpj = prov.cnpj()
    assert match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj) is not None
    cnpj = prov.cnpj(with_mask=False)
    assert match(r'\d{14}', cnpj) is not None


# Generated at 2022-06-13 23:28:49.807737
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.brazil import BrazilProvider

    for _ in range(0, 100):
        cpf_with_mask = BrazilProvider(gender=Gender.MALE).cpf()
        assert len(cpf_with_mask) == 14
        assert cpf_with_mask[3] == '.'
        assert cpf_with_mask[7] == '.'
        assert cpf_with_mask[11] == '-'

        cpf_without_mask = BrazilProvider(gender=Gender.MALE).cpf(with_mask=False)
        assert len(cpf_without_mask) == 11


# Generated at 2022-06-13 23:28:58.125226
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Instantiating a BrazilSpecProvider object
    provider_obj = BrazilSpecProvider(seed=0)
    # Retrieving a cpf with mask
    cpf = provider_obj.cpf()
    # Asserting cpf is a string
    assert isinstance(cpf, str)
    # Asserting cpf is really a cpf
    assert cpf == '230.067.458-77'
    # Retrieving a cpf without mask
    cpf = provider_obj.cpf(with_mask=False)
    # Asserting cpf is a string
    assert isinstance(cpf, str)
    # Asserting cpf is really a cpf
    assert cpf == '230.067.458-77'


# Generated at 2022-06-13 23:29:01.024359
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider(seed=0)
    value = provider.cnpj(with_mask=False)
    assert value == '10603714000173'
    value = provider.cnpj(with_mask=True)
    assert value == '10.603.714/0001-73'

# Generated at 2022-06-13 23:29:03.208991
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    test_instance = BrazilSpecProvider()
    assert type(test_instance.cpf()) == str
    assert len(test_instance.cpf()) == 14
    assert type(test_instance.cpf(False)) == str
    assert len(test_instance.cpf(False)) == 11


# Generated at 2022-06-13 23:29:05.246045
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf(with_mask=False) == "04403311240"

# Generated at 2022-06-13 23:29:08.499945
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj(with_mask=False)
    assert cnpj is not None
    assert len(cnpj) == 14

# Generated at 2022-06-13 23:29:12.489959
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Arrange
    with_mask = True
    provider = BrazilSpecProvider()

    # Act
    resultado = provider.cpf(with_mask=with_mask)

    # Assert
    assert type(resultado) == str


# Generated at 2022-06-13 23:29:18.854195
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print("Starting test for BrazilSpecProvider_cnpj")
    expected = "33.449.698/0001-36"
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj(with_mask=True)
    assert cnpj == expected
    print("Finished test for BrazilSpecProvider_cnpj")


# Generated at 2022-06-13 23:29:22.901934
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print(BrazilSpecProvider().cnpj())
    print(BrazilSpecProvider().cnpj())
    print(BrazilSpecProvider().cnpj())
    print(BrazilSpecProvider().cnpj())


# Generated at 2022-06-13 23:29:40.254072
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    '''Test BrazilSpecProvider_cnpj()'''
    brazil = BrazilSpecProvider()
    assert len(brazil.cnpj()) == 18
    assert len(brazil.cnpj(with_mask=False)) == 14


# Generated at 2022-06-13 23:29:43.988339
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print("cpf: " + BrazilSpecProvider(seed=42).cpf())
    assert BrazilSpecProvider(seed=42).cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:29:45.935887
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf(False) == '70015705747'

# Generated at 2022-06-13 23:29:49.073888
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method."""
    length = len(BrazilSpecProvider(seed=12345).cnpj())
    assert length == 18

# Generated at 2022-06-13 23:30:04.699587
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """This is the unit test of the method cpf of the BrazilSpecProvider class."""
    from mimesis.enums import Gender
    from mimesis.providers.person.en import Person
    from mimesis.providers.address.en import Address
    from mimesis.providers.person.pt_br import BrazilSpecProvider

    person_en = Person('en')
    address_en = Address('en')
    person_pt_br = Person('pt-br')
    address_pt_br = Address('pt-br')
    person_br = BrazilSpecProvider()
    # test cpf method
    assert len(person_br.cpf()) == 14
    assert person_br.cpf(with_mask=False) == person_pt_br.cpf(with_mask=False)

# Generated at 2022-06-13 23:30:08.589186
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""
    bsp = BrazilSpecProvider(seed=123)
    assert '77.732.230/0001-70' == bsp.cnpj()


# Generated at 2022-06-13 23:30:16.977336
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender
    from mimesis.providers.internet import Internet

    brazil_spec = BrazilSpecProvider()
    internet = Internet('pt-BR')

    for _ in range(100):
        cnpj = brazil_spec.cnpj()
        assert len(cnpj) is 18
        assert cnpj.isdigit()

    for _ in range(100):
        cnpj = brazil_spec.cnpj(with_mask=False)
        assert len(cnpj) is 14

    # For CPF
    for _ in range(100):
        cnpj = internet.cnpj()
        assert len(cnpj) is 14

    # For CPF (False)

# Generated at 2022-06-13 23:30:23.295203
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    provider = BrazilSpecProvider("test")
    assert provider.cpf() == "020.333.895-61"
    provider = BrazilSpecProvider("test")
    assert provider.cpf(with_mask=False) == "56321411129"


# Generated at 2022-06-13 23:30:27.198286
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    result = provider.cnpj(with_mask=False)
    assert isinstance(result, str)
    assert len(result) == 14
    assert result == '7773223000170'


# Generated at 2022-06-13 23:30:38.425331
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender

    print('\n\n############### Unit test for method cpf')
    # Init a provider for Brazil locale
    brazil_provider = BrazilSpecProvider()
    # Get a random CPF with Mask
    cpf_brazil_without_mask = brazil_provider.cpf(with_mask=False)
    print('CPF without mask:', cpf_brazil_without_mask)
    cpf_brazil_with_mask = brazil_provider.cpf(with_mask=True)
    print('CPF with mask:', cpf_brazil_with_mask)
    # Get a random female

# Generated at 2022-06-13 23:30:55.998741
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test for BrazilSpecProvider.cpf."""
    instance = BrazilSpecProvider()
    instance.seed(1730165014)
    cpf = instance.cpf()
    assert cpf == '003.847.283-19'

# Generated at 2022-06-13 23:30:58.169629
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj(with_mask=False)
    assert len(cnpj) == 14
    assert cnpj.isdigit()


# Generated at 2022-06-13 23:30:59.925707
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    _cnpj = BrazilSpecProvider().cnpj()
    assert _cnpj == "7.347.250/0001-73"


# Generated at 2022-06-13 23:31:03.836427
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    for i in range(10):
        assert BrazilSpecProvider.cpf(BrazilSpecProvider()) == BrazilSpecProvider().cpf()


# Generated at 2022-06-13 23:31:07.876766
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider(seed=42)
    cpf = provider.cpf()
    assert cpf != '001.137.297-40', 'Should be different from 001.137.297-40'
    assert cpf == '138.543.853-53', 'Should be equal to 138.543.853-53'


# Generated at 2022-06-13 23:31:11.133304
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    c = br.cpf()
    print(c)
    assert c == '219.532.817-13'

# Generated at 2022-06-13 23:31:14.066313
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj."""
    assert BrazilSpecProvider().cnpj() == '77.732.230/0001-70'

# Generated at 2022-06-13 23:31:21.583956
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    result = provider.cnpj()
    assert isinstance(result, str)
    assert len(result.replace(".", "").replace("-", "").replace("/", "")) == 14

    result_2 = provider.cnpj(with_mask=False)
    assert isinstance(result_2, str)
    assert len(result_2) == 14


# Generated at 2022-06-13 23:31:33.679472
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    count = 0
    while True:
        cpf = provider.cpf()
        if cpf != '000.000.000-00' and cpf != '111.111.111-11' and cpf != '222.222.222-22' and cpf != '333.333.333-33' and cpf != '444.444.444-44' and cpf != '555.555.555-55' and cpf != '666.666.666-66' and cpf != '777.777.777-77' and cpf != '888.888.888-88' and cpf != '999.999.999-99':
            break

    assert True



# Generated at 2022-06-13 23:31:40.566879
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    generator = BrazilSpecProvider()
    assert generator.cpf() == '481.579.998-54'
    assert generator.cpf(with_mask=False) == '48157999854'
    assert generator.cpf(with_mask=True) == '481.579.998-54'
    assert generator.cpf(gender=Gender.FEMALE) == '871.467.670-41'
    assert generator.cpf(gender=Gender.MALE) == '211.043.738-11'
    assert generator.cpf(with_mask=False, gender=Gender.FEMALE) == '87146767041'
    assert generator.cpf(with_mask=True, gender=Gender.MALE) == '211.043.738-11'



# Generated at 2022-06-13 23:32:00.313420
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():

    obj = BrazilSpecProvider()
    result = obj.cpf(True)
    assert isinstance(result, str)
    assert len(result) == 14
    assert result[3] == '.'
    assert result[7] == '.'
    assert result[11] == '-'

    result = obj.cpf(False)
    assert isinstance(result, str)
    assert len(result) == 11



# Generated at 2022-06-13 23:32:09.347442
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print('Test method cnpj of BrazilSpecProvider')
    brazil_spec_provider = BrazilSpecProvider()
    assert len(brazil_spec_provider.cnpj(with_mask=False)) == 14
    assert brazil_spec_provider.cnpj(with_mask=True).find('.') > 0
    assert brazil_spec_provider.cnpj(with_mask=True).find('-') > 0
    assert brazil_spec_provider.cnpj(with_mask=True).find('/') > 0


# Generated at 2022-06-13 23:32:11.448766
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf(with_mask=True) == '001.137.297-40'


# Generated at 2022-06-13 23:32:16.254282
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()

    assert provider.cnpj() == '77.732.230/0001-70'
    assert provider.cnpj(with_mask=False) == '77732230000170'
    assert len(provider.cnpj()) == 18


# Generated at 2022-06-13 23:32:18.966737
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    for i in range(0, 100):
        assert len(bsp.cnpj()) == 18



# Generated at 2022-06-13 23:32:22.749535
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    cnpj_mask = provider.cnpj(True)
    assert cnpj == '7773223000170'
    assert cnpj_mask == '77.732.230/0001-70'


# Generated at 2022-06-13 23:32:26.582315
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.person import Person
    from mimesis.builtins.spec import BR

    cpf = BR().cpf()
    assert cpf is not None
    assert len(cpf) == 14

    p = Person()
    assert p.cpf() is not None
    assert len(p.cpf()) == 14



# Generated at 2022-06-13 23:32:32.999881
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    
    # Test Case 1
    print("\nTest Case 1\n")
    bsp = BrazilSpecProvider()
    print("\nTest Case 1: CNPJ: " + bsp.cnpj())
    
    # Test Case 2
    print("\nTest Case 2\n")
    bsp = BrazilSpecProvider()
    print("\nTest Case 2: CNPJ: " + bsp.cnpj())


# Generated at 2022-06-13 23:32:40.588052
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    br = BrazilSpecProvider()
    cnpj = br.cnpj()
    assert len(cnpj) == 18
    assert set(cnpj[:2]).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
    assert set(cnpj[2]).issubset({'.'})
    assert set(cnpj[3:5]).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
    assert set(cnpj[5]).issubset({'.'})

# Generated at 2022-06-13 23:32:43.464260
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    result = provider.cpf()
    assert result and result.__class__ == str and len(result) == 14



# Generated at 2022-06-13 23:33:24.100989
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""

    bsp = BrazilSpecProvider()
    assert bsp.cnpj()


# Generated at 2022-06-13 23:33:28.827235
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '058.827.528-18'
    assert BrazilSpecProvider().cpf(with_mask=False) == '18411395980'


# Generated at 2022-06-13 23:33:32.003868
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    data = BrazilSpecProvider().cnpj()
    assert len(data) == 18
    assert data == '77.732.230/0001-70'


# Generated at 2022-06-13 23:33:34.345639
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    print(b.cnpj())


# Generated at 2022-06-13 23:33:38.695409
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert len(BrazilSpecProvider().cnpj()) == 18
    assert len(BrazilSpecProvider().cnpj(with_mask=False)) == 14



# Generated at 2022-06-13 23:33:42.191883
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    loc = BrazilSpecProvider()
    cnpj = loc.cnpj()
    assert str(type(cnpj)) == "<class 'str'>"
    assert len(cnpj) == 18
    return cnpj




# Generated at 2022-06-13 23:33:48.666248
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    provider = BrazilSpecProvider()
    assert provider.cpf() == provider.cpf(with_mask=True)
    assert provider.cpf(with_mask=False) == provider.cpf(with_mask=False)


# Generated at 2022-06-13 23:33:56.989033
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    br_person = Person('pt-br')
    cpf = br_person.cpf()
    assert(cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-' and cpf[15] == '-' and cpf[14] != '0')


# Generated at 2022-06-13 23:34:00.787168
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    pt_br = BrazilSpecProvider()
    cnpj = pt_br.cnpj()
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'

# Generated at 2022-06-13 23:34:04.293276
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Verifies the masking and generation of cpf numbers."""
    br = BrazilSpecProvider()
    cpf = br.cpf()
    cpf_1 = br.cpf(with_mask=False)
    assert len(cpf) == 14
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1
    assert len(cpf_1) == 11
    assert cpf_1[-2:] == cpf[11:]



# Generated at 2022-06-13 23:35:38.491551
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bp = BrazilSpecProvider()
    cnpj = bp.cnpj()
    assert cnpj == '97.831.639/0001-02'

# Generated at 2022-06-13 23:35:40.834513
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj() == '77.732.230/0001-70'

# Generated at 2022-06-13 23:35:48.890847
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Get an instance of class BrazilSpecProvider
    brazil_provider = BrazilSpecProvider()

    # Get a CNPJ with mask
    cnpj_with_mask = brazil_provider.cnpj(with_mask=True)
    # Get a CNPJ without mask
    cnpj_without_mask = brazil_provider.cnpj()

    assert len(cnpj_with_mask) == 18
    assert len(cnpj_without_mask) == 14
    assert cnpj_with_mask[12] == '-'
    assert cnpj_with_mask[8] == '/'
    assert cnpj_with_mask[5] == '.'
    assert cnpj_with_mask[2] == '.'

# Generated at 2022-06-13 23:35:50.822139
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf(False) == '00113729740'
    assert BrazilSpecProvider().cpf(True) == '001.137.297-40'


# Generated at 2022-06-13 23:35:52.466988
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Get a random CNPJ."""
    assert len(BrazilSpecProvider().cnpj(with_mask=False)) == 14


# Generated at 2022-06-13 23:35:53.413796
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    obj = BrazilSpecProvider()
    assert len(obj.cnpj()) == 14

# Generated at 2022-06-13 23:35:55.006028
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brasil_cpf = BrazilSpecProvider()
    assert type(brasil_cpf.cpf()) is str


# Generated at 2022-06-13 23:35:58.829804
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Create an instance of BrazilSpecProvider
    brazil = BrazilSpecProvider()
    assert brazil.cnpj(True) == '77.732.230/0001-70'
    assert brazil.cnpj(False) == '77732230000170'


# Generated at 2022-06-13 23:36:02.193996
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    cnpj = b.cnpj()
    print("CNPJ: " + cnpj)



# Generated at 2022-06-13 23:36:04.050030
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj(with_mask=True)
    print(cnpj)
    assert cnpj is not None

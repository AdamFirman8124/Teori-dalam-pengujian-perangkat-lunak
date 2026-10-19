

# Generated at 2022-06-13 23:28:34.435449
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()

    assert isinstance(cpf, str)
    assert len(cpf) == 14



# Generated at 2022-06-13 23:28:36.316736
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    print(bsp.cpf())
# test_BrazilSpecProvider_cpf()


# Generated at 2022-06-13 23:28:48.101099
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider(seed=0)
    # Test with mask
    result = brazil_provider.cpf(with_mask=True)
    assert result == '001.137.297.40'
    assert len(result) == 14
    result = brazil_provider.cpf(with_mask=True)
    assert result == '001.824.749.23'
    # Test without mask
    result = brazil_provider.cpf(with_mask=False)
    assert result == '001824749'
    assert len(result) == 9
    result = brazil_provider.cpf(with_mask=False)
    assert result == '00182474923'
    assert len(result) == 11
    # Test with mask and seed
    result = brazil_prov

# Generated at 2022-06-13 23:28:51.309220
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test if cpf method return 11 characters."""
    from mimesis import BrazilSpecProvider
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 11


# Generated at 2022-06-13 23:28:53.338153
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test the method cnpj."""
    provider = BrazilSpecProvider().cnpj()
    assert len(provider) == 18

# Generated at 2022-06-13 23:29:01.110181
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for cnpj method in BrazilSpecProvider class.

    Note:
        The tests are based on the following CNPJs:
        - https://www.geradordecnpj.com/
        - https://www.4devs.com.br/gerador_de_cnpj
        - https://cnpj-valido.com.br/
    """
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj(with_mask=False)
    assert len(cnpj) == 14
    assert bsp.cnpj(with_mask=False) == '50314607000125'
    assert bsp.cnpj(with_mask=False) == '11205591000124'

# Generated at 2022-06-13 23:29:05.295158
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider(seed=123)
    res_1 = provider.cpf()
    res_2 = provider.cpf(False)
    assert res_1 == '471.589.902-34'
    assert res_2 == '47158990234'


# Generated at 2022-06-13 23:29:13.033573
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj1 = provider.cnpj()
    for i in range(0, 10):
        cnpj2 = provider.cnpj()
        if cnpj1 == cnpj2:
            print("ERROR: cnpj1 = cnpj2")
            print("cnpj1 = ", cnpj1)
            print("cnpj2 = ", cnpj2)
            return
    print("SUCCESS: different cnpj were generated")

# Generated at 2022-06-13 23:29:27.073995
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    p = BrazilSpecProvider()
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())
    print(p.cpf())


#

# Generated at 2022-06-13 23:29:30.252868
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for BrazilSpecProvider.cpf."""
    provider = BrazilSpecProvider()
    result = provider.cpf()
    assert isinstance(result, str)
    assert len(result) == 14
    assert result[12:] != '--'


# Generated at 2022-06-13 23:29:49.713163
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from pymimesis import Mimesis
    from mimesis.typing import Seed

    seed = Seed.random()
    mimesis = Mimesis(seed=seed)
    brazil_spec_provider = mimesis.BrazilSpecProvider()

    result = brazil_spec_provider.cpf()

    # expected value: '006.054.748-89'
    expected = '006.054.748-89'
    assert result == expected

# Generated at 2022-06-13 23:29:51.540645
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert len(cnpj) == 18

# Generated at 2022-06-13 23:29:58.419756
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    for _ in range(10):
        cpf = brazil.cpf(with_mask=True)
        assert len(cpf) == 14, "It must be equal to 14"
        assert cpf[3] == '.', "3th element should be '.'"
        assert cpf[7] == '.', "7th element should be '.'"
        assert cpf[11] == '-', "11th element should be '-'"


# Generated at 2022-06-13 23:30:08.942360
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brasil_cpf = BrazilSpecProvider()
    assert brasil_cpf.cpf() != '000.000.000-00'
    assert brasil_cpf.cpf() != '111.111.111-11'
    assert brasil_cpf.cpf() != '222.222.222-22'
    assert brasil_cpf.cpf() != '333.333.333-33'
    assert brasil_cpf.cpf() != '444.444.444-44'
    assert brasil_cpf.cpf() != '555.555.555-55'
    assert brasil_cpf.cpf() != '666.666.666-66'
    assert brasil_cpf.cpf() != '777.777.777-77'
    assert brasil_cpf.cpf()

# Generated at 2022-06-13 23:30:11.245693
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert(BrazilSpecProvider().cpf(False) == "31595079412")


# Generated at 2022-06-13 23:30:15.394118
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # arrange
    from mimesis.specs import BrazilSpecProvider as spec
    from mimesis.typing import Seed

    seed = Seed(1)
    sut = spec(seed)

    expected_value = '13.175.683/0001-62'
    # act
    actual_value = sut.cnpj(with_mask=True)

    # assert
    assert expected_value == actual_value

# Generated at 2022-06-13 23:30:19.762070
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert isinstance(provider.cnpj(), str)
    assert len(provider.cnpj()) == 18
    assert provider.cnpj(with_mask=False).isdigit()


# Generated at 2022-06-13 23:30:22.934608
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    test = BrazilSpecProvider()
    cpf = test.cpf()
    assert isinstance(cpf, str)



# Generated at 2022-06-13 23:30:25.816174
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # It is not necessary to set the seed parameter when using
    # a unit test, beacuse the seed is different every time
    provider = BrazilSpecProvider()
    print(provider.cnpj())

# Generated at 2022-06-13 23:30:28.615113
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf."""
    # Setup
    random = BrazilSpecProvider()

    # Act
    cpf = random.cpf()

    # Assert
    assert len(cpf) == 14


# Generated at 2022-06-13 23:31:00.164943
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider
    brazil.random = (1,1,1,1,1,1,1,1,1,1,10,11)
    assert (brazil.cpf(with_mask=False) == '11111111111')


# Generated at 2022-06-13 23:31:03.888906
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf()
    assert provider.cpf(with_mask=False)


# Generated at 2022-06-13 23:31:07.635351
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Test cnpj with mask
    provider = BrazilSpecProvider()
    assert provider.cnpj(with_mask=True) == '21.688.299/0001-84'
    # Test cnpj without mask
    assert provider.cnpj(with_mask=False) == '21688299000184'


# Generated at 2022-06-13 23:31:12.979581
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil_spec_provider = BrazilSpecProvider()
    for i in range(3):
        cnpj = brazil_spec_provider.cnpj()
        assert len(cnpj) == 18
        assert cnpj.isdigit() == True


# Generated at 2022-06-13 23:31:21.051585
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers import BrazilSpecProvider
    import re

    brazil_provider = BrazilSpecProvider()

    for _ in range(1000):
        cnpj = brazil_provider.cnpj()
        assert re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', cnpj) is not None


# Generated at 2022-06-13 23:31:24.002654
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    provider = BrazilSpecProvider()
    cnpj_with_mask = '77.732.230/0001-70'
    assert provider.cnpj(with_mask=True) == cnpj_with_mask



# Generated at 2022-06-13 23:31:26.019245
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    print(provider.cpf())


# Generated at 2022-06-13 23:31:27.819251
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert len(provider.cnpj()) == 18

# Generated at 2022-06-13 23:31:32.630254
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18
    cnpj = bsp.cnpj(with_mask=False)
    assert len(cnpj) == 14


# Generated at 2022-06-13 23:31:34.809427
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:32:38.625359
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    data_provider = BrazilSpecProvider()
    assert data_provider._validate_cpf('37226672340') == True


# Generated at 2022-06-13 23:32:41.806005
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazilian_provider = BrazilSpecProvider()
    assert brazilian_provider.cpf()
    assert brazilian_provider.cpf()
    assert brazilian_provider.cpf()
    assert brazilian_provider.cpf()


# Generated at 2022-06-13 23:32:52.971777
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    result = BrazilSpecProvider().cnpj()
    assert len(result) == 18
    assert result[0:2] != '00'
    assert result[2:5] != '000'
    assert result[5:8] != '000'
    assert result[8:12] != '0000'
    assert result[12:14] != '00'
    assert result[14:] != '00'
    assert result[2:3] == '.'
    assert result[5:6] == '.'
    assert result[8:9] == '/'
    assert result[12:13] == '-'



# Generated at 2022-06-13 23:32:56.838479
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert cnpj is not None

# Generated at 2022-06-13 23:32:58.213914
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    sp = BrazilSpecProvider()
    cnpj = sp.cnpj()
    assert len(cnpj) == 18

# Generated at 2022-06-13 23:33:01.923441
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Test if a CNPJ with mask is correctly generated
    from mimesis.providers.brazil import BrazilSpecProvider
    provider = BrazilSpecProvider()
    result = provider.cnpj(with_mask=True)
    assert len(result) == 18
    assert '.' in result
    assert '/' in result
    assert '-' in result
    # Test if a CNPJ without mask is correctly generated
    result = provider.cnpj(with_mask=False)
    assert len(result) == 14
    assert '.' not in result
    assert '/' not in result
    assert '-' not in result


# Generated at 2022-06-13 23:33:08.682971
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert len(provider.cnpj()) == 18
    assert len(provider.cnpj(with_mask=False)) == 14
    assert len(provider.cnpj()) == 18
    assert len(provider.cnpj(with_mask=False)) == 14


# Generated at 2022-06-13 23:33:16.050132
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert len(BrazilSpecProvider().cnpj()) == 18
    assert len(BrazilSpecProvider().cnpj(False)) == 14

    brazil = BrazilSpecProvider()
    broj = brazil.cnpj()
    assert broj[2] != '.'
    assert broj[6] != '.'
    assert broj[10] != '/'
    assert broj[15] != '-'
    broj1 = BrazilSpecProvider().cnpj(with_mask=False)
    assert broj1.isdigit()

# Generated at 2022-06-13 23:33:19.709280
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazilSpecProvider = BrazilSpecProvider()
    cpf = brazilSpecProvider.cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:33:22.845893
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of BrazilSpecProvider class."""
    g = BrazilSpecProvider()
    assert g.cnpj(with_mask=True) == '09.837.920/0001-99'


# Generated at 2022-06-13 23:36:03.391431
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider(seed=42)
    assert bsp.cpf(with_mask=True) == '073.924.955-28'
    assert bsp.cpf(with_mask=False) == '07392495528'


# Generated at 2022-06-13 23:36:06.678075
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method BrazilSpecProvider_cnpj."""
    obj = BrazilSpecProvider()
    assert len(obj.cnpj()) == 18

# Generated at 2022-06-13 23:36:12.371014
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    from mimesis import BrazilSpecProvider as CPF
    cpfs = CPF()
    assert len(cpfs.cpf()) == 14
    assert len(cpfs.cpf(False)) == 11


# Generated at 2022-06-13 23:36:19.638252
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    _cnpj = BrazilSpecProvider().cnpj()
    assert len(_cnpj) == 18
    assert _cnpj.count('.') == 2
    assert _cnpj.count('/') == 1
    assert _cnpj.count('-') == 1
    assert _cnpj[12:13] == '-'



# Generated at 2022-06-13 23:36:23.192147
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    expected = '77.732.230/0001-70'
    result = BrazilSpecProvider().cnpj(with_mask=True)
    print(result)
    assert expected == result



# Generated at 2022-06-13 23:36:39.206696
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    p = BrazilSpecProvider()
    assert len(p.cpf()) == 14
    assert len(p.cpf(with_mask=False)) == 11


# Generated at 2022-06-13 23:36:48.979393
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    bz = BrazilSpecProvider('pt-br')
    with_mask = bz.cpf()
    without_mask = bz.cpf(with_mask=False)
    assert len(with_mask) == 14
    assert len(without_mask) == 11
    assert with_mask[-2:].isdigit()
    assert with_mask.count('.') == 2
    assert with_mask.count('-') == 1
    assert without_mask[-2:].isdigit()


# Generated at 2022-06-13 23:36:52.133781
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bz = BrazilSpecProvider()
    cpf = bz.cpf()
    print(cpf)
    print(len(cpf))
    print(cpf.isdigit())


# Generated at 2022-06-13 23:36:58.390710
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()

    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert len(cpf.replace('.', '').replace('-', '')) == 11


# Generated at 2022-06-13 23:37:06.165037
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    # It is necessary that the verify digit is correct
    provider_1 = BrazilSpecProvider()
    assert provider_1.cnpj() == "23.892.806/0001-63"
    assert provider_1.cnpj() == "77.732.230/0001-70"
    assert provider_1.cnpj() == "05.989.906/0001-26"
    assert provider_1.cnpj() == "93.319.927/0001-09"
    assert provider_1.cnpj() == "64.094.470/0001-92"
    assert provider_1.cnpj() == "05.501.836/0001-08"
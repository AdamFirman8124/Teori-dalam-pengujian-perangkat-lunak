

# Generated at 2022-06-13 23:28:31.885456
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider(0)
    assert provider.cnpj(False) == '45.837.685/0001-67'

# Generated at 2022-06-13 23:28:35.966153
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
    cpf = brazil_provider.cpf(True)
    assert re.match("^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf) != None



# Generated at 2022-06-13 23:28:43.009549
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print('test_BrazilSpecProvider_cpf started...')
    brazilSpecProvider = BrazilSpecProvider()
    brazilSpecProvider.seed('mimesis_seed')
    cpf = brazilSpecProvider.cpf(False)
    expectedCpf = '51331719278'
    assert cpf == expectedCpf
    print('test_BrazilSpecProvider_cpf OK!')


# Generated at 2022-06-13 23:28:44.939882
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '003.238.428-18'


# Generated at 2022-06-13 23:28:49.734530
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    assert isinstance(bsp.cpf(), str)
    assert isinstance(bsp.cpf(True), str)
    assert isinstance(bsp.cpf(False), str)
    assert bsp.cpf() != bsp.cpf()
    assert bsp.cpf(False) != bsp.cpf(False)


# Generated at 2022-06-13 23:28:52.439316
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_spec_provider = BrazilSpecProvider()
    assert brazil_spec_provider.cpf() == '399.349.578-82'
    

# Generated at 2022-06-13 23:28:54.463399
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    assert brazil.cnpj() == '77.732.230/0001-70'


# Generated at 2022-06-13 23:28:57.553493
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Arrange
    from mimesis.enums import Gender

    brazil = BrazilSpecProvider()
    cnpj = '65.067.723/0001-82'
    # Act
    pass
    # Assert
    assert brazil.cnpj() == cnpj

# Generated at 2022-06-13 23:29:03.498559
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider"""
    # Given
    brazil_provider = BrazilSpecProvider()
    # When
    result1 = [brazil_provider.cpf() for _ in range(50)]
    # Then
    assert len(result1) == 50 and len(result1[0]) == 14 and result1[0].startswith('123')
    # And
    # Given
    brazil_provider = BrazilSpecProvider()
    # When
    result2 = [brazil_provider.cpf(with_mask = False) for _ in range(50)]
    # Then
    assert len(result2) == 50 and len(result2[0]) == 11 and result2[0].startswith('123')


# Generated at 2022-06-13 23:29:08.100942
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil_ptbr_provider import BrazilSpecProvider
    b = BrazilSpecProvider()
    c = b.cnpj()
    print(c)
    assert c == "38.375.793/0001-63"

# Generated at 2022-06-13 23:29:18.271719
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Tests method BrazilSpecProvider.cnpj()."""
    provider = BrazilSpecProvider()
    assert provider.cnpj() == '77.732.230/0001-70'



# Generated at 2022-06-13 23:29:27.844354
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('pt-br')
    p = BrazilSpecProvider()

    for _ in range(10):
        cpf = p.cpf()
        assert len(cpf) == 14

        # Checksum validation https://www.geradordecpf.org/algoritmo_do_cpf.htm
        raw_cpf = cpf.replace('.', '').replace('-', '')
        assert int(raw_cpf[-2:]) == p.cpf_checksum(raw_cpf[:-2])



# Generated at 2022-06-13 23:29:30.120878
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    BR = BrazilSpecProvider()
    print(BR.cpf())


# Generated at 2022-06-13 23:29:31.306132
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    pass

# Generated at 2022-06-13 23:29:44.722893
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Get instances of provider
    br_provider = BrazilSpecProvider()
    br_provider_normal = BrazilSpecProvider("normal_seed")
    br_provider_fixed = BrazilSpecProvider("fixed_seed")

    # test method cnpj of class BrazilSpecProvider
    br_cnpj_list = []
    br_provider_normal_cnpj_list = []
    br_provider_fixed_cnpj_list = []

    br_cnpj_list.append(br_provider.cnpj(False))
    br_provider_normal_cnpj_list.append(br_provider_normal.cnpj(False))
    br_provider_fixed_cnpj_list.append(br_provider_fixed.cnpj(False))

    # Test that cnpj should

# Generated at 2022-06-13 23:29:48.387848
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cp = BrazilSpecProvider()
    cnpj = cp.cnpj()
    assert len(cnpj) == 14
    cnpj = cp.cnpj(with_mask=False)
    assert len(cnpj) == 12


# Generated at 2022-06-13 23:29:51.322389
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.person.pt_br import BrazilSpecProvider
    bs = BrazilSpecProvider()
    print(bs.cpf())



# Generated at 2022-06-13 23:29:53.741975
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    BrazilSpecProvider.cnpj(with_mask=True) == "77.732.230/0001-70"

test_BrazilSpecProvider_cnpj()

# Generated at 2022-06-13 23:29:56.511597
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    for _ in range(1, 10):
        print(bsp.cnpj())


# Generated at 2022-06-13 23:30:06.013638
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    obj = BrazilSpecProvider()
    cnpj = obj.cnpj()

    # Test of the length
    assert(len(cnpj) == 18)
    # Test of the mask
    cnpj_list = [int(i) for i in cnpj if i != '.' and i != '-' and i != '/']
    first_dv = obj.get_verifying_digit_cnpj(cnpj_list, 6)
    assert(first_dv == cnpj_list[12])



# Generated at 2022-06-13 23:30:23.082076
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """
    Test method BrazilSpecProvider.cpf.
    """
    # Test for method cpf
    assert BrazilSpecProvider().cpf()
    print("Method BrazilSpecProvider.cpf() passed all tests!")


# Generated at 2022-06-13 23:30:24.922939
# Unit test for method cnpj of class BrazilSpecProvider

# Generated at 2022-06-13 23:30:26.972323
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    assert brazil.cnpj() == "77.732.230/0001-70"


# Generated at 2022-06-13 23:30:31.432722
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    settings = Settings('pt-br')
    settings.seed = 2
    my_provider = BrazilSpecProvider(settings.seed)

    assert my_provider.cpf() == '741.851.415-19'
    assert my_provider.cpf(with_mask=False) == '74185141519'


# Generated at 2022-06-13 23:30:38.384164
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj1 = provider.cnpj()
    cnpj2 = provider.cnpj(with_mask=False)
    cnpj3 = provider.cnpj()
    cnpj4 = provider.cnpj(with_mask=False)

    assert cnpj1 == cnpj2
    assert cnpj1 != cnpj3
    assert cnpj3 == cnpj4

# Generated at 2022-06-13 23:30:44.495502
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bp = BrazilSpecProvider()
    # Test cpf without mask
    cpf = bp.cpf(with_mask=False)
    assert len(cpf) is 11
    # Test cpf with mask
    cpf = bp.cpf()
    assert len(cpf) is 14


# Generated at 2022-06-13 23:30:45.734478
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    BrazilSpecProvider.cnpj() # TODO: Add test cases

# Generated at 2022-06-13 23:30:56.752353
# Unit test for method cnpj of class BrazilSpecProvider

# Generated at 2022-06-13 23:30:59.216744
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert len(BrazilSpecProvider().cpf()) == 14
    assert BrazilSpecProvider().cpf().find('.') == 3
    assert BrazilSpecProvider().cpf().find('-') == 7


# Generated at 2022-06-13 23:31:04.821436
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import BrazilSpecProvider
    brazil_provider = BrazilSpecProvider()
    for i in range(0, 50):
        cpf = brazil_provider.cpf()
        assert len(cpf) == 14, 'length of cpf must be 14'


# Generated at 2022-06-13 23:31:32.566058
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert cpf
    assert isinstance(cpf, str)



# Generated at 2022-06-13 23:31:44.211060
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test for BrazilSpecProvider_cpf.

    Test data was manually verified in http://www.geradordecpf.org/validador-de-cpf.htm
    and http://www.geradordecpf.org/cpf-aleatorio-validador.htm."""


# Generated at 2022-06-13 23:31:46.222381
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj(with_mask=True)
    assert cnpj == '77.732.230/0001-70'


# Generated at 2022-06-13 23:31:48.939783
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() != None
    assert provider.cpf(with_mask=False) != None


# Generated at 2022-06-13 23:31:53.193615
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
    cpf_without_mask = brazil_provider.cpf(with_mask=False)
    cpf_with_mask = brazil_provider.cpf(with_mask=True)

    assert cpf_without_mask == '00113729740'
    assert cpf_with_mask == '001.137.297-40'



# Generated at 2022-06-13 23:31:55.210709
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() != provider.cpf()


# Generated at 2022-06-13 23:31:56.831471
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    b.cnpj()

# Generated at 2022-06-13 23:32:02.324907
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    cpf = b.cpf()
    cpf_without_mask = b.cpf(False)
    assert len(cpf) == len(cpf_without_mask) == 14
    assert isinstance(b.cpf(False), str)
    assert '.' in cpf
    assert '-' in cpf
    assert '.' not in cpf_without_mask
    assert '-' not in cpf_without_mask


# Generated at 2022-06-13 23:32:14.512316
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil import BrazilSpecProvider
    from mimesis.enums import Gender
    import re

    specProvider = BrazilSpecProvider(seed=42)
    cnpj = specProvider.cnpj()

    assert cnpj != None
    assert cnpj != ''
    assert cnpj != ' '
    assert cnpj != '  '
    assert cnpj != '    '
    assert type(cnpj) == str
    assert cnpj != specProvider.cnpj()
    assert re.match(r'\d{2}.\d{3}.\d{3}/\d{4}-\d{2}', cnpj)
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:32:17.985748
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Asserts if the generated CNPJ is valid."""
    from mimesis.builtins import BrazilSpecProvider as BSP
    bsp = BSP()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:33:29.985567
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    expected_result = '77.732.230/0001-70'
    obj = BrazilSpecProvider()
    result = obj.cnpj()
    assert result == expected_result


# Generated at 2022-06-13 23:33:36.569265
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider(seed = 1)
    assert provider.cnpj(with_mask=True) == "52.031.853/0001-17"
    assert provider.cnpj(with_mask=False) == "52031.853/000117"


# Generated at 2022-06-13 23:33:39.701556
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert len(BrazilSpecProvider(seed=10).cnpj()) == 14


# Generated at 2022-06-13 23:33:40.306981
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    pass

# Generated at 2022-06-13 23:33:43.527174
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert len(cpf) == 14
    cpf = bsp.cpf(with_mask=False)
    assert len(cpf) == 11
    
    

# Generated at 2022-06-13 23:33:47.486169
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br_provider = BrazilSpecProvider()
    cpf = br_provider.cpf()

    assert len(cpf) == 14
    assert '.' in cpf
    assert '-' in cpf


# Generated at 2022-06-13 23:33:51.761826
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""

    cnpj = BrazilSpecProvider().cnpj()

    assert len(cnpj) == 18
    assert isinstance(cnpj, str)


# Generated at 2022-06-13 23:33:58.716776
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj() != provider.cnpj()
    assert provider.cnpj(with_mask=False) != provider.cnpj(with_mask=False)
    assert len(provider.cnpj()) == 18
    assert len(provider.cnpj(with_mask=False)) == 14


# Generated at 2022-06-13 23:34:01.478526
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider(seed = '512e0f').cnpj(with_mask = True)
    assert cnpj == '83.921.569/0001-05'

# Generated at 2022-06-13 23:34:02.611179
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    print(cpf)


# Generated at 2022-06-13 23:37:04.094896
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    cnpj = b.cnpj(True)
    assert isinstance(cnpj,str) and len(str(cnpj)) > 12 and len(str(cnpj)) < 19


# Generated at 2022-06-13 23:37:07.292397
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == "039.691.864-18"
    assert BrazilSpecProvider().cpf(with_mask=False) == "03969186418"


# Generated at 2022-06-13 23:37:17.949335
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()

    assert isinstance(cpf, str)
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'

    cpf = provider.cpf(with_mask=False)
    assert isinstance(cpf, str)
    assert len(cpf) == 11



# Generated at 2022-06-13 23:37:22.940840
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Check that the cpf method of class BrazilSpecProvider works fine."""
    # initialize class BrazilSpecProvider
    brazil_spec_provider = BrazilSpecProvider()
    # assert that the cpf has 11 characters
    assert len(brazil_spec_provider.cpf()) == 11
    # assert that the cpf is different from the last one
    assert brazil_spec_provider.cpf() != brazil_spec_provider.cpf()


# Generated at 2022-06-13 23:37:24.708495
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for BrazilSpecProvider.cpf()."""
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:37:30.153131
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.base import BaseSpecProvider
    from mimesis.builtins.base import BaseSpecProvider
    bsp = BrazilSpecProvider()
    for _ in range(10):
        cpf = bsp.cpf(with_mask=True)
        print(cpf)



# Generated at 2022-06-13 23:37:37.005691
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from random import seed
    from mimesis import BrazilSpecProvider
    from mimesis.providers.person import Person

    provider = BrazilSpecProvider()
    person_provider = Person('pt-br')

    for i in range(0, 15):
        for j in range(4):
            valid_cpf = provider.cpf(with_mask=False)
            invalid_cpf = provider.cpf(with_mask=False)

            # check invalid_cpf contains equal numbers
            equal_numbers = valid_cpf[0] * 11
            assert invalid_cpf != equal_numbers
            assert invalid_cpf != valid_cpf

            # check invalid_cpf contains 9 numbers
            assert len(invalid_cpf) == 11
            assert len(valid_cpf) == 11



# Generated at 2022-06-13 23:37:44.392413
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from re import compile
    from random import seed
    random_seed = 123456789
    seed(random_seed)
    provider = BrazilSpecProvider()
    with_mask = True
    cnpj = provider.cnpj()
    assert(compile('^[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}$').match(cnpj))


# Generated at 2022-06-13 23:37:46.362435
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    BR = BrazilSpecProvider()
    print(BR.cnpj())


# Generated at 2022-06-13 23:37:51.284476
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1

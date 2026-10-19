

# Generated at 2022-06-13 23:28:37.212622
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil import BrazilSpecProvider
    from mimesis.schema import Field, Schema

    class CPF(Schema):
        """Provide CPF."""

        document = Field('cpf')

    cpf = CPF()
    brazil = BrazilSpecProvider()

    for i in range(10):
        assert cpf.document() == brazil.cpf()


# Generated at 2022-06-13 23:28:40.430612
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    for i in range(100):
        assert BrazilSpecProvider().cnpj()
        assert len(BrazilSpecProvider().cnpj()) == 18


# Generated at 2022-06-13 23:28:50.580810
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bp = BrazilSpecProvider()
    cnpj = bp.cnpj()

    assert len(cnpj) == 18  # cnpj length with mask
    assert cnpj[2:3] == '.'  # third character should be '.'
    assert cnpj[6:7] == '.'  # seventh character should be '.'
    assert cnpj[10:11] == '/'  # eleventh character should be '/'
    assert cnpj[15:16] == '-'  # sixteenth character should be '-'

    # Unit test for method cnpj of class BrazilSpecProvider with parameter as False
    cnpj = bp.cnpj(with_mask=False)

    assert len(cnpj) == 14  # cnpj length without mask


# Generated at 2022-06-13 23:28:54.677913
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.builtins import BrazilSpecProvider

    provider = BrazilSpecProvider()
    provider.person.create(gender=Gender.FEMALE, seed='1')
    provided_value = provider.cpf()
    expected = '170.283.969-40'
    assert provided_value == expected


# Generated at 2022-06-13 23:28:57.131905
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    for i in range(0, 100):
        b = BrazilSpecProvider()
        cnpj = b.cnpj(with_mask=False)
        assert len(cnpj) == 14


# Generated at 2022-06-13 23:29:04.258777
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    c2 = BrazilSpecProvider()
    # Test when with_mask is True
    cpf = c2.cpf()
    assert type(cpf) == str and len(cpf) == 14
    # Test when with_mask is False
    cpf = c2.cpf(with_mask=False)
    assert type(cpf) == str and len(cpf) == 11


# Generated at 2022-06-13 23:29:10.966226
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider"""
    # Need to test with random seed
    # Need to test with locale pt-br
    # Need to test with locale en
    # Need to test with locale pt-PT
    # Need to test with locale es
    # Need to test with locale it
    # Need to test with locale de
    pass


# Generated at 2022-06-13 23:29:15.029056
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
    print (brazil_provider.cpf(with_mask = True))


# Generated at 2022-06-13 23:29:18.118936
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    assert len(b.cnpj().replace(".", "").replace("/", "").replace("-", "")) == 14


# Generated at 2022-06-13 23:29:27.005905
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """ Test method cpf of class BrazilSpecProvider. """
    _seed = 324
    _with_mask = True
    _cpf_without_dv = [3,2,4,0,0,0,0,0,0]
    _cpf = '324.000.000-00'

    brazil = BrazilSpecProvider(_seed)
    assert _cpf_without_dv == brazil._cpf(_cpf_without_dv, 1)
    assert _cpf == brazil.cpf()



# Generated at 2022-06-13 23:29:35.182410
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method BrazilSpecProvider.cnpj"""
    assert BrazilSpecProvider().cnpj()

# Generated at 2022-06-13 23:29:42.218832
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    arquivo = open('brazil-cpf.txt', 'w')
    gerador = BrazilSpecProvider()
    for _ in range(10):
        cpf = gerador.cpf(with_mask=True)
        arquivo.write(cpf + '\n')
    arquivo.close()


# Generated at 2022-06-13 23:29:47.658539
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    cpf = brazil.cpf()
    parts = cpf.split('-')
    assert(len(parts)==2)
    assert(len(parts[0])==9)
    assert(len(parts[1])==2)
    assert(len(parts[0].split('.'))==3)


# Generated at 2022-06-13 23:29:53.201641
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    cpf = BrazilSpecProvider().cpf(with_mask=False)
    assert len(cpf) == 11


# Generated at 2022-06-13 23:29:58.281942
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf."""
    expected_result = """Test failed! : BrazilSpecProvider.cpf()
Result '001137297-40' does not match with expected '00113729740'"""

    result = BrazilSpecProvider().cpf()

    assert result == '00113729740', expected_result


# Generated at 2022-06-13 23:30:08.883059
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import BrazilianSpecProvider
    from mimesis.enums import Gender
    from mimesis.exceptions import NonEnumerableError

    brazil_provider = BrazilianSpecProvider()
    brazil_provider.seed_instance('1234567890')

    # Unit test for method gender of class BrazilSpecProvider
    assert brazil_provider.gender(Gender.MALE) == "Masculino"
    assert brazil_provider.gender(Gender.FEMALE) == "Feminino"
    assert (brazil_provider.gender(Gender.MALE, order='f')
            == "Feminino")
    assert (brazil_provider.gender(Gender.FEMALE, order='f')
            == "Masculino")

# Generated at 2022-06-13 23:30:12.598763
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 14
    assert len(provider.cpf(with_mask=False)) == 11
    assert provider.cpf(with_mask=False).isdigit()


# Generated at 2022-06-13 23:30:25.257419
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.datetime import Datetime
    from mimesis.enums import Gender
    from mimesis.builtins import BrazilSpecProvider
    from mimesis.builtins import BrazilSpecProvider
    from mimesis.providers.datetime import Datetime
    from mimesis.enums import Gender
    from mimesis.builtins import BrazilSpecProvider
    from mimesis.builtins import BrazilSpecProvider
    from mimesis.providers.datetime import Datetime
    from mimesis.enums import Gender
    from mimesis.builtins import BrazilSpecProvider
    from mimesis.builtins import BrazilSpecProvider
    from mimesis.providers.datetime import Datetime
    from mimesis.enums import Gender
    from mimesis.builtins import BrazilSpecProvider

# Generated at 2022-06-13 23:30:28.189795
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test the method cnpj of class BrazilSpecProvider."""
    assert len(BrazilSpecProvider().cnpj()) == 18
    assert BrazilSpecProvider().cnpj(with_mask=False) == BrazilSpecProvider().cnpj()


# Generated at 2022-06-13 23:30:31.432184
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    a = BrazilSpecProvider()

    # test cgj with mask
    assert a.cnpj()

    # test cgj without mask
    assert a.cnpj(with_mask=False)


# Generated at 2022-06-13 23:30:47.594157
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    cnpj = brazil.cnpj()
    assert cnpj == '53.855.087/0001-33'


# Generated at 2022-06-13 23:30:51.331238
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    a = BrazilSpecProvider()
    for i in range(0, 10):
        print(a.cnpj(with_mask=True))
        print(a.cnpj(with_mask=False))


# Generated at 2022-06-13 23:30:53.158098
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil import BrazilSpecProvider
    BrazilSpecProvider().cnpj()


# Generated at 2022-06-13 23:30:56.376171
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf(False)
    assert len(cpf) == 11
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:30:57.892672
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 11


# Generated at 2022-06-13 23:31:01.060039
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    '''Test cnpj method of BrazilSpecProvider'''
    bs = BrazilSpecProvider()
    assert bs.cnpj() == '74.530.908/0001-69'
    assert bs.cnpj(with_mask=False) == '74530908000169'


# Generated at 2022-06-13 23:31:02.201389
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    BP = BrazilSpecProvider()
    for _ in range(0, 10):
        assert len(BP.cpf()) == 14

# Generated at 2022-06-13 23:31:04.829416
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    result = provider.cpf()
    print("BrazilSpecProvider.cpf: ", result)


# Generated at 2022-06-13 23:31:08.482749
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print(BrazilSpecProvider().cnpj(with_mask=True))
    assert BrazilSpecProvider().cnpj(with_mask=True) == '98.187.793/0001-20'


# Generated at 2022-06-13 23:31:22.050720
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()

    bsp_cnpj = bsp.cnpj(with_mask=False)
    assert len(bsp_cnpj) == 14

    # A cnpj number must have the following format: ddd.ddd.ddd/dddd-dd.
    # So, the number 0 must not be in the first-third, eighth and tenth positions.
    # The number 1 can be in any position, so we will remove it from the code
    bsp_cnpj_without_first_third_eighth_and_tenth_position_ones = bsp_cnpj.replace('.', '').replace('/', '')[:8] + bsp_cnpj[10:12] + bsp_cnpj[13:]
    assert bsp_cnpj_without_first_third

# Generated at 2022-06-13 23:31:54.203107
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""
    from mimesis.providers import BrazilSpecProvider
    seed = 'Panama city'
    br_spec = BrazilSpecProvider(seed=seed)
    cnpj = br_spec.cnpj()
    assert cnpj is not None
    assert br_spec.cnpj(with_mask=False) == '99370956000181'


# Generated at 2022-06-13 23:32:00.150558
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins import BrazilSpecProvider

    brazilProvider = BrazilSpecProvider()

    cpf = brazilProvider.cpf()

    assert len(cpf) == 14, "Length should be 14"

    assert cpf[3] == '.', "Char position 3 should be a dot"
    assert cpf[7] == '.', "Char position 7 should be a dot"
    assert cpf[11] == '-', "Char position 11 should be a dash"


# Generated at 2022-06-13 23:32:01.783674
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider()

# Generated at 2022-06-13 23:32:14.179549
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    digito1 = provider.random.randint(0, 9)
    digito2 = provider.random.randint(0, 9)
    digito3 = provider.random.randint(0, 9)
    digito4 = provider.random.randint(0, 9)
    digito5 = provider.random.randint(0, 9)
    digito6 = provider.random.randint(0, 9)
    digito7 = provider.random.randint(0, 9)
    digito8 = provider.random.randint(0, 9)
    digito9 = provider.random.randint(0, 9)
    digito10 = provider.random.randint(0, 9)
    digito11 = provider.random.randint(0, 9)
    digito12

# Generated at 2022-06-13 23:32:20.017888
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
    assert isinstance(brazil_provider.cpf(), str)
    assert len(brazil_provider.cpf()) == 14
    assert len(brazil_provider.cpf(False)) == 11
    assert '-' in brazil_provider.cpf()
    assert '.' in brazil_provider.cpf()


# Generated at 2022-06-13 23:32:20.991267
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    BrazilSpecProvider.cpf()


# Generated at 2022-06-13 23:32:25.407338
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # test method cnpj()
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert isinstance(cnpj, str)
    assert len(cnpj) == 18
    assert bool(re.match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj))

# Generated at 2022-06-13 23:32:34.679748
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis import BrazilSpecProvider
    from mimesis.enums import Gender
    bsp = BrazilSpecProvider()

    cnpj = bsp.cnpj(with_mask=False)
    assert cnpj not in [None, ""]
    assert isinstance(cnpj, str)
    assert len(cnpj) == 14

    cnpj = bsp.cnpj(with_mask=True)
    assert cnpj not in [None, ""]
    assert isinstance(cnpj, str)
    assert len(cnpj) == 18
    assert '.' in cnpj
    assert '/' in cnpj
    assert '-' in cnpj

# Generated at 2022-06-13 23:32:38.265169
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():

    brazil_provider = BrazilSpecProvider()

    cpf = brazil_provider.cpf()

    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:32:39.934960
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import doctest 
    doctest.testmod(verbose=True)


# Generated at 2022-06-13 23:33:46.585455
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    assert isinstance(bsp.cnpj(), str)
    assert bsp.cnpj() == bsp.cnpj()
    assert bsp.cnpj() != bsp.cnpj()


# Generated at 2022-06-13 23:33:49.496017
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    instance = BrazilSpecProvider()
    cnpj = instance.cnpj()
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:33:53.287249
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert len(b.cpf()) == 14
    assert len(b.cpf(True)) == 14
    assert len(b.cpf(False)) == 11


# Generated at 2022-06-13 23:33:56.646848
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert isinstance(provider.cnpj(), str)


# Generated at 2022-06-13 23:34:01.434605
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():

    provider = BrazilSpecProvider()
    test_dict = {}
    for x in range(1,100):
        final_cnpj = provider.cnpj()
        test_dict[final_cnpj] = 1

    # If this fails it means that there were equal cnpj's generated
    assert len(test_dict) == 99


# Generated at 2022-06-13 23:34:02.608012
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    f = BrazilSpecProvider()
    assert f.cpf()


# Generated at 2022-06-13 23:34:06.878993
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 14 #para cpf com máscara
    assert len(provider.cpf(with_mask=False)) == 11 #para cpf sem máscara


# Generated at 2022-06-13 23:34:13.680056
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import random 
    brazilian = BrazilSpecProvider()

    cpfs = []
    for i in range(100):
        cpf = brazilian.cpf()
        assert len(cpf) == 14
        assert cpf not in cpfs
        cpfs.append(cpf)


# Generated at 2022-06-13 23:34:18.281496
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf_1 = provider.cpf()
    cpf_2 = provider.cpf()

    assert cpf_1 != cpf_2
    assert len(cpf_1) == 14
    assert len(cpf_2) == 14

    assert '.' in cpf_1
    assert '.' in cpf_2

    assert '-' in cpf_1
    assert '-' in cpf_2


# Generated at 2022-06-13 23:34:20.478028
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider()
    c = cpf.cpf()
    assert len(c) == 14
    print(c)


# Generated at 2022-06-13 23:37:33.930298
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender

    from tests.strategies import (
        strategies,
        seed_strategies,
    )
    from mimesis.builtins.br import BrazilSpecProvider

    seed_strategy = seed_strategies
    for seed in seed_strategy:
        for with_mask in strategies:
            provider = BrazilSpecProvider(seed)
            cnpj = provider.cnpj(with_mask)
            assert Provider.cnpj(cnpj) == cnpj
            # print(cnpj)


# Generated at 2022-06-13 23:37:36.588264
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf(with_mask=False)
    print(cpf)
    assert len(cpf) == 11


# Generated at 2022-06-13 23:37:38.203989
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bz = BrazilSpecProvider()
    assert bz.cnpj() != bz.cnpj()



# Generated at 2022-06-13 23:37:40.755355
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:37:42.604067
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    obj = BrazilSpecProvider()
    print(obj.cpf())


# Generated at 2022-06-13 23:37:45.957847
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider(seed=123456789)
    #print(bsp.cpf())

    # Unit test for method cnpj of class BrazilSpecProvider

# Generated at 2022-06-13 23:37:53.127084
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    cnpj = b.cnpj()
    print(cnpj)
    assert isinstance(cnpj, str)
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'
    assert cnpj[2:6] != '0000'
    assert cnpj[5:8] != '000'
    assert cnpj[8:12] != '0000'
    assert cnpj[12:16] != '0000'

# Generated at 2022-06-13 23:37:55.797415
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for BrazilSpecProvider-cpf."""
    bsp = BrazilSpecProvider(seed=12345)
    assert bsp.cpf(with_mask=False) == '00113729740'


# Generated at 2022-06-13 23:38:03.984242
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    result = BrazilSpecProvider().cpf(with_mask=True)
    assert len(result) == 14
    assert result.startswith('###')
    assert result.endswith('##')
    assert result.count('.') == 2
    assert result.count('-') == 1


# Generated at 2022-06-13 23:38:06.963761
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers import BrazilSpecProvider
    
    # Test 1: Verify the generated CNPJ by comparing it with a fixed CNPJ
    # Reference: https://www.4devs.com.br/gerador_de_cnpj
    provider = BrazilSpecProvider()
    assert provider.cnpj() == '77.732.230/0001-70'

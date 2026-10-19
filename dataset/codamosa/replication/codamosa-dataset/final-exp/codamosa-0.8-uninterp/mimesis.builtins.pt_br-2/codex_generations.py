

# Generated at 2022-06-13 23:28:35.441161
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    cnpj = brazil.cnpj()
    assert len(cnpj) == 14
    assert cnpj == '12.916.718/0001-01'

# Generated at 2022-06-13 23:28:48.001230
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf."""
    c = BrazilSpecProvider()
    
    # Test format of CPF
    assert c.cpf() == '910.574.469-49'
    assert c.cpf() == '279.871.741-60'
    assert c.cpf() == '136.348.133-49'
    assert c.cpf() == '943.946.225-80'
    
    # Test without mask
    assert c.cpf(with_mask=False) == '91057599476'
    assert c.cpf(with_mask=False) == '19458648651'
    assert c.cpf(with_mask=False) == '83226677224'
    assert c.cpf(with_mask=False) == '07455258098'



# Generated at 2022-06-13 23:28:50.329752
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    result = BrazilSpecProvider.cnpj(with_mask=True)
    assert len(result) == 18


# Generated at 2022-06-13 23:28:52.748228
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj(False) == BrazilSpecProvider().cnpj(False)
    assert BrazilSpecProvider().cnpj() == BrazilSpecProvider().cnpj()

# Generated at 2022-06-13 23:28:54.753432
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    _provider = BrazilSpecProvider()
    assert _provider.cpf() != '000.000.000-00'


# Generated at 2022-06-13 23:28:56.927182
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    cnpj = b.cnpj(with_mask=False)
    b.reset_seed()
    assert cnpj == b.cnpj(with_mask=False)


# Generated at 2022-06-13 23:29:04.040831
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    # if I did not remember, the test_contacts_data_provider.py
    # already tests the function cnpj().

    # Returns a str that has the format ###.###.###/##
    provider.cnpj()

    # Returns a str that has the format ###.###.###/##
    provider.cnpj(with_mask=True)



# Generated at 2022-06-13 23:29:06.065923
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf()
    assert BrazilSpecProvider().cpf(with_mask=False)


# Generated at 2022-06-13 23:29:10.929172
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    assert len(cnpj) == 18
    cnpj = BrazilSpecProvider().cnpj(with_mask = False)
    assert len(cnpj) == 14




# Generated at 2022-06-13 23:29:13.923722
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    assert (len(br.cpf()) == 14)


# Generated at 2022-06-13 23:29:22.524401
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    assert len(bsp.cnpj()) == 14

# Generated at 2022-06-13 23:29:25.809519
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Arrange
    provider = BrazilSpecProvider()
    # Act
    result = provider.cnpj()
    # Assert
    assert len(result) == 18



# Generated at 2022-06-13 23:29:30.738945
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bs = BrazilSpecProvider()
    cnpj = bs.cnpj()
    assert len(cnpj) == 18
    c = 0
    for i in cnpj:
        if i == ".":
            c += 1
    assert c == 2
    assert cnpj.find("/") != -1
    assert cnpj.find("-") != -1



# Generated at 2022-06-13 23:29:39.857145
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bz = BrazilSpecProvider()
    cnpj = bz.cnpj()
    lcnpj = [int(i) for i in cnpj if i.isdigit()]
    peso = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i, _ in enumerate(lcnpj):
        soma += peso[i] * lcnpj[i]
    resto = soma % 11
    assert(resto == 0 or resto == 1 or resto >= 11)


# Generated at 2022-06-13 23:29:51.278052
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    bp = BrazilSpecProvider()
    p = Person('pt-br', seed=42)
    str_cpf = bp.cpf()
    assert bp.cpf_masked == str_cpf == '560.687.538-97'
    str_cpf = bp.cpf(with_mask=False)
    assert str_cpf == '56068753897'
    p.use_gender(Gender.MALE)
    assert p.cpf() == '560.687.538-97'
    p.use_gender(Gender.FEMALE)
    assert p.cpf() == '560.687.538-97'


# Generated at 2022-06-13 23:29:55.814886
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import re

    assert re.match('[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}$', BrazilSpecProvider().cnpj(with_mask=True))



# Generated at 2022-06-13 23:30:03.928239
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    from mimesis.providers.brazil.brazil_provider import BrazilSpecProvider
    brazil_provider = BrazilSpecProvider()
    cnpj = brazil_provider.cnpj(with_mask=False)
    assert len(cnpj) == 14



# Generated at 2022-06-13 23:30:06.812467
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider(seed=1)
    cpf = provider.cpf()
    assert cpf == '718.918.654-77'


# Generated at 2022-06-13 23:30:09.165102
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazilprovider = BrazilSpecProvider()
    cnpj = brazilprovider.cnpj()
    assert cnpj

# Generated at 2022-06-13 23:30:11.493134
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider.cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:30:20.547289
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    prov = BrazilSpecProvider()
    for i in range(10):
        print(prov.cnpj())

# Generated at 2022-06-13 23:30:29.283785
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import unittest

    class CpfTestCase(unittest.TestCase):
        def setUp(self):
            self.cpf = BrazilSpecProvider().cpf()

        def test_cpf_with_mask(self):
            expected = self.cpf[3] == '.' and \
                       self.cpf[7] == '.' and \
                       self.cpf[11] == '-' and \
                       len(self.cpf) == 14
            self.assertTrue(
                expected,
                msg='cpf without mask expected. '
                    'Example: 001.137.297-40. Invalid value: ' + self.cpf
            )

        def test_cpf_without_mask(self):
            cpf_without_mask = BrazilSpecProvider().cpf(False)

# Generated at 2022-06-13 23:30:40.290199
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    r = BrazilSpecProvider(seed=0)
    assert r.cnpj() == '77.732.230/0001-70'
    assert r.cnpj(with_mask=False) == '77732230000170'
    r.seed(0)
    assert r.cnpj() == '77.732.230/0001-70'
    assert r.cnpj(with_mask=False) == '77732230000170'
    r.seed(1)
    assert r.cnpj() == '00.852.711/0001-06'
    assert r.cnpj(with_mask=False) == '00852711000106'
    r.seed(2)
    assert r.cnpj() == '80.063.513/0001-90'

# Generated at 2022-06-13 23:30:44.901556
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert (
        len(cpf) == 14 and
        cpf[3] == '.' and
        cpf[7] == '.' and
        cpf[11] == '-'
    )


# Generated at 2022-06-13 23:30:48.943555
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for the method cpf of class BrazilSpecProvider."""
    brazil = BrazilSpecProvider()
    cpf = brazil.cpf(with_mask=False)
    assert len(cpf) == 11


# Generated at 2022-06-13 23:30:52.550393
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    if provider.validate_cpf(cpf):
        return True
    else:
        return False


# Generated at 2022-06-13 23:31:01.027765
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    "Unit test for method cnpj of class BrazilSpecProvider"
    resultado = BrazilSpecProvider.cnpj()
    assert len(resultado) == 18
    lista = [int(i) for i in resultado if i.isdigit()]
    assert len(lista) == 14
    assert int(lista[0]) <3
    assert int(lista[1]) <  10
    assert int(lista[2]) <  10
    assert int(lista[3]) <  10
    assert int(lista[4]) <  10
    assert int(lista[5]) <10
    assert int(lista[6]) <10
    assert int(lista[7]) <10
    assert int(lista[8]) <10
    assert int(lista[9]) <10
    assert int

# Generated at 2022-06-13 23:31:05.775865
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
    result = brazil_provider.cpf()

    # Check if the result lenght is 11
    assert len(result) == 11

    # Check if the result is a cpf
    assert result == '001.137.297-40'


# Generated at 2022-06-13 23:31:17.753648
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Creates instance of BrazilSpecProvider
    brazil = BrazilSpecProvider()

    # Check if method cpf of class BrazilSpecProvider
    # return only string
    assert isinstance(brazil.cpf(), str)

    # Check if method cpf of class BrazilSpecProvider
    # return string with 11 characters
    assert len(brazil.cpf()) == 11

    # Check if method cpf of class BrazilSpecProvider
    # return string with characters of numbers or dots
    assert brazil.cpf().replace(".", "").isnumeric() == True

    # Check if method cpf of class BrazilSpecProvider
    # return string with 11 characters and dots
    assert len(brazil.cpf(with_mask=False)) == 11



# Generated at 2022-06-13 23:31:21.238578
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf."""
    provider = BrazilSpecProvider()
    assert provider.cpf() == '002.629.298-12'


# Generated at 2022-06-13 23:31:40.859563
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import re
    a = BrazilSpecProvider()
    b = a.cnpj(True)
    assert re.match(r"\d{2}.\d{3}.\d{3}/\d{4}-\d{2}", b)


# Generated at 2022-06-13 23:31:45.259571
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    with_mask = True
    bsp = BrazilSpecProvider()
    assert len(bsp.cpf(with_mask)) == 14
    assert bsp.cpf(with_mask)[3] == '.'
    assert bsp.cpf(with_mask)[7] == '.'
    assert bsp.cpf(with_mask)[11] == '-'
    with_mask = False
    assert len(bsp.cpf(with_mask)) == 11

# Generated at 2022-06-13 23:31:51.381747
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider"""
    brazil_provider = BrazilSpecProvider()
    cpf = brazil_provider.cpf()
    assert cpf[-2] == '-'
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert len(cpf) == 14


# Generated at 2022-06-13 23:31:56.145203
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj(False) == '7773223000170'
    assert len(provider.cnpj()) == 18
    assert provider.cnpj() == provider.cnpj(True)



# Generated at 2022-06-13 23:32:04.137958
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    from mimesis.enums import Gender, PersonalTitle
    from mimesis.providers.person import Person
    from mimesis.builtins import RussiaSpecProvider


    seed = RussiaSpecProvider().random.randint(1, 10000)
    # seed = 274
    br = BrazilSpecProvider(seed=seed)
    ru = RussiaSpecProvider(seed=seed)
    person = Person(seed=seed)
    person1 = Person(seed=seed+1)
    person2 = Person(seed=seed+2)
    print("seed = {}".format(seed))
    print("br.cnpj() = {}\n".format(br.cnpj()))
    print("ru.inn() = {}\n".format(ru.inn()))


# Generated at 2022-06-13 23:32:06.627405
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    assert len(br.cpf()) == 14


# Generated at 2022-06-13 23:32:09.290565
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf(with_mask=True) == provider.cpf(with_mask=False)


# Generated at 2022-06-13 23:32:11.388441
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    ob = BrazilSpecProvider()
    assert ob.cnpj() == '77.732.230/0001-70'

# Generated at 2022-06-13 23:32:17.609383
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    for bsp in BrazilSpecProvider():
        cnpj = bsp.cnpj(True)
        assert cnpj
        assert len(cnpj) == 18
        assert cnpj[2] == '.'
        assert cnpj[6] == '.'
        assert cnpj[10] == '/'
        assert cnpj[15] == '-'
        #print(cnpj)


# Generated at 2022-06-13 23:32:24.084714
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test the method BrazilSpecProvider.cpf."""
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert len(cpf) == 14
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1
    assert cpf.count('0') <= 3

    cpf = bsp.cpf(with_mask=False)
    assert len(cpf) == 11
    assert cpf.count('0') <= 3


# Generated at 2022-06-13 23:33:08.187366
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Test using BaseSpecProvider
    provider = BaseSpecProvider()
    cpf = provider.cpf()
    assert isinstance(cpf, str)
    # Test using BrazilSpecProvider
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert isinstance(cpf, str)


# Generated at 2022-06-13 23:33:14.314390
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf(with_mask=True)
    assert len(cpf) == 14
    assert len(provider._mask_cpf(cpf)) == 14
    assert provider.cpf(with_mask=False) == provider._unmask_cpf(cpf)


# Generated at 2022-06-13 23:33:21.846850
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    provider = BrazilSpecProvider(seed=12345678)
    assert provider.cpf() == '001.137.297-40'
    assert provider.cpf() == '001.137.297-40'
    assert provider.cpf(True) == '001.137.297-40'
    assert provider.cpf(False) == '00113729740'
    

# Generated at 2022-06-13 23:33:30.310241
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cpf = BrazilSpecProvider().cnpj()
    actual_mask = '{}.{}.{}-{}.{}'.format(cpf[0:2], cpf[3:3], cpf[5:5], cpf[8:8], cpf[12:])
    expected_mask = "##.###.###/####-##"

    assert actual_mask == expected_mask


# Generated at 2022-06-13 23:33:42.445431
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # This function tests that the BrazilSpecProvider.cnpj function generates
    # a properly formatted string.
    from . import BrazilSpecProvider
    from . import datetime
    from mimesis.builtins import Random
    from mimesis.registry import DataRegistry
    from mimesis.exceptions import NonEnumerableError
    assert datetime
    assert BrazilSpecProvider
    assert Random
    assert DataRegistry
    assert NonEnumerableError

    seed = datetime.datetime.now()
    bsp = BrazilSpecProvider(seed)
    assert isinstance(bsp, BrazilSpecProvider)
    assert bsp.cnpj(False) == bsp.cnpj()


# Generated at 2022-06-13 23:33:55.916542
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Given
    list_length = 1000
    brazil_spec_provider = BrazilSpecProvider()
    cnpj_with_mask = [brazil_spec_provider.cnpj() for i in range(list_length)]
    cnpj_only_numbers = [brazil_spec_provider.cnpj(with_mask=False) for i in range(list_length)]

    # When
    cnpj_with_mask_list = [True if """.-/""" in x else False for x in cnpj_with_mask]
    cnpj_only_numbers_list = [True if """.-/""" in x else False for x in cnpj_only_numbers]

    # Then
    assert True in cnpj_with_mask_list
    assert False in cnpj_only

# Generated at 2022-06-13 23:33:59.176687
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    br = BrazilSpecProvider()
    result = br.cnpj()
    assert isinstance(result, string)
    assert len(result) == 18


# Generated at 2022-06-13 23:34:00.597520
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    generator = BrazilSpecProvider()
    cpf_generated = generator.cpf()
    print(cpf_generated)


# Generated at 2022-06-13 23:34:03.781866
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    CPF = BrazilSpecProvider()
    # Create an iterable
    CPF_list = [CPF.cpf() for _ in range(1000)]

    # Check whether all elements in the iterable are unique
    assert len(CPF_list) == len(set(CPF_list))

    # Test cpf without mask
    assert CPF.cpf(with_mask=False) == '0113759297'


# Generated at 2022-06-13 23:34:08.179243
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf(False)
    assert len(cpf) == 11
    assert not '-' in cpf
    assert not '.' in cpf
    assert cpf.isdigit()


# Generated at 2022-06-13 23:35:50.367995
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    
    #Test without mask (default)
    result = bsp.cpf()
    assert result[0] != "0"
    assert result[1] != "0"
    assert result[2] != "0"
    assert len(result) == 11
    
    #Test with mask
    result = bsp.cpf(with_mask=True)
    assert result[0] != "0"
    assert result[1] != "0"
    assert result[2] != "0"
    assert len(result) == 14
    assert result[3] == "."
    assert result[7] == "."
    assert result[11] == "-"
    

# Generated at 2022-06-13 23:35:52.330408
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj(with_mask=False) == '775323000017'


# Generated at 2022-06-13 23:35:58.442499
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    
    from mimesis.providers.person.pt_br import BrazilSpecProvider
    from mimesis.builder import SeedBuilder
    from mimesis.enums import Gender
    from mimesis.providers.person.enums import MaritalStatus

    brazil = BrazilSpecProvider()
    sb = SeedBuilder()

    for i in range(0, 10):
        print('{} - CPF: {}'.format(i, brazil.cpf()))

    for i in range(0, 10):
        print('{} - CPF: {}'.format(i, brazil.cpf(with_mask=False)))


# Generated at 2022-06-13 23:36:02.419188
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    expected_cpf = '024.851.938-81'
    cpf = bsp.cpf()
    assert expected_cpf == cpf


# Generated at 2022-06-13 23:36:12.301486
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    print(cpf)

    assert len(cpf) == 14
    dv1 = int(cpf[10])
    dv2 = int(cpf[11])
    cpf = int(cpf[0:10])
    assert __calc_dv_cpf(cpf) == dv1 and __calc_dv_cpf(11 * str(cpf) + str(dv1)) == dv2


# Generated at 2022-06-13 23:36:14.920598
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bs = BrazilSpecProvider()
    bs.cpf()
    return True


# Generated at 2022-06-13 23:36:16.604813
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br_provider = BrazilSpecProvider()
    cpf = br_provider.cpf()
    print(cpf)


# Generated at 2022-06-13 23:36:39.208076
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Test if the result is from type str
    provider = BrazilSpecProvider()
    result = provider.cpf()
    assert isinstance(result, str) == True
    # Test if the result is from type str with mask
    provider = BrazilSpecProvider()
    result = provider.cpf(True)
    assert isinstance(result, str) == True
    # Test if the result is in the correct pattern
    provider = BrazilSpecProvider()
    result = provider.cpf(True)
    assert bool(re.match(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', result)) == True
    # Test if the result is in the correct pattern without mask
    provider = BrazilSpecProvider()
    result = provider.cpf()

# Generated at 2022-06-13 23:36:44.786401
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    t = BrazilSpecProvider()
    test = t.cpf()
    assert isinstance(test, str)
    assert len(test) == 14
    assert test[3] == "."
    assert test[7] == "."
    assert test[11] == "-"


# Generated at 2022-06-13 23:36:48.068741
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    if (bsp.cnpj(False, False) != bsp.cnpj(False, False)):
        assert False
    else:
        assert True


# Generated at 2022-06-13 23:28:35.362871
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    result = provider.cnpj(with_mask=True)
    assert result



# Generated at 2022-06-13 23:28:39.226728
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider(seed=42).cpf()
    assert cpf == '005.783.097-73'


# Generated at 2022-06-13 23:28:49.810416
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print('*'*30)
    print('Test method cnpj of class BrazilSpecProvider.')
    print('*'*30)
    x = BrazilSpecProvider()
    print('*'*30)
    print('Input with_mask=True')
    print('*'*30)
    for i in range(10):
        print(x.cnpj())
    print('*'*30)
    print('Input with_mask=False')
    print('*'*30)
    for i in range(10):
        print(x.cnpj(with_mask=False))
    #77.732.230/0001-70
    print('*'*30)
    print('Method cnpj of class BrazilSpecProvider finished with success.')
    print('*'*30)


# Generated at 2022-06-13 23:28:52.834697
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins.brazil import BrazilSpecProvider
    actual = BrazilSpecProvider().cpf()
    expected = '###.###.###-##'
    assert str(actual).match(expected)

# Generated at 2022-06-13 23:28:54.505159
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '010.625.222-42'


# Generated at 2022-06-13 23:29:01.163919
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('pt-br')
    gender = Gender.FEMALE
    cpf = person.cpf(gender)
    cpf_without_mask = person.cpf(gender, False)
    assert len(cpf) == 14
    assert len(cpf_without_mask) == 11
    assert cpf == cpf_without_mask[:3] + '.' + cpf_without_mask[3:6] + '.' + cpf_without_mask[6:9] + '-' + cpf_without_mask[9:]
    assert cpf_without_mask.isdigit()


# Generated at 2022-06-13 23:29:12.884065
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Validate data returned by method cnpj()."""
    # From example of https://github.com/modesto-angel/mimesis
    # Also stored on file brazil_cnpj_examples.txt

# Generated at 2022-06-13 23:29:15.345402
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert len(provider.cnpj(False)), 14

# Generated at 2022-06-13 23:29:20.905472
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    assert BrazilSpecProvider.Meta.name == 'brazil_provider'
    assert brazil.cnpj() is not None
    assert brazil.cnpj(with_mask=False) is not None



# Generated at 2022-06-13 23:29:27.141087
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test method cnpj of class BrazilSpecProvider."""
    bsp = BrazilSpecProvider()

    assert(bsp.cnpj() == '77.732.230/0001-70')
    assert(bsp.cnpj() == '77.732.230/0001-70')
    assert(bsp.cnpj() == '77.732.230/0001-70')



# Generated at 2022-06-13 23:29:34.985508
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() != BrazilSpecProvider().cpf()


# Generated at 2022-06-13 23:29:38.840690
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() == '128.923.162-02'
    assert provider.cpf(with_mask=False) == '12892316202'


# Generated at 2022-06-13 23:29:41.787065
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    assert brazil.cpf() == brazil.cpf(with_mask=False)


# Generated at 2022-06-13 23:29:45.437843
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:29:50.231417
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    result = provider.cpf()
    assert len(result) == 14
    assert result[3] == "."
    assert result[7] == "."
    assert result[11] == "-"


# Generated at 2022-06-13 23:29:52.749664
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj(with_mask=True) == "77.732.230/0001-70"


# Generated at 2022-06-13 23:29:57.075387
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """[summary]
    """
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert isinstance(cpf, str)
    assert len(cpf) == 14


# Generated at 2022-06-13 23:30:03.074394
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    method = BrazilSpecProvider(seed=42).cnpj
    assert method() == '77.732.230/0001-70'
    assert method(with_mask=False) == '77732230000170'
    assert method(with_mask=True) == method()


# Generated at 2022-06-13 23:30:04.605672
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert (provider.cpf())


# Generated at 2022-06-13 23:30:06.663953
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import doctest
    doctest.testmod(BrazilSpecProvider(BrazilSpecProvider(BrazilSpecProvider)))

# Generated at 2022-06-13 23:30:28.696597
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Test by random seeds
    provider = BrazilSpecProvider()
    for _ in range(20):
        cnpj = provider.cnpj()
        assert len(cnpj) == 18
        assert cnpj[2] == '.'
        assert cnpj[6] == '.'
        assert cnpj[10] == '/'
        assert cnpj[15] == '-'
    # Test with custom mask
    cnpj = provider.cnpj(True)
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'
    # Test without mask
    cnpj = provider.cnpj(False)

# Generated at 2022-06-13 23:30:33.862174
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    cnpj = brazil.cnpj()
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'

# Generated at 2022-06-13 23:30:42.747260
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method BrazilSpecProvider.cnpj."""
    brazil_spec_provider = BrazilSpecProvider()

    # EncodingTest
    cnpj_with_encoding = brazil_spec_provider.cnpj(with_mask=True)
    assert type(cnpj_with_encoding) == str

    # ConsectivesCharactersTest
    iter = 10000
    previous_cnpj_consectives = brazil_spec_provider.cnpj()
    for _ in range(iter):
        cnpj_consectives = brazil_spec_provider.cnpj()

# Generated at 2022-06-13 23:30:47.735060
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf_test = bsp.cpf()
    assert(len(cpf_test) == 14)
    assert(cpf_test.count('.') == 2)
    assert(cpf_test.count('-') == 1)


# Generated at 2022-06-13 23:30:49.532953
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:30:51.325675
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() == True


# Generated at 2022-06-13 23:31:00.240425
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil.person import BrazilSpecProvider as bsp
    brasil_provider = bsp(seed=1234)

    assert brasil_provider.cpf() == '161.740.058-61'
    assert brasil_provider.cpf() == '249.226.991-41'
    assert brasil_provider.cpf() == '188.657.945-50'
    assert brasil_provider.cpf() == '108.915.059-70'
    assert brasil_provider.cpf() == '019.961.307-00'
    assert brasil_provider.cpf() == '123.751.873-69'
    assert brasil_provider.cpf() == '084.720.591-50'

# Generated at 2022-06-13 23:31:10.326945
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj(): 
    brazil = BrazilSpecProvider()
    assert len(brazil.cnpj(False)) == 14
    assert len(brazil.cnpj()) == 18
    assert brazil.cnpj().count('.') == 2
    assert brazil.cnpj().count('/') == 1
    assert brazil.cnpj().count('-') == 1
    assert brazil.cnpj(False).count('.') == 0
    assert brazil.cnpj(False).count('/') == 0
    assert brazil.cnpj(False).count('-') == 0
    assert brazil.cnpj(with_mask=False) == brazil.cnpj(False)
    assert brazil.cnpj(with_mask=True) == brazil.cnpj()

# Generated at 2022-06-13 23:31:23.109392
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert(len(cnpj) == 18)
    with_mask = True
    cnpj_masked = bsp.cnpj(with_mask)
    assert(len(cnpj_masked) == 18)
    assert(cnpj_masked[2] == '.')
    assert(cnpj_masked[6] == '.')
    assert(cnpj_masked[10] == '/')
    assert(cnpj_masked[15] == '-')
    assert(cnpj_masked[0:2] == cnpj[0:2])
    assert(cnpj_masked[3:6] == cnpj[2:5])

# Generated at 2022-06-13 23:31:28.737225
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf1 = provider.cpf()
    if cpf1 == provider.cpf():
        print("Os cpfs sao iguais")
    else:
        print("Os cpfs nao sao iguais")

test_BrazilSpecProvider_cpf()



# Generated at 2022-06-13 23:31:56.485073
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp=BrazilSpecProvider()
    assert bsp.cpf() == '529.366.941-34'



# Generated at 2022-06-13 23:31:59.876125
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider"""
    provider = BrazilSpecProvider()
    assert provider.cnpj(with_mask=False) == '79654452000184'

# Generated at 2022-06-13 23:32:03.614245
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj_true = '77.732.230/0001-70'
    cnpj_false = '77.732.230-0001-70'
    cn = BrazilSpecProvider()
    for i in range(1000):
        assert cn.cnpj() == cnpj_true
    for i in range(1000):
        assert cn.cnpj(with_mask=False) != cnpj_false

# Generated at 2022-06-13 23:32:07.038237
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider(seed=123)
    cpf = brazil.cpf()
    assert cpf == '126.129.821-17'

# Generated at 2022-06-13 23:32:09.231865
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import doctest
    doctest.testmod(extraglobs={'br': BrazilSpecProvider()})


# Generated at 2022-06-13 23:32:12.654310
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print("----------test_BrazilSpecProvider_cpf()----------")
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    print(cpf)


# Generated at 2022-06-13 23:32:23.233926
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('pt-br')
    cpf_data = person.cpf(Gender.FEMALE)
    assert len(cpf_data) == 14
    assert cpf_data[3] == '.'
    assert cpf_data[7] == '.'
    assert cpf_data[11] == '-'

    cpf_data = person.cpf(Gender.MALE, with_mask=False)
    assert len(cpf_data) == 11
    assert cpf_data[3] != '.'
    assert cpf_data[7] != '.'
    assert cpf_data[11] != '-'


# Generated at 2022-06-13 23:32:26.447775
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    result = BrazilSpecProvider().cnpj()
    assert result != '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])



# Generated at 2022-06-13 23:32:31.433253
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method "cpf" of class "BrazilSpecProvider"."""
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert type(cpf) == str
    assert cpf == '291.355.019-90'


# Generated at 2022-06-13 23:32:35.013687
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Function to get a random CPF and test its mask."""
    assert len(BrazilSpecProvider().cpf()) == 14
    assert BrazilSpecProvider().cpf()[3] == '.'
    assert BrazilSpecProvider().cpf()[7] == '.'
    assert BrazilSpecProvider().cpf()[11] == '-'


# Generated at 2022-06-13 23:33:45.203544
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj().replace('.', '').replace('-', '').replace('/', '')
    assert len(cnpj) == 14
    assert int(cnpj[0]) == 2 or \
            int(cnpj[0]) == 3 or \
            int(cnpj[0]) == 5 or \
            int(cnpj[0]) == 6 or \
            int(cnpj[0]) == 7 or \
            int(cnpj[0]) == 8

# Generated at 2022-06-13 23:33:48.038719
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    brazil = BrazilSpecProvider()
    asse

# Generated at 2022-06-13 23:33:50.870627
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    result = b.cpf()
    print("result is :{}".format(result))


# Generated at 2022-06-13 23:34:02.996885
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    import pytest

    param_with_mask = [True, False]

    for mask in param_with_mask:
        provider = BrazilSpecProvider(seed=123456789)
        cnpj = provider.cnpj(with_mask=mask)
        assert len(cnpj) == 19 and cnpj[2] == '.' and cnpj[6] == '.'\
            and cnpj[10] == '/' and cnpj[15] == '-'

        cnpj = provider.cnpj(with_mask=mask)

# Generated at 2022-06-13 23:34:06.565894
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    b = BrazilSpecProvider()
    assert len(b.cnpj()) == 18
    assert len(b.cnpj(with_mask=False)) == 14


# Generated at 2022-06-13 23:34:14.702993
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    cpfs = [BrazilSpecProvider().cpf() for _ in range(10)]
    for cpf in cpfs:
        assert cpf[3] == '.'
        assert cpf[7] == '.'
        assert cpf[11] == '-'
        assert len(cpf) == 14



# Generated at 2022-06-13 23:34:19.284965
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()

    cpf_no_mask = []
    for i in range(100):
        cpf_no_mask.append(brazil_provider.cpf(with_mask=False))
    assert len(cpf_no_mask) == len(set(cpf_no_mask))

    cpf_mask = []
    for i in range(100):
        cpf_mask.append(brazil_provider.cpf(with_mask=True))
    assert len(cpf_mask) == len(set(cpf_mask))


# Generated at 2022-06-13 23:34:20.248789
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider.cpf


# Generated at 2022-06-13 23:34:29.237305
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider.
    """
    provider = BrazilSpecProvider()

    # First test
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'

    # Second test
    cpf = provider.cpf(with_mask=False)
    assert len(cpf) == 11
    # assert isinstance(cpf, int)

    # Third test
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'

    # Fourth test

# Generated at 2022-06-13 23:34:34.689050
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert len(set(cpf)) == 15



# Generated at 2022-06-13 23:37:44.580844
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    b = BrazilSpecProvider()
    assert len(b.cnpj()) == 14
    assert len(b.cnpj(with_mask=False)) == 12


# Generated at 2022-06-13 23:37:48.570655
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    provider = BrazilSpecProvider()
    assert provider.cpf() in ['69312112140', '59722383671', '51146454508']


# Generated at 2022-06-13 23:37:50.774571
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    print(cnpj)
    assert type(cnpj) == str


# Generated at 2022-06-13 23:38:03.984246
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brsp = BrazilSpecProvider()
    out = brsp.cnpj()
    print(out)
    assert out
    assert len(out) == 17
    assert out.count('.') == 2
    assert out.count('/') == 1
    assert out.count('-') == 1


# Generated at 2022-06-13 23:38:11.950628
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider.
    """
    locale_provider = BrazilSpecProvider()
    cpf = locale_provider.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf[0:3].isdigit()
    assert cpf[4:7].isdigit()
    assert cpf[8:11].isdigit()
    assert cpf[12:14].isdigit()


# Generated at 2022-06-13 23:38:14.559259
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 14
    assert len(provider.cpf(False)) == 11


# Generated at 2022-06-13 23:38:17.880686
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf(with_mask=True)
    assert cpf == "098.566.261-00"

if __name__ == "__main__":
    test_BrazilSpecProvider_cpf()

# Generated at 2022-06-13 23:38:20.285960
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj() == '12.804.335/0001-44'

# Generated at 2022-06-13 23:38:30.657720
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    #cpf_with_mask = BrazilSpecProvider().cpf()
    #print(cpf_with_mask)
    import unittest
    from mimesis.enums import Gender
    from mimesis.providers.identifiers import BrazilSpecProvider
    from mimesis.typing import Seed
    from mimesis.exceptions import NonEnumerableError

    class BrazilSpecProviderTestCase(unittest.TestCase):
        """Test case for the BrazilSpecProvider."""

        def setUp(self):
            """Setup the BrazilSpecProvider."""
            self.cpf = BrazilSpecProvider(seed=1)

        def test_cpf(self):
            """Should return a random CPF."""
            result = self.cpf.cpf()
            self.assertTrue(result)
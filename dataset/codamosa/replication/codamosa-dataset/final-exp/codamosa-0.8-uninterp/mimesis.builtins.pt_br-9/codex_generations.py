

# Generated at 2022-06-13 23:28:36.634090
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for method cnpj of class BrazilSpecProvider"""
    seed = '33500900000103'
    expected_cnpj = '33.500.900/0001-03'

    brazil_provider = BrazilSpecProvider(seed)
    cnpj = brazil_provider.cnpj(with_mask=True)

    assert cnpj == expected_cnpj

# Generated at 2022-06-13 23:28:39.217399
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    assert len(cnpj) == 18

# Generated at 2022-06-13 23:28:44.405566
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Method for testing the BrazilSpecProvider class' cnpj method."""
    print('Testing BrazilSpecProvider class\' cnpj method.')
    provider = BrazilSpecProvider()

    cnpj = provider.cnpj(with_mask=True)

    print('Here is a random CNPJ: ' + cnpj)


# Generated at 2022-06-13 23:28:46.752422
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider(seed=13)
    assert bsp.cpf() == '003.653.732-89'


# Generated at 2022-06-13 23:28:49.621372
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    tsp = BrazilSpecProvider()
    assert tsp.cpf()
    assert tsp.cpf(with_mask=False)


# Generated at 2022-06-13 23:28:54.794205
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis import BrazilSpecProvider as bsp
    from mimesis.enums import Gender
    from pprint import pprint

    bz = bsp()    
    # With mask
    print('CNPJ with mask')
    pprint(bz.cnpj())

    # Without mask
    print('CNPJ without mask')
    pprint(bz.cnpj(False))


# Generated at 2022-06-13 23:29:04.386341
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '020.947.112-06'
    assert BrazilSpecProvider().cpf() == '338.082.636-13'
    assert BrazilSpecProvider().cpf() == '347.411.814-68'
    assert BrazilSpecProvider().cpf() == '965.947.775-07'
    assert BrazilSpecProvider().cpf() == '888.420.452-76'
    assert BrazilSpecProvider().cpf() == '584.659.120-88'
    assert BrazilSpecProvider().cpf() == '336.914.713-23'
    assert BrazilSpecProvider().cpf() == '992.463.734-93'
    assert BrazilSpecProvider().cpf() == '414.599.054-17'

# Generated at 2022-06-13 23:29:13.429922
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method BrazilSpecProvider.cnpj(with_mask=True)."""
    bzprov = BrazilSpecProvider()
    cnpj = bzprov.cnpj()
    assert isinstance(cnpj, str)
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'
    assert cnpj[14] != '-'
    assert cnpj[-3:] != '000'



# Generated at 2022-06-13 23:29:18.521680
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert cnpj
    assert len(cnpj) == 18
    assert provider.cnpj(with_mask=True) == provider.cnpj(with_mask=False)


# Generated at 2022-06-13 23:29:23.668715
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.locale.pt_br.brazil import BrazilSpecProvider
    brazil = BrazilSpecProvider()
    print(brazil.cnpj())
    print(brazil.cnpj(with_mask=False))


# Generated at 2022-06-13 23:29:43.988351
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil import BrazilSpecProvider
    from random import seed

    seed(0)
    print(BrazilSpecProvider().cnpj())
    seed(0)
    print(BrazilSpecProvider().cnpj())
    seed(0)
    print(BrazilSpecProvider().cnpj())
    seed(0)
    print(BrazilSpecProvider().cnpj())
    seed(0)
    print(BrazilSpecProvider().cnpj())


# Generated at 2022-06-13 23:29:46.634975
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert len(BrazilSpecProvider().cnpj()) == 14
    assert BrazilSpecProvider().cnpj(with_mask=False) == BrazilSpecProvider().cnpj()


# Generated at 2022-06-13 23:29:53.711061
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test BrazilSpecProvider.cpf by hypothesis."""
    from hypothesis import given, assume, example
    from hypothesis.strategies import integers, text
    from mimesis.providers import BrazilSpecProvider
    from mimesis.enums import Gender

    @given(text())
    def test_cpf_with_mask(s):
        """Test cpf with mask."""
        cpf = BrazilSpecProvider(seed=s).cpf()
        assert cpf[3] == cpf[7] == '.'
        assert cpf[11] == '-'
        assert len(cpf) == 14
        assert cpf[:3].isdigit()
        assert cpf[4:7].isdigit()
        assert cpf[8:11].isdigit()
        assert cpf[12:].isdigit()



# Generated at 2022-06-13 23:29:57.779195
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    brf = BrazilSpecProvider()
    cnpj = brf.cnpj()
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:30:01.039249
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf_test = provider.cpf()
    assert len(cpf_test) == 14
    assert cpf_test[3] == "."
    assert cpf_test[7] == "."
    assert cpf_test[11] == "-"


# Generated at 2022-06-13 23:30:04.839070
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf(False)
    print(cpf)
    assert len(cpf) == 11


# Generated at 2022-06-13 23:30:07.415905
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    assert brazil.cpf() == '964.135.115-35'


# Generated at 2022-06-13 23:30:09.524420
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    obj = BrazilSpecProvider()
    cnpj = obj.cnpj()
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:30:11.462947
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print(BrazilSpecProvider().cnpj())
    print(BrazilSpecProvider().cnpj(1))


# Generated at 2022-06-13 23:30:18.247489
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method BrazilSpecProvider.cnpj."""
    provider = BrazilSpecProvider(seed=123)

    # Test default return without mask
    result = provider.cnpj(with_mask=False)
    assert isinstance(result, str)
    assert len(result) == 14
    assert result == '77732230000170'

    # Test default return with mask
    result = provider.cnpj(with_mask=True)
    assert isinstance(result, str)
    assert len(result) == 18
    assert result == '77.732.230/0001-70'

    # Always return the same valu with a seed
    provider = BrazilSpecProvider(seed=123)
    result = provider.cnpj()
    assert isinstance(result, str)
    assert len(result) == 18

# Generated at 2022-06-13 23:30:38.657075
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.data import BRAZIL
    from mimesis.enums import Gender

    g = Gender.MALE
    locale = 'pt-br'

    person = BRAZIL[locale].person(g)

    cpf = person.cpf()
    assert isinstance(cpf, str)
    assert len(cpf) == 14

    cpf = person.cpf(with_mask=False)
    assert isinstance(cpf, str)
    assert len(cpf) == 11

# Generated at 2022-06-13 23:30:42.308793
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil.brazil_spec import BrazilSpecProvider
    provider_cnpj = BrazilSpecProvider()
    provider_cnpj.cnpj()

# Generated at 2022-06-13 23:30:47.996669
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """
    Function to test the method cnpj of class BrazilSpecProvider
    """
    print('Testing method cnpj of class BrazilSpecProvider')
    provider = BrazilSpecProvider()
    assert len(provider.cnpj(True)) == 18
    assert len(provider.cnpj(False)) == 14


# Generated at 2022-06-13 23:30:49.821329
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '071.960.064-33'


# Generated at 2022-06-13 23:30:56.543669
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj(False)
    assert len(cnpj) == 14
    cnpj = provider.cnpj()
    pattern = re.compile('[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}')
    assert pattern.match(cnpj)
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:31:03.436151
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    prov = BrazilSpecProvider()

    # Test if the returned value is a string
    cpf = prov.cpf()
    assert isinstance(cpf, str)

    # Test if the returned value is a string
    cpf_with_mask = prov.cpf(with_mask=True)
    assert isinstance(cpf_with_mask, str)

    # Test if the returned value has the correct length
    assert len(cpf) == 11
    assert len(cpf_with_mask) == 14

    # Test if the returned value respect the CPF pattern
    assert cpf_with_mask[3] == '.'
    assert cpf_with_mask[7] == '.'
    assert cpf_with_mask[-3] == '-'

    # Test if the returned value is unique
    unique = set()
    unique

# Generated at 2022-06-13 23:31:05.113116
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:31:07.253479
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    obj = BrazilSpecProvider()
    cnpj = obj.cnpj() #random cnpj
    assert True

# Generated at 2022-06-13 23:31:09.989488
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    loc = BrazilSpecProvider()
    print("BrazilSpecProvider.cnpj():", loc.cnpj(with_mask=True))


# Generated at 2022-06-13 23:31:12.845779
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bz = BrazilSpecProvider()
    assert len(bz.cnpj()) == 19


# Generated at 2022-06-13 23:31:43.889203
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test for method cpf of class BrazilSpecProvider."""
    # Test sort list method with
    # sort_method=insertion_sort and sort_order=descending
    from mimesis.enums import SortOrder

    brazil_provider = BrazilSpecProvider()

    cpf = brazil_provider.cpf(with_mask=True)
    print('cpf:',cpf,'\n')

test_BrazilSpecProvider_cpf()


# Generated at 2022-06-13 23:31:47.151313
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    assert(bsp.cnpj() == '53.717.521/0001-54')


# Generated at 2022-06-13 23:31:50.303463
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert isinstance(cpf, str)
    assert len(cpf) == 14
    assert cpf[3] == '.'

# Generated at 2022-06-13 23:31:58.126029
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import re
    import unittest
    from mimesis.builtins.brazil import BrazilSpecProvider
    class CPFSpec(unittest.TestCase):
        """
        Unit test for method cpf of class BrazilSpecProvider
        """
        def test_cpf_masked(self):
            """
            tests of cpf method with mask
            """
            # instantiate the BrazilSpecProvider class
            cpf = BrazilSpecProvider()
            # testing the cpf method
            self.assertTrue(re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf.cpf()))

        def test_cpf_not_masked(self):
            """
            tests of cpf method with mask
            """
            # instantiate the BrazilSpecProvider class
           

# Generated at 2022-06-13 23:32:00.955837
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    print(BrazilSpecProvider().cnpj())
    print(BrazilSpecProvider().cnpj(with_mask=True))


# Generated at 2022-06-13 23:32:03.872025
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    spec = BrazilSpecProvider()
    assert len(spec.cnpj()) == 14
    assert len(spec.cnpj(with_mask=False)) == 14

# Generated at 2022-06-13 23:32:16.152189
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from unittest import TestCase
    from mimesis.enums import Gender
    
    class TestBrazilSpecProvider(TestCase):
        def test_cpf(self):
            bsp = BrazilSpecProvider()
            
            self.assertEqual(10, len(bsp.cpf()))
            self.assertEqual(14, len(bsp.cpf(with_mask=True)))
            self.assertEqual(bsp.cpf(with_mask=False), bsp.cpf(with_mask=True).replace('.','').replace('-',''))
                
    test = TestBrazilSpecProvider()
    test.test_cpf()

if __name__ == '__main__':
    print('Testing...')
    test_BrazilSpecProvider_cpf()
    print('Test finished!')

# Generated at 2022-06-13 23:32:25.622453
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()

    cnpj = provider.cnpj()
    assert len(cnpj) == 18
    assert cnpj[2:3] == '.'
    assert cnpj[6:7] == '.'
    assert cnpj[10:11] == '/'
    assert cnpj[15:16] == '-'
    assert cnpj[2:6] is not None
    assert cnpj[6:10] is not None
    assert cnpj[10:15] is not None
    assert cnpj[15:] is not None
    assert cnpj[:2] is not None
    assert cnpj[:2] is not None
    assert cnpj[:2] is not None
    assert cnpj[:2] is not None

# Generated at 2022-06-13 23:32:28.265710
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bs = BrazilSpecProvider(seed=1)
    assert bs.cnpj() == '77.732.230/0001-70'

# Generated at 2022-06-13 23:32:31.433175
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18

# Generated at 2022-06-13 23:33:41.010231
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider.Meta.name
    cnpj = '945.079.841/0001-96'
    assert brazil.cnpj() == cnpj


# Generated at 2022-06-13 23:33:43.940368
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert len(BrazilSpecProvider().cnpj()) == 14
    assert BrazilSpecProvider().cnpj().find('.') == 2
    assert BrazilSpecProvider().cnpj().find('/') == 6
    assert BrazilSpecProvider().cnpj().find('-') == 12



# Generated at 2022-06-13 23:33:47.366062
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf(): 
    brazil_provider = BrazilSpecProvider()
    print(brazil_provider.cpf())
    print(brazil_provider.cpf(False))


# Generated at 2022-06-13 23:33:50.205070
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_spec = BrazilSpecProvider()

    cpf = brazil_spec.cpf()
    assert cpf is not None


# Generated at 2022-06-13 23:33:57.749411
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf[:9].isdigit()
    assert cpf[-2:].isdigit()
    assert cpf[9] == '-'
    assert cpf[3] == '.'
    assert cpf[7] == '.'


# Generated at 2022-06-13 23:34:00.438489
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj1 = provider.cnpj()
    cnpj2 = provider.cnpj()
    assert cnpj1 != cnpj2

# Generated at 2022-06-13 23:34:07.060218
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = BrazilSpecProvider()
    cpf = p.cpf()
    p2 = Person('pt')
    p2.gender = Gender.MALE
    person = p2.full_name()

    assert isinstance(cpf, str), f"Expected <class 'str'>, got {type(cpf)}"
    assert cpf == "474.632.268-62", \
        f"Expected '474.632.268-62', got {cpf}"
    assert len(cpf) == 14, f"Expected 14, got {len(cpf)}"
    assert isinstance(person, str), \
        f"Expected <class 'str'>, got {type(person)}"

# Generated at 2022-06-13 23:34:13.128828
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Testing the method BrazilSpecProvider.cpf."""
    assert BrazilSpecProvider().cpf() == '947.648.593-74'
    assert BrazilSpecProvider().cpf(with_mask=False) == '94764859374'


# Generated at 2022-06-13 23:34:17.001277
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for BrazilSpecProvider.cnpj()."""
    bt = BrazilSpecProvider()
    cnpj = bt.cnpj()

    # test the format of CNPJ: 99.999.999/9999-99
    assert len(cnpj) == 18



# Generated at 2022-06-13 23:34:25.381510
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.data import BR_PROVINCE_CODES
    from mimesis.providers.misc import Miscellaneous
    from mimesis.providers.datetime import Datetime
    cnpj = Miscellaneous('pt-br').cnpj()
    assert len(cnpj) == 18
    assert cnpj[0:2] in BR_PROVINCE_CODES
    assert cnpj[13:15] == Datetime('pt-br').century()
    assert cnpj.count('.') == 2
    assert cnpj.count('-') == 1
    assert cnpj.count('/') == 1

# Generated at 2022-06-13 23:37:37.680011
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """
    Test method cpf of class BrazilSpecProvider
    """
    # Test type of return
    bp = BrazilSpecProvider()
    result = bp.cpf()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:37:41.498320
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    a = BrazilSpecProvider()
    b = a.cnpj()
    print(len(b))


if __name__ == '__main__':
    test_BrazilSpecProvider_cnpj()

# Generated at 2022-06-13 23:37:47.424127
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    br = BrazilSpecProvider()
    p = Person('pt-br')
    for _ in range(20):
        print(p.cnpj(with_mask=True))
        #print(br.cnpj(with_mask=True))



# Generated at 2022-06-13 23:37:51.922923
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider"""
    brazil = BrazilSpecProvider()
    assert brazil.cnpj() == '91.670.444/0001-41'


# Generated at 2022-06-13 23:38:03.984255
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test the method cpf of class BrazilSpecProvider."""
    brazil_provider = BrazilSpecProvider()
    result = brazil_provider.cpf()

    assert isinstance(result, str)
    assert len(result) == 14
    assert result[3] == '.'
    assert result[7] == '.'
    assert result[11] == '-'


# Generated at 2022-06-13 23:38:06.284336
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    obj = BrazilSpecProvider()
    cpf = obj.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:38:07.784751
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert len(b.cpf()) == 14


# Generated at 2022-06-13 23:38:09.396631
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert len(b.cpf()) == 14


# Generated at 2022-06-13 23:38:19.069088
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender
    from mimesis.providers.generic import Provider
    provider = Provider()
    agender = provider.person.get(gender=Gender.FEMALE, locale='pt-br')
    bgender = provider.person.get(gender=Gender.MALE, locale='pt-br')
    cpf = provider.brazil.cpf()
    cnpj = provider.brazil.cnpj()
    print('Nome:', ' '.join([agender.title(), agender.last_name()]))
    print('CPF:', cpf)
    print('Nome:', ' '.join([bgender.title(), bgender.last_name()]))
    print('CNPJ:', cnpj)
    assert 11 == len(cpf.replace('.','',3))

# Generated at 2022-06-13 23:38:24.884647
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """This function tests method cnpj of class BrazilSpecProvider"""
    instance = BrazilSpecProvider()
    cnpj1 = instance.cnpj()
    cnpj2 = instance.cnpj(with_mask=False)

    assert len(cnpj1) == 18
    assert len(cnpj2) == 14

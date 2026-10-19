

# Generated at 2022-06-13 23:28:34.519478
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    print(bsp.cpf())

# Generated at 2022-06-13 23:28:36.669898
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    BSP = BrazilSpecProvider()
    assert len(BSP.cpf()) == 14
    assert len(BSP.cpf(False)) == 11


# Generated at 2022-06-13 23:28:40.528796
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj() == '18.764.461/0001-03'
    assert BrazilSpecProvider().cnpj(with_mask=False) == '18764461000103'

# Generated at 2022-06-13 23:28:48.919430
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider(seed = 123)
    p = b.cpf()
    assert str(p) == "012.345.678-90"
    p = b.cpf()
    assert str(p) == "123.456.789-01"
    p = b.cpf()
    assert str(p) == "234.567.890-12"
    p = b.cpf()
    assert str(p) == "345.678.901-23"
    p = b.cpf()
    assert str(p) == "456.789.012-34"


# Generated at 2022-06-13 23:28:54.145109
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Setup
    provider = BrazilSpecProvider()
    # Exercise
    t = provider.cnpj()
    # Verify
    assert isinstance(t, str)
    assert len(t) == 14
    assert t[2:3] == '.'
    assert t[6:7] == '.'
    assert t[10:11] == '/'
    assert t[15:16] == '-'


# Generated at 2022-06-13 23:28:57.563317
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for class BrazilSpecProvider method cpf."""
    brazil_provider = BrazilSpecProvider(seed=20001)
#    print(brazil_provider.cpf())
    assert brazil_provider.cpf() == '536.406.076-18'


# Generated at 2022-06-13 23:29:03.753852
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    sp = BrazilSpecProvider()
    cpf = sp.cpf(with_mask=False)
    assert len(cpf) == 11
    cpf = sp.cpf(with_mask=True)
    assert len(cpf) == 14


# Generated at 2022-06-13 23:29:14.572136
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test for method cnpj of class BrazilSpecProvider."""
    from mimesis.random import Random
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    import re

    seed = 12345
    random_ = Random(seed=seed)
    bsp = BrazilSpecProvider(seed)

    cnpj_1 = bsp.cnpj()
    cnpj_2 = bsp.cnpj()

    # cnpj should be of the form
    # nnn.nnn.nnn/nnnn-nn
    # where n is an integer 0-9
    assert re.match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj_1)

# Generated at 2022-06-13 23:29:20.306733
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:29:22.773987
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == "709.535.886-90"


# Generated at 2022-06-13 23:29:36.993325
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person('pt-br')
    p.seed(0)
    assert p.cnpj() == '11.035.307/0001-32'
    assert p.cnpj(with_mask=False) == '11035307000132'


# Generated at 2022-06-13 23:29:39.423544
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert len(b.cpf()) == 14


# Generated at 2022-06-13 23:29:41.215577
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    print(b.cpf())


# Generated at 2022-06-13 23:29:52.664884
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import random
    import unittest

    def get_verifying_digit_cnpj(cnpj, peso):
        """Calculate the verifying digit for the CNPJ.

        :param cnpj: List of integers with the CNPJ.
        :param peso: Integer with the weight for the modulo 11 calculate.
        :returns: The verifying digit for the CNPJ.
        """
        soma = 0
        if peso == 5:
            peso_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        elif peso == 6:
            peso_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

# Generated at 2022-06-13 23:30:02.804472
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import json
    import pytest
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    expected_cnpj = '84.465.936/0001-50'
    person = Person('pt-br')
    #Inicializa o objeto de teste e o objeto esperado
    test_obj = BrazilSpecProvider() 
    test_obj.cnpj() #Inicia o metódo que será testado
    cnpj_result = person.cnpj(with_mask=True) #Pega o resultado da funcao alvo
    assert cnpj_result == expected_cnpj #Verifica se o resultado é o esperado


# Generated at 2022-06-13 23:30:05.118544
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bp = BrazilSpecProvider()
    for i in range(10):
        print(bp.cpf(True))


# Generated at 2022-06-13 23:30:12.430094
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import BrazilSpecProvider
    from mimesis.enums import Gender
    from mimesis.enums import Currency
    from mimesis.enums import Country
    from mimesis.enums import Language
    from mimesis.enums import Profession
    from mimesis.enums import PaymentSystem
    from mimesis.enums import PaymentMethod
    from mimesis.enums import InternetProtocol

    provider = BrazilSpecProvider()
    assert provider.cpf() == provider.cpf()

# Generated at 2022-06-13 23:30:18.736858
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import BrazilSpecProvider, locales, Seed
    from mimesis.builtins import RandomCode
    from mimesis.data import CPF as CPFData
    from mimesis.enums import CodeType
    from mimesis.exceptions import NonEnumerableError
    from mimesis.typing import DataField
    from mimesis.providers.base import BaseDataProvider

    ###########################################################################
    #                   TEST FOR __init__()                                   #
    ###########################################################################
    assert isinstance(BrazilSpecProvider(), BrazilSpecProvider)
    assert BrazilSpecProvider().locale == 'pt-br'
    assert BrazilSpecProvider._meta.name == 'brazil_provider'
    assert BrazilSpecProvider().__module__ == 'mimesis.providers.pt-br'
    ###########################################################################


# Generated at 2022-06-13 23:30:24.917148
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 14
    assert len(provider.cpf(with_mask=False)) == 11
    # Test multiple cpfs to ensure the randomness
    cpfs = [provider.cpf() for _ in range(2)]
    assert len(cpfs) == len(set(cpfs))



# Generated at 2022-06-13 23:30:27.595178
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil import BrazilSpecProvider
    brazil_provider = BrazilSpecProvider('en')
    assert len(brazil_provider.cpf()) == 14


# Generated at 2022-06-13 23:30:44.661820
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    result = provider.cpf(True)
    assert result
    print("test_BrazilSpecProvider_cpf = " + result)


# Generated at 2022-06-13 23:30:47.831756
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for method cnpj of BrazilSpecProvider."""
    brazil = BrazilSpecProvider()
    print(brazil.cnpj())


# Generated at 2022-06-13 23:30:52.213188
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf1 = bsp.cpf()
    cpf2 = bsp.cpf()
    assert len(cpf1) == 14
    assert len(cpf2) == 14
    assert cpf1 != cpf2


# Generated at 2022-06-13 23:30:55.076193
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider(seed=1)
    cpf = b.cpf()
    print(cpf)
    assert cpf == '179.672.051-55'


# Generated at 2022-06-13 23:30:56.624004
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    print(bsp.cpf(False))


# Generated at 2022-06-13 23:30:59.064235
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from .mimesis_tests import BrazilSpecProviderTestCase

    test_case = BrazilSpecProviderTestCase('test_BrazilSpecProvider_cnpj')
    test_case.run()


# Generated at 2022-06-13 23:31:01.866121
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    gen = BrazilSpecProvider()
    assert len(gen.cpf(with_mask = False)) == 11

# Generated at 2022-06-13 23:31:03.093966
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazilSpecProvider = BrazilSpecProvider()
    brazilSpecProvider.cpf(with_mask=True)
    

# Generated at 2022-06-13 23:31:06.830809
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'

# Generated at 2022-06-13 23:31:13.685533
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test for BrazilSpecProvider.cpf()"""

    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert isinstance(cpf, str)
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:31:44.657479
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    # Build provider
    bsp = BrazilSpecProvider()
    # Build cnpj: a number consisting of 14 digits
    cnpj = bsp.cnpj(with_mask=False)
    assert cnpj.isdigit()
    assert len(cnpj) == 14
    print(cnpj)


# Generated at 2022-06-13 23:31:48.080869
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider_br = BrazilSpecProvider()
    cnpj_sample = provider_br.cnpj()
    print(cnpj_sample)
    assert True


# Generated at 2022-06-13 23:31:52.617178
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj1 = provider.cnpj()
    cnpj2 = provider.cnpj(with_mask=False)
    assert cnpj1 == cnpj2
    assert len(cnpj1) == 18


# Generated at 2022-06-13 23:31:55.984966
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    cpf = brazil.cpf()
    assert brazil.validate_cpf(cpf) is True


# Generated at 2022-06-13 23:31:59.225969
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj_value = BrazilSpecProvider(seed=42).cnpj()
    assert cnpj_value == '03.297.366/0001-68'


# Generated at 2022-06-13 23:32:11.509563
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method."""
    from mimesis.providers.datetime import Datetime
    import datetime

    datetime = Datetime('pt-br')
    date = datetime.date(datetime.now().year)
    assert date.month < 10

    brazil = BrazilSpecProvider()
    cnpj = brazil.cnpj(with_mask=False)
    cnpj_list = [int(i) for i in cnpj]
    cnpj_list, cnpj_list[0] = cnpj_list[0], 0
    cnpj_list0 = [int(i) for i in cnpj_list]
    cnpj_without_dv = cnpj_list0[:12]

    first_dv = brazil.get_verifying_digit_cnp

# Generated at 2022-06-13 23:32:13.243665
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    print(cnpj)
    

# Generated at 2022-06-13 23:32:15.574198
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj(True)
    assert len(cnpj) == 18

# Generated at 2022-06-13 23:32:17.984457
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    assert len(bsp.cnpj().replace('.', '').replace('-', '').replace('/', '')) == 14

# Generated at 2022-06-13 23:32:21.778510
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    br = BrazilSpecProvider()
    assert type(br.cnpj()) == str
    assert len(br.cnpj()) == 18
    assert br.cnpj(with_mask=True) == br.cnpj()


# Generated at 2022-06-13 23:33:43.600391
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Test 1
    from mimesis.providers import BrazilSpecProvider
    brazil = BrazilSpecProvider()
    cnpj = brazil.cnpj()
    print(cnpj)
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'

    # Test 2
    from mimesis.providers import BrazilSpecProvider
    brazil = BrazilSpecProvider()
    cnpj = brazil.cnpj(False)
    print(cnpj)
    assert len(cnpj) == 14
    assert cnpj[2] != '.'
    assert cnpj[6] != '.'

# Generated at 2022-06-13 23:33:47.549588
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """
    Test for BrazilSpecProvider
    """
    try:
        b = BrazilSpecProvider()
        b.cnpj()
        assert True
    except:
        assert False


# Generated at 2022-06-13 23:33:51.819864
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf[3] == cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:33:56.775796
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    braz = BrazilSpecProvider()
    cnpj = braz.cnpj(False)

    assert len(cnpj) == 14
    assert cnpj.isdigit()



# Generated at 2022-06-13 23:33:59.418778
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    actual = BrazilSpecProvider.cnpj
    expected = '46825282000110'
    assert actual() == expected


# Generated at 2022-06-13 23:34:01.973573
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test BrazilSpecProvider class method cnpj."""
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:34:03.690306
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert isinstance(cpf,str)
    assert len(cpf) == 14


# Generated at 2022-06-13 23:34:07.375608
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():

    bsp = BrazilSpecProvider()

    assert bsp.cnpj() == '77.732.230/0001-70'
    assert bsp.cnpj(with_mask=False) == '77732230000170'



# Generated at 2022-06-13 23:34:12.391102
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    p = BrazilSpecProvider()
    cpf = p.cpf()
    assert(len(cpf) == 14)
    assert(cpf == '538.876.983-56')


# Generated at 2022-06-13 23:34:14.200015
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert len(provider.cnpj()) == 18


# Generated at 2022-06-13 23:37:37.269443
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method BrazilSpecProvider.cpf()."""
    # test with True (boolean)
    provider = BrazilSpecProvider()
    assert isinstance(provider.cpf(True), str)
    assert provider.cpf(True).__len__() == 14

    # test with False (boolean)
    assert isinstance(provider.cpf(False), str)
    assert provider.cpf(False).__len__() == 11
    assert provider.cpf(True) != provider.cpf(False)


# Generated at 2022-06-13 23:37:40.235580
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    provider = BrazilSpecProvider()
    assert provider.cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:37:46.723381
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():

    '''
    Description:  This function is used to test the method cpf of class BrazilSpecProvider.
    Param: no
    Return:no
    Author: YuanYang
    Date: 2020-08-25
    '''

    brazil_provider = BrazilSpecProvider()
    print(brazil_provider.cpf())


# Generated at 2022-06-13 23:37:51.839188
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    r = provider.cpf()
    assert r.__class__ == str
    assert len(r) == 14
    assert type(r) == str
    assert r[3] == '.'



# Generated at 2022-06-13 23:38:03.984246
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'


# Generated at 2022-06-13 23:38:06.108926
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    print(cpf)


# Generated at 2022-06-13 23:38:08.251231
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil_spec_provider = BrazilSpecProvider()
    a_cnpj = brazil_spec_provider.cnpj()
    assert len(a_cnpj) == 14

# Generated at 2022-06-13 23:38:15.116729
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test cpf method of BrasilSpecProvider class."""
    from mimesis.providers.brasil.brazil import BrazilSpecProvider

    provider = BrazilSpecProvider()
    result = provider.cpf()
    assert result
    assert len(result) == 14
    assert result.count('.') == 2
    assert result.count('-') == 1
    assert result[3] == '.'
    assert result[7] == '.'
    assert result[11] == '-'


# Generated at 2022-06-13 23:38:17.073325
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test cpf method."""

    b = BrazilSpecProvider()
    assert len(b.cpf(True)) == 14



# Generated at 2022-06-13 23:38:18.562156
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil import BrazilSpecProvider
    BrazilSpecProvider.cpf()

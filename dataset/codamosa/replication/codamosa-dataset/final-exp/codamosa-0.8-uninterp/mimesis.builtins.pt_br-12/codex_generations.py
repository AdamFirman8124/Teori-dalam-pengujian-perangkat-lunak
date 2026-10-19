

# Generated at 2022-06-13 23:28:36.000420
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.providers.brazil_provider import BrazilSpecProvider
    from mimesis.enums import Gender
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:28:42.591687
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    brazilSpecProvider = BrazilSpecProvider()

    for _ in range(1000):
        assert len(brazilSpecProvider.cpf(False)) == 11
        assert len(brazilSpecProvider.cpf(True)) == 14
        assert isinstance(brazilSpecProvider.cpf(True), str)



# Generated at 2022-06-13 23:28:48.622343
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1
    assert cpf.count('_') == 0


# Generated at 2022-06-13 23:28:50.933831
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    BrazilSpecProvider().cpf()
    """
    '945.965.249-56'
    """


# Generated at 2022-06-13 23:28:52.649949
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider(seed=987).cpf() == '370.852.485-35'


# Generated at 2022-06-13 23:28:56.916702
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.person.pt_br import BrazilSpecProvider

    from datetime import datetime

    provider = BrazilSpecProvider()
    person_provider = Person(locale='pt-br', provider=BrazilSpecProvider)

    print(person_provider.ssn())

# Generated at 2022-06-13 23:28:58.953678
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert len(provider.cpf()) == 14
    assert provider.cpf(False) == '01313709744'


# Generated at 2022-06-13 23:29:03.611321
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""
    brazil_spec_provider = BrazilSpecProvider()
    cnpj = brazil_spec_provider.cnpj()
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:29:08.667466
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    cpf = br.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf[12:].isdigit()



# Generated at 2022-06-13 23:29:11.960022
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    test_provider = BrazilSpecProvider(seed=10)
    assert test_provider.cnpj() == '77.732.230/0001-70'


# Generated at 2022-06-13 23:29:29.285002
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class with seed 1234567890
    """
    seed = 1234567890
    brazil_spec_provider = BrazilSpecProvider(seed)

    cpf_list = ['304.291.979-77',
                '879.054.487-07',
                '664.895.171-99',
                '206.020.152-70',
                '807.419.527-60',
                '990.651.527-50',
                '486.867.151-10',
                '671.717.836-27',
                '011.041.654-20',
                '180.601.885-90']

    for count in range(0, len(cpf_list)):
        assert cpf_list[count] == brazil_spec_

# Generated at 2022-06-13 23:29:41.661030
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    brazil = BrazilSpecProvider()
    person = Person('en')

    for _ in range(10):
        with_mask = brazil.random.randint(0, 1)
        cnpj = brazil.cnpj(with_mask)
        if with_mask:
            assert cnpj.count('.') == 2
            assert cnpj.count('/') == 1
            assert cnpj.count('-') == 1
            assert len(cnpj) == 18
        else:
            assert len(cnpj) == 14



# Generated at 2022-06-13 23:29:46.249771
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider(seed=0)

    assert provider.cpf() == "876.142.926-72"
    assert provider.cpf(with_mask=False) == "87614292672"


# Generated at 2022-06-13 23:29:53.494728
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers import BrazilSpecProvider as BSP
    from mimesis.providers import BrazilSpecProvider
    from mimesis.enums import Gender
    import re
    bsp = BSP()
    bsp1 = BSP(seed=100)
    bsp2 = BSP('en')
    bsp3 = BSP(seed=100, locale='it')
    expected_cnpj1 = bsp1.cnpj()
    expected_cnpj2 = bsp2.cnpj()
    expected_cnpj3 = bsp3.cnpj()
    assert re.search(r'\d{2}.\d{3}.\d{3}/\d{4}-\d{2}', expected_cnpj1)

# Generated at 2022-06-13 23:29:59.100879
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    cpf_no_mask = bsp.cpf(False)
    assert len(cpf_no_mask) == 11



# Generated at 2022-06-13 23:30:00.632705
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 23:30:06.990755
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bs = BrazilSpecProvider()
    cnpj = bs.cnpj(True)
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'


# Generated at 2022-06-13 23:30:08.905005
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf(with_mask=False)
    print(cpf)


# Generated at 2022-06-13 23:30:12.301576
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    seed = 'mySecretSeed'
    object_provider = BrazilSpecProvider(seed)
    assert object_provider.cpf(with_mask=True) == '055.659.525-78'



# Generated at 2022-06-13 23:30:14.623636
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    return BrazilSpecProvider().cpf(with_mask=True)

# Generated at 2022-06-13 23:30:30.970881
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    cnpj = BrazilSpecProvider().cnpj()
    assert len(cnpj) == int(18)

# Generated at 2022-06-13 23:30:34.442991
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    # Setup
    brazil_provider = BrazilSpecProvider()

    # Exercise
    result_cnpj = brazil_provider.cnpj()

    # Verify
    assert result_cnpj

# Generated at 2022-06-13 23:30:38.505822
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of BrazilSpecProvider."""
    for i in range(10):
        assert len(BrazilSpecProvider().cnpj()) == 18
        assert len(BrazilSpecProvider().cnpj(False)) == 14


# Generated at 2022-06-13 23:30:44.144556
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf1 = bsp.cpf()
    cpf2 = bsp.cpf()
    assert len(cpf1) == 14
    assert len(cpf2) == 14
    assert cpf1 != cpf2


# Generated at 2022-06-13 23:30:48.056656
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    for i in range(10):
        assert provider.cnpj(False) == provider.cnpj(True).replace('.','').replace('/','').replace('-','')


# Generated at 2022-06-13 23:30:58.052057
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers import BrazilSpecProvider
    from mimesis.enums import Gender
    from mimesis import Person
    from mimesis import Datetime

    p = Person(BrazilSpecProvider)
    datetime = Datetime(BrazilSpecProvider)
    print('\nPassport: ' + p.passport())
    
    print('\nCPF: ' + p.cpf())
    
    # Teste do método que retorna o número de título de eleitor
    print(p.titulo_eleitor())

    # Teste do método que retorna o nome do mês em português do Brasil
    print(datetime.month_name())

    # Teste do método que retorna o nome do dia da semana em

# Generated at 2022-06-13 23:31:06.869659
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test method cnpj of class BrazilSpecProvider."""
    from unittest import TestCase

    from .provider_brazil_spec import BrazilSpecProvider
    from .regex_utils import (verify_cnpj, verify_cpf)

    cases = [True, False]
    provider = BrazilSpecProvider()
    for case in cases:
        for i in range(20):
            result = provider.cnpj(with_mask=case)

            if case:
                TestCase().assertTrue(verify_cnpj(result))
            else:
                TestCase().assertFalse(verify_cnpj(result))



# Generated at 2022-06-13 23:31:15.491393
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test the BrazilSpecProvider.cpf() method."""
    bsp = BrazilSpecProvider()

    for i in range(100):  # test #1
        result1 = bsp.cpf(with_mask=True)
        result2 = bsp.cpf(with_mask=False)
        assert result1 != result2

    result1 = bsp.cpf(with_mask=False)
    result2 = bsp.cpf(with_mask=False)
    assert result1 != result2


# Generated at 2022-06-13 23:31:23.338790
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender

    data = BrazilSpecProvider()
    # CPF without mask
    assert data.cpf(with_mask=False) == '88394848208'
    # CPF with mask
    assert data.cpf(with_mask=True) == '883.948.482-08'
    # CPF with mask and gender
    assert data.cpf(with_mask=True, gender=data.random.choice(Gender)) == '883.948.482-08'


# Generated at 2022-06-13 23:31:25.890553
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:32:00.274200
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_provider = BrazilSpecProvider()
  
    assert len(brazil_provider.cpf(False)) == 11
    assert len(brazil_provider.cpf(False)) == 11
    
    assert len(brazil_provider.cpf(True)) == 14
    assert len(brazil_provider.cpf(True)) == 14


# Generated at 2022-06-13 23:32:12.493759
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    
    # Setup readline to mock input function
    import readline
    readline.parse_and_bind("tab: complete")
    readline.set_completer(lambda text, state: state < 6 and readline.get_line_buffer().split()[state] or None)

#    def input_fake(*args):
#        values = ["9", "6", "8", "3", "3", "7", "4", "8", "7", "6", "0", "4"]
#        return values[readline.get_current_history_length()]
#    readline.set_pre_input_hook(lambda: readline.insert_text(input_fake()))
#    readline.set_startup_hook(lambda: readline.insert

# Generated at 2022-06-13 23:32:16.391431
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test the method cpf of class BrazilSpecProvider."""
    from mimesis import BrazilSpecProvider
    print('BrazilSpecProvider.cpf():')
    cpf = BrazilSpecProvider().cpf()
    print(cpf)


# Generated at 2022-06-13 23:32:19.513679
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    result = BrazilSpecProvider().cnpj()
    assert result == '77.732.230/0001-70'
    print(result)


# Generated at 2022-06-13 23:32:23.810662
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    from mimesis.builtins.brazil import BrazilSpecProvider
    provider_cpf = BrazilSpecProvider()
    assert provider_cpf.cpf() == '054.416.109-47'
    assert provider_cpf.cpf(with_mask=False) == '05441610947'


# Generated at 2022-06-13 23:32:25.868442
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    s = BrazilSpecProvider()
    cnpj = s.cnpj()
    assert cnpj is not None
    assert len(cnpj) == 18


# Generated at 2022-06-13 23:32:31.145904
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Compare generated string with a valid CPF."""
    brazil_spec_provider = BrazilSpecProvider()
    cpf = brazil_spec_provider.cpf(with_mask=True)
    assert len(cpf) == 14
    assert cpf == '097.374.831-98'



# Generated at 2022-06-13 23:32:35.324002
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.builtins.brazil import BrazilSpecProvider
    brazil_spec_provider = BrazilSpecProvider()
    cpf1 = brazil_spec_provider.cpf()
    cpf2 = brazil_spec_provider.cpf()
    assert cpf1 != cpf2
    assert len(cpf1) == 14
    assert len(cpf2) == 14


# Generated at 2022-06-13 23:32:42.151783
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert len(cnpj) == 18
    assert cnpj[2] == '.'
    assert cnpj[6] == '.'
    assert cnpj[10] == '/'
    assert cnpj[15] == '-'
    assert cnpj[0:2].isdigit()
    assert cnpj[3:6].isdigit()
    assert cnpj[7:10].isdigit()
    assert cnpj[11:15].isdigit()
    assert cnpj[16:18].isdigit()
    print('>>> BrazilSpecProvider::cnpj returns "{cnpj}""'.format(cnpj=cnpj))


# Generated at 2022-06-13 23:32:50.137117
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.providers.brazil.brazil_provider import BrazilSpecProvider
    from mimesis.builtins import BrazilSpecProvider as BuiltInBrazil
    
    bsp = BrazilSpecProvider(seed=42)
    bi = BuiltInBrazil(seed=42)

    assert bsp.cnpj(with_mask=True) == '09.175.674/0001-52'
    assert bsp.cnpj(with_mask=False) == '09175675000152'

    # I'm not sure this is the best way to do this.
    # It would be really nice if we could use mocks in the unittest.
    # But this is working for now
    bi.cnpj = lambda *args : '09.175.674/0001-52'


# Generated at 2022-06-13 23:33:58.581335
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    assert (b.cpf(with_mask=True) == "112.926.692-23")


# Generated at 2022-06-13 23:34:06.146272
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """This test intends to validate the method cnpj() of class BrazilSpecProvider"""
    brazil_provider = BrazilSpecProvider()
    cnpj = brazil_provider.cnpj(with_mask=True)
    cnpj_without_mask = brazil_provider.cnpj(with_mask=False)
    assert len(cnpj) == 18
    assert len(cnpj_without_mask) == 14
    assert cnpj[0:2].isdigit() and cnpj[19:12].isdigit()
    assert cnpj_without_mask[0:12].isdigit()
    assert not cnpj == cnpj_without_mask
    assert cnpj[2] == '.' and cnpj[6] == '.' and cnpj[10] == '/'

# Generated at 2022-06-13 23:34:12.017224
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    res = br.cpf()
    assert len(res) == 14
    assert res[3] == '.' and res[7] == '.' and res[11] == '-'


# Generated at 2022-06-13 23:34:14.891171
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert (len(cnpj) == 18)
    print(cnpj)


# Generated at 2022-06-13 23:34:18.611780
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test BrazilSpecProvider's method cpf."""
    tester = BrazilSpecProvider()
    cpf = tester.cpf()
    assert len(cpf) == 14
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'


# Generated at 2022-06-13 23:34:21.063117
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == "076.326.751-71"
    assert BrazilSpecProvider().cpf(False) == "04212519471"


# Generated at 2022-06-13 23:34:21.821211
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    pass


# Generated at 2022-06-13 23:34:24.596798
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    br = BrazilSpecProvider()
    cpf = (br.cpf())
    print(cpf)
    return cpf


# Generated at 2022-06-13 23:34:26.661575
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    BR = BrazilSpecProvider(seed=12345)
    cpf = BR.cpf()
    assert cpf == "907.942.299-32"



# Generated at 2022-06-13 23:34:31.304334
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Testing BrazilSpecProvider class method cnpj"""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.brazil import BrazilSpecProvider
    p = Person('en')
    test_data = p.cnpj()
    assert test_data == '17.891.753/0001-55'
    test_data = p.cnpj()
    assert test_data == '95.759.296/0001-18'


# Generated at 2022-06-13 23:37:58.549265
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpf = BrazilSpecProvider().cpf()
    assert len(cpf.replace('.', '').replace('-', '')) == 11


# Generated at 2022-06-13 23:38:05.385540
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil_provider = BrazilSpecProvider()
    cnpj = brazil_provider.cnpj(with_mask=True)
    assert cnpj.count('.') == 2
    assert cnpj.count('-') == 1
    cnpj = cnpj.replace('.', '').replace('-', '')
    assert (len(cnpj) == 14) and (cnpj.isdigit())

# Generated at 2022-06-13 23:38:13.009842
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()

    cpf = brazil.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf.count('.') == 2
    assert cpf.count('-') == 1
    assert cpf.isdigit()

    cpf_no_mask = brazil.cpf(with_mask=False)
    assert len(cpf_no_mask) == 11
    assert cpf_no_mask.isdigit()


# Generated at 2022-06-13 23:38:14.767811
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider.cnpj() == '77.732.230/0001-70'



# Generated at 2022-06-13 23:38:18.960811
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test for BrazilSpecProvider.cnpj."""
    b = BrazilSpecProvider()
    assert isinstance(b.cnpj(False), str)
    assert b.cnpj(False).__len__() == 14

    b = BrazilSpecProvider(seed=12345)
    assert b.cnpj(False) == '838302000135'

# Generated at 2022-06-13 23:38:30.261467
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # The assert methods are used to verify the expected result, a specific value.
    # assertEqual is used to verify that the result is equal to the expected value.
    # assertNotEqual is used to verify that the result is different from the expected value.

    # On the other hand, assertTrue is used to verify that the result is true.
    # assertFalse is used to verify that the result is false.

    bsp = BrazilSpecProvider()
    # You need to create an object to call the method.
    # BrazilSpecProvider() is the class object, whose function is to create objects.
    # bsp is the object. Once obtained, the method can be called.

    assert len(bsp.cpf()) == 14
    assert bsp.cpf().startswith("000.")
    assert bsp.cpf().endswith("-00")
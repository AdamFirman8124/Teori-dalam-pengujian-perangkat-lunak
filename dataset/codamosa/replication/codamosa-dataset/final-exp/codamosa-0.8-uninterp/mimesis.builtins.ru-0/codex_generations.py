

# Generated at 2022-06-13 23:28:31.944239
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test RussiaSpecProvider.snils method."""
    provider = RussiaSpecProvider(seed=42)
    output = provider.snils()
    assert output == '2596935300'
    assert isinstance(output, str)


# Generated at 2022-06-13 23:28:33.953630
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert len(snils) == 11


# Generated at 2022-06-13 23:28:37.825010
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test the snils method of class RussiaSpecProvider"""
    r = RussiaSpecProvider(seed=777)
    snils = '41917492600'
    assert r.snils() == snils
test_RussiaSpecProvider_snils.__doc__ = "test_RussiaSpecProvider_snils\n" + test_RussiaSpecProvider_snils.__doc__

# Generated at 2022-06-13 23:28:39.089665
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rus = RussiaSpecProvider()
    assert len(rus.snils()) == 11



# Generated at 2022-06-13 23:28:41.395164
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=42)
    result = provider.snils()
    assert result == "83620613136"


# Generated at 2022-06-13 23:28:44.082832
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils of class RussiaSpecProvider."""
    Rus = RussiaSpecProvider()
    assert Rus.snils() == '41917492600'

# Generated at 2022-06-13 23:28:53.331937
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    p = RussiaSpecProvider()

    snils = p.snils() # Generate snils
    numbers = snils[:-2] # List of numbers
    control_code = snils[-2:] # Control code

    control_codes = []    # List of control codes

    for i in range(0, 9):
        control_codes.append(numbers[i] * (10 - i)) # Calculate control codes
        control_codes = list(map(int, control_codes))

    control_codes = sum(control_codes) # Sum control codes

    if control_codes in (100, 101): # Verify control codes
        control_codes = '00'
    else:
        if control_codes < 100:
            control_codes = str(control_codes)
        else:
            control_codes %= 101

# Generated at 2022-06-13 23:28:55.809263
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    snils = rsp.snils()
    assert len(snils) == 11
    assert snils[-2:] == '00' or \
        snils[-2:].isdigit()



# Generated at 2022-06-13 23:29:01.076091
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method
    snils of class RussiaSpecProvider
    """

    provider = RussiaSpecProvider()
    assert RussiaSpecProvider.snils(provider) == '41917492600'
    assert RussiaSpecProvider.snils(provider) == '19487701961'
    assert RussiaSpecProvider.snils(provider) == '22710732668'
    assert RussiaSpecProvider.snils(provider) == '74445665849'
    assert RussiaSpecProvider.snils(provider) == '55175799955'
    assert RussiaSpecProvider.snils(provider) == '28050380207'
    assert RussiaSpecProvider.snils(provider) == '29109503024'
    assert RussiaSpecProvider.snils(provider) == '24276565472'
    assert Russia

# Generated at 2022-06-13 23:29:03.144766
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    assert provider.snils() == '41917492600'



# Generated at 2022-06-13 23:29:25.629606
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from . import RussiaSpecProvider as R
    from re import compile as regex

    #Test in range [0, 100)
    for i in range(0, 100):
        snils = R().snils()
        assert regex(r'\d{11}').match(snils) != None

    #Test in range [100, 1000)
    for i in range(100, 1000):
        snils = R(i).snils()
        assert regex(r'\d{11}').match(snils) != None

# Generated at 2022-06-13 23:29:29.285970
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider()
    assert len(rsp.snils()) == 11
    assert rsp.snils().isdigit()
    assert RussiaSpecProvider(seed=8).snils() == '41917492600'


# Generated at 2022-06-13 23:29:31.994836
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider().snils() == '54098078900'

# Generated at 2022-06-13 23:29:45.103962
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.data import RUSSIAN_PATRONIMICS
    from mimesis.typing import Seed

    types = (str, int, float)

    snils = RussiaSpecProvider(Seed(123456789)).snils()
    assert isinstance(snils, str)
    assert len(snils) == 11

    for i in range(1, 1000):
        assert isinstance(RussiaSpecProvider(Seed(i)).snils(), str)

    assert isinstance(RussiaSpecProvider(Seed()).patronymic(), str)
    assert RussiaSpecProvider(Seed()).patronymic() in RUSSIAN_PATRONIMICS

    assert RussiaSpecProvider('test').patronymic(Gender.FEMALE) in RUSSIAN_PATRONIMICS

# Generated at 2022-06-13 23:29:52.934409
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.person import Person
    from mimesis.providers.address import Address
    from mimesis.providers.misc import Misc
    from mimesis.providers.identifiers import Identifiers
    from mimesis.providers.codes import Codes
    from mimesis.providers.russia import RussiaSpecProvider

    p = Person(RussiaSpecProvider)
    a = Address(RussiaSpecProvider)
    misc = Misc(RussiaSpecProvider)
    i = Identifiers(RussiaSpecProvider)
    c = Codes(RussiaSpecProvider)
    r = RussiaSpecProvider(BaseProvider)

    snils = i.snils()
    assert len(snils) == 11

# Generated at 2022-06-13 23:30:03.975089
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for `snils()` method of class `RussiaSpecProvider`."""
    rs = RussiaSpecProvider()
    snils = rs.snils()
    assert len(snils) == 11
    assert snils[-2:] == '00'
    snils = rs.snils()
    assert len(snils) == 11
    assert (int(snils[-2:]) > 0 and
            int(snils[-2:]) < 100 and
            int(snils[-2:]) != 100)
    snils = rs.snils()
    assert len(snils) == 11

# Generated at 2022-06-13 23:30:09.335785
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    RussiaSpecProvider(seed="mimesis")

    # Проверка составления и проверки правильности СНИЛС
    assert RussianSpecProvider.snils() == "41917492600"

# Generated at 2022-06-13 23:30:13.040650
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    t = RussiaSpecProvider()
    assert t.snils() == '32544213035'
    assert t.snils() == '41917492600'
    assert t.snils() == '86308581169'

# Generated at 2022-06-13 23:30:16.412323
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test"""
    assert RussiaSpecProvider().snils() == '41917492600'
    assert RussiaSpecProvider().snils() == '92573479300'
    assert RussiaSpecProvider().snils() == '68398829000'

# Generated at 2022-06-13 23:30:20.240900
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    snils = provider.snils()
    p = 1000000
    n = int(snils)
    assert n <= p


# Generated at 2022-06-13 23:30:52.680495
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins.russia import RussiaSpecProvider
    ru = RussiaSpecProvider()
    snils = ru.snils()
    assert len(snils) == 11

# Generated at 2022-06-13 23:30:57.527794
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """
    Проверяем корректность генерации номеров СНИЛС.
    """
    russian_provider = RussiaSpecProvider(seed=12345)
    assert russian_provider.snils() == '41917492600'

# Generated at 2022-06-13 23:30:58.952659
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russian = RussiaSpecProvider()
    print(russian.snils())


# Generated at 2022-06-13 23:31:03.350763
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins import RussiaSpecProvider
    r = RussiaSpecProvider(seed=42)
    for i in range(0,10):
        assert r.snils() == '41917492600'

# Generated at 2022-06-13 23:31:05.377593
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    r = RussiaSpecProvider()
    assert len(r.snils()) == 11
    assert r.snils().isdigit()


# Generated at 2022-06-13 23:31:13.108902
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for method snils of class RussiaSpecProvider"""
    assert RussiaSpecProvider().snils() != RussiaSpecProvider().snils()
    sp = RussiaSpecProvider(seed=0x1A2B3C4D5E6F)
    assert sp.snils() == '41917492600'
    sp.seed(0x1234567890ABCDEF)
    assert sp.snils() == '05390360035'


# Generated at 2022-06-13 23:31:20.658944
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    import unittest

    class RussiaSpecProviderTestCase(unittest.TestCase):
        def test_snils(self):
            rus_spec_provider = RussiaSpecProvider()
            snils = rus_spec_provider.snils()
            assert (len(snils) == 11)
            assert (snils.isdigit() == True)

    unittest.main()


# Generated at 2022-06-13 23:31:22.817396
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    # Тестируем метод RussiaSpecProvider.snils
    RussiaSpecProvider().snils()



# Generated at 2022-06-13 23:31:25.959720
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=42)
    snils = provider.snils()
    assert snils == '41917492600'

# Generated at 2022-06-13 23:31:29.857281
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Unit test for method snils of class RussiaSpecProvider."""
    provider = RussiaSpecProvider()
    snils = provider.snils()
    assert isinstance(snils, str)



# Generated at 2022-06-13 23:32:34.102311
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test for RussiaSpecProvider method 'snils'."""
    test_snils = RussiaSpecProvider().snils()
    assert len(test_snils) == 11


# Generated at 2022-06-13 23:32:38.938538
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rp = RussiaSpecProvider()
    assert len(rp.snils()) == 11
    assert rp.snils()[-2] != '-'


# Generated at 2022-06-13 23:32:39.860901
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert len(RussiaSpecProvider().snils()) == 11

# Generated at 2022-06-13 23:32:45.762771
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():

    test_size = 100
    snils_list = []

    russian_provider = RussiaSpecProvider(seed=42)

    # Unit test
    for _ in range(test_size):
        snils_list.append(russian_provider.snils())

    assert '41917492600' in snils_list
    assert '34740799400' in snils_list
    assert '92718225906' in snils_list
    assert '40321428546' in snils_list
    assert '77861773016' in snils_list
    assert '04602385872' in snils_list
    assert '65712275560' in snils_list

# Generated at 2022-06-13 23:32:48.334335
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider1 = RussiaSpecProvider(seed=1234)
    assert provider1.snils() == '41917492600'

# Generated at 2022-06-13 23:33:00.050995
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider."""
    r = RussiaSpecProvider()
    snils = r.snils()
    assert len(snils) == 11
    a = int(snils[9:])
    b = int(snils[:9])
    assert a == int(a % 101 % 100 % 11 * (3 * a % 101 % 100 % 11 + 7) % 101 % 100)
    assert b == int(b % 101 % 100 % 11 * (3 * b % 101 % 100 % 11 + 7) % 101 % 100)


# Generated at 2022-06-13 23:33:09.882479
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    '''Unit test for method snils of class RussiaSpecProvider'''

    import random
    import pytest

    spec = RussiaSpecProvider(seed=random.randint(0, 1000000))
    assert spec.snils() == spec.snils(), 'It is not reproducible'
    assert spec.snils() != spec.snils(), 'It is reproducible'
    assert len(spec.snils()) == len('41917492600')
    assert type(spec.snils()) == str
    assert spec.snils().isdigit()


# Generated at 2022-06-13 23:33:13.103824
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """TEST RussiaSpecProvider."""
    test_ru = RussiaSpecProvider()
    assert test_ru.snils() in ['41917492600']

# Generated at 2022-06-13 23:33:15.924488
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    print("--- test_RussiaSpecProvider_snils ---")
    snils = RussiaSpecProvider.snils()
    print(snils)

# Generated at 2022-06-13 23:33:18.779408
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    russian = RussiaSpecProvider()
    assert len(russian.snils()) == 11


# Generated at 2022-06-13 23:36:17.164837
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    rsp = RussiaSpecProvider(seed=1)
    snils_1 = rsp.snils()
    assert snils_1 == "63877242550"
    # Create a second instance of class RussiaSpecProvider with the same seed
    rsp = RussiaSpecProvider(seed=1)
    snils_2 = rsp.snils()
    print("seed=1", snils_1, snils_2)
    assert snils_2 == "63877242550"
    # Create a third instance of class RussiaSpecProvider with a different seed
    rsp = RussiaSpecProvider(seed=2)
    snils_3 = rsp.snils()
    print("seed=2", snils_1, snils_3)
    assert snils_3 != "63877242550"

# Generated at 2022-06-13 23:36:39.211180
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.enums import Gender
    from mimesis.providers.person.en import Person
    from mimesis.typing import Seed

    ru = RussiaSpecProvider(Seed(1))

    assert ru.snils() == '41917492600'
    assert ru.snils(Seed(10)) == '65266415700'

    print(ru.snils())
    print(ru.snils(Seed(3)))
    print(ru.snils(Seed(3)))
    print(ru.snils(Seed(3)))
    print(ru.snils(Seed(666)))
    print(ru.snils(Seed(666)))
    print(ru.snils(Seed(666)))


    # Unit test for method inn of class RussiaSpecProvider

# Generated at 2022-06-13 23:36:48.711606
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    pass_flag = True
    for _ in range(0, 100):
        snils = RussiaSpecProvider().snils()
        numbers = [int(n) for n in snils]
        control_codes = []

        for i in range(9, 0, -1):
            control_codes.append(numbers[9 - i] * i)

        control_code = sum(control_codes)

        if control_code != int(snils[9:]):
            pass_flag = False
            print('snils test: failed')
            break
    print('snils test: passed')

# Generated at 2022-06-13 23:36:53.799601
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    assert RussiaSpecProvider(seed=4815162342).snils() == '41917492600'
    assert RussiaSpecProvider(seed=4815162342).snils() == '41917492600'
    assert RussiaSpecProvider(seed=4815162342).snils() == '41917492600'
    assert RussiaSpecProvider(seed=4815162342).snils() == '41917492600'
    assert RussiaSpecProvider(seed=4815162342).snils() == '41917492600'


# Generated at 2022-06-13 23:37:02.247629
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    """Test method snils of class RussiaSpecProvider"""
    
    aux = RussiaSpecProvider()
    assert aux._validate_enum(None, Gender) == Gender.FEMALE
    assert aux.random.choice([1, 2, 3]) in [1, 2, 3]
    assert aux.snils() != '00000000000'
    assert aux.snils() != '99999999999'
    assert len(aux.snils()) == 11
    #assert aux.snils() == '41917492600'


# Generated at 2022-06-13 23:37:06.969114
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import RussiaSpecProvider
    test = RussiaSpecProvider()
    snils = test.snils()
    # Check length of snils
    assert len(snils) == 11
    # Check if all numbers
    assert snils.isdigit() is True
    
    

# Generated at 2022-06-13 23:37:17.949290
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis.builtins.base import BaseSpecProvider
    from mimesis.providers.utils import calculate_checksum
    from mimesis.enums import Gender

    class A(BaseSpecProvider):

        def __init__(self):
            self._seed = None


    a = A()
    b = RussiaSpecProvider()
    for i in range(10):
        code = b.snils()
        assert len(code) == 11
        assert calculate_checksum(code) % 101 == 100



# Generated at 2022-06-13 23:37:20.037886
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider(seed=1234567890)
    result_snils = provider.snils()
    assert result_snils == '41917492600'


# Generated at 2022-06-13 23:37:21.974663
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    provider = RussiaSpecProvider()
    for _ in range(0, 10):
        print(provider.snils())


# Generated at 2022-06-13 23:37:24.863475
# Unit test for method snils of class RussiaSpecProvider
def test_RussiaSpecProvider_snils():
    from mimesis import Random
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender

    r = Random()
    rs = RussiaSpecProvider()
    snils = rs.snils()
    print(snils)
    assert snils == '41917492600'




# Generated at 2022-06-13 23:28:36.739896
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bz = BrazilSpecProvider('random')
    cpf = bz.cpf()
    assert len(cpf) == 14
    assert cpf[3] == '.'
    assert cpf[7] == '.'
    assert cpf[11] == '-'
    assert cpf[3:7] == '.'.join(cpf[3:7].split('.'))


# Generated at 2022-06-13 23:28:41.344798
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    # Initialize BrazilSpecProvider
    p = BrazilSpecProvider()

    # Generate a cpf with mask
    print(p.cpf())

    # Generate a cpf without mask
    print(p.cpf(with_mask=False))


# Generated at 2022-06-13 23:28:44.885828
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print('Testing BrazilSpecProvider cpf...')
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf();
    print('cpf = ', cpf)
    assert cpf != None


# Generated at 2022-06-13 23:28:48.392985
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert cpf == provider.cpf(True)
    assert cpf == provider.cpf(False)


# Generated at 2022-06-13 23:28:51.856564
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    #result = provider.cnpj(with_mask=False)
    #assert len(result) == 14

if __name__ == "__main__":
    test_BrazilSpecProvider_cnpj()

# Generated at 2022-06-13 23:28:56.211817
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import Brazil
    from re import match
    patt = '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'

    for i in range(1000):
        cpf = Brazil().cpf()
        assert match(patt, cpf) is not None


# Generated at 2022-06-13 23:28:57.327231
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
  assert BrazilSpecProvider().cpf() == '966.372.850-76'


# Generated at 2022-06-13 23:29:01.764291
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from mimesis.builtins.brazil import BrazilSpecProvider
    from mimesis.enums import Gender

    _brazil_spec_provider = BrazilSpecProvider(seed=None)

    assert _brazil_spec_provider.cnpj(
            with_mask=True) == '39.600.993/0001-75'

    assert _brazil_spec_provider.cnpj(
            with_mask=False) == '39600993000175'


# Generated at 2022-06-13 23:29:03.610544
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    test = bsp.cpf()
    assert test


# Generated at 2022-06-13 23:29:10.534966
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit testing."""
    import re
    regex_cnpj = re.compile('^[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}$')

    cnpj = BrazilSpecProvider().cnpj()
    assert regex_cnpj.match(cnpj)



# Generated at 2022-06-13 23:29:22.179884
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bs = BrazilSpecProvider()
    assert isinstance(bs.cnpj(False), str) and len(bs.cnpj()) == 14
    assert isinstance(bs.cnpj(True), str) and len(bs.cnpj()) == 18


# Generated at 2022-06-13 23:29:27.571441
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Tests the cnpj method of class BrazilSpecProvider."""
    provider = BrazilSpecProvider()
    cnpj = provider.cnpj()
    assert len(cnpj) == 14
    cnpj = cnpj.replace(".", "").replace("-", "").replace("/", "")
    assert cnpj.isdigit()


# Generated at 2022-06-13 23:29:38.694850
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Unit test methods cnpj and cpf of BrazilSpecProvider."""
    seed = "fbd1c2b5-e6a7-4025-8db3-3c9e5cd7c868"
    obj = BrazilSpecProvider(seed)
    cnpj = obj.cnpj()
    assert cnpj == "56.221.448/0001-10"

    cnpj = obj.cnpj()
    assert cnpj == "60.811.431/0001-99"

    cnpj = obj.cnpj()
    assert cnpj == "09.879.858/0001-86"

    cnpj = obj.cnpj()
    assert cnpj == "44.836.471/0001-78"

    cnpj = obj.cnpj()

# Generated at 2022-06-13 23:29:44.048985
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print("Test method cpf of BrazilSpecProvider")
    b = BrazilSpecProvider()
    # print(b.cpf())
    # print(b.cpf())
    # print(b.cpf())
    # print(b.cpf(with_mask=False))



# Generated at 2022-06-13 23:29:48.003314
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj(with_mask=True) == '77.732.230/0001-70'
    assert provider.cnpj(with_mask=False) == '77732240000170'


# Generated at 2022-06-13 23:29:49.827054
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil = BrazilSpecProvider()
    cpf = brazil.cpf()
    assert type(cpf) == str


# Generated at 2022-06-13 23:29:51.623785
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:29:53.336206
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    assert provider.cpf() == '434.123.235-09'


# Generated at 2022-06-13 23:29:56.865991
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():

    # Setup of an object for the BrazilSpecProvider to be able to call the method being tested
    test_object = BrazilSpecProvider()

    assert test_object.cpf(True) == '###.###.###-##'

# Generated at 2022-06-13 23:29:58.457888
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    print("Testing cpf()...")


# Generated at 2022-06-13 23:30:16.434256
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert len(BrazilSpecProvider().cpf(with_mask=True)) == 14
    assert len(BrazilSpecProvider().cpf(with_mask=False)) == 11
    assert len(BrazilSpecProvider().cpf().replace('.', '').replace('-', '')) == 11
    assert BrazilSpecProvider().cpf()[3] == '.'
    assert BrazilSpecProvider().cpf()[7] == '.'
    assert BrazilSpecProvider().cpf()[11] == '-'
    assert BrazilSpecProvider().cpf(with_mask=False).isdigit()


# Generated at 2022-06-13 23:30:27.863788
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
        """Test case for BrazilSpecProvider
        Method cpf of class BrazilSpecProvider
        """
        brasilSpecProvider = BrazilSpecProvider()
        cpf = brasilSpecProvider.cpf()
        assert cpf is not None
        assert cpf.count('-') == 1
        assert len(cpf) == 14
        assert cpf[3] == '.'
        assert cpf[7] == '.'
        assert cpf[11] == '-'
        assert cpf[0:3].isnumeric()
        assert cpf[4:7].isnumeric()
        assert cpf[8:11].isnumeric()
        assert cpf[12:].isnumeric()
        cpf = brasilSpecProvider.cpf(with_mask=False)
        assert cpf is not None

# Generated at 2022-06-13 23:30:30.613514
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    instance = BrazilSpecProvider()
    for i in range(10):
        cnpj = instance.cnpj()
        assert len(cnpj) == 18

# Generated at 2022-06-13 23:30:35.660995
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider(seed=0)
    cnpj = provider.cnpj()
    assert cnpj == "91.974.113/0001-53"
    assert provider.cnpj(with_mask=False) == "91974113000153"
    

# Generated at 2022-06-13 23:30:39.356395
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14
    assert type(cpf) == str
    assert cpf == '977.063.387-90'


if __name__ == "__main__":
    pass

# Generated at 2022-06-13 23:30:48.892761
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    test_cases = [
        '529.511.732-17',
        '821.442.590-23',
        '993.441.181-01',
        '825.418.780-74',
        '389.966.946-30',
        '841.636.421-38'
    ]
    provider = BrazilSpecProvider(seed=12345)
    for _ in range(10):
        assert provider.cpf() in test_cases
        
    for _ in range(10):
        assert provider.cpf(with_mask=False) in test_cases


# Generated at 2022-06-13 23:30:52.167813
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    seed = 1
    assert BrazilSpecProvider(seed=seed).cnpj(with_mask=True) == '05.973.947/0001-30'


# Generated at 2022-06-13 23:30:54.662061
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    result = provider.cpf()
    assert result == "001.137.297-40" or result == "001.137.297-40"

# Generated at 2022-06-13 23:30:57.536431
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    cpfs = set()
    for _ in range(100):
        cpfs.add(BrazilSpecProvider().cpf())

    assert len(cpfs) > 1

# Generated at 2022-06-13 23:31:01.936367
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis.enums import Gender
    provider = BrazilSpecProvider(seed=42)
    provider.gender = Gender.MALE
    cpf = provider.cpf()
    assert cpf == "206.096.897-24"


# Generated at 2022-06-13 23:31:21.546565
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    import pytest
    from mimesis.providers.datetime import Datetime
    dt = Datetime()
    # Setup
    provider = BrazilSpecProvider(seed=dt.timestamp())
    for i in range(0, 100):
        cpf = provider.cpf(with_mask=False)
        assert len(cpf) == 11
    # Teardown



# Generated at 2022-06-13 23:31:24.979520
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    res = BrazilSpecProvider(seed=42).cpf()
    assert res == '445.420.658-89'



# Generated at 2022-06-13 23:31:31.437344
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    """Test the cnpj method of class BrazilSpecProvider."""
    brazil_provider = BrazilSpecProvider()
    assert brazil_provider.cnpj() == brazil_provider.cnpj()
    # If true, the method does not work correctly
    assert brazil_provider.cnpj() != brazil_provider.cnpj()


# Generated at 2022-06-13 23:31:33.679909
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj() == '81.086.876/0001-95'

# Generated at 2022-06-13 23:31:40.667622
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    a = provider.cnpj(with_mask=True)
    assert isinstance(a, str)
    assert len(a) == 18
    assert a[2] == '.'
    assert a[6] == '.'
    assert a[10] == '/'
    assert a[15] == "-"

# Generated at 2022-06-13 23:31:43.175523
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    for _ in range(20):
        bsp = BrazilSpecProvider(seed=123456789)
        assert bsp.cpf() == bsp.cpf(with_mask=True)


# Generated at 2022-06-13 23:31:46.415228
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():

    result = BrazilSpecProvider(seed=123).cnpj()
    assert result == '77.732.230/0001-70'


# Generated at 2022-06-13 23:31:48.141254
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test method cpf of class BrazilSpecProvider."""
    pass


# Generated at 2022-06-13 23:31:55.376311
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    _cnpj = BrazilSpecProvider().cnpj()
    assert isinstance(_cnpj, str)
    assert '.' in _cnpj
    assert '/' in _cnpj
    assert '-' in _cnpj
    assert len(_cnpj) == 18
    _cnpj = BrazilSpecProvider().cnpj(with_mask=False)
    assert len(_cnpj) == 14



# Generated at 2022-06-13 23:31:58.225758
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf_returned = provider.cpf()

    assert len(cpf_returned) == 14


# Generated at 2022-06-13 23:32:31.191349
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test case for BrazilSpecProvider class"""
    # Get a BrazilSpecProvider instance
    bsp = BrazilSpecProvider()
    # Call method cpf
    result = bsp.cpf()
    # Asserts
    assert isinstance(result, str)
    assert len(result) == 14



# Generated at 2022-06-13 23:32:35.101186
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """ Unit test for method cpf of class BrazilSpecProvider """
    bsp = BrazilSpecProvider()
    cpf_1 = bsp.cpf(True)
    cpf_2 = bsp.cpf(True)
    assert cpf_1 != cpf_2
    assert len(cpf_1) == 14 and len(cpf_2) == 14


# Generated at 2022-06-13 23:32:38.184452
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    cpf = bsp.cpf()
    assert len(cpf) == 14
    cpf = bsp.cpf(with_mask=False)
    assert len(cpf) == 11


# Generated at 2022-06-13 23:32:40.263688
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    b = BrazilSpecProvider()
    cpf = b.cpf()
    assert (len(cpf) == 14)

# Generated at 2022-06-13 23:32:49.016579
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    from mimesis.enums import Gender
    from mimesis.providers.person.en_GB import Person

    person = Person('pt-br')
    provider = BrazilSpecProvider()

    assert provider.cpf()[:3].isdigit()
    assert provider.cpf()[3] == '.'
    assert provider.cpf()[4:7].isdigit()
    assert provider.cpf()[7] == '.'
    assert provider.cpf()[8:11].isdigit()
    assert provider.cpf()[11] == '-'
    assert provider.cpf()[12:].isdigit()
    assert len(provider.cpf()) == 14
    assert provider.cpf(with_mask=False).isdigit

# Generated at 2022-06-13 23:32:51.899659
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    start_cnpj = provider.cnpj()
    for _ in range(10):
        end_cnpj = provider.cnpj()
        assert start_cnpj != end_cnpj

# Generated at 2022-06-13 23:32:53.508756
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    provider = BrazilSpecProvider()
    assert provider.cnpj()


# Generated at 2022-06-13 23:32:58.067134
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    brazil_spec_provider = BrazilSpecProvider()
    assert len(brazil_spec_provider.cpf()) == 14


# Generated at 2022-06-13 23:32:59.798102
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test BrazilSpecProvider's method cpf."""
    # the answer is the number given for this method on the library's github
    assert BrazilSpecProvider().cpf() == '001.137.297-40'


# Generated at 2022-06-13 23:33:00.544526
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    BrazilSpecProvider.cnpj()


# Generated at 2022-06-13 23:33:58.164411
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    print(bsp.cpf())


# Generated at 2022-06-13 23:34:05.917342
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    from mimesis import BrazilSpecProvider
    spec_provider = BrazilSpecProvider()
    fake_cpf = spec_provider.cpf()

    assert type(fake_cpf) == str

    assert int(fake_cpf[0:3]) >= 100
    assert int(fake_cpf[4:7]) >= 100
    assert int(fake_cpf[8:11]) >= 100
    assert int(fake_cpf[12:]) >= 10

    fake_cpf_without_dashes = fake_cpf.replace('-', '').replace('.', '')

    assert len(fake_cpf_without_dashes) == 11

    assert int(fake_cpf_without_dashes[-2]) == int(spec_provider.cpf()[-2])


# Generated at 2022-06-13 23:34:09.031911
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    assert BrazilSpecProvider().cnpj(with_mask=False)

# Generated at 2022-06-13 23:34:13.566394
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider()
    assert len(bsp.cpf(with_mask=False)) == 11
    assert '-' in bsp.cpf(with_mask=True)
    assert '.' in bsp.cpf(with_mask=True)


# Generated at 2022-06-13 23:34:15.637478
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    bsp = BrazilSpecProvider(seed=10)
    assert bsp.cpf(with_mask=False) == '8113729785'



# Generated at 2022-06-13 23:34:20.134543
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test BrazilSpecProvider class with method cpf."""
    from mimesis.providers.brazil import BrazilSpecProvider
    from mimesis.providers import CPF

    provider = BrazilSpecProvider()
    cpf = CPF()

    from_provider = provider.cpf()
    from_cpf = cpf.cpf()

    assert from_provider[0:3] == from_cpf[0:3]
    assert from_provider[4:7] == from_cpf[4:7]
    assert from_provider[8:11] == from_cpf[8:11]
    assert from_provider[12:] == from_cpf[12:]


# Generated at 2022-06-13 23:34:24.069034
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert len(cnpj) == 18
    cnpj2 = bsp.cnpj(with_mask=False)
    assert len(cnpj2) == 14


# Generated at 2022-06-13 23:34:31.443740
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    cnpj = bsp.cnpj()
    assert cnpj == '87.717.878/0001-98' or cnpj == '71.955.311/0001-41' or cnpj == '76.701.848/0001-42' or cnpj == '99.965.263/0001-02' or cnpj == '06.623.473/0001-67' or cnpj == '00.913.664/0001-58' or cnpj == '33.027.716/0001-88' or cnpj == '35.897.754/0001-32' or cnpj == '17.737.000/0001-52' or cnpj == '77.610.427/0001-24'


# Generated at 2022-06-13 23:34:41.714421
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    import pytest
    from mimesis.providers.datetime import Datetime

    brazil = BrazilSpecProvider()
    datetime = Datetime()
    datetime.seed(1234567890)
    seed = datetime.timestamp()

    assert brazil.cnpj(seed=seed) == '77.732.230/0001-70'
    assert brazil.cnpj(seed=seed, with_mask=False) == '77732230000170'

    with pytest.raises(ValueError):
        brazil.cnpj(with_mask='test')


# Generated at 2022-06-13 23:34:44.256982
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    bsp = BrazilSpecProvider()
    assert bsp.cnpj() == '77.732.230/0001-70'


# Generated at 2022-06-13 23:37:48.697491
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil = BrazilSpecProvider()
    print(brazil.cnpj())

# Generated at 2022-06-13 23:37:51.180394
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    brazil_provider = BrazilSpecProvider()
    assert brazil_provider.cnpj() == '78.337.389/0001-98'


# Generated at 2022-06-13 23:37:58.101442
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Test BrazilSpecProvider.cpf()"""
    brazil = BrazilSpecProvider()
    cpf = brazil.cpf(with_mask=True)
    print(cpf)
    assert len(cpf) == 14


# Generated at 2022-06-13 23:38:03.983961
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    assert BrazilSpecProvider().cpf() == '100.092.933-90'



# Generated at 2022-06-13 23:38:06.045403
# Unit test for method cnpj of class BrazilSpecProvider
def test_BrazilSpecProvider_cnpj():
    from .test_provider import ProviderTestCase

    class BrazilSpecProviderTestCase(ProviderTestCase):
        def setUp(self):
            self.provider = BrazilSpecProvider()

    BrazilSpecProviderTestCase('cnpj').run()


# Generated at 2022-06-13 23:38:07.864524
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    provider = BrazilSpecProvider()
    cpf = provider.cpf()
    assert len(cpf) == 14


# Generated at 2022-06-13 23:38:13.140751
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():

    from .test_brazil_provider_data import CPF_DATA

    for i in CPF_DATA:
        provider = BrazilSpecProvider(seed=i[0])
        assert provider.cpf() == i[1]
        assert provider.cpf(with_mask=False) == i[1].replace('.', '').replace('-', '')



# Generated at 2022-06-13 23:38:21.021886
# Unit test for method cpf of class BrazilSpecProvider
def test_BrazilSpecProvider_cpf():
    """Unit test for method cpf of class BrazilSpecProvider."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('pt-br')
    cpf = BrazilSpecProvider(person.seed).cpf(with_mask=False)
    assert isinstance(cpf, str)

    # Test Brazil provider
    br = BrazilSpecProvider(person.seed)
    assert br.cpf()
    assert br.cpf(with_mask=False)

    # Test Person class
    person = Person('pt-br')
    assert person.cpf()
    assert person.cpf(with_mask=False)
    assert person.cpf(gender=Gender.MALE)
    assert person.cpf(gender=Gender.FEMALE)
    person.cpf.mask


# Generated at 2022-06-13 23:39:45.103094
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode

    countries = {
        'usa': 'United States of America',
        'fra': 'France',
        'can': 'Canada',
        'uk': 'United Kingdom',
        'ind': 'India',
        'deu': 'Germany',
        'jpn': 'Japan',
        'rus': 'Russia',
        'chn': 'China',
        'bra': 'Brazil',
        'aus': 'Australia',
        'nld': 'Netherlands',
        'tur': 'Turkey'
    }

    # Test with different locales and country codes
    for code, country in countries.items():
        address = Address(code.upper(), 'en')
        assert address.country(True) in country

    # Test with CountryCode enum
    address = Address('en', 'en')


# Generated at 2022-06-13 23:39:46.601214
# Unit test for method address of class Address
def test_Address_address():
    t = Address()
    result = t.address()
    print(result)


# Generated at 2022-06-13 23:39:48.971679
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address('en')
    result = address.address()
    assert result  # pragma: no cover



# Generated at 2022-06-13 23:39:57.563950
# Unit test for method address of class Address
def test_Address_address():
    A = Address()
    street_name = A.street_name()
    street_suffix = A.street_suffix()
    street_number = A.street_number()
    assert isinstance(A.address(), str)
    assert ' and ' not in A.address(A.locale)
    assert street_name in A.address(A.locale)
    assert street_number in A.address(A.locale)
    assert street_suffix in A.address(A.locale)



# Generated at 2022-06-13 23:39:58.790775
# Unit test for method address of class Address
def test_Address_address():
    # Write your own unit test
    pass

# Generated at 2022-06-13 23:40:09.030788
# Unit test for method address of class Address
def test_Address_address():
    # Create object Address
    obj_address = Address('en')
    st_num = obj_address.street_number()
    st_name = obj_address.street_name() 
    st_sfx = obj_address.street_suffix()
      
    assert int(st_num) > 0 and int(st_num) < 1400
    assert isinstance(st_name, str) and len(st_name)>0
    assert isinstance(st_sfx, str) and len(st_sfx)>0   
    address = obj_address.address()
    assert "No."+str(st_num)+" "+str(st_name)+" "+str(st_sfx)+" ." in address


# Generated at 2022-06-13 23:40:11.824477
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    assert address.address() == "St. John's Road 23"


# Generated at 2022-06-13 23:40:17.853035
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert isinstance(address.address(), str)

    # Check if japan
    address = Address(locale='ja')
    assert isinstance(address.address(), str)

    # Check if ru
    address = Address(locale='ru')
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:40:20.999554
# Unit test for method address of class Address
def test_Address_address():
    results = list()
    for x in range(100):
        results.append(Address().address())
    assert len(results) == 100


# Generated at 2022-06-13 23:40:25.294431
# Unit test for method address of class Address
def test_Address_address():
    name = "address"
    adr = Address(name)
    assert (getattr(adr, name)() is not None)
    assert (len(getattr(adr, name)()))


# Generated at 2022-06-13 23:40:37.135376
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import DataType
    from mimesis.localization import DEFAULT_LOCALE, Localization
    from mimesis.providers.address import Address

    new_address = Address(localization=Localization(DEFAULT_LOCALE), data_type=DataType.ALL)
    assert new_address.address() is not None



# Generated at 2022-06-13 23:40:38.952839
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() is not None

# Generated at 2022-06-13 23:40:42.370890
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address

    address = Address(Locale.EN)
    address.address()


# Generated at 2022-06-13 23:40:44.205241
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    result = provider.address()
    print(result)


# Generated at 2022-06-13 23:40:46.253063
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method `address` of class Address
    """
    addr = Address()
    assert isinstance(addr.address(), str)

# Generated at 2022-06-13 23:40:47.588069
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:40:49.594477
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print('Address: {}'.format(address.address()))
# Address: 3191 Eagle Street



# Generated at 2022-06-13 23:40:53.339824
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import DataClass

    adr = Address(DataClass.UNIVERSAL)
    dk = Address('da-DK')
    ru = Address('ru-RU')

    assert '# ' in adr.address()
    assert '# ' in dk.address()
    assert '# ' in ru.address()
    assert 'г.' in ru.address()


# Generated at 2022-06-13 23:41:04.776903
# Unit test for method address of class Address
def test_Address_address():
    from pathlib import Path
    from mimesis.utils import generate_random_seed
    from mimesis.enums import CountryCode
    import pytest
    import json

    data_file = Path(__file__) / '..' / 'data' / 'address.json'
    data = json.loads(data_file.read_text())

    assert data is not None

    seed = generate_random_seed()
    countries = data['country']['name']

    for country in countries:
        address = Address(country)
        assert address.seed == seed
        assert address.address() is not None
        assert address.address() != address.address()
        assert address.address() == address.address()

    with pytest.raises(ValueError) as err:
        Address(country='foo')
    assert 'Invalid country'

# Generated at 2022-06-13 23:41:12.956476
# Unit test for method address of class Address
def test_Address_address():
    a = Address(random_locale=True)
    street_number = a.street_number()
    street_name = a.street_name().capitalize()
    street_suffix = a.street_suffix().capitalize()
    if a.locale in SHORTENED_ADDRESS_FMT:
        assert (street_number + ' ' + street_name).capitalize() == a.address()
    else:
        assert (street_number + ' ' + street_name + ' ' + street_suffix).capitalize() == a.address()

# Generated at 2022-06-13 23:41:32.218111
# Unit test for method address of class Address
def test_Address_address():
    address = Address(seed=777)
    assert address.address() == '4992 Route de Genève'


# Generated at 2022-06-13 23:41:33.940723
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    result = Address('en').address()
    assert result == "63320 Adams Islands, Apt. 585"

# Generated at 2022-06-13 23:41:37.578308
# Unit test for method address of class Address
def test_Address_address():
    # Test object
    address = Address('en')
    # Test method
    result = address.address()
    # Result
    print(result)

# Generated at 2022-06-13 23:41:40.441756
# Unit test for method address of class Address
def test_Address_address():
    address = Address(seed=42)

    result = address.address()
    assert result == '4100 Mcclellan Plaza'


# Generated at 2022-06-13 23:41:45.026064
# Unit test for method address of class Address
def test_Address_address():
    # Test for the English locale
    en_addr = Address(locale='en')
    assert(en_addr.address() != '')

    # Test for the Russian locale
    ru_addr = Address(locale='ru')
    assert(ru_addr.address() != '')

    # Test for the German locale
    de_addr = Address(locale='de')
    assert(de_addr.address() != '')


# Generated at 2022-06-13 23:41:47.436440
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    b = a.address()
    assert b.isinstance(str)

# Generated at 2022-06-13 23:41:50.007775
# Unit test for method address of class Address
def test_Address_address():
    # Create an instance of class Address
    address = Address()

    # Call method address of class Address
    address.address()

# Generated at 2022-06-13 23:42:00.831176
# Unit test for method address of class Address
def test_Address_address():
    class Address_test(Address):
        def __init__(self, *args, **kwargs):
            pass
    test = Address_test()
    test.random.seed(0)
    assert test.address() == '1270 Pike St.'
    test.random.seed(1)
    assert test.address() == '826 Ivaloo St.'
    test.random.seed(2)
    assert test.address() == '2190 Northland Plaza'
    test.random.seed(3)
    assert test.address() == '4499 Algoma Ave.'
    test.random.seed(4)
    assert test.address() == '5530 Route 1'
    test.random.seed(5)
    assert test.address() == '2890 Lower McDonald Ave. Apt. 154'

# Generated at 2022-06-13 23:42:01.347075
# Unit test for method address of class Address
def test_Address_address():
    pass

# Generated at 2022-06-13 23:42:01.927493
# Unit test for method address of class Address
def test_Address_address():
    pass

# Generated at 2022-06-13 23:42:24.293909
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')

    domain = 'es'
    add_es = Address(domain)

    address.seed(0)
    add_es.seed(0)

    assert address.address() == '311 South First Street Apt. 366'

    # 1º15'58"W
    lg = '-1.265833'
    # -40º6'17"N
    lt = '-40.104625'
    ba = 'Malvinas 5508 Apt. 844'

    # More complex test with random values in some fields.
    assert add_es.address() == f'{ba}, {lt} {lg}, {domain}'

# Generated at 2022-06-13 23:42:26.992212
# Unit test for method address of class Address
def test_Address_address():
    """ Test Address address """

    address = Address( 'zh_CN')

    assert address.address()

# Generated at 2022-06-13 23:42:29.946671
# Unit test for method address of class Address
def test_Address_address():
    class c:
        pass
    c.locale = Locale.en
    add = Address(c)
    assert add.address() != None


# Generated at 2022-06-13 23:42:32.433300
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    ad = Address()
    
    assert isinstance(ad.address(), str)
    assert len(ad.address()) > 0


# Generated at 2022-06-13 23:42:41.137553
# Unit test for method address of class Address

# Generated at 2022-06-13 23:42:55.128592
# Unit test for method address of class Address
def test_Address_address():
    import unittest
    import random
    import difflib
    # Debug messages
    # import sys
    # sys.tracebacklimit = 0

    class TestAddress(unittest.TestCase):
        address = Address(locale='en')

        def test_address(self):
            result = self.address.address()
            assert result is not None
            assert len(result) > 0
            if random.getrandbits(1):
                result = self.address.address(force_type='short')
                assert result is not None
                assert len(result) > 0
            if random.getrandbits(1):
                result = self.address.address(force_type='full')
                assert result is not None
                assert len(result) > 0

        def test_address_with_fail(self):
            result = self.address

# Generated at 2022-06-13 23:42:57.261481
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    address = provider.address()
    assert isinstance(address, str)


# Generated at 2022-06-13 23:42:59.629400
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())

# Generated at 2022-06-13 23:43:01.533288
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    # print(address.address())


# Generated at 2022-06-13 23:43:05.185946
# Unit test for method address of class Address
def test_Address_address():
    # Initialize Address()
    addr = Address()
    # method_name = address
    result = addr.address()
    assert result in addr._data["address_fmt"]

# Generated at 2022-06-13 23:43:32.495190
# Unit test for method address of class Address
def test_Address_address():
    assert Address.address()


# Generated at 2022-06-13 23:43:37.229448
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.builtins import Address

    addr = Address(Locale.EN)
    for i in range(10):
        ad = addr.address()
        assert '\n' not in ad
        assert '\t' not in ad


# Generated at 2022-06-13 23:43:38.622804
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() != a.address()


# Generated at 2022-06-13 23:43:42.891877
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    for i in range(4):
        address = Address(Locale('en'))
        assert len(address.address()) == len('123 Fake St. 33B')

    address = Address(Locale('ja'))
    assert len(address.address()) == len('京都市烏丸区上白檀町２丁目３−１４')


# Generated at 2022-06-13 23:43:47.074014
# Unit test for method address of class Address
def test_Address_address():
    add = Address()
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())



# Generated at 2022-06-13 23:43:49.448070
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    ad = Address('zh')
    res = ad.address()
    print(res)


# Generated at 2022-06-13 23:43:55.134895
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_num = address.street_number(maximum=9999)
    street_name = address.street_name()
    street_sfx = address.street_suffix()
    print('{} {} {}'.format(street_num, street_name, street_sfx))
    print(address.address())


# Generated at 2022-06-13 23:43:57.094595
# Unit test for method address of class Address
def test_Address_address():
    provider = Address('en')
    address = provider.address()
    assert type(address) == str


# Generated at 2022-06-13 23:44:05.733528
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address.

    :return: None.
    """
    address = Address()
    assert isinstance(address.address(), str)

    address = Address(seed=42)
    assert address.address() == '5506, Robel Mountains'
    assert address.address() == '5506, Robel Mountains'

    address = Address(seed='42')
    assert address.address() == '5506, Robel Mountains'
    assert address.address() == '5506, Robel Mountains'

    address = Address(locale='en-US')
    assert address.address() == '5506, Robel Mountains'
    assert address.address() == '5506, Robel Mountains'

    address = Address(locale='ja')
    assert address.address() == '22条西'


# Unit

# Generated at 2022-06-13 23:44:07.100698
# Unit test for method address of class Address
def test_Address_address():
    address = Address.address()
    assert type(address) is str


# Generated at 2022-06-13 23:45:22.200720
# Unit test for method address of class Address
def test_Address_address():
    assert len(Address().address()) > 1


# Generated at 2022-06-13 23:45:27.534106
# Unit test for method address of class Address
def test_Address_address():
    """Test for address method of Address class"""
    result = Address().address().split(",")
    assert len(result) == 2
    assert result[0] == '2792' or result[0] == '45'
    assert result[1] == ' Mozart Street' or result[1] == ' Dorian Road'


# Generated at 2022-06-13 23:45:30.253027
# Unit test for method address of class Address
def test_Address_address():
    address = Address("en")
    print("---new Address('en') address()---")
    print("address: ", address.address())


# Generated at 2022-06-13 23:45:32.620860
# Unit test for method address of class Address
def test_Address_address():
    p = Address('en')
    assert type(p.address()) is str
    assert p.address() == '1414 Ebony Hill, Meganland, 602210'

# Generated at 2022-06-13 23:45:37.229963
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    address = Address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()
    assert address.address()


# Generated at 2022-06-13 23:45:38.592913
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())
    # Output: '555 1st St'


# Generated at 2022-06-13 23:45:41.961575
# Unit test for method address of class Address
def test_Address_address():
    """Unit testing method address of class Address"""
    from pprint import pprint
    address = Address()
    a = address.address()
    assert a is not None, "Random address is null"
    pprint(a)


# Generated at 2022-06-13 23:45:57.943189
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())
# address = Address()
# print(address.address())
# print(address.country())
# print(address.city())
# print(address.state())
# print(address.latitude())
# print(address.longitude())
# print(address.coordinates())
# print(address.province())
# print(address.country_code())
# print(address.calling_code())
# print(address.continent())
# print(address.street_name())
# print(address.street_number())
# print(address.street_suffix())
# print(address.postal_code())
# print(address.zip_code())

# Generated at 2022-06-13 23:46:00.729260
# Unit test for method address of class Address
def test_Address_address():
    """A random full address."""
    assert Address().address()


# Generated at 2022-06-13 23:46:02.480711
# Unit test for method address of class Address
def test_Address_address():
    import random
    random.seed(10)
    assert Address().address() == 'Rua Amélia, 9'
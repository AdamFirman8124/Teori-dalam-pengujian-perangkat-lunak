

# Generated at 2022-06-13 23:39:48.752857
# Unit test for method address of class Address
def test_Address_address():
    import pytest
    from mimesis.enums import Locale
    from mimesis.providers.addresses import Address

    class TestAddressData:
        n = None
        fmt = None
        locale = None
        abbr = False


# Generated at 2022-06-13 23:39:51.484893
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()
    test_Address_address()

# Generated at 2022-06-13 23:39:54.283107
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    add = Address('zh-CN')
    a = add.address()
    print(a)

# Generated at 2022-06-13 23:39:58.926126
# Unit test for method address of class Address
def test_Address_address():
  address = Address()
  print(address.address()) # 56855 Dorton Bypass
  print(address.address()) # 56912 Brook Center
  print(address.address()) # 76534 Fayette Route
  print(address.address()) # 24977 North Junction
  print(address.address()) # 80950 North Glen
  print(address.address()) # 55583 East Trace
  print(address.address()) # 95480 Webster Highway
  print(address.address()) # 96952 Emmet Bypass
  print(address.address()) # 93938 Travis Course
  print(address.address()) # 51571 Chadwick Glen
  print(address.address()) # 13820 South Branch
  print(address.address()) # 25708 Skiles Place
  print(address.address()) # 72227 Derek Island
  print(address.address())

# Generated at 2022-06-13 23:40:00.924187
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    r = a.address()
    print(r)


# Generated at 2022-06-13 23:40:02.882804
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    address.address()

    # TODO: Add asserts

# Generated at 2022-06-13 23:40:13.674032
# Unit test for method address of class Address
def test_Address_address():
    import json
    import random
    import pytest
    import inspect
    import os
    import re
    import sys
    import pathlib
    import importlib
    import mimesis

    # Get path to directory which contains this file
    # and parent directory and then add to import paths
    # utility_dir_path = os.path.dirname(os.path.dirname(__file__))

    project_dir_path = pathlib.Path(__file__).parent.parent.absolute()

    sys.path.append(project_dir_path.as_posix())

    # Unit test for Address.address() method
    address = mimesis.Address('ru')

    method_name = 'address'

    result = address.address()

    # Init paths to files which contains actual values
    # pytest.fixture(scope='session

# Generated at 2022-06-13 23:40:16.881566
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    address = Address(locale='en')
    assert (address.address())[0] == '5'


# Generated at 2022-06-13 23:40:18.076592
# Unit test for method address of class Address
def test_Address_address():
    x = Address()
    for i in range(len(x.address())):
        assert len(x.address()) != 0

# Generated at 2022-06-13 23:40:19.749550
# Unit test for method address of class Address
def test_Address_address():
    assert Address('en').address()
    assert Address('ru').address()
    assert Address('zh').address()
    assert Address('ja').address()
    assert Address('de').address()
    assert Address('uk').address()
    assert Address('fr').address()


# Generated at 2022-06-13 23:40:34.175144
# Unit test for method address of class Address
def test_Address_address():
    # Generate a full address with locale=en
    locale='en'
    address = Address(locale=locale).address()
    # Example of address: '199 E. Street, Zanesville, NJ, 57854'
    print(address)
    # Check the type of address and print it
    assert isinstance(address, str)
    print(f'\naddress is type={type(address)}')

    # Generate a full address with locale=ko
    locale='ko'
    address = Address(locale=locale).address()
    # Example of address: '경기도 부천시 소사본동 790-5'
    print(address)
    # Check the type of address and print it
    assert isinstance(address, str)

# Generated at 2022-06-13 23:40:36.292319
# Unit test for method address of class Address
def test_Address_address():
    import re
    from mimesis import Address
    address = Address('en')
    assert re.match(r'\d+\s[\w ]+', address.address())

# Generated at 2022-06-13 23:40:45.479915
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import DataFields

    adr = Address('en')
    assert adr.address() == '39 Sycamore Street'
    assert adr.address(DataFields.FULL_ADDRESS) == '39 Sycamore Street'

    assert adr.address(DataFields.POSTAL_CODE) == '94124'
    assert adr.address(DataFields.CITY) == 'San Francisco'
    assert adr.address(DataFields.REGION) == 'CA'
    assert adr.address(DataFields.COUNTRY) == 'United States'



# Generated at 2022-06-13 23:40:48.134067
# Unit test for method address of class Address
def test_Address_address():

    from mimesis.exceptions import NonEnumerableError

    address = Address()
    assert type(address.address()) == str
    assert len(address.address()) > 0

    assert address.address() != address.address()

    address.address()

    fr_address = Address('fr')
    assert fr_address.address() != fr_address.address()

    with NonEnumerableError():
        address.address(form='lol')

# Generated at 2022-06-13 23:40:50.406214
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()

    assert result is not None



# Generated at 2022-06-13 23:40:51.498027
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    assert Address().address() != ''

# Generated at 2022-06-13 23:41:01.031851
# Unit test for method address of class Address
def test_Address_address():
    """Method for unit testing of address() method of class Address.
    """
    from mimesis.enums import Locale
    from copy import copy
    address = Address(Locale.EN)
    place = address.address()
    # Place must always remain the same for each locale
    # in order for the method to work correctly.
    assert place != address.address()
    en_address = copy(address)
    address = Address(Locale.RU)
    assert address.address() != en_address.address()
    address = Address(Locale.JA)
    assert address.address() != en_address.address()

# Generated at 2022-06-13 23:41:02.206175
# Unit test for method address of class Address
def test_Address_address():
    Address().address()


# Generated at 2022-06-13 23:41:04.578422
# Unit test for method address of class Address
def test_Address_address():
    obj = Address(seed=12345)
    expected = "980 Río de la Plata"
    result = obj.address()
    assert expected == result


# Generated at 2022-06-13 23:41:05.596057
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()


# Generated at 2022-06-13 23:41:13.934694
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='zh')
    assert address.address() != ''
    assert address.address() != ''
    assert address.address() != ''
    assert address.address() != ''


# Generated at 2022-06-13 23:41:18.114895
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    addr = provider.address()
    assert isinstance(addr, str)
    assert isinstance(provider.address(locale='en-EN'), str)
    assert isinstance(provider.address(locale='en_EN'), str)



# Generated at 2022-06-13 23:41:20.321810
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    assert a.address() == '1482 Anthony Port, Krystleborough'


# Generated at 2022-06-13 23:41:28.949174
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    address_list = [
        "Decemvirs Street",
        "LPT-283, Tiburtina Valeria",
        "2-Chome, Daikoku",
        "Rua Gualter Duarte",
        "Plakentias 21a",
        "Leytonstone Road",
        "Friedrichstraße",
        "boulevard d'Anjou",
    ]
    address = Address(Locale.EN, seed=1234567)

    assert address.address() in address_list

# Generated at 2022-06-13 23:41:33.027895
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    lst = [
        address.address()
        for _ in range(0, 10)
    ]
    assert len(lst) == 10



# Generated at 2022-06-13 23:41:35.416928
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert type(a.address()) == str

# Generated at 2022-06-13 23:41:44.954496
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    # {st_num} {st_name}
    adr.address()
    # {st_num} {st_name} {st_sfx}
    adr.address()
    # {st_num} {st_name} {st_sfx}, {city}, {state}, {zip}
    adr.address()
    # {st_num} {st_name} {st_sfx} {city}
    adr.address()
    # {st_num} {st_name} {st_sfx}, {city}
    adr.address()
    # {st_num} {st_name} {st_sfx}, {city} {zip}
    adr.address()

# Generated at 2022-06-13 23:41:49.329307
# Unit test for method address of class Address
def test_Address_address():
    try:
        assert isinstance(Address().address(), str)
    except AssertionError:
        raise AssertionError("Method test failed!")

    # Unit test for method street_number of class Address

# Generated at 2022-06-13 23:41:59.148908
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='ja')
    test_street_number = address.street_number()[0]
    assert len(test_street_number) == 4

    test_street_name = address.street_name()
    assert len(test_street_name) > 0

    test_street_suffix = address.street_suffix()
    assert len(test_street_suffix) > 0

    test_address = address.address()
    test_address_split = test_address.split()
    assert (test_street_number in test_address_split)
    assert (test_street_name in test_address_split)
    assert (test_street_suffix in test_address_split)


# Generated at 2022-06-13 23:42:09.864931
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    from mimesis.utils import get_locale

    locales = Locale.set() - {
        Locale.JA,
        Locale.ZH_CN,
        Locale.KO_KR,
        Locale.KM_KH,
        Locale.LO_LA,
    }
    pattern = (
        r'\d\d? \w+ \w+'
        r'|\d\d? \w+'
    )

    for locale in locales:
        address = Address(locale=get_locale(locale))
        assert re.fullmatch(pattern,
            address.address()) is not None


# Generated at 2022-06-13 23:42:20.415327
# Unit test for method address of class Address
def test_Address_address():
    a = Address(providers_locales=['es', 'en', 'ja', 'ru'])
    b = Address(seed=1)
    assert a.address() == 'Dirección de correo electrónico, calle después de 28'
    assert b.address() == '20, Olduar Avenue'



# Generated at 2022-06-13 23:42:22.987141
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis import Address
    ad = Address('en')
    print(ad.address())


# Generated at 2022-06-13 23:42:24.842942
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert type(result) == str


# Generated at 2022-06-13 23:42:34.814760
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""

# Generated at 2022-06-13 23:42:41.203047
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert addr.address() == 'Бориса Ельцина, 22'
    assert addr.address() == 'Вознесенский переулок, 51/8'
    assert addr.address() == 'Джамбул, 4513'
    assert addr.address() == 'Джамбул, 4513, 52'
    assert addr.address() == 'Джамбул, 4513, 52, 62'
    assert addr.address() == 'Джамбул, 4513, 52, 62, 19'

# Generated at 2022-06-13 23:42:43.040656
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    # print(a.address())
    pass


# Generated at 2022-06-13 23:42:51.175308
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    a = Address()
    st_num = a.street_number()
    st_name = a.street_name()
    st_suffix = a.street_suffix()
    address = a.address()
    assert '{}' not in address
    assert st_num in address
    assert st_name in address
    assert st_suffix in address


# Generated at 2022-06-13 23:42:53.077588
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert len(address.address()) > 0


# Generated at 2022-06-13 23:42:57.104683
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    Ad = Address(Locale.en)
    a = Ad.address()
    assert isinstance(a, str)
    #print(a)


# Generated at 2022-06-13 23:42:59.083210
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()


# Generated at 2022-06-13 23:43:13.122580
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    add = a.address()
    assert add
    assert isinstance(add, str)


# Generated at 2022-06-13 23:43:16.791880
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='pt-BR')
    result = address.address()
    assert type(result) == str


# Generated at 2022-06-13 23:43:23.672041
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import DatetimeFormat
    from mimesis.providers.datetime import Datetime
    from mimesis.tools import random_datetime

    address = Address('en')
    dt = Datetime(address.locale)
    dt_fmt = DatetimeFormat
    date = random_datetime(dt, min_year=2000, max_year=2018)
    print("\n**Testing Address.address()**")
    print("1. Full address in address_fmt: \n\t", address.address())
    print("2. Full address in address_ex_fmt \
(with Datetime format): \n\t", address.address(dt_fmt.DATE_SLASHES.value, date))

if __name__ == '__main__':
    test_Address_address

# Generated at 2022-06-13 23:43:28.891541
# Unit test for method address of class Address
def test_Address_address():
    a = Address()

    st_num = a.street_number()
    st_name = a.street_name()
    st_sfx = a.street_suffix()

    data = a.address()

    assert data == f'{st_num} {st_name} {st_sfx}'


# Generated at 2022-06-13 23:43:34.743896
# Unit test for method address of class Address
def test_Address_address():
    assert Address('zh').address() is not None
    """
    def test_Address_latitude(self):
        assert Address('en').latitude() is not None
        assert Address('en').latitude(dms=True) is not None

    def test_Address_longitude(self):
        assert Address('en').longitude() is not None
        assert Address('en').longitude(dms=True) is not None
    """


# Generated at 2022-06-13 23:43:42.300572
# Unit test for method address of class Address
def test_Address_address():
    add = Address("en")
    street_number = add.street_number()
    street_name = add.street_name()
    street_suffix = add.street_suffix()
    # print("street_number: %s | street_name: %s | street_suffix: %s" % (street_number, street_name, street_suffix))
    address = add.address()
    # print("address: %s" % address)
    assert isinstance(street_number, str)
    assert isinstance(street_name, str)
    assert isinstance(street_suffix, str)
    assert isinstance(address, str)



# Generated at 2022-06-13 23:43:47.466118
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('zh')
    result = addr.address()
    assert isinstance(result, str)
    assert len(result) >= 7

    addr = Address('zh')
    for i in range(100):
        assert isinstance(addr.address(), str) >= 7


# Generated at 2022-06-13 23:43:48.931675
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    print(addr.address())


# Generated at 2022-06-13 23:43:52.877975
# Unit test for method address of class Address
def test_Address_address():
    p = Address(seed=0)
    assert p.address() == '1216 W. Jenifer Street',\
        "'address()' method of 'Address' class with seed=0 should be 1216 W. Jenifer Street."


# Generated at 2022-06-13 23:43:58.316767
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()

    assert isinstance(addr.address(), str)
    assert isinstance(addr.address(thousand_separator=''), str)
    assert isinstance(addr.address(decimal_mark='.'), str)
    assert isinstance(addr.address(thousand_separator='', decimal_mark='.'), str)


# Generated at 2022-06-13 23:44:12.745507
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None


# Generated at 2022-06-13 23:44:21.220646
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.builtins import LatinAlphabet, RussianAlphabet

    lat_address = Address(Locale.EN)
    rus_address = Address(Locale.RU)

    for i in range(100):
        en_res = lat_address.address()
        assert isinstance(en_res, str)
        assert len(
            en_res.split(
                ' ')) >= 4
        assert en_res.replace(
            ' ', '').isalpha()
        assert en_res.replace(' ', '') == \
            "".join(
                i for i in en_res if i.isalpha())

    for i in range(100):
        ru_res = rus_address.address()
        assert isinstance(ru_res, str)

# Generated at 2022-06-13 23:44:33.719448
# Unit test for method address of class Address
def test_Address_address():

    addr = Address()
    assert addr.address() == '254 Hamilton Street'
    assert addr.address() == '375 Newkirk Avenue #579'
    assert addr.address() == '375 Newkirk Avenue #579'
    assert addr.address() == '1203 Hart Place'
    assert addr.address() == '6141 Avenue J'
    assert addr.address() == '2449 Maple Avenue'

    addr = Address(locale='ru')
    assert addr.address() == 'пр.Ленина, 309'
    assert addr.address() == 'ул.Магистральная, 34'
    assert addr.address() == 'ул.Красный проспект, 13'


# Generated at 2022-06-13 23:44:36.976556
# Unit test for method address of class Address
def test_Address_address():
    address1 = Address()
    address2 = Address()
    list1 = []
    for i in range(100):
        address = address1.address()
        list1.append(address)
    for i in range(100):
        address = address2.address()
        if address not in list1:
            assert False
    assert True


# Generated at 2022-06-13 23:44:38.777724
# Unit test for method address of class Address
def test_Address_address():
    assert len(Address().address()) >= 1


# Generated at 2022-06-13 23:44:41.043769
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    for i in range(100):
        assert child_validate('address', a.address())

# Generated at 2022-06-13 23:44:44.279471
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address."""
    test_obj = Address()
    result = test_obj.address()
    assert isinstance(result, str)



# Generated at 2022-06-13 23:44:58.523989
# Unit test for method address of class Address
def test_Address_address():
    seed = 0
    instance = Address(seed=seed)
    assert instance.address()=='Alfonso Sainz de Baranda, 13'
    assert instance.address()=='José de Entrala, 23'
    assert instance.address()=='Paseo de la Castellana, 65'
    assert instance.address()=='Plaza de España, 35'
    assert instance.address()=='Plaza del Carmen, 34'
    assert instance.address()=='Calle de Alcalá, 25'
    assert instance.address()=='Plaza del Callao, 24'
    assert instance.address()=='Calle de La Palma, 14'
    assert instance.address()=='Calle de Santa Isabel, 3'
    assert instance.address()=='Plaza de la Lealtad, 22'



# Generated at 2022-06-13 23:44:59.435049
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())

# Generated at 2022-06-13 23:45:05.930141
# Unit test for method address of class Address
def test_Address_address():
    # Given
    ad = Address()
    """
    When
    exectuing address()
    """
    result = ad.address()
    """
    Then
    address() should return string
    """
    assert isinstance(result, str)


# Generated at 2022-06-13 23:45:39.255452
# Unit test for method address of class Address
def test_Address_address():
    class Test:
        def __init__(self, locale):
            self.a = Address(locale)

        def address(self):
            return self.a.address()

        def address_with_name(self):
            return self.a.address()

    x = Test('en')
    y = Test('ru')
    z = Test('ja')
    assert (x.address() == y.address())
    assert (x.address() != y.address())
    assert (x.address() != z.address())
    assert (y.address() != z.address())



# Generated at 2022-06-13 23:45:40.129969
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    print(obj.address())

# Generated at 2022-06-13 23:45:42.449432
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    a = Address('en')
    assert a.address() is not None


# Generated at 2022-06-13 23:45:42.977339
# Unit test for method address of class Address
def test_Address_address():
    assert Address.address()


# Generated at 2022-06-13 23:45:45.381562
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for 'address' method from class Address."""
    addr = Address()
    print(addr.address())


# Generated at 2022-06-13 23:45:48.965600
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()
    print("testing Address class - address() - [OK]")

# Generated at 2022-06-13 23:46:09.941621
# Unit test for method address of class Address
def test_Address_address():
    from binascii import unhexlify
    from mimesis.builtins import hash_code
    from mimesis.providers import Address

    a = Address()

# Generated at 2022-06-13 23:46:14.687541
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address()"""
    adr = Address()
    # Locale "zh" uses a different address pattern than
    # all other locales, because of its unique address format.
    adr_pattern = SHORTENED_ADDRESS_FMT.get(adr.locale, '')
    if adr_pattern:
        adr_pattern += '#'
    assert adr.address() == adr.address(pattern=adr_pattern)
    assert all(map(lambda x: x, adr.address()))


# Generated at 2022-06-13 23:46:17.721568
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale="en")
    result = address.address()
    assert isinstance(result,str)

# Generated at 2022-06-13 23:46:19.193807
# Unit test for method address of class Address
def test_Address_address():
    for x in range(1, 10):
        print(Address(seed=x).address())

# Generated at 2022-06-13 23:47:26.043089
# Unit test for method address of class Address
def test_Address_address():
    result = Address('en').address()
    assert result is not None


# Generated at 2022-06-13 23:47:33.863436
# Unit test for method address of class Address
def test_Address_address():
    address_1 = Address(locale='zh')
    assert address_1.address() == '11-6-902'
    assert address_1.state() == '四川省'
    assert address_1.city() == '射洪'
    assert address_1.province() == '四川省'
    assert address_1.postal_code() == '615402'

    address_2 = Address(locale='ja')
    assert address_2.address() == '千代田区北の丸公園'
    assert address_2.state() == '東京都'
    assert address_2.city() == '東京都'
    assert address_2.province() == '東京都'

# Generated at 2022-06-13 23:47:37.565302
# Unit test for method address of class Address
def test_Address_address():
    """Test method Address.address."""
    a = Address()
    addr = a.address()
    assert isinstance(addr, str)
    assert len(addr) in range(5, 35)


# Generated at 2022-06-13 23:47:41.228994
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender
    from mimesis.builtins import Person
    import random
    address = Address()
    p = Person()
    p.name(gender=Gender.MALE)
    street_name = address.street_name()
    assert street_name in address.address()
    assert p.name(gender=Gender.MALE) not in address.address()


# Generated at 2022-06-13 23:47:42.225840
# Unit test for method address of class Address
def test_Address_address():
    Address().address()


# Generated at 2022-06-13 23:47:44.490039
# Unit test for method address of class Address
def test_Address_address():
    c = Address()
    for _ in range(10):
        address = c.address()
        assert address is not None



# Generated at 2022-06-13 23:47:48.649933
# Unit test for method address of class Address
def test_Address_address():
    _addr = Address(seed=1234)
    assert _addr.address() == '17865 W.Fulton Rd.' or \
           _addr.address() == '5049 West Fulton Rd.' or \
           _addr.address() == '692 W. Fulton Rd.'


# Generated at 2022-06-13 23:47:53.786885
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address method."""
    from mimesis.enums import Locale, CountryCode
    from mimesis.providers.address import Address
    from mimesis.typing import Generator
    locale = Locale.RU
    cntry = CountryCode.A2
    _gen = Generator()
    _addr = Address(_gen, locale=locale)
    assert _addr.address() != _addr.address()
    assert _addr.street_number() != _addr.street_number()
    assert _addr.street_name() != _addr.street_name()
    assert _addr.street_suffix() != _addr.street_suffix()
    assert _addr.region() != _addr.region()
    assert _addr.region(abbr=False) != _addr.region(abbr=True)

# Generated at 2022-06-13 23:47:57.471197
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:47:59.696336
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    add = Address()
    print(add.address())

# Generated at 2022-06-13 23:48:58.694081
# Unit test for method address of class Address
def test_Address_address():
    a = Address(provider='address', locales='en')
    assert a.address() == a.address()


# Generated at 2022-06-13 23:48:59.747121
# Unit test for method address of class Address
def test_Address_address():
    lc = Address()
    assert lc.address()


# Generated at 2022-06-13 23:49:05.686670
# Unit test for method address of class Address
def test_Address_address():
    # Given
    street_name = 'street_name'

    addr = Address(commands={'street_name': street_name})

    # When
    result = addr.address()

    # Then
    assert result == '1 {}'.format(street_name)



# Generated at 2022-06-13 23:49:10.565239
# Unit test for method address of class Address
def test_Address_address():
    locale = 'en'
    instance = Address(locale)
    result = instance.address()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:49:18.201446
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import AddressItem
    from mimesis.builtins import address
    from tests.utils import debug_print

    # debug_print(address.address())
    # debug_print(address.address(AddressItem.STREET_ADDRESS))
    # debug_print(address.address(AddressItem.STREET_NAME))
    # debug_print(address.address(AddressItem.CITY_NAME))
    debug_print(address.address(AddressItem.POSTAL_CODE))
    # debug_print(address.address(AddressItem.COUNTRY))
    # debug_print(address.address(AddressItem.COUNTRY_CODE))
    # debug_print(address.address(AddressItem.STATE_NAME))
    # debug_print(address.address(AddressItem.STATE_ABBR))

# Generated at 2022-06-13 23:49:31.770051
# Unit test for method address of class Address
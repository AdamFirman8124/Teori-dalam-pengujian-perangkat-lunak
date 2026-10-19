

# Generated at 2022-06-13 23:39:37.376285
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    from mimesis.enums import Locale

    ad = Address(Locale.EN)
    assert ad.address() in [
        '{st_num} {st_name} {st_sfx}'.format(
            st_num=ad.street_number(),
            st_name=ad.street_name(),
            st_sfx=ad.street_suffix(),
        ),
        '{st_num} {st_name}'.format(
            st_num=ad.street_number(),
            st_name=ad.street_name(),
        )]


# Generated at 2022-06-13 23:39:39.721927
# Unit test for method address of class Address
def test_Address_address():
    obj1 = Address()
    result = obj1.address()
    assert result is not None



# Generated at 2022-06-13 23:39:40.875563
# Unit test for method address of class Address
def test_Address_address():
    pass



# Generated at 2022-06-13 23:39:42.016567
# Unit test for method address of class Address
def test_Address_address():
    address_class = Address()
    assert isinstance(address_class.address(), str)


# Generated at 2022-06-13 23:39:44.892653
# Unit test for method address of class Address
def test_Address_address():
    """Test module Address.

    test method address of class Address
    """
    address = Address()
    assert address.address() is not None

# Generated at 2022-06-13 23:39:46.325425
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != ""
    assert Address().address() != None


# Generated at 2022-06-13 23:39:47.933066
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    for _ in range(20):
        assert address.address()


# Generated at 2022-06-13 23:39:48.571180
# Unit test for method address of class Address
def test_Address_address():
    add=Addr

# Generated at 2022-06-13 23:39:50.146950
# Unit test for method address of class Address
def test_Address_address():
    prv = Address()
    addr = prv.address()
    assert isinstance(addr, str)



# Generated at 2022-06-13 23:39:52.752384
# Unit test for method address of class Address
def test_Address_address():
    addr = Address(locale='en')

    res = addr.address()
    assert isinstance(res, str) and res



# Generated at 2022-06-13 23:40:00.311383
# Unit test for method address of class Address
def test_Address_address():
  address = Address()
  assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:40:03.087719
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    addr = a.address()
    assert (addr.count(' ') > 1)



# Generated at 2022-06-13 23:40:04.959853
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    print('Address: ', adr.address())



# Generated at 2022-06-13 23:40:08.219152
# Unit test for method address of class Address
def test_Address_address():
    a = Address(patcher=lambda n: n)
    assert a._data['address_fmt'] == '{st_num} {st_name} {st_sfx}'
    assert a.address() == "1 Rue des Abbesses"

# Generated at 2022-06-13 23:40:09.573326
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    # Create fake address
    for _i in range(10):
        print(address.address())


# Generated at 2022-06-13 23:40:18.518285
# Unit test for method address of class Address
def test_Address_address():
    import json
    import os
    import sys
    import unittest

    root_dir = os.path.dirname(os.path.dirname(__file__))
    if root_dir not in sys.path:
        sys.path.append(root_dir)

    import mimesis

    class AddressTestCase(unittest.TestCase):
        def setUp(self):
            self.add = mimesis.Address()
            self.add.seed(0)
            with open(os.path.join(root_dir, 'test_data_files', 'address.json'), encoding='utf-8') as f:
                self.add_data = json.load(f)

        def test_address(self):
            for _ in range(100):
                generated = self.add.address()

# Generated at 2022-06-13 23:40:22.396432
# Unit test for method address of class Address
def test_Address_address():
    
    import mimesis
    add = mimesis.Address('en')
    print(add.address())
    print(add.address())
    print(add.address())

# Generated at 2022-06-13 23:40:32.957918
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address()."""
    from collections import defaultdict
    from unittest import TestCase

    from mimesis.enums import Locale
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.address import Address

    class AddressTestCase(TestCase):

        def setUp(self):
            self.addr = Address(Locale.EN)

        def test_address(self):
            result = self.addr.address()
            pattern = r'\d{1,4} ' + r'[\w\- ]+' + '[( [\w\- ]+)]?'
            self.assertRegex(result, pattern)

        def test_address_other_locale(self):
            addr = Address(Locale.RU)
            result = addr.address()

# Generated at 2022-06-13 23:40:34.134359
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == '420 Stratford Terrace'


# Generated at 2022-06-13 23:40:40.963120
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address()."""
    from mimesis.enums import CountryCode
    from mimesis.providers.address import Address
    
    address_en_gb = Address(locale='en-gb')
    address_en_us = Address(locale='en-us')
    address_ru_ru = Address(locale='ru-ru')
    address_ja = Address(locale='ja')
    address_zh_cn = Address(locale='zh-cn')
    
    assert (address_zh_cn.address() == '1261QuanRoad')
    assert (address_en_gb.address() == '1444E. Kirk Avenue')
    assert (address_en_us.address() == '1334N. Smith Drive Apt. 27')

# Generated at 2022-06-13 23:40:58.542511
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    result = a.address()
    assert isinstance(result, str)


if __name__ == '__main__':
    # Unit test
    test_Address_address()

# Generated at 2022-06-13 23:40:59.433603
# Unit test for method address of class Address
def test_Address_address():
    address_obj = Address()
    assert isinstance(address_obj.address(), str)



# Generated at 2022-06-13 23:41:08.187793
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    from mimesis.typing import Seed
    from mimesis.providers.address import Address

    address_es_ES = Address('es-ES', Seed.create_seed(''))
    print(address_es_ES.country(allow_random=True))
    print(address_es_ES.address())

    address_en_US = Address('en-US', Seed.create_seed(''))
    print(address_en_US.country_code(CountryCode.A3))
    print(address_en_US.address())

    address_en_GB = Address('en-GB', Seed.create_seed(''))
    print(address_en_GB.country())
    print(address_en_GB.address())

# Generated at 2022-06-13 23:41:10.908517
# Unit test for method address of class Address
def test_Address_address():
    # Test value
    a = Address()

    assert a.address()

    a = Address('ja')
    assert a.address()


# Generated at 2022-06-13 23:41:13.411886
# Unit test for method address of class Address
def test_Address_address():
    """Test for method address."""
    address = Address()
    address_address = address.address()
    assert isinstance(address_address, str)
    assert len(address_address) > 0
    assert address_address.endswith('Street') or address_address.endswith('Road')


# Generated at 2022-06-13 23:41:15.265326
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:41:26.203442
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender

    a = Address('en')
    assert a.address().split()[0] == '1'

    a = Address()
    assert a.address().startswith('ул.') and 'пос.' in a.address()

    a = Address('be')
    assert (a.address().startswith(
        f'{a.random.choice(Gender.MALE)} Суздальская') or
        a.address().startswith(
        f'{a.random.choice(Gender.FEMALE)} Суздальская'))

    a = Address('ja')
    assert ' ' not in a.address()

    a = Address()
    assert ' ' not in a.address()


#

# Generated at 2022-06-13 23:41:28.058462
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    data = address.address()
    assert isinstance(data, str)

# Generated at 2022-06-13 23:41:39.679918
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    for _ in range(1000):
        st_name, st_num, st_sfx = \
            address.street_name(), address.street_number(), \
            address.street_suffix()

        if address.locale in SHORTENED_ADDRESS_FMT:
            assert any(
                # Make sure a street name and a street number are
                # present in the address.
                st_name in address.address() and
                st_num in address.address()
            )
            continue

        if address.locale == 'ja':
            address.address()
            continue


# Generated at 2022-06-13 23:41:41.073999
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)


# Generated at 2022-06-13 23:42:11.628557
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    a = Address()
    assert len(a.address()) > 0


# Generated at 2022-06-13 23:42:14.917179
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('pt-br').address()
    print(addr)
    assert isinstance(addr, str)
    assert addr

# Generated at 2022-06-13 23:42:16.695804
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    # No assertion needed, just useful to check if code is OK
    print(a.address())

# Generated at 2022-06-13 23:42:27.416647
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.exceptions import NonEnumerableError
    from mimesis.enums import CountryCode
    from random import random
    from copy import copy
    from os import environ
    from mimesis.providers.address import Address
    from mimesis.providers.utils import get_locale

    a = Address(environ.get('LOCALE'))
    test_data = [
        ('', ''),
        ('address_fmt', ''),
        ('postal_code_fmt', ''),
        ('country', ''),
        ('city', ''),
        ('street', ''),
        ('state', ''),
    ]
    for key, val in test_data:
        a._datafile = ''
        a._data = {'x': 'x'}
        a._data[key] = val


# Generated at 2022-06-13 23:42:34.411600
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == 'Forsthausstraße 3'
    assert Address('en').address() == '159 W. Ash St.'
    assert Address('fr').address() == '4, Rue du Lac'
    assert Address('ru').address() == 'пер. Осипенко, д. 77'
    assert Address('zh').address() == '桂法街 8 号'
    assert Address('ja').address() == '福島県 土商戸 ケロリ'


# Generated at 2022-06-13 23:42:36.666257
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    for locale in Locale:
        print(Address(locale).address())

if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:42:37.994446
# Unit test for method address of class Address
def test_Address_address():
    state = Address('en')
    Address_address = state.address()
    assert isinstance(Address_address, str)

# Generated at 2022-06-13 23:42:39.383258
# Unit test for method address of class Address
def test_Address_address():
    address = Address('zh')
    assert address.address() != []

#Unit test for method street_number of class Address

# Generated at 2022-06-13 23:42:53.962358
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    assert Address().address() == '{}, {}'.format(Address().street_number(),
                                                  Address().street_name())
    assert Address(locale='it').address() == '{} {}'.format(
        Address().street_number(),
        Address().street_name(),
    )
    assert Address(locale='ja').address() == '{} {}'.format(
        Address().city(),
        Address().random.custom_code('###'),
    )
    assert Address(locale='es').address() == '{} {} {}'.format(
        Address().street_number(),
        Address().street_name(),
        Address().street_suffix(),
    )

# Generated at 2022-06-13 23:43:01.221283
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode

    address = Address('en')
    assert address.address() == '114 E North St'

    assert address.address_random_country() == '18-27 E North St'

    address.seed(1)
    assert address.address() == '305 N Main St, Oak Ridge, Tennessee, 37830'

    address = Address('ru')
    address.seed(1)
    print(address.address())
    assert address.address() == 'ул. Пре-да, д. 19, оф. 7'

    address = Address('nl')
    address.seed(1)
    assert address.address() == 'Kennelijkweg 46'

    address.seed(1)
    address.set_locale('en')


# Generated at 2022-06-13 23:44:13.421026
# Unit test for method address of class Address
def test_Address_address():
    import random
    import pytest
    from mimesis.enums import Locale

    # Test locale
    locale = Locale.EN
    # Seed to get the same number every run
    seed = 0
    # Initialize the class
    address = Address(random.Random(seed), locale)

    # Test the method address
    test_address = address.address()

    # Test the address
    assert test_address == '238 Buell Street'



# Generated at 2022-06-13 23:44:15.762216
# Unit test for method address of class Address
def test_Address_address():
    print('Address.address()')
    addr = Address(random_locale=True)
    print(addr.address())



# Generated at 2022-06-13 23:44:22.277242
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert addr.street_number() != 0
    assert addr.street_name() != ""
    street = addr.address()
    assert street.find(".") == -1
    assert street.find("Street") == -1
    print("Method address passed test")

# Generated at 2022-06-13 23:44:24.566532
# Unit test for method address of class Address
def test_Address_address():
    addr = Address(locale='en')
    address = addr.address()
    assert isinstance(address, str)

# Generated at 2022-06-13 23:44:28.537201
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('en')
    get_address = addr.address()
    assert isinstance(get_address,str)
    assert len(get_address) > 0


# Generated at 2022-06-13 23:44:31.457040
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    add = Address("fa")
    assert add.address() is not None

# Generated at 2022-06-13 23:44:34.723337
# Unit test for method address of class Address
def test_Address_address(): 
    from pdb import set_trace; set_trace()
    from mimesis.builtins import Address

    uk_addr = Address('uk')
    print(uk_addr.address())


# Generated at 2022-06-13 23:44:38.525067
# Unit test for method address of class Address
def test_Address_address():
    address_obj=Address(locale='en')
    assert address_obj.address()=="12257 N. Eagan Haven" or "12257 N. Eagan Haven" in address_obj.address()


# Generated at 2022-06-13 23:44:40.791457
# Unit test for method address of class Address
def test_Address_address():
    generator = Address('ja')
    assert generator.address()
    assert isinstance(generator.address(), str)

# Generated at 2022-06-13 23:44:43.618649
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    a = Address()
    assert isinstance(a.address(), str)

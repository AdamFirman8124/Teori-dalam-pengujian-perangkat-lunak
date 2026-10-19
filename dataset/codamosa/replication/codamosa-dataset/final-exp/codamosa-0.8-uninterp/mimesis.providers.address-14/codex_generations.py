

# Generated at 2022-06-13 23:39:49.779896
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.utils import generate_seed
    from mimesis.enums import Location
    from mimesis.providers.address import Address

    seed = generate_seed(12)
    a = Address(seed)
    address = a.address()
    assert type(address) == str
    assert len(address) > 2
    print(address)

    a = Address(seed, locale = Location.US)
    address = a.address()
    assert type(address) == str
    assert len(address) > 2
    print(address)


# Generated at 2022-06-13 23:40:00.774865
# Unit test for method address of class Address
def test_Address_address():
    from random import choice

    from pprint import pprint
    from mimesis import Address, Person
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider

    # Create Russian provider for generate name in Russian.
    russian = RussiaSpecProvider()

    # Create Address object
    address = Address('ru')
    person = Person('ru', gender=Gender.FEMALE)

    # Generate a random street number
    print(address.street_number())

    # Generate a random full address
    print(address.address())
    pprint(russian.address())

    # Generate a postal code
    print(address.postal_code())

    # Generate a zip code
    print(address.zip_code())

    # Get a random calling code of random country

# Generated at 2022-06-13 23:40:12.240665
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    # Result for locale "en"
    assert Address('en').address() == '{} {} {}'.format(
        Address('en').street_number(),
        Address('en').street_name(),
        Address('en').street_suffix(),
    )

    # Result for locale "ru"
    assert Address('ru').address() == '{} {}'.format(
        Address('ru').street_name(),
        Address('ru').street_number(),
    )

    # Result for locale "ja"

# Generated at 2022-06-13 23:40:19.665564
# Unit test for method address of class Address
def test_Address_address():
    """Test for generate address"""
    address_1 = Address()
    print(address_1.address())
    # '201 Rodgers Junction'

    address_2 = Address(locale = 'zh')
    print(address_2.address())
    # '罗科港城市站'

if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:40:21.700320
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())



# Generated at 2022-06-13 23:40:23.767597
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='zh')
    address.address()

# Generated at 2022-06-13 23:40:29.117560
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis.local import Local
    ln = Local('en')
    address = Address(local = 'en')
    address.address()
    assert address.address() == address.street_number() + " " + address.street_name()
    
    

# Generated at 2022-06-13 23:40:30.433374
# Unit test for method address of class Address
def test_Address_address():
    provider = Address('en')
    assert provider.address()


# Generated at 2022-06-13 23:40:34.736539
# Unit test for method address of class Address
def test_Address_address():
    # Assert for default behaviour
    a = Address('en')
    s = a.address()
    assert s is not None
    assert len(s) > 0

    # Assert for japan behaviour
    a = Address('ja')
    s = a.address()
    assert s is not None
    assert len(s) > 0


# Generated at 2022-06-13 23:40:35.913422
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    print(addr.address())


# Generated at 2022-06-13 23:40:47.695766
# Unit test for method address of class Address
def test_Address_address():
    d.address()
    d.address()
    d.address()
    d.address()
    d.address()
    d.address()
    d.address()
    d.address()
    d.address()
    d.address()
    d.address()


# Generated at 2022-06-13 23:40:50.341737
# Unit test for method address of class Address
def test_Address_address():
    """Test function"""
    address = Address()
    print(address.address())
    print(address.address())
    print(address.address())
    print(address.address())


# Generated at 2022-06-13 23:40:52.012894
# Unit test for method address of class Address
def test_Address_address():
    import mimesis
    address = mimesis.Address()

    result = address.address()
    assert result



# Generated at 2022-06-13 23:40:53.345044
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    address = provider.address()

    assert address



# Generated at 2022-06-13 23:40:55.597764
# Unit test for method address of class Address
def test_Address_address():
    assert len(Address().address())>0


# Generated at 2022-06-13 23:41:00.803448
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address()."""
    from mimesis import Address
    from mimesis.enums import CountryCode

    a = Address()
    data_set = [
        (a.address(), 'en'),
        (a.address(), None),
    ]

    if a.locale.startswith('en'):
        data_set.append(
            (a.address(), 'scotland'),
        )

    for i in data_set:
        # print(i[1], i[0])
        a = Address(i[1])

        address = a.address()
        st_num = a.street_number()
        st_name = a.street_name()
        st_sfx = a.street_suffix()

# Generated at 2022-06-13 23:41:03.063407
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.address()
    assert address != None
    assert isinstance(address, str)


# Generated at 2022-06-13 23:41:04.495625
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address().address()


# Generated at 2022-06-13 23:41:08.022057
# Unit test for method address of class Address
def test_Address_address():
    """Test method address in class Address."""
    a = Address()
    res = a.address()
    assert len(res) > 1
    assert isinstance(res, str)


# Generated at 2022-06-13 23:41:10.094616
# Unit test for method address of class Address
def test_Address_address():
    provider = Address(locale='en')
    result = provider.address()
    assert result



# Generated at 2022-06-13 23:41:27.795486
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    a = Address(locale=Locale.US)
    assert a.address() == '1207 E James Ave'

# Generated at 2022-06-13 23:41:37.411680
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    # 1.Default locale
    addr = Address()
    
    assert addr.address() == '1410 Deron Heights'
    assert addr.address() == '2536 Fritsch Parkway'

    # 2. Different locale
    addr = Address(locale = Locale.RU)
    assert addr.address() == '1207 Киселевский Вал, дом 32'

    addr = Address(locale = Locale.JA)
    assert addr.address() == '江東区 北三条東 二丁目 七番地'
    

# Generated at 2022-06-13 23:41:46.308585
# Unit test for method address of class Address
def test_Address_address():
    class testClazz:
        def __init__(self,locale):
            self._datafile = 'address.json'
            self.locale = locale

        def _pull(self,datafile):
            self._data = {}
            self._load_data_into(self._data,datafile)

    # en
    test_obj = testClazz('en')
    test_obj._pull(test_obj._datafile)
    obj = Address(test_obj)
    assert obj.address()!=None
    print(obj.address())
    # zh
    test_obj = testClazz('zh')
    test_obj._pull(test_obj._datafile)
    obj = Address(test_obj)
    assert obj.address()!=None
    print(obj.address())


# Generated at 2022-06-13 23:41:49.648991
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    result = ad.address()
    assert isinstance(result, str)



# Generated at 2022-06-13 23:41:51.309417
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()


# Generated at 2022-06-13 23:41:58.599217
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode

    a = Address()
    print(a.address())
    print(a.street_number())
    print(a.street_name())
    print(a.street_suffix())

    a = Address('ru')
    print(a.state())
    print(a.postal_code())

    print(a.country_code())
    print(a.country_code(CountryCode.A3))

    print(a.country())

    a = Address('en')
    print(a.city())

# Generated at 2022-06-13 23:42:09.101392
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    add = Address(seed=0)
    add.seed(0)
    assert add.address() == '1223 Baker Street'

    add.locale('de')
    assert add.address() == '1223 Baker Street'

    add.locale('ru')
    assert add.address() == '1223 Baker Street'

    add.locale('ru')
    assert add.address() == '1223 Baker Street'

    add.locale('en-US')
    assert add.address() == '1223 Baker Street'

    add.locale('it')
    assert add.address() == 'Via Baker, 1223'

    add.locale('it-IT')
    assert add.address() == 'Via Baker, 1223'

    add.locale('es')

# Generated at 2022-06-13 23:42:11.628553
# Unit test for method address of class Address
def test_Address_address():
    """
    Test Address.address()
    """
    address = Address()
    print(address.address())
    print("######")



# Generated at 2022-06-13 23:42:18.936007
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import EN
    from mimesis.enums import CountryCode

    address = Address(locale='en')
    assert isinstance(address.address(), str)

    fmt = EN().address.address()
    us = Address(locale='ru')
    assert us.address() == fmt

    assert len(Address().country_code(CountryCode.A2)) == 2
    assert len(Address().country_code(CountryCode.A3)) == 3

    assert country in Address().country(allow_random=True)

# Generated at 2022-06-13 23:42:23.040453
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_number = address.street_number()
    street_name = address.street_name()
    street_suffix = address.street_suffix()
    assert '{} {} {}'.format(street_number, street_name, street_suffix) == address.address()


# Generated at 2022-06-13 23:42:59.753302
# Unit test for method address of class Address
def test_Address_address():
    instance = Address()
    assert isinstance(instance.address(), str)
    assert isinstance(instance.city(), str)
    assert isinstance(instance.city(), str)
    assert isinstance(instance.continent(), str)
    assert isinstance(instance.continent(code=True), str)
    assert isinstance(instance.country_code(), str)
    assert isinstance(instance.country_code(CountryCode.A2), str)
    assert isinstance(instance.country_code(CountryCode.A3), str)
    assert isinstance(instance.country_code(CountryCode.NUMERIC), str)
    assert isinstance(instance.state(), str)
    assert isinstance(instance.state(abbr=True), str)



# Generated at 2022-06-13 23:43:02.871500
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    # Every time returns different value.
    assert address.address() != address.address()


# Generated at 2022-06-13 23:43:17.180715
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    from mimesis.enums import CountryCode

    adr = Address('en')
    print(adr.address())
    print(adr.address())
    print(adr.address())
    print(adr.address())

    adr_fr = Address('fr')
    print(adr_fr.address())
    print(adr_fr.address())

    adr_cs = Address('cs')
    print(adr_cs.address())
    print(adr_cs.address())
    print(adr_cs.address())
    print(adr_cs.address())

    adr_de = Address('de')
    print(adr_de.address())
    print(adr_de.address())
    print(adr_de.address())
    print(adr_de.address())

    ad

# Generated at 2022-06-13 23:43:18.964269
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    provider = Address(Locale.EN)
    assert provider.address() != ""

# Generated at 2022-06-13 23:43:20.970222
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    street = a.address()
    result = all(item in street for item in [a.street_number(), a.street_name().replace("'", "")])
    assert result

# Generated at 2022-06-13 23:43:23.240326
# Unit test for method address of class Address
def test_Address_address():
    a = Address(seed=42)
    assert a.address() == '251 Alberta Terrace'

# Generated at 2022-06-13 23:43:24.232145
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    print(address.address())
    print('\n')


# Generated at 2022-06-13 23:43:29.005542
# Unit test for method address of class Address
def test_Address_address():
    data = Address('en')
    address_1 = data.address()
    address_2 = data.address()

    assert type(address_1) == type(address_2) == str
    assert '\n' in address_1
    assert '\n' in address_2


# Generated at 2022-06-13 23:43:29.949204
# Unit test for method address of class Address
def test_Address_address():
    assert isinstance(Address().address(), str)

# Generated at 2022-06-13 23:43:31.455837
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None


# Generated at 2022-06-13 23:44:02.210504
# Unit test for method address of class Address
def test_Address_address():
    same_string = []
    for _ in range(4):
        same_string.append(Address().address())
    assert len(set(same_string))==1

# Generated at 2022-06-13 23:44:03.061181
# Unit test for method address of class Address
def test_Address_address():
    assert len(Address().address())==5

# Generated at 2022-06-13 23:44:04.937834
# Unit test for method address of class Address
def test_Address_address():
    """Random address."""
    address = Address(locale='zh')
    assert address.address()

# Generated at 2022-06-13 23:44:06.214960
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:44:09.585493
# Unit test for method address of class Address
def test_Address_address():
    print("Generate Address#address()")
    address = Address(random_state=0)
    assert address.address() == "600 Aberdeen Ave"

# Generated at 2022-06-13 23:44:17.006163
# Unit test for method address of class Address
def test_Address_address():
    from .code import Code
    code = Code()

    # Locales after 'el' contain full address formats.
    for locale in code.locales[6:]:
        addr = Address(locale=locale)
        assert len(addr.address()) > 0

    # The remaining locales have address formats without street suffix.
    for locale in code.locales[:6]:
        address = Address(locale=locale).address()
        assert len(address) > 0 and 'street_suffix' not in address


# Generated at 2022-06-13 23:44:22.151501
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    # Generate new object of class Address
    address = Address()
    # Get some random address
    result = address.address()
    assert result == '1400 Northpoint Parkway'


# Generated at 2022-06-13 23:44:22.914839
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()

# Generated at 2022-06-13 23:44:24.691040
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address().address()


# Generated at 2022-06-13 23:44:28.677298
# Unit test for method address of class Address
def test_Address_address():
    for _ in range(100):
        addr = Address('ru').address()
        assert addr is not None

assert Address.address() is not None


# Generated at 2022-06-13 23:45:13.524517
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    b = a.address()
    assert bool(b)



# Generated at 2022-06-13 23:45:17.043243
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_address = address.address()
    assert street_address != None
    assert isinstance(street_address, str)


# Generated at 2022-06-13 23:45:20.172367
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert isinstance(addr.address(), str)
    return addr.address()

if __name__ == "__main__":
    print(test_Address_address())

# Generated at 2022-06-13 23:45:21.647850
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    d = a.address()
    assert isinstance(d, str)

# Generated at 2022-06-13 23:45:23.577238
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    x = address.address()
    assert type(x) == str


# Generated at 2022-06-13 23:45:25.597059
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    print(address.address())


# Generated at 2022-06-13 23:45:38.166896
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.address import Address

    a = Address()
    assert a.address() != a.address()
    _ = a.country_code(CountryCode.A2)
    _ = a.country_code(CountryCode.A3)
    _ = a.country_code(CountryCode.NUMERIC)
    with pytest.raises(NonEnumerableError):
        _ = a.country_code('💩')
    _ = a.code
    _ = a.city
    _ = a.continent
    _ = a.postal_code
    _ = a.region
    _ = a.state
    _ = a.street_name
    _ = a.street_number
   

# Generated at 2022-06-13 23:45:57.940192
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() == "מספר רחוב 1 שם רחוב"
    assert a.address() == "מספר רחוב 1 שם רחוב"
    assert a.address() == "מספר רחוב 1 שם רחוב"
    assert a.address() == "מספר רחוב 1 שם רחוב"
    assert a.address() == "מספר רחוב 1 שם רחוב"

# Generated at 2022-06-13 23:46:09.981373
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    address = provider.address()
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"
    assert address == "Zimmerman Straße, 6985"

# Generated at 2022-06-13 23:46:10.829298
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    address.address()

# Generated at 2022-06-13 23:46:58.019545
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.exceptions import NonEnumerableError
    from mimesis.enums import CountryCode
    from mimesis.providers.address import Address
    a = Address()

    # Default locale
    value = a.address()
    assert isinstance(value, str)
    assert len(value) > 10

    # Custom locale, city names in English
    value = a.address(locale='be')
    assert isinstance(value, str)
    assert len(value) > 10

    # Custom locale, city names in Russian
    value = a.address(locale='ru')
    assert isinstance(value, str)
    assert len(value) > 10

    # Custom locale, city names in Japanese
    value = a.address(locale='ja')
    assert isinstance(value, str)

# Generated at 2022-06-13 23:47:00.016226
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    test_address = address.address()
    assert len(test_address) > 5

# Generated at 2022-06-13 23:47:13.642892
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    add = Address()
    assert isinstance(add.address(), str)
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()
    assert add.address() != add.address()


# Generated at 2022-06-13 23:47:16.669254
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())
    print(Address(locale='ko').address())
    print(Address(locale='ja').address())
    print(Address(locale='ko').address())


# Generated at 2022-06-13 23:47:20.049800
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    resultset = []
    for i in range(100):
        obj = Address()
        resultset.append(obj.address())
        print(resultset[i])



# Generated at 2022-06-13 23:47:20.883956
# Unit test for method address of class Address
def test_Address_address():
    assert Address()


# Generated at 2022-06-13 23:47:30.064741
# Unit test for method address of class Address
def test_Address_address():
    import sys
    import random
    if random.randint(1,4) == 1:
        sys.exit(0)
    import pytest
    from mimesis.enums import Country
    from mimesis.providers.address import Address
    from mimesis.utils import Token

# Generated at 2022-06-13 23:47:32.997302
# Unit test for method address of class Address
def test_Address_address():
    address = Address("en")
    print("full address: ", address.address())
    print("street_number: ", address.street_number())
    print("street_name: ", address.street_name())
    print("street_suffix: ", address.street_suffix())


# Generated at 2022-06-13 23:47:38.120714
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    locale = 'zh'
    local_address = Address(locale=locale)
    address = local_address.address()

    assert ' ' in address
    assert address[0].isdigit()


# Generated at 2022-06-13 23:47:50.079378
# Unit test for method address of class Address
def test_Address_address():
    """Test for Address.address()"""
    from mimesis.enums import Locale
    from mimesis.enums import AddressFormats as AF


# Generated at 2022-06-13 23:48:23.957983
# Unit test for method address of class Address
def test_Address_address():
    address_test = Address()
    result = address_test.address()
    assert result

# Generated at 2022-06-13 23:48:26.441318
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address()
    assert address.address() is not None
    assert type(address.address()) == str


# Generated at 2022-06-13 23:48:27.609213
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    address.address()
    # =》'814 Shoshone Place'


# Generated at 2022-06-13 23:48:31.069895
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert ' ' in addr.address()
    assert addr.street_number().isnumeric()


# Generated at 2022-06-13 23:48:32.728875
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address_provider = Address()

    assert address_provider.address()


# Generated at 2022-06-13 23:48:35.876218
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    assert address.address()
    assert address.address()
    assert address.address()



# Generated at 2022-06-13 23:48:39.700718
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    b = Address()
    result = a.address()

    assert a.address() != b.address()
    assert isinstance(result, str)

# Generated at 2022-06-13 23:48:43.064873
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    ad = a.address()
    assert isinstance(ad, str)
    assert ad.strip()


# Generated at 2022-06-13 23:48:56.390143
# Unit test for method address of class Address
def test_Address_address():
    # Version 1
    import json
    import os
    import sys
    import unittest

    basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    sys.path.append(basepath)

    from mimesis.builtins import Address as Address_

    class AddressTestCase(unittest.TestCase):
        """Test case for Address class."""

        def setUp(self):
            """Set up for test."""
            self.address = Address_()

        def test_address(self):
            """Test Address.address."""
            pattern = self.address.pattern('address_fmt')

            for locale in self.address.available_locales:
                self.address.set_locale(locale)

# Generated at 2022-06-13 23:48:58.917456
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address_class = Address('en')
    assert address_class.address() == '2836 Raymond Court'

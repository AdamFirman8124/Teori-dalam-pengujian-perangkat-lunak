

# Generated at 2022-06-13 23:39:41.574785
# Unit test for method address of class Address
def test_Address_address():
    """Testing address method."""
    address = Address()
    addr = address.address()
    assert isinstance(addr, str)
    assert len(addr.split('\n')) > 0



# Generated at 2022-06-13 23:39:48.656747
# Unit test for method address of class Address
def test_Address_address():
    a = Address(seed=1234)
    # Random address from en locale
    assert a.address() == '920 Manley Orchard\n'
    # Random address from ru locale
    b = Address('ru')
    assert b.address() == 'улица Бориса Богданова\n'
    # Random address from zh locale
    c = Address('zh')
    assert c.address() == '18号\n'



# Generated at 2022-06-13 23:39:50.853789
# Unit test for method address of class Address
def test_Address_address():
    assert type(Address.address()) is str
    assert Address.address() in Address._data['street']['name']
    assert Address.address() != Address.address()


# Generated at 2022-06-13 23:39:57.381578
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import RegionCode

    # init Address class
    address1 = Address('en')
    address2 = Address('ru')

    assert isinstance(address1, Address)

    # get address, if locale is en
    assert address1.address()
    # locale is ru and address contain region id
    assert address2.address(region_code=RegionCode.IN)

# Generated at 2022-06-13 23:39:58.532973
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()


# Generated at 2022-06-13 23:40:00.995481
# Unit test for method address of class Address
def test_Address_address():
    # arrange
    address = Address()

    # act
    result = address.address()

    # assert
    assert type(result) is str
    assert len(result) == 11

# Generated at 2022-06-13 23:40:04.642765
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    st_num = address.street_number()
    st_name = address.street_name()

    result = address.address()
    assert result == st_num + ' ' + st_name

# Generated at 2022-06-13 23:40:05.968607
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:40:07.470807
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:40:09.759212
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    assert(len(address.address().split(' ')) == 3)


# Generated at 2022-06-13 23:40:16.313509
# Unit test for method address of class Address
def test_Address_address():
    result =  Address().address()
    assert result
    assert not isinstance(result, Address)


# Generated at 2022-06-13 23:40:30.348988
# Unit test for method address of class Address

# Generated at 2022-06-13 23:40:31.267913
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()

# Generated at 2022-06-13 23:40:33.254233
# Unit test for method address of class Address
def test_Address_address():
    address=Address('en')
    print(address.address())
    #57380 Blevins Branch


# Generated at 2022-06-13 23:40:36.588595
# Unit test for method address of class Address
def test_Address_address():
    from mimesis_address_ko import Address as Address_ko
    from mimesis_address_tr import Address as Address_tr
    from mimesis_address_en import Address as Address_en

    assert Address_en().address() != Address_ko().address() != Address_tr().address()


# Generated at 2022-06-13 23:40:38.713937
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    address = provider.address()
    assert isinstance(address, str)

# Generated at 2022-06-13 23:40:49.317188
# Unit test for method address of class Address
def test_Address_address():
    print("\n### test_Address_address() ###")

    from random import choice

    from mimesis import Address

    address = Address('en')
    address_fmt = address._data['address_fmt']

    for _ in range(10):
        st_num = address.street_number()
        st_name = address.street_name()

        if address.locale in SHORTENED_ADDRESS_FMT:
            print(address_fmt.format(
                st_num=st_num,
                st_name=st_name,
            ))


# Generated at 2022-06-13 23:40:51.073799
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    print(Address(Locale('en')).address())


# Generated at 2022-06-13 23:40:52.289071
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.address()
    assert address is not None


# Generated at 2022-06-13 23:40:53.467071
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())



# Generated at 2022-06-13 23:41:00.423463
# Unit test for method address of class Address
def test_Address_address():
    print("---test_Address_address---")
    a = Address(local='es')
    print(a.address())
    print()



# Generated at 2022-06-13 23:41:01.883301
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == '1064 Tabor Ln.'



# Generated at 2022-06-13 23:41:04.295783
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    assert '{} {} {}'.format(address.street_number(), address.street_name(), address.street_suffix()) == address.address()

# Generated at 2022-06-13 23:41:06.061119
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    addr = address.address()
    assert isinstance(addr, str)


# Generated at 2022-06-13 23:41:07.970856
# Unit test for method address of class Address
def test_Address_address():
    address = Address('fr')
    assert isinstance(address.address(), str)

# Generated at 2022-06-13 23:41:10.804067
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    data = address.address()
    assert isinstance(data, str)
    assert data



# Generated at 2022-06-13 23:41:13.004750
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    address.random.seed(42)
    assert address.address() == '362 Jast Parkways'


# Generated at 2022-06-13 23:41:17.644015
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    assert address.address() == "3491 Efren Street"
    address = Address(locale='ja')
    assert address.address() == "鹿児島市中央区大手町5－5－5"

# Generated at 2022-06-13 23:41:18.514204
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != address

# Generated at 2022-06-13 23:41:30.105338
# Unit test for method address of class Address
def test_Address_address():
    print("test for address of class Address")
    print("\n--------Start--------")
    print("locale : tu")
    a = Address(locale="tu") # Test-specific locale
    print(a.address())
    print("\n")
    print("locale : en-US")
    b = Address(locale="en-US")
    print(b.address())
    print("\n")
    print("locale : ch-CH")
    c = Address(locale="ch-CH")
    print(c.address())
    print("\n")
    print("locale : zh-CN")
    d = Address(locale="zh-CN")
    print(d.address())
    print("\n")
    print("locale : en-CA")

# Generated at 2022-06-13 23:41:41.240458
# Unit test for method address of class Address
def test_Address_address():
    _address = Address(locale='ja')
    addr = _address.address()
    assert(addr == '表司{1}丁目　{2}番地')
    addr = _address.address()
    assert(addr == '表司{1}丁目　{2}番地')

# Generated at 2022-06-13 23:41:43.604700
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    assert ad.street_number() is not None
    assert ad.street_name() is not None
    assert ad.street_suffix() is not None
    assert ad.address() is not None

# Generated at 2022-06-13 23:41:44.937461
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    assert type(obj.address()) == str



# Generated at 2022-06-13 23:41:47.089952
# Unit test for method address of class Address
def test_Address_address():
    # Unit tests for method address of class Address
    address = Address()
    address.address()



# Generated at 2022-06-13 23:41:48.223132
# Unit test for method address of class Address
def test_Address_address():
    ad = Address('en')
    print(ad.address())


if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:41:55.682149
# Unit test for method address of class Address
def test_Address_address():
    import sys
    address = Address(sys._getframe(0).f_code.co_name)
    print(address.address())
    print(address.street_number())
    print(address.street_name())
    print(address.street_suffix())
    print(address.state())
    print(address.postal_code())
    print(address.country())
    print(address.city())

if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:41:58.822177
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    assert isinstance(provider.address(), str)


# Generated at 2022-06-13 23:42:00.833147
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:42:09.641018
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('en')
    assert addr.address() == '30916 Barbara Branch'
    assert addr.address() == '91346 Sharon Key'
    assert addr.address() == '27656 Teresa Dam'

    addr = Address('fr')
    assert addr.address() == '42, rue du 11 novembre, 40000'

    addr = Address('ja')
    assert addr.address() == '鹿児島県八代市千代町45-67'

    addr = Address('pl')
    assert addr.address() == '25208-2707'
    assert addr.address() == '74-890'


# Generated at 2022-06-13 23:42:10.500913
# Unit test for method address of class Address
def test_Address_address():
    pass


# Generated at 2022-06-13 23:42:16.501395
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())

# Generated at 2022-06-13 23:42:21.375150
# Unit test for method address of class Address
def test_Address_address():
    a = Address(seed=444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444)
    assert a.address() == '892 W. Central St.'


# Generated at 2022-06-13 23:42:24.789768
# Unit test for method address of class Address
def test_Address_address():
    a = Address()

    def test_Address_address():
        a = Address()
        for i in range(0, 1000):
            assert type(a.address()) == str
            assert a.address() != ''



# Generated at 2022-06-13 23:42:26.650567
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result not in ['', None]


# Generated at 2022-06-13 23:42:28.818991
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(),str)
    pass


# Generated at 2022-06-13 23:42:30.710435
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    a = address.address()
    assert (len(a) > 0)


# Generated at 2022-06-13 23:42:32.529276
# Unit test for method address of class Address
def test_Address_address():
    print("test_Address_address: ")
    address = Address()
    print(address.address())

# Generated at 2022-06-13 23:42:40.235861
# Unit test for method address of class Address
def test_Address_address():
    address = Address('es')
    street_name = address.street_name()
    street_number = address.street_number()
    street_suffix = address.street_suffix()
    full_address = address.address()
    fmt = address._data['address_fmt']
    assert isinstance(street_name, str)
    assert isinstance(street_number, str)
    assert isinstance(street_suffix, str)
    assert isinstance(full_address, str)
    assert fmt.format(
        st_num=street_number,
        st_name=street_name,
        st_sfx=street_suffix) == full_address


# Generated at 2022-06-13 23:42:42.314024
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    assert isinstance(Address() .address(), str)

# Generated at 2022-06-13 23:42:44.748295
# Unit test for method address of class Address
def test_Address_address():
    """Check if the address method works correctly"""
    assert Address().address() == "1600 Pennsylvania Avenue Northwest"

# Generated at 2022-06-13 23:42:53.478675
# Unit test for method address of class Address
def test_Address_address():
    # Initialize a class
    address = Address()

    # Generate a random full address
    result = address.address()

    assert isinstance(result, str)
    assert len(result) <= 80


# Generated at 2022-06-13 23:42:56.800393
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers import Address
    provider = Address(Locale.ENGLISH)
    assert provider.address() == '1123 Queen St'

# Generated at 2022-06-13 23:43:02.244181
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    s = set()
    for i in range(100):
        s.add(a.address())
    assert "7301, c/ de l'Alhambra" in s


# Generated at 2022-06-13 23:43:05.259385
# Unit test for method address of class Address
def test_Address_address():
    # Init
    ad = Address()
    print(ad.address())
    print(ad.federal_subject())


# Generated at 2022-06-13 23:43:09.760578
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print('address = ' + str(address.address()))
    print('address = ' + str(address.address()))
    print('address = ' + str(address.address()))


# Generated at 2022-06-13 23:43:20.835349
# Unit test for method address of class Address
def test_Address_address():
    """Test for method address in class Address."""
    from mimesis.enums import Locale

    address = Address(locale=Locale.EN)
    output = address.address()
    pattern = r'\d{1,4} [a-zA-Z]{5,15} Street'

    assert re.search(pattern, output)

    pattern = r'\d{1,4} [a-zA-Z]{5,15}'
    output = address.address()

    assert re.search(pattern, output)

    address = Address(locale=Locale.JP)
    output = address.address()

    assert re.search(r'\d{1,4}', output)


# Generated at 2022-06-13 23:43:22.628375
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    assert address.address() == '1352 Clinton Street'

# Generated at 2022-06-13 23:43:24.476183
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    addr = Address('it')
    s = addr.address()
    assert isinstance(s, str)
    assert len(s) > 7
    assert s.find('Corso') != -1

# Generated at 2022-06-13 23:43:26.986816
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    result = provider.address()
    print('result =', result)
    assert isinstance(result, str)



# Generated at 2022-06-13 23:43:37.351234
# Unit test for method address of class Address
def test_Address_address():
    from pytest import raises
    from mimesis.enums import Gender, CountryCode
    from mimesis.enums import AddressFormats as AF

    a = Address(
        'en',
        gender=Gender.MALE,
        country_code=CountryCode.A2,
        formatter=AF.NATIONAL
    )
    a.seed(123)
    assert a.address() == '6694 Campbell Station'
    assert a.address() == '6342 N. Montgomery Street'
    assert a.address() == '566 N. Park Road'

    a = Address(
        'ru',
        gender=Gender.MALE,
        country_code=CountryCode.A2,
        formatter=AF.NATIONAL
    )
    a.seed(123)

# Generated at 2022-06-13 23:43:49.738988
# Unit test for method address of class Address
def test_Address_address():
    adress = Address()
    adress.address()


# Generated at 2022-06-13 23:43:52.550411
# Unit test for method address of class Address
def test_Address_address():
    a = Address()

    assert(a.address() == a.address())
    assert(isinstance(a.address(), str))


# Generated at 2022-06-13 23:43:57.992826
# Unit test for method address of class Address
def test_Address_address():  # unit test for Address().address() method
    from mimesis.enums import Locale

    # example of the Russian address
    Address(Locale.RU).address()

    # example of the English address
    Address(Locale.EN).address()

    # example of the Japanese address
    Address(Locale.JA).address()

# Generated at 2022-06-13 23:43:59.374015
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)

# Generated at 2022-06-13 23:44:00.971144
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert (addr.address())


# Generated at 2022-06-13 23:44:02.542836
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    result = a.address()
    print(result)


# Generated at 2022-06-13 23:44:04.666617
# Unit test for method address of class Address
def test_Address_address():
    provider = Address(locale='en')
    result = provider.address()
    assert isinstance(result, str)



# Generated at 2022-06-13 23:44:05.521744
# Unit test for method address of class Address
def test_Address_address():
    assert Address.address()


# Generated at 2022-06-13 23:44:16.893336
# Unit test for method address of class Address
def test_Address_address():
    print("\n" + "#" * 3 + " " + "test_Address_address" + " " + "#" * 3 + "\n")

    from mimesis.enums import Locale
    from mimesis.exceptions import NonEnumerableError

    address = Address()

    for _ in range(10):
        print(address.address())

    address = Address(Locale.CA)
    print(address.address())

    address = Address(Locale.KW)
    print(address.address())

    address = Address(Locale.CN)
    print(address.address())

    address = Address(None)
    print(address.address())

    try:
        Address(Locale.EN)
    except NonEnumerableError:
        pass


# Generated at 2022-06-13 23:44:19.275826
# Unit test for method address of class Address
def test_Address_address():
    addr = Address(locale='es-MX')
    addr.address()

# Generated at 2022-06-13 23:44:58.623702
# Unit test for method address of class Address
def test_Address_address():
    name = "Address_address"
    random = Random()
    address = Address(random)

# Generated at 2022-06-13 23:45:01.963432
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    name = address.address()
    assert isinstance(name, str)
    for i in range(8):
        name = address.address()
        assert isinstance(name, str)


# Generated at 2022-06-13 23:45:04.958667
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    # print(a.address())
    assert a.address() != a.address()


# Generated at 2022-06-13 23:45:06.629105
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    res = ad._get_fs('lt',dms=True)
    print(res)

# Generated at 2022-06-13 23:45:07.828556
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('ja')
    assert addr.address() != addr.address()


# Generated at 2022-06-13 23:45:12.828059
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    street_addr = a.address()
    assert street_addr is not None
    print('Street address: {}'.format(street_addr))



# Generated at 2022-06-13 23:45:19.921589
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    # en-US
    address = Address('en-US')
    assert 'San Francisco' in address.city()
    assert address.country() == 'United States'
    assert address.postal_code() == '94014'
    assert (address.street_number() + ' ' +
            address.street_name() + ' ' +
            address.street_suffix()) in address.address()
    assert address.region() == 'CA'
    assert address.continent() == 'America'
    assert address.calling_code() == '1'
    assert address.country_code() in COUNTRY_CODES[CountryCode.A2]
    # de
    address = Address('de')
    assert 'Graz' in address

# Generated at 2022-06-13 23:45:22.116992
# Unit test for method address of class Address
def test_Address_address():
    adr = Address('en')
    assert adr.address() != None
    assert adr.address() != ''
    print('test Address address() ok')


# Generated at 2022-06-13 23:45:27.793829
# Unit test for method address of class Address
def test_Address_address():
    _address = Address(locale='nl')
    street_name = _address.street_name()
    street_number = _address.street_number()
    street_suffix = _address.street_suffix()
    assert f'{street_number} {street_name} {street_suffix}' == _address.address()

test_Address_address()

# Generated at 2022-06-13 23:45:29.792400
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() != address.address()


# Generated at 2022-06-13 23:46:27.096453
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    print(result)


# Generated at 2022-06-13 23:46:29.573144
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    print(adr.address())
    print(adr.address())
    print(adr.address())
    print(adr.address())


# Generated at 2022-06-13 23:46:30.671216
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    assert adr.address() != 'default'

# Generated at 2022-06-13 23:46:34.151634
# Unit test for method address of class Address
def test_Address_address():
    address_str = Address().address()
    assert address_str


# Generated at 2022-06-13 23:46:41.457505
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address, en, ru
    from mimesis.utils import to_camel_case

    address = Address(locale='en')
    address.seed(1234567890)

    result = address.address()
    assert result == '207 Leander Parkway'

    address = Address(locale='es')
    address.seed(1234567890)
    result = address.address()
    assert result == '207 Leander Park'

    # Test DataProvider.__str__
    assert address.__str__() == address.address()

    # TODO: Do not use diacritics in unit tests
    address = Address(locale='cs')
    address.seed(1234567890)
    result = address.address()
    assert result == '207 Leander Štěpánka'

# Generated at 2022-06-13 23:46:44.016444
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    adr = Address(Locale.EN)
    print(adr.address())

# Generated at 2022-06-13 23:46:48.441383
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    address = Address('en')
    assert address.address() is not None
    assert address.address() != ''
    assert address.addre

# Generated at 2022-06-13 23:46:51.189610
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result == "104, Nelson Street" or result == "104, Nelson St."

# Generated at 2022-06-13 23:46:58.018070
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address(locale='tr').address()
    assert Address().address() != Address(locale='ja').address()
    assert Address(locale='ja').address() == Address(locale='ja').address()


# Generated at 2022-06-13 23:47:00.017087
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result is not None
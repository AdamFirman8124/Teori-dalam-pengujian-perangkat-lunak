

# Generated at 2022-06-13 23:39:46.672200
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.exceptions import NonEnumerableError

    my_addr = Address(Locale.RUSSIAN)
    my_address = my_addr.address()
    # my_address is a string
    assert isinstance(my_address, str)
    # my_address not empty
    assert my_address is not ''
    # my_address is composed of street number, street name and street suffix
    assert (my_address.find(my_addr.street_number()) != -1) and \
           (my_address.find(my_addr.street_name()) != -1) and \
           (my_address.find(my_addr.street_suffix()) != -1)

    my_addr = Address(Locale.CHINESE)
    my_address = my

# Generated at 2022-06-13 23:39:48.710295
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    address = Address(Locale['en'])
    assert address.address() != ''

# Generated at 2022-06-13 23:39:50.267803
# Unit test for method address of class Address
def test_Address_address():
    address = Address('zh')
    print(address.street_name())
    print(address.address())


# Generated at 2022-06-13 23:39:52.805783
# Unit test for method address of class Address
def test_Address_address():
    assert len(Address().address()) == 32
    assert Address().address() == '1171 Rue des Chênes'


# Generated at 2022-06-13 23:39:54.676767
# Unit test for method address of class Address
def test_Address_address():
    a=Address('pt-BR')
    assert a.address() != ''

# Generated at 2022-06-13 23:39:58.642643
# Unit test for method address of class Address
def test_Address_address():
    prov = Address()
    addr = prov.address()
    assert len(addr) > 0
    return addr

if __name__ == '__main__':
    for i in range(10):
        print(test_Address_address())

# Generated at 2022-06-13 23:40:06.214644
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Country
    from mimesis.builtins import RussiaSpecProvider
    result = []
    ru = RussiaSpecProvider(
            country=Country.RUSSIAN_FEDERATION)
    ruAddress = ru.Address()
    ruResult = ruAddress.address()
    ruResult1 = ruAddress.address()
    uk = RussiaSpecProvider(
            country=Country.UNITED_KINGDOM)
    ukAddress = uk.Address()
    ukResult = ukAddress.address()
    ukResult1 = ukAddress.address()
    br = RussiaSpecProvider(
            country=Country.BRAZIL)
    brAddress = br.Address()
    brResult = brAddress.address()
    brResult1 = brAddress.address()

# Generated at 2022-06-13 23:40:09.809086
# Unit test for method address of class Address
def test_Address_address():
    Addr = Address()
    country = Addr._data['country']['current_locale']
    print(Addr.address())
    print(Addr.address())
    print(Addr.address())
    print(country)


# Generated at 2022-06-13 23:40:13.438031
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='en')
    result = a.address()
    assert result
    print(result)

if __name__ == "__main__":
    test_Address_address()

# Generated at 2022-06-13 23:40:27.857382
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for address method of Address class."""
    a = Address('en')

# Generated at 2022-06-13 23:40:37.350972
# Unit test for method address of class Address
def test_Address_address():
    # Set locale to 'en'
    address = Address(locale='en')

    test_address = address.address()
    assert isinstance(test_address, str) is True


# Generated at 2022-06-13 23:40:42.169601
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""

    # create an instance
    obj = Address()

    # execute the method
    address = obj.address()

    # check if the address is in the correct format
    assert address is not None
    assert address != ''

# Generated at 2022-06-13 23:40:43.581922
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    address = Address()
    result = address.address()
    assert isinstance(result, str)
    assert result != ''


# Generated at 2022-06-13 23:40:46.958877
# Unit test for method address of class Address
def test_Address_address():
    address = Address('de')
    assert address.address() != '0000'
    assert address.address() != '00000'



# Generated at 2022-06-13 23:40:48.264205
# Unit test for method address of class Address
def test_Address_address():
    a = Address('ru')
    assert a.address() is not None


# Generated at 2022-06-13 23:40:55.885606
# Unit test for method address of class Address
def test_Address_address():
    # Create object of class Address
    ad = Address()

    # Set locale to ru
    # Set number of dataset in random generator
    ad.seed(1, 'ru')

    # Get address
    # We got: Вьюи набережная, строение 7

    ad.address()
    '''
    >>> Вьюи набережная, строение 7
    '''

    # Change locale
    # Set new random number
    ad.seed(1, 'en')

    ad.address()
    '''
    >>> 5637 Bruton Terrace
    '''



# Generated at 2022-06-13 23:40:58.280387
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale = 'en')
    a = address.address()
    patA = re.compile(r'^\d{1,4} [A-Z][a-z]{1,10} [A-Z][a-z]{1,10}$')
    assert re.match(patA, a)

# Generated at 2022-06-13 23:40:59.762209
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:41:06.609060
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender
    from mimesis.typing import AddressType
    from mimesis.providers.geography import Address

    a = Address()
    assert a.address()
    assert a.address(separator=';')
    assert a.address(person=a.person(gender=Gender.FEMALE))
    assert a.address(clean=True)
    assert a.address(address_type=AddressType.SIMPLE)
    assert a.address(address_type=AddressType.LONG)
    assert a.address(address_type=AddressType.SHORT)

# Generated at 2022-06-13 23:41:10.093131
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address

    a = Address()
    check_type = str
    assert check_type(a.address()) == True



# Generated at 2022-06-13 23:41:18.676269
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:41:30.182519
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    address_provider1 = Address()
    print(address_provider1.address())  # 1002 SW Gibbs St
    print(address_provider1.address())  # 55 Rosalind Way
    print(address_provider1.address())  # 3146 Sunset Blvd
    address_provider2 = Address('en')
    print(address_provider2.address())  # 1109 SW Gibbs St
    print(address_provider2.address())  # 4898 Birke Ln
    print(address_provider2.address())  # 519 Kings Way
    address_provider3 = Address('ru')
    print(address_provider3.address())  # Пр-т Воздухофлотский, д.40 к

# Generated at 2022-06-13 23:41:32.134124
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert type(result) == str


# Generated at 2022-06-13 23:41:33.240604
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    # address
    assert address.address()


# Generated at 2022-06-13 23:41:45.345686
# Unit test for method address of class Address

# Generated at 2022-06-13 23:41:49.951174
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    addr = Address('ru')
    # test only first 10 address
    for _ in range(10):
        assert len(addr.address()) >= 10

# Generated at 2022-06-13 23:41:58.638120
# Unit test for method address of class Address
def test_Address_address():
    from pprint import pprint
    from random import seed
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Country
    from mimesis.providers.address import Address
    from mimesis.providers.geography import Geography

    seed(0)
    gr = Geography(locale='ru')
    ar = Address(gr)
    ar_en = Address(Country.ENGLISH)
    russia = RussiaSpecProvider(gr)

    pprint(ar.address())

    pprint(list(ar_en.address()))

    pprint(russia.address())

# Generated at 2022-06-13 23:42:00.065570
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())

# Generated at 2022-06-13 23:42:01.549554
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    result = a.address()
    assert len(result) > 0


# Generated at 2022-06-13 23:42:02.789443
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    assert callable(obj)


# Generated at 2022-06-13 23:42:20.208914
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import AddressFormat
    # Create object of Address class with using Russian locale and
    # selecting specific address format.
    adr = Address(locale='ru', address_format=AddressFormat.SHORT)
    # Create object of RussiaSpecProvider class with using default
    # address format.
    rus = RussiaSpecProvider(locale='ru')

    for _ in range(10):
        assert rus.address() == adr.address()
    # Test address format for other locales.
    assert (adr.address() == 'Гусарский переулок, д. 10')

# Generated at 2022-06-13 23:42:22.329534
# Unit test for method address of class Address
def test_Address_address():
    # Arrange
    address = Address("en")

    # Act
    result = address.address()

    # Assert
    assert result



# Generated at 2022-06-13 23:42:23.375791
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())

# Generated at 2022-06-13 23:42:25.580845
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    address = Address()
    print(address.address())
    print(address.address())



# Generated at 2022-06-13 23:42:31.356826
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    from mimesis.localization import RU

    a = Address(localization=RU)
    assert a.address() != a.address()

    b = Address(locale=CountryCode.RU)
    assert b.address() != b.address()

    en = Address(locale='en')
    assert en.address() != en.address()

# Generated at 2022-06-13 23:42:33.806201
# Unit test for method address of class Address
def test_Address_address():
    test_Address1 = Address()
    result = test_Address1.address()
    assert result is not None
    assert len(result) > 0


# Generated at 2022-06-13 23:42:35.797548
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    result = obj.address()
    assert(isinstance(result, str))
    assert(len(result) > 0)


# Generated at 2022-06-13 23:42:38.986144
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())
    print(address.street_name())
    print(address.street_suffix())
    print(address.street_number())


if __name__ == "__main__":
    test_Address_address()

# Generated at 2022-06-13 23:42:41.932563
# Unit test for method address of class Address
def test_Address_address():

    # TODO: Add unit tests for functions inside Address module
    # class Address(BaseDataProvider):
    return True

# Generated at 2022-06-13 23:42:44.189395
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address().address()


# Generated at 2022-06-13 23:43:00.376976
# Unit test for method address of class Address
def test_Address_address():
    a = Address(Region.AMERICA)
    a.address()  # 1 Testway Drive
    a.address()  # Apt. 556
    a.address()  # Suite 849
    a.address()  # Suite 958
    a.address()  # Apartment 0254
    a.address()  # Suite 183
    a.address()  # Suite 881
    a.address()  # Suite 959
    a.address()  # Suite 656
    a.address()  # Apt. 952
    a.address()  # Suite 389

    b = Address(Region.JAPAN)
    b.address()  # 大阪市海岸区塩屋町５－２−３３
    b.address

# Generated at 2022-06-13 23:43:02.199785
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:43:16.750743
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussianSpecProvider
    from mimesis.enums import Gender
    from mimesis.schema import Field, Schema

    address_provider = Address('ru')
    rs = RussianSpecProvider('ru')

    address_template = {
        'street_name': Field('address.street_name'),
        'street_number': Field('address.street_number', maximum=99),
        'street_suffix': Field('address.street_suffix'),
        'city': Field('address.city'),
        'country': Field('address.country'),
        'postal_code': Field('address.postal_code'),
    }
    schema = Schema(address_template)

    address = address_provider.address()
    address_serialized = schema.create(iterations=1)
    address

# Generated at 2022-06-13 23:43:22.588436
# Unit test for method address of class Address
def test_Address_address():
    # проверка при локальном провайдере
    address_local = Address('ru')
    assert address_local.address() == '5 улица Арбузова кв. 103'
    assert len(address_local.address()) == 25
    # проверка при глобальном провайдере
    address_global = Address()
    assert len(address_global.address()) == 25

# Generated at 2022-06-13 23:43:25.630942
# Unit test for method address of class Address
def test_Address_address():
    locale = "en-US"
    address = Address(locale=locale)
    for i in range(10):
        print(address.address())


# Generated at 2022-06-13 23:43:36.103128
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    # assert address.address() == '1107 Joe Ford Apt. 984'
    assert address.state() == 'Kansas'
    assert address.state(abbr=True) == 'KS'
    assert address.region() == 'Kansas'
    # assert address.region(abbr = True) == 'KS'
    assert address.postal_code() == '113052'
    assert address.zip_code() == '113052'
    assert address.country_code() == 'US'
    assert address.country_code(CountryCode.A3) == 'USA'
    assert address.country_code(CountryCode.NUMERIC) == '840'
    assert address.country_code(CountryCode.ENUM) == 'US'
    # assert address.country_code(CountryCode

# Generated at 2022-06-13 23:43:48.519577
# Unit test for method address of class Address
def test_Address_address():
    # Prove that values for different locales and formats of address are different.
    addr_ru = Address("ru")
    addr_en = Address("en")
    addr_ja = Address("ja")
    addr_de = Address("de")
    addr_fr = Address("fr")

    assert addr_ru.address() != addr_en.address()
    assert addr_ru.address() != addr_ja.address()
    assert addr_ru.address() != addr_de.address()
    assert addr_ru.address() != addr_fr.address()
    assert addr_en.address() != addr_ja.address()
    assert addr_en.address() != addr_de.address()
    assert addr_en.address() != addr_fr.address()
    assert addr_ja.address() != addr_de.address()
    assert addr

# Generated at 2022-06-13 23:43:49.932018
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address method."""
    print(Address().address())



# Generated at 2022-06-13 23:43:52.341259
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    ma = Address()
    assert ma.address()

# Generated at 2022-06-13 23:43:53.830224
# Unit test for method address of class Address
def test_Address_address():
    address1 = Address('zh')
    print(address1.address())

# Generated at 2022-06-13 23:44:03.816281
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    assert a.address()


# Generated at 2022-06-13 23:44:07.501192
# Unit test for method address of class Address
def test_Address_address():
    """Check logic of method address() of class Address."""
    from mimesis.builtins import Address
    a = Address()
    assert a._validate_locale(a.locale)
    assert isinstance(a.address(), str)



# Generated at 2022-06-13 23:44:12.807198
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
   
    data = Address(Locale.EN)
    print(data.address())
    print(data.address())
    print(data.address())
    print(data.address())
    print(data.address())


# Generated at 2022-06-13 23:44:17.846536
# Unit test for method address of class Address
def test_Address_address():
    """Test method address."""
    import pytest
    ADDRESS = ['2598 Elm Drive',
               '12 West Street',
               '797 Rosedale St.',
               '80825 Nolan Court',
               '897959 Mount Street',
               '4250 Roslyn Street']

    for i in range(10):
        assert Address(seed=i * 10).address() in ADDRESS


# Generated at 2022-06-13 23:44:21.593766
# Unit test for method address of class Address
def test_Address_address():
    for n in range(0, 10):
        adr = Address()
        ans = adr.address()
        print(ans)

test_Address_address()

# Generated at 2022-06-13 23:44:23.945013
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    assert provider.address() in provider._data['address_fmt']



# Generated at 2022-06-13 23:44:28.953621
# Unit test for method address of class Address
def test_Address_address():
    """Test address method of class Address."""
    provider = Address()
    result = provider.address().split('\n')
    assert len(result) == 4
    assert result[2].split()[1].isdigit()



# Generated at 2022-06-13 23:44:32.342160
# Unit test for method address of class Address
def test_Address_address():
    """Generate an address and print it."""
    address = Address('en')
    print(address.address())


# Generated at 2022-06-13 23:44:35.806001
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    _addr = Address()
    assert _addr.address() != None, "We should have an address"

    _addr = Address('es')
    assert _addr.address() != None, "We should have an address"


# Generated at 2022-06-13 23:44:42.640044
# Unit test for method address of class Address
def test_Address_address():
    # Usage of Address class
    a = Address('en')

    # Generate a random full address (street number, street name and
    # street suffix). Default format is:
    # '{st_num} {st_name} {st_sfx}'
    address = a.address()

    # Example of address: '1294 South Green Street'
    print(address)



# Generated at 2022-06-13 23:45:10.589771
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert type(a.address()) is str
    assert len(a.address()) > 0


# Generated at 2022-06-13 23:45:13.897862
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result == '221B Baker Street'  # For locale en

# Generated at 2022-06-13 23:45:17.128778
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('en')
    print("=====================================")
    print("Full address:",  addr.address())


# Generated at 2022-06-13 23:45:20.050331
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    result = a.address()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:45:24.579163
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address()

    address_ = address.address()
    assert isinstance(address_, str)
    assert address_


# Generated at 2022-06-13 23:45:27.212525
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    assert address.address() != ''


# Generated at 2022-06-13 23:45:28.659572
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:45:34.926627
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale, Gender

    a = Address(locale=Locale.ZH_CN, gender=Gender.MALE)

    result = a.address()
    assert isinstance(result, str)
    assert len(result) > 0

    result = a.address()
    assert isinstance(result, str)
    assert len(result) > 0

# Generated at 2022-06-13 23:45:36.558362
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    a = addr.address()
    print(a)



# Generated at 2022-06-13 23:45:37.651254
# Unit test for method address of class Address
def test_Address_address():

    address = Address("en")
    assert address.address() is not None


# Generated at 2022-06-13 23:46:00.999203
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert addr.address() is not None


# Generated at 2022-06-13 23:46:11.349280
# Unit test for method address of class Address

# Generated at 2022-06-13 23:46:12.582227
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='fr')
    print(address.address())


# Generated at 2022-06-13 23:46:14.127765
# Unit test for method address of class Address
def test_Address_address():
    address_obj = Address()
    assert address_obj.address() == '4834 Meadowcrest Lane'

# Generated at 2022-06-13 23:46:16.805831
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() != ''
    assert address.address() is not None

test_Address_address()

# Generated at 2022-06-13 23:46:20.274237
# Unit test for method address of class Address
def test_Address_address():
    adress = Address()
    test_address = adress.address()
    print(test_address)
    assert test_address != None, "Function address() of class Address() must return an address"
    print("Successfully passed test_Address_address()\n")


# Generated at 2022-06-13 23:46:23.881372
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    result = Address(Locale.PT_BR).address()
    print(result)



# Generated at 2022-06-13 23:46:27.576613
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    addr = address.address()
    assert isinstance(addr, str)
    assert len(addr) != 0

# Generated at 2022-06-13 23:46:31.798469
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address().count(' ') == 2
    assert (a.address() == '{} {}'.format(a.street_number(), a.street_name()))
    assert len(a.address()) > 0


# Generated at 2022-06-13 23:46:40.704440
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == '1022 Southwest Johnson Hill'
    assert Address(lang="zh").address() == '吉尔达,孔雀街 410 路'
    assert Address(lang="ko").address() == '쿠바에서비스거리85-7315'
    assert Address(lang="vi").address() == 'Số 2, đường Cỏ Chài'
    assert Address(lang="ja").address() == '象島自治体二丁目86番地の87'

# Generated at 2022-06-13 23:47:15.672515
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Country
    from mimesis.builtins import Germany
    from mimesis.builtins import Japan

    # Use \ as line break as valid in Python's string literals
    assert Address().address() == "95\
 Rue Comtesse de Ségur"

    assert Address().address() == '93 West College Ave'

    assert Address(locale='de', region=Country.GERMANY).address() == "5\
 Postreiter-Weg"

    assert Address(locale='de', region=Country.GERMANY).address() == "5\
 Postreiter-Weg"

    assert Address(locale='de', region=Country.GERMANY).address() == "5\
 Postreiter-Weg"

    address = Address(Germany())

# Generated at 2022-06-13 23:47:19.108130
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    address = Address().address()
    for key in SHORTENED_ADDRESS_FMT.keys():
        address = Address(key).address()
        assert(address) is not None
        assert(address)

# Generated at 2022-06-13 23:47:22.839320
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender
    # create a object of class Address
    address = Address(Gender.MALE, 'en')
    # get a random address
    full_address = address.address()
    #print address
    print(full_address)


# Generated at 2022-06-13 23:47:24.108343
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() is not None


# Generated at 2022-06-13 23:47:25.959519
# Unit test for method address of class Address
def test_Address_address():
    ad = Address("zh")
    result = ad.address()
    print(result)


# Generated at 2022-06-13 23:47:27.516373
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    result = adr.address()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:47:31.197637
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    address = Address()
    result = address.address()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:47:33.863072
# Unit test for method address of class Address
def test_Address_address():
    assert Address('en').address() \
        == "3221 Stewart Lane"



# Generated at 2022-06-13 23:47:34.419946
# Unit test for method address of class Address
def test_Address_address():
    pass

# Generated at 2022-06-13 23:47:35.847775
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result is not None


# Generated at 2022-06-13 23:47:57.616643
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address().address()

# Generated at 2022-06-13 23:48:00.810029
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address()."""
    ad = Address()
    address = ad.address()  # noqa: WPS421
    assert len(address) > 0



# Generated at 2022-06-13 23:48:08.260229
# Unit test for method address of class Address
def test_Address_address():
    # class Address(BaseDataProvider):
    a = Address()
    assert a.street_number() == str(a.random.randint(1, 1400))
    assert a.street_name() in a._data['street']['name']
    assert a.street_suffix() in a._data['street']['suffix']
    # if 'address_fmt' in self._data:
    #     if 'name' in self._data['street'] and \
    #             'suffix' in self._data['street']:
    #         return self._data['address_fmt'].format(
    #             st_num=self.street_number(),
    #             st_name=self.street_name(),
    #             st_sfx=self.street_suffix(),
    #         )

# Generated at 2022-06-13 23:48:11.191685
# Unit test for method address of class Address
def test_Address_address():
    address = Address("en").address()
    assert address  # Check the address is not None

# Generated at 2022-06-13 23:48:12.908901
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    print(address.address())


# Generated at 2022-06-13 23:48:16.752133
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address
    """
    print("\nTesting Address.address")
    assert Address().address() != ""
    assert Address(locale="zh-cn").address() != ""
    assert Address(locale="ja").address() != ""

# Generated at 2022-06-13 23:48:27.038744
# Unit test for method address of class Address
def test_Address_address():
    class fake_provider:
        def __init__(self, random_return):
            self.random = fake_random()
            self.random.randint = lambda a, b: random_return
            self.random.choice = lambda x: random_return
            self._data = {
                'street': {
                    'name': ['fake_name'],
                    'suffix': ['fake_suffix']
                },
                'address_fmt': '{fake_fmt}',
                'state': {
                    'abbr': ['fake_abbr'],
                },
                'city': ['fake_city']
            }

    class fake_random:
        def choice(self, _):
            return 'fake_choice'

        def __init__(self):
            self.randint = None

# Generated at 2022-06-13 23:48:27.895765
# Unit test for method address of class Address
def test_Address_address():
    # test code
    print(Address().address())


# Generated at 2022-06-13 23:48:38.657626
# Unit test for method address of class Address
def test_Address_address():

    a = Address('en')
    assert a.address() == '134 West Hazen Pass'
    # assert a.address() == '217 West North Prairie'
    # assert a.address() == '2554 East Adams'
    # assert a.address() == '25 Boyer Road'

    a = Address('ru')
    assert a.address() == 'аул Юрьевка, 12а'
    # assert a.address() == 'переулок Луначарского, 6, 1'
    # assert a.address() == 'улица Некрасовская, 21а, 1'
    # assert a.address() == 'поселок Микрора

# Generated at 2022-06-13 23:48:51.091874
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    a1 = Address(Locale.RU)
    assert a1.address() == 'Татарское землячество, д. 11 а'
    a2 = Address(Locale.UK)
    assert a2.address() == 'бул. Тернопільське шосе, буд. 14 а'
    a3 = Address(Locale.EN)
    assert a3.address() == '1250 Braddock Dr'

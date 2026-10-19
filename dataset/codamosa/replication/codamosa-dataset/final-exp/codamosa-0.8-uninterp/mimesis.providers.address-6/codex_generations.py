

# Generated at 2022-06-13 23:39:36.596604
# Unit test for method address of class Address
def test_Address_address():
    a = Address('ru')
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)
    assert isinstance(a.address(), str)


# Generated at 2022-06-13 23:39:44.249317
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='en')
    street = a.address()
    assert street != None

    a = Address(locale='fr')
    street = a.address()
    assert street != None

    a = Address(locale='fi')
    street = a.address()
    assert street != None

    a = Address(locale='ja')
    street = a.address()
    assert street != None


# Generated at 2022-06-13 23:39:45.889165
# Unit test for method address of class Address
def test_Address_address():
    provider = Address('en')
    result = provider.address()
    assert result
    print(result)


# Generated at 2022-06-13 23:39:48.287621
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    print(adr.address())
    print(adr.address())
    print(adr.address())
    print(adr.address())
    print(adr.address())

# Generated at 2022-06-13 23:39:55.089988
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis.builtins import RussiaSpecProvider

    rus = Address(RUS)
    assert rus.address() in rus._data['address']

    russpec = RussiaSpecProvider(RUS)
    eng = Address(EN)
    assert russpec.address() == eng.address()

# Generated at 2022-06-13 23:39:56.345549
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    a = Address('en')
    assert a.address()

# Generated at 2022-06-13 23:39:57.337534
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()

# Generated at 2022-06-13 23:39:58.121869
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != '{}'

# Generated at 2022-06-13 23:40:00.033686
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())


# Generated at 2022-06-13 23:40:03.178888
# Unit test for method address of class Address
def test_Address_address():
    mimesis_address = Address()
    address1 = mimesis_address.address()
    assert len(address1)
    assert isinstance(address1, str)


# Generated at 2022-06-13 23:40:11.933461
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    address = Address(CountryCode.RU)
    assert address.address()

# Generated at 2022-06-13 23:40:13.312757
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    result = provider.address()
    assert result == ''

# Generated at 2022-06-13 23:40:14.807341
# Unit test for method address of class Address
def test_Address_address():
    a = Address("en")
    print(a.address())


# Generated at 2022-06-13 23:40:18.068402
# Unit test for method address of class Address
def test_Address_address():
    address_obj = Address("tr")
    print(address_obj.address())


# Generated at 2022-06-13 23:40:23.559927
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider
    address = Address(RussiaSpecProvider)
    addr = address.address()
    assert addr == '2-ая Московская улица'


# Generated at 2022-06-13 23:40:27.089282
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address as AddressTest
    address_test = AddressTest('en')
    assert address_test.address() == "1400 W. 24th Street"

# Generated at 2022-06-13 23:40:30.898143
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address"""
    @classmethod
    def test2(Details):
        """Class method test2."""
        return Details.address()

    @classmethod
    def test5(Details):
        """Class method test5."""
        return Details.address()

# Generated at 2022-06-13 23:40:33.572000
# Unit test for method address of class Address
def test_Address_address():
    """Test Address address."""
    address = Address()
    result = address.address()
    assert isinstance(result, str)
    assert len(result) > 0


# Generated at 2022-06-13 23:40:35.055401
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    result = provider.address()
    assert len(result) >= 10



# Generated at 2022-06-13 23:40:37.330946
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    res = address.address()
    assert res == '2742 John Wall' or res == '1813 Paul Mason'


# Generated at 2022-06-13 23:40:47.633675
# Unit test for method address of class Address
def test_Address_address():
    """ Test the address method."""
    import time
    start_time=time.time()
    a = Address()
    assert a.address()
    print('Test Address->address: ', time.time()-start_time)


# Generated at 2022-06-13 23:40:54.604800
# Unit test for method address of class Address
def test_Address_address():
    # Test for LANGUAGE_CODE: 'ru'
    a = Address(lang='ru')
    out = a.address()

# Generated at 2022-06-13 23:40:59.189655
# Unit test for method address of class Address
def test_Address_address():
    # Test 1
    address = Address()
    result = address.address()
    print(result)
    assert result is not None
    # Test 2
    address = Address()
    result = address.address()
    print(result)
    assert result is not None

# Generated at 2022-06-13 23:41:00.622507
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())


# Generated at 2022-06-13 23:41:02.495989
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == '888-5461 Duis Street'

# Generated at 2022-06-13 23:41:10.228658
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    assert Address('en').address() == '594 Gleason Crossing'
    assert Address(Locale.SPANISH).address() == '10891 Job Rd.'

    assert Address(locale='de').address() == '7605 Hauptstr.'
    assert Address(locale='de', seed=1).address() == '7605 Hauptstr.'

    assert Address(locale='ru').address() == 'Извилинская улица, д. 1'
    assert Address(locale='ja').address() == '〒171-0014 東京都豊島区東池袋2-45-17'


# Generated at 2022-06-13 23:41:10.954022
# Unit test for method address of class Address
def test_Address_address():
    adr = Address(locale='en')
    print(adr.address())

# Generated at 2022-06-13 23:41:13.612981
# Unit test for method address of class Address
def test_Address_address():
    _address = Address(random=12345678)
    assert _address.address() == "964 Veda Vista, Watsica, AZ 80692"



# Generated at 2022-06-13 23:41:16.612888
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address.

    Function generate random full address.
    """

    address = Address()
    assert address.address()
    assert type(address.address()) == str

# Generated at 2022-06-13 23:41:27.795444
# Unit test for method address of class Address

# Generated at 2022-06-13 23:41:43.528587
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    from mimesis.enums import CountryCode
    address = Address('en')
    # print(address.address())
    print(address.country_code())
    print(address.country_code(CountryCode.A3))
    print(address.country_code(CountryCode.A2_RANDOM))
    print(address.country_code(CountryCode.A3_RANDOM))
    print(address.calling_code())
    print(address.calling_code())
    print(address.calling_code())

# Generated at 2022-06-13 23:41:44.859959
# Unit test for method address of class Address
def test_Address_address():
    assert Address("en").address() == "1078 Silva Walks, Baileyview"

# Generated at 2022-06-13 23:41:48.319100
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import AddressFormats


    provider = Address()
    fmt = provider.random.choice(AddressFormats)
    print(fmt)
    print(AddressFormats.US_SIMPLE)
    print(AddressFormats.US_FULL)
    print(AddressFormats.RU_SIMPLE)
    print(AddressFormats.RU_FULL)
    print(AddressFormats.PT)
    print(AddressFormats.JP)
    print(AddressFormats.CN)

# Generated at 2022-06-13 23:41:59.183202
# Unit test for method address of class Address
def test_Address_address():
    # Test Address.address()
    a = Address('en')
    assert isinstance(a.address(), str)
    assert a.locale == 'en'
    a = Address('zh')
    assert isinstance(a.address(), str)
    assert a.locale == 'zh'
    a = Address('ar')
    assert isinstance(a.address(), str)
    assert a.locale == 'ar'
    a = Address('ru')
    assert isinstance(a.address(), str)
    assert a.locale == 'ru'
    a = Address('ja')
    assert isinstance(a.address(), str)
    assert a.locale == 'ja'
    a = Address('de-DE')
    assert isinstance(a.address(), str)
    assert a.locale == 'de-DE'
   

# Generated at 2022-06-13 23:42:02.311733
# Unit test for method address of class Address
def test_Address_address():
    # Setup
    addr = Address()
    # Exercise
    result = addr.address()
    assert result
    assert isinstance(result, str)


# Generated at 2022-06-13 23:42:05.453946
# Unit test for method address of class Address
def test_Address_address():
    """Test case"""
    address1 = Address()
    address2 = Address('ja')
    assert address1.address() == '123 Main St.'
    assert address2.address() == '東京都千代田区'

# Generated at 2022-06-13 23:42:07.028160
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())
    print(a.address())

# Generated at 2022-06-13 23:42:08.814543
# Unit test for method address of class Address
def test_Address_address():
    provider = Address("en")
    address = provider.address()

    assert address



# Generated at 2022-06-13 23:42:10.792248
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()



# Generated at 2022-06-13 23:42:17.737842
# Unit test for method address of class Address
def test_Address_address():
    mimesis_address = Address("en")
    en_address1 = mimesis_address.address()
    assert(isinstance(en_address1, str))
    assert(len(en_address1) > 0)

    mimesis_address = Address("es")
    es_address1 = mimesis_address.address()
    assert(isinstance(es_address1, str))
    assert(len(es_address1) > 0)


# Generated at 2022-06-13 23:42:31.957740
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address()."""
    a = Address()

    result = a.address()
    assert isinstance(result, str)

    result = Address(locale='ru').address()
    assert isinstance(result, str)

    result = a.address()
    assert any([x.isdigit() for x in result])

    result = a.address()
    assert any([x.isalpha() for x in result])



# Generated at 2022-06-13 23:42:39.603334
# Unit test for method address of class Address
def test_Address_address():
    """
    Test method address of class Address.
    Note: the test may be slow, because the
    method generates a large number of data.
    """

    from mimesis.builtins.enums import AddressFormats

    def check_string(result: str, exp: str) -> None:
        """Check number of substrings in string.

        :param result: String which tests.
        :param exp: String which expected.
        :return: None
        """
        assert result.count(exp), True

    add = Address()
    assert add.address(), not None
    assert add.address(AddressFormats.SHORT), not None



# Generated at 2022-06-13 23:42:41.536876
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())

# Generated at 2022-06-13 23:42:55.534303
# Unit test for method address of class Address
def test_Address_address():
  from mimesis.providers.address import Address
  from mimesis.enums import Locale
  fa=Address('fa', Locale.FA.value)
  print(fa.address())
  print('##############################')
  print(fa.calling_code())
  print('##############################')
  print(fa.continent())
  print('##############################')
  print(fa.postal_code())
  print('##############################')
  print(fa.state(True))
  print('##############################')
  print(fa.country())
  print('##############################')
  print(fa.state())
  print('##############################')
  print(fa.region())
  print('##############################')
  print(fa.federal_subject())

# Generated at 2022-06-13 23:42:58.356729
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    actual_value = addr.address()
    assert actual_value is not None
    assert isinstance(actual_value, str)
    assert actual_value


# Generated at 2022-06-13 23:43:00.236995
# Unit test for method address of class Address
def test_Address_address():
    A = Address()
    print(A.address())

# Generated at 2022-06-13 23:43:03.338392
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    ADDRESS_NUM=5
    for _ in range(ADDRESS_NUM):
        address.address()

# Generated at 2022-06-13 23:43:07.310171
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    address = Address()
    new_address = address.address()
    assert new_address is not None
    assert len(new_address) > 0


# Generated at 2022-06-13 23:43:08.641471
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() != None

# Generated at 2022-06-13 23:43:11.237213
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert isinstance(address.address(), str) == True



# Generated at 2022-06-13 23:43:29.290316
# Unit test for method address of class Address
def test_Address_address():
    for i in range(10):
        addr = Address('en').address()
        print(addr)


# Generated at 2022-06-13 23:43:30.839416
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    x=address.address()
    return x


# Generated at 2022-06-13 23:43:33.089924
# Unit test for method address of class Address
def test_Address_address():
    data = Address()
    result = data.address()
    print(result)


# Generated at 2022-06-13 23:43:34.835158
# Unit test for method address of class Address
def test_Address_address():
    # assert Address().address() == '20/0/0'
    assert 1 == 0


# Generated at 2022-06-13 23:43:38.134533
# Unit test for method address of class Address
def test_Address_address():
    """This function tests the address method of class Address."""
    address = Address()
    for _ in range(10):
        print(address.address())



# Generated at 2022-06-13 23:43:40.500577
# Unit test for method address of class Address
def test_Address_address():
    root = Address()

    assert len(root.address().split('\n')) == 1

"""
Unit tests for the methods of class Address
"""



# Generated at 2022-06-13 23:43:43.120596
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    assert obj.address()


# Generated at 2022-06-13 23:43:48.297074
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    address = Address().address()
    assert address
    assert isinstance(address, str)

    address = Address(CountryCode.ES).address()
    assert address
    assert isinstance(address, str)


# Generated at 2022-06-13 23:43:51.176894
# Unit test for method address of class Address
def test_Address_address():
    # Test addresses
    addresses = ['1953, Rue des Chartreux', '12, Rue des Rosiers']
    obj = Address('en')
    # Checking that address is one of expected
    assert obj.address() in addresses

# Generated at 2022-06-13 23:43:53.213677
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:44:13.011337
# Unit test for method address of class Address
def test_Address_address():
    """Method address() should return a full address."""
    addr = Address()
    full_address = addr.address()
    assert full_address



# Generated at 2022-06-13 23:44:13.883587
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    ad = Address()
    assert ad.address()

# Generated at 2022-06-13 23:44:14.695017
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    assert address.address() == '7962 Red Hawk Circle'



# Generated at 2022-06-13 23:44:16.565905
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='zh')
    print(a.address())


# Generated at 2022-06-13 23:44:17.369591
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() != ''

# Generated at 2022-06-13 23:44:20.651435
# Unit test for method address of class Address
def test_Address_address():
    x0 = Address()
    x1 = Address()
    assert x0.address() != x1.address()


# Generated at 2022-06-13 23:44:22.531248
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    print(address.address())

# Generated at 2022-06-13 23:44:24.872837
# Unit test for method address of class Address
def test_Address_address():
    """ function to test address() method of class Address. """
    name = Address()
    print(name.address())

# Generated at 2022-06-13 23:44:29.530916
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address()
    assert address.address() != ''
    assert address.address() != ' '
    assert address.address() == address.address()



# Generated at 2022-06-13 23:44:31.069352
# Unit test for method address of class Address
def test_Address_address():
    """Test address."""
    assert Address().address()

# Generated at 2022-06-13 23:45:22.025098
# Unit test for method address of class Address
def test_Address_address():
    add = Address("en")
    result = add.address()
    assert type(result) == str


# Generated at 2022-06-13 23:45:24.838010
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    addr = adr.address()
    assert(addr)


# Generated at 2022-06-13 23:45:33.800229
# Unit test for method address of class Address
def test_Address_address():
    """Call to method address of class Address."""
    add = Address(seed=10)

    assert add.address() == 'Rua Joaquina Lima, 1'

    add.locale = 'en-GB'
    assert add.address() == 'Flat 1,\n1 Bryanston Street'

    add.locale = 'pt'
    assert  add.address() == 'Avenida Almirante Barroso, Abadia das Neves, Bariri'

    add.locale = 'ru'
    assert add.address() == 'ул. Небитов, д. 5, корп. 10, Коломенск'


# Generated at 2022-06-13 23:45:34.925767
# Unit test for method address of class Address
def test_Address_address():
    assert Address('en').address() is not None


# Generated at 2022-06-13 23:45:57.935989
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    d = a._data
    fmt = d['address_fmt']

    # All formats in address_fmt should contains three variables: st_num, st_name, st_sfx
    for k, v in fmt.items():
        assert '{st_num}' in v
        assert '{st_name}' in v
        assert '{st_sfx}' in v

    st_num = a.street_number()
    st_name = a.street_name()

    # TODO: Update when new locales/data will be added.
    # Check if address is correct based on locale.
    if a.locale in SHORTENED_ADDRESS_FMT:
        generated_address = a.address()
        assert '{st_num}' not in generated_address

# Generated at 2022-06-13 23:46:01.429301
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    data = a.address()
    assert len(data) > 0
    assert isinstance(data, str)


# Generated at 2022-06-13 23:46:05.883780
# Unit test for method address of class Address
def test_Address_address():
    dataProvider = Address()
    json_data = dataProvider._pull(dataProvider._datafile)
    result = dataProvider.address()
    assert result == ("{st_num} {st_name}"
                        .format(st_num=dataProvider.street_number(),
                                st_name=dataProvider.street_name()))


# Generated at 2022-06-13 23:46:12.518087
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    # street number should be 1-1400
    st_num = int(address.street_number())
    assert 1 <= st_num <= 1400
    # get street name
    st_name = address.street_name()
    assert isinstance(st_name, str)
    # get street suffix
    st_sfx = address.street_suffix()
    assert isinstance(st_sfx, str)
    # get address
    result = address.address()
    assert isinstance(result, str)



# Generated at 2022-06-13 23:46:15.261881
# Unit test for method address of class Address
def test_Address_address():
    from pprint import pprint
    from random import seed
    from random import randint
    seed(randint(0, 10000))
    for i in range(10):
        pprint([Address('en').address() for i in range(10)])

# Generated at 2022-06-13 23:46:22.349005
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    a = Address(seed=0)
    assert a.address() == '2037 HWY 97' # Current locale

    a = Address(seed=0, locale='zh-CN')
    assert a.address() == '816江苏路'

    a = Address(seed=0, locale='ja-JP')
    assert a.address() == '東京都杉並区佐藤町3丁目20番地'


# Generated at 2022-06-13 23:47:56.020159
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import AddressComponent
    from mimesis import Address

    a = Address()
    #AddressComponent.STREET_NAME.value
    #AddressComponent.STREET_NUMBER.value
    #AddressComponent.STREET_SUFFIX.value
    #AddressComponent.STATE.value
    #AddressComponent.COUNTRY.value
    #AddressComponent.CITY.value
    #AddressComponent.POSTAL_CODE_FORMAT.value
    #AddressComponent.POSTAL_CODE.value
    #AddressComponent.FULL_ADDRESS.value
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())

# Generated at 2022-06-13 23:48:03.575894
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import AddressFormats
    from mimesis.typing import Seed

    a = Address(seed=Seed.RANDOM)
    assert isinstance(a.address(), str)
    assert a.address(formatter=AddressFormats.COMMON)
    assert not a.address(formatter=AddressFormats.COMMON)

    a = Address('ru', seed=Seed.RANDOM)
    assert isinstance(a.address(), str)
    assert a.address(formatter=AddressFormats.COMMON)
    assert not a.address(formatter=AddressFormats.COMMON)

# Generated at 2022-06-13 23:48:05.861228
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address(locale='en')
    address.address()
    # '42641 Miguel Spur, Verona, Osinatown'


# Generated at 2022-06-13 23:48:09.189615
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address

    a = Address()
    r = a.address()
    assert bool(r)



# Generated at 2022-06-13 23:48:12.908977
# Unit test for method address of class Address
def test_Address_address():
    # Arrange
    from mimesis import Address

    a = Address()

    # Action
    result = a.address()

    # Assert
    assert isinstance(result, str)


# Generated at 2022-06-13 23:48:14.889959
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:48:15.737047
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()

# Generated at 2022-06-13 23:48:26.651881
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Language
    from mimesis.localization import DEFAULT_LANGUAGE
    from mimesis.mapping import REGIONS
    # Initialize object Address
    addr = Address(language=Language.EN)
    # Get the default locale
    locale = DEFAULT_LANGUAGE
    # Get the region
    region = REGIONS[locale]
    # Get the country
    country = region['country']['current_locale']
    # Get the city
    city = addr.random.choice(region['city'])
    # Get the street
    street = addr.random.choice(region['street']['name'])
    # Get the street suffix
    street_suffix = addr.random.choice(region['street']['suffix'])
    # Get the street number
    street

# Generated at 2022-06-13 23:48:27.321970
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()


# Generated at 2022-06-13 23:48:32.112845
# Unit test for method address of class Address
def test_Address_address():
    """Test address and zip_code method.
    """

    import pytest

    from mimesis.builtins import Address as address

    addr = address(seed=1)
    assert addr.address() == '112 Woylie Turn'
    assert addr.address() == '1161 Glyer Rd'
    assert addr.address() == '1161 Glyer Rd'
    assert addr.address() == '1599 E 10th Ln'
    assert addr.address() == '1599 E 10th Ln'
    assert addr.address() == '1599 E 10th Ln'
    assert addr.address() == '1599 E 10th Ln'
    assert addr.zip_code() == '85945-5656'
    assert addr.zip_code() == '85945-5656'
    assert addr.zip_code()
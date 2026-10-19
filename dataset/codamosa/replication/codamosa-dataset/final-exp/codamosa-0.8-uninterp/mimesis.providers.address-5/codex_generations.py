

# Generated at 2022-06-13 23:39:46.276679
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    # French
    address = Address(locale=Locale.FR)
    st_num = address.street_number()
    st_name = address.street_name()
    st_sfx = address.street_suffix()
    assert address.address() == '{} {} {}'.format(st_num, st_name, st_sfx)

    # Chinese
    address = Address(locale=Locale.ZH_HANS)
    assert address.address() == st_name

    # English
    address = Address(locale=Locale.EN)
    assert address.address() == st_name

    # German
    address = Address(locale=Locale.DE)
    assert address.address() == st_name

    # Russian

# Generated at 2022-06-13 23:39:47.892071
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    weight = len(A.address())/len(A.address())
    assert weight > 0.9

# Generated at 2022-06-13 23:39:51.922650
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    # Init instance of class Address
    address = Address()

    # DataProvider.seed(None)
    # Common tests
    # data = [address.address() for _ in range(10)]
    result = address.address()
    assert 'street' in result
    assert isinstance(result, str)
    assert isinstance(address.address(), str)

# Generated at 2022-06-13 23:39:54.280995
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    addr = address.address()
    assert isinstance(addr, str)

# Generated at 2022-06-13 23:39:55.850750
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:40:02.367465
# Unit test for method address of class Address
def test_Address_address():
    print('\n=== Test Address class, method address ===')
    import test_provider_Address
    test = True
    for _ in range(10):
        if test_provider_Address.address_test(
                Address.address,
                parameter="address"
        ):
            print('Address passed')
        else:
            test = False
            print('Address failed')
            break
    if test:
        print('Test passed\n')
    else:
        print('Test failed\n')


# Generated at 2022-06-13 23:40:13.188480
# Unit test for method address of class Address
def test_Address_address():
    region = Address('zh')
    assert region.address() == '陕西省西安市西秦路15号'
    assert Address().address() == '927 Colby Place'
    assert Address('ja').address() == '東京都港区南麻布5-8-13'
    assert Address('en').address() == '60 Hagan Crossing'
    assert Address('ru').address() == 'ул. Академика Иванова, д. 51'
    assert Address('uk').address() == 'вул. Івана Франка, буд. 21'


# Generated at 2022-06-13 23:40:22.188047
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Country
    from mimesis.enums import Language
    from mimesis.providers.address import Address
    
    #initialize Address with default local
    a = Address()

    # test for default local
    assert a.address() == '407-8165 Cras Ave'

    #test for locale
    a = Address(local = Language.ENGLISH)
    assert a.address() == '407-8165 Cras Ave'
    

# Generated at 2022-06-13 23:40:26.277937
# Unit test for method address of class Address
def test_Address_address():
    language = Address()
    lang = language.provider('lang')
    example = language.address
    assert lang.address == example()
    assert lang.street_number in example()
    assert lang.street_name in example()
    assert lang.postal_code in example()
    assert lang.zip_code in example()
    assert lang.province_abbr in example()
    assert lang.province in example()
    assert lang.city in example()
    assert lang.country in example()
    assert lang.state_abbr in example()
    assert lang.state in example()

# Generated at 2022-06-13 23:40:28.932387
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    result = provider.address()
    print(result)
    assert isinstance(result, str)

# Generated at 2022-06-13 23:40:41.128640
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import en_US

    # Address with default locale
    a = Address()

    # Address with locale
    a1 = Address(a)
    assert a1.address() == a.address()

    # Address with locale
    a2 = Address(locale='en')
    a3 = Address(locale='en-US')
    a4 = Address(locale='en_US')
    a5 = Address(locale='EN_us')
    assert a2.address() == a3.address() == a4.address() == a5.address()

    # Address with locale
    a6 = Address(locale='ja-JP')
    assert a6.address().startswith('東京都')

    # Address with locale
    addr = Address(en_US)

# Generated at 2022-06-13 23:40:43.912806
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    # print(a.address())
    assert a.address()!=None


# Generated at 2022-06-13 23:40:45.306852
# Unit test for method address of class Address
def test_Address_address():
    print(Address(locale='en').address())


# Generated at 2022-06-13 23:40:47.005959
# Unit test for method address of class Address
def test_Address_address():
    assert isinstance(Address().address(), str)
    assert len(Address().address()) == 0


# Generated at 2022-06-13 23:40:49.378595
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0


# Generated at 2022-06-13 23:40:51.457893
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    for i in range(0,10):
        print(i+1, address.address())


# Generated at 2022-06-13 23:40:53.507730
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address()."""
    address = Address()
    assert address.address()


# Generated at 2022-06-13 23:40:55.840655
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    address.address()


# Generated at 2022-06-13 23:40:57.335470
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    print(adr.address())


# Generated at 2022-06-13 23:41:07.083410
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    # Test for locale 'en'
    ad = Address(locale=Locale.EN)
    for _ in range(100):
        assert isinstance(ad.address(), str)
        assert len(ad.address()) > 0

    # Test for locale 'fil'
    ad = Address(locale=Locale.FIL)
    for _ in range(100):
        assert isinstance(ad.address(), str)
        assert len(ad.address()) > 0

    # Test for locale 'nl'
    ad = Address(locale=Locale.NL)
    for _ in range(100):
        assert isinstance(ad.address(), str)
        assert len(ad.address()) > 0

    # Test for locale 'ja'
    ad = Address(locale=Locale.JA)

# Generated at 2022-06-13 23:41:19.942941
# Unit test for method address of class Address
def test_Address_address():
    locale = 'en'
    class_ = Address(locale)
    res = class_.address()
    assert len(res) > 0


# Generated at 2022-06-13 23:41:32.394512
# Unit test for method address of class Address
def test_Address_address():
    expected_result = [
        '5434 Columbia Pointe, Nelsonmouth, RI 68210',
        '596 Prince Street, Ronaldodeath, KY 21693',
        '1490 Lighthouse Bay Drive, Adamschester, ND 81759',
        '7180 Falcon Ridge, East Torie, GA 94040',
        '6024 Rolling Acres, South Marielle, TN 24829',
    ]
    example_address = Address()
    result = []
    [result.append(example_address.address()) for i in range(5)]
    assert all(result == expected_result)


# Generated at 2022-06-13 23:41:37.972784
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address()
    format = "пл.{st_num} {st_name} {st_sfx}"
    assert address.address(format=format)


# Generated at 2022-06-13 23:41:38.643748
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()

# Generated at 2022-06-13 23:41:42.697969
# Unit test for method address of class Address
def test_Address_address():
    generator = Address()

    # I've taken a result from random run, becasue
    # the result changes each time.
    #
    # The result is '424562 Capricorn Lane'
    address_result = generator.address()

    assert address_result == "424562 Capricorn Lane"



# Generated at 2022-06-13 23:41:45.231020
# Unit test for method address of class Address
def test_Address_address():

    obj = Address('en')
    print(obj.address())
    print(obj.street_number())
    print(obj.zip_code())
    print(obj.calling_code())
    print(obj.continent())



# Generated at 2022-06-13 23:41:48.197978
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result is not None


# Generated at 2022-06-13 23:41:50.007763
# Unit test for method address of class Address
def test_Address_address():
    # Tests for address() method
    print(Address().address())

# Generated at 2022-06-13 23:41:52.542858
# Unit test for method address of class Address
def test_Address_address():
    """Test for method address of class Address."""
    result = Address().address()
    assert result is not None

# Generated at 2022-06-13 23:41:53.741125
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('en')
    print(addr.address())
    data = {'address':[addr.address() for i in range(10)]}
    print(data)


# Generated at 2022-06-13 23:42:14.600687
# Unit test for method address of class Address
def test_Address_address():
    a = Address(seed=1337)
    assert a.address() == '3147 Schiller Straße'
    assert a.address() == '3743 Ortigas Avenue'
    assert a.address() == '3484 Nguyễn Văn Linh Avenue'
    assert a.address() == '1055 Ashburton Road'
    assert a.address() == '8410 High Street'
    assert a.address() == '1871 Main St'
    assert a.address() == '101 First St'
    assert a.address() == '6018 Avenue du Parc'
    assert a.address() == '60-902 Poznań, Piłsudskiego 6'
    assert a.address() == '3-1-2 Asakusa, Taito-ku, Tokyo'

# Generated at 2022-06-13 23:42:16.305390
# Unit test for method address of class Address
def test_Address_address():
    address_object = Address()
    result = address_object.address()
    assert (type(result) == 'str')

# Generated at 2022-06-13 23:42:18.428358
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    assert isinstance(a.address(), str)



# Generated at 2022-06-13 23:42:25.282136
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for test_Address_address()."""
    from mimesis.enums import Locale
    from mimesis.localization import SHORTENED_ADDRESS_FORMATS
    address = Address()

    for locale in SHORTENED_ADDRESS_FORMATS:
        address = Address(locale=Locale(locale))
        assert isinstance(address.address(), str)
        assert len(address.address()) > 10

    assert isinstance(address.address(), str)
    assert len(address.address()) > 10

# Generated at 2022-06-13 23:42:26.336032
# Unit test for method address of class Address
def test_Address_address():
    assert len(Address().address()) > 0

# Generated at 2022-06-13 23:42:31.709642
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address.
    """
    address = Address()
    address_obj = address._data['address_fmt']
    assert address.address() == address_obj.format(
        st_num=address.street_number(),
        st_name=address.street_name(),
        st_sfx=address.street_suffix(),
    )

# Generated at 2022-06-13 23:42:33.307979
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() in Address().get_data("address_fmt")


# Generated at 2022-06-13 23:42:35.411074
# Unit test for method address of class Address
def test_Address_address():
  address_obj = Address()

  assert isinstance(address_obj.address(),str)


# Generated at 2022-06-13 23:42:37.000328
# Unit test for method address of class Address
def test_Address_address():
    result = Address("zh").address()
    assert result is not None
    assert len(result) > 0

# Generated at 2022-06-13 23:42:40.439555
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='zh')
    print(address.address())
    print(address.postal_code())
    print(address.country_code())
    print(address.country_code(CountryCode.A3))
    print(address.country())

if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:42:55.003715
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()
    assert len(Address().address()) != 0


# Generated at 2022-06-13 23:42:57.492308
# Unit test for method address of class Address
def test_Address_address():
    add = Address()
    print(add.address())

if __name__ == "__main__":
    test_Address_address()

# Generated at 2022-06-13 23:43:01.823106
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    result = adr.address()
    assert isinstance(result, str)
    assert len(result) > 0


# Generated at 2022-06-13 23:43:04.269266
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address().address()

# Generated at 2022-06-13 23:43:17.986610
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Country
    from mimesis.localization import Localization
    from mimesis.types import Involatile
    address = Address(localization=Localization(locales=['en-GB']))
    address.seed(1)
    assert address.address() == '27 Hyde Lane'
    assert address.address() == '310 Bridge Street'
    assert address.address() == '9 Military Street'
    assert address.address() == '14 Glendale Street'
    assert address.address() == '39 Prospect Avenue'
    address = Address(localization=Localization(locales=['de-DE']))
    address.seed(1)
    assert address.address() == 'Winterbergweg 38'
    assert address.address() == 'Taunusring 87'

# Generated at 2022-06-13 23:43:31.093945
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.exceptions import NonEnumerableError
    from mimesis.enums import CountryCode
    from mimesis.utils import random_int
    from mimesis.builtins import Address

    _address = Address()

    for _ in range(random_int(1, 10)):
        assert _address.address()
        assert _address.address(locale='en')
        # return int(1)

    assert _address.state()
    assert _address.state(True)
    assert _address.region()
    assert _address.region(True)
    assert _address.province()
    assert _address.province(True)
    assert _address.federal_subject()
    assert _address.federal_subject(True)
    assert _address.prefecture()

# Generated at 2022-06-13 23:43:33.666269
# Unit test for method address of class Address
def test_Address_address():
    res=Address().address()
    assert len(Address().address()) >= 1
    assert (Address().address()) in res


# Generated at 2022-06-13 23:43:35.937317
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert isinstance(result, str)
    assert len(result) > 0


# Generated at 2022-06-13 23:43:37.515425
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())

# Generated at 2022-06-13 23:43:39.671342
# Unit test for method address of class Address
def test_Address_address():
    """Test for method address of class Address."""
    address = Address()
    for _ in range(10):
        assert address.address()


# Generated at 2022-06-13 23:44:08.338670
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address()."""
    addr = Address()
    assert isinstance(addr.address(), str)


# Generated at 2022-06-13 23:44:10.407355
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address().__class__ == str


# Generated at 2022-06-13 23:44:12.279038
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    a1 = address.address()
    print(a1)



# Generated at 2022-06-13 23:44:14.514306
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() is not None
    assert isinstance(a.address(), str)



# Generated at 2022-06-13 23:44:15.668184
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    ad.address()

# Generated at 2022-06-13 23:44:21.406097
# Unit test for method address of class Address
def test_Address_address():
    address1 = Address()
    address2 = Address()
    assert address1.address() != address2.address()
    assert isinstance(address1.address(), str)
    assert isinstance(address2.address(), str)



# Generated at 2022-06-13 23:44:23.256453
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    assert bool(obj.address()) == True


# Generated at 2022-06-13 23:44:24.934124
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address().count(" ") == 2


# Generated at 2022-06-13 23:44:36.332232
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address as Address1
    from random import choice as random_choice
    from json import loads as json_loads

    address = Address1()

    address_en = json_loads(open("address_en.json").read())
    address_en_address = address_en["address"]

    street_name = lambda: random_choice(address_en_address["street"]["name"])
    street_suffix = lambda: random_choice(address_en_address["street"]["suffix"])

    assert address.address() == "{} {}, {} {} {}".format(
        address.street_number(),
        street_name(),
        street_name(),
        street_suffix(),
        address.city(),
    )


# Generated at 2022-06-13 23:44:58.451101
# Unit test for method address of class Address
def test_Address_address():
    import pytest
    from mimesis.builtins import Localization
    from mimesis.enums import Language
    # Unit test for method address of class Address
    @pytest.mark.parametrize(
        'localization',
        Localization.get_available_languages(
            Language.from_alias('ru'),
        ),
    )
    def test_address(localization):
        ad = Address(localization, seed=123)
        assert ad.address() == '26/2 Сергея Гени-Карпова проспект, г.Иркутск'

    test_address()

# Generated at 2022-06-13 23:45:26.478909
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    a = addr.address()
    assert isinstance(a, str)


# Generated at 2022-06-13 23:45:29.162174
# Unit test for method address of class Address
def test_Address_address():
    addr = Address(locale='en')
    print(addr.address())


# Generated at 2022-06-13 23:45:40.298293
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address()
    assert address.address() == '{st_num} {st_name}'
    assert address.address() == '{st_num} {st_name} {st_sfx}'
    assert address.address() == '{st_num} {st_name} {st_sfx} {st_sfx}'
    assert address.address() == '{st_num} {st_name} {st_sfx} {st_sfx} {st_sfx}'
    assert address.address() == '{st_num} {st_name} {st_sfx} {st_sfx}'
    assert address.address() == '{st_num} {st_name} {st_sfx}'
    assert address.address()

# Generated at 2022-06-13 23:45:57.937493
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address

    addr = Address()
    assert bool(addr.address())
    assert bool(addr.address())
    assert bool(addr.address())
    assert bool(addr.address())
    assert bool(addr.address())

    #  test for ja language
    from mimesis.localization import JapaneseLocalization

    local_ja = JapaneseLocalization()
    addr = Address(local_ja)
    assert bool(addr.address())
    assert bool(addr.address())
    assert bool(addr.address())
    assert bool(addr.address())
    assert bool(addr.address())

    #  test for zh language
    from mimesis.localization import ChineseLocalization

    local_zh = ChineseLocalization()
    addr = Address(local_zh)
    assert bool(addr.address())


# Generated at 2022-06-13 23:46:02.920999
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_format = address._data['street']['name_fmt']
    address_format = address._data['address_fmt']
    output = address.address()
    assert street_format in output
    assert address_format in output



# Generated at 2022-06-13 23:46:04.609090
# Unit test for method address of class Address
def test_Address_address():
    a = Address(seed=123)
    print(a.address())

# Generated at 2022-06-13 23:46:05.980446
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None


# Generated at 2022-06-13 23:46:07.069558
# Unit test for method address of class Address
def test_Address_address():
    assert 'address' in Address().address()

# Generated at 2022-06-13 23:46:10.209722
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    a = Address('en')
    i = a.address()
    assert isinstance(i, str)
    return i


# Generated at 2022-06-13 23:46:11.613985
# Unit test for method address of class Address
def test_Address_address():

    addr = Address()
    result = addr.address()
    assert result, result
    assert type(result) == str, result

# Generated at 2022-06-13 23:46:53.068822
# Unit test for method address of class Address
def test_Address_address():
    print('Testing Address address')
    print('expected to be  10 Downing St, London SW1A 2AA, United Kingdom')
    test_Address = Address(locale='en')
    result = test_Address.address()
    print(result)
    assert 'London' in result, result
    assert 'SW1A' in result, result
    assert 'United Kingdom' in result, result
    print('expected to be  10-1 Akasaka 9-chome, Minato-ku, Tokyo, 107-0052, Japan')
    test_Address = Address(locale='ja')
    result = test_Address.address()
    print(result)
    assert 'Tokyo' in result, result
    assert '107-0052' in result, result
    assert 'Japan' in result, result

# Generated at 2022-06-13 23:46:59.423735
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    b = Address()
    c = Address()
    d = Address()
    e = Address()
    f = Address()

    assert(a.address() == "4038 Oakridge Place")
    assert(b.address() == "1290 Hickory Trail")
    assert(c.address() == "1057 Bernice Pass")
    assert(d.address() == "61354 Eastview Lane")
    assert(e.address() == "5111 Mockingbird Hill")
    assert(f.address() == "2919 Bowman Way")


# Generated at 2022-06-13 23:47:02.923032
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    test = a.address()
    print(test)


# Generated at 2022-06-13 23:47:04.129724
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())

# Generated at 2022-06-13 23:47:05.764666
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    assert provider.address()


# Generated at 2022-06-13 23:47:08.707847
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)
    assert a.address() == '123 Sweet Street #17, Apt. 898'


# Generated at 2022-06-13 23:47:10.924096
# Unit test for method address of class Address
def test_Address_address():
  from mimesis.enums import DataProvider
  a = Address(DataProvider.KOREAN)
  print(a.address())

# Generated at 2022-06-13 23:47:12.610634
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())


# Generated at 2022-06-13 23:47:14.900213
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    assert len(address.address()) == 3


# Generated at 2022-06-13 23:47:21.211372
# Unit test for method address of class Address
def test_Address_address():
    """Test method Address.address()"""

    from mimesis.enums import Locale
    from mimesis import Address

    a = Address()

    # Check if the method returns a result
    assert a.address() != None
    assert a.address() != ' '

    # Check for the correct length
    assert len(a.address()) >= 10

    # Check if exists Address for other locales
    for locale in Locale:
        _a = Address(locale)
        assert _a.address() != None
        assert _a.address() != ' '
        assert len(_a.address()) >= 10



# Generated at 2022-06-13 23:39:40.675216
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    result = address.address()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:39:41.549260
# Unit test for method address of class Address
def test_Address_address():
    fn = Address().address()
    assert fn != fn



# Generated at 2022-06-13 23:39:47.149737
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    fmt = address._data['address_fmt']
    st_num = address.street_number()
    st_name = address.street_name()
    st_sfx = address.street_suffix()
    assert address.address() == fmt.format(st_num=st_num, st_name=st_name, st_sfx=st_sfx)

# Generated at 2022-06-13 23:39:49.185043
# Unit test for method address of class Address
def test_Address_address():
    assert Address('en').address()
    assert Address('uk').address()
    assert Address('es').address()


# Generated at 2022-06-13 23:39:53.075211
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    obj = Address(random_state=0)
    assert obj.address() == '3677 Hansons Branch Apt. 052'

# Generated at 2022-06-13 23:39:55.519673
# Unit test for method address of class Address
def test_Address_address():
    addressGenerator = Address(locale='en')
    print(addressGenerator.address())



# Generated at 2022-06-13 23:39:57.474023
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    a = Address('en')
    assert a.address()


# Generated at 2022-06-13 23:40:01.669861
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    person = Person(Gender.MALE, RussiaSpecProvider)
    person.name
    pass



# Generated at 2022-06-13 23:40:03.584157
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    assert a.address() != None

# Generated at 2022-06-13 23:40:05.303082
# Unit test for method address of class Address
def test_Address_address():
    address1 = Address().address()
    address2 = Address().address()
    assert address1 != address2


# Unit tests for Address class

# Generated at 2022-06-13 23:40:12.886649
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='en')
    result = a.address()
    assert result is not None and result != ''

# Generated at 2022-06-13 23:40:17.229939
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.address()
    # print(address) # debug
    if ' ' in address:
        assert True
    else:
        assert False


# Generated at 2022-06-13 23:40:25.503534
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    from mimesis.enums import Locale

    _obj = Address(locale=Locale.CANADA_FRENCH)
    _str = '{0} {1} {2}'.format(
        _obj.street_number(),
        _obj.street_name(),
        _obj.street_suffix(),
    )
    assert _obj.address() == _str

# Generated at 2022-06-13 23:40:27.733673
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address()."""
    assert Address().address() in Address()._data['address_fmt']

# Generated at 2022-06-13 23:40:31.679609
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_number = address.street_number()
    street_name = address.street_name()
    street_suffix = address.street_suffix()
    print("{} {} {}".format(street_number, street_name, street_suffix))



# Generated at 2022-06-13 23:40:36.478185
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    result = address.address()
    assert bool(address.validate.street(result))
    assert address.validate.street_number(address.street_number(), result)
    assert address.validate.street_name(address.street_name(), result)
    assert address.validate.street_suffix(address.street_suffix(), result)


# Generated at 2022-06-13 23:40:40.054034
# Unit test for method address of class Address
def test_Address_address():
    from doctest import testmod
    from mimesis.builtins import address

    address_ = Address()

    assert isinstance(address_.address(), str)

    # doctest for address method
    testmod()


# Generated at 2022-06-13 23:40:43.590888
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    a = Address()
    assert (a.address() != '')
    assert (len(a.address()) > 0)

# Generated at 2022-06-13 23:40:47.306991
# Unit test for method address of class Address
def test_Address_address():
    address=Address()
    print(address.address())
    print(address.calling_code())
    print(address.city())
    print(address.coordinates())
    print(address.country_cde())
    print(address.country())
    print(address.latitude())
    print(address.longitude())
    print(address.postal_code())
    print(address.region())
    print(address.state())
    print(address.street_name())
    print(address.street_number())
    print(address.street_suffix())
    print(address.zip_code())

# Generated at 2022-06-13 23:40:49.680503
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    b = a.address()
    assert isinstance(b, str)
    assert len(b) > 0
    assert " " in b


# Generated at 2022-06-13 23:40:56.708390
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address()
    assert address.address()


# Generated at 2022-06-13 23:40:58.932705
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    assert type(a.address()) is str


# Generated at 2022-06-13 23:41:00.473164
# Unit test for method address of class Address
def test_Address_address():
    address_test=Address()
    print(address_test.address())

# Generated at 2022-06-13 23:41:06.264452
# Unit test for method address of class Address
def test_Address_address():
    random.seed(0)

    a = Address(random)
    assert a.address() == "50 Pinnock Dr"

    random.seed(1)
    a = Address(random)
    assert a.address() == "8 Oakwood Ln"

    # Test for internationalization of Address.address
    random.seed(0)
    a = Address(random, locale="ru_RU")
    assert a.address() == "пер. Солнечный, 3-18"

# Generated at 2022-06-13 23:41:08.759000
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    result = address.address()
    print(result)


# Generated at 2022-06-13 23:41:11.063115
# Unit test for method address of class Address
def test_Address_address():
    address = Address().address()
    assert address is not None
    assert address is not ''


# Generated at 2022-06-13 23:41:12.065217
# Unit test for method address of class Address
def test_Address_address():
    assert type(Address().address()) == str

# Generated at 2022-06-13 23:41:13.566102
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    print('Address address(...)', obj.address())

# Generated at 2022-06-13 23:41:16.207162
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    address = Address()
    print(address.address())



# Generated at 2022-06-13 23:41:20.664624
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_number = address.street_number()
    street_name = address.street_name()
    street_suffix = address.street_suffix()
    address_fmt = address._data['address_fmt']
    expected = address_fmt.format(st_num=street_number, st_name=street_name, st_sfx=street_suffix)

    assert address.address() == expected


# Generated at 2022-06-13 23:41:27.353275
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert type(address.address()) == str


# Generated at 2022-06-13 23:41:38.490798
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender

    p = Address(locale='en')
    test_address = p.address()
    assert isinstance(test_address, str)
    assert test_address.count(' ') == 3
    assert test_address.split(' ')[0].isdigit()

    p = Address(locale='ja')
    test_address = p.address()
    assert isinstance(test_address, str)
    assert test_address.count(' ') == 2
    assert test_address.split(' ')[0] in p.data['city']

    p = Address(locale='en')
    test = p.build_address()
    assert isinstance(test, dict)
    for key, value in test.items():
        assert len(value) != 0


# Generated at 2022-06-13 23:41:41.326088
# Unit test for method address of class Address
def test_Address_address():
    """Check if address is not empty and has required format.
    """
    addr_str = Address(
        "en").address()
    assert addr_str


# Generated at 2022-06-13 23:41:42.466469
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert type(address.address()) == str


# Generated at 2022-06-13 23:41:43.567727
# Unit test for method address of class Address
def test_Address_address():
    ad = Address('en')
    a = ad.address()
    print(a)

# Generated at 2022-06-13 23:41:48.430462
# Unit test for method address of class Address
def test_Address_address():

    # Locale en_US
    Address_en_US = Address(locale='en_US')
    address_en_US = Address_en_US.address()
    assert isinstance(address_en_US, str)

    # Locale en_UK
    Address_en_UK = Address(locale='en_UK')
    address_en_UK = Address_en_UK.address()
    assert isinstance(address_en_UK, str)

    # Locale ja
    Address_ja = Address(locale='ja')
    address_ja = Address_ja.address()
    assert isinstance(address_ja, str)

# Generated at 2022-06-13 23:41:51.201422
# Unit test for method address of class Address
def test_Address_address():
    address = Address('fr')
    assert address.address() == "Le carré d'or 32/25 rue Sébastopol"


# Generated at 2022-06-13 23:41:53.633943
# Unit test for method address of class Address
def test_Address_address():
  address = Address('zh')
  r = address.address()
  assert r
  print(r)


# Generated at 2022-06-13 23:41:54.226919
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()

# Generated at 2022-06-13 23:41:55.734649
# Unit test for method address of class Address
def test_Address_address():
    for i in range(10):
        print(Address().address())


# Generated at 2022-06-13 23:42:01.875609
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    assert address.address() != ''


# Generated at 2022-06-13 23:42:04.143841
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address()."""
    address = Address()
    addr = address.address()
    assert type(addr) is str
    assert addr



# Generated at 2022-06-13 23:42:05.592687
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.address()
    assert address



# Generated at 2022-06-13 23:42:13.751286
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    from mimesis.builtins import Address
    country_kg = Address("ru")
    country_kg.country(allow_random=True)
    country_kg.postal_code()
    country_kg.country(allow_random=True)
    country_kg.region()
    country_kg.street_number()
    country_kg.street_name()
    country_kg.state()
    country_kg.city()
    country_kg.calling_code()
    country_kg.zip_code()
    country_kg.country_code()
    country_kg.address()
    country_kg.coordinates()

# Generated at 2022-06-13 23:42:16.233841
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    for _ in range(0, 100):
        method_result = provider.address()
        print(method_result)
        print('\n')

# Generated at 2022-06-13 23:42:17.594876
# Unit test for method address of class Address
def test_Address_address():
    pass


# Generated at 2022-06-13 23:42:18.615520
# Unit test for method address of class Address
def test_Address_address():
    assert Address('ru').address()


# Generated at 2022-06-13 23:42:29.028333
# Unit test for method address of class Address
def test_Address_address():

    add1 = Address(locale='it')
    add2 = Address(locale='en')
    add3 = Address(locale='pt')
    add4 = Address(locale='fr')
    add5 = Address(locale='zh')
    add6 = Address(locale='ja')
    add7 = Address(locale='ru')
    add8 = Address(locale='es')
    add9 = Address(locale='de')
    add10 = Address(locale='ko')

    assert 'Via' in add1.address()
    assert 'Rua' in add3.address()
    assert 'Rue' in add4.address()
    assert '路' in add5.address()
    assert '丁目' in add6.address()

# Generated at 2022-06-13 23:42:30.367988
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert len(addr.address().split(' ')) == 6

# Generated at 2022-06-13 23:42:38.462409
# Unit test for method address of class Address

# Generated at 2022-06-13 23:42:49.532330
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    expected = '{} {} {}'.format(
        address.street_number(),
        address.street_name(),
        address.street_suffix(),
    )
    actual = address.address()
    assert actual == expected


# Generated at 2022-06-13 23:42:57.541839
# Unit test for method address of class Address
def test_Address_address():
    c = Address(seed=1234)
    assert c.address() == 'Brasil 1801'
    assert c.address() == 'Av. Colina 441'
    assert c.address() == 'Rua dos Pinheiros 486'
    assert c.address() == 'Av. Brasil 943'
    assert c.address() == 'R. Gregório de Matos 67'
    assert c.address() == 'R. dos Goitacazes 342'


# Generated at 2022-06-13 23:42:59.689462
# Unit test for method address of class Address
def test_Address_address():
    ob = Address()
    return ob.address()

# Generated at 2022-06-13 23:43:13.098970
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address"""
    address = Address(random_state=1)
    # test for ru locale
    address.set_locale('ru')
    assert address.address() == 'Улица Поправки6'
    # test for ja locale
    address.set_locale('ja')
    assert address.address() == '記帳会社8-9-9'
    # test for ua locale
    address.set_locale('ua')
    assert address.address() == 'ул. Монастирська, 29'
    # test for us locale
    address.set_locale('us')
    assert address.address() == '12295 Summit Street'

# Generated at 2022-06-13 23:43:15.090869
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()


# Generated at 2022-06-13 23:43:17.623711
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    assert address.address().__len__() > 10
    assert address.address().__len__() < 40


# Generated at 2022-06-13 23:43:19.588389
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    address = Address()
    print(address.address())
    
# test_Address_address()



# Generated at 2022-06-13 23:43:22.000223
# Unit test for method address of class Address
def test_Address_address():

    addr = Address()
    assert isinstance(addr.address(), str)


# Generated at 2022-06-13 23:43:26.033918
# Unit test for method address of class Address
def test_Address_address():
    a1 = Address('en')
    print(a1.address())  # e.g. 672 Williams Street
    a2 = Address('ja')
    print(a2.address())  # e.g. 48-7-14 Yamada street

# Generated at 2022-06-13 23:43:34.241631
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address."""
    ad = Address('en')
    assert ad.street_number() == ad.street_number()
    assert ad.street_name() == ad.street_name()
    assert ad.street_suffix() == ad.street_suffix()
    assert ad.address() == ad.address()
    assert ad.state(abbr=True) == ad.state(abbr=True)
    assert ad.postal_code() == ad.postal_code()
    assert ad.country() == ad.country()
    assert ad.city() == ad.city()

# Generated at 2022-06-13 23:43:50.556789
# Unit test for method address of class Address
def test_Address_address():
    address_obj = Address()
    assert address_obj.address() == '{0[0]} {0[1]} {0[2]}'.format(address_obj.random.choices(population=address_obj._data['street']['name'],k=3))


# Generated at 2022-06-13 23:43:52.602795
# Unit test for method address of class Address
def test_Address_address():
    assert Address('zh').address() == 'Dakelichang'


# Generated at 2022-06-13 23:43:54.884116
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='en')
    assert a.address().startswith('22')



# Generated at 2022-06-13 23:43:56.845786
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale="en-us")
    assert address.address() == "2943 Hallows Rue"

# Generated at 2022-06-13 23:44:05.592999
# Unit test for method address of class Address

# Generated at 2022-06-13 23:44:09.780867
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    print(Address(Locale.EN).address())
    assert Address(Locale.EN).address() == '686 Town Street, Wyman, AR 2200'


# Generated at 2022-06-13 23:44:13.519902
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale 
    print("Calling Address.address")
    address = Address(locale=Locale.ENGLISH)
    for a in range(10):
        print(address.address())


# Generated at 2022-06-13 23:44:16.257321
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address

    rs = Address(Locale.FRENCH)
    assert rs.address()

# Generated at 2022-06-13 23:44:29.312122
# Unit test for method address of class Address
def test_Address_address():
	print('\nTest Address_address')
	fmt_t = '{}, {}, {}, {}, {}'
	address_generator = Address()
	print(address_generator.address())
	print(fmt_t.format(address_generator.street_number(), address_generator.street_name(), address_generator.street_suffix(), address_generator.state(), address_generator.country()))
	print()
	print(address_generator.address())
	print(fmt_t.format(address_generator.street_number(), address_generator.street_name(), address_generator.street_suffix(), address_generator.state(), address_generator.country()))


# Generated at 2022-06-13 23:44:30.840817
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() is not None


# Generated at 2022-06-13 23:45:16.142852
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis.enums import AddressFormat
    loc_list = [AddressFormat.FULL, AddressFormat.SHORTENED, 'ja']
    for loc in loc_list:
        ad = Address(locale=loc)
        result = ad.address()
        assert isinstance(result, str)
        assert len(result) > 0


# Generated at 2022-06-13 23:45:18.113415
# Unit test for method address of class Address
def test_Address_address():
    ad = Address('en')
    field = 'address'
    for i in range(10):
        assert isinstance(ad.address(), str)
        assert ad.field(field) == ad.address()

# Generated at 2022-06-13 23:45:20.818340
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    addr = address.address()
    assert isinstance(addr,str)

# Generated at 2022-06-13 23:45:34.897535
# Unit test for method address of class Address
def test_Address_address():
    from utils import seed
    from random import randint
    from collections import OrderedDict
    
    # Translate function from mimesis
    from mimesis.builtins import Translator
    translator = Translator('en')
    
    seed(4)
    # The maximum value of street number is 1400
    maximum = randint(1, 1400)
    
    # Initialize Address class
    data = Address()
    
    # Generate a random address
    result = data.address()
    assert result == '1331 Maple Hill'
    
    # Generate a random full address
    result = data.address(maximum)
    assert result == '1123 Maple Hill'
    
    # Get a random street name
    result = data.street_name()
    assert result == 'Maple Hill'
    
    # Get a random

# Generated at 2022-06-13 23:45:36.520222
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()

    assert type(obj.address()) == str
    assert obj.address() != ''


# Generated at 2022-06-13 23:45:38.436827
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert 0 < len(a.address()) <= 100


# Generated at 2022-06-13 23:45:45.612108
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='en')
    res = a.address()
    assert all(isinstance(i, str) for i in (res,))
    assert res

    b = Address(locale='ja')
    assert b.address()
    c = Address(locale='si')
    assert c.address()
    d = Address(locale='et')
    assert d.address()
    e = Address(locale='sl')
    assert e.address()


# Generated at 2022-06-13 23:46:00.652232
# Unit test for method address of class Address
def test_Address_address():
    address_obj = Address()
    assert address_obj.address() != ""

# Generated at 2022-06-13 23:46:07.159561
# Unit test for method address of class Address
def test_Address_address():
    # Initialize address object and call method address()
    address = Address()
    a = address.address()
    street_name = address.street_name()
    street_number = address.street_number()

    # test whether address is string
    assert isinstance(a, str)

    # test whether address contains street_name
    assert street_name in a

    # test whether address contains street_number
    assert street_number in a

    # test whether address contains street_name
    assert street_number in a

# Generated at 2022-06-13 23:46:10.996054
# Unit test for method address of class Address
def test_Address_address():
    # Initialize a address instance
    address = Address()

    # Generate a random full address
    full_address = address.address()
    assert full_address
    assert isinstance(full_address, str)


# Generated at 2022-06-13 23:47:11.679714
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None
    assert address.address() != ""


# Generated at 2022-06-13 23:47:15.391518
# Unit test for method address of class Address
def test_Address_address():
    dap = Address()
    for _ in range(0, 100, 10):
        result = dap.address()
        assert result is not None
        assert isinstance(result, str)


# Generated at 2022-06-13 23:47:16.777660
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    # print(address.address())
    assert address.address() == address.address()


# Generated at 2022-06-13 23:47:19.976167
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    address = adr.address()
    assert isinstance(address, str)
    assert len(address) is not 0
    assert len(address) is not None
    assert address is not None


# Generated at 2022-06-13 23:47:23.155718
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    Addr = Address()
    assert Addr.address() in Addr.address()
    assert Addr.address() not in Addr.address()


# Generated at 2022-06-13 23:47:25.415394
# Unit test for method address of class Address
def test_Address_address():
    # Check if method address of class Address
    # returns an str instance
    assert isinstance(Address().address(), str)


# Generated at 2022-06-13 23:47:28.844109
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address.

    Run with Python's pytest.
    """
    a = Address()
    assert a.address() == ('{st_num} {st_name} {st_sfx} St.\n'
                           '{zip} {city}, {state} {country}')

# Generated at 2022-06-13 23:47:31.706486
# Unit test for method address of class Address
def test_Address_address():
    obj = Address();
    r = obj.address();
    assert r != '', 'str is empty';


# Generated at 2022-06-13 23:47:33.863279
# Unit test for method address of class Address
def test_Address_address():
    # Initialize address
    address = Address()
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:47:45.586052
# Unit test for method address of class Address
def test_Address_address():
    class UnitTestAddress(Address):
        """Unit test for method address of class Address."""

        class Meta:
            """Class for metadata."""

            pass

    unit_test_address = UnitTestAddress(locale='en')
    # Street number
    assert unit_test_address.street_number() in {
        '1800', '2035', '1860', '1604', '1545',
        '1301', '2450', '1665', '1679', '2124',
    }
    # Full address
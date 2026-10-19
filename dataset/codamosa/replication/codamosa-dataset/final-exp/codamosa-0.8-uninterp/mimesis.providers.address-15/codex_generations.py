

# Generated at 2022-06-13 23:39:27.451171
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()


# Generated at 2022-06-13 23:39:29.485754
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en_US')
    print(address.address())

# Generated at 2022-06-13 23:39:36.713802
# Unit test for method address of class Address
def test_Address_address():
    # Test with type = 'short'
    locales = ['es', 'en', 'nb']

    for l in locales:
        a = Address(l)
        assert l in SHORTENED_ADDRESS_FMT
        assert a.address() in \
            SHORTENED_ADDRESS_FMT[l]

    # Test with type = 'full'
    locales = ['ru', 'zh', 'ja']

    for l in locales:
        a = Address(l)
        assert l not in SHORTENED_ADDRESS_FMT
        assert a.address() in \
            a._data['address_fmt']

# Generated at 2022-06-13 23:39:38.592654
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address()"""
    assert Address.address().count(" ") > 1

# Generated at 2022-06-13 23:39:41.028321
# Unit test for method address of class Address
def test_Address_address():
    ad = Address('en')
    ad.address()
    print(ad.address())
    assert ad.address() != ''

# Generated at 2022-06-13 23:39:47.414118
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    st_num = address.street_number()
    st_name = address.street_name()
    st_sfx = address.street_suffix()
    fmt = address._data['address_fmt']

    assert address.address() == fmt.format(
            st_num=st_num,
            st_name=st_name,
            st_sfx=st_sfx,
    )


# Generated at 2022-06-13 23:39:50.105967
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    adr = Address(locale='en')
    result = adr.address()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:40:00.812616
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    assert(type(Address().address()) == str)
    assert(type(Address().address()) != int)
    assert(len(Address().address())>0)
    assert(len(Address().address())<100)
    assert(Address('tr').address()[:2]!='1 ') # Dont start with a number
    assert(Address().address()[-1]!=' ') # Dont end with a space
    # Only call when it is not overrided
    def test_Aaddress():
        x=Address().address()
        assert(x[:2] != '1 ')  # Dont start with a number
        assert(x[-1] != ' ')  # Dont end with a space
    z=Address

# Generated at 2022-06-13 23:40:04.102869
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    # Check if is a string
    assert isinstance(addr.address(), str)

    # Check if the length is correct
    assert len(addr.address()) > 0

# Generated at 2022-06-13 23:40:06.180143
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    print(address.address())
    print(address.address())
    print(address.address())


# Generated at 2022-06-13 23:40:18.313381
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider

    provider = Address(locale='en')
    assert isinstance(provider, BaseDataProvider)

    assert len(provider.address()) >= 3

    provider = Address(locale='ru')
    assert isinstance(provider, BaseDataProvider)

    assert len(provider.address()) >= 3

    provider = Address(locale='en')
    assert isinstance(provider, BaseDataProvider)
    address = provider.address()
    assert len(address) >= 3
    assert isinstance(address, str)

    provider = Address()
    assert isinstance(provider, BaseDataProvider)

    assert len(provider.address()) >= 3

    provider = Address(locale='en')
    assert isinstance(provider, BaseDataProvider)


# Generated at 2022-06-13 23:40:24.879014
# Unit test for method address of class Address
def test_Address_address():
    # Test that the function works
    a = Address()
    a.address()

    # Test that the function does not work after resetting the provider
    a.reset_provider()
    try:
        a.address()
        assert False
    except AttributeError:
        assert True
    except Exception:
        assert False


# Generated at 2022-06-13 23:40:26.825567
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    result = address.address()
    assert result is not None

if __name__ == "__main__":
    test_Address_address()

# Generated at 2022-06-13 23:40:30.188887
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    
    addr = Address('en')
    print(addr.address())
    print(addr.address())
    print(addr.address())
    print(addr.address())



# Generated at 2022-06-13 23:40:32.140150
# Unit test for method address of class Address
def test_Address_address():
    "Unit test for method address of class Address"
    _Address = Address()
    assert _Address.address()


# Generated at 2022-06-13 23:40:34.374593
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    for _ in range(0, 100):
        result = address.address()
        assert result



# Generated at 2022-06-13 23:40:36.139922
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None
    assert address.address()
    assert address.address()


# Generated at 2022-06-13 23:40:37.771284
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert isinstance(address.address(), str)
    assert isinstance(address.address(True), str)

# Generated at 2022-06-13 23:40:45.438337
# Unit test for method address of class Address
def test_Address_address():
    print('Address: ' + Address().address())
    print('Address: ' + Address('ru').address())
    print('Address: ' + Address('zh').address())
    print('Address: ' + Address('ja').address())
    print('Address: ' + Address('fr').address())
    print('Address: ' + Address('it').address())
    print('Address: ' + Address('es').address())
    print('Address: ' + Address('pt').address())
    print('Address: ' + Address('de').address())


# Generated at 2022-06-13 23:40:53.439513
# Unit test for method address of class Address
def test_Address_address():
	""" Test method address of class Address """

	from mimesis.providers.address import Address
	from mimesis.enums import CountryCode

	address = Address()
	print('-----------------')

	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())
	print(address.address())

# Generated at 2022-06-13 23:41:03.963249
# Unit test for method address of class Address
def test_Address_address():
    print("Test for method address of class Address:")
    test_object = Address("en")
    result1 = test_object.address()
    result2 = test_object.address()
    print("The two result is same? : {}".format(result1 == result2))
    print("The length of result1: {}".format(len(result1)))
    print("The length of result2: {}".format(len(result2)))
    print("The results: {}, {}".format(result1, result2))


# Generated at 2022-06-13 23:41:06.530868
# Unit test for method address of class Address
def test_Address_address():
    # Test for Address.address
    address = Address()
    result = address.address()
    assert result != ''
    assert type(result) is str


# Generated at 2022-06-13 23:41:08.653950
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()


# Generated at 2022-06-13 23:41:10.556815
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert len(a.address()) > 0


# Generated at 2022-06-13 23:41:12.753161
# Unit test for method address of class Address
def test_Address_address():
    """Test function address."""
    address = Address()
    location = address.address()
    assert isinstance(location, str)


# Generated at 2022-06-13 23:41:23.822651
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    assert Address().country_code(CountryCode.A2) == "dz"
    assert Address().postal_code() == "42660"
    assert Address().zip_code() == "42660"
    assert Address().region() == "Mizoram"
    assert Address().state() == "ZA-EC"
    assert Address().prefecture() == "ZA-EC"
    assert Address().federal_subject() == "ZA-EC"
    assert Address().province() == "ZA-EC"
    assert Address().street_number() == "503"
    assert Address().street_name() == "Park Lane"
    assert Address().street_suffix() == "Road"

# Generated at 2022-06-13 23:41:26.390705
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    res = address.address()
    assert isinstance(res, str)
    assert len(res) > 0


# Generated at 2022-06-13 23:41:27.622085
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() != ""

# Generated at 2022-06-13 23:41:30.411592
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    s = a.address()
    assert type(s) == str


# Generated at 2022-06-13 23:41:43.843521
# Unit test for method address of class Address
def test_Address_address():
    # Unit test for method address of class Address
    # should return the address by default
    assert Address().address() == "123 Славянская улица"
    # should return the address in ru
    assert Address(locale='ru').address() == "123 Славянская улица"
    # should return the address in ru
    assert Address(locale='ru').address() == "123 Славянская улица"
    # should return the address in ru
    assert Address(locale='ru').address() == "123 Славянская улица"
    # should return the address in ru

# Generated at 2022-06-13 23:42:01.156664
# Unit test for method address of class Address
def test_Address_address():
    my_address = Address(lang='en')
    print('Street number:', my_address.street_number())
    print('Street name:', my_address.street_name())
    print('Street suffix:', my_address.street_suffix())
    print('address:', my_address.address())
    print('state:', my_address.state())
    print('province:', my_address.province())
    print('postal code:', my_address.postal_code())
    print('country code:', my_address.country_code())
    print('country:', my_address.country())
    print('city:', my_address.city())
    print('latitude:', my_address.latitude())
    print('longitude:', my_address.longitude())

# Generated at 2022-06-13 23:42:02.291047
# Unit test for method address of class Address
def test_Address_address():
    provider = Address(locale='en')
    assert provider.address()


# Generated at 2022-06-13 23:42:03.524748
# Unit test for method address of class Address
def test_Address_address():
    print('Address.address() =', Address().address())

# Generated at 2022-06-13 23:42:13.376750
# Unit test for method address of class Address
def test_Address_address():
    class TestAddress:
        def test_random_address(self):
            a = Address()
            assert a.address() == 'Address'

    class TestJapaneseAddress:
        def test_random_address(self):
            a = Address(locale='ja')
            assert a.address() == 'Address'

    class TestShortenedAddress:
        def test_random_address(self):
            a = Address(locale='en-short')
            assert a.address() == 'Address'

        def test_fr_address(self):
            a = Address(locale='fr')
            assert a.address() == 'Address'

    class TestGermanAddress:
        def test_random_address(self):
            a = Address(locale='de')
            assert a.address() == 'Address'


# Generated at 2022-06-13 23:42:19.075171
# Unit test for method address of class Address
def test_Address_address():
    """ Test case for generate a random full address.
        Please run this file directly if you want to test this case.
    """
    addr = Address()
    country = addr.country()
    zipcode = addr.zip_code()
    city = addr.city()
    street = addr.street_name()
    full_addr = addr.address()
    print('Full Address: {}, {} {} {}'.format(full_addr, city, zipcode, country))


# Generated at 2022-06-13 23:42:21.553303
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address method."""
    address = Address()
    public_address = address.address()
    assert public_address is not None


# Generated at 2022-06-13 23:42:22.985632
# Unit test for method address of class Address
def test_Address_address():
    a = Address()

    assert a.address() != a.address()



# Generated at 2022-06-13 23:42:27.883484
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()
    assert Address('en').address()
    assert Address('ru').address()
    assert Address('zh').address()
    #assert Address().address(locale='ne')
    #assert Address().address(locale='be')
    assert Address('kz').address()
    assert Address('uz').address()


# Generated at 2022-06-13 23:42:29.332263
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print(a.address())


# Generated at 2022-06-13 23:42:38.797702
# Unit test for method address of class Address
def test_Address_address():
    a_es = Address(locale='es')
    a_en = Address(locale='en')
    a_ja = Address(locale='ja')
    a_fr = Address(locale='fr')
    a_de = Address(locale='de')
    a_ru = Address(locale='ru')
    a_pt = Address(locale='pt')
    a_zh = Address(locale='zh')

    assert len(a_es.address()) >= 5
    assert len(a_en.address()) >= 5
    assert len(a_ja.address()) >= 5
    assert len(a_fr.address()) >= 5
    assert len(a_de.address()) >= 5
    assert len(a_ru.address()) >= 5
    assert len(a_pt.address()) >= 5

# Generated at 2022-06-13 23:42:55.837518
# Unit test for method address of class Address
def test_Address_address():
    address_generator = Address()

    address_generator.address()

    assert address_generator.address()


# Generated at 2022-06-13 23:43:02.526385
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    street_number = address.street_number()
    street_name = address.street_name()
    street_suffix = address.street_suffix()
    address_fmt = address._data['address_fmt']
    address_1 = address.address()
    assert isinstance(address_1, str)
    assert address_1 == address_fmt.format(
        st_num=street_number,
        st_name=street_name,
        st_sfx=street_suffix
    )

    address_2 = Address('ja').address()
    assert isinstance(address_2, str)

# Generated at 2022-06-13 23:43:16.959000
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider

    ru = RussiaSpecProvider()
    ru_address = ru.address.address()
    result = ru_address.split('\n')

    assert len(result) == 2
    assert ru.address.is_valid(full_address=ru_address)

    ru_address_split = ru_address.split('\n')

    ru_street_number = ru_address_split[0]
    ru_street_name = ru_address_split[1]
    ru_street_suffix = ru_street_name.split()[-1]

    ru_street_name_ = ru.address.street_name()
    ru_street_suffix_ = ru.address.street_suffix()

    ru_street_number_ = ru.address.street_number()

    ru

# Generated at 2022-06-13 23:43:19.034743
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    result = a.address()
    assert result != None
    assert len(result) > 0
    print(result)


# Generated at 2022-06-13 23:43:20.325869
# Unit test for method address of class Address
def test_Address_address():
    address = Address('zh')
    assert address.address() == '829大街路'


# Generated at 2022-06-13 23:43:22.434419
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    provider = Address('pl')
    address = provider.address()
    assert isinstance(address, str)
    assert len(address) > 0


# Generated at 2022-06-13 23:43:24.126504
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert ' ' in a.address()

# Generated at 2022-06-13 23:43:25.752362
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)


# Generated at 2022-06-13 23:43:35.690602
# Unit test for method address of class Address
def test_Address_address():
    import pytest
    from mimesis.providers.address import Address
    from mimesis.enums import Locale, CountryCode

    class TestAddress:
        def test_street_name(self, address):
            street_name = address.street_name()
            assert isinstance(street_name, str)
            assert street_name == address.street_name()

    class TestAddressJA:
        def test_address_ja(self, address):
            address_ja = address.address()
            assert isinstance(address_ja, str)

    # for each local
    for local in Locale:        
        # create a address obj
        address = Address(local)
        # create a test function
        def test_address(self, address = address, local = local):
            address = address.address()

# Generated at 2022-06-13 23:43:38.893767
# Unit test for method address of class Address
def test_Address_address():
    a = Address("en")
    assert a.address() == a.address("en")
    assert a.address("fr") != a.address("en")


# Generated at 2022-06-13 23:44:00.363571
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode

    obj = Address()
    address = obj.address()

    assert address is not None

    if obj.locale not in SHORTENED_ADDRESS_FMT:
        assert obj.street_suffix() in address

    if obj.locale == 'ja':
        assert obj.city() in address

    assert obj.street_number() in address
    assert obj.street_name() in address


# Generated at 2022-06-13 23:44:02.082820
# Unit test for method address of class Address
def test_Address_address():
    m = Address()
    result = m.address()
    assert isinstance(result, str)



# Generated at 2022-06-13 23:44:03.251381
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()
    print(address.address())

# Generated at 2022-06-13 23:44:05.108454
# Unit test for method address of class Address
def test_Address_address():
    generator = Address('zh')
    result = generator.address()
    assert result is not None


# Generated at 2022-06-13 23:44:08.338411
# Unit test for method address of class Address
def test_Address_address():
    locale = 'zh'
    provider = Address(locale)
    result = provider.address()
    print(result)
    assert result is not None


# Generated at 2022-06-13 23:44:09.300806
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    address = Address(Locale.EN)
    address.address()

# Generated at 2022-06-13 23:44:11.208885
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    # print(a.address())
    pass


# Generated at 2022-06-13 23:44:12.606434
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('en')
    print(addr.address())


# Generated at 2022-06-13 23:44:20.327891
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    print(a.address())
    print(a.state())
    print(a.region())
    print(a.province())
    print(a.federal_subject())
    print(a.prefecture())
    print(a.postal_code())
    print(a.zip_code())
    print(a.country_code())
    print(a.country())
    print(a.city())
    print(a.latitude())
    print(a.longitude())
    print(a.coordinates())
    print(a.continent())
    print(a.calling_code())


if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:44:21.874846
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() != None


# Generated at 2022-06-13 23:44:39.581388
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == Address().address()

# Generated at 2022-06-13 23:44:58.451106
# Unit test for method address of class Address
def test_Address_address():
    test_data = [('0', '0'), ('1', '1'), ('2', '2'), ('3', '4'), ('4', '4')]
    for data in test_data:
        # print(data)
        input_data = data[1]
        output = Address.address(input_data)
        assert output == data[0], f'{output} != {data[0]}'
    print("Method address of class Address has passed all the test")



# Generated at 2022-06-13 23:45:06.180254
# Unit test for method address of class Address
def test_Address_address():
    """Unittest for method address of class Address

    ...

    Methods
    -------
    test_Address_address()
        Test method address of class Address.
    """
    # Prepare data
    _locale = 'en'
    _seed = 0
    _address_fmt = '{st_num} {st_name} {st_sfx}'
    _st_num = '1'
    _st_name = 'Mockingbird'
    _st_sfx = 'Lane'
    _address = '1 Mockingbird Lane'
    # Make instance of Address
    address = Address(_locale, _seed)
    # Test address method of class Address
    assert _address == address.address()

# Generated at 2022-06-13 23:45:15.762858
# Unit test for method address of class Address
def test_Address_address():
    # This test is to validate method address of class Address
    # We will validate this method by comparing several times the result of
    # this method with the result of a random address
    # The reason of this is to verify the output with a real address
    # The probability of this method fails is very small
    
    # Create an object of class Address
    address = Address()
    # The following lines test the method by a random address
    print ("[info] Testing address():")
    print (" ",address.address())    


# Generated at 2022-06-13 23:45:21.518377
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    output = address.address()
    assert isinstance(output, str)
    assert output == "South Avenida Américo Vespucio 4545"
    assert address.address() == "East Avenida España 1546"
    assert address.address() == "Calle de Gral. Pardiñas, 14"
    assert isinstance(address.address(), str)
    assert address.address() == "Carrera 8, CALLE 105, BOGOTÁ D.C."
    assert address.address() == "2637 N. Burlingame Ave."
    assert address.address() == "Rua João Pessoa, 966"
    assert address.address() == "Rua 11 de Junho, 893"
    assert address.address() == "Avenida Rio Verde, 816"


# Generated at 2022-06-13 23:45:25.427084
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() # Tested for locale ru
    assert Address(locale='en').address()
    assert Address(locale='zh').address()
    assert Address(locale='ja').address()


# Generated at 2022-06-13 23:45:26.357813
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address is not None

# Generated at 2022-06-13 23:45:28.586453
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    print(address.address())
    print(address.address())
    print(address.address())



# Generated at 2022-06-13 23:45:34.417667
# Unit test for method address of class Address
def test_Address_address():
  from mimesis.enums import Gender
  from mimesis.builtins import Address
  adress = Address('en')
  assert adress.address() == '{st_num} {st_name} {st_sfx}'.format(st_num=str(adress.street_number()),st_name=adress.street_name(),st_sfx=adress.street_suffix())



# Generated at 2022-06-13 23:45:36.012780
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    for _ in range(10):
        assert addr.address() != "None"


# Generated at 2022-06-13 23:46:05.839325
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address()


# Generated at 2022-06-13 23:46:08.880814
# Unit test for method address of class Address
def test_Address_address():
    provider = Address('zh')
    result = provider.address()
    assert result == '汤丽路152号'


# Generated at 2022-06-13 23:46:12.142699
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    a = Address('zh')
    ans = a.address()
    assert ans != '', 'The address is empty.'
    assert len(
        ''.join(ans.split(' '))
    ) == int(13), 'The street number is not right.'



# Generated at 2022-06-13 23:46:13.067347
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    print(a.address())


# Generated at 2022-06-13 23:46:13.632242
# Unit test for method address of class Address
def test_Address_address():
    Address().address()

# Generated at 2022-06-13 23:46:15.002758
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    adr = Address(Locale.EN)
    adr.address()

# Generated at 2022-06-13 23:46:23.931835
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    from mimesis.enums import CountryCode
    from mimesis_ru import RussiaSpecProvider
    from mimesis_uk import UkraineSpecProvider
    from mimesis_ja import JapanSpecProvider

    assert Address(locale='en-US').address()
    assert Address(locale='en-GB').address()

    # Locales for Russia
    ru = Address(RussiaSpecProvider)
    ru_address = ru.address()
    ru_st_num = ru.street_number()
    ru_st_name = ru.street_name()
    ru_st_sfx = ru.street_suffix()

    assert ru_address

# Generated at 2022-06-13 23:46:26.164468
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() != address.address()

# Generated at 2022-06-13 23:46:28.283991
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    res = provider.address()
    assert len(res) > 0


# Generated at 2022-06-13 23:46:29.899354
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    addr = ad.address()
    assert isinstance(addr, str)


# Generated at 2022-06-13 23:46:50.952160
# Unit test for method address of class Address
def test_Address_address():
    """Test the Address.address method."""
    address = Address()
    result = address.address()
    assert isinstance(result, str)


# Generated at 2022-06-13 23:47:00.488183
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    from mimesis.enums import AddressFormats

    from mimesis.providers.address import Address
    from mimesis.providers.datetime import Datetime

    a = Address('en')
    d = Datetime('zh')
    print(a.country(allow_random=True))
    print(a.address())
    print(a.postal_code())
    print(a.zip_code())
    print(a.country_code(CountryCode.A2))
    print(a.state())
    print(a.region())
    print(a.federal_subject())
    print(a.province())
    print(a.prefecture())
    print(a.continent())
    print(a.calling_code())

# Generated at 2022-06-13 23:47:13.705045
# Unit test for method address of class Address
def test_Address_address():
    """
    Unit test for method address() of class Address().
    """
    a = Address()
    assert a.address() == '478 Greenwood Trail'
    assert a.address() == '847 Monterey Way'
    assert a.address() == '3196 Muir Hill Trail'
    assert a.address() == '63 Village Avenue'
    assert a.address() == '52799 Birchwood Place'
    assert a.address() == '4 Clemons Junction'
    assert a.address() == '0 Coolidge Plaza'
    assert a.address() == '48 Hallows Park'
    assert a.address() == '90767 Saint Paul Street'
    assert a.address() == '2 Eastwood Street'
    assert a.address() == '36 Mendota Road'
    assert a.address() == '5204 Golf Course Center'
   

# Generated at 2022-06-13 23:47:15.956341
# Unit test for method address of class Address
def test_Address_address():
    """Test method address() of class Address."""
    a = Address(locale='en')
    assert a.address() in a._data['address_fmt']


# Generated at 2022-06-13 23:47:18.742981
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    res = address.address()
    assert res is not None
    assert res is not ""
    assert isinstance(res, str)


# Generated at 2022-06-13 23:47:28.169768
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    adr = Address(seed=12345)
    assert (adr.address() == "042 Wills Islands, Apt. 653")
    assert (adr.address('ru') == "28 Пензенская, корп. 11, кв. 41")
    assert (adr.address(seed=12345) == "042 Wills Islands, Apt. 653")
    assert (adr.address(Locale.EN, seed=12345) == "042 Wills Islands, Apt. 653")
    assert (adr.address('ru', seed=12345) == "28 Пензенская, корп. 11, кв. 41")

# Generated at 2022-06-13 23:47:34.012547
# Unit test for method address of class Address
def test_Address_address():
    """Test function address of class Address."""
    pa = Address('zh')
    for _ in range(10):
        pa.address()
    assert pa.address() == '海臨路25号'

    pa = Address('')
    for _ in range(10):
        pa.address()
    assert pa.address() == '100 S. Pecan St.'

# Generated at 2022-06-13 23:47:34.847789
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())

# Generated at 2022-06-13 23:47:37.154443
# Unit test for method address of class Address
def test_Address_address():
    for _ in range(10):
        i = Address('en')
        assert i.address()
        # assert '{address}'.format(address=i.address()) == i.address()


# Generated at 2022-06-13 23:47:38.282802
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    result = provider.address()
    print(result)

# Generated at 2022-06-13 23:48:05.037583
# Unit test for method address of class Address
def test_Address_address():
    """Check Address.address().

    Check if the generated address is in Address Format.

    Example of the format:
        - {st_num} {st_name} {st_sfx}
        - {st_num} {st_name}
        - {city} {address_building_number}-{address_building_number}-{address_building_number}
    """
    add = Address()

# Generated at 2022-06-13 23:48:13.604290
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import address as addr
    result = addr.address()
    assert isinstance(result, str)
    fmt = '{st_num} {st_name} {st_sfx}'
    st_num, st_name, st_sfx = result.split()
    assert int(st_num) >= 1
    assert st_name in addr._data['street']['name']
    assert st_sfx in addr._data['street']['suffix']


# Generated at 2022-06-13 23:48:16.731367
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.address()
    assert address is not None

# Generated at 2022-06-13 23:48:27.039718
# Unit test for method address of class Address
def test_Address_address():
    import json
    import unittest

    from mimesis.exceptions import NonEnumerableError

    class AddressTestCase(unittest.TestCase):

        def setUp(self) -> None:
            """Initialize attributes.
            """
            self.address = Address('en')

        def test_street_name(self):
            """Test method Address.street_name()
            """
            street_name = self.address.street_name()
            self.assertTrue(street_name)
            self.assertTrue(isinstance(street_name, str))

        def test_street_number(self):
            """Test method Address.Street_number()
            """
            street_number = self.address.street_number()
            self.assertTrue(street_number)

# Generated at 2022-06-13 23:48:28.310669
# Unit test for method address of class Address
def test_Address_address():
    provider = mimesis.address.Address()
    addr = provider.address()
    assert isinstance(addr, str)



# Generated at 2022-06-13 23:48:30.304895
# Unit test for method address of class Address
def test_Address_address():
    # Initialize object
    addr = Address(seed=0)
    address = addr.address()
    assert address == 'W8422 Deerfield Crossing', "Address is invalid : " + address


# Generated at 2022-06-13 23:48:34.441673
# Unit test for method address of class Address
def test_Address_address():
    # Test for predefined locale
    instance = Address(locale='en')
    assert type(instance.address()) is str
    assert instance.address() == instance.address()

    # Test for random locale
    instance = Address()
    assert type(instance.address()) is str
    assert instance.address() == instance.address()

    # Test for predefined locale
    instance = Address(locale='ja')
    assert type(instance.address()) is str
    assert instance.address() == instance.address()



# Generated at 2022-06-13 23:48:35.302331
# Unit test for method address of class Address
def test_Address_address():
    assert Address.address()

# Generated at 2022-06-13 23:48:37.932114
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result is not None


# Generated at 2022-06-13 23:48:42.339834
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    for i in range(100):
        #print(address.address())
        assert (address.address() is not None)

if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:49:11.398274
# Unit test for method address of class Address
def test_Address_address():
    uk = Address('en-GB')
    us = Address('en-US')
    ja = Address('ja')

    assert uk.address() == '9 Bute Street'
    assert us.address() == '21 Mark Street'
    assert ja.address() == '東京都千代田区丸の内一丁目7番1号　アパートメント3'


# Generated at 2022-06-13 23:49:16.197003
# Unit test for method address of class Address
def test_Address_address():
    # Where testing will be performed
    test_locale = 'en'
    address_a = Address(test_locale).address()
    address_b = Address(test_locale).address()

    assert address_a != address_b
    print("Test for method address of class Address")
    print("\tAddress A: ", address_a)
    print("\tAddress B: ", address_b)


# Generated at 2022-06-13 23:49:22.870157
# Unit test for method address of class Address
def test_Address_address():
    address1 = Address('en')
    address2 = Address('es')
    address3 = Address('ja')
    address4 = Address('zh')

    assert address1.address()
    assert address2.address()
    assert address3.address()
    assert address4.address()

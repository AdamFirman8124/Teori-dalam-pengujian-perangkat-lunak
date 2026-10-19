

# Generated at 2022-06-13 23:39:49.444109
# Unit test for method address of class Address
def test_Address_address():
    import re
    from mimesis.builtins.de import Address

    a = Address()
    assert re.match(r'^[0-9]+ .+ .$', a.address())

    from mimesis.builtins.ru import Address

    a = Address()
    assert re.match(
        r'^[0-9]+-я ?[а-яА-ЯёЁ ]+$', a.address()
    ) == a.address()
    assert re.match(
        r'^[0-9]+\s([А-Я][а-я]{1,})\s([А-Я][а-я]{1,}),\s\d{3}\s(\w{2})$',
        a.address()
    ) == a.address()


# Generated at 2022-06-13 23:39:52.211344
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:40:01.900742
# Unit test for method address of class Address
def test_Address_address():
    # test_street_number
    a1 = Address(locale='ja').street_number()
    print('test_street_number: ', a1)
    # test_street_name
    a2 = Address(locale='ja').street_name()
    print('test_street_name: ', a2)
    # test_street_suffix
    a3 = Address(locale='ja').street_suffix()
    print('test_street_suffix: ', a3)
    # test_address
    a4 = Address(locale='ja').address()
    print('test_address: ', a4)
    # test_state
    a5 = Address(locale='ja').state()
    print('test_state: ', a5)
    # test_region
    a6 = Address(locale='ja').region

# Generated at 2022-06-13 23:40:06.107509
# Unit test for method address of class Address
def test_Address_address():
    from .address import Address
    from .person import Person

    person = Person('en')
    full_name = person.full_name()

    address = Address('en')
    assert '#' not in address.address()
    assert len(address.address()) != 0


# Generated at 2022-06-13 23:40:08.448844
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.__class__.__name__ == 'Address'
    assert a.address() != a.address()


# Generated at 2022-06-13 23:40:09.456795
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    address.address()
    pass

# Generated at 2022-06-13 23:40:18.430966
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() in ['Rd. 786, Thalia Dale', 'Eads Way, Gia', 'Rue 616, Cambria', '721 Lakewood Gardens', 'Rue 434, Bruno', 'Brouwerstraat 70', 'Kolobovskoye Shosse, 1', 'Улица Лыкова, 2', 'Viale dei Mille, 92', 'Μιχαλακοπούλου  56']

# Generated at 2022-06-13 23:40:19.120064
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() == a.address()

# Generated at 2022-06-13 23:40:22.384550
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    
    a = Address(Locale.EN)
    print(a.address())

# Generated at 2022-06-13 23:40:28.458654
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())



# Generated at 2022-06-13 23:40:36.734580
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider

    assert RussiaSpecProvider.Address().address() == 'г Рязань, ул Тверская, 15, кв 16'

# Generated at 2022-06-13 23:40:38.045707
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address().
    """
    address = Address()
    address.address()


# Generated at 2022-06-13 23:40:42.171497
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    assert address.address() == '99К, Красногвардейская, Заводской'


# Generated at 2022-06-13 23:40:43.589449
# Unit test for method address of class Address
def test_Address_address():
    """Test Address address method."""
    assert Address().address()



# Generated at 2022-06-13 23:40:46.424604
# Unit test for method address of class Address
def test_Address_address():
    import pytest
    a = Address()
    with pytest.raises(AssertionError):
        a.address(locale='')
    assert isinstance(a.address(), str)


# Generated at 2022-06-13 23:40:49.157829
# Unit test for method address of class Address
def test_Address_address():
    # Read the file address.json
    # If the file does not exist,
    # the GeneratorError exception is thrown
    address = Address('en')
    assert address.address() != None


# Generated at 2022-06-13 23:40:50.166394
# Unit test for method address of class Address
def test_Address_address():
    x=Address()
    print(x.address())

# Generated at 2022-06-13 23:40:51.416961
# Unit test for method address of class Address
def test_Address_address():
    test = Address()
    address = test.address()
    assert address


# Generated at 2022-06-13 23:40:54.898883
# Unit test for method address of class Address
def test_Address_address():

    address = Address('ja')
    assert address.address() == '〒123-4567 東京都大田区北町1丁目1-1'

# Generated at 2022-06-13 23:40:57.386983
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    print("Random Address: %s" % a.address())
    # return random address


# Generated at 2022-06-13 23:41:12.908606
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis.enums import CountryCode

    address = Address()
    assert address.address() != ''
    assert address.address(country_code=CountryCode.A2) != ''



# Generated at 2022-06-13 23:41:16.631610
# Unit test for method address of class Address
def test_Address_address():
    # The Address class is the class that the start address of China is the
    # origin, so it starts with the address of Beijing
    Address().address() == '北京市天安门'
    # Because the address is random, the probability of generating other
    # addresses is very low, so the output may not be accurate
    assert False

# Generated at 2022-06-13 23:41:18.669186
# Unit test for method address of class Address
def test_Address_address():
    ad = Address('en')
    assert type(ad.address()) == str
    assert type(ad.address()) != float


# Generated at 2022-06-13 23:41:20.169818
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    assert type(adr.address()) == str


# Generated at 2022-06-13 23:41:22.509778
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ru')
    result = address.address()
    assert result



# Generated at 2022-06-13 23:41:26.269264
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    result = address.address()
    assert isinstance(result, str)



# Generated at 2022-06-13 23:41:31.520523
# Unit test for method address of class Address
def test_Address_address():
    print("########### Unit test for method address of class Address ###############")
    from mimesis.enums import Locale
    address = Address(Locale.ENGLISH)
    print(address.address())


# Generated at 2022-06-13 23:41:32.677082
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)


# Generated at 2022-06-13 23:41:39.133716
# Unit test for method address of class Address
def test_Address_address(): # noqa
    from mimesis.providers.address import Address
    from mimesis.enums import Country
    a = Address(Country.RUSSIA)
    assert isinstance(a.address(), str)
    assert a.address() == '34, Студенческая улица'


# Generated at 2022-06-13 23:41:42.048853
# Unit test for method address of class Address
def test_Address_address():
    address = Address(random_state=0)
    result = address.address()
    assert result == '1395 Mockingbird Lane'
    assert isinstance(result, str)



# Generated at 2022-06-13 23:41:58.216562
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())
    print(address.address())
    print(address.address())
    print(address.address())
    print(address.address())


if __name__ == "__main__":
    test_Address_address()

# Generated at 2022-06-13 23:42:00.597731
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address,
    or the method contains sub methods.

    """
    Address().address()

# Generated at 2022-06-13 23:42:02.366324
# Unit test for method address of class Address
def test_Address_address():
  provider = Address()
  assert type(provider.address()) == str
  assert len(provider.address()) > 0

# Generated at 2022-06-13 23:42:03.263754
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != ''

# Generated at 2022-06-13 23:42:04.491249
# Unit test for method address of class Address
def test_Address_address():
    address = Address()

    assert address.address() != ""


# Generated at 2022-06-13 23:42:05.492703
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != None


# Generated at 2022-06-13 23:42:06.694905
# Unit test for method address of class Address
def test_Address_address():
    assert Address('ru').address() != ''


# Generated at 2022-06-13 23:42:08.101110
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    print(addr.address())



# Generated at 2022-06-13 23:42:11.163973
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    result = address.address()
    assert isinstance(result, str)
    assert len(result) >= 5


# Generated at 2022-06-13 23:42:20.476654
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.person import Person
    p = Person(gender=Gender.FEMALE, _seed=10)
    address = Address(p.locale)
    assert address.address() == "7880 John Hicks Plaza"
    assert address.street_name() == "John Hicks Plaza"
    assert address.street_number(maximum=80) == "78"
    assert address.street_number(maximum=20) == "20"
    assert address.street_number(maximum=10) == "2"
    assert address.street_number(maximum=1) == "1"
    assert address.street_suffix() == "Plaza"
    assert address.state

# Generated at 2022-06-13 23:42:35.723401
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    for _ in range(100):
        assert address.address()


# Generated at 2022-06-13 23:42:41.345293
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider

    address = Address()
    address_ru = Address(locale='ru')

    assert isinstance(address.address(), str)
    assert isinstance(address_ru.address(), str)

    assert address.address() != address.address()
    assert address_ru.address() != address_ru.address()

    assert address.address() != address_ru.address()

    rs = RussiaSpecProvider()

    assert rs.address.full_address() != rs.address.full_address()

    address = Address(locale='ja')
    assert address.address() != address.address()

# Generated at 2022-06-13 23:42:48.569958
# Unit test for method address of class Address
def test_Address_address():
    address_provider = Address()
    st_number = address_provider.street_number()
    st_name = address_provider.street_name()
    country = address_provider.country(allow_random=True)
    full_address = address_provider.address()
    assert( st_number in full_address and st_name in full_address and country in full_address )

# Generated at 2022-06-13 23:42:51.826615
# Unit test for method address of class Address
def test_Address_address():
    result = Address().address()
    print(result)
    assert result
    assert isinstance(result, str)


# Generated at 2022-06-13 23:42:55.843663
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussianSpecProvider
    rus = RussianSpecProvider
    lv = Address(rus)
    for i in range(5):
        assert rus.address() in lv.address()

# Generated at 2022-06-13 23:43:01.666624
# Unit test for method address of class Address
def test_Address_address():
    test_address = Address(provider='uk')
    res1 = test_address.address()
    assert isinstance(res1, str)
    test_address = Address(provider='us')
    res1 = test_address.address()
    assert isinstance(res1, str)
    test_address = Address(provider='us')
    res2 = test_address.address()
    assert res1 != res2
    test_address = Address(provider='de')
    res1 = test_address.address()
    assert isinstance(res1, str)
    test_address = Address(provider='de')
    res2 = test_address.address()
    assert res1 != res2
    test_address = Address(provider='NL')
    res1 = test_address.address()

# Generated at 2022-06-13 23:43:05.599307
# Unit test for method address of class Address
def test_Address_address():
    obj_address = Address()
    address_str = obj_address.address()
    assert type(address_str) == str
    assert len(address_str) > 0


# Generated at 2022-06-13 23:43:09.564699
# Unit test for method address of class Address
def test_Address_address():
	from mimesis.localization import set_localization
	from mimesis.providers.address import Address

	set_localization('ru')
	a = Address()
	a.address()

# Generated at 2022-06-13 23:43:16.187363
# Unit test for method address of class Address
def test_Address_address():
    provider = Address('ru')
    address_from_method = provider.address()
    assert isinstance(address_from_method, str)

    provider = Address('fr')
    address_from_method = provider.address()
    assert isinstance(address_from_method, str)



# Generated at 2022-06-13 23:43:23.362658
# Unit test for method address of class Address
def test_Address_address():
    '''
    函数作用：
        测试 Address 类的 address 函数（方法）
    函数参数：
        无
    :return:
    '''

    from mimesis.enums import Locale
    res1 = Address(Locale.RU).address()
    res2 = Address(Locale.EN).address()
    res3 = Address(Locale.ZH).address()
    # res1 = Address(Locale(language = 'ru')).address()
    # res2 = Address(Locale(language = 'en')).address()
    # res3 = Address(Locale(language = 'zh')).address()

# Generated at 2022-06-13 23:43:39.193201
# Unit test for method address of class Address
def test_Address_address():
    # Given:
    address = Address()

    # When:
    result = address.address()

    # Then:
    assert isinstance(result, str)


# Generated at 2022-06-13 23:43:44.738624
# Unit test for method address of class Address
def test_Address_address():
    # Create provider instance:
    address = Address(locale='ru')

    # Get a random full address:
    address.address()
    # Note:
    # Московское ш., д. 8, корп. 1


# Generated at 2022-06-13 23:43:47.000280
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    address = Address()
    assert address.address() == '42 President St.'

# Generated at 2022-06-13 23:43:49.738213
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert re.match(r'\d{1,3} [a-zA-Z]+ [a-zA-Z]+', addr.address()) is not None

# Generated at 2022-06-13 23:44:01.407750
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())
    print(address.postal_code())
    print(address.country_code())
    print(address.country())
    print(address.city())
    print(address.province())
    print(address.federal_subject())
    print(address.prefecture())
    print(address.region())
    print(address.state())
    print(address.street_name())
    print(address.street_suffix())
    print(address.street_number())
    print(address.calling_code())
    print(address.continent())
    print(address.continent('code'))
    print(address.continent('name'))
    print(address.latitude())
    print(address.latitude(dms=True))

# Generated at 2022-06-13 23:44:02.985650
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    assert isinstance(ad.address(), str)
    assert ad.address()


# Generated at 2022-06-13 23:44:05.191822
# Unit test for method address of class Address
def test_Address_address():
    address = Address()

    result = address.address()
    assert result

    result = address.address()
    assert result

# Generated at 2022-06-13 23:44:08.527706
# Unit test for method address of class Address
def test_Address_address():
    a = Address.create('ja')
    assert a.address() == '千葉県白井市1-2-3'



# Generated at 2022-06-13 23:44:11.893931
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    addr = Address()
    a = addr.address()
    assert len(a) > 0
    assert len(a.split()) > 0

# Generated at 2022-06-13 23:44:13.167086
# Unit test for method address of class Address
def test_Address_address():
    addresses = set()
    ad = Address('en')
    for i in range(100):
        addresses.add(ad.address())
    assert len(addresses) == 100

# Generated at 2022-06-13 23:44:37.690208
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    from mimesis.enums import Country

    addr = Address(Country.CHINA)
    assert addr.address() == '北京市朝阳区阜通东大街6-132号'

    addr = Address(Country.RUSSIA)
    assert addr.address() == 'Apt. 649, PSC 2521, Box 5226, Nizhnevartovsk'

    addr = Address(Country.UNITED_KINGDOM)
    assert addr.address() == 'Flat 14, 94 Fortfield Road'

    addr = Address(Country.UNITED_STATES)
    assert addr.address() == '3336 N. Coventry Ct.'

    addr = Address('zh_CN')

# Generated at 2022-06-13 23:44:39.181107
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == Address().address()

# Generated at 2022-06-13 23:44:40.915542
# Unit test for method address of class Address
def test_Address_address():
    for _ in range(10):
        assert Address('en').address()


# Generated at 2022-06-13 23:44:42.581630
# Unit test for method address of class Address
def test_Address_address():

    # test for address fake data
    print(Address().address())

# Generated at 2022-06-13 23:44:43.293481
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()

# Generated at 2022-06-13 23:44:58.521365
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert type(a.address()) is str

# Generated at 2022-06-13 23:45:02.660127
# Unit test for method address of class Address
def test_Address_address():
    address = Address(locale='en')
    print("Locale: ", address.locale, "\n")

    print("Street name: ", address.street_name())
    print("Street number: ", address.street_number())
    print("Street suffix: ", address.street_suffix())
    print("Address: ", address.address())

# Generated at 2022-06-13 23:45:03.582772
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:45:05.214880
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())


# Generated at 2022-06-13 23:45:09.014566
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    result = a.address()

    assert isinstance(result, str)
    assert result != ''


# Generated at 2022-06-13 23:45:38.626161
# Unit test for method address of class Address
def test_Address_address():
    """Test address method of Address class."""
    address = Address()
    assert address.address() is not None



# Generated at 2022-06-13 23:45:39.875258
# Unit test for method address of class Address
def test_Address_address():
    add = Address()
    assert add.address() != add.address()



# Generated at 2022-06-13 23:45:41.553804
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None

# Generated at 2022-06-13 23:45:42.408145
# Unit test for method address of class Address
def test_Address_address():
    Address().address()


# Generated at 2022-06-13 23:45:44.527011
# Unit test for method address of class Address
def test_Address_address():
    address_test = Address()
    assert address_test.address()

# Generated at 2022-06-13 23:45:57.944652
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Variant
    from mimesis.localization import localization
    from mimesis.providers.address import Address

    pre = {
        Variant.ORIGINAL: {
            'code': 'ru',
            'name': 'Russian',
        },
    }

    localization.set_locale_from_dict(pre)
    data = Address('ru')

    assert data.address() != ''

# Generated at 2022-06-13 23:46:09.981284
# Unit test for method address of class Address
def test_Address_address():
    _ = Address('en').address()
    _ = Address('en').calling_code()
    _ = Address('en').city()
    _ = Address('en').continent()
    _ = Address('en').country()
    _ = Address('en').country_code()
    _ = Address('en').latitude()
    _ = Address('en').longitude()
    _ = Address('en').postal_code()
    _ = Address('en').region()
    _ = Address('en').state()
    _ = Address('en').street_name()
    _ = Address('en').street_number()
    _ = Address('en').street_suffix()
    _ = Address('en').zip_code()
    _ = Address('en').coordinates()
    _ = Address('en').coordinates(dms=True)


# Unit

# Generated at 2022-06-13 23:46:11.982952
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    print(result)


if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:46:13.510675
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() is not None


# Generated at 2022-06-13 23:46:15.492586
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    locale = Locale.en

    s = Address(locale)

    assert len(s.address()) == 34

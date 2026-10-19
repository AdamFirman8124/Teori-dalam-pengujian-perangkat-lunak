

# Generated at 2022-06-13 23:39:36.329093
# Unit test for method address of class Address
def test_Address_address():
    addr = Address(seed=1)
    assert addr.address() == addr.address()
    assert addr.address(seed=1) == addr.address()
    assert addr.address(seed=2) == addr.address(seed=2)
    assert addr.address() != addr.address(seed=2)

    addr = Address(seed=1, locale='ru')
    assert addr.address() == addr.address()
    assert addr.address(seed=1) == addr.address()
    assert addr.address(seed=2) == addr.address(seed=2)
    assert addr.address() != addr.address(seed=2)

    addr = Address(seed=1, locale='ja')
    assert addr.address() == addr.address()
    assert addr.address(seed=1) == addr.address()
    assert addr.address

# Generated at 2022-06-13 23:39:39.826220
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    add1 = address.address()
    assert type(add1) == str
    assert len(add1) > 0


# Generated at 2022-06-13 23:39:46.498551
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address"""

    obj = Address(locale='en')
    assert obj.address() == '223 Newtown Crossing\n'

    obj = Address(locale='ru')
    assert obj.address() == 'улица Карла Маркса\n'

    obj = Address(locale='ja')
    assert obj.address() == '3221-11田中市\n'

# Generated at 2022-06-13 23:39:47.412826
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())

# Generated at 2022-06-13 23:39:50.492252
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    for i in range(0, 5):
        print(address.address())



# Generated at 2022-06-13 23:39:54.723343
# Unit test for method address of class Address
def test_Address_address():
    # m = Address('en')
    # print(m.address())
    # m = Address('es')
    # print(m.address())
    m = Address('ja')
    print(m.address())


# Generated at 2022-06-13 23:39:57.439097
# Unit test for method address of class Address
def test_Address_address():
    address_provide = Address()
    address_provide.set_seed(123)
    print(address_provide.address())


# Generated at 2022-06-13 23:39:59.025791
# Unit test for method address of class Address
def test_Address_address():
    for i in range(10):
        assert Address('en').address()

# Generated at 2022-06-13 23:40:00.650955
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert type(a.address()) is str

# Generated at 2022-06-13 23:40:02.267035
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    print(address.address())

# Generated at 2022-06-13 23:40:14.623742
# Unit test for method address of class Address
def test_Address_address():
    # initialize a new instance of Address
    address = Address()
    # set locale to ru
    address.set_locale('ru')
    # generate address at random
    address.address()
    # set locale to ja
    address.set_locale('ja')
    # generate address at random
    address.address()
    # set locale to en
    address.set_locale('en')
    # generate address at random
    address.address()
    # generate address at random
    address.address()


# Generated at 2022-06-13 23:40:18.411094
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    assert adr.address() is not None
    assert adr.address() != adr.address()


# Generated at 2022-06-13 23:40:23.905516
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.builtins import RussianAddress
    a = Address(locale = Locale.RUSSIAN)
    b = RussianAddress()
    assert a.address() == b.address()


# Generated at 2022-06-13 23:40:30.106593
# Unit test for method address of class Address
def test_Address_address():
    import pytest
    from mimesis.builtins import Address as __address

    a = __address()

    # test with default locale: en-US
    assert a.locale == 'en_US'
    assert ' ' in a.address()

    a.set_locale('ja')
    # test with locale: ja
    assert len(a.address()) == 6

# Generated at 2022-06-13 23:40:31.685978
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert isinstance(result, str)

# Generated at 2022-06-13 23:40:33.329661
# Unit test for method address of class Address
def test_Address_address():
    address = Address().address()
    assert address is not None

# Generated at 2022-06-13 23:40:35.758174
# Unit test for method address of class Address
def test_Address_address():
    """Test for method Address.address()."""
    address_test = Address()
    result = address_test.address()
    assert result is not None
    assert isinstance(result, str)


# Generated at 2022-06-13 23:40:39.615015
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import DataField
    address = Address(DataField.ADDRESSES_EN)
    address_text = address.address()
    assert isinstance(address_text, str)
    assert len(address_text) > 0


# Generated at 2022-06-13 23:40:43.596088
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())

if __name__ == "__main__":
    test_Address_address()

# Generated at 2022-06-13 23:40:45.078484
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider
    russian_provider = russia=RussiaSpecProvider()
    ru_address = russian_provider.address()
    print(ru_address)

# Generated at 2022-06-13 23:40:52.686876
# Unit test for method address of class Address
def test_Address_address():
    #Create a object of class Address
    address = Address()
    #Generate a full address
    result = address.address()

    assert isinstance(result, str)

# Generated at 2022-06-13 23:40:54.583366
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result



# Generated at 2022-06-13 23:41:02.926366
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('ar')
    res = addr.address()
    print(res)
    assert res in [
    '{st_num} {st_name} {st_sfx}'.format(
        st_num=addr.street_number(),
        st_name=addr.street_name(),
        st_sfx=addr.street_suffix(),
    ),
    '{st_num} {st_name}'.format(
        st_num=addr.street_number(),
        st_name=addr.street_name(),
    )
    ]


# Generated at 2022-06-13 23:41:14.346637
# Unit test for method address of class Address
def test_Address_address():

    # Case 1 - Check if result is a string
    result = Address().address()
    assert isinstance(result, str)

    # Case 2 - Check if result of this method is equals to result
    # of street_number() + street_name() for locale cs_CZ
    result1 = Address('cs_CZ').address()
    result2 = Address('cs_CZ').street_number() + ' ' + \
        Address('cs_CZ').street_name()
    assert  result1 == result2

    # Case 3 - Check if result of this method is equals to result
    # of street_number() + street_name() for locale ja
    result1 = Address('ja').address()
    result2 = Address('ja').street_number() + ' ' + \
        Address('ja').street_name()

# Generated at 2022-06-13 23:41:16.194563
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    result = addr.address()
    assert result != None
    assert isinstance(result, str)

# Generated at 2022-06-13 23:41:17.976603
# Unit test for method address of class Address
def test_Address_address():
    """test_address() method test."""
    a = Address()
    assert isinstance(a.address(), str)



# Generated at 2022-06-13 23:41:20.518811
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    address = Address(Locale.ES)
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:41:24.140669
# Unit test for method address of class Address
def test_Address_address():
    s = Address(locale='fr')
    x = s.address()
    print(x)
    assert (x is not None)
    assert (type(x) is str)


# Generated at 2022-06-13 23:41:27.368405
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address()"""
    fake = Address()
    address = fake.address()
    assert(type(address) == str)


# Generated at 2022-06-13 23:41:28.897727
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None


# Generated at 2022-06-13 23:41:43.375570
# Unit test for method address of class Address
def test_Address_address():
    provider = Address('en')
    assert provider.address() != None


# Generated at 2022-06-13 23:41:45.533435
# Unit test for method address of class Address
def test_Address_address():
    address = Address(seed=0)
    assert address.address() == '前原' \
        '町' \
        '9-9'



# Generated at 2022-06-13 23:41:52.544897
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_number = address.street_number()
    street_name = address.street_name()
    street_suffix = address.street_suffix()
    address_ = address.address()
    assert street_name in address_
    assert street_number in address_
    assert street_suffix in address_

# Generated at 2022-06-13 23:41:53.633907
# Unit test for method address of class Address
def test_Address_address():
	assert Address().address() 


# Generated at 2022-06-13 23:41:57.783698
# Unit test for method address of class Address
def test_Address_address():
    address1 = Address('en').address()
    address2 = Address('ru').address()
    address3 = Address('ja').address()

    assert address1 != address2 and address1 != address3
    assert address2 != address3 and address2 != address1
    assert address3 != address1 and address3 != address2

# Generated at 2022-06-13 23:42:08.241662
# Unit test for method address of class Address
def test_Address_address():
    """Unit test method address of class Address."""

# Generated at 2022-06-13 23:42:10.248588
# Unit test for method address of class Address
def test_Address_address():
    print(Address(seed=228).address())


# Generated at 2022-06-13 23:42:11.629378
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() != address.address()

# Generated at 2022-06-13 23:42:14.073579
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address()
    a = Address('en')
    assert a.address()
    a = Address('ru')
    assert a.address()
    a = Address('ja')
    assert a.address()


# Generated at 2022-06-13 23:42:16.180620
# Unit test for method address of class Address
def test_Address_address():
    # instance Address
    address = Address()
    # get address for default locale
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:42:32.734713
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    v = a.address()
    print(v)
    assert len(v) > 0

# Generated at 2022-06-13 23:42:33.907144
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:42:40.606935
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    st_num = provider.street_number()
    st_name = provider.street_name()
    assert (provider.address() == f'{st_num} {st_name}')
    assert (provider.address() != f'{st_num} {st_name}')
    assert (provider.address() != f'{st_num} {st_name}')
    assert (provider.address() != f'{st_num} {st_name}')
    assert (provider.address() != f'{st_num} {st_name}')
    assert (provider.address() != f'{st_num} {st_name}')
    assert (provider.address() != f'{st_num} {st_name}')

# Generated at 2022-06-13 23:42:41.918207
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())


# Generated at 2022-06-13 23:42:43.791001
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address() != a.address()

# Generated at 2022-06-13 23:42:57.417671
# Unit test for method address of class Address
def test_Address_address():
    """Test that the method address working correctly."""
    a1 = Address()
    a2 = Address(locale='zh')
    a3 = Address(locale='ja')

    address1 = '{st_num} {st_name} {st_sfx}'.format_map(vars(a1))
    address2 = '{st_num} {st_name} {st_sfx}'.format_map(vars(a2))
    address3 = '{st_num} {st_name} {st_sfx}'.format_map(vars(a3))

    assert address1.islower()
    assert address2.islower()
    assert len(address3) == 20
    assert address1.split() != address2.split()
    assert address1.split() != address3.split()
   

# Generated at 2022-06-13 23:43:02.375193
# Unit test for method address of class Address
def test_Address_address():
    i = 0
    while i < 1000:
        i += 1
        #I use here a russian locale
        generator = Address(locale='ru')
        address = generator.address()
        assert address
        del generator

# Generated at 2022-06-13 23:43:04.323348
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('zh')
    assert addr.address()


# Generated at 2022-06-13 23:43:05.985328
# Unit test for method address of class Address
def test_Address_address():
    _address = Address()
    assert _address.address()


# Generated at 2022-06-13 23:43:07.847601
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)


# Generated at 2022-06-13 23:43:34.240218
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    from mimesis.providers.address import Address
    ad = Address()
    assert ad.address()
    assert ad.street_suffix()
    assert ad.street_number()
    assert ad.street_name()
    assert ad.state()
    assert ad.postal_code()
    assert ad.zip_code() == ad.zip_code()
    assert ad.country_code(CountryCode.A2)
    assert ad.country_code(CountryCode.A3)
    assert ad.country_code(CountryCode.NUMERIC)
    assert ad.city()
    assert ad.latitude()
    assert ad.longitude()
    assert ad.coordinates()
    assert ad.continent()
    assert ad.calling_code()
    assert ad.province

# Generated at 2022-06-13 23:43:37.082539
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert re.fullmatch(r'\d+\s\w+', addr.address()) == None


# Generated at 2022-06-13 23:43:38.435022
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('zh')
    print(addr.address())

# Generated at 2022-06-13 23:43:39.840240
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address()

# Generated at 2022-06-13 23:43:50.314987
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from random import randint
    provider = Address(locale=Locale.EN)
    index_1 = randint(0, len(provider._data['street']['name'])-1)
    index_2 = randint(0, len(provider._data['street']['suffix'])-1)
    num = randint(1, 1400)
    answer = str(num)+' '+provider._data['street']['name'][index_1]+' '+provider._data['street']['suffix'][index_2]
    assert provider.address() == answer


# Generated at 2022-06-13 23:43:55.231847
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    a1 = adr.address()
    a2 = adr.address()
    assert a1 != a2
    #print('address:', a1)
    print('address:')
    print(a1)


# Generated at 2022-06-13 23:43:56.846004
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:43:59.212393
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='en')
    f = a.address()
    assert f != a.address


# Generated at 2022-06-13 23:44:03.140162
# Unit test for method address of class Address
def test_Address_address():
    instance = Address()
    result = instance.address()

    '''
    assert isinstance(result, str)
    assert re.fullmatch(
        r'^\d*,\s*\w+\s*\w+$',
        result,
    )
    '''
    assert True

# Generated at 2022-06-13 23:44:14.863434
# Unit test for method address of class Address
def test_Address_address():
    en_a = Address(locale="en")
    ja_a = Address(locale="ja")
    es_a = Address(locale="es")
    bn_a = Address(locale="bn")
    pt_BR_a = Address(locale="pt-BR")
    zh_a = Address(locale="zh")
    it_a = Address(locale="it")

    en_add = en_a.address()
    ja_add = ja_a.address()
    es_add = es_a.address()
    bn_add = bn_a.address()
    pt_BR_add = pt_BR_a.address()
    zh_add = zh_a.address()
    it_add = it_a.address()


# Generated at 2022-06-13 23:44:38.038056
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import RussiaSpecProvider
    from pytest import fixture
    from random import Random
    random = Random()
    address = Address(random)

    @fixture(scope='class')
    def ru_address_fmt(address: Address) -> str:
        address.set_locale('ru')
        ru_address_fmt = address._data['address_fmt']
        return ru_address_fmt

    @fixture(scope='class')
    def ru_sp_address_fmt(address: Address) -> str:
        address.set_locale('ru-RU')
        ru_sp_address_fmt = RussiaSpecProvider(random).data['address_fmt']
        return ru_sp_address_fmt


# Generated at 2022-06-13 23:44:41.288339
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()

    assert provider.address() == "50 Galvin Center"
    assert provider.address() == "58 N. Franklin St. Apt. 4"

    return True

# Generated at 2022-06-13 23:44:58.451037
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    ad = Address(Locale.EN)
    for i in range(10):
        print(ad.address())

# Generated at 2022-06-13 23:45:01.222087
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    adr = Address(Locale.EN)
    result = adr.address()
    assert(result)


# Generated at 2022-06-13 23:45:02.811295
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    dt = address.address()
    assert dt
    assert type(dt) == str


# Generated at 2022-06-13 23:45:16.833622
# Unit test for method address of class Address
def test_Address_address():
    mimesis.Address().address()
    # '通り名, 74 - 20-1'
    mimesis.Address(locale='zh').address()
    # '75 巷, No.73 - 25Th'
    mimesis.Address(locale='ja').address()
    # '781st стр, д.66 - 78-15-14'
    mimesis.Address(locale='ru').address()
    # '69 th St, 丁 34-834-83'
    mimesis.Address(locale='zh').address()
    # '535 St, No.82 - 22-1'
    mimesis.Address(locale='ja').address()
    # 'Стр, д.63 - 82-31-21'

# Generated at 2022-06-13 23:45:19.819745
# Unit test for method address of class Address
def test_Address_address():
    print("Get a random full address")
    test_Address = Address()
    test_Address.address()


# Generated at 2022-06-13 23:45:24.361380
# Unit test for method address of class Address
def test_Address_address():
    m = Address(locale='en-US')
    address1 = m.address()
    address2 = m.address()
    assert address1 != address2
    assert isinstance(address1, str)


# Generated at 2022-06-13 23:45:28.713419
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert result
    print('result: ', result)
    assert len(result) > 1
    assert isinstance(result, str)


# Generated at 2022-06-13 23:45:30.858584
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    result = a.address()
    assert type(result) == str


# Generated at 2022-06-13 23:46:03.037680
# Unit test for method address of class Address
def test_Address_address():
    """Testing method address of class Address.

    Method returns a full address
    with street number, name and suffix.
    """
    a = Address('en')
    assert a.address() in ['125 West Street',
                           '88 S. Park St.',
                           ]


# Generated at 2022-06-13 23:46:06.429990
# Unit test for method address of class Address
def test_Address_address():
    import re
    a = Address()
    r = re.compile(r'\d+\s+\w+\s+\w+')
    res = r.match(a.address())
    assert res is not None

# Generated at 2022-06-13 23:46:10.450083
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    full_address = address.address()
    assert full_address == '{} {} {} {}'.format(address.street_number(), address.street_name(), address.street_suffix(), address.postal_code())

# Generated at 2022-06-13 23:46:12.825444
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.builtins import Address
    from mimesis.enums import Locale

    address = Address(locale=Locale.EN)
    address = address.address()
    assert isinstance(address, str)


# Generated at 2022-06-13 23:46:14.260584
# Unit test for method address of class Address
def test_Address_address():
    address = Address('zh')
    for _ in range(0,10):
        print(address.address())

# Generated at 2022-06-13 23:46:17.633284
# Unit test for method address of class Address
def test_Address_address():
    address = Address("es_MX")
    # print(address.address())
    assert address.address().__class__.__name__ == "str"


# Generated at 2022-06-13 23:46:19.198943
# Unit test for method address of class Address
def test_Address_address():
    # Init
    address = Address()
    result = address.address()

    # Check
    assert bool(result)

# Generated at 2022-06-13 23:46:26.714634
# Unit test for method address of class Address
def test_Address_address():
    import random
    from mimesis import Address
    from mimesis.enums import CountryCode
    from mimesis.providers import Provider, Person, Address as Address2
    from string import ascii_letters

    # Test with ja locale
    random.seed(0)
    address = Address('ja')
    assert address.address() == "県　　　　　　　県　　　　　　　県　　　　　　　県　　　　　　　県　　　　　　　県　　　　　　　県　　　　　　　県"



# Generated at 2022-06-13 23:46:31.797642
# Unit test for method address of class Address
def test_Address_address():
    address=Address('en')
    print(address.address())
    print(address.state(False))
    print(address.country())
    print(address.city())
    print(address.latitude())
    print(address.longitude())
    print(address.calling_code())
    print(address.continent())
    print(address.continent(True))

# Generated at 2022-06-13 23:46:34.981084
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:47:21.162790
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    from mimesis.providers.base import BaseDataProvider
    from pytest import raises
    from unittest import TestCase

    assert(Address.Meta.name == 'address')

    addr = Address(Locale.EN)
    assert(isinstance(addr, BaseDataProvider))
    assert(isinstance(addr._data, dict))
    assert(isinstance(addr._seed, int))
    assert(isinstance(addr.generator, BaseDataProvider))

    # Raise exception if locale is not set.
    with raises(AttributeError):
        addr = Address()

    # Raise exception if fmt is not supported.
    with raises(KeyError):
        addr.country_code(CountryCode.A4)


# Generated at 2022-06-13 23:47:23.114593
# Unit test for method address of class Address
def test_Address_address():

    gen_address = Address('tr')
    gen_address.address()
    gen_address.address()

# Generated at 2022-06-13 23:47:24.406316
# Unit test for method address of class Address
def test_Address_address():
    address = Address('ja')
    address.address()


# Generated at 2022-06-13 23:47:30.688766
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode

    addr = Address(locale='en')
    for _ in range(10):
        assert isinstance(addr.address(), str)

    addr = Address(locale='ru')
    for _ in range(10):
        assert isinstance(addr.address(), str)

    addr = Address(locale='zh')
    for _ in range(10):
        assert isinstance(addr.address(), str)

    addr = Address(locale='ja')
    for _ in range(10):
        assert isinstance(addr.address(), str)


# Generated at 2022-06-13 23:47:32.007129
# Unit test for method address of class Address
def test_Address_address():
    tester = Address()
    address = tester.address()
    print(address)



# Generated at 2022-06-13 23:47:33.972131
# Unit test for method address of class Address
def test_Address_address():
	address = Address()
	assert(address.address() == '{st_num} {st_name} {st_sfx}')


# Generated at 2022-06-13 23:47:41.257629
# Unit test for method address of class Address
def test_Address_address():
    address = Address('zh')
    print(address.address())
    print(address.address())
    print()
    #
    address = Address('de')
    print(address.address())
    print(address.address())
    print()
    #
    address = Address('en')
    print(address.address())
    print(address.address())
    print()
    #
    address = Address('es')
    print(address.address())
    print(address.address())
    print()
    #
    address = Address('fr')
    print(address.address())
    print(address.address())
    print()
    #
    address = Address('it')
    print(address.address())
    print(address.address())
    print()
    #
    address = Address('ja')

# Generated at 2022-06-13 23:47:42.662775
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:47:53.664692
# Unit test for method address of class Address
def test_Address_address():
    """Test for method address of class Address."""
    from mimesis.enums import Localization, Locale
    from mimesis.providers import Address

    cls = Address(locale=Localization.SIMPLIFIED_CHINESE)
    assert cls.address() != cls.address()
    assert cls.address() != cls.address()
    assert cls.address() != cls.address()

    cls = Address(locale=Locale('en', 'US'))
    assert cls.address() != cls.address()
    assert cls.address() != cls.address()
    assert cls.address() != cls.address()

    cls = Address(locale=Locale('hu', 'HU'))
    cls.address() != cls.address()

# Generated at 2022-06-13 23:48:08.739980
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.providers.address import Address
    from mimesis.enums import Country
    from mimesis.builtins import RussiaSpecProvider

    ru = RussiaSpecProvider(Country.RUSSIA)

    a = Address()
    assert a.address()
    a = Address(Country.GERMANY)
    assert a.address()
    a = Address(Country.JAPAN)
    assert a.address()
    a = Address(Country.RUSSIA)
    assert a.address()
    a = Address(Country.UKRAINE)
    assert a.address()
    a = Address(Country.US)
    assert a.address()
    a = Address(Country.UK)
    assert a.address()

    # Cover the case for ru locale if ru city is the last item in ru.address_fmt
    ru

# Generated at 2022-06-13 23:48:44.539936
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert (addr.address()) == ("1119 Hillside Drive")

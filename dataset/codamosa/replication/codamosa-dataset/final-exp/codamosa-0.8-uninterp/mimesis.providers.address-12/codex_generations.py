

# Generated at 2022-06-13 23:39:44.199172
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    address = Address(locale=Locale.RU)
    st_num = address.street_number()
    st_name = address.street_name()
    st_sfx = address.street_suffix()

    # Address format for locale RU
    fmt = '{st_num}, {st_name}, {st_sfx}'

    assert address.address() == fmt.format(
        st_num=st_num,
        st_name=st_name,
        st_sfx=st_sfx,
    )


# Generated at 2022-06-13 23:39:45.889303
# Unit test for method address of class Address
def test_Address_address():
    result = Address().address()
    print(result)
    assert isinstance(result, str)



# Generated at 2022-06-13 23:39:47.678714
# Unit test for method address of class Address
def test_Address_address():
    address = Address(seed=1234)
    assert address.address() == '0700 N. Lincoln St.'



# Generated at 2022-06-13 23:39:49.358703
# Unit test for method address of class Address
def test_Address_address():
    c = Address('en','US')
    assert c.address() is not None


# Generated at 2022-06-13 23:39:53.075682
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.address()
    assert address is not None and isinstance(address, str) is True \
           and len(address) > 1


# Generated at 2022-06-13 23:39:53.891064
# Unit test for method address of class Address
def test_Address_address():
    generator = Address('en')
    assert generator.address() != ''


# Generated at 2022-06-13 23:39:54.705138
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None

# Generated at 2022-06-13 23:40:06.138556
# Unit test for method address of class Address
def test_Address_address():
    # Create a Address object us
    us = Address('us')
    # Create a Address object ru
    ru = Address('ru')
    # Create a Address object de
    de = Address('de')
    # Create a Address object ja
    ja = Address('ja')
    # Create a Address object vi
    vi = Address('vi')
    # Create a Address object ko
    ko = Address('ko')

    # [address_fmt: '##STREET', STREET, STREET_SUFFIX]
    address_fmt_1 = us.address()
    assert isinstance(address_fmt_1, str)

    # [address_fmt: '##STREET, CITY STATE ZIPCODE']
    address_fmt_2 = ru.address()
    assert isinstance(address_fmt_2, str)

# Generated at 2022-06-13 23:40:07.646229
# Unit test for method address of class Address
def test_Address_address():
    # General function
    a = Address()
    assert a.address()


# Generated at 2022-06-13 23:40:09.949976
# Unit test for method address of class Address
def test_Address_address():
    k = Address()
    print(k.address())
    print(k.province())
    print(k.city())


# Generated at 2022-06-13 23:40:16.882796
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='en')
    # print(a.address())



# Generated at 2022-06-13 23:40:19.523571
# Unit test for method address of class Address
def test_Address_address():
    a = Address('en')
    assert a.address() != a.address()



# Generated at 2022-06-13 23:40:20.435095
# Unit test for method address of class Address
def test_Address_address():
    pass

# Generated at 2022-06-13 23:40:22.530351
# Unit test for method address of class Address
def test_Address_address():
    print(Address(),"address"+"()")


# Generated at 2022-06-13 23:40:25.572525
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())
    print(address.address())
    print(address.address())



# Generated at 2022-06-13 23:40:33.044468
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()
    assert Address().address()
    assert Address().address()
    assert Address('en').address()
    assert Address('en').address()
    assert Address('en').address()
    assert Address('ru').address()
    assert Address('ru').address()
    assert Address('ru').address()
    assert Address('fr').address()
    assert Address('fr').address()
    assert Address('fr').address()
    assert Address('es').address()
    assert Address('es').address()
    assert Address('es').address()


# Generated at 2022-06-13 23:40:33.619323
# Unit test for method address of class Address
def test_Address_address():
    pass

# Generated at 2022-06-13 23:40:37.207762
# Unit test for method address of class Address
def test_Address_address():
    # This unit test is designed to check the correct output of the method address()
    # of class Address

    # Creation of the object address, which is of class Address
    address = Address()

    # The result is saved in the variable below
    result = address.address()

    # Check that the result is not null
    assert result is not None


# Generated at 2022-06-13 23:40:48.263628
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locales

    en = Address(Locales.EN)
    ru = Address(Locales.RU)
    ja = Address(Locales.JA)

    # ru_locale_address
    ru_locale_address = ru.address()

    # ja_locale_address
    ja_locale_address = ja.address()

    # en_locale_address
    en_locale_address = en.address()

    assert ru_locale_address
    assert ru_locale_address != ja_locale_address
    assert ru_locale_address != en_locale_address
    assert ru_locale_address in ru.__repr__()

    assert ja_locale_address
    assert ja_locale_address in ja.__repr__()

    assert en

# Generated at 2022-06-13 23:40:50.218959
# Unit test for method address of class Address
def test_Address_address():
    r = Address()
    print(r.address())
    print(r.address())
    print(r.address())

# Generated at 2022-06-13 23:40:56.600300
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert len(a.address())>0


# Generated at 2022-06-13 23:40:58.835232
# Unit test for method address of class Address
def test_Address_address():

    ad = Address()
    for i in range(1000):
        ad.address()


# Generated at 2022-06-13 23:41:01.986079
# Unit test for method address of class Address
def test_Address_address():
    obj = Address()
    for _ in range(10):
        result = obj.address()
        assert isinstance(result, str)
        assert 0 < len(result) <= 100


# Generated at 2022-06-13 23:41:03.347751
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() is not None

# Generated at 2022-06-13 23:41:14.601192
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street = address.street_name()
    number = address.street_number()
    suffix = address.street_suffix()
    assert "____" not in test_Address_address.__doc__

# Generated at 2022-06-13 23:41:15.910714
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    print(adr.address())


# Generated at 2022-06-13 23:41:18.031158
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.address()
    assert isinstance(address, str) and len(address) > 0



# Generated at 2022-06-13 23:41:20.004653
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert type(a.address()) == str

# Generated at 2022-06-13 23:41:21.192680
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() == '7867984 H S R E Á'

# Generated at 2022-06-13 23:41:26.126038
# Unit test for method address of class Address
def test_Address_address():
    """
    Unit test for method address of class Address
    """
    addr = Address(Field.LOCALE_RU)
    addr_str = addr.address()
    print(addr_str)
    assert isinstance(addr_str, str)


# Generated at 2022-06-13 23:41:39.527233
# Unit test for method address of class Address
def test_Address_address():
    data_provider = Address()
    assert data_provider.address() != '' # Assert that string is not empty.


# Generated at 2022-06-13 23:41:41.284901
# Unit test for method address of class Address
def test_Address_address():
    """Test Address address."""
    A = Address('ja')
    assert A.address() is not None


# Generated at 2022-06-13 23:41:47.197855
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale

    ad = Address(Locale.EN)
    ans1 = '458 Thomas Junctions'
    ans2 = '서울특별시 은평구 갈현동 69-27'
    ans3 = '越前市横田３６－２２'
    assert ad.address() == ans1
    ad = Address(Locale.KR)
    assert ad.address() == ans2
    ad = Address(Locale.JA)
    assert ad.address() == ans3

# Generated at 2022-06-13 23:41:49.829464
# Unit test for method address of class Address
def test_Address_address():
    # From address fmt '{st_num} {st_name} {st_sfx}'
    # to address fmt '{st_num} {st_name}'
    from mimesis.enums import Locales
    address = Address(Locales.CA)
    assert ' ' not in address.address()


# Generated at 2022-06-13 23:41:51.035302
# Unit test for method address of class Address
def test_Address_address():
    pass


# Generated at 2022-06-13 23:41:53.053365
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    assert len(adr.address()) > 0


# Generated at 2022-06-13 23:41:54.592690
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert len(a.address()) == 13

# Generated at 2022-06-13 23:42:02.834119
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    from mimesis.types import Seed

    a1 = Address(Locale.EN, Seed(12345))
    a2 = Address(Locale.RU, Seed(12345))
    a3 = Address(Locale.JA, Seed(12345))

    assert a1.address() == '8515 Western Street'
    assert a2.address() == 'ул. Безулицевых, д. 107, кв. 31'
    assert a3.address() == 'Kōriyama-shi Osaka-fu 5-1-1-1-1-1'

# Generated at 2022-06-13 23:42:12.829590
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Gender
    from .enums import AddressType

    print("\n=======method address of class Address=======")
    # address_fmt 的 format 会对应到 _data['address_fmt'] 中的变量名
    # print(address_fmt)
    # address_fmt = '{st_num} {st_name}'

    address = Address()
    print("\n---1---")
    for i in range(5):
        print(address.address())

    print("\n---2---")
    address.set_locale('zh')
    print(address.address())

    print("\n---3---")
    # 会从 _data['address_fmt'] 中随机取一

# Generated at 2022-06-13 23:42:14.928964
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


# Generated at 2022-06-13 23:42:41.421681
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import Locale
    from mimesis.localization import Localization
    from mimesis.exceptions import NonExistentLocaleError

    localizations_to_test = ['en', 'ru', 'uk', 'be', 'ja']
    _localization = Localization()

    address = Address(Locale.EN)
    assert address.address() == '{st_num} {st_name}, {st_sfx}'.format(
        st_num=address.street_number(),
        st_name=address.street_name(),
        st_sfx=address.street_suffix()
    )

    address = Address(Locale.RU)

# Generated at 2022-06-13 23:42:44.128187
# Unit test for method address of class Address
def test_Address_address():
    from pprint import pprint
    a = Address()
    pprint (a.address())


# Generated at 2022-06-13 23:42:45.981795
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)

# Generated at 2022-06-13 23:42:47.811388
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address().address()



# Generated at 2022-06-13 23:42:50.588442
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() == "Eingang Stadtweg"


# Generated at 2022-06-13 23:42:51.870855
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address() != Address().address()

# Generated at 2022-06-13 23:42:57.549100
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis.enums import Locale
    from mimesis.localization import _

    locale = Locale('en')
    address = Address(locale)
    result = address.address()
    assert isinstance(result, str)
    assert _('street name') + ' ' in result
    assert _('street nr') in result

# Generated at 2022-06-13 23:43:05.781826
# Unit test for method address of class Address
def test_Address_address():
    add = Address()
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    print(add.address())
    return


# Generated at 2022-06-13 23:43:07.653537
# Unit test for method address of class Address
def test_Address_address():
    adr = Address('en')
    assert isinstance(adr.address(), str)

# Generated at 2022-06-13 23:43:10.132611
# Unit test for method address of class Address
def test_Address_address():
    sd = Address('hy')
    assert type(sd.address()) is str


# Generated at 2022-06-13 23:43:48.849160
# Unit test for method address of class Address
def test_Address_address():
    provider = Address()
    address = provider.address()
    if len(address.split(',')) == 2:
        print(address)
        print('SUCCESS')
    else:
        print('FAIL')


# Generated at 2022-06-13 23:43:50.986321
# Unit test for method address of class Address
def test_Address_address():
    address = Address()

    assert len(address.address()) == 5
    assert len(address.address()) > 0


# Generated at 2022-06-13 23:43:53.522524
# Unit test for method address of class Address
def test_Address_address():
    """ Test for method address of class Address. """
    object = Address()
    object.address()

# Generated at 2022-06-13 23:43:54.554701
# Unit test for method address of class Address
def test_Address_address():
    address = Address('zh')
    result = address.address()
    assert(result in address._data['address'])


# Generated at 2022-06-13 23:43:56.930584
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())


if __name__ == '__main__':
    test_Address_address()

# Generated at 2022-06-13 23:43:58.558282
# Unit test for method address of class Address
def test_Address_address():
    gen = Address(locale='en')
    assert gen.address() != gen.address()

# Generated at 2022-06-13 23:43:59.942619
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())

# Generated at 2022-06-13 23:44:02.183381
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address"""
    address = Address()
    assert address.address() != ''


# Generated at 2022-06-13 23:44:06.724273
# Unit test for method address of class Address
def test_Address_address():
    """Test Address.address()."""
    a = Address(seed=15)
    assert a.address() == '83910 Roob Gateway'
    assert a.address() == '83910 Roob Gateway'
    assert a.address() == '83910 Roob Gateway'
    assert a.address() == '83910 Roob Gateway'



# Generated at 2022-06-13 23:44:08.147044
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    res = addr.address()
    print(res)


# Generated at 2022-06-13 23:45:38.478909
# Unit test for method address of class Address
def test_Address_address():
    t = Address()
    assert t.address()
    assert t.address()
    assert t.address()

# Generated at 2022-06-13 23:45:43.248676
# Unit test for method address of class Address
def test_Address_address():
    """Check if Address.address() is working."""
    for locale in ['ja', 'en', 'ru', 'de', 'es', 'ca', 'cs', 'online']:
        a = Address(locale)
        address = a.address()
        assert address
        assert isinstance(address, str)
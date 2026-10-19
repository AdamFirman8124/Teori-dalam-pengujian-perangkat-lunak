

# Generated at 2022-06-13 23:39:42.418436
# Unit test for method address of class Address
def test_Address_address():
    import pytest

    x = Address()
    assert x.address()

# Generated at 2022-06-13 23:39:44.095695
# Unit test for method address of class Address
def test_Address_address():
    address = Address(seed=5)
    print(address.address())


# Generated at 2022-06-13 23:39:45.542520
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert isinstance(a.address(), str)


# Generated at 2022-06-13 23:39:53.434545
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    from mimesis.exceptions import UnsupportedLanguageError

    from .address import Address

    pa = Address('en')
    # '{st_num} {st_name} {st_sfx}'
    res = pa.address()
    assert len(res) > 1

    pa = Address('ru')
    # '{st_name} {st_num}'
    res = pa.address()
    assert len(res) > 1

    pa = Address('ja')
    # '{city} {street} {number}'
    res = pa.address()
    assert len(res) > 1

    pa = Address('en')
    with pytest.raises(UnsupportedLanguageError):
        pa.address(language_code='asd')



# Generated at 2022-06-13 23:40:01.138505
# Unit test for method address of class Address
def test_Address_address():
    # Testing with default locale.
    a = Address()
    assert isinstance(a.address(), str)
    assert a.address() != ""
    assert a.address() != None
    assert a.address() != ' '
    assert isinstance(a.address(), str)
    assert isinstance(a.address(city='test'), str)
    # Testing with non-existing locale.
    a = Address(locale="xx_XX")
    assert isinstance(a.address(), str)
    assert a.address() != ""
    assert a.address() != None
    assert a.address() != ' '


# Generated at 2022-06-13 23:40:12.534325
# Unit test for method address of class Address
def test_Address_address():
    a = Address()

# Generated at 2022-06-13 23:40:14.422376
# Unit test for method address of class Address
def test_Address_address():
    tmp_address = Address()
    assert isinstance(tmp_address.address(), str)


# Generated at 2022-06-13 23:40:17.564251
# Unit test for method address of class Address
def test_Address_address():
    myAddress = Address()
    for i in range(10):
        print(myAddress.address())


# Generated at 2022-06-13 23:40:22.535614
# Unit test for method address of class Address
def test_Address_address():
    # Case 1.
    adr = Address('en')
    assert adr.address() == '7570 Church Street'

    # Case 2.
    adr = Address()
    assert adr.address() == '2538 Yacht Road'

# Generated at 2022-06-13 23:40:23.478580
# Unit test for method address of class Address
def test_Address_address():
    ad = Address('en')
    res = ad.address()
    assert len(res) < 100


# Generated at 2022-06-13 23:40:42.491875
# Unit test for method address of class Address
def test_Address_address():
    a = Address(locale='zh')
    assert isinstance(a.address(), str)

# Generated at 2022-06-13 23:40:45.478717
# Unit test for method address of class Address
def test_Address_address():
    locale = 'en'
    obj = Address(locale=locale)
    address = obj.address()
    print(address)
    # assert address == '90660 Jeffrey Apt. 278'


# Generated at 2022-06-13 23:40:50.623388
# Unit test for method address of class Address
def test_Address_address():
    _address = Address()
    _addresses = ['8763 W. John Wall Fwy', '33392 S. Dayton Cir',
                  '96550 N. Fort Worth Tpke', '846 W. Nokomis Blvd']
    _current_add = _address.address()
    assert _current_add != None
    assert _current_add in _addresses
    assert str(_current_add) in _addresses


# Generated at 2022-06-13 23:40:54.205509
# Unit test for method address of class Address
def test_Address_address():
    data = Address('ru')
    st_num = data.street_number()
    st_name = data.street_name()
    st_sfx = data.street_suffix()
    my_address = data.address()
    assert isinstance(my_address, str)
    assert st_num in my_address
    assert st_name in my_address
    assert st_sfx in my_address


# Generated at 2022-06-13 23:41:01.284904
# Unit test for method address of class Address
def test_Address_address():
    # test address method
    provider = Address()
    actual = provider.address()
    assert actual == '143, Elizabeth Way' \
        or '55 Chestnut, Elizabeth Way' \
        or '143, Elizabeth Way' \
        or '55 Chestnut, Elizabeth Way' \
        or '143, Elizabeth Way' \
        or '55 Chestnut, Elizabeth Way' \
        or '143, Elizabeth Way' \
        or '55 Chestnut, Elizabeth Way'


test_Address_address()

# Generated at 2022-06-13 23:41:03.833192
# Unit test for method address of class Address
def test_Address_address():
  address = Address()
  assert address.address() in address._data['address_fmt']
  assert isinstance(address.address(), str)


# Generated at 2022-06-13 23:41:09.626081
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    address = Address('en')
    assert address.address() == '35041 Burgess Coves, North Kara, FL 56867-9041'
    assert address.address() == '6442 May Mountains, New Anitashire, WV 30151'
    assert address.address() == '55387 Savannah Villages, East Corine, VA 21034'


# Generated at 2022-06-13 23:41:11.012109
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    print(address.address())

# Generated at 2022-06-13 23:41:13.293400
# Unit test for method address of class Address
def test_Address_address():
    a = Address(seed=127)
    assert a.address() == '1032 جوليه بيل'


# Generated at 2022-06-13 23:41:24.636646
# Unit test for method address of class Address
def test_Address_address():
    s = Address()
    #Main
    assert s.Address() == '${ street_number } ${ street_name } ${ street_suffix }'
    s = Address(locale= 'en')
    assert s.address() == '${ street_number } ${ street_name } ${ street_suffix }'
    s = Address(locale= 'en_GB')
    assert s.address() == '${ street_number } ${ street_name }'
    ##List
    s = Address(locale= 'ja')
    assert s.address() in (
        "${city} ${ random.randints(amount=3, a=1, b=100) }"
        for _ in range(10)
    )
    s = Address(locale= 'zh')

# Generated at 2022-06-13 23:41:44.416076
# Unit test for method address of class Address
def test_Address_address():
    """
    Testing method address of class Address
    """
    full_address = Address('es').address()
    assert full_address != ""
    assert type(full_address) == str


# Generated at 2022-06-13 23:41:46.358218
# Unit test for method address of class Address
def test_Address_address():
    
    address = Address(
        locale='en')

    addr = address.address()
    assert addr is not None
    assert addr != ''
    assert isinstance(addr, str)


# Generated at 2022-06-13 23:41:52.869287
# Unit test for method address of class Address
def test_Address_address():
    # Initialize
    addr = Address('en')

    # Get address
    lu = addr.address()
    print(type(lu))
    print(lu)
    # Output
    # <class 'str'>
    # 1766 Julie Park
    # 1342 Melanie Ridges Suite 695



# Generated at 2022-06-13 23:41:54.830050
# Unit test for method address of class Address
def test_Address_address():
    assert Address('en').address()
    assert Address('fr').address()
    assert Address('ru').address()

# Generated at 2022-06-13 23:41:57.035508
# Unit test for method address of class Address
def test_Address_address():
    from pprint import pprint
    a = Address('zh',random_locale=True).address()
    pprint(a)

# Generated at 2022-06-13 23:41:58.607216
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    assert isinstance(addr.address(), str)


# Generated at 2022-06-13 23:42:01.477020
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    result = address.address()
    assert isinstance(result, str)
    assert result != ''


# Generated at 2022-06-13 23:42:02.745436
# Unit test for method address of class Address
def test_Address_address():
    address = Address("zh")
    print(address.address())


# Generated at 2022-06-13 23:42:06.888623
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import AddressFormats
    addr1 = Address(AddressFormats.FULL)
    # Check for empty street suffix
    addr2 = Address(AddressFormats.SHORT)
    assert addr1.address() != ''
    assert addr1.address() != addr2.address()


# Generated at 2022-06-13 23:42:11.124055
# Unit test for method address of class Address
def test_Address_address():
    print("\n#####################################################\n")
    print("testing Address --> address \n")
    a = Address()
    adr = a.address()
    print(adr)
    assert adr
    print("Address --> address --> OK\n")
    return True


# Generated at 2022-06-13 23:42:38.099712
# Unit test for method address of class Address
def test_Address_address():
    adrs = Address()

# Generated at 2022-06-13 23:42:39.411278
# Unit test for method address of class Address
def test_Address_address():
    ad = Address()
    result = ad.address()
    print(result)

# Generated at 2022-06-13 23:42:48.787173
# Unit test for method address of class Address
def test_Address_address():
    from pprint import pprint
    a = Address(locale='zh')
    print(a._data['address_fmt'])
    pprint(random.choices(a._data['address_fmt'],k=7))
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())
    print(a.address())


if __name__ == "__main__":
    import random
    test_Address_address()

# Generated at 2022-06-13 23:42:51.624702
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    address = Address('en')
    assert address.address()

# Generated at 2022-06-13 23:42:55.991032
# Unit test for method address of class Address
def test_Address_address():
    addr = Address('en')
    assert addr.address() is not None
    assert isinstance(addr.address(), str)
    assert len(addr.address()) > 0
    assert addr.address().count(' ') > 0


# Generated at 2022-06-13 23:42:57.750769
# Unit test for method address of class Address
def test_Address_address():
    """Test method address() of class Address."""
    a = Address()

    assert a.address()


# Generated at 2022-06-13 23:43:00.771718
# Unit test for method address of class Address
def test_Address_address():
    adr = Address(seed=1)
    assert adr.address() == '2471 Stang Road'

# Generated at 2022-06-13 23:43:03.338204
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    adr = Address()
    print(adr.address())

# Generated at 2022-06-13 23:43:06.827323
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    actual = address.address()
    assert ((len(actual) > 4) and (len(address.street_name()) > 2))

# Generated at 2022-06-13 23:43:09.759592
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address."""
    data = Address()
    assert isinstance(data.address(), str)



# Generated at 2022-06-13 23:43:32.396958
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()

    print(addr.address())


# Generated at 2022-06-13 23:43:34.929304
# Unit test for method address of class Address
def test_Address_address():
    addr = Address()
    res = addr.address()
    assert isinstance(res, str)
    assert len(res) > 5
    assert res == addr.address()


# Generated at 2022-06-13 23:43:37.048031
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address()


# Generated at 2022-06-13 23:43:38.892620
# Unit test for method address of class Address
def test_Address_address():
    doc_str = 'Generate a random full address.'
    assert doc_str == Address.address.__doc__

# Generated at 2022-06-13 23:43:41.557821
# Unit test for method address of class Address
def test_Address_address():
    instance = Address(lang="zh_CN")

    for i in range(99):
        print(instance.address())


# Generated at 2022-06-13 23:43:53.991131
# Unit test for method address of class Address
def test_Address_address():
    
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.builtins.en_GB import en_GB
    from mimesis.builtins.es_ES import es_ES
    from mimesis.builtins.fr_FR import fr_FR
    from mimesis.builtins.it_IT import it_IT
    from mimesis.builtins.zh_CN import zh_CN
    
    # Unit test for method address of class Address with gender, german, italian, france, spanish and chinese locales
    address = Address(gender=Gender.MALE, locale='de_DE')
    address.address()
    
    address = Address(gender=Gender.FEMALE, locale='it_IT')
    address.address()
    


# Generated at 2022-06-13 23:44:04.163518
# Unit test for method address of class Address

# Generated at 2022-06-13 23:44:05.148929
# Unit test for method address of class Address
def test_Address_address():
    print(Address().address())


# Generated at 2022-06-13 23:44:07.237209
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    address = a.street_name()
    assert isinstance(address, str)
    assert address is not None


# Generated at 2022-06-13 23:44:11.459511
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis.builtins import Address

    add = Address()
    result = add.address()
    print(result)

# Generated at 2022-06-13 23:44:35.599550
# Unit test for method address of class Address
def test_Address_address():
    obj = Address("zh-CN")
    result = obj.address()
    assert result is not None
    assert len(result) > 0
    assert isinstance(result, str)


# Generated at 2022-06-13 23:44:39.903683
# Unit test for method address of class Address
def test_Address_address():
    """Test function address.

    :return: None
    """
    adr = Address()
    assert ' '.join(adr.address().split()) == adr.address()
    assert len(adr.address().split()) > 3


# Generated at 2022-06-13 23:44:58.521491
# Unit test for method address of class Address
def test_Address_address():
    from pprint import pprint
    import random

    a = Address()
    random.seed(0) # seed, so that test is repeatable
    assert a.address() == '12 Arlington Avenue'
    random.seed(1) # seed, so that test is repeatable
    assert a.address() == '3 Park Avenue'
    random.seed(2) # seed, so that test is repeatable
    assert a.address() == '42 Bradley Junction'
    random.seed(3) # seed, so that test is repeatable
    assert a.address() == '55 Fischer Street'
    random.seed(4) # seed, so that test is repeatable
    assert a.address() == '3355 West Street'

# Generated at 2022-06-13 23:45:01.000154
# Unit test for method address of class Address
def test_Address_address():
    from mimesis import Address
    my_address = Address('en')
    print(my_address.address())


# Generated at 2022-06-13 23:45:04.704577
# Unit test for method address of class Address
def test_Address_address():
    # Run method(s) of class Address
    address_1 = Address().address()
    print(address_1)


# Generated at 2022-06-13 23:45:07.904160
# Unit test for method address of class Address
def test_Address_address():
    """test_Address_address"""
    address = Address()
    assert isinstance(address.address(), str)

# Generated at 2022-06-13 23:45:08.358063
# Unit test for method address of class Address
def test_Address_address():
    assert Address().address()

# Generated at 2022-06-13 23:45:12.650565
# Unit test for method address of class Address
def test_Address_address(): 
    a = Address()
    # print(a.address())
    assert len(a.address())>0


# Generated at 2022-06-13 23:45:15.499595
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    a = address.address()
    print(a)

if __name__ == "__main__":
    test_Address_address()

# Generated at 2022-06-13 23:45:19.283615
# Unit test for method address of class Address
def test_Address_address():
    """Test method address of class Address"""
    a = Address()
    assert a.address() is not None
    assert a.address() is not ''


# Generated at 2022-06-13 23:45:41.388156
# Unit test for method address of class Address
def test_Address_address():
    a = Address()
    assert a.address()


# Generated at 2022-06-13 23:45:42.248747
# Unit test for method address of class Address
def test_Address_address():
    pass



# Generated at 2022-06-13 23:45:48.965596
# Unit test for method address of class Address
def test_Address_address():
    user_test = Address('de')
    street_addr = user_test.address()
    if street_addr.startswith('str.'):
        print(street_addr)
        assert True
    else:
        assert False


# Generated at 2022-06-13 23:46:01.043984
# Unit test for method address of class Address
def test_Address_address():
    address = Address()

    print(address.address())
    print(address.address())
    print(address.address())

# Generated at 2022-06-13 23:46:11.439430
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.localization import EN
    from mimesis.exceptions import NonEnumerableError

    address = Address(locale=EN)

    try:
        assert address.street_number(maximum='str')
    except TypeError as e:
        assert str(e) == 'maximum must be of type int, not str'

    assert isinstance(
        address.street_number(maximum=1400),
        str
    )

    assert isinstance(address.street_name(), str)
    assert isinstance(address.street_suffix(), str)
    assert isinstance(address.address(), str)
    assert isinstance(address.state(), str)
    assert isinstance(address.region(), str)
    assert isinstance(address.province(), str)
    assert isinstance(address.federal_subject(), str)
   

# Generated at 2022-06-13 23:46:16.922734
# Unit test for method address of class Address
def test_Address_address():
    from mimesis.enums import CountryCode
    a = Address(seed=0)
    check_streetname_address = a.address()
    check_streetname_address2 = a.address()
    assert a.postal_code() == '02543'
    assert a.zip_code() == '02543'
    assert a.state() == 'North Carolina'
    assert a.region() == 'North Carolina'
    assert a.region(abbr=True) == 'NC'
    assert a.province() == 'North Carolina'
    assert a.province(abbr=True) == 'NC'
    assert a.federal_subject() == 'North Carolina'
    assert a.federal_subject(abbr=True) == 'NC'
    assert a.prefecture() == 'North Carolina'

# Generated at 2022-06-13 23:46:19.067999
# Unit test for method address of class Address
def test_Address_address():
    address = Address('en')
    result = address.address()
    assert len(result) > 0


# Generated at 2022-06-13 23:46:20.534892
# Unit test for method address of class Address
def test_Address_address():
    obj = [Address('es').address() for i in range(100)]
    assert obj


# Generated at 2022-06-13 23:46:31.820953
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    from mimesis.utils import get_locale_from_string

    address = Address(get_locale_from_string('en'))
    for _ in range(100):
        assert ' ' in address.address()

    address = Address(Locale.PT_BR)
    for _ in range(100):
        assert ' ' in address.address()

    address = Address(get_locale_from_string('ja'))
    for _ in range(100):
        assert ' ' in address.address()

    address = Address(get_locale_from_string('ru'))
    for _ in range(100):
        assert ' ' in address.address()

   

# Generated at 2022-06-13 23:46:33.094780
# Unit test for method address of class Address
def test_Address_address():
    # Initialize object
    address = Address()

    # Generate address
    result = address.address()
    assert result



# Generated at 2022-06-13 23:47:01.197762
# Unit test for method address of class Address
def test_Address_address():
    # test_address
    assert Address().address()


# Generated at 2022-06-13 23:47:14.096123
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for Address.address()."""
    address = Address()

    # English
    current_locale = address.get_locale()

    if current_locale == 'en':
        assert address.address() == '83 W. Church St.'

    # Japanese
    address.set_locale('ja')
    assert address.address() == '神奈川県横浜市西区美園町9-4-1'

    # Russian
    address.set_locale('ru')
    assert address.address() == 'ул. Разъезжая, д. 10, кв. 53'

    # Chinese
    address.set_locale('zh_CN')

# Generated at 2022-06-13 23:47:18.619971
# Unit test for method address of class Address
def test_Address_address():
    # Arrange
    num = 40
    # Act
    adr = Address()
    # Assert
    assert adr.street_number(num).isdigit()
    assert len(adr.street_name()) > 0
    assert len(adr.street_suffix()) > 0
    assert len(adr.address()) > 0


# Generated at 2022-06-13 23:47:20.056773
# Unit test for method address of class Address
def test_Address_address():
    adr = Address()
    a = adr.address()
    print(a)



# Generated at 2022-06-13 23:47:23.690128
# Unit test for method address of class Address
def test_Address_address():
    """Unit test for method address of class Address."""
    import random
    addr = Address('en')
    # print(addr.address())
    print(random.choice(addr._data['address_fmt']))


# Generated at 2022-06-13 23:47:26.229814
# Unit test for method address of class Address
def test_Address_address():
    data = Address('ru')
    address_mock = 'Ленина, 38'
    assert data.address() == address_mock

# Generated at 2022-06-13 23:47:32.754868
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    assert address.address() == '1530 Dasyatis Street'
    assert address.address() == '8815 Isopleura Road'
    assert address.address() == '1775 Sambucus Boulevard'
    assert address.address() == '6760 Siliquaria Street'
    assert address.address() == '6462 Thunnus Avenue'
    assert address.address() == '2917 Phalangium Court'
    assert address.address() == '6442 Hylaeosaurus Circle'
    assert address.address() == '1932 Aceria Road'
    assert address.address() == '761 Mola Street'
    assert address.address() == '1906 Biomphalaria Street'


# Generated at 2022-06-13 23:47:37.007631
# Unit test for method address of class Address
def test_Address_address():
    """
    test for method address
    """
    assert Address("zh").address() in ('陈岗路74号', '黎杨路7号', '瑞景东里9号')
    assert Address("en").address() in ('63827 Cynthia Isle', '8515 Prentice Wells', '448 Chadwick Islands')


# Generated at 2022-06-13 23:47:40.551631
# Unit test for method address of class Address
def test_Address_address():
    a = Address('zh')
    b = Address('en')
    c = Address('en')
    assert a.address() == '北京市海淀区圆明园路'
    assert b.address() == '700 Heather Grove'
    assert c.address() == '1507 Deercreek Crossing'


# Generated at 2022-06-13 23:47:44.409361
# Unit test for method address of class Address
def test_Address_address():
    address = Address()
    street_number = address.street_number()
    street_name = address.street_name()
    street_suffix = address.street_suffix()
    assert address.address() == f'{street_number} {street_name} {street_suffix}'
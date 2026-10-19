

# Generated at 2022-06-13 23:13:02.519029
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Testing
    assert len(PolandSpecProvider().pesel()) == 11

# Generated at 2022-06-13 23:13:10.805066
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """
    Make sure that pesel() method works well.
    """
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11, "Wrong lenght of pesel: 11 is expected"

    pesel2 = PolandSpecProvider().pesel(birth_date=Datetime().datetime(1940, 2018))
    assert pesel == pesel2, "pesel() method has invalid birth_date argument"

    pesel3 = PolandSpecProvider().pesel(gender=Gender.FEMALE)
    assert pesel == pesel3, "pesel() method has invalid gender argument"


# Generated at 2022-06-13 23:13:22.556462
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    plProvider = PolandSpecProvider()
    result = plProvider.pesel()

    assert len(result) == 11
    assert result[0] in '0'
    assert result[1] in '123456789'
    assert result[2] in '0123456789'
    assert result[3] in '0123456789'
    assert result[4] in '0123456789'
    assert result[5] in '0123456789'
    assert result[6] in '0123456789'
    assert result[7] in '0123456789'
    assert result[8] in '0123456789'
    assert result[9] in '0123456789'
    assert result[10] in '0123456789'


# Generated at 2022-06-13 23:13:36.435189
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl_provider = PolandSpecProvider()
    pesel11 = pl_provider.pesel()
    pesel11 = pesel11[:-1]
    peseldate = pesel11[:2]
    peselmonth = pesel11[2:4]
    peselyear = pesel11[4:6]
    peselcontrol = pesel11[-1:]
    peselcontrol = int(peselcontrol)
    peselgender = pesel11[-2:-1]
    peselgender = int(peselgender)
    peselnumber = pesel11[6:]

    peselnumber = int(peselnumber)

    peselmonth = int(peselmonth)
    peselyear = int(peselyear)

    peselmonth = peselmonth-20

# Generated at 2022-06-13 23:13:42.974364
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel of class PolandSpecProvider."""
    p = PolandSpecProvider()
    assert type(p.pesel()) == str
    assert p.pesel('1940') == '40022815575'
    assert p.pesel(gender=Gender.FEMALE) == '89070821558'
    assert p.pesel(gender=Gender.MALE) == '37080631485'
    assert p.pesel(gender=Gender.FEMALE) != p.pesel(gender=Gender.MALE)


# Generated at 2022-06-13 23:13:46.105484
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert provider.pesel() == provider.pesel()

# Generated at 2022-06-13 23:13:55.810027
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test Polish PESEL generation."""
    pl = PolandSpecProvider(seed=1337)
    assert pl.pesel() == '99072806807'
    assert pl.pesel(birth_date='10.05.1962', gender=Gender.MALE) == '62051066606'
    assert pl.pesel(gender=Gender.FEMALE) == '02070368601'
    assert pl.pesel(gender=Gender.FEMALE) == '02070368601'
    assert pl.pesel(gender=Gender.FEMALE) == '02070368601'
    assert pl.pesel() == '99072806807'
    assert pl.pesel(gender=Gender.FEMALE) == '02070368601'

# Generated at 2022-06-13 23:13:59.522747
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Given
    provider = PolandSpecProvider()
    date_object = Datetime().datetime(1940, 2018)
    gender = Gender.MALE

    # When
    result = provider.pesel(birth_date=date_object, gender=gender)

    # Then
    assert type(result) == str
    assert len(result) == 11


test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:14:03.562729
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    assert len(poland.pesel()) == 11

# # Unit test for method pesel of class PolandSpecProvider
# def test_PolandSpecProvider_pesel_birth_date():
#     poland = PolandSpecProvider()
#     assert len(poland.pesel(
#         birth_date="2012-12-31")) == 11

# Generated at 2022-06-13 23:14:05.599860
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(pesel) == 11


# Generated at 2022-06-13 23:16:28.435951
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
  assert(True)

# Generated at 2022-06-13 23:16:35.282445
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider_pl = PolandSpecProvider()
    date = Datetime().datetime(1940, 2018)
    pesel = provider_pl.pesel(birth_date=date, gender=Gender.MALE)
    assert len(pesel) == 11

    pesel = provider_pl.pesel(birth_date=date, gender=Gender.FEMALE)
    assert len(pesel) == 11

    pesel = provider_pl.pesel(birth_date=date, gender=Gender.UNKNOWN)
    assert len(pesel) == 11



# Generated at 2022-06-13 23:16:39.089189
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test for pesel of class PolandSpecProvider."""
    test_poland_provider = PolandSpecProvider()
    test_date = Datetime().datetime(1980, 1990)
    test_gender = Gender.MALE
    result = len(test_poland_provider.pesel(test_date, test_gender))
    assert result == 11

# Generated at 2022-06-13 23:16:56.039274
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.person import Person

    provider = PolandSpecProvider(seed=12345)
    address = Address('en')
    datetime = Datetime()
    person = Person()

    def check_pesel(pesel: str, birth_date: DateTime, gender: Gender):
        # verify length of PESEL
        assert len(pesel) == 11, "PESEL should be 11 digits long"
        # verify checksum digit
        pesel_coeffs = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)

# Generated at 2022-06-13 23:16:58.416066
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider"""
    #assert PolandSpecProvider().pesel() == '01081999364'
    pass

# Generated at 2022-06-13 23:17:06.688506
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """
    Example of test case used to check the behavior of pesel method. 
    """
    p = PolandSpecProvider()
    # check the length of PESEL
    assert len(p.pesel()) == 11
    # check if it starts with '99'
    p.seed(99)
    assert p.pesel()[0:2] == '99'

# Generated at 2022-06-13 23:17:09.517184
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert len(p.pesel()) == 11

# Generated at 2022-06-13 23:17:11.698899
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesel = p.pesel(gender=Gender.MALE)
    assert len(pesel) == 11
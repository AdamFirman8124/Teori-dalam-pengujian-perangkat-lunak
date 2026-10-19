

# Generated at 2022-06-13 23:13:12.428547
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()

    # Test for pesel with a gender as an argument.
    m_pesel = provider.pesel(gender=Gender.MALE)
    f_pesel = provider.pesel(gender=Gender.FEMALE)
    # The last digit of the m_pesel is 1,3,5,7,9.
    # The last digit of the f_pesel is 0,2,4,6,8.
    assert int(m_pesel) % 2 == 1
    assert int(f_pesel) % 2 == 0

    # Test for pesel without a gender as an argument.
    pesel = provider.pesel()
    # The last digit of the pesel is 0,1,2,3,4,5,6,7,8,9.
    assert int(pesel) % 2

# Generated at 2022-06-13 23:13:19.908487
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test whether method :func:`pesel` generates a valid PESEL."""
    import datetime
    from mimesis.enums import Gender
    from mimesis.providers.person.pl.poland_provider import PolandSpecProvider

    p = PolandSpecProvider()
    assert p.pesel(
        birth_date=datetime.date(1990, 9, 1),
        gender=Gender.MALE,
    ) == '90090154681'

# Generated at 2022-06-13 23:13:22.893969
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert len(provider.pesel()) == 11
    assert len(provider.pesel(birth_date='1990-02-28', gender=Gender.MALE)) == 11

# Generated at 2022-06-13 23:13:29.589391
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert provider.pesel().__len__() == 11
    assert provider.pesel(gender=Gender.MALE).endswith(('1', '3', '5', '7', '9'))
    assert provider.pesel(gender=Gender.FEMALE).endswith(('0', '2', '4', '6', '8'))

# Generated at 2022-06-13 23:13:33.020061
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(pesel) == 11
    assert pesel.isdigit() == True

# Generated at 2022-06-13 23:13:38.823372
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=47)
    assert provider.pesel(datetime.datetime(1994, 4, 27), Gender.FEMALE) == '94042790249'
    assert provider.pesel(datetime.datetime(1987, 5, 7), Gender.MALE) == '87050793828'


# Generated at 2022-06-13 23:13:44.889410
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from datetime import datetime
    PolandSpecProvider(seed=1).pesel(birth_date=datetime(1990, 7, 21), gender=Gender.MALE)
    # Returns: '90072100813'


# Generated at 2022-06-13 23:13:47.555705
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()

    assert len(poland_provider.pesel()) == 11

# Generated at 2022-06-13 23:13:56.717941
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel of class PolandSpecProvider."""
    from datetime import datetime
    plsp = PolandSpecProvider(seed=123)
    result = [plsp.pesel(datetime(year=2008, month=1, day=2), gender=Gender.MALE) for i in range(10)]
    assert result == ['01225800816', '01225800816', '01225800816', '01225800816', '01225800816', '01225800816', 
                      '01225800816', '01225800816', '01225800816', '01225800816']
    result = [plsp.pesel(datetime(year=2008, month=1, day=2), gender=Gender.FEMALE) for i in range(10)]

# Generated at 2022-06-13 23:14:01.056201
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis import poland_provider
    seeder = poland_provider.PolandSpecProvider(seed=12345)
    pesel = seeder.pesel()
    assert pesel == '88040300858'

# Generated at 2022-06-13 23:14:25.372604
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert pesel[2] in ['0', '1', '2', '3']
    assert (int(pesel[0]) + int(pesel[4])) % 2 != 0
    assert int(pesel[9]) != 0
    assert int(pesel[10]) != 0

# Generated at 2022-06-13 23:14:27.208197
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider.pesel(birth_date=Datetime().datetime(1940, 2018))


# Generated at 2022-06-13 23:14:29.440375
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    a = PolandSpecProvider()
    assert len(a.pesel()) == 11
    assert isinstance(a.pesel(), str)


# Generated at 2022-06-13 23:14:33.335910
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Test for method pesel of class PolandSpecProvider
    pl = PolandSpecProvider()
    assert pl.pesel(birth_date=Datetime().datetime(1991, 1, 1),
                    gender=Gender.MALE) == '910101000000'
    assert pl.pesel(birth_date=Datetime().datetime(1940, 1, 1),
                    gender=Gender.FEMALE) == '400101000000'

# Generated at 2022-06-13 23:14:43.697878
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel of class PolandSpecProvider"""

    # Create instance of class PolandSpecProvider
    provider = PolandSpecProvider()

    # Generate numbers of PESEL and birth dates and genders
    pesels = [provider.pesel() for i in range(10)]
    birth_dates = []
    genders = []
    for pesel in pesels:
        y = int(pesel[0:2])
        m = int(pesel[2:4])
        d = int(pesel[4:6])
        if m in (21, 41, 61):
            year = int('18{:02d}'.format(y))
        elif m in (22, 42, 62):
            year = int('20{:02d}'.format(y))
        elif m in (23, 43, 63):
            year

# Generated at 2022-06-13 23:14:47.235850
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_list = []
    p = PolandSpecProvider()
    for i in range (0, 100):
        pesel = p.pesel()
        pesel_list.append(pesel)
    # Check that all pesels have 11 digits
    assert all((len(pesel) == 11) for pesel in pesel_list)


# Generated at 2022-06-13 23:14:52.182538
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    psp = PolandSpecProvider()
    pesel = psp.pesel(gender=Gender.FEMALE)
    assert type(pesel) == str
    assert len(pesel) == 11


# Generated at 2022-06-13 23:15:00.321305
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    mimesis.seed(MI_SEED)
    pl_spec_provider = mimesis.PolandSpecProvider()
    pesel = pl_spec_provider.pesel(birth_date=mimesis.Datetime().datetime(2017,2017), gender=mimesis.Gender.MALE)
    print(pesel)
    assert len(str(pesel)) == 11


# Generated at 2022-06-13 23:15:02.715815
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    s = p.pesel()
    assert len(s) == 11


# Generated at 2022-06-13 23:15:08.028787
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """docstring"""
    obj = PolandSpecProvider()
    pesel = obj.pesel()
    assert len(pesel) == 11
    assert pesel.isdigit()
    assert 1950 <= int(pesel[0:2]) <= 99


# Generated at 2022-06-13 23:16:07.209913
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    seed = 5
    pesel = PolandSpecProvider(seed).pesel()
    expected_pesel = '46111764673'
    assert pesel == expected_pesel

# Generated at 2022-06-13 23:16:09.668259
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test pesel method of class PolandSpecProvider"""
    pp = PolandSpecProvider()
    assert isinstance(pp.pesel(), str)
    assert len(pp.pesel()) == 11


# Generated at 2022-06-13 23:16:17.296836
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.providers.person import Person
    person = Person('pl')
    person_birth_date = Datetime().datetime(1940, 2018)
    person_gender = Gender.MALE
    providers_pesel = person.pesel(birth_date=person_birth_date,
                                   gender=person_gender)
    pl_provider = PolandSpecProvider()
    pl_provider_pesel = pl_provider.pesel(birth_date=person_birth_date,
                                          gender=person_gender)
    assert providers_pesel == pl_provider_pesel

# Generated at 2022-06-13 23:16:20.448353
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test to check correctness of pesel method of PolandSpecProvider
    class.
    """
    poland_provider = PolandSpecProvider()
    result = poland_provider.pesel(Datetime().datetime(1999, 6, 15), Gender.MALE)
    assert result == "99061573836"

# Generated at 2022-06-13 23:16:30.103237
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test method for method pesel of class PolandSpecProvider."""
    seed = "1234567890"
    pesel = PolandSpecProvider(seed=seed).pesel()
    assert pesel == "83051369893"

    gender = Gender.FEMALE
    pesel = PolandSpecProvider(seed=seed).pesel(gender=gender)
    assert pesel == "85071500243"

    gender = Gender.MALE
    pesel = PolandSpecProvider(seed=seed).pesel(gender=gender)
    assert pesel == "89061600403"

    date_object = Datetime(seed=seed).datetime(1980,1990)
    pesel = PolandSpecProvider(seed=seed).pesel(birth_date=date_object)
    assert pesel == "81042968693"


# Generated at 2022-06-13 23:16:33.122464
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    year = int(pesel[0:2]) + 2000
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    assert len(pesel) == 11

# Generated at 2022-06-13 23:16:35.532859
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesel_number_1 = p.pesel()
    pesel_number_2 = p.pesel()
    assert(len(pesel_number_1) == 11)
    assert(len(pesel_number_2) == 11)
    assert(pesel_number_1 != pesel_number_2)


# Generated at 2022-06-13 23:16:38.491612
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    seed = '3765979145737706725'
    p = PolandSpecProvider(seed)
    assert p.pesel(birth_date=Datetime().datetime(1980, 1, 2), gender=Gender.FEMALE) == '80010210451'

# Generated at 2022-06-13 23:16:44.328196
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    p = PolandSpecProvider()
    pesel = p.pesel(gender=Gender.FEMALE)
    print(pesel, len(pesel))
    assert len(pesel) == 11

# Generated at 2022-06-13 23:16:49.418855
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    l = PolandSpecProvider() # Initialization of PolandSpecProvider
    g = Gender.FEMALE
    l.pesel(gender=g) # Execution of pesel method with chosen varialbe gender value

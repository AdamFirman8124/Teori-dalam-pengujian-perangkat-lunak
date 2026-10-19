

# Generated at 2022-06-13 23:12:59.652998
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11


# Generated at 2022-06-13 23:13:06.032204
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    from datetime import datetime
    from mimesis.enums import Gender
    assert len(provider.pesel(
        birth_date=datetime(2003, 11, 21),
        gender=Gender.FEMALE)) == 11
    assert len(provider.pesel(
        birth_date=datetime(2003, 11, 21),)) == 11
    assert len(provider.pesel()) == 11


# Generated at 2022-06-13 23:13:14.547057
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider().gender() == Gender.MALE
    PolandSpecProvider().gender() == Gender.FEMALE
    date_object = Datetime().datetime(1940, 2018)
    print('date_object: ', date_object)
    year, month, day = date_object.date().year, date_object.date().month, date_object.date().day
    print('year: ', year)
    print('month: ', month)
    print('day: ', day)
    year_digits = [int(d) for d in str(year)][-2:]
    print('year_digits: ', year_digits)
    month_digits = [int(d) for d in '{:02d}'.format(month)]
    print('month_digits: ', month_digits)
    day_digits

# Generated at 2022-06-13 23:13:17.354277
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    print("PESEL: {}".format(pesel))
    assert len(pesel) == 11

# Generated at 2022-06-13 23:13:24.308895
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel(gender=Gender.FEMALE) == '04060217698'
    assert PolandSpecProvider().pesel(gender=Gender.MALE) == '92082313278'
    assert PolandSpecProvider().pesel(birth_date=Datetime(2019, 7, 1).datetime()) == '19070785766'
    assert PolandSpecProvider().pesel(birth_date=Datetime(1952, 11, 17).datetime(end=23, end_included=True)) == '52111757544'


# Generated at 2022-06-13 23:13:26.800416
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()

    assert len(provider.pesel()) == 11


# Generated at 2022-06-13 23:13:29.174074
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert provider.pesel() == '88122779652'


# Generated at 2022-06-13 23:13:32.041226
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    provider.pesel(birth_date=provider.datetime(1970, 2000), gender=Gender.MALE)

# Generated at 2022-06-13 23:13:36.441408
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel(birth_date=datetime(2000, 5, 5), gender=Gender.FEMALE)
    assert pesel == '00055505522' or pesel == '00055505500'

# Generated at 2022-06-13 23:13:37.843153
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11 and 'Pesel: ' + pesel

# Generated at 2022-06-13 23:13:51.314399
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl_provider = PolandSpecProvider()
    pesel = pl_provider.pesel(birth_date=pl_provider.datetime.datetime(1960, 3, 12), gender=Gender.MALE)
    assert pesel == '60031275071'



# Generated at 2022-06-13 23:13:56.114636
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider(seed=42)
    assert p.pesel() == '90041106323'
    assert p.pesel(birth_date='1865-05-02', gender=Gender.FEMALE) == '86050209891'
    assert p.pesel(birth_date='1865-05-02', gender=Gender.MALE) == '86050209904'

# Generated at 2022-06-13 23:14:00.401894
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    data = provider.pesel()
    assert type(data) == str
    assert len(data) == 11


# Generated at 2022-06-13 23:14:02.952714
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    assert poland.pesel() != poland.pesel()

# Generated at 2022-06-13 23:14:05.268482
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_generator = PolandSpecProvider()
    pesel = pesel_generator.pesel(gender=Gender.MALE)
    assert len(pesel) == 11
    assert pesel_generator.validate_pesel(pesel) == True

# Generated at 2022-06-13 23:14:06.154864
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    p.pesel()

# Generated at 2022-06-13 23:14:11.175111
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesel = p.pesel()
    assert len(pesel) == 11
    assert pesel.startswith('0') == False
    assert pesel.startswith('8') == False
    assert pesel.startswith('9') == False


# Generated at 2022-06-13 23:14:13.719364
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    print("PESEL: ", pesel)


# Generated at 2022-06-13 23:14:19.547559
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # create instance
    a = PolandSpecProvider(seed=1)

    # pesel with birth date
    pesel = a.pesel(birth_date=Datetime().datetime(1950, 1960))
    assert pesel == '52092626147'  # -> this value is generated by seed

    # pesel with gender
    pesel = a.pesel(gender=Gender.MALE)
    assert pesel == '58032106758'  # -> this value is generated by seed


# Generated at 2022-06-13 23:14:22.406781
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    assert len(poland.pesel()) == 11

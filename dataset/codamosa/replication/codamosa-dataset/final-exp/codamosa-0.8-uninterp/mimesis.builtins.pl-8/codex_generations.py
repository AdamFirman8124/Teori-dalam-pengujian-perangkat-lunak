

# Generated at 2022-06-13 23:13:10.231944
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Test for male
    pl = PolandSpecProvider(seed=1)
    assert pl.pesel(gender=Gender.MALE) == '78312248573'
    # Test for female
    assert pl.pesel(gender=Gender.FEMALE) == '78082580200'
    # Test for genderless
    assert pl.pesel() == '75102328525'
    # Test with custom date
    dt = pl.datetime(2000, 2017)
    assert dt.year == 2016
    assert dt.month == 10
    assert dt.day == 6
    assert pl.pesel(birth_date=dt, gender=Gender.MALE) == '16100677848'
    # Test for PESEL out of range (too young)

# Generated at 2022-06-13 23:13:15.141551
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import datetime
    poland_spec_provider = PolandSpecProvider()
    pesel = poland_spec_provider.pesel(birth_date = datetime.datetime(2000, 1, 1), gender = Gender.MALE)
    assert len(pesel) == 11

# Generated at 2022-06-13 23:13:18.329168
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """
    Test if pesel method return correct value
    """
    p = PolandSpecProvider()
    x = p.pesel()
    assert x == '74041411484', "Error on pesel method"

# Generated at 2022-06-13 23:13:27.709714
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    birth_date = Datetime().datetime(1940, 2019)
    year = birth_date.date().year
    month = birth_date.date().month
    day = birth_date.date().day

    pesel_digits = [int(d) for d in str(year)][-2:]

    if 1800 <= year <= 1899:
        month += 80
    elif 2000 <= year <= 2099:
        month += 20
    elif 2100 <= year <= 2199:
        month += 40
    elif 2200 <= year <= 2299:
        month += 60
    pesel_digits += [int(d) for d in '{:02d}'.format(month)]

    pesel_digits += [int(d) for d in '{:02d}'.format(day)]

    series_number = 3#random

# Generated at 2022-06-13 23:13:39.911709
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    # Arrange
    pl_spec_provider = PolandSpecProvider(seed=None)
    year = 2018
    month = 8
    day = 3
    gender = Gender.FEMALE

    # Act
    pesel = pl_spec_provider.pesel(birth_date=DateTime(year=year, month=month, day=day),
                                   gender=gender)

    # Assert
    assert pesel == '18083074144'

    # Arrange
    pl_spec_provider = PolandSpecProvider(seed=None)
    year = 2002
    month = 6
    day = 27
    gender = Gender.MALE

    # Act
    pesel = pl_spec_provider.pesel(birth_date=DateTime(year=year, month=month, day=day),
                                   gender=gender)



# Generated at 2022-06-13 23:13:41.651819
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert provider.pesel().__len__() == 11

# Generated at 2022-06-13 23:13:46.734393
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=0)
    assert provider.pesel(birth_date=Datetime().datetime(2000, 2018)) == '03081204045'

import unittest


# Generated at 2022-06-13 23:13:51.806355
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel(birth_date=Datetime().datetime(), gender=Gender.MALE)
    assert len(pesel) == 11
    nums = [int(d) for d in pesel]
    # Here is checksum test
    assert sum(nums[-2:]) == 11


# Generated at 2022-06-13 23:13:53.801932
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test for method pesel of class PolandSpecProvider"""
    provider = PolandSpecProvider()
    assert provider.pesel() != ""


# Generated at 2022-06-13 23:14:00.777321
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_datetime_object= Datetime().datetime(1940, 2018)
    print(pesel_datetime_object.date().year)
    print(pesel_datetime_object.date().month)
    print(pesel_datetime_object.date().day)
    pesel= PolandSpecProvider().pesel(pesel_datetime_object,Gender.MALE)
    print(pesel)
    # Check if last digit of string is even
    print('The last digit of pesel is even? (1 - True, 0 - False)',pesel[-1] % 2 == 0)
    # Return True if PESEL number is valid, else False
    def valid_pesel(pesel):
        is_valid = True
        numbers = list(map(int, pesel))

# Generated at 2022-06-13 23:14:52.605922
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    k = PolandSpecProvider()
    print(k.pesel())


# Generated at 2022-06-13 23:14:56.175943
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    v = PolandSpecProvider()
    import datetime
    assert len(v.pesel(datetime.datetime.now())) == 11


# Generated at 2022-06-13 23:15:00.165078
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    p = PolandSpecProvider()
    assert p.pesel() == "83101722344"


# Generated at 2022-06-13 23:15:01.785988
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel()

# Generated at 2022-06-13 23:15:09.653231
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()
    assert len(pl.pesel()) == 11
    assert len(pl.pesel(gender = Gender.MALE)) == 11
    assert len(pl.pesel(gender = Gender.FEMALE)) == 11
    assert pl.pesel().isalnum()
    assert pl.pesel(gender = Gender.MALE).isalnum()
    assert pl.pesel(gender = Gender.FEMALE).isalnum()

# Generated at 2022-06-13 23:15:12.451006
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    polish_data = PolandSpecProvider()
    result = polish_data.pesel()
    assert len(result) == 11
    assert result.isnumeric()

# Generated at 2022-06-13 23:15:15.242104
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert pesel.isdigit()



# Generated at 2022-06-13 23:15:17.183446
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider(seed=42).pesel()
    assert pesel == '97111812131'

# Generated at 2022-06-13 23:15:31.918932
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis import PolandSpecProvider
    polandSpecProvider = PolandSpecProvider()
    actual = polandSpecProvider.pesel(None, None)
    assert len(actual) == 11
    assert actual[0].isnumeric()
    assert ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'].count(actual[3]) == 1
    assert actual[3] == '0' or actual[3] == '1' or actual[3] == '2'   
    assert actual[4] == '0' or actual[4] == '1' or actual[4] == '2' or actual[4] == '3'

# Generated at 2022-06-13 23:15:35.708934
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    peselProvider = PolandSpecProvider(seed=20)
    print("\ntest_PolandSpecProvider_pesel:")
    for i in range(4):
        print("pesel:",peselProvider.pesel(birth_date="2006-02-10"))

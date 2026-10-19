

# Generated at 2022-06-13 23:13:01.434771
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() == '97072238283'

# Generated at 2022-06-13 23:13:04.260587
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(pesel) == 11
    assert pesel.isdigit()


# Generated at 2022-06-13 23:13:06.486339
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(pesel) == 11
    assert type(pesel) is str

# Generated at 2022-06-13 23:13:11.926007
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(birth_date = "1998-01-01")
    assert len(pesel) == 11
    assert pesel[2] == "1"
    assert [1, 3, 5, 7, 9].count(int(pesel[9])) == 1
    assert [0, 2, 4, 6, 8].count(int(pesel[9])) == 1


# Generated at 2022-06-13 23:13:13.088070
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() != None


# Generated at 2022-06-13 23:13:14.983431
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider(seed=101).pesel(gender=Gender.MALE)

# Generated at 2022-06-13 23:13:17.716630
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    dt = Datetime().datetime(1960, 2000)
    assert PolandSpecProvider().pesel(dt, Gender.MALE).__len__()==11


# Generated at 2022-06-13 23:13:27.435027
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider_obj = PolandSpecProvider(seed=123456789)
    assert PolandSpecProvider_obj.pesel(gender=Gender.MALE)  == '99030772895'
    assert PolandSpecProvider_obj.pesel(gender=Gender.MALE)  == '89050178962'
    assert PolandSpecProvider_obj.pesel(gender=Gender.MALE)  == '94081818682'
    assert PolandSpecProvider_obj.pesel(gender=Gender.FEMALE)== '89022726562'
    assert PolandSpecProvider_obj.pesel(gender=Gender.FEMALE)== '80061619446'
    assert PolandSpecProvider_obj.pesel(gender=Gender.FEMALE)== '97053123372'

# Generated at 2022-06-13 23:13:34.134888
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""

    from mimesis.builtins.pl import PolandSpecProvider
    provider = PolandSpecProvider('seed')

    birth_date = '1990-01-01'
    gender = Gender.FEMALE
    result = provider.pesel(birth_date, gender)

    assert result == '90101112345'

# Generated at 2022-06-13 23:13:36.372390
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11


# Generated at 2022-06-13 23:13:55.850205
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    poland_provider = PolandSpecProvider()

    pesel = poland_provider.pesel()
    # Check if pesel has 11 digits.
    assert len(pesel) == 11
    # Check pesel for validity.
    pesel_digits = [int(d) for d in pesel]
    pesel_coeffs = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
    sum_v = sum([nc * nd for nc, nd in zip(pesel_coeffs, pesel_digits)])
    checksum_digit = sum_v % 10
    assert checksum_digit == pesel_digits[-1]


# Generated at 2022-06-13 23:14:05.660024
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()   # Create a instance of PolandSpecProvider
    pesel = pl.pesel()          # Generate a pesel of a random person with Random
    if len(pesel) != 11:
        print("Error in function pesel: pesel number not consist of 11 digits. pesel: {}".format(pesel))
    elif not pesel.isdigit():
        print("Error in function pesel: pesel number not consist of only digits. pesel: {}".format(pesel))
    else:
        pesel_digits = [int(d) for d in pesel]
        pesel_coeffs = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)

# Generated at 2022-06-13 23:14:14.219481
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import pytest

    from mimesis.enums import Gender
    from mimesis.exceptions import NonEnumerableError

    provider = PolandSpecProvider('pl')
    for _ in range(1000):
        birth_date = Datetime().datetime(1940, 2050)
        gender = provider.random.choice(Gender)
        pesel = provider.pesel(birth_date, gender)
        birth_year = int(pesel[:2])
        if birth_year < 40:
            birth_year += 2000
        else:
            birth_year += 1900
        birth_month = int(pesel[2:4])
        if birth_month > 80:
            birth_month -= 80
        elif birth_month > 20:
            birth_month -= 20
        elif birth_month > 40:
            birth_month -= 40

# Generated at 2022-06-13 23:14:17.020318
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert isinstance(int(pesel), int)


# Generated at 2022-06-13 23:14:19.394687
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    peselProvider = PolandSpecProvider()

    pesel = peselProvider.pesel(birth_date=Datetime().datetime(1951, 11, 22), gender=Gender.FEMALE)
    assert pesel == "51222111630"

# Generated at 2022-06-13 23:14:27.321742
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    person_data_1 = provider.pesel(birth_date=Datetime().datetime(
        year=1995, month=1, day=1), gender=Gender.MALE)
    person_data_2 = provider.pesel(birth_date=Datetime().datetime(
        year=1995, month=1, day=1), gender=Gender.FEMALE)
    assert person_data_1 != person_data_2

test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:14:29.249554
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    provider.pesel()
    assert len(str(provider.pesel())) == 11

# Generated at 2022-06-13 23:14:32.754370
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=42)
    assert provider.pesel(birth_date=None, gender="male") == '93041470217'
    assert provider.pesel(birth_date=None, gender="female") == '84012942660'
    assert provider.pesel(birth_date=None, gender="unknown") == '78053240895'

# Generated at 2022-06-13 23:14:35.013508
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert provider.pesel()

# Generated at 2022-06-13 23:14:40.558446
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Function for test the method pesel of class PolandSpecProvider."""
    from datetime import datetime
    from mimesis.enums import Gender
    p = PolandSpecProvider()
    pesel = p.pesel(birth_date=datetime(1950, 5, 10), gender=Gender.MALE)
    print(pesel)

if __name__ == '__main__':
    test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:15:11.046111
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test PolandSpecProvider.pesel method."""
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert isinstance(pesel, str)


# Generated at 2022-06-13 23:15:13.823887
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_spec_provider = PolandSpecProvider()
    assert len(poland_spec_provider.pesel()) == 11


# Generated at 2022-06-13 23:15:15.661882
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print(PolandSpecProvider().pesel())



# Generated at 2022-06-13 23:15:18.388834
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel(birth_date='2000-10-10')
    assert pesel == '00141010051'


# Generated at 2022-06-13 23:15:25.615446
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider"""
    pl = PolandSpecProvider()
    pesel = pl.pesel()
    assert len(pesel) == 11
    assert pesel[0] == '0' or pesel[0] == '1' or pesel[0] == '2'
    assert pesel[1] == '0' or pesel[1] == '1' or pesel[1] == '2' or pesel[1] == '3'
    assert pesel[5] == '0' or pesel[5] == '1' or pesel[5] == '2' or pesel[5] == '3'


# Generated at 2022-06-13 23:15:30.337476
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    gender_list = ['male', 'female', 'not specified']
    for gender in gender_list:
        print("Generate pesel for " + gender)
        gender_map = {'male': Gender.MALE,
                      'female': Gender.FEMALE,
                      'not specified': None}
        if gender == 'not specified':
            pesel = PolandSpecProvider().pesel()
        else:
            pesel = PolandSpecProvider().pesel(gender=gender_map[gender])
        print("{} pesel: {}".format(gender, pesel))

# Generated at 2022-06-13 23:15:38.090076
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel() of class PolandSpecProvider."""
    from mimesis.builtins import PolandSpecProvider
    pl = PolandSpecProvider()
    assert len(pl.pesel()) == 11
    assert len(pl.pesel(gender=Gender.MALE)) == 11
    assert len(pl.pesel(gender=Gender.FEMALE)) == 11
    assert len(pl.pesel(birth_date=pl.datetime(1940, 2018))) == 11


# Generated at 2022-06-13 23:15:39.465106
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    #pesel
    poland = PolandSpecProvider()
    print(poland.pesel())

# Generated at 2022-06-13 23:15:46.555585
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    seed = 1234567890
    expected_PESEL = "56100711264"
    pesel_1 = PolandSpecProvider(seed).pesel()
    assert pesel_1 == expected_PESEL
    pesel_2 = PolandSpecProvider(seed).pesel()
    assert pesel_2 == expected_PESEL
    pesel_3 = PolandSpecProvider(seed).pesel(gender=Gender.FEMALE)
    assert pesel_3 != expected_PESEL
    pesel_4 = PolandSpecProvider(seed).pesel(gender=Gender.FEMALE)
    assert pesel_4 != expected_PESEL
    expected_PESEL = "62120511353"
    pesel_5 = PolandSpecProvider(seed).pesel(gender=Gender.MALE)
    assert pesel_5

# Generated at 2022-06-13 23:15:48.123418
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    psp = PolandSpecProvider()
    result = psp.pesel()
    assert len(result) == 11

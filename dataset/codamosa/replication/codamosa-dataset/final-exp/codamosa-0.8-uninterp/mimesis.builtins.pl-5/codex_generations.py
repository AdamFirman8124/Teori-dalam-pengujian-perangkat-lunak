

# Generated at 2022-06-13 23:13:01.155213
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()
    person_data_1 = pl.pesel()
    return person_data_1 == pl.pesel(person_data_1[:6], Gender.MALE)


# Generated at 2022-06-13 23:13:02.196875
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() == "94120700783"


# Generated at 2022-06-13 23:13:05.293381
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    psp = PolandSpecProvider()
    assert isinstance(psp.pesel(), str)
    assert len(psp.pesel()) == 11


# Generated at 2022-06-13 23:13:07.862282
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    assert poland.pesel() != poland.pesel()
    assert len(poland.pesel()) == 11

# Generated at 2022-06-13 23:13:09.680829
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert len(p.pesel()) == 11


# Generated at 2022-06-13 23:13:21.965052
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
	prov = PolandSpecProvider()
	res = prov.pesel();
	print(res)
	print(type(res))
	assert type(res) == str
	# test for gender
	test_male = prov.pesel(gender=Gender.MALE)
	test_female = prov.pesel(gender=Gender.FEMALE)
	assert (test_male[-1] == '1' or test_male[-1] == '3' or test_male[-1] == '5' or test_male[-1] == '7' or test_male[-1] == '9')

# Generated at 2022-06-13 23:13:29.717960
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Check if method pesel of class PolandSpecProvider works properly."""
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    
    assert len(pesel)==11,\
        "pesel length is incorrect"
    
    assert not(any(int(c) < 0 for c in pesel)),\
        "pesel should not contain negative numbers"


# Generated at 2022-06-13 23:13:34.199914
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert isinstance(pesel, str)
    assert len(pesel) == 11

test_PolandSpecProvider_pesel()


# Generated at 2022-06-13 23:13:44.217993
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from datetime import date
    print("Testing for method pesel of class PolandSpecProvider")
    isOK = True
    for gender in Gender:
        date_object = date(1990, 12, 12)
        pesel = PolandSpecProvider().pesel(birth_date=date_object, gender=gender)
        print(pesel)
        my_sum = 0
        for i in range(0, 10):
            my_sum += int(pesel[i]) * (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)[i]
        control_digit = my_sum % 10
        if (control_digit != 0):
            control_digit = 10 - control_digit
        my_digit = int(pesel[10])
        if (my_digit != control_digit):
            isOK = False
           

# Generated at 2022-06-13 23:13:48.008632
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel(birth_date=Datetime().datetime(2010, 12, 12), gender=Gender.FEMALE) == '10121281222'

# Generated at 2022-06-13 23:14:05.868141
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()

    # Check that it is a string of length 11
    assert isinstance(pesel, str)
    assert len(pesel) == 11

    # Check that all the values in the string are integers
    for value in pesel:
        assert isinstance(int(value), int)


# Generated at 2022-06-13 23:14:14.142992
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel of class PolandSpecProvider."""
    import datetime
    # Test pesel method of class PolandSpecProvider
    generator = PolandSpecProvider()
    date_to_test = datetime.datetime(1992, 7, 24)
    pesel = '92072406380'
    assert generator.pesel(date_to_test, Gender.MALE) == pesel
    assert generator.pesel(date_to_test, Gender.FEMALE) != pesel
    assert generator.pesel(date_to_test) != pesel
    assert generator.pesel(date_to_test) != generator.pesel(date_to_test)
    assert generator.pesel() != pesel
    assert generator.pesel(Gender.MALE) != pesel

# Generated at 2022-06-13 23:14:19.021432
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from random import seed
    from re import compile

    seed(42)
    p = PolandSpecProvider()
    pattern = compile('[0-9]{11}')

    assert pattern.match(p.pesel()) is not None
    assert pattern.match(p.pesel(gender=Gender.MALE)) is not None
    assert pattern.match(p.pesel(gender=Gender.FEMALE)) is not None

# Generated at 2022-06-13 23:14:23.089342
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Given
    provider = PolandSpecProvider()
    expected = (11)
    # When
    result = provider.pesel()
    # Then
    assert len(result) == expected


# Generated at 2022-06-13 23:14:31.235253
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider"""
    # Test pass
    provider = PolandSpecProvider()
    for _ in range(10):
        birth_date = Datetime().datetime(1940, 2018)
        pesel = provider.pesel(birth_date)
        print('PESEL:', pesel)
        assert len(pesel) == 11

    # Test fail
    provider = PolandSpecProvider()
    birth_date = Datetime().datetime(1940, 2018)
    pesel = provider.pesel(birth_date, Gender.FEMALE)
    print('PESEL:', pesel)
    assert len(pesel) != 11


# Generated at 2022-06-13 23:14:32.531151
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(pesel) == 11

# Generated at 2022-06-13 23:14:35.823873
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from random import seed
    seed(1)
    generator = PolandSpecProvider()
    print("PESEL: " + generator.pesel())


# Generated at 2022-06-13 23:14:39.320956
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    # Arrange
    provider = PolandSpecProvider()
    # Act
    pesel = provider.pesel()
    # Assert
    assert len(pesel) == 11

# Generated at 2022-06-13 23:14:46.608040
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from datetime import date
    import random

    random.seed("This is a seed")
    pesel_provider = PolandSpecProvider("This is a seed")

    assert pesel_provider.pesel(birth_date=date(1940,8,1), gender=Gender.MALE) == '40080254364'
    assert pesel_provider.pesel(birth_date=date(1940,8,1), gender=Gender.FEMALE) == '40080254370'
    assert pesel_provider.pesel(birth_date=date(1940,8,1)) == '40080254369'


# Generated at 2022-06-13 23:14:52.740145
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() == '97062030593'
    assert PolandSpecProvider().pesel() == '73111591837'
    assert PolandSpecProvider().pesel() == '17042261340'

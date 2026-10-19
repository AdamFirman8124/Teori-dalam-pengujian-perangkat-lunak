

# Generated at 2022-06-13 23:13:04.563338
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """
    Test for PolandSpecProvider.pesel
    """
    assert PolandSpecProvider().pesel() == "97082732138"


# Generated at 2022-06-13 23:13:07.909554
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider.pesel(PolandSpecProvider(), birth_date = '2000-01-01',
        gender = Gender.MALE)
# Tear down
PolandSpecProvider.reset_seed(PolandSpecProvider())

# Generated at 2022-06-13 23:13:12.946465
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    pl_provider = PolandSpecProvider()
    pesel = pl_provider.pesel(gender=Gender.FEMALE)
    assert isinstance(pesel, str)
    assert len(pesel) == 11
    pesel = pl_provider.pesel(gender=Gender.MALE)
    assert isinstance(pesel, str)
    assert len(pesel) == 11

# Generated at 2022-06-13 23:13:16.965090
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(gender=Gender.MALE)
    assert len(pesel) == 11
    assert PolandSpecProvider().pesel(gender=Gender.FEMALE)[10] in (0, 2, 4, 6, 8)

# Generated at 2022-06-13 23:13:20.593923
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print("\nUnit test for method pesel of class PolandSpecProvider")
    provider = PolandSpecProvider()
    print(provider.pesel(gender=Gender.FEMALE))


# Generated at 2022-06-13 23:13:23.942937
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    test_pr = PolandSpecProvider()
    pesel_value = test_pr.pesel(birth_date = Datetime().datetime(1950, 1987),
                                gender = Gender.FEMALE)
    assert len(pesel_value) == 11
    

# Generated at 2022-06-13 23:13:31.195826
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.builtins.poland import PolandSpecProvider
    p = PolandSpecProvider()
    for i in range(0, 100):
        pesel = p.pesel()
        print(pesel)


if __name__ == '__main__':
    p = PolandSpecProvider()
    print(p.regon())
    print(p.nip())
    print(p.pesel())

# Generated at 2022-06-13 23:13:32.680342
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert len(PolandSpecProvider().pesel()) == 11

# Generated at 2022-06-13 23:13:34.526282
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert(len(PolandSpecProvider().pesel()) == 11)


# Generated at 2022-06-13 23:13:37.131480
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider()
    pesel.pesel(birth_date="2020-02-08", gender=Gender.MALE)
    # print(pesel.pesel(birth_date="2020-02-08", gender=Gender.MALE))

# Generated at 2022-06-13 23:14:14.427833
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """
    GIVEN PolandSpecProvider
    WHEN  The function pesel is called
    THEN  Check if the returned value is correct
    """
    prov = PolandSpecProvider()
    value = prov.pesel()
    assert len(value) == 11
    assert value[-1] == str(
        int(value[0]) * 9 +
        int(value[1]) * 7 +
        int(value[2]) * 3 +
        int(value[3]) * 1 +
        int(value[4]) * 9 +
        int(value[5]) * 7 +
        int(value[6]) * 3 +
        int(value[7]) * 1 +
        int(value[8]) * 9 +
        int(value[9]) * 7 )[-1]


# Generated at 2022-06-13 23:14:16.874552
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    x=PolandSpecProvider()
    print(x.pesel())
    assert x.pesel() is not None


# Generated at 2022-06-13 23:14:19.095629
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider(seed=10).pesel(birth_date=datetime.datetime(2015, 10, 22), gender=Gender.MALE) == '15102749004'


# Generated at 2022-06-13 23:14:23.129878
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test that method pesel works correctly."""
    provider = PolandSpecProvider()
    pesel = provider.pesel()

    assert len(pesel) == 11
    assert int(pesel) > 0


# Generated at 2022-06-13 23:14:26.955080
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Run a unit test on the method pesel of class PolandSpecProvider."""
    p = PolandSpecProvider(seed=12345)
    pesel = p.pesel()
    assert pesel == "90141225696"


# Generated at 2022-06-13 23:14:29.184236
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    print("pesel: " + pesel)
    assert len(pesel) == 11


# Generated at 2022-06-13 23:14:35.276680
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandRandomProvider = PolandSpecProvider()
    myPesel = PolandRandomProvider.pesel()
    pesel_list = list(myPesel)
    # PolandRandomProvider.pesel() documentation describes it as gender
    # independent. However, the implementation makes it male gender centered.
    # The following section checks that the gender is independent
    gender_number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gender_digit = pesel_list[-2]
    assert gender_digit in gender_number_list
    # Checksum digit is calculated according to the Polish Ministry of
    # Digitization
    # The following section checks that the checksum digit is correct

# Generated at 2022-06-13 23:14:36.354559
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert len(PolandSpecProvider().pesel()) == 11

# Generated at 2022-06-13 23:14:45.272982
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    expected = ['66122218353',
                '46122217741',
                '16122213309',
                '96122218527',
                '36122218118',
                '26122213387',
                '06122218882',
                '46122214407',
                '46122216572',
                '06122219389',
                '96122216085',
                '86122217115',
                '86122213974',
                '86122214198',
                '86122217059',
                '86122219642',
                '86122218366',
                '86122219632',
                '86122217694',
                '86122216381']

    provider = PolandSpecProvider(seed=1)

# Generated at 2022-06-13 23:14:52.022231
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert pesel.isnumeric() == True
    pesel = PolandSpecProvider().pesel(birth_date='2018-12-12')
    assert pesel.isnumeric() == True
    assert len(pesel) == 11
    pesel = PolandSpecProvider().pesel(birth_date='2018-12-12', gender=Gender.MALE)
    assert pesel.isnumeric() == True
    assert len(pesel) == 11
    pesel = PolandSpecProvider().pesel(birth_date='2018-12-12', gender=Gender.FEMALE)
    assert pesel.isnumeric() == True
    assert len(pesel) == 11


# Generated at 2022-06-13 23:16:27.779418
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import random
    import datetime
    from mimesis.builtins.poland import PolandSpecProvider as pl
    PESEL = pl(random.seed(1))
    assert PESEL.pesel(birth_date=datetime.datetime(1960,1,1), gender="FEMALE") == "60010199108"
    assert PESEL.pesel(birth_date=datetime.datetime(1960,1,1), gender="MALE") == "60010199107"
    assert PESEL.pesel(birth_date=datetime.datetime(1960,1,1), gender=Gender.FEMALE) == "60010199108"
    assert PESEL.pesel(birth_date=datetime.datetime(1960,1,1), gender=Gender.MALE) == "60010199107"


# Generated at 2022-06-13 23:16:30.186627
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    generated_pesel = provider.pesel()
    assert generated_pesel != provider.pesel()

# Generated at 2022-06-13 23:16:38.457590
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Import
    from datetime import datetime

    # Create object for PolandSpecProvider class
    object_PolandSpecProvider = PolandSpecProvider(seed=12345)

    # Provide pesel with gender Male
    result_string = object_PolandSpecProvider.pesel(gender=Gender.MALE)

    # Check if result is correct
    assert result_string == '9812169426'

    # Provide pesel with gender Female
    result_string = object_PolandSpecProvider.pesel(gender=Gender.FEMALE)

    # Check if result is correct
    assert result_string == '9412209807'

    # Provide pesel with initial date
    result_string = object_PolandSpecProvider.pesel(
        birth_date=datetime(1993, 12, 20, 0, 0))

    # Check if result is correct

# Generated at 2022-06-13 23:16:41.769297
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    spec_poland = PolandSpecProvider()
    pesel = spec_poland.pesel()
    assert len(pesel) == 11

# Generated at 2022-06-13 23:16:47.542038
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    test_provider = PolandSpecProvider(seed=42)
    pesel = test_provider.pesel()
    correct_pesel = "59071505489"
    assert pesel == correct_pesel
    assert len(pesel) == 11


# Generated at 2022-06-13 23:16:54.632411
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print(PolandSpecProvider().pesel())
    print(PolandSpecProvider().pesel(gender=Gender.MALE))
    print(PolandSpecProvider().pesel(gender=Gender.FEMALE))

if __name__ == "__main__":
    test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:17:02.949607
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(birth_date='2017-06-15', gender=Gender.MALE)
    assert len(pesel) == 11
    # Assert that first two digits of pesel
    # are the last two digits of 2017
    assert pesel[:2] == '17'
    # Assert that third and fourth digits
    # of pesel are the month of birth
    assert pesel[2:4] == '06'
    # Assert that fifth and sixth digits
    # of pesel are the day of birth
    assert pesel[4:6] == '15'
    # Assert that last digit of pesel is even
    # which means that person is male
    assert int(pesel[-1]) % 2 == 0

# Generated at 2022-06-13 23:17:18.229450
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print("\nUnit tests for method pesel of class PolandSpecProvider")
    print("------------------------------------------------------------------")
    print("\tA random Pesel should be generated")
    print("------------------------------------------------------------------")
    s = PolandSpecProvider()
    pesel = s.pesel()
    assert (type(pesel) == type("")), "It should return a string"
    print("The generated Pesel is: " + str(pesel))
    assert len(pesel) == 11, "The length of the pesel should be 11"
    print("\tPesel generated correctly")
    print("------------------------------------------------------------------")
    print("\tA Pesel with a given date should be generated")
    print("------------------------------------------------------------------")
    date_object = Datetime().datetime(2019, 2019)

# Generated at 2022-06-13 23:17:19.801265
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider(seed=1).pesel()
    assert pesel == '64071355442'

# Generated at 2022-06-13 23:17:24.758692
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider"""
    # Case 1
    print(PolandSpecProvider().pesel())

    # Case 2
    print(PolandSpecProvider().pesel(birth_date=DateTime('2016-01-01'), gender=Gender.MALE))

    # Case 3
    print(PolandSpecProvider().pesel(birth_date=DateTime('2016-01-01'), gender=Gender.FEMALE))


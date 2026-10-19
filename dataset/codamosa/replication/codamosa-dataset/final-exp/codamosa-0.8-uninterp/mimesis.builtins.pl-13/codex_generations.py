

# Generated at 2022-06-13 23:13:09.957835
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Run tests for method pesel of class PolandSpecProvider."""
    # Get object of PolandSpecProvider
    poland_provider = PolandSpecProvider()
    pesel_list = []
    # Run loop 1000 times
    for i in range(1000):
        # Add PESEL to list
        pesel_list.append(poland_provider.pesel(gender=Gender.MALE))
    # Calculate number of elements included in the list
    number_of_pesels = len(pesel_list)
    # Calculate number of unique PESELs included in the list
    number_of_unique_pesels = len(set(pesel_list))
    # Check if both calculated numbers are equal
    assert number_of_pesels == number_of_unique_pesels


# Generated at 2022-06-13 23:13:22.113908
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    from datetime import datetime
    from mimesis.enums import Gender
    from mimesis.providers import PolandSpecProvider
    from mimesis.exceptions import NonEnumerableError
    from mimesis.typing import DateTime

    poland_provider = PolandSpecProvider()
    poland_provider.seed(654654654654654)
    pesel0 = poland_provider.pesel()
    assert pesel0 == '54033126198'

    # test with Datetime object
    datetime_dt = datetime(year=1986, month=3, day=31)
    random_pesel = PolandSpecProvider().pesel(
        birth_date=datetime_dt,
        gender=Gender.MALE,
    )

# Generated at 2022-06-13 23:13:26.003796
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """unittest"""
    obj = PolandSpecProvider()
    result = obj.pesel()
    print(result)
    assert len(result) == 11


# Generated at 2022-06-13 23:13:36.257678
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    tests = {
        '85120610484': True,
        '08051003173': True,
        '45071511607': True,
        '69101208639': True,
        '89121510762': True,
        '11101815323': True,
        '13022117719': True,
        '07060334535': True,
        '95090710263': True,
    }
    for test in tests.keys():
        assert PolandSpecProvider().pesel(test) == test
        assert PolandSpecProvider().pesel(test[:6]) == test


# Generated at 2022-06-13 23:13:38.475819
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    print(pesel)


# Generated at 2022-06-13 23:13:43.044315
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()
    assert poland_provider.pesel() != poland_provider.pesel()
    assert len(poland_provider.pesel()) == 11
    assert poland_provider.pesel(gender=Gender.MALE)[-1] in ['1', '3', '5', '7', '9']
    assert poland_provider.pesel(gender=Gender.FEMALE)[-1] in ['0', '2', '4', '6', '8']


# Generated at 2022-06-13 23:13:54.395434
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel() of PolandSpecProvider class."""
    from mimesis.enums import Gender
    p = PolandSpecProvider()
    pesel = p.pesel(birth_date=p.datetime(1990, 1990), gender=Gender.MALE)
    check = int(pesel[-1])
    pesel = pesel[:-1]
    pesel = [int(d) for d in pesel]
    pesel_coeffs = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
    sum_v = sum([nc * nd for nc, nd in zip(pesel_coeffs, pesel)])
    checksum_digit = sum_v % 10
    assert check == checksum_digit

# Generated at 2022-06-13 23:13:58.122733
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()
    pesel = pl.pesel()
    assert len(pesel) == 11

    pesel = pl.pesel(birth_date=None, gender=Gender.MALE)
    assert len(pesel) == 11

    pesel = pl.pesel(birth_date=None, gender=Gender.FEMALE)
    assert len(pesel) == 11

# Generated at 2022-06-13 23:13:59.728774
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert(PolandSpecProvider().pesel().__len__() == 11)

# Generated at 2022-06-13 23:14:05.771020
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()

    pesel = poland.pesel(birth_date_time=datetime.datetime(1990, 10, 9), gender=Gender.FEMALE)
    assert len(pesel) == 11
    assert pesel[-2] in ['2', '4', '6', '8', '0']

    pesel = poland.pesel(birth_date_time=datetime.datetime(1990, 10, 9), gender=Gender.MALE)
    assert len(pesel) == 11
    assert pesel[-2] in ['1', '3', '5', '7', '9']

# Generated at 2022-06-13 23:14:21.617932
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    _PolandSpecProvider = PolandSpecProvider(seed = 10)
    _pesel = _PolandSpecProvider.pesel(birth_date='1980-10-11',
                                               gender=Gender.MALE)
    assert _pesel == '88101176037'

    _PolandSpecProvider = PolandSpecProvider(seed=10)
    _pesel = _PolandSpecProvider.pesel(birth_date='1980-10-11',
                                       gender=Gender.FEMALE)
    assert _pesel == '88101116034'

    _PolandSpecProvider = PolandSpecProvider(seed=10)
    _pesel = _PolandSpecProvider.pesel(birth_date='1980-10-11')
    assert _pesel == '88101116086'


# Generated at 2022-06-13 23:14:23.088922
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() != None


# Generated at 2022-06-13 23:14:27.501257
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Arrange
    expected_pesel = '82012903595'
    pl_provider = PolandSpecProvider()

    # Act
    pesel = pl_provider.pesel(birth_date=Datetime().datetime(1982, 1, 29))

    # Assert
    assert pesel == expected_pesel

# Generated at 2022-06-13 23:14:34.567438
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel(birth_date=None, gender=Gender.MALE) == '77022600936' or p.pesel(birth_date=None, gender=Gender.MALE) == '87042760786' or p.pesel(birth_date=None, gender=Gender.MALE) == '79103445047'
    assert p.pesel(birth_date=None, gender=Gender.FEMALE) == '45122037667' or p.pesel(birth_date=None, gender=Gender.FEMALE) == '95122310445' or p.pesel(birth_date=None, gender=Gender.FEMALE) == '97123046960'

# Generated at 2022-06-13 23:14:43.310022
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider(seed=1)

    assert p.pesel(gender=Gender.MALE) == '91071255899'
    assert p.pesel(gender=Gender.FEMALE) == '72120817341'
    assert p.pesel(birth_date=PolandSpecProvider(seed=2).datetime(datetime_format='%Y-%m-%d %H:%M:%S', start=1949)) == '49011623511'
    assert p.pesel(birth_date=PolandSpecProvider(seed=3).datetime(datetime_format='%Y-%m-%d %H:%M:%S', start=1979)) == '79052430603'


# Generated at 2022-06-13 23:14:44.183295
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() is not None

# Generated at 2022-06-13 23:14:47.860947
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_provider_instance = PolandSpecProvider()
    pesel_provider_instance2 = PolandSpecProvider()
    assert len((pesel_provider_instance.pesel())) == 11
    assert len((pesel_provider_instance2.pesel())) == 11
    assert pesel_provider_instance.pesel() != pesel_provider_instance2.pesel()

# Generated at 2022-06-13 23:14:52.178341
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    pesel = (poland.pesel(gender=Gender.MALE))
    first_digit_gender_male = int(pesel[-1]) % 2
    assert first_digit_gender_male == 1
    pesel = (poland.pesel(gender=Gender.FEMALE))
    first_digit_gender_female = int(pesel[-1]) % 2
    assert first_digit_gender_female == 0


# Generated at 2022-06-13 23:14:55.924093
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    obj = PolandSpecProvider()
    pesel_1 = obj.pesel(birth_date=datetime.datetime(1993, 5, 29), gender=Gender.MALE)
    pesel_2 = obj.pesel(birth_date=datetime.datetime(1993, 5, 29), gender=Gender.FEMALE)
    assert len(pesel_1) == 11
    assert len(pesel_2) == 11


# Generated at 2022-06-13 23:14:59.371683
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    for _ in range(10):
        assert len(provider.pesel()) == 11



# Generated at 2022-06-13 23:15:47.953600
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()
    pl.pesel(birth_date=pl.datetime(2000, 2001), gender=Gender.MALE)

# Generated at 2022-06-13 23:15:49.018881
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    print(p.pesel()) # ok



# Generated at 2022-06-13 23:15:51.698788
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import datetime
    from mimesis.enums import Gender

    pesel_provider = PolandSpecProvider()
    pesel_provider.seed(101)

    pesel_correct = '10010087615'
    pesel_generated = pesel_provider.pesel(
        datetime.date(2010, 1, 1), Gender.MALE)
    assert pesel_correct == pesel_generated

# Generated at 2022-06-13 23:15:52.860719
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=42)

    assert provider.pesel(datetime.datetime(2000,3,3), Gender.MALE) == '00030327172'

# Generated at 2022-06-13 23:15:54.011023
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Tests if method pesel of PolandSpecProvider generetes valid 11-digit number."""
    poland = PolandSpecProvider()
    assert len(poland.pesel().strip()) == 11

# Generated at 2022-06-13 23:15:58.047391
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import pytest
    from mimesis.enums import Gender

    provider = PolandSpecProvider()
    gender = Gender.FEMALE
    pesel = provider.pesel(birth_date=Datetime().datetime(1991, 1, 1),
                           gender=gender)
    assert len(pesel) == 11
    assert int(pesel) > 0

    gender = Gender.MALE
    pesel = provider.pesel(birth_date=Datetime().datetime(1991, 1, 1),
                           gender=gender)
    assert len(pesel) == 11
    assert int(pesel) > 0

    pesel = provider.pesel(birth_date=Datetime().datetime(1991, 1, 1))
    assert len(pesel) == 11
    assert int(pesel) > 0


# Generated at 2022-06-13 23:16:00.671067
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    date_object = "1990-01-02"
    gender = "male"
    assert len(PolandSpecProvider().pesel(date_object, gender)) == 11

# Generated at 2022-06-13 23:16:09.668321
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # empty parameters should be processed correctly
    assert len(PolandSpecProvider().pesel()) == 11
    assert len(PolandSpecProvider().pesel(gender=Gender.MALE)) == 11
    assert len(PolandSpecProvider().pesel(gender=Gender.FEMALE)) == 11

    # test method with gender parameter should return correct value
    assert (PolandSpecProvider().pesel(gender=Gender.MALE))[10] == '1'
    assert (PolandSpecProvider().pesel(gender=Gender.MALE))[10] == '3'
    assert (PolandSpecProvider().pesel(gender=Gender.MALE))[10] == '5'
    assert (PolandSpecProvider().pesel(gender=Gender.MALE))[10] == '7'

# Generated at 2022-06-13 23:16:17.298229
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel() in ['44071401358',
                    '01140901359',
                    '97080700818',
                    '70102306787']
    assert p.pesel(gender=Gender.MALE) in ['24070201527',
                                       '65031900909',
                                       '86072501708',
                                       '59010901833']
    assert p.pesel(gender=Gender.FEMALE) in ['06050901065',
                                         '62091801184',
                                         '63102901567',
                                         '57212901897']

# Generated at 2022-06-13 23:16:18.894906
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl_provider = PolandSpecProvider()
    pesel = pl_provider.pesel()
    assert len(pesel) == 11


# Generated at 2022-06-13 23:17:02.931409
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert isinstance(p.pesel(), str)
    assert len(p.pesel()) == 11
    assert p.pesel().isdigit()


# Generated at 2022-06-13 23:17:07.636009
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    datetime_object = datetime(year=1991, month=11, day=2)
    assert PolandSpecProvider().pesel(birth_date=datetime_object, gender=Gender.MALE) == '91020668148'

# Generated at 2022-06-13 23:17:19.401274
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    from mimesis.providers import Generic
    from mimesis.enums import Gender
    generic = Generic('pl')
    for i in range(100):
        # Ensures that the generated date is within the range 1940-2018
        pesel = generic.poland_provider.pesel(Gender.MALE)
        assert int(pesel[:2]) in [18, 19, 20, 21, 22]
        assert 1 <= int(pesel[2:4]) <= 12
        assert 1 <= int(pesel[4:6]) <= 31
        assert 0 <= int(pesel[6:9]) <= 999
        assert int(pesel[9]) % 2 == 1
        assert 0 <= int(pesel[10]) <= 9

# Generated at 2022-06-13 23:17:25.170156
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from mimesis.providers import PolandSpecProvider
    provider = PolandSpecProvider()
    print(provider.pesel(date_object=provider.datetime(), gender=Gender.MALE))  # noqa: E501
    print(provider.pesel(date_object=provider.datetime(), gender=Gender.FEMALE))  # noqa: E501
    print(provider.pesel(date_object=provider.datetime(), gender=None))  # noqa: E501


# Generated at 2022-06-13 23:17:29.912361
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(birth_date=Datetime(2019, 12, 15).datetime(), gender=Gender.FEMALE)
    assert pesel == '19121574124'


# Generated at 2022-06-13 23:17:32.608907
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert (len(pesel) == 11)

# Generated at 2022-06-13 23:17:34.655071
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel of class PolandSpecProvider."""
    pesel_provider = PolandSpecProvider()
    pesel = pesel_provider.pesel()

    assert isinstance(pesel, str)

    assert len(pesel) == 11

# Generated at 2022-06-13 23:17:36.752303
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel() == '97100100174'

# Generated at 2022-06-13 23:17:44.486744
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Unit test for method pesel of class PolandSpecProvider

    from datetime import datetime
    from mimesis.enums import Gender

    test_cases = (
        (None, Gender.MALE, datetime(1971, 4, 4)),
        (None, Gender.FEMALE, datetime(2003, 7, 14)),
        ('91032713166', None, None)
    )

    poland_provider = PolandSpecProvider(seed=0)

    for test_case in test_cases:
        pesel = poland_provider.pesel(
            test_case[0],
            test_case[1],
        )

        assert poland_provider.validate_pesel(pesel), 'invalid PESEL'

# Generated at 2022-06-13 23:17:52.359385
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    # Result of method pesel of class PolandSpecProvider must be str
    assert type(poland.pesel()) == str
    # Output of method pesel of class PolandSpecProvider contains 11 digits
    assert len(poland.pesel()) == 11

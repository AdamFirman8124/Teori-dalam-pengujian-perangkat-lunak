

# Generated at 2022-06-13 23:13:01.154152
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=1234)
    result = provider.pesel(birth_date=provider.datetime(2000, 2018), gender=provider.gender())
    assert result == '20153253399'


# Generated at 2022-06-13 23:13:02.615511
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert(p.pesel() != 0)

# Generated at 2022-06-13 23:13:04.611664
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert '96081867170' == PolandSpecProvider().pesel(gender=Gender.MALE)

# Generated at 2022-06-13 23:13:10.413835
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    print(provider.pesel(birth_date='1961-06-22', gender=Gender.MALE))
    print(provider.pesel(birth_date='1961-06-22', gender=Gender.FEMALE))
    print(provider.pesel(birth_date='1961-06-22'))
test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:13:15.194741
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
	provider = PolandSpecProvider()
	assert provider.pesel(gender=Gender.FEMALE) == '84120677977'
	assert provider.pesel(gender=Gender.MALE) == '95080543189'

  # Unit test for method nip of class PolandSpecProvider

# Generated at 2022-06-13 23:13:17.090484
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl_provider = PolandSpecProvider()
    assert len(pl_provider.pesel()) == 11


# Generated at 2022-06-13 23:13:23.015080
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(birth_date=Datetime().datetime(1946, 1, 3), gender=Gender.MALE)

    assert len(pesel) == 11
    #January 3rd, 1946
    assert pesel[0:2] == "46"
    assert pesel[2:4] == "01"
    assert pesel[4:6] == "03"


# Generated at 2022-06-13 23:13:27.609760
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    # Should be a 11 digit number
    assert len(pesel) == 11
    assert int(pesel[:-1]) % 10 == int(pesel[-1])

# Generated at 2022-06-13 23:13:29.996609
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert (provider.pesel() == '01010110101')


# Generated at 2022-06-13 23:13:40.758564
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test that pesel returns right values."""
    provider = PolandSpecProvider()
    pesel_1 = provider.pesel(birth_date='1990-01-01', gender=Gender.MALE)
    pesel_2 = provider.pesel(birth_date='1990-01-01', gender=Gender.FEMALE)
    pesel_3 = provider.pesel(birth_date='1990-01-01', gender=Gender.UNKNOWN)

    assert len(pesel_1) == 11
    assert len(pesel_2) == 11
    assert len(pesel_3) == 11

    pesel_start_1 = int(pesel_1[:6])
    pesel_start_2 = int(pesel_2[:6])

# Generated at 2022-06-13 23:13:57.182176
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    provider = PolandSpecProvider(seed=12346)
    pesel = provider.pesel

    # testing date stamp
    date = pesel(birth_date=(Datetime().datetime(year=2018, month=10, day=23)), gender=Gender.MALE)
    assert date[:4] == '0347'

    # testing generated pesel
    assert pesel() == '92082508155'
    assert pesel() == '98120795254'
    assert pesel() == '95101452786'
    assert pesel() == '94072478151'
    assert pesel() == '96111028703'
    assert pesel() == '93032979239'
    assert pesel() == '90102823868'
    assert pesel() == '91102116691'
    assert pesel

# Generated at 2022-06-13 23:14:03.494657
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    gen = PolandSpecProvider(seed=1234)
    assert gen.pesel(birth_date=gen.datetime(1940, 2018), gender=Gender.MALE) == '1809030027'
    assert gen.pesel(birth_date=gen.datetime(1940, 2018), gender=Gender.FEMALE) == '9912030301'
    assert gen.pesel(birth_date=gen.datetime(1940, 2018), gender=None) == '8809030049'


# Generated at 2022-06-13 23:14:08.932902
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    print(p.pesel())
    print(p.pesel(datetime(year=1955, month=2, day=9), Gender.MALE))
    print(p.pesel(datetime(year=2000, month=12, day=12), Gender.FEMALE))

# Generated at 2022-06-13 23:14:18.749092
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import unittest
    from mimesis.exceptions import NoParamException

    class TestPolandSpecProviderPesel(unittest.TestCase):

        def setUp(self):
            self.unit = PolandSpecProvider()

        def test_pesel(self):
            self.assertTrue(
                self.unit.pesel(birth_date='02-02-1970', gender=0))

        def test_pesel_with_wrong_parameters(self):
            with self.assertRaises(NoParamException):
                self.unit.pesel(birth_date='02-02-1970', gender='male')

        def tearDown(self):
            del self.unit

    unittest.main()

# Generated at 2022-06-13 23:14:30.034317
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    assert PolandSpecProvider().pesel() == "13011712822"
    assert PolandSpecProvider().pesel(Datetime().datetime(1990, 1, 1)) == "14010111608"
    assert PolandSpecProvider().pesel(Datetime().datetime(2018, 1, 1)) == "18220118670"
    assert PolandSpecProvider().pesel(Datetime().datetime(2000, 1, 1)) == "00020203324"
    assert PolandSpecProvider().pesel(Datetime().datetime(1943, 1, 1)) == "43010110174"
    assert PolandSpecProvider().pesel(Datetime().datetime(1943, 1, 1), Gender.FEMALE) == "43010114626"

# Generated at 2022-06-13 23:14:32.655431
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.providers import PolandSpecProvider
    if PolandSpecProvider.pesel(birth_date=Datetime().datetime(1997, 2, 20), gender=Gender.FEMALE) == "97020851514":
        assert True
    else:
        assert False

# Generated at 2022-06-13 23:14:35.305167
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert len(provider.pesel()) == 11


# Generated at 2022-06-13 23:14:41.173132
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Create object PolandSpecProvider with seed 1
    # (seed 1 will make PolandSpecProvider method pesel give always the same result)
    provider = PolandSpecProvider(1)

    # Make provider method pesel generate 11-digit PESEL
    # assign result to variable output
    output = provider.pesel()
    # print result to screen
    print(output)

    # Assert that method pesel return 11-digit PESEL
    assert output == '22050331743'


# Generated at 2022-06-13 23:14:43.601872
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(str(pesel)) == 11


# Generated at 2022-06-13 23:14:47.861013
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    a = PolandSpecProvider(seed=42)
    print(a.pesel(birth_date=Datetime().datetime(1996, 1, 20), gender=Gender.MALE))
    print(a.pesel(birth_date=Datetime().datetime(1996, 1, 20), gender=Gender.FEMALE))
    print(a.pesel(birth_date=Datetime().datetime(1996, 1, 20)))


# Generated at 2022-06-13 23:14:56.557665
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(str(pesel)) == 11, 'PESEL should have length 11'


# Generated at 2022-06-13 23:15:03.922809
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    from mimesis.providers import Person
    from time import time

    pesel = PolandSpecProvider().pesel()
    assert all(str(i) in pesel for i in range(10))

    # Check for year validity
    year = str(pesel[0:2])
    if int(year) > 18:
        assert int(pesel[2:4]) <= 12
    else:
        assert int(pesel[2:4]) <= 53

    # Check for date validity
    date = Person('pl').date_of_birth()
    assert int(pesel[0:2]) == date.year % 100
    assert int(pesel[2:4]) == date.month
    assert int(pesel[4:6]) == date.day

    #

# Generated at 2022-06-13 23:15:11.316230
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()
    gender = 1
    result = pl.pesel(gender=gender)
    print(result)
    assert len(result) == 11
    assert gender in (1, 3, 5, 7, 9)
    gender = 2
    result = pl.pesel(gender=gender)
    print(result)
    assert len(result) == 11
    assert gender in (0, 2, 4, 6, 8)


# Generated at 2022-06-13 23:15:20.011030
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    from datetime import datetime
    assert poland.pesel(birth_date=datetime(2018, 4, 29), gender=Gender.MALE) == '18042918953'
    assert poland.pesel(birth_date=datetime(2018, 4, 29), gender=Gender.FEMALE) == '18042928953'
    assert poland.pesel(birth_date=datetime(2018, 4, 29)) == '18042988905'
    assert poland.pesel(gender=Gender.MALE) == '92082218459'
    assert poland.pesel(gender=Gender.FEMALE) == '50211013396'
    assert poland.pesel() == '98120349728'

# Generated at 2022-06-13 23:15:21.937844
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() != ""


# Generated at 2022-06-13 23:15:32.145081
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import random

    test_seed = random.randint(1,100)
    random.seed(test_seed)

    poland_provider = PolandSpecProvider()

    test_date = poland_provider.datetime(1940, 2018)

    test_gender = poland_provider.gender()

    test_pesel = poland_provider.pesel(test_date,test_gender)

    import pdb
    pdb.set_trace()

    assert len(test_pesel) == 11


# Generated at 2022-06-13 23:15:35.452657
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel(gender=Gender.MALE)
    assert len(pesel) == 11
    assert int(pesel[-1]) % 2 == 1 # last digit is male gender

# Generated at 2022-06-13 23:15:44.243589
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import mimesis

    spec_poland = mimesis.PolandSpecProvider()
    spec_poland.seed(0)
    assert spec_poland.pesel() == '86120627288'

# Generated at 2022-06-13 23:15:50.497024
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    provider = PolandSpecProvider(seed=123)

    # Case1
    result_case1 = provider.pesel(birth_date=1308656654, gender=Gender.MALE)
    expected_result_case1 = '92041333009'
    assert result_case1 == expected_result_case1

    # Case2
    result_case2 = provider.pesel(birth_date=1337377400, gender=Gender.FEMALE)
    expected_result_case2 = '12052093275'
    assert result_case2 == expected_result_case2

    # Case3
    result_case3 = provider.pesel(birth_date=1364566654, gender=None)

# Generated at 2022-06-13 23:15:51.575335
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    x = PolandSpecProvider()
    pesel = x.pesel()
    assert len(pesel) == 11
    assert type(pesel) == str

# Generated at 2022-06-13 23:16:35.345996
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()

# Generated at 2022-06-13 23:16:38.558848
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis import PolandProvider
    pl = PolandProvider()
    assert len(pl.pesel()) == 11
    assert len(pl.pesel(gender=Gender.MALE)) == 11
    assert len(pl.pesel(gender=Gender.FEMALE)) == 11



# Generated at 2022-06-13 23:16:40.674919
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test PolandSpecProvider.pesel() method."""
    pass



# Generated at 2022-06-13 23:16:49.570684
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_cls_1 = PolandSpecProvider(seed=1)
    assert pesel_cls_1.pesel(gender=Gender.MALE, birth_date=datetime.datetime(1967, 12, 1)) == "67120115641"
    assert pesel_cls_1.pesel(gender=Gender.FEMALE, birth_date=datetime.datetime(1967, 12, 1)) == "67120147230"
    assert pesel_cls_1.pesel(gender=Gender.UNKNOWN, birth_date=datetime.datetime(1967, 12, 1)) == "67120147230"

# Generated at 2022-06-13 23:16:58.378613
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Test with gender parameter
    p = PolandSpecProvider()
    assert p.pesel(gender=Gender.FEMALE).startswith("94")
    assert p.pesel(gender=Gender.FEMALE).startswith("94")
    assert p.pesel(gender=Gender.MALE).startswith("85")
    assert p.pesel(gender=Gender.MALE).startswith("85")
    # Test without gender parameter
    p = PolandSpecProvider()
    assert isinstance(p.pesel(), str)
    assert isinstance(p.pesel()[0], str)
    # Test with birth_date parameter
    p = PolandSpecProvider()
    assert p.pesel(birth_date=Datetime().datetime(1993, 6, 8)).startswith("9306")


# Generated at 2022-06-13 23:17:01.830497
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    x = PolandSpecProvider
    x.pesel(birth_date= Datetime().datetime(1940, 2018), gender= Gender.MALE)

# Generated at 2022-06-13 23:17:15.036754
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    poland = PolandSpecProvider()
    pesel = poland.pesel(gender=Gender.MALE)
    assert len(pesel) == 11
    assert poland.validate_pesel(pesel)
    assert int(pesel[9]) % 2 == 1
    assert poland.validate_pesel(poland.pesel(gender=Gender.FEMALE))
    assert poland.validate_pesel(poland.pesel(gender=Gender.FEMALE))
    assert poland.validate_pesel(poland.pesel())


# Generated at 2022-06-13 23:17:17.495960
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print("\n\nUnit test for method pesel of class PolandSpecProvider")
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    print("PESEL length: ", len(pesel), " Pesel: ", pesel)


# Generated at 2022-06-13 23:17:19.014771
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(birth_date=None, gender=None)
    assert len(pesel) == 11


# Generated at 2022-06-13 23:17:24.275426
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert provider.pesel(birth_date=None, gender=None) is not None
    assert provider.pesel(birth_date=None, gender=Gender.MALE) is not None
    assert provider.pesel(birth_date=None, gender=Gender.FEMALE) is not None
    assert provider.pesel(birth_date=Datetime().datetime(1970, 1, 1), gender=Gender.FEMALE) is not None

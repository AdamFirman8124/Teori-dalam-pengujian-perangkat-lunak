

# Generated at 2022-06-13 23:13:05.929771
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    P = PolandSpecProvider()
    print("Generated rand PESEL is", P.pesel())
    print("Generated rand PESEL is", P.pesel(birth_date = P.datetime(1940, 2018),gender = Gender.MALE))
    print("Generated rand PESEL is", P.pesel(gender = Gender.MALE))
    print("Generated rand PESEL is", P.pesel(gender = Gender.FEMALE))
    print("Generated rand PESEL is", P.pesel(birth_date = P.datetime(1940, 2018)))

# Generated at 2022-06-13 23:13:14.472029
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    data = []
    for _ in range(100):
        data.append(PolandSpecProvider().pesel())
    assert len(set(data)) == 100
    for d in data:
        assert len(d) == 11
        assert int(d[0]) in (0, 1, 2, 3)
    assert PolandSpecProvider().pesel(birth_date=Datetime().datetime(1900, 1929), gender=Gender.FEMALE)
    assert PolandSpecProvider().pesel(birth_date=Datetime().datetime(1900, 1929), gender=Gender.MALE)
    assert PolandSpecProvider().pesel(birth_date=Datetime().datetime(1930, 1969), gender=Gender.FEMALE)

# Generated at 2022-06-13 23:13:22.300850
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # arrange
    test_seed = '9beb7fb4-fbac-4c98-bee4-52d71137b375'
    test_gender = Gender.FEMALE
    test_birthdate = Datetime().datetime(1940, 2018, seed=test_seed)
    expected_pesel = '06510760072'

    # act
    actual_pesel = PolandSpecProvider().pesel(test_birthdate, test_gender)

    # assert
    assert actual_pesel == expected_pesel

# Generated at 2022-06-13 23:13:25.829923
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    ctx = PolandSpecProvider()
    print(ctx.pesel(birth_date=ctx.datetime(1990, 2018), gender=ctx.gender()))

# Generated at 2022-06-13 23:13:30.406891
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider(seed = "abcd")
    assert poland.pesel(1940, Gender.MALE) == '40011312345'
    assert poland.pesel(2000, Gender.FEMALE) == '20101234456'

# Generated at 2022-06-13 23:13:40.898465
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Defining the number of tests that should be performed
    # for the code under test (the method pesel of class PolandSpecProvider)
    test_count = 100

    # Iteration of the tests
    for i in range(0, test_count):
        # Generating a random date of birth in the form of a string
        # and converting it to the DateTime format
        random_date = PolandSpecProvider().datetime(1940, 2018)

        # Generating a random gender (MALE or FEMALE)
        random_gender = PolandSpecProvider().random.choice([Gender.MALE, Gender.FEMALE])

        # Generation of a random PESEL number
        generated_pesel = PolandSpecProvider().pesel(birth_date=random_date, gender=random_gender)

        # The length of the generated PESEL should be equal to

# Generated at 2022-06-13 23:13:52.524385
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """
    Call test methods for PolandSpecProvider.pesel() and test if pesel
    number is generated.
    """
    my_seed = "1"
    test_generator = PolandSpecProvider(my_seed)
    gender = Gender.MALE

    assert test_generator.pesel(gender=gender) == "97012702042"
    assert test_generator.pesel(gender=gender) == "97040601051"
    assert test_generator.pesel(gender=gender) == "97052401121"
    assert test_generator.pesel(gender=gender) == "97071701080"
    assert test_generator.pesel(gender=gender) == "97082101054"


# Generated at 2022-06-13 23:13:57.983234
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    for i in range(100):
        pesel = provider.pesel()
        assert len(pesel) == 11
        assert pesel[:2] in ("40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65")


# Generated at 2022-06-13 23:14:05.984411
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # that's my birthday
    seed = '2cf25739ae0f4e4a831f4c6dab4f4aee'
    expected_pesel = '92052407038'

    pesel = PolandSpecProvider(seed).pesel()

    assert pesel == expected_pesel

    expected_pesel = '46062505573'

    pesel = PolandSpecProvider(seed).pesel(gender=Gender.MALE)

    assert pesel == expected_pesel

    expected_pesel = '25052503906'

    pesel = PolandSpecProvider(seed).pesel(gender=Gender.FEMALE)

    assert pesel == expected_pesel

    expected_pesel = '52042403592'

    pesel = PolandSpecProvider().pesel()

    assert pesel != expected_

# Generated at 2022-06-13 23:14:09.213511
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    print(pesel)


# Generated at 2022-06-13 23:14:20.942258
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test."""
    import doctest
    doctest.testmod()


# Generated at 2022-06-13 23:14:22.856883
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(pesel) == 11 and type(pesel) == str


# Generated at 2022-06-13 23:14:27.275278
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider(seed=42)
    assert p.pesel(birth_date='2018-01-01', gender=Gender.MALE) == '18010100000000'
    assert p.pesel(birth_date='2017-01-01', gender=Gender.FEMALE) == '17010100000001'

# Generated at 2022-06-13 23:14:34.442000
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider(seed=12345)
    pesel = poland_provider.pesel(birth_date=Datetime().datetime(1940, 2018), gender=Gender.MALE)
    assert isinstance(pesel, str)
    assert len(pesel) == 11
    pesel = poland_provider.pesel(birth_date=Datetime().datetime(1940, 2018), gender=Gender.FEMALE)
    assert isinstance(pesel, str)
    assert len(pesel) == 11
    pesel = poland_provider.pesel(birth_date=Datetime().datetime(1940, 2018))
    assert isinstance(pesel, str)
    assert len(pesel) == 11
    pesel = poland_provider.pesel()

# Generated at 2022-06-13 23:14:43.918377
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    from datetime import datetime

    pl_provider = PolandSpecProvider(seed=12345567)
    pesel_0 = pl_provider.pesel()
    pesel_1 = pl_provider.pesel(datetime(1969, 1, 1))
    pesel_2 = pl_provider.pesel(birth_date=datetime(1982, 1, 1),
                                gender=Gender.MALE)

    assert isinstance(pesel_0, str)
    assert len(pesel_0) == 11
    assert isinstance(pesel_1, str)
    assert len(pesel_1) == 11
    assert isinstance(pesel_2, str)
    assert len(pesel_2) == 11


# Generated at 2022-06-13 23:14:47.132617
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis import PolandSpecProvider
    from datetime import datetime

    p = PolandSpecProvider()
    pesel = p.pesel(datetime.strptime("1980-06-22", "%Y-%m-%d"))
    assert pesel == "80622129506"


# Generated at 2022-06-13 23:14:51.532932
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    for _ in range(1000):
        pesel = provider.pesel()
        assert len(pesel) == 11

# Generated at 2022-06-13 23:14:53.567529
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Create an instance of PolandSpecProvider and use it to generate a PESEL
    number.

    :return: A PESEL number
    """
    pesel = PolandSpecProvider().pesel()
    print(pesel)

# Generated at 2022-06-13 23:14:55.138350
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider.pesel()

# Generated at 2022-06-13 23:15:02.729068
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Class that provides special data for Poland (pl)."""
    test_object = PolandSpecProvider()

    list_of_pesels = []
    length_of_list_of_pesels = 100

    for i in range(length_of_list_of_pesels):
        list_of_pesels.append(test_object.pesel())

    for pesel in list_of_pesels:
        if not pesel.isdigit() or len(pesel) != 11:
            print("Failed: Pesel is not valid")
        else:
            print("Success", pesel)



# Generated at 2022-06-13 23:15:17.121267
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel() == p.pesel()
    assert p.pesel(birth_date='2018.01.01', gender=Gender.MALE) == p.pesel(birth_date='2018.01.01', gender=Gender.MALE)
    assert p.pesel(birth_date='2018.01.01', gender=Gender.FEMALE) == p.pesel(birth_date='2018.01.01', gender=Gender.FEMALE)


# Generated at 2022-06-13 23:15:19.820343
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = '92081673294'
    poland = PolandSpecProvider(seed=5974)
    assert poland.pesel(birth_date=Datetime().datetime(1992, 8, 16), gender=Gender.MALE) == pesel

# Generated at 2022-06-13 23:15:21.801702
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import pytest
    assert PolandSpecProvider().pesel() is not None


# Generated at 2022-06-13 23:15:25.540763
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=9)
    assert provider.pesel(birth_date="25-02-1999",gender=Gender.MALE) == "99022520991"

# Generated at 2022-06-13 23:15:38.694032
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from datetime import datetime
    from mimesis.enums import Gender

    gen = PolandSpecProvider()
    # default birth date is 1940-2018
    pesel_number = gen.pesel()
    assert len(pesel_number) == 11
    assert int(pesel_number[2:4]) in range(0, 13)
    assert int(pesel_number[4:6]) in range(0, 32)
    assert int(pesel_number[6:9]) in range(0, 999)
    assert int(pesel_number[9]) % 2 == 0
    # birth date = datetime.datetime(2000, 1, 1)
    pesel_number = gen.pesel(datetime(2000, 1, 1))
    assert len(pesel_number) == 11

# Generated at 2022-06-13 23:15:47.070516
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # create object of PolandSpecProvider
    provider = PolandSpecProvider()
    # generate random 11-digit PESEL
    pesel = provider.pesel()
    # save year, month, day and sex of person
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    sex = int(pesel[9])
    # check if year is between 1899 and 2100
    assert 0 <= year <= 99  # ok
    # check if month is between 1 and 12
    assert 1 <= month <= 12  # ok
    # check if day is between 1 and 31
    assert 1 <= day <= 31   # ok
    # check if sex is between 1 and 9
    assert 0 <= sex <= 9  # ok

# Generated at 2022-06-13 23:15:48.167568
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    assert len(PolandSpecProvider().pesel()) == 11

# Generated at 2022-06-13 23:15:53.045570
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
	"""Test pesel
	"""
	test_data = [
		{
			"output": '720604331636'
		},
		{
			"output": '470709382685'
		},
		{
			"output": '090119512113'
		},
		{
			"output": '490313366295'
		},
		{
			"output": '840129007347'
		}
	]

	def compare_test_data(test_data):
		pesel = PolandSpecProvider().pesel().upper()
		assert test_data["output"] == pesel
		return True

	for test in test_data:
		assert compare_test_data(test) == True

# Generated at 2022-06-13 23:15:55.908788
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Generate random 11-digit PESEL using pesel method of class
    PolandSpecProvider"""
    dtp = PolandSpecProvider()
    pesel = dtp.pesel()
    print(pesel)


# Generated at 2022-06-13 23:15:58.472644
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
   p = PolandSpecProvider()
   pesel_list = []
   pesel_list.append(p.pesel())
   pesel_list.append(p.pesel())
   pesel_list.append(p.pesel())
   pesel_list.append(p.pesel())
   pesel_list.append(p.pesel())
   pesel_list.append(p.pesel())
   return pesel_list


# Generated at 2022-06-13 23:16:12.768223
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_data = PolandSpecProvider().pesel(gender=Gender.MALE)
    assert len(pesel_data) == 11
    assert int(pesel_data[9]) % 2 != 0


# Generated at 2022-06-13 23:16:17.298354
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_provider = PolandSpecProvider()
    pesel_provider.pesel(gender=Gender.FEMALE)
    pesel_provider.pesel(birth_date=pesel_provider.datetime(1990, 2018),
                         gender=Gender.FEMALE)

# Generated at 2022-06-13 23:16:18.630437
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    pass


# Generated at 2022-06-13 23:16:24.409968
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test pesel method in PolandSpecProvider.
        Input:
        Output:
    """
    test_provider = PolandSpecProvider()
    assert len(test_provider.pesel(birth_date=Datetime().datetime(1900, 2000))) == 11
    assert len(test_provider.pesel(birth_date=Datetime().datetime(1900, 2000), gender=Gender.MALE)) == 11
    assert len(test_provider.pesel(birth_date=Datetime().datetime(1900, 2000), gender=Gender.FEMALE)) == 11


# Generated at 2022-06-13 23:16:29.272805
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland = PolandSpecProvider()
    pesel = poland.pesel()
    pesel_int = int(pesel)
    assert pesel_int % 10 == 0
    assert len(pesel) == 11

if __name__ == "__main__":
    test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:16:31.597118
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    test = PolandSpecProvider()
    test.pesel(birth_date=test.datetime(year=1994, month=9, day=8), gender=Gender.MALE)

# Generated at 2022-06-13 23:16:33.874641
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    # print(pesel)
    assert len(pesel) == 11


# Generated at 2022-06-13 23:16:36.618037
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pp=PolandSpecProvider()
    assert bool(int(pp.pesel()[2])%2) == bool(int(pp.pesel()[10])%2)
    assert int(pp.pesel()[0:2])<20

# Generated at 2022-06-13 23:16:47.154933
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('pl')
    assert person.pesel()
    assert person.pesel(birth_date=person.datetime(), gender=Gender.FEMALE)
    assert person.pesel(birth_date=person.datetime(), gender=Gender.MALE)
    # Check exception
    try:
        person.pesel(birth_date=person.datetime(), gender='Anonymous')
    except TypeError:
        pass


# Generated at 2022-06-13 23:16:56.291036
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test for method pesel of class PolandSpecProvider."""
    seed = "totally_random_seed"

    instance = PolandSpecProvider(seed=seed)

    assert instance.pesel(gender=Gender.FEMALE) == "73070458463"
    assert instance.pesel(gender=Gender.MALE) == "83052926503"
    assert instance.pesel(gender=None) == "27080044293"


# Generated at 2022-06-13 23:18:32.263735
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    print(p.pesel())

# Generated at 2022-06-13 23:18:34.333709
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(DateTime().datetime(), Gender.FEMALE)
    print(pesel)

test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:18:40.121212
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()
    pesel = pl.pesel()
    assert len(pesel) == 11
    pesel_sum = 0
    for i,el in enumerate(pesel):
        if i < 10:
            pesel_sum += (1,3,7,9,1,3,7,9,1,3)[i] * int(el)
    pesel_sum %= 10
    assert pesel_sum == 0

test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:18:41.764153
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    assert len(pesel) == 11
    int(pesel)
    return pesel


# Generated at 2022-06-13 23:18:43.812132
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    n = PolandSpecProvider()
    n.pesel()

# Generated at 2022-06-13 23:18:51.961768
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""

    PL = PolandSpecProvider()

    digit = PL.pesel()
    message = '{} is not equal to 11'.format(len(digit))
    assert len(digit) == 11, message

    digit = PL.pesel(birth_date='13-02-1988', gender=Gender.FEMALE)
    assert digit == '88021401182', '{} is not equal to 88021401282'.format(digit)

    digit = PL.pesel(birth_date='13-02-1988')
    assert digit == '88021401181', '{} is not equal to 88021401281'.format(digit)

    digit = PL.pesel(gender=Gender.MALE)

# Generated at 2022-06-13 23:19:07.464992
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pol_provider = PolandSpecProvider('TestPolishProvider')
    pesel = pol_provider.pesel()
    assert len(pesel) == 11
    assert type(pesel) == str
    assert pesel[:2] in ['90', '91', '99']  # Check if pesel has been created in 1990-1999
    assert int(pesel[2:4]) in range(12, 32)  # Check if month is in range (1-12)
    assert int(pesel[4:6]) in range(1, 32)  # Check if day is in range (1-31)
    assert int(pesel[2:4]) == 1 or int(pesel[4:6]) <= 30  # Check if given day belongs to given month
    assert int(pesel[10]) in range(10)  # Check if

# Generated at 2022-06-13 23:19:20.026308
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from datetime import datetime
    from mimesis.enums import Gender
    pl = PolandSpecProvider()
    pl.seed(1337)
    for _ in range(100):
        pesel = pl.pesel()
        assert len(pesel) == 11
        assert pesel[0] in ['1', '2', '3', '4', '5']
        assert pesel[1] in ['9', '8', '7', '6']
        assert pesel[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        assert pesel[3] in ['0', '1']

# Generated at 2022-06-13 23:19:24.402363
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    s = PolandSpecProvider()
    list_of_pesel = [s.pesel() for x in range(100)]
    assert len(list(dict.fromkeys(list_of_pesel))) == 100

# Generated at 2022-06-13 23:19:30.110763
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
      from mimesis.enums import Gender
      import datetime
      pesel = PolandSpecProvider().pesel(birth_date=datetime.datetime(1998, 3, 5), gender=Gender.MALE)
      assert len(pesel) == 11 and pesel.isnumeric()


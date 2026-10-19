

# Generated at 2022-06-13 23:13:04.595190
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    a = PolandSpecProvider()
    assert len(a.pesel()) == 11
    assert a.pesel(gender=Gender.FEMALE)[9] % 2 == 0
    assert a.pesel(gender=Gender.MALE)[9] % 2 == 1



# Generated at 2022-06-13 23:13:13.776903
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.builtins import PolandSpecProvider
    from mimesis.enums import Gender
    from datetime import datetime

    pesel = PolandSpecProvider()
    assert len(pesel.pesel()) == 11

    assert len(pesel.pesel(Gender.MALE)) == 11
    assert len(pesel.pesel(Gender.FEMALE)) == 11

    assert len(pesel.pesel(datetime(1600, 7, 12))) == 11
    assert len(pesel.pesel(datetime(1900, 7, 12))) == 11
    assert len(pesel.pesel(datetime(2000, 7, 12))) == 11
    assert len(pesel.pesel(datetime(2100, 7, 12))) == 11
    assert len(pesel.pesel(datetime(2200, 7, 12)))

# Generated at 2022-06-13 23:13:16.000275
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesel = p.pesel(Gender.FEMALE)
    print(pesel)

# Generated at 2022-06-13 23:13:20.438756
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    timestamp = datetime.datetime.now()
    pl = PolandSpecProvider()
    print(pl.pesel(birth_date=timestamp, gender=Gender.MALE))
    print(pl.pesel(birth_date=timestamp, gender=Gender.FEMALE))

# Generated at 2022-06-13 23:13:22.300463
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert len(provider.pesel()) == 11


# Generated at 2022-06-13 23:13:26.069469
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    print(pesel)

test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:13:28.458549
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11


# Generated at 2022-06-13 23:13:33.470749
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()  # pesel = pesel(datetime.date(2001, 1, 1), Gender.MALE)
    print(pesel)


if __name__ == "__main__":
    test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:13:41.256824
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()

# Generated at 2022-06-13 23:13:48.503486
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel(birth_date=None, gender=Gender.MALE)
    print(pesel)
    assert len(str(pesel)) == 11
    print("--- In function: test_PolandSpecProvider_pesel ---")
    print("pesel =", pesel)
    print("pesel length =", len(str(pesel)))



# Generated at 2022-06-13 23:14:05.043405
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Tests pesel method of class PolandSpecProvider."""
    psp = PolandSpecProvider()
    pesels = [psp.pesel(gender=gender) for _ in range(10) for gender in (Gender.MALE, Gender.FEMALE)]
    pesels_m = [p for p in pesels if p[9] in ("1", "3", "5", "7", "9")]
    pesels_f = [p for p in pesels if p[9] in ("0", "2", "4", "6", "8")]
    assert len(pesels) == len(pesels_m) + len(pesels_f)
    assert len(pesels) == 20



# Generated at 2022-06-13 23:14:10.771637
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    seed = "da6cfdb0-9e17-4c59-b1dd-cbea6a8d6e39"
    pesel_number = "57121233236"
    PESEL = PolandSpecProvider(seed=seed)
    assert PESEL.pesel(birth_date = "1998-12-12", gender="Male") == pesel_number

# Generated at 2022-06-13 23:14:13.954624
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test pesel method.

    Expected:
        True
    """
    pol = PolandSpecProvider()
    res = pol.pesel()
    assert len(res) == 11

# Generated at 2022-06-13 23:14:19.235445
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from mimesis.providers.datetime import Datetime
    from datetime import datetime
    datetime_object = Datetime(datetime=datetime(2017, 2, 28,))
    p = PolandSpecProvider()
    actual = p.pesel(datetime_object.datetime(2017, 2, 28,),Gender.FEMALE)
    assert actual == '17022500237'

# Generated at 2022-06-13 23:14:26.593304
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    if PolandSpecProvider().pesel(birth_date='2018-12-31', gender=Gender.MALE) != '90312307123':
        raise ReferToGNCPA('dates don\'t match')
    if PolandSpecProvider().pesel(birth_date='1990-07-28', gender=Gender.FEMALE) != '90072892362':
        raise ReferToGNCPA('dates don\'t match')


# Generated at 2022-06-13 23:14:33.117656
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    '''
    Count occurences of PESEL numbers in the list of 100000.
    Return:
    {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 1023}
    '''
    rand = PolandSpecProvider()
    li = []
    oc = {x:li.count(x) for x in li}
    for i in range(100000):
        li.append(rand.pesel())
        oc = {x:li.count(x) for x in li}
    print(oc)


# Generated at 2022-06-13 23:14:39.237420
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis import PolandSpecProvider
    polandSpecProvider = PolandSpecProvider()
    birth_date = polandSpecProvider.datetime(datetime_format='%m-%d-%Y')
    gender = polandSpecProvider.gender(Gender.MALE)
    pesel = polandSpecProvider.pesel(birth_date, gender)
    assert pesel


# Generated at 2022-06-13 23:14:46.221744
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
	provider = PolandSpecProvider('47c86b02f9b35bf3bc3bc3bc3bc3bc3bc3bc3bc3bc3bc3b')
	result_1 = provider.pesel(birth_date=None, gender=None)
	assert result_1 == "43081218158"

	provider = PolandSpecProvider('47c86b02f9b35bf3bc3bc3bc3bc3bc3bc3bc3bc3bc3bc3b')
	result_2 = provider.pesel(provider.datetime(1940, 2018), gender=None)
	assert result_2 == "55012419553"


# Generated at 2022-06-13 23:14:49.311607
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert 11 == len(p.pesel())

# Generated at 2022-06-13 23:14:52.815222
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()
    pesel = poland_provider.pesel()
    assert pesel

# Generated at 2022-06-13 23:15:08.957063
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()
    assert len(poland_provider.pesel(birth_date="1997-07-25", gender=Gender.MALE)) == 11

# Generated at 2022-06-13 23:15:12.172796
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert len(provider.pesel()) == 11
    assert isinstance(provider.pesel(), str)



# Generated at 2022-06-13 23:15:15.798167
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert pesel.isdigit()



# Generated at 2022-06-13 23:15:18.180306
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test pesel"""
    # Arrange
    poland_provider = PolandSpecProvider()

    # Act
    result = poland_provider.pesel()

    # Assert
    assert result.isdigit()

# Generated at 2022-06-13 23:15:22.362376
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel_number = provider.pesel(gender = Gender.MALE)
    print(pesel_number)
    assert len(pesel_number) == 11


# Generated at 2022-06-13 23:15:35.895913
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import random
    random.seed(1)
    a = PolandSpecProvider(seed=1)

    assert a.pesel(gender='male') == '73061612390'
    assert a.pesel(gender='female') == '96050119800'
    assert a.pesel() == '83080418177'
    b = PolandSpecProvider(seed=2)
    assert b.pesel(gender='male') == '80030507075'
    assert b.pesel(gender='female') == '90051011776'
    assert b.pesel() == '53041811813'
    c = PolandSpecProvider(seed=3)
    assert c.pesel(gender='male') == '90052800709'
    assert c.pesel(gender='female') == '79080505570'
   

# Generated at 2022-06-13 23:15:38.641373
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    output = provider.pesel()
    assert len(output) == 11
    for i in output:
        assert int(i) >= 0
        assert int(i) <= 9


# Generated at 2022-06-13 23:15:41.105219
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel(birth_date='1998-11-04', gender=Gender.FEMALE)
    assert pesel == '98114566680'

# Generated at 2022-06-13 23:15:48.743375
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    genders = set(Gender)
    wrong_genders = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    assert genders - wrong_genders == set()

    gender = Gender.MALE
    assert gender == Gender.MALE

    gender = Gender.FEMALE
    assert gender == Gender.FEMALE

    pesel_provider = PolandSpecProvider()
    pesel_val = pesel_provider.pesel(gender=Gender.MALE)
    assert len(pesel_val) == 11

    pesel_provider = PolandSpecProvider()
    pesel_val = pesel_provider.pesel(gender=Gender.FEMALE)
    assert len(pesel_val) == 11

# Generated at 2022-06-13 23:15:51.362377
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=42)
    result = provider.pesel()
    print(result)
    assert result == '97070129130'



# Generated at 2022-06-13 23:16:19.095751
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesel = p.pesel()
    assert type(pesel) == str and len(pesel) == 11
    pesel = p.pesel(gender=Gender.MALE)
    assert type(pesel) == str and len(pesel) == 11
    pesel = p.pesel(gender=Gender.FEMALE)
    assert type(pesel) == str and len(pesel) == 11
    #to be completed


# Generated at 2022-06-13 23:16:21.853894
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_generator = PolandSpecProvider()
    pesel_instance = pesel_generator.pesel(birth_date='1995-12-13', gender='male')
    assert pesel_instance == "951213000002"

# Generated at 2022-06-13 23:16:23.816871
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider"""
    provider = PolandSpecProvider()
    assert len(provider.pesel()) == 11

# Generated at 2022-06-13 23:16:29.137354
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import datetime

    provider = PolandSpecProvider()
    arr = []
    for i in range(0, 10):
        pesel = provider.pesel(datetime.date(1989, 5, 6))
        if (pesel not in arr):
            print(pesel)
            arr.append(pesel)


# Generated at 2022-06-13 23:16:32.523922
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_extract = PolandSpecProvider().pesel(datetime.datetime(1941, 1, 22), Gender.MALE)
    print(pesel_extract)

if __name__ == '__main__':
    test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:16:34.060337
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    actualPesel = PolandSpecProvider().pesel()
    assert len(actualPesel) == 11


# Generated at 2022-06-13 23:16:35.746249
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = 10082417560
    assert PolandSpecProvider().pesel(birth_date=pesel) == str(pesel)

# Generated at 2022-06-13 23:16:36.693357
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider.pesel(Gender.UNISEX)

# Generated at 2022-06-13 23:16:40.439530
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesel_number = p.pesel()
    assert len(pesel_number) == 11
    assert pesel_number.isdigit() == True

# Generated at 2022-06-13 23:16:49.042660
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    test = PolandSpecProvider()
    assert len(test.pesel()) == 11
    assert len(test.pesel(birth_date=Datetime().datetime())) == 11
    assert len(test.pesel(gender=Gender.MALE)) == 11
    assert len(test.pesel(birth_date=Datetime().datetime(), gender=Gender.FEMALE)) == 11


# Generated at 2022-06-13 23:17:17.215572
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_1 = PolandSpecProvider().pesel(birth_date=Datetime().datetime(2007, 1, 15), gender=Gender.FEMALE)
    assert pesel_1 == '76011567919'
    pesel_2 = PolandSpecProvider().pesel(birth_date=Datetime().datetime(1961, 6, 1), gender=Gender.MALE)
    assert pesel_2 == '61060127263'

# Generated at 2022-06-13 23:17:19.588564
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()
    pesel = poland_provider.pesel()

    # Length of pesel should be equal to 11
    assert len(pesel) == 11

# Generated at 2022-06-13 23:17:20.513954
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() == "81012158706"

# Generated at 2022-06-13 23:17:36.524014
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """
    Test of method pesel of class PolandSpecProvider
    """
    ps = PolandSpecProvider(seed=20)
    assert ps.pesel(birth_date=Datetime().datetime(year=1987, month=8, day=23)) == '87082300001'
    assert (ps.pesel(birth_date=Datetime().datetime(year=1987, month=8, day=23), gender=Gender.MALE) ==
            '87082300001')
    assert (ps.pesel(birth_date=Datetime().datetime(year=1987, month=8, day=23), gender=Gender.FEMALE) ==
            '87082300001')

# Generated at 2022-06-13 23:17:38.106428
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print(PolandSpecProvider(seed=1234567890).pesel())


# Generated at 2022-06-13 23:17:39.470154
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel() == p.pesel()

# Generated at 2022-06-13 23:17:43.104569
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()
    date_object = Datetime().datetime(1990, 2017)
    gender = Gender.MALE
    pesel = poland_provider.pesel(date_object, gender)
    print(pesel)


# Generated at 2022-06-13 23:17:43.971008
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
	prov_pl = PolandSpecProvider()
	print(prov_pl.pesel())

# Generated at 2022-06-13 23:17:59.612286
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    print (pesel)
    assert len(pesel) == 11
    # Should be a 10-digit number (NIP)
    # Pesel = [6] [1] [9] [7] [0] [1] [0] [0] [0] [0] [5]
    # Weights = [6] [5] [7] [2] [3] [4] [5] [6] [7]
    # SUM = (6 * 6) + (1 * 5) + (9 * 7) + (7 * 2) + (0 * 3) + (1 * 4) + (0 * 5) + (0 * 6) + (0 * 7) = 90
    # Checksum = 90 % 11 = 9 = 5; LAST DIGIT =

# Generated at 2022-06-13 23:18:02.380141
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()

    print(provider.pesel())
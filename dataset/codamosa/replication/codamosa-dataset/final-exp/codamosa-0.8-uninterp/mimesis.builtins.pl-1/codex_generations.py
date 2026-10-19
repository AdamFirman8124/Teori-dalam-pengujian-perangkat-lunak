

# Generated at 2022-06-13 23:13:03.080747
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=4321)
    assert provider.pesel(gender=Gender.MALE) == '96081159469'


# Generated at 2022-06-13 23:13:05.017928
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    test_pl = PolandSpecProvider(seed=0)
    assert test_pl.pesel() == '93070813602'

# Generated at 2022-06-13 23:13:13.321436
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_list = []
    for a in range(1, 1001):
        pesel_list.append(PolandSpecProvider().pesel())
    for a in range(1, 1001):
        assert(pesel_list[a] != PolandSpecProvider().pesel())
    pesel_list = []
    for a in range(1, 1001):
        pesel_list.append(PolandSpecProvider().pesel(birth_date = Datetime().datetime(2000,2000)))
    for a in range(1, 1001):
        assert(pesel_list[a] != PolandSpecProvider().pesel(birth_date = Datetime().datetime(2000,2000)))


# Generated at 2022-06-13 23:13:19.405889
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()
    pesel = poland_provider.pesel(birth_date=poland_provider.datetime(1980, 1, 1).date(), gender=Gender.MALE)
    print(poland_provider.datetime(1980, 1, 1).date())
    print(pesel)
    return pesel


# Generated at 2022-06-13 23:13:27.914038
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    cls = PolandSpecProvider()
    print(cls.pesel(birth_date=Datetime().datetime('1850-01-01')))
    print(cls.pesel(birth_date=Datetime().datetime('1950-01-01')))
    print(cls.pesel(birth_date=Datetime().datetime('2000-01-01')))
    print(cls.pesel(birth_date=Datetime().datetime('2100-01-01')))
    print(cls.pesel(birth_date=Datetime().datetime('2200-01-01')))
    print(cls.pesel(birth_date=Datetime().datetime('1850-01-01'), gender=Gender.MALE))


# Generated at 2022-06-13 23:13:31.385033
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    t = p.pesel(birth_date='1999-10-01', gender=Gender.MALE)
    assert t == '99100190014'

# Generated at 2022-06-13 23:13:36.508665
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesels = []
    for i in range(10000):
        pesel = p.pesel()
        if pesel not in pesels:
            pesels.append(pesel)
            print(pesel)


# Generated at 2022-06-13 23:13:41.907528
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    provider = PolandSpecProvider()
    for gender in Gender:
        pesel = provider.pesel(gender=gender)
        assert len(pesel) == 11
        gender_digit = int(pesel[8])
        if gender == Gender.MALE:
            assert gender_digit in (1, 3, 5, 7, 9)
        if gender == Gender.FEMALE:
            assert gender_digit in (0, 2, 4, 6, 8)


# Generated at 2022-06-13 23:13:46.545634
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    returned_value = provider.pesel()
    assert len(returned_value) == 11
    assert isinstance(returned_value, str)

# Generated at 2022-06-13 23:13:50.940640
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=123456)
    assert provider.pesel() == '97012218200'  # PESEL for Ben Affleck
    assert provider.pesel(birth_date=Datetime().datetime(1944, 1944)) == \
        '4401221523'



# Generated at 2022-06-13 23:14:36.845566
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print("\n ********************** Unit test for method pesel of class PolandSpecProvider ...")
    p = PolandSpecProvider()
    gender = Gender.MALE
    pesel = p.pesel(gender = gender)
    print("pesel = ", pesel)
    assert gender == Gender.MALE


# Generated at 2022-06-13 23:14:38.729465
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Test for verifying Person class
    for i in range(10):
        assert PolandSpecProvider().pesel()

# Generated at 2022-06-13 23:14:45.025002
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # We can see if our generated pesel is correct here:
    # http://www.bph.pl/egzamin-adwokacki/egzamin-pisemny/pytania-egzaminacyjne/egzamin-z-wiedzy-o-rzeczypospolitej-polskiej-i-prawie-polskim/archiwum-pytan/r.2009/2009_19_10.html?plik=2
    pesel = PolandSpecProvider.pesel()
    print(pesel)


# Generated at 2022-06-13 23:14:48.807804
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=8)
    assert provider.pesel(birth_date=None, gender=None) == '97052301223'
    assert provider.pesel(birth_date=None, gender=Gender.MALE) == '54020901291'
    assert provider.pesel(birth_date=None, gender=Gender.FEMALE) == '26042001288'


# Generated at 2022-06-13 23:15:01.257393
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl_provider = PolandSpecProvider(seed=42)

    pesel = pl_provider.pesel()
    assert pesel == '39032713391'

    pesel = pl_provider.pesel(birth_date=pl_provider.datetime(1940, 2018))
    assert pesel == '39032713391'

    pesel = pl_provider.pesel(gender=Gender.MALE)
    assert pesel == '39032713391'

    pesel = pl_provider.pesel(birth_date=pl_provider.datetime(1940, 2018),
                              gender=Gender.FEMALE)
    assert pesel == '39032713391'

# Generated at 2022-06-13 23:15:14.737635
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel(birth_date=None, gender=Gender.MALE) == "82060912441"
    assert p.pesel(birth_date=None, gender=Gender.FEMALE) == "87061460218"
    assert p.pesel(birth_date=None, gender=None) == "55092429842"
    assert p.pesel(birth_date=Datetime().datetime(year=1980, month=1, day=1), gender=Gender.MALE) == "80101060141"
    assert p.pesel(birth_date=Datetime().datetime(year=1980, month=1, day=1), gender=Gender.FEMALE) == "80101060016"

# Generated at 2022-06-13 23:15:16.820158
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel=PolandSpecProvider().pesel()
    assert len(pesel)==11


# Generated at 2022-06-13 23:15:18.581211
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    for i in range(1, 1000):
        print(PolandSpecProvider().pesel())

if __name__ == "__main__":
    test_PolandSpecProvider_pesel()

# Generated at 2022-06-13 23:15:23.510891
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from random import seed
    from datetime import datetime
    from mimesis.builtins import PolandSpecProvider 
    from mimesis.enums import Gender, Weekday

    seed(10)
    pl_provider=PolandSpecProvider()

    # Test 1
    pesel_no=pl_provider.pesel()
    assert isinstance(pesel_no, str)
    assert len(pesel_no)==11 

    # Test 2
    birth_date=datetime(1990, 10, 12)
    gender=Gender.FEMALE
    pesel_no=pl_provider.pesel(birth_date, gender)
    assert isinstance(pesel_no, str)
    assert len(pesel_no)==11 

    # Test 3
    birth_date=pl_provider.datetime

# Generated at 2022-06-13 23:15:30.224604
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.providers import Person
    from mimesis.enums import Gender
    p = PolandSpecProvider()
    pesel_m = p.pesel(gender=Gender.MALE)
    pesel_f = p.pesel(gender=Gender.FEMALE)
    pesel = p.pesel()
    person_m = Person('pl').create(birth_date='1976-12-20')
    pesel_m_2 = p.pesel(person_m)
    person_f = Person('pl').create(birth_date='2000-01-01', gender=Gender.FEMALE)
    pesel_f_2 = p.pesel(person_f)
    pesel_2 = p.pesel()
    assert len(pesel) == 11

# Generated at 2022-06-13 23:16:26.999441
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider_test = PolandSpecProvider()
    pesel = provider_test.pesel()
    pesel_size = 11
    assert len(pesel) == pesel_size


# Generated at 2022-06-13 23:16:30.308311
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert provider.pesel(birth_date=Datetime().datetime(1940, 2018), gender=provider.gender.MALE()) == '00206226538'

# Generated at 2022-06-13 23:16:31.600969
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    print(p.pesel())

# Generated at 2022-06-13 23:16:34.824990
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    pl = PolandSpecProvider()
    assert len(pl.pesel()) == 11
    assert len(pl.pesel(gender=Gender.MALE)) == 11
    assert len(pl.pesel(gender=Gender.FEMALE)) == 11


# Generated at 2022-06-13 23:16:37.490509
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    doc_provider = PolandSpecProvider()
    pesel = doc_provider.pesel()
    assert pesel is not None

# EOF

# Generated at 2022-06-13 23:16:38.785255
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_obj = PolandSpecProvider()
    assert len(pesel_obj.pesel()) == 11


# Generated at 2022-06-13 23:16:44.654524
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test function"""
    # test correct behavior of function
    poland_spec_provider = PolandSpecProvider()
    pesel = poland_spec_provider.pesel()
    assert isinstance(pesel, str)
    assert len(pesel) == 11



# Generated at 2022-06-13 23:16:46.772661
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11

# Generated at 2022-06-13 23:16:56.181337
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pps = PolandSpecProvider()
    assert len(pps.pesel(birth_date=1970, gender=Gender.FEMALE)) == 11
    assert int(pps.pesel("1990-01-01", Gender.MALE)[9]) in (0, 2, 4, 6, 8)
    assert int(pps.pesel("1990-01-01", Gender.FEMALE)[9]) in (1, 3, 5, 7, 9)


# Generated at 2022-06-13 23:16:58.501901
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider_pesel = PolandSpecProvider()
    pesel = PolandSpecProvider_pesel.pesel()
    assert pesel == pesel

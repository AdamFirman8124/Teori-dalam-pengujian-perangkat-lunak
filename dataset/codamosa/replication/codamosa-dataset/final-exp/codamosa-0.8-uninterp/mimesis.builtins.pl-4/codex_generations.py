

# Generated at 2022-06-13 23:13:05.676427
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""
    assert PolandSpecProvider().pesel() == '96111839085'
    assert PolandSpecProvider().pesel(gender=Gender.MALE) == '95120947085'
    assert PolandSpecProvider().pesel(gender=Gender.FEMALE) == '93112441093'
    assert PolandSpecProvider().pesel(birth_date=Datetime().datetime(1993, 11, 24)) == '93112441093'


# Generated at 2022-06-13 23:13:12.998900
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    pesel0 = p.pesel(gender=Gender.MALE)
    pesel1 = p.pesel(gender=Gender.FEMALE)
    assert isinstance(pesel0, str) & isinstance(pesel1, str) & len(pesel0) == 11 & \
           len(pesel1) == 11 & pesel0[-2].isdigit() & pesel1[-2].isdigit() & \
           (int(pesel0[-2]) % 2 != 0) & (int(pesel1[-2]) % 2 == 0)

# Generated at 2022-06-13 23:13:15.348352
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel(birth_date='1996-07-25') == '96072529972'

# Generated at 2022-06-13 23:13:19.785013
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider."""

    # create a new instance of class PolandSpecProvider
    provider = PolandSpecProvider()
    assert len(provider.pesel()) == 11 and provider.pesel().isdigit()


# Generated at 2022-06-13 23:13:27.403330
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.builtins import PolandSpecProvider
    import datetime
    p = PolandSpecProvider()

    #test: all dates 1940-2018, all genders
    for year in range(1940,2019):
        for month in range(1,13):
            for day in range(1,29):
                try:
                    date_object = datetime.datetime(year,month,day)

                    for gender in [Gender.MALE, Gender.FEMALE, Gender.OTHER]:
                        pesel = p.pesel(birth_date=date_object, gender=gender)
                        assert len(pesel)==11
                except:
                    pass



# Generated at 2022-06-13 23:13:30.863143
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    locale = 'pl'
    seed = '1'
    provider = PolandSpecProvider(seed)
    provider.pesel()
    assert provider.pesel() == '05610302392'

# Generated at 2022-06-13 23:13:38.772521
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from mimesis.enums import Gender
    from mimesis.providers.date_time import Datetime
    test_pesel = PolandSpecProvider().pesel(Datetime().datetime(1940, 2018),  Gender.FEMALE)

    assert(len(test_pesel) == 11)
    assert(test_pesel[9:10] in ['0','2','4','6','8'] )


# Generated at 2022-06-13 23:13:41.474262
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel() == "88092414562"

# Generated at 2022-06-13 23:13:47.495462
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=144)
    # check whether pesel is valid
    assert provider.pesel(gender=Gender.MALE) == '98052715191'
    assert provider.pesel(gender=Gender.FEMALE) == '41022476301'

# Generated at 2022-06-13 23:13:49.400872
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider_instance = PolandSpecProvider()
    return PolandSpecProvider_instance.pesel()


# Generated at 2022-06-13 23:14:16.578460
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    a = PolandSpecProvider()
    b = a.pesel()
    c = a.pesel(birth_date=Datetime().datetime(2000, 1, 1), gender=Gender.MALE)
    d = a.pesel(birth_date=Datetime().datetime(2000, 1, 1), gender=Gender.FEMALE)


# Generated at 2022-06-13 23:14:18.196438
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert pesel == "98052104635"

# Generated at 2022-06-13 23:14:20.947851
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    # print(provider.pesel())
    return



# Generated at 2022-06-13 23:14:28.698079
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    dt = Datetime(seed=5)
    assert PolandSpecProvider(seed=5).pesel(dt.datetime(1979, 1979), Gender.FEMALE) == '79112402740'
    assert PolandSpecProvider(seed=5).pesel(dt.datetime(1979, 1979), Gender.MALE) == '79112402749'
    assert PolandSpecProvider(seed=5).pesel(dt.datetime(1979, 1979)) == '79112402747'
    assert PolandSpecProvider().pesel()


# Generated at 2022-06-13 23:14:31.180715
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_spec_provider = PolandSpecProvider()
    pesel = poland_spec_provider.pesel()
    len_pesel = len(pesel)
    assert len_pesel == 11

# Generated at 2022-06-13 23:14:33.257141
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Unit test for method pesel of class PolandSpecProvider"""
    
    pesel_provider = PolandSpecProvider()
    x=pesel_provider.pesel()
    assert len(x) == 11

# Generated at 2022-06-13 23:14:43.696445
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    PolandSpecProvider(seed=0).pesel(gender=Gender.MALE)
    PolandSpecProvider(seed=1).pesel(gender=Gender.FEMALE)
    PolandSpecProvider(seed=2).pesel(birth_date=Datetime().datetime(1940, 2018))
    PolandSpecProvider(seed=3).pesel(gender=Gender.MALE, birth_date=Datetime().datetime(1940, 2018))

# Get birth_date from pesel
pesel_birth_date = Datetime().datetime(1940, 2018)
pesel_value = PolandSpecProvider(seed=3).pesel(gender=Gender.MALE, birth_date=pesel_birth_date)
birth_date_str = pesel_value[0:2] + pesel_value[2:4]
year = "19"

# Generated at 2022-06-13 23:14:47.951880
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    test_pesel = PolandSpecProvider()
    for i in range(10):
        assert len(test_pesel.pesel()) == 11
    assert len(test_pesel.pesel(birth_date='2000-12-30', gender=Gender.MALE)) == 11
    assert len(test_pesel.pesel(birth_date='1999-11-29', gender=Gender.FEMALE)) == 11


# Generated at 2022-06-13 23:14:54.069361
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    new_PolandSpecProvider = PolandSpecProvider()
    new_pesel = new_PolandSpecProvider.pesel()
    assert len(new_pesel) == 11
    assert "1" <= new_pesel[0] <= "9"


# Generated at 2022-06-13 23:15:01.544536
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    male_pesel = PolandSpecProvider().pesel(gender=Gender.MALE)
    female_pesel = PolandSpecProvider().pesel(gender=Gender.FEMALE)
    #assert male_pesel[-1] in ["1", "3", "5", "7", "9"], "method pesel generates the wrong control digit"
    #assert female_pesel[-1] in ["0", "2", "4", "6", "8"], "method pesel generates the wrong control digit"
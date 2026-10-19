

# Generated at 2022-06-13 23:12:59.854374
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    p = PolandSpecProvider(seed=42)

    assert p.pesel() == '21082400183'

# Generated at 2022-06-13 23:13:04.482503
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    birthdate = Datetime().datetime(1950, 2018)
    assert provider.pesel(birth_date = birthdate, gender = Gender.MALE) == '45132034963'
    assert provider.pesel(birth_date = birthdate, gender = Gender.FEMALE) == '45132034972'


# Generated at 2022-06-13 23:13:07.046822
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel_object = PolandSpecProvider(seed=123)
    pesel_object.pesel()
    #assert 1 == 0
    return

# Generated at 2022-06-13 23:13:09.680282
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert all(map(lambda x: x in '0123456789', pesel))

# Generated at 2022-06-13 23:13:12.527216
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Use pre-defined seed for repeatability
    random.seed(0)
    pl_provider = PolandSpecProvider(seed=0)
    pesel = pl_provider.pesel()
    assert pesel == "83070935863"

# Generated at 2022-06-13 23:13:22.429798
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    poland_provider = PolandSpecProvider()
    pesel = poland_provider.pesel()
    assert len(pesel) == 11
    assert int(pesel[0:2]) in range(40, 100) or int(pesel[0:2]) in range(21, 40) or int(pesel[0:2]) in range(1, 21)
    assert int(pesel[2:4]) in range(1, 13)
    assert int(pesel[4:6]) in range(1, 32)
    assert int(pesel[6:9]) in range(0, 1000)
    assert int(pesel[9:]) in range(0, 10)

# Generated at 2022-06-13 23:13:36.435357
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel of class PolandSpecProvider."""
    pl = PolandSpecProvider()
    assert len(pl.pesel() == 11)
    assert int(pl.pesel()[0]) in (1,2,3,4,5,6,7,8,9,0)
    assert int(pl.pesel()[1]) in (0,1,2,3,4,5,6,7,8,9)
    assert int(pl.pesel()[2]) in (0,1,2,3,4,5,6,7,8,9)
    assert int(pl.pesel()[3]) in (1,2,3,4,5,6,7,8,9,0)

# Generated at 2022-06-13 23:13:38.185516
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    assert PolandSpecProvider().pesel() == '55110300850'


# Generated at 2022-06-13 23:13:43.232349
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    from mimesis.enums import Gender
    from mimesis.builtins import PolandSpecProvider
    from datetime import datetime

    poland_provider = PolandSpecProvider()

    pesel_1 = poland_provider.pesel()  # 2018-05-15
    print(pesel_1)

    pesel_2 = poland_provider.pesel(datetime(1990, 12, 8))
    print(pesel_2)  # 1990-12-08

    date_object = poland_provider.datetime(datetime(1990, 12, 8),
                                           datetime(1999, 1, 31))
    pesel_3 = poland_provider.pesel(date_object)
    print(pesel_3)  # 1998-03-20

    pesel_4 = poland_

# Generated at 2022-06-13 23:13:47.385552
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    import datetime
    provider.pesel(birth_date=datetime.datetime.now())
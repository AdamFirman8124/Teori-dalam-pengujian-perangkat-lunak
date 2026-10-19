

# Generated at 2022-06-13 23:13:03.573742
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    from mimesis.builtins.poland import PolandSpecProvider
    from mimesis.enums import Gender

    p = PolandSpecProvider()

    # Birth date is given, gender is not given
    p.pesel(birth_date=p.datetime(1940, 2018))

    # Birth date is not given, gender is given
    p.pesel(gender=Gender.FEMALE)

assert test_PolandSpecProvider_pesel() is None

# Generated at 2022-06-13 23:13:05.982035
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    assert p.pesel().isdigit() and len(p.pesel()) == 11



# Generated at 2022-06-13 23:13:09.728028
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    seed = "12345678901234567890123456789012345678901234567890"
    psp = PolandSpecProvider(seed=seed)
    print(psp.pesel())


# Generated at 2022-06-13 23:13:16.487855
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    p = PolandSpecProvider()
    assert p.pesel(birth_date=Datetime().datetime(1950, 2003), gender=Gender.MALE) == '50011075682'
    assert p.pesel(birth_date=Datetime().datetime(1950, 2003), gender=Gender.FEMALE) == '50011075692'
    assert p.pesel() == '84030842063'


# Generated at 2022-06-13 23:13:18.671210
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pl = PolandSpecProvider()
    actual = pl.pesel()
    assert len(actual) == 11

# Generated at 2022-06-13 23:13:21.554457
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    ply = PolandSpecProvider()
    # print(ply.pesel(birth_date='1967-04-22', gender=Gender.FEMALE))
    print(ply.pesel())

# Generated at 2022-06-13 23:13:25.330341
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel = PolandSpecProvider().pesel()
    assert len(pesel) == 11
    assert isinstance(pesel, str)

# Generated at 2022-06-13 23:13:38.591617
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p_1 = PolandSpecProvider()
    p_2 = PolandSpecProvider()
    p_3 = PolandSpecProvider()
    p_4 = PolandSpecProvider()
    p_5 = PolandSpecProvider()
    p_6 = PolandSpecProvider()
    p_7 = PolandSpecProvider()
    p_8 = PolandSpecProvider()
    p_9 = PolandSpecProvider()
    p_10 = PolandSpecProvider()
    pesel_1 = p_1.pesel()
    pesel_2 = p_2.pesel()
    pesel_3 = p_3.pesel()
    pesel_4 = p_4.pesel()
    pesel_5 = p_5.pesel()
    pesel_6 = p_6.pesel()
    pesel_7 = p_7.pesel()
   

# Generated at 2022-06-13 23:13:39.485849
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pass



# Generated at 2022-06-13 23:13:52.226049
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    pesel1 = PolandSpecProvider().pesel(birth_date=Datetime().datetime(1920, 1, 1), gender=Gender.MALE)
    print(pesel1)
    assert pesel1[2] == '8'
    assert pesel1[3] == '2'
    assert pesel1[9] == '5' or pesel1[9] == '7' or pesel1[9] == '9'

    pesel2 = PolandSpecProvider().pesel(birth_date=Datetime().datetime(2010, 12, 31), gender=Gender.FEMALE)
    print(pesel2)
    assert pesel2[2] == '0'
    assert pesel2[3] == '1'
    assert pesel2[9] == '0' or pesel2[9] == '2'
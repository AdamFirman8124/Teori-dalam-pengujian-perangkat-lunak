

# Generated at 2022-06-13 23:13:03.125686
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Test if the correct length of the returned string is 11 characters (pesel length)
    pl = PolandSpecProvider(seed=0)
    answer = pl.pesel()
    assert len(answer) == 11
    # Test if there are only digits in returned string
    assert answer.isdigit()


# Generated at 2022-06-13 23:13:05.472129
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider(seed=47)
    gen_pesel = provider.pesel()
    assert gen_pesel == "9808251757"

# Generated at 2022-06-13 23:13:09.239699
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    import pdb
    # pdb.set_trace()
    poland = PolandSpecProvider()
    p = poland.pesel()
    print(p)
    # 88110916961
    assert len(p) == 11


# Generated at 2022-06-13 23:13:11.658850
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    polandSpecProvider = PolandSpecProvider()
    print("PESEL: ")
    for i in range(100):
        print(polandSpecProvider.pesel())

# Generated at 2022-06-13 23:13:15.399207
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    p = PolandSpecProvider()
    rsl = p.pesel(gender=Gender.MALE)
    assert rsl[9] in ('1', '3', '5', '7', '9')

# Generated at 2022-06-13 23:13:23.003310
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    """Test method pesel of class PolandSpecProvider."""
    assert PolandSpecProvider().pesel(birth_date=Datetime().datetime(1940, 2018), gender='male') == '79032308525'
    assert PolandSpecProvider().pesel(birth_date=Datetime().datetime(1940, 2018), gender='female') == '79031808525'
    assert PolandSpecProvider().pesel() != '79032308525'
    assert PolandSpecProvider().pesel() != '79031808525'


# Generated at 2022-06-13 23:13:31.316773
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    provider = PolandSpecProvider()
    assert len(provider.pesel()) == 11
    assert len(provider.pesel(birth_date='2018-03-10')) == 11
    assert len(provider.pesel(birth_date=Datetime().datetime(1940, 2018))) == 11
    assert len(provider.pesel(gender=Gender.MALE)) == 11
    assert len(provider.pesel(gender=Gender.FEMALE)) == 11



# Generated at 2022-06-13 23:13:36.435787
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    print()
    print("Unit test for method pesel of class PolandSpecProvider")
    provider = PolandSpecProvider()
    pesel = provider.pesel()
    print(pesel)
    print(type(pesel))
    print(len(pesel))
    return


# Generated at 2022-06-13 23:13:39.820917
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():

    p = PolandSpecProvider()
    pesel = p.pesel(birth_date=p.datetime(2000,2019),gender=Gender.MALE)
    #print(pesel)
    assert len(pesel) == 11


# Generated at 2022-06-13 23:13:45.852237
# Unit test for method pesel of class PolandSpecProvider
def test_PolandSpecProvider_pesel():
    # Given
    polandSpec = PolandSpecProvider(seed=1)
    gender = Gender.FEMALE

    # When
    result = polandSpec.pesel(gender=gender)

    # Then
    assert result == '94123001368'
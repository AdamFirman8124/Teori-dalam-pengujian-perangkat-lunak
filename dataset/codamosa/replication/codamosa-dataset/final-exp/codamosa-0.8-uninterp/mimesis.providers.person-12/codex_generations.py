

# Generated at 2022-06-14 00:36:30.156223
# Unit test for method username of class Person
def test_Person_username():
    p = Person()
    result = p.username()
    pattern = r'^[a-z]+\d+$'
    assert re.fullmatch(pattern, result) is not None



# Generated at 2022-06-14 00:36:35.589481
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Test for length
    nationality = Person().nationality(Gender.male)
    assert len(nationality) > 2
    
    # Test for type
    assert type(nationality) is str
    
    # Test for value
    assert nationality in NATIONALITIES
    

# Generated at 2022-06-14 00:36:38.608526
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    result = p.nationality()
    print(result)
    assert result in p._data['nationality']

# Generated at 2022-06-14 00:36:41.793909
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert 'Russian' == Person().nationality()


# Generated at 2022-06-14 00:36:44.823578
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person()
    title = p.gender()
    assert title in GENDERS


# Generated at 2022-06-14 00:36:59.716706
# Unit test for method gender of class Person
def test_Person_gender():
    print("Start test_Person_gender")
    person = Person(seed=0)
    assert person.gender() == "Woman"
    assert person.gender(symbol=True) == "♀"
    assert person.gender(iso5218=True) == 2
    assert person.gender(gender=Gender.FEMALE) == "Woman"
    assert person.gender(gender=Gender.FEMALE, symbol=True) == "♀"
    assert person.gender(gender=Gender.FEMALE, iso5218=True) == 2
    assert person.gender(gender=Gender.MALE) == "Man"
    assert person.gender(gender=Gender.MALE, symbol=True) == "♂"
    assert person.gender(gender=Gender.MALE, iso5218=True) == 1

# Generated at 2022-06-14 00:37:10.812405
# Unit test for method username of class Person
def test_Person_username():
    
    domain = '@example.com'
    template = 'l-dd'
    
    name = Person(seed=1).username(template)
    assert name == 's-18', name
    
    template = 'U.dd'
    name = Person(seed=1).username(template)
    assert name == 'A.18', name
    
    template = 'U_dd'
    name = Person(seed=1).username(template)
    assert name == 'A_18', name
    
    template = 'UU.dd'
    name = Person(seed=1).username(template)
    assert name == 'As.18', name
    
    template = 'UU_dd'
    name = Person(seed=1).username(template)
    assert name == 'As_18', name
    

# Generated at 2022-06-14 00:37:12.113595
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)

# Generated at 2022-06-14 00:37:15.187826
# Unit test for method gender of class Person
def test_Person_gender():
    '''
    Test_Person_gender() -> None
    '''
    person = Person()
    for _ in range(100):
        assert person.gender() in GENDER_LIST


# Generated at 2022-06-14 00:37:19.663050
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert len(person.nationality()) >= len(list(NATIONALITIES))


# Generated at 2022-06-14 00:37:29.010857
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert isinstance(p.surname(), str)


# Generated at 2022-06-14 00:37:31.509965
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person()
    # test for random value from enum Gender
    assert p.gender() in [item.name for item in Gender]



# Generated at 2022-06-14 00:37:36.625964
# Unit test for method gender of class Person
def test_Person_gender():
    rnd = Random()

    provider = Provider(rnd)

    gender = provider.gender()

    assert isinstance(gender, str)
    assert gender in ('Male', 'Female')


# Generated at 2022-06-14 00:37:38.832919
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = f.Person()
    assert isinstance(person.nationality(), str)

# Generated at 2022-06-14 00:37:41.892374
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in NATIONALITIES

# Generated at 2022-06-14 00:37:45.147446
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Capture the result of the function in a variable
    result = Person.nationality(Person)
    # Check that the function returns the expected output
    assert type(result) == str

test_Person_nationality()


# Generated at 2022-06-14 00:37:54.649457
# Unit test for method surname of class Person
def test_Person_surname():
    """Test method surname of class Person"""
    # Create object of class Person
    person = gramfuzz.field.Person()

    # Create list of test values

# Generated at 2022-06-14 00:37:56.170144
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(10):
        assert Person().nationality() in NATIONALITIES

# Generated at 2022-06-14 00:38:06.982028
# Unit test for method surname of class Person
def test_Person_surname():
    # If isinstance(surnames, list) or surnames is None, then this method
    # must return a random item from the surnames
    provider = KProvider()
    surname = provider.surname()
    assert surname in provider._data['surname']['male'] + \
                    provider._data['surname']['female']

    # If isinstance(surnames, dict), then this method must check the
    # validity of the gender parameter and return a random item from the
    # surnames list, specified gender key
    with pytest.raises(NonEnumerableError):
        provider.surname(gender='string')

    surname = provider.surname(gender=Gender.male)
    assert surname in provider._data['surname']['male']


# Generated at 2022-06-14 00:38:10.072624
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()

    for _ in range(10):
        surname = person.surname()
        assert surname in SURNAMES_RU, 'Surname is wrong.'



# Generated at 2022-06-14 00:38:19.914616
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Generated person
    person = Person(random=Random())

    # Test that person is not None
    assert person != None

# Test for method gender of class Person

# Generated at 2022-06-14 00:38:32.511312
# Unit test for method surname of class Person
def test_Person_surname():
    """Tests ``surnames`` method of ``Person`` class.
    """
    # Test default surname method.
    obj = Person('en')
    actual = obj.surname()
    assert isinstance(actual, str), repr(actual)

    # Test with gender
    for gender in Gender:
        actual = obj.surname(gender=gender)
        assert isinstance(actual, str), repr(actual)

    # Test with wrong gender
    with pytest.raises(NonEnumerableError):
        obj.surname(gender='male')

    # Test with incorrect gender
    with pytest.raises(NonEnumerableError):
        obj.surname(gender=1)

    # Test with incorrect gender
    with pytest.raises(NonEnumerableError):
        obj.surname(gender=3)

# Generated at 2022-06-14 00:38:36.919389
# Unit test for method gender of class Person
def test_Person_gender():
    from fake import random, SeedFactory
    gen = SeedFactory('Hello!')
    rnd = random.Random()
    rnd.seed_instance = gen
    provider = Person(rnd)
    for x in range(1000):
        assert provider.gender()

# Generated at 2022-06-14 00:38:46.171729
# Unit test for method surname of class Person
def test_Person_surname():
    def is_sname(sname, gender=None):
        return sname in Person._data['surname']

    # Assert that the surname generated using the Person.surname()
    # method is in the name list of the _data dict in the Person class
    try:
        assert is_sname(Person.surname(), Gender.male)
        assert is_sname(Person.surname(), Gender.female)
        assert is_sname(Person.surname(), Gender.unisex)
    except NonEnumerableError as e:
        print(e)



# Generated at 2022-06-14 00:38:51.197631
# Unit test for method email of class Person
def test_Person_email():
    """Test method email of class Person."""
    person = Person()
    email = person.email()

    assert isinstance(email, str)
    assert '@' in email



# Generated at 2022-06-14 00:38:56.238250
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(seed=12345)
    nationalities = []
    for i in range(100):
        nationalities.append(p.nationality(Gender.MALE))
    assert nationalities[:5] == ['Irish', 'Samoan', 'Malian', 'Korean', 'Malian']

    nationalities = []
    for i in range(100):
        nationalities.append(p.nationality(Gender.FEMALE))
    assert nationalities[:5] == ['Malian', 'Tunisian', 'Ivorian', 'Samoan', 'Mauritanian']


# Generated at 2022-06-14 00:38:59.044510
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert isinstance(p.surname(), str)
    assert p.surname() in SURNAMES


# Generated at 2022-06-14 00:39:02.885724
# Unit test for method gender of class Person
def test_Person_gender():
    result = Person().gender(symbol=True)
    assert isinstance(result, str) and len(result) == 1 or isinstance(result, int)

# Generated at 2022-06-14 00:39:06.913692
# Unit test for method surname of class Person
def test_Person_surname():
    # Test function with incorrect status
    with pytest.raises(NonEnumerableError):
        person = Person()
        person.surname(status=None)
        

# Generated at 2022-06-14 00:39:12.424069
# Unit test for method surname of class Person
def test_Person_surname():
    assert isinstance(Person().surname(), str)
    assert isinstance(Person().surname(Gender.male()), str)
    assert isinstance(Person().surname(Gender.female()), str)

# Generated at 2022-06-14 00:39:30.049967
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(random=Random())

    value = person.nationality()
    assert isinstance(value, str)

# Generated at 2022-06-14 00:39:32.356267
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Case when method returns a nationality
    assert isinstance(Person().nationality(), str)



# Generated at 2022-06-14 00:39:35.647539
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=0)
    assert person.nationality() == 'Russian'
    assert person.nationality(Gender.MALE) == 'Russian'
    assert person.nationality(Gender.FEMALE) == 'Russian'


# Generated at 2022-06-14 00:39:38.344326
# Unit test for method surname of class Person
def test_Person_surname():
    # Test with an empty dictionary
    provider = Person()
    surnames = provider._data['surname']
    surname = provider.surname()
    assert surname in surnames


# Generated at 2022-06-14 00:39:42.977253
# Unit test for method surname of class Person
def test_Person_surname():
    item = Person()
    assert isinstance(item.surname(), str)
    assert len(item.surname()) > 1


# Generated at 2022-06-14 00:39:47.340723
# Unit test for method gender of class Person
def test_Person_gender():
    for _ in range(10):
        assert Person().gender() in GENDERS


# Generated at 2022-06-14 00:39:55.048718
# Unit test for method gender of class Person
def test_Person_gender():
    person = Person(rnd=Random())
    
    for i in range(0, 100):
        assert person.gender() in PERSON_GENDER
    for i in range(0, 100):
        assert person.gender(True) in PERSON_GENDER_ISO5218
    for i in range(0, 100):
        assert person.gender(False, True) in PERSON_GENDER_SYMBOLS

# Generated at 2022-06-14 00:40:06.907585
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    f = p.nationality(Gender.FEMALE)
    m = p.nationality(Gender.MALE)
    n = p.nationality()
    assert (f in p.nationality(Gender.FEMALE)), f"{f} is not in {p.nationality(Gender.FEMALE)}"
    assert (m in p.nationality(Gender.MALE)), f"{m} is not in {p.nationality(Gender.MALE)}"
    assert (n in p.nationality(Gender.FEMALE)), f"{n} is not in {p.nationality(Gender.FEMALE)}"


# Generated at 2022-06-14 00:40:12.185951
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    random_nationality = person.nationality()
    assert random_nationality in person._data['nationality']

# Generated at 2022-06-14 00:40:15.408780
# Unit test for method nationality of class Person
def test_Person_nationality():
    for enum_object in Gender:
        name = Person().nationality(enum_object)
        assert isinstance(name, str)
        assert name


# Generated at 2022-06-14 00:40:43.893944
# Unit test for method email of class Person
def test_Person_email():
    """Test for method email of class Person."""

    def test_Person_email_with_domains():
        """Test email method with custom domains."""
        domains = ('gmail', 'hotmail', 'yahoo')
        email = Person.email(domains=domains)
        assert bool(re.match(r'[a-z0-9]+@gmail\.com', email))

    def test_Person_email_with_unique_flag():
        """Test email method with unique flag."""
        email = Person.email(unique=True)
        assert bool(re.match(r'[a-z0-9]+@gmail\.com', email))

    def test_Person_email_with_unique_flag_and_custom_domains():
        """Test email method with unique flag and custom domains."""

# Generated at 2022-06-14 00:40:46.230923
# Unit test for method nationality of class Person
def test_Person_nationality():
    r = Person()
    assert type(r.nationality()) == str

# Generated at 2022-06-14 00:40:49.622434
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person('en')
    result = person.nationality()
    print(result)
    assert result == 'American'
test_Person_nationality()


# Generated at 2022-06-14 00:40:53.745966
# Unit test for method surname of class Person
def test_Person_surname():
    # Create instance of class Person
    p = Person(seed=0)

    # Run method `surname` for class Person
    result = p.surname()

    # Result should be equal to "Иванов"
    assert result == "Иванов"
    
test_Person_surname()

# Generated at 2022-06-14 00:40:58.699068
# Unit test for method email of class Person
def test_Person_email():
    from datagenerator.generator.person import Person
    person = Person()
    expect_result = 'johann.wolfgang@gmail.com'
    result = person.email()
    assert result == expect_result


# Generated at 2022-06-14 00:41:04.101421
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    for i in range(100):
        assert person.email() == '_'.join(person.first_name().split()) + '.' + '_'.join(person.last_name().split()) + '@' + person.random.choice(EMAIL_DOMAINS)


# Generated at 2022-06-14 00:41:14.318637
# Unit test for method email of class Person
def test_Person_email():
    # It should generate a random email.
    # It should make email addresses unique.
    # It should raise a ValueError when «unique» is True and the provider was seeded.
    random = Random()
    person = Person(random)
    # email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    for _ in range(2):
        email = person.email()
        assert isinstance(email, str)
        assert len(email) > 5
    for _ in range(2):
        email = person.email(unique=True)
        assert isinstance(email, str)
        assert len(email) > 5

# Generated at 2022-06-14 00:41:28.892123
# Unit test for method surname of class Person
def test_Person_surname():
    pr = Person(seed=12345)
    assert pr.surname() == 'Медведев'
    assert pr.surname(gender=Gender.MALE) == 'Медведев'
    assert pr.surname(gender=Gender.FEMALE) == 'Иванова'
    assert pr.last_name() == 'Медведев'
    assert pr.last_name(gender=Gender.MALE) == 'Медведев'
    assert pr.last_name(gender=Gender.FEMALE) == 'Иванова'
    assert pr.surname(gender='FEMALE') == 'Иванова'

# Generated at 2022-06-14 00:41:36.158946
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed = 0)
    assert person.nationality(Gender.FEMALE) == 'Украинка'

if __name__ == '__main__':
    person = Person(seed = 0)
    print(person.nationality(Gender.FEMALE))
    test_Person_nationality()

# Класс Place содержит методы для генерации информации о разного рода локациях и местах.


# Generated at 2022-06-14 00:41:45.082633
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    # Surnames separated by gender.
    surnames = provider._data['surname']['male']
    assert isinstance(provider.surname(), str)
    assert provider.surname(Gender.FEMALE) in \
           provider._data['surname']['female']

# Generated at 2022-06-14 00:42:27.255072
# Unit test for method surname of class Person

# Generated at 2022-06-14 00:42:30.642509
# Unit test for method nationality of class Person
def test_Person_nationality():
    obj = Person()
    assert len(obj.nationality().split(' ')) < 2
    assert len(obj.nationality('male').split(' ')) < 2
    assert len(obj.nationality('female').split(' ')) < 2


# Generated at 2022-06-14 00:42:34.386265
# Unit test for method surname of class Person
def test_Person_surname():
    random = Random()

    assert isinstance(Person(random).surname(), str)



# Generated at 2022-06-14 00:42:41.554331
# Unit test for method nationality of class Person
def test_Person_nationality():
    obj = Person()

# Generated at 2022-06-14 00:42:48.847230
# Unit test for method surname of class Person
def test_Person_surname():
    # Check the generated surnames are in list of surnames
    list_surnames = person.surnames
    generated_surnames = []
    for _ in range(10000):
        generated_surnames.append(person.surname())
    assert all(surname in list_surnames for surname in generated_surnames)


# Generated at 2022-06-14 00:42:50.969727
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person('en')
    assert isinstance(person.nationality(), str)


# Generated at 2022-06-14 00:42:54.390579
# Unit test for method email of class Person
def test_Person_email():
    provider = Person()
    result = provider.email()
    assert result is not None and len(result) > 0


# Generated at 2022-06-14 00:43:01.696261
# Unit test for method surname of class Person
def test_Person_surname():
    person = PersonProvider(None)

    germany_male = person.surname(gender=Gender.male, nationalities=['Germany'])
    assert 'german' in germany_male.lower()
    assert 'ß' in germany_male
    assert germany_male.islower()
    assert germany_male[0].isupper()
    
    germany_female = person.surname(gender=Gender.female, nationalities=['Germany'])
    assert 'german' in germany_female.lower()
    

# Generated at 2022-06-14 00:43:05.666176
# Unit test for method nationality of class Person
def test_Person_nationality():

    assert(Person().nationality() == 'Russian' or 'British' or 'German' or 'Slovene' or 'Estonian')


# Generated at 2022-06-14 00:43:08.826839
# Unit test for method surname of class Person
def test_Person_surname():
    name = Person().surname()
    assert type(name) == str


# Generated at 2022-06-14 00:43:53.076806
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Test with None gender
    p1 = Person()
    nationality1 = p1.nationality()
    assert nationality1 in NATIONALITIES

    # Test with Gender.MALE
    p2 = Person()
    nationality2 = p2.nationality(gender=Gender.MALE)
    assert nationality2 in NATIONALITIES_MALE

    # Test with Gender.FEMALE
    p3 = Person()
    nationality3 = p3.nationality(gender=Gender.FEMALE)
    assert nationality3 in NATIONALITIES_FEMALE

    # Test with incorrect value
    p4 = Person()
    with raises(NonEnumerableError):
        p4.nationality('w')
        
test_Person_nationality()


# Generated at 2022-06-14 00:44:03.944878
# Unit test for method surname of class Person
def test_Person_surname():
    """Test of the method surname() of class Person"""
    my_person = Person()
    my_surname = my_person.surname()
    # test that the surname is of the correct type
    assert type(my_surname) is str
    print('Surname is of the correct type')
    
    # test that the surname is not empty
    assert (my_surname != '')
    print('Surname is not empty')
    

# Generated at 2022-06-14 00:44:07.211294
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=1)
    assert person.nationality() == 'Australian'
    assert person.nationality(gender=Gender.male) == 'Japanese'
    assert person.nationality(gender=Gender.female) == 'New Zealand'

# Generated at 2022-06-14 00:44:11.694841
# Unit test for method surname of class Person
def test_Person_surname():
    r = random.choice(Person().surname())
    assert(r)


# Generated at 2022-06-14 00:44:14.903589
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    for i in range(10):
        assert 1 <= len(person.nationality()) <= 50

# Generated at 2022-06-14 00:44:22.346248
# Unit test for method nationality of class Person
def test_Person_nationality():
    test_success = 0
    test_failed = 0
    p = Person()
    for _ in range(10):
        if p.nationality():
            test_success += 1
        else:
            test_failed += 1
    print('Success: {0}, Failed: {1}'.format(test_success, test_failed))
# Run
test_Person_nationality()


# Generated at 2022-06-14 00:44:24.287785
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person('ru')
    assert person.nationality() == 'Russian'
    assert person.nationality() == 'Russian'



# Generated at 2022-06-14 00:44:26.242062
# Unit test for method nationality of class Person
def test_Person_nationality():
    r = Person()
    args = ('',)
    kwargs = {}
    assert r.nationality(*args, **kwargs) == 'American'


# Generated at 2022-06-14 00:44:30.210937
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert isinstance(p.surname(), str)



# Generated at 2022-06-14 00:44:33.203382
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person('en_GB')
    assert provider.surname() in SURNAME_LIST


# Generated at 2022-06-14 00:45:11.270409
# Unit test for method surname of class Person
def test_Person_surname():
    random = Random()
    p = Person(random=random)
    assert type(p.surname()) is str

# Generated at 2022-06-14 00:45:24.097151
# Unit test for method nationality of class Person
def test_Person_nationality():
    def test_Person_nationality_001():
        person_1 = Person()
        person_1.seed(0)
        nationality_1 = person_1.nationality()
        expected_1 = "Chinese"
        assert nationality_1 == expected_1
        print("Test #1 for method nationality of class Person - Passed")

    def test_Person_nationality_002():
        person_1 = Person()
        person_1.seed(1)
        nationality_1 = person_1.nationality()
        expected_1 = "Italian"
        assert nationality_1 == expected_1
        print("Test #2 for method nationality of class Person - Passed")

    def test_Person_nationality_003():
        person_1 = Person()
        person_1.seed(2)
        nationality_1 = person_1.nationality()


# Generated at 2022-06-14 00:45:32.502164
# Unit test for method surname of class Person
def test_Person_surname():
    # case 1
    person = Person()

# Generated at 2022-06-14 00:45:41.919187
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    result = p.surname()
    assert result in p._data['surname']
    result = p.surname(gender=Gender.male)
    assert result in p._data['surname']['male']
    result = p.surname(gender=Gender.female)
    assert result in p._data['surname']['female']


# Generated at 2022-06-14 00:45:42.610543
# Unit test for method surname of class Person
def test_Person_surname():
    pass

# Generated at 2022-06-14 00:45:45.196575
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    print(nationality)

    assert nationality
    assert type(nationality) == str


# Generated at 2022-06-14 00:45:50.258459
# Unit test for method nationality of class Person
def test_Person_nationality():
    import random
    person = Person(random.Random(0))
    assert person.nationality().lower() == "finnish"
    assert issubclass(person.nationality.__class__, str)
    assert issubclass(person.nationality(Gender.FEMALE).__class__, str)
    assert issubclass(person.nationality(Gender.MALE).__class__, str)

# Generated at 2022-06-14 00:45:54.365187
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person('en')
    print(person.nationality(Gender.MALE))
    print(person.nationality(Gender.FEMALE))
    print(person.nationality())

test_Person_nationality()


# Generated at 2022-06-14 00:45:57.026444
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname(Gender.FEMALE)
    assert surname == 'Нестерова'
    

# Generated at 2022-06-14 00:45:59.714791
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert type(p.nationality()) == str
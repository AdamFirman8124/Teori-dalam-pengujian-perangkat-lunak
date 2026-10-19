

# Generated at 2022-06-14 00:36:31.369896
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    assert re.match(r'[a-zA-Z0-9_-]+@\w+\.\w+', p.email())

# Generated at 2022-06-14 00:36:34.819514
# Unit test for method surname of class Person
def test_Person_surname():
    Person_ = Person(seed=None)
    surname = ''
    assert isinstance(Person_.surname(), str)
    assert Personsurname is not None


# Generated at 2022-06-14 00:36:39.136898
# Unit test for method email of class Person
def test_Person_email():

    # Arrange
    provider = Person()
    # Act
    email = provider.email()
    # Assert
    assert re.match(r'.+@.+', email), 'Email is invalid'

# Generated at 2022-06-14 00:36:41.566281
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person.nationality(Person(), gender=Gender.MALE) == 'Russian'


# Generated at 2022-06-14 00:36:44.674608
# Unit test for method surname of class Person
def test_Person_surname():
       nameGenerator = Person()
       assert nameGenerator.surname() in SURNAMES

# Generated at 2022-06-14 00:36:53.246311
# Unit test for method email of class Person
def test_Person_email():
    """
    Test for method email of class Person
    """
    person = Person()
    count = 0
    while count < 100:
        assert isinstance(person.email(), str)
        assert re.fullmatch(r'[a-z0-9.\-_]+@[a-z0-9.\-_]+', person.email())
        assert person.email() == person.email(unique=True)
        count += 1

# Generated at 2022-06-14 00:36:55.984735
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert surname in SURNAME


# Generated at 2022-06-14 00:37:02.692740
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert isinstance(Person.nationality(), str)
    assert Person.nationality() in PERSON_NATIONALITIES
    assert Person.nationality(Gender.MALE) in PERSON_NATIONALITIES
    assert Person.nationality(Gender.FEMALE) in PERSON_NATIONALITIES
    
    
    

# Generated at 2022-06-14 00:37:05.151057
# Unit test for method nationality of class Person
def test_Person_nationality():
    PL = Person(localization="pl_PL")
    assert isinstance(PL.nationality(), str)


# Generated at 2022-06-14 00:37:11.820980
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()

    nationalities = person.get_data('nationality')

    for _ in range(100):
        nationality = person.nationality()
        assert nationality in nationalities

    nationalities = person.get_data('nationality')['male']
    for _ in range(100):
        nationality = person.nationality(gender='male')
        assert nationality in nationalities

    nationalities = person.get_data('nationality')['female']
    for _ in range(100):
        nationality = person.nationality(gender='female')
        assert nationality in nationalities

# Generated at 2022-06-14 00:37:28.515084
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person('ru_RU')
    assert isinstance(p.surname(Gender.MALE), str)


# Generated at 2022-06-14 00:37:29.810016
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() != 'Russian'

# Generated at 2022-06-14 00:37:30.850346
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert callable(Person.nationality)


# Generated at 2022-06-14 00:37:32.845538
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationalities = person._data['nationality']

    assert person.nationality() in nationalities

# Generated at 2022-06-14 00:37:37.999184
# Unit test for method surname of class Person
def test_Person_surname():
	assert Person().surname() == 'Buckley'
	assert Person().surname(gender='male') == 'Dunn'
	assert Person().surname(gender='female') == 'Ford'

# Generated at 2022-06-14 00:37:42.101354
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surnames = person.surname()
    print(surnames)


# Generated at 2022-06-14 00:37:44.673507
# Unit test for method email of class Person
def test_Person_email():
    assert Person().email()
    assert Person().email(unique=True)
    assert Person().email(unique=True, domains=('test.com', 'some.com'))


# Generated at 2022-06-14 00:37:52.483284
# Unit test for method nationality of class Person
def test_Person_nationality():
    '''
    :Description:
        This unit test will test if the random nationality is in the list of nationalities in the data.py file
    :Returns:
        True if the nationality returned is in the list of nationalities
    :Raise:
        AssertionError if the nationality is not in the list of nationalities
    '''
    random_nationality = Person().nationality()
    assert random_nationality in NATIONALITY


# Generated at 2022-06-14 00:38:02.305909
# Unit test for method surname of class Person
def test_Person_surname():
    from random import Random
    from faker import Faker
    from faker.providers.person.en_AZ import Provider as PersonProvider

    fake = Faker()
    fake.add_provider(PersonProvider)

    random_obj = Random()
    random_obj.seed(0)
    fake.random = random_obj

    def test_surname_None():
        assert fake.surname() == 'Hacıqulu'
        assert fake.surname(gender=Gender.FEMALE) == 'Qarayeva'
        assert fake.surname(gender=Gender.MALE) == 'Hacıqulu'


# Generated at 2022-06-14 00:38:07.661534
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()

    nationalities = person.nationalities

    for nationality in nationalities:
        res = person.nationality()
        assert isinstance(res, str)
        assert res in nationalities

# Generated at 2022-06-14 00:38:25.914684
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker_ru import constants as constants
    
    # Test 1. Default parameters.
    person = Person()
    assert person.nationality() in constants.NATIONALITIES
    
    # Test 2. Use specified gender.
    gender = Gender.FEMALE
    nationality = person.nationality(gender=gender)
    assert nationality in constants.NATIONALITIES_FEMALE
    
    # Test 3. Use incorrect gender.
    gender = 'a'
    try:
        nationality = person.nationality(gender=gender)
    except NonEnumerableError:
        pass
    else:
        assert False, "ValueError не вызван"


# Generated at 2022-06-14 00:38:29.491266
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    nationality = p.nationality()
    assert(isinstance(nationality, str))


# Generated at 2022-06-14 00:38:32.153044
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert isinstance(p.surname(), str)



# Generated at 2022-06-14 00:38:38.956045
# Unit test for method nationality of class Person
def test_Person_nationality():
    nationalities = Person.nationality()
    assert isinstance(nationalities, tuple)
    assert len(nationalities) == 29
    # Test for method nationality of class Person
    def test_Person_nationality():
        nationalities = Person.nationality()
        assert isinstance(nationalities, tuple)
        assert len(nationalities) == 29


# Generated at 2022-06-14 00:38:41.639922
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in ('French', 'American', 'Chinese')

# Generated at 2022-06-14 00:38:47.436265
# Unit test for method email of class Person
def test_Person_email():
     
    assert Person().email() == 'c.taylor@live.com'
    assert Person().email() != 'm@example.com'
    
    
    
    
    

test_Person_email()

# Generated at 2022-06-14 00:38:51.075289
# Unit test for method surname of class Person
def test_Person_surname():
    person_obj1 = Person(seed=0)
    assert person_obj1.surname() == 'Cannon'
    person_obj2 = Person(seed=0)
    assert person_obj2.surname() == 'Cannon'

# Generated at 2022-06-14 00:38:54.575419
# Unit test for method nationality of class Person
def test_Person_nationality():
    data = [x for x in range(10000)]
    for i in data:
        p = Person()
        p.nationality()


# Generated at 2022-06-14 00:38:56.237924
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname()

# Generated at 2022-06-14 00:38:58.612673
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    surname = p.surname()
    assert isinstance(surname, str)

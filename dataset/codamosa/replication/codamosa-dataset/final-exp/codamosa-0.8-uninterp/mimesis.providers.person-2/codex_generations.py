

# Generated at 2022-06-14 00:36:28.219160
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Unit test for method nationality of class Person"""
    provider = Person(
        random=Random(),
        locale='ru'
    )
    country = provider.nationality()
    assert country in LOCALES.get('ru').get('nationality')

# Generated at 2022-06-14 00:36:32.572633
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    
    choice1 = person.nationality()
    choice2 = person.nationality()
    try:
        assert choice1 != choice2
    except AssertionError:
        pass

# Generated at 2022-06-14 00:36:34.003826
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    print(person.surname())

# Generated at 2022-06-14 00:36:35.933156
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert isinstance(person.nationality(), str) # ==> True
    print('Done!!!')

# Generated at 2022-06-14 00:36:38.537876
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    for _ in range(10):
        person.nationality()


# Generated at 2022-06-14 00:36:41.754721
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    result = p.email()

# Generated at 2022-06-14 00:36:45.883223
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Test method nationality of class Person."""
    person = Person()
    result = person.nationality()

    assert result == 'Russian'
    assert isinstance(result, str)


# Generated at 2022-06-14 00:36:50.365393
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Arrange
    person = Person()
    nationality = person.nationality()
    # Assert
    assert type(nationality) == str and nationality != ''

# Generated at 2022-06-14 00:36:54.003509
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in NATIONALITY, "The method nationality has error at {0}".format(person.nationality())


# Generated at 2022-06-14 00:36:57.798473
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert type(nationality) == str
    assert nationality in person._data.get("nationality")


# Generated at 2022-06-14 00:37:11.971284
# Unit test for method surname of class Person
def test_Person_surname():
    test_list = ["O'Sullivan", "Pérez", "Suárez", "Zhong", "Østby", "Łukasik", "Şahin", "Šuranova", "Ṣààdé",
             "Fischer", "Larsen", "Jensen", "Barber", "Hanson", "Nguyen"]
    P1 = Person(locale='en')
    result_list = []
    for i in range(10):
        result_list.append(P1.surname())
    assert(len(result_list)==10)
    assert(False not in [True if each in test_list else False for each in result_list])
    
    

# Generated at 2022-06-14 00:37:19.152459
# Unit test for method email of class Person
def test_Person_email():
    # Test with None value of argument
    with pytest.raises(AttributeError) as excinfo:
        random_item(Person(seed=None).email())

    # Test with list of custom domains for emails
    assert len(random_item(Person(seed=None).email(domains=["gmail.com"]))) > len(random_item(Person(seed=None).email()))

    # Test with value True for argument unique
    assert len(random_item(Person(seed=None).email(unique=True))) > len(random_item(Person(seed=None).email()))
 

# Generated at 2022-06-14 00:37:29.203079
# Unit test for method surname of class Person
def test_Person_surname():
    m = Person()
    #print(m.surname())
    #print(m.last_name())
    #print(m.title())
    #print(m.full_name())
    #print(m.username())
    #print(m.password())
    #print(m.email())
    #print(m.social_media_profile())
    #print(m.gender())
    #print(m.sex())
    #print(m.height())
    #print(m.weight())
    #print(m.blood_type())
    #print(m.sexual_orientation())
    #print(m.occupation())
    #print(m.political_views())
    #print(m.worldview())
    #print(m.views_on())
    #print(m.nationality())


# Generated at 2022-06-14 00:37:32.450583
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname(gender=Gender.female)
    with pytest.raises(NonEnumerableError):
        p.surname(gender='qwerty')



# Generated at 2022-06-14 00:37:36.317299
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person()
    assert p.random.choice(p._data['gender']) == p.gender()


# Generated at 2022-06-14 00:37:39.399492
# Unit test for method email of class Person
def test_Person_email():
    try:
        Person(seed=42).email(unique=True)
    except ValueError:
        pass
    else:
        assert False



# Generated at 2022-06-14 00:37:42.435415
# Unit test for method gender of class Person
def test_Person_gender():
    for i in range(100):
        assert Person.gender().isalpha()  # Method gender of class Person returns strings only



# Generated at 2022-06-14 00:37:46.612945
# Unit test for method gender of class Person
def test_Person_gender():
    provider = Faker.Faker()
    result = provider.gender()
    assert type(result) == str
    result = provider.gender(symbol=True)
    assert result in GENDER_SYMBOLS
    result = provider.gender(iso5218=True)
    assert type(result) == int
    assert result in [0, 1, 2, 9]


# Generated at 2022-06-14 00:37:58.723127
# Unit test for method nationality of class Person

# Generated at 2022-06-14 00:38:08.386648
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Name of method or class 
    string_example = r'Person.nationality(gender: Gender = None) -> str'
    # Expected result of unit test
    result = 'Russian'
    # Run a unit test
    assert isinstance(result, str) and len(result) > 0, \
        f"Expected {string_example} to be a string and return not empty string, got {result}"
    
    string_example = r'Person.nationality(gender: Gender = None) -> str'
    result = 'Russian'
    assert isinstance(result, str) and len(result) > 0, \
        f"Expected {string_example} to be a string and return not empty string, got {result}"
    
    string_example = r'Person.nationality(gender: Gender = None) -> str'
    result

# Generated at 2022-06-14 00:38:32.535536
# Unit test for method nationality of class Person
def test_Person_nationality():
    
    person = Person()
    nationality = person.nationality()
    assert nationality in person._data['nationality']
    
    nationality = person.nationality('male')
    assert nationality in person._data['nationality']['male']
    
    nationality = person.nationality('female')
    assert nationality in person._data['nationality']['female']
    
    nationality = person.nationality(gender=None)
    assert nationality in person._data['nationality']
    
    nationality = person.nationality(gender=Gender.MALE)
    assert nationality in person._data['nationality'][Gender.MALE.value]
    
    nationality = person.nationality(gender=Gender.FEMALE)
    assert nationality in person._data['nationality'][Gender.FEMALE.value]

# Generated at 2022-06-14 00:38:34.751598
# Unit test for method gender of class Person
def test_Person_gender():
    gender = Person('en').gender()
    assert gender in ('Male', 'Female')


# Generated at 2022-06-14 00:38:36.721327
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert isinstance(p.nationality(), str)

# Generated at 2022-06-14 00:38:40.895184
# Unit test for method email of class Person
def test_Person_email():
    
    # Generate a set of random emails
    emails = [Person.email() for _ in range(100)]

    # Check if addresses are unique
    assert len(set(emails)) == len(emails)  # All emails are unique

# Generated at 2022-06-14 00:38:44.631633
# Unit test for method username of class Person
def test_Person_username():
    # Arrange
    person = Person()

    # Act
    result = person.username()

    # Assert
    assert isinstance(result, str)


# Generated at 2022-06-14 00:38:47.954347
# Unit test for method nationality of class Person
def test_Person_nationality():
    try:
        for i in range(1000):
            s = Person().nationality()
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-14 00:38:58.652095
# Unit test for method gender of class Person
def test_Person_gender():
    from datagen import Person
    from datagen._compat import xrange, next
    from datagen.enum import Gender

    provider = Person()

    # Test default values
    for _ in xrange(100):
        gender = provider.gender()
        assert isinstance(gender, str)
        assert gender in provider._data['gender']

    # Test iso5218 flag
    for _ in xrange(100):
        gender = provider.gender(iso5218=True)
        assert isinstance(gender, int)
        assert gender in (0, 1, 2, 9)

    # Test symbol flag
    male = provider.gender(symbol=True)
    assert isinstance(male, str)
    assert len(male) == 1
    assert male in Gender.get_all_symbols()

    # Test different genders

# Generated at 2022-06-14 00:39:00.202466
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    val = p.surname()
    assert isinstance(val, str)



# Generated at 2022-06-14 00:39:05.989596
# Unit test for method surname of class Person
def test_Person_surname():
    pes = Person()
    surname = pes.surname(Gender.Female)
    assert isinstance(surname, str)
    assert surname != ''
    assert surname.strip()
    assert surname[0].isupper()

# Generated at 2022-06-14 00:39:11.644974
# Unit test for method surname of class Person
def test_Person_surname():
    # Arrange
    p = Person()

    # Act
    actual = p.surname()

    # Assert
    assert actual in SURNAMES


# Generated at 2022-06-14 00:39:34.002725
# Unit test for method surname of class Person
def test_Person_surname():
    # Test with random seed
    provider = Person(seed=8233101018)
    assert provider.surname(Gender.MALE) == 'Kovac'

    # Test with specific seed
    provider = Person(seed=8233101018)
    assert provider.surname(Gender.MALE) == 'Kovac'

    # Test exception
    provider = Person(seed=8233101018)
    with pytest.raises(NonEnumerableError):
        provider.surname(Gender.UNKNOWN)


# Generated at 2022-06-14 00:39:35.733172
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert person.surname() in person._surnames



# Generated at 2022-06-14 00:39:36.729983
# Unit test for method gender of class Person
def test_Person_gender():
    assert Person().gender() in GENDER

# Generated at 2022-06-14 00:39:38.339220
# Unit test for method nationality of class Person
def test_Person_nationality():
    for i in range(10):
        assert isinstance(Person().nationality(), str)



# Generated at 2022-06-14 00:39:50.731566
# Unit test for method surname of class Person
def test_Person_surname():
    # Test 1
    surname = Person.surname(Gender.MALE)
    assert surname == "Иванов"
    # Test 2
    surname = Person.surname(Gender.FEMALE)
    assert surname == "Андреева"
    # Test 3
    surname = Person.surname(Gender.DIVERSE)
    assert surname == "Перцов"
    # Test 4
    surname = Person.surname(Gender.ANDROGYNOUS)
    assert surname == "Мамаев"
    # Test 5
    surname = Person.surname(Gender.UNKNOWN)
    assert surname == "Кириллова"

# Generated at 2022-06-14 00:39:54.007558
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in PERSON_NATIONALITIES


# Generated at 2022-06-14 00:40:06.907073
# Unit test for method surname of class Person
def test_Person_surname():
    surname = Person.surname(Gender.MALE)
    print(surname)
    assert surname in PERSON_MALE_SURNAMES
    
    surname = Person.surname(Gender.FEMALE)
    print(surname)
    assert surname in PERSON_FEMALE_SURNAMES
    
    surname = Person.surname(Gender.NOT_APPLICABLE)
    print(surname)
    assert surname in PERSON_GENDER_NOT_APPLICABLE_SURNAMES

# Generated at 2022-06-14 00:40:14.963520
# Unit test for method surname of class Person
def test_Person_surname():
    from faker import Faker
    fake = Faker()
    fake.seed(0)
    assert fake.surname(Gender.MALE) == 'Watson'
    fake.seed(1)
    assert fake.surname(Gender.FEMALE) == 'Flores'


# Generated at 2022-06-14 00:40:20.682527
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person()
    assert type(p.gender(iso5218=True)) == int

    for gender in [0, 1, 2, 9]:
        assert gender in [0, 1, 2, 9]

# Generated at 2022-06-14 00:40:31.633440
# Unit test for method email of class Person
def test_Person_email():
    cases = [
        {
            'seed': None,
            'domains': None,
            'unique': True,
            'result': 'k-5x@gmail.com',
        },
        {
            'seed': None,
            'domains': ('yandex.ru',),
            'unique': True,
            'result': 'i-7t@yandex.ru',
        },
    ]

    for case in cases:
        person = Person(seed=case['seed'])
        email_ = person.email(
            domains=case['domains'],
            unique=case['unique'],
        )
        assert email_ == case['result'], 'Expected is "{}", but got "{}"'.format(case['result'], email_)


# Generated at 2022-06-14 00:41:04.640663
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    name_list = ['Hernandez', 'Erikson', 'Hunt', 'Pearson', 'Faulkner']
    for _ in range(25):
        surname = person.surname()
        assert isinstance(surname, str)
        assert surname in name_list


# Generated at 2022-06-14 00:41:09.862275
# Unit test for method email of class Person
def test_Person_email():
    name = 'test_Person_email'
    person = Person(name=name)
    
    result = person.email()
    print(name + ': ' + result)

    assert result is not None


# Generated at 2022-06-14 00:41:11.717541
# Unit test for method gender of class Person
def test_Person_gender():
    """
    it should return a random gender for Person
    """
    assert type(Person().gender(symbol=True)) == str


# Generated at 2022-06-14 00:41:15.990518
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person('uk')
    assert type(person.nationality()) == str
test_Person_nationality()

# Generated at 2022-06-14 00:41:21.534691
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname(gender=Gender.MALE) in SURNAMES[Gender.MALE]
    assert Person.surname(gender=Gender.FEMALE) in SURNAMES[Gender.FEMALE]

# Generated at 2022-06-14 00:41:27.466915
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    counter = {}
    for _ in range(1000):
        surname = p.surname()
        counter[surname] = counter.get(surname, 0) + 1
    assert len(counter) > 1

# Generated at 2022-06-14 00:41:32.975853
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Testing only the countries that have "common" gender
    # greek, georgian and polish
    assert Person().nationality() in ['greek', 'georgian', "polish"]

# Generated at 2022-06-14 00:41:43.179288
# Unit test for method surname of class Person
def test_Person_surname():
    def test_1(Person):
        assert Person.surname()

    def test_2(Person):
        assert Person.surname(Gender.MALE)

    def test_3(Person):
        assert Person.surname(Gender.FEMALE)

    def test_4(Person):
        with pytest.raises(NonEnumerableError):
            Person.surname('female')

    def test_5(Person):
        with pytest.raises(NonEnumerableError):
            Person.surname('male')

    # Execute functions
    for function in (test_1, test_2, test_3,
                     test_4, test_5):
        function(Person())

# Generated at 2022-06-14 00:41:52.961152
# Unit test for method nationality of class Person
def test_Person_nationality():
    #
    from fake_factory.providers import BaseProvider
    from fake_factory.providers.person.en_US import Provider as PersonEnProvider
    #
    # Initialize the provider for English
    eng_provider = PersonEnProvider(BaseProvider())
    # Get a random nationality for English
    nationality_eng = eng_provider.nationality()
    # Check the nationality
    assert isinstance(nationality_eng, str), 'Not a string object'
    assert nationality_eng != '', 'Empty string object'

###

# Generated at 2022-06-14 00:41:57.285994
# Unit test for method surname of class Person
def test_Person_surname():
    import unittest
    class TestSurname(unittest.TestCase):
        def test_return_type(self):
            a = Person().surname()
            self.assertIsInstance(a, str)
        def test_return_value(self):
            a = Person().surname()
            self.assertIn(a, SURNAME)

    unittest.main()


# Generated at 2022-06-14 00:42:26.076770
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Checks for value
    assert isinstance(Person().nationality(), str)

# Generated at 2022-06-14 00:42:29.755775
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert re.match("^[a-z]+( [a-z]+)?$", person.surname())

test_Person_surname()

# Generated at 2022-06-14 00:42:40.540201
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()

    # Make sure that all nationalities are unique in list
    assert len(person._data['nationality']) == len(set(person._data['nationality']))

    # Make sure that Russian is in list
    assert 'Russian' in person._data['nationality']

    # Make sure that nationality() is always in nationalities
    assert person.nationality() in person._data['nationality']

    # Make sure that nationalities are case sensitive
    assert 'russian' not in person._data['nationality']

    # Make sure that nationalities are separated by gender
    assert 'Male' in person._data['nationality']['Male']
    assert 'Female' in person._data['nationality']['Female']

    # Make sure that nationalities of both genders are unique

# Generated at 2022-06-14 00:42:42.375981
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname() in SURNAMES


# Generated at 2022-06-14 00:42:44.935632
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITIES


# Generated at 2022-06-14 00:42:48.800236
# Unit test for method surname of class Person
def test_Person_surname():
    name = Person().surname(Gender.MALE)
    assert name is not None


# Generated at 2022-06-14 00:42:51.491493
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    assert(p.email(['test@test.com']) == 'test@test.com'), 'This is not a proper email'


# Generated at 2022-06-14 00:42:54.973658
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person()
    assert provider.nationality() in provider._data['nationality']


# Generated at 2022-06-14 00:42:58.518279
# Unit test for method surname of class Person
def test_Person_surname():
    assert len(Person().surname()) > 0
    assert len(Person().surname(Gender.MALE)) > 0
    assert len(Person().surname(Gender.FEMALE)) > 0



# Generated at 2022-06-14 00:43:01.630964
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    print(provider.surname())

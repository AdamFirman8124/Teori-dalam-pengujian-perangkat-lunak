

# Generated at 2022-06-14 00:36:29.359147
# Unit test for method email of class Person
def test_Person_email():
    provider = Person()
    for _ in range(100):
        email = provider.email()
        assert email.count('@') == 1
        assert email.split('@')[0].isalpha()
        assert email.split('@')[1].isalpha()
        assert len(email.split('@')[1].split('.')) == 2

# Generated at 2022-06-14 00:36:34.562785
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    p1 = p.surname(Gender.MALE)
    assert p1.startswith('Иванов')
    p2 = p.surname(Gender.FEMALE)
    assert p2.startswith('Иванова')
    p3 = p.surname()
    assert p3 in ('Иванов', 'Иванова')
    p4 = p.last_name()
    assert p3 == p4
    p5 = p.surname(gender = 'МУЖСКОЙ')
    assert p5.startswith('Иванов')

# Generated at 2022-06-14 00:36:37.124093
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=10)
    assert person.surname() == 'Bass'


# Generated at 2022-06-14 00:36:42.447629
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert isinstance(nationality, str)
    assert nationality in PERSON_NATIONALITY



# Generated at 2022-06-14 00:36:44.732942
# Unit test for method gender of class Person
def test_Person_gender():
    from fake import fake
    assert fake.gender() == 'Female'


# Generated at 2022-06-14 00:36:48.003107
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(random=MockRandom())
    assert p.nationality() == 'Russian'


# Generated at 2022-06-14 00:36:51.862008
# Unit test for method email of class Person
def test_Person_email():
    from tests.tools import assert_call
    from faker_ru.providers import Person

    p = Person()
    assert_call(p.email, 'Wong_87@vivaldi.com')


# Generated at 2022-06-14 00:36:57.028886
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname('MALE') == 'Козлов'
    
if __name__ == '__main__':
    test_Person_surname()
    print('All tests successful')
 


# Generated at 2022-06-14 00:37:03.351722
# Unit test for method gender of class Person
def test_Person_gender():
    person = Person()
    assert person.gender() in GENDER_TITLES
    assert person.gender(symbol=True) in GENDER_SYMBOLS
    assert person.gender(iso5218=True) in [0, 1, 2, 9]

# Generated at 2022-06-14 00:37:05.951135
# Unit test for method surname of class Person
def test_Person_surname():
    data = Person().surname()
    assert isinstance(data, str) == True
test_Person_surname()

# Generated at 2022-06-14 00:37:17.837074
# Unit test for method surname of class Person
def test_Person_surname():
    surname1 = Person().surname()
    assert isinstance(surname1, str)

    surname2 = Person().surname(Gender.MALE)
    assert isinstance(surname2, str)

    surname3 = Person().surname(Gender.FEMALE)
    assert isinstance(surname3, str)

# Generated at 2022-06-14 00:37:19.507667
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person()
    print(provider.nationality(gender=Gender.MALE))


# Generated at 2022-06-14 00:37:22.082402
# Unit test for method nationality of class Person
def test_Person_nationality():
    person=Person()
    assert isinstance(person.nationality(),str)

if __name__ == '__main__':
    test_Person_nationality()

# Generated at 2022-06-14 00:37:24.548714
# Unit test for method surname of class Person
def test_Person_surname():
    generator = Person()
    generator.seed(2)
    assert generator.surname() == 'Smith'

# Generated at 2022-06-14 00:37:28.231318
# Unit test for method nationality of class Person
def test_Person_nationality():
    with Person:
        result = Person.nationality()
        assert type(result) == str

# Generated at 2022-06-14 00:37:36.991586
# Unit test for method surname of class Person
def test_Person_surname():
    # Tests of the method surname
    # on the class Person with the default value of parameter
    person = Person()
    assert person.surname() in person._data['last_names']
    person = Person(name="Ivan")
    assert person.surname() in person._data['last_names']
    # Tests of the method surname
    # on the class Person with the value of parameter
    person = Person(name="Ivan", gender=Gender.MALE)
    assert isinstance(person.surname(), str)
    assert person.surname() in person._data['last_names']['m']
    person = Person(name="Ivan", gender=Gender.FEMALE)
    assert isinstance(person.surname(), str)

# Generated at 2022-06-14 00:37:42.895864
# Unit test for method nationality of class Person
def test_Person_nationality():
    for item in [None, Gender.MALE, Gender.FEMALE, 'Not a Gender class']:
        if item is None or item == Gender.MALE or item == Gender.FEMALE:
            assert type(Person().nationality(item)) == str
        elif item == 'Not a Gender class':
            with pytest.raises(NonEnumerableError):
                Person().nationality(item)


# Generated at 2022-06-14 00:37:45.558998
# Unit test for method email of class Person
def test_Person_email():
    assert len(Person().email()) > 0
    assert len(Person().email(unique=True)) > 0
    assert len(Person().email(domains=('gmail.com',))) > 0

# Generated at 2022-06-14 00:37:49.140437
# Unit test for method surname of class Person
def test_Person_surname():
    with pytest.raises(NonEnumerableError):
        person = Person(5)

# Generated at 2022-06-14 00:37:52.349054
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(locales=(Locales.ENGLISH,))
    nationality = person.nationality()
    assert nationality in person._data["nationality"]

# Generated at 2022-06-14 00:37:58.331336
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person('en')
    surname = person.surname()
    print(surname)

# Generated at 2022-06-14 00:38:03.141714
# Unit test for method email of class Person
def test_Person_email():
    for i in range(100):
        assert isinstance(Person().email(), str)


# Generated at 2022-06-14 00:38:15.102501
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person(provider_locale='ru')
    assert p.surname()
    assert p.surname(Gender.MALE) == 'Петров'
    assert p.surname(Gender.FEMALE) == 'Константинопольская'

    p = Person(provider_locale='en')
    assert p.surname()
    assert p.surname(Gender.MALE) == 'Smith'
    assert p.surname(Gender.FEMALE) == 'Johnson'

    p = Person(provider_locale='uk')
    assert p.surname()
    assert p.surname(Gender.MALE) == 'Петренко'
    assert p.s

# Generated at 2022-06-14 00:38:17.269579
# Unit test for method email of class Person
def test_Person_email():
    email = Person.generator().email()
    assert isinstance(email, str) and email.count('@') == 1

# Generated at 2022-06-14 00:38:19.961958
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert person.surname() in person._data['surname'], "Error on Person.surname method"


# Generated at 2022-06-14 00:38:22.301116
# Unit test for method surname of class Person
def test_Person_surname():
    """Unit test for method surname of class Person."""

    person = Person()
    surname = person.surname()
    assert surname in SURNAMES



# Generated at 2022-06-14 00:38:24.962555
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surnames = [person.surname() for _ in range(100)]
    
    assert surnames
    assert type(surnames[0]) is str
    assert len(set(surnames)) > 1

# Generated at 2022-06-14 00:38:31.266145
# Unit test for method email of class Person
def test_Person_email():
    from faker import Faker

    assert Faker().email(domains=('example.com', )) == '1d@example.com'
    assert Faker().email(unique=True) == '1d@example.com'
    assert Faker().email(unique=True) == '2d@example.com'
    assert Faker().email(unique=True) == '3d@example.com'
    assert Faker().email(unique=True) == '4d@example.com'
    assert Faker().email(unique=True) == '5d@example.com'

# Generated at 2022-06-14 00:38:45.499386
# Unit test for method surname of class Person
def test_Person_surname():
    from faker.providers.person.en_US import Provider as PersonProvider
    from faker.providers.person.ru_RU import Provider as PersonRuProvider
    from faker.providers.person.de_DE import Provider as PersonDeProvider
    from faker.providers.person.fi_FI import Provider as PersonFiProvider
    from faker.providers.person.en_GB import Provider as PersonGBProvider
    from faker.providers.person.en_CA import Provider as PersonCAProvider
    from faker.providers.person.en_AU import Provider as PersonAUProvider
    from faker.providers.person.en_NZ import Provider as PersonNZProvider
    from faker.utils.loading import find_available_locales
    import pytest



# Generated at 2022-06-14 00:38:48.414541
# Unit test for method surname of class Person
def test_Person_surname():
    # Test for method surname of class Person
    person = Person()
    assert isinstance(person.surname(), str)

# Generated at 2022-06-14 00:39:03.053107
# Unit test for method surname of class Person
def test_Person_surname():
    from faker import Faker
    fake = Faker(['ru_RU', ])
    fake.seed(0)
    assert fake.surname(gender=Gender.FEMALE) == 'Сидорова'
    assert fake.surname(gender=Gender.MALE) == 'Галеев'
    assert fake.surname() == 'Колесникова'
    fake.seed_instance(0)
    assert fake.surname() == 'Самойлов'
    
    
    
    fake = Faker(['en_GB', ])
    fake.seed(0)
    assert fake.surname(gender=Gender.FEMALE) == 'Holland'

# Generated at 2022-06-14 00:39:14.654508
# Unit test for method email of class Person

# Generated at 2022-06-14 00:39:17.669596
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert isinstance(nationality, str)

# Generated at 2022-06-14 00:39:22.075201
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in ["Russian", "Ukrainian", "German", "Polish", "Italian", "French", "American", "British", "Irish", "Korean", "Chinese", "Japanese"]


# Generated at 2022-06-14 00:39:25.899246
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    nations = set()
    for i in range(10000):
        nations.add(p.nationality())
    assert len(nations) == len(NATIONALITY)
    

# Generated at 2022-06-14 00:39:36.106588
# Unit test for method email of class Person
def test_Person_email():
    from faker.utils.loading import find_available_language
    from faker.utils.text import slugify
    from faker.generator import Generator
    from faker.config import AVAILABLE_LOCALES
    
    
    
    def _create_language_loader():
        from faker.providers.date_time import Provider as DateTimeProvider
        import gettext
        loader = gettext.NullTranslations()
        provider = DateTimeProvider(loader)
        return provider
    
    
    
    def _create_language_loader():
        from faker.providers.date_time import Provider as DateTimeProvider
        import gettext
        loader = gettext.NullTranslations()
        provider = DateTimeProvider(loader)
        return provider
    
    

# Generated at 2022-06-14 00:39:37.726734
# Unit test for method surname of class Person
def test_Person_surname():
    s = Person()
    assert isinstance(s.surname(), str)


# Generated at 2022-06-14 00:39:42.383873
# Unit test for method surname of class Person
def test_Person_surname():
    surnames = ['Abbamondi', 'Abbing', 'Abbott', 'Abbruscato']
    person = Person()
    surname_1 = person.surname()
    surname_2 = person.surname()
    assert all(surname in surnames for surname in (surname_1, surname_2))
    assert person.surname(gender=Gender.MALE) in surnames
    assert person.surname(gender=Gender.FEMALE) in surnames



# Generated at 2022-06-14 00:39:51.788016
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person(seed=32542).nationality(Gender.MAN) in genders_by_key(
        'nationality', Gender.MAN)
    assert Person(seed=9874).nationality(Gender.MAN) in genders_by_key(
        'nationality', Gender.MAN)
    assert Person(seed=9853).nationality() in genders_by_key(
        'nationality', Gender.MAN) + genders_by_key('nationality',
                                                    Gender.WOMAN)
    assert Person(seed=23456).nationality(Gender.MAN) in genders_by_key(
        'nationality', Gender.MAN)
    assert Person(seed=9873).nationality(Gender.MAN) in genders_by_key(
        'nationality', Gender.MAN)



# Generated at 2022-06-14 00:39:53.876477
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    nation = p.nationality()
    assert nation in p._data['nationality']

# Generated at 2022-06-14 00:40:12.623504
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationalities = person.nationality(Gender.MALE)
    nationalities = person.nationality(Gender.FEMALE)
    nationalities = person.nationality()
    return


# Generated at 2022-06-14 00:40:22.606856
# Unit test for method nationality of class Person
def test_Person_nationality():
    from fake2db.providers import Person
    from fake2db import exceptions as excepts

    def _case_1():
        p = Person()
        n = p.nationality()

        assert n in p._data['nationality']
        assert isinstance(n, str)

    def _case_2():
        p = Person()
        n = p.nationality(gender='male')

        assert n in p._data['nationality']['male']
        assert isinstance(n, str)

    def _case_3():
        p = Person()
        n = p.nationality(gender='female')

        assert n in p._data['nationality']['female']
        assert isinstance(n, str)

    def _case_4():
        p = Person()

# Generated at 2022-06-14 00:40:29.057135
# Unit test for method surname of class Person
def test_Person_surname():
    # Test with non-enum value
    with pytest.raises(NonEnumerableError):
        provider = Person()
        provider.surname('some value')

# Generated at 2022-06-14 00:40:36.656517
# Unit test for method surname of class Person
def test_Person_surname():
    print("")
    print("Test surname of class Person")
    print("=" * 60)
    # -------------------------------
    # Import library
    from faker import Faker
    from faker.config import DEFAULT_LOCALE
    from enum import Enum
    from faker.providers.person.en_US import Provider

    # Generate a fake person
    fake = Faker(locale=DEFAULT_LOCALE)
    fake.add_provider(Provider)
    # -------------------------------
    # Get all surnames of fake person
    surnames = fake.surnames
    print("Get all surnames of fake person:")
    print(surnames)
    print("")
    # -------------------------------
    # Get the first name of fake person
    surname = fake.surname()

# Generated at 2022-06-14 00:40:41.255191
# Unit test for method surname of class Person
def test_Person_surname():
    expected_name = "Машков"
    expected_gender = Gender.MALE
    generated_name = Person.surname(gender=expected_gender)
    assert expected_name in generated_name



# Generated at 2022-06-14 00:40:43.158511
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)

# Generated at 2022-06-14 00:40:47.479863
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person('es')
    assert person.surname() != False
#test_Person_surname()
print(test_Person_surname())


# Generated at 2022-06-14 00:40:55.754070
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Test method nationality of class Person."""
    provider = PersonProvider()

# Generated at 2022-06-14 00:40:58.964814
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname(Person()) == 'Иванов'


# Generated at 2022-06-14 00:41:03.857259
# Unit test for method nationality of class Person
def test_Person_nationality():
    values = valid_values_nationality()
    for i in range(len(values)):
        params = values[i][0]
        result = values[i][1]
        person = Person(seed=params)
        assert person.nationality() == result


# Generated at 2022-06-14 00:41:32.975696
# Unit test for method surname of class Person
def test_Person_surname():
    assert len(Person.surname(Gender.MALE)) >= 2
    assert Person.surname(Gender.MALE) in g.PATTERNS.NAMES.all('surnames')['MALE']
    assert len(Person.surname(Gender.FEMALE)) >= 2
    assert Person.surname(Gender.FEMALE) in g.PATTERNS.NAMES.all('surnames')['FEMALE']
    assert len(Person.surname()) >= 2

# Generated at 2022-06-14 00:41:34.018207
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert isinstance(nationality, str)


# Generated at 2022-06-14 00:41:44.275734
# Unit test for method surname of class Person
def test_Person_surname():
    from pyfaker.utils import get_random_item
    from pyfaker.enums import Gender, TitleType
    person = Person()

    assert person.surname()
    assert person.surname(gender=get_random_item(Gender))
    assert person.surname(gender=get_random_item(Gender), lower=False)
    assert person.surname(gender=get_random_item(Gender), title_type=TitleType.title)
    assert person.surname(gender=get_random_item(Gender), title_type=TitleType.title, lower=False)
    assert person.surname(gender=get_random_item(Gender), title_type=TitleType.suffix)

# Generated at 2022-06-14 00:41:48.799776
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    result = p.surname()
    assert result
    assert isinstance(result, str)
    assert result in p._data['surname']


# Generated at 2022-06-14 00:41:51.346147
# Unit test for method nationality of class Person
def test_Person_nationality():
    words = [Person().nationality() for _ in range(500)]
    res = [i for i in words if i != 'Russian']
    assert res != []



# Generated at 2022-06-14 00:41:52.706510
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    
    # Validating for string
    assert isinstance(person.nationality(), str)

# Generated at 2022-06-14 00:41:54.885193
# Unit test for method surname of class Person
def test_Person_surname():
    data = load_data()
    p = Person(data)
    s = p.surname(Gender.MALE)
    assert isinstance(s, str)


# Generated at 2022-06-14 00:42:00.243260
# Unit test for method surname of class Person
def test_Person_surname():
    seed(1)
    p = Person('ru')
    assert p.surname(Gender.MALE) == 'Павлов'
    assert p.surname(Gender.FEMALE) == 'Кондрашева'



# Generated at 2022-06-14 00:42:05.380236
# Unit test for method nationality of class Person
def test_Person_nationality():
    print()
    print('Test Person.nationality():')
    p = Person()
    p.max_iterations = 500
    gender = Gender.MALE
    v = p.nationality(gender)
    assert v in p.data['nationality']['male']
    print('OK')


# Generated at 2022-06-14 00:42:17.937929
# Unit test for method surname of class Person
def test_Person_surname():
    # the first test
    person = Person('en')
    surname = person.surname()
    assert type(surname) is str and len(surname) > 0
    
    # the second test
    person = Person('en')
    surname = person.surname()
    assert type(surname) is str and len(surname) > 0
    
    # the third test
    person = Person('en')
    surname = person.surname(Gender.FEMALE)
    assert type(surname) is str and len(surname) > 0
    
    # the fourth test
    person = Person('en')
    surname = person.surname(Gender.MALE)
    assert type(surname) is str and len(surname) > 0
    
    # the fifth

# Generated at 2022-06-14 00:43:01.899749
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    res = p.surname()
    assert res, res
    res = p.surname(None)
    assert res, res
    res = p.surname(Gender.male)
    assert res, res
    res = p.surname(Gender.female)
    assert res, res

# Generated at 2022-06-14 00:43:06.493693
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Unit test for method nationality of class Person."""
    for _ in range(100):
        nationality = Person().nationality()
        assert isinstance(nationality, str)



# Generated at 2022-06-14 00:43:08.993245
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() in SURNAMES

# Generated at 2022-06-14 00:43:12.566834
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() != None



# Generated at 2022-06-14 00:43:17.950998
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Initialize the class
    person = Person()
    # Get nationality
    result = person.nationality()
    # Check the result, is string or not
    assert isinstance(result, string_types)

# Generated at 2022-06-14 00:43:19.771246
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)


# Generated at 2022-06-14 00:43:22.155022
# Unit test for method surname of class Person
def test_Person_surname():
    name = Person().surname()
    assert isinstance(name, str)



# Generated at 2022-06-14 00:43:26.728695
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Arrange
    person = Person()
    actual = None
    expected = None

    # Act
    actual = person.nationality()

    # Assert
    assert actual != expected

# Generated at 2022-06-14 00:43:29.033124
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(seed=123456789)
    print(p.nationality())


# Generated at 2022-06-14 00:43:34.526990
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(10):
        assert isinstance(Person().surname(), str)
        assert isinstance(Person().surname(Gender.MALE), str)
        assert isinstance(Person().surname(Gender.FEMALE), str)
        assert isinstance(Person().last_name(), str)
        assert isinstance(Person().last_name(Gender.MALE), str)
        assert isinstance(Person().last_name(Gender.FEMALE), str)

# Generated at 2022-06-14 00:45:01.324532
# Unit test for method surname of class Person
def test_Person_surname():
    """Test for method surname of class Person.

    For all test cases we use the same seed for random.
    """
    seed = 4
    r = random.Random(seed)
    p = Person(r)

    surnames = p._data['surname']
    gender = Gender.MALE

    # All surnames include in male surnames.
    surnames_male = surnames[Gender.MALE]

    # If a surname not in list we raise an exception.
    surnames_male_set = set(surnames_male)

    for _ in range(1000):
        surname = p.surname(gender=gender)
        assert surname in surnames_male_set

    # Test for random seed
    assert p.surname(gender=gender) == 'Williams'



# Generated at 2022-06-14 00:45:05.093761
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Provider(locale='ru_RU')
    result = provider.nationality()

    assert result in provider.data['nationality']


# Generated at 2022-06-14 00:45:16.951619
# Unit test for method surname of class Person
def test_Person_surname():
    # Surnames
    assert t.Person().surname() in SURNAMES
    assert t.Person().surname(Gender.female) in SURNAMES_FEMALE
    assert t.Person().surname(Gender.male) in SURNAMES_MALE
    assert t.Person().surname(Gender.androgynous) in SURNAMES_ANDROGYNOUS
    assert t.Person().surname(Gender.unknown) in SURNAMES_UNKNOWN

    # Custom surnames
    surnames = ['Surname1', 'Surname2', 'Surname3']
    assert t.Person(surnames).surname() in surnames


# Generated at 2022-06-14 00:45:18.632816
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITIES


# Generated at 2022-06-14 00:45:22.800549
# Unit test for method email of class Person
def test_Person_email():
    # Initialization
    email = Person().email()
    # Assertion
    assert isinstance(email, str)



# Generated at 2022-06-14 00:45:30.574135
# Unit test for method surname of class Person
def test_Person_surname():
    # male
    random_male = random.bernoulli(0.5)
    if random_male:
        gender = Gender.MALE
    # female
    else:
        gender = Gender.FEMALE
    # homo
    random_homo = random.randint(0, 1)
    if random_homo == 0:
        title_type = TitleType.PREFIX
    # hetero
    else:
        title_type = TitleType.SUFFIX
    # surname
    random_surname = random.randint(0, 99)
    if random_surname >= 0 and random_surname <= 24:
        surname = 'Иванов'

# Generated at 2022-06-14 00:45:31.690478
# Unit test for method email of class Person
def test_Person_email():
    assert Person().email(unique=True)
    

# Generated at 2022-06-14 00:45:35.603451
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person.nationality(gender=Gender.MALE) in Person.nationality(gender=Gender.MALE)
    assert Person.nationality(gender=Gender.FEMALE) in Person.nationality(gender=Gender.FEMALE)

# Generated at 2022-06-14 00:45:48.967975
# Unit test for method username of class Person
def test_Person_username():
    # if random is not None, then test
    # randomness of method is not necessary.
    provider = Person(random=None)
    default_template = 'l.d'

    names = set()
    for _ in range(200):
        name = provider.username(template=default_template)
        assert re.fullmatch(r'[a-z]{1,2}\.[0-9]{4}', name), \
            'Username must match the template!'
        names.add(name)

    assert len(names) >= 100, \
        'Generated names are not unique!'

# Generated at 2022-06-14 00:45:51.955531
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert type(person.surname()) == str

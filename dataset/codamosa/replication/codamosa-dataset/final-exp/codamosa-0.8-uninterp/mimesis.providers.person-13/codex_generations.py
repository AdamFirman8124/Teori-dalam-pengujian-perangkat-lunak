

# Generated at 2022-06-14 00:36:37.258334
# Unit test for method surname of class Person
def test_Person_surname():
    locale_list = ['en', 'ru', 'uk', 'jp']

    for locale in locale_list:
        # Initialize Person by locale
        person = Person(locale)

        # Get random gender
        gender = get_random_item(Gender, rnd=person.random)

        # Get random surname by gender
        surname = person.surname(gender)

        # If surname is None, then it is a problem
        assert surname is not None


# Generated at 2022-06-14 00:36:48.949886
# Unit test for method email of class Person
def test_Person_email():
    # Testing with not argument
    provider = Person()
    result = provider.email()
    # Check
    assert isinstance(result, str) and '@' in result

    # Testing with next argument:
    provider = Person()
    result = provider.email(domains=('example.com', 'example.org'))
    # Check
    assert isinstance(result, str) and result[-11:] in ('example.com', 'example.org')

    # Testing with next argument:
    provider = Person()
    result = provider.email(unique=True)
    # Check
    assert isinstance(result, str) and '@' in result

    # Testing with next argument:
    provider = Person(seed=10)
    result = provider.email(unique=True)
    # Check

# Generated at 2022-06-14 00:36:52.282918
# Unit test for method nationality of class Person
def test_Person_nationality():

    instance = Person()
    assert isinstance(instance.nationality(), str)
test_Person_nationality()

# Generated at 2022-06-14 00:36:58.270099
# Unit test for method email of class Person
def test_Person_email():
    assert Person().email() == "ryank@gmail.com"
    assert Person().email() == "daniel.petrov@yahoo.com"
    assert Person().email() == "bob3475@list.ru"

# Generated at 2022-06-14 00:37:05.418300
# Unit test for method surname of class Person
def test_Person_surname():
    assert isinstance(Person().surname(Gender.MALE), str)
    assert isinstance(Person().surname(Gender.FEMALE), str)
    assert isinstance(Person().surname(), str)
    assert isinstance(Person().surname(None), str)
    assert isinstance(Person().surname(None), str)


# Generated at 2022-06-14 00:37:10.882960
# Unit test for method surname of class Person
def test_Person_surname():
    gender = [list(Gender)[0],list(Gender)[1],list(Gender)[2]]
    surnames = [['Jones', 'Williams', 'Brown'], ['Taylor', 'Davies', 'Evans'], ['Thompson', 'Edwards', 'Roberts']]
    for i in range(0,3):
        #print(gender[i])
        assert Person.surname(gender[i]) in surnames[i]

# Generated at 2022-06-14 00:37:12.168911
# Unit test for method username of class Person
def test_Person_username():
    p = Person(random=Random())
    assert isinstance(p.username(), str)

# Generated at 2022-06-14 00:37:14.207448
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        assert isinstance(Person().nationality(), str)


# Generated at 2022-06-14 00:37:15.396672
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert 'Russian' in Person().nationality()


# Generated at 2022-06-14 00:37:21.767069
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    for _ in range(1000):
        assert person.nationality() in NATIONALITY
        assert person.nationality(Gender.MALE) in NATIONALITY
        assert person.nationality(Gender.FEMALE) in NATIONALITY


# Generated at 2022-06-14 00:37:34.458278
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Provider()

    outputs = []

    for __ in range(100):
        output = person.nationality()
        outputs.append(output)

    expected_outputs = NATIONALITIES[GENDER.MALE]
    assert all([output in expected_outputs for output in outputs])

# Generated at 2022-06-14 00:37:38.470057
# Unit test for method surname of class Person
def test_Person_surname():
    # Setup
    random = Random()
    person = Person(random)
    # Exercise
    result = person.surname()
    # Verify
    assert isinstance(result, str)

# Generated at 2022-06-14 00:37:47.375168
# Unit test for method surname of class Person
def test_Person_surname():
    faker = Person(random.Random(42))
    assert faker.surname() == 'Bosco'

    faker = Person(random.Random(42))
    assert faker.surname(gender='M') == 'Bosco'

    faker = Person(random.Random(42))
    assert faker.surname(gender='F') == 'Santana'

    # Unit test for method last_name of class Person
    faker = Person(random.Random(42))
    assert faker.last_name() == 'Bosco'


# Generated at 2022-06-14 00:37:55.658382
# Unit test for method nationality of class Person
def test_Person_nationality():
    def _test(gender: Gender):
        # First we need to get a list of all nationalities
        nationalities = Person()._data['nationality']
        if isinstance(nationalities, dict):
            nationalities = nationalities[gender]

        # Then we check that all nationalities belong to a particular gender
        for nationality in nationalities:
            assert nationality.casefold().endswith(gender.name.casefold())

    for gender in Gender:
        _test(gender)
# Enum for country codes

# Generated at 2022-06-14 00:38:00.307549
# Unit test for method surname of class Person
def test_Person_surname():
    p=Person(seed=53)
    assert p.surname() == 'Archer'
    assert p.surname(p.Gender.male) == 'Archer'
    assert p.surname(p.Gender.female) == 'Decker'
    
    
test_Person_surname()

# Generated at 2022-06-14 00:38:03.548821
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()

    # 1. Default arguments
    result = person.nationality()
    assert result in person._data['nationality']

    # 2. Specifying gender
    for gender in Gender:
        result = person.nationality(gender)
        assert result in person._data['nationality'][gender]

# Generated at 2022-06-14 00:38:06.897441
# Unit test for method email of class Person
def test_Person_email():
    assert Person().email() == 'foretime10@live.com'
test_Person_email()


# Generated at 2022-06-14 00:38:09.977183
# Unit test for method email of class Person
def test_Person_email():
    """
    Unit test for method email
    """
    person = Person(seed=0)
    ref = 'foretime10@live.com'
    act = person.email()
    assert act == ref

# Generated at 2022-06-14 00:38:16.665171
# Unit test for method surname of class Person
def test_Person_surname():
    for i in range(100):
        # Get surname with specified gender.
        assert isinstance(Person().surname(Gender.MALE), str)
        assert isinstance(Person().surname(Gender.FEMALE), str)

        # Get surname with random gender.
        assert isinstance(Person().surname(), str)
        
        # Get surname with incorrect gender.
        try:
            Person().surname(Gender.OTHER)
        except NonEnumerableError:
            pass
            

# Generated at 2022-06-14 00:38:24.444182
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert isinstance(Person.nationality(Person()), str)
import datetime
from datetime import datetime as dt

from faker.utils.formatters import date_time
from faker.providers.date_time.en_GB import Provider as enGBProvider
from faker.providers.date_time.en_US import Provider as enUsProvider
from faker.providers.date_time.ja_JP import Provider as jaJPProvider
from faker.providers.date_time.ru_RU import Provider as ruRUProvider
from faker.providers.date_time.zh_CN import Provider as zhCNProvider
from faker.providers.company.en_GB import Provider as enGbCompProvider



# Generated at 2022-06-14 00:38:37.822881
# Unit test for method surname of class Person
def test_Person_surname():
    """Unit test for method surname of class Person"""
    p = Person()
    for _ in range(100):
        s = p.surname()
        assert isinstance(s, str)

# Generated at 2022-06-14 00:38:40.080730
# Unit test for method nationality of class Person
def test_Person_nationality():
    a = Person()
    # Test for the correctness of the return value of the method nationality
    assert isinstance(a.nationality(), str)

# Generated at 2022-06-14 00:38:43.852422
# Unit test for method email of class Person
def test_Person_email():
    # call method email for class Person
    result = Person().email()
    # check that result is valid email
    assert re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', result)



# Generated at 2022-06-14 00:38:45.405620
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in PERSON_DATA['nationality']

# Generated at 2022-06-14 00:38:47.902108
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person('ru')
    assert isinstance(p.nationality(), str)

# Generated at 2022-06-14 00:38:50.735153
# Unit test for method nationality of class Person
def test_Person_nationality():
    obj = Person()
    result = obj.nationality()
    assert result

# Generated at 2022-06-14 00:38:56.848503
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        p = Person()
        nationality = p.nationality()
        match = re.fullmatch(r'[a-zA-Z\s]+$', nationality)
        assert match is not None, \
            'Value "{}" is not a valid nationality.'.format(nationality)

test_Person_nationality()

# Generated at 2022-06-14 00:38:59.147033
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person()
    result = provider.nationality()
    assert isinstance(result, str)
    assert len(result) > 0
    assert result in NATIONALITIES


# Generated at 2022-06-14 00:39:02.543175
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Test if its not equal to none
    assert(Person().nationality() != None)
    
test_Person_nationality()


# Generated at 2022-06-14 00:39:07.022490
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    result = person.surname('male')
    assert isinstance(result, str)
    assert result in person.surname_list
    print(result)


# Generated at 2022-06-14 00:39:19.758834
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert isinstance(surname, str)
    

# Generated at 2022-06-14 00:39:23.459020
# Unit test for method surname of class Person
def test_Person_surname():
    """Unit test for method surname of class Person."""
    person = Person()
    s = person.surname()
    assert len(s) > 0

# Generated at 2022-06-14 00:39:31.547082
# Unit test for method nationality of class Person
def test_Person_nationality():
    # A list of the correct values that this method returns
    correct_values = [
        'Latvian',
        'Russian',
        'Macedonian',
        'Georgian',
        'Armenian',
        'Greek',
        'Uzbek',
        'Turkmen',
        'Tajik',
        'Belarussian',
        'Moldavian',
        'Kazakh'
    ]

    obj = Person()

    # Method should return one of the values in the list
    assert obj.nationality() in correct_values


# Generated at 2022-06-14 00:39:34.752589
# Unit test for method username of class Person
def test_Person_username():
    provider = Faker('en_US')
    assert provider.username(template='Ud') == 'Dd'
    assert provider.username(template='l') == 'a'
    assert provider.username(template='U') == 'A'



# Generated at 2022-06-14 00:39:36.441296
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        a = Person().nationality()
        assert a

# Generated at 2022-06-14 00:39:38.436514
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert nationality in person._data['nationality'], nationality



# Generated at 2022-06-14 00:36:30.993293
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    output = person.surname(gender=Gender.MALE)
    assert output in person._data['surname']['male']
    output = person.surname(gender=None)
    assert output in person._data['surname']['male'] or output in person._data['surname']['female']
    output = person.surname(gender=Gender.FEMALE)
    assert output in person._data['surname']['male']

# Generated at 2022-06-14 00:36:45.289929
# Unit test for method surname of class Person
def test_Person_surname():
    # fail: surname = None
    with pytest.raises(NonEnumerableError):
        provider = Person(random=Random())
        provider.surname(surname=None)
    # fail: gender = None
    with pytest.raises(NonEnumerableError):
        provider = Person(random=Random())
        provider.surname(gender=None)
    # pass: gender = Gender.MALE
    provider = Person(random=Random())
    result = provider.surname(gender=Gender.MALE)
    assert isinstance(result, str)
    assert result in SURNAMES_MALE
    # pass: gender = Gender.FEMALE
    provider = Person(random=Random())
    result = provider.surname(gender=Gender.FEMALE)
    assert isinstance(result, str)


# Generated at 2022-06-14 00:36:50.788776
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person()
    nationalities = provider._data['nationality']
    for i in range(100):
        value = provider.nationality()
        assert value in nationalities


# Generated at 2022-06-14 00:36:55.640030
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person.nationality(gender=None)
    assert Person.nationality(gender=Gender.FEMALE)
    assert Person.nationality(gender=Gender.MALE)
    assert Person.nationality(gender=Gender.UNKNOWN)



# Generated at 2022-06-14 00:36:58.137836
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() == 'Russian', 'Method nationality not work'

# Generated at 2022-06-14 00:37:02.083713
# Unit test for method nationality of class Person
def test_Person_nationality():

    person = PersonProvider(random=Random(None))

    assert isinstance(person.nationality(), str) == True

# Generated at 2022-06-14 00:37:04.672399
# Unit test for method nationality of class Person
def test_Person_nationality():
    n = Nation(person_nationality())
    assert n.name == "American"

# Generated at 2022-06-14 00:37:06.215468
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITIES


# Generated at 2022-06-14 00:37:09.559827
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker import Faker
    from pprint import pprint
    fake = Faker('ru_RU')
    pprint(fake.nationality(gender='female'))
# test_Person_nationality()

# Generated at 2022-06-14 00:37:13.113098
# Unit test for method nationality of class Person
def test_Person_nationality():
    nat = Person().nationality()
    assert isinstance(nat, str)
    assert len(nat) >= 3


# Generated at 2022-06-14 00:37:28.685219
# Unit test for method surname of class Person
def test_Person_surname():
    """Testing Person._surname method."""
    test_cases = [
        (None, {}),
        (Gender.MALE, {Gender.MALE: ["Smith", "Jones"], Gender.FEMALE: []}),
        (Gender.FEMALE, {Gender.MALE: [], Gender.FEMALE: ["Nguyen", "Simon"]}),
        (Gender.OTHER, {Gender.MALE: [], Gender.FEMALE: []}),
    ]

    for gender, surnames in test_cases:
        p = Person(surnames=surnames)
        assert isinstance(p.surname(gender=gender), str)

# Generated at 2022-06-14 00:37:37.274346
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=12345)
    surname = person.surname()
    expected = 'Корежук'
    assert surname == expected
    surname = person.surname(gender='male')
    expected = 'Почепа'
    assert surname == expected
    surname = person.surname(gender='male', unique=True)
    expected = 'Петко'
    assert surname == expected
    surnames = person.surname(quantity=5)
    expected = ['Корежук', 'Таборовский', 'Хохлова', 'Вельковский', 'Подлужный']

# Generated at 2022-06-14 00:37:42.742319
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=1234)
    assert person.surname(Gender.MALE) == 'Barrett'
    assert person.surname(Gender.FEMALE) == 'Barrett'
    assert person.surname(Gender.UNKNOWN) == 'Barrett'
    assert person.surname() == 'Barrett'


# Generated at 2022-06-14 00:37:49.572712
# Unit test for method nationality of class Person
def test_Person_nationality():

    person = Person(seed=42)

    try:
        nationalities = person.nationality

    except NonEnumerableError as e:
        assert str(e) == 'The «enums.Gender» must be used to generate a' \
                         ' random value.',\
            'Метод «nationality» класса «Person» ведет себя ' \
            'не так, как ожидалось.'


# Generated at 2022-06-14 00:38:00.746179
# Unit test for method nationality of class Person
def test_Person_nationality():
    nationalities = Person.nationality()
    if not isinstance(nationalities, str):
        print('Method Person.nationality() should return str, but return {0}.'
              .format(type(nationalities)))
        assert False

    nationalities = Person.nationality(Gender.FEMALE)
    if not isinstance(nationalities, str):
        print('Method Person.nationality() should return str, but return {0}.'
              .format(type(nationalities)))
        assert False

    nationalities = Person.nationality(Gender.MALE)
    if not isinstance(nationalities, str):
        print('Method Person.nationality() should return str, but return {0}.'
              .format(type(nationalities)))
        assert False

    print('Success test for method nationality of class Person.')
    assert True

#

# Generated at 2022-06-14 00:38:02.080519
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()

    assert provider.surname()

# Generated at 2022-06-14 00:38:14.829672
# Unit test for method surname of class Person
def test_Person_surname():
    p1 = Person(locale='English')
    p2 = Person(locale='Russian')
    p3 = Person(locale='Ukrainian')
    
    first_names = []
    surnames = []
    first_names_ru = []
    surnames_ru = []
    first_names_ua = []
    surnames_ua = []
    
    # Generating 1000 surnames and first names for each locale.
    for _ in range(1000):
        first_names.append(p1.name())
        surnames.append(p1.surname())
        first_names_ru.append(p2.name())
        surnames_ru.append(p2.surname())
        first_names_ua.append(p3.name())

# Generated at 2022-06-14 00:38:23.213535
# Unit test for method email of class Person
def test_Person_email():
    from os import urandom as _urandom    
    from random import choice as _choice
    import string as _string
    from faker import Faker as _Faker
    #rnd = Random()
    rnd = _Faker()
    #rnd.seed(0)
    rnd.random.seed(0)
    lst = ['gmail.com', 'live.com', 'yahoo.com', 'mail.ru']
    itr = 1000
    lst1 = []
    lst2 = []
    for _ in range(itr):
        #email = Person(rnd).email(domains=lst,unique=True)
        email = rnd.person().email(domains=lst,unique=True)
        lst1.append(email)
        lst2.append(email)

# Generated at 2022-06-14 00:38:29.631523
# Unit test for method surname of class Person
def test_Person_surname():
    # Base test
    result = Person.surname()
    assert len(result) > 0

    # Test with gender of undefined
    result = Person.surname(None)
    assert len(result) > 0

    # Test with random gender
    result = Person.surname(Gender.male)
    assert len(result) > 0

    result = Person.surname(Gender.female)
    assert len(result) > 0


# Generated at 2022-06-14 00:38:32.870420
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(1000):
        assert(Person().surname() in Person()._data['surname'])


# Generated at 2022-06-14 00:38:41.337025
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() == 'Russian'

# Generated at 2022-06-14 00:38:47.256612
# Unit test for method surname of class Person
def test_Person_surname():
    obj = Person()
    assert isinstance(obj.surname(), str)
    assert obj.surname() not in ""


# Generated at 2022-06-14 00:38:50.024515
# Unit test for method nationality of class Person
def test_Person_nationality():
    nationalities = [Person().nationality() for i in range(10)]
    for nationality in nationalities:
        assert nationality in NATIONALITY_LIST


# Generated at 2022-06-14 00:38:54.081383
# Unit test for method surname of class Person
def test_Person_surname():
    Faker.seed(0)
    assert Person().surname() == 'Garcia'


# Generated at 2022-06-14 00:38:56.687978
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert len(p.nationality()) > 0
    assert len(p.nationality(Gender.male)) > 0
    assert len(p.nationality(Gender.female)) > 0


# Generated at 2022-06-14 00:38:58.409579
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in person._data['nationality']


# Generated at 2022-06-14 00:39:02.119864
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker import Faker
    from faker.providers import BaseProvider
    
    
    class MyPersonProvider(BaseProvider):
        def nationality(self):
            return 'Russian'
    
    
    fake = Faker()
    fake.add_provider(MyPersonProvider)
    
    
    nationality = fake.nationality()
    assert nationality == 'Russian'
    


# Generated at 2022-06-14 00:39:12.910095
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()

# Generated at 2022-06-14 00:39:16.038508
# Unit test for method nationality of class Person
def test_Person_nationality():
    
    #Make a real instance
    person = Person()

    #Call the method nationality
    result = person.nationality()
    
    #Check if the type is string
    assert isinstance(result,str)


# Generated at 2022-06-14 00:39:30.373809
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname() == 'Лавров'
    assert Person.surname('Макаренко') == 'Макаренко'
    assert Person.surname({'М':'Лавров'}) == 'Лавров'
    assert Person.surname({'Ж':'Лавровой'}) == 'Лавровой'

    assert Person.surname(gender='М') == 'Лавров'
    assert Person.surname(gender='Ж') == 'Лавровой'

    assert Person.surname(gender=Gender.MALE) == 'Лавров'
   

# Generated at 2022-06-14 00:39:51.918083
# Unit test for method nationality of class Person
def test_Person_nationality():
    from pydantic import BaseModel
    from vader.utils import enum_from_config

    class Gender(enum.Enum):
        MALE = 1
        FEMALE = 2

    class Config(BaseModel):
        nationalities: dict

        class Config:
            enum_generate_upper_case = False

    config = {
        'nationalities': {
            Gender.MALE.name: ['Male_Nationality_1', 'Male_Nationality_2'],
            Gender.FEMALE.name: ['Female_Nationality_1', 'Female_Nationality_2'],
        },
    }

    # Load Nationality enum
    Nationality = enum_from_config(config=config, config_class=Config)

    # Check that male nationality is correct

# Generated at 2022-06-14 00:39:54.725703
# Unit test for method nationality of class Person
def test_Person_nationality():
    ''' Test nationality (random) '''
    my_person = Person('en')
    nat = my_person.nationality()
    assert(nat != None)


# Generated at 2022-06-14 00:39:59.369706
# Unit test for method nationality of class Person
def test_Person_nationality():
    for i in range(100):
        assert (isinstance(Person().nationality(), str))
    print('Test for nationality of class Person has passed!')


# Generated at 2022-06-14 00:40:01.967210
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert person.surname("male") in person._data['surname']['male']
    # Unit test for method last_name of class Person

# Generated at 2022-06-14 00:40:06.908875
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert len(Person().nationality()) == len("Japanese")

# Generated at 2022-06-14 00:40:11.670236
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Test method nationality of class Person."""
    assert Person().nationality() in NATIONALITIES

# Generated at 2022-06-14 00:40:14.962947
# Unit test for method nationality of class Person
def test_Person_nationality():
    obj = Person()
    result = obj.nationality()
    assert result is not None



# Generated at 2022-06-14 00:40:20.967824
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert p.nationality() in p._data['nationality']
    assert p.nationality() in p._data['nationality']
    assert p.nationality() in p._data['nationality']
    assert p.nationality() in p._data['nationality']
    assert p.nationality() in p._data['nationality']

# Generated at 2022-06-14 00:40:27.042977
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()

    result = person.surname()
    assert type(result) == str

    result = person.surname(gender=Gender.MALE)
    assert type(result) == str

    result = person.surname(gender=Gender.FEMALE)
    assert type(result) == str


# Generated at 2022-06-14 00:40:31.152377
# Unit test for method nationality of class Person
def test_Person_nationality():
    items = Person.nationality.items

    assert isinstance(items, dict)
    assert len(items) == 3
    assert all(
        isinstance(gender, Gender) for gender in items.keys())
    assert all(
        isinstance(nationalities, list) for nationalities in items.values())



# Generated at 2022-06-14 00:41:06.745627
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    
    # Проверка передачи параметра типа Gender
    assert person.surname(Gender.male) 
    
    # Проверка передачи параметра типа str 
    assert person.surname('male')
    
    # Проеверка вызова без параметров
    assert person.surname()


# Generated at 2022-06-14 00:41:11.541994
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    for i in range(1000):
        n = person.nationality()
        assert isinstance(n, str)
        assert n in person._data['nationality']


# Generated at 2022-06-14 00:41:13.761750
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITIES

# Generated at 2022-06-14 00:41:16.362239
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    # The surname can be a string
    provider.surname()



# Generated at 2022-06-14 00:41:18.765776
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=0)
    assert person.nationality() == 'Russian'


# Generated at 2022-06-14 00:41:27.792938
# Unit test for method surname of class Person
def test_Person_surname():
    """Unit test for method surname of class Person."""

    # Arrange
    person = Person()
    expected_result_type = str
    result_types = list()

    # Act
    for _ in range(100):
        result = person.surname()
        result_types.append(type(result))

    # Assert
    assert all(isinstance(result_type, expected_result_type) for result_type in result_types)



# Generated at 2022-06-14 00:41:30.051106
# Unit test for method surname of class Person
def test_Person_surname():
    person_provider = Person(random=Random())
    surname = person_provider.surname()
    assert len(surname) > 0

# Generated at 2022-06-14 00:41:32.976309
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)
    print(person.surname())


# Generated at 2022-06-14 00:41:41.507570
# Unit test for method surname of class Person
def test_Person_surname():
    import re
    import pytest
    print("Test Person_surname")
    usernames =[
    'Roman',
    'Ivanov',
    'Frolov',
    'Alex',
    'Dmitriy',
    'Petrov',
    'Pupkin'
    ]
    p = Person()
    for _ in range(7):
        assert (p.surname() in usernames)


# Generated at 2022-06-14 00:41:44.274498
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert p.nationality() in p._data['nationality']

# Generated at 2022-06-14 00:42:17.219509
# Unit test for method surname of class Person
def test_Person_surname():
    print('\nPerson.surname')

    person = Person()
    surname1 = person.surname(Gender.MALE)
    surname2 = person.surname(Gender.FEMALE)
    surname3 = person.surname(Gender.NEUTRAL)

    print('{:<15}{:<15}{:<15}'.format(surname1, surname2, surname3))

# Generated at 2022-06-14 00:42:20.522208
# Unit test for method email of class Person
def test_Person_email():
    from faker.providers.person.hr_HR import Person
    p = Person(None)
    assert p.email()
    assert p.email(unique=True)
    assert '@' in p.email()


# Generated at 2022-06-14 00:42:29.756291
# Unit test for method surname of class Person
def test_Person_surname():
    from faker import Faker
    from faker.providers.person.ru_RU import Provider

    faker = Faker(['ru_RU'])
    faker.add_provider(Provider)

    gender = Gender('FEMALE')
    surname = faker.surname(gender)
    print(surname)
    print(type(gender))

test_Person_surname()


# Generated at 2022-06-14 00:42:34.955190
# Unit test for method surname of class Person
def test_Person_surname():
    random_person = Person()
    random_surname = random_person.surname()
    assert random_surname == random_person.last_name()

# Generated at 2022-06-14 00:42:37.130496
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname() in SURNAME
    assert p.last_name() in SURNAME


# Generated at 2022-06-14 00:42:42.410505
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(seed=0)
    assert p.nationality() == 'Chuvash'
    assert p.nationality(Gender.MALE) == 'Chuvash'
    assert p.nationality(Gender.FEMALE) == 'Chuvash'


# Generated at 2022-06-14 00:42:46.522101
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        assert Person().nationality() in PERSON['nationality']

test_Person_nationality()

# Generated at 2022-06-14 00:42:48.798234
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        assert Person().nationality() in NATIONALITIES



# Generated at 2022-06-14 00:42:50.482875
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    email = person.email()

# Generated at 2022-06-14 00:42:52.438611
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = PersonFactory()
    assert person.nationality() in person._data['nationality']



# Generated at 2022-06-14 00:43:53.418199
# Unit test for method nationality of class Person
def test_Person_nationality():
    from names import get_nationality

    # Test with seed
    person_1 = Person(seed=1)
    nationality_1 = person_1.nationality()
    assert nationality_1.lower() == 'taiwanese'

    # Test without seed
    person_2 = Person()
    nationality_2 = person_2.nationality()
    assert nationality_2.lower() == 'indonesian'

    # Test with ‘nationality’ data
    person_3 = Person(nationality='kyrgyz')
    nationality_3 = person_3.nationality()
    assert nationality_3.lower() == 'kyrgyz'

    # Test with method get_nationality()
    person_4 = Person()
    person_4.nationality = get_nationality
    nationality_4 = person_4.nationality()

# Generated at 2022-06-14 00:43:56.716691
# Unit test for method surname of class Person
def test_Person_surname():
    with Person() as p:
        assert p.surname() in p._data["surname"]

# Generated at 2022-06-14 00:44:00.548821
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    name = person.last_name()
    assert isinstance(name, str)
    assert len(name) > 0

# Generated at 2022-06-14 00:44:04.246303
# Unit test for method surname of class Person
def test_Person_surname():
    rnd = faker.Faker('en_US')
    p = Person(rnd)
    assert p.surname(Gender.Male) in SURNAMES_MALE


# Generated at 2022-06-14 00:44:08.099524
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname(random=Random()) == 'Петров'
    assert Person.surname(random=Random()) == 'Петров'
    assert Person.surname(random=Random()) == 'Петров'



# Generated at 2022-06-14 00:44:11.092526
# Unit test for method nationality of class Person
def test_Person_nationality():
    values = Person().nationality()
    assert isinstance(values, str)

# Generated at 2022-06-14 00:44:15.564839
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert len(surname) == 3, "surname length should be 3"
    assert surname.istitle(), "surname should be in title case"

# Generated at 2022-06-14 00:44:18.893890
# Unit test for method nationality of class Person
def test_Person_nationality():
    
    print("unittest for method nationality of class Person")
    
    for i in range(10):
        random_nationality = faker.nationality()
        print("random_nationality: ", random_nationality)
    
    pass

# Generated at 2022-06-14 00:44:21.140186
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(100):
        _ = Person().surname()


# Generated at 2022-06-14 00:44:28.357600
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    for _ in range(1000):
        # The first element of tuple is a gender
        surname = person.surname(Gender.FEMALE)
        assert surname in surnames_female, '"{}" is not a valid surname.'.format(surname)

    for _ in range(1000):
        surname = person.surname(Gender.MALE)
        assert surname in surnames_male, '"{}" is not a valid surname.'.format(surname)

    for _ in range(1000):
        surname = person.surname(Gender.UNDEFINED)
        assert surname in surnames_undefined, '"{}" is not a valid surname.'.format(surname)

    for _ in range(1000):
        surname = person.surname()
        assert surname in surnames
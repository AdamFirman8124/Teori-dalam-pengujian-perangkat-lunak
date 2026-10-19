

# Generated at 2022-06-14 00:36:30.515837
# Unit test for method nationality of class Person
def test_Person_nationality():
    l = list(set([Person().nationality() for _ in range(100)]))
    assert isinstance(l, list)
    assert len(set(l)) == len(l)
    assert len(l) > 1

# Generated at 2022-06-14 00:36:39.757871
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    
    # Test with gender
    for _ in range(100):
        assert person.nationality(Gender.MALE) in COUNTRIES
    for _ in range(100):
        assert person.nationality(Gender.FEMALE) in COUNTRIES
    for _ in range(100):
        assert person.nationality(Gender.UNKNOWN) in COUNTRIES
    
    # Test without gender
    for _ in range(100):
        assert person.nationality() in COUNTRIES

# Generated at 2022-06-14 00:36:48.533050
# Unit test for method surname of class Person
def test_Person_surname():
    @vcr.use_cassette
    def test_Person_surname_object():
        person = Person()
        p = person.surname(Gender.MALE)
        assert isinstance(p, str)

    @vcr.use_cassette
    def test_Person_surname_is_string():
        person = Person()
        p = person.surname(Gender.MALE)
        assert isinstance(p, str)

    @vcr.use_cassette
    def test_Person_surname_is_not_empty():
        person = Person()
        p = person.surname(Gender.MALE)
        assert isinstance(p, str)
        assert p != ''


# Generated at 2022-06-14 00:36:51.071399
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        nation = person.nationality()
        assert nation in NATIONALITY

# Generated at 2022-06-14 00:36:54.871255
# Unit test for method nationality of class Person
def test_Person_nationality():
    '''Testing nationality method'''
    prof_gen = Person()
    assert isinstance(prof_gen.nationality(),str)

# Generated at 2022-06-14 00:36:59.580624
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(locale='en')
    nationalities = p._data['nationality']

    for i in range(len(nationalities)):
        n = p.nationality()
        assert n in nationalities



# Generated at 2022-06-14 00:37:10.058888
# Unit test for method surname of class Person
def test_Person_surname():

    def check_surname(name: str, gender: Gender, surnames: List[str]):
        assert name in surnames

    persons = Person()


# Generated at 2022-06-14 00:37:11.989623
# Unit test for method surname of class Person
def test_Person_surname():
    from hypothesis import given
    from hypothesis.strategies import text
    from hypothesis.extra.pytest import register_assert_rewrite
    register_assert_rewrite()

    @given(text())
    def test_Person_surname(surname):
        pass

# Generated at 2022-06-14 00:37:17.666857
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person(seed=42)
    assert p.last_name() == 'Путин'
    assert p.last_name(Gender.MALE) == 'Путин'
    assert p.last_name(Gender.FEMALE) == 'Казанская'
    assert p.surname() == 'Путин'


# Generated at 2022-06-14 00:37:20.938015
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=0)

    result = person.nationality()

    expected = 'Irish'
    assert result == expected


# Generated at 2022-06-14 00:37:30.321944
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert isinstance(person.nationality(), str)



# Generated at 2022-06-14 00:37:31.423735
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()


# Generated at 2022-06-14 00:37:35.766284
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    assert person.email() != ''
    assert person.email() != None 
    assert person.email() != '@'

# Generated at 2022-06-14 00:37:38.521929
# Unit test for method username of class Person
def test_Person_username():
    fake = Faker()
    print(fake.username())
    # Output:
    #   trisha34


# Generated at 2022-06-14 00:37:42.396429
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()

    assert(person.nationality() != person.nationality())


# Generated at 2022-06-14 00:37:43.470583
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITY

# Generated at 2022-06-14 00:37:46.785126
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() != Person().nationality()

# Generated at 2022-06-14 00:37:52.805288
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    iter_limit = 100
    
    for _ in range(iter_limit):
        email_1 = p.email(unique=True)
        email_2 = p.email(unique=True)
        assert email_1 != email_2
        
test_Person_email()

# Generated at 2022-06-14 00:37:54.275799
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    p.nationality()


# Generated at 2022-06-14 00:38:01.201678
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationalities = person._data['nationality']
    all_nationalities = person.nationality(PersonGender.Male) + ' ' + person.nationality(PersonGender.Female)
    all_nationalities = all_nationalities.split(' ')
    all_nationalities = set(all_nationalities)

    assert len(all_nationalities) == len(nationalities)
    for nationality in nationalities:
        assert nationality in all_nationalities
 
## Unit test for method last_name of class Person

# Generated at 2022-06-14 00:38:18.320728
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    name = person.surname()
    assert name
    assert isinstance(name, str)

# Generated at 2022-06-14 00:38:23.763496
# Unit test for method nationality of class Person
def test_Person_nationality():

    from faker_ru import Person

    p = Person(seed=1)
    assert p.nationality() == 'Россиянин'
    assert p.nationality() == 'Россиянин'

    p.reset_seed()

    assert p.nationality() == 'Россиянин'
    assert p.nationality() == 'Россиянин'


# Generated at 2022-06-14 00:38:25.314489
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert person.surname() in person._data['surname']

# Generated at 2022-06-14 00:38:26.968544
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert type(nationality) == str



# Generated at 2022-06-14 00:38:32.656982
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Arrange
    pr = Person(seed=1234)
    expected = 'Russian'
    # Act
    actual = pr.nationality()
    # Assert
    assert actual == expected

# Run unit tests
test_Person_nationality()


# Generated at 2022-06-14 00:38:38.880488
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    n = p.nationality()
    assert n in p._data['nationality']
test_Person_nationality()
test_Person_nationality()
test_Person_nationality()
test_Person_nationality()
test_Person_nationality()
 

# Generated at 2022-06-14 00:38:42.143049
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert isinstance(p.nationality(),str)
    assert len(p.nationality())>0

# Generated at 2022-06-14 00:38:47.040525
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert isinstance(nationality, str)

# Generated at 2022-06-14 00:38:49.042257
# Unit test for method surname of class Person
def test_Person_surname():
    assert 'Иванов' in Person.surname()


# Generated at 2022-06-14 00:39:00.465328
# Unit test for method email of class Person
def test_Person_email():
    provider = Person()
    print(provider.email())
    provider = Person()
    print(provider.email())
    provider = Person()
    print(provider.email())
    
    
test_Person_email()

name = 'Pritish'
#print(name.startswith('P'))
print()

import re
print(re.fullmatch(r'[Ul\.\-\_d]*[Ul]+[Ul\.\-\_d]*', 'Ud'))

#print(re.findall('Ud', 'Ud'))

import random
print(random.choice(EMAIL_DOMAINS))

# Generated at 2022-06-14 00:39:19.657918
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker_ru import RussianProvider
    from faker_en import EnglishProvider
    faker = Faker()
    faker.add_provider(RussianProvider)
    faker.add_provider(EnglishProvider)
    faker.add_provider(Person)
    rand = faker.random
    rand.seed(42)
    for i in range(15):
        print(faker.nationality(Gender.MALE))


# Generated at 2022-06-14 00:39:23.390599
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person("en")
    person.nationality()
    assert person.nationality() in PERSON_NATIONALITY_EN

test_Person_nationality()

# Generated at 2022-06-14 00:39:30.695473
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Check that all nationalities are distinct.
    assert len({Person().nationality() for i in range(100)}) == 100
    assert len({Person().nationality(Gender.FEMALE) for i in range(100)}) == 100
    assert len({Person().nationality(Gender.MALE) for i in range(100)}) == 100
    assert len({Person().nationality(Gender.NOT_STATED) for i in range(100)}) == 100


# Generated at 2022-06-14 00:39:37.055412
# Unit test for method surname of class Person
def test_Person_surname():
    person = PersonProvider()
    assert person.surname()
    assert isinstance(person.surname(), str)
    assert isinstance(person.surname(gender='male'), str)
    assert isinstance(person.surname(gender='female'), str)
    assert isinstance(person.surname(gender=Gender.MALE), str)
    assert isinstance(person.surname(gender=Gender.FEMALE), str)

    with pytest.raises(ValueError):
        person.surname(gender='undefined')

    with pytest.raises(NonEnumerableError):
        person.surname(gender=1)


# Generated at 2022-06-14 00:39:39.879275
# Unit test for method nationality of class Person
def test_Person_nationality():
    i = 0
    while i < 10:
        x = Person()
        assert isinstance(x.nationality(), str)
        i += 1


# Generated at 2022-06-14 00:39:44.057557
# Unit test for method nationality of class Person
def test_Person_nationality():
    with pytest.raises(NonEnumerableError):
        assert Person().nationality(gender='invalid')



# Generated at 2022-06-14 00:39:48.813280
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person(seed=42)
    assert p.surname('male') == 'Петров'
    assert p.surname() == 'Могилевская'
    assert p.surname('female') == 'Балуева'


# Generated at 2022-06-14 00:39:52.305463
# Unit test for method nationality of class Person
def test_Person_nationality():
    pass



# Generated at 2022-06-14 00:39:54.519271
# Unit test for method surname of class Person
def test_Person_surname():
    Person = Person()
    assert Person.surname() in SURNAMES
#######


# Generated at 2022-06-14 00:39:58.560018
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert isinstance(surname, str) == True


# Generated at 2022-06-14 00:41:44.540596
# Unit test for method nationality of class Person
def test_Person_nationality():
    # create a random instance of Person class
    p = Person()
    # test the method nationality
    assert (p.nationality() is not None)
    assert (p.nationality(Gender.MALE) is not None)
    assert (p.nationality(Gender.FEMALE) is not None)

# Generated at 2022-06-14 00:41:53.200159
# Unit test for method surname of class Person
def test_Person_surname():
    # check if method surname works well
    person = Person()
    surname = person.surname()
    assert person.surname(gender=Gender.FEMALE) in person._data['surname']['female']
    assert surname in person._data['surname']['male']
    assert person.last_name(gender=Gender.MALE) in person._data['surname']['male']
    assert surname != None
    assert type(surname) == str


# Generated at 2022-06-14 00:41:56.394179
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=10)
    assert 'Смирнов' == person.surname()
    # Unit test for method last_name of class Person

# Generated at 2022-06-14 00:42:00.305227
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)


# Generated at 2022-06-14 00:42:06.863669
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Unit test for method nationality of class Person."""
    for gender in Gender:
        for _ in range(10):
            value = get_random_item(Person, method_name='nationality',
                                    args=(gender,))
            assert value in Person(seed=SEED)._data['nationality'][gender]

    value = get_random_item(Person, method_name='nationality')
    assert value in Person(seed=SEED)._data['nationality']


# Generated at 2022-06-14 00:42:09.916224
# Unit test for method nationality of class Person
def test_Person_nationality():
    person_obj = faker.Faker().Person()
    assert person_obj.nationality() != person_obj.nationality()



# Generated at 2022-06-14 00:42:12.754585
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() != ""

# Generated at 2022-06-14 00:42:22.903719
# Unit test for method nationality of class Person
def test_Person_nationality():
    clock = MockClock(datetime(2017, 1, 1, 11, 11, 11))
    generator = Generator(clock=clock, random=SystemRandom())

    locales = Locales.from_available()
    person = Person(generator=generator, locales=locales)
    from enum import Enum, auto
    class Gender(Enum):
        FEMALE = auto()
        MALE = auto()
        NOT_APPLICABLE = auto()
        NOT_KNOWN = auto()
        PREFER_NOT_TO_SAY = auto()

    NATIONALITY_FEMALE = person.nationality(Gender.FEMALE)
    assert NATIONALITY_FEMALE == 'algerian'

    NATIONALITY_MALE = person.nationality(Gender.MALE)
    assert NATIONALITY_MALE == 'american'

# Generated at 2022-06-14 00:42:33.028229
# Unit test for method username of class Person
def test_Person_username():
    testdata = [
        ('U_d', True),
        ('U.d', True),
        ('U-d', True),
        ('UU-d', True),
        ('UU.d', True),
        ('UU_d', True),
        ('ld', True),
        ('l-d', True),
        ('Ud', True),
        ('l.d', True),
        ('l_d', True),
        ('default', True),
        ('#', False),
        ('###', False),
        ('A1', False),
        ('', False),
    ]

    rnd = random.Random(0)

    for template, success in testdata:
        person = Person(random=rnd)
        if success:
            person.username(template=template)

# Generated at 2022-06-14 00:42:40.804925
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=42)
    names = [person.surname() for i in range(100)]

# Generated at 2022-06-14 00:43:02.590236
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        assert Person().nationality() in NATIONALITIES

# Generated at 2022-06-14 00:43:16.607661
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person(seed=4)

    results = []
    for _ in range(100000):
        results.append(p.surname())

    assert 'Андрейкин' in results
    assert 'Сидоров' in results
    assert 'Соболев' in results
    assert 'Егоров' in results
    assert 'Альфиров' in results
    assert 'Софрон' in results
    assert 'Акимов' in results
    assert 'Гусаков' in results
    assert 'Баранов' in results
    assert 'Платов' in results

    # Test for gender

# Generated at 2022-06-14 00:43:21.916255
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    email = person.email()
    assert re.match(r"[a-zA-Z0-9_\.]+@[a-zA-Z0-9\-]+\.[a-z]+", email) is not None



# Generated at 2022-06-14 00:43:35.045264
# Unit test for method email of class Person
def test_Person_email():
    example = Person()
    # Test case 1 - non unique email
    res = example.email()
    assert type(res) == str
    assert not res.__contains__('+')
    assert not res.__contains__('{')
    # Test case 2 - unique email
    res = example.email(unique=True)
    assert type(res) == str
    assert not res.__contains__('+')
    assert not res.__contains__('{')
    # Test case 3 - unique email with seed
    example = Person(seed=0)
    res = example.email(unique=True)
    assert res == '1@aol.com'
    assert type(res) == str
    assert not res.__contains__('+')
    assert not res.__contains__('{')
    # Test

# Generated at 2022-06-14 00:43:47.301443
# Unit test for method email of class Person
def test_Person_email():
    sample_data = [
        'hongsheng@gmail.com',
        'jason_hongsheng@hotmail.com',
        'jason_hongsheng@live.com',
        'jason_hongsheng@yahoo.com',
        'jason_hongsheng@aol.com',
        'jason_hongsheng@yandex.ru',
        'jason_hongsheng@mail.ru',
        'jason_hongsheng@inbox.ru',
        'jason_hongsheng@list.ru',
        'jason_hongsheng@bk.ru',
    ]
    person = Person()
    for email in sample_data:
        assert person.email() in sample_data

# Generated at 2022-06-14 00:44:04.350936
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Unit test for method nationality of class Person.

    See :py:data:`test_data.test_Person.test_Person_nationality` for details.
    """
    from .test_data import test_Person

    # Initialize class Person
    p = Person(seed=8)
    # Get nationalities for gender Male
    nationalities_male = p.nationality(
        gender=Gender.Male
    )
    # Get nationalities for gender Female
    nationalities_female = p.nationality(
        gender=Gender.Female
    )
    # Get nationalities for gender None
    nationalities_none = p.nationality()

    assert nationalities_male == Gender.Male.value, (
        'Failed to get nationalities for gender "Male" with seed = 8'
    )

# Generated at 2022-06-14 00:44:05.799564
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert isinstance(p.nationality(), str)


# Generated at 2022-06-14 00:44:09.218227
# Unit test for method username of class Person
def test_Person_username():
    p = randomgen.Person(seed=None)
    assert p.username()
result = test_Person_username()
print(result)
 

# Generated at 2022-06-14 00:44:12.269272
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(seed=1)
    assert p.nationality() == 'Russian'
    assert p.nationality() == 'Russian'



# Generated at 2022-06-14 00:44:15.000747
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert isinstance(nationality, str)



# Generated at 2022-06-14 00:45:31.255656
# Unit test for method surname of class Person
def test_Person_surname():
    # Setup
    from faker import Faker
    from faker.providers.person.vi_VN import Provider as PersonProvider
    rnd = Random()
    rnd.seed(0)
    fake = Faker()
    fake.add_provider(PersonProvider)

    # Exercise
    result = fake.surname()

    # Verify
    assert result == 'Trần'

    # Cleanup - none necessary



# Generated at 2022-06-14 00:45:33.515266
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        _ = Generator().nationality()
        _ = Generator().nationality(gender=Gender.MALE)
        _ = Generator().nationality(gender=Gender.FEMALE)


# Generated at 2022-06-14 00:45:36.115077
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person.nationality()
    assert p



# Generated at 2022-06-14 00:45:39.355337
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert isinstance(Person().nationality(), str)
    assert Person().nationality() in NATIONALITIES


# Generated at 2022-06-14 00:45:43.100174
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert person.surname(gender=Gender.MALE) == "Петров"


# Generated at 2022-06-14 00:45:46.559006
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(random=Random(6))
    nationalities = person.nationality(Gender.MALE)
    assert nationalities == 'British', f"Expected 'British', got '{nationalities}' instead"



# Generated at 2022-06-14 00:45:48.056417
# Unit test for method surname of class Person
def test_Person_surname():
    from names import Person
    p = Person()
    surname = p.surname()
    assert surname

# Generated at 2022-06-14 00:45:52.078460
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(10):
        surname = factory.surname()
        assert isinstance(surname, str)
        assert surname


# Generated at 2022-06-14 00:45:54.695839
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    result = person.surname()
    assert isinstance(result, str)


# Generated at 2022-06-14 00:45:56.682514
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert nationality == 'Russian'
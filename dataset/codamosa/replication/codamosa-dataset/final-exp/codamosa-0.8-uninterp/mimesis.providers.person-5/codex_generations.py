

# Generated at 2022-06-14 00:36:32.936706
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()

    surname = person.surname()
    assert isinstance(surname, str)
    assert len(surname) >= 1

    surname = person.surname(gender=Gender.MALE)
    assert isinstance(surname, str)
    assert len(surname) >= 1

    surname = person.surname(gender=Gender.FEMALE)
    assert isinstance(surname, str)
    assert len(surname) >= 1

    try:
        surname = person.surname(gender=int(Gender.MALE))
    except NonEnumerableError:
        pass
    else:
        assert False, "NonEnumerableError wasn't raised"


# Generated at 2022-06-14 00:36:42.932986
# Unit test for method gender of class Person
def test_Person_gender():
    random.seed(0)
    p = Person(seed=0)
    test_count = 100

    for i in range(test_count):
        assert p.gender() in [
            'Male',
            'Female',
        ]

    for i in range(test_count):
        assert p.gender(iso5218=True) in [
            0, 1, 2, 9
        ]

    for i in range(test_count):
        assert p.gender(symbol=True) in [
            '♂',
            '♀',
            '⚤',
            '⚢',
            '⚣',
            '⚥',
            '⚦',
            '⚧',
            '⚨',
        ]



# Generated at 2022-06-14 00:36:51.264065
# Unit test for method surname of class Person
def test_Person_surname():
    from random import Random
    from datetime import datetime

    class MyRandom(Random):
        def __init__(self, seed):
            self.seed = seed
            super().__init__()


# Generated at 2022-06-14 00:36:56.959091
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() != ""
    assert Person().nationality(Gender.MALE) != ""
    assert Person().nationality() not in NATIONALITY_MALE
    assert Person().nationality(Gender.MALE) in NATIONALITY_MALE


# Generated at 2022-06-14 00:37:03.204751
# Unit test for method email of class Person
def test_Person_email():
    person = Person(random.Random())
    for _ in range(0, 200):
        assert(re.fullmatch(r'^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$', person.email()))


# Generated at 2022-06-14 00:37:04.980039
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(10):
        surname = Person().surname()
        assert surname in SURNAMES

# Generated at 2022-06-14 00:37:06.550327
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() != None

# Generated at 2022-06-14 00:37:10.736673
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person
    gender = Gender
    nationalities = p.nationality(gender)
    gender_male = gender.MALE
    gender_female = gender.FEMALE
    print("This is your gender:", gender_male)
    print("This is your nationality:", gender_female)


# Generated at 2022-06-14 00:37:20.176955
# Unit test for method surname of class Person
def test_Person_surname():
    # two or more surnames possible
    surnames_dict = {
        Gender.FEMALE: ['Авдошина', 'Агапова'],
        Gender.MALE: ['Авдошин', 'Агапов'],
    }
    surnames_list = ['Авдошина', 'Агапова']
    surnames_string = 'Авдошина'

    # Check whether one of the surnames from the dictionary is output
    person = Person('ru')
    assert person.surname(Gender.FEMALE) in surnames_dict[Gender.FEMALE]

    # Check for passing a dictionary with surnames separated by gender
    person

# Generated at 2022-06-14 00:37:22.647852
# Unit test for method email of class Person
def test_Person_email():
    global Person
    global random
    random = Random()
    Person = Person(random=random)
    assert Person.email() == Person.email()

test_Person_email()

# Generated at 2022-06-14 00:37:31.509608
# Unit test for method email of class Person
def test_Person_email():
    provider = Person()
    result = provider.email()
    assert isinstance(result, str)


# Generated at 2022-06-14 00:37:44.389619
# Unit test for method surname of class Person
def test_Person_surname():
    # Surnames separated by gender.
    person = Person(surnames={"male": ["Иванов", "дешевый", "великий"], 
                              "female": ["Иванова", "плохая", "маленькая"]})
    assert isinstance(person.surname(gender=Gender.male), str)
    assert person.surname(gender=Gender.male) in ["Иванов", "дешевый", "великий"]
    assert isinstance(person.surname(gender=Gender.female), str)

# Generated at 2022-06-14 00:37:53.352940
# Unit test for method nationality of class Person
def test_Person_nationality():
    from hypothesis import settings
    from hypothesis import strategies as st
    from pydantic_generator.strategies import Enums
    from ..enums import Gender

    @settings(max_examples=250)
    @given(st.data())
    def test_Person_nationality(data):
        settings = data.draw(Enums(Gender))
        person = Person(locale='ru_RU')
        nationality = person.nationality(gender=settings)
        assert isinstance(nationality, str)
        assert len(nationality) > 1

    test_Person_nationality()

# Generated at 2022-06-14 00:37:57.352481
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(random.Random(0))

    assert person.nationality(Gender.MALE) == "Soviet"
    assert person.nationality(Gender.FEMALE) == "American"
    assert person.nationality() == "Italian"
    
    
    

# Generated at 2022-06-14 00:37:58.755056
# Unit test for method nationality of class Person
def test_Person_nationality():
   P = Person()
   assert isinstance(P.nationality(), str)

# Generated at 2022-06-14 00:38:01.646555
# Unit test for method nationality of class Person
def test_Person_nationality():
    m = Person().nationality()


# Generated at 2022-06-14 00:38:06.096109
# Unit test for method gender of class Person
def test_Person_gender():
    rnd = random.Random()
    person = Person(rnd)
    assert person.gender() in GENDER_TYPES
    return



# Generated at 2022-06-14 00:38:15.808131
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker.generator import Generator
    from faker.providers.person.en import Provider
    from faker.providers.address.en import Provider as AddressProvider
    from faker.providers.person.ru import Provider as RuProvider

    # A seed to reproduce the results.
    seed = 9664596182507

    # Create a generator with seed.
    generator = Generator()
    generator.add_provider(Provider)
    generator.add_provider(AddressProvider)
    generator.add_provider(RuProvider)
    generator.seed(seed)

    # Generate name.
    nationality = generator.nationality()

    assert type(nationality) == str
    assert nationality == 'Russian'


# Generated at 2022-06-14 00:38:17.567059
# Unit test for method gender of class Person
def test_Person_gender():
    generator = Generator()
    gender = generator.gender()
    assert gender in GENDER_TYPES


# Generated at 2022-06-14 00:38:21.348582
# Unit test for method nationality of class Person
def test_Person_nationality():
    from fakegen.enums import Gender

    person = Person()

    res = person.nationality()
    assert isinstance(res, str)

    res = person.nationality(gender=Gender.FEMALE)
    assert isinstance(res, str)

# Generated at 2022-06-14 00:38:39.913841
# Unit test for method nationality of class Person
def test_Person_nationality():
    person_nationality = Person().nationality()
    assert isinstance(person_nationality, str)
    return True


# Generated at 2022-06-14 00:38:44.244158
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=4545)
    actual = person.surname(gender=Gender.FEMALE)
    expected = 'Tugay'
    assert actual == expected


# Generated at 2022-06-14 00:38:49.041852
# Unit test for method surname of class Person
def test_Person_surname():
    # Create an instance of class Person
    person = Person()
    # Generate a random surname
    surname = person.surname()
    # Check that the generated surname is in the list of surnames
    ok_(surname in person._data["surname"])


# Generated at 2022-06-14 00:38:53.698713
# Unit test for method nationality of class Person
def test_Person_nationality():
    output = Person().nationality()
    assert isinstance(output,str)

# Generated at 2022-06-14 00:38:56.363814
# Unit test for method surname of class Person
def test_Person_surname():
    from ...enums import Gender

    r = Person(seed=1)
    r.surname(gender=Gender.MALE)
    r.surname(gender=Gender.FEMALE)



# Generated at 2022-06-14 00:39:04.525041
# Unit test for method surname of class Person
def test_Person_surname():
    # Check for correctness.
    for _ in range(100):
        surname = Person().surname()
        assert isinstance(surname, str), \
            "\"surname\" must be a string."
        assert len(surname) > 0, \
            "\"surname\" cannot be an empty string."

    # Check some surnames.
    surnames = (
        'Василенко',
        'Погорельський',
        'Кобзарь',
        'Руденко',
        'Маренко',
        'Македонський',
    )
    for surname in surnames:
        assert Person().surname

# Generated at 2022-06-14 00:39:09.079340
# Unit test for method surname of class Person
def test_Person_surname():
    # In this case the generator is initialized in the 
    # "standard" way (by default)
    generator = faker.Faker()
    # The generator generates data
    surname = generator.surname()
    # Test
    assert len(surname) >= 1



# Generated at 2022-06-14 00:39:11.645461
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert isinstance(surname, str)



# Generated at 2022-06-14 00:39:14.269383
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in Person._data['nationality']

# Generated at 2022-06-14 00:39:28.516908
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(['r', 'g'], seed=1337)
    assert p.nationality() == 'Indian'
    p = Person(['r', 'm'], seed=1337)
    assert p.nationality() == 'Polish'
    p = Person(['r', 'f'], seed=1337)
    assert p.nationality() == 'Mexican'
    p = Person(['r', 'i'], seed=1337)
    assert p.nationality() == 'Hindi'
    p = Person(['r', 'a'], seed=1337)
    assert p.nationality() == 'Jewish'
    p = Person(['r', 'e'], seed=1337)
    assert p.nationality() == 'French'

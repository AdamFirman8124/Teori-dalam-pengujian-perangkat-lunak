

# Generated at 2022-06-14 00:36:30.714989
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    name = person.username()
    email = person.email()
    assert str(name) in email

# Generated at 2022-06-14 00:36:36.721211
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=1234)
    surname = person.surname()
    assert surname == "Смирнов"
    surname = person.surname(Gender.FEMININE)
    assert surname == "Александрова"


# Generated at 2022-06-14 00:36:45.659831
# Unit test for method surname of class Person
def test_Person_surname():

    # initialization
    per = Person()

    # default
    surnames = per.surname()
    
    assert isinstance(surnames, str),\
           'test_Person_surname(): wrong type of surnames in default mode'

    # gender
    surnames = per.surname(Gender.MALE)
    
    assert isinstance(surnames, str),\
           'test_Person_surname(): wrong type of surnames in gender mode'

    # wrong gender
    try:
        per.surname('')
    except NonEnumerableError:
        pass
    else:
        raise AssertionError('test_Person_surname(): wrong gender')


# Generated at 2022-06-14 00:36:49.626021
# Unit test for method email of class Person
def test_Person_email():
    # Setup
    person = Person()
    # Exercise
    # Verify
    assert (person.email() == 'f.stolz@example.com')
    # Cleanup - none necessary



# Generated at 2022-06-14 00:36:57.303607
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname(Person()) in [
        'Майоров',
        'Борисов',
        'Дмитриев',
        'Артемьев',
        'Егорова',
        'Григорьева',
        'Елизавета',
        'Анна'
    ]

# Generated at 2022-06-14 00:37:02.355505
# Unit test for method surname of class Person
def test_Person_surname():
    name = Person()
    full_name = name.surname()
    assert isinstance(full_name,str)
    assert len(full_name) > 0
test_Person_surname()

# Generated at 2022-06-14 00:37:12.289618
# Unit test for method email of class Person
def test_Person_email():
    from .random_generators import RandomGenerator
    from .providers import BaseProvider
    from .enums import Gender

    person = Person(random=RandomGenerator())

    for i in range(20):
        # print(person.email())
        assert person.email()

    for i in range(20):
        # print(person.email(unique=True))
        assert person.email(unique=True)

    for i in range(20):
        # print(person.email(domains=('gmail.com', 'hotmail.com')))
        assert person.email(domains=('gmail.com', 'hotmail.com'))

    provider = BaseProvider(random=RandomGenerator())


# Generated at 2022-06-14 00:37:17.256575
# Unit test for method surname of class Person
def test_Person_surname():
    gen = Person()
    assert isinstance(gen.surname(), str)
    assert isinstance(gen.surname(gender=Gender.male), str)
    assert isinstance(gen.surname(gender=Gender.female), str)
    assert isinstance(gen.surname(gender=Gender.andriod), str)


# Generated at 2022-06-14 00:37:19.758624
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker import Faker
    fake = Faker()
    nationalities = fake.nationality()
    assert isinstance(nationalities, str)   

# Generated at 2022-06-14 00:37:26.818026
# Unit test for method nationality of class Person
def test_Person_nationality():
    r = Person()
    r = Person(seed=10)
    assert r.nationality() == 'Cherokee'
    assert r.nationality(gender='female') == 'Eskimo'
    assert r.nationality(gender='male') == 'Finnish'
    assert r.nationality(gender=Gender.Male) == 'Finnish'
    assert r.nationality(gender=Gender.Female) == 'Eskimo'

test_Person_nationality()

 

# Generated at 2022-06-14 00:37:56.704468
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person(seed=None)
    assert isinstance(p.surname(), str)

# Generated at 2022-06-14 00:37:59.205655
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    a = p.nationality()
    assert isinstance(a, str)
    assert len(a) > 0
    

# Generated at 2022-06-14 00:38:03.464180
# Unit test for method nationality of class Person
def test_Person_nationality():
    # create a instance
    person = Person()

    # test method nationality
    assert isinstance(person.nationality(), str)

# Generated at 2022-06-14 00:38:06.780262
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname()
person = Person()
person.surname()


# Generated at 2022-06-14 00:38:08.759493
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert isinstance(person.nationality(), str)


# Generated at 2022-06-14 00:38:10.969147
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert nationality, 'Method nationality should not be null.'



# Generated at 2022-06-14 00:38:16.438899
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=1)
    assert person.surname() in ('Нечаев', 'Лукьянов', 'Карпов', 'Антонов', 'Овчинников', 'Соколов')
    
test_Person_surname()

# Generated at 2022-06-14 00:38:17.695198
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person.nationality() in NATION[0]

# Generated at 2022-06-14 00:38:20.010564
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person('en')
    # print(person.nationality())
    assert person.nationality() in NATIONALITIES


# Generated at 2022-06-14 00:38:32.066785
# Unit test for method nationality of class Person
def test_Person_nationality():
    from fake_data.utils import enum


    @enum.unique
    class TestNationality(enum.Enum):
        russian = 0
        american = 1


    person = Person()

    nationalities_dict = {
        TestNationality.russian: 'russian',
        TestNationality.american: 'american',
    }

    person.nationality = nationalities_dict

    assert person.nationality(TestNationality.russian) == 'russian'
    assert person.nationality(TestNationality.american) == 'american'
    assert person.nationality(TestNationality.russian) == 'russian'
    assert person.nationality(TestNationality.american) == 'american'

# Generated at 2022-06-14 00:38:53.075755
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)
    assert len(person.surname()) > 0


# Generated at 2022-06-14 00:38:58.162415
# Unit test for method surname of class Person
def test_Person_surname():
    person = Provider(Person)
    surname = person.surname()
    print(surname)
    assert surname is not None
    assert isinstance(surname, str)
    assert surname.isalpha()
    assert surname.isdigit() == False
    

# Generated at 2022-06-14 00:39:07.523294
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person.create(seed=1234)
    assert person.surname('male') == 'Шилов'
    assert person.surname('female') == 'Прохорова'
    assert person.surname(Gender.male) == 'Шилов'
    assert person.surname(Gender.female) == 'Прохорова'
    assert person.surname(None) == 'Краснов'
    assert person.surname() == 'Краснов'

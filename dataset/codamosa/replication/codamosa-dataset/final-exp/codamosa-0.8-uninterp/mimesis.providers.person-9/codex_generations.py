

# Generated at 2022-06-14 00:36:37.730169
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    assert p.email(unique=False) == 'legalcousin96@yahoo.com'
    assert p.email(unique=True) == 'nigellabashirian32@hotmail.com'
    assert p.email(unique=True) != 'nigellabashirian32@hotmail.com'
    assert p.email(unique=True).startswith('q')
    assert p.email(unique=True).endswith('@hotmail.com')

# Generated at 2022-06-14 00:36:47.785883
# Unit test for method username of class Person
def test_Person_username():
    provider = Person()

# Generated at 2022-06-14 00:36:52.043817
# Unit test for method gender of class Person
def test_Person_gender():
    m = Person(random=Random())
    assert isinstance(m.gender(iso5218=True), int)
    assert isinstance(m.gender(), str)
    assert isinstance(m.gender(symbol=True), str)

    try:
        m.gender(iso5218=True, symbol=True)
    except TypeError:
        pass
    else:
        raise AssertionError(
            "Method Person.gender() can't use the symbol and iso5218 arguments "
            "together"
        )


# Generated at 2022-06-14 00:36:57.670081
# Unit test for method gender of class Person
def test_Person_gender():

    p = Person(seed=1)

    results = [p.gender() for _ in range(10)]

    assert results == ['Female', 'Male', 'Male', 'Female', 'Female',
                       'Male', 'Male', 'Female', 'Female', 'Female']


# Generated at 2022-06-14 00:37:00.130110
# Unit test for method email of class Person
def test_Person_email():
    assert Person().email() == 'georgenia_halter@yahoo.se'


# Generated at 2022-06-14 00:37:06.007489
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person('ru', seed=0)
    assert p.surname() == 'Скалкин'
    assert p.surname() == 'Снежных'
    assert p.surname() == 'Зайцев'


# Generated at 2022-06-14 00:37:07.562506
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    assert(provider.surname())


# Generated at 2022-06-14 00:37:12.921356
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    name = person.nationality()
    assert isinstance(name, str)


# Generated at 2022-06-14 00:37:22.879205
# Unit test for method email of class Person
def test_Person_email():
    from faker.providers.person.en_US import Provider
    from faker.providers.person.ru_RU import Provider as ProviderRu
    from faker.providers.person.es_ES import Provider as ProviderEs


    provider = Provider()
    faker = Factory.create('en_US')
    faker.add_provider(provider)

    print('\nTest for method email:', end='\n\n')

    print('1. Test with default domains:', end='\n\n')

    print('1.1. Seed: None')
    print('   1.1.1. Unique: False')
    print('   1.1.2. Unique: True')

    print('1.2. Seed: 10')
    print('   1.2.1. Unique: False')

# Generated at 2022-06-14 00:37:25.941815
# Unit test for method gender of class Person
def test_Person_gender():
    """Unit test of method gender of class Person"""
    gender = Person.provider().gender()
    assert gender in ('Male', 'Female', 'Other')

# Generated at 2022-06-14 00:37:49.291420
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), string_types)



# Generated at 2022-06-14 00:38:00.512357
# Unit test for method surname of class Person

# Generated at 2022-06-14 00:38:03.982796
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert isinstance(surname, str), 'Return type should be string'


# Generated at 2022-06-14 00:38:08.608586
# Unit test for method surname of class Person
def test_Person_surname():
    names = ['Иванов', 'Петров']
    p = Person(names)
    surname = p.surname()
    assert surname in names


# Generated at 2022-06-14 00:38:10.405770
# Unit test for method surname of class Person
def test_Person_surname():
    # Check if the function return a string
    assert isinstance(Person().surname(), str)


# Generated at 2022-06-14 00:38:15.851827
# Unit test for method email of class Person
def test_Person_email():
    p = Person(seed=1)

    assert p.email() == 'gveneziano1973@gmail.com'
    assert p.email(unique=True) == 'Randall.Haley@hotmail.com'
    assert p.email(['com', 'net']) == 'james_gilmore@hotmail.com'

 
# Unit tests for method social_media_profile of class Person

# Generated at 2022-06-14 00:38:20.004702
# Unit test for method nationality of class Person
def test_Person_nationality():
    """
    Test nationality method of gender
    """
    person = Person()
    assert isinstance(person.nationality(), str)
    assert isinstance(person.nationality(gender = Gender.FEMALE), str)
    assert isinstance(person.nationality(gender = Gender.MALE), str)

# Generated at 2022-06-14 00:38:27.029051
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person()
    g1 = p.gender()
    g2 = p.gender()
    g3 = p.gender()
    g4 = p.gender(symbol=True)
    g5 = p.gender(iso5218=True)
    assert(g1 in ('Male', 'Female'))
    assert(g2 in ('Male', 'Female'))
    assert(g3 in ('Male', 'Female'))
    assert(g4 in ('\u2642', '\u2640'))
    assert(g5 in (0, 1, 2, 9))
    for g in (g1, g2, g3, g4, g5):
        try:
            assert(g1 != g2 != g3 != g4 != g5 != g)
        except:
            return False
    return True
print

# Generated at 2022-06-14 00:38:30.423760
# Unit test for method nationality of class Person
def test_Person_nationality():
    value = Person().nationality()
    assert_equal(str, type(value))
    assert_true(len(value) != 0)

# Generated at 2022-06-14 00:38:37.000403
# Unit test for method nationality of class Person
def test_Person_nationality():
    for i in range(100):
        p = Person()
        assert isinstance(p.nationality(), str)
        assert p.nationality() in p._data['nationality']
        assert isinstance(p.nationality(Gender.MALE), str)
        assert isinstance(p.nationality(Gender.FEMALE), str)


# Generated at 2022-06-14 00:39:04.324397
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    nationality = person.nationality()
    assert nationality in person._data['nationality']


# Generated at 2022-06-14 00:39:11.097036
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    for i in range(100):
        assert person.surname() in sur_list
        assert person.surname(gender=Gender.FEMALE) in sur_list
        assert person.surname(gender=Gender.MALE) in sur_list
        assert person.surname(gender=Gender.UNDEFINED) in sur_list

# Generated at 2022-06-14 00:39:14.492423
# Unit test for method surname of class Person
def test_Person_surname():
    """Method surname of class Person."""
    person = Person()
    surname = person.surname()
    assert isinstance(surname, str)



# Generated at 2022-06-14 00:39:29.341438
# Unit test for method surname of class Person
def test_Person_surname():
    # Test with random number
    assert Person(seed=0).surname() == 'Шевцов'
    assert Person(seed=1).surname() == 'Шевченко'
    assert Person(seed=2).surname() == 'Шевчун'
    # Test with non-random number
    assert Person(seed=0).surname() == 'Шевцов'
    assert Person(seed=0).surname() == 'Шевцов'
    assert Person(seed=0).surname() == 'Шевцов'
    # Test with gender
    assert Person(seed=0).surname(Gender.MALE) == 'Шевцов'

# Generated at 2022-06-14 00:39:31.607897
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person(random=Random())
    gender = Gender.FEMALE
    surname = provider.surname(gender=gender)
    assert surname in surnames[gender]


# Generated at 2022-06-14 00:39:35.557874
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Create a sample template for Person class
    sample_data = {
        'nationality': ['Russian']
    }
    # Create a provider
    provider = Person(sample_data)
    # Call method nationality and save result
    result = provider.nationality()
    # The result must be Russian
    assert result == "Russian"

# Generated at 2022-06-14 00:39:44.553281
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    # Test with default domains
    n = 0
    while n < 100:
        n += 1
        assert re.match("[a-z]+\d+@[a-z]+\.com", p.email())
    # Test with custom domains
    custom_domains = ['some.com', 'other.com', 'next.com']
    n = 0
    while n < 100:
        n += 1
        assert re.match("[a-z]+\d+@[a-z]+\.(com|org|ru)", p.email(domains=custom_domains))


# Generated at 2022-06-14 00:39:46.093160
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    assert p.email() == p.email()


# Generated at 2022-06-14 00:39:50.032863
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(10):
        assert isinstance(Person().surname(), str)
# Code for testing module
if __name__ == "__main__":
    test_Person_surname()
    print("All tests were successful!")

__all__ = ['Person']

# Generated at 2022-06-14 00:40:00.490617
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person()

    # Integer
    assert provider.nationality(0) == 'Russian'
    assert provider.nationality(1) == 'Russian'
    assert provider.nationality(2) == 'Russian'

    # If a variable is an integer,
    # then it is automatically converted to an Enum object.
    assert provider.nationality(Gender.NOT_KNOWN) == 'Russian'
    assert provider.nationality(Gender(0)) == 'Russian'
    assert provider.nationality(Gender.MALE) == 'Russian'
    assert provider.nationality(Gender(1)) == 'Russian'
    assert provider.nationality(Gender.FEMALE) == 'Russian'
    assert provider.nationality(Gender(2)) == 'Russian'

    assert provider.nationality(Gender.NOT_APPLICABLE) == 'Russian'

# Generated at 2022-06-14 00:40:21.585995
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()

    assert person.surname()
    assert person.surname(gender=Gender.MALE)
    assert person.surname(gender=Gender.FEMALE)


# Generated at 2022-06-14 00:40:26.206868
# Unit test for method surname of class Person
def test_Person_surname():
    a = Person(seed=2).surname()
    b = Person(seed=2).surname()
    c = Person().surname()

    assert a == b
    assert not a == c

# Generated at 2022-06-14 00:40:28.752942
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    
    for _ in range(100):
        assert p.nationality() in p._data['nationality']


# Generated at 2022-06-14 00:40:36.207092
# Unit test for method email of class Person
def test_Person_email():
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # Check the availability of the necessary keys in the dictionary
    assert isinstance(Person.email, Callable)
    # Test random generation
    provider = Person()
    p1 = provider.email()
    p2 = provider.email()
    assert p1 != p2
    # Test unique generation
    provider = Person()
    p1 = provider.email(unique=True)
    p2 = provider.email(unique=True)
    assert p1 == timestamp + '1'
    assert p2 == timestamp + '2'
    p3 = provider.email(unique=True)
    assert p3 == timestamp + '3'


# Generated at 2022-06-14 00:40:42.996515
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Test for method nationality of class Person
    person = Person()

    # Test for function Person.nationality()
    assert type(person.nationality()) == str

    # Test for function Person.nationality() with parameter gender
    assert type(person.nationality(gender=Gender.MALE)) == str

    # Test for function Person.nationality() with parameter gender
    assert type(person.nationality(gender=Gender.FEMALE)) == str


# Generated at 2022-06-14 00:40:50.376747
# Unit test for method surname of class Person
def test_Person_surname():
    from faker import Faker
    from faker.providers.person.en_US import Provider
    from faker_e164.providers.person import E164PersonProvider

    fake = Faker()
    fake.add_provider(Provider)
    fake.add_provider(E164PersonProvider)
    assert fake.surname()
    assert fake.last_name()

# Generated at 2022-06-14 00:40:55.978322
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    for i in range(100):
        surname = provider.surname()
        assert surname in SURNAME


# Generated at 2022-06-14 00:41:10.169632
# Unit test for method username of class Person
def test_Person_username():
    print('Unit test for method username of class Person')
    p1 = Person(random=DiscreteRandom(seed=1))
    p2 = Person(random=Random(seed=1))
    p3 = Person(random=DiscreteRandom(seed=2))
    p4 = Person(random=Random(seed=2))
    test_username = Person(random=DiscreteRandom(seed=1))

    res1 = p1.username('U_d')
    res2 = p2.username('U_d')
    res3 = p3.username('U_d')
    res4 = p4.username('U_d')
    test_username.username('U_d')
    if res1 == test_username.username('U_d'):
        print('test1 is OK')

# Generated at 2022-06-14 00:41:12.519236
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=1)
    nationality = person.nationality()
    assert nationality == 'Russian'
# Test method nationality of class Person
test_Person_nationality()
 

# Generated at 2022-06-14 00:41:16.607237
# Unit test for method nationality of class Person
def test_Person_nationality():
    sample_dataset = Person().nationality()
    print(sample_dataset)

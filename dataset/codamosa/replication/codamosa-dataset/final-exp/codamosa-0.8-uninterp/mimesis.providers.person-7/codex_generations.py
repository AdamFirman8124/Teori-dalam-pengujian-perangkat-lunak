

# Generated at 2022-06-14 00:36:32.573509
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname(Gender.MALE) == 'Иванов'
    assert Person().surname(Gender.FEMALE) == 'Сидорова'
    assert Person().surname(Gender.ANDROGYNY) == 'Иванов'

# Generated at 2022-06-14 00:36:35.983400
# Unit test for method gender of class Person
def test_Person_gender():
    test_Person_gender_str = Person().gender()
    assert isinstance(test_Person_gender_str, str)

# Generated at 2022-06-14 00:36:39.397450
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert(p.nationality() == 'Russian')



# Generated at 2022-06-14 00:36:42.146805
# Unit test for method gender of class Person
def test_Person_gender():
    gender_func = Person.gender
    result = gender_func(mimesis())
    assert isinstance(result, str)

# Generated at 2022-06-14 00:36:45.042753
# Unit test for method gender of class Person
def test_Person_gender():
    person = Person()
    result = person.gender()
    assert result in GENDER

# Generated at 2022-06-14 00:36:50.027119
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    result1 = provider.surname()
    result2 = provider.surname()
    assert result1 != result2


# Generated at 2022-06-14 00:36:53.674764
# Unit test for method nationality of class Person
def test_Person_nationality():
    print('::: TESTING METHOD ::: nationality')
    for x in range(0, 10):
       assert Person().nationality() in NATIONALITIES

# Generated at 2022-06-14 00:36:59.236566
# Unit test for method nationality of class Person
def test_Person_nationality():
    # initialization
    r1 = Random()
    nationalities1 = r1.nationality()
    # test
    r2 = Random()
    nationalities2 = r2.nationality()
    assert nationalities1 == nationalities2, 'The nationalities are different'

# Generated at 2022-06-14 00:37:00.821772
# Unit test for method email of class Person
def test_Person_email():
    assert Person().email()


# Generated at 2022-06-14 00:37:06.352825
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    surname = provider.surname()
    assert type(surname) == str
    assert len(surname) > 5

# Generated at 2022-06-14 00:37:12.373229
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality(None) is not None

# Generated at 2022-06-14 00:37:14.727946
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    s = p.surname(Gender.MALE)
    assert s in p._data['surname_male']


# Generated at 2022-06-14 00:37:17.993763
# Unit test for method nationality of class Person
def test_Person_nationality():
    x = Person()
    assert x.nationality() in NATIONALITIES
    
test_Person_nationality()


# Generated at 2022-06-14 00:37:20.310675
# Unit test for method surname of class Person
def test_Person_surname():

    p = Person(seed=4785)

    assert p.surname(Gender.MALE) == 'Васильев'



# Generated at 2022-06-14 00:37:25.018772
# Unit test for method email of class Person
def test_Person_email():
    # Generate person:
    person = Person()
    # Get email from method and print it:
    email = person.email()
    print(email)
# Run the test:
if __name__ == '__main__':
    test_Person_email()

'''
adirosan@yahoo.com
'''


# Generated at 2022-06-14 00:37:29.640285
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname(Gender.MALE) in Person._data['surname']['male']
    assert Person().surname(Gender.FEMALE) in Person._data['surname']['female']


# Generated at 2022-06-14 00:37:33.472668
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(Person.Nationality.RU)
    for i in range(10):
        assert p.nationality() == 'Русский'
    return 'Person.nationality() - Ok'

print(test_Person_nationality())


# Generated at 2022-06-14 00:37:41.224124
# Unit test for method gender of class Person
def test_Person_gender():
    person = Person()
    gender = person.gender()
    assert gender in ['Male', 'Female', 'Other']

    gender = person.gender(symbol=True)
    assert gender in ['♂', '♀', '⚲']

    gender = person.gender(iso5218=True)
    assert gender in [0, 1, 2, 9]
    save_result(person, 'Person', 'gender')

# Generated at 2022-06-14 00:37:43.907842
# Unit test for method surname of class Person
def test_Person_surname():
    pass
    # p = Person()
    # for i in range(10000):
    #     pr = p.surname()
    #     assert type(pr) == str

# Generated at 2022-06-14 00:37:50.568557
# Unit test for method gender of class Person
def test_Person_gender():
    gender_symbol = True
    gender_iso5218 = False
    result = Person(seed=1).gender(symbol=gender_symbol,
                                   iso5218=gender_iso5218)
    expected = '♂'
    assert result == expected
    
    
test_Person_gender()

# Generated at 2022-06-14 00:38:03.574176
# Unit test for method email of class Person
def test_Person_email():
    person = Person()

    assert '@' in person.email()
    assert '.' in person.email()
    assert len(person.email()) is not None
    assert '@' in person.email('example.com')
    assert '.' in person.email('example.com')
    assert person.email('example.com').endswith('example.com')
    assert '@' in person.email(('example.com',))
    assert '.' in person.email(('example.com',))
    assert person.email(('example.com',)).endswith('example.com')
    assert '@' in person.email(['example.com'])
    assert '.' in person.email(['example.com'])
    assert person.email(['example.com']).endswith('example.com')


# Unit test

# Generated at 2022-06-14 00:38:08.245716
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    x=person.nationality()
    assert x is not None
    assert x is not ''
    assert type(x)==str
    print('Person.nationality - ok')

# Generated at 2022-06-14 00:38:12.382328
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Test for method nationality of class Person"""
    from datetime import datetime
    from random import seed
    from loremipsum import Generator

    seed(datetime.now())
    text = Generator().generate_sentence()
    assert len(text) > 0

# Generated at 2022-06-14 00:38:14.535349
# Unit test for method nationality of class Person
def test_Person_nationality():
    r = Person()
    r.nationality()
    res = r.nationality()
    assert isinstance(res, str)

# Generated at 2022-06-14 00:38:16.359001
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(10):
        assert isinstance(Person.surname(), str)

# Generated at 2022-06-14 00:38:20.049111
# Unit test for method surname of class Person
def test_Person_surname():
    # Set seed
    random.seed(4)
    # Create object
    person = faker.Person()
    # Check length
    assert len(person.surname()) == 7
    # Check type
    assert isinstance(person.surname(), str)


# Generated at 2022-06-14 00:38:26.310303
# Unit test for method nationality of class Person
def test_Person_nationality():
    import random
    from faker.providers.person.en_US import Provider as EnUsPerson
    
    p = Person(random.Random())
    assert p.nationality() in EnUsPerson.nationalities


# Generated at 2022-06-14 00:38:28.242154
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname is not None


# Generated at 2022-06-14 00:38:35.745649
# Unit test for method nationality of class Person
def test_Person_nationality():
    testing = [
        Армянская,
        Русская,
        Украинская
    ]
    obj = Generator()
    for i in range(0,len(testing)):
        assert testing[i] in obj._data['nationality']
test_Person_nationality()



# Generated at 2022-06-14 00:38:41.484726
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    n2 = person.nationality(gender=Gender.FEMALE)
    n3 = person.nationality(gender=Gender.MALE)
    assert n2 == "Russian"
    assert n3 == "Russian"

test_Person_nationality()

# Generated at 2022-06-14 00:39:29.907544
# Unit test for method surname of class Person
def test_Person_surname():
    from names import get_first_name

    person = Person('en')

    first_name = get_first_name(gender='female')
    surname = person.surname(gender='female')

    assert surname.endswith('a')

# Generated at 2022-06-14 00:39:31.299752
# Unit test for method email of class Person
def test_Person_email():
    result = Person().email()
    assert result == 'oabirch@telkomsa.net'


# Generated at 2022-06-14 00:39:35.230864
# Unit test for method surname of class Person
def test_Person_surname():
    pr = Person(seed=1)
    assert pr.surname() == 'Baranov'
    assert pr.surname(gender=Gender.MALE) == 'Baranov'
    assert pr.surname(gender=Gender.FEMALE) == 'Baranova'


# Generated at 2022-06-14 00:39:44.553132
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person(locale='en').surname()
    assert Person(locale='ru').surname()
    assert Person(locale='it').surname()
    assert Person(locale='de').surname()
    assert Person(locale='es').surname()
    assert Person(locale='pt').surname()
    assert Person(locale='fa').surname()
    assert Person(locale='fr').surname()
    assert Person(locale='he').surname()
    assert Person(locale='id').surname()

# Generated at 2022-06-14 00:39:46.614004
# Unit test for method nationality of class Person
def test_Person_nationality():
    # prepare objects
    person = Person(seed=0)
    # perform test
    nationality = person.nationality(gender=Gender.MALE)
    # perform assertion
    assert 'hongkong' == nationality


# Generated at 2022-06-14 00:39:48.813042
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=1234)
    assert person.nationality() == 'Armenian'


# Generated at 2022-06-14 00:39:53.629062
# Unit test for method surname of class Person
def test_Person_surname():
    # Init
    pr = Prank()
    p = Person(pr)
    # Test
    assert isinstance(p.surname(), str)


# Generated at 2022-06-14 00:40:06.908062
# Unit test for method nationality of class Person

# Generated at 2022-06-14 00:40:11.076455
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person()
    assert provider.nationality() in NATIONALITIES

# Generated at 2022-06-14 00:40:13.371283
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() in Person._data.get('surname')


# Generated at 2022-06-14 00:40:32.299424
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert isinstance(p.nationality(), str)

# Generated at 2022-06-14 00:40:36.422008
# Unit test for method nationality of class Person
def test_Person_nationality():
    print('Test for method "nationality" of class Person')

    for _ in range(100):
        nationality = Person().nationality()
        assert nationality in NATIONALITIES

    print('Tested successfully.')

    return 0

# Generated at 2022-06-14 00:40:38.762113
# Unit test for method nationality of class Person
def test_Person_nationality():
    obj = Person() 

    assert isinstance(obj.nationality(), str)

# Generated at 2022-06-14 00:40:41.796440
# Unit test for method email of class Person
def test_Person_email():
    data = (),
    msg = 'is not an instance of class Person'
    assert isinstance(Person(), Person), msg
    assert isinstance(Person().email(), str), msg


# Generated at 2022-06-14 00:40:47.384037
# Unit test for method username of class Person
def test_Person_username():
    data = [
        ['', 'l.d'],
        [None, 'l-d'],
        ['dU_', 'ddU_'],
        ['U', 'dd'],
        ['l', 'dd'],
        ['d', 'ld'],
        ['ld', 'ld'],
        ['dUd', 'dUd'],
    ]

    for template, default in data:
        print('template: {}, default: {}'.format(template, default))
        assert Person().username(template) != Person().username(template)


# Generated at 2022-06-14 00:40:48.653844
# Unit test for method nationality of class Person
def test_Person_nationality():
    nationality = Person().nationality
    assert nationality == 'Russian'


# Generated at 2022-06-14 00:40:50.574965
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    surname = p.surname()
    assert(surname)

# Generated at 2022-06-14 00:40:57.025890
# Unit test for method surname of class Person
def test_Person_surname():
    """
    This is a unit test for method surname of class Person
    """

# Generated at 2022-06-14 00:41:10.316236
# Unit test for method surname of class Person
def test_Person_surname():
    """Test method surname of class Person"""
    random_generator = Random()
    generator = random_generator.person()
    assert generator.surname() in SURNAMES
    assert generator.surname(
        gender=Gender.male
    ) in SURNAMES['male']
    assert generator.surname(
        gender=Gender.female
    ) in SURNAMES['female']
    assert generator.surname(
        gender='male'
    ) in SURNAMES['male']
    assert generator.surname(
        gender='female'
    ) in SURNAMES['female']
    assert generator.surname(
        gender='not_correct_value'
    ) in SURNAMES['male'] + SURNAMES['female']

# Generated at 2022-06-14 00:41:19.098682
# Unit test for method nationality of class Person
def test_Person_nationality():
    correct_count = 0
    for i in range(100):
        nationality = Person().nationality()
        assert nationality in NATIONALITIES, 'Not all nationalities are generated.'
        correct_count += 1
    assert correct_count == 100, "Method nationality of class Person is incorrect!"
    print('-> test_Person_nationality() ok.')

test_Person_nationality()


# Generated at 2022-06-14 00:41:41.974079
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        assert len(Person.nationality()) == 6 or len(Person.nationality()) == 7

# Generated at 2022-06-14 00:41:48.697776
# Unit test for method nationality of class Person
def test_Person_nationality():
    faker = Faker()

    assert faker.nationality() in NATIONALITIES
    assert faker.nationality(gender=Gender.MALE) in NATIONALITIES
    assert faker.nationality(gender=Gender.FEMALE) in NATIONALITIES

# Generated at 2022-06-14 00:41:56.702596
# Unit test for method email of class Person
def test_Person_email():
    
    # Arrange
    person = Person()
    
    # Act
    email1 = person.email()
    email2 = person.email()
    
    # Assert
    assert type(email1) is str
    assert type(email2) is str
    assert email1 == email2
    assert '@' in email1
    assert '.' in email1
    assert '@' in email2
    assert '.' in email2
    
    

# Generated at 2022-06-14 00:41:58.901546
# Unit test for method nationality of class Person
def test_Person_nationality():
    item_from_nationality = Person().nationality()
    assert item_from_nationality in NATIONALITIES


# Generated at 2022-06-14 00:42:08.725004
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person(seed=10)
    p.random.randstr = lambda n: ''.join(random.sample('abcdefgh', n))

    assert p.surname() == 'fdfa'
    assert p.surname(Gender.FEMALE) == 'cgh'
    assert p.surname('f') == 'bhee'
    assert p.surname(gender='male') == 'fheb'
    assert p.surname(gender=Gender.MALE) == 'eefg'

    assert p.surname([]) == ''
    assert p.surname({}) == ''

    with pytest.raises(NonEnumerableError) as e:
        p.surname('something')

# Generated at 2022-06-14 00:42:18.142080
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname() == 'Иванов'
    assert p.surname() == 'петров'
    assert p.surname() == 'Сидоров'
    assert p.surname(Gender.female) == 'Александровна'
    assert p.surname(Gender.female) == 'Петровна'
    assert p.surname(Gender.female) == 'Ивановна'

# Generated at 2022-06-14 00:42:25.737154
# Unit test for method surname of class Person

# Generated at 2022-06-14 00:42:29.756530
# Unit test for method email of class Person
def test_Person_email():
    assert Person.email(None, 'test') == 'test@test.test'
    assert Person.email(None, 'test', domains=('test.test',)) == 'test@test.test'


# Generated at 2022-06-14 00:42:35.103608
# Unit test for method nationality of class Person
def test_Person_nationality():
    '''
    Unit test for Person
    '''
    
    seed = 42
    nationalities = []
    with Person.create(seed=seed) as p:
        for _ in range(10):
            nationalities.append(p.nationality())

# Generated at 2022-06-14 00:42:38.324182
# Unit test for method surname of class Person
def test_Person_surname():
    pr = Person()
    for gender, surnames in pr._data['surname'].items():
        surname = pr.surname(gender)
        assert surname in surnames, "Surname {} is not in {}".format(
            surname, surnames
        )


# Generated at 2022-06-14 00:43:17.460698
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITIES



# Generated at 2022-06-14 00:43:23.521023
# Unit test for method nationality of class Person
def test_Person_nationality():
    from persona.exceptions import NonEnumerableError
    from persona.enums import Gender
    from persona.generators import Person

    p = Person()

    with pytest.raises(NonEnumerableError):
        p.nationality(Gender.unknown)
        
    x = p.nationality()
    assert x in p._data['nationality']
    
    x1 = p.nationality(Gender.male)
    assert x1 in p._data['nationality']['male']
    
    x2 = p.nationality(Gender.female)
    assert x2 in p._data['nationality']['female']


# Generated at 2022-06-14 00:43:31.374581
# Unit test for method surname of class Person
def test_Person_surname():
    from vedis import Vedis
    from faker.providers.person.ru_RU import Provider
    from faker.providers.person.en_US import Provider
    from faker.providers.person.uk_UA import Provider

    # Create DB and insert test values.
    db = Vedis(':memory:')

# Generated at 2022-06-14 00:43:36.797795
# Unit test for method nationality of class Person
def test_Person_nationality():
    person_gen = Person(random_state=1)
    print(person_gen.nationality())
    print(person_gen.nationality(gender=Gender.male))
    print(person_gen.nationality(gender=Gender.female))

# Generated at 2022-06-14 00:43:40.852353
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert isinstance(person.nationality(), str)
    assert len(person.nationality()) > 0


# Generated at 2022-06-14 00:43:44.525646
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    surname = p.surname(Gender.MALE)
    assert surname in p._data['surname'][Gender.MALE.value]
test_Person_surname()


# Generated at 2022-06-14 00:43:49.173510
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=123)
    assert person.nationality() == "Russian"
    assert person.nationality(gender=Gender.FEMALE) == "Russian"
    assert person.nationality(gender=Gender.MALE) == "Russian"

# Generated at 2022-06-14 00:43:53.551329
# Unit test for method surname of class Person
def test_Person_surname():
    from faker import Faker
    f = Faker()
    assert f.surname() == "Иванов"


# Generated at 2022-06-14 00:43:56.807362
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(10):
        assert isinstance(Person().nationality(), str)

# Generated at 2022-06-14 00:43:59.952083
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(10):
        assert len(Person().nationality()) >= 3


# Generated at 2022-06-14 00:45:11.429481
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname= person.surname()
    assert type(surname)==str
test_Person_surname()

# Generated at 2022-06-14 00:45:24.283001
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(
        'gh67fhd1fg2j3lkh4gf56hj7kl8i9op0',
        seed='3485tfn5gn45ngf4'
    )
    surnames = person.surnames_by_gender

# Generated at 2022-06-14 00:45:29.798610
# Unit test for method nationality of class Person
def test_Person_nationality():
    from . import Gender

    # Check the nationalities for male and female
    p = Person()
    assert p.nationality(Gender.FEMALE) in p._data['nationality'][Gender.FEMALE]
    assert p.nationality(Gender.MALE) in p._data['nationality'][Gender.MALE]

    # Check the nationalities for random gender
    for _ in range(100):
        assert p.nationality() in p._data['nationality']

# Generated at 2022-06-14 00:45:32.049768
# Unit test for method email of class Person
def test_Person_email():
    """Unit test for method email of class Person."""
    r = Person()
    r.email()
    r.email(unique=True)
    r.email(domains=['example.com'])


# Generated at 2022-06-14 00:45:37.494079
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person(random=Random())
    surname = provider.surname()
    assert isinstance(surname, str)
    assert len(surname) > 0


# Generated at 2022-06-14 00:45:41.681947
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    print(surname)
    
test_Person_surname()


# Generated at 2022-06-14 00:45:45.100532
# Unit test for method surname of class Person
def test_Person_surname():
    # The method was called
    surname = Person().surname()
    # The method returns a string
    assert isinstance(surname, str)
    # There is a surname
    assert surname in SURNAMES


# Generated at 2022-06-14 00:45:54.626648
# Unit test for method username of class Person
def test_Person_username():
    from faker.providers.person import Provider
    from faker.utils.random import get_random_element
    random = get_random_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # range 0..9
    if random == 0:
        assert Provider.username(None, 'U_d') == 'N_1879'
    elif random == 1:
        assert Provider.username(None, 'U.d') == 'G.1845'
    elif random == 2:
        assert Provider.username(None, 'U-d') == 'I-1869'
    elif random == 3:
        assert Provider.username(None, 'UU-d') == 'Oy-1847'

# Generated at 2022-06-14 00:45:59.764956
# Unit test for method email of class Person
def test_Person_email():
    assert Person().email() != Person().email()

    assert Person().email('gmail.com') != Person().email('gmail.com')

    email = Person(seed=2568).email('gmail.com')
    assert email == 'kimberley14@gmail.com'

# Generated at 2022-06-14 00:46:06.239279
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Unit test for method Person.nationality."""
    from random import seed

    person = Person(random=seed(1))
    assert ['Russian', 'Armenian', 'Ukrainian'] == person.nationality

    person = Person(random=seed(2))
    assert {
        Gender.FEMALE: ['Russian'],
        Gender.MALE: ['Armenian', 'Ukrainian'],
        Gender.BOTH: ['Russian', 'Armenian', 'Ukrainian'],
    } == person.nationality
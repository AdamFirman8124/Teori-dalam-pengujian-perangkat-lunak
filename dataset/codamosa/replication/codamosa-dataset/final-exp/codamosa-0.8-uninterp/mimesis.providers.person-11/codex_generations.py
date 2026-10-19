

# Generated at 2022-06-14 00:36:22.642444
# Unit test for method surname of class Person
def test_Person_surname():
    faker = Faker('uk_UA')
    assert faker.surname()


# Generated at 2022-06-14 00:36:30.858029
# Unit test for method gender of class Person
def test_Person_gender():
    for _ in range(100):
        assert Person().gender() in (
            'Male',
            'Female',
        )

    for _ in range(100):
        assert Person().gender(symbol=True) in (
            '♂',
            '♀',
        )

    for _ in range(100):
        assert Person().gender(iso5218=True) in (0, 1, 2, 9)
        assert isinstance(Person().gender(iso5218=True), int)



# Generated at 2022-06-14 00:36:45.262389
# Unit test for method email of class Person
def test_Person_email():
    p = Person()
    for _ in range(10):
        assert isinstance(p.email(), str)
        assert len(p.email().split('@')) == 2
        assert len(p.email().split('.')) == 2
if __name__ == '__main__':
    test_Person_email()
    print(Person().full_name())
    print(Person().username())
    print(Person().password())
    print(Person().email())
    print(Person().telephone())
    print(Person().height())
    print(Person().weight())
    print(Person().nationality())
    print(Person().identifier())
    print(Person().avatar())

# see a full list of available languages:
# http://www.loc.gov/standards/iso639-2/php/code_list.php

# Generated at 2022-06-14 00:36:48.062488
# Unit test for method username of class Person
def test_Person_username():
    person = Person(seed=42)
    assert person.username() == 'joseph.2017'

# Generated at 2022-06-14 00:36:54.475266
# Unit test for method gender of class Person
def test_Person_gender():
    """
    Unit test for method gender of class Person.
    :return: Nothing.
    """
    # Create a local variable «provider».
    provider = Person()
    # Get a random gender.
    gender = provider.gender()
    # Check result.
    assert gender in ('Male', 'Female')


# Generated at 2022-06-14 00:36:57.669828
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person()
    gender = p.gender()
    assert gender in GENDER_FULLNAMES


# Generated at 2022-06-14 00:37:02.232695
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert type(surname) == str
    assert len(surname) > 0


# Generated at 2022-06-14 00:37:10.884189
# Unit test for method nationality of class Person
def test_Person_nationality():
    globals_ = globals()
    p = Person(rnd=Random())
    # Test Item
    nationality = p.nationality(Gender.MALE)
    assert_true(nationality in globals_['NATIONALITIES'][0])
    # Test Item
    nationality = p.nationality(Gender.FEMALE)
    assert_true(nationality in globals_['NATIONALITIES'][1])
    # Test Item
    nationality = p.nationality()
    assert_true(nationality in globals_['NATIONALITIES'][0] or  
                nationality in globals_['NATIONALITIES'][1])
    

# Generated at 2022-06-14 00:37:14.700623
# Unit test for method nationality of class Person
def test_Person_nationality():
    # test
    person = Person('en')
    nationality = person.nationality()
    # expected
    expected = True
    # result
    result = nationality in ['German', 'French', 'English', 'Hungarian',
                             'Irish', 'Scottish', 'Welsh', 'Italian']
    # compare
    assert expected == result

# Generated at 2022-06-14 00:37:18.311484
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert len(surname) > 0
    assert isinstance(surname, str)


# Generated at 2022-06-14 00:37:31.295726
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person('ru')
    assert person.nationality() in person._data['nationality']
    assert person.nationality(gender=Gender.male) in person._data['nationality']['male']
    assert person.nationality(gender=Gender.female) in person._data['nationality']['female']


# Generated at 2022-06-14 00:37:33.552838
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname.__name__ == 'surname'
    print('test_Person_surname passed.')

# Generated at 2022-06-14 00:37:45.068399
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(1, 100):
        x = Person().surname()
        assert isinstance(x, str)

        x = Person().surname(gender=Gender.MALE)
        assert isinstance(x, str)

        x = Person().surname(gender=Gender.FEMALE)
        assert isinstance(x, str)

        x = Person().surname(gender=Gender.ZERO)
        assert isinstance(x, str)

        try:
            x = Person().surname(gender=Gender.__members__)
            assert False
        except NonEnumerableError:
            pass
        except Exception:
            assert False

if __name__ == '__main__':
    test_Person_surname()
 

# Generated at 2022-06-14 00:37:49.680205
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert (
        isinstance(p.nationality(), str) and
        p.nationality() in p._data['nationality']
    )


# Generated at 2022-06-14 00:37:55.362208
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    surname_masculine = p.surname(gender=Gender.MASCULINE)
    surname_feminine = p.surname(gender=Gender.FEMININE)
    surname = p.surname()
    assert surname == surname_masculine or surname == surname_feminine


# Generated at 2022-06-14 00:37:57.251412
# Unit test for method nationality of class Person
def test_Person_nationality():
	profile = Person()
	result = profile.nationality()
	print(result)
	assert True


# Generated at 2022-06-14 00:38:03.710263
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    result = person.nationality()
    assert isinstance(result, str)
    assert result in person._data["nationality"]
    assert result == person.nationality(gender=Gender.MALE)
    assert isinstance(person.nationality(gender=None), str)


# Generated at 2022-06-14 00:38:08.759744
# Unit test for method email of class Person
def test_Person_email():
    print("Test if Person().email() works")
    p = Person()

    for _ in range(100):
        email = p.email()

    assert isinstance(email, str)
    print("Success") 

# Generated at 2022-06-14 00:38:10.723328
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Example of unit test."""
    instance = Person()
    value = instance.nationality()
    assert value == 'US', value

# Generated at 2022-06-14 00:38:14.704792
# Unit test for method surname of class Person
def test_Person_surname():
    person_obj = Person()
    person_obj.random.seed(0)
    first_name = person_obj.surname()
    assert first_name == 'Натурилья'


# Generated at 2022-06-14 00:38:23.267667
# Unit test for method surname of class Person
def test_Person_surname():
    print('Test Person.surname')
    rnd = Random()
    person = Person(random=rnd)
    assert isinstance(person.surname(), str)
    assert person.surname().isalpha()
    assert len(person.surname()) >= 3
    assert person.surname() in person._data['surnames']

# Generated at 2022-06-14 00:38:36.025427
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()

    assert isinstance(person.surname(), str)
    assert person.surname() != person.surname()

    person = Person(random=Random())

    assert isinstance(person.surname(), str)
    assert person.surname() == person.surname()

    person = Person(data={
        'first_name': {'male': ['John']},
        'last_name': {'male': ['Doe'], 'female': ['Doe']},
    })

    assert isinstance(person.surname(), str)
    assert person.surname() == 'Doe'


# Generated at 2022-06-14 00:38:43.471919
# Unit test for method surname of class Person
def test_Person_surname():
    assert len(Person().surname()) >= 2
    assert len(Person().surname(gender='male')) >= 2
    assert len(Person().surname(gender='female')) >= 2
    assert not re.findall(r'[A-Z]', Person().surname())
    assert len(Person().surname(gender='male')) >= 2
    assert not re.findall(r'[A-Z]', Person().surname(gender='female'))



# Generated at 2022-06-14 00:38:50.479525
# Unit test for method surname of class Person
def test_Person_surname():
    provider = PersonProvider()

    # Check default data
    assert provider.surname()

    # Check custom data
    provider = PersonProvider(provider='ru')

    assert provider.surname()
    assert provider.surname()
    assert provider.surname()

    provider = PersonProvider(provider='en')

    assert provider.surname()
    assert provider.surname()
    assert provider.surname()

# Generated at 2022-06-14 00:39:00.539781
# Unit test for method surname of class Person
def test_Person_surname():
    test_for_surname = Person(seed=1234567890)
    assert(test_for_surname.surname() == "Abraham")
    assert(test_for_surname.surname(Gender.MALE) == "Abraham")
    assert(test_for_surname.surname(Gender.FEMALE) == "Abrams")

    assert(test_for_surname.surname() == "Abraham")
    assert(test_for_surname.surname() == "Abraham")
    assert(test_for_surname.surname() == "Abraham")


# Generated at 2022-06-14 00:39:01.731015
# Unit test for method nationality of class Person
def test_Person_nationality():
    nationalities = Person().nationality()
    assert nationalities in nationalitylist
                        

# Generated at 2022-06-14 00:39:04.489398
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    n = p.nationality()
    assert n in p._data['nationality']
    

# Generated at 2022-06-14 00:39:08.328688
# Unit test for method surname of class Person
def test_Person_surname():
    pr = Provider()

    for i in range(10):
        surname = pr.surname()
        assert isinstance(surname, str)
        assert surname in SURNAMES

# Generated at 2022-06-14 00:39:14.620814
# Unit test for method email of class Person
def test_Person_email():
    # Create object of class Person
    obj = Person()
    # Get random email
    result = obj.email()
    # Check that result is string
    assert isinstance(result, str)
    # Check that result is email
    assert re.match(r'[^@]+@[^@]+\.[^@]+', result)

# Generated at 2022-06-14 00:39:17.046381
# Unit test for method nationality of class Person
def test_Person_nationality():
    n = Person().nationality()
    assert n



# Generated at 2022-06-14 00:39:31.194591
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname()

# Generated at 2022-06-14 00:39:35.904272
# Unit test for method nationality of class Person
def test_Person_nationality():
    with pytest.raises(NonEnumerableError):
        Person().nationality(gender=10)

    assert Person().nationality(gender=Gender.FEMALE) in NATIONALITIES_FEMALE
    assert Person().nationality(gender=Gender.MALE) in NATIONALITIES_MALE
    assert Person().nationality(gender=None) in NATIONALITIES_MALE



# Generated at 2022-06-14 00:39:37.643580
# Unit test for method surname of class Person
def test_Person_surname():
    result = Person().surname()
    assert result in SURNAME
    assert len(result) > 0


# Generated at 2022-06-14 00:39:43.301434
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker import Factory
    from faker.providers.person.hu_HU import Provider as HuProvider
    from faker.providers.person.zh_CN import Provider as ZhProvider
    from faker.providers.person.es_ES import Provider as EsProvider

    # Check that nationality is required
    fake = Factory.create()
    assert isinstance(fake.nationality(), str)

    # Check that nationality is random value
    value_a = fake.nationality()
    value_b = fake.nationality()
    assert value_a != value_b

    # Check that nationality can return different value
    # based on Gender
    fake = Factory.create(locale='hu_HU')
    assert isinstance(fake.nationality(Gender.FEMALE), str)

# Generated at 2022-06-14 00:39:51.610130
# Unit test for method surname of class Person
def test_Person_surname():
    # generate a global random object to use the same value in every function
    random = Faker.Faker()

    # call test function

# Generated at 2022-06-14 00:39:54.082155
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITIES


# Generated at 2022-06-14 00:39:56.659393
# Unit test for method nationality of class Person
def test_Person_nationality():
    x = Person(seed=42)
    assert x.nationality() == 'Russian'

# Generated at 2022-06-14 00:39:59.946578
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    nationalities = p._data['nationality']
    result = p.nationality()
    assert result in nationalities


# Generated at 2022-06-14 00:40:06.909462
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Create new instance of Person class
    per = Person()
    # Get value for test
    result = per.nationality()
    # Test result
    assert result in per._data["nationality"]


# Generated at 2022-06-14 00:40:20.499600
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Unit tests for class Person: test nationality.
    # Prepare data.
    seed = 1234
    rnd = Random()
    rnd.seed(seed)
    person = Person(seed=seed)

    # Get a random Russian nationality.
    nationality = person.nationality()
    assert nationality == 'Russian'
    assert nationality == 'Russian'

    # Get a random English nationality.
    nationality = person.nationality()
    assert nationality == 'English'

    # Get a random view on.
    with pytest.raises(NonEnumerableError):
        person.nationality('Wrong value.')

    # Get a random German nationality.
    nationality = person.nationality()
    assert nationality == 'German'

# Generated at 2022-06-14 00:40:43.785782
# Unit test for method surname of class Person
def test_Person_surname():
    a = Person()
    assert a.surname(Gender.Male) in SURNAMES_MALE
    assert a.surname(Gender.Female) in SURNAMES_FEMALE


# Generated at 2022-06-14 00:40:46.682600
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in person._data['nationality']


# Generated at 2022-06-14 00:40:53.259762
# Unit test for method nationality of class Person
def test_Person_nationality():
    allure.dynamic.description("""
        Person generator unit test
            - nationality method
    """)
    allure.dynamic.title("Person method nationality")
    allure.dynamic.severity(allure.severity_level.CRITICAL)

    with allure.step("Generate a random nationality and check the result"):
        person = Person()
        result = person.nationality()
        assert result in list(*person._data.values())



# Generated at 2022-06-14 00:41:07.703222
# Unit test for method nationality of class Person
def test_Person_nationality():
    from datagenpy.base import get_random_item

    NATIONALITIES = tuple(Person._data['nationality'])   # Russian, Spanish
    n = Person()

    gender = get_random_item(Gender, rnd=n.random)
    gender_str = gender._value_ if isinstance(gender, Gender) else gender
    # print(gender_str)

    t = n.nationality(gender=gender)
    #print(t)

    assert t in NATIONALITIES
    assert t in NATIONALITIES
    assert t in NATIONALITIES
test_Person_nationality()

assert Person().nationality() in Person._data['nationality']
assert Person().nationality(Gender.FEMALE) in Person._data['nationality']
assert Person().nationality(Gender.MALE) in Person._data['nationality']
p

# Generated at 2022-06-14 00:41:13.197761
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(10):
        surnames = ('Черепанова', 'Перфильева', 'Грибанов', 'Игнатов', 'Царев')
        person = Person()
        assert person.surname() in surnames



# Generated at 2022-06-14 00:41:17.396399
# Unit test for method nationality of class Person
def test_Person_nationality():
    # create a random Person object
    data = Person()
    # call the method nationality of object data
    result = data.nationality()
    # check the type of result
    assert isinstance(result,str)

# Generated at 2022-06-14 00:41:20.143565
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    assert person.email() == "krbatty@hotmail.com"

# Generated at 2022-06-14 00:41:23.845991
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person('ru')
    assert isinstance(person.surname, str)
    assert isinstance(person.surname(gender=Gender.male), str)


# Generated at 2022-06-14 00:41:28.508806
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person
    assert provider.surname()
    assert provider.surname(gender=Gender.male) in provider.surname
    assert provider.surname(gender=Gender.female) in provider.surname


# Generated at 2022-06-14 00:41:30.090156
# Unit test for method nationality of class Person
def test_Person_nationality():
    obj = Person()
    assert obj.nationality() in obj._data['nationality']


# Generated at 2022-06-14 00:41:53.655141
# Unit test for method nationality of class Person
def test_Person_nationality():
    for i in range(100):
        assert isinstance(Person().nationality(), str)
test_Person_nationality()


# Generated at 2022-06-14 00:41:56.592619
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname(Gender.MALE) in list_of_data['male_surnames']
    assert Person().surname(Gender.FEMALE) in list_of_data['female_surnames']


# Generated at 2022-06-14 00:41:58.198425
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert type(Person().nationality()) == str

# Generated at 2022-06-14 00:42:05.855127
# Unit test for method nationality of class Person
def test_Person_nationality():
    person_a = Person(locale='ru_RU')
    person_b = Person(locale='en_US')
    nationalities_a = [person_a.nationality() for i in range(100)]
    nationalities_b = [person_b.nationality() for i in range(100)]
    for i in nationalities_a:
        print(i)
        
test_Person_nationality()

print("\n")

for i in nationalities_b:
    print(i)


# Generated at 2022-06-14 00:42:18.265049
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker.providers.person.ru_RU import person
    from faker import Faker
    Faker.seed(0)
    f = Faker('ru_RU')
    f.add_provider(person)
    assert f.nationality(person.Gender.MALE) == 'Русский'
    Faker.seed(0)
    assert f.nationality(person.Gender.MALE) == 'Русский'
    Faker.seed(1)
    assert f.nationality(person.Gender.MALE) == 'Украинец'
    Faker.seed(2)
    assert f.nationality(person.Gender.MALE) == 'Белорус'

# Generated at 2022-06-14 00:42:20.735588
# Unit test for method nationality of class Person
def test_Person_nationality():
    global gender
    global nationality
    global Person
    gender = fake.gender
    nationality = fake.nationality
    Person = fake.Person(gender, nationality)
    assert_type(Person, Person)



# Generated at 2022-06-14 00:42:32.055384
# Unit test for method username of class Person
def test_Person_username():
    prv = Person()
    assert 'U_d' in prv._data['username_fmt']
    assert 'U.d' in prv._data['username_fmt']
    assert 'U-d' in prv._data['username_fmt']
    assert 'UU-d' in prv._data['username_fmt']
    assert 'UU.d' in prv._data['username_fmt']
    assert 'UU_d' in prv._data['username_fmt']
    assert 'ld' in prv._data['username_fmt']
    assert 'l-d' in prv._data['username_fmt']
    assert 'Ud' in prv._data['username_fmt']
    assert 'l.d' in prv._data['username_fmt']

# Generated at 2022-06-14 00:42:38.227720
# Unit test for method surname of class Person
def test_Person_surname():
    surname = Person().surname(Gender.MALE)
    assert surname in Person._data['surname']['male']

    surname = Person().surname(Gender.FEMALE)
    assert surname in Person._data['surname']['female']

    surname = Person().surname(Gender.ANDROGYNOUS)
    assert surname in Person._data['surname']['androg']
test_Person_surname()

# Generated at 2022-06-14 00:42:41.479516
# Unit test for method surname of class Person
def test_Person_surname():
    print('Test for method "surname"')
    provider = Person()
    print(provider.surname())


# Generated at 2022-06-14 00:42:46.354369
# Unit test for method nationality of class Person
def test_Person_nationality():
    name_nat = [np.random.choice(Person().nationality()) for _ in range(1000)]
    assert(len(np.unique(name_nat))>10)
    

# Generated at 2022-06-14 00:43:34.150523
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert isinstance(Person().nationality(),str)
    assert isinstance(Person().nationality(Gender.Male),str)
    assert isinstance(Person().nationality(Gender.Female),str)

# Generated at 2022-06-14 00:43:45.430085
# Unit test for method email of class Person
def test_Person_email():
    from datagenerator.generators.bases.base import RandomTestCase
    from datagenerator.generators.simulation.person import Person
    class PersonTestCase(RandomTestCase):
        def test_Person_basic(self):
            Person(random=self._random)

        def test_Person_email(self):
            person = Person(random=self._random)
            email = person.email()
            self.assertNotEqual(email, '')
            self.assertNotEqual(email, None)
            self.assertIsInstance(email, str)
            self.assertFalse(email.startswith('@'))

        def test_Person_email_with_domain(self):
            domains = ('@gmail.com',)
            person = Person(random=self._random)

# Generated at 2022-06-14 00:43:53.814150
# Unit test for method email of class Person
def test_Person_email():
    # Tests for specific values in a list of emails
    for email in [
        'c-koch@hotmail.com',
        'foretime10@live.com',
        'fernando-hernandez@gmail.com',
        'samuel-phillips@hotmail.com',
        'carolyn-west@gmail.com',
    ]:
        assert email in Person().email(unique=True, count=5)
test_Person_email()

# Generated at 2022-06-14 00:43:56.367398
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert type(p.nationality()) is str

# Generated at 2022-06-14 00:44:11.001779
# Unit test for method surname of class Person
def test_Person_surname():
    # Case 1
    person = Person()
    # Test 1
    assert(person.surname() in person._data['surname'])
    # Test 2
    assert(person.surname(gender=Gender.male) in person._data['surname'])
    # Test 3
    assert(person.surname(gender=Gender.female) in person._data['surname'])

    # Case 2
    person = Person(surnames={
        Gender.male: ['Стасюк'],
        Gender.female: ['Марія'],
    })
    # Test 1
    assert(person.surname() in ['Стасюк', 'Марія'])
    # Test 2

# Generated at 2022-06-14 00:44:16.172677
# Unit test for method surname of class Person
def test_Person_surname():
    seed(0)
    person = Person(seed=0)
    
    assert person.surname(gender=Gender.male) == 'Брюханов'
    assert person.surname(gender=Gender.female) == 'Киселева'

# Generated at 2022-06-14 00:44:23.632779
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker import Faker
    from faker_ru.providers.person import Person
    from faker_ru.enums import Gender
    import pytest
    fake = Faker('ru_RU')
    p = Person(fake)
    b_male = p.nationality(Gender.male)
    b_female = p.nationality(Gender.female)
    # Test
    assert isinstance(b_male, str)
    assert isinstance(b_female, str)

# Generated at 2022-06-14 00:44:25.486823
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() in _data['surname']


# Generated at 2022-06-14 00:44:29.097372
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(10):
        nationality = Person().nationality()
        assert nationality in Person._data['nationality']


# Generated at 2022-06-14 00:44:32.611533
# Unit test for method surname of class Person
def test_Person_surname():
    pass


# Generated at 2022-06-14 00:45:17.772977
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    person.nationality()
    
    
    

# Generated at 2022-06-14 00:45:29.296261
# Unit test for method surname of class Person
def test_Person_surname():
    """Test surname method
    """
    # Create an instance of Person class
    # For more information check classes section
    person = Person()

    # Print one of the following surnames:
    # Иванов, Петрова, Сидоров, Кузнецов
    # Passing gender as a positional parameter
    print(person.surname(Gender.MALE))
    print(person.surname(Gender.FEMALE))

    # Passing gender as a keyword parameter
    print(person.surname(gender=Gender.MALE))
    print(person.surname(gender=Gender.FEMALE))

    # Returning all surnames for male
    male_surnames = person.surname(Gender.MALE, all=True)

# Generated at 2022-06-14 00:45:39.241575
# Unit test for method email of class Person
def test_Person_email():
    ui = Person(seed=112312)
    assert ui.email() == 'adam_gorny@gmail.com'
    assert ui.email(unique=True) == 'frankek_1921@gmail.com'
    assert ui.email(domains=('a.com', 'b.com'), unique=True) == 'mclarena_8765@a.com'


# Generated at 2022-06-14 00:45:51.611182
# Unit test for method username of class Person
def test_Person_username():
    provider = Person()

    for _ in range(100):
        generated_username = provider.username('Ud')
        assert re.fullmatch(r'[A-Z]\d+', generated_username), \
            'Not a valid username'
        assert re.fullmatch(r'[A-Z]\d+', generated_username), \
            'Not a valid username'
        assert re.fullmatch(r'[A-Z]\d+', generated_username), \
            'Not a valid username'
        assert re.fullmatch(r'[A-Z]\d+', generated_username), \
            'Not a valid username'
        assert re.fullmatch(r'[A-Z]\d+', generated_username), \
            'Not a valid username'

# Generated at 2022-06-14 00:45:54.111317
# Unit test for method surname of class Person
def test_Person_surname():
    p = RandomPerson()
    assert isinstance(p.surname(), str)


# Generated at 2022-06-14 00:46:03.509915
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker.generator import Generator
    from faker.providers.person.en_US import Provider as PersonProvider
    from faker.utils.loading import resolve_provider_to_local
    from faker.utils.datafile import load

    locale = 'ru'
    person = resolve_provider_to_local('person', locale)
    person = load('{}/{}/{}.json'.format('faker', 'providers', person))
    gen = Generator(PersonProvider)
    gen.add_provider(PersonProvider(gen, person))

    result = gen.nationality()
    assert result in person['nationality']


# Generated at 2022-06-14 00:46:05.108426
# Unit test for method nationality of class Person
def test_Person_nationality():
    pid = Person(seed=42)
    assert pid.nationality() == 'Russian'


# Generated at 2022-06-14 00:46:09.525840
# Unit test for method nationality of class Person
def test_Person_nationality():
    nations = ['Russian', 'Ukrainian']
    p = Person()
    p._data['nationality'] = nations
    nationality = p.nationality()
    assert nationality in nations

# Generated at 2022-06-14 00:46:11.947273
# Unit test for method surname of class Person
def test_Person_surname():
    rv = Person().surname(gender='male')
    assert rv in rv

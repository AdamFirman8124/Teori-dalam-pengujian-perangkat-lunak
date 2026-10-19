

# Generated at 2022-06-14 00:36:27.723023
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in _data['nationality']


# Generated at 2022-06-14 00:36:32.072694
# Unit test for method email of class Person
def test_Person_email():
    from faker import Faker
    faker = Faker()
    p = Person(faker)
    assert len(p.email()) > 5
    assert p.email() in ALL_EMAILS

# Generated at 2022-06-14 00:36:39.842166
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() != ''
    assert Person().nationality() != ' '
    assert Person().nationality() != None
    assert Person().nationality() != []
    assert Person().nationality() != {}
    assert Person().nationality('Male') != ''
    assert Person().nationality('Male') != ' '
    assert Person().nationality('Male') != None
    assert Person().nationality('Male') != []
    assert Person().nationality('Male') != {}
    
    
    

# Generated at 2022-06-14 00:36:41.609633
# Unit test for method surname of class Person
def test_Person_surname():
   obj = Person()
   assert isinstance(obj.surname(),(str))


# Generated at 2022-06-14 00:36:49.486975
# Unit test for method email of class Person
def test_Person_email():

    result = []
    params = [
        (
            (),
            {'unique': False},
        ),
        (
            ('gmail.com', 'mail.ru',),
            {'unique': False},
        ),
        (
            ('gmail.com', 'mail.ru',),
            {'unique': True},
        ),
    ]

    for p in params:
        obj = Person()
        result.append(obj.email(domains=p[0], unique=p[1]['unique']))
    return pprint(result)


# print(test_Person_email())


# Generated at 2022-06-14 00:37:04.574895
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person()._validate_enum(0, Gender) == 'neutral'
    assert Person()._validate_enum(1, Gender) == 'male'
    assert Person()._validate_enum(2, Gender) == 'female'
    assert Person()._validate_enum(9, Gender) == 'androgine'

    assert Person()._validate_enum(0, TitleType) == 'prefix'
    assert Person()._validate_enum(1, TitleType) == 'suffix'

    assert Person().name()
    assert Person().random.choice(USERNAMES)
    assert Person().username()
    assert Person().password()
    assert Person().email()

    assert Person().social_media_profile()
    assert Person().gender()
    assert Person().height()
    assert Person().weight()
    assert Person().blood_type

# Generated at 2022-06-14 00:37:10.236908
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Faker(['ru_RU'])
    test_cases = (
        (Gender.MALE, 'Украинец'),
        (Gender.FEMALE, 'Украинка'),
    )
    provider.add_provider(Person)
    for gender, expected in test_cases:
        assert provider.person.nationality(gender=gender) == expected



# Generated at 2022-06-14 00:37:17.522784
# Unit test for method email of class Person
def test_Person_email():
    '''
    Test for a email method of Person class
    '''
    r = Random()
    r.set_seed()
    p = Person(r=r)
    result = p.email('gmail.com')
    assert result == 'sue64@gmail.com'
    result = p.email('yandex.ru', unique=True)
    assert result == 'lscnI6@yandex.ru'
    
    

# Generated at 2022-06-14 00:37:21.674377
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=seed)
    surname = person.surname()
    if (surname != 'Clemons') & (surname != 'Ingram'):
        assert False, 'Test method "surname" of class "Person" failed.'
    else:
        assert True, 'Test method "surname" of class "Person" passed.'

# Generated at 2022-06-14 00:37:24.430043
# Unit test for method surname of class Person
def test_Person_surname():
    name = Person().surname()
    assert isinstance(name, str)
    assert len(name) > 2


# Generated at 2022-06-14 00:37:35.654348
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    s = person.nationality()
    assert s


# Generated at 2022-06-14 00:37:38.832940
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname()
    assert Person.surname(Gender.Male)
    assert Person.surname(Gender.Female)



# Generated at 2022-06-14 00:37:47.761530
# Unit test for method email of class Person
def test_Person_email():
    person = Person(random=Random())
    assert person.email() == person.email()

    # Get the same email
    random = Random(seed=42)
    person = Person(random=random)
    person.email(unique=True)

    random = Random(seed=42)
    person = Person(random=random)
    assert person.email(unique=True) == person.email(unique=True)


# Generated at 2022-06-14 00:37:52.228645
# Unit test for method email of class Person
def test_Person_email():
    """Generate a random email.
    :Example:
    foretime10@live.com
    """
    person = Person()
    for i in range(10):
        print(person.email())

# Generated at 2022-06-14 00:38:02.122149
# Unit test for method nationality of class Person
def test_Person_nationality():
    def test_NotImplementedError():
        person = Person(random=DeterministicGenerator(0))

        assert person.nationality(1) == 'Russian'
        assert person.nationality(2) == 'Russian'

    def test_arguments_in_incorrect_format():
        person = Person(random=DeterministicGenerator(0))

        assert person.nationality(0) == 'Russian'
        assert person.nationality(3) == 'Russian'

    def test_is_enum():
        person = Person(random=DeterministicGenerator(0))

        assert person.nationality(Gender.MALE) == 'Russian'
        assert person.nationality(Gender.FEMALE) == 'Russian'


# Generated at 2022-06-14 00:38:14.867381
# Unit test for method email of class Person
def test_Person_email():
    '''
    Check that the email method produces emails that end with a valid TLD, unless a custom list of domains is provided
    '''
    tlds = ['com','net','org','edu','gov','co.uk','cz']
    custom_tlds = ['com','net','org','edu','gov','co.uk','cz', 'dev']
    
    person = Person(rnd=rnd)
    email = person.email()
    assert email[-3:] in tlds
    assert email[-4:] not in tlds
    
    email = person.email(domains=custom_tlds)
    assert email[-3:] in custom_tlds
    assert email[-4:] not in custom_tlds
    assert email[-4:] not in tlds
    

# Generated at 2022-06-14 00:38:23.965214
# Unit test for method surname of class Person
def test_Person_surname():
    user = Person
    names = 'Vasyukov Alvarado Vergara Pugh Mcgee Delacruz Morin Bowers Kent'.split(' ')
    random_list = []
    random_list2 = []
    for x in range(30):
        random_list.append(user.surname())
        random_list2.append(user.surname(gender=Gender.male))
    assert(random_list2.count(user.surname(gender=Gender.male)) + random_list.count(user.surname())==30)
    assert(random_list.count(user.surname()) + random_list2.count(user.surname(gender=Gender.male))==30)
    assert(user.surname(gender=Gender.male) in random_list2)

# Generated at 2022-06-14 00:38:32.686334
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname(Gender.MALE) in NAME_SURNAMES_RU_MALE
    assert Person().surname(Gender.FEMALE) in NAME_SURNAMES_RU_FEMALE
    
"""
Test some properties of methods in the Person class.

The tests are random, that's why they may fail.

You have to be extremely lucky to fail the Person.telephone() test.
"""

if __name__ == '__main__':
    provider = Person()
    
    def test_Person_first_name():
        assert provider.name(Gender.MALE) in NAME_FIRST_NAMES_RU_MALE
        assert provider.name(Gender.FEMALE) in NAME_FIRST_NAMES_RU_FEMALE
        

# Generated at 2022-06-14 00:38:37.567434
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    result = person.surname()
    assert isinstance(result, str)

    # Empty surnames
    person.surnames = []
    result = person.surname()
    assert result == ''

# Generated at 2022-06-14 00:38:45.685705
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() in MALE_SURNAMES
    assert Person().surname(gender=Gender.female) in FEMALE_SURNAMES
    assert Person().surname(gender=Gender.female) in FEMALE_SURNAMES
    assert Person().surname(gender=Gender.male) in MALE_SURNAMES

    assert Person().last_name() in MALE_SURNAMES
    assert Person().last_name(gender=Gender.female) in FEMALE_SURNAMES
    assert Person().last_name(gender=Gender.female) in FEMALE_SURNAMES
    assert Person().last_name(gender=Gender.male) in MALE_SURNAMES


# Generated at 2022-06-14 00:38:55.496895
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert isinstance(p.surname(), str)
    assert len(p.surname()) > 0


# Generated at 2022-06-14 00:38:57.421026
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person.nationality() == "American"


# Generated at 2022-06-14 00:38:58.960320
# Unit test for method surname of class Person
def test_Person_surname():
    person = PersonFactory()
    assert isinstance(person.surname(), str)

# Generated at 2022-06-14 00:39:11.252394
# Unit test for method nationality of class Person

# Generated at 2022-06-14 00:39:19.467837
# Unit test for method nationality of class Person
def test_Person_nationality():

    from random import randint
    from random import seed

    from faker.providers.person.ru_RU import Provider
    from faker.providers.person.en_US import Provider

    provider = Provider
    seed(10)

    assert provider.nationality(provider) == 'Russian'
    seed(1)
    assert provider.nationality(provider) == 'Russian'
    seed(2)
    assert provider.nationality(provider) == 'Russian'
    seed(3)
    assert provider.nationality(provider) == 'Russian'
    seed(4)
    assert provider.nationality(provider) == 'Russian'
    seed(5)
    assert provider.nationality(provider) == 'Russian'
    seed(6)
    assert provider.nationality(provider) == 'Russian'
   

# Generated at 2022-06-14 00:39:26.422366
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(seed=42)
    assert person.nationality(gender=Gender.FEMALE) == 'Brazilian'
    assert person.nationality(gender=Gender.MALE) == 'Brazilian'
    assert person.nationality(gender=Gender.OTHER) == 'Brazilian'
    assert person.nationality() == 'Brazilian'

# Generated at 2022-06-14 00:39:32.890294
# Unit test for method surname of class Person
def test_Person_surname():
    # Surnames separated by gender.
    assert Person().surname() in SURNAME
    assert Person().surname(gender=Gender.MALE) in SURNAME_MALE
    assert Person().surname(gender=Gender.FEMALE) in SURNAME_FEMALE
    
    # Surnames not separated by gender.
    assert Person().surname() in SURNAME
    assert Person().surname(gender=Gender.MALE) in SURNAME
    assert Person().surname(gender=Gender.FEMALE) in SURNAME

# Generated at 2022-06-14 00:39:35.477145
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person()
    answer = provider.nationality()
    print(answer)
    return answer

# test_Person_nationality()


# Generated at 2022-06-14 00:39:39.879276
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)
    assert isinstance(person.surname(Gender.male), str)
    assert isinstance(person.surname(Gender.female), str)


# Generated at 2022-06-14 00:39:45.506200
# Unit test for method email of class Person
def test_Person_email():
    person = Person(random=False)
    assert person.email() == 'foretime10@live.com'
    person.seed(0)
    assert person.email() == 'foretime10@live.com'
test_Person_email()


# Generated at 2022-06-14 00:40:06.907227
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() != ''
    assert Person().surname(gender=Gender.FEMALE) != ''
    assert Person().surname(gender=Gender.MALE) != ''


# Generated at 2022-06-14 00:40:18.110097
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    names = []
    for _ in range(100):
        name = p.surname()
        assert name not in names
        names.append(name)
    names = []
    for _ in range(100):
        name = p.surname(Gender.Male)
        assert name not in names
        names.append(name)
    names = []
    for _ in range(100):
        name = p.surname(Gender.Female)
        assert name not in names
        names.append(name)

# Generated at 2022-06-14 00:40:21.080600
# Unit test for method email of class Person
def test_Person_email():
    person = Person(random=Random())

    assert isinstance(person.email(unique=True), str)
    assert isinstance(person.email(), str)


# Generated at 2022-06-14 00:40:28.318024
# Unit test for method surname of class Person
def test_Person_surname():
    p1 = Person()
    assert isinstance(p1.surname(), str)
    assert p1.surname() != p1.surname()
    assert p1.surname(Gender.MALE) != p1.surname(Gender.FEMALE)
    assert p1.surname(Gender.FEMALE) != p1.surname(Gender.MALE)


# Generated at 2022-06-14 00:40:29.584741
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert 'Russian' == Person().nationality()



# Generated at 2022-06-14 00:40:35.607961
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Check value 'Nationality' if gender equal None
    assert Person.nationality(Person) == 'American', ('Nationality is not equal'
                                                      ' American')
    # Check value 'Nationality' if gender equal 'FEMALE'
    assert Person.nationality(Person, 'FEMALE') == 'American', ('Nationality is not equal'
                                                      ' American')
    # Check value 'Nationality' if gender equal 'MALE'
    assert Person.nationality(Person, 'MALE') == 'American', ('Nationality is not equal'
                                                      ' American')
    # Check value 'Nationality' if gender equal 'FEMALE'
    assert Person.nationality(Person, 'FEMALE') == 'American', ('Nationality is not equal'
                                                      ' American')
    # Check type of value 'Nationality'

# Generated at 2022-06-14 00:40:39.031573
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(locale='en')
    nationalities = p._data['nationality']
    nationality = p.nationality()
    assert nationality in nationalities

test_Person_nationality()

# Generated at 2022-06-14 00:40:44.480249
# Unit test for method nationality of class Person
def test_Person_nationality():
    from random import Random
    from datetime import datetime
    from namegen.main import Person

    rnd = Random(datetime.now())

    person = Person(random=rnd)
    nationality = person.nationality()
    print(nationality)
    assert isinstance(nationality, str)

test_Person_nationality()
 
pass
test_Person_identifier

# Generated at 2022-06-14 00:40:47.371149
# Unit test for method surname of class Person
def test_Person_surname():
    item = Person()
    assert type(item.surname()) is str


# Generated at 2022-06-14 00:40:51.521994
# Unit test for method nationality of class Person
def test_Person_nationality():
    # arrange
    p = Person()
    # act
    nationality = p.nationality(Gender.male)
    # assert
    if(nationality in p._data['nationality']):
        assert True
    else:
        assert False
test_Person_nationality()



# Generated at 2022-06-14 00:41:22.046875
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname()
    assert isinstance(surname, str)

# Generated at 2022-06-14 00:41:25.089281
# Unit test for method nationality of class Person
def test_Person_nationality():
    pers = Person()
    assert pers.nationality('m') == pers.nationality()

# Generated at 2022-06-14 00:41:32.976697
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    surname = person.surname(Gender.male)
    assert isinstance(surname, str)
    assert len(surname) > 0
    surname = person.surname(Gender.female)
    assert isinstance(surname, str)
    assert len(surname) > 0
    surname = person.surname()
    assert isinstance(surname, str)
    assert len(surname) > 0

# Generated at 2022-06-14 00:41:35.023485
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert isinstance(person.nationality(Gender.MALE),str)
    assert isinstance(person.nationality(Gender.FEMALE),str)
    assert isinstance(person.nationality(),str)


# Generated at 2022-06-14 00:41:39.312719
# Unit test for method surname of class Person
def test_Person_surname():
    # Verify that method surname returns a string
    provider = Person(random=Random())
    data = provider.surname()

    assert isinstance(data, str)
    print(data)

test_Person_surname()


# Generated at 2022-06-14 00:41:45.082717
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Unit test method Person.nationality.
    """
    person = Person(seed=1)

    assert person.nationality() == 'Angolan'

# Generated at 2022-06-14 00:41:54.744985
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person('en')
    for i in range(100):
        assert p.nationality() in NATIONALITIES
    for i in range(100):
        assert p.nationality(Gender.FEMALE) in FEMALE_NATIONALITIES
    for i in range(100):
        assert p.nationality(Gender.MALE) in MALE_NATIONALITIES

    with pytest.raises(NonEnumerableError):
        p.nationality(Gender.FEMALE.value)
    with pytest.raises(NonEnumerableError):
        p.nationality(Gender.MALE.value)
    with pytest.raises(NonEnumerableError):
        p.nationality(Gender.NOT_APPLICABLE.value)

# Generated at 2022-06-14 00:42:00.186833
# Unit test for method surname of class Person
def test_Person_surname():
    surname = LocalPerson.surname()
    assert isinstance(surname, str)


# Generated at 2022-06-14 00:42:05.638786
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person('en')

    surname1 = person.surname()
    surname2 = person.surname()
    surname3 = person.surname(Gender.FEMALE)
    surname4 = person.surname(Gender.FEMALE)

    assert surname1 != surname2
    assert surname3 != surname4
    

# Generated at 2022-06-14 00:42:13.732871
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname() in p._data['surname']
from unittest import TestCase, main

from pydantic import ValidationError
from pytest import raises
from faker import Faker

from lr2irsi.random.utils import NonEnumerableError
from lr2irsi.random.enums import Gender
from lr2irsi.random.models import (
    Person,
)



# Generated at 2022-06-14 00:42:47.305890
# Unit test for method nationality of class Person
def test_Person_nationality():
    for _ in range(100):
        assert Person.nationality() in Person._data['nationality']
test_Person_nationality()

# Generated at 2022-06-14 00:42:49.407856
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert(isinstance(p.surname(),str))


# Generated at 2022-06-14 00:42:57.575545
# Unit test for method nationality of class Person
def test_Person_nationality():
    from faker.providers.person import Provider
    provider = Provider(localizer=None)
    assert provider.nationality()
    assert provider.nationality(gender=Gender.MALE)
    assert provider.nationality(gender=Gender.FEMALE)
    assert provider.nationality(gender='male')
    assert provider.nationality(gender='female')
    assert provider.nationality(gender=0)
    assert provider.nationality(gender=1)


# Generated at 2022-06-14 00:43:00.935044
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() in SURNAME_GER


# Generated at 2022-06-14 00:43:06.040902
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert isinstance(p.surname(), str) == True
    assert len(p.surname()) >= 3


# Generated at 2022-06-14 00:43:14.103228
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Person(random=RANDOM)
    number_of_tests = 10
    key = 0
    while key < number_of_tests:
        result = provider.nationality()
        if result in NATIONALITY:
            key += 1
        else:
            key = 0
    assert key == number_of_tests

# Generated at 2022-06-14 00:43:22.353400
# Unit test for method surname of class Person
def test_Person_surname():
    # Arrange
    first_names = ['Дарт', 'Роберт', 'Родриго']
    surnames = ['Вейдер', 'Скариган', 'Кеноби']
    person = Person(first_names=first_names, surnames=surnames)
    # Act
    # Assert
    assert person.surname() in surnames


# Generated at 2022-06-14 00:43:27.638745
# Unit test for method nationality of class Person
def test_Person_nationality():
    
    person = Person(seed=123456789)
    
    assert person.nationality() == "Russian"
    assert person.nationality() == "Chinese"
    assert person.nationality() == "French"

# Generated at 2022-06-14 00:43:33.384832
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person('en')

    surnames = person.surname()
    assert isinstance(surnames, str) and surnames

    surnames = person.surname(gender=Gender.FEMALE )
    assert isinstance(surnames, str) and surnames


# Generated at 2022-06-14 00:43:39.621023
# Unit test for method nationality of class Person
def test_Person_nationality():

    person = Person(seed=42)
    random_nationality = person.nationality() 
    assert random_nationality == "Iranian"
    nationalities = person.nationality(gender=Gender.MALE)
    assert nationalities == "Italian"
    nationalities = person.nationality(gender=Gender.FEMALE)
    assert nationalities == "Iranian"


# Generated at 2022-06-14 00:44:12.039040
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    surname = p.surname()
    assert isinstance(surname, str)
    assert surname != ''


# Generated at 2022-06-14 00:44:17.982169
# Unit test for method surname of class Person
def test_Person_surname():
    # Testing surnames
    assert len(Person().surname(Gender.male)) > 0
    assert len(Person().surname(Gender.female)) > 0
    assert len(Person().surname()) > 0
    assert len(Person().last_name()) > 0
    assert len(Person().last_name(Gender.male)) > 0
    assert len(Person().last_name(Gender.female)) > 0

# Generated at 2022-06-14 00:44:22.781247
# Unit test for method nationality of class Person
def test_Person_nationality():
    nationalities = [
        'Russian',
        'German',
        'Italian',
        'French',
        'Canadian',
        'English',
        'American',
        'Japanese',
        'Chinese',
        'Indian'
    ]
    for i in range(10):
        assert Person().nationality() in nationalities


# Generated at 2022-06-14 00:44:26.533592
# Unit test for method surname of class Person
def test_Person_surname():
    # Initialize the default provider
    provider = BasicProvider()
    # Generate a random last name
    surname = provider.surname()
    assert isinstance(surname, str)
    assert len(surname) > 0


# Generated at 2022-06-14 00:44:36.304085
# Unit test for method email of class Person
def test_Person_email():

    # Arrange
    EMAIL_DOMAINS = ('ya.ru', 'yandex.ru', 'yandex.ua', 'yandex.com')
    random = Random()
    person = Person(random)

    # Act
    email_address = person.email(domains=EMAIL_DOMAINS)

    # Assert
    assert re.fullmatch(r'[\w\d]+(\.[\w\d]+)*@([a-zA-Z]{2,}\.)?ya\.ru|yandex\.ru|yandex\.ua|yandex\.com', email_address) is not None


# Generated at 2022-06-14 00:44:41.296717
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    assert p.nationality() in ['Russian', 'Azerbaijani-Tajik', 'Latvian', 'Tajik']

# Generated at 2022-06-14 00:44:51.566005
# Unit test for method nationality of class Person
def test_Person_nationality():
    print("Проверка класса Person на метод nationality")
    # Задаём словарь с национальностями {"male": ["male1", "male2"], "female": []}
    # для этого создаём объект класса Person
    person = Person()
    # Создаём копипируем из него _data
    data = person._data
    # Альтернативный вари

# Generated at 2022-06-14 00:44:53.670526
# Unit test for method nationality of class Person
def test_Person_nationality():
    provider = Factory(locale='ru').create(Person)
    nationality_result = provider.nationality()
    assert nationality_result in data.PERSON_NATIONALITY



# Generated at 2022-06-14 00:44:57.542773
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person(seed=0)
    assert p.nationality() == 'Russian'
    print('Unit test for method nationality of class Person')
    print(p.nationality())
    print('Unit test is done')

# Generated at 2022-06-14 00:45:00.847998
# Unit test for method surname of class Person
def test_Person_surname():
    from prf.utils import get_random_item
    from prf.enums import Gender
    provider = Person()
    assert type(provider.surname(get_random_item(Gender))) == str


# Generated at 2022-06-14 00:45:34.279505
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person()
    for _ in range(10):
        result = provider.surname()
        assert isinstance(result, str)
        assert len(result) > 0


# Generated at 2022-06-14 00:45:38.845817
# Unit test for method surname of class Person
def test_Person_surname():
    np = Person(seed=1)
    actual = np.surname()
    expected = 'Долина'

    assert actual == expected

# Generated at 2022-06-14 00:45:51.494770
# Unit test for method nationality of class Person
def test_Person_nationality():
    """
    Test method Person.nationality of class Person.
    """
    # Create a instance
    person = Person(random=Random(), seed=12345)

    # Nationality
    assert person.nationality() == 'Colombian'
    assert person.nationality() == 'Belarusian'
    assert person.nationality() == 'Belarusian'
    assert person.nationality() == 'Belarusian'
    assert person.nationality() == 'Belarusian'
    assert person.nationality() == 'Belarusian'
    assert person.nationality() == 'Russian'
    assert person.nationality() == 'Azerbaijani'
    assert person.nationality() == 'Egyptian'
    assert person.nationality() == 'Moroccan'
    assert person.nationality() == 'Moroccan'
   

# Generated at 2022-06-14 00:45:54.415729
# Unit test for method email of class Person
def test_Person_email():
    pr = Person()
    assert re.match(r'[\w\d]+@[.\w]+',pr.email())

# Generated at 2022-06-14 00:46:03.427121
# Unit test for method nationality of class Person
def test_Person_nationality():
    
    assert Person.nationality(Person, gender=Gender.FEMALE) in Person()._data['nationality'][Gender.FEMALE.value]
    assert Person.nationality(Person, gender=Gender.MALE) in Person()._data['nationality'][Gender.MALE.value]
    assert Person.nationality(Person) in Person()._data['nationality']
    assert Person.nationality(Person, gender=None) in Person()._data['nationality']
    
    with pytest.raises(NonEnumerableError):
        Person.nationality(Person, gender=3)

# Generated at 2022-06-14 00:46:05.051417
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(gender=None), str)



# Generated at 2022-06-14 00:46:10.855775
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Unit test for method nationality of class Person.

    Test data should be like a tuple.
    For example:

        test_data = (
            {'gender': Gender.MALE},
            {'gender': Gender.FEMALE},
        )

    And results should be like a tuple.
    For example:

        results = (
            'Russian',
            'Russian',
        )

    In this case you should use:

        assert test(test_data, results)

    """

    test_data = (
        {'gender': Gender.MALE},
        {'gender': Gender.FEMALE},
    )

    results = (
        'Russian',
        'Russian',
    )

    assert test(test_data, results)
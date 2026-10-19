

# Generated at 2022-06-14 00:36:30.715301
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in person._data['nationality']


# Generated at 2022-06-14 00:36:33.863567
# Unit test for method surname of class Person
def test_Person_surname():
    Person_instance = Person()
    assert isinstance(Person_instance.surname(), (str,))

# Generated at 2022-06-14 00:36:38.944207
# Unit test for method email of class Person
def test_Person_email():
    """
    This test checks for the correctness of the function email
    """
    instance = Person()
    result = instance.email()
    assert len(result) > 0
    assert result.find('@') > 0
    
    
    
    

# Generated at 2022-06-14 00:36:42.350097
# Unit test for method surname of class Person
def test_Person_surname():
    _ = Person()
    # Test the type of the returned result
    assert( isinstance(_.surname(), str) )

# Generated at 2022-06-14 00:36:44.712751
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname() != ''


# Generated at 2022-06-14 00:36:59.716589
# Unit test for method email of class Person
def test_Person_email():
    person = Person.seed(seed=0)
    assert person.email() == 'BONITA.NGUYEN@YAHOO.COM', 'Value is not equal'
    assert person.email() == 'SAMANTHAMANNING@COMCAST.NET', 'Value is not equal'
    assert person.email() == 'JIMSTEWART@HOTMAIL.COM', 'Value is not equal'
    assert person.email() == 'WILLIEBLACK@HOTMAIL.COM', 'Value is not equal'
    assert person.email() == 'JOHNPIERCE@GMAIL.COM', 'Value is not equal'
    assert person.email() == 'SHARONREED@HOTMAIL.COM', 'Value is not equal'

# Generated at 2022-06-14 00:37:03.204263
# Unit test for method surname of class Person
def test_Person_surname():
    data = Person()
    assert isinstance(data.surname(), str)


# Generated at 2022-06-14 00:37:08.328989
# Unit test for method surname of class Person
def test_Person_surname():
    print("test_Person_surname is running")
    for i in range(100):
        result = Person().surname()
        #print(result)
        if result in SURNAME:
            continue
        else:
            raise Exception("surname error")
    print("Pass test_Person_surname")

# Generated at 2022-06-14 00:37:17.198833
# Unit test for method surname of class Person
def test_Person_surname():
    from datetime import datetime
    from mock import patch, Mock

    rnd = random.Random()
    rnd.seed(datetime.now())
    p = Person(rnd)

    # 1. Test with no arguments
    with patch.object(rnd, 'choice', return_value=('No', 'known', 'gender')):
        assert p.surname() == 'No'
        assert p.surname(Gender.MALE) == 'known'
        assert p.surname(Gender.FEMALE) == 'gender'

    # 2. Test with incorrect gender
    with patch.object(rnd, 'choice', return_value='expected value'):
        assert p.surname(333) == 'expected value'

    # 3. Test with no known gender

# Generated at 2022-06-14 00:37:20.486911
# Unit test for method nationality of class Person
def test_Person_nationality():
    result = Person.nationality()
    assert result in PERSON_NATIONALITY
test_Person_nationality()

# Generated at 2022-06-14 00:37:50.991429
# Unit test for method surname of class Person
def test_Person_surname():
    for _ in range(100):
        obj = Person(random=Random(0))
        result = obj.surname()
        assert result == 'Cheng'

    obj = Person(seed=0)
    result = obj.surname()
    assert result == 'Cheng'

    obj = Person(random=Random(0))
    result = obj.surname(gender=Gender.male)
    assert result == 'Cheng'

    obj = Person(random=Random(0))
    result = obj.surname(gender=Gender.female)
    assert result == 'Hansen'

    surnames = {
        Gender.male: ['Cheng'],
        Gender.female: ['Hansen']
    }
    obj = Person(random=Random(0))

# Generated at 2022-06-14 00:37:57.255714
# Unit test for method gender of class Person
def test_Person_gender():
    for i in range(100):
        gender = Person().gender()
        assert isinstance(gender, str)
        assert gender.lower() in [
            'male',
            'woman',
            'girl',
            'boy',
        ]



# Generated at 2022-06-14 00:37:59.362315
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    res = p.surname()
    exp = 'Surname'
    assert res == exp


# Generated at 2022-06-14 00:38:05.649737
# Unit test for method gender of class Person
def test_Person_gender():
    rng = random.Random()
    seed = random.randint(0, 65535)
    print('Seed for random generator: %d' % seed)
    rng.seed(seed)
    i = 0
    while i < 10000:
        p = Person(rng, 'en_US')
        g = p.gender()
        if g not in ('Male', 'Female'):
            print('Test failed')
            print('Random seed was: %d' % seed)
            print('Generated value was: %s' % g)
            print('Expected are: Male, Female')
            exit()
        i += 1
    print('Test successful')


# Generated at 2022-06-14 00:38:09.671790
# Unit test for method gender of class Person
def test_Person_gender():
    pr = Person()
    assert pr.gender() in GENDER_SYMBOLS


# Generated at 2022-06-14 00:38:14.218627
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person.nationality('male', 'Russian') == 'Russian'
    assert Person.nationality('female', 'Ukrainian') == 'Ukrainian'
    assert Person.nationality('other', 'Belarusian') == 'Belarusian'

    print('Testing method nationality of class Person: OK')

# Generated at 2022-06-14 00:38:17.016823
# Unit test for method nationality of class Person
def test_Person_nationality():
    NATIONALITIES = ('russian', 'ukrainian')
    person = Person(nationality=NATIONALITIES)

    assert person.nationality() in NATIONALITIES
test_Person_nationality()


# Generated at 2022-06-14 00:38:20.004730
# Unit test for method surname of class Person
def test_Person_surname():
    from faker import Faker
    f = Faker()
    for i in range(10):
        surname = f.surname()
        assert isinstance(surname, str)


# Generated at 2022-06-14 00:38:21.739324
# Unit test for method gender of class Person
def test_Person_gender():
    el = Person.language()
    assert isinstance(el, str)
    assert len(el) > 0


# Generated at 2022-06-14 00:38:27.047631
# Unit test for method gender of class Person
def test_Person_gender():
    """Test method gender of class Person."""
    person = Person()

    assert person.gender() in (
        'Male', 'Female', 'Androgynous', 'Neuter', 'Intersex'
    )
    

# Generated at 2022-06-14 00:38:54.556372
# Unit test for method email of class Person
def test_Person_email():
    data = {
        'seed': 0,
        'unique': False,
    }
    test_values = (
        '0fri78ra1@hotmail.com',
        '9i1a88b6a@hotmail.com',
        'k1ic7p8fj@hotmail.com',
        'c5bj95d5f@hotmail.com',
        'w0kt7rqvb@hotmail.com',
        '6l7t8d8g1@hotmail.com',
        'trll6y1vk@hotmail.com',
        'i9q3s3s8s@hotmail.com',
        'yvkvx8x1i@hotmail.com',
        'ljsa8nsfk@hotmail.com',
    )



# Generated at 2022-06-14 00:39:02.893506
# Unit test for method email of class Person

# Generated at 2022-06-14 00:39:06.914616
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    for _ in range(100):
        nationalit = person.nationality(g)
        assert isinstance(nationalit, str)


# Generated at 2022-06-14 00:39:11.730292
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person.nationality('en') == Person.nationality('en')
    assert Person.nationality('en') in Person._data['nationality'].values()

# Generated at 2022-06-14 00:39:14.700321
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    email = person.email()
    assert isinstance(email, str)
    assert email


# Generated at 2022-06-14 00:39:23.112963
# Unit test for method username of class Person
def test_Person_username():
    name = Person().username()
    assert '_' in name
    assert name[0].isupper()
    assert '.' not in name
    assert '-' not in name
    assert '_' in name
    assert name[-1].isdigit()
    assert name == 'Ornith1742'
    assert name != 'Ornith1742'


# Generated at 2022-06-14 00:39:26.890863
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person(localization='en')
    result = person.nationality()
    print('Nationality: ' + result)
    
test_Person_nationality()


# Generated at 2022-06-14 00:39:38.839033
# Unit test for method email of class Person
def test_Person_email():
    from faker.providers import BaseProvider
    from faker.providers.person.en_US import Provider

    p = Person(providers=[BaseProvider, Provider])
    domains = ('163.com', 'google.com', 'm.com', 'mail.com',
               'qq.com', 'sina.com', 'sina.cn', 'sina.com.cn',
               'sina.net', 'sohu.com', 'tom.com', 'vip.163.com',
               'vip.sina.com', 'yeah.net')
    email = p.email(domains=domains)
    assert '@' in email
    assert email.split('@')[1] in domains


# Generated at 2022-06-14 00:39:44.417668
# Unit test for method surname of class Person
def test_Person_surname():
    assert type(Person.surname()) == str
if __name__ == '__main__':
    test_Person_surname()
    print('Done')


# Generated at 2022-06-14 00:39:45.981989
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname() is not None


# Generated at 2022-06-14 00:40:21.207295
# Unit test for method email of class Person
def test_Person_email():
    for _ in range(100):
        provider = Person(locale='ru_RU')
        print(provider.email())

# Generated at 2022-06-14 00:40:28.794774
# Unit test for method surname of class Person
def test_Person_surname():
    # If the data set is empty, raises IndexError
    data = {}
    prng = random.Random()
    prng.seed(1)
    person = Person(data, prng)
    with pytest.raises(IndexError):
        person.surname()
    data['surname'] = []
    person = Person(data, prng)
    with pytest.raises(IndexError):
        person.surname()



# Generated at 2022-06-14 00:40:31.395035
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(seed=42)
    assert person.surname(Gender.Female) == 'Strigon'
    assert person.surname(Gender.Male) == 'Strout'



# Generated at 2022-06-14 00:40:43.434829
# Unit test for method username of class Person
def test_Person_username():
    
    from datetime import datetime
    datetime.now()
    # 
    from pydantic import ValidationError
    
    error_cases = ['U', 'l', 'dd', 'Udd', 'Ud', 'U_d_', 'UUU_d__d', 'dUUUd', '.', 'Un' ]
    for case in error_cases: 
        with pytest.raises(ValidationError): 
            Person().username(template=case)

    assert Person().username()

    r=Person(seed=1)
    assert r.username()=='Ruth_1805'
    
    
    

# Generated at 2022-06-14 00:40:47.792188
# Unit test for method email of class Person
def test_Person_email():
    Provider = Person()
    result = Provider.email()
    assert isinstance(result, str)
    assert result == 'Amanda_Sanchez@gmail.com'


# Generated at 2022-06-14 00:40:48.952270
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality()

# Generated at 2022-06-14 00:40:51.344131
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = Person()
    for i in range(100):
        assert p.nationality() in NATIONALITIES


# Generated at 2022-06-14 00:40:56.895730
# Unit test for method email of class Person
def test_Person_email():
    pattern = re.compile(r"^[-a-zA-Z0-9_.]+@[-a-zA-Z0-9_.]+")
    person = Person()
    assert pattern.match(person.email()) is not None

# Generated at 2022-06-14 00:41:02.320731
# Unit test for method surname of class Person
def test_Person_surname():
    items = ['Belousova', 'Dmitrieva', 'Zakharova', 'Ivanova', 'Sidorova']
    p = Person(seed=0)
    assert p.surname() in items



# Generated at 2022-06-14 00:41:06.623424
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in NATIONALITIES
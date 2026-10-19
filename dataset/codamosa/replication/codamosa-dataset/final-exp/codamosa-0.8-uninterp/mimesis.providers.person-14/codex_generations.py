

# Generated at 2022-06-14 00:36:28.119023
# Unit test for method nationality of class Person
def test_Person_nationality():
    for i in range(100):
        assert isinstance(Person().nationality(), str)


# Generated at 2022-06-14 00:36:30.671069
# Unit test for method surname of class Person
def test_Person_surname():
    provider = Person(random=Random())
    actual = provider.surname()
    assert actual

# Generated at 2022-06-14 00:36:33.274263
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    assert isinstance(person.surname(), str)


# Generated at 2022-06-14 00:36:35.682898
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Arrange
    person = Person()
    # Act
    result = person.nationality()
    # Assert
    assert isinstance(result, str)

# Generated at 2022-06-14 00:36:39.303167
# Unit test for method nationality of class Person
def test_Person_nationality():
    for i in range(len(GENDER)):
        assert Person().nationality(GENDER[i]) in NATIONALITY[GENDER[i]]


# Generated at 2022-06-14 00:36:49.920631
# Unit test for method surname of class Person
def test_Person_surname():
    from faker.generator import Generator
    from faker.factory import Factory

    fake = Factory.create()
    gen = Generator(fake)
    gen.seed(4321)

    assert gen.surname() == 'Мамонтов'
    assert gen.surname(gender='male') == 'Мамонтов'
    assert gen.surname(gender='female') == 'Перминова'
    assert gen.surname(gender='binary') == 'Перминов'
    assert gen.surname(gender='androgynous') == 'Бирубин'
    # test with other seed value
    gen.seed(1234)

# Generated at 2022-06-14 00:36:54.130947
# Unit test for method surname of class Person
def test_Person_surname():
    for i in range(10):
        p = Person()
        result = p.surname()
        assert result.isalpha()
        assert len(result.split()) == 1


# Generated at 2022-06-14 00:36:57.261481
# Unit test for method email of class Person
def test_Person_email():
    person = Person()
    email = person.email()
    assert isinstance(email, str)
    assert '@' in email

# Generated at 2022-06-14 00:37:00.436877
# Unit test for method nationality of class Person
def test_Person_nationality():
    result = []
    for _ in range(10000):
        result.append(Person().nationality())
    assert len(set(result)) > 1 

# Generated at 2022-06-14 00:37:08.524856
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person()

    # The default result should be a string
    res = p.gender()
    assert isinstance(res, str)

    # If the parameter iso5218 the result should be one of the followings:
    # 0, 1, 2, 9
    res = p.gender(iso5218=True)
    assert res in [0, 1, 2, 9]

    # If the symbol parameter is True, the result should be one of the followings:
    # ♂, ♀, ⚲
    res = p.gender(symbol=True)
    assert res in ['♂', '♀', '⚲']

# Generated at 2022-06-14 00:37:28.392832
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert isinstance(person.nationality(),str)


# Generated at 2022-06-14 00:37:37.100674
# Unit test for method username of class Person
def test_Person_username():
    """Unit test for method username of class Person."""
    # Test with default template
    provider = Person()
    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    username = provider.username()
    assert len(username) != 0

    # Test

# Generated at 2022-06-14 00:37:39.576732
# Unit test for method nationality of class Person
def test_Person_nationality():
    """Test method nationality of class Person."""
    person = Person()
    assert person.nationality() in person._data['nationality']

# Generated at 2022-06-14 00:37:50.053485
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert len(p.surname()) == 8
    assert p.surname() in p._data['surname']
    assert p.surname(Gender.FEMALE) in p._data['surname']['female']
    assert p.surname(Gender.MALE) in p._data['surname']['male']
    assert p.surname(Gender.NOT_KNOWN) in p._data['surname']['not_known']
    assert p.surname(Gender.NOT_APPLICABLE) in p._data['surname']['not_applicable']
    assert p.surname(Gender.OTHER) in p._data['surname']['other']
    assert p.surname(Gender.UNSPECIFIED) in p._

# Generated at 2022-06-14 00:37:56.379582
# Unit test for method surname of class Person
def test_Person_surname():
    # test_data = [{'gender': 'm', 'count': 0}]
    person = Person()
    # assert person.surname(
    #     gender='m') == 'Андреев'
    # assert person.surname(
    #     gender='f') == 'Щурланова'
    print(person.surname())


# Generated at 2022-06-14 00:37:57.875844
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in person._data['nationality']


# Generated at 2022-06-14 00:38:03.253626
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(lang='en')
    surname = person.surname()

    check_result(surname, fnames=('surname', ))

# Generated at 2022-06-14 00:38:12.176730
# Unit test for method nationality of class Person
def test_Person_nationality():
    # Test data
    data = [
        (Gender.MALE, 'Russian'),
        (Gender.FEMALE, 'Russian'),
        (None, 'Russian'),
    ]
    # Loop to iterate over test data
    for (p1, p2) in data:
        # Print current test data
        print(f'{p1!r}, {p2!r}')
        # Run test point
        result = Person(p1, p2)
        # Assertion
        assert result == p2

# Generated at 2022-06-14 00:38:20.552284
# Unit test for method surname of class Person
def test_Person_surname():
    def check_Person():
        person = Person('en')
        assert person.surname()

    def check_Person_with_data():
        surnames = (
            'Dupont', 'Dupond', 'Ho Ngoc', 'Dupont'
        )
        person = Person('en', {'surname': surnames})
        assert person.surname()

    check_Person()
    check_Person_with_data()

# Generated at 2022-06-14 00:38:24.568702
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname()
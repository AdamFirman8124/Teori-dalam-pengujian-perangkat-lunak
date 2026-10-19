

# Generated at 2022-06-14 00:36:44.895750
# Unit test for method nationality of class Person
def test_Person_nationality():
    test_cases = [
        (None, True),
        (Gender.MALE, True),
        (Gender.FEMALE, True),
    ]
    for gender, is_valid in test_cases:
        # Arrange
        person = Person(random=Random())
        # Act
        nationality = person.nationality(gender=gender)
        # Assert
        assert isinstance(nationality, str) and len(nationality) > 0
        assert nationality in person._data['nationality']
asd = Person(random=Random())
asd.nationality()


# Generated at 2022-06-14 00:36:48.480612
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person.create()
    surname = person.surname()
    assert surname in Person.surnames()


# Generated at 2022-06-14 00:36:52.679386
# Unit test for method email of class Person
def test_Person_email():
    p = Person(seed=0)
    assert p.email(domains='gmail.com', unique=True) == 'thq3vq8n3@gmail.com'



# Generated at 2022-06-14 00:36:58.207118
# Unit test for method nationality of class Person
def test_Person_nationality():
    pass_flag = True
    for _ in range(2000):
        _p = Person()
        res = _p.nationality()
        if res not in NATIONALITIES:
            pass_flag = False
            break

    assert(pass_flag == True)

# Generated at 2022-06-14 00:36:59.580265
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person().surname()

# Generated at 2022-06-14 00:37:06.891871
# Unit test for method surname of class Person
def test_Person_surname():
    p1 = Person()
    print(p1.surname())
    p2 = Person(language='ru')
    print(p2.surname())
    p3 = Person(language='fr')
    print(p3.surname())
    p4 = Person(language='it')
    print(p4.surname())
    p5 = Person(language='es')
    print(p5.surname())
test_Person_surname()


# Generated at 2022-06-14 00:37:08.729401
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person(random=True)
    assert isinstance(p.surname(), str)

# Generated at 2022-06-14 00:37:12.953562
# Unit test for method nationality of class Person
def test_Person_nationality():
    fake = Faker()
    assert fake.nationality() in NATIONALITIES


# Generated at 2022-06-14 00:37:14.738363
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in PERSON_DATA.nationality


# Generated at 2022-06-14 00:37:25.479189
# Unit test for method gender of class Person
def test_Person_gender():
    def test_gender(g: Gender, i: int, s: str, expected: str):
        value = Person.gender(g, False, False)
        assert value == expected, "gender('{0}', {1}, {2})".format(g, i, s)

    test_gender(Gender.FEMALE, 0, '', 'Female')
    test_gender(Gender.MALE, 0, '', 'Male')
    test_gender(Gender.NOT_KNOWN, 0, '', 'Not known')
    test_gender(Gender.NOT_APPLICABLE, 0, '', 'Not applicable')
    test_gender(Gender.OTHER, 0, '', 'Other')
    test_gender(Gender.PREFER_NOT_TO_SAY, 0, '', 'Prefer not to say')

# Generated at 2022-06-14 00:37:39.877330
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    sn = p.surname()
    print(sn)

if __name__ == '__main__':
    test_Person_surname()
 

# Generated at 2022-06-14 00:37:56.279966
# Unit test for method surname of class Person
def test_Person_surname():
    from unittest import TestCase

    from faker.providers.person import Provider as PersonProvider

    class TestPerson(TestCase):

        def setUp(self):
            # Need to be non-deterministic in order to avoid the same
            # surnames being chosen
            self.person = PersonProvider(random=generator)

        def test_surname(self):
            """Ensure that surnames are generated correctly"""
            # The surnames list should be non-deterministic
            self.assertNotEqual(self.person.surname(), self.person.surname())

        def test_surname_gender(self):
            """Ensure that surnames are generated correctly based on gender"""
            # The surnames list should be non-deterministic

# Generated at 2022-06-14 00:37:57.986086
# Unit test for method nationality of class Person
def test_Person_nationality():
    seed(0)
    person = Person(seed=0)
    nationality = person.nationality()

    assert nationality == "Russian"


# Generated at 2022-06-14 00:38:05.284308
# Unit test for method gender of class Person
def test_Person_gender():
    p = Person("")

    g = p.gender()
    assert g in ("Male", "Female")

    g = p.gender(iso5218=True)
    assert g in (0, 1, 2, 9)

    g = p.gender(symbol=True)
    assert g in ("♂", "♀")
    
    # test_Person_gender()

# Generated at 2022-06-14 00:38:08.125583
# Unit test for method surname of class Person
def test_Person_surname():
    p = Person()
    assert p.surname() in SURNAMES


# Generated at 2022-06-14 00:38:12.278906
# Unit test for method nationality of class Person
def test_Person_nationality():
    person = Person()
    assert person.nationality() in NATIONALITIES

    nationalities = person._data['nationality']
    if isinstance(nationalities, dict):
        for gender in nationalities:
            assert person.nationality(gender) in nationalities[gender]

# Generated at 2022-06-14 00:38:15.782259
# Unit test for method surname of class Person
def test_Person_surname():
    new_Person = Person()
    assert isinstance(new_Person.surname(), str)


# Generated at 2022-06-14 00:38:24.634550
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person(random=MockRandom())

    surnames = person._data['surnames']
    assert person.surname() in surnames
    assert person.surname() in surnames[Gender.FEMALE]
    assert person.surname() in surnames[Gender.MALE]

    surnames = ('Smith', 'Johnson', 'Williams', 'Jones', 'Brown')
    assert person.surname(surnames=surnames) in surnames

    surnames = {Gender.MALE: ('Smith',), Gender.FEMALE: ('Johnson',)}
    assert person.surname(surnames=surnames) in surnames[Gender.MALE]
    assert person.surname(surnames=surnames, gender='male') in surnames[
        Gender.MALE]

# Generated at 2022-06-14 00:38:25.752946
# Unit test for method nationality of class Person
def test_Person_nationality():
    pass


# Generated at 2022-06-14 00:38:27.816125
# Unit test for method gender of class Person
def test_Person_gender():
    person = Person(random=Random())
    assert isinstance(person.gender(), str)
    assert person.gender() in GENDERS

test_Person_gender()

# Generated at 2022-06-14 00:38:39.987310
# Unit test for method gender of class Person
def test_Person_gender():
    random = ParserLocal()
    provider = Provider(random)

    assert provider.gender() != provider.gender()



# Generated at 2022-06-14 00:38:45.604799
# Unit test for method surname of class Person
def test_Person_surname():
    assert Person.surname(None) == Person.surname(None)
    assert Person.surname(None) != Person.surname(None)
    assert Person.surname(None) != Person.surname('female')
    assert Person.surname(None) != Person.surname('male')
    assert Person.surname('male') != Person.surname('female')
    assert Person.surname('male') == Person.surname('male')
    assert Person.surname('female') == Person.surname('female')


# Generated at 2022-06-14 00:38:47.742562
# Unit test for method nationality of class Person
def test_Person_nationality():
    assert Person().nationality() in NATIONALITIES



# Generated at 2022-06-14 00:38:54.870421
# Unit test for method surname of class Person
def test_Person_surname():
    print("test Person_surname...")
    seed(0)
    # test Person_surname with Gender as param
    m = Person("Male") 
    assert m.surname(Gender.MALE) in MALE_SURNAMES
    # test Person_surname with Gender enum element as param
    assert m.surname(Gender.FEMALE) in FEMALE_SURNAMES
    # test Person_surname with string param
    assert m.surname("Female") in FEMALE_SURNAMES



# Generated at 2022-06-14 00:38:57.321190
# Unit test for method nationality of class Person
def test_Person_nationality():
    g = Person()
    g.seed(12345)
    assert g.nationality() == 'Russian'

# Generated at 2022-06-14 00:38:58.247339
# Unit test for method nationality of class Person
def test_Person_nationality():
    pass


# Generated at 2022-06-14 00:38:59.401595
# Unit test for method nationality of class Person
def test_Person_nationality():
    p = PersonProvider()
    assert p.nationality() in p._data['nationality']

# Generated at 2022-06-14 00:39:06.022929
# Unit test for method nationality of class Person
def test_Person_nationality():
    person=Person(seed=5)
    assert person.nationality(gender=Gender.Male)=='Russian'
    assert person.nationality(gender=Gender.Female)=='Russian'
    person=Person()
    assert person.nationality()=='Russian'
    assert person.nationality()=='Russian'

# Generated at 2022-06-14 00:39:14.700960
# Unit test for method gender of class Person
def test_Person_gender():
    """Unit test for method gender of class Person"""
    # Arrange
    expected = Gender.MALE
    rnd = MockRandom([0.0])
    provider = rnd.provider(Person)

    # Act
    actual = provider.gender()

    # Assert
    assert expected == actual
    print('No bugs found')


test_Person_gender()


# Generated at 2022-06-14 00:39:29.586630
# Unit test for method surname of class Person
def test_Person_surname():
    person = Person()
    if person.seed:
        seed(person.seed)
    surname_check_str(person.surname())
    surname_check_str(person.surname(Gender.MAN))
    surname_check_str(person.surname(Gender.WOMAN))
    surname_check_str(person.last_name())
    surname_check_str(person.last_name(Gender.MAN))
    surname_check_str(person.last_name(Gender.WOMAN))
    surname_check_dict(person.surname(gender=Gender.MAN), Gender.MAN)
    surname_check_dict(person.surname(gender=Gender.WOMAN), Gender.WOMAN)
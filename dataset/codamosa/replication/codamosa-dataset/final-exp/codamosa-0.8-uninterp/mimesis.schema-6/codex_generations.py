

# Generated at 2022-06-14 01:07:33.388805
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert isinstance(field, AbstractField)

# Generated at 2022-06-14 01:07:42.714191
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()

    assert field('en_US')
    assert field('email')
    assert field('email', pattern='^[a-z0-9]*@[a-z0-9]*')
    assert field('personal.full_name', gender='F')
    assert field('personal.full_name', key=lambda x: x.split(' ')[0])
    assert field('personal.full_name', key=lambda x: x.split(' ')[0], gender='F')
    assert field('personal.full_name', key=lambda x: True, gender='M')



# Generated at 2022-06-14 01:07:49.921641
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field()

    assert 'cjk' in str(f)
    assert f('cjk')

    assert 'code' in str(f)
    assert f('code', key=lambda x: len(x) > 4)
    assert f('code')

    assert f('randint', minimum=0, maximum=100) <= 100
    assert f('randint', minimum=0, maximum=100) >= 0

    assert f('pybool') is True or f('pybool') is False

    assert 'Jaime' in f('person.full_name')
    assert 'Lannister' in f('person.full_name')

    assert 'en_GB' in f('locale.code')

    assert '@' in f('email')

    assert f('location.state')
    assert f('location.city')


# Generated at 2022-06-14 01:08:03.193215
# Unit test for method create of class Schema
def test_Schema_create():
    """Test case for method create of class Schema."""
    from mimesis.enums import Gender
    from mimesis.schema import Field
    from mimesis.typing import Person

    schema = Field()

    def person_schema() -> Person:
        """Creates a dict with person data."""
        return {
            'full_name': schema('full_name'),
            'address': schema('address'),
            'gender': schema('gender', value_updater=lambda x: Gender.MALE),
        }

    for person in Schema(person_schema).create(3):
        assert isinstance(person, dict), (
            'Not filled schema returned by class Schema'
        )
        assert 'full_name' in person, (
            'Not filled schema returned by class Schema'
        )
       

# Generated at 2022-06-14 01:08:12.226406
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Check that magic method works."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('ru')

    field = Field(locale='ru', providers=[person])

    name = field('full_name', gender=Gender.MALE)
    assert name
    assert type(name) == str

    surname = field('surname', gender=Gender.FEMALE)
    assert surname
    assert type(surname) == str



# Generated at 2022-06-14 01:08:14.159935
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert callable(f('text', 'name'))

# Generated at 2022-06-14 01:08:21.157561
# Unit test for method create of class Schema
def test_Schema_create():
    def schema():
        return {
            'first_name': Field('en').name(),
            'last_name': Field('en').surname(),
            'address': Field('en').address(),
            'phone': Field('en').telephone(),
            'email': Field('ru').email(),
        }

    s = Schema(schema)
    result = s.create(10)
    assert len(result) == 10

# Generated at 2022-06-14 01:08:31.040136
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.data import (
        ADJECTIVES,
        NOUNS,
    )
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    result = AbstractField()('uuid')
    assert isinstance(result, str) and len(result) == 36

    result = AbstractField()('text')
    assert isinstance(result, str) and len(result) > 0

    result = AbstractField()('code')
    assert isinstance(result, str) and len(result) > 0

    result = AbstractField()('username')
    assert isinstance(result, str) and len(result) > 0

    result = AbstractField()('username', length=10)
    assert isinstance(result, str) and len(result) == 10


# Generated at 2022-06-14 01:08:33.318683
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('address.building_number') != ''

# Generated at 2022-06-14 01:08:41.656335
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Create instance with locale 'en'
    field = Field(locale='en')

    # All of this field are not supported
    assert field('__name__') is None
    assert field.__name__

    # All of this field are supported
    assert callable(field.datetime)
    assert callable(field.processors.markdown)
    assert callable(field.choice.fruits)
    assert callable(field.time.dst)
    assert callable(field.processors.markdown)
    assert callable(field.choice.fruits)
    assert field('datetime') is not None
    assert field('processors.markdown') is not None
    assert field('choice.fruits') is not None
    assert field('time.dst') is not None

# Generated at 2022-06-14 01:09:43.947946
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of class AbstractField."""
    f = Field()

    # call without name
    f()

    # call with name
    f('hello')

    # call with key
    f(name='hello', key='lower')

    # call with kwargs
    f(name='hello', key='lower', num=5)

    # call by using tails
    f('en.hello')
    f('en.hello', key='lower')
    f('en.hello', key='lower', num=5)
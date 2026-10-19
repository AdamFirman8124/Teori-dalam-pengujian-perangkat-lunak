

# Generated at 2022-06-14 01:07:37.318751
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.enums import Gender
    from mimesis.schema import Field
    from mimesis.schema import Schema

    class PersonSchema:
        """Test schema."""

        def __init__(self):
            self.example = Field('example')
            self.gender = Field('gender')
            self.full_name = Field('full_name')
            self.gender = Field('gender')
            self.occupation = Field('occupation')
            self.which_gender = Field('choice', data=Gender)
            self.name = Field('name')

    schema = Schema(PersonSchema)
    data = schema.create(iterations=10)

    assert isinstance(data, list)
    assert len(data) == 10
    assert all(isinstance(obj, dict) for obj in data)


# Generated at 2022-06-14 01:07:38.432033
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert Field() is not None

# Generated at 2022-06-14 01:07:48.905995
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method ``AbstractField.__call__``."""
    from mimesis.providers.person import Person
    from mimesis.providers.business import Business

    class Wrapper(AbstractField):
        pass

    person = Person('en')
    business = Business('en')
    field = Wrapper('en', providers=[business, person])

    assert field('full_name') == person.full_name()
    assert field('full_name', key=str.upper) == person.full_name().upper()

    with Wrapper('en', providers=[person]) as person_field:
        assert person_field('full_name') == person.full_name()
        assert person_field('full_name', key=str.upper) == person.full_name().upper()


# Generated at 2022-06-14 01:08:02.280127
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.providers import Address, Person
    from mimesis.enums import Gender
    from mimesis.schema import Field
    from mimesis.typing import SchemaType

    Person = Person('en', seed=42)

    def example_schema(field: Field) -> SchemaType:
        return {
            'full_name': field('full_name'),
            'age': field('age'),
            'gender': field('gender', value=Gender.MALE),
            'email': field('email'),
            'home_address': {
                'country': field('country'),
                'region': field('region'),
                'city': field('city'),
            },
        }

    test_schema = Schema(example_schema)

# Generated at 2022-06-14 01:08:10.344406
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    name = field._gen.choice.Meta.name
    data = field(name)

    assert callable(field._gen.choice)
    assert isinstance(field(name), str)
    assert isinstance(field(name), str)
    assert data == field(name)

    field2 = AbstractField(providers=[field._gen.choice])
    assert field2(name) != field(name, seed=field2.seed)

# Generated at 2022-06-14 01:08:11.172671
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    pass

# Generated at 2022-06-14 01:08:23.598091
# Unit test for constructor of class AbstractField
def test_AbstractField():
    from mimesis.providers.datetime import Datetime, Timezone
    from mimesis.providers.network import Network

    def assert_field(field, name, value):
        assert isinstance(field, AbstractField) and \
            isinstance(field(), AbstractField)

        result = field(name)
        assert isinstance(value, list) and result in value

    field = Field()

    assert_field(field, 'timezone', Timezone.meta().timezones)
    assert_field(field, 'timezone.name',
                 Timezone.meta().timezones)
    assert_field(field, 'datetime.timezone',
                 Timezone.meta().timezones)


# Generated at 2022-06-14 01:08:35.199712
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.providers import Person, Address

    class MySchema:
        def __init__(self, field: AbstractField):
            self.field = field
            self.data = {
                'full_name': field('full_name'),
                'address': field('address.full_address'),
                'age': field('age'),
            }

        def __call__(self) -> JSON:
            return self.data

    schema = Schema(MySchema)
    sc = schema.create(iterations=2)
    assert isinstance(sc[0], JSON)
    assert isinstance(sc, list)
    assert len(sc) == 2



# Generated at 2022-06-14 01:08:40.555850
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    af = AbstractField()
    assert af("choice", (1, 2, 3)) == 1



# Generated at 2022-06-14 01:08:43.812483
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for AbstractField.__call__."""
    field = AbstractField()
    assert field('full_name') is not None

# Generated at 2022-06-14 01:09:08.548866
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    gen = Field()
    gen('code')
    gen('code', code_type='hex')
    gen('text', 'Sentence')



# Generated at 2022-06-14 01:09:17.187083
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()

    field('foo')
    field('foo', 'bar')
    field('foo', baz='baz')
    field('foo', key=lambda x: x)  # Function will be applied
    field('foo', key=lambda x: x)  # Function will not be applied
    # Unsupported field
    try:
        field('unsupported')
    except UnsupportedField:
        pass
    # Wrong field name
    try:
        field('wrong.field.name')
    except UnacceptableField:
        pass
    # Undefined field
    try:
        field()
    except UndefinedField:
        pass



# Generated at 2022-06-14 01:09:21.854951
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method __call__ of class AbstractField."""
    field = Field()
    f = field('name')
    assert f is not None
    assert isinstance(f, str)

# Generated at 2022-06-14 01:09:26.417160
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test call with provider name."""
    fields = AbstractField()
    assert isinstance(fields.text(words=10), str)
    assert fields.text(name='text.text', words=10) == fields.text(words=10)



# Generated at 2022-06-14 01:09:34.263459
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of class AbstractField."""

    field = AbstractField(locale='ru')
    value = field('text.words', amount=1)

    assert isinstance(value, str)
    assert len(value.split()) == 1

    def func(value: str) -> str:
        return value.upper()

    value = field('text.words', amount=1, key=func)
    assert value.split() == value.split()

# Generated at 2022-06-14 01:09:42.026316
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    def return_html(x: str) -> str:
        return str(x)

    field = Field()
    assert field('url', scheme='https') == 'https://www.example.com'
    assert field('phone', code='+7') == "+7 (913) 286-18-06"
    assert field('system.uuid4') == "f610d3c7-a5f5-4b0f-b0a1-fefdafbc874c"
    assert field('system.uuid4', key=return_html) == "f610d3c7-a5f5-4b0f-b0a1-fefdafbc874c"

# Generated at 2022-06-14 01:09:46.252239
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    field = Field()
    method = field('datetime')
    assert isinstance(method, Callable)



# Generated at 2022-06-14 01:09:49.893207
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Given
    fld = Field()

    # When
    result = fld('datetime.now')

    # Then
    assert result is not None
    assert isinstance(result, str)

# Generated at 2022-06-14 01:09:59.171817
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    class TestSchema(object):
        """Test Schema object."""

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            """Initialize test schema."""
            self.client = 'lorem ipsum'
            self.field = Field(*args, **kwargs)

        def get_schema(self) -> dict:
            """Return schema.

            :return: Schema.
            """
            return {
                'client': self.client,
                'name': self.field('person.full_name'),
            }

    schema = TestSchema()
    assert schema.get_schema() == {
        'client': 'lorem ipsum',
        'name': 'Heather Stewart',
    }

    schema = TestSchema(locale='ru')
    assert schema

# Generated at 2022-06-14 01:10:08.120050
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    receiver = Field('ru', '1234')
    provider1 = receiver._gen.datetime
    provider2 = receiver._gen.text
    result = receiver('day', provider=provider1)
    assert result == provider1.day(provider=provider1)
    assert isinstance(result, int)
    result = receiver('text', provider=provider2)
    assert result == provider2.text(provider=provider2)
    assert isinstance(result, str)
    result = receiver('text')
    assert result == provider2.text()
    assert isinstance(result, str)



# Generated at 2022-06-14 01:10:57.465962
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField(seed=42)
    provider = field('provider')
    assert 'en' == provider.locale
    assert 42 == field._gen._seed

# Generated at 2022-06-14 01:11:05.342485
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test calling method __call__ of class AbstractField."""
    field = AbstractField()
    assert field('uuid')
    assert field(name='uuid')
    assert field('uuid', version=4)
    assert field('uuid', version=4, key=str)
    #
    import uuid
    assert field('uuid', version=4, key=uuid.UUID)


# Generated at 2022-06-14 01:11:11.527428
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('password', length=2)
    assert field('password', length=2, key=lambda x: x.upper()) is None
    assert field('get_random_int', a=-1, b=10, key=lambda x: x ** 2)



# Generated at 2022-06-14 01:11:16.769680
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()

    # Test for None
    assert field() is None

    # Test for common cases
    assert field('person.name')
    assert field('person.name', key=lambda x: x.upper()) == \
           field('person.name').upper()

# Generated at 2022-06-14 01:11:28.456305
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    import copy
    from mimesis.enums import Gender
    from mimesis.providers.address import (
        Address,
        AddressProvider,
    )

    f = AbstractField()

    class TestAddress(Address):
        """Test address class."""

        def full_name(self, gender: Gender = None) -> str:
            return 'Address'

    TestAddressProvider = AddressProvider(copy.copy(f))

    f.add_providers(TestAddressProvider.__name__, TestAddressProvider())

    assert (f('full_name') == 'Address')
    assert (f(
        'full_name',
        gender=Gender.MALE,
    ) == 'Address')

# Generated at 2022-06-14 01:11:38.653242
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from datetime import date

    locale = 'ru'
    field = AbstractField(locale)
    date_ = date(2018, 11, 28)

    # Successful
    assert field('datetime.date', year=2018, month=11, day=28) == date_
    assert field('datetime', year=2018, month=11, day=28) == date_
    assert field('datetime.date', year=2018, month=11, day=28,
                 key=lambda x: x.strftime('%d/%m/%Y')) == '28/11/2018'
    assert field('cryptographic.hash',
                 key=lambda x: (x.hexdigest(), x))[0] == 'c68f39913f901f3ddf44c707357a7d70e4f1452'
   

# Generated at 2022-06-14 01:11:48.240089
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    import random as rnd
    from mimesis.data import DATABASES, GENDERS
    from mimesis.enums import Gender

    f = AbstractField(seed=42)
    f2 = AbstractField(seed=42)

    random_int = rnd.randint(1,10)
    assert f('integer', maximum=random_int) == f2('integer', maximum=random_int) == 3

    assert f('integer', minimum=random_int, maximum=100) == f2('integer', minimum=random_int, maximum=100) == 38
    assert f('integer', minimum=random_int, maximum=100) != f2('integer', minimum=random_int, maximum=100) == 74

    rnd_gender = rnd.choice(list(GENDERS.values()))
    assert f('gender')

# Generated at 2022-06-14 01:11:54.273515
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.internet import Internet

    field_i = Field(providers=(Internet,))
    assert field_i('ipv4') is not None

    field_u = Field(providers=(Internet,))

    # Check for KeyError (UnsupportedField)
    # ~~ https://github.com/lk-geimfari/mimesis/issues/619
    try:
        field_u('choice')
    except KeyError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 01:12:02.519466
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Initialize field
    field = Field()

    # Call with string
    result = field('uuid')
    # Call with string and key
    result = field('uuid', key=lambda x: x.upper())
    # Call with string and keyword arguments
    result = field('uuid', digit=False)

    # Call with string which contains '.'
    result = field('security.md5')
    # Call with string and keyword arguments
    result = field('security.md5', seed=None)

    # Call with string which contains '..'
    result = field('security.md5.name')



# Generated at 2022-06-14 01:12:13.505136
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Tests AbstractField."""
    locale = 'en'
    seed = 'mimesis'

    af = AbstractField(locale, seed)

    # Commented because of
    # https://github.com/lk-geimfari/mimesis/issues/619
    # assert 'choice' == af('choice')
    # assert 1 == af('choice', (1, 2, 3, 4))
    assert af('platform', key=lambda x: x.lower()) in ['linux', 'mac', 'windows']
    assert af('date', year=1995, month=1, day=1, fmt='%y-%m-%d') == '95-01-01'
    assert af('system', 'hostname')


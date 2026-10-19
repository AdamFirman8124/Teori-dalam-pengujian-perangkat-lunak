

# Generated at 2022-06-14 01:07:32.614003
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()

    assert field('text') != field('text')
    assert field('uuid4') != field('uuid4')
    assert field('uuid4') != field('uuid4')
    assert field('uuid4') == field('uuid4') == str(field)
    assert field('useragent', key=lambda x: x.get('family')) == 'Other'
    assert field('useragent', key=lambda x: x.get('version')) == '0.0.0'
    assert field('internet.ip_v4') != field('internet.ip_v4')
    assert field('datetime.datetime_now') != field('datetime.datetime_now')
    assert field('datetime.time') != field('datetime.time')
    assert field('text', length=10)


# Generated at 2022-06-14 01:07:34.018208
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('full_name')


# Generated at 2022-06-14 01:07:42.771230
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from random import randint
    from string import ascii_letters

    f = Field()
    for i in range(100):
        # Check names of methods
        # and data returned by them
        name = ''.join(
            [i for i in ascii_letters if i.isalpha()]
            [randint(1, len(ascii_letters))]
        )
        result = f(name)
        assert name in dir(f)
        assert len(result) > 0

        # Check names of methods
        # and data returned by them
        # with lower the first letter
        name = ''.join(
            [i for i in ascii_letters if i.isalpha()]
            [randint(1, len(ascii_letters))]
        )
        result = f(name=name)

# Generated at 2022-06-14 01:07:45.030184
# Unit test for method create of class Schema
def test_Schema_create():
    assert len(Schema(lambda: None).create()) == 0
    assert len(Schema(lambda: None).create(iterations=3)) == 3

# Generated at 2022-06-14 01:07:53.817088
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test AbstractField."""
    obj = AbstractField()
    assert isinstance(obj, AbstractField)
    assert obj(name='email')
    assert obj(name='email', key=str.upper)
    assert obj(name='email', key=str.upper, full=True)
    assert obj(name='ipv4')
    assert obj(name='ipv4', key=lambda x: x)
    assert obj(name='ipv4', key=lambda x: x, private=True)
    assert obj(name='system.choice')

# Generated at 2022-06-14 01:08:06.829119
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Check AbstractField.__call__()."""
    # This test checks the work of the method name
    # which should return any method from the provider
    # by name.
    # This test is also checking the successful work
    # of the provider name that means that if the
    # method names are not unique, the first method will
    # be returned.
    f = Field()

    assert f(name='uuid4') != f(name='uuid4')
    assert f(name='uuid4') != f(name='uuid4')

    # Check that result is different
    # if the name has provider name
    assert f(name='cryptographic.uuid4') != f(name='cryptographic.uuid4')
    assert f(name='internet.uuid4') != f(name='internet.uuid4')

    #

# Generated at 2022-06-14 01:08:12.185943
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test abstract field method __call__."""
    field = Field()
    name = 'full_name'
    key = lambda x: x.split(' ')[0]
    result = field(name=name, key=key)
    assert isinstance(result, str)

# Generated at 2022-06-14 01:08:24.092046
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis import cls_
    from mimesis import roman
    from mimesis.enums import Gender
    from mimesis.schema import AbstractField

    field = AbstractField()
    assert field('get_full_name', gender=Gender.FEMALE) == \
        cls_.Person('en').get_full_name(gender=Gender.FEMALE)
    assert field('name', gender=Gender.MALE) == \
        cls_.Person('en').name(gender=Gender.MALE)
    assert field('get_first_name_male') == \
        cls_.Person('en').get_first_name_male()
    assert field('roman', x=10) == roman.RomanNumber('en').roman(x=10)

# Generated at 2022-06-14 01:08:25.880990
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    assert Field().__call__('name') == 'Mimesis'

# Generated at 2022-06-14 01:08:30.941451
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field.locale == 'en'
    assert field.seed is None

    field = AbstractField('ru', 'some-seed')
    assert field.locale == 'ru'
    assert field.seed == 'some-seed'


# Generated at 2022-06-14 01:08:55.482684
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field()

    def _test(method: str) -> bool:
        return f(method, 'person', key=str)

    # won't raise exception
    _test('full_name')

# Generated at 2022-06-14 01:08:59.901514
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test initialization of class Field."""
    f = Field()
    assert f
    assert f.seed is None
    assert f.locale == 'en'


# Unit test magic method call

# Generated at 2022-06-14 01:09:02.842541
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert f is not None
    assert f.seed is not None
    assert f.locale is not None



# Generated at 2022-06-14 01:09:08.972938
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = AbstractField(locale='en', seed=1234)
    result = f('telephone', key=lambda x: x.replace('-', ' '))

    assert result == '622 337 748'

    f = AbstractField(locale='en', seed=1234)
    result = f('datetime.datetime',
               key=lambda x: x.strftime('%d.%m.%Y'))

    assert result == '12.01.2008'

# Generated at 2022-06-14 01:09:15.889919
# Unit test for method create of class Schema
def test_Schema_create():
    """Test AbstractField.__call__ with another class."""
    from mimesis.schema import Field

    field = Field()

    schema = Schema(lambda: {
        'name': field('first_name', gender='male'),
        'email': field('email'),
    })

    data = schema.create(iterations=2)

    for document in data:
        assert 'name' in document
        assert 'email' in document

# Generated at 2022-06-14 01:09:28.229964
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    def make_address(address):
        return address.replace(',', '')

    def make_name(name):
        return name.upper()

    field = AbstractField()

    assert field('code', pattern='###-###') == '085-547'
    assert field('person.full_name', gender=Gender.FEMALE) == 'Tammy Hester'
    assert field(
        'address.street_name',
        key=make_address,
    ) == '1238 William Meadors Street'

    field._gen.add_providers(Address(field.locale, field.seed),
                             Person(field.locale, field.seed))


# Generated at 2022-06-14 01:09:33.135064
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test the constructor of class AbstractField."""
    field = Field()
    # ValueError: The provider is not supported: None
    assert field(name='None') == None

# Generated at 2022-06-14 01:09:33.926225
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    pass

# Generated at 2022-06-14 01:09:48.979671
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method __call__ of class AbstractField."""
    expected_names = [
        'Person.name',
        'name',
        'Person.occupation',
        'occupation',
        'Person.full_name',
        'full_name',
    ]
    result_names = []

    field = Field()

    # Check first case
    # Result must be an instance of string.
    result = field('Person.name')
    assert isinstance(result, str)
    result_names.append(result)

    # Check second case
    # In case when the method name is not a part of
    # any data provider, we expect a KeyError.
    try:
        field('unknown_name')
    except KeyError:
        result_names.append('unknown_name')

    # Check third case
    # In

# Generated at 2022-06-14 01:09:57.687317
# Unit test for method create of class Schema
def test_Schema_create():
    def my_schema() -> dict:
        """Example of simple schema."""
        return {
            'name': 'Ivan',
            'age': '20',
        }

    schema = Schema(my_schema)
    assert [
        {'name': 'Ivan', 'age': '20'},
        {'name': 'Ivan', 'age': '20'},
        {'name': 'Ivan', 'age': '20'},
    ] == schema.create(3)

# Generated at 2022-06-14 01:10:31.678214
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Define a schema
    def address():
        return {
            'country': Field('country.name', key=str.title),
            'region': Field('region.name', key=str.title),
            'city': Field('city.name', key=str.title),
            'address': Field('address.address'),
            'postal_code': Field('address.postal_code'),
        }

    schema = Schema(address)
    data = schema.create(10)
    assert len(data) == 10

# Generated at 2022-06-14 01:10:43.183312
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method AbstractField.__call__.

    :return: True if test passed.
    """
    provider = Generic('en')
    field = AbstractField(providers=[provider])
    res_1 = field('choice', choices=['a', 'b', 'c'])
    res_2 = field('choice', choices=['a', 'b', 'c'])

    assert field('choice', choices=['a', 'b', 'c']) in ('a', 'b', 'c')
    assert res_1 == res_2

    a = field('choice', choices=[1, 2, 3], key=str)
    b = field('choice', choices=[1, 2, 3], key=str)

    assert a == b

    property_a = field('property', categories=[
        'Person', 'Name'])
    property_

# Generated at 2022-06-14 01:10:52.702720
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of class AbstractField.

    Check if it returns proper value when
    trying to get value by name of method.
    """
    field = Field()

    # Set of pairs (method name, type of the result)

# Generated at 2022-06-14 01:11:00.500552
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.data import CAR_MAKERS

    field = AbstractField()
    assert field('manufacturer') in CAR_MAKERS
    assert field('manufacturer', key=lambda x: x) in CAR_MAKERS
    assert field('foo') is None
    assert field('food') is None
    assert field('data') is None
    assert field('data.foo') is None
    assert field('data.food') is None
    assert field('china.manufacturer') is None
    assert field('china') is None

# Generated at 2022-06-14 01:11:12.016360
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    field = AbstractField()  # pylint: disable=no-value-for-parameter

    field('name')
    field('first_name')
    field('name.gender')
    field('name.gender', 'M')
    field('name.gender', gender='M')
    field('datetime.datetime', datetime=True)
    field('datetime.datetime', datetime=True, key=lambda x: x.year)
    field('datetime.datetime', datetime=True, key=lambda x: x.month)
    field('datetime.datetime', datetime=True, key=lambda x: x.day)

# Generated at 2022-06-14 01:11:19.933540
# Unit test for method create of class Schema
def test_Schema_create():
    """Function which unit test method create of class Schema."""
    import json

    class _Person:
        """A class with a schema."""

        @staticmethod
        def schema():
            """Return schema."""
            return {
                "first_name": "Person.name",
                "last_name": "Person.surname",
                "age": "Person.age",
                "birthday": "Person.birthday",
            }

    person = Field()

    schema = Schema(_Person.schema)
    result = schema.create(iterations=3)


# Generated at 2022-06-14 01:11:32.145244
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__."""
    field = Field()

    assert field('uuid')
    assert field('uuid', hyphenated=True)
    assert field('uuid', key=lambda x: x.upper())
    assert field('uuid', hyphenated=True, key=lambda x: x.upper())

    assert field('address.city')
    assert field('address.city', key=lambda x: x.title())
    assert field('address.city_name')
    assert field('address.building_number')
    assert field('address.building_number', key=lambda x: x.title())

    assert field('science.chemistry.element_symbol')
    assert field('science.chemistry.element_symbol', key=lambda x: x.title())

# Generated at 2022-06-14 01:11:39.883876
# Unit test for method create of class Schema
def test_Schema_create():
    """Check that a list of filled schemas is valid."""
    from mimesis.schema import Field
    from mimesis.typing import JSON

    field = Field()

    def schema():
        return {
            'name': field('person.full_name'),
            'address': field('address.address'),
            'phone': field('telecom.mobile_phone'),
            'gender': field('datetime.gender'),
        }

    schema_obj = Schema(schema)
    result = schema_obj.create(iterations=2)
    assert isinstance(result, list)
    assert isinstance(result[0], JSON)
    assert isinstance(result[1], JSON)
    assert isinstance(result[0], JSON) is True
    assert isinstance(result[0], JSON) is True



# Generated at 2022-06-14 01:11:46.204482
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.enums import Gender
    from mimesis.schema import Field

    field = Field()
    schema = Schema(lambda: {
        'name': field('full_name', gender=Gender.MALE),
        'address': field('address'),
    })
    result = schema.create()
    assert len(result) == 1
    assert isinstance(result, list)
    result.append(schema.create(5))
    assert len(result) == 2

# Generated at 2022-06-14 01:11:52.878091
# Unit test for method create of class Schema
def test_Schema_create():
    def schema() -> JSON:
        field = Field()
        return {
            'name': field('name'),
            'surname': field('surname'),
            'age': field('age_random'),
            'email': field('email'),
            'country': field('country'),
            'city': field('city'),
            'number': field('number_sequence'),
        }

    generator = Schema(schema)
    assert len(generator.create(20)) == 20

# Generated at 2022-06-14 01:12:48.739324
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    g = Generic('ru')
    field = AbstractField(locale='ru', providers=(g.address,))
    assert field.__call__(name='building_number') > 0

    field = AbstractField()
    with raises(UndefinedField):
        field.__call__()

# Generated at 2022-06-14 01:12:52.902180
# Unit test for method create of class Schema
def test_Schema_create():
    assert isinstance(Schema(lambda: {'foo': 'bar'}).create(1)[0], dict)

# Generated at 2022-06-14 01:12:59.681214
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField(locale='ru', seed=123)
    assert str(field) == 'AbstractField <ru>'
    assert field(name='string', lowercase=True) == 'gxhkjxfz'
    assert field(name='Code.iban', country_code='RU') == 'RU6316336000507765037'



# Generated at 2022-06-14 01:13:07.155251
# Unit test for method create of class Schema
def test_Schema_create():
    """Test that the method returns the right list."""
    from mimesis import Person
    from mimesis import Generic

    def schema():  # pylint: disable=unused-variable, missing-docstring
        person = Person('en')
        return {
            'name': person.full_name(),
            'age': person.age(18, 60),
            'gender': person.gender(),
            'birthday': {
                'year': Generic('en').year(),
                'month': Generic('en').month(),
                'day': Generic('en').date(),
            }
        }

    s = Schema(schema)
    assert isinstance(s.create(), list)
    assert len(s.create(5)) == 5
    assert len(s.create()) == 1

# Generated at 2022-06-14 01:13:11.361093
# Unit test for method create of class Schema
def test_Schema_create():
    def _schema():
        return {
            'data': [
                {'id': 1, 'name': 'John Doe'},
                {'id': 2, 'name': 'Adam Levine'},
                {'id': 3, 'name': 'Kate Moss'},
            ]
        }

    result = Schema(_schema).create(3)
    assert result == [{
        'data': [
            {'id': 1, 'name': 'John Doe'},
            {'id': 2, 'name': 'Adam Levine'},
            {'id': 3, 'name': 'Kate Moss'},
        ]
    }] * 3

# Generated at 2022-06-14 01:13:16.004800
# Unit test for method create of class Schema
def test_Schema_create():
    """Test method create of class Schema."""
    data = Schema(lambda: []).create(3)
    assert len(data) == 3
    assert all([isinstance(i, list) for i in data])

# Generated at 2022-06-14 01:13:22.613420
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Initialize field object
    field = Field()
    # Get method name (of any data provider)
    name = 'person.full_name'
    # Get method with name
    m = getattr(field, name)
    # Check if result equals with value
    assert m() == field(name)

# Generated at 2022-06-14 01:13:31.794126
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Makes an instance of AbstractField.
    field = Field()

    # Check AttributeError
    try:
        field('foo')
    except UndefinedField:
        pass
    else:
        raise AssertionError()

    # Check ValueError
    try:
        field('bar')
    except UndefinedField:
        pass
    else:
        raise AssertionError()

    # Check callable
    test = lambda x: x
    assert isinstance(field('uuid', key=test), str)

# Generated at 2022-06-14 01:13:45.560127
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.files import File

    field = Field()
    assert field('hex_color') in field._gen.color.WebColor.colors
    assert field('hex_color') in field._gen.color.WebColor.colors
    assert field('name', key=lambda x: x.upper()) == 'АНТОН'
    assert field('file.name') in File.name
    assert field('file.extension') in File.extension

    field = Field('ru')
    assert field('hex_color') in field._gen.color.WebColor.colors
    assert field('hex_color') in field._gen.color.WebColor.colors

# Generated at 2022-06-14 01:13:51.090427
# Unit test for method create of class Schema
def test_Schema_create():
    def schema():
        return {
            'test': 'foo',
        }

    assert Schema(schema).create(10) == [
        {'test': 'foo'} for _ in range(10)
    ]
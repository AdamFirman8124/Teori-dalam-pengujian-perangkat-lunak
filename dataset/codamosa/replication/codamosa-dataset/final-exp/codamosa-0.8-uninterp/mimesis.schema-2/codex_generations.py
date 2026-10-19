

# Generated at 2022-06-14 01:07:15.816929
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert isinstance(field, AbstractField)
    assert field.__class__.__name__ == 'AbstractField'



# Generated at 2022-06-14 01:07:18.239049
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert callable(field)
    assert isinstance(field('datetime'), str)


# Generated at 2022-06-14 01:07:22.140622
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of the class AbstractField."""
    field = AbstractField()
    assert field('__doc__')
    assert field('choice', key=str)
    assert field('address.address')



# Generated at 2022-06-14 01:07:29.504566
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis import Person
    from mimesis.enums import Gender

    data = Schema(Person('en').create_person_schema)
    men = data.create(100)
    assert len(men) == 100
    for person in men:
        assert person['name']

        if person['gender'].lower() == Gender.MALE.value.lower():
            assert person['male_title']
        else:
            assert person['female_title']

    women = data.create(1000)
    assert len(women) == 1000
    for person in women:
        assert person['name']

        if person['gender'].lower() == Gender.MALE.value.lower():
            assert person['male_title']
        else:
            assert person['female_title']

# Generated at 2022-06-14 01:07:31.333301
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field()
    result = f('person.full_name')
    assert isinstance(result, str)

# Generated at 2022-06-14 01:07:33.768244
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = Field()
    assert f.__str__() == 'AbstractField <en>'

# Generated at 2022-06-14 01:07:35.910198
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test constructor without parameters."""
    field = AbstractField()
    assert str(field) == 'AbstractField <en>'



# Generated at 2022-06-14 01:07:43.884985
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('date_time.date')

    # Test case for UnacceptableField
    try:
        field('list.list.list')
    except UnacceptableField:
        assert True

    # Test case for UnsupportedField
    try:
        field('MethodOfUnsupportedDataProvider')
    except UnsupportedField:
        assert True

    # Test case for UndefinedField
    try:
        field()
    except UndefinedField:
        assert True



# Generated at 2022-06-14 01:07:49.879067
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()

    assert isinstance(field, AbstractField)
    assert hasattr(field, 'locale')
    assert hasattr(field, 'seed')
    assert hasattr(field, '_gen')
    assert hasattr(field, '_table')



# Generated at 2022-06-14 01:08:03.197293
# Unit test for method create of class Schema
def test_Schema_create():
    import sys
    import pytest

    for version in ['2.7', '3.4', '3.5', '3.6', '3.7']:
        if sys.version_info.major == 2 and sys.version_info.minor == 7:
            # Default Python interpreter
            schema = Schema(lambda: {'a': 'a'})
            assert schema.create() == [{'a': 'a'}]
        elif sys.version_info.major == 2 and sys.version_info.minor != 7:
            # Not supported versions
            with pytest.raises(UndefinedSchema):
                Schema(lambda: {'a': 'a'})

# Generated at 2022-06-14 01:08:23.144887
# Unit test for method create of class Schema
def test_Schema_create():
    def schema():  # pylint: disable = missing-docstring
        return {'hello': 'world'}

    assert Schema(schema=schema).create(iterations=3) == [
        {'hello': 'world'},
        {'hello': 'world'},
        {'hello': 'world'},
    ]

# Generated at 2022-06-14 01:08:26.633087
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    import doctest
    doctest.testmod(raise_on_error=False)

# Generated at 2022-06-14 01:08:38.583821
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    result1 = field('age', lower=10, upper=90)
    assert result1 in range(10, 91)
    result2 = field('provider.age', lower=10, upper=90)
    assert result2 in range(10, 91)
    result3 = field('person.full_name')
    assert result3
    result4 = field('full_name')
    assert result4
    result5 = field('full_name', provider='person')
    assert result5
    result6 = field(
        'full_name',
        provider='person',
        key=lambda name: name.split(' ')[-1],
    )
    assert result6 == result5.split(' ')[-1]

# Generated at 2022-06-14 01:08:50.275088
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """
    That method should works well.

    Test method __call__ of class AbstractField.
    """
    field = Field()

    try:
        field()
    except UndefinedField:
        assert True
    else:
        assert False

    try:
        field(name='underscore')
    except UnsupportedField:
        assert True
    else:
        assert False

    try:
        field(name='t.n.t')
    except UnacceptableField:
        assert True
    else:
        assert False

    value = field(name='datetime.datetime', pattern='%Y.%m.%d %H:%M:%S')
    assert isinstance(value, str)
    assert value == '1976.11.18 15:45:01'

# Generated at 2022-06-14 01:09:01.116346
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from importlib import import_module
    from mimesis import Generic
    from mimesis.exceptions import UndefinedField

    gen = Generic('en')
    field = AbstractField(
        providers=[import_module('mimesis.providers.network')]
    )
    result = field('mac_address')
    assert len(result.split(':')) == 6
    assert result == gen.network.mac_address()

    assert result == Field('en', providers=[
        import_module('mimesis.providers.network')])('mac_address')
    assert result == Field(providers=[
        import_module('mimesis.providers.network')])('mac_address')

# Generated at 2022-06-14 01:09:07.198252
# Unit test for method create of class Schema
def test_Schema_create():
    # type: () -> None
    """Test method create of class Schema."""
    def _schema(obj):
        # type: (Any) -> JSON
        """Test schema."""
        return {
            'id': obj.code.isbn(),
            'name': obj.text.word(),
        }

    result = Schema(_schema).create(iterations=10)
    assert isinstance(result, list)

# Generated at 2022-06-14 01:09:09.656289
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test a call method of AbstractField."""
    assert isinstance(AbstractField()(), str)

# Generated at 2022-06-14 01:09:12.699638
# Unit test for constructor of class AbstractField
def test_AbstractField():
    af = AbstractField()
    assert af is not None
    assert af.seed is None
    assert af.locale == 'en'
    assert not af._table

# Generated at 2022-06-14 01:09:14.133097
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = Field()
    assert isinstance(field._gen, Generic)

# Generated at 2022-06-14 01:09:18.076875
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = Field()
    assert f.locale == 'en'
    assert f.seed is None

# Generated at 2022-06-14 01:09:38.550710
# Unit test for method create of class Schema
def test_Schema_create():
    """Check that method create of class Schema returns a needed list."""
    from mimesis.providers.schema import Schema

    sc = Schema()

    schema = {
        'name': sc.name(),
        'surname': sc.surname(),
        'address': sc.address(),
    }

    test = sc.create(schema, 4)
    assert isinstance(test, list)
    assert isinstance(test[0], dict)
    assert len(test) == 4
    assert list(test[0].keys()) == ['name', 'surname', 'address']



# Generated at 2022-06-14 01:09:43.795081
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    field = AbstractField()
    field(name='full_name')
    field(name='person.full_name')
    field(name='person.full_name', key=str.lower)

# Generated at 2022-06-14 01:09:49.995251
# Unit test for method create of class Schema
def test_Schema_create():
    schema = {'a': 1, 'b': 2}
    s = Schema(lambda: schema)
    assert s.create() == [schema]


if __name__ == '__main__':
    # Ignore PyTypeCheckerBear(#483)
    test_Schema_create()  # pragma: no cover

# Generated at 2022-06-14 01:09:59.170856
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Testing method __call__.

    This method should work as a standard call of method, but
    by the name of the method.
    """
    field = Field()

    assert field('enum', (1, 2, 3), value='a') == 'a'
    assert field('choice', ((1, 'a'), (2, 'b')), items=False) == 2

    # Test for explicit definition of provider
    assert field('datetime.timestamp') is not None

    # Test for key function
    assert field('timestamp', key=lambda x: int(x)) == field.timestamp()

    # Test for using default attributes
    provider_name = field.choice((1, 2, 3), items=False)
    method_name = field.choice((4, 5, 6), items=False)

# Generated at 2022-06-14 01:10:05.612163
# Unit test for method create of class Schema
def test_Schema_create():
    """Tests for Schema."""
    from mimesis import Person
    from mimesis.schema import Schema
    from mimesis.schema.types import JSON

    _person = Person('en')

    _schema = {
        'name': _person.full_name,
        'age': _person.age,
        'sex': _person.gender,
        'profession': _person.occupation,
    }

    data = Schema(_schema).create(iterations=10)
    assert isinstance(data, List)
    assert isinstance(data[0], JSON)

# Generated at 2022-06-14 01:10:08.622666
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert str(field) == 'AbstractField <en>'

    field = AbstractField(locale='ru')
    assert str(field) == 'AbstractField <ru>'



# Generated at 2022-06-14 01:10:12.736628
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test call of object of the class AbstractField."""
    field = AbstractField()
    assert field.__call__('name', 'male') == 'John'
    assert field.__call__('name', 'female') == 'Mary'
    assert field.__call__('text', 'lorem_ipsum') == 'Lorem ipsum dolor sit amet'

# Generated at 2022-06-14 01:10:17.103778
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test for the AbstractField."""
    expected = '<Field en>'
    field = AbstractField('en')
    result = str(field)
    assert result == expected



# Generated at 2022-06-14 01:10:22.868258
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    class TestField(AbstractField):
        """Test field."""

    fields = {
        'provider.method':
            TestField(locale='ru'),
        'method':
            TestField(locale='en'),
    }

    assert fields['provider.method']('provider.method')
    assert fields['method']('method')

# Generated at 2022-06-14 01:10:32.771657
# Unit test for method create of class Schema
def test_Schema_create():
    """Test for method create of class Schema."""
    from mimesis import Person
    p = Person('en')
    name = p.full_name()
    age = p.age()
    s = Schema(lambda: dict(name=name, age=age))

    result = s.create(5)
    assert isinstance(result, list)
    assert len(result) == 5
    assert all(isinstance(i, dict) for i in result)
    assert all(isinstance(i['name'], str) for i in result)
    assert all(isinstance(i['age'], int) for i in result)
    assert all(i['name'] == name for i in result)
    assert all(i['age'] == age for i in result)

# Generated at 2022-06-14 01:11:07.113935
# Unit test for constructor of class AbstractField
def test_AbstractField():
    from mimesis.schemes import AbstractScheme

    f = Field()
    assert isinstance(f, AbstractScheme)

    for lang, _ in f.available_locales():
        f = Field(locale=lang)
    assert f.locale == 'en'

    f = Field(seed=42)
    assert f.seed == 42

# Generated at 2022-06-14 01:11:11.010478
# Unit test for method create of class Schema
def test_Schema_create():
    import mimesis

    person_schema = mimesis.schema.Generic(locale='ru')
    schema = Schema(person_schema.person)

    assert len(schema.create(iterations=100)) == 100

# Generated at 2022-06-14 01:11:17.352438
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert callable(AbstractField.__init__)
    assert isinstance(AbstractField(), AbstractField)
    assert hasattr(AbstractField(), '__call__')
    assert isinstance(str(AbstractField()), str)
    assert isinstance(str(AbstractField('ru')), str)
    assert isinstance(str(AbstractField(seed=123)), str)


# Generated at 2022-06-14 01:11:20.010901
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert str(Field(seed=42)) == 'AbstractField <en>'

# Generated at 2022-06-14 01:11:29.706472
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field('get_gender') in ['male', 'female']
    assert field('get_gender', gender='male') == 'male'

    assert field('datetime.random_datetime', datetime=1993,
                 month=8, day=11, format='%Y-%m-%d') == '1993-08-11'

    assert field('get_locale') == 'en'
    assert field('get_seed') is None

    assert field('__len__(us)') == 50
    assert field('random_int', minimum=None, maximum=100) <= 100

# Generated at 2022-06-14 01:11:33.304574
# Unit test for method create of class Schema
def test_Schema_create():
    #: :type: Schema
    schema = Schema(lambda: {
        'name': 'Roger'
    })

    assert schema.create(5) == [{'name': 'Roger'} for _ in range(5)]



# Generated at 2022-06-14 01:11:37.702802
# Unit test for method create of class Schema
def test_Schema_create():
    """Test method create of Schema class."""
    def schema() -> dict:
        """Return dictionary."""
        return {'a': 1, 'b': 2}

    s = Schema(schema)
    assert len(s.create(5)) == 5

# Generated at 2022-06-14 01:11:39.742492
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Unit test for constructor of class AbstractField."""
    field = AbstractField()
    assert field is not None

# Generated at 2022-06-14 01:11:49.107234
# Unit test for method create of class Schema
def test_Schema_create():
    """Unit test for method create of class Schema.

    :return:
    """
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.geo import Geo

    def create_user_schema():
        """Define user schema."""
        return {
            "first_name": Field.person.name(),
            "last_name": Field.person.surname(),
            "address": Field.geo.address(),
            "dob": Field.datetime.date(start=1950, end=2000),
            "email": Field.person.email(),
            "phone": Field.person.telephone(),
            "ip_address": Field.internet.ip_address(),
        }

    data = Schema(create_user_schema)
    schema = data.create(2)


# Generated at 2022-06-14 01:11:53.448901
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert isinstance(field, AbstractField)


# Unit tests for method __call__ of class AbstractField

# Generated at 2022-06-14 01:13:22.686001
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    from mimesis.providers.datetime import Datetime

    field = Field(providers=[Datetime])
    assert isinstance(field('date'), str)

# Generated at 2022-06-14 01:13:35.653394
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    provider = Field()

    assert callable(provider), '[Errno 1] Callable object expected'

    # No params
    with Schema(lambda: provider()) as sc:
        data = sc.create()

    # Name
    with Schema(lambda: provider('name')) as sc:
        data = sc.create()

    # Name + Key
    with Schema(lambda: provider('name', key=lambda x: x.title())) as sc:
        data = sc.create()

    # Name + Kwargs
    with Schema(lambda: provider('first_name', gender='female')) as sc:
        data = sc.create()

    # Name + Key + Kwargs
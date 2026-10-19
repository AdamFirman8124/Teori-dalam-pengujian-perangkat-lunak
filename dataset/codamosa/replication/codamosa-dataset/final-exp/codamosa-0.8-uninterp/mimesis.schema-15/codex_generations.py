

# Generated at 2022-06-14 01:07:27.288668
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for calling magic method AbstractField.__call__."""
    from mimesis.enums import Gender
    from mimesis.providers import Cryptographic, Datetime, Person, Science
    from mimesis.providers.internet import Internet

    field = AbstractField(seed=15)
    field._gen.add_providers(Person, Datetime, Science, Internet, Cryptographic)
    try:
        field()  # No name is given
        assert False
    except UndefinedField:
        assert True
    except UnsupportedField:
        assert False

# Generated at 2022-06-14 01:07:34.380989
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field.locale == 'en'
    assert field.seed is None
    assert field._gen is not None
    assert field._table == {}

    field = AbstractField('en')
    assert field.locale == 'en'
    assert field.seed is None
    assert field._gen is not None
    assert field._table == {}

    import datetime
    field = AbstractField(seed=datetime.datetime.now())
    assert field.locale == 'en'
    assert field.seed is not None
    assert field._gen is not None
    assert field._table == {}

    class TestProvider:
        @staticmethod
        def foo():
            return 'Hello'

    field = AbstractField(providers=[TestProvider])
    assert field.locale == 'en'

# Generated at 2022-06-14 01:07:44.442553
# Unit test for method create of class Schema
def test_Schema_create():
    field = Field(seed=0)
    schema_ = {
        'id': field('uuid'),
        'name': field('full_name'),
        'age': field('age'),
    }

    s = Schema(schema_)
    res = s.create(iterations=10)
    for x in res:
        assert isinstance(x, JSON)


# Generated at 2022-06-14 01:07:50.850259
# Unit test for method create of class Schema
def test_Schema_create():
    def schema() -> JSON:
        """Example schema."""
        field = Field()
        return {
            'id': field('uuid'),
            'name': field('person.full_name'),
        }

    filled_schema = Schema(schema).create(iterations=5)
    assert len(filled_schema) == 5

# Generated at 2022-06-14 01:07:54.001494
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    value = field('choice', ['foo', 'bar', 'baz'])
    assert value in ['foo', 'bar', 'baz']

# Generated at 2022-06-14 01:08:01.164528
# Unit test for constructor of class AbstractField
def test_AbstractField():
    import pytest

    with pytest.raises(UndefinedField):
        # noinspection PyUnusedLocal
        def func() -> None:
            field = AbstractField()
            field()

    def func2() -> None:
        field = AbstractField()
        field('a', 'sdfsdfsdf')

    with pytest.raises(ValueError):
        func2()

# Generated at 2022-06-14 01:08:07.542316
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test init of class AbstractField."""
    f1 = AbstractField('en')
    assert f1.locale == 'en'

    f2 = AbstractField(seed=123456)
    assert f2.seed == 123456

    f3 = AbstractField(locale='en', seed=123456)
    assert f3.seed == 123456
    assert f3.locale == 'en'
    assert isinstance(f3._gen, Generic)

# Generated at 2022-06-14 01:08:14.651623
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.builtins import UkraineSpecProvider
    providers = [RussiaSpecProvider, UkraineSpecProvider]
    field = Field(providers=providers)
    assert field('russian.name') == field('russian.surname')
    assert 'ukrainian.tax_id' in dir(field)



# Generated at 2022-06-14 01:08:21.697147
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.address import Address
    from pprint import pprint

    field = AbstractField()
    assert field is not None

    field._gen.add_providers(Address)

    r = field('address.city')
    assert isinstance(r, str)

    assert r == field('address.city')

    address = field('address', country='US')
    assert isinstance(address, dict)
    pprint(address)

# Generated at 2022-06-14 01:08:27.818179
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for call method."""
    f = AbstractField()

    assert 'большой' == f('gender', case='nominative')
    assert 'a' == f('ordinal', num=1)
    assert 'United States of America' == f('country')

# Generated at 2022-06-14 01:08:53.413725
# Unit test for constructor of class AbstractField
def test_AbstractField():
    provider = Generic()
    f = AbstractField(providers=(provider,))
    assert f.locale == 'en'
    assert f._gen.provider is provider



# Generated at 2022-06-14 01:08:59.005514
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.base import BaseProvider as BP
    from mimesis.providers.user import BaseUser as BU
    f = AbstractField()
    assert f(name='full_name', key=str)
    assert f(name='BP.get_hash', method='md5', text='Hello world!')
    assert f(name='BU.full_name', key=list)

# Generated at 2022-06-14 01:09:01.208398
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert isinstance(field, AbstractField)



# Generated at 2022-06-14 01:09:02.309410
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field()


# Generated at 2022-06-14 01:09:12.377585
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()

    # Check working of case-insensitive
    result = field('Surname')
    assert isinstance(result, str)
    assert len(result) > 0

    # Check working of case-sensitive
    result = field('Name')
    assert isinstance(result, str)
    assert len(result) > 0

    # Check working of method which belongs to a specific provider
    result = field('address.zip_code')
    assert isinstance(result, str)
    assert len(result) == 9

    # Check that exception are raised if method not supported
    try:
        field('not_supported')
    except UnsupportedField as e:
        assert e.title == 'not_supported'
    else:
        raise Exception('Field not exists!')

    # Check that exception are raised if method not defined

# Generated at 2022-06-14 01:09:17.608055
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()

    assert callable(field) is True

# Generated at 2022-06-14 01:09:26.146328
# Unit test for method create of class Schema
def test_Schema_create():
    foo = 'schema.foo'
    schema = {foo: Field()}

    class Bar(Schema):
        """Test class Bar."""

        def __init__(self, **kwargs):
            """Initialize Bar.

            :param kwargs: Kwargs of Schema.
            """
            super().__init__(**kwargs)

    bar = Bar(schema=schema)

    assert isinstance(bar.create(), list)

# Generated at 2022-06-14 01:09:38.424399
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    schema = Schema(lambda: {
        'name': Field('person.full_name'),
        'title': Field('text.title', key=lambda x: x.capitalize()),
        'job': Field('job.profession'),
        'github': Field('internet.username',
                        key=lambda x: 'https://github.com/{}/'.format(x)),
    })

    data = schema.create(3)
    assert len(data) == 3
    assert data[0]['name']
    assert data[1]['name']
    assert data[2]['name']
    assert data[0]['title']
    assert data[1]['title']
    assert data[2]['title']
    assert data[0]['job']
    assert data[1]['job']

# Generated at 2022-06-14 01:09:47.379396
# Unit test for method create of class Schema
def test_Schema_create():
    def test_schema() -> dict:
        """Test schema."""
        return {
            'name': Field()('username'),
            'surname': Field()('last_name'),
            'email': Field()('email')
        }

    _schema = Schema(test_schema)
    data = _schema.create(iterations=5)
    assert len(data) == 5
    assert isinstance(data[0], dict)

# Generated at 2022-06-14 01:09:49.210609
# Unit test for constructor of class AbstractField
def test_AbstractField():
    af = AbstractField()

    assert af.locale == 'en'
    assert af.seed is None
    assert af._gen



# Generated at 2022-06-14 01:10:19.755432
# Unit test for method create of class Schema
def test_Schema_create():
    f = Field()
    assert len(Schema(lambda: {'a': f('person.name'), 'b': f('person.surname')}).create(2)) == 2

# Generated at 2022-06-14 01:10:31.387469
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Check the call magic method."""
    from mimesis.providers.address import Address

    field = AbstractField()
    # First scenario
    result = field('address')
    assert isinstance(result, str)

    # Second scenario
    result = field('Address.address')
    assert isinstance(result, str)

    # Third scenario
    result = field('Address.address', separator='\n')
    assert isinstance(result, str)

    # Fourth scenario
    address_provider = Address(field.locale, field.seed)
    field._gen.add_providers(address_provider)

    result = field('address')
    assert isinstance(result, str)

    result = field('Address.address')
    assert isinstance(result, str)


# Generated at 2022-06-14 01:10:38.473143
# Unit test for method create of class Schema
def test_Schema_create():
    """Test Schema.create()."""
    from mimesis.typing import JSON

    # pylint: disable=unused-variable
    @Field.schema(iterations=1)
    def test_schema() -> JSON:
        return {
            'foo': Field('datetime.datetime'),
        }

    schema = test_schema.create()
    assert schema[0]['foo'] == Field('datetime.datetime')()

# Generated at 2022-06-14 01:10:42.120331
# Unit test for constructor of class AbstractField
def test_AbstractField():
    abstract_field = AbstractField()
    assert isinstance(abstract_field, AbstractField)



# Generated at 2022-06-14 01:10:47.509131
# Unit test for method create of class Schema
def test_Schema_create():
    import pprint

    def schema(field: Field) -> dict:
        return {
            'name': field.name(),
            'phone': field.telephone(),
            'email': field.email(domains=['mail.ru']),
        }

    s = Schema(schema)
    pprint.pprint(s.create())

# Generated at 2022-06-14 01:10:59.303751
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of the class."""
    field = AbstractField()

    # Call of simple method
    result = field('name')
    assert result is not None

    # Call of method of a DataProvider
    result = field('person.name')
    assert result is not None

    # Call of method with kwargs
    result = field('person.name', gender=None)
    assert result is not None

    # Call of method with keyword argument key
    result = field(
        'person.name',
        gender=None,
        key=lambda x: x.split(' ')[0],
    )
    assert result is not None

# Generated at 2022-06-14 01:11:04.320882
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field()
    assert f('barcode')
    assert f('barcode', key=lambda x: int(x)) == int(f('barcode'))
    assert f('datetime.datetime')



# Generated at 2022-06-14 01:11:09.598740
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()

    assert field
    assert field.locale == 'en'
    assert not field.seed

    field = AbstractField(locale='ru', seed=10)
    assert field.locale == 'ru'
    assert field.seed == 10

# Generated at 2022-06-14 01:11:18.695239
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    assert Field(seed=123).__call__('chair') == 'Chair'
    assert Field(seed=123).__call__('chair', quantity=2, plural=True) == 'Chairs'
    assert Field(seed=123).__call__('choice', args=['a', 'b']) == 'a'
    assert Field(seed=123).__call__('choice', args=[], quantity=2) == []

    # Fix https://github.com/lk-geimfari/mimesis/issues/619
    assert Field(seed=123).__call__('choice', args=['a', 'b'], quantity=2) == ['a', 'b']

    # Fix https://github.com/lk-geimfari/mimesis/issues/518
    assert Field().__call__('lorem_ipsum')

# Generated at 2022-06-14 01:11:31.192877
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    data = AbstractField()
    assert 'blue' == data('color')
    assert 'blue' == data('color', key=lambda x: x.lower())

    # Test for explicitly specifying the data provider
    assert 'a' == data('text.ascii', key=lambda x: x[0])

    def tail_parser(name):
        return name.rsplit('.', 1)[-1]

    assert 'ascii' == data('text.ascii', key=tail_parser)

    # Providers a tuple of name and data-provider
    data.add_providers(('text', data))
    assert 'a' == data('text.ascii', key=lambda x: x[0])

    # Raise a UnacceptableField exception
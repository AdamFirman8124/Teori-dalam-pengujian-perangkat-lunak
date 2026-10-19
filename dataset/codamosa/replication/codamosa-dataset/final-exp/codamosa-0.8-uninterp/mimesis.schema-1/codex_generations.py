

# Generated at 2022-06-14 01:07:41.238815
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method __call__."""
    field = AbstractField()
    assert field() is None

    assert isinstance(field('uuid'), str)

    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    class FooProvider(Generic):
        """Test provider with existing method."""

        def foo(self) -> str:
            """Return 'foo'."""
            return 'foo'

    class BarProvider(Generic):
        """Test provider with existing method."""

        def bar(self) -> str:
            """Return 'bar'."""
            return 'bar'

    test_provider = [FooProvider, BarProvider]

    field = AbstractField(providers=test_provider)
    assert isinstance(field('foo'), str)
    assert field() is None

    field = Abstract

# Generated at 2022-06-14 01:07:47.595310
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    #  Wrong input name
    abstract_field = AbstractField()
    field_name = 'name'
    kwargs = {'str': 'str'}
    assert abstract_field(field_name, **kwargs) is not None

    # Wrong input name
    field_name = 'screma'
    kwargs = {'str': 'str'}
    assert abstract_field(field_name, **kwargs) is None

# Generated at 2022-06-14 01:07:51.690321
# Unit test for method create of class Schema
def test_Schema_create():
    """Test for method create of class Schema."""
    sch = Schema(lambda: {'a': 1, 'b': 2})
    assert sch.create(iterations=2) == [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]

# Generated at 2022-06-14 01:07:53.339044
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field.locale == 'en'

# Generated at 2022-06-14 01:08:03.349242
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = AbstractField()
    assert isinstance(f, AbstractField)

    # The first provider is `datetime`
    assert isinstance(f('datetime'), str)
    # The first provider is `datetime`
    assert isinstance(f('date'), str)
    # The first provider is `datetime`
    assert isinstance(f('seed'), str)
    # The first provider is `text`
    assert isinstance(f('lorem_ipsum'), str)
    # The first provider is `text`
    assert isinstance(f('title'), str)
    # The first provider is `text`
    assert isinstance(f('language'), str)
    # The first provider is `person`
    assert isinstance(f('full_name'), str)
    # The first provider is `person`

# Generated at 2022-06-14 01:08:15.504555
# Unit test for method create of class Schema
def test_Schema_create():
    # If a schema is a list of dicts,
    # the result must be a list of lists of dicts
    schema = [{'name': lambda: 'Test',
               'age': lambda: 42,
               }]
    result = Schema(lambda: schema).create(iterations=5)
    assert result == [[{'name': 'Test',
                        'age': 42}]] * 5

    # If a schema is a list of str,
    # the result must be a list of lists of str
    schema = ['test']
    result = Schema(lambda: schema).create(iterations=5)
    assert result == [['test']] * 5

    # If a schema is a list of float,
    # the result must be a list of lists of float
    schema = [3.14]

# Generated at 2022-06-14 01:08:25.156365
# Unit test for method create of class Schema
def test_Schema_create():
    """Unit test for method create of class Schema."""
    import mimesis.data as data
    import mimesis.builtins

    def assert_providers(providers, result):
        """Assert that the provided data matches the data from the schema."""
        field = Field(data.US, providers=providers)
        schema = Schema(data.Schemas.CONTACT)
        model = schema.create()[0]

        assert model.get('name') is not None
        assert model.get('address') is not None
        assert model.get('telephone') is not None
        assert model.get('age') is not None
        assert model.get('credit_card') is not None
        assert model.get('telephone') == field('telephone', mask='###-###-####')

# Generated at 2022-06-14 01:08:38.195746
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test unit AbstractField.__call__."""
    meth = AbstractField()
    assert isinstance(meth.__call__('full_name'), str)
    assert isinstance(meth.__call__('person'), dict)
    assert isinstance(meth.__call__('person.full_name'), str)
    assert isinstance(meth.__call__('person.name'), str)
    assert isinstance(meth.__call__('person.username'), str)
    assert isinstance(meth.__call__('person.sex'), str)
    assert isinstance(meth.__call__('person.age'), int)
    assert isinstance(meth.__call__('person.place_of_birth'), str)
    assert isinstance(meth.__call__('person.birth_date'), str)

# Generated at 2022-06-14 01:08:50.275186
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test of type and content class AbstractField."""
    f = Field()
    assert isinstance(f, AbstractField)
    assert f.locale == 'en'
    assert f.seed is None

    f = Field('ru')
    assert f.locale == 'ru'

    f = Field(locale='ru', seed=42)
    assert f.locale == 'ru'
    assert f.seed == 42

    def key_func(item):
        """Return item after multiplying by 2."""
        return item * 2

    f = Field('fr')
    assert f('masculine') == 'homme'
    assert f('masculine', key=key_func) == 'hommehomme'
    assert f('business.company_name') == 'Inc.'



# Generated at 2022-06-14 01:08:52.789626
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field('person.name') != field('person.surname')

# Generated at 2022-06-14 01:09:21.074450
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField(locale='en')
    assert isinstance(field, AbstractField)

# Generated at 2022-06-14 01:09:23.899301
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = Field()
    f = Field('ru')
    f = Field(seed=42)
    assert callable(f)



# Generated at 2022-06-14 01:09:28.980987
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """
    Test initialization of class AbstractField.

    :return:
    """
    field = Field(seed=123)
    assert isinstance(field, AbstractField)
    assert field._gen is not None

# Generated at 2022-06-14 01:09:35.562345
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field()
    assert f('ab_id') == '7b1e8f1d-9e60-4026-aa7a-8b8e0d65ab50'
    assert f('ab_id', key=lambda x: x[:10]) == '7b1e8f1d-9'

# Generated at 2022-06-14 01:09:37.462125
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert callable(field), 'Field must be callable object!'

# Generated at 2022-06-14 01:09:41.529737
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = Field(locale='en')
    assert field.locale == 'en'
    assert field.seed is not None
    assert field._gen is not None

# Generated at 2022-06-14 01:09:52.484252
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test :class:`~mimesis.schema.AbstractField`.

    Test constructor of class AbstractField:
    - Check if Locale is changed
    - Check if seed is changed
    - Check if providers are added in constructor
    - Check if providers are added by context manager
    """

    f = Field()
    assert f.locale == 'en'
    assert f.seed is None
    f = Field(locale='ru', seed=1)
    assert f.locale == 'ru'
    assert f.seed == 1
    assert len(f._gen.__providers__) == 29

    # TODO: Add test for providers


# Generated at 2022-06-14 01:10:01.642542
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    import pytest  # type: ignore
    from mimesis.exceptions import ResponseDataProviderException

    field = Field(locale='en')

    # UndefinedField
    with pytest.raises(UndefinedField):
        field()

    # UndefinedField
    with pytest.raises(UndefinedField):
        field(None, None)

    # UndefinedField
    with pytest.raises(UndefinedField):
        field(None, None, None, None)

    # UnsupportedField
    with pytest.raises(UnsupportedField):
        field(name='unsupported_name')

    # UnacceptableField
    with pytest.raises(UnacceptableField):
        field(name='unsupported_name.unsupported_name.unsupported_name')

    # ResponseDataProviderException

# Generated at 2022-06-14 01:10:03.279497
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field('person.full_name')



# Generated at 2022-06-14 01:10:06.938428
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = Field()
    assert isinstance(field, Field)

# Generated at 2022-06-14 01:10:24.399011
# Unit test for constructor of class AbstractField
def test_AbstractField():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.providers.cryptographic import Cryptographic

    field = Field(providers=[RussiaSpecProvider, Cryptographic])
    assert field._table == {}
    assert field.locale == 'en'
    assert field.seed is None


# Generated at 2022-06-14 01:10:26.172392
# Unit test for constructor of class AbstractField
def test_AbstractField():
    provider = Generic('ru')
    assert provider.uuid()
    field = AbstractField('ru', provider)
    assert field._table == {}


# Generated at 2022-06-14 01:10:31.673249
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    import unittest
    from mimesis.exceptions import UndefinedField

    class FieldTestCase(unittest.TestCase):

        def test_without_name(self):
            def test():
                field = AbstractField()
                field()
            self.assertRaises(UndefinedField, test)

    unittest.main()

# Generated at 2022-06-14 01:10:35.135363
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Check that it works correctly."""
    fld = Field()
    result = fld('sha1', key=lambda s: s[:8])
    assert callable(result)

# Generated at 2022-06-14 01:10:36.502622
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    return f is not None

# Generated at 2022-06-14 01:10:39.561711
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Unit test for constructor of class AbstractField."""
    field = AbstractField()
    assert 'en' == field.locale
    assert field.seed
    assert Generic == type(field._gen)



# Generated at 2022-06-14 01:10:46.224808
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.address import Address
    from mimesis.providers.date import Date
    from mimesis.providers.person import Person

    from_ = AbstractField(providers=[Address, Date, Person])
    assert from_('person.full_name') == from_.person.full_name()

# Generated at 2022-06-14 01:10:48.058728
# Unit test for constructor of class AbstractField
def test_AbstractField():
    abf = AbstractField()
    assert str(abf) == 'AbstractField <en>'



# Generated at 2022-06-14 01:10:50.289301
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    assert callable(AbstractField().__call__)

# Generated at 2022-06-14 01:10:55.642961
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert Field().__str__() == 'AbstractField <en>'
    assert Field('ru').__str__() == 'AbstractField <ru>'
    assert Field('en', b'123').__str__() == 'AbstractField <en>'



# Generated at 2022-06-14 01:11:23.010028
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert str(f) == 'AbstractField <en>'

    f = AbstractField(locale='ru', seed=123)
    assert str(f) == 'AbstractField <ru>'
    assert f.seed == 123

    f = AbstractField(providers=('person', 'datetime'))
    assert str(f) == 'AbstractField <en>'



# Generated at 2022-06-14 01:11:24.702339
# Unit test for constructor of class AbstractField
def test_AbstractField():
    _ = AbstractField()


# Generated at 2022-06-14 01:11:30.787906
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()

    # Calling methods of data provider
    field('enumeration.enumeration')
    field('enumeration.enumeration', size=10)
    field('enumeration.enumeration', length=10)
    field('enumeration.enumeration', length=10, as_list=True)

    # Using key function
    field('enumeration.enumeration', str.capitalize)

    # Using key function with args
    field('enumeration.enumeration', str.format, '{}', '{}')

    # Explicitly using provider
    field('system.system_uuid')
    field('system.system_uuid', version=4)
    field('system.system_uuid', as_string=True)

    # Using tail - for example for key-value method


# Generated at 2022-06-14 01:11:32.541244
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field is not None


# Generated at 2022-06-14 01:11:35.847633
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert f.locale == 'en'
    assert f.seed is None
    assert f.__str__().startswith('<class')

# Generated at 2022-06-14 01:11:40.668902
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert not AbstractField()._gen.providers
    assert len(AbstractField()._gen.providers) == 0

# Generated at 2022-06-14 01:11:49.252983
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__."""
    class Class:
        """A class for testing."""

        def tail(self) -> Any:
            """Return data."""
            return 'Test'

        @staticmethod
        def test() -> Any:
            """Return data."""
            return 'Test'

    class Validator:
        """Class for validating."""

        def __init__(self, locale: str, data: Any) -> None:
            """Initialize validator.

            :param locale: Locale
            :param data: Data to validate
            """
            self.locale = locale
            self.data = data


# Generated at 2022-06-14 01:11:52.325386
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert callable(field)



# Generated at 2022-06-14 01:12:02.476859
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method ``__call__`` of class ``AbstractField``."""
    field = AbstractField()
    result = field('uuid')
    assert isinstance(result, str)
    assert len(result) == 36

    # Test for explicit provider
    result = field('providers.uuid')
    assert isinstance(result, str)
    assert len(result) == 36

    # Check if exception will raise
    raised = False
    try:
        field('unsupported')
    except UnsupportedField:
        raised = True
    assert raised, 'Method must raise an exception'

# Generated at 2022-06-14 01:12:14.188813
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test class AbstractField."""
    from mimesis.providers.internet import Internet
    from mimesis.providers.person import Person
    from mimesis.providers.phone import Phone

    c = AbstractField()
    b = AbstractField(locale='ru')

    a = AbstractField(providers=[Internet, Person, Phone])
    assert a('domain_name') == c('domain_name')
    assert a('full_name') == c('full_name')
    assert a('phone_number') == c('phone_number')

    assert isinstance(a, AbstractField)
    assert isinstance(b, AbstractField)
    assert isinstance(c, AbstractField)
    assert a != b or a != c or b != c
    assert str(a) == 'AbstractField <en>'

# Generated at 2022-06-14 01:12:47.967139
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field
    assert field.locale == 'en'
    assert field.seed is None



# Generated at 2022-06-14 01:12:57.238440
# Unit test for constructor of class AbstractField
def test_AbstractField():

    def test_default_providers():
        field = AbstractField()
        assert field._gen._default_providers == [
            'address',
            'business',
            'cryptographic',
            'date_time',
            'financial',
            'food',
            'hardware',
            'internet',
            'lorem',
            'numbers',
            'person',
            'transport',
            'user_agent',
        ]

    def test_all_providers():
        field = AbstractField(providers='all')
        assert field._gen._default_providers == []

    def test_other_providers():
        other_providers = [
            'address',
            'business',
            'food',
            'internet',
            'numbers',
            'transport',
        ]
        field = Abstract

# Generated at 2022-06-14 01:12:59.373008
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField(locale='en')
    assert field.locale == 'en'
    assert field.seed is None
    assert field._gen



# Generated at 2022-06-14 01:13:04.313621
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test constructor of AbstractField."""
    field = AbstractField()
    field2 = AbstractField('en')
    assert field
    assert field2
    assert isinstance(field, AbstractField)
    assert isinstance(field2, AbstractField)

# Generated at 2022-06-14 01:13:06.919303
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = Field()
    assert isinstance(f, AbstractField)
    assert callable(f)



# Generated at 2022-06-14 01:13:10.677115
# Unit test for constructor of class AbstractField
def test_AbstractField():
    a = AbstractField()
    assert str(a) == 'AbstractField <en>', 'Wrong __str__'
    assert isinstance(a, AbstractField)
    assert callable(a)

# Generated at 2022-06-14 01:13:13.147058
# Unit test for constructor of class AbstractField
def test_AbstractField():
    try:
        AbstractField()
        assert True
    except Exception:
        assert False

# Generated at 2022-06-14 01:13:18.519184
# Unit test for constructor of class AbstractField
def test_AbstractField():
    ab_field = AbstractField(locale='en', seed=123)
    fields_test_name = {
        'full_name': 'Kevin'
    }
    for k, v in fields_test_name.items():
        val = ab_field(k)
        assert k in val
        assert ' ' in val

# Generated at 2022-06-14 01:13:22.107917
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()

    assert field('random_element', ['foo', 'bar']) in ['foo', 'bar']



# Generated at 2022-06-14 01:13:25.490700
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert f.locale == 'en'
    assert f.seed is None



# Generated at 2022-06-14 01:14:26.142170
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field  # noqa: Z421

# Generated at 2022-06-14 01:14:29.465658
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert isinstance(field(), UndefinedField)
    assert isinstance(field(name='Name', key=None), str)

# Generated at 2022-06-14 01:14:31.304425
# Unit test for constructor of class AbstractField
def test_AbstractField():  # noqa
    import logging
    logger = logging.getLogger(__name__)
    logger.info(Field())

# Generated at 2022-06-14 01:14:34.878299
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = Field(locale='en', seed=None, providers=None)
    assert field.locale == 'en'
    assert field.seed is None
    assert field._table == {}  # type: ignore


test_AbstractField()

# Generated at 2022-06-14 01:14:35.841943
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert Field() is not None

# Generated at 2022-06-14 01:14:40.524834
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    field = AbstractField('ru')
    field = AbstractField(seed=42)
    field = AbstractField(providers=['datetime'])
    field = AbstractField('en', seed=42, providers=['datetime'])

# Generated at 2022-06-14 01:14:43.467077
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test AbstractField constructor."""
    field = AbstractField()
    assert isinstance(field, Field)



# Generated at 2022-06-14 01:14:47.474336
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert f.locale == 'en'
    assert f.seed is None
    assert callable(f)
    assert f.__str__() == 'AbstractField <en>'

    f = AbstractField(seed=42)
    assert f.locale == 'en'
    assert f.seed == 42



# Generated at 2022-06-14 01:14:49.891972
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = Field()
    assert field is not None



# Generated at 2022-06-14 01:14:57.902640
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert isinstance(f, AbstractField)
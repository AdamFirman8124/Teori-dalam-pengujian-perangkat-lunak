

# Generated at 2022-06-14 01:07:18.071555
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test functionality of method :meth:`AbstractField.__call__`."""
    from mimesis.providers.address import Address
    from mimesis.providers.text import Text
    from mimesis.providers.internet import Internet

    # Default locale
    a = Field()

    # Create a field with custom providers
    custom_provider_field = Field(providers=[Address, Text, Internet()])

    # Get generic
    b = Field(providers=[Address, Text()])
    assert a(b.choice.Meta.name) == b.choice()

    # Get address
    address = b('address')
    assert address.city() == b.address.city()
    assert address.zip_code() == b.address.zip_code()

    # Get random text
    text = b('text')

# Generated at 2022-06-14 01:07:19.297587
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = AbstractField()
    assert f


# Generated at 2022-06-14 01:07:31.924072
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers import Bitcoin
    from mimesis.providers.base import BaseDataProvider

    def test_with_providers():
        expected = '36d8958c-d025-5be8-c87b-5d6c26ef48ba'

        class Test(BaseDataProvider):
            """Helper class."""

            class Meta:
                """Class Meta."""

                name = 'test'

            @classmethod
            def test_uuid(cls):
                """Helper method."""
                return expected

        field = Field(providers=[Test])
        result = field('test.test_uuid')
        assert expected == result

    def test_with_default_providers():
        uuid = Field()('uuid')
        assert len(uuid.split('-')) == 5


# Generated at 2022-06-14 01:07:33.584517
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('code.random_element') is not None

# Generated at 2022-06-14 01:07:36.987451
# Unit test for method create of class Schema
def test_Schema_create():
    def get_full_name():
        return {
            'first_name': Field('first_name'),
            'last_name': Field('last_name'),
        }

    s = Schema(get_full_name)
    assert len(s.create()) == 1

# Generated at 2022-06-14 01:07:43.832957
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method __call__ of class AbstractField."""
    field = Field()
    assert isinstance(field('title'), str)
    assert isinstance(field('title', upper=True), str)
    assert isinstance(field('title', key=lambda x: x.title()), str)
    assert field('title').isupper() is False
    assert field('title', upper=True).isupper() is True

# Generated at 2022-06-14 01:07:54.862044
# Unit test for method create of class Schema
def test_Schema_create():
    """Test class Schema."""
    import json

    class SchemaTest(Schema):
        """Test class."""

        def __init__(self):
            """Initialize test class."""
            super().__init__(self.schema)

        def schema(self) -> dict:
            """Return JSON object."""
            return {
                'name': 'John',
                'surname': 'Smith',
            }

    test_class = SchemaTest()
    result = test_class.create(iterations=4)

    assert isinstance(result, list)
    assert json.dumps({
        'name': 'John',
        'surname': 'Smith',
    }) in result

# Generated at 2022-06-14 01:07:56.741032
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test constructor of class AbstractField."""
    assert isinstance(Field(), Field)

# Generated at 2022-06-14 01:08:05.610641
# Unit test for constructor of class AbstractField
def test_AbstractField():
    from mimesis.builtins import Dummy

    f = Field(providers=(Dummy(),))
    assert isinstance(f._gen, Generic)

    # Check setting locale
    f = Field(locale='ru')
    assert f.locale == 'ru'

    # Check setting seed
    f = Field(seed=1)
    assert f.seed == 1

    f = Field(providers=(Dummy(),))
    assert f._gen.has_provider(Dummy().Meta.name)



# Generated at 2022-06-14 01:08:12.571558
# Unit test for constructor of class AbstractField
def test_AbstractField():
    from mimesis.providers import Food
    from mimesis.schema import AbstractField
    from mimesis.typing import JSON

    field = AbstractField(providers=[Food])

    expected = {
        'apple': 'Apple'
    }
    result = field('fruit')   # type: JSON
    assert result == expected.get(result)



# Generated at 2022-06-14 01:08:33.249865
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field()
    f('uuid', version=1)

# Generated at 2022-06-14 01:08:41.164092
# Unit test for method create of class Schema
def test_Schema_create():
    """Test method create of class Schema."""
    from mimesis.providers.internet import Internet
    from mimesis.providers.text import Text

    field = AbstractField(locale='en', seed='seed', providers=[Text, Internet])

    schema = {
        'name': field('words'),
        'surname': field('words'),
        'email': field('email'),
        'password': field('password'),
    }

    data_generator = Schema(schema)
    res = data_generator.create(10)

    assert len(res) == 10
    assert isinstance(res[0], dict)
    assert set(res[0].keys()) == set(schema.keys())

# Generated at 2022-06-14 01:08:42.102479
# Unit test for constructor of class AbstractField
def test_AbstractField():
    a = AbstractField()
    assert isinstance(a._gen, Generic)

# Generated at 2022-06-14 01:08:48.492826
# Unit test for method create of class Schema
def test_Schema_create():
    schema = Schema(lambda: [{'name': 'Python'}, {'name': 'Java'}])
    result = schema.create(2)
    assert result == [
        [{'name': 'Python'}, {'name': 'Java'}],
        [{'name': 'Python'}, {'name': 'Java'}]
    ]

# Generated at 2022-06-14 01:08:59.907491
# Unit test for method create of class Schema
def test_Schema_create():
    """Test for Schema.create."""
    from mimesis.enums import Gender
    from mimesis.schema import Field
    def user() -> JSON:
        gen = Field()
        rv = {
            'first_name': gen('first_name', gender=Gender.MALE),
            'last_name': gen('last_name', gender=Gender.MALE),
            'status': gen.person.occupation(),
            'gender': gen.person.gender(gender=Gender.MALE),
            'street_address': gen.address.street_address(),
            'postal_code': gen.address.postal_code(),
            'country': gen.address.country()
        }
        return rv

    schema = Schema(schema=user)

# Generated at 2022-06-14 01:09:01.543718
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = Field()
    assert f is not None

# Generated at 2022-06-14 01:09:07.521452
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__()."""
    field = Field()
    assert callable(field) is True
    _number = field('number')
    assert isinstance(_number, int)



# Generated at 2022-06-14 01:09:11.630632
# Unit test for method create of class Schema
def test_Schema_create():
    s = {'foo': 'Bar', 'bar': 'Foo'}

    def schema() -> dict:
        return s

    assert Schema(schema).create() == [s]

# Generated at 2022-06-14 01:09:23.954570
# Unit test for method create of class Schema

# Generated at 2022-06-14 01:09:29.740237
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.builtins import RussiaSpecProvider
    field = Field(str, providers=[RussiaSpecProvider])
    result = field('is_region')
    assert callable(result) is True
    result = field('rus.is_region')
    assert callable(result) is True
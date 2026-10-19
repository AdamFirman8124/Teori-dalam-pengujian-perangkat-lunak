

# Generated at 2022-06-14 01:07:27.942789
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField."""
    # Test.
    field = AbstractField()
    assert field('Person.full_name')

    # Test
    assert field('Person.full_name', gender='male')

# Generated at 2022-06-14 01:07:30.479896
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    def my_key(value: str) -> str:
        """Return 'my_key({})'.format(value)."""
        return 'my_key({})'.format(value)

    f = Field()
    assert f('fqdn', key=my_key) == 'my_key(mimesis.com)'

# Generated at 2022-06-14 01:07:34.436111
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField('en')
    assert field('full_name') == 'Robin Johnson'
    assert field('personal.full_name') == 'Robin Johnson'
    assert field('coins') == 'BTC'
    assert field('currency_code') == 'USD'

# Generated at 2022-06-14 01:07:43.040853
# Unit test for method create of class Schema
def test_Schema_create():
    """Test for class Schema.create()."""
    from mimesis import Person
    from mimesis.enums import Gender

    person = Person()

    data = [{
        'gender': person.gender(),
        'age': person.age(),
        'name': person.name(),
        'surname': person.surname()
    } for _ in range(3)]

    def schema() -> Any:
        """Implements schema."""
        person = Person()

        return {
            'gender': person.gender(),
            'age': person.age(),
            'name': person.name(),
            'surname': person.surname(),
        }

    s = Schema(schema)

    output = s.create(3)
    assert data == output
    assert data[0]['gender']

# Generated at 2022-06-14 01:07:46.900059
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test that it can return value by any name of provider's method.

    .. doctest::
        :options: +NORMALIZE_WHITESPACE

        >>> random_field = AbstractField()
        >>> random_field('text.word') in ['mollitia', 'quo', 'veniam', 'ad']
        True
    """

# Generated at 2022-06-14 01:07:51.329834
# Unit test for method create of class Schema
def test_Schema_create():
    s = Schema(
        lambda: {'foo': 'Foo', 'bar': 'bar'}
    )

    assert s.create(iterations=10) == [{'foo': 'Foo', 'bar': 'bar'}
                                       for _ in range(10)]

# Generated at 2022-06-14 01:08:04.001170
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field(locale='en')
    assert field('username') != field('username')


field = Field(locale='en')
assert field('username') != field('username')

field = Field(locale='en')
assert field('username') != field('username')
assert field('name.full_name') != field('name.full_name')

field = Field(locale='en')
assert field('username') != field('username')
assert field('name.full_name') != field('name.full_name')

field = Field(locale='en')
assert field('username') != field('username')
assert field('name.full_name') != field('name.full_name')

field = Field(locale='en')
assert field('username') != field('username')
assert field('name.full_name')

# Generated at 2022-06-14 01:08:05.607394
# Unit test for method create of class Schema
def test_Schema_create():
    assert len(Schema(SchemaType(
        str,
        int,
        bool,
    )).create(10)) == 10

# Generated at 2022-06-14 01:08:16.242402
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.builtins import ISO4217
    from mimesis.enums import Gender

    from mimesis.schema import Field

    def animal_schema(name: str) -> dict:
        field = Field(providers=[RussiaSpecProvider, ISO4217])

# Generated at 2022-06-14 01:08:25.173190
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    def my_schema() -> JSON:
        field = AbstractField(locale='en')
        return {
            'name': field('full_name', gender=Gender.FEMALE, token='-'),
            'age': field('age'),
            'email': field('email', key=lambda x: x.upper()),
            'phone': field('phone_number'),
            'custom': field('exists', Person.Meta.name)
        }

    schema = Schema(my_schema)
    data = schema.create(iterations=3)
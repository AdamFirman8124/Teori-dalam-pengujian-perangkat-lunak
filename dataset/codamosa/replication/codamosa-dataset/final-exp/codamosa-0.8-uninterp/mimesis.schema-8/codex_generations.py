

# Generated at 2022-06-14 01:07:27.951432
# Unit test for method create of class Schema
def test_Schema_create():
    """Unit test for method create of class Schema."""
    from mimesis.builtins import Person, RussiaSpecProvider
    from mimesis.enums import Gender
    from mimesis.providers.internet import Internet

    field = Field(locale='ru', providers=[Person, RussiaSpecProvider, Internet])

    def _provider() -> JSON:
        """Test method for provider."""
        return {
            'name': field('person.full_name', gender=Gender.FEMALE),
            'age': field('person.age'),
            'address': field('russia.address'),
            'email': field('internet.email'),
            'gender': field('universal.gender'),
        }

    schema = Schema(_provider)

    assert schema.create() == [_provider()]

# Generated at 2022-06-14 01:07:32.663782
# Unit test for method create of class Schema
def test_Schema_create():
    # Define a schema
    schema = {
        'name': '{{ personal.full_name() }}',
        'profession': '{{ business.occupation() }}',
        'address': '{{ address.address() }}',
    }

    # Create filled schema
    create = Schema(
        schema).create

    assert isinstance(create(), list)
    assert isinstance(create()[0], dict)

# Generated at 2022-06-14 01:07:36.383018
# Unit test for method create of class Schema
def test_Schema_create():
    schema = {
        'name': {
            'first_name': 'Personal.name',
            'last_name': 'Personal.surname',
        },
        'address': 'Address.region'
    }

    res = Schema(schema)
    assert len(res.create(10)) == 10

# Generated at 2022-06-14 01:07:37.589489
# Unit test for method create of class Schema
def test_Schema_create():
    pass

# Generated at 2022-06-14 01:07:39.202044
# Unit test for method create of class Schema
def test_Schema_create():
    assert len(Schema(SchemaType).create()) == 1

# Generated at 2022-06-14 01:07:48.032980
# Unit test for method create of class Schema
def test_Schema_create():
    """Unit test for method create of class Schema.

    Check that method Schema.create works correctly.
    Replace the schema method with a stub.
    Create a N-length list with the same element.
    Check length of list and value of every element.
    """

    # Stub for schema method
    def schema():
        return 1

    schema_length = 10
    schema_elem = 1

    assert len(Schema(schema).create(schema_length)) == schema_length
    assert all(Schema(schema).create(schema_length)[0] == schema_elem for i in range(schema_length))

# Generated at 2022-06-14 01:07:55.866272
# Unit test for method create of class Schema
def test_Schema_create():
    """Unit test for method create of class Schema."""
    from mimesis.constants import FIELDS
    from mimesis.enums import Gender

    def test(gen: Generic, field: AbstractField) -> List[str]:
        """Generate list with elements of data."""
        gender = gen.gender(gender=Gender.FEMALE)
        field(FIELDS['gender'], gender=Gender.FEMALE)
        return [str(gen.uuid4()), gen.code.imei(), gen.person.full_name(gender)]

    data = Schema(test)
    assert len(data.create(5)) == 5

# Generated at 2022-06-14 01:08:04.535400
# Unit test for method create of class Schema
def test_Schema_create():
    """Method create of class Schema."""
    # Define schema
    schema = {
        'string': '{{ text.word }}',
        'integer': '{{ datetime.unix_timestamp }}',
        'float': '{{ math.constant(name=pi) }}',
        'date': '{{ datetime.date }}',
    }

    Generator = Schema(schema)
    assert isinstance(Generator, Schema)
    result = Generator.create(10)
    assert isinstance(result, list)

# Generated at 2022-06-14 01:08:06.603849
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert isinstance(field, AbstractField)

# Generated at 2022-06-14 01:08:15.797282
# Unit test for method create of class Schema
def test_Schema_create():
    """Test create method of class Schema."""
    def dummy_schema() -> dict:
        """Dummy schema."""
        return {
            'id': 123456,
            'product': 'MagicMock',
        }

    schema = Schema(dummy_schema)
    iterations = 10

    result = schema.create(iterations)
    assert len(result) == iterations

    for item in result:
        assert isinstance(item, dict)
        assert item['id'] == 123456
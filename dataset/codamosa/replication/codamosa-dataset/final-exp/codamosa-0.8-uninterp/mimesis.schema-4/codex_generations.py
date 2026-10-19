

# Generated at 2022-06-14 01:07:27.132089
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.enums import Gender
    from mimesis.schema import Field

    f = Field()
    species_list = f.science.species(
        gender=Gender.FEMALE,
        with_subspecies=True
    )

# Generated at 2022-06-14 01:07:29.792658
# Unit test for method create of class Schema
def test_Schema_create():
    def get_data() -> JSON:
        """Get data."""
        return {
            'name': 'John',
            'age': 18,
        }
    schema = Schema(get_data)
    iterations = 3
    data = schema.create(iterations)
    assert len(data) == iterations

# Generated at 2022-06-14 01:07:36.383720
# Unit test for method create of class Schema
def test_Schema_create():
    """Unit test for create method of Schema class."""
    from mimesis.data import FINANCIAL

    field = Field(locale='en', seed=123)
    data = field.person.full_name

    schema = Schema(lambda: {
        'name': data,
        'currency': field(FINANCIAL.CURRENCY, code=True),
    })

    result = schema.create(iterations=12)
    assert len(result) == 12
    for item in result:
        assert 'name' in item
        assert 'currency' in item

# Generated at 2022-06-14 01:07:39.020235
# Unit test for method create of class Schema
def test_Schema_create():
    def schema():
        """Test schema."""
        return {'a': 1}

    schema = Schema(schema)
    assert schema.create() == [{'a': 1}]

# Generated at 2022-06-14 01:07:44.538046
# Unit test for method create of class Schema
def test_Schema_create():
    data = [{"hi": "hello"}, {"hi": "hello"}, {"hi": "hello"}]
    schema = lambda: {"hi": "hello"}
    assert Schema(schema).create(3) == data

# Generated at 2022-06-14 01:07:55.975523
# Unit test for method create of class Schema
def test_Schema_create():
    # test1: create with non-callable schema
    # Expected: UndefinedSchema
    try:
        Schema('notSchema').create(1)
        raise AssertionError('Should be UndefinedSchema')
    except UndefinedSchema:
        pass

    # test2: create with callable schema
    # Expected: list of filled schemas

    def not_create_schema(field: Field) -> JSON:
        return {
            'a': field('choice', key=lambda x: x.lower(),
                       items=['A', 'B', 'C']),
            'b': field('random_int', minimum=2, maximum=8),
        }

    created_schemas = Schema(not_create_schema).create(5)


# Generated at 2022-06-14 01:08:01.345428
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():  # pragma: no cover
    field = AbstractField()
    field('full_name')
    for key in ['personal', 'titular']:
        field(key)
    field('timezone')


if __name__ == '__main__':  # pragma: no cover
    test_AbstractField___call__()

# Generated at 2022-06-14 01:08:14.591287
# Unit test for method create of class Schema
def test_Schema_create():
    """Test for method create of class Schema."""
    from mimesis.schema import Schema
    from mimesis.enums import Gender as g
    from mimesis.builtins import RussiaSpecProvider

    provider = RussiaSpecProvider

    def schema():
        """Generate random data."""
        return {
            'name': provider.full_name(),
            'gender': provider.gender(),
            'age': provider.age(minimum=18, maximum=99),
            'title': provider.title(gender=g.FEMALE),
            'salary': provider.price(),
        }

    s = Schema(schema)

    assert len(s.create(iterations=1)) == 1
    assert len(s.create(iterations=2)) == 2

# Generated at 2022-06-14 01:08:20.744516
# Unit test for method create of class Schema
def test_Schema_create():
    s = Schema(lambda: {"name": "dummy"})
    assert isinstance(s, Schema)
    assert s.create() == [{'name': 'dummy'}]

    # Unit test for method __init__ of class Schema
    with pytest.raises(UndefinedSchema):
        Schema("{}")


# Generated at 2022-06-14 01:08:24.438460
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField's method __call__."""
    f = Field()
    result = f('full_name')
    assert result is not None
    assert ' ' in result

# Generated at 2022-06-14 01:08:45.661505
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for AbstractField.__call__."""
    field = Field()

    assert field('word')
    assert callable(field('word'))
    assert field('word', length=3)

    field = Field(providers=[])
    with pytest.raises(UnsupportedField):
        field('word')

# Generated at 2022-06-14 01:08:46.770051
# Unit test for constructor of class AbstractField
def test_AbstractField():
    af = AbstractField()
    assert af is not None

# Generated at 2022-06-14 01:08:51.909574
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.builtins.schema import (
        Schema,
    )
    s = Schema()
    assert s.create() == []
    assert len(s.create(10)) == 10

# Generated at 2022-06-14 01:09:00.962707
# Unit test for method create of class Schema
def test_Schema_create():
    """Test for a method create of class Schema."""
    from mimesis.enums import Gender
    from mimesis.schema import Field

    def schema():
        """Lambda schema."""
        x = Field('datetime.datetime')
        y = Field('datetime.date')
        z = Field('person.full_name', gender=Gender.MALE)
        return {'x': x, 'y': y, 'z': z}

    schema_ = Schema(schema)
    result = schema_.create(3)
    assert len(result) == 3
    # Check all keys are in the result of create method
    keys = list(result[0].keys())
    assert 'x' in keys
    assert 'y' in keys
    assert 'z' in keys

# Generated at 2022-06-14 01:09:08.717382
# Unit test for method create of class Schema
def test_Schema_create():
    """Test method create in class Schema."""
    from pprint import pprint
    from mimesis.schema import Field
    from mimesis.enums import Gender

    schema = Field(locale='en')
    empty_schema = Schema(schema.create_schema())

    @empty_schema.schema
    def person_schema() -> dict:
        """Generate a schema for a person."""

# Generated at 2022-06-14 01:09:13.157741
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert AbstractField(locale='ru', seed=11)._gen.seed == 11
    assert AbstractField(locale='ru', seed=11)._gen.seed != 10
    assert AbstractField(locale='ru', seed=10)._gen.seed == 10

# Generated at 2022-06-14 01:09:19.715990
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.providers.person import Person

    field = AbstractField(providers=[
        RussiaSpecProvider,
        Person
    ])

    assert field('telephone_number')
    assert field('rus.telephone_number')

    assert field('full_name.first_name')

# Generated at 2022-06-14 01:09:25.050375
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test AbstractField class.

    Test cases:
        1. Correct initialization and test on *attribute*
        2. Test on *attribute* with an incorrect value
    """
    f = AbstractField()
    if f._gen is None:
        raise ValueError('Attribute _gen must not be None.')

    if f._table is None:
        raise ValueError('Attribute _table must not be None.')



# Generated at 2022-06-14 01:09:31.773435
# Unit test for method create of class Schema
def test_Schema_create():
    """Test for method create of class Schema."""
    from mimesis.providers.person import Person
    from mimesis.schema import Field

    person = Person('ru')
    schema = Schema({'name': Field(locale='ru')})
    assert schema.create() == [{'name': person.full_name()}]

# Generated at 2022-06-14 01:09:40.643338
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.enums import Coin
    from mimesis.providers.currency import Currency

    currency = Field(locale='en',
                     providers=[Currency])
    assert currency.providers[0].__class__.__name__ == 'Currency'

    provider = currency._gen.currency

    assert str(currency) == 'Field <en>'
    assert currency('get_currency_name') == provider.get_currency_name()
    assert currency('code') == provider.code()

    assert currency('choice', Coin.HEAD) == Coin.HEAD
    assert currency('coin') in Coin.ALL

    assert currency('get_currency_name',
                    key=lambda x: str(x).upper()) == \
        provider.get_currency_name().upper()
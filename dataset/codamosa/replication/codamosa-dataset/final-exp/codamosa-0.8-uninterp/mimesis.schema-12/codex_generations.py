

# Generated at 2022-06-14 01:07:50.270717
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    f = Field()
    first_name = f('person.first_name')
    assert first_name



# Generated at 2022-06-14 01:07:52.164008
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert isinstance(AbstractField(), AbstractField)



# Generated at 2022-06-14 01:08:05.725861
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # pylint: disable=import-outside-toplevel
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.providers.payment import Payment
    field = AbstractField(providers=[Address, Payment])
    assert field('gender', kwargs={'gender': Gender.MALE.value}) == Gender.MALE.value
    assert field('postcode') # noqa: S101
    assert field('credit_card_number') # noqa: S101
    assert field.address.postcode() # noqa: S101
    assert field('address.postcode') # noqa: S101
    assert field('address.postcode') # noqa: S101
    assert isinstance(field('address.postcode'), str)

# Generated at 2022-06-14 01:08:12.164611
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Unit test for class AbstractField."""
    assert Field(locale='ru', seed=1)
    assert Field(locale='ru', seed=1)._gen is not None
    assert Field(locale='ru', seed=1).locale == 'ru'
    assert Field(locale='ru', seed=1).seed == 1

# Generated at 2022-06-14 01:08:24.092463
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():

    # Unit test for method __call__ with supported providers

    # Create instance of AbstractField Class
    field = AbstractField()

    # Schema for test
    schema = {
        'first_name': 'personal.full_name',
        'last_name': 'personal.full_name',
        'age': 'datetime.random_age',
        'gender': 'personal.gender',
        'datetime': 'datetime.datetime',
    }

    # Get result from AbstractField
    person = {
        key: val(field)  # pylint: disable=E1102
        for key, val in schema.items()
    }

    # Check if all keys in dictionary
    assert set(person.keys()) == set(schema.keys())

    # Unit test for method __call__ with unsupported providers

    # Create instance of Abstract

# Generated at 2022-06-14 01:08:25.402302
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field is not None

# Generated at 2022-06-14 01:08:31.359408
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField(seed='100')
    assert field('uuid4') == '1a5b8ff9-b948-400f-990b-5444ec45d55f'
    assert field('first_name') == 'Павел'
    assert field('phone') == '+7(985)486-16-62'

# Generated at 2022-06-14 01:08:38.125349
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method AbstractField.__call__."""
    field = AbstractField()
    assert len(field('address.city')) > 0

    provider_pk = field('provider.pk')

    field('provider.add_providers', provider_pk)
    pk = field('provider.pk')
    assert pk is not None



# Generated at 2022-06-14 01:08:39.070401
# Unit test for constructor of class AbstractField
def test_AbstractField():
    f = Field()
    assert f is not None

# Generated at 2022-06-14 01:08:42.084958
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test AbstractField constructor."""
    field = AbstractField()
    assert field is not None
    assert isinstance(field, AbstractField)


# Generated at 2022-06-14 01:09:04.483621
# Unit test for constructor of class AbstractField
def test_AbstractField():
    s = AbstractField()

    assert str(s) == 'AbstractField <en>'
    assert isinstance(s('uuid'), str)

# Generated at 2022-06-14 01:09:06.418336
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field('uk')

    assert field('word')



# Generated at 2022-06-14 01:09:13.246577
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__()."""
    field = Field()
    assert field('full_name') == 'Alijah Estrada'
    assert field('uuid') == 'ba0706c2-e5a1-5bc2-8a5b-297675be55d6'
    assert field('email', provider='person') == 'Elmer.Crona@hotmail.com'

# Generated at 2022-06-14 01:09:18.366425
# Unit test for constructor of class AbstractField
def test_AbstractField():
    regex = '[a-z]{16}'
    f = Field(providers=[Generic])
    assert f('token', regex=regex)
    assert f('token', regex=regex)



# Generated at 2022-06-14 01:09:28.741616
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.generic import Generic
    from mimesis.exceptions import UnsupportedField
    from mimesis.enums import Gender

    f = Field()
    try:
        f()
    except UndefinedField:
        pass
    else:
        raise AssertionError('UndefinedField not raised.')

    f = Field()
    f.add_providers(Generic)
    f(name='email', prefix=None)

    f = Field(providers=Generic)
    f(name='email', prefix=None)



# Generated at 2022-06-14 01:09:38.566749
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    g = Generic('en', seed=None)
    field = AbstractField(locale='en', seed=None, providers=g)

    name = 'name'
    method = 'full_name'
    key = 'capitalize'
    kwargs = {}
    fn = lambda x: getattr(x, key)()

    assert hasattr(getattr(g, name), method)

    value = field(name + '.' + method)(**kwargs)
    expected = fn(getattr(getattr(g, name), method)(**kwargs))
    assert value == expected

    value = field(method, key=fn)(**kwargs)
    expected = fn(getattr(getattr(g, name), method)(**kwargs))
    assert value == expected

# Generated at 2022-06-14 01:09:43.279933
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field('faker.name.first_name') is not None

    assert field('faker.name', gender=None) == field('faker.name.name')



# Generated at 2022-06-14 01:09:52.639062
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test cases for constructor of class AbstractField."""
    field = AbstractField()

    assert field.locale == 'en'
    assert field.seed == None
    assert field._gen is not None

    field = AbstractField()

    assert field.locale == 'en'
    assert field.seed == None
    assert field._gen is not None

    field = AbstractField('ru')

    assert field.locale == 'ru'
    assert field.seed == None
    assert field._gen is not None

    field = AbstractField(seed=123)

    assert field.locale == 'en'
    assert field.seed == 123
    assert field._gen is not None

    field = AbstractField('ru', seed=123)

    assert field.locale == 'ru'
    assert field.seed == 123
    assert field._gen is not None

# Generated at 2022-06-14 01:09:57.670780
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    import random
    field = Field(locale='en', seed=random.random())

    for _ in range(1000):
        person = field('person')
        person_name = field('person.name')
        address = field('address.street')
        assert isinstance(person, dict)
        assert isinstance(person_name, str)
        assert isinstance(address, str)



# Generated at 2022-06-14 01:10:04.356590
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.builtins import Address

    Generic.add_provider(Address)
    field = AbstractField(providers=[Address, Address])
    assert field('city').capitalize() in ['Amsterdam', 'Berlin', 'London']
    assert field('address.city').capitalize() in ['Amsterdam', 'Berlin', 'London']
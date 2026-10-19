

# Generated at 2022-06-14 01:07:27.132131
# Unit test for method create of class Schema
def test_Schema_create():
    """Test method create of Schema class.

    :return: None
    """
    from mimesis.providers.person import Person
    from mimesis.enums import Gender
    from mimesis.builtins import spec

    def sch_person() -> dict:
        person = Person('en', seed=0)
        return {
            'name': person.full_name(gender=Gender.MALE),
            'age': person.age(),
            'birthday': person.birthday().strftime(spec('%Y-%m-%d')),
            'cpf': person.cpf(),
        }

    schema = Schema(sch_person)
    data = schema.create(iterations=3)


# Generated at 2022-06-14 01:07:34.317478
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from . import fields

    field = AbstractField(providers=fields.providers)

    assert isinstance(field('name'), str)
    assert isinstance(field('name', gender='male'), str)
    assert isinstance(field('name', key=str.upper), str)
    assert isinstance(field('name', gender='male', key=str.upper), str)

    assert isinstance(field('person.name', gender='male'), str)
    assert 'name' in dir(field._gen.person)

    assert isinstance(field('person.name', gender='male', key=str.upper), str)
    assert isinstance(field('none.name'), str)
    assert isinstance(field('none.name', key=str.upper), str)

    assert isinstance(field('none.name', key=str.upper), str)

# Generated at 2022-06-14 01:07:38.605922
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    ab = AbstractField()
    assert ab.__call__('seed') == ab.seed
    assert ab.__call__('choice', items=['red', 'green', 'blue']) in ['red', 'green', 'blue']
    assert ab.__call__('choice', items=['red', 'green', 'blue'], key=lambda x: x.title()) in ['Red', 'Green', 'Blue']

# Generated at 2022-06-14 01:07:44.581018
# Unit test for method create of class Schema
def test_Schema_create():
    def sch(field: Field) -> JSON:
        """Create test schema."""
        return {
            'name': field('full_name'),
            'email': field('email'),
            'password': field('password')
        }

    s = Schema(sch)
    assert len(s.create(iterations=10)) == 10

# Generated at 2022-06-14 01:07:55.730370
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test the method __call__."""
    field = Field()

    assert callable(field.__call__)

    assert field.__call__('frozen_string', length=8)
    assert field.__call__('random_int', maximum=99)
    assert field.__call__('random_jose', length=32)
    with pytest.raises(UndefinedField):
        field.__call__()
    with pytest.raises(UndefinedField):
        field.__call__('')
    with pytest.raises(UnsupportedField):
        field.__call__('unsupported_field')
    with pytest.raises(UnacceptableField):
        field.__call__('wrong.field.name')



# Generated at 2022-06-14 01:08:06.671516
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():  # type: ignore
    """Test method __call__ of class AbstractField."""
    field = AbstractField()

    assert field('full_name')
    assert field('capitalized_name')
    assert field('choices')
    assert field('file_extension')
    assert field('file_name')
    assert field('full_path')
    assert field('nautical_ship_name')
    assert field('ship_name')
    assert field('file_extension', file_type='audio')
    assert field('file_extension', file_type='video')
    assert field('file_size', size_unit='KB')
    assert field('file_size', size_unit='MB')

# Generated at 2022-06-14 01:08:14.835948
# Unit test for method create of class Schema
def test_Schema_create():
    def schema1():
        return {
            'foo': {
                'strange': Field('number.between', 1, 100),
                'bar': Field('number.between', 1, 100),
            },
            'baz': Field('number.between', 1, 100),
            'qux': Field('number.between', 1, 100),
        }

    data1 = Schema(schema1).create(iterations=3)
    print(data1)

# Generated at 2022-06-14 01:08:25.042613
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for call method.

    Test for ``__call__`` method.
    """
    field = AbstractField()
    result = field('uuid', version=1)
    assert result
    assert isinstance(result, str)
    assert len(result) == 32
    assert result.count('-') == 4

    result = field('uuid', version=4)
    assert result
    assert isinstance(result, str)
    assert len(result) == 36
    assert result.count('-') == 4

    result = field('hexadecimal', size=10, capital_letters=True)
    assert result
    assert isinstance(result, str)
    assert len(result) == 10

    result = field('title')
    assert result
    assert isinstance(result, str)



# Generated at 2022-06-14 01:08:29.332688
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.datetime import Datetime

    f = AbstractField('en')
    f._gen = Datetime()
    assert callable(f)
    assert f('now')

# Generated at 2022-06-14 01:08:34.087613
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField('en')
    result = field('choice', [1, 2, 3, 4, 5])
    assert result in [1, 2, 3, 4, 5]

# Generated at 2022-06-14 01:08:58.906334
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field('personal.full_name')
    assert field('personal.full_name', localization='ru')
    assert field('datetime.datetime', formatter='%Y-%m-%d')
    assert field('datetime.datetime', datetime_format='%Y-%m-%d')
    assert field('datetime.datetime', formatter='%Y-%m-%d', datetime_format='%Y-%m-%d')
    assert field('datetime.datetime', datetime_format='%Y-%m-%d', datetime_format='%Y-%m-%d')

# Generated at 2022-06-14 01:09:03.618028
# Unit test for method create of class Schema
def test_Schema_create():
    schema = Schema(lambda: dict(
        foo=1, bar=2, baz=4, text=lambda: 'foo bar'
    ))

    assert len(schema.create()) == 1
    assert len(schema.create(5)) == 5

# Generated at 2022-06-14 01:09:15.580371
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert callable(field)
    assert field.locale == 'en'
    assert issubclass(field.__class__, AbstractField)
    assert field('full_name').split()[0] in ['Amber', 'Joshua', 'Emma', 'William']
    assert field('full_name', 'en').split()[0] in ['Amber', 'Joshua', 'Emma', 'William']
    assert field('full_name', 'ru').split()[0] in ['Абрам', 'Авдей', 'Агриппина', 'Александр']
    assert 'a' in field('email')

# Generated at 2022-06-14 01:09:23.527932
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test ``__call__`` method of ``AbstractField`` class."""
    # Arrange
    field = AbstractField()
    prov_name = 'identifiers'
    method_name = 'hash'

    # Act
    res = field(prov_name + '.' + method_name)

    # Assert
    assert isinstance(res, str)
    assert len(res) == 64



# Generated at 2022-06-14 01:09:31.326631
# Unit test for method create of class Schema
def test_Schema_create():
    from mimesis.providers.datetime import Datetime

    class FakeSchema:
        def __init__(self):
            self.dt = Datetime()
            self.field = AbstractField(locale='ru',
                                       providers=[self.dt])

        def __call__(self):
            return self.field('date', format='%d.%m.%Y')

    schema = Schema(FakeSchema)
    result = schema.create(2)
    assert len(result) == 2
    assert isinstance(result[0], str)

# Generated at 2022-06-14 01:09:40.891440
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    field = AbstractField()

    # Test for regular call
    result = field('number')
    assert isinstance(result, int)

    result = field('seed')
    assert isinstance(result, str)

    # Test for qualified call
    result = field('datetime.date')
    assert isinstance(result, str)

    result = field('datetime.timestamp')
    assert isinstance(result, int)

    # Test for negative cases
    try:
        field()
        assert False  # pragma: no cover
    except UndefinedField:
        assert True

    try:
        field('wrong_method')
        assert False  # pragma: no cover
    except UnsupportedField:
        assert True


# Generated at 2022-06-14 01:09:48.330490
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # SetUp
    field = Field()

    # Assertions
    assert 'Arthur' == field(key=lambda x: x.split(' ')[0],
                             full_name=True)
    assert 'Arthur' == field(key=lambda x: x.split(' ')[0],
                             full_name=True,
                             gender='male')

# Generated at 2022-06-14 01:09:54.836083
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of class AbstractField."""
    field = Field()

    for _ in range(5):
        assert field('person.full_name') == field.person.full_name()

    assert field('cryptographic.hash_id') == field.cryptographic.hash_id(64)
    assert field('code.hash_id') == field.code.hash_id(64)

# Generated at 2022-06-14 01:09:59.017312
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of class AbstractField."""
    field = AbstractField()

    field('hello')
    assert field('world')

    try:
        field()
    except UndefinedField:
        assert True
    else:
        assert False

    field = AbstractField(providers=[])
    assert field('hello')
    assert field('world')

# Generated at 2022-06-14 01:10:11.317961
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = AbstractField()
    result = f('datetime')
    assert len(result) == 19

    result = f('datetime', pattern='yyyy-MM-dd HH:mm:ss')
    assert len(result) == 19

    result = f('uuid')
    assert len(result) == 36

    # Result should be integer type
    result = f('uuid', key=lambda x: int(x, 16))
    assert isinstance(result, int)

    # Result should be float type
    result = f('currency', key=lambda x: float(x[1:]))
    assert isinstance(result, float)

    # Result should be float type
    result = f('currency', key=lambda x: float(x[1:]), code='usd')
    assert isinstance(result, float)
    assert x.start

# Generated at 2022-06-14 01:10:50.634555
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    import types

    field = Field()

    assert isinstance(field, AbstractField)
    assert isinstance(field.seed, (int, type(None)))
    assert isinstance(field.locale, str)
    assert field.locale == 'en'
    assert field.seed is None
    assert field('text') is not None
    assert field('bitcoin') is not None
    assert field('datetime') is not None
    assert field('hardware') is not None
    assert field('internet') is not None
    assert field('user_agent') is not None
    assert field('code') is not None
    assert field('software') is not None
    assert field('cryptographic') is not None
    assert field('telegram') is not None

# Generated at 2022-06-14 01:10:55.466769
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for class AbstractField call method."""
    field = Field()



# Generated at 2022-06-14 01:11:06.179913
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    class CustomSchema(Schema):
        def __call__(self):
            from mimesis.providers.datetime import Datetime

            dt = Datetime(seed=1234)

            return {
                'id': dt.uuid4(),
                'name': dt.uuid4(),
                'created_at': dt.datetime(start=2018, end=2019).isoformat(),
            }

    f = CustomSchema(schema=Schema(schema=CustomSchema))
    f.create()

# Generated at 2022-06-14 01:11:09.579754
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__ method."""
    test_field = AbstractField()
    assert test_field.__call__('name') == 'Martha'

# Generated at 2022-06-14 01:11:12.272815
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    assert str(Field()) == 'AbstractField <en>', ('AbstractField must return '
                                                  'English locale by default')



# Generated at 2022-06-14 01:11:21.964419
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for AbstractField.__call__."""
    from mimesis.enums import Gender

    def key_func(raw_text: str) -> str:
        """A key function."""
        return raw_text.lower()

    a = Field()
    b = a('text', key=lambda x: x)
    c = a('personal.full_name')
    d = a('personal.gender', value_type=Gender.FEMALE)
    e = a('personal.full_name', gender=Gender.MALE)
    f = a('personal.full_name', gender=Gender.FEMALE, key=key_func)
    g = a('personal.gender', value_type=Gender.FEMALE, key=key_func)

# Generated at 2022-06-14 01:11:30.075258
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__."""
    s = r'[a-zA-Z]'
    f = Field()
    assert f('regex.pattern', s) == s
    assert f('choice', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    assert f('just_str', 'str') == 'str'

# Generated at 2022-06-14 01:11:39.102325
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('name') == 'Noah'
    assert field('name', middle='Fiona') == 'Fiona'
    assert field('full_name') == 'Noah Michael'
    assert field('full_name', middle='Fiona') == 'Noah Fiona'
    assert field('full_name', middle='Fiona', last='Fox') == 'Noah Fiona Fox'
    assert field('full_name', middle='Fiona', last='Fox',
                 key=lambda x: x.lower()) == 'noah fiona fox'
    assert field('ipv4') == '192.168.0.22'
    assert field('ipv4', use_dhcp=False) == '192.168.0.23'
    assert field('address.slug') == 'south-tracey-land'

# Generated at 2022-06-14 01:11:48.471908
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():  # noqa: W0621,W0612
    """Unit test for method __call__ of class AbstractField."""
    af = AbstractField(seed=1)

    assert af('uuid4') == '52786f5e-df00-40e5-b2a7-fc4bc4d4c089'
    assert af('crc32') == '0xF3F3B825'
    assert af('name') == 'Rene'
    assert af('last_name') == 'Brust'
    assert af('phone_number') == '+1 (685) 491-9459'
    assert af('ipv4') == '251.184.77.168'

# Generated at 2022-06-14 01:12:02.513546
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method __call__."""
    # TODO: Rewrite this test!
    # data = [
    #     ('en.datetime.date', 'datetime.datetime.date'),
    #     ('datetime.date', 'datetime.datetime.date'),
    #     ('en.provider.date', 'datetime.datetime.date'),
    #     ('provider.date', 'provider.Datetime.date'),
    #     ('en.provider.date', 'provider.Datetime.date'),
    # ]

    # for name, result in data:
    #     field = AbstractField()
    #     iterator = iter(field(name))
    #     assert str(next(iterator)) == result

# Generated at 2022-06-14 01:13:21.675698
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    fields = Field(locale='en')
    assert callable(fields('datetime', year=1000, month=1, day=1))
    assert callable(fields('person.full_name'))
    assert callable(fields('person.full_name', key=str))

# Generated at 2022-06-14 01:13:30.476492
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('age') > 0
    assert field('credit_card_number') is not None
    assert field('date_time') is not None
    assert field('title') is not None
    assert field('full_name') is not None
    assert field('ip') is not None
    assert field('fake', key=lambda x: isinstance(x, str)) is True
    assert field('false', key=lambda x: isinstance(x, bool)) is False
    assert field('ssn') is not None
    assert field('none') is None



# Generated at 2022-06-14 01:13:32.287233
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field.locale == 'en'
    assert callable(field)

# Generated at 2022-06-14 01:13:34.366772
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    pass

# Generated at 2022-06-14 01:13:37.654818
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    assert Field().__call__('name') is None
    assert Field().__call__('user_agent') is None
    assert Field().__call__('person.full_name') is None

# Generated at 2022-06-14 01:13:49.496195
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__."""
    def _test(field):
        assert field('full_name')
        assert field('full_name', key=lambda x: x.split(' ')[0])
        assert field('full_name', middle=True, key=lambda x: x.split(' ')[1])
        assert field('uri', domain='example.com')

    f1 = AbstractField()
    _test(f1)
    f2 = AbstractField(locale='ru')
    _test(f2)
    f3 = AbstractField(seed=42)
    _test(f3)



# Generated at 2022-06-14 01:13:56.254105
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method __call__ of class AbstractField."""
    locale = 'en'
    seed = '27c982c9-9f0a-4fc5-aa0f-e8f852c48d18'
    field = Field(locale, seed)

    assert field('name') == 'Fuck'

    field('full_name', first_name='Fuck', last_name='Ullman') == \
        'Fuck Ullman'

    field('full_name', key=lambda x: x.lower()) == 'fuck ullman'

    assert field('full_name', key=lambda x: x.upper()) == 'FUCK ULLMAN'

    assert field('full_name', 'first_name') == 'Fuck'

    assert field('name', 'first_name') == 'Fuck'


# Generated at 2022-06-14 01:13:58.925815
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.schema import Field

    gen = Field()

    assert gen('address.country') == 'United States'

# Generated at 2022-06-14 01:14:07.252629
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test ``__call__`` method of class :class:`~mimesis.schema.AbstractField`."""
    fld = AbstractField()
    _key = fld.choice
    _kwargs = {'items': ['one', 'two', 'three']}

    result = fld('choice', **_kwargs)
    assert result == _key(**_kwargs)

    # First method in the first provider
    result = fld('token', **_kwargs)
    assert result == '6Bzp6L-T6ZSZ'

    result = fld('token', key=str.upper, **_kwargs)
    assert result == '6BZP6L-T6ZSZ'

    # Explicitly defined method in a provider

# Generated at 2022-06-14 01:14:11.374097
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()

    def is_even(num: int) -> bool:
        return num % 2 == 0

    assert isinstance(field('biome'), str)
    assert isinstance(field('room'), str)
    assert isinstance(field('metadata'), dict)
    assert isinstance(field('is_even', key=is_even), bool)



# Generated at 2022-06-14 01:14:40.560193
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Tests for AbstractField."""
    field = Field()
    field.__call__(name='fmt.format')
    field.__call__(name='person.full_name')

# Generated at 2022-06-14 01:14:53.652098
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Asserts for tail parser
    assert AbstractField().tail_parser('provider.attribute', object) == object.provider.attribute
    assert AbstractField().tail_parser('provider.attribute.another', object) == object.provider.attribute
    # Asserts for key parameter
    assert AbstractField().__call__('uuid4', key=lambda x: x.split('-')) == ['b7bd4ec4', '4b61', 'b4aa', '965b', 'acb8c5a6439d']
    assert AbstractField().__call__('uuid4', key=lambda x: x.split('-')) == ['a3e6d457', 'f3a1', '4ea1', 'bff7', 'e9e6ab8f6124']
    # Asserts for unsupported field
   

# Generated at 2022-06-14 01:14:58.528465
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__() method."""
    dp = AbstractField()
    field = dp('integer', minimum=10)

    assert field is not None
    assert isinstance(field, int)
    assert field >= 10

# Generated at 2022-06-14 01:15:08.110349
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.person import Person

    provider = Generic(locale='en')
    provider.add_provider(Person)

    field = AbstractField(provider=provider)
    assert isinstance(field('full_name'), str) is True
    assert isinstance(field('person.full_name'), str) is True

    assert field('full_name', 'upper') == field('full_name').upper()
    assert field('person.full_name', 'upper') == field(
        'person.full_name').upper()

    try:
        field('full_name.lower')
    except UnacceptableField:
        assert True

    try:
        field('full_name_1')
    except UndefinedField:
        assert True


# Generated at 2022-06-14 01:15:18.921085
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method AbstractField.__call__."""
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    class PersonWithAddress(Person):  # type: ignore
        """Person with address provider."""

        class Meta:
            """Meta."""

            name = 'person.with.address'

        @property
        def address(self) -> Address:
            """Address."""
            return Address(locale=self.locale, seed=self.seed)

    field = Field(locale='ru', providers=[PersonWithAddress])
    # Get method and compare with result value
    method = field('person.with.address.full_name')
    assert method == 'Иван игнатьевич Божко'


# Generated at 2022-06-14 01:15:24.439208
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for method __call__."""
    field = Field()

    name = 'full_name'
    key = lambda x: x.split(' ')

    result = field(name, key=key)
    assert len(result) > 0

# Generated at 2022-06-14 01:15:36.993392
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()

    s = field('seed')
    assert len(s) == 32
    assert s == '3e085b5f5df1b5d5cbf1830b8c1e22cd'

    s = field('seed', key=lambda x: x.upper())
    assert len(s) == 32
    assert s == '3E085B5F5DF1B5D5CBF1830B8C1E22CD'

    s = field('email', domains=['gmail.com'])
    assert s == 'j.bell@gmail.com'

    s = field('seed', key=lambda x: x.upper(), seed=123456)
    assert len(s) == 32

# Generated at 2022-06-14 01:15:47.202290
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from dataclasses import dataclass
    from mimesis import en

    class MyProvider:
        def __init__(self, *args, **kwargs):
            pass

        @dataclass
        class Meta:
            name = 'my'
            unit = 'test'

        #: Some field
        field: str = 'field'

        def method(self):
            return self.field

    abstract_field = AbstractField()
    abstract_field = AbstractField(providers=(MyProvider, ))

    assert abstract_field.field
    assert abstract_field.method == 'field'
    assert abstract_field('field') == 'field'

    assert abstract_field('method')
    assert abstract_field('method') == 'field'
    assert abstract_field('my.method') == 'field'


# Generated at 2022-06-14 01:15:51.243114
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__."""
    f = Field()

    assert f('full_name') is not None
    assert f('address.address') is not None
    assert f('non.existent.tail') is None

# Generated at 2022-06-14 01:15:52.171682
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    pass



# Generated at 2022-06-14 01:16:37.071387
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of class AbstractField."""
    field = Field()
    assert field('address.address') == '3928 Mockingbird Street'



# Generated at 2022-06-14 01:16:42.443767
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test method __call__ of class AbstractField."""
    field = AbstractField()
    data = field('full_name')
    assert data is not None

    data = field('user_agent')
    assert data is not None

    data = field('date')
    assert data is not None

# Generated at 2022-06-14 01:16:47.313937
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    class Test(AbstractField):
        pass
    provider = Test()
    result = provider('choice', ['a', 'b'], key=lambda x: x.upper())
    assert result in ['A', 'B']



# Generated at 2022-06-14 01:16:53.244695
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = Field(locale='en')

    def key(s: str) -> str:
        """Add an ``a`` to the end of str.

        :return: Formatted str.
        """
        return s + 'a'

    assert f('name') != f('name')
    assert f('name', key=key) == (f('name') + 'a')



# Generated at 2022-06-14 01:16:57.816960
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test an instance of class AbstractField."""
    field = AbstractField()
    assert field('codename') == 'penguin'
    assert field('codename', key=str.upper) == 'PENGUIN'
    assert field('codename', key=str.upper) == 'PENGUIN'


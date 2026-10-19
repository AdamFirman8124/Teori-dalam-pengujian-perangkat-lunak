

# Generated at 2022-06-14 01:07:48.610384
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test AbstractField.__call__."""
    from mimesis.providers.person import Person

    field = Field()

    # Test for method person.full_name
    assert field('full_name') != ''

    # Test for method person.full_name with key
    assert field('full_name', lambda x: x) != ''

    # Test for method person.full_name,
    # when name is not in providers
    try:
        field('empty')
    except UndefinedField:
        pass
    except Exception:
        raise

    # Test for method person.full_name
    # with kwargs
    assert field(
        'full_name',
        gender=Person.MALE
    ) != ''

    # Test for method person.full_name
    # with args

# Generated at 2022-06-14 01:07:58.040624
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # TODO: Need to test all data providers
    from mimesis.enums import Gender, MaritalStatus

    f = Field(locale='en')
    # TODO: Need to provide to __call__ Field method data providers
    # TODO: Instead of using `_gen`
    assert f._gen.person.full_name(gender=Gender.MALE) == f(
        'person.full_name', gender=Gender.MALE)
    assert f._gen.person.full_name(gender=Gender.MALE) == f(
        'full_name', gender=Gender.MALE,
    )
    assert f._gen.person.full_name(gender=Gender.MALE) == f(
        'person.full_name', gender=Gender.MALE,
    )


# Generated at 2022-06-14 01:08:00.557640
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = Field()

    assert field.seed is None
    assert field.locale == 'en'

# Generated at 2022-06-14 01:08:11.050629
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = AbstractField('en')
    assert isinstance(f('uuid'), str)
    assert f('uuid') != f('uuid')
    assert len(f('uuid')) == 36

    assert f('uuid.uuid4') != f('uuid.uuid4')
    assert len(f('uuid.uuid4')) == 36

    assert f('uuid.uuid4',
             key=lambda x: '-'.join((x[:8], x[8:12], x[12:16],
                                     x[16:20], x[20:]))) == f('uuid.uuid4')


# Generated at 2022-06-14 01:08:17.682544
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert callable(field)

    assert field() is None

    with field.random.seed(42):
        assert field('person.username') == 'Bert_Quigley'

        assert field(
            'datetime.timestamp',
            fmt='%Y-%m-%d %H:%M:%S',
            tzinfo='UTC',
        ) == '2018-12-29 04:01:35'

        assert field(
            'datetime.timestamp',
            fmt='%Y-%m-%d %H:%M:%S',
            tzinfo='UTC',
            key=str.upper,
        ) == '2018-12-29 04:01:35'.upper()


# Generated at 2022-06-14 01:08:23.944013
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    f = AbstractField()
    assert f('uuid')
    assert f('fullname') == f('person.fullname')
    assert f('fullname') != f('code.isbn')
    assert f('code.isbn', length=10)
    assert f('code.isbn', key=lambda x: len(x) == 13)
    assert f('code.isbn', key=lambda x: len(x) == 10)
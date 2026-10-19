

# Generated at 2022-06-14 01:07:44.230489
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # UndefinedField
    field = AbstractField()
    assert field('name') == UndefinedField()

    # UnsupportedField
    assert field('name', other='kwargs') == UnsupportedField('name')

    # Callable
    assert field('str', key=len) == len(field._gen.str())


# Generated at 2022-06-14 01:07:50.318639
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field('name')

    try:
        field()
    except UndefinedField:
        assert True
    else:
        assert False

    try:
        field('provider.name.method')
    except UnacceptableField:
        assert True
    else:
        assert False



# Generated at 2022-06-14 01:07:54.774410
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    for i in range(100):
        assert field('random_int') != field('random_int')
    for i in range(100):
        assert field('person.full_name') in field('person.full_name')

# Generated at 2022-06-14 01:08:01.345654
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('person.full_name')
    assert field('person.get_full_name', gender='male')
    assert field('person.full_name', key=lambda x: x.upper())
    assert field('person.full_name', key=str.lower)
    assert field('person', key=str)



# Generated at 2022-06-14 01:08:04.286212
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    pass

# Generated at 2022-06-14 01:08:15.526766
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    from mimesis.providers.date import Date
    from datetime import datetime

    field = AbstractField(locale='en')
    result = field('datetime', key=lambda d: d.strftime('%d.%m.%Y %H:%M:%S'))

    assert result is not None, 'Bad result'

    gen = Generic('en')
    date = Date('en', gen.seed)
    result_two = date.datetime(
        key=lambda d: d.strftime('%d.%m.%Y %H:%M:%S')
    )

    assert result_two == result, (
        f'{result} != {result_two}'
    )



# Generated at 2022-06-14 01:08:22.132980
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = Field()
    assert field('name') != ''
    assert field('name', key=str.upper) != ''
    assert field('random_digit', minimum=10, maximum=13) in (10, 11, 12, 13)

    # ValueError because unsuppoted method name
    try:
        field('foo')
    except ValueError:
        pass
    else:
        assert False



# Generated at 2022-06-14 01:08:31.440749
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField(locale='ru')

    # test_name_not_in_table
    with assert_raises(UndefinedField):
        field()

    # test_if_name_in_table
    field._table['test'] = lambda: 'test'
    assert field(name='test') == 'test'

    # test_if_name_not_in_table_with_key
    with assert_raises(UndefinedField):
        field(key=str)

    # test_if_name_in_table_with_key
    field._table['test'] = lambda: 'test'
    assert field('test', key=str) == 'test'

    # test_if_name_is_not_string
    with assert_raises(UndefinedField):
        field(name=1)

    # test

# Generated at 2022-06-14 01:08:41.164081
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField(seed=123)

    # Test when name of method is explicitly specified
    assert field('personal.full_name') == 'Kaitlyn'
    assert field('full_name', key=lambda x: x.split(' ')[0]) == 'Kaitlyn'

    # Test when there is an ambiguity in the name of the method (the same
    # names of the methods in different data providers)
    assert field('social.username') == 'rvw_kent'
    assert field('username', key=lambda x: x.split(' ')[0]) == 'rvw_kent'

    # Test without name of method
    assert field(key=lambda x: x.code) == 'J0N'

    # Test when name of method is not found

# Generated at 2022-06-14 01:08:42.387267
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Check if the method works correctly."""
    pass
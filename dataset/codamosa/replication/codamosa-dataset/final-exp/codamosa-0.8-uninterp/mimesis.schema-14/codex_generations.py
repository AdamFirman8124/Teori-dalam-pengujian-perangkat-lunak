

# Generated at 2022-06-14 01:07:37.892260
# Unit test for constructor of class AbstractField
def test_AbstractField():
    field = AbstractField()
    assert field(name='phone_number', mask='(+##) ### ##-##-##') is not None

# Generated at 2022-06-14 01:07:48.370767
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    field = Field(seed=23)

    # create(name: str, key: Callable, kwargs: dict)
    assert 'Clemson' == field('name', kwargs={'token': 'university', 'scheme': 'name'})
    assert 'name' in field(name='name', key=lambda x: x.lower())

    # create(name: str, kwargs: dict)
    assert 'Jefferson' == field('name', kwargs={'name': 'surname'})

    # create(name: str)
    assert 'Jefferson' == field('name', kwargs={'name': 'surname'})



# Generated at 2022-06-14 01:07:51.577644
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for AbstractField.__call__."""
    field = Field()
    assert field('geography.country')



# Generated at 2022-06-14 01:08:00.316960
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    _field = Field()

    # Test for name is None
    try:
        _field()
    except Exception as e:
        assert str(e) == 'Field must be defined.'

    # Test for name is not None
    method = _field('uuid4')
    assert isinstance(method(), str)
    assert len(method()) == 36
    assert method.__name__ == 'uuid4'

    # Test for two objects of the same class with the same name
    assert _field('choice') != _field('choice', [1, 2, 3])

# Generated at 2022-06-14 01:08:02.445727
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test __call__ method of AbstractField class.

    1. Should not raise an error if the name of method is not defined.
    2. Should raise an error if name already exists in class.

    """
    field = Field()
    assert field('__str__') == field.__str__()

    try:
        assert field('__init__')
    except UndefinedField:
        pass



# Generated at 2022-06-14 01:08:04.535567
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    field = AbstractField()
    assert field('string.hexadecimal')



# Generated at 2022-06-14 01:08:05.346678
# Unit test for constructor of class AbstractField
def test_AbstractField():
    schema = Field()
    return schema
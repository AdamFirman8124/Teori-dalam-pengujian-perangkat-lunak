

# Generated at 2022-06-14 01:07:35.442504
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Check constructor of class AbstractField."""
    field = AbstractField()

# Generated at 2022-06-14 01:07:46.553953
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Unit test for method __call__ of class AbstractField."""
    field = Field()

    assert field('choice')

    assert field('full_name', key=lambda x: x.split(' ')[0]) == \
        field('person.full_name', key=lambda x: x.split(' ')[0])

    assert field('title') == field('text.title')

    try:
        field('wrong.field')
    except UndefinedField:
        pass

    try:
        field('wrong.field.name')
    except UnacceptableField:
        pass

    # create some provider
    class CusProvider:

        def get_method(self):
            return 'test'

    assert field('get_method', providers=CusProvider) == 'test'



# Generated at 2022-06-14 01:07:48.626377
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test for method '__init__'."""
    field = AbstractField()

# Generated at 2022-06-14 01:07:52.224246
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert Field()
    assert Field('en')
    assert Field('en', seed=None)
    assert Field('en', seed=10)
    assert Field('en', providers=None)

# Generated at 2022-06-14 01:07:58.657683
# Unit test for constructor of class AbstractField
def test_AbstractField():
    """Test for init of AbstractField."""
    new_field = AbstractField()
    assert new_field
    assert new_field.locale == 'en'

    new_field_with_locale = AbstractField(locale='ru')
    assert new_field_with_locale
    assert new_field_with_locale.locale == 'ru'



# Generated at 2022-06-14 01:08:12.571722
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    # Test 1, the method which has two arguments
    f = Field()
    assert f('SAMPLE', size=8) == 'FFE14499'

    # Test 2, if method not found, then error raises
    f = Field()
    try:
        f('test')
        raise AssertionError()
    except UndefinedField:
        pass

    # Test 3, if method has two arguments, but key function applied
    f = Field()
    assert f('SAMPLE', key=lambda x: x.upper(), size=8) == 'FFE14499'

    # Test 4, if method has two arguments, but key function applied
    f = Field()
    assert f('sample', key=lambda x: x.upper(), size=8) == 'FFE14499'

    # Test 5, if explicit provider chosen, then method from this provider

# Generated at 2022-06-14 01:08:24.256052
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():
    """Test for `AbstractField.__call__`.

    .. warning:: This method can break. It's a unit test for
        :func:`~mimesis.schema.AbstractField.__call__` and can break
        when the method is changed.
    """
    loc = Generic('en')

    f = AbstractField()


# Generated at 2022-06-14 01:08:31.969059
# Unit test for method __call__ of class AbstractField
def test_AbstractField___call__():

    def key(result: str) -> str:
        value = result.split(' ')[0]
        return f'{value}@mail.com'

    field = Field()
    assert field('person.full_name') == 'Robert Houston'
    assert field('person.full_name', key=key) == 'Robert@mail.com'
    assert field('datetime.datetime') == 'Wed, 5 Nov 2003 05:35:30 GMT'



# Generated at 2022-06-14 01:08:36.023885
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert AbstractField().__class__.__name__ == 'AbstractField'
    assert AbstractField(locale='ru', seed=123).__class__.__name__ \
        == 'AbstractField'

# Generated at 2022-06-14 01:08:37.390007
# Unit test for constructor of class AbstractField
def test_AbstractField():
    assert isinstance(AbstractField(), AbstractField)
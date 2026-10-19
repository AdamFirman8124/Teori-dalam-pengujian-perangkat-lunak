

# Generated at 2022-06-14 00:05:53.256102
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g.person


# Generated at 2022-06-14 00:06:05.508181
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    assert Generic()._person(Generic().locale, Generic().seed) != None
    assert Generic()._person(Generic().locale, Generic().seed) == Generic().person
    assert Generic()._address(Generic().locale, Generic().seed) != None
    assert Generic()._address(Generic().locale, Generic().seed) == Generic().address
    assert Generic()._datetime(Generic().locale, Generic().seed) != None
    assert Generic()._datetime(Generic().locale, Generic().seed) == Generic().datetime
    assert Generic()._business(Generic().locale, Generic().seed) != None
    assert Generic()._business(Generic().locale, Generic().seed) == Generic().business
    assert Generic()._text(Generic().locale, Generic().seed) != None

# Generated at 2022-06-14 00:06:10.681926
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider
    class TestProvider(BaseProvider):
        class Meta:
            name = 'test_provider'
        def test_method(self):
            return 'test_method'

    obj = Generic('ru')
    obj.add_provider(TestProvider)
    assert hasattr(obj, 'test_provider')
    assert obj.test_provider.test_method() == "test_method"


# Generated at 2022-06-14 00:06:22.742057
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider of class Generic."""
    # Test without exception
    class TestProvider(BaseProvider):
        """Test provider for test_Generic_add_provider."""

        class Meta:
            """Class for metadata."""

            name = 'test_provider'

        def __init__(self, seed: int = None):
            """Initialize attributes.

            :param seed: Seed.
            """
            super().__init__(seed=seed)

        def test_func(self):
            """Test function."""
            pass

    # Test with exception
    class TestProvider2(object):
        """Test provider 2 for test_Generic_add_provider."""

        def test_func(self):
            """Test function."""
            pass

    gen = Generic()

    gen.add_provider(TestProvider)

# Generated at 2022-06-14 00:06:35.146315
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # positive test
    class CustomProvider(BaseProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        class Meta:
            name = 'custom'

        def custom(self):
            return "CUSTOM"

    generic = Generic()
    generic.add_provider(CustomProvider)
    assert generic.custom.custom() == "CUSTOM"

    # negative tests
    class CustomProvider(object):
        """Class without inheritance from BaseProvider."""

        class Meta:
            name = 'custom'

        def custom(self):
            return "CUSTOM"

    generic = Generic()

# Generated at 2022-06-14 00:06:37.925075
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test __getattr__ Method."""
    assert callable(Generic().address)



# Generated at 2022-06-14 00:06:44.426304
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Testing(BaseProvider):
        class Meta:
            name = 'test'

        def foo(self) -> str:
            return 'bar'

    provider = Generic()
    provider.add_provider(Testing)

    assert hasattr(provider, 'test')
    assert hasattr(provider.test, 'foo')
    assert provider.test.foo() == 'bar'


# Generated at 2022-06-14 00:06:46.106887
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    assert len (Generic().__getattr__('address')) > 0


# Generated at 2022-06-14 00:06:55.044687
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic(seed=123456, locale='en')
    assert isinstance(g.person(), Person)
    assert isinstance(g.address(), Address)
    assert isinstance(g.datetime(), Datetime)
    assert isinstance(g.business(), Business)
    assert isinstance(g.text(), Text)
    assert isinstance(g.food(), Food)
    assert isinstance(g.science(), Science)
    assert isinstance(g.transport(), Transport)
    assert isinstance(g.code(), Code)
    assert isinstance(g.unit_system(), UnitSystem)
    assert isinstance(g.file(), File)
    assert isinstance(g.numbers(), Numbers)
    assert isinstance(g.development(), Development)
    assert isinstance(g.hardware(), Hardware)

# Generated at 2022-06-14 00:06:57.167011
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    gen = Generic()
    gen.person = Person
    assert gen.person == Person

# Generated at 2022-06-14 00:07:32.126254
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    # Check return value
    generic = Generic()
    assert isinstance(generic.person, Person)
    assert isinstance(generic.address, Address)
    assert isinstance(generic.datetime, Datetime)
    assert isinstance(generic.business, Business)
    assert isinstance(generic.text, Text)
    assert isinstance(generic.food, Food)
    assert isinstance(generic.science, Science)
    assert isinstance(generic.transport, Transport)
    assert isinstance(generic.code, Code)
    assert isinstance(generic.unit_system, UnitSystem)
    assert isinstance(generic.file, File)
    assert isinstance(generic.numbers, Numbers)
    assert isinstance(generic.development, Development)
    assert isinstance(generic.hardware, Hardware)

# Generated at 2022-06-14 00:07:36.390671
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()
    g.add_provider(Business)
    assert g.business.__class__ == Business

test_Generic_add_provider()

# Generated at 2022-06-14 00:07:51.816356
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider."""
    from mimesis.builtins.base import BaseSpecProvider
    import mimesis.builtins

    class TestClass(BaseSpecProvider):
        """Test class."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        @property
        def foo_bar(self) -> str:
            """Test function."""
            return 'foo_bar'

    test_generic = Generic()
    test_generic.add_provider(TestClass)
    assert test_generic.testclass.foo_bar == 'foo_bar'

    with pytest.raises(TypeError) as excinfo:
        test_generic.add_provider(mimesis.builtins.Generic)

# Generated at 2022-06-14 00:07:57.056265
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        class Meta:
            name = 'my_provider'

        def __init__(self):
            super().__init__()
            self.data = ['1', '2', '3']

        def foo(self):
            return self.random.choice(self.data)

    g = Generic()
    g.add_provider(MyProvider)
    g.my_provider.foo()
    g.add_provider(MyProvider)
    g.my_provider.foo()

# Generated at 2022-06-14 00:08:01.983677
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test adding a custom provider to Generic() object."""
    g = Generic('en')
    g.add_provider(CustomProvider)
    assert hasattr(g, 'custom_provider')

    g.add_provider(CustomProvider2)
    assert hasattr(g, 'customprovider2')



# Generated at 2022-06-14 00:08:07.645302
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.crypto import Bitcoin
    a = Generic()
    assert 'Bitcoin' not in dir(a)
    assert a.__dir__().count('Bitcoin') == 0
    a.add_provider(Bitcoin)
    assert 'Bitcoin' in dir(a)
    assert a.__dir__().count('Bitcoin') == 1
    assert a.Bitcoin
    assert a.Bitcoin.address()


# Generated at 2022-06-14 00:08:11.484591
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for Generic_add_provider."""
    class TestProvider(BaseProvider):
        def test(self, a):
            return a

    provider = Generic()
    provider.add_provider(TestProvider)
    assert provider.test.test(1) == 1


# Generated at 2022-06-14 00:08:15.487741
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # Create instance of class Generic
    generic = Generic()
    # Add new provider to instance of class Generic
    generic.add_provider(Address)
    assert hasattr(generic, 'address')
    assert generic.address.__class__.__name__ == 'Address'


# Generated at 2022-06-14 00:08:21.252245
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # Arrange
    provider = Generic()
    # Act
    class FooProvider(BaseProvider):
        class Meta:
            name = 'foo'
    provider.add_provider(FooProvider)
    # Assert
    assert hasattr(provider, 'foo')


# Generated at 2022-06-14 00:08:24.796468
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Simple(BaseProvider):
        class Meta:
            name = 'example'

        def method(self):
            return 42

    generic = Generic()
    generic.add_provider(Simple)

    assert generic.example is not None
    assert generic.example.method() == 42
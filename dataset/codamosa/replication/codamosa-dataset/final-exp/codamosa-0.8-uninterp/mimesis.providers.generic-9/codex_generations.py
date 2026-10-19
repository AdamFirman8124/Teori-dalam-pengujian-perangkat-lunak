

# Generated at 2022-06-14 00:05:56.527988
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    g.person()
    assert g.person()
    assert g.person().full_name



# Generated at 2022-06-14 00:06:04.640047
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Cls(BaseProvider):
        _text = Text(seed=1)

        class Meta:
            name = 'cls'

        def foo(self):
            return self._text.text(10)

    generic = Generic()
    generic.add_provider(Cls)
    assert hasattr(generic, 'cls')
    assert generic.cls.foo() == 'tkvncktjau'

    with pytest.raises(TypeError):
        generic.add_provider(Generic)



# Generated at 2022-06-14 00:06:14.424590
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider method of class Generic.

    :return: None
    """
    class MyProvider(BaseProvider):
        """Docstring."""
        def __init__(self, seed=None):
            # type: (int) -> None
            super(MyProvider, self).__init__(seed=seed)
            self.__my_attribute = ['a', 'b', 'c']

        def __get_attribute(self):
            # type: () -> str
            return self.random.choice(self.__my_attribute)

        class Meta:
            """Docstring."""
            name = 'myprovider'

    generic = Generic('es')
    assert not hasattr(generic, 'myprovider')
    generic.add_provider(MyProvider)
    assert hasattr(generic, 'myprovider')
   

# Generated at 2022-06-14 00:06:20.862027
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic('en')
    generic.file
    generic.numbers
    generic.development
    generic.hardware
    generic.clothing
    generic.internet
    generic.path
    generic.payment
    generic.cryptographic
    generic.structure
    generic.choice

# Generated at 2022-06-14 00:06:34.662426
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert callable(g.person.full_name)
    assert callable(g.person.username)
    assert callable(g.address.address)
    assert callable(g.datetime.now)
    assert callable(g.business.company)
    assert callable(g.text.create_sentence)
    assert callable(g.food.drink)
    assert callable(g.transport.airport_code)
    assert callable(g.code.barcode)
    assert callable(g.unit_system.mass)
    assert callable(g.file.extension)
    assert callable(g.numbers.integer)
    assert callable(g.development.language)
    assert callable(g.hardware.cpu_name)

# Generated at 2022-06-14 00:06:38.528744
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()

    actual = [g.person, g.address, g.datetime, g.business,
              g.text, g.food, g.science]

    assert len(actual) == 7
    assert all(isinstance(a, BaseProvider) for a in actual)



# Generated at 2022-06-14 00:06:40.763210
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    provider.add_provider(Pizza)
    assert provider.pizza


# Generated at 2022-06-14 00:06:43.301618
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    x = Generic().__getattr__('person')
    assert x is not None
    assert callable(x) is False

# Generated at 2022-06-14 00:06:54.833328
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider method of class Generic."""
    class MyProvider(BaseProvider):
        """Example of custom provider."""

        class Meta:
            """Describe a name of provider."""

            name = 'my_provider'

        def my_method(self) -> str:
            """Return a random string."""
            return self.random.choice(['a', 'b', 'c'])

        def my_method_args(self, *args, **kwargs) -> str:
            """Return a random string from *args."""
            return self.random.choice(args)

        def my_method_kwargs(self, *args, **kwargs) -> str:
            """Return a random string from **kwargs."""
            return self.random.choice(list(kwargs.values()))

    g = Generic()

# Generated at 2022-06-14 00:06:59.880339
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    generic.__getattr__('person')
    assert isinstance(generic.person, Person)
    assert generic.person.full_name() != generic.person.full_name()



# Generated at 2022-06-14 00:07:25.589624
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        class Meta:
            name = 'my_provider'
    
    a = Generic('en')
    a.add_provider(MyProvider)
    assert hasattr(a, 'my_provider') and issubclass(type(a.my_provider), BaseProvider)
    assert a.my_provider != a.file
    assert hasattr(a.my_provider, 'text') and hasattr(a.my_provider, 'integer')


# Generated at 2022-06-14 00:07:34.227724
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider_1 = Generic()
    provider_1.add_provider(type('CustomProvider',
                                 (BaseProvider,),
                                 {'random_element': lambda x: 'CustomProvider',
                                  'Meta': type('Meta', (), {'name': 'custom'})}))
    assert isinstance(provider_1.custom, type('CustomProvider',
                                              (BaseProvider,),
                                              {'random_element': lambda x: 'CustomProvider',
                                               'Meta': type('Meta', (), {'name': 'custom'})}))


# Generated at 2022-06-14 00:07:38.872848
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider method of class Generic."""
    from mimesis import Generic
    from mimesis.providers.text import Lorem
    g = Generic()
    g.add_provider(Lorem)
    assert g.lorem

# Generated at 2022-06-14 00:07:42.089189
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    gen = Generic()
    assert hasattr(gen, 'person')

# Generated at 2022-06-14 00:07:46.210471
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    Generic().add_provider(BaseProvider)
    assert hasattr(Generic(), 'base_provider')


# Generated at 2022-06-14 00:07:54.694040
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test for method __getattr__ of class Generic."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    test_generic = Generic()
    test_generic.gender = Gender.MALE
    test_generic.locale = 'ru'
    tester = Person(test_generic.locale, test_generic.seed)
    result_from_generic = test_generic.name
    result_from_provider = tester.name
    assert result_from_generic == result_from_provider


# Generated at 2022-06-14 00:07:56.689652
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        class Meta:
            name = 'custom'

    g = Generic()
    g.add_provider(CustomProvider)
    assert isinstance(g.custom, CustomProvider)

# Generated at 2022-06-14 00:08:07.786799
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test adding provider to an object of class Generic."""
    from mimesis.exceptions import FieldNotFound  # noqa: E301 # pylint: disable=import-outside-toplevel

    class Foo(BaseProvider):
        """Custom provider."""

        class Meta:
            """Class for metadata."""
            name = 'foo'

        def foo(self) -> str:
            """Form and return example data."""
            return 'foo'

    class Bar(BaseProvider):
        """Custom provider."""

        def bar(self) -> str:
            """Form and return example data."""
            return 'bar'

    data_provider = Generic()
    data_provider.add_provider(Foo)
    data_provider.add_provider(Bar)


# Generated at 2022-06-14 00:08:12.244117
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()
    g.add_provider(CustomProviderOne)
    g.add_provider(CustomProviderTwo)
    assert g.custom_provider_one.get_custom_provider_one() == 'Hello World'
    assert g.custom_provider_two.get_custom_provider_two() == 'Bye World'



# Generated at 2022-06-14 00:08:23.574090
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic('ru')
    assert g.person.full_name() == 'Иванов Анатолий'
    assert g.address.city() == 'Суздаль'
    assert g.datetime.date() == '1988-01-02'
    assert g.business.company() == 'АЛЬФА'
    assert g.text.title() == 'Капитас Рима'
    assert g.food.fruit() == 'помидор'

    class RecordLabel(BaseProvider):
        class Meta:
            name = 'record_label'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


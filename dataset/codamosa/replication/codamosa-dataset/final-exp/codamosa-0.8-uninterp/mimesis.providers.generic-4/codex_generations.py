

# Generated at 2022-06-14 00:06:03.179939
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider."""

    class MyProvider(BaseProvider):
        class Meta:
            name = 'myprovider'

        def get_data(self, **kwargs):
            return 'myprovider'

    generic = Generic()
    generic.add_provider(MyProvider)
    assert 'myprovider' == generic.myprovider.get_data()

# Generated at 2022-06-14 00:06:08.005676
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Method __getattr__ of class Generic."""
    generic = Generic()
    generic.add_provider(TestProvider)
    test = generic.test_provider()
    assert isinstance(test, Test)


# Generated at 2022-06-14 00:06:20.076891
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    def test_metaclass_provider(case: dict) -> None:
        """Test meta class for providers."""
        gen = Generic()
        assert hasattr(gen, case['name'])

        provider = getattr(gen, case['name'])
        assert isinstance(provider, case['type'])

    cases = (
        {'name': 'person', 'type': Person},
        {'name': 'address', 'type': Address},
        {'name': 'datetime', 'type': Datetime},
        {'name': 'business', 'type': Business},
        {'name': 'text', 'type': Text},
        {'name': 'food', 'type': Food},
        {'name': 'science', 'type': Science},
    )

    for case in cases:
        yield test_metaclass_

# Generated at 2022-06-14 00:06:27.143737
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class ExampleProvider(BaseProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def example_method(self):
            return 'example'

    class Meta:
        name = 'example'

    ExampleProvider.Meta = Meta

    generic = Generic()
    generic.add_provider(ExampleProvider)

    assert generic.example.example_method() == 'example'


# Generated at 2022-06-14 00:06:33.862212
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    Generic.add_provider(Generic)

    assert Generic.Generic
    assert Generic.Generic().__class__.__name__ == 'Generic'

    Generic.add_provider(Person)
    assert Generic.Person
    assert Generic.Person().__class__.__name__ == 'Person'


# Generated at 2022-06-14 00:06:37.604642
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    # Check attribute exists
    generic = Generic(language='en')
    person = getattr(generic, 'person')
    assert isinstance(person, Person)

    # Check attribute not exists
    assert hasattr(generic, '_x') is False



# Generated at 2022-06-14 00:06:48.833754
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic(locale="fr")
    assert isinstance(g.person(), Person)
    assert isinstance(g.address(), Address)
    assert isinstance(g.datetime(), Datetime)
    assert isinstance(g.business(), Business)
    assert isinstance(g.text(), Text)
    assert isinstance(g.food(), Food)
    assert isinstance(g.science(), Science)
    assert isinstance(g.transport, Transport)
    assert isinstance(g.code, Code)
    assert isinstance(g.unit_system, UnitSystem)
    assert isinstance(g.file, File)
    assert isinstance(g.numbers, Numbers)
    assert isinstance(g.development, Development)
    assert isinstance(g.hardware, Hardware)
    assert isinstance(g.clothing, Clothing)

# Generated at 2022-06-14 00:06:51.479211
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():

    class Provider(BaseProvider):
        pass

    provider = Provider()
    generic = Generic(seed=42)
    generic.add_provider(Provider)

    assert provider == generic.provider

# Generated at 2022-06-14 00:06:52.995207
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    assert generic.person == generic._person(generic.locale, generic.seed)


# Generated at 2022-06-14 00:07:04.365027
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.identifier import Identifier
    from mimesis.providers.name import Name
    from mimesis.providers.person import Person
    from mimesis.providers.structural import Structural

    generic = Generic()
    assert 'identifier' not in dir(generic)
    assert 'name' not in dir(generic)
    assert 'person' in dir(generic)
    assert 'structural' not in dir(generic)
    generic.add_provider(Identifier)
    generic.add_provider(Name)
    generic.add_provider(Structural)
    generic.add_provider(type(generic))

    assert 'identifier' in dir(generic)
    assert 'name' in dir(generic)
    assert 'person' in dir(generic)
    assert 'structural'

# Generated at 2022-06-14 00:07:25.098211
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic(seed=42)
    street__name = g.address._data['el']['street_suffix']
    assert g.address.street_suffix == street__name

# Generated at 2022-06-14 00:07:31.732604
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test Generic.add_provider()."""
    import mimesis.providers.person
    generic = Generic(locale='en')
    generic.add_provider(mimesis.providers.person.Person)
    assert hasattr(generic, 'person')
    assert generic.person.full_name() == 'Richard Brown'

# Generated at 2022-06-14 00:07:32.964291
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    address = Address
    Generic.add_provider(address)


# Generated at 2022-06-14 00:07:35.441117
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass

# Generated at 2022-06-14 00:07:43.860338
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Provider(BaseProvider):
        class Meta:
            name = 'provider'

        def __init__(self, seed=None):
            super().__init__(seed)

        def foo(self):
            return 'bar'

    generic = Generic()

    generic.add_provider(Provider)
    assert generic.provider.foo() == 'bar'

    generic.add_provider(Science)
    assert generic.science.get_periodic_element()

    try:
        generic.add_provider(BaseDataProvider)
    except TypeError:
        assert 1


# Generated at 2022-06-14 00:07:48.222306
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert isinstance(g.person, Person)
    assert isinstance(g.address, Address)
    assert isinstance(g.datetime, Datetime)

# Generated at 2022-06-14 00:07:49.168086
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    assert callable(Generic().person)

# Generated at 2022-06-14 00:07:57.165263
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
	# Test case 1
	# The method __getattr__ should return self.address
	# with attrname = 'address'

	# Setup
	g = Generic('en')
	attrname = 'address'
	expected = Address(locale='en', seed=12)

	# Assertion
	assert getattr(g, attrname) == expected
	assert g.address == expected
	# Test case 2
	# The method __getattr__ should return self.address
	# with attrname = 'Address'

	# Setup
	g = Generic('en')
	expected = Address(locale='en', seed=12)
	attrname = 'Address'

	# Assertion
	assert getattr(g, attrname) == expected
	assert g.Address == expected
	# Test case 3
	# The method __

# Generated at 2022-06-14 00:07:58.579385
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic(seed=42)
    print(generic.food.fruit_name())

# Generated at 2022-06-14 00:08:02.427583
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic()
    assert not hasattr(generic, 'foobar')
    foobar = BaseProvider()
    generic.add_provider(foobar)
    assert hasattr(generic, 'foobar')

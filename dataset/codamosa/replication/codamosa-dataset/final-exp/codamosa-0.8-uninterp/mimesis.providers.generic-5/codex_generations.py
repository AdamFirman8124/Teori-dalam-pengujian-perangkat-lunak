

# Generated at 2022-06-14 00:05:57.570341
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic()
    class CustomProvider(BaseProvider):
        def foo(self):
            pass

    assert not hasattr(generic, 'custom_provider')
    generic.add_provider(CustomProvider)
    assert hasattr(generic, 'custom_provider')
    assert hasattr(generic.custom_provider, 'foo')


# Generated at 2022-06-14 00:06:12.202272
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic('de', seed=123)
    assert isinstance(generic._address, Address)
    assert isinstance(generic.address, Address)
    assert isinstance(generic._business, Business)
    assert isinstance(generic.business, Business)
    assert isinstance(generic._datetime, Datetime)
    assert isinstance(generic.datetime, Datetime)
    assert isinstance(generic._food, Food)
    assert isinstance(generic.food, Food)
    assert isinstance(generic._person, Person)
    assert isinstance(generic.person, Person)
    assert isinstance(generic._science, Science)
    assert isinstance(generic.science, Science)
    assert isinstance(generic._text, Text)
    assert isinstance(generic.text, Text)
    assert isinstance(generic.transport, Transport)

# Generated at 2022-06-14 00:06:16.904726
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Provider(BaseProvider):
        """Test for add_provider method."""

        class Meta:
            """Class for metadata."""
            name = 'provider'

    generic = Generic()
    generic.add_provider(Provider)
    assert hasattr(generic, 'provider')



# Generated at 2022-06-14 00:06:20.943950
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    obj = Generic()
    assert isinstance(obj.person, Person)
    assert isinstance(obj.address, Address)
    assert isinstance(obj.datetime, Datetime)
    assert isinstance(obj.internet, Internet)
    assert isinstance(obj.clothing, Clothing)

# Generated at 2022-06-14 00:06:22.086476
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic('en')
    assert g.add_provider(None) == None

# Generated at 2022-06-14 00:06:29.857071
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.development import Development
    from mimesis.providers.internet import Internet
    g = Generic('en')
    assert not hasattr(g, 'development')
    assert not hasattr(g, 'internet')
    g.add_provider(Development)
    g.add_provider(Internet)
    assert isinstance(g.development, Development)
    assert isinstance(g.internet, Internet)
    try:
        g.add_provider(Generic)
        assert False
    except:
        assert True


# Generated at 2022-06-14 00:06:34.983124
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    # Create instance of class Generic
    g = Generic(seed=123456789)
    # Define list of attributes
    attrs=['address', 'datetime', 'person']
    # Iterate over list of attributes
    for attr in attrs:
        # Check if attribute has been retrieved
        assert hasattr(g, attr)


# Generated at 2022-06-14 00:06:39.910543
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():

    class Test(Generic):
        pass

    class Custom(BaseProvider):

        class Meta:
            name = 'custom'

        def foo(self) -> str:
            return 'bar'

    gen = Test()
    gen.add_provider(Custom)

    assert getattr(gen, 'custom', None) is not None
    assert callable(getattr(gen, 'custom', None))
    assert gen.custom.foo() == 'bar'


# Generated at 2022-06-14 00:06:50.057131
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis import Person as Person_provider
    from mimesis.person import Person as Person_
    from mimesis.generic import Generic

    # Create custom provider
    class Interfaces(Person_):
        class Meta:
            name = "interfaces"

    class Bbb(Person_):
        class Meta:
            name = "bbb"

    # Create object of generic class
    generic = Generic()

    # Add custom provider
    generic.add_provider(Interfaces)

    # Add custom provider
    generic.add_provider(Bbb)

    # Get provider by name
    interfaces = getattr(generic, "interfaces")
    bbb = getattr(generic, "bbb")

    # Check that provider is used
    assert isinstance(interfaces, Interfaces)

# Generated at 2022-06-14 00:07:00.264677
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    g = Generic()
    assert callable(g.person)
    assert callable(g.address)
    assert callable(g.datetime)
    assert callable(g.business)
    assert callable(g.text)
    assert callable(g.food)
    assert callable(g.science)
    assert callable(g.transport)
    assert callable(g.code)
    assert callable(g.unit_system)
    assert callable(g.file)
    assert callable(g.numbers)
    assert callable(g.hardware)
    assert callable(g.clothing)
    assert callable(g.internet)
    assert callable(g.path)
    assert callable(g.payment)



# Generated at 2022-06-14 00:06:04.713107
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test for method __getattr__ of class Generic."""
    generic = Generic()
    generic.__getattr__('person')

# Generated at 2022-06-14 00:06:11.304459
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g.person
    assert g.address
    assert g.business
    assert g.datetime
    assert g.text
    assert g.food
    assert g.science
    assert g.transport
    assert g.code
    assert g.unit_system
    assert g.file
    assert g.numbers
    assert g.development
    assert g.hardware
    assert g.clothing
    assert g.internet
    assert g.path
    assert g.payment
    assert g.cryptographic
    assert g.structure
    assert g.choice



# Generated at 2022-06-14 00:06:13.318954
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    g.person.full_name()

# Generated at 2022-06-14 00:06:23.915378
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test for method __getattr__."""
    generic = Generic()
    assert isinstance(generic, BaseDataProvider)
    assert isinstance(generic.person, Person)
    assert isinstance(generic.business, Business)
    assert isinstance(generic.address, Address)
    assert isinstance(generic.datetime, Datetime)
    assert isinstance(generic.text, Text)
    assert isinstance(generic.science, Science)
    assert isinstance(generic.food, Food)
    assert isinstance(generic.transport, Transport)
    assert isinstance(generic.code, Code)
    assert isinstance(generic.unit_system, UnitSystem)
    assert isinstance(generic.file, File)
    assert isinstance(generic.numbers, Numbers)
    assert isinstance(generic.development, Development)

# Generated at 2022-06-14 00:06:31.920978
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Test:
        # pylint: disable=too-few-public-methods
        class Meta:
            # pylint: disable=too-few-public-methods
            name = 'test'

    gen = Generic()
    gen.add_provider(Test)
    assert hasattr(gen, 'test')
    assert isinstance(gen.test, Test)


# Generated at 2022-06-14 00:06:39.183846
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider of class Generic"""

    from mimesis.providers.custom.dummy import DummyCustomProvider
    from mimesis.providers.custom.dummy import DummyCustomProvider2
    g = Generic()
    g.add_provider(DummyCustomProvider)
    g.add_provider(DummyCustomProvider2)
    result = g.dummycustomprovider.name
    assert result == 'dummycustomprovider'
    result = g.dummycustomprovider2.foo
    assert result == 'foo'



# Generated at 2022-06-14 00:06:40.878531
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test Generic.add_provider."""
    _ = Generic()



# Generated at 2022-06-14 00:06:44.425750
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    gen = Generic()
    assert hasattr(gen, 'person')
    assert isinstance(gen.person, Person)


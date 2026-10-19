

# Generated at 2022-06-14 00:06:07.004991
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    g = Generic()
    attributes = g.__dict__.keys()
    for attribute in attributes:
        if not attribute.startswith('_'):
            print(attribute)
            assert getattr(g, attribute)
        else:
            attribute = attribute.replace('_', '', 1)
            assert getattr(g, attribute)



# Generated at 2022-06-14 00:06:10.695536
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.person import Person  # noqa: E501

    g = Generic()
    g.add_provider(Person)
    os = g.person.operating_system

# Generated at 2022-06-14 00:06:16.511568
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.identifier import Identifier
    generic = Generic()
    assert 'identifier' not in dir(generic)
    generic.add_provider(Identifier)
    assert 'identifier' in dir(generic)
    assert isinstance(generic.identifier, Identifier)


# Generated at 2022-06-14 00:06:30.768904
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic(seed=1)
    g.person.full_name(gender='male')
    g.person.full_name(gender='female')
    g.business.company()
    g.address.address()
    g.food.fruit()
    g.food.vegetable()
    g.science.planet()
    g.transport.bike()
    g.code.cvv()
    g.unit_system.information()
    g.file.extension()
    g.numbers.number(end=1000)
    g.development.operating_system()
    g.hardware.component()
    g.clothing.shoe()
    g.internet.email()
    g.path.path()
    g.payment.iban()
    g.cryptographic.hash()

# Generated at 2022-06-14 00:06:37.990484
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test adding a provider to Generic object."""
    import mimesis.providers.payment.en_US as en_US_payment
    generic = Generic('en')
    generic.add_provider(en_US_payment.CreditCard)
    assert len(dir(generic)) == len(dir(Generic('en'))) + 1
    assert 'credit_card' in dir(generic)
    assert 'CreditCard' in dir(en_US_payment)
    print("Added a provider to Generic object successfully!")



# Generated at 2022-06-14 00:06:48.837939
# Unit test for method add_provider of class Generic

# Generated at 2022-06-14 00:06:52.419637
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.builtins import RussiaSpecProvider
    g = Generic()
    g.add_provider(RussiaSpecProvider)
    assert hasattr(g, 'russia_spec')
    assert isinstance(g.russia_spec, RussiaSpecProvider)


# Generated at 2022-06-14 00:06:55.574821
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    g = Generic('ar_SA')
    assert g.person.full_name == 'أحمد علي'
    assert g.business.company_name == 'بيتزا هت'



# Generated at 2022-06-14 00:07:02.033762
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        class Meta:
            name = 'custom'

        def custom_method(self) -> int:
            return 2

    g = Generic()
    g.add_provider(CustomProvider)
    assert isinstance(g.custom, CustomProvider)



# Generated at 2022-06-14 00:07:09.935888
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    provider = Generic()

    assert provider.person
    assert provider.address
    assert provider.datetime
    assert provider.business
    assert provider.text
    assert provider.food
    assert provider.science
    assert provider.transport
    assert provider.code
    assert provider.unit_system
    assert provider.file
    assert provider.numbers
    assert provider.development
    assert provider.hardware
    assert provider.clothing
    assert provider.internet
    assert provider.path
    assert provider.payment
    assert provider.cryptographic
    assert provider.structure


# Generated at 2022-06-14 00:07:36.913032
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Tests for Generic.add_provider() method."""
    gen = Generic()

    class MyProvider(BaseProvider):
        """Provider for testing."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def foo(self):
            return 'bar'

    # Expected: add MyProvider to Generic()
    gen.add_provider(MyProvider)
    assert isinstance(gen.my_provider, MyProvider)
    assert gen.my_provider.foo() == 'bar'
    assert gen.my_provider.seed == gen.seed

    # Expected: add MyProvider to Generic() and override seed
    gen.add_provider(MyProvider, seed=123456789)
    assert gen.my_provider.seed == 123

# Generated at 2022-06-14 00:07:42.241877
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # Initialize the class and add a custom provider
    generic = Generic(seed=12345)
    class CustomProvider(BaseProvider):
        pass
    generic.add_provider(CustomProvider)
    # Validate that the custom provider was added
    assert isinstance(generic.customprovider, CustomProvider)


# Generated at 2022-06-14 00:07:54.815393
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    # Test for normal work
    generic = Generic()
    assert generic.person.email() == 'alex_90@gmail.com'
    assert generic.address.province() == 'Нижегородская обл.'
    assert generic.datetime.timestamp() >= 0
    assert generic.business.business_number()
    assert generic.text.text()
    assert generic.datetime.date()
    assert generic.food.fruit()
    assert generic.science.biology()
    assert generic.transport.airport()
    assert generic.code.isbn()
    assert generic.unit_system.time()
    assert generic.file.mime_type()
    assert generic.numbers.decimal(maximum=10)
    assert generic.development.id_()

# Generated at 2022-06-14 00:07:56.860735
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic('en')
    # Localized provider
    assert isinstance(g.person, Person)
    # Non-localized provider
    assert isinstance(g.code, Code)



# Generated at 2022-06-14 00:08:01.580994
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert(g.person)
    assert(g.person_full_name())
    assert(g.address)
    assert(g.address_full_address())
    assert(g.datetime)
    assert(g.datetime_date())

# Generated at 2022-06-14 00:08:06.375253
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic()
    assert generic.code.file is not None
    generic.add_provider(Code)
    assert hasattr(generic, 'code')



# Generated at 2022-06-14 00:08:10.232948
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    assert generic.business.company_name() == 'Daniel_and_Company'
    assert hasattr(generic, 'business')
    assert generic.code.isbn(part='group') == '978'


# Generated at 2022-06-14 00:08:15.971725
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        class Meta:
            name = 'customProvider'
        def method(self):
            return 42
    provider = Generic()
    provider.add_provider(CustomProvider)
    assert provider.__dir__().__contains__('customProvider')
    assert provider.customProvider.method() == 42


# Generated at 2022-06-14 00:08:25.607681
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""
    class Provider(BaseProvider):
        """The custom provider."""

        def __init__(self, *args, **kwargs):
            """Initialize attributes lazily."""
            super().__init__(*args, **kwargs)

        def foo(self):
            """The provider's method."""
            return 'bar'

    provider = Provider()
    assert provider.foo() == 'bar'

    g = Generic()
    g.add_provider(Provider)

    assert g.provider.foo() == 'bar'
    assert g.provider.foo() == 'bar'



# Generated at 2022-06-14 00:08:31.318555
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    # test first use cache
    g.food.get_recipe_name()
    food_provider = g.food._handler
    # test use cache
    g.food.get_recipe_name()
    food_provider_cached = g.food._handler
    assert food_provider == food_provider_cached


# Generated at 2022-06-14 00:08:48.696348
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass
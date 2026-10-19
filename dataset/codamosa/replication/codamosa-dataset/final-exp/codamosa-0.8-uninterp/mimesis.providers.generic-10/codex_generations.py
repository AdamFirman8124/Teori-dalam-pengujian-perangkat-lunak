

# Generated at 2022-06-14 00:05:55.673288
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic()
    try:
        generic.add_provider(generic.choice)
        assert True
    except:
        assert False

test_Generic_add_provider()



# Generated at 2022-06-14 00:06:04.718146
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g.person.full_name() == 'laura'
    assert g.address.city() == 'city'
    assert g.datetime.date() == 'date'
    assert g.business.company() == 'company'
    assert g.text.words() == 'words'
    assert g.food.vegetable() == 'vegetable'
    assert g.science.element() == 'element'
    assert g.transport.license_plate() == 'license_plate'
    assert g.code.imei() == 'imei'
    assert g.unit_system.celsius() == 'celsius'
    assert g.unit_system.fahrenheit() == 'fahrenheit'
    assert g.file.extension() == 'extension'
    assert g.numbers.positive_integer

# Generated at 2022-06-14 00:06:11.304867
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Tests add_provider method."""
    provider = Generic()
    assert not hasattr(provider, 'provider')

    class Provider(BaseProvider):
        class Meta:
            name = 'provider'

    provider.add_provider(Provider)
    assert hasattr(provider, 'provider')


# Generated at 2022-06-14 00:06:18.083875
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic('ru')
    assert generic.code.code.get_issuer_identification_number() == '4007'
    code_provider = BaseProvider()
    generic.add_provider(code_provider)
    assert generic.code.code.get_issuer_identification_number() == '0497'
    assert generic.code.code.get_language() == 'ru'

# Generated at 2022-06-14 00:06:24.984255
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g.person()
    assert g.address()
    assert g.datetime()
    assert g.business()
    assert g.text()
    assert g.food()
    assert g.science()
    assert g.transport()
    assert g.code()
    assert g.unit_system()
    assert g.file()
    assert g.numbers()
    assert g.development()
    assert g.hardware()
    assert g.clothing()
    assert g.internet()
    assert g.path()
    assert g.payment()
    assert g.cryptographic()
    assert g.structure()
    assert g.choice()

# Generated at 2022-06-14 00:06:29.763309
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.builtins.custom_provider import CustomProvider
    bottom = Generic()
    assert 'custom' not in bottom.__dir__()
    bottom.add_provider(CustomProvider)
    assert 'custom' in bottom.__dir__()

# Generated at 2022-06-14 00:06:35.648850
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """
    Unit test for method add_provider of class Generic
    """
    def check_result(result):
        assert 'provider' in result
        assert isinstance(result, Provider)

    class Provider(BaseProvider):
        def provider(self):
            return self

    generic = Generic()
    generic.add_provider(Provider)
    check_result(generic.provider())


# Generated at 2022-06-14 00:06:41.129886
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    gen = Generic('en')
    name = gen.person.full_name()
    assert isinstance(name, str)
    assert len(name.split()) > 0

    # Access to attribute without underscore
    address = gen.address
    city = address.city()
    assert isinstance(city, str)
    assert len(city.split()) > 0
    assert city.isalpha()

    # Access to method
    country_code = address.country_code()
    assert isinstance(country_code, str)
    assert len(country_code.split()) == 0

# Generated at 2022-06-14 00:06:48.833044
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(Person):
        """Provider with custom methods."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def method1(self):
            """Return 1."""
            return 1

        def method2(self, *args):
            """Return args."""
            return args

    g = Generic(locale='en')
    g.add_provider(CustomProvider)
    assert g.custom_provider.method1() == 1
    assert g.custom_provider.method2(2, 3) == (2, 3)

# Generated at 2022-06-14 00:06:52.746901
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    gen = Generic('en')
    gen.add_provider(Choice)
    gen.add_provider(Path)
    assert callable(gen.path)
    assert callable(gen.choice)
    gen.add_provider(Person)
    assert callable(gen.person)


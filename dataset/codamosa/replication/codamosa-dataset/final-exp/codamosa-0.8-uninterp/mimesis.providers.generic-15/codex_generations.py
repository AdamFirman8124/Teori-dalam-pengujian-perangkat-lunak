

# Generated at 2022-06-14 00:05:49.773867
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic('en')
    assert g.address.address()
    assert g.business.company()
    assert g.datetime.datetime()
    assert g.text.text()
    assert g.transport.airplane()
    assert g.development.programming_language()
    assert g.hardware.network()
    assert g.internet.domain_word()
    assert g.path.file_extension()
    assert g.payment.payment_gateway()
    assert g.structure.uuid4()


# Generated at 2022-06-14 00:05:53.337314
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    gen = Generic()
    assert isinstance(gen.person, Person)
    # ...


# Generated at 2022-06-14 00:06:04.001096
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    generic = Generic('en')
    name = generic.person.full_name()

    assert isinstance(name, str)
    assert len(name) > 0

    name = generic.person.full_name()

    assert isinstance(name, str)
    assert len(name) > 0

    code = generic.code.isbn(part='all')

    assert isinstance(code, str)
    assert len(code) > 0

    code = generic.code.isbn(part='all')

    assert isinstance(code, str)
    assert len(code) > 0


# Generated at 2022-06-14 00:06:04.814364
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass

# Generated at 2022-06-14 00:06:07.578896
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    provider.add_provider(Person)
    print(provider.person)

# Generated at 2022-06-14 00:06:19.848218
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test method __getattr__ of class Generic."""
    g = Generic()
    assert isinstance(g.person, Person)
    assert isinstance(g.address, Address)
    assert isinstance(g.text, Text)
    assert isinstance(g.business, Business)
    assert isinstance(g.food, Food)
    assert isinstance(g.science, Science)
    assert isinstance(g.transport, Transport)
    assert isinstance(g.unit_system, UnitSystem)
    assert isinstance(g.file, File)
    assert isinstance(g.numbers, Numbers)
    assert isinstance(g.development, Development)
    assert isinstance(g.hardware, Hardware)
    assert isinstance(g.clothing, Clothing)
    assert isinstance(g.internet, Internet)
    assert isinstance

# Generated at 2022-06-14 00:06:26.544456
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test method add_provider."""
    from mimesis.providers.other import Other

    class OtherProvider(Other):
        """Class for testing generic provider."""

        class Meta:
            name = 'other'
            unit = 'other'

    generic = Generic('ru')
    assert not hasattr(generic, 'other')
    generic.add_provider(OtherProvider)
    assert hasattr(generic, 'other')
    assert generic.other.other()

# Generated at 2022-06-14 00:06:38.552083
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic(seed=42)
    assert generic.person.full_name() == 'Paul Johnson'
    assert generic.person.age() == 40
    assert generic.person.gender() == 'Male'
    assert generic.person.username() == 'johnson-p'
    assert generic.address.address() == '870 Hudson St.'
    assert generic.datetime.datetime() == '04/08/1979 18:48:24'
    assert generic.datetime.date() == '11/24/1980'
    assert generic.datetime.date() == '11/24/1980'
    assert generic.datetime.date() == '11/24/1980'
    assert generic.datetime.time() == '07:42:32'

    generic = Generic(seed=84)

# Generated at 2022-06-14 00:06:42.067674
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.generic import Generic
    from mimesis.providers.code import Code
    g = Generic()
    g.add_provider(Code)
    assert 'code' in dir(g)

# Generated at 2022-06-14 00:06:51.113545
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # test for add a custom provider
    generic = Generic('en')
    class CustomProvider(BaseProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        def foo(self):
            return 'foo'
    custom_provider = CustomProvider('en')
    generic.add_provider(custom_provider)
    assert hasattr(generic, 'custom_provider')
    assert generic.custom_provider.foo() == 'foo'
    # test for add a custom provider with name
    class CustomProviderWithName(BaseProvider):
        class Meta:
            name = 'custom_provider_with_name'
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

# Generated at 2022-06-14 00:07:15.132088
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider
    class A(BaseProvider):
        class Meta:
            name = 'A'
        def a(self):
            return 'A'
    class B(BaseProvider):
        class Meta:
            name = 'B'
        def b(self):
            return 'B'
    class C(BaseProvider):
        def c(self):
            return 'C'
    class D(BaseProvider):
        class Meta:
            name = 'D'
        def d(self):
            return 'D'
    g = Generic()
    assert g.a
    assert g.b
    try:
        g.c
    except AttributeError:
        assert True
    assert g.d

# Generated at 2022-06-14 00:07:18.101336
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""
    from mimesis.providers.test import TestProvider

    g = Generic()
    g.add_provider(TestProvider)
    assert isinstance(g.test, TestProvider)



# Generated at 2022-06-14 00:07:26.992793
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()

    # Check if add_provider will raise TypeError
    # if we try to add smth that is not a class
    try:
        provider.add_provider('')
    except TypeError:
        pass
    else:
        raise AssertionError('TypeError')

    # If provider is not a subclass of BaseProvider TypeError should be raised
    class CustomProvider(object):
        pass

    try:
        provider.add_provider(CustomProvider)
    except TypeError:
        pass
    else:
        raise AssertionError('CustomProvider is not subclass of '
                             'BaseProvider')

    # If provider is a subclass of BaseProvider, it should be added to our
    # Generic() object as an attribute
    provider.add_provider(Choice)

# Generated at 2022-06-14 00:07:29.323446
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass



# Generated at 2022-06-14 00:07:32.733603
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    gen = Generic()
    gen.add_provider(Code)
    gen.add_provider(Payment)
    assert hasattr(gen, 'code')
    assert hasattr(gen, 'payment')

    # Unit test for method add_providers of class Generic

# Generated at 2022-06-14 00:07:38.398794
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers import Science as ScienceTest

    class Science(ScienceTest):
        """Test class for provider Science."""
        pass

    gen = Generic()
    gen.add_provider(Science)
    assert gen.science



# Generated at 2022-06-14 00:07:54.508544
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider
    from mimesis.builtins import RussiaSpecProvider

    fake = Generic()
    fake.add_provider(RussiaSpecProvider)

    assert 'russia_spec' in dir(fake)
    assert isinstance(fake.russia_spec, RussiaSpecProvider)
    assert fake.russia_spec.seed == fake.seed

    with pytest.raises(TypeError):
        fake.add_provider('str')  # type: ignore

    class A(BaseProvider):  # type: ignore
        """Class for testing."""

        class Meta:
            """Metaclass for testing."""

            name = 'test'

    fake.add_provider(A)
    assert 'test' in dir(fake)
    assert isinstance(fake.test, A)

# Generated at 2022-06-14 00:08:06.338344
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person as CustomPerson

    class CustomPerson2(CustomPerson):
        class Meta:
            """Class for metadata."""

            name = 'person'

    g = Generic()
    g.add_provider(CustomPerson)
    g.add_provider(CustomPerson2)
    if g.person.gender == g.person2.gender:
        assert True
    else:
        assert False

    class CustomPerson(CustomPerson):
        class Meta:
            """Class for metadata."""

            name = 'person'

    g.add_provider(CustomPerson)
    if g.person.gender == g.person.gender:
        assert True
    else:
        assert False


# Generated at 2022-06-14 00:08:09.949544
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    gen = Generic()
    assert gen.person
    assert gen.person.full_name() == "Spencer Sanders"



# Generated at 2022-06-14 00:08:16.210095
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider

    class TestProvider(BaseProvider):
        """This is a test provider."""

        def foo(self) -> str:
            """Return foo."""
            return "foo"

    g = Generic('en')
    g.add_provider(TestProvider)
    assert g.test.foo() == "foo"

# Generated at 2022-06-14 00:08:50.953113
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.builtins.mimesis import mimesis
    # test for exception
    try:
        mimesis.add_provider(mimesis.Generic)
        assert True == False
    except TypeError as e:
        assert e
    # test for successful
    class TestProvider(BaseProvider):
        class Meta:
            name = 'test_provider'

        def method(self):
            return True

    mimesis.add_provider(TestProvider)
    t = mimesis
    assert hasattr(t, 'test_provider')
    assert TestProvider(seed=mimesis.seed)
    assert TestProvider(seed=mimesis.seed).method()
    del TestProvider



# Generated at 2022-06-14 00:08:52.439621
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass
    # TODO - write unit test



# Generated at 2022-06-14 00:09:03.540579
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()
    g.add_provider(Person)
    g.add_provider(Address)
    g.add_provider(Datetime)
    g.add_provider(Business)
    g.add_provider(Text)
    g.add_provider(Food)
    g.add_provider(Science)
    g.add_provider(Transport)
    g.add_provider(Code)
    g.add_provider(UnitSystem)
    g.add_provider(File)
    g.add_provider(Numbers)
    g.add_provider(Development)
    g.add_provider(Hardware)
    g.add_provider(Clothing)
    g.add_provider(Internet)
    g.add_provider(Path)
    g

# Generated at 2022-06-14 00:09:07.971347
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    test = Generic() 
    print(test.__getattr__('person'))
    test.add_provider(Generic)
    print(test.__getattr__('generic'))

# Generated at 2022-06-14 00:09:11.897393
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test method add_provider of class Generic."""
    g = Generic()
    assert not hasattr(g, 'output')
    g.add_provider(Output)
    assert hasattr(g, 'output')


# Generated at 2022-06-14 00:09:13.714649
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()

    test_str = generic.text.sentence(5)
    assert isinstance(test_str, str) is True



# Generated at 2022-06-14 00:09:20.104638
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        def foo(self) -> str:
            return 'foobar'

    gen = Generic()
    gen.add_provider(MyProvider)
    assert gen.foo().foo() == 'foobar'
    assert gen.myprovider.foo() == 'foobar'


# Generated at 2022-06-14 00:09:24.295925
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    new_provider = provider.add_provider('test')
    assert new_provider == None


# Generated at 2022-06-14 00:09:33.182744
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test method add_provider of class Generic."""
    mock_provider = type(
        'MockProvider',
        (BaseProvider,),
        {'Meta': type('Meta', (), {'name': 'mock'})}
    )
    g = Generic()
    g.add_provider(mock_provider)
    assert isinstance(g.mock, mock_provider)


# Generated at 2022-06-14 00:09:35.746271
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic('ru')
    provider.add_provider(CustomProvider)
    assert provider.custom_provider.name() == "CustomProvider"


# Generated at 2022-06-14 00:10:03.509672
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        """Custom provider."""

        class Meta:
            """Class for metadata."""

            name = 'custom_provider'

        def something(self, *args, **kwargs):
            """Custom method.

            :param args: Arguments.
            :param kwargs: Keyword arguments.
            :return: Provider from base class.
            """
            return self.datetime

    g = Generic()
    assert not hasattr(g, 'custom_provider')
    g.add_provider(CustomProvider)
    assert hasattr(g, 'custom_provider')
    assert isinstance(g.custom_provider, CustomProvider)
    g.add_provider(g.custom_provider.__class__)  # will not be added again

# Generated at 2022-06-14 00:10:10.103041
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.finance import Currency, CurrencyCode
    currency = Currency(seed=42)
    currency_code = CurrencyCode(seed=42)
    providers = [currency, currency_code]
    for provider in providers:
        g = Generic()
        g.add_provider(provider)
        assert g.currency.get_value() == (
            'dollar', 'dollar', 7.0, '$')
        assert g.currency_code.value == 'RUB'



# Generated at 2022-06-14 00:10:16.157852
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.science import Science
    m = Generic()
    m.add_provider(Science)
    try:
        m.add_provider(str)
    except TypeError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 00:10:23.636409
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for Generic.add_provider method."""
    from mimesis.providers.sql import SQL
    from mimesis.providers.development import Development

    generic = Generic('en')
    assert 'sql' not in generic.__dir__()

    generic.add_provider(SQL)
    generic.add_provider(Development)

    assert isinstance(generic.sql, SQL)
    assert isinstance(generic.development, Development)



# Generated at 2022-06-14 00:10:24.375274
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    assert 1 == 1

# Generated at 2022-06-14 00:10:29.318295
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    import mimesis.providers.person.en as person
    import mimesis.providers.person.ru as person_ru

    class CustomPerson(person.Person):

        class Meta:
            name = 'custom_person'

    g = Generic()
    person_ = person.Person(seed=g.seed)
    custom_person = CustomPerson(seed=g.seed)
    g.add_provider(CustomPerson)

    assert g.custom_person.name() == custom_person.name()
    g.locale = 'ru'
    ru_person = person_ru.Person(seed=g.seed)
    assert g.custom_person.name() == ru_person.name()
    assert g.custom_person.name() != person_.name()


# Generated at 2022-06-14 00:10:34.591096
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Season(BaseProvider):
        class Meta:
            name = 'season'

        def _get_formatted_month(self, date_time_format: str) -> str:
            """Format date and add a month.

            :param date_time_format: Format of datetime.
            :return: Formatted date in Spanish.
            """
            dt = self.datetime('es')
            return dt.format(date_time_format)

        def winter(self):
            return self._get_formatted_month('%B')

    gen = Generic('en')
    gen.add_provider(Season)
    assert gen.season.winter() == "January"



# Generated at 2022-06-14 00:10:41.486261
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.travel import Travel
    custom_provider = Travel
    generic = Generic('en')
    generic.add_provider(custom_provider)
    assert issubclass(custom_provider, BaseProvider)
    assert generic.travel.seed == generic.seed
    assert generic.travel.__class__ == custom_provider


# Generated at 2022-06-14 00:10:49.788942
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Generic.__getattr__()."""
    from mimesis.providers.address import Address as _Address
    from mimesis.providers.date import Datetime as _Datetime
    from mimesis.providers.food import Food as _Food
    from mimesis.providers.person import Person as _Person
    from mimesis.providers.science import Science as _Science
    from mimesis.providers.text import Text as _Text
    gen = Generic()

    assert isinstance(gen.person, _Person)
    assert isinstance(gen.address, _Address)
    assert isinstance(gen.datetime, _Datetime)
    assert isinstance(gen.food, _Food)
    assert isinstance(gen.text, _Text)
    assert isinstance(gen.science, _Science)

    # Check

# Generated at 2022-06-14 00:10:55.500257
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        class Meta:
            name = 'MyProvider'

    provider = Generic()
    provider.add_provider(MyProvider)
    assert provider.MyProvider.__class__.__name__ == 'MyProvider'

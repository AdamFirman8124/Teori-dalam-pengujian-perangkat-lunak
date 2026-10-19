

# Generated at 2022-06-14 00:05:52.148825
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""
    g = Generic('en')
    g.add_provider(Person)
    g.add_provider(Address)
    assert not hasattr(g, 'person')
    assert not hasattr(g, 'address')
    g.person
    g.address
    assert hasattr(g, 'person')
    assert hasattr(g, 'address')


# Generated at 2022-06-14 00:05:58.838617
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    test = Generic()
    class CustomProvider(BaseProvider):
        class Meta:
            name = 'custom_provider'
    test.add_provider(CustomProvider)
    assert test.custom_provider.__class__.__name__ == 'CustomProvider'


# Generated at 2022-06-14 00:06:04.794306
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        def __init__(self) -> None:
            super().__init__()

        def foo(self) -> None:
            pass

    g = Generic('en')
    g.add_provider(CustomProvider)

    assert hasattr(g, 'custom_provider')
    assert hasattr(g.custom_provider, 'foo')


# Generated at 2022-06-14 00:06:10.794059
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    data = Generic()
    assert data.person.name(gender='male') == 'Justin'
    assert data.person.surname(gender='male') == 'Powell'
    assert data.datetime.datetime(
        minimum=-3600) > '2017-09-08 17:53:23'
    assert data.datetime.datetime() < '2017-09-08 17:53:23'

# Generated at 2022-06-14 00:06:23.135198
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.file import File
    from mimesis.providers.hardware import Hardware
    from mimesis.providers.code import Code
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.cryptographic import Cryptographic
    from mimesis.providers.person import Person
    from mimesis.providers.text import Text
    from mimesis.providers.business import Business
    from mimesis.providers.date import Datetime
    from mimesis.providers.address import Address
    from mimesis.providers.science import Science
    from mimesis.providers.choice import Choice
    from mimesis.providers.payment import Payment
    from mimesis.providers.internet import Internet
    from mimesis.providers.path import Path

# Generated at 2022-06-14 00:06:32.090841
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    # test get an provider
    generic = Generic()
    assert generic.person.full_name() == 'Perry Rodriguez'

    # test get an address
    assert generic.address.city() == 'Monroe'

    # test get an datetime
    assert generic.datetime.date(start='2017-01-01', end='2017-12-31')

    # test get an business
    assert generic.business.bic('russia') == '044525593'
    assert generic.business.vatin('russia') == '7661446569'

    # test get an text
    assert generic.text.sentence(quantifier=('a', 'b')) == 'b b b'

    # test get an food
    assert generic.food.fruits() == 'cherry'

    # test get an science

# Generated at 2022-06-14 00:06:40.831457
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """This module provide the basic functionality to add providers.
    """
    from mimesis.builtins.custom_provider import Custom
    from mimesis.enums import Gender
    from mimesis.builtins.custom_provider import (
        CustomProviders as CustomProvidersEnum,
    )
    generic = Generic()
    # Add the Custom provider
    generic.add_provider(Custom)
    data_provider = generic.custom

    # Get the phone number
    data = data_provider.phone_number()
    assert data

    # Get a date
    data = data_provider.date(start=1980, end=2000, fmt='%Y-%m-%d')
    assert data

    # Get the name of a character
    data = data_provider.name(gender=Gender.MALE)


# Generated at 2022-06-14 00:06:50.512168
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    gen = Generic()
    assert (gen.person() != '')
    assert (gen.address() != '')
    assert (gen.datetime() != '')
    assert (gen.business() != '')
    assert (gen.text() != '')
    assert (gen.food() != '')
    assert (gen.science() != '')
    assert (gen.transport() != '')
    assert (gen.choice() != '')
    assert (gen.code() != '')
    assert (gen.unit_system() != '')
    assert (gen.file() != '')
    assert (gen.numbers() != '')
    assert (gen.development() != '')
    assert (gen.hardware() != '')
    assert (gen.clothing() != '')
    assert (gen.internet() != '')

# Generated at 2022-06-14 00:06:56.345496
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        ...

    # Normal usage
    try:
        Generic().add_provider(CustomProvider)
    except TypeError:
        assert False
    else:
        assert True

    # If custom provider is not a subclass of BaseProvider
    try:
        Generic().add_provider(object)
    except TypeError:
        assert True
    else:
        assert False

    # If custom provider is not a class
    try:
        Generic().add_provider(CustomProvider())
    except TypeError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 00:07:06.007135
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from .custom_provider import MyProvider
    from .custom_provider import MyProviderV2
    
    my_provider = MyProvider()
    my_provider_v2 = MyProviderV2()

    gen = Generic()
    gen.add_provider(my_provider.__class__)
    gen.add_provider(my_provider_v2.__class__)
    
    assert gen.my_provider_v2
    assert gen.my_provider_v2.provider_name == 'MyProviderV2'
    assert gen.my_provider
    assert gen.my_provider.provider_name == 'MyProvider'


# Generated at 2022-06-14 00:07:31.727884
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic('en')
    assert generic.person.full_name() == 'John Parker'
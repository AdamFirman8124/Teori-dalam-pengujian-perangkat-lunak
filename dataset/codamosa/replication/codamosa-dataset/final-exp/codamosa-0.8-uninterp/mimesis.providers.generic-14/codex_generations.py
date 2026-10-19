

# Generated at 2022-06-14 00:06:01.054146
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g.person is not None
    assert isinstance(g.person, Person)
    assert g.text is not None
    assert isinstance(g.text, Text)


# Generated at 2022-06-14 00:06:06.947006
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def method(self) -> int:
            return 0
    gen = Generic()
    try:
        gen.add_provider(CustomProvider)
        assert True
    except TypeError:
        assert False


# Generated at 2022-06-14 00:06:12.649168
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    provider.add_provider(MyProvider)
    assert 'myprovider' in dir(provider)



# Generated at 2022-06-14 00:06:16.110242
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    generic = Generic()
    result = generic.random.__class__.__name__
    assert result == 'Random'

# Generated at 2022-06-14 00:06:26.458734
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic(seed=1)
    assert isinstance(g.business, Business)
    assert isinstance(g.food, Food)
    assert isinstance(g.science, Science)
    assert isinstance(g.transport, Transport)
    assert isinstance(g.code, Code)
    assert isinstance(g.unit_system, UnitSystem)
    assert isinstance(g.file, File)
    assert isinstance(g.numbers, Numbers)
    assert isinstance(g.development, Development)
    assert isinstance(g.hardware, Hardware)
    assert isinstance(g.clothing, Clothing)
    assert isinstance(g.internet, Internet)
    assert isinstance(g.path, Path)
    assert isinstance(g.payment, Payment)
    assert isinstance(g.cryptographic, Cryptographic)


# Generated at 2022-06-14 00:06:35.573166
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.builtins import SpainSpecProvider

    generic = Generic(locale='en')
    provider1 = RussiaSpecProvider
    provider2 = SpainSpecProvider

    generic.add_provider(provider1)
    assert generic.russia
    assert not hasattr(generic, '_russia')
    generic.add_provider(provider2)
    assert generic.spain
    assert not hasattr(generic, '_spain')



# Generated at 2022-06-14 00:06:39.183666
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()
    assert g.person
    g.add_provider(Person)
    assert g.person
    assert g.person_
    g.add_provider(Address)
    assert g.address
    assert g.address_
    g.add_provider(Datetime)
    assert g.datetime
    assert g.datetime_

# Generated at 2022-06-14 00:06:42.166954
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test getting attribute without underscore."""

    generic = Generic()
    generic.add_provider(Provider)
    generic.provider()
    assert Provider.count == 1


# Generated at 2022-06-14 00:06:49.448053
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test for method __getattr__."""
    provider = Generic()
    assert hasattr(provider, '__getattr__')
    assert isinstance(provider.name, Person)
    provider.add_provider(Person)
    assert isinstance(provider.person, Person)



# Generated at 2022-06-14 00:06:59.493186
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from tests.test_providers.test_classes.custom_providers import (
        CustomProvider,
        ProviderFactory
    )

    generic = Generic()

    # add CustomProvider
    generic.add_provider(CustomProvider)
    assert hasattr(generic, 'custom')

    # add ProviderFactory
    generic.add_provider(ProviderFactory)
    assert hasattr(generic, 'provider_factory')

    # add List of providers
    generic.add_providers(CustomProvider, ProviderFactory)
    assert hasattr(generic, 'custom')
    assert hasattr(generic, 'provider_factory')

# Generated at 2022-06-14 00:07:26.643062
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    assert isinstance(generic.person, Person)
    assert isinstance(generic.address, Address)
    assert isinstance(generic.datetime, Datetime)
    assert isinstance(generic.business, Business)
    assert isinstance(generic.text, Text)
    assert isinstance(generic.food, Food)
    assert isinstance(generic.science, Science)
# test_Generic___getattr__()


# Generated at 2022-06-14 00:07:31.533224
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.other import Junk
    g = Generic()
    g.add_provider(Junk)
    assert hasattr(g, 'junk')
    assert isinstance(g.junk, Junk)



# Generated at 2022-06-14 00:07:35.855639
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    gen = Generic('ru')
    gen.add_provider(MyProvider)
    assert gen.myprovider.get_provider_name() == 'MyProvider'


# Generated at 2022-06-14 00:07:51.229134
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class FakeProvider(BaseProvider):
        pass

    generic = Generic()
    generic.add_provider(FakeProvider)
    assert 'fakeprovider' in dir(generic), \
        'Failed to add simple provider'
    assert isinstance(generic.fakeprovider, FakeProvider), \
        'Failed to add simple provider'
    assert generic.fakeprovider._seed == generic._seed, 'Unsuccessful test of seed'
    assert generic.fakeprovider._locale == generic._locale, 'Unsuccessful test of locale'

    class FakeProviderMeta(BaseProvider):
        class Meta:
            name = 'custom_provider'

    generic = Generic()
    generic.add_provider(FakeProviderMeta)
    assert 'custom_provider' in dir(generic), \
        'Failed to add provider with meta'

# Generated at 2022-06-14 00:07:55.773368
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic"""
    class MyProvider(BaseProvider):
        class Meta:
            name = 'my_provider'
    
    d = Generic()
    d.add_provider(MyProvider)
    assert hasattr(d, 'my_provider')
    assert not isinstance(getattr(d, 'my_provider'), classmethod)


# Generated at 2022-06-14 00:08:00.235444
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic(seed=42)
    providers = BaseProvider.__subclasses__()
    providers_list = list(providers)

    # Count of providers in Generic() object
    count_before = len(generic.__dict__)
    count_after = len(providers_list) + count_before

    # Generate providers for Generic object
    for provider in providers_list:
        generic.add_provider(provider)

    count_providers_in_object = len(generic.__dict__)

    # Check that providers was added
    assert (count_after == count_providers_in_object), "Providers wasn't added. Expected {}, but was {}".format(
        count_after, count_providers_in_object)


# Generated at 2022-06-14 00:08:02.060857
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic()
    generic.add_provider(Person)



# Generated at 2022-06-14 00:08:05.588663
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.cryptographic import Cryptographic
    g = Generic()
    g.add_provider(Cryptographic)
    assert isinstance(g.cryptographic, Cryptographic)


# Generated at 2022-06-14 00:08:13.579966
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    # The __getattr__ method of class Generic will call method
    # _method of class BaseDataProvider(if it is available),
    # so test for available method
    assert hasattr(generic, 'person')
    assert hasattr(generic, 'address')
    assert hasattr(generic, 'business')
    assert hasattr(generic, 'text')
    assert hasattr(generic, 'food')
    assert hasattr(generic, 'science')
    assert hasattr(generic, 'development')
    assert hasattr(generic, 'hardware')
    assert hasattr(generic, 'clothing')
    assert hasattr(generic, 'internet')
    assert hasattr(generic, 'path')
    assert hasattr(generic, 'payment')
    assert hasattr(generic, 'cryptographic')

# Generated at 2022-06-14 00:08:24.907434
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # Step 1. Add provider
    # Case 1.1. Successful adding
    # Case 1.2. Faulty adding (class is not a subclass of BaseProvider)
    # Case 1.3. Faulty adding (it's not a class)
    # Step 2. Adding many providers at a time
    # Case 2.1. Successful adding

    # Create instance of class Generic
    generic = Generic()

    # Step 1. Add provider
    # Case 1.1. Successful adding
    generic.add_provider(Person)
    assert generic.person is not None, 'Failed to add provider'

    # Case 1.2. Faulty adding (class is not a subclass of BaseProvider)

# Generated at 2022-06-14 00:08:49.359508
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        class Meta:
            name = 'custom_provider'

        def get_something(self):
            return 'something'

    g = Generic()
    g.add_provider(CustomProvider)

    assert hasattr(g, 'custom_provider')
    assert isinstance(g.custom_provider, CustomProvider)



# Generated at 2022-06-14 00:08:55.682854
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    from mimesis.providers.person import Person
    from mimesis.exceptions import FieldValueError

    generic = Generic('en')
    assert isinstance(generic.person, Person)
    assert generic.person.full_name() == 'David Shaw'

    with pytest.raises(AttributeError):
        generic.not_attribute

    with pytest.raises(FieldValueError):
        generic.person.not_action()



# Generated at 2022-06-14 00:09:03.972504
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.field = 'my_field'

    my_provider = Generic()
    my_provider.add_provider(MyProvider)
    assert my_provider.my_provider.field == 'my_field'



# Generated at 2022-06-14 00:09:11.676412
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for method add_provider of class Generic."""
    provider = Generic()
    class CustomProvider(BaseProvider):
        class Meta:
            """Class for metadata."""

            name = 'custom'
        def random_test(self):
            """..."""
            return "test"

    provider.add_provider(CustomProvider)
    assert hasattr(provider, 'custom')
    assert hasattr(provider.custom, 'random_test')


# Generated at 2022-06-14 00:09:14.235161
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class TestProvider(BaseProvider):
        class Meta:
            name = 'test_provider'
    gen = Generic()
    assert 'test_provider' not in dir(gen)
    gen.add_provider(TestProvider)
    assert 'test_provider' in dir(gen)



# Generated at 2022-06-14 00:09:18.978678
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person as P

    tmax = 0.1
    provider = Generic('ru')
    for i in range(10000):
        start = time.time()
        provider.person
        provider.person
        provider.person
        provider.person
        end = time.time()
        t = end - start
        tmax = max(tmax, t)
        if tmax > 0.1:
            raise AssertionError('Failed because {} > 0.1'.format(tmax))

    p1 = provider.person
    p2 = provider.person

    assert not p1 == p2
    assert not p1.occupation() == p2.occupation()
    assert not p1.birthday() == p2.birthday()

# Generated at 2022-06-14 00:09:29.273517
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        class Meta:
            name = 'custom'

        def foo(self) -> str:
            return 'foo'

    obj = Generic()
    obj.add_provider(CustomProvider)

    assert obj.custom.foo() == 'foo'
    assert not hasattr(obj, '_custom')

# Generated at 2022-06-14 00:09:35.059074
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider

    class CustomProvider(BaseProvider):
        pass

    g = Generic()
    g.add_provider(CustomProvider)
    assert hasattr(g, 'custom_provider')



# Generated at 2022-06-14 00:09:42.554102
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for add_provider method of class Generic."""
    class Provider(BaseProvider):
        def foo(self):
            return 'bar'

    generic = Generic()
    generic.add_provider(Provider)

    assert generic.provider.foo() == 'bar'

    # Test case when provider has name
    class Provider(BaseProvider):
        class Meta:
            name = 'foo'
        def foo(self):
            return 'bar'

    generic = Generic()
    generic.add_provider(Provider)

    assert generic.foo.foo() == 'bar'

# Generated at 2022-06-14 00:09:54.035517
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    assert inspect.isclass(Generic._person)
    assert inspect.isclass(Generic._address)
    assert inspect.isclass(Generic._datetime)
    assert inspect.isclass(Generic._choice)

    assert issubclass(Generic._person, BaseProvider)
    assert issubclass(Generic._address, BaseProvider)
    assert issubclass(Generic._datetime, BaseProvider)
    assert issubclass(Generic._choice, BaseProvider)

    g = Generic()
    assert isinstance(g.person, Generic._person)
    assert isinstance(g.address, Generic._address)
    assert isinstance(g.datetime, Generic._datetime)
    assert isinstance(g.choice, Generic._choice)


# Generated at 2022-06-14 00:10:21.347523
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.person import Person
    from mimesis.providers.address import Address
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.business import Business
    from mimesis.providers.text import Text
    from mimesis.providers.food import Food
    from mimesis.providers.science import Science
    from mimesis.providers.transport import Transport
    from mimesis.providers.code import Code
    from mimesis.providers.units import UnitSystem
    from mimesis.providers.file import File
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.development import Development
    from mimesis.providers.hardware import Hardware

# Generated at 2022-06-14 00:10:27.542130
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test method add_provider"""
    class TestProvider(BaseProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def do_something(self):
            return 'Doing something'

    generic = Generic()
    generic.add_provider(TestProvider)
    assert generic.test_provider.do_something() == 'Doing something'

# Generated at 2022-06-14 00:10:32.869742
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for add_provider of class Generic."""
    generic = Generic()
    provider = Business()
    generic.add_provider(provider)

    assert provider.__dict__ == generic.business.__dict__


# Generated at 2022-06-14 00:10:36.736465
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic(seed=123)
    assert generic.person.name() == "Юрий"


# Generated at 2022-06-14 00:10:45.247660
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    g.seed = 10
    g.locale = 'ru'

    person = g.person
    assert person.full_name() == 'Елена Крамарь'
    assert person.full_name(gender='male') == 'Юрий Бурцев'
    assert person.full_name(gender='female') == 'Надежда Рябцева'
    assert person.full_name(middle_name=True) == 'Елена Вадимовна Крамарь'

# Generated at 2022-06-14 00:10:54.922859
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider
    generic = Generic()
    class CustomProvider(BaseProvider):
        def foo(self):
            return 'bar'

    assert 'custom' not in dir(generic)

    generic.add_provider(CustomProvider)

    assert 'custom' in dir(generic)
    assert generic.custom.foo() == 'bar'

    try:
        generic.add_provider(1)
    except TypeError:
        pass
    else:
        raise AssertionError('The provider must be a class')


# Generated at 2022-06-14 00:11:04.721644
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        class Meta:
            name = 'my_provider'
            class_type = 'static'


        def my_provider_method(self, *args, **kwargs):
            print('My provider method')

    g = Generic()
    assert not hasattr(g, 'my_provider')

    g.add_provider(MyProvider)
    assert hasattr(g, 'my_provider')


# Generated at 2022-06-14 00:11:09.737773
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()

    assert hasattr(g, 'choice')
    assert not hasattr(g, 'foo')
    g.add_provider(Test)
    assert hasattr(g, 'foo')


# Generated at 2022-06-14 00:11:16.455576
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    provider = Generic('uk')
    assert provider.person.full_name() == 'Ирина Анубис'
    assert provider.person.full_name(gender=provider.person.GENDER.MALE) ==\
        'Феликс Шевченко'
    assert provider.person.full_name(gender=provider.person.GENDER.FEMALE) ==\
        'Валентина Усманова'


# Generated at 2022-06-14 00:11:19.590831
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic: Generic = Generic()
    assert generic.person.last_name()
    assert generic.address.latitude()



# Generated at 2022-06-14 00:11:38.069750
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():

    class Provider(BaseProvider):
        """Test provider."""

        class Meta:
            """Class for metadata."""

            name = 'test_provider'

        def some_data(self) -> str:
            """This method doesn't conflict with other method."""
            return 'test'

    g = Generic()
    assert g.__dict__.get('test_provider') is None

    g.add_provider(Provider)
    assert g.test_provider.some_data() == 'test'


# Generated at 2022-06-14 00:11:49.112683
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test add_provider method of class Generic."""
    assert Generic().add_provider(Person)
    assert Generic().add_provider(Address)
    assert Generic().add_provider(Datetime)
    assert Generic().add_provider(Business)
    assert Generic().add_provider(Text)
    assert Generic().add_provider(Food)
    assert Generic().add_provider(Science)
    assert Generic().add_provider(Transport)
    assert Generic().add_provider(Code)
    assert Generic().add_provider(UnitSystem)
    assert Generic().add_provider(File)
    assert Generic().add_provider(Numbers)
    assert Generic().add_provider(Development)
    assert Generic().add_provider(Hardware)
    assert Generic().add_provider(Clothing)
   

# Generated at 2022-06-14 00:11:56.857325
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    gen = Generic()
    def cls1():
        class Cls1(BaseProvider):
            class Meta:
                name = 'cls1'

            def foo(self):
                return 'bar'

    gen.add_provider(cls1)
    assert gen.cls1().foo() == 'bar'

    class Cls2(BaseProvider):
        class Meta:
            name = 'cls2'

        def foo(self):
            return 'bar'

    gen.add_provider(Cls2)
    assert gen.cls2().foo() == 'bar'

# Generated at 2022-06-14 00:12:00.089401
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test for method __getattr__ of class Generic."""
    g = Generic('en')
    assert g.random_int(1, 10) == 2


# Generated at 2022-06-14 00:12:03.518882
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    provider.add_provider(Locale)
    assert provider.locale is not None


# Generated at 2022-06-14 00:12:10.798257
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.code import Code
    from mimesis.providers.text import Text
    generic = Generic("ru")
    assert generic.add_provider(Numbers)
    assert generic.add_provider(Code)
    assert generic.add_provider(Text)
    assert "numbers" in dir(generic)
    assert "code" in dir(generic)
    assert "text" in dir(generic)



# Generated at 2022-06-14 00:12:20.104233
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    import pytest
    from mimesis.providers.transport import Transport

    generic = Generic('ru')
    generic.add_provider(Transport)
    assert callable(generic.transport.plane)
    with pytest.raises(TypeError) as e:
        generic.add_provider(UnitSystem)
    assert str(e.value) == 'The provider must be a subclass of BaseProvider'
    with pytest.raises(TypeError) as e:
        generic.add_provider(10)
    assert str(e.value) == 'The provider must be a class'


# Generated at 2022-06-14 00:12:21.877181
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for the provider adding to class Generic."""
    from mimesis.providers.datetime import Datetime
    from mimesis.enums import Gender
    generic = Generic('en')
    generic.add_provider(Datetime)



# Generated at 2022-06-14 00:12:37.518538
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        def __init__(self, locale: str = '', seed: int = None) -> None:
            super().__init__(locale=locale, seed=seed)

        def method(self) -> str:
            return 'test'

    class MyProvider2(BaseProvider):
        class Meta:
            name = 'test_class'

        def __init__(self, locale: str = '', seed: int = None) -> None:
            super().__init__(locale=locale, seed=seed)

        def method(self) -> str:
            return 'test'

    generic = Generic()
    generic.add_provider(MyProvider)
    assert generic.my_provider.method() == 'test'

    generic = Generic()

# Generated at 2022-06-14 00:12:41.630465
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Provider(BaseProvider):
        class Meta:
            name = 'test'

        def foo(self):
            pass

    g = Generic()
    g.add_provider(Provider)

    assert hasattr(g, 'test')
    assert hasattr(g.test, 'foo')

# Generated at 2022-06-14 00:13:13.873463
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    for method in ['add_provider', 'add_providers']:
        with pytest.raises(TypeError):
            Generic().__getattribute__(method)(5)
        with pytest.raises(TypeError):
            Generic().__getattribute__(method)('str')
        with pytest.raises(TypeError):
            Generic().__getattribute__(method)(
                BaseProvider)
        with pytest.raises(TypeError):
            Generic().__getattribute__(method)(
                BaseDataProvider)
        with pytest.raises(TypeError):
            Generic().__getattribute__(method)(
                Generic)
        with pytest.raises(TypeError):
            Generic().__getattribute__(method)(
                CustomBase)
        Generic().__getattribute__(method)(CustomProvider)
        Generic().__

# Generated at 2022-06-14 00:13:20.781589
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Prov(BaseProvider):
        class Meta:
            name = 'prov'

    g = Generic()
    assert not hasattr(g, 'prov')
    g.add_provider(Prov)
    assert hasattr(g, 'prov')
    assert isinstance(g.prov, Prov)


# Generated at 2022-06-14 00:13:26.821520
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for add_provider method."""
    from mimesis.providers.misc import Misc

    generic = Generic()
    generic.add_provider(Misc)
    assert 'misc' in dir(generic)



# Generated at 2022-06-14 00:13:35.518594
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    import unittest

    class BaseProvider(object):
        class Meta(object):
            name = 'my_provider'

    class CustomProvider(BaseProvider):
        pass

    class TestCase(unittest.TestCase):
        def test__check_for_class(self):
            gen = Generic()
            with self.assertRaises(TypeError):
                gen.add_provider('Not a class')

        def test__check_for_subclass(self):
            gen = Generic()
            with self.assertRaises(TypeError):
                gen.add_provider(BaseProvider)

        def test__check_for_name(self):
            gen = Generic()
            gen.add_provider(CustomProvider)
            self.assertTrue(hasattr(gen, 'my_provider'))


# Generated at 2022-06-14 00:13:37.480195
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Provider(BaseProvider):
        class Meta:
            name = 'provider'

        def test(self) -> str:
            return 'test'

    gen = Generic()
    gen.add_provider(Provider)
    assert gen.provider.test() == 'test'



# Generated at 2022-06-14 00:13:43.290260
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    import unittest
    from mimesis.providers.custom.extras import Extras

    class TestCase(unittest.TestCase):
        def test_add_provider(self):
            g = Generic()
            g.add_provider(Extras)
            self.assertEqual(g.extras.protocol(), 'http')

    unittest.main()

# Generated at 2022-06-14 00:13:55.494169
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for adding provider.

    :return: None
    """

    generic = Generic()
    assert 'seed' not in generic

    class Seed(BaseProvider):
        """Custom provider."""

        class Meta:
            """Class for metadata."""

            name = 'seed'

        def __init__(self, *args, **kwargs) -> None:
            """Initialize attributes.

            :param args: Arguments.
            :param kwargs: Keyword arguments.
            """
            super().__init__(*args, **kwargs)

        def seed(self) -> int:
            """Get the seed.

            :return: Seed.
            """
            return self.random.seed()

    generic.add_provider(Seed)
    assert generic.seed.seed() == generic.seed.seed()

# Generated at 2022-06-14 00:14:04.489518
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        def test(self):
            return self.random.randint(0, 10)

    c = Generic()
    c.add_provider(CustomProvider)

    assert isinstance(c.custom_provider.test(), int)
    assert c.custom_provider.test() <= 10

    c = Generic()
    c.add_providers(CustomProvider)
    assert isinstance(c.custom_provider.test(), int)
    assert c.custom_provider.test() <= 10


# Generated at 2022-06-14 00:14:07.866344
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.movie import Movie
    
    generic = Generic()

    assert generic.add_provider(Movie) == None
    assert generic.movie.__class__.__name__ == 'Movie'


# Generated at 2022-06-14 00:14:16.644062
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for Generic.add_provider method."""
    data = Generic()
    data.add_provider(Person)
    assert data.person is not None

    data.add_provider(Address)
    assert data.address is not None

    data.add_provider(Datetime)
    assert data.datetime is not None

    data.add_provider(Business)
    assert data.business is not None

    data.add_provider(Text)
    assert data.text is not None

    data.add_provider(Food)
    assert data.food is not None

    data.add_provider(Choice)
    assert data.choice is not None

    data.add_provider(Structure)
    assert data.structure is not None

    data.add_provider(Cryptographic)
    assert data

# Generated at 2022-06-14 00:14:42.182650
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    assert generic.name


# Generated at 2022-06-14 00:14:55.272035
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.person import Person
    from mimesis.providers.business import Business
    class CustomProvider(BaseProvider):
        def gen_some_string(self):
            return 'random data'
    try:
        g = Generic()
        g.add_provider(Person)
        assert g.person is not None
        g.add_provider(Business)
        assert g.business is not None
        g.add_provider(CustomProvider)
        assert g.CustomProvider is not None
        assert g.CustomProvider.gen_some_string() == 'random data'
    except Exception as e:
        print("Exception occur: {}".format(e))
        assert False


# Generated at 2022-06-14 00:14:58.737469
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():

    class CustomProvider(BaseProvider):
        class Meta:
            name = 'custom_provider'

    g = Generic()
    g.add_provider(CustomProvider)
    assert isinstance(g.custom_provider, CustomProvider)


# Generated at 2022-06-14 00:15:06.008237
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.generic import Generic
    from mimesis.providers.base import BaseProvider
    generic = Generic('en')
    class CustomProvider(BaseProvider):
        def foo(self):
            pass
    generic.add_provider(CustomProvider)
    assert 'customprovider' in dir(generic)
    assert 'foo' in dir(generic.customprovider)


# Generated at 2022-06-14 00:15:09.300622
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic(seed=777)
    assert g.file is None
    g.add_provider(File)
    assert g.file is not None



# Generated at 2022-06-14 00:15:13.156401
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider."""
    from mimesis.providers.code import Code
    generic = Generic()
    assert not hasattr(generic, 'code')
    generic.add_provider(Code)
    assert hasattr(generic, 'code')



# Generated at 2022-06-14 00:15:18.246644
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class TestProvider(BaseProvider):
        @property
        def bad_word(self) -> str:
            return 'bad'

    g = Generic()
    g.add_provider(TestProvider)

    assert g.test_provider.bad_word == 'bad'
    g.add_provider("Hello world")



# Generated at 2022-06-14 00:15:30.632427
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    
    assert g.person.full_name() == 'Doris Jacobs'
    assert g.address.city() == 'North Randy'
    assert g.datetime.timestamp() == 1520681536
    assert g.business.company() == 'Furniture'
    assert g.text.sentence() == 'Sed magnam maiores sit quaerat.'
    assert g.food.fruit() == 'Orange'
    assert g.science.is_isbn13() == False
    assert g.transport.make() == 'Chevrolet'
    assert g.code.md5hash() == '132b0f5dad5de5d5dcd939a3a3ade2e1'
    assert g.unit_system.imperial_weight() == '0.651 (Lb)'


# Generated at 2022-06-14 00:15:31.775592
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass

# Generated at 2022-06-14 00:15:39.421937
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic"""
    class CustomProvider(BaseProvider):
        """Custom provider class."""

        class Meta:
            """Meta class."""

            name = 'custom_provider'

    generic = Generic()
    generic.add_provider(CustomProvider)
    assert hasattr(generic, 'custom_provider')

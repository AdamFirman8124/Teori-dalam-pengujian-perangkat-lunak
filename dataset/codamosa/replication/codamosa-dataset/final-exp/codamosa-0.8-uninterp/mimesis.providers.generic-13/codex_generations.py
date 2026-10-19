

# Generated at 2022-06-14 00:05:56.853974
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass

# Generated at 2022-06-14 00:06:08.942738
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    g = Generic()
    assert g.person.name() == 'Luther'
    assert g.address.room() == '172A'
    assert g.datetime.month() == 'June'
    assert g.business.company() == 'Dorothy House'
    assert g.text.title() == 'Dangerous alliance'
    assert g.food.fruit() == 'Grapefruit'
    assert g.science.chemical_element_name() == 'Barium'
    assert g.transport.vehicle() == 'Road Tractor'
    assert g.code.isbn() == '978-3-16-148410-0'
    assert g.unit_system.length_unit() == 'Foot'

# Generated at 2022-06-14 00:06:13.887715
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    import pytest
    from mimesis.providers.person import Person

    generic = Generic()
    assert isinstance(generic._person, Person)
    assert isinstance(generic.person, Person)


# Generated at 2022-06-14 00:06:20.123522
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""
    # Test method add_provider of class Generic
    gen = Generic()
    gen.add_provider(Person)
    gen.add_provider(Science)
    gen.add_provider(BaseDataProvider)
    gen.add_provider(BaseProvider)
    assert hasattr(gen, 'person') and hasattr(gen, 'science')

# Generated at 2022-06-14 00:06:30.074065
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic(seed=10)

    assert isinstance(g.person, Person)
    assert isinstance(g.address, Address)
    assert isinstance(g.datetime, Datetime)
    assert isinstance(g.business, Business)
    assert isinstance(g.text, Text)
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


# Generated at 2022-06-14 00:06:36.014467
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for method add_provider of class Generic."""
    from mimesis.providers.person import Person as PersonProvider
    generic = Generic('en')
    generic.add_provider(PersonProvider)
    assert generic.person is not None
    assert generic.person.full_name() == 'Rebecca Broome'



# Generated at 2022-06-14 00:06:47.816603
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # Test with subclass of BaseProvider
    class TestProvider(BaseProvider):
        class Meta:
            name = 'test_provider'

        def test_method(self):
            return 'This is a test method'

    generic = Generic()
    # Add TestProvider
    generic.add_provider(TestProvider)
    # Check if it is added
    assert hasattr(generic, 'test_provider')
    assert hasattr(generic.test_provider, 'test_method')
    assert generic.test_provider.test_method() == 'This is a test method'

    # Test with non-subclass of BaseProvider
    class TestProvider2:
        class Meta:
            name = 'test_provider2'

        def test_method(self):
            return 'This is a test method'

    # Check if TypeError is

# Generated at 2022-06-14 00:06:53.336174
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        class Meta:
            name = 'custom_provider'

        def example_method(self):
            return 'Hello World!'

    g = Generic()

    assert 'custom_provider' not in g.__dict__.keys()

    g.add_provider(CustomProvider)

    assert 'custom_provider' in g.__dict__.keys()
    assert g.custom_provider.example_method() == 'Hello World!'


# Generated at 2022-06-14 00:06:56.339439
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
     from mimesis.providers.person import Person, Gender

     gen = Generic()
     g = gen.person()
     assert isinstance(g, Person)
     print(g.full_name(gender=Gender.FEMALE))



# Generated at 2022-06-14 00:07:00.324715
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    gen = Generic()
    gen.add_provider(Person)
    assert gen.person is not None

# Generated at 2022-06-14 00:07:31.380616
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.identifier import PersonIdentifier
    from mimesis.providers.company import Company
    from mimesis.providers.person import Person
    from mimesis.providers.company import Company
    from mimesis.providers.file import File
    from mimesis.providers.payment import Payment
    from mimesis.providers.internet import Internet
    from mimesis.providers.text import Text
    from mimesis.providers.misc import Misc
    class Addr(BaseProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    g = Generic("pl")

# Generated at 2022-06-14 00:07:39.328197
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for add_provider()."""
    g = Generic()
    class MyProvider(BaseProvider):
        class Meta:
            """Class for metadata."""
            name = 'my_provider'
        def __call__(self):
            pass
    g.add_provider(MyProvider)
    assert g.my_provider
    assert isinstance(g.my_provider, MyProvider)


# Generated at 2022-06-14 00:07:54.877518
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test that a custom provider can be added to Generic() object."""
    class TestProvider(BaseProvider):
        """Test Data Provider."""

        class Meta:
            """Class for metadata."""

            name = 'test'

        def __init__(self, *args, **kwargs):
            """Initialize attributes."""
            super().__init__(*args, **kwargs)
            self.some_data = 42

        def to_str(self):
            """Return some data."""
            return str(self.some_data)

    class TestProvider2(BaseProvider):
        """Test Data Provider."""

        class Meta:
            """Class for metadata."""

            name = 'test2'

        def __init__(self, *args, **kwargs):
            """Initialize attributes."""

# Generated at 2022-06-14 00:07:57.702726
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    gr = Generic()
    assert gr.person.__class__.__name__ == 'Person'
    assert gr.address.__class__.__name__ == 'Address'
    assert gr.datetime.__class__.__name__ == 'Datetime'
    assert gr.business.__class__.__name__ == 'Business'
    assert gr.text.__class__.__name__ == 'Text'
    assert gr.food.__class__.__name__ == 'Food'
    assert gr.science.__class__.__name__ == 'Science'


# Generated at 2022-06-14 00:08:05.941290
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test the method add_provider of class Generic."""
    generic_object = Generic()
    assert not hasattr(generic_object, 'my_provider')
    from mimesis.providers.mimesis import Mimesis
    generic_object.add_provider(Mimesis)
    assert hasattr(generic_object, 'mimesis')
    assert callable(generic_object.mimesis)
    assert isinstance(generic_object.mimesis, Mimesis)



# Generated at 2022-06-14 00:08:09.290857
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    MyProvider = BaseProvider()
    provider.add_provider(MyProvider)
    assert isinstance(provider.my_provider, MyProvider)
    assert provider.my_provider.seed == provider.seed

# Generated at 2022-06-14 00:08:16.906389
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Custom(BaseProvider):
        """Custom class."""

        class Meta:
            """Meta class."""
            name = 'custom'

        def foo(self) -> str:
            """Foo function."""
            return 'bar'

    g = Generic()
    g._add_provider(Custom)
    assert hasattr(g, 'custom')
    assert callable(g.custom.foo)
    assert g.custom.foo() == 'bar'



# Generated at 2022-06-14 00:08:20.732338
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    assert Generic().add_provider(cls=Text)

# Generated at 2022-06-14 00:08:22.448558
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""
    g = Generic()



# Generated at 2022-06-14 00:08:25.392356
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.network import Network
    g = Generic()
    g.add_provider(Network)
    assert hasattr(g, 'network')
    assert callable(getattr(g, 'network'))

# Generated at 2022-06-14 00:08:47.611313
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""
    a = Generic()
    assert not hasattr(a, 'edureka')
    a.add_provider(Edureka)
    assert hasattr(a, 'edureka')


# Generated at 2022-06-14 00:08:54.094886
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseDataProvider
    from mimesis.providers.card import Card
    g = Generic()
    g.add_provider(BaseDataProvider)
    try:
        g.add_provider(Card)
    except TypeError:
        pass
    else:
        raise Exception



# Generated at 2022-06-14 00:08:58.263030
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        class Meta:
            name = 'my_provider'

        def my_provider(self):
            return 'my_provider'

    generic = Generic()
    generic.add_provider(MyProvider)
    assert generic.my_provider.my_provider() == 'my_provider'

# Generated at 2022-06-14 00:09:01.381339
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    test_obj = Generic("en", 1)
    assert test_obj.person
    assert test_obj.address


# Generated at 2022-06-14 00:09:13.270989
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.address import Address
    from mimesis.providers.business import Business
    from mimesis.providers.person import Person
    from mimesis.providers.datetime import Datetime
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

# Generated at 2022-06-14 00:09:18.711231
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic('en')
    class Person(BaseProvider):
        def some_method(self):
            print('Hello')
    generic.add_provider(Person)
    generic.person.some_method()
    assert generic.person.some_method() == None

# Generated at 2022-06-14 00:09:34.057566
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """ Unit test for method add_provider of class Generic. """
    from mimesis.enums import Gender
    class MyPersonProvider(Person):
        class Meta:
            name = 'custom_person'

        def get_full_name(self, gender: Gender = None) -> str:
            if gender == Gender.NEUTRAL:
                parts = [self.random_element(self._data['name']['neutral'])]
            else:
                parts = [
                    self.random_element(self._data['name']['male']),
                    self.random_element(self._data['name']['female']),
                ]
            parts.append(self.random_element(self._data['surname']))
            return super().get_full_name(gender) + self.separator().join(parts)




# Generated at 2022-06-14 00:09:39.699936
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    try:
        assert Generic().person
        assert Generic().address
        assert Generic().datetime
        assert Generic().business
        assert Generic().text
        assert Generic().food
        assert Generic().science
    except AssertionError:
        raise AssertionError()


# Generated at 2022-06-14 00:09:43.584941
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    pass

# Generated at 2022-06-14 00:09:52.647913
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.example import Example
    from mimesis.enums import Gender
    my_provider = Generic(seed=42)
    my_provider.add_provider(Example)
    assert my_provider.example.full_name(gender=Gender.MALE) == 'Алексеев Максим'
    assert my_provider.example.full_name(gender=Gender.FEMALE) == 'Елизарова Ульяна'

# Generated at 2022-06-14 00:10:22.844911
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test _Generic.__getattr__."""

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
    assert isinstance

# Generated at 2022-06-14 00:10:32.060840
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.converter import Converter
    from mimesis.providers.probability import Probability
    from mimesis.providers.food import Food
    g = Generic()
    g.add_provider(Converter)
    g.add_provider(Probability)
    g.add_provider(Food)
    assert g.converter.degrees_to_radians(180) == 3.141592653589793
    assert g.probability.percent() == '73'
    assert g.food.food('dairy') == 'milk'


# Generated at 2022-06-14 00:10:34.632141
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class TestProvider(BaseProvider):
        def foo(self):
            return 'foo'
    gen = Generic()
    gen.add_provider(TestProvider)
    assert gen.test_provider.foo() == 'foo'

# Generated at 2022-06-14 00:10:42.664433
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class LocaleProvider(BaseProvider):
        def locale(self) -> str:
            return "en_US"

    g = Generic("::1")
    assert g.__dict__.get("locale_provider") is None
    g.add_provider(LocaleProvider)
    assert isinstance(g.locale_provider, LocaleProvider)
    assert g.locale_provider.locale() == "en_US"


# Generated at 2022-06-14 00:10:47.751293
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()

    class CustomProvider(BaseProvider):
        def get_something(self):
            return 'something'

    g.add_provider(CustomProvider)
    assert g.custom_provider.get_something() == 'something'


# Generated at 2022-06-14 00:10:49.637397
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g._person.full_name() == g.person.full_name()


# Generated at 2022-06-14 00:10:57.215702
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        class Meta:
            name = 'custom'

    class CustomProvider2(BaseProvider):
        class Meta:
            name = 'custom2'

    g = Generic(languages=['en'], timezone='Europe/Kiev')
    g.add_provider(CustomProvider)
    g.add_provider(CustomProvider2)

    assert g.custom
    assert g.custom2

# Generated at 2022-06-14 00:11:13.441619
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""
    class MyProvider(BaseProvider):

        class Meta:
            """Class for metadata."""

            name = 'provider'

        def hello_from_custom_provider(self):
            print("Hello from custom provider!")

    g = Generic(seed=42)
    g.add_provider(provider=MyProvider)

    p1 = MyProvider(seed=42)
    p2 = g.provider()

    assert p1.get_provider_name() == 'provider'
    assert p2.get_provider_name() == 'provider'
    assert p1.hello_from_custom_provider() == p2.hello_from_custom_provider()


# Generated at 2022-06-14 00:11:18.591317
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Test method __getattr__ of class Generic."""
    from mimesis import Generic
    g = Generic()
    person = g.person()
    assert person.name()
    assert person.full_name()

# Generated at 2022-06-14 00:11:20.166594
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    provider = Generic()
    provider.__getattr__('person')

# Generated at 2022-06-14 00:11:44.429637
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.development import CSharp
    from mimesis.providers.structure import SQL
    from mimesis.providers.unit_system import ImperialUnits

    g = Generic()
    g.add_provider(CSharp)
    g.add_provider(SQL)
    g.add_provider(ImperialUnits)
    assert g.csharp()
    assert g.sql()
    assert g.imperial_units()
    assert callable(g.csharp)
    assert callable(g.sql)
    assert callable(g.imperial_units)

# Generated at 2022-06-14 00:11:49.501692
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Unit test for method add_provider of class Generic."""

    class MyProvider(BaseProvider):
        def foo(self):
            return 'MyProvider'

    generic = Generic()
    generic.add_provider(MyProvider)

    assert hasattr(generic, 'myprovider')
    assert generic.myprovider.foo() == 'MyProvider'



# Generated at 2022-06-14 00:11:54.036035
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic('en')
    assert generic.person is not None
    assert generic.address is not None
    assert generic.datetime is not None
    assert generic.business is not None
    assert generic.text is not None
    assert generic.food is not None
    assert generic.science is not None


# Generated at 2022-06-14 00:12:03.446072
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.development import Development, Development
    dev_1 = Development(seed=0)
    dev_2 = Development(seed=0)
    gen_1 = Generic(seed=0)
    gen_2 = Generic(seed=0)

    assert gen_1.development.provider_name == 'development'
    assert gen_2.development.provider_name == 'development'
    assert gen_1.development.platform == dev_1.platform
    assert gen_2.development.platform == dev_2.platform
    assert gen_1.development.methods == dev_1.methods
    assert gen_2.development.methods == dev_2.methods

    gen_1.add_provider(Development)
    gen_2.add_providers(Development)

# Generated at 2022-06-14 00:12:06.819991
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Provider(BaseProvider):
        class Meta:
            name = 'provider'

        def do(self) -> str:
            return 'test'

    gen = Generic()
    gen.add_provider(Provider)
    assert gen.provider.do() == 'test'

# Generated at 2022-06-14 00:12:19.219629
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic('ru')
    attr = g.__getattr__('person')
    assert(attr.username())
    assert(attr.full_name())
    assert(attr.password())
    assert(attr.address.address())
    assert(attr.address.city())
    assert(attr.address.country())
    assert(attr.address.address())
    assert(attr.address.postal_code())
    assert(attr.address.latitude())
    assert(attr.address.longitude())
    assert(attr.datetime.date())
    assert(attr.datetime.datetime())
    assert(attr.datetime.time())
    assert(attr.datetime.timestamp())
    assert(attr.datetime.month())
    assert(attr.datetime.year())

# Generated at 2022-06-14 00:12:20.589115
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    Generic().add_provider(Person)
    


# Generated at 2022-06-14 00:12:23.336847
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.person import Person
    def test():
        a=Generic()
        a.add_provider(Person)
        return a
    test()

# Generated at 2022-06-14 00:12:39.047857
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.development.cpp import Cpp
    from mimesis.providers.development.csharp import CSharp
    from mimesis.providers.development.html import Html
    from mimesis.providers.development.java import Java
    from mimesis.providers.development.javascript import Javascript
    from mimesis.providers.development.python import Python
    from mimesis.providers.development.ruby import Ruby
    from mimesis.providers.development.swift import Swift

    data = Generic()
    data.add_provider(Cpp)
    data.add_provider(CSharp)
    data.add_provider(Html)
    data.add_provider(Java)
    data.add_provider(Javascript)

# Generated at 2022-06-14 00:12:51.820830
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    from mimesis.providers.address import Address as ADR
    from mimesis.providers.business import Business as BNS
    from mimesis.providers.datetime import Datetime as DTT
    from mimesis.providers.food import Food as FD
    from mimesis.providers.person import Person as PRS
    from mimesis.providers.science import Science as SC
    from mimesis.providers.text import Text as TXT

    g = Generic()
    assert isinstance(g.person, PRS)
    assert isinstance(g.address, ADR)
    assert isinstance(g.datetime, DTT)
    assert isinstance(g.business, BNS)
    assert isinstance(g.text, TXT)
    assert isinstance(g.food, FD)

# Generated at 2022-06-14 00:13:25.453358
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class CustomProvider(BaseProvider):
        """Custom provider example."""
        def __init__(self, seed: int = None) -> None:
            super().__init__(seed=seed)

        class Meta:
            """Class for metadata."""
            name = 'custom_provider'

    generic = Generic()
    generic.add_provider(CustomProvider)

    assert hasattr(generic, 'custom_provider')

# Generated at 2022-06-14 00:13:26.422266
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    pass

# Generated at 2022-06-14 00:13:29.288587
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    m = Generic()
    m.add_provider(Text)
    assert m.text is not None


# Generated at 2022-06-14 00:13:33.838691
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class MyProvider(BaseProvider):
        class Meta:
            name = 'my_provider'

        def foo(self):
            return 'foo'

    generic = Generic()

    generic.add_provider(MyProvider)

    assert hasattr(generic, 'my_provider')
    assert generic.my_provider.foo() == 'foo'


# Generated at 2022-06-14 00:13:43.180063
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    assert hasattr(Generic(), 'person')
    assert hasattr(Generic(), 'food')
    assert hasattr(Generic(), 'datetime')
    assert hasattr(Generic(), 'address')
    assert hasattr(Generic(), 'business')
    assert hasattr(Generic(), 'text')
    assert hasattr(Generic(), 'science')
    assert hasattr(Generic(), 'transport')
    assert hasattr(Generic(), 'clothing')
    assert hasattr(Generic(), 'file')
    assert hasattr(Generic(), 'numbers')
    assert hasattr(Generic(), 'development')
    assert hasattr(Generic(), 'hardware')
    assert hasattr(Generic(), 'internet')
    assert hasattr(Generic(), 'path')
    assert hasattr(Generic(), 'payment')
    assert hasattr(Generic(), 'cryptographic')

# Generated at 2022-06-14 00:13:52.974865
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.utils import random_int

    class CustomProvider(BaseProvider):
        def __init__(self, seed: int = None, *args, **kwargs):
            super().__init__(seed)

        class Meta:
            name = 'custom'

        def func(self):
            return random_int(1, 10)

    generic = Generic()

    pr = CustomProvider()
    generic.add_provider(pr)

    a = generic.custom.func()
    b = generic.custom.func()
    assert a != b

# Generated at 2022-06-14 00:13:59.783282
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    """Unit test for method __getattr__ of class Generic."""
    g = Generic()

    attr = getattr(g, 'person')
    assert isinstance(attr, Person)

    attr = getattr(g, 'address')
    assert isinstance(attr, Address)

    attr = getattr(g, 'datetime')
    assert isinstance(attr, Datetime)

    attr = getattr(g, 'business')
    assert isinstance(attr, Business)

    attr = getattr(g, 'text')
    assert isinstance(attr, Text)

    attr = getattr(g, 'food')
    assert isinstance(attr, Food)

    attr = getattr(g, 'science')
    assert isinstance(attr, Science)



# Generated at 2022-06-14 00:14:09.705376
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    g.__getattr__('person')
    g.__getattr__('address')
    g.__getattr__('datetime')
    g.__getattr__('business')
    g.__getattr__('text')
    g.__getattr__('food')
    g.__getattr__('science')
    g.__getattr__('transport')
    g.__getattr__('code')
    g.__getattr__('unit_system')
    g.__getattr__('file')
    g.__getattr__('numbers')
    g.__getattr__('development')
    g.__getattr__('hardware')
    g.__getattr__('clothing')
    g.__getattr__('internet')
    g.__getattr__('path')

# Generated at 2022-06-14 00:14:14.163083
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test if the new provider works."""
    g = Generic('en')
    g.add_provider(Code)
    assert g.code.true_false() == g._code(seed=g.seed).true_false()
    assert hasattr(g, 'code')



# Generated at 2022-06-14 00:14:22.560848
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from .providers.weather import Weather
    from .providers.music import Music
    weather = Weather(seed=123)
    music = Music(seed=123)
    generic = Generic('en', seed=123)
    generic.add_provider(weather)
    generic.add_provider(music)
    assert 'weather' in dir(generic)
    assert 'music' in dir(generic)
    assert weather.__dict__ == generic.weather.__dict__
    assert music.__dict__ == generic.music.__dict__

# Generated at 2022-06-14 00:15:17.187069
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic()
    assert('datetime' in dir(generic))


# Generated at 2022-06-14 00:15:29.911130
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.person import Person as PersonProvider
    from mimesis.providers.address import Address as AddressProvider
    from mimesis.providers.other import Other as OtherProvider
    from mimesis.providers.business import Business as BusinessProvider
    from mimesis.base import BaseSpecProvider

    # Normal execution
    generic = Generic()
    generic.add_provider(PersonProvider)
    generic.add_provider(AddressProvider)
    generic.add_provider(OtherProvider)
    generic.add_provider(BusinessProvider)

    # Normal execution, call by class name
    generic = Generic()
    generic.add_provider(PersonProvider())
    generic.add_provider(AddressProvider())
    generic.add_provider(OtherProvider())
    generic.add_provider(BusinessProvider())



# Generated at 2022-06-14 00:15:37.752537
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    assert 'hello' not in provider.__dict__

    class Hello(BaseProvider):
        def say_hello(self):
            return 'Hello'
    provider.add_provider(Hello)

    assert 'hello' in provider.__dict__
    assert provider.hello.say_hello() == 'Hello'

    class Hi(BaseProvider):
        def say_hi(self):
            return 'Hi'
    provider.add_provider(Hi)

    assert 'hi' in provider.__dict__
    assert provider.hi.say_hi() == 'Hi'


# Generated at 2022-06-14 00:15:45.912327
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    import mimesis
    from mimesis.builtins import RussiaSpecProvider

    class Person(RussiaSpecProvider):
        """Person class."""

        class Meta:
            """Class for metadata."""

            name = 'person'
            """Name of provider."""

    assert mimesis.Generic()._person.__class__ == mimesis.Person
    assert mimesis.Generic().person.__class__ == mimesis.Person

    generic = mimesis.Generic()
    generic.add_provider(Person)

    assert generic.person.__class__ == Person

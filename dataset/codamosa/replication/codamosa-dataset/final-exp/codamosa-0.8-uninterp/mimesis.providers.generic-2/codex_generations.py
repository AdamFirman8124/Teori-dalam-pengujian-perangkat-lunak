

# Generated at 2022-06-14 00:06:11.363025
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    assert g.person.full_name
    assert g.business.company_name
    assert g.transport.car.brand
    assert g.science.chemical_element
    assert g.code.semver
    assert g.unit_system.temperature
    assert g.file.extension
    assert g.numbers.decimal
    assert g.development.random_boolean
    assert g.hardware.cpu.model
    assert g.clothing.shirt.color
    assert g.internet.ipv4
    assert g.path.home
    assert g.payment.visa
    assert g.cryptographic.hash
    assert g.structure.uuid
    assert g.choice.elements(['a', 'b', 'c'])


# Generated at 2022-06-14 00:06:20.692901
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.config import Config
    from mimesis.providers.person import Person
    class TestProvider(BaseProvider):

        @classmethod
        def _file(cls) -> str:
            """Return name of data file."""
            return 'test.json'

        class Meta:
            """Class for metadata."""

            name = 'testprovider'

    test_provider = TestProvider
    generic = Generic()
    generic.add_provider(test_provider)
    assert generic.testprovider # pass


# Generated at 2022-06-14 00:06:25.176402
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    generic = Generic()
    generic.add_provider(Generic)
    assert 'generic' in dir(generic)
    generic.add_provider(Generic)
    assert len(dir(generic)) == 1


# Generated at 2022-06-14 00:06:31.793465
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    """Test for method add_provider of class Generic."""
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.base import BaseDataProvider

    class NewProvider(BaseProvider):
        def method(self):
            return self.__class__.__name__

    class NewDataProvider(BaseDataProvider):
        def method(self):
            return self.__class__.__name__

    gen = Generic('en')
    gen.add_provider(NewProvider)
    gen.add_provider(NewDataProvider)

    assert gen.new_provider.method() == 'NewProvider'
    assert gen.new_data_provider.method() == 'NewDataProvider'

# Generated at 2022-06-14 00:06:35.178745
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic('en')
    person = generic.person
    assert person != None
    assert type(person) == Person

# Generated at 2022-06-14 00:06:41.025293
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class A(BaseProvider):
        class Meta:
            name = 'A'

        def add_provider(self, cls):
            self.a = 'a'

    class B(BaseProvider):
        class Meta:
            name = 'B'

        def add_provider(self, cls):
            self.b = 'b'

    class C(BaseProvider):
        class Meta:
            name = 'c'

        def add_provider(self, cls):
            self.c = 'c'

    generic = Generic()
    generic.add_provider(A)
    generic.add_provider(B)
    generic.add_provider(C)
    assert generic.A.a == 'a'
    assert generic.B.b == 'b'

# Generated at 2022-06-14 00:06:45.433303
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers import numbers

    class _Numbers(numbers.Numbers):

        class Meta:
            name = 'foo'

    generic = Generic('ru')
    assert isinstance(generic.foo, _Numbers)
    assert generic.foo.seed == generic.seed

# Generated at 2022-06-14 00:06:54.662338
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic()
    print(g.person)
    print(g.address)
    print(g.datetime)
    print(g.business)
    print(g.text)
    print(g.food)
    print(g.science)
    print(g.transport)
    print(g.code)
    print(g.unit_system)
    print(g.file)
    print(g.numbers)
    print(g.development)
    print(g.hardware)
    print(g.clothing)
    print(g.internet)
    print(g.path)
    print(g.payment)
    print(g.cryptographic)
    print(g.structure)
    print(g.choice)


# Generated at 2022-06-14 00:07:01.652140
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Custom(BaseProvider):
        class Meta:
            name = 'custom_provider'

        def foo(self):
            return 'bar'

    data = Generic()
    data.add_provider(Custom)
    assert hasattr(data, 'custom_provider')
    assert data.custom_provider.foo() == 'bar'


# Generated at 2022-06-14 00:07:04.329846
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    from mimesis.providers.develop import Development
    generic = Generic()
    generic.add_provider(Development)
    assert generic.development.provider



# Generated at 2022-06-14 00:06:06.388284
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class Car(BaseProvider):
        def get_model(self):
            model = ["sport", "crossover", "sedan", "hatchback"]
            return self.random.choice(model)

    def get_random_provider():
        print(Generic().add_provider(Car).choice)

    for _ in range(5):
        get_random_provider()



# Generated at 2022-06-14 00:06:08.646695
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    provider.add_provider(BaseProvider)
    assert hasattr(provider, "baseprovider")


# Generated at 2022-06-14 00:06:20.374165
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    from functools import partial
    from mimesis.enums import Gender
    from mimesis.random import Random
    from test.utils import DATA_PROVIDERS
    from mimesis.providers.person import Person
    from mimesis.providers.person import Person as CustomPerson
    generic = Generic()
    
    # Without custom providers
    data_providers = [str(i.__class__.__name__).split('.')[-1]
                      for i in DATA_PROVIDERS]
    for i in generic.__dir__():
        assert str(i) in data_providers

    pl = Random().choice(DATA_PROVIDERS)
    provider_name = str(pl.__class__.__name__).split('.')[-1].lower()

# Generated at 2022-06-14 00:06:30.086036
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    a = Generic()
    print(a.person)
    print(a.business)
    print(a.datetime)
    print(a.address)
    print(a.text)
    print(a.food)
    print(a.science)
    print(a.transport)
    print(a.code)
    print(a.unit_system)
    print(a.file)
    print(a.numbers)
    print(a.development)
    print(a.hardware)
    print(a.clothing)
    print(a.internet)
    print(a.path)
    print(a.payment)
    print(a.cryptographic)
    print(a.structure)
    print(a.choice)


# Generated at 2022-06-14 00:06:39.910808
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    g = Generic(seed=0)
    assert g.person.name(sex='male') == 'Степан'
    assert g.person.name(sex='female') == 'Торук'
    assert g.address.address() == 'ЗБИМ'
    assert g.datetime.datetime(tzinfo=True) == \
           'Ср, 16 Лан 3000 15:24:23 +03:00'
    assert g.business.company() == 'Федяш'
    assert g.text.sentence() == 'Адип'
    assert g.food.vegetable() == 'Кальдэ'
    assert g.science.molecule() == 'Сикватин'

# Generated at 2022-06-14 00:06:50.056909
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    import pytest
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.person import Personal
    from mimesis.providers.person import PersonDataProvider
    from mimesis.providers import Person

    class MyPerson(Person):
        """Custom Provider."""

        class Meta:
            """Provider metadata."""

            name = 'my_person'

    def my_person(locale: str = 'en') -> Person:
        """Create custom provider.

        :param locale: Locale code.
        :return: Provider.
        """
        return MyPerson(locale=locale, seed=1)

    class CustomPerson(Person):
        """Custom Provider."""

        class Meta:
            """Provider metadata."""


# Generated at 2022-06-14 00:06:50.907179
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    pass



# Generated at 2022-06-14 00:06:54.127962
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    provider = Generic()
    assert hasattr(provider, 'text')
    from mimesis.providers.text import Text
    provider.add_provider(Text)
    assert hasattr(provider, 'text')


# Generated at 2022-06-14 00:06:55.526663
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    # If a provider is not a class
    provider = BaseProvider()
    generic = Generic()
    generic.add_provider(provider)


# Generated at 2022-06-14 00:07:01.147693
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    try:
        x = Generic()
        person = Generic().person
        print('Type is : {}'.format(type(person)))
        assert True
    except Exception as e:
        print(e)
        assert False
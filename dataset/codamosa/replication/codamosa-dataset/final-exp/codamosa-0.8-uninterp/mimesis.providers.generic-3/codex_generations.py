

# Generated at 2022-06-14 00:05:50.341377
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    g = Generic()
    assert not hasattr(g, '_provider_1')
    g.add_provider(Provider)
    assert hasattr(g, 'provider1')


# Generated at 2022-06-14 00:05:56.724114
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    a = Generic(seed=2562)
    a.person.full_name()
    assert a.person.full_name() == 'Jared Brown'

# There is not need to test the remaining methods 
# because they are already tested in tests/test_providers

# Generated at 2022-06-14 00:06:00.917578
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    test = Generic()
    assert not hasattr(test, 'add_provider')
    test.add_provider(Generic)
    assert hasattr(test, 'add_provider')


# Generated at 2022-06-14 00:06:03.237307
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class TestProvider(BaseProvider):
        class Meta:
            name = 'test'

        def foo(self):
            return 'bar'


# Generated at 2022-06-14 00:06:07.512744
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    # Given
    person = Generic(seed=123456789)

    # When
    gender = person.gender

    # Then
    assert gender == 'Female'
    assert isinstance(gender, str)



# Generated at 2022-06-14 00:06:14.106634
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    gen_obj = Generic('en')
    assert 'movies' not in dir(gen_obj)

    from mimesis.providers.movies import Movies
    gen_obj.add_provider(Movies)
    assert 'movies' in dir(gen_obj)

    from mimesis.providers.joke import Joke
    gen_obj.add_provider(Joke)
    assert 'joke' in dir(gen_obj)

# Generated at 2022-06-14 00:06:16.566013
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    obj = Generic('en')
    assert isinstance(obj.datetime, Datetime)



# Generated at 2022-06-14 00:06:26.227756
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    generic = Generic()
    person = generic.person
    address = generic.address
    datetime = generic.datetime
    business = generic.business
    text = generic.text
    food = generic.food
    science = generic.science
    assert (person.__class__.__name__ == 'Person'
            and address.__class__.__name__ == 'Address'
            and datetime.__class__.__name__ == 'Datetime'
            and business.__class__.__name__ == 'Business'
            and text.__class__.__name__ == 'Text'
            and food.__class__.__name__ == 'Food'
            and science.__class__.__name__ == 'Science')

# Generated at 2022-06-14 00:06:38.320312
# Unit test for method __getattr__ of class Generic
def test_Generic___getattr__():
    # Testing with Person provider
    person_obj = Generic().person
    assert isinstance(person_obj, Person)

    # Testing with Address provider
    address_obj = Generic().address
    assert isinstance(address_obj, Address)

    # Testing with Datetime provider
    datetime_obj = Generic().datetime
    assert isinstance(datetime_obj, Datetime)

    # Testing with Business provider
    business_obj = Generic().business
    assert isinstance(business_obj, Business)

    # Testing with Text provider
    text_obj = Generic().text
    assert isinstance(text_obj, Text)

    # Testing with Food provider
    food_obj = Generic().food
    assert isinstance(food_obj, Food)

    # Testing with Science provider
    science_obj = Generic().science

# Generated at 2022-06-14 00:06:44.017587
# Unit test for method add_provider of class Generic
def test_Generic_add_provider():
    class FooProvider(BaseProvider):
        class Meta:
            name = 'foo_provider'

        def bar(self) -> str:
            return 'bar'

        @property
        def baz(self):
            return 'baz'

    generic = Generic()
    generic.add_provider(FooProvider)


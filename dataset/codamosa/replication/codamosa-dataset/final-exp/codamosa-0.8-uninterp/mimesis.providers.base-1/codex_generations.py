

# Generated at 2022-06-13 23:50:42.652542
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        _datafile = 'test.json'

        def get_random_item(self, data: dict = None) -> dict:
            with self.override_locale('ru') as provider:
                return provider._data

    test_provider = TestProvider(locale='en')
    data = test_provider.get_random_item()
    assert data['test'] == 'test'
    data = test_provider.get_random_item()
    assert data['test'] == 'тест'

# Generated at 2022-06-13 23:50:48.763942
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    from mimesis.providers.person import Person as Per

    with Person().override_locale('sk') as person:
        assert person._data == Per()._data
    with Per().override_locale('sk') as person:
        assert person._data['male_first_names'] == ['Adam', 'Adrian', 'Anton']

# Generated at 2022-06-13 23:50:55.499801
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test : method ``override_locale`` of class ``BaseDataProvider``.
    """
    class MockProvider(BaseDataProvider):
        """Mock provider."""
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes for data providers.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale=locale, seed=seed)

    provider = MockProvider(locales.EN)

    with provider.override_locale(locales.EN):
        assert provider.locale == locales.EN

    with provider.override_locale(locales.RU):
        assert provider.locale == locales.RU



# Generated at 2022-06-13 23:51:04.046719
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider.

    This method tests the use of the method override_locale of class
    BaseDataProvider.
    """
    from mimesis.providers.address import Address

    with Address().override_locale('ru') as address:
        assert address.get_current_locale() == 'ru'
        assert address.get_city() != 'New York'

    with Address().override_locale('en') as address:
        assert address.get_current_locale() == 'en'
        assert address.get_city() == 'New York'
    try:
        with Address().override_locale('ru'):
            pass
    except ValueError:
        pass

# Generated at 2022-06-13 23:51:12.008102
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeProvider(BaseDataProvider):
        __methods__ = (
            'fake_method',
        )

        def fake_method(self):
            return self.get_current_locale()

    p = FakeProvider()
    assert p.fake_method() == locales.DEFAULT_LOCALE

    with FakeProvider().override_locale(locales.RU) as p:
        assert p.fake_method() == locales.RU

    assert p.fake_method() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:17.564841
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider.

    :return: True if test is succeeded.
    """
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    class TestPerson(Person):
        """Class to test method override_locale of class BaseDataProvider."""

        def __init__(self, locale: str = locales.EN) -> None:
            """Initialize attributes.

            :param locale: Locale.
            """
            super().__init__(locale=locale)

    # prepare data
    p1 = TestPerson()
    p1.seed = '2009271328'
    p2 = TestPerson(locale='ru')
    p2.seed = '2009271328'

    # check
    assert p1.full_name

# Generated at 2022-06-13 23:51:23.470407
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.locales import RU, EN

    class TestProvider(BaseDataProvider):

        def __init__(self, locale=EN, seed=None):
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test'

    tp = TestProvider(locale=RU, seed=None)
    assert tp.get_curre

# Generated at 2022-06-13 23:51:31.277280
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest

    class TestProvider(BaseDataProvider):
        _datafile = 'person.json'

        def __init__(self):
            super().__init__(locale='ru-RU', seed=2)

        def name(self):
            return 'Seed: {}'.format(self.seed)

    provider = TestProvider()
    with pytest.raises(ValueError):
        with provider.override_locale('ru'):
            provider.name()

    provider = TestProvider()
    with provider.override_locale('ru'):
        assert provider.name() == 'Seed: 2'

    with provider.override_locale('en'):
        assert provider.name() == 'Seed: 2'


# Generated at 2022-06-13 23:51:41.167377
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class LocaleDependentProvider(BaseDataProvider):

        def __init__(self):
            super().__init__()

        def get_current_locale(self):
            return 'en'

    class NotLocaleDependentProvider(BaseDataProvider):
        def __init__(self):
            super().__init__()

    ldp = LocaleDependentProvider()
    with ldp.override_locale('ru') as provider:
        current_locale = provider.get_current_locale()
    assert current_locale == 'ru'
    nldp = NotLocaleDependentProvider()
    with nldp.override_locale('ru'):
        pass

# Generated at 2022-06-13 23:51:43.909639
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale_dependant_provider = BaseDataProvider(locale=locales.EN)
    locale_dependant_provider.override_locale(locales.EN)

# Generated at 2022-06-13 23:52:02.386258
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # initialize data provider
    provider = BaseDataProvider()

    # check
    assert provider.locale == locales.DEFAULT_LOCALE
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

    # reset locale
    provider.locale = locales.EN

    # check
    assert provider.locale == locales.EN
    assert provider.get_current_locale() == locales.EN

    # override locale
    override_locale = provider.override_locale(locales.RU)

    # check
    with override_locale as provider1:
        assert provider1.locale == locales.RU
        assert provider1.get_current_locale() == locales.RU

    # check
    assert provider.locale == locales.EN
    assert provider.get

# Generated at 2022-06-13 23:52:11.236126
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DataProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None):
            super().__init__(locale=locale, seed=seed)

        def get_current_locale(self):
            return self.locale

    dp = DataProvider('en')
    assert dp.get_current_locale() == 'en'
    with dp.override_locale('ru') as dp:
        assert dp.get_current_locale() == 'ru'
    assert dp.get_current_locale() == 'en'

# Generated at 2022-06-13 23:52:25.026499
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.food import Food
    from mimesis.builtins.usability import Usability
    import pytest
    from random import choice

    def get_restore_locale(provider: BaseDataProvider) -> str:
        """Get the locale and restore it.

        :param provider: Any instance of BaseDataProvider.
        :return: current locale.
        """
        locale = provider.locale
        provider._override_locale(locales.EN)
        return locale

    def test_raise_attribute_error():
        """Test raise of AttributeError.

        :raises AttributeError: Raised if attribute
         'locale' not exists in instance.
        """
        us = Usability()

# Generated at 2022-06-13 23:52:34.792103
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed=None):
            super().__init__(locale=locale, seed=seed)

        @property
        def data(self) -> JSON:
            return self._data

    provider = Provider()
    with provider.override_locale('ru') as data:
        assert data.get_current_locale() == 'ru'

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE
    assert provider._data == {}



# Generated at 2022-06-13 23:52:38.809158
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        pass

    provider = Provider()

    def test_func():
        with provider.override_locale(locale='ru'):
            assert provider.get_current_locale() == 'ru'

    test_func()
    assert provider.get_current_locale() == 'en'

    print(repr(provider))



# Generated at 2022-06-13 23:52:43.360616
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    p = Person()
    with p.override_locale():
        assert p.get_current_locale() == 'en'
        
    # Unit test for method _pull of class BaseDataProvider

# Generated at 2022-06-13 23:52:52.183135
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override_locale method.

    But normally it is required to use context manager in unit test,
    e.g. ``with provider.override_locale('es')``.
    """
    from mimesis.builtins import Person
    from mimesis.enums import Gender

    provider = Person()
    assert provider.locale == locales.EN

    provider_with_new_locale = provider.override_locale(locales.RU)
    assert isinstance(provider_with_new_locale, Person)
    assert provider_with_new_locale.locale == locales.RU

    for _ in range(10):
        assert provider_with_new_locale.full_name(gender=Gender.FEMALE) != provider.full_name(gender=Gender.FEMALE)


# Generated at 2022-06-13 23:52:52.766558
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:53:07.394725
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider"""
    class _TestLocale(BaseDataProvider):
        """Test class of BaseDataProvider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None
                     ) -> None:
            super().__init__(locale=locale, seed=seed)
            self.locale = locale

    test = _TestLocale()
    with test.override_locale('kk') as inner:
        assert inner.get_current_locale() == 'kk'
        assert test.get_current_locale() == 'en'
        assert str(inner) == '<_TestLocale kk>'
        assert str(test) == '<_TestLocale en>'

# Generated at 2022-06-13 23:53:21.035578
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    _test_data = {'test': 'специальный'}
    _test_locale ='ru'
    _test_origin_locale = 'en'
    _test_datafile = 'test_override_locale.json'

    with open(_test_datafile, 'w+', encoding='utf-8') as f:
        json.dump(_test_data, f)

    class TestDataProvider(BaseDataProvider):
        """TestDataProvider."""

        def __init__(self, locale=_test_origin_locale, seed=None):
            super().__init__(locale=locale, seed=seed)
            self._datafile = _test_datafile

        def test_func(self):
            self.test_data = self._data

   

# Generated at 2022-06-13 23:53:37.914761
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self):
            super().__init__(locale='en')
            self._datafile = 'data.json'
            self._data = self._pull()

        def foo(self):
            return self.random.choice(self._data['foo'])

    provider = Provider()
    assert provider.foo() in ['bar', 'baz', 'qaz']
    with provider.override_locale(locale='ru'):
        assert provider.foo() in ['привет', 'мир']
    assert provider.foo() in ['bar', 'baz', 'qaz']
    assert provider.locale == locales.EN
    assert provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:53:49.279816
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class TestProvider(BaseDataProvider):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def __str__(self) -> str:
            """Human-readable representation of locale."""
            locale = getattr(self, 'locale', locales.DEFAULT_LOCALE)
            return '{} <{}>'.format(self.__class__.__name__, locale)

    provider = TestProvider('ru')
    assert provider.get_current_locale() == 'ru'

    with provider.override_locale('en'):
        assert provider.get_current_locale() == 'en'

    assert provider.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:53:55.826215
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    r = BaseDataProvider(seed=1)
    assert r.get_current_locale() == locales.DEFAULT_LOCALE
    with r.override_locale(locale='fr'):
        assert r.get_current_locale() == 'fr'
    assert r.get_current_locale() == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:54:04.437121
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    p = BaseDataProvider('es')
    assert p._pull.cache_info().currsize == 1

    with p.override_locale('ru'):
        assert p._pull.cache_info().currsize == 1
        assert p._datafile == 'test.json'

    assert p._pull.cache_info().currsize == 1



# Generated at 2022-06-13 23:54:13.086074
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class _TestProvider(BaseDataProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._datafile = 'test.json'

        def get_city(self) -> str:
            return self._data['city']

    provider = _TestProvider(locale='ru')

    with provider.override_locale('en'):
        city = provider.get_city()

    assert city == 'London'

# Generated at 2022-06-13 23:54:23.500668
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method 'override_locale' of BaseDataProvider class."""

    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    # create instances
    p1 = Person(locale='ru')
    p2 = Person(locale='en')
    p3 = Person(locale='ru')
    a1 = Address(locale='ru')
    a2 = Address(locale='en')

    # test of get_current_locale
    assert p1.get_current_locale() == 'ru'
    assert p2.get_current_locale() == 'en'

    # test of override_locale
    with p1.override_locale('en'):
        assert p1.get_current_locale() == 'en'


# Generated at 2022-06-13 23:54:27.184613
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    locale_1 = provider.get_current_locale()
    with provider.override_locale(locales.EN):
        locale_2 = provider.get_current_locale()
    locale_3 = provider.get_current_locale()

    assert locale_1 != locale_2
    assert locale_1 == locale_3



# Generated at 2022-06-13 23:54:32.005307
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        class Meta:
            code = 'test_provider'
            name = 'Test Provider'


        def __init__(self, locale=locales.EN, seed=None):
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test.json'

        def get_data(self, key: str) -> Dict[str, Any]:
            return self._data.get(key, {})
        """``get_data`` method returns the data by ``key`` from JSON."""

    p = Provider('ru')

    assert p.locale == 'ru'


# Generated at 2022-06-13 23:54:37.992867
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    class MyProvider(BaseDataProvider):
        """Test class."""

        def __init__(self, locale=locales.EN, seed=None):
            """Init function."""
            super().__init__(locale=locale, seed=seed)

        def something(self):
            """Test method."""
            return self.locale

    provider = MyProvider()
    with provider.override_locale(locales.RU):
        assert provider.locale == locales.RU

    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:54:47.558401
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Subclass(BaseDataProvider):
        def __init__(self, locale=locales.EN):
            super().__init__(locale=locale)
            self._datafile = 'file.json'
        def get_current_locale(self):
            return 'ru'

    with pytest.raises(ValueError):
        Subclass().override_locale(locale='ru')

    with pytest.raises(UnsupportedLocale):
        Subclass(locale='AA').override_locale(locale='ru')

    result = Subclass(locale='en').override_locale(locale='ru')
    assert result is not None
    assert len(result._pull.cache_info().misses) == 1

    result = Subclass(locale='en-US').override_locale

# Generated at 2022-06-13 23:55:12.306085
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    units = [{'name': 'Metric', 'symbol': 'm'},
            {'name': 'Centimeter', 'symbol': 'cm'},
            {'name': 'Kilometer', 'symbol': 'km'}]
    lengths = {'Metric': units[0:2], 'Imperial': units}

    class TestProvider(BaseDataProvider):
        def test(self, locale: str) -> Dict:
            return self.lengths(locale)

        @property
        def lengths(self) -> Dict:
            return lengths


    tp = TestProvider()
    assert tp.test('en') == lengths[0:2]

    tp = TestProvider()

# Generated at 2022-06-13 23:55:18.136521
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Testing override_locale."""
    from mimesis.builtins import Builtins

    buitins = Builtins()
    original_locale = buitins.get_current_locale()

    assert original_locale == locales.DEFAULT_LOCALE

    with buitins.override_locale(locales.RU):
        assert buitins.get_current_locale() == locales.RU

    assert buitins.get_current_locale() == original_locale

# Generated at 2022-06-13 23:55:24.612880
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Example usage of context manager «override_locale»."""
    import mimesis.builtins
    from mimesis.enums import Gender

    locale = locales.EN
    user_data = mimesis.builtins.User(locale=locale)
    with user_data.override_locale(locales.RU):
        assert user_data.gender() == Gender.MASCULINE

    mimesis.builtins.User(locale=locale)
    mimesis.builtins.User(locale=locale)
    mimesis.builtins.User(locale=locale)
    assert user_data.gender() == Gender.MASCULINE

# Generated at 2022-06-13 23:55:33.393216
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers import Personal

    provider = Personal('ru')
    with provider.override_locale('en') as p:
        assert p.get_current_locale() == locales.EN
        assert p.gender(Gender.MALE) != provider.gender(Gender.MALE)

    assert provider.get_current_locale() == locales.RU
    assert provider.gender(Gender.MALE) != Personal('en').gender(Gender.MALE)

# Generated at 2022-06-13 23:55:43.518653
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    from mimesis.builtins import USASpecification

    # BaseDataProvider not have locale attribute
    with pytest.raises(ValueError) as exc_info:
        with USASpecification().override_locale(locales.EN):
            assert False
    assert str(exc_info.value) == '«USASpecification» has not locale dependent'

    # Error when invalid locale passed
    with pytest.raises(UnsupportedLocale) as exc_info:
        with USASpecification(locale=locales.RU).override_locale():
            assert False
    assert str(exc_info.value) == 'Invalid locale: »»'

    # OK

# Generated at 2022-06-13 23:55:49.421811
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    #class FirstName(BaseDataProvider):
    #    pass
    #class LastName(BaseDataProvider):
    #    pass
    #
    #first_name1 = FirstName(locale='ru')
    #last_name1 = LastName(locale='ru')
    #
    #with first_name1.override_locale('en'):
    #    assert first_name1.get_current_locale() == 'en'
    #
    #assert first_name1.get_current_locale() == 'ru'
    #assert last_name1.get_current_locale() == 'ru'
    pass

# Generated at 2022-06-13 23:55:59.548399
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        class Meta:
            locale_dependent = True

        def __init__(self, locale='', seed=''):
            super().__init__(locale=locale, seed=seed)

    data = {'test': 'test'}

    t = TestProvider(locale='en')
    t._data = data['en'] = {'test': 'en',}

    with t.override_locale('ru') as l:
        l._data = data['ru'] = {'test': 'ru',}
        assert l.get_current_locale() == 'ru'
        assert l._data == {'test': 'ru',}
        assert l.test == 'ru'

    assert t.get_current_locale() == 'en'

# Generated at 2022-06-13 23:56:04.580658
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class Foo:

        def __init__(self, locale):
            self.locale = locale

    def main():
        foo = Foo(locales.EN)
        with foo.override_locale(locales.RU):
            bar = foo.locale

        foo2 = Foo(locales.EN)
        with foo2.override_locale(locales.RU):
            bar2 = foo.locale

        return bar, bar2

    bar, bar2 = main()
    assert bar == bar2 == locales.RU

# Generated at 2022-06-13 23:56:13.945909
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None) -> None:
            super().__init__(seed=seed, locale=locale)

        def get_current_locale(self) -> str:
            return self.locale

    provider = TestProvider(locale='en')
    with provider.override_locale() as new_provider:
        assert new_provider.get_current_locale() == locales.DEFAULT_LOCALE

    assert provider.get_current_locale() == 'en'


# Generated at 2022-06-13 23:56:24.414087
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.EN, seed: Seed = None) -> None:
            self._datafile = 'test.json'
            super().__init__(locale=locale, seed=seed)
            self._pull()

        def foo(self) -> str:
            return self._data['foo']


    t = TestProvider()
    assert t.foo() == 'FOO'
    with t.override_locale(locale='ru') as _t:
        assert _t.foo() == 'FOO_RU'
    assert t.foo() == 'FOO'

# Generated at 2022-06-13 23:57:10.736312
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """
    Проверяет правильность переопределения локали для провайдера.
    """
    Base = BaseDataProvider()
    locale = locales.RU
    try:
        with Base.override_locale(locale):
            assert Base.locale == locale
    except ValueError:
        assert True
    else:
        assert False

# Generated at 2022-06-13 23:57:11.709457
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:57:17.794664
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class TestProvider(BaseDataProvider):
        def get_data(self, key: str, default: str = '') -> Any:
            """Return data from provider's dictionary.

            :param key: Key of data object.
            :param default: Default value.
            """
            return self._data.get(key, default)

    provider = TestProvider()
    with provider.override_locale(locales.EN) as provider:
        print("\nLocale in contextmanager (english):", provider.get_current_locale())

    print("\nLocale out of contextmanager(default):", provider.get_current_locale())


# Generated at 2022-06-13 23:57:25.158485
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address

    provider = Address()
    obj =  provider.override_locale('ro').__enter__()
    assert obj.get_current_locale() == 'ro'

    provider = Address()
    obj = provider.override_locale().__enter__()
    assert obj.get_current_locale() == 'en'

    provider = Address(locale='ru')
    obj = provider.override_locale('ro').__enter__()
    assert obj.get_current_locale() == 'ro'

    provider = Address()
    obj = provider.override_locale('ro').__enter__()
    assert obj.get_current_locale() == 'ro'

# Generated at 2022-06-13 23:57:33.246313
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.person import Person

    en_person = Person(locale='en')
    with en_person.override_locale('ru') as _:
        assert en_person.get_current_locale() == 'ru', \
            'Locale not overridden! :('
    assert en_person.get_current_locale() == 'en', \
        'Locale not restored! :('



# Generated at 2022-06-13 23:57:37.998501
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the BaseDataProvider.override_locale() method."""
    bdp = BaseDataProvider(locale='en')
    with bdp.override_locale('fr'):
        bdp.locale = 'fr'
    assert bdp.locale == 'en'

# Generated at 2022-06-13 23:57:38.927483
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass


# Generated at 2022-06-13 23:57:51.185843
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, locale: str = locales.EN):
            super().__init__(locale)

        def get_current_locale(self):
            return self.locale

        def get_data(self):
            return self._data

    provider = Provider(locale=locales.EN)
    assert provider.get_current_locale() == locales.EN

    with provider.override_locale(locale=locales.RU) as p:
        assert p.get_current_locale() == locales.RU

    assert provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:57:58.752466
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # if __name__ != '__main__':
    #     pytest.skip('Tests for BaseDataProvider.override_locale() are disabled')

    provider = BaseDataProvider()
    provider._pull = lambda locale: setattr(provider, '_pull_data', locale)

    with provider.override_locale('ru'):
        assert provider._pull_data == 'ru'

    # idempotence
    with provider.override_locale('ru'):
        assert provider._pull_data == 'ru'

    with provider.override_locale('en'):
        assert provider._pull_data == 'en'

    assert provider._pull_data is None

    # changing global locale should not affect overridden locale
    provider.locale = 'ru'
    assert provider._pull_data is None



# Generated at 2022-06-13 23:58:09.263002
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.date import DateTime
    from mimesis.providers.address import Address
    from mimesis.providers.internet import Internet
    from mimesis.providers.person import Person
    from mimesis.providers.lorem import Lorem

    def test_datetime(datetime):
        assert isinstance(datetime, DateTime)
        return datetime.date()

    def test_person(person):
        assert isinstance(person, Person)
        return person.full_name()

    def test_lorem(lorem):
        assert isinstance(lorem, Lorem)
        return lorem.text()

    def test_address(address):
        assert isinstance(address, Address)
        return address.address()


# Generated at 2022-06-13 23:59:29.013017
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    # Initialization instance of class BaseDataProvider
    bdp = BaseDataProvider()

    with bdp.override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'

    assert bdp.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:59:38.727426
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestClass(BaseDataProvider):
        _datafile = 'name.json'

    with TestClass() as test_class:
        locale = test_class.get_current_locale()
        assert locale == locales.DEFAULT_LOCALE

    with TestClass(locale='ru') as test_instance:
        locale = test_instance.get_current_locale()
        assert locale == 'ru'

    with TestClass() as test_instance:
        with test_instance.override_locale(locale='ru'):
            locale = test_instance.get_current_locale()
        assert locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:59:40.411797
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert False


# Generated at 2022-06-13 23:59:54.506336
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestData(BaseDataProvider):

        def __init__(self, locale=locales.EN):
            super().__init__(locale=locale)
            self._data = ''

    provider = TestData()
    locale = locales.DEFAULT_LOCALE

    # AttributeError
    assert provider.get_current_locale() == locale
    with provider.override_locale(locale='ru'):
        provider.get_current_locale()
        assert provider.locale == locales.RU

    # Locale not supported
    provider.locale = 'not supported'
    with provider.override_locale(locale='ru'):
        assert provider.locale == locales.RU



# Generated at 2022-06-14 00:00:02.603152
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MockDataProvider(BaseDataProvider):
        """Mock class for testing the method override_locale in class BaseDataProvider."""

        def __init__(self):
            """Initialize attributes for data providers."""
            super().__init__(locale=locales.EN)
            self._datafile = 'car.json'
            self._pull()

        def __str__(self) -> str:
            """Human-readable representation of locale."""
            locale = getattr(self, 'locale', locales.DEFAULT_LOCALE)
            return '{} <{}>'.format(self.__class__.__name__, locale)

    p = MockDataProvider()
    assert p.locale == locales.DEFAULT_LOCALE
    with p.override_locale() as provider:
        assert provider.loc

# Generated at 2022-06-14 00:00:12.913226
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    # Test BaseDataProvider._override_locale
    from mimesis.providers import Person
    person = Person(locale='ru')
    assert person.name() == 'Александр'
    assert person.name(gender='male') == 'Александр'
    person._override_locale('en')
    assert person.name() == 'Lee'
    assert person.name(gender='female') == 'Rebekah'
    person._override_locale('ru')
    assert person.name() == 'Александр'

    # Test BaseDataProvider.override_locale
    from mimesis.providers import Address
    address = Address()
    address

# Generated at 2022-06-14 00:00:17.541842
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    foo = BaseDataProvider()
    with foo.override_locale('en') as f:
        assert f.locale == 'en'
    assert foo.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-14 00:00:18.566618
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 00:00:29.095463
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Person

    person = Person(locale='es')
    with person.override_locale('en'):
        assert person.locale == locales.EN

    assert person.locale == locales.ES

    with person.override_locale():
        assert person.locale == locales.DEFAULT_LOCALE

    assert person.locale == locales.ES

    # Test for exception
    p = BaseDataProvider(locale=locales.DEFAULT_LOCALE)
    try:
        with p.override_locale():
            assert True
    except ValueError:
        assert True
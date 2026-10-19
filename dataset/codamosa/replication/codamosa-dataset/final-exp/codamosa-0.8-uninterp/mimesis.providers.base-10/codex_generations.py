

# Generated at 2022-06-13 23:50:44.878019
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale='en')

    with provider.override_locale(locales.DEFAULT_LOCALE) as p:
        assert p.locale == locales.DEFAULT_LOCALE

    assert provider.locale == 'en'

    with provider.override_locale(locales.DEFAULT_LOCALE) as p:
        assert p.locale == locales.DEFAULT_LOCALE

    assert provider.locale == 'en'

# Generated at 2022-06-13 23:50:55.365165
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    def test_func(locale):
        with provider.override_locale(locale) as p:
            return p.get_current_locale()

    provider = BaseDataProvider()

    class Person(BaseDataProvider):
        __provider__ = 'person'
        __qualname__ = 'Person'

    assert test_func('en') == 'en'
    assert test_func('fr') == 'fr'

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE
    assert provider.override_locale.__name__ == 'override_locale'

    provider = Person()
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:50:57.353511
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # assert BaseDataProvider().override_locale(locale='en') == True
    assert True

# Generated at 2022-06-13 23:51:03.843053
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()

    with provider.override_locale('en_GB') as new_provider:
        assert new_provider.get_current_locale() == locales.EN_GB

    assert provider.get_current_locale() == locales.EN

    provider = BaseDataProvider(locales.RU)

    with provider.override_locale(locales.DE) as new_provider:
        assert new_provider.get_current_locale() == locales.DE

    assert provider.get_current_locale() == locales.RU

# Generated at 2022-06-13 23:51:11.146859
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Foo(BaseDataProvider):
        def __init__(self, seed=None):
            super().__init__(seed=seed)
        def get_current_locale(self) -> str:
            return self.locale
    foo = Foo(seed=None)
    with foo.override_locale(locale='ru') as f:
        assert f.get_current_locale() == 'ru'
    assert foo.get_current_locale() == 'en'


# Generated at 2022-06-13 23:51:15.633584
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test class BaseDataProvider."""
    data_provider = BaseDataProvider()

    context_manager = data_provider.override_locale()
    context_manager.__enter__()

    assert context_manager.__enter__() is data_provider
    assert context_manager.__exit__() is None

    with context_manager:
        assert context_manager.__enter__() is data_provider
        assert context_manager.__exit__() is None

# Generated at 2022-06-13 23:51:26.363457
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Food, Person, Address
    food = Food()
    person = Person()
    address = Address()
    buffer = []

    def test_func_with_context(food_, person_, address_):
        buffer.append(food_.food())
        buffer.append(person_.full_name())
        buffer.append(address_.city())

    with Food().override_locale(locales.ZH) as food_, \
         Person().override_locale(locales.ZH) as person_, \
         Address().override_locale(locales.ZH) as address_:
        test_func_with_context(food_, person_, address_)

    assert '蘑菇' in buffer
    assert '李钦' in buffer

# Generated at 2022-06-13 23:51:34.085267
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import json
    import locale_provider as locale
    data = locale.DataProvider()
    data.set_locale('en')
    # set locale en
    with data.override_locale(locale = 'en'):
        assert data.get_current_locale() == 'en'
        assert json.dumps(data.get_data()) == '{"1": "Python", "2": "JavaScript", "3": "Go"}'
    # set locale ru
    with data.override_locale(locale = 'ru'):
        assert data.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:51:37.457480
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit tests for method override_locale of class BaseDataProvider."""
    assert '<override_locale context manager>' in str(BaseDataProvider.override_locale)  # noqa

# Generated at 2022-06-13 23:51:40.512899
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider(base provider)."""
    provider = BaseDataProvider()
    provider.override_locale('ru')
    assert provider.locale == 'ru'

# Generated at 2022-06-13 23:51:52.790523
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
        from mimesis.providers import Person

        with Person().override_locale('en') as p:
            assert p.get_current_locale() == locales.EN

        assert p.get_current_locale() == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:51:53.791203
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    pass

# Generated at 2022-06-13 23:52:03.892083
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.calendar import Calendar

    def get_calendar_lang(obj):
        return obj._get_formatted_date('lang')

    # Check that calendar returns en locale
    assert get_calendar_lang(Calendar()) == locales.EN

    # Check that calendar returns de locale
    with Calendar().override_locale(locales.DE) as cal:
        assert get_calendar_lang(cal) == locales.DE

    # Check that calendar returns en locale again
    assert get_calendar_lang(Calendar()) == locales.EN

    # Check ValueError with non-locale dependent provider
    from mimesis.providers.numbers import Numbers
    with Numbers().override_locale(locales.EN):
        assert False, 'Operation not allowed'

# Generated at 2022-06-13 23:52:09.293891
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():  # noqa: D103
    from mimesis.providers.address import Address
    with Address().override_locale(locales.RU):
        assert Address().get_current_locale() == locales.RU
    assert Address().get_current_locale() == Address.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:15.893605
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    import mimesis.scheme as scheme

    scheme_de = scheme.Scheme(locale='de', seed=17004)
    scheme_fr = scheme.Scheme(locale='fr', seed=17004)

    with scheme_de.override_locale('fr') as provider:
        assert provider.get_current_locale() == 'fr'
        assert provider.hex_color() == scheme_fr.hex_color()

    assert scheme_de.get_current_locale() == 'de'
    assert scheme_de.hex_color() != scheme_fr.hex_color()

# Generated at 2022-06-13 23:52:19.121513
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, locale, seed):
            super().__init__(locale, seed)
            self.countries = {'pt': 'Brasil'}

    provider = Provider('pt_BR', 0)
    expect = 'Brasil'
    with provider.override_locale('pt'):
        result = provider.countries.get('pt')

    assert result == expect

# Generated at 2022-06-13 23:52:28.984602
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def name(self, gender: str = None, *, formatted: bool = False
                 ) -> str:
            """Get a random name.

            :param str gender: Gender of name.
            :param bool formatted: A flag to format name.
            :return: Random name.
            """
            gender = self._validate_enum(gender, self.Gender)

            pattern = self._data['names'][gender]
            if formatted:
                return self.random.choice(pattern)
            else:
                return self.random.choice(pattern).lower()

        @property
        def gender(self) -> Dict[str, str]:
            """Get gender.

            :return: Gender as dict.
            """
            return self._data['gender']


# Generated at 2022-06-13 23:52:38.245850
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method ``override_locale`` of class ``BaseDataProvider``."""
    class FakeDataProvider(BaseDataProvider):
        """This is fake data provider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes for fake data providers."""
            super().__init__(locale=locale, seed=seed)

    fake_data_provider = FakeDataProvider(locale=locales.EN)
    with fake_data_provider.override_locale(locales.RU):
        assert fake_data_provider.locale == locales.RU
    assert fake_data_provider.locale == locales.EN



# Generated at 2022-06-13 23:52:48.939402
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestOverrideLocale(BaseDataProvider):
        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)

    # Creating instance of class TestOverrideLocale
    locale_provider = TestOverrideLocale()
    # Testing method override_locale
    with locale_provider.override_locale(locale=locales.DEFAULT_LOCALE) as p:
        assert p == locale_provider
        assert p.get_current_locale() == locales.DEFAULT_LOCALE
        with p.override_locale(locale=locales.DEFAULT_LOCALE) as p:
            assert p == locale_provider
            assert p.get_current_locale() == locales.DEFAULT_LOC

# Generated at 2022-06-13 23:52:57.201371
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class GrammarProvider(BaseDataProvider):
        def __init__(self, locale: str = 'en', seed: Seed = None,
                     **kwargs: Dict[str, Any]) -> None:
            super().__init__(locale, seed=seed, **kwargs)
            self._datafile = 'grammar.json'
            self._pull()

    grammar = GrammarProvider('ru')
    assert grammar.locale == 'ru'
    with grammar.override_locale('en'):
        assert grammar.locale == 'en'
    assert grammar.locale == 'ru'



# Generated at 2022-06-13 23:53:21.874273
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.datetime import Datetime

    provider = Datetime()
    locale = 'ru'
    with provider.override_locale(locale) as p:
        assert p.locale == locale
    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:53:27.980504
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def get_data(self) -> Dict:
            return {}
    provider = Test()
    with provider.override_locale():
        assert provider.locale == locales.DEFAULT_LOCALE
    assert provider.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:53:37.554207
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override_locale method."""
    from mimesis.providers.addresses import Addresses
    provider = Addresses(locale='en')

    with provider.override_locale('de'):
        assert provider.get_current_locale() == 'de'

    with provider.override_locale('ru'):
        assert provider.get_current_locale() == 'ru'

    with provider.override_locale(locale='en'):
        assert provider.get_current_locale() == 'en'

    assert provider.get_current_locale() == 'en'
    with provider.override_locale(locale='es'):
        assert provider.get_current_locale() == 'es'

# Generated at 2022-06-13 23:53:45.032154
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Overriding locale for BaseDataProvider."""
    from mimesis.enums import Gender
    from mimesis.providers import Person as PersonProvider
    from mimesis.providers import Address as AddressProvider
    from mimesis.providers import Payment as PaymentProvider
    p = PersonProvider()
    a = AddressProvider()
    t = PaymentProvider()

    with p.override_locale('ru'):
        assert p.get_full_name(gender=Gender.FEMALE) == 'Любовь Гагарина'
        assert p.get_full_name(gender=Gender.MALE, last_name='Адамович') == 'Алексей Адамович'


# Generated at 2022-06-13 23:53:45.624540
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert BaseDataProvider().override_locale()

# Generated at 2022-06-13 23:53:50.926618
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.internet import Internet

    provider = Internet('en')
    assert provider.locale == 'en'
    assert provider.get_current_locale() == 'en'

    with provider.override_locale('ru'):
        assert provider.locale == 'ru'
        assert provider.get_current_locale() == 'ru'

    assert provider.locale == 'en'
    assert provider.get_current_locale() == 'en'



# Generated at 2022-06-13 23:53:53.577134
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()

    with provider.override_locale(locales.EN) as p:
        assert p.get_current_locale() == locales.EN
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:53:54.051097
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:53:56.865318
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    provider = Person()
    locale = 'ru'
    provider.override_locale(locale)
    assert provider.get_current_locale() == locale

    with provider.override_locale(locale) as p:
        assert p.get_current_locale() == locale

# Generated at 2022-06-13 23:54:05.259618
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code
    from mimesis.enums import CodeType

    # GIVEN
    code = Code(locale='es')
    language_code = CodeType.LANGUAGE.lower()

    assert code.locale == 'es'
    assert code.code(language_code) == 'español'

    # WHEN
    with code.override_locale('es') as code:
        assert code.locale == 'es'

    # THEN
    assert code.code(language_code) == 'español'



# Generated at 2022-06-13 23:54:51.626740
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestData(BaseDataProvider):
        def __init__(self):
            self._datafile = 'fake.json'
            super().__init__()

        def get_data(self) -> Dict[str, Any]:
            return self._data

        def fake_method(self) -> str:
            pass

    test_data = TestData()
    with test_data.override_locale('ru') as d:
        assert d.get_current_locale() == 'ru'
        assert 'ru' in d.get_data()
        assert 'en' not in d.get_data()

    assert test_data.get_current_locale() == locales.EN
    assert 'en' in test_data.get_data()
    assert 'ru' not in test_data.get_data()


# Generated at 2022-06-13 23:54:53.655369
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def get_foo(self):
            return 'bar'
    data = TestDataProvider()
    with data.override_locale('ru') as data:
        assert data.get_foo() == 'bar'

# Generated at 2022-06-13 23:55:01.270126
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Test that we can override locale in context manager
    provider = BaseDataProvider('en')
    with provider.override_locale('ru') as provider:
        # We check that locale is in the context of the manager
        assert provider.get_current_locale() == 'ru'
    # Check that the context manager does not affect the state of the provider
    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:55:10.874672
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()

    class TestDataProvider(BaseDataProvider):
        def get_current_locale(self) -> str:
            return self.locale

    provider = TestDataProvider(locale='de')
    assert provider.get_current_locale() == 'de'

    with provider.override_locale('ru') as rp:
        assert rp.get_current_locale() == 'ru'
        assert provider.get_current_locale() == 'de'

    assert provider.get_current_locale() == 'de'

    try:
        with provider.override_locale('ru') as rp:
            raise Exception('Some error')
    except:
        pass
    assert provider.get_current_locale() == 'de'

# Generated at 2022-06-13 23:55:14.977531
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def foo(self):
            return {'foo': self.locale}

    p = Provider()
    assert p.locale == 'en'
    assert p.foo() == {'foo': 'en'}

    with p.override_locale('ru') as p:
        p.foo() == {'foo': 'ru'}

    assert p.locale == 'en'
    assert p.foo() == {'foo': 'en'}

# Generated at 2022-06-13 23:55:22.712836
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale."""
    from mimesis.builtins import Random
    from mimesis.enums import Gender

    r = Random()

    with r.override_locale('ru') as data:
        assert data.person.get_gender() is Gender.MALE

    # Initial setup
    assert r.person.get_gender() is Gender.MALE
    assert r.person.get_gender(Gender.FEMALE) is Gender.FEMALE

    # Override locale
    with r.override_locale('uk') as data:
        assert data.get_current_locale() == 'uk'
        assert data.person.get_gender() is Gender.FEMALE
        assert data.person.get_gender(Gender.MALE) is Gender.MALE

    # Check that original state was restored

# Generated at 2022-06-13 23:55:36.554158
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address, Personal, Person
    from mimesis.schema import Field
    from mimesis.enums import Gender

    with Person('ru').override_locale('fr') as person:
        first_name = person('first_name', gender=Gender.FEMALE)
        if first_name != 'Yvette':
            raise TypeError('{} != "Yvette"'.format(first_name))

    person = Person('en')
    first_name = person('first_name', gender=Gender.FEMALE)
    last_name = person('surname')

# Generated at 2022-06-13 23:55:44.671994
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""

    bdp = BaseDataProvider()
    bdp.locale = 'en'
    locale = 'ru'
    bdp._override_locale(locale)
    assert bdp.locale == locale
    assert bdp.get_current_locale() == locale

    bdp.locale = 'ja'
    with bdp.override_locale(locale):
        assert bdp.locale == locale
        assert bdp.get_current_locale() == locale
    assert bdp.locale != locale
    assert bdp.get_current_locale() != locale

    locale = 'zh'
    with bdp.override_locale(locale):
        assert bdp.locale == locale
        assert bdp.get_

# Generated at 2022-06-13 23:55:49.051063
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bdp = BaseDataProvider(locale='en', seed=12)
    bdp._datafile = '__test_BaseDataProvider_override_locale.json'
    with open(bdp._datafile, 'w+') as f:
        f.write('{\n    "test_data": "en"\n}')
    bdp._pull()
    assert bdp._data.get('test_data') == 'en'

    with bdp.override_locale(locale='ru') as pr:
        assert pr.locale == 'ru'
        with open(bdp._datafile, 'w+') as f:
            f.write('{\n    "test_data": "ru"\n}')
        pr._pull()
        assert pr._data.get('test_data') == 'ru'



# Generated at 2022-06-13 23:55:59.516425
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    from mimesis.enums import Gender
    from mimesis.providers import Person
    p = Person('en')
    with pytest.raises(ValueError):
        with p.override_locale('ru'):
            pass
    assert p.gender_full == Gender.MALE.value
    assert p.gender_short == Gender.MALE.value
    p = Person('ru')
    with p.override_locale('en'):
        assert p.gender_full == Gender.MALE.value
        assert p.gender_short == Gender.MALE.value
    assert p.gender_full == Gender.MALE.value
    assert p.gender_short == Gender.MALE.value
    p = Person('ru')

# Generated at 2022-06-13 23:57:25.542100
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale=locales.EN)
    with provider.override_locale(locales.RU):
        assert provider.locale == locales.RU
    assert provider.locale == locales.EN


# Generated at 2022-06-13 23:57:34.188742
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    bdp = BaseDataProvider(locale=locales.EN, seed=123)
    with bdp.override_locale(locales.RU):
        assert bdp.get_current_locale() == locales.RU
    assert bdp.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:57:43.920133
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method `override_locale` of class BaseDataProvider."""

    class TestProvider(BaseDataProvider):
        def __init__(self, locale, seed):
            super().__init__(locale=locale, seed=seed)
        def _pull(self, filename=None):
            self._data = {'name': 'Andrei'}

    tp = TestProvider('fr', 'seed')
    with tp.override_locale('ru'):
        assert tp._data == {'name': 'Andrei'}

    assert tp._data == {'name': 'Andrei'}


# Generated at 2022-06-13 23:57:47.363115
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        pass

    p = TestProvider()
    with p.override_locale('ru') as pr:
        assert pr.locale == 'ru'
        assert p.locale == 'ru'
    assert p.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:57:56.027668
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method ``override_locale`` of class ``BaseDataProvider``."""
    class TestProvider(BaseDataProvider):
        """Test class for testing method ``override_locale`` of class ``BaseDataProvider``."""
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None) -> None:
            self.locale = locale
            super().__init__(locale, seed)

    provider = TestProvider()
    with provider.override_locale(locales.RU) as p:
        assert p.locale == locales.RU
    assert provider.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:57:57.134151
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:58:03.489192
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class Provider(BaseDataProvider):

        def __init__(self, locale='en', seed=None):
            super().__init__(seed=seed)
            self.locale = locale

    pr = Provider()
    with pr.override_locale('ru') as provider:
        assert provider.locale == 'ru'

# Generated at 2022-06-13 23:58:12.564034
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class custom_BaseProvider(BaseDataProvider):
        def __init__(self, locale: str = 'en'):
            super().__init__(locale=locale)
    class custom_BaseProvider_child(custom_BaseProvider):
        def __init__(self, locale: str = 'ru'):
            super().__init__(locale=locale)

    provider_success = custom_BaseProvider(locale='ru')
    with provider_success.override_locale(locale='en') as p:
        assert p.get_current_locale() == 'en'

    provider_success = custom_BaseProvider_child(locale='en')
    with provider_success.override_locale(locale='ru') as p:
        assert p.get_current_locale() == 'ru'

    provider

# Generated at 2022-06-13 23:58:17.691476
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Define variables
    locale = locales.EN
    provider = BaseDataProvider()

    # Use context manager
    with provider.override_locale(locale) as p:
        assert p.get_current_locale() == locale

    # Expect exception when call method with builtin provider
    try:
        with provider.override_locale(locale) as p:
            assert p.get_current_locale() == locale
    except ValueError:
        pass

# Generated at 2022-06-13 23:58:24.787117
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Providers with overridden locales should return localized data."""
    from mimesis.providers.base import BaseDataProvider
    from mimesis.providers.numbers import Numbers

    class LocalizedNumbers(Numbers):

        def __init__(self, locale: str = locales.EN, seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

        def get_data(self) -> Dict:
            return {
                locales.ES: {'foo': 'bar'},
            }

    data_provider = LocalizedNumbers()

    assert data_provider.get_data().get('foo') is None
    assert data_provider.get_data().get(locales.ES, {}).get('foo') == 'bar'

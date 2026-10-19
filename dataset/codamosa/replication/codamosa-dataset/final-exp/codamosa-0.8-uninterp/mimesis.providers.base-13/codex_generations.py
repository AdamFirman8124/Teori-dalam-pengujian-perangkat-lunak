

# Generated at 2022-06-13 23:50:41.475821
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test of method override_locale of class BaseDataProvider."""
    class TestClass(BaseDataProvider):
        """Test class."""
        pass

    test = TestClass()

    with test.override_locale(locales.RU) as _test:
        assert _test.get_current_locale() == locales.RU

    assert test.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:50:43.211192
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider"""
    pass

# Generated at 2022-06-13 23:50:46.928630
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bp = BaseDataProvider()
    with bp.override_locale('ru'):
        assert isinstance(bp.get_current_locale(), str)
test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:50:53.135469
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeClass(BaseDataProvider):
        def __init__(self, locale, seed):
            super().__init__()

    fake_data_provider = FakeClass('en', '4')
    with fake_data_provider.override_locale('ru'):
        assert fake_data_provider.locale == 'ru'

    fake_data_provider = FakeClass('en', '4')
    with fake_data_provider.override_locale('ru'):
        fake_data_provider.locale = 'ua'
        assert fake_data_provider.locale == 'ua'

    fake_data_provider = FakeClass('en', '4')
    with fake_data_provider.override_locale('ru'):
        fake_data_provider.locale = fake_

# Generated at 2022-06-13 23:51:03.226849
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    def check_value(provider: BaseDataProvider, locale: str,
                    value: Any) -> None:
        with provider.override_locale(locale):
            assert provider.full_name() == value

    provider = Person('ru')
    check_value(provider, 'ru', 'Вера Павловna')
    check_value(provider, 'be', 'Анастасія Ціціна')
    check_value(provider, 'en', 'Graham Villarreal')
    check_value(provider, 'de', 'Lauren Helbig')
    check_value(provider, 'uk', 'Микита Савич')
    check

# Generated at 2022-06-13 23:51:09.160899
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for BaseDataProvider.override_locale."""
    from mimesis.providers.builtins import Builtins
    builtins = Builtins()
    locale = locales.EN
    with builtins.override_locale(locale=locale) as builtins:
        if builtins.get_current_locale() != locale:
            raise AssertionError(
                '«{}» is not equal «{}»'.format(
                    builtins.get_current_locale(),
                    locale,
                )
            )

# Generated at 2022-06-13 23:51:15.637798
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def get_time_zone(self) -> str:
            return self.random.choice(self._data['timeZone'])

    data_provider = TestDataProvider()
    with data_provider.override_locale('ru') as p:
        time_zone = p.get_time_zone()
        assert (time_zone in data_provider._data['timeZone']) == True
    return data_provider

# Generated at 2022-06-13 23:51:24.239044
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def test_locale_dependent(self):
            return self.random.boolean()
    provider = TestDataProvider()

    # Test for correct working of contextmanager.
    with provider.override_locale('ru') as provider:
        assert provider.test_locale_dependent()

    # Test for lru_cache.
    with provider.override_locale('en'):
        provider.test_locale_dependent()
        provider.test_locale_dependent()

    # Test for exception
    with provider.override_locale('en'):
        pass

# Generated at 2022-06-13 23:51:27.797257
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        pass

    with TestProvider().override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'

    assert TestProvider().get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:32.562116
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for ``override_locale`` method.
    """

    class Foo(BaseDataProvider):
        def __init__(self, locale: str = 'en'):
            self.locale = locale

        def get_current_locale(self):
            return self.locale

    foo = Foo('en')

    with foo.override_locale('ru') as f:
        assert f.get_current_locale() == 'ru'
    assert foo.get_current_locale() == 'en'

# Generated at 2022-06-13 23:51:44.964611
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    with BaseDataProvider().override_locale() as dp1:
        assert dp1.get_current_locale() == locales.DEFAULT_LOCALE
    # dp1.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:51:52.414091
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider.override_locale().
    """
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    class Street(Address):
        """A class for testing."""

        def __init__(self, locale: str = 'en', seed: Seed = None) -> None:
            """Initialize attributes.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale, seed)
            self._datafile = 'streets.json'
            self._pull()

        def street(self) -> str:
            """Get the full street name.

            :return: The full street name.
            """
            street_name = self._data['street_name']

# Generated at 2022-06-13 23:51:55.899092
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    person = Person()
    with person.override_locale('en'):
        assert person.locale == 'en'

"""
    def __getattr__(self, key: str) -> Any:
        if key in self._data:
            return self._data[key]
        else:
            object.__getattribute__(self, key)
"""

# Generated at 2022-06-13 23:52:04.017644
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale='en',
                     seed=None):
            super().__init__(locale, seed)

    provider = TestProvider('ru')
    assert provider.locale == 'ru'

    ru_first_name = provider.first_name()
    assert ru_first_name

    with provider.override_locale('en') as p:
        assert p.locale == 'en'
        en_first_name = p.first_name()
        assert en_first_name
        assert en_first_name != ru_first_name

    assert provider.locale == 'ru'



# Generated at 2022-06-13 23:52:10.954422
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    # Unit test for method override_locale of class BaseDataProvider
    person = Person()
    with person.override_locale('ru') as person_ru:
        assert person_ru.locale == 'ru'
        assert person.locale == 'en'

# Generated at 2022-06-13 23:52:24.856934
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.schema import Field

    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None):
            super().__init__(locale, seed)
            self.field = Field('test')

        def test(self, method=None):
            return getattr(self.field, method or 'test')()

    provider = TestProvider()

    assert provider.test(method='test')

    with provider.override_locale(locales.MK) as provider_mk:
        assert provider_mk.locale == locales.MK
        assert provider_mk.get_current_locale() == 'mk'
        assert provider_mk.test(method='test')


# Generated at 2022-06-13 23:52:30.390893
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method _override_locale of class BaseDataProvider."""
    from mimesis.providers.text import Text
    for content in Text()._data:
        assert content in Text()._data



# Generated at 2022-06-13 23:52:34.490747
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test function for BaseDataProvider class"""

    from mimesis.builtins import Person
    p = Person()
    p._override_locale(locales.EN)
    assert p.locale == locales.EN
    assert p.get_current_locale() == locales.EN



# Generated at 2022-06-13 23:52:42.354526
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    dp = BaseDataProvider()
    with dp.override_locale(locale=locales.EN):
        assert dp.locale == locales.EN_US

    with dp.override_locale(locale=locales.RU):
        assert dp.locale == locales.RU_RU

    try:
        with dp.override_locale(locale=locales.DEFAULT_LOCALE):
            assert False
    except ValueError:
        assert True

# Generated at 2022-06-13 23:52:47.698978
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class A(BaseDataProvider):
        pass

    with A.override_locale() as p:
        assert isinstance(p, A)

    with pytest.raises(ValueError):
        with A.override_locale() as p:
            assert isinstance(p, A)

# Generated at 2022-06-13 23:53:01.134231
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.address import Address
    with Address().override_locale(locales.ES) as p:
        assert p.get_current_locale() == locales.ES
        assert isinstance(p.address_line(), str)
        assert p.address_line() != 'Address line'

# Generated at 2022-06-13 23:53:11.084289
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from random import Random
    from mimesis.providers.base import BaseDataProvider
    from mimesis.typing import Seed

    seed = Seed(42)
    locale = 'en'

# Generated at 2022-06-13 23:53:16.757513
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Currency
    with Currency().override_locale('en') as curr:
        assert curr.get_current_locale() == 'en'
        assert curr.get_fraction() in ('PEN', 'AUD', 'BRL', 'DKK', 'USD')



# Generated at 2022-06-13 23:53:28.092084
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.providers.card import CreditCard
    from mimesis.exceptions import NonEnumerableError
    #  Temporary overridden locale.
    with Address(locale='en').override_locale('ru') as address:
        assert address.get_current_locale() == 'ru'
        assert address.country() == 'США'
    #  Check default locale.
    assert Address().get_current_locale() == 'en'
    #  Use builtin provider.
    with CreditCard().override_locale(locale='en'):
        pass
    #  Check non-locale-dependent provider.
    with CreditCard().override_locale(locale='en') as credit_card:
        assert credit_card.type

# Generated at 2022-06-13 23:53:35.086469
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Language
    # Create an instance of a class.
    enum = Language(locale='ru')
    # Expected result.
    result = {'locale': 'ru'}
    # Call the method.
    with enum.override_locale('en') as p:
        # Check result.
        assert p.get_current_locale() == result.get('locale')

# Generated at 2022-06-13 23:53:39.455340
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def __init__(self):
            super().__init__()
            self.locale = 'es'

        def get_current_locale(self):
            return self.locale

    test_provider = TestDataProvider()
    assert test_provider.get_current_locale() == 'es'
    with test_provider.override_locale('ru'):
        assert test_provider.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:53:45.700690
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    with provider.override_locale(locale='en') as provider:
        assert provider.get_current_locale() == 'en'
        with provider.override_locale(locale='ru') as provider:
            assert provider.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:53:50.695062
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.geography import Geography
    from mimesis.providers.person import Person

    p = Person('en')
    with p.override_locale('ru'):
        assert p.get_current_locale() == 'ru'

    g = Geography('en')
    with g.override_locale('ru'):
        assert g.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:53:56.002877
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        pass
    provider = TestProvider('ru')
    assert provider.get_current_locale() == 'ru'

    with provider.override_locale('en'):
        assert provider.get_current_locale() == 'en'
        provider.override_locale('zh')
        assert provider.get_current_locale() == 'zh'

    assert provider.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:54:09.833245
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.locales import __all__ as locales
    from mimesis.providers.address import Address
    from mimesis.providers.base import BaseDataProvider
    from mimesis.providers.geography import Geography
    from mimesis.providers.person import Person
    from mimesis.typing import LocaleCode

    class TestClass(BaseDataProvider):
        def __init__(self, locale: LocaleCode = None,
                     seed: Seed = None) -> None:
            super().__init__(seed)
            self.locale = locale

    test_class = TestClass()

    assert isinstance(test_class, BaseDataProvider)
    assert isinstance(test_class, Address)
    assert isinstance(test_class, Geography)

# Generated at 2022-06-13 23:54:22.207128
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for BaseDataProvider._override_locale."""
    provider = BaseDataProvider()

    with provider.override_locale(locales.EN):
        assert provider.get_current_locale() == locales.EN

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:54:28.749398
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bdp = BaseDataProvider()
    with bdp.override_locale('ru') as russian_bdp:
        assert bdp.get_current_locale() == 'ru'
        assert bdp is russian_bdp
    assert bdp.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:54:33.126263
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = 'ru'
    dp = BaseDataProvider(locale='be')
    assert dp.get_current_locale() == locales.BE
    with dp.override_locale(locale) as provider:
        assert provider.get_current_locale() == locale
    assert dp.get_current_locale() == locales.BE

# Generated at 2022-06-13 23:54:37.520651
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider('ru')
    with provider.override_locale('en') as provider:
        print(provider.get_current_locale())

test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:54:41.089128
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import RussiaSpecProvider
    with RussiaSpecProvider().override_locale('ru') as r:
        assert r.get_current_locale() == 'ru'
    assert RussiaSpecProvider().get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:54:52.536741
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for BaseDataProvider.override_locale."""
    from mimesis.enums import Gender

    with BaseDataProvider(locale=locales.EN).override_locale(locales.RU) as bdp:
        bdp.random.seed(1234)
        assert bdp.random.randint(1, 10) == 10
        assert bdp.random.randint(1, 10) == 5
        assert bdp.random.randint(1, 10) == 6
        assert bdp.random.randint(1, 10) == 3
        assert bdp.random.randint(1, 10) == 3
        assert bdp.random.randint(1, 10) == 8
        assert bdp.random.randint(1, 10) == 7

# Generated at 2022-06-13 23:54:58.146961
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestOverridenLocale(BaseDataProvider):
        def __init__(self, locale=locales.EN, seed=None):
            super().__init__(locale=locale, seed=seed)

        def get_current_locale(self):
            return 'current locale: {}'.format(self.locale)

    bsp = TestOverridenLocale()

    with bsp.override_locale(locale=locales.RU):
        assert bsp.get_current_locale() == 'current locale: ru'

    assert bsp.get_current_locale() == 'current locale: en'

# Generated at 2022-06-13 23:55:06.398810
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    class Provider(BaseDataProvider):
        """Class Provider."""
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale, seed)

    p = Provider(locale='ru')
    with p.override_locale('en'):
        assert p.locale == 'en'


if __name__ == '__main__':
    test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:55:12.106152
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, locale: str = 'en'):
            super().__init__(locale=locale)

        def get_locale(self) -> str:
            return self.locale
    provider = Provider()
    expected = 'foo'
    with provider.override_locale(expected) as p:
        assert expected == p.get_locale()
    assert provider.locale != expected

# Generated at 2022-06-13 23:55:17.115268
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, seed=None, locale='en'):
            super().__init__(seed=seed, locale=locale)

    provider = TestProvider(locale='de')
    with provider.override_locale('en') as prov:
        print(prov, ":", prov._data)

    print(provider, ":", provider._data)

# Generated at 2022-06-13 23:55:33.622781
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code

    original_locale = Code().get_current_locale()
    assert original_locale == 'en'

    with Code().override_locale('ru'):
        assert Code().get_current_locale() == 'ru'

    assert Code().get_current_locale() == original_locale



# Generated at 2022-06-13 23:55:42.529673
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Expected value {'name': 'Иван', 'surname': 'Петров'}
    result = DictProvider().override_locale('ru').name()
    assert result == {'name': 'Иван', 'surname': 'Петров'}

    # Expected value {'name': 'Juan', 'surname': 'González'}
    result = DictProvider().override_locale('es-PY').name()
    assert result == {'name': 'Juan', 'surname': 'González'}


# Test for method _pull of class BaseProvider

# Generated at 2022-06-13 23:55:47.279582
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider

    This test is an example and is not included in unit tests pack.
    """
    from mimesis.providers.numbers import Numbers

    numbers = Numbers()
    with numbers.override_locale():
        assert numbers.get_current_locale() == 'en'
    assert numbers.get_current_locale() == 'en'

# Generated at 2022-06-13 23:55:56.281197
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.EN, seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
            self._data = ['one', 'two', 'three']
            self._datafile = ''

    provider = TestProvider()
    with provider.override_locale('ru') as overridden_provider:
        assert provider.get_current_locale() == 'ru'
        assert overridden_provider.get_current_locale() == 'ru'
        assert provider == overridden_provider
    assert provider.get_current_locale() == 'en'
    assert provider != overridden_provider

# Generated at 2022-06-13 23:56:02.258442
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Locale

    m = Locale('ru')
    locale = m.locale
    with m.override_locale('en') as _m:
        assert _m.locale == 'en'
        assert getattr(_m, 'locale', None) != locale
    assert m.locale == locale

# Generated at 2022-06-13 23:56:08.365402
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Personal
    with Personal().override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'
    assert Personal().get_current_locale() == 'en'

# Generated at 2022-06-13 23:56:14.194345
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class TestData(BaseDataProvider):
        def __init__(self, locale=locales.EN):
            super().__init__(locale=locale)

    test_data = TestData()
    with test_data.override_locale(locales.ES) as t:
        assert t.locale == locales.ES

    assert test_data.locale == locales.EN

# Generated at 2022-06-13 23:56:25.863967
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.builtins import Person
    from mimesis.builtins import Address

    person = Person('fr')
    person.seed(1234)  # for reproducible results
    with person.override_locale('en') as p:
        assert p.get_current_locale().lower() == 'en'

        name_person_fr = 'Arya'
        name_person_en = 'Edward'

        assert person.name(gender=Gender.FEMALE) == name_person_fr  # fr
        assert p.name(gender=Gender.MALE) == name_person_en  # en

    address = Address('de')
    with address.override_locale('en') as a:
        assert a.city() == 'Fremont'  #

# Generated at 2022-06-13 23:56:29.720312
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    provider = Address()

    with provider.override_locale(locales.JA) as obj:
        assert obj.get_current_locale() == locales.JA

    assert obj.get_current_locale() == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:56:38.804089
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        pass

    seed = 1

    locale = 'ru'
    locale_other = 'en'

    tdp = TestDataProvider(seed=seed)
    tdp_other = TestDataProvider(locale=locale, seed=seed)

    def is_locale_dependent(provider) -> bool:
        return getattr(provider, 'locale', None) is not None

    assert str(tdp) == 'TestDataProvider <en>'

    with tdp_other.override_locale(locale_other):
        assert str(tdp_other) == 'TestDataProvider <en>'
        assert tdp_other.locale == locale_other

    assert str(tdp_other) == 'TestDataProvider <ru>'
    assert tdp_other.loc

# Generated at 2022-06-13 23:56:54.049519
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Dummy(BaseDataProvider):
        pass
    provider = Dummy()
    assert provider.locale == locales.EN
    with provider.override_locale('ru') as p:
        assert p.locale == 'ru'
    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:57:03.027636
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method BaseDataProvider.override_locale."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    def test_it_works(person: Person, gender: Gender) -> None:
        """Test it works."""
        with person.override_locale(locales.EN):
            assert person.gender(gender) == \
                person.gender(gender, locale=locales.EN)

            assert person.full_name(gender) == \
                person.full_name(gender, locale=locales.EN)

    def test_it_raises_value_error(person: Any, gender: Gender) -> None:
        """Test it raises value error."""

# Generated at 2022-06-13 23:57:13.521835
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Person
    class_name = Person.__name__
    origin_locale = locales.RU
    override_locale = locales.EN
    person = Person(origin_locale)
    assert getattr(person, 'locale', locales.DEFAULT_LOCALE) == origin_locale
    with person.override_locale(override_locale) as p:
        assert getattr(p, 'locale', locales.DEFAULT_LOCALE) == override_locale
    assert getattr(person, 'locale', locales.DEFAULT_LOCALE) == origin_locale


# Generated at 2022-06-13 23:57:23.876469
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider.

    This test method is not a real unit test,
    it just a functional test and the only purpose is to cover 100%
    of the code by unit tests,
    to make the coverage of BaseDataProvider
    as much as possible.
    """
    class MyProvider(BaseDataProvider):
        """Provider class for testing."""
        def test_method(self):
            """Method for test."""
            return self.get_current_locale()

    provider = MyProvider()
    provider.test_method()

    with provider.override_locale(locales.RU):
        provider.test_method()

    with provider.override_locale(locales.RU):
        with provider.override_locale(locales.DE):
            provider.test_method

# Generated at 2022-06-13 23:57:38.279779
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    # lint:ok
    class MockBaseDataProvider(BaseDataProvider):
        def __init__(self, **kwargs: Any) -> None:
            super().__init__(**kwargs)  # type: ignore
            self.locale = ''

        def get_data(self, key: str) -> str:
            """Get data from dict by key.

            :param key: Key of dict.
            :return: Data from dict by key.
            """
            self._pull()
            data = self._data
            current_locale = self.locale
            return {'data': data.get(key), 'locale': current_locale}

    provider = MockBaseDataProvider(seed=12345)
    locale = provider.get_current_

# Generated at 2022-06-13 23:57:52.773379
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, locale: str = None, seed: Seed = None):
            super().__init__(locale=locale, seed=seed)
            self._data = {}
            self._data['__all__'] = {'data': ['foo', 'bar', 'baz']}

        def get_data(self):
            return self._data['__all__']['data']

    p = Provider()
    assert p.get_current_locale() == 'en'

    with p.override_locale(locale='ru'):
        assert p.get_current_locale() == 'ru'

    assert p.get_current_locale() == 'en'

    p2 = Provider('ru')

# Generated at 2022-06-13 23:58:03.944032
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the override_locale method of the BaseDataProvider class."""
    from mimesis.builtins import Address, Demography, Person

    seed = '1234567890'

    result = {}

    with Person('en').override_locale('ru') as p:
        result['ru'] = p.full_name(gender='male')

    with Person('en').override_locale('zh') as p:
        result['zh'] = p.full_name(gender='female')

    with Person('en').override_locale('en') as p:
        result['en'] = p.full_name(gender='all')

    with Address('en').override_locale('ru') as a:
        result['ru'] += a.postal_code()


# Generated at 2022-06-13 23:58:12.591676
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    # Importing imported module to prevent a circular import
    from mimesis.providers.address import Address
   
    # Testing __str__
    address = Address()
    assert str(address) == 'Address <en>'
    
    # Testing method override_locale
    with address.override_locale('ru'):
        assert str(address) == 'Address <ru>'

    # Testing the functionality of method override_locale
    # with address.override_locale('ru'):
    #     assert 'Россия' in address.country()
    #     assert 'Россия' not in address.country('en')
    #     assert 'Россия' in address.country('ru')
    #     assert 'Россия' not in address.

# Generated at 2022-06-13 23:58:21.152823
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method ``override_locale`` of class ``BaseDataProvider``."""
    from mimesis.encoders import BaseEncoder

    class MyEncoder(BaseEncoder):
        """Class for test."""

    assert_equal = functools.partial(assert_equal,
                                     'override_locale()')

    encoder = MyEncoder()

    with encoder.override_locale('en') as instance:
        assert_equal(instance.locale, 'en')

    with encoder.override_locale('ru') as instance:
        assert_equal(instance.locale, 'ru')
        assert_equal(instance.get_current_locale(), 'ru')
        assert_equal(encoder.get_current_locale(), 'en')



# Generated at 2022-06-13 23:58:31.634907
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class ToyClass(BaseDataProvider):
        pass
    class ToyClass2(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            super().__init__(self, locale=locale)

    tc = ToyClass()
    tc2 = ToyClass2()

    with tc.override_locale(locales.CS):
        assert tc.locale == locales.CS
    with tc2.override_locale(locales.EN) as tc2_en:
        assert tc2.locale == locales.EN, 'Cannot override locale'
        assert tc2_en.locale == locales.EN
    assert tc2.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:58:49.253381
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    from mimesis.enums import Gender
    p = Person('en')
    assert p.get_current_locale() == locales.EN
    with p.override_locale(locales.RU) as p1:
        assert p1.get_current_locale() == locales.RU
    p2 = p1.override_locale(locales.DE)
    assert p2.get_current_locale() == locales.DE

# Generated at 2022-06-13 23:59:02.783666
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DataProvider(BaseDataProvider):
        def get_data(self, key: str) -> str:
            return self._data[key]

        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test.json'

    provider = DataProvider()

    with provider.override_locale(locales.RU):
        assert provider.get_data('key') == 'русский'

    assert provider.get_data('key') == 'english'

if __name__ == '__main__':
    # Unit test for method override_locale of class BaseDataProvider
    print(test_BaseDataProvider_override_locale())

# Generated at 2022-06-13 23:59:10.916533
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit-test for class BaseDataProvider."""
    from mimesis.builtins import Code
    code = Code().build()
    code_ru = code.override_locale(locales.RU)
    assert code_ru == Code(seed=code.seed, locale=locales.RU)
    assert code.get_current_locale() == locales.DEFAULT_LOCALE
    assert code_ru.get_current_locale() == locales.RU

# Generated at 2022-06-13 23:59:14.752029
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
     x = BaseDataProvider()
     with x.override_locale('ru'):
         print(x.locale)
     print(x.locale)

# Generated at 2022-06-13 23:59:18.837671
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Arrange
    class Provider(BaseDataProvider):
        def get_email(self) -> str:
            return 'a@b.com'

    provider = Provider()
    # Act
    with provider.override_locale(locales.RU):
        # Assert
        assert provider.locale == locales.RU
        assert provider.get_email() == 'a@b.com'

# Generated at 2022-06-13 23:59:23.454995
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    p = BaseDataProvider()
    with pytest.raises(ValueError):
        with p.override_locale('ru'):
            pass

# Generated at 2022-06-13 23:59:32.884090
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """
    Unit test for method :meth:`BaseDataProvider.override_locale` of class :class:`BaseDataProvider`.
    """
    class SampleProvider(BaseDataProvider):
        """Sample (for unit test) provider derived from BaseDataProvider."""
        def __init__(self, locale: str = locales.EN, seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
        def test_method(self, locale: str = locales.EN):
            """Returns locale name."""
            return self.locale
    #
    # Test context manager on an instance of SampleProvider
    provider = SampleProvider()

# Generated at 2022-06-13 23:59:40.298927
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)
        def get_current_locale(self):
            return self.locale
    # Test BaseDataProvider __str__ method
    test_provider = TestDataProvider()
    assert str(test_provider) == 'TestDataProvider <en>'
    # Test BaseDataProvider get_current_locale method
    assert test_provider.get_current_locale() == 'en'
    # Test BaseDataProvider override_locale method
    with test_provider.override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'
    assert test_provider.get_current_loc

# Generated at 2022-06-13 23:59:48.910268
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class SampleProvider(BaseDataProvider):
        def get_current_locale(self) -> str:
            return self.locale

    locale_for_test_BaseDataProvider_override_locale = 'en'
    provider = SampleProvider(locale_for_test_BaseDataProvider_override_locale)
    locale = provider.get_current_locale()
    assert locale == locale_for_test_BaseDataProvider_override_locale, \
           'locale not match {0}'.format(locale_for_test_BaseDataProvider_override_locale)
    with provider.override_locale() as p:
        assert locale != p.get_current_locale(), 'locale match {0}'.format(locale)

# Generated at 2022-06-13 23:59:56.763365
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Method override_locale returns provider with overridden locale."""
    import mimesis.data.person as person

    locale = person.Person.EN
    person_instance = person.Person(locale='ru')
    with person_instance.override_locale(locale=locale) as person_en:
        assert person_en.get_current_locale() == locale
    assert person_instance.get_current_locale() == 'ru'

# Generated at 2022-06-14 00:00:27.566649
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def get_data(self):
            return self._data

    locale = locales.EN
    provider = Provider(locale)
    with provider.override_locale(locale) as provider:
        assert provider.get_data()

    with provider.override_locale(locale) as provider:
        assert provider.get_data()

    with provider.override_locale(locale + '-' + locales.RU) as provider:
        assert provider.get_data()


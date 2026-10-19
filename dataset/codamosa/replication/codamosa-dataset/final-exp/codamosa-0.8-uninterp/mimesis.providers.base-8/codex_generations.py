

# Generated at 2022-06-13 23:50:47.845312
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    class TestProvider(BaseDataProvider):
        """Test class for testing class BaseDataProvider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None):
            """Initialize attributes for data providers.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale=locale, seed=seed)

        def foo(self):
            """Return current locale for testing."""
            return self.locale

    prov = TestProvider('ru', seed=123)
    assert prov.foo() == locales.RU
    with prov.override_locale('en') as pr:
        assert pr.foo() == locales.EN

# Generated at 2022-06-13 23:50:59.979923
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of BaseDataProvider class.

    """
    from mimesis.enums import Gender, LocaleCode as LC

    class TestEnDataProvider(BaseDataProvider):

        """Test data provider for English locale."""

        def __init__(self, **kwargs):
            super().__init__(LC.EN, **kwargs)

        def get_full_name(self, gender: Gender = None):
            return 'John Doe'

    class TestRuDataProvider(BaseDataProvider):

        """Test data provider for Russian locale."""

        def __init__(self, **kwargs):
            super().__init__(LC.RU, **kwargs)

        def get_full_name(self, gender: Gender = None):
            return 'Ivan Ivanov'

    en = TestEnDataProvider()


# Generated at 2022-06-13 23:51:11.619275
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        class Meta:
            name = 'test_provider'

    tp = TestProvider()
    assert tp.locale == locales.DEFAULT_LOCALE
    assert tp.get_current_locale() == locales.DEFAULT_LOCALE

    with tp.override_locale(locales.RU) as p:
        assert p.locale == locales.RU
        assert p.get_current_locale() == locales.RU

        p.locale = 'fake_locale'
        assert p.locale == 'fake_locale'
        assert p.get_current_locale() == 'fake_locale'

    assert tp.locale == locales.DEFAULT_LOCALE
    assert tp.get_current_locale()

# Generated at 2022-06-13 23:51:16.266798
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    EN = locales.EN
    RU = locales.RU
    assert provider.get_current_locale() is EN
    with provider.override_locale(RU):
        assert provider.get_current_locale() is RU
    assert provider.get_current_locale() is EN

# Generated at 2022-06-13 23:51:22.994341
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.holidays import Holidays

    holidays_en = Holidays()
    holidays_ru = Holidays(locale='ru')
    holidays_en.get_christmas('12-25')
    holidays_ru.get_christmas('12-25')
    with holidays_en.override_locale() as holidays_en_ru:
        holidays_en_ru.get_christmas('12-25')

# Generated at 2022-06-13 23:51:38.851030
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Address
    from mimesis.providers import Person
    from mimesis.providers import Science
    from tests.utils import TestDataProvider

    with TestDataProvider().override_locale('ru-RU'):
        address = Address(seed=None)
        person_ru = Person(seed=None)
        science_ru = Science(seed=None)

    with TestDataProvider().override_locale('en-US'):
        person_en = Person(seed=None)
        science_en = Science(seed=None)


# Generated at 2022-06-13 23:51:43.216685
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.person import Person
    person = Person()
    info = person.info()

    with person.override_locale(locales.PT):
        info_pt = person.info()
        assert info != info_pt

    info_en = person.info()
    assert info == info_en



# Generated at 2022-06-13 23:51:51.117970
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from typing import Any, Dict, Generator, Literal
    from mimesis.providers.base import BaseDataProvider
    class TestBaseDataProvider(BaseDataProvider):
        _datafile = 'test'
        def __init__(self, seed: Seed = None) -> None:
            super().__init__(seed=seed)
        def _pull(self, datafile: str = '') -> None:
            super()._pull(datafile)
        @functools.lru_cache(maxsize=None)
        def get_data(self, key: str) -> Any:
            try:
                return self._data[key]
            except KeyError:
                return self._data['en'][key]
    locale: Literal[locales.LOCALES['es'], locales.LOCALES['pt']]


# Generated at 2022-06-13 23:51:53.452366
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data_provider = BaseDataProvider()
    with data_provider.override_locale('ru'):
        assert data_provider.get_current_locale() == 'ru'
    assert data_provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:51:55.690058
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Locale
    data_provider = Locale()
    with data_provider.override_locale(locales.RU):
        assert data_provider.locale == locales.RU
    assert data_provider.locale == locales.EN

# Generated at 2022-06-13 23:52:11.602364
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        pass

    locale = 'en'
    provider = TestProvider(locale=locale)
    assert provider.get_current_locale() == locale

    provider.override_locale('ru')
    assert provider.get_current_locale() == 'ru'

    with provider.override_locale('en') as p:
        assert p.get_current_locale() == 'en'
    assert provider.get_current_locale() == 'ru'


# Generated at 2022-06-13 23:52:25.082944
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def _pull(self, datafile: str = '') -> None:
            locale = self.locale
            self._data = locale

    provider = TestProvider()

    with provider.override_locale(locales.EN):
        assert provider.locale == locales.EN
        assert provider._data == locales.EN

    with provider.override_locale(locales.DE):
        assert provider.locale == locales.DE
        assert provider._data == locales.DE

    with provider.override_locale(locales.DE_BY):
        assert provider.locale == locales.DE_BY
        assert provider._data == locales.DE_BY

    with provider.override_locale(locales.DE_CH):
        assert provider.locale == local

# Generated at 2022-06-13 23:52:36.614557
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    class MyDataProvider(BaseDataProvider):

        def __init__(self, locale=locales.EN, seed=None, override_locale=None):
            super().__init__(locale, seed=seed)
            if override_locale:
                self._override_locale(override_locale)

        @property
        def value(self):
            return self.get_current_locale()

    provider = MyDataProvider(
        override_locale=locales.RU)
    with provider.override_locale(locales.DE):
        assert provider.value == provider.EN
    assert provider.value == provider.RU

# Generated at 2022-06-13 23:52:42.297953
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Testing method override_locale of class BaseDataProvider.

    Testing the context manager. Function raise exception
    when context will not created.
    """
    # Initial data
    locale = locales.RU
    class TestProvider(BaseDataProvider):
        _datafile = 'builtins.json'

        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

        def get_test_data(self) -> Dict[str, str]:
            """Get test data."""
            data = self._data
            return data

    provider = TestProvider(locale='en')

    # Actual data
    with provider.override_locale(locale):
        actual = provider.get_test_data()

# Generated at 2022-06-13 23:52:48.491218
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person

    en = Person('en')
    ru = Person('ru')
    with en.override_locale('ru') as person:
        assert en.get_full_name() == ru.get_full_name()
        assert person.get_full_name() == ru.get_full_name()
    assert en.get_full_name() != ru.get_full_name()

# Generated at 2022-06-13 23:52:53.291108
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()

    with provider.override_locale('ru'):
        assert provider.locale == 'ru'

    assert provider.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:55.386013
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    base = BaseDataProvider()
    with base.override_locale(locale='de-DE') as provider:
        assert provider.locale == 'de-de'



# Generated at 2022-06-13 23:53:01.639391
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    l = BaseDataProvider()

    with l.override_locale(locales.EN):
        assert l.get_current_locale() == locales.EN

    with l.override_locale(locales.RU):
        assert l.get_current_locale() == locales.RU

    assert l.get_current_locale() not in [locales.RU, locales.EN]

# Generated at 2022-06-13 23:53:11.084213
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Verify the method override_locale of class BaseDataProvider."""
    from mimesis.providers.address import Address
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.internet import Internet
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.person import Person

    address = Address(seed=1)
    datetime = Datetime(seed=1)
    internet = Internet(seed=1)
    numbers = Numbers(seed=1)
    person = Person(seed=1)

    with address.override_locale(locales.EN):
        name = person.full_name()
        block = numbers.hexadecimal(upper=True, number_type=str)
        country = address.country()
        city = address.city

# Generated at 2022-06-13 23:53:21.333892
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person(locale='en')
    with person.override_locale('ru') as ru_persons:
        assert ru_persons.get_current_locale() == 'ru'
        assert ru_persons.full_name(gender=Gender.FEMALE) != ''

    with person.override_locale():
        assert person.full_name(gender=Gender.FEMALE) != ''
        assert person.get_current_locale() == 'en'

    with person.override_locale('ru_RU'):
        assert person.full_name(gender=Gender.FEMALE) != ''
        assert person.get_current_locale() == 'ru_RU'

# Generated at 2022-06-13 23:53:32.171056
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeDataProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)

    fdp = FakeDataProvider()
    ctx1 = fdp.override_locale('ru')
    assert ctx1 is not None
    
    ctx2 = ctx1.override_locale('en')
    assert ctx2 is not None

# Generated at 2022-06-13 23:53:34.851267
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Use context manager for override locale."""

    class ExampleProvider(BaseDataProvider):
        """Example provider."""

    provider = ExampleProvider()
    with provider.override_locale(locale=locales.RU):
        assert provider.get_current_locale() == locales.RU

# Generated at 2022-06-13 23:53:41.288616
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Override locale in context manager."""
    class DataProvider(BaseDataProvider):
        def get_data(self, key) -> Any:
            return self._data.get(key)

    p = DataProvider(locale='en')
    assert p.get_data('a') == 1

    with p.override_locale('ru') as p_ru:
        assert p_ru.get_data('a') == 2

    assert p.get_data('a') == 1

    with p.override_locale('ru') as p_ru:
        assert p_ru.get_data('a') == 2

    assert p.get_data('a') == 1

    with p.override_locale('en') as p_en:
        assert p_en.get_data('a') == 1


# Generated at 2022-06-13 23:53:46.009400
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass
#test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:53:53.299305
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    dp = BaseDataProvider()
    with dp.override_locale(locales.RU) as _dp:
        assert dp == _dp
        assert dp.locale == locales.RU
        assert _dp.locale == locales.RU
    assert dp.locale == locales.EN

# Generated at 2022-06-13 23:53:56.415248
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    """
    :return:
    """
    foo = BaseDataProvider()
    with foo.override_locale('ru'):
        assert 'ru' == foo.get_current_locale() and 'en' != foo.get_current_locale()

# Generated at 2022-06-13 23:54:06.220671
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Address
    from mimesis.enums import Gender
    from mimesis.typing import Locale

    ad = Address()

    with ad.override_locale(locale=Locale('ru')):
        assert ad.locale == Locale('ru')
        assert ad.full_name(gender=Gender.FEMALE) == 'Варвара Довжина'
        assert ad.full_name(gender=Gender.MALE) == 'Гаврила Загробнов'

    with ad.override_locale('en'):
        assert ad.locale == Locale('en')
        assert ad.full_

# Generated at 2022-06-13 23:54:15.454130
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Person(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'person.json'
            self._pull()

        @property
        def full_name(self) -> str:
            return self.random.choice(self._data['name'])
    with Person(locale='ru') as person:
        assert person.full_name == 'Иван Алексеевич Ананьев'
    with person.override_locale(locale='en') as en_person:
        assert en_person.full_name == 'Ivan A.'

# Generated at 2022-06-13 23:54:29.857317
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale='en')

    with provider.override_locale('ru') as provider_wrapper:
        assert provider_wrapper.get_current_locale() == 'ru'
    assert provider.get_current_locale() == 'en'

    try:
        with provider.override_locale('ru') as provider_wrapper:
            assert provider_wrapper.get_current_locale() == 'ru'
            with provider.override_locale('apa') as nested_provider_wrapper:
                assert nested_provider_wrapper.get_current_locale() == 'apa'
            assert provider_wrapper.get_current_locale() == 'ru'
        assert provider.get_current_locale() == 'en'
    except AttributeError:
        pass

# Generated at 2022-06-13 23:54:41.243839
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''
    Unit test for method override_locale of class BaseDataProvider
    :return: None
    '''

    class _Test(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None):
            self._datafile = 'dataprovider.json'
            super().__init__(locale, seed)

        def boolean(self) -> bool:
            return self.random.boolean()

    test = _Test()

    try:
        with test.override_locale('ru'):
            assert test.boolean()
        with test.override_locale(locales.EN):
            assert test.boolean()
    except ValueError as e:
        print("Exception occured and caught\n{}".format(e))

# Generated at 2022-06-13 23:54:53.349178
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis.builtins
    with mimesis.builtins.Person('ru').override_locale('ru') as p:
        assert str(p) == \
            '<BuiltinsPerson <ru>>'
        with p.override_locale('en') as p_en:
            assert str(p_en) == \
                '<BuiltinsPerson <en>>'


# Generated at 2022-06-13 23:55:00.697328
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the property ``override_locale`` of class ``BaseDataProvider``."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    with Person('en_GB').override_locale('en_US') as locale_person:
        assert locale_person.gender(Gender.FEMALE) == 'Female'


# Generated at 2022-06-13 23:55:07.642406
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code
    from mimesis.exceptions import UnsupportedLocale

    # Arrange
    provider = Code()

    # Act
    with provider.override_locale() as code:
        assert type(code) == Code
        assert code.locale == locales.DEFAULT_LOCALE

    # Assert
    with pytest.raises(UnsupportedLocale):
        with provider.override_locale('non-existent-locale'):
            pass

# Generated at 2022-06-13 23:55:17.001452
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    global current_locale
    global origin_locale

    from mimesis.enums import Gender
    from mimesis.providers import Address

    current_locale = 'en-US'
    origin_locale = current_locale

    address = Address(current_locale)

    with address.override_locale('en') as en_address:
        assert 'en' == en_address.get_current_locale()
        assert address.get_current_locale() == origin_locale

    assert address.get_current_locale() == current_locale

    # Unit test without context manager
    with address.override_locale('en') as en_address:
        assert 'en' == en_address.get_current_locale()
        assert address.get_current_locale() == origin_loc

# Generated at 2022-06-13 23:55:25.766689
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Personal
    from mimesis.exceptions import UnsupportedLocale
    from mimesis.typing import Locale

    personal = Personal()
    with personal.override_locale('lv'):
        new_locale = personal.get_current_locale()
        assert personal.full_name() != 'Arturs Dubra'
        assert new_locale == 'lv'

    # Raise UnsupportedLocale when locale not supported
    with pytest.raises(UnsupportedLocale):
        _ = personal.override_locale().__enter__()

    # Raise ValueError when locale-dependent provider do not have locale

# Generated at 2022-06-13 23:55:38.746140
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import FruitProvider
    from mimesis.typing import Locale, Pattern

    provider = FruitProvider()
    with provider.override_locale(locale=locales.JA):
        assert provider.get_current_locale() == locales.JA

    with provider.override_locale(locale=locales.DE):
        assert provider.get_current_locale() == locales.DE

    with provider.override_locale(locale=locales.DE):
        assert provider.get_current_locale() == locales.DE

    provider.reseed(seed=1)
    assert provider.random.get_seed() == 1

    provider.reseed(seed=None)
    assert provider.random

# Generated at 2022-06-13 23:55:49.415816
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code
    from mimesis.enums import Gender
    from mimesis.providers.code import CodeSpecification
    from mimesis.providers.person import PersonSpecification
    from mimesis.providers.person.en import Person as ENProvider
    from mimesis.providers.person.ru import Person as RUPersonProvider

    provider = ENProvider('ru')

    def test():
        """Test."""
        return provider.name(gender=Gender.FEMALE)

    assert test() == 'Анестасия'

    with provider.override_locale('ru'):
        assert test() == 'Ирина'

    assert test() == 'Анестасия'

    code = Code('ru')
    code

# Generated at 2022-06-13 23:55:59.549552
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Setup
    from mimesis.providers.address import Address
    from mimesis.providers.personal import Person

    p1 = Person(locale='ru')
    p2 = Person(locale='ru')

    # Execute
    with p1.override_locale('en'):
        with p2.override_locale('ru'):
            assert p1.full_name() == 'Virginia M. Hansen'
            assert p2.full_name() == 'Максим Фёдоров'

    with Person(seed=1000, locale='ru').override_locale('en'):
        assert Person(seed=1000, locale='en').full_name() == 'Raymond A. Mills'

# Generated at 2022-06-13 23:56:03.810968
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class A(BaseDataProvider):
        def __init__(self, locale, seed=None):
            super().__init__(locale, seed)
            self._datafile = 'test.json'

    a = A('en')

    with a.override_locale('zh'):
        assert a.get_current_locale() != 'en'

    assert a.get_current_locale() == 'en'

# Generated at 2022-06-13 23:56:08.001835
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    with BaseDataProvider().override_locale(locales.RU) as provider:
        assert provider.get_current_locale() == locales.RU

# Generated at 2022-06-13 23:56:29.129132
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale=locales.EN)
    locale = locales.RU
    with provider.override_locale(locale):
        assert provider.locale == locale
    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:56:34.948111
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address

    address = Address(seed=1)
    with address.override_locale('ru') as ru_address:
        assert ru_address.postal_code() == '666118'
    with address.override_locale() as ru_address:
        assert ru_address.postal_code() == '666118'

# Generated at 2022-06-13 23:56:36.771675
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    with BaseDataProvider(locale='en').override_locale('ru') as p:
        assert p.locale == 'ru'
    assert p.locale == 'en'

# Generated at 2022-06-13 23:56:42.865701
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Locale

    with Locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'
        provider.get_current_locale() == 'ru'

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:56:55.118644
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    fake = BaseDataProvider()
    with fake.override_locale(locales.EN) as fake_en:
        assert fake_en.get_current_locale() == locales.EN

    with fake.override_locale(locales.RU) as fake_ru:
        assert fake_ru.get_current_locale() == locales.RU
        assert fake.get_current_locale() == locales.EN

    with fake.override_locale(locales.RU) as fake_ru:
        assert fake_ru.get_current_locale() == locales.RU
        with fake.override_locale(locales.BE) as fake_be:
            assert fake_be.get_current_locale()

# Generated at 2022-06-13 23:57:01.538978
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class TestData(BaseDataProvider):
        def __init__(self):
            self._datafile = 'test.json'
            super().__init__()
        def get_data(self):
            return self._data

    data_provider = TestData()

    with data_provider.override_locale(locales.EN) as provider:
        assert provider.get_current_locale() == 'en'

    assert data_provider.get_current_locale() != 'en'



# Generated at 2022-06-13 23:57:13.531154
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class Foo(BaseDataProvider):
        def __init__(self, locale=locales.EN, seed=None):
            super().__init__(locale=locale, seed=seed)
        def from_en(self): return self.locale == locales.EN
        def from_ru(self): return self.locale == locales.RU

    foo = Foo()
    assert foo.from_en()
    with foo.override_locale(locales.RU) as f:
        assert f.from_ru()
    assert foo.from_en()

# Generated at 2022-06-13 23:57:23.278804
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale='ru')
    locale = provider.get_current_locale()

    assert locale == 'ru'

    with provider.override_locale('uk'):
        locale = provider.get_current_locale()

    assert locale == 'ru'

    with provider.override_locale('uk') as prv:
        assert prv.get_current_locale() == 'uk'

    assert provider.get_current_locale() == 'ru'

    with provider.override_locale('uk') as prv:
        assert prv.get_current_locale() == 'uk'

    assert provider.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:57:34.550118
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.locale = 'en'
        def get_current_locale(self):
            return getattr(self, 'locale', locales.DEFAULT_LOCALE)
    test = Test()
    assert test.get_current_locale() == 'en'
    try:
        with test.override_locale('ru'):
            assert test.get_current_locale() == 'ru'
            raise Exception('Some exception')
    except Exception:
        pass
    assert test.get_current_locale() == 'en'

# Generated at 2022-06-13 23:57:37.741265
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # lint:disable=missing-params
    # TODO: Implement test for BaseDataProvider._override_locale
    pass

# Generated at 2022-06-13 23:58:18.914688
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class A(BaseDataProvider):
        def __init__(self, locale, seed=None):
            super().__init__(locale, seed)

        def get_current_locale(self):
            return self.locale

    def get_test_locale():
        return locales.JP

    a = A(locale=locales.EN)

    with a.override_locale(locales.JP):
        assert a.get_current_locale() is get_test_locale()

    assert a.get_current_locale() != get_test_locale()

# Generated at 2022-06-13 23:58:29.933799
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def get_name(self, key: str) -> str:
            names = self._data['first_names']
            return names[key]

    p = Provider(locale='ru')
    assert p.get_name('male') == 'Абрам'
    assert p.get_name('female') == 'Августа'

    with p.override_locale('en') as p:
        assert p.get_name('male') == 'Adam'
        assert p.get_name('female') == 'Augusta'

    assert p.get_name('male') == 'Абрам'
    assert p.get_name('female') == 'Августа'


# Generated at 2022-06-13 23:58:35.645881
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeDataProvider(BaseDataProvider):

        def get_current_locale(self) -> str:
            return 'en'

    with FakeDataProvider().override_locale('ru') as provider:
        assert provider

    with FakeDataProvider().override_locale('ru') as provider:
        assert provider



# Generated at 2022-06-13 23:58:41.099778
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    foo = BaseProvider()
    with foo.override_locale('en'):
        assert foo.get_current_locale() == 'en'
    with foo.override_locale('es'):
        assert foo.get_current_locale() == 'es'



# Generated at 2022-06-13 23:58:51.251947
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale=locales.EN, seed=None):
            super().__init__(locale, seed)

        def test_method(self):
            return self.get_current_locale()

        def __str__(self):
            super().__str__()

    test_provider = TestProvider()
    assert test_provider.test_method() == 'en'

    with test_provider.override_locale('ru') as test_provider:
        assert test_provider.test_method() == 'ru'

    assert test_provider.test_method() == 'en'

test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:59:04.441002
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the ``override_locale`` method of ``BaseProvider``."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person()
    sub_person = Person()

    assert person.gender() in Gender
    assert person.gender(Gender.FEMALE) == Gender.FEMALE
    assert sub_person.gender() == Gender.MALE
    assert sub_person.gender(Gender.FEMALE) == Gender.FEMALE

    with person.override_locale('ru') as provider:
        assert person.gender() == Gender.FEMALE
        assert sub_person.gender() == Gender.MALE
        assert sub_person.gender(Gender.FEMALE) == Gender.FEMALE

    assert person.gender() in Gender
    assert person.gender

# Generated at 2022-06-13 23:59:07.839854
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    with Person.override_locale('en'):
        assert Person().get_current_locale() == 'en'
    with Person.override_locale('ru'):
        assert Person().get_current_locale() == 'ru'


# Generated at 2022-06-13 23:59:13.844508
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class BaseDataProviderMock(BaseDataProvider):
        """Mock class for BaseDataProvider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes for data providers.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale=locale, seed=seed)
            self._data: JSON = {}
            self._datafile = ''
            self._setup_locale(locale)
            self._data_dir = Path(__file__).parent.parent.joinpath('data')

        def __str__(self) -> str:
            """Human-readable representation of locale."""
            return self.__class__.__name__

       

# Generated at 2022-06-13 23:59:20.459875
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test_data.json'
            self._pull(self._datafile)

    test_provider = TestProvider(locale='ru')
    origin_locale = test_provider.get_current_locale()
    with test_provider.override_locale(locale="en") as _:
        override_locale = _.get_current_locale()

    assert origin_locale == 'ru'
    assert override_locale == 'en'

# Generated at 2022-06-13 23:59:26.041834
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from .region import Region

    ru_region = Region(locale=locales.RU)
    with ru_region.override_locale(locales.EN):
        assert ru_region.get_current_locale() == locales.EN
    assert ru_region.get_current_locale() == locales.RU
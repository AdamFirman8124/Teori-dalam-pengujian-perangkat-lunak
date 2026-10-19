

# Generated at 2022-06-13 23:50:49.284800
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bdp = BaseDataProvider()
    
    assert bdp.get_current_locale() == locales.EN
    
    with bdp.override_locale(locales.RU) as ru_bdp:
        assert ru_bdp.get_current_locale() == locales.RU
        
    assert ru_bdp.get_current_locale() == locales.EN
    
    with bdp.override_locale(locales.FR) as fr_ru_bdp:
        fr_ru_bdp.get_current_locale() == locales.FR
        
        with fr_ru_bdp.override_locale(locales.RU) as ru_bdp:
            assert ru_bdp.get_current_locale() == locales.RU
        


# Generated at 2022-06-13 23:50:53.505530
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data_provider = BaseDataProvider()
    with data_provider.override_locale('pt_BR') as data_provider:
        assert isinstance(data_provider._data, dict)
        assert data_provider.get_current_locale() == 'pt_BR'
    assert data_provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:50:59.269006
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    p = Person(seed=100)
    with p.override_locale('es') as _:
        assert p.name(gender=Gender.MALE) == 'Benicio'
        assert _.name(gender=Gender.MALE) == 'Benicio'

# Generated at 2022-06-13 23:51:04.080632
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data = BaseDataProvider(locale="en")
    with data.override_locale("es") as f:
        assert str(f) == "BaseDataProvider <es>" #!
    assert str(data) == "BaseDataProvider <en>" #!

# Generated at 2022-06-13 23:51:09.881704
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.providers import Generic

    # There is no need to test all providers, it is enough to test the base
    provider = Generic()
    locale = 'ru'
    with provider.override_locale(locale):
        assert provider.locale == locale
    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:51:13.497710
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    dataprovider = BaseDataProvider()
    try:
        with dataprovider.override_locale():
            assert True
    except ValueError:
        assert True
    except:
        assert False

# Generated at 2022-06-13 23:51:22.222575
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.person import Person
    import pytest
    from testtools import call_with, get_locale, get_random_locale
    for i in range(50):
        with Person(seed=i).override_locale(get_locale(i)) as p:
            assert p.locale == get_locale(i)
    with pytest.raises(ValueError):
        with Person().override_locale(get_random_locale()):
            pass


# Generated at 2022-06-13 23:51:29.568369
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class Provider(BaseDataProvider):

        def __init__(self, locale=locales.EN, *args, **kwargs):
            super().__init__(locale=locale, *args, **kwargs)

        def get_provider(self):
            return self.__class__.__name__

    provider = Provider()
    with provider.override_locale(locales.RU) as p:
        assert p.get_provider() == 'Provider'
        assert p._data['currency']['code'] == 'руб.'

    assert provider.get_provider() == 'Provider'
    assert provider._data['currency']['code'] == 'руб.'


# Generated at 2022-06-13 23:51:38.516915
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Address
    address = Address()
    with address.override_locale(locales.DEFAULT_LOCALE) as addr:
        assert address.locale == address.get_current_locale()
        assert addr.locale == addr.get_current_locale()
    assert address.locale != address.get_current_locale()
    with address.override_locale('la') as addr:
        city = addr.city()
        assert city == 'Romae'
        assert address.locale == address.get_current_locale()
        assert addr.locale == addr.get_current_locale()


# Generated at 2022-06-13 23:51:39.319374
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Find a way to test overridden locale
    pass

# Generated at 2022-06-13 23:51:55.550835
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data = BaseDataProvider()
    with data.override_locale('ru') as data:
        assert data.get_current_locale() == 'ru'
    assert data.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:03.071382
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Person

    with Person().override_locale('en') as en_person:
        assert isinstance(en_person, Person)
        assert en_person.locale == 'en'
        assert en_person.full_name() != ''

    with Person().override_locale('ru') as ru_person:
        assert isinstance(ru_person, Person)
        assert ru_person.locale == 'ru'
        assert ru_person.full_name() != ''


# Generated at 2022-06-13 23:52:11.885727
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(seed=0)

    message = 'AttributeError: «BaseDataProvider» has not locale dependent'

    # Check if AttributeError is raised when locale isn't provided
    try:
        with provider.override_locale() as foo:
            pass
    except ValueError as e:
        assert str(e) == message

    # Check if provider's locale changes inside context manager
    with provider.override_locale(locale='ru') as foo:
        assert foo.locale == 'ru'

    # Check if provider's locale changes outside context manager, too
    assert provider.locale == 'ru'

# Generated at 2022-06-13 23:52:25.251046
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers import Address
    from mimesis.providers import Business
    from mimesis.providers import Code
    from mimesis.providers import Person
    person = Person('ru')
    person.seed(198)
    person_code = Code('ru')
    person_code.seed(198)
    address = Address('ru')
    address.seed(198)
    business = Business('ru')
    business.seed(198)

    assert person.full_name(gender=Gender.FEMALE) == 'Валерия Руденко'
    assert person_code.postal_code() == '061770'
    assert address.street_name() == 'Северный'


# Generated at 2022-06-13 23:52:28.901881
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider override_locale."""




# Generated at 2022-06-13 23:52:33.488159
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MockProvider(BaseDataProvider):
        def foo(self, locale=locales.RU):
            with self.override_locale(locale) as provider:
                assert provider.locale == locale

    provider = MockProvider()
    provider.foo()

# Generated at 2022-06-13 23:52:36.574513
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Cls(BaseDataProvider):
        pass

    provider = Cls()
    with provider.override_locale('ru'):
        assert provider.locale == 'ru'
    assert provider.locale != 'ru'

# Generated at 2022-06-13 23:52:46.065474
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert BaseDataProvider.override_locale.__name__ == 'contextmanager'
    assert BaseDataProvider.override_locale.__qualname__ == 'BaseDataProvider.override_locale'
    assert BaseDataProvider(locale='en').override_locale('en').get_current_locale() == 'en'
    assert BaseDataProvider(locale='en').override_locale().get_current_locale() == 'en'
    assert BaseDataProvider(locale='ru').override_locale().get_current_locale() == 'ru'
    assert BaseDataProvider(locale='ru').override_locale('en').get_current_locale() == 'en'

# Generated at 2022-06-13 23:52:54.237251
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestLocale(BaseDataProvider):
        def __init__(self, locale, seed=None):
            super().__init__(locale=locale, seed=seed)

        def get_full_name(self):
            return self.locale

    test = TestLocale('uk')
    with test.override_locale('ru'):
        assert test.get_full_name() == 'ru'

    assert test.get_full_name() == 'uk'

# Generated at 2022-06-13 23:52:59.350838
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale."""
    class Foo(BaseDataProvider):
        """Test class."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            """Initialize attributes."""
            super().__init__(locale=locale)

        def provide(self) -> str:
            """Get locale."""
            return self.locale

    f = Foo()
    assert f.provide() == locales.DEFAULT_LOCALE

    with f.override_locale('ru'):
        assert f.provide() == 'ru'

    assert f.provide() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:53:28.210230
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test class BaseDataProvider method override_locale."""
    from mimesis.builtins import Gender

    class TestProvider(BaseDataProvider):
        """Test class for BaseDataProvider"""

        def __init__(self, locale: str = 'en',
                     seed: Seed = None):
            super().__init__(locale, seed)
            self._datafile = 'test.json'
            self._pull()

        def get_gender(self) -> str:
            """Get gender."""
            return 'male'

        def get_gender_en(self) -> str:
            """Get gender."""
            return 'female'

        def get_gender_ru(self) -> str:
            """Get gender."""
            return 'male'

    provider = TestProvider(locale='ru')

    assert provider.get_gender

# Generated at 2022-06-13 23:53:33.747313
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.geo import Geography
    from mimesis.providers.internet import Internet
    from mimesis.providers.identifiers import Identifiers

    data_provider = Datetime(seed=42)
    data_provider.seed = 42
    data_provider._update_locale('ru')

    assert data_provider.locale == 'ru'
    num = Numbers()._validate_enum(None, numbers.Weekday)
    assert num == 1

    geo = Geography(seed=42)
    with geo.override_locale('ru'):
        geo.locale.split('.').pop(0)
        geo.locale = 'ru'


# Generated at 2022-06-13 23:53:40.468925
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.person import Person

    person_en = Person('en')
    person_ru = Person('ru')
    person_de = Person('de')

    assert person_en.get_current_locale() == 'en'
    assert person_ru.get_current_locale() == 'ru'
    assert person_de.get_current_locale() == 'de'

    with person_en.override_locale('ru') as person:
        assert person.get_current_locale() == 'ru'

    with person_ru.override_locale('de') as person:
        assert person.get_current_locale() == 'de'


# Generated at 2022-06-13 23:53:45.750426
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()

    with provider.override_locale('en'):
        assert provider.get_current_locale() == 'en'

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:53:47.147500
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale='ru')
    assert provider.get_current_locale() == 'ru'


# Generated at 2022-06-13 23:53:57.739443
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    
    from mimesis.data import CurrencyCodes
    from mimesis.enums import Currency, CurrencyCodes as EnumCode
    
    cc = CurrencyCodes()
    assert cc.get_current_locale() == 'en'
    
    # test with currency enum
    with cc.override_locale('ru') as new_cc:
        assert new_cc.get_current_locale() == 'ru'
        assert new_cc.currency(currency=Currency.RUBLE) == 'RUB'
    assert cc.get_current_locale() == 'en'
    assert cc.currency(currency=Currency.RUBLE) == 'RUB'
    
    # test without enum
    with cc.override_locale('ru') as new_cc:
        assert new_

# Generated at 2022-06-13 23:54:02.005507
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)
            self.locale = locale
            self.data = {'en': 'test', 'ru': 'тест'}
        def get_data(self):
            return self.data.get(self.locale)

    provider = TestProvider()
    assert provider.get_data() == 'test'
    with provider.override_locale(locales.RU):
        assert provider.get_data() == 'тест'

# Generated at 2022-06-13 23:54:11.376099
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class ProviderWithLocale(BaseDataProvider):
        def __init__(self, locale: str = locales.EN) -> None:
            super().__init__(locale=locale)

    provider = ProviderWithLocale()
    assert provider.get_current_locale() == locales.EN

    with provider.override_locale(locales.CS) as provider:
        assert provider.get_current_locale() == locales.CS

    assert provider.get_current_locale() == locales.EN


# Generated at 2022-06-13 23:54:19.717604
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, seed: Seed = None, locale: str = None):
            super().__init__(seed=seed, locale=locale)

    provider = TestProvider(locale='ru')

    with provider.override_locale('en_US') as p:
        assert p.get_current_locale() == 'en_US'
        assert p.locale == 'en_US'

    assert provider.get_current_locale() == 'ru'
    assert provider.locale == 'ru'

# Generated at 2022-06-13 23:54:28.173051
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider1 = BaseDataProvider('en')
    # print(provider1.get_current_locale())
    with provider1.override_locale(locale='ru'):
        # print(provider1.get_current_locale())
        pass
    # print(provider1.get_current_locale())
    # assert provider1.get_current_locale() == 'en'


if __name__ == '__main__':
    test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:55:11.914457
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.datetime import Datetime
    from mimesis.builtins import en, ru

    dt = Datetime()

    with dt.override_locale('ru') as ru_provider:
        assert ru_provider.get_current_locale() == 'ru'

    assert dt.get_current_locale() == 'en'

    with ru_provider.override_locale('en') as en_provider:
        assert en_provider.get_current_locale() == 'en'

    assert ru_provider.get_current_locale() == 'ru'

    en_provider = en.Datetime()
    ru_provider = ru.Datetime()

    assert en_provider.get_current_locale() == 'en'
    assert ru_

# Generated at 2022-06-13 23:55:19.019889
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Region

    provider = Region()
    with provider.override_locale('ru') as ru:
        assert ru.get_current_locale() == 'ru'
        assert ru.province() == 'Татарстан'
        assert ru.province() == 'Республика Кабардино-Балкария'

    assert provider.get_current_locale() == 'en'
    assert provider.province() == 'North Dakota'
    assert provider.province() == 'Kentucky'

# Generated at 2022-06-13 23:55:27.373267
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Check method override_locale of class BaseDataProvider."""
    class TestDataProvider(BaseDataProvider):

        _datafile = 'test.json'

        def __init__(self, locale='en') -> None:
            super().__init__(locale)

        def get_some_data(self) -> Dict[str, int]:
            return self._data

    provider = TestDataProvider()

    with provider.override_locale('en') as test_provider:
        result = test_provider.get_some_data()
        assert result == {'hi': 1}

    with provider.override_locale('ru') as test_provider:
        result = test_provider.get_some_data()
        assert result == {'hi': 2}


# Generated at 2022-06-13 23:55:40.888173
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import (
        Address,
        Person,
    )

    locale = 'ru'
    assert locale in locales.SUPPORTED_LOCALES

    with BaseDataProvider(locale=locale).override_locale('en'):
        p = Person('en')
        per_en = p.full_name()

    with BaseDataProvider(locale=locale).override_locale('ru'):
        p = Person('ru')
        per_ru = p.full_name()

    assert per_en != per_ru

    with Address('en').override_locale('ru'):
        a = Address('ru')
        address_ru = a.address()

    a = Address('ru')
    address_ru_locale = a.address()
    assert address_ru_

# Generated at 2022-06-13 23:55:46.487401
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Unit test for method override_locale of class BaseDataProvider
    class TestProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None) -> None:
            super().__init__(locale=locale, seed=seed)
        @property
        def lorem(self):
            return self._data['lorem']
    provider = TestProvider(locale='uk_UA')
    with provider.override_locale('ru_RU') as p:
        assert p.lorem == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    assert provider.lorem != 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'

# Generated at 2022-06-13 23:55:55.493258
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit-test for BaseDataProvider.override_locale()."""
    from mimesis.providers.address import Address

    address_ru = Address(locale='ru')
    with address_ru.override_locale(locale='de') as address:
        assert address.locale == 'de'
        assert address.state() == 'Berlin'
    assert address_ru.locale == 'ru'

    from mimesis.providers.builtins import Builtins

    Builtins()


if __name__ == '__main__':
    test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:56:03.936184
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale in class BaseDataProvider."""
    class TestProvider(BaseDataProvider):
        """TestProvider."""

        def get_current_locale(self) -> str:
            """Get current locale.

            :return: Current locale.
            """
            return self.locale
    test_provider = TestProvider()
    with test_provider.override_locale('be') as p:
        assert p.get_current_locale() == locales.BE
    assert test_provider.get_current_locale() == locales.EN


# Generated at 2022-06-13 23:56:08.839500
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    print(BaseDataProvider)
    print(BaseDataProvider())
    print(BaseDataProvider())
    print(BaseDataProvider.override_locale)
    print(dir(BaseDataProvider))

if __name__ == '__main__':
    test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:56:12.322068
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    my_Dict = BaseDataProvider(locale='ru').override_locale('en')
    assert my_Dict.get_current_locale() == 'en'


# Generated at 2022-06-13 23:56:15.615949
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    bu = BaseDataProvider()
    with bu.override_locale(locale='kk') as foo:
        assert foo.locale == 'kk'

    assert bu.locale == 'en'
    return



# Generated at 2022-06-13 23:57:38.498979
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def __init__(self, locale: str = 'en', seed: Seed = None) -> None:
            self._datafile = 'test.json'
            super().__init__(locale=locale, seed=seed)

    t = Test()
    with t.override_locale('ru'):
        assert t.get_current_locale() == locales.RU
    assert t.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:57:52.987778
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.internet import Internet
    from mimesis.providers.person import Person
    from mimesis.providers.address import Address
    
    internet = Internet(seed=4)
    person = Person(locale='zh')
    address = Address(locale='tr')
    
    # Change Internet and Person
    with person.override_locale('ru'):
        with internet.override_locale('ru'):
            # Person generate Russian (ru) names
            assert person.last_name() == 'Винокурова'
            # Internet generate Russian (ru) domains
            assert internet.email() == 'Калинина.Рамиль@mail.ru'

    # Change Person and Address

# Generated at 2022-06-13 23:58:01.106731
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DataProvider(BaseDataProvider):
        @staticmethod
        def get_country_flag_emoji(country: str = None):
            return country if country else 'Russia'
    current_provider = DataProvider()
    with current_provider.override_locale('de') as provider_de:
        assert provider_de.get_country_flag_emoji(
            'Germania') == 'Germania'
    assert current_provider.get_country_flag_emoji() == 'Russia'

# Generated at 2022-06-13 23:58:11.628861
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    loader = locales.get_locale_loader(locales.DEFAULT_LOCALE)
    DataProvider = BaseDataProvider.__class__
    provider = DataProvider(locale=locales.EN)

    en_provider = loader('en')
    with provider.override_locale(locales.EN) as _provider:
        en_provider.validate_enum(locales.DEFAULT_LOCALE, locales.SUPPORTED_LOCALES)
        en_provider.validate_enum(_provider.locale, locales.SUPPORTED_LOCALES)

    ru_provider = loader('ru')

# Generated at 2022-06-13 23:58:14.706737
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        pass
    test = Test(locale='cs')
    with test.override_locale('en') as t:
        assert t.get_current_locale() == 'en'
    assert test.get_current_locale() == 'cs'

# Generated at 2022-06-13 23:58:22.998845
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Check BaseDataProvider.override_locale"""
    from mimesis.providers import Person

    en_person = Person(locale='en')
    fr_person = Person(locale='fr')

    assert en_person.locale == locales.EN
    assert fr_person.locale == locales.FR

    with en_person.override_locale(locale=locales.FR) as new_person:
        assert new_person.get_current_locale() == locales.FR
        assert new_person.locale == locales.FR
        assert en_person.locale == locales.EN
        assert en_person.get_current_locale() == locales.EN

        assert new_person.full_name() == fr_person.full_name()
        assert new_person.name()

# Generated at 2022-06-13 23:58:30.826735
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Setup
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                seed: Seed = None):
            super().__init__(locale, seed)
        def get_current_locale(self):
            return self.locale

    provider = TestProvider()

    locale = 'ru'

    # Exercise
    with provider.override_locale(locale):
        locale_ru = provider.get_current_locale()

    # Verify
    assert locale_ru == locale

    # Cleanup - none

# Generated at 2022-06-13 23:58:38.693455
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.utils import Constant
    from mimesis import locales
    from mimesis.exceptions import NonEnumerableError, UnsupportedLocale
    from mimesis.providers import Address, AddressItem, AddressCode, \
        Person, PersonItem, PersonTitle, PersonName
    class MyAddress(Address):
        """MyAddress."""

        def __init__(self, **kwargs):
            """MyAddress.__init__."""
            super().__init__(**kwargs)
            self._datafile = 'address.json'

    class MyPerson(Person):
        """MyPerson."""

        def __init__(self, **kwargs):
            """MyPerson.__init__."""

# Generated at 2022-06-13 23:58:45.764350
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TempProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
            self._data = {}
            self._datafile = ''

        def __str__(self) -> str:
            locale = getattr(self, 'locale', locales.DEFAULT_LOCALE)
            return '{} <{}>'.format(self.__class__.__name__, locale)

    prov = TempProvider(locale=locales.EN)
    prov.locale = 'go'
    with prov.override_locale(locales.EN) as locale:
        assert locale.locale == locales.EN

# Generated at 2022-06-13 23:58:51.486783
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyProvider(BaseDataProvider):
        def __init__(self):
            super(MyProvider, self).__init__(locale='en')
            self._data = {'en': 'English', 'ru': 'Russian'}
            self._datafile = ''

    provider = MyProvider()

    with provider.override_locale('ru') as overridden_provider:
        assert overridden_provider.get_data('ru') == 'Russian'
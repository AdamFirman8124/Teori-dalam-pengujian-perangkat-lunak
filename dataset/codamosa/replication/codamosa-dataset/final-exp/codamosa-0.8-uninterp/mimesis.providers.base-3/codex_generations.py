

# Generated at 2022-06-13 23:50:48.946910
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method ``override_locale()`` of class ``BaseDataProvider``."""
    class TestDataProvider(BaseDataProvider):
        def __init__(self):
            super(TestDataProvider, self).__init__()
            self._pull('test.json')

        def get_data(self, value: str) -> Any:
            return self._data[value]

    p = TestDataProvider()
    assert p.get_data('name') == 'One'

    with p.override_locale('ru'):
        assert p.get_data('name') == 'Один'

    assert p.get_data('name') == 'One'

    with p.override_locale('ru-RU'):
        assert p.get_data('name') == 'Один'

   

# Generated at 2022-06-13 23:50:55.552559
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DummyProvider(BaseDataProvider):
        """Unit test for method override_locale of class BaseDataProvider."""

        def get_current_locale(self) -> str:
            """Get current locale.

            If locale is not defined then this method will always return ``en``,
            because ``en`` is default locale for all providers, excluding builtins.

            :return: Current locale.
            """
            return self.locale

    provider = DummyProvider()
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

    with provider.override_locale(locales.EN):
        assert provider.get_current_locale() == locales.EN

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:51:00.493196
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis
    Base = mimesis.BaseDataProvider
    b = Base()
    with b.override_locale('ru') as l:
        l.locale == 'ru'
        b.locale == 'ru'
    b.locale == 'en'



# Generated at 2022-06-13 23:51:06.939492
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Check method override_locale of class BaseDataProvider."""
    class Provider(BaseDataProvider):
        _datafile = 'test.json'

    provider = Provider()
    with provider.override_locale(locales.EN) as p:
        assert p.locale == locales.EN
        assert p._data['test'] == 'test'
    assert provider.locale == locales.DEFAULT_LOCALE
    assert provider._data['test'] == 'Hello'

# Generated at 2022-06-13 23:51:17.244433
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    class TestProvider(BaseDataProvider):
        """Test provider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)

        def get(self, key: str) -> str:
            return self._data[key]

    with TestProvider('ru') as provider:
        assert provider.get_current_locale() == 'ru'
        assert provider.get('currency.code.aed') == 'AED'

    with provider.override_locale('en'):
        assert provider.get_current_locale() == 'en'
        assert provider.get('currency.code.aed') == 'AED'


# Generated at 2022-06-13 23:51:22.150569
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data_provider = BaseDataProvider()
    with data_provider.override_locale('override_locale'):
        assert data_provider.get_current_locale() == 'override_locale'


## Unit test for method _validate_enum of class BaseProvider

# Generated at 2022-06-13 23:51:30.425498
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method :meth:`override_locale` of class :class:`BaseDataProvider`."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    class PersonTest(Person):
        """Class for testing ``override_locale`` function."""

        @property
        def test_genders(self) -> Dict[str, Gender]:
            """Overriding genders to test overridden locale."""
            return {'male': Gender.MALE,
                    'female': Gender.FEMALE,
                    'neutral': Gender.NEUTRAL}

    provider = PersonTest()
    provider._pull.cache_clear()
    assert provider.get_current_locale() == locales.EN
    assert provider.test_genders['male'] == Gender.MALE
   

# Generated at 2022-06-13 23:51:39.814957
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.code import Code as CodeDataProvider

    origin_locale = 'ru'
    locale = 'en'
    code = CodeDataProvider(origin_locale)

    # Test by changing locale, checking and chaging back
    with code.override_locale(locale) as _:
        assert _.get_current_locale() == locale

    assert code.get_current_locale() == origin_locale


# Generated at 2022-06-13 23:51:49.051963
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.schema import HexColorCode, Number, Text
    from mimesis.builtins import Person, Code
    from mimesis.enums import Gender, Compliance

    person = Person('en')
    code = Code('en')
    with person.override_locale('ru'):
        assert person.get_current_locale() == 'ru'
        assert person.full_name(gender=Gender.MALE) in {'Иван Иванов', 'Дмитрий Петров'}
        assert code.hash(algorithm=Compliance.SHA1) == 'SHA-1'
    assert person.get_current_locale() == 'en'
    assert isinstance(person.full_name(gender=Gender.MALE), str)


# Generated at 2022-06-13 23:51:55.410388
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    with provider.override_locale('ru') as ru:
        assert ru.get_current_locale() == 'ru'
    assert provider.get_current_locale() != 'ru'

# Generated at 2022-06-13 23:52:12.515080
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bdp = BaseDataProvider(locale=locales.EN, seed=42)
    assert bdp._pull.cache_info() == CacheInfo(hits=0, misses=1, maxsize=None, currsize=1)
    with bdp.override_locale(locale=locales.RU):
        assert bdp._pull.cache_info() == CacheInfo(hits=0, misses=2, maxsize=None, currsize=2)
    assert bdp._pull.cache_info() == CacheInfo(hits=1, misses=2, maxsize=None, currsize=1)

# Generated at 2022-06-13 23:52:21.139819
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test of method BaseDataProvider.override_locale."""
    class TestProvider(BaseDataProvider):
        def _pull(self) -> None:
            self._data = {'test_1': 'foo', 'test_2': 'bar'}

    provider = TestProvider(locale='en')
    with provider.override_locale(locale='ru') as new_provider:
        assert new_provider._data == {'test_1': 'foo', 'test_2': 'bar'}

# Generated at 2022-06-13 23:52:31.532707
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        pass
    seed = 5
    provider = TestProvider(seed=seed)
    with provider.override_locale('ru') as temp:
        assert temp.locale == 'ru'
        items = ['яблоко', 'банан', 'киви', 'апельсин']
        assert temp.random.choice(items) == 'яблоко'
    # Locale back to default
    assert provider.locale == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:52:37.274699
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        pass

    provider = TestProvider()
    assert provider.locale == locales.EN
    with provider.override_locale(locales.RU) as p:
        assert p.locale == locales.RU

    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:52:49.362625
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class Provider(BaseDataProvider):
        pass

    provider = Provider()

    with provider.override_locale(locales.RU) as p:
        assert p.get_current_locale() == locales.RU
    assert provider.get_current_locale() == locales.EN

    provider = Provider(locale=locales.DE)
    with provider.override_locale(locales.RU) as p:
        assert p.get_current_locale() == locales.RU
    assert provider.get_current_locale() == locales.DE

    with provider.override_locale() as p:
        assert p.get_current_locale() == locales.EN
    assert provider.get_current_locale() == locales.DE



# Generated at 2022-06-13 23:52:53.568412
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bdp = BaseDataProvider()
    with bdp.override_locale(locales.RU):
        assert bdp.locale == locales.RU
    assert bdp.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:59.700834
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Person
    from mimesis.enums import Gender
    from mimesis.exceptions import UnsupportedLocale
    from mimesis.builtins import RussiaSpecProvider
    import pytest

    p1 = Person()
    p2 = Person(locale='es')
    assert p1.get_current_locale() == 'en'
    assert p2.get_current_locale() == 'es'
    with pytest.raises(UnsupportedLocale):
        p = Person(locale='zz')
    with pytest.raises(ValueError):
        p = RussiaSpecProvider()
        with p.override_locale('en'):
            print(p.gender())
    with p1.override_locale('en') as p:
        assert p == p1
       

# Generated at 2022-06-13 23:53:07.424640
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis.builtins as mimesis
    with mimesis.Person.override_locale('en') as provider:
        assert provider.get_current_locale() == 'en'

    with provider.override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'

    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:53:18.372416
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''
    1) Purpose: test function override_locale of class BaseDataProvider
    2) Input: None
    3) Expected Output: .
    4) Result: .
    '''
    provider = BaseDataProvider()
    with provider.override_locale(locales.EN):
        assert provider.get_current_locale() == locales.EN
        with provider.override_locale(locales.RU):
            assert provider.get_current_locale() == locales.RU
        assert provider.get_current_locale() == locales.EN



# Generated at 2022-06-13 23:53:19.644278
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis import Code
    pass

# Generated at 2022-06-13 23:53:37.354763
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def __init__(self):
            super().__init__()

        def get_data(self, lang: str) -> Dict[str, str]:
            with self.override_locale(lang):
                return {
                    'a': self._data['a'],
                    'b': self._data['b'],
                }

    provider = TestDataProvider()

    data_en = provider.get_data(locales.EN)
    assert provider.locale == locales.EN
    assert provider._datafile == 'test.json'
    assert provider._data_dir.exists()
    assert provider._data_dir.is_dir()
    assert data_en == {
        'a': 'a',
        'b': 'b',
    }

    data_ru

# Generated at 2022-06-13 23:53:44.616005
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestBaseDataProvider(BaseDataProvider):
        _datafile = 'addresses.json'
        def get_country(self, *args, **kwargs):
            return 'USA'

    provider = TestBaseDataProvider(locale='ru')

    with provider.override_locale(locale='en'):
        assert provider.get_country() == 'USA'
        assert provider.locale == 'en'

    assert provider.locale == 'ru'

    # Raises when has not _locale attribute
    class TestBaseProvider(BaseProvider):
        pass

    provider = TestBaseProvider()

    with pytest.raises(ValueError):
        with provider.override_locale(locale='en'):
            pass

# Generated at 2022-06-13 23:53:53.021204
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data = [{
        'en': 'English locale was set',
        'ru': 'Был установлен русский локаль',
    }]
    class TestProvider(BaseDataProvider):
        def get_data(self) -> str:
            return super().get_data()

    provider = TestProvider()
    provider.add_provider_method('get_data', data)

    with provider.override_locale('ru') as provider:
        assert provider.get_data() == 'Был установлен русский локаль'

    # Get default value
    assert provider.get_data() == 'English locale was set'

# Generated at 2022-06-13 23:53:57.292628
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    provider = TestProvider()
    assert provider.locale == 'en'

    with provider.override_locale('ru'):
        assert provider.locale == 'ru'

    assert provider.locale == 'en'



# Generated at 2022-06-13 23:54:02.048871
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Foo(BaseDataProvider):
        def __init__(self, locale=locales.EN):
            super().__init__(locale=locale)
            self._datafile = 'test_foo.json'

    datafile = 'test_foo.json'
    for locale in locales.SUPPORTED_LOCALES:
        with open(datafile, 'w') as f:
            json.dump({'hello': 'Hello'}, f)

        foo = Foo(locale=locale)
        with foo.override_locale('en') as f:
            print(f.get_current_locale(), f._data)

        with foo.override_locale('ru') as f:
            print(f.get_current_locale(), f._data)

# Generated at 2022-06-13 23:54:08.279775
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.person import Person
    p = Person(locale='nb')
    with p.override_locale('en') as person:
        assert person.name() != 'Solveig'
        assert person.name() == 'Patrick'
    assert p.name() == 'Solveig'



# Generated at 2022-06-13 23:54:18.057521
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.person import Person
    provider = Person()
    with provider.override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'
    assert provider.get_current_locale() == 'en'
    assert p.get_current_locale() == 'ru'
    assert p.full_name() != provider.full_name()

    with provider.override_locale(locales.DEFAULT_LOCALE):
        assert provider.get_current_locale() == locales.DEFAULT_LOCALE
    with provider.override_locale('fr'):
        assert provider.get_current_locale() == 'fr'
        assert provider.full_name() != p.full

# Generated at 2022-06-13 23:54:24.700528
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Method «_override_locale» is defined exactly right."""
    provider = BaseDataProvider()
    setattr(provider, 'locale', 'en')
    with provider.override_locale() as p:
        check_locale = getattr(p, 'locale', 'en')
    assert check_locale == 'en'

    with provider.override_locale(locale='ru') as p:
        check_locale = getattr(p, 'locale', 'ru')
    assert check_locale == 'ru'



# Generated at 2022-06-13 23:54:31.651807
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale, seed):
            super().__init__(locale, seed)

    provider_o = TestProvider('en', seed=1)
    with provider_o.override_locale('ru') as provider:
        assert provider.locale == 'ru'
        assert provider_o.locale == 'en'

    assert provider_o.locale == 'en'

# Generated at 2022-06-13 23:54:39.875222
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the context manager.

    BaseDataProvider.override_locale() is a context manager and should
    return the object itself to allow further methods to be called on it.
    """
    class RuProvider(BaseDataProvider):
        pass

    ru_provider = RuProvider()
    with ru_provider.override_locale(locale='ru') as ru_provider:
        assert ru_provider.get_current_locale() == 'ru'

    assert ru_provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:55:04.506082
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider"""
    class TestClass(BaseDataProvider):
        def __init__(self, locale=locales.EN):
            super().__init__(locale)

    t = TestClass()
    try:
        t._override_locale(locales.RU)
    except:
        assert False
        t._override_locale(locales.EN)
    else:
        assert True
        t._override_locale(locales.EN)

# Generated at 2022-06-13 23:55:06.987724
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    from mimesis.builtins import Personal

    with pytest.raises(ValueError) as e:
        personal = Personal()
        with personal.override_locale('af') as p:
            print(p.full_name)

    assert str(e.value) == '«Personal» has not locale dependent'



# Generated at 2022-06-13 23:55:09.809765
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    locale = 'ru-RU'
    with provider.override_locale(locale):
        assert provider.locale == locale
    assert provider.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:55:17.125209
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # BaseDataProvider.override_locale()
    p = BaseDataProvider(locale='en')
    assert p.get_current_locale() == 'en'
    with p.override_locale('ru') as x:
        assert x.get_current_locale() == 'ru'
        with x.override_locale('en') as y:
            assert y.get_current_locale() == 'en'
        assert x.get_current_locale() == 'ru'
    assert p.get_current_locale() == 'en'

# Generated at 2022-06-13 23:55:24.199248
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Processor

    processor = Processor(seed=1234)
    # locale is not dependent
    with processor.override_locale(locale='ru') as proc:
        assert proc.get_current_locale() == 'ru'
    assert processor.get_current_locale() == locales.DEFAULT_LOCALE

    processor = Processor(seed=1234, locale='ru')
    # locale is dependent
    with processor.override_locale(locale='en') as proc:
        assert proc.get_current_locale() == 'en'
    assert processor.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:55:33.029420
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        _datafile = 'test.json'

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)

    provider = TestProvider(locale='ru')
    with provider.override_locale(locale='en') as provider:
        assert provider.locale == 'en'

    assert provider.locale == 'ru'

# Generated at 2022-06-13 23:55:39.945323
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test case for method override_locale of class BaseDataProvider."""
    from mimesis.providers.base import BaseDataProvider
    from mimesis.providers.geography import Geography
    from mimesis.providers.personal import Personal
    from mimesis.providers.misc import Coin
    from mimesis.providers.science import Science
    from mimesis.providers.commerce import Commerce

    russian = 'ru'
    chinese = 'zh'
    english = 'en'
    france = 'fr'

    # Test for locale-dependent providers
    bdp = BaseDataProvider(locale=english)
    geo = Geography(locale=english)
    per = Personal(locale=english)
    sci = Science(locale=english)
    com = Commerce(locale=english)


# Generated at 2022-06-13 23:55:44.986181
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    reg = BaseDataProvider()
    loc = 'uk'
    with reg.override_locale(locale=loc):
        assert reg.get_current_locale() == loc

# Generated at 2022-06-13 23:55:50.900883
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    class Provider(BaseDataProvider):
        """Provider for testing."""


# Generated at 2022-06-13 23:55:56.769773
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person()
    with p.override_locale('en'):
        assert p.full_name(gender=Gender.MALE) == 'Jeremiah Irwin'

    with p.override_locale('ru'):
        assert p.full_name(gender=Gender.MALE) == 'Александр Рыбаков'

    with p.override_locale('es'):
        assert p.full_name(gender=Gender.MALE) == 'Roberto Camacho'

    assert p.full_name(gender=Gender.MALE) == 'Nguyễn Quỳnh Hoa'

# Generated at 2022-06-13 23:56:40.547968
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, provider: BaseDataProvider = None):
            self.provider = provider

        def __enter__(self):
            return self.provider

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    class TestProviderLocale(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            self.locale = locale

    provider = TestProviderLocale(locale=locales.RU)
    test_provider = TestProvider(provider)
    with test_provider.override_locale(locale=locales.DEFAULT_LOCALE):
        assert provider.locale == locales.DEFAULT_LOCALE

    assert provider.locale == local

# Generated at 2022-06-13 23:56:55.350407
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestClass(BaseDataProvider):
        pass

    provider = TestClass()

    # When
    with provider.override_locale('ru') as new_provider:
        # Then
        assert provider.get_current_locale() == 'ru'

    # When
    with provider.override_locale('fr') as new_provider:
        # Then
        assert provider.get_current_locale() == 'fr'

    # When
    with pytest.raises(NonEnumerableError):
        with provider.override_locale('en-US') as new_provider:
            pass

# def test_BaseDataProvider_pull():
#     class TestClass(BaseDataProvider):
#         pass
    
#     provider = TestClass()

#     provider._pull(datafile='holidays.json

# Generated at 2022-06-13 23:57:03.550523
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import (
        Address, Code, Datetime, File, FileSystem, HTML, Lorem, Person,
        Text, Vehicle)
    from mimesis.providers.code import CodeProvider

    ad = Address(locale='kk')  # Kazakhstan
    assert str(ad) == 'Address <kk>'
    assert ad.street_name(token='#') == 'ТОРГАЙ ТОЛЕБЕК'
    assert ad.state(token='#') == 'АСТАНА'
    assert ad.country(token='#') == 'ҚАЗАКСТАН'

# Generated at 2022-06-13 23:57:16.569128
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    
    person = Person('en')
    person_with_override = person.override_locale('ru')
    for i in range(10):
        gender_with_override = person_with_override.gender()
        gender_without_override = person.gender()
        assert gender_with_override in Gender and gender_without_override in Gender

        assert gender_with_override != gender_without_override

# Generated at 2022-06-13 23:57:25.175599
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class Test(BaseDataProvider):
        def __init__(self, locale: str = locales.EN, seed: Seed = None):
            super().__init__(locale, seed)
            self._datafile = 'dataprovider.json'
            self._pull()

        @property
        def data(self) -> JSON:
            return self._data

        def locale(self) -> str:
            return getattr(self, 'locale', locales.DEFAULT_LOCALE)

    try:
        with Test().override_locale():
            pass
    except:
        pass
    else:
        raise AssertionError('Should be raised ValueError!')

    test = Test()
    with test.override_locale('ru') as test:
        assert test.data['ru'] == test.data['_']

# Generated at 2022-06-13 23:57:31.588059
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.identifier import Identifier
    isinstance(BaseDataProvider(), BaseProvider)
    isinstance(Identifier(), BaseDataProvider)
    with Identifier().override_locale('ru'):
        assert Identifier().get_current_locale() == 'ru'


# Generated at 2022-06-13 23:57:38.050868
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """A test for BaseDataProvider.override_locale."""
    class AnyProvider(BaseDataProvider):
        """Any class to test context manager."""
        pass
    provider_instance = AnyProvider()
    locale = 'de-DE'
    with provider_instance.override_locale(locale):
        assert provider_instance.locale == locale


test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:57:46.157129
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import os
    import tempfile
    f = tempfile.NamedTemporaryFile(delete=False)
    with f as file:
        file.write("""{"a":{"a":"b"}}""".encode('utf8'))
        file.seek(0)
        
    FileDataProvider = BaseDataProvider.__bases__[0]
    f__file = FileDataProvider._FileDataProvider__file
    FileDataProvider._FileDataProvider__file = f.name

    with open('/tmp/dummy.json', 'r', encoding='utf8') as file:
        os.remove('/tmp/dummy.json')
        content = json.load(file)
        assert content['a']['a'] == 'b'

    FileDataProvider._FileDataProvider__file = f__file


# Generated at 2022-06-13 23:57:54.194603
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test of method override_locale of class BaseDataProvider."""
    hidden_locale = 'hidden'
    provider = BaseDataProvider(locale=hidden_locale)

    with provider.override_locale() as p:
        assert p.locale == locales.DEFAULT_LOCALE
        assert p.get_current_locale() == locales.DEFAULT_LOCALE

    assert provider.locale == hidden_locale
    assert provider.get_current_locale() == hidden_locale

# Generated at 2022-06-13 23:58:03.981069
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.identifiers import Passport
    from mimesis.providers.internet import Internet

    assert Passport().generate() == 'AT19NBNW826526576'
    assert Passport().generate() == 'AT19NBNW826526576'

    with Internet().override_locale():
        assert Internet().generate() == 'крышка-упругость'
        assert Internet().generate() == 'крышка-упругость'

    assert Passport().generate() == 'AT19NBNW826526576'
    assert Passport().generate() == 'AT19NBNW826526576'

# Generated at 2022-06-13 23:59:34.037819
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Business, Person
    from mimesis.providers.utils import select_locale, randomize

    person_uk = Person(locale='uk')
    person_ru = Person(locale='ru')
    person_en = Person(locale='en')

    business_ru = Business(locale='ru')

    # Add locale provider to the registry
    registry = {
        locales.RU: person_ru,
        locales.EN: person_en,
        locales.UK: person_uk
    }

    # Randomly choose current locale
    with randomize(1):
        current_locale = select_locale(registry, locales.RU)

    assert current_locale == locales.RU

    # Select locale from registry using the context manager

# Generated at 2022-06-13 23:59:36.993137
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Здесь должно быть Unit test for method override_locale of class BaseDataProvider
    pass

# Generated at 2022-06-13 23:59:52.574967
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    _ = BaseDataProvider()

    class TestBaseDataProvider(BaseDataProvider):

        def __init__(self):
            super().__init__()
            self._datafile = ''
            self._pull()

        def get_locale(self):
            """The method that returns the current locale."""
            return getattr(self, 'locale', locales.DEFAULT_LOCALE)

    class TestDataProvider(TestBaseDataProvider):
        pass

    test_data_provider = TestDataProvider()

    locale_ru = locales.RU
    locale_en = locales.EN

    current_locale = test_data_provider.get_locale()
    assert current_locale == locales.DEFAULT_LOCALE


# Generated at 2022-06-14 00:00:01.169804
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    with Person().override_locale('ru'):
        assert Person().full_name() == 'Андрей Вадимович Захаров'
        assert Person().full_name() == 'Андрей Вадимович Захаров'

    with Person().override_locale('en'):
        assert Person().username() == 'matthew_jones'
        assert Person().username() == 'matthew_jones'
        assert Person().username() == 'matthew_jones'



# Generated at 2022-06-14 00:00:14.998735
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.person import Person
    person = Person('ru')
    with person.override_locale('ru') as new_person:
        assert new_person.locale == 'ru'
        assert person.locale == 'ru'
        with new_person.override_locale('en') as new_person_en:
            assert new_person_en.locale == 'en'
            assert new_person.locale == 'en'
        assert new_person.locale == 'ru'
    assert person.locale == 'ru'

# Generated at 2022-06-14 00:00:19.980484
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.utils import Provider

    p = Person('en')
    with p.override_locale('ru') as s:
        assert 'Женский' in s.gender().title()

    # Test BaseProvider
    p = Provider('en')
    with p.override_locale('ru') as s:
        assert 'Женский' not in s.gender().title()


# Generated at 2022-06-14 00:00:29.163244
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from abc import ABCMeta
    from mimesis import Person
    from mimesis.builtins.common import Common
    from mimesis.builtins.constants import Convenience, Flags, NonBinary
    from mimesis.providers.internet import Internet

    cases = [
        (Internet, Convenience.EMPTY_STRING),
        (Common, Convenience.EMPTY_STRING),
        (Flags, NonBinary.NOT_APPLICABLE),
        (Person, 'en'),
    ]

    for provider, expected_locale in cases:
        with provider().override_locale() as _:
            assert _.get_current_locale() == expected_locale

    with Person().override_locale('ru') as _:
        assert _.get_current_locale() == 'ru'
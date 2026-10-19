

# Generated at 2022-06-13 23:50:45.159594
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)

        def get_current_locale(self):
            return self.locale

    p = Provider(locale='ru')
    with p.override_locale('en') as override_provider:
        locale = override_provider.get_current_locale()
        assert locale != p.get_current_locale()
        assert locale == 'en'
    assert p.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:50:52.645466
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider's method override_locale."""
    locale = locales.EN
    provider = BaseDataProvider(locale=locale)
    with provider.override_locale(locale):
        assert provider.get_current_locale() == locale

    locale = 'ru-RU'
    provider = BaseDataProvider(locale=locale)
    with provider.override_locale(locale):
        assert provider.get_current_locale() == locale

# Generated at 2022-06-13 23:51:02.686679
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyProvider(BaseDataProvider):
        pass
    provider = MyProvider(locale='cz')
    assert provider.locale == 'cz'
    with provider.override_locale('de') as pr:
        assert pr.locale == 'de'
    assert provider.locale == 'cz'
    with provider.override_locale('de') as pr:
        pr._override_locale('en')
        assert pr.locale == 'en'
    assert provider.locale == 'cz'

    with provider.override_locale('ru'):
        with provider.override_locale('en'):
            assert provider.locale == 'en'
        assert provider.locale == 'ru'
    assert provider.locale == 'cz'

# Generated at 2022-06-13 23:51:10.519990
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        __slots__ = ['_datafile']
        _datafile = 'test'

        def test_method(self):
            return self._data[self.locale]

    provider = TestProvider()

    with provider.override_locale('ru') as rp:
        assert rp.test_method()['test'] == 'русский'

    with provider.override_locale('en') as rp:
        assert rp.test_method()['test'] == 'English'

# Generated at 2022-06-13 23:51:19.269441
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, seed=None, locale=locales.DEFAULT_LOCALE):
            super().__init__(seed=seed,  locale=locale)

    test1 = TestProvider(locale='en')
    test2 = TestProvider(locale='ru')

    with test1.override_locale('ru') as newtest:
        assert test1.locale == 'ru'
        assert newtest.locale == 'ru'
        assert newtest.random.seed == test1.random.seed

    with test2.override_locale('en') as newtest:
        assert test2.locale == 'ru'
        assert newtest.locale == 'en'
        assert newtest.random.seed == test2.random.seed


# Generated at 2022-06-13 23:51:24.949218
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        pass

    class ProviderRu(BaseDataProvider):
        def __init__(self, locale: str = 'ru') -> None:
            super().__init__(locale)

    provider = Provider()
    provider_ru = ProviderRu()

    with provider.override_locale(locales.RU) as pr:
        assert pr.locale == locales.RU
        assert provider.locale == loca

# Generated at 2022-06-13 23:51:33.435864
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    from .datetime import Datetime
    from .numbers import Numbers
    from .person import Person

    num = Numbers()
    dt = Datetime()
    per = Person()

    # Error if override_locale for providers without locale attribute

    try:
        with num.override_locale(locales.RU):
            raise RuntimeError('Wrongly worked.')
    except AttributeError:
        assert True
    else:
        assert False

    try:
        with dt.override_locale(locales.RU):
            raise RuntimeError('Wrongly worked.')
    except AttributeError:
        assert True
    else:
        assert False

    # Override English with Russian


# Generated at 2022-06-13 23:51:37.830783
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """ Unit test for method override_locale of class BaseDataProvider """
    class Test(BaseDataProvider):
        def __init__(self):
            super().__init__(locale='ru-RU')

    test = Test()
    locale = 'en'
    with test.override_locale(locale) as p:
        assert isinstance(p, Test)
        assert p.locale == locale

    assert test.locale != locale



# Generated at 2022-06-13 23:51:44.916057
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class LocalizedProvider(BaseDataProvider):
        class Meta:
            name = 'LocalizedProvider'

    class NotLocalizedProvider(BaseDataProvider):
        class Meta:
            name = 'NotLocalizedProvider'

    class LocalizedNotLocalizedProvider(BaseDataProvider):
        class Meta:
            name = 'LocalizedNotLocalizedProvider'

        def get_current_locale(self) -> str:
            return getattr(self, 'locale') or super().get_current_locale()

    data_provider_with_locale = LocalizedProvider()
    data_provider_without_locale = NotLocalizedProvider()
    data_provider_localized_not_localized = LocalizedNotLocalizedProvider()

    data_provider_with_locale.locale = 'ru'

# Generated at 2022-06-13 23:51:52.384938
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit - test for method override_locale of class BaseDataProvider."""
    class C(BaseDataProvider):
        """Helper class."""
        pass
    fp = C(locale='en')
    with fp.override_locale('en'):
        assert fp.get_current_locale() == 'en'
        with fp.override_locale('ru'):
            assert fp.get_current_locale() == 'ru'
    assert fp.get_current_locale() == 'en'
    def c():
        """Inner function for test."""
        with fp.override_locale('not'):
            assert fp.get_current_locale() == 'not'
    fp = BaseProvider()

# Generated at 2022-06-13 23:52:08.745471
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """test_BaseDataProvider_override_locale."""
    from mimesis.providers import Business
    provider = Business()
    with provider.override_locale() as p:
        assert p.get_current_locale() == locales.DEFAULT_LOCALE
    with provider.override_locale(locales.EN) as p:
        assert p.get_current_locale() == locales.EN


# Generated at 2022-06-13 23:52:12.804695
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    base_data_provider = BaseDataProvider()
    assert base_data_provider.get_current_locale() == locales.EN

    with base_data_provider.override_locale(locales.RU):
        assert base_data_provider.get_current_locale() == 'ru'

    assert base_data_provider.get_current_locale() == locales.EN



# Generated at 2022-06-13 23:52:19.976252
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.language import Language

    lang = Language()

    with lang.override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'
        assert provider.get_language() in lang.data['ru']

    assert lang.get_current_locale() == 'en'
    assert lang.get_language() in lang.data['en']

# Generated at 2022-06-13 23:52:31.071088
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code as CodeProvider
    from mimesis.data import Code as CodeDataProvider
    from mimesis.enums import CodeLanguage

    # Get categories from local 'en'
    with CodeDataProvider().override_locale() as provider:
        en_categories = provider._data.keys()

    # Get categories from local 'ru'
    with CodeDataProvider().override_locale('ru') as provider:
        ru_categories = provider._data.keys()

    assert en_categories != ru_categories
    assert CodeLanguage.JAVA in en_categories
    assert CodeLanguage.JAVA in ru_categories
    assert CodeLanguage.JAVA not in \
        CodeProvider().get_categories()

# Generated at 2022-06-13 23:52:36.494124
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class A(BaseDataProvider):
        _datafile = 'test'
    locale = locales.EN
    a = A(locale)
    result = a.get_current_locale()
    assert result == locale

    with a.override_locale('ru') as x:
        result = x.get_current_locale()
        assert result == 'ru'
        assert x._datafile == 'test'


# Generated at 2022-06-13 23:52:43.241284
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the override_locale method."""
    class Dummy(BaseDataProvider):
        datafile = 'dummy.json'

    provider = Dummy()

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

    with provider.override_locale(locales.EN) as p:
        assert p.get_current_locale() == locales.EN

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:52:52.004962
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    with Address.override_locale('ua') as address:
            assert address.get_current_locale() == 'ua'
            assert address.full_address() == 'Львівська область, місто Львів, вулиця Товарна, будинок 101'

# Generated at 2022-06-13 23:52:59.023315
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.builtins import BugTracker
    import sys
    import pytest
    class TestBugTracker(BugTracker):
        def get_status(self):
            return self.override_locale('ru')._data.get('status')[0]
    # Init
    tr = TestBugTracker()
    tr.seed = 1
    tr.locale = 'en'
    tr._pull()
    # Checks
    assert 'Resolved' == tr.get_status()
    assert 'Решено' == tr.override_locale('ru').get_status()
    # Check ValueError
    bt = BugTracker()
    with pytest.raises(ValueError) as excinfo:
        with bt.override_locale('ru'):
            pass

# Generated at 2022-06-13 23:53:11.296464
# Unit test for method override_locale of class BaseDataProvider

# Generated at 2022-06-13 23:53:18.983758
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale=locales.EN)
    assert provider.locale == locales.EN
    assert provider.get_current_locale() == locales.EN
    with provider.override_locale(locale=locales.RU):
        assert provider.locale == locales.RU
        assert provider.get_current_locale() == locales.RU
    assert provider.locale == locales.EN
    assert provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:53:33.467984
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, seed=None):
            super().__init__(locale='en', seed=seed)

    provider = Provider()
    with provider.override_locale('fr'):
        assert provider.get_current_locale() == 'fr'

    # locale should be restored to en
    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:53:37.352248
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Person

    robert = Person()
    with robert.override_locale('en') as p:
        assert p.full_name() == 'Henry Ferguson'
    assert robert.full_name() != 'Henry Ferguson'

# Generated at 2022-06-13 23:53:38.820695
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # TODO: implement test
    pass

# Generated at 2022-06-13 23:53:50.253244
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Person(BaseDataProvider):
        def __init__(self, locale='ru'):
            super().__init__(locale=locale)

        def fname(self):
            return self._data['first_names']

    p = Person(locale='ru')

# Generated at 2022-06-13 23:54:00.468037
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender, Greeting
    from mimesis.providers.greetings import Greetings
    from mimesis.providers.internet import Internet

    providers = dict()

    with BaseDataProvider.override_locale(locale=locales.DE) as provider:
        providers['BaseDataProvider'] = provider

    with Internet.override_locale(locale=locales.DE,
                                  seed=123) as provider:
        providers['Internet'] = provider

    with Greetings.override_locale(locale=locales.DE,
                                   seed=123456) as provider:
        providers['Greetings'] = provider

    assert providers['BaseDataProvider'].get_current_locale() == locales.DE
    assert providers['BaseDataProvider'].seed is None

# Generated at 2022-06-13 23:54:13.157166
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Cryptographic
    from mimesis.providers.date import DateTime

    dt = DateTime()

    with dt.override_locale('ru') as dt:
        assert repr(dt) == 'DateTime <ru>'
        assert dt.full_date() == 'суббота, 1 июня 2019 года'

    with dt.override_locale('fr') as dt:
        assert repr(dt) == 'DateTime <fr>'
        assert dt.full_date() == 'samedi 1 juin 2019'

    with dt.override_locale('ar') as dt:
        assert repr(dt) == 'DateTime <ar>'

# Generated at 2022-06-13 23:54:23.610193
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider.override_locale."""
    class ExampleProvider(BaseDataProvider):

        def __init__(self, locale: str = '', seed: Seed = None) -> None:
            """Initialize attributes."""
            super().__init__(seed=seed)
            self._data = {
                'en': {
                    'drink': 'water',
                    'uk': {
                        'drink': 'tea',
                        'ua': {
                            'drink': 'coffee',
                        },
                    },
                },
            }
            self._setup_locale(locale)

        def drink(self) -> Dict:
            """Return random drink."""
            return self._data[self.locale]

    provider = ExampleProvider(locale='en_US')
    assert provider.drink

# Generated at 2022-06-13 23:54:26.718172
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        @property
        def foo(self):
            return 'foo'

    test_provider = TestProvider(seed=1)
    with test_provider.override_locale():
        assert test_provider.foo == 'foo'
    

# Generated at 2022-06-13 23:54:33.678283
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Food

    def action():
        with food.override_locale('ru') as f:
            assert f.get_current_locale() == 'ru'
            assert f.get_item('fruit') == 'яблоко'

    food = Food()
    assert food.get_current_locale() == 'en'
    assert food.get_item('fruit') == 'apple'
    action()
    assert food.get_current_locale() == 'en'
    assert food.get_item('fruit') == 'apple'

# Generated at 2022-06-13 23:54:45.040060
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DummyProvider(BaseDataProvider):
        def __init__(self):
            super().__init__()
            self._data = {
                '_datafile': 'dummy.json',
                'one': 'one',
                'two': 'two',
                'three': 'three',
            }
            self._pull(self._datafile)

    dp = DummyProvider()
    # CASE 1: EN locale
    assert dp.get_current_locale() == locales.EN.lower()
    with dp.override_locale() as dp:
        assert dp.get_current_locale() == locales.EN.lower()
    assert dp.get_current_locale() == locales.EN.lower()
    # CASE 2: RU locale
    assert dp.get_current_

# Generated at 2022-06-13 23:55:05.677998
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''
    Test for method override_locale of class BaseDataProvider
    
    @return: Nothing
    '''
    from mimesis.builtins import Code
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    with BaseDataProvider().override_locale('ru'):
        assert BaseDataProvider().get_current_locale() == 'ru'
        assert Code().make_code() == '8'
        assert Code().make_code(digits=2) == '98'
        assert Code().make_code(digits=8) == '98765432'
        assert Code().make_code(digits=10) == '9876543210'
        assert Code().make_code(digits=12) == '987654321098'


# Generated at 2022-06-13 23:55:12.205506
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    import mimesis

    data_provider = BaseDataProvider()
    assert data_provider.locale == locales.DEFAULT_LOCALE

    with data_provider.override_locale(locales.RU):
        assert data_provider.locale == locales.RU

    # ValueError: «BaseDataProvider» has not locale dependent
    with mimesis.BaseDataProvider.override_locale(locales.EN):
        pass

# Generated at 2022-06-13 23:55:15.502447
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data = {'a': 'b'}
    x = BaseDataProvider()
    x._data = data
    with x.override_locale('ru'):
        assert x._data == data
    assert x._data == data

# Generated at 2022-06-13 23:55:22.368752
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Create instance of class
    data_provider = BaseDataProvider()
    # Call method of class
    expected_result = BaseDataProvider()
    # Check that instance of class is returned
    assert isinstance(expected_result, BaseDataProvider)
    # Check that methods of class work
    assert str(expected_result) == 'BaseDataProvider <en>'

# Generated at 2022-06-13 23:55:36.267886
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestOverrideLocale(BaseDataProvider):

        def __init__(self, **kwargs: Any) -> None:
            super().__init__(kwargs.get('locale', locales.EN))
            self.locale_dependent_field = self.data['locale_dependent_field']

        @property
        def data(self) -> Dict:
            if not self._data:
                self._pull('test_data')
            return self._data

        @data.setter
        def data(self, value: Any) -> None:
            self._data = value

    provider = TestOverrideLocale()
    assert provider.get_current_locale() == locales.EN
    assert provider.locale_dependent_field == 1

    with provider.override_locale(locales.RU):
        assert provider

# Generated at 2022-06-13 23:55:44.429235
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    from mimesis.builtins import AbstractBuiltinsProvider
    from mimesis.builtins.en.builtins import BaseBuiltins
    from mimesis.builtins import Builtins
    from mimesis.builtins.en.internet import Internet
    from mimesis.builtins.ko.internet import Internet as Internet_ko

    locale_ko = 'ko'
    locale_en = 'en'

    class TestBaseDataProvider(BaseDataProvider):
        datafile = 'test.json'


        def get_data(self) -> Dict[str, str]:
            if not self._data:
                self._pull()
            return self._data


    class TestAbstractBuiltinsProvider(TestBaseDataProvider,
                                       AbstractBuiltinsProvider):
        pass




# Generated at 2022-06-13 23:55:50.509047
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    obj = BaseDataProvider(seed=42)

    try:
        with obj.override_locale('ru'):
            pass
    except ValueError:
        pass
    except Exception as e:
        print(e)
        raise e

    try:
        with obj.override_locale('en') as obj:
            print(obj)
    except Exception as e:
        print(e)
        raise e

# Run unit tests for BaseDataProvider
test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:55:56.860360
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
     class Foo(BaseDataProvider):
        def bar(self):
            return self.locale
     foo = Foo()

     with foo.override_locale(locales.DEFAULT_LOCALE):
         assert foo.bar() == locales.DEFAULT_LOCALE
     with foo.override_locale(locales.EN):
         assert foo.bar() == locales.EN



# Generated at 2022-06-13 23:55:59.527017
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    with pytest.raises(ValueError):
        with BaseDataProvider().override_locale('en'):
            pass


# Generated at 2022-06-13 23:56:07.332513
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale, locale_en=None, locale_ru=None):
            super().__init__(locale=locale)
            self._data = {
                'locale_en': locale_en,
                'locale_ru': locale_ru,
            }

        def get_current_locale(self) -> str:
            return self.locale

        def __getitem__(self, key: str) -> Dict:
            return self._data[key]

    provider = TestProvider('en', 'hello', 'привет')
    assert provider['locale_en'] == 'hello'


# Generated at 2022-06-13 23:56:35.718085
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person, Person as Person_ko
    from mimesis.providers.geography import Geography as Geography_ru

    person = Person(locale='ko')
    assert person.full_name() == '배성운'

    person = Person(locale='ko')
    with person.override_locale(locale='ru') as _:
        assert person.full_name() == 'Катюша Ростова'

    # Check if locale was not changed after context manager
    assert person.full_name() == '배성운'

    # Check if these are not the same instance of class Person
    assert not isinstance(person, Person_ko)

# Generated at 2022-06-13 23:56:39.856448
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Monkey patch to skip opening of a local file.
    class MyProvider(BaseDataProvider):
        def _pull(self, datafile: str = '') -> None:
            self._data = {'foo': 'bar'}

    provider = MyProvider()
    with provider.override_locale():
        assert provider.get_current_locale() == locales.EN
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:56:45.423714
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    faker = BaseDataProvider(locale='ru')
    with faker.override_locale('en'):
        faker.get_current_locale() == 'en'
    faker.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:56:48.573813
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    @BaseDataProvider.override_locale('ru')
    def foo(provider):
        return provider.locale

    assert foo(BaseDataProvider()) == 'ru'



# Generated at 2022-06-13 23:56:54.892317
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class _Dummy(BaseDataProvider):
        def __init__(self):
            self.locale = 'ru'

    dummy = _Dummy()
    with dummy.override_locale('en') as d:
        assert d.get_current_locale() == 'en'
        assert dummy.get_current_locale() != 'en'

    assert dummy.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:57:04.230601
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def __init__(self, locale='en', seed=None):
            pass

        def get_data(self, key, default=None):
            return self._data.get(key, default)

    test_data_provider = TestDataProvider()

    # Test if «AttributeError» raises when attribute «locale» is not defined
    raised_error = False
    try:
        with test_data_provider.override_locale('en'):
            pass
    except ValueError:
        raised_error = True
    finally:
        assert raised_error

    # Test if locale «en» and locale «ru» returns different locale
    for locale in ('en', 'ru'):
        with test_data_provider.override_locale(locale):
            assert test_

# Generated at 2022-06-13 23:57:14.474451
# Unit test for method override_locale of class BaseDataProvider

# Generated at 2022-06-13 23:57:21.434537
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.misc import Misc
    misc = Misc()
    for lang in locales.SUPPORTED_LOCALES:
        with misc.override_locale(lang):
            assert str(misc) == 'Misc <{}>'.format(lang)
        misc.locale = lang
        assert misc.get_current_locale() == lang
        assert str(misc) == 'Misc <{}>'.format(lang)

# Generated at 2022-06-13 23:57:30.100788
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.data = {}

    t_en = Test(locale='en')
    d_en = t_en.data

    with t_en.override_locale('ru') as t_ru:
        assert t_ru.locale == 'ru'
        d_ru = t_ru.data

    assert t_en.locale == 'en'
    assert t_en.data is d_en
    assert t_en.data is not d_ru

# Generated at 2022-06-13 23:57:40.237183
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.auto import Auto
    auto = Auto()
    with auto.override_locale(locales.RU):
        assert auto.get_current_locale() == locales.RU
    assert auto.get_current_locale() == locales.EN
    with auto.override_locale(locales.UK):
        assert auto.get_current_locale() == locales.UK
        with auto.override_locale(locales.BE):
            assert auto.get_current_locale() == locales.BE
        assert auto.get_current_locale() == locales.UK
    assert auto.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:58:18.012356
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:58:24.960039
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def __init__(self, locale: str, seed: Seed = None):
            super().__init__(locale=locale, seed=seed)

    meta = Test(locale='ru')
    assert meta.get_current_locale() == locales.RU
    assert meta.locale == locales.RU

    with meta.override_locale('en'):
        assert meta.get_current_locale() == locales.EN

    assert meta.get_current_locale() == locales.RU
    assert meta.locale == locales.RU

    with meta.override_locale(locales.EN) as m:
        assert m.get_current_locale() == locales.EN

    assert meta.get_current_locale() == local

# Generated at 2022-06-13 23:58:28.100897
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestClass(BaseDataProvider):
        pass

    with TestClass.override_locale(locales.EN) as provider:
        assert provider.locale == locales.EN
        assert isinstance(provider, TestClass)


# Generated at 2022-06-13 23:58:43.342770
# Unit test for method override_locale of class BaseDataProvider

# Generated at 2022-06-13 23:58:51.910605
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Using method override_locale of class BaseDataProvider
    # for overriding current locale of class Person.
    # Example:
    #  - person = Person()
    #  - with person.override_locale(locale=locales.RU):
    #       person.full_name()
    from mimesis.builtins import Person
    person = Person()
    locale = locales.RU
    full_name = ''
    with person.override_locale(locale=locale):
        full_name = person.full_name()
    assert full_name
    assert isinstance(full_name, str)

# Generated at 2022-06-13 23:59:00.903092
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider.

    :return: Nothing.
    """
    from mimesis import Datetime, Person

    with Datetime().override_locale('ru') as dt:
        assert dt.get_current_locale() == 'ru'
        assert dt.day(sunday_first=True) == 'воскресенье'

    with Person().override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:59:08.685602
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'data.json'
        def get_data(self):
            return self._pull()
    provider1 = TestProvider()
    with provider1.override_locale(locale=locales.RU):
        assert provider1.get_current_locale() == locales.RU
    assert provider1.get_current_locale() == locales.EN
    assert provider1._data != {}

# Generated at 2022-06-13 23:59:12.483068
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):

        def __init__(self, locale: str = locales.EN, seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'mimesis.json'

    provider = Provider()
    with provider.override_locale(locales.RU) as new_provider:
        assert new_provider.get_current_locale() == locales.RU
    assert provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:59:18.978349
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    locale = 'ru'

    class TestDataProvider(BaseDataProvider):
        def test(self):
            return self.locale == locale

    tdp = TestDataProvider()
    assert tdp.locale == locales.EN
    assert tdp.test() is False
    with tdp.override_locale(locale=locale):
        assert tdp.locale == locale
        assert tdp.test() is True
    assert tdp.locale == locales.EN
    assert tdp.test() is False

# Generated at 2022-06-13 23:59:30.698967
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Basic operation
    class Provider(BaseDataProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__datafile = 'test_data.json'
            self._pull()

        @property
        def _datafile(self) -> str:
            return self.__datafile

        @_datafile.setter
        def _datafile(self, value: str) -> None:
            self.__datafile = value

        def do_something(self) -> str:
            return self._data['test_key']['test_value']

    with Provider(locale='en') as p:
        assert p.get_current_locale() == 'en'
        assert p.do_something() == 'test_value'
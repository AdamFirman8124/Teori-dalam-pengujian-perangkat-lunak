

# Generated at 2022-06-13 23:50:46.991870
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.providers.misc import __
    from mimesis.enums import Locale
    class MyDataProvider(BaseDataProvider):
        def __init__(self):
            super().__init__(locale = Locale.EN)

    with contextlib.suppress(ValueError):
        MyDataProvider().override_locale()

    dp = Address(locale=Locale.NETHERLANDS)
    assert dp.get_current_locale() == dp.locale
    assert dp.get_current_locale() == __.locale

    with dp.override_locale() as new_dp:
        dp_locale = new_dp.get_current_locale()
        dp_locale == new_dp

# Generated at 2022-06-13 23:50:51.640258
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)

    test = Test()
    origin_locale = test.get_current_locale()
    with test.override_locale(locales.RU) as test:
        assert test.get_current_locale() == locales.RU
    assert test.get_current_locale() == origin_locale

# Generated at 2022-06-13 23:51:02.514577
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test of the BaseDataProvider.override_locale."""
    def get_method(provider, method):
        """Get method of the provider."""
        f = provider.__getattribute__(method)
        return f.__func__

    class SampleProvider(BaseDataProvider):
        """Sample provider for unit test."""

        def __init__(self, locale=locales.EN, seed=None):
            """Initialize attributes for provider."""
            super().__init__(locale, seed=seed)
            self.data = {'locale': 'en'}

        def _pull(self):
            """Set data for provider."""
            self.data = {'locale': 'en'}
            self.test = {'test': 'en'}

    provider = SampleProvider()

# Generated at 2022-06-13 23:51:06.728093
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person

    for locale in locales.SUPPORTED_LOCALES:
        with Person().override_locale(locale):
            assert Person().get_current_locale() == locale

    assert Person().get_current_locale() == locales.EN


# Generated at 2022-06-13 23:51:07.269424
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:51:16.002391
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    # assert provider.get_current_locale() == locales.DEFAULT_LOCALE
    # assert provider.__str__() == 'BaseDataProvider <en>'
    with provider.override_locale('ru') as new_provider:
        assert new_provider.get_current_locale() == 'ru'
        assert new_provider.__str__() == 'BaseDataProvider <ru>'
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE
    assert provider.__str__() == 'BaseDataProvider <en>'

# Generated at 2022-06-13 23:51:23.130877
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # initialize
    class Provider(BaseDataProvider):
        # ...
        pass

    provider = Provider(locale=locales.JA)

    # check
    with provider.override_locale(locales.RU) as p:
        assert p.get_current_locale() == locales.RU
        # ...

    assert provider.get_current_locale() == locales.JA
    # ...

    # ...
    # cleanup


# Generated at 2022-06-13 23:51:31.067526
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    # pylint: disable=W0212
    # pylint: disable=W0231
    class TestProvider(BaseDataProvider):
        """Class to test override_locale method."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                seed: Seed = None) -> None:
            """Initialize attributes for data providers.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(seed=seed)
            self._data: JSON = {}
            self._datafile = ''
            self._setup_locale(locale)
            self._data_dir = Path(__file__).parent.parent.joinpath('data')


# Generated at 2022-06-13 23:51:41.730343
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method `override_locale`.

    :return: Pass or Fail
    :rtype: bool
    """
    from mimesis.builtins import Generic
    from mimesis.enums import Gender

    g = Generic()
    g.reseed(240)
    with g.override_locale('ru') as gen:
        assert gen.person.full_name() == 'Катюша Демидова'
        assert gen.person.gender() == Gender.FEMALE

        assert gen.person.full_name(gender=Gender.MALE) == 'Паша Иванов'
        assert gen.person.gender(gender=Gender.MALE) == Gender.MALE

        assert gen.person.full_name(gender='male')

# Generated at 2022-06-13 23:51:50.784037
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.enums import Gender
    from mimesis.builtins import Person

    p = Person()

    with p.override_locale('ru') as person:
        gender = person.gender(Gender.MALE)
        assert gender == 'М'

    with p.override_locale('ru') as person:
        gender = person.gender(Gender.FEMALE)
        assert gender == 'Ж'

    gender = p.gender(Gender.FEMALE)
    assert gender == 'Female'

# Generated at 2022-06-13 23:52:07.878975
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override_locale method of BaseDataProvider."""
    class Provider(BaseDataProvider):
        """Dummy class."""

        def _setup_locale(self, locale: str) -> None:
            """Dummy method."""
            pass

        def _pull(self) -> None:
            """Dummy method."""
            pass

    provider = Provider(locale='en-US')
    with provider.override_locale(locale='de-DE'):
        assert provider.locale == 'de-DE'

    with provider.override_locale(locale='en-US'):
        assert provider.locale == 'en-US'

# Generated at 2022-06-13 23:52:15.824266
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class DataProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            self._datafile = 'street.json'
            super().__init__(locale=locale)
            self._pull()

        def street_name(self) -> str:
            return self.random.choice(self._data.get('streets'))

        def street_prefix(self) -> str:
            return self.random.choice(self._data.get('prefixes'))

    dp = DataProvider(locale='ru')

    with dp.override_locale(locale='it'):
        assert dp.street_prefix() == 'Piazza'


# Generated at 2022-06-13 23:52:16.512204
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert True

# Generated at 2022-06-13 23:52:27.582414
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override_locale context manager."""
    class MyDataProvider(BaseDataProvider):
        """Data provider class for testing."""

    data_provider = MyDataProvider()
    with data_provider.override_locale(locale='ru') as overridden_provider:
        assert overridden_provider.locale == 'ru'
        assert data_provider.locale == 'ru'
    assert data_provider.locale == locales.EN
    assert overridden_provider.locale == 'ru'

    with data_provider.override_locale(locale='es') as overridden_provider:
        assert overridden_provider.locale == 'es'
    assert data_provider.locale == locales.EN
    assert overridden_provider.locale == 'es'

# Generated at 2022-06-13 23:52:35.083131
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address
    from mimesis.enums import Gender

    with Address.override_locale('ru') as ru:
        ru_address = ru.address()

    with Address.override_locale('en') as en:
        en_address = en.address()

    assert ru_address != en_address
    with Address.override_locale('ru') as ru:
        assert ru.gender(gender=Gender.FEMALE) == 'Женский'

# Generated at 2022-06-13 23:52:41.424491
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.lorem import Lorem
    lorem = Lorem('ru')
    assert lorem.get_current_locale() == 'ru'
    with lorem.override_locale('en'):
        assert lorem.get_current_locale() == 'en'
    assert lorem.get_current_locale() == 'ru'
    assert lorem.get_sentence() == 'Ut nihil necessitatibus voluptatem.'
    with lorem.override_locale('ru'):
        assert lorem.get_current_locale() == 'ru'
    assert lorem.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:52:46.240505
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import AdministrativeDivision

    assert AdministrativeDivision.get_current_locale() == 'en'

    with AdministrativeDivision.override_locale('ru'):
        assert AdministrativeDivision.get_current_locale() == 'ru'

    assert AdministrativeDivision.get_current_locale() == 'en'


# Generated at 2022-06-13 23:52:53.637872
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FooProvider(BaseDataProvider):
        def get_current_locale(self):
            return self.locale

    fp = FooProvider('en')
    with fp.override_locale('ru') as fp:
        assert fp.get_current_locale() == 'ru'
    assert fp.get_current_locale() == 'en'


# Generated at 2022-06-13 23:52:58.157117
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None):
            super().__init__(locale=locale, seed=seed)
    tp = TestProvider()
    with tp.override_locale('ru'):
        assert tp.locale == 'ru'


# Generated at 2022-06-13 23:53:05.097516
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from .builtins import LanguageSpecProvider
    generate = LanguageSpecProvider.generate
    with LanguageSpecProvider().override_locale() as provider:
        assert provider.locale == locales.EN
        assert provider.generate() == generate()



# Generated at 2022-06-13 23:53:32.157269
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    de = BaseDataProvider(locale=locales.DE)
    assert de.get_current_locale() == locales.DE
    with de.override_locale(locales.EN):
        assert de.get_current_locale() == locales.EN
    assert de.get_current_locale() == locales.DE


# Generated at 2022-06-13 23:53:37.720440
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    p = BaseDataProvider()
    assert p.locale == 'en'
    p.locale = 'fr_FR'
    with p.override_locale('ru_RU') as provider:
        assert provider.locale == 'ru_RU'
    assert p.locale == 'fr_FR'
    try:
        with p.override_locale() as provider:
            raise ValueError
        raise ValueError
    except ValueError: pass



# Generated at 2022-06-13 23:53:43.295675
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    obj = BaseDataProvider()
    with obj.override_locale('uk'):
        pass
    assert getattr(obj, 'locale', locales.DEFAULT_LOCALE) == 'en'


# Generated at 2022-06-13 23:53:48.482357
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Example for using method override_locale.

    >>> import mimesis
    >>> personal = mimesis.Personal('en')
    >>> with personal.override_locale('ru'):
    ...     print(personal.full_name())
    ...
    Игорь Куралев
    >>> print(personal.full_name())
    Jack White
    """

# Generated at 2022-06-13 23:53:58.585387
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.address import Address
    from mimesis.enums import Currency

    address = Address()
    # After using the context manager the value of
    # the current locale will be uk
    with address.override_locale('uk') as addr:
        assert addr.get_current_locale() == 'uk'
        assert addr.currency(Currency.UAH) == 'грн.'
        assert address.get_current_locale() == 'en'
        assert address.currency(Currency.UAH) == 'UAH'
    assert address.get_current_locale() == 'en'

    # If the context manager is not used,
    # the method will always return an error.

# Generated at 2022-06-13 23:54:07.744646
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Foo(BaseDataProvider):
        seed = 'a'
        _datafile = 'bar.json'
        def get_data(self, key: str) -> Dict[str, Any]:
            return self._data[key]

    foo = Foo()
    assert foo.get_data('a') == {'a': 'A'}

    with foo.override_locale('ru') as foo:
        assert foo.get_data('a') == {'a': 'А'}

# Generated at 2022-06-13 23:54:19.015917
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class DataProvider(BaseDataProvider):
        """Data provider."""

        def get_data(self, data_type: str, datafile: str = '') -> Any:
            """Get data by type of data.

            :param data_type: Type of data.
            :param datafile: Data file name.
            :return: Data.
            """
            if not datafile:
                datafile = self._datafile

            self._pull(datafile=datafile)
            return self._data[data_type]

    dp = DataProvider()
    with dp.override_locale(locale='en') as dp:
        assert str(dp) == 'DataProvider <en>'
    assert str(dp) == 'DataProvider <en-US>'

# Generated at 2022-06-13 23:54:24.788379
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Language
    from mimesis.providers.code import Code
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.geo import Geo
    from mimesis.providers.internet import Internet
    from mimesis.providers.lorem import Lorem
    from mimesis.providers.misc import Misc
    from mimesis.providers.number import Number
    from mimesis.providers.payment import Payment
    from mimesis.providers.person import Person
    from mimesis.providers.science import Science
    from mimesis.providers.structures import Structures


# Generated at 2022-06-13 23:54:31.305170
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    p = Person()
    with p.override_locale('uk') as p:
        assert p.full_name() == (
            'Степан Григорович Сидоренко')
    assert p.full_name() == "Jason Spears"


# Generated at 2022-06-13 23:54:38.727929
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override_locale method of class BaseDataProvider."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    
    p1 = Person(seed=0)
    p2 = Person(seed=0)
    with p1.override_locale('de') as overridden:
        assert p1.full_name() == p2.full_name() == 'Jannik Peters'
        assert overridden.full_name() == 'Jannik Peters'
        assert overridden.gender() == 'male'
        assert overridden.gender() == p1.gender() == p2.gender() == Gender.MALE

    assert overridden.full_name() == 'Jannik Peters'
    assert overridden.gender() == Gender.MALE

# Generated at 2022-06-13 23:55:22.706013
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self):
            super().__init__(seed=None)

    with Provider().override_locale(locales.DE) as provider:
        assert provider.locale == locales.DE
    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:55:30.573046
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    demo = BaseDataProvider()

    default_locale = locales.EN

    demo.locale = default_locale
    assert demo.get_current_locale() == default_locale

    with demo.override_locale('ru'):
        assert demo.get_current_locale() == locales.RU

    assert demo.get_current_locale() == default_locale



# Generated at 2022-06-13 23:55:42.693192
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)

        def get_current_locale(self) -> str:
            return self.locale
    # END Class TestProvider
    tp = TestProvider()
    with tp.override_locale('en') as provider:
        assert provider.locale == 'en'
        assert tp.locale == 'en'
        provider._override_locale('ru')
        assert provider.locale == 'ru'
        assert tp.locale == 'ru'
    assert tp.locale == 'en'

# Generated at 2022-06-13 23:55:51.389886
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.identifier import Identifier

    d = Datetime(locale='en', seed=0)
    i = Identifier(seed=0)

    with d.override_locale('ru') as dt:
        with i.override_locale('ru') as id_:
            assert dt.get_current_locale() == 'ru'
            assert isinstance(dt, BaseDataProvider)
            assert id_.get_current_locale() == 'ru'
            assert isinstance(id_, BaseDataProvider)

    assert d.get_current_locale() == 'en'
    assert i.get_current_locale() == 'en'
    assert isinstance(d, BaseDataProvider)

# Generated at 2022-06-13 23:56:00.339968
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit-test for BaseDataProvider.override_locale"""
    from mimesis.builtins import Gender
    from mimesis.enums import Gender as GenderEnum

    class DummyProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE,
                     seed=None):
            super().__init__(locale=locale, seed=seed)
            self._data = {
                'en': {'foo': 'bar'},
                'ru': {'foo': 'бар'},
                'uk': {'foo': 'бар'},
            }

        def foo(self, gender: Gender = None):
            return getattr(self, 'gender')

    provider = DummyProvider()

    assert provider.locale == locales.DEFAULT_LOC

# Generated at 2022-06-13 23:56:03.954345
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    b = BaseDataProvider(locale="it")
    with b.override_locale(locale="ru"):
        assert b.locale == "ru"
    assert b.locale == "it"



# Generated at 2022-06-13 23:56:14.712774
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MultiLocaleProvider(BaseDataProvider):
        def __init__(self, seed: Seed = None):
            """Initialize attributes.

            :param seed: Seed for random.
            """
            super().__init__(seed=seed)

        @property
        def data(self):
            return self._data

        def __str__(self):
            return '{} <{}>'.format(self.__class__.__name__, self.locale)

    provider = MultiLocaleProvider()

    # Test
    with provider.override_locale(locales.RU):
        assert provider.data == {'_meta': {'locale': locales.RU}}

    assert provider.data == {'_meta': {'locale': locales.EN}}

# Generated at 2022-06-13 23:56:22.033746
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestClass(BaseDataProvider):
        pass
    obj = TestClass()
    obj._data = 'Test'

    with obj.override_locale(locale='ru') as o:
        assert o._data == 'Test'
        assert o.locale == 'ru'
    assert obj.locale == locales.DEFAULT_LOCALE
    assert obj._data == 'Test'



# Generated at 2022-06-13 23:56:28.249342
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    locale = 'en'
    seed = 1
    prv = BaseDataProvider(locale=locale, seed=seed)

    with prv.override_locale(locale='ru') as new_prv:
        assert new_prv.get_current_locale() == 'ru'
        assert new_prv.locale == 'ru'

    assert prv.get_current_locale() == 'en'
    assert prv.locale == 'en'


# Generated at 2022-06-13 23:56:33.900622
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.person import Person
    locale = 'ru'
    with Person(locale=locale).override_locale('en') as provider:
        assert provider.get_current_locale() == 'en'
        assert provider.full_name() in provider._data['person']['full_name']

# Generated at 2022-06-13 23:58:09.681210
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DataProvider(BaseDataProvider):
        class Meta:
            locales = ['en', 'ru']

    data_provider = DataProvider(seed=123)
    assert str(data_provider) == 'DataProvider <en>'
    with data_provider.override_locale('ru') as data_provider_with_ru_locale:
        assert str(data_provider_with_ru_locale) == 'DataProvider <ru>'
    assert str(data_provider) == 'DataProvider <en>'


# Generated at 2022-06-13 23:58:20.722352
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
   Provider = Dict[str, Any]

# Generated at 2022-06-13 23:58:27.212665
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Provider

    provider = Provider()

    with provider.override_locale(locales.DE) as p:
        assert p.get_current_locale() == locales.DE
        assert provider.get_current_locale() == locales.EN

    assert provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:58:34.774231
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis.providers.date as date_providers
    from mimesis.providers.builtins import LocaleProvider

    def get_locale(provider: BaseDataProvider) -> str:
        return getattr(provider, 'locale', locales.DEFAULT_LOCALE)

    with date_providers.Date('ru').override_locale('en') as provider:
        assert get_locale(provider) == 'en'

    assert get_locale(date_providers.Date('ru')) == 'ru'

    with LocaleProvider().override_locale('en') as provider:
        assert get_locale(provider) == locales.DEFAULT_LOCALE
    # End unit test for override_locale BaseDataProvider



# Generated at 2022-06-13 23:58:46.950194
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    
    try:
        with BaseDataProvider().override_locale('ru'):
            pass
        # self._override_locale
        assert False
    except Exception as e:
        assert str(e) == "«BaseDataProvider» has not locale dependent"
    
    try:
        with BaseDataProvider(locale = 'ru').override_locale('ru'):
            assert BaseDataProvider(locale = 'ru').locale == 'ru'
        # self._override_locale
        assert False
    except Exception as e:
        assert str(e) == "«BaseDataProvider» has not locale dependent"

# Generated at 2022-06-13 23:58:52.616659
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person, Datetime
    from mimesis.enums import Gender

    p = Person()
    d = Datetime()

    with p.override_locale('ru'):
        assert isinstance(p.full_name(Gender.MALE), str)
        assert isinstance(p.full_name(Gender.FEMALE), str)
        assert isinstance(d.date(), str)
        assert isinstance(d.time(), str)


# Generated at 2022-06-13 23:59:05.278710
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DemoProvider(BaseDataProvider):
        def get_current_locale(self):
            return self.locale

    provider = DemoProvider()
    assert provider.get_current_locale() == provider.DEFAULT_LOCALE
    with provider.override_locale('ru_RU'):
        assert provider.get_current_locale() == 'ru_RU'
    assert provider.get_current_locale() == provider.DEFAULT_LOCALE

    # This value is not locale-dependent, so it is not possible to override
    class DemoNonProvider(BaseProvider):
        def get_current_locale(self):
            return self.locale
    provider = DemoNonProvider()
    assert provider.get_current_locale() == provider.DEFAULT_LOCALE

# Generated at 2022-06-13 23:59:12.089970
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Data(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None,
                     **kwargs: Any) -> None:
            super().__init__(locale, seed)

    class Override(BaseDataProvider):
        file = '__test_override_locale.json'

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None,
                     **kwargs: Any) -> None:
            super().__init__(locale, seed)
            self._datafile = self.file

    kwargs = {'lang': 'it'}

    with Override(**kwargs) as provider:
        assert provider.get_current_locale() == 'it'
        assert provider

# Generated at 2022-06-13 23:59:20.195969
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import random as real_random
    import mimesis

    # Set up testing data
    real_random.seed(1)
    first = real_random.random()
    print(first)

    provider = mimesis.Address()
    origin_locale = provider.get_current_locale()

    # Use context-manager override_locale
    with provider.override_locale(mimesis.RU):
        print(real_random.random())
        new_locale = provider.get_current_locale()
        assert new_locale == mimesis.RU, 'Error'

    # Check random generator
    old_seed = real_random.getstate()

    print(real_random.random())
    provider.reseed(1)
    print(real_random.random())
    provider.reseed

# Generated at 2022-06-13 23:59:23.216090
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        pass

    provider = Provider()
    provider.override_locale(locale='en')


# Generated at 2022-06-13 23:50:48.658946
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Address, Names

    def get_address(names: Names, address: Address) -> str:
        """Get address."""
        with address.override_locale('ru'):
            full_name = (names.full_name(), 'country')
            return address.address(full_name)

    names = Names()
    address = Address()
    result = get_address(names, address)
    answer = 'Королев Анастасия Тарасовна, ул. Самаркандская, 14'
    assert result == answer

# Generated at 2022-06-13 23:50:58.832631
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

        @property
        def prop(self):
            return self.locale

    provider = TestProvider(locale='ru')
    test_locale = 'en'

    with provider.override_locale(test_locale) as p:
        assert p.prop == test_locale
        assert provider.prop == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:08.117154
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    import mimesis.providers.geography as geography
    with geography.Geography.override_locale('fr'):
        assert geography.Geography().country_name() == 'États-Unis'
    with geography.Geography.override_locale('en'):
        assert geography.Geography().country_name() == 'United States'


BaseDataProvider.test_BaseDataProvider_override_locale = \
    test_BaseDataProvider_override_locale

# Generated at 2022-06-13 23:51:13.255407
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import City
    a = City()
    with a.override_locale('kk') as b:
        assert b.locale == 'kk'

    assert a.locale == 'en'

# Generated at 2022-06-13 23:51:19.603220
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person()
    with p.override_locale(locales.RU):
        assert p.get_current_locale() == 'ru'
        assert p.get_full_name(gender=Gender.FEMALE) == 'Татьяна Владимировна Петрова'
    assert p.get_current_locale() == locales.DEFAULT_LOCALE
    assert p.get_full_name(gender=Gender.FEMALE) == 'Carol Alba'

# Generated at 2022-06-13 23:51:22.324839
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider('en')
    with provider.override_locale('ru') as data_provider:
        assert data_provider.locale == 'ru'

# Generated at 2022-06-13 23:51:29.743908
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = 'zz'

    fake = BaseDataProvider(locale='ru')

    fake.get_current_locale() == locals.DEFAULT_LOCALE
    fake.override_locale(locale=locale)
    fake.get_current_locale() == locale
    fake.get_current_locale() == locals.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:30.639083
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:51:39.640077
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    with Person('en').override_locale('ru') as p:
        locale = p.get_current_locale()
        name = p.full_name(gender=Gender.MALE)
    assert name == 'Александр Козлов'
    assert locale == 'ru'

# Generated at 2022-06-13 23:51:46.110231
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MockProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

        def _pull(self, datafile: str = '') -> None:
            pass

    provider = MockProvider('en')

    with provider.override_locale('ru'):
        assert provider.get_current_locale() == 'ru'

    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:52:02.887779
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.exceptions import ValueError

    addr = Address(locale='en')
    with addr.override_locale(locale='ru'):
        assert addr.get_current_locale() == 'ru'
        assert addr.city() == 'Краснодар'
    try:
        with addr.override_locale(locale='ru'):
            assert False
    except ValueError:
        assert True

# Generated at 2022-06-13 23:52:11.323461
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Creating an instance of the BaseDataProvider
    random_provider = BaseDataProvider(locale='en')
    # Checking the method
    assert 'BaseDataProvider <en>' == str(random_provider)
    # Override locale
    with random_provider.override_locale('ru'):
        assert 'BaseDataProvider <ru>' == str(random_provider)
    assert 'BaseDataProvider <en>' == str(random_provider)
# End of testing method override_locale of class BaseDataProvider

# Generated at 2022-06-13 23:52:20.257354
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.datetime import Datetime
    en = Datetime()
    ru = Datetime(locale='ru')
    assert en.day_of_week() != ru.day_of_week()
    with ru.override_locale('en'):
        assert en.day_of_week() == ru.day_of_week()
    assert en.day_of_week() != ru.day_of_week()

# Generated at 2022-06-13 23:52:25.486538
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    adr = BaseDataProvider()
    with adr.override_locale('en'):
        assert adr.locale == 'en'

# Generated at 2022-06-13 23:52:33.875033
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis.builtins
    provider = mimesis.builtins.Data

    with provider.override_locale(locales.EN):
        assert provider.get_current_locale() == locales.EN
        assert provider.get_locale() == locales.EN

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE
    assert provider.get_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:44.046022
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """
    This function is a unit test for method override_locale of class BaseDataProvider
    """
    class TestDataProvider(BaseDataProvider):
        """This is a class for testing override_locale method."""

        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None) -> None:
            """Initialize attributes in class TestDataProvider."""
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test.json'

        def get_data(self, key: str) -> JSON:
            """Get data from JSON file.

            :param key: Key of data in JSON file.
            :return: Data from JSON file.
            """
            self._pull()
            return self._data[key]

    # Tests for providers with locales:
   

# Generated at 2022-06-13 23:52:48.897055
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeProvider(BaseDataProvider):
        def __init__(self):
            super().__init__(locale='en')

    provider = FakeProvider()
    with provider.override_locale('ru') as provider_russian:
        assert provider.locale == 'en'
        assert provider_russian.locale == 'ru'

    assert provider.locale == 'en'

# Generated at 2022-06-13 23:52:57.403394
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Initialize provider
    provider = BaseDataProvider()
    # Override locale (a) using context manager
    with provider.override_locale('uk') as new_provider:
        # Override locale (b) using context manager
        with new_provider.override_locale('ru') as new_provider_b:
            new_provider_b.get_current_locale()
        # New locale (b) is overriden by locale (a)
        new_provider.get_current_locale()
    # Locale (a) is overriden by default locale
    provider.get_current_locale()

# Generated at 2022-06-13 23:53:10.661579
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Example(BaseDataProvider):
        """Example class which is a subclass of BaseDataProvider."""

        def __init__(self, locale: str = locales.EN) -> None:
            super().__init__(locale)
            self._datafile = 'example.json'
            self._pull()

        def __str__(self) -> str:
            """Print info about current locale."""
            return super().__str__()

        def get_name(self, name: str) -> str:
            """Get name for locale.

            :param name: Name for locale.
            :return: Example.
            """
            return self._data[name]

    example = Example()
    assert str(example) == 'Example <en>'
    assert example.get_name('name') == 'Example'

# Generated at 2022-06-13 23:53:19.949053
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Data(BaseDataProvider):
        _datafile = 'test.json'
        def __init__(self, seed=None):
            super().__init__(seed=seed)

        def get_test(self):
            return self._data['test']

    data = Data(seed=12345)
    with data.override_locale('ru') as provider:
        assert provider.locale == 'ru'
        assert data.get_test() == 'data'

    assert data.locale == 'en'
    assert data.get_test() == 2

# Generated at 2022-06-13 23:53:45.354067
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    dp = BaseDataProvider()
    locale = 'zz'
    with dp.override_locale(locale) as d:
        assert d.locale == locale
        assert d.get_current_locale() == locale
    assert dp.locale != locale

# Generated at 2022-06-13 23:53:53.467063
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method BaseDataProvider.override_locale."""
    providers = [
        'Personal', 'Business', 'Commerce', 'Address', 'Code', 'Cryptographic',
        'DateTime', 'FileSystem', 'Food', 'Government', 'Internet',
        'Lorem', 'Payment', 'Person', 'Text', 'Transport', 'University',
        'Weather'
    ]

    test_values = {
        'en': 'i luv you',
        'ru': 'я люблю тебя',
        'de': 'ich liebe dich',
        'es': 'te quiero'
    }

    for provider in providers:
        p = getattr(locales, provider)(seed=0)

# Generated at 2022-06-13 23:53:58.144287
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import RussiaSpecProvider
    a = RussiaSpecProvider("ru", datafile="holidays.json")
    with a.override_locale("RU") as day:
        x = day.get_new_year_date()
        y = day.get_new_year_date()
        assert x == y
        z = day.get_new_year_date("RU")
        assert z == y and z != "1-1"



# Generated at 2022-06-13 23:54:11.853402
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Food

    bdp = BaseDataProvider()
    with bdp.override_locale('en') as provider:
        assert bdp.locale == 'en'
        assert provider == bdp
        assert bdp.get_current_locale() == 'en'
        assert Food().get_current_locale() == 'en'
        assert provider.get_current_locale() == 'en'

        assert Food().get_current_locale() == 'en'
        # assert not hasattr(bdp, 'locale')
        assert provider.locale == 'en'
        assert bdp.locale == 'en'

    assert bdp.get_current_locale() != 'en'
    assert bdp.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:54:21.321447
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class TestProvider(BaseDataProvider):
        _datafile = 'test.json'

        def get_something(self) -> Dict[str, str]:
            return self._data

    test_provider = TestProvider(locale='en')

    # If the method is called with an acceptable locale,
    # the context manager blocks the execution
    # and returns the provider itself.
    with test_provider.override_locale(locale='en') as tp:
        # Passed locale as argument should be get by the provider
        assert tp.get_current_locale() == 'en'
        # Data is always read from file en/test.json
        assert tp.get_something() == {
            'locale': 'en',
            'value': 'english',
        }

    # Any non-acceptable locale will rise an

# Generated at 2022-06-13 23:54:25.187522
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Text

    t = Text()
    with t.override_locale('ru') as text:
        assert text.get_current_locale() == 'ru'

        t = Text()

        assert t.get_current_locale() == 'uk'

# Generated at 2022-06-13 23:54:30.286137
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class A(BaseDataProvider):
        def arg(self, item=None):
            return item
    a = A('de')
    with a.override_locale(locale='ru'):
        assert a.arg('germany') == 'germany'
    assert a.arg('russia') == 'russia'

# Generated at 2022-06-13 23:54:35.324707
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MockDataProvider(BaseDataProvider):
        pass

    mock = MockDataProvider()
    with mock.override_locale(locales.EN) as mdp:
        assert mdp is mock
        assert mdp.get_current_locale() == locales.EN

    assert mock.get_current_locale() == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:54:40.973532
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    from mimesis.enums import Gender

    person = Person('ru')
    person.gender = Gender.MALE
    with person.override_locale('en'):
        person.gender = Gender.FEMALE
    assert person.gender == Gender.MALE



# Generated at 2022-06-13 23:54:48.053297
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    provider = BaseDataProvider(locale='en')
    # check that context manager works
    with provider.override_locale('ru'):
        assert provider.locale == 'ru'
    # check that context manager returns origin_locale
    assert provider.locale == 'en'



# Generated at 2022-06-13 23:55:40.757470
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Address
    from mimesis.enums import CountrySubdivisionType
    with Address(locale='en') as a:
        # Check locales
        assert a.get_current_locale() == 'en'
        assert a.PROVIDER_LOCALE == 'en'
        # Check override_locale method
        with a.override_locale(locale='ru') as rus_a:
            assert rus_a.get_current_locale() == 'ru'
            assert a.get_current_locale() == 'ru'
            assert rus_a.PROVIDER_LOCALE == 'ru'
            assert rus_a.address.street_name() != a.address.street_name()

# Generated at 2022-06-13 23:55:48.213578
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class SomeProvider(BaseDataProvider):
        def __init__(self, locale: str = 'en', seed: Seed = None):
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test_file.json'

    with SomeProvider() as p:
        assert str(p) == 'SomeProvider <en>'
        with p.override_locale('ru') as p:
            assert str(p) == 'SomeProvider <ru>'
        assert str(p) == 'SomeProvider <en>'

# Generated at 2022-06-13 23:55:59.450604
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person

    name_ru = Person('ru').full_name()
    name_default = Person().full_name()
    with Person().override_locale('ru') as person_ru:
        assert name_ru == person_ru.full_name()
    assert name_default == Person().full_name()

    with Person().override_locale(None) as person_default:
        assert name_default == person_default.full_name()
    assert name_default == Person().full_name()

    try:
        with Person('ru').override_locale('ru') as person_ru:
            assert name_ru == person_ru.full_name()
    except:
        pass

# Generated at 2022-06-13 23:56:05.498764
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Person

    p = Person(seed=1337)
    p.seed = None
    for flag in (True, False):
        with p.override_locale('ru'):
            pass

    for flag in (True, False):
        with p.override_locale('en'):
            pass

    for flag in (True, False):
        with p.override_locale('ru'):
            pass

    assert p.locale == 'en'



# Generated at 2022-06-13 23:56:11.882954
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Address
    a = Address()
    with a.override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'
        assert provider.country() == 'Россия'
        assert isinstance(provider, BaseDataProvider)
    assert provider.get_current_locale() == 'en'


# Generated at 2022-06-13 23:56:16.513848
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    with provider.override_locale('ru') as instance:
        assert instance.locale == locales.RU
    assert provider.locale == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:56:27.524808
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class AbstractDataProvider(BaseDataProvider):
        @property
        def value(self) -> int:
            return 1
    class MyDataProvider(AbstractDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)
            self._file = 'test.json'
            self._pull()
    class MyDataProvider2(AbstractDataProvider):
        @property
        def value(self) -> int:
            return 1
    provider: BaseDataProvider = MyDataProvider(locale=locales.EN)
    provider2: BaseDataProvider = MyDataProvider2(locale=locales.EN)
    locale: str = 'ru'
    value: int = 1


# Generated at 2022-06-13 23:56:34.471827
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Generic
    from re import match
    with BaseDataProvider.override_locale('ru'):
        assert match(r'Случайное число: \d+', Generic('ru').random_number())
    assert match(r'Random number: \d+', Generic('en').random_number())

# Generated at 2022-06-13 23:56:40.984502
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    dp = BaseDataProvider()
    dp.get_current_locale = lambda: locales.RU
    assert dp.get_current_locale() == locales.RU

    with dp.override_locale(locales.EN):
        assert dp.get_current_locale() == locales.EN

    assert dp.get_current_locale() == locales.RU

    with dp.override_locale(locales.EN):
        assert dp.get_current_locale() == locales.EN

        with dp.override_locale(locales.DE):
            assert dp.get_current_locale() == locales.DE

        assert dp.get_current_locale() == locales.EN

    assert dp.get_current_loc

# Generated at 2022-06-13 23:56:49.048450
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    
    # Default locale is English.
    provider = BaseDataProvider()
    assert provider.get_current_locale() == 'en'

    # Check that locale will be overridden.
    with provider.override_locale('ru') as result:
        assert result == provider
        assert provider.get_current_locale() == 'ru'

    # Check that locale will be restored on exit.
    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:58:21.592099
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Foo(BaseDataProvider):

        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)

        def get_current_locale(self) -> str:
            """Get current locale.

            If locale is not defined then this method will always return ``en``,
            because ``en`` is default locale for all providers, excluding builtins.

            :return: Current locale.
            """
            return self.locale

        def _override_locale(self, locale: str = locales.DEFAULT_LOCALE) -> None:
            """Overrides current locale with passed and pull data for new locale.

            :param locale: Locale
            :return: Nothing.
            """
            self.locale = locale


# Generated at 2022-06-13 23:58:28.391514
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    global test
    test = {}
    provider = BaseDataProvider()
    data = {}
    provider._pull = lambda : data.update(ru={'override_locale': 'test'})
    with provider.override_locale():
        pass
    assert (data['ru']['override_locale']) == 'test'

# Generated at 2022-06-13 23:58:34.748601
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale='en')
    assert provider.get_current_locale() == locales.EN
    with provider.override_locale(locale='ru') as pr:
        assert pr == provider
    assert provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:58:45.201209
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def get_current_locale(self):
            return self.locale
    provider = TestProvider()
    provider.locale = 'en'
    with provider.override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'
    assert provider.locale == 'en'
    with provider.override_locale('zh') as provider:
        assert provider.get_current_locale() == 'zh'
    assert provider.locale == 'en'

# Generated at 2022-06-13 23:58:54.175497
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """BaseDataProvider: Test that you should be able to specify a locale
    for a provider for a certain period of time.
    """
    from mimesis import Address, Personal
    from mimesis.enums import Gender

    de = Personal('de')
    ru = Sex()

    with ru.override_locale('ru'):
        assert ru.get_current_locale() == 'ru'
        assert ru.male() == 'Мужской'

    assert ru.get_current_locale() == 'en'
    assert ru.male() == 'Male'
    assert ru.male(full=True) == 'Male'

    with ru.override_locale('ru'):
        assert ru.male() == 'Мужской'

# Generated at 2022-06-13 23:58:59.124954
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert True
    

# Generated at 2022-06-13 23:59:03.947491
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    p = BaseDataProvider()
    with p.override_locale(locales.EN):
        e = p.get_current_locale()
        assert e == locales.EN
    d = p.get_current_locale()
    assert d == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:59:10.594478
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.internet import Internet
    from mimesis.providers.person import Person

    internet = Internet()
    with internet.override_locale('ko') as provider:
        assert provider.locale == 'ko'
        assert provider.domain_name() == 'hanmail.net'

    person = Person()
    with person.override_locale('ru') as provider:
        assert provider.full_name() == 'Евгений Горбунов'

    with internet.override_locale() as provider:
        assert provider.locale == 'en'
        assert provider.tld() == 'com'

# Generated at 2022-06-13 23:59:20.197578
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''Test method override_locale of class BaseDataProvider'''

    class MyProvider(BaseDataProvider):
        def get_current_locale(self):
            return self.locale

    # Check if exception is raised with non-localized provider
    my_provider = MyProvider()
    with pytest.raises(ValueError):
        with my_provider.override_locale():
            pass

    # Check if override_locale method is work for localized data providers
    my_provider = MyProvider(locale='ru')
    with my_provider.override_locale():
        assert my_provider.get_current_locale() == 'en'

    with my_provider.override_locale('en'):
        assert my_provider.get_current_locale() == 'en'



# Generated at 2022-06-13 23:59:25.988755
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.files import Files
    a = 'Hello {}'.format(Files(locale='en').file_name())
    with Files().override_locale(locale='en') as f:
        b = 'Hello {}'.format(f.file_name())
    assert a == b


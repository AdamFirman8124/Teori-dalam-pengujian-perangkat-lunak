

# Generated at 2022-06-13 23:50:46.442342
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    from mimesis.builtins import (
        Business,
        Food,
        Person,
    )

    person = Person()
    business = Business()
    food = Food()

    def assert_random(provider: BaseDataProvider) -> None:
        """Check that the provider has changed its locale.

        :param provider: Provider.
        :return: Nothing.
        """
        locale = provider.get_current_locale()
        assert locale == locales.EN
        assert person.last_name() != provider.last_name()
        assert person.last_name(locale=locale) == provider.last_name()
        assert business.company() != provider.company()
        assert business.company(locale=locale) == provider.company()

# Generated at 2022-06-13 23:50:52.666026
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class SuperProvider(BaseDataProvider):
        pass

    global provider
    provider = SuperProvider()
    with provider.override_locale(locales.EN):
        assert provider.get_current_locale() == locales.EN
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:01.571780
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis import Address, Person

    assert Address().locale == locales.EN
    assert Person().locale == locales.EN

    with Address().override_locale(locales.RU) as address:
        assert address.locale == locales.RU
        assert address.full_address() != Address().full_address()

    assert Address().locale == locales.EN

    with Person().override_locale(locales.RU) as person:
        assert person.locale == locales.RU
        assert person.full_name() != Person().full_name()

    assert Person().locale == locales.EN

# Generated at 2022-06-13 23:51:13.296088
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.datetime import Datetime
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider

    dt = Datetime(locale='ru')
    with dt.override_locale('en') as dt:
        assert dt.get_current_locale() == 'en'
        assert dt.date() == '02/28/1995'

    assert dt.get_current_locale() == 'ru'
    assert dt.date() == '28.02.1995'

    rus = RussiaSpecProvider(locale='ru')
    with rus.override_locale('en') as rus:
        assert rus.get_current_locale() == 'en'

# Generated at 2022-06-13 23:51:22.273053
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address
    from mimesis.enums import Gender

    address = Address()
    with address.override_locale('ru'):
        assert address.full_address(
            gender=Gender.FEMALE,
            min_zip_code=101000,
            max_zip_code=101000
        ) == 'Москва, Кусковское шоссе, д. 1, кв. 1'


# Generated at 2022-06-13 23:51:30.488406
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyProvider(BaseDataProvider):

        def __init__(self):
            super().__init__()
            self._datafile = 'foo'

        def foo(self, locale: str = locales.EN) -> str:
            return locale

    provider = MyProvider()
    assert (provider.locale == 'en')
    with provider.override_locale('ru'):
        assert (provider.foo() == 'ru')
    assert (provider.foo() == 'en')
    with provider.override_locale():
        assert (provider.foo() == 'en')
        with provider.override_locale('ru'):
            assert (provider.foo() == 'ru')


# Generated at 2022-06-13 23:51:38.090389
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the context manager «override_locale»."""
    class A(BaseDataProvider):
        def foo(self):
            return self.locale
    a = A()
    assert a.locale == locales.DEFAULT_LOCALE
    assert a.foo() == locales.DEFAULT_LOCALE
    with a.override_locale('ru'):
        assert a.locale == 'ru'
        assert a.foo() == 'ru'
    assert a.locale == locales.DEFAULT_LOCALE
    assert a.foo() == locales.DEFAULT_LOCALE

    class B:
        def foo(self):
            return self.locale
    b = B()
    try:
        with b.override_locale('ru'):
            pass
    except ValueError:
        pass

# Generated at 2022-06-13 23:51:47.209296
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        class Meta:
            locales = ['ru']

        def __init__(self, provider: str, *args, **kwargs) -> None:
            super(Provider, self).__init__(*args, **kwargs)
            self.provider = provider

    p1 = Provider('p1', 'ru_RU')
    assert p1.provider == 'p1'
    assert p1.locale == 'ru_ru'
    p2 = Provider('p2', 'en_US')

    with p1.override_locale('ru_RU'):
        assert p1.locale == 'ru_ru'
        assert p1.provider == 'p1'
        assert p2.locale == 'en_us'


# Generated at 2022-06-13 23:51:54.323156
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address
    from mimesis.enums import Gender
    from mimesis.providers import TelephoneCode

    tp = TelephoneCode(locale='nl_NL')

    with tp.override_locale('en') as prv:

        tp_en = prv
        assert tp_en.get_current_locale() == 'en'

        assert tp_en.get_telephone_code() == '+54'
        assert tp_en.get_telephone_code('AR') == '+54'

    with tp.override_locale('ru') as prv:

        tp_ru = prv
        assert tp_ru.get_current_locale() == 'ru'


# Generated at 2022-06-13 23:52:00.592453
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):

        def get_current_locale(self) -> str:
            return super().get_current_locale()

    p = TestProvider(locale='ru')
    with p.override_locale('en'):
        assert p.get_current_locale() == 'en'


# Generated at 2022-06-13 23:52:16.232010
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override locale."""
    class Sample(BaseDataProvider):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def get_locale(self):
            return self.get_current_locale()


    sample = Sample(seed=123)
    assert sample.get_locale() == 'en'

    with sample.override_locale('ru'):
        assert sample.get_locale() == 'ru'

    with sample.override_locale('sk'):
        assert sample.get_locale() == 'sk'

    assert sample.get_locale() == 'en'



# Generated at 2022-06-13 23:52:21.358357
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Dummy(BaseDataProvider):
        pass

    dummy = Dummy()
    with dummy.override_locale('ru') as dummy_ru:
        assert dummy_ru.locale == 'ru'

    assert dummy.locale == 'en'



# Generated at 2022-06-13 23:52:29.298314
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person

    person = Person(locale='en')

    with person.override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'
        assert isinstance(p.full_name(), str)

    with person.override_locale() as p:
        assert p.get_current_locale() == locales.DEFAULT_LOCALE
        assert isinstance(p.full_name(), str)

    assert person.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:52:38.174136
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale='ru')
    try:
        with provider.override_locale('en'):
            assert provider.get_current_locale() == 'en'
    except ValueError:
        pass
    else:
        raise ValueError("BaseDataProvider has not locale dependent")

    def get_locale(self):
        return self.locale

    BaseDataProvider.get_current_locale = get_locale

    try:
        with provider.override_locale('en'):
            assert provider.get_current_locale() == 'en'
    except ValueError:
        pass
    else:
        raise ValueError("BaseDataProvider has not locale dependent")

    # reset BaseDataProvider
    BaseDataProvider._pull.cache_clear()
    BaseDataProvider._pull = BaseDataProvider._

# Generated at 2022-06-13 23:52:39.885802
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import RussiaSpecProvider
    ru_provider = RussiaSpecProvider()
    ru_provider.override_locale('ru')

# Generated at 2022-06-13 23:52:43.803870
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    number = Number(seed=123456789)
    with number.override_locale('ru') as num:
        assert num.one() == 'один'

# Generated at 2022-06-13 23:52:50.934801
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test BaseDataProvider override_locale."""
    import mimesis.builtins as builtins
    from mimesis.builtins import ListDataProvider

    provider = ListDataProvider('en')
    # All locales are supported by ListDataProvider
    supported_locales = list(locales.SUPPORTED_LOCALES)
    supported_locales.remove('en')
    with provider.override_locale(supported_locales[0]):
        # You don't need to write anything here!
        pass

    # Test when locale is unsupported
    with provider.override_locale('unknown'):
        assert provider.locale == 'unknown'

    # Test if provider is non-locale-dependent
    with builtins.Person(seed=42).override_locale('unknown'):
        assert builtins.Person

# Generated at 2022-06-13 23:52:56.756353
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Creates object of class BaseDataProvider for test."""
    provider = BaseDataProvider()
    with provider.override_locale(locale=locales.UA):
        assert provider.locale == locales.UA
    assert provider.locale == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:53:10.106878
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    # Set up data
    class MyProvider(BaseDataProvider):
        """My provider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes for data providers.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale=locale, seed=seed)
            self._data: JSON = {}
            self._datafile = ''
            self._setup_provider()

        def _setup_provider(self) -> None:
            """Set up provider."""
            # Set up content of JSON file for locale en and ru

# Generated at 2022-06-13 23:53:21.966910
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # define a new class
    class TestDataProvider(BaseDataProvider):
        __attributes__ = ['gender']
        _datafile = 'test.json'
        def __init__(self):
            super().__init__(locale='en')
        def get_gender(self):
            return self._data['gender']

    # instantiate test class
    test_class = TestDataProvider()
    # set reference value
    expected = 'Female'
    # switch locale
    with test_class.override_locale('ru_RU'):
        # check locale
        assert test_class.locale == 'ru_RU'
        # check gender
        assert test_class.get_gender() == expected
    # restore locale
    assert test_class.locale == 'en'

# Generated at 2022-06-13 23:53:35.217301
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override_locale method"""
    class TestDataProvider(BaseDataProvider):
        """Test data provider for unit tests"""
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def override_locale(self, locale):
            return super().override_locale(locale)

    data_provider = TestDataProvider(locale='en-US')
    with data_provider.override_locale('ru-RU') as ru:
        ru_locale = ru.get_current_locale()
    assert ru_locale == 'ru-RU'


# Generated at 2022-06-13 23:53:44.900917
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)
            self._datafile = 'test.json'

        def _pull(self, datafile: str = '') -> None:
            super()._pull(datafile)
            self._data = {
                'test': 'this is a test'
            }

        def get_test(self) -> str:
            return self._data['test']

    provider = TestDataProvider(locale=locales.EN, seed=42)
    assert provider.get_test() == 'this is a test'

    provider = TestDataProvider(locale=locales.RU, seed=42)
    assert provider.get_test

# Generated at 2022-06-13 23:53:52.305470
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FooProvider(BaseDataProvider):
        def __init__(self, locale='en', seed=None):
            super().__init__(locale=locale, seed=seed)

    provider = FooProvider()
    provider.locale = 'en'
    with provider.override_locale('ru') as p:
        assert p == provider
        assert p.locale == 'ru'
    assert provider.locale == 'en'

# Generated at 2022-06-13 23:53:55.208495
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method ``override_locale`` of class ``BaseDataProvider``."""
    from mimesis.builtins import Person

    with Person().override_locale('ru') as p:
        assert p.name() != Person().name()

# Generated at 2022-06-13 23:53:58.710951
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    with BaseDataProvider().override_locale(locales.CS) as dp:
        assert dp.locale == locales.CS

# Generated at 2022-06-13 23:54:02.111147
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis import Person

    origin_locale = Person().get_current_locale()
    russian_locale = 'ru'

    person = Person()
    assert origin_locale == person.get_current_locale()
    with person.override_locale(locale=russian_locale):
        assert russian_locale == person.get_current_locale()
    assert origin_locale == person.get_current_locale()

# Generated at 2022-06-13 23:54:12.676949
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person('en', seed=11)
    name = p.full_name(gender=Gender.FEMALE)
    assert name == 'Ruth Fleming'

    with p.override_locale('ru'):
        name = p.full_name(gender=Gender.FEMALE)
        assert name == 'Виктория Морозова'

    name = p.full_name(gender=Gender.FEMALE)
    assert name == 'Ruth Fleming'

# Generated at 2022-06-13 23:54:20.810554
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    assert provider.locale == 'en'
    with provider.override_locale(locales.DEFAULT_LOCALE) as overridden:
        assert overridden == provider
        assert provider.locale == locales.DEFAULT_LOCALE
    assert provider.locale == 'en'

    provider.locale = locales.DEFAULT_LOCALE
    with provider.override_locale() as overridden:
        assert overridden == provider
        assert provider.locale == 'en'
    assert provider.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:54:29.375730
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.payment import Payment
    p = Payment()
    payment_types = p.payment_method()
    with p.override_locale('de_DE') as provider:
        payment_types_de = provider.payment_method()

    payment_types_de_diff = list(set(payment_types_de) - set(payment_types))
    assert payment_types_de_diff
    assert payment_types_de_diff[0] == 'Girocard'

# Generated at 2022-06-13 23:54:33.640717
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class User(BaseDataProvider):
        pass

    user = User(locale='ru')
    assert user.get_current_locale() == 'ru'

    with user.override_locale('en'):
        assert user.get_current_locale() == 'en'

    assert user.get_current_locale() == 'ru'


# Generated at 2022-06-13 23:54:51.259985
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Create an instance of class BaseDataProvider with
    # the following parameters:
    # locale='ru'
    provider = BaseDataProvider(locale='ru')
    # Call method override_locale of provider with the
    # following parameter:
    # locale='en'
    with provider.override_locale(locale='en'):
        # Check that the result of calling __str__ of provider
    # is equal to the string 'BaseDataProvider <en>'
        assert str(provider) == 'BaseDataProvider <en>'
    # Check that the result of calling __str__ of provider
    # is equal to the string 'BaseDataProvider <ru>'
    assert str(provider) == 'BaseDataProvider <ru>'


# Generated at 2022-06-13 23:54:54.221475
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Unit
    # Override locale for the current context using the context manager
    with Unit('ru').override_locale() as unit:
        assert unit.languages == ['русский']

# Generated at 2022-06-13 23:55:05.677764
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''
    Test for BaseDataProvider class instance.
    :return: void
    '''
    x=True
    print('Test BaseDataProvider class instance')
    print('BaseDataProvider: override_locale method test')
    class TestDataProvider(BaseDataProvider):
        '''
        Class for testing BaseDataProvider instance
        '''
        class Meta:
            '''
            Internal class for testing BaseDataProvider instance
            '''
            locales = ['en']
            provider = 'test'
        def __init__(self, locale = locales.DEFAULT_LOCALE,
                         seed = None) -> None:
            '''
            Metod override class initializer
            :param locale: current locale
            :param seed: see for random()
            '''
            self.seed = seed
            self.random = random
           

# Generated at 2022-06-13 23:55:06.056899
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert True

# Generated at 2022-06-13 23:55:10.663389
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address
    from mimesis.enums import Country

    address = Address('en')
    country = Country.ENGLAND
    with address.override_locale('ru') as address:
        assert address.country(code=country.value) == \
            'Великобритания'



# Generated at 2022-06-13 23:55:19.527196
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins.numbers import Numbers
    n = Numbers()

    # If locale is not defined then this method will always return
    # "en", because "en" is default locale for all providers,
    # excluding builtins.

    with n.override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'
        assert len(repr(p)) == len('Numbers <ru>')

    assert p.get_current_locale() == 'ru'

    # Unit test for value error.
    # Make sure that context manager override_locale
    # raises an error if the instance of BaseDataProvider
    # is not locale dependent.

    from mimesis.builtins.numbers import Number
   

# Generated at 2022-06-13 23:55:23.004171
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def _pull(self):
            self._data = {
                'test': 'test_data'
            }


    tp = TestProvider()
    with tp.override_locale('en') as provider:
        assert provider.get_current_locale() == 'en'


# Generated at 2022-06-13 23:55:32.839012
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method `override_locale` of class BaseDataProvider."""
    from mimesis.providers.generic import Generic

    provider = Generic()

    with provider.override_locale('ru') as fake:
        assert fake.get_current_locale() == 'ru'

    with provider.override_locale() as fake:
        assert fake.get_current_locale() == 'en'

    with provider.override_locale('fr') as fake:
        assert fake.get_current_locale() == 'fr'

# Generated at 2022-06-13 23:55:41.086315
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.science import Science

    try:
        with Science().override_locale('de') as sp:
            assert sp.locale == 'de'
            sp.reseed(1)
            assert sp.scientific_notation() == '2,71828183e+00'
            assert sp.scientific_notation() == '-1,41421356e+00'
            assert sp.scientific_notation() == '-2,4494898e-16'
    except Exception:
        assert 1 == 2

# Generated at 2022-06-13 23:55:46.261522
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Text
    from mimesis.enums import Gender, Locale
    provider = Text(Locale.EN, 'seed')
    with provider.override_locale(locale=Locale.RU):
        assert provider.get_current_locale() == Locale.RU
    assert provider.get_current_locale() == Locale.EN

# Generated at 2022-06-13 23:56:12.360024
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        """Test Provider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

    provider = TestProvider(locale=locales.EN)
    locale_ru = locales.RU

    with provider.override_locale(locale=locale_ru):
        assert len(provider._data) == len(TestProvider(locale=locale_ru)._data)

# Generated at 2022-06-13 23:56:20.600592
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    def test_function():
        return 'Привет, мир!'

    provider = BaseDataProvider(locale='ru')
    assert provider.get_current_locale() == 'ru'

    with provider.override_locale('en-us'):
        assert provider.get_current_locale() == 'en-us'
        assert test_function() == 'Привет, мир!'

    assert provider.get_current_locale() == 'ru'
    assert test_function() == 'Привет, мир!'

# Generated at 2022-06-13 23:56:25.367889
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Region
    from mimesis.enums import Locale
    from mimesis.typing import JSON
    with Region('ru').override_locale(Locale.EN) as region:
        assert isinstance(region, Region)
        assert region.locale == Locale.EN
        assert isinstance(region.data, JSON)

# Generated at 2022-06-13 23:56:35.330570
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person
    from mimesis.providers.text import Text
    from mimesis.providers.internet import Internet
    from mimesis.providers.identifier import Identifier
    from mimesis.providers.file import File
    from mimesis.providers.code import Code

    providers: Dict[str, BaseProvider] = {
        'address': Address(),
        'person': Person(),
        'text': Text(),
        'internet': Internet(),
        'identifier': Identifier(),
        'file': File(),
        'code': Code(),
    }

    with providers['address'].override_locale('en') as en:
        assert en.get_current_locale() == 'en'

    assert providers

# Generated at 2022-06-13 23:56:41.009885
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale='en-US'):
            super().__init__(locale=locale)
            self._datafile = 'test_provider.json'

        @classmethod
        def get_json(cls):
            return {
                "test": {
                    "ru": ["тест"],
                    "en": ["test"],
                    "fr": ["test"],
                }
            }

    provider = TestProvider(locale='en-US')
    with provider.override_locale(locale='ru-RU') as prov:
        assert prov.get_current_locale() == 'ru-RU'

# Generated at 2022-06-13 23:56:52.357671
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyDataProvider(BaseDataProvider):
        def get_numerus(self) -> str:
            return self.random.choice(['a', 'b'])

    p = MyDataProvider()
    with p.override_locale('en'):
        assert p.get_numerus() in ['a', 'b']
    with p.override_locale('ru'):
        assert p.get_numerus() in ['a', 'b']
    with p.override_locale('en'):
        assert p.get_numerus() in ['a', 'b']


# Generated at 2022-06-13 23:56:59.620837
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Pseudo
    p = Pseudo()
    locale = locales.EN
    with p.override_locale(locale):
        assert p.get_current_locale() == locale
    assert p.get_current_locale() == p.locale == locales.PSEUDO
    try:
        with p.override_locale(locale):
            pass
    except ValueError:
        pass

# Generated at 2022-06-13 23:57:05.640220
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    p = BaseDataProvider()
    with p.override_locale():
        assert p.locale == locales.EN
    # test to pass not correct type of value "locale"
    with p.override_locale(locale='ru'):
        assert p.locale == 'ru'
    # test to pass not correct value of locale
    with p.override_locale(locale='28'):
        assert p.locale == '28'


# Generated at 2022-06-13 23:57:14.849440
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Sun
    from mimesis.enums import DayOfWeek as Day

    locale = 'ru' # is day of week as sun.get_day_of_week(locale=locale)
    provider = Sun()
    with provider.override_locale(locale) as new_provider:
        day = new_provider.get_day_of_week()
        assert day == Day.WEDNESDAY.value # en == Day.WEDNESDAY
    assert day != Day.WEDNESDAY.value # ru != Day.WEDNESDAY

# Generated at 2022-06-13 23:57:24.251414
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # We never use a method for testing in a real project because a unit test
    # should not depend on other methods.
    # But in our case our method pulls data from disk.
    # If we don't use the method _pull in unit test then we will check
    # if the code is correctly written, but we will not correctly check the
    # work of the method itself.
    # That's why we use the method get_current_locale for unit testing.
    # get_current_locale uses method _pull.
    class FirstFileProvider(BaseDataProvider):
        _datafile = 'first.json'

    provider = FirstFileProvider(locales.RU)
    assert provider.get_current_locale() == locales.RU

    with provider.override_locale(locales.EN):
        assert provider.get_current_

# Generated at 2022-06-13 23:58:09.948456
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    try:
        with BaseDataProvider().override_locale():
            raise AssertionError('Not raise AttributeError')
    except AttributeError:
        pass

    class DataProvider(BaseDataProvider):
        def __init__(self, locale: str = None, seed: Seed = None):
            super().__init__(locale=locale, seed=seed)

    locale_list = ['en', 'ru', 'es', 'ru_RU', 'zh', 'zh_CN']
    for loc in locale_list:
        with DataProvider(loc).override_locale() as dp:
            assert dp.locale == loc

# Generated at 2022-06-13 23:58:13.902804
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis
    cl = mimesis.Code()
    assert hasattr(cl, '_override_locale')
    

# Generated at 2022-06-13 23:58:22.350980
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.providers.locales import FR
    from mimesis.providers.person import Person
    from mimesis.providers.science import Science

    def get_provider(pro: BaseDataProvider, locale: str = locales.DEFAULT_LOCALE) -> BaseDataProvider:
        with pro.override_locale(locale):
            return pro

    address = Address()
    science = Science()

    person = Person()
    assert person.get_current_locale() == person.locale == locales.DEFAULT_LOCALE
    person = get_provider(person, FR)
    assert person.get_current_locale() == person.locale == FR.lower()


# Generated at 2022-06-13 23:58:31.348350
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    from mimesis.data import Address, Address as AddressRU

    locale = locales.EN
    address = Address(locale)

    with address.override_locale(locales.RU) as provider:
        assert isinstance(provider, BaseDataProvider)
        assert provider.locale == locales.RU
        assert isinstance(provider, AddressRU)

    assert address.locale == locale

    with pytest.raises(ValueError):
        with address.override_locale():
            pass

# Generated at 2022-06-13 23:58:36.465664
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.en import American
    from mimesis.builtins.ru import Russian

    provider_ru = Russian()
    with provider_ru.override_locale(locales.EN) as provider_en:
        assert isinstance(provider_en, American)

    provider_en = American()
    with provider_en.override_locale(locales.RU) as provider_ru:
        assert isinstance(provider_ru, Russian)

# Generated at 2022-06-13 23:58:43.085541
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
        def get_name(self) -> str:
            return 'Name'

    f_p = FakeProvider()
    f_p.override_locale(locale='ru').get_name()
    assert f_p.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:58:50.860090
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Internet
    from mimesis.providers.geography import Geography
    from mimesis.providers.misc import Misc

    g = Geography()
    m = Misc()
    i = Internet()
    print(i.email())

    with g.override_locale('ru') as russian_geo:
        print(russian_geo.country())
        print(russian_geo.address.city())
        print(g.country())

    print(g.country())
    print(i.email())

# Generated at 2022-06-13 23:59:03.287400
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender

    # Test with not locale-dependent provider
    provider = BaseProvider()
    with provider.override_locale(locales.EN):
        assert provider.locale == locales.DEFAULT_LOCALE

    # Test with locale-dependent provider
    provider = BaseDataProvider(locales.RU)
    with provider.override_locale(locales.EN):
        assert provider.locale == locales.EN

        person = provider.person.full_name(gender=Gender.MALE)

        assert person in ('John Clarke', 'John Watson', 'John Terry',
                          'John Taylor', 'John Rodrigues')

    assert provider.locale == locales.RU



# Generated at 2022-06-13 23:59:06.698228
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        pass

    provider = Provider()
    with provider.override_locale(locale=locales.EN):
        assert provider.locale == locales.EN

    assert provider.locale == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:59:18.331481
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class _TestProvider(_TestProvider):
        def __init__(self, seed=None):
            self.seed = seed
            self.random = random
            if seed is not None:
                self.reseed(seed)
            self.locale = 'ru_RU'

        def get_current_locale(self) -> str:
            return self.locale

    tp = _TestProvider()
    with tp.override_locale('ru_RU') as tp:
        assert tp.get_current_locale() == 'ru_RU'

    with tp.override_locale('en_US') as tp:
        assert tp.get_current_locale() == 'en_US'

    assert tp.get_current_locale() == 'ru_RU'
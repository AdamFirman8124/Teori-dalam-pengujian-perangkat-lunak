

# Generated at 2022-06-13 23:50:42.947636
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.internet import Internet
    p1 = Internet(locale='ru')
    p2 = Internet(locale='ru')
    with p1.override_locale('en') as provider:
        assert p1.get_current_locale() == 'en'
        assert provider.get_current_locale() == 'en'
        assert p2.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:50:55.375940
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Business
    from mimesis.providers import Person
    from mimesis.enums import Gender
    from mimesis.providers.address import Address

    address = Address(locale='ru')
    business = Business(locale='ru')
    person = Person(locale='ru')

    with business.override_locale('en') as b_data:
        assert b_data.locale == 'en'
        assert person.locale == 'ru'
        assert address.locale == 'ru'
        assert business.locale == 'en'
        assert (business.company_name() ==
                'Web and Mobile Media, Inc.')
        assert (business.company_name(locale='ru') ==
                'Рога и копыта')



# Generated at 2022-06-13 23:50:56.085319
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:51:04.724298
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class TestDataProvider(BaseDataProvider):
        """Test class which raises ValueError when locale overridden."""

        def __init__(self, locale: str, seed: Seed = None) -> None:
            """Initialise TestDataProvider with locale."""
            super().__init__(locale, seed)
            self._data['test_key'] = self.random.randint(10)

        def test_method(self) -> int:
            """Get random int."""
            return self._data['test_key']

    test_locales = ('en', 'ru', 'kk')

    test_provider = TestDataProvider(test_locales[0])

    for test_locale in test_locales:
        with test_provider.override_locale(test_locale) as locale_provider:
            assert locale

# Generated at 2022-06-13 23:51:11.426006
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        pass
    tdp = TestDataProvider()
    with tdp.override_locale('ru'):
        assert tdp.locale == 'ru'


# Generated at 2022-06-13 23:51:21.370101
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Currency, Locale
    from mimesis.enums import CurrencyCode, LocaleCode

    mimesis_locale = Locale()
    mimesis_currency = Currency()
    with mimesis_locale.override_locale(str(LocaleCode.RU)) as new_locale:
        assert new_locale.get_current_locale() != mimesis_locale.get_current_locale() == str(LocaleCode.EN)
    with mimesis_currency.override_locale(str(LocaleCode.RU)) as new_currency:
        assert new_currency.get_current_locale() != mimesis_currency.get_current_locale() == str(LocaleCode.EN)

# Generated at 2022-06-13 23:51:29.937042
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestBaseDataProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE):
            self._datafile = 'test.json'
            super().__init__(locale)

        def override_locale(self, locale: str = locales.DEFAULT_LOCALE):
            self._override_locale(locale)

        def get_foo(self):
            return self._data['foo']

    provider = TestBaseDataProvider()
    assert provider.get_foo() == 'bar'
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

    with provider.override_locale(locales.EN):
        assert provider.get_foo() == 'bar'
        assert provider.get_current_locale() == locales.EN

   

# Generated at 2022-06-13 23:51:35.839601
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class _A(BaseDataProvider):
        pass

    with _A.override_locale(locales.AR) as a:
        assert a.get_current_locale() == locales.AR

    assert _A().get_current_locale() == locales.EN

# Generated at 2022-06-13 23:51:39.283574
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """
    """
    pass

# Generated at 2022-06-13 23:51:48.360557
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.person import Person
    from mimesis.providers.internet import Internet
    from mimesis.providers.misc import Misc
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.text import Text
    from mimesis.providers.currency import Currency
    from mimesis.providers.geography import Geography
    from mimesis.providers.identifiers import Identifiers

    rnd = Random()

    def get_data(obj, locale) -> Dict[str, str]:
        data = {}

# Generated at 2022-06-13 23:52:07.522545
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale=locales.EN):
            super().__init__(locale)

        def __repr__(self):
            return self.locale

    t = TestProvider()
    with t.override_locale(locales.EN):
        assert t.locale == locales.EN
    with t.override_locale(locales.RU):
        assert t.locale == locales.RU
    with t.override_locale(locales.DE):
        assert t.locale == locales.DE


# Generated at 2022-06-13 23:52:19.203767
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    print(1)
    from mimesis import Person
    p = Person('ko')
    print(p.full_name())
    with p.override_locale('zh') as new:
        # print(new.full_name())
        print(p.full_name())
        print(p.full_name())
    print(p.full_name())
    from mimesis import Person
    p = Person('ko')
    print(p.full_name())
    with p.override_locale('zh') as new:
        # print(new.full_name())
        print(p.full_name())
        print(p.full_name())
    print(p.full_name())

# Generated at 2022-06-13 23:52:29.008819
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('en')
    fullname = person.full_name(gender=Gender.MALE)
    assert fullname in ('Jim Carroll', "Kamran Hyder")  # noqa: WPS421, WPS237

    with person.override_locale('ru'):
        fullname = person.full_name(gender=Gender.MALE)
        assert fullname in ('Трофим Цуканов', 'Игорь Кушнаренков')  # noqa: WPS421, WPS237

    fullname = person.full_name(gender=Gender.MALE)

# Generated at 2022-06-13 23:52:34.977136
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale."""
    from mimesis.builtins import Address
    from mimesis.data import STATES_EN
    addr = Address()
    state_en = addr.state()

    addr.override_locale(locales.RU)
    assert addr.state() == STATES_EN['ru'][0]

    addr.override_locale(locales.EN)
    assert addr.state() == state_en

# Generated at 2022-06-13 23:52:45.709342
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import unittest.mock as mock

    class A(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            self.locale = locale
            self.seed = seed
            self.random = random
            self.data = {}
            self.datafile = ''

        def _setup_locale(self, locale: str = locales.DEFAULT_LOCALE) -> None:
            self.locale = locale

        def get_current_locale(self):
            return self.locale

        def _pull(self) -> None:
            self.data = {
                self.get_current_locale(): self.get_current_locale(),
            }

    # Mocking _pull to avoid loading data

# Generated at 2022-06-13 23:52:54.952988
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for BaseDataProvider._override_locale."""
    from mimesis.builtins import Person
    from mimesis.enums import Gender

    p = Person(locale=locales.EN)
    assert 'max' == p.full_name(gender=Gender.MALE)
    with p.override_locale(locales.RU) as person:
        assert 'Максим' == person.full_name(gender=Gender.MALE)
    assert 'max' == p.full_name(gender=Gender.MALE)

# Generated at 2022-06-13 23:53:02.716589
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    print('Testing method «override_locale» of class «BaseDataProvider»')
    bdp = BaseDataProvider()

    # Reset locale
    bdp._override_locale(locales.DEFAULT_LOCALE)

    # Change locale from «en» to «ru», then back to «en»
    with bdp.override_locale(locales.RU) as locale_provider:
        assert locale_provider.get_current_locale() == locales.RU

    assert bdp.get_current_locale() == locales.DEFAULT_LOCALE
    print('Test passed')

# Generated at 2022-06-13 23:53:08.135485
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis.builtins
    provider = mimesis.builtins.General()
    with provider.override_locale(locales.EN) as p:
        assert p.get_current_locale() == locales.EN
        assert provider.get_current_locale() == locales.RU
    assert provider.get_current_locale() == locales.RU

# Generated at 2022-06-13 23:53:22.065303
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import (
        Address,
        Business,
        Code,
        Crypto,
        FileSystem,
        Geography,
        Lorem,
        Person,
    )

    class Test(BaseDataProvider):

        def __init__(self, seed: Seed = None, locale: str = locales.EN):
            super().__init__(seed=seed, locale=locale)

        def get_test(self) -> str:
            return self.get_current_locale()

    def test_default_locale(provider) -> None:
        """Test default locale."""
        assert provider.get_current_locale() == locales.EN

    def test_override_locale(provider) -> None:
        """Test locale which was overridden from overridden_locale."""
       

# Generated at 2022-06-13 23:53:25.886829
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person

    person = Person()

    with person.override_locale('ru'):
        assert person.full_name() == 'Константин Прибылов'

    assert person.full_name() == 'Christopher Butler'


# Generated at 2022-06-13 23:53:51.825507
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider:
        '''Test provider.'''

        def override_locale(self, locale):
            yield self

    provider = Provider()
    with provider.override_locale('ru'):
        assert True
    try:
        provider.override_locale('ru')
    except:
        assert False

    provider_without_override = Provider()
    try:
        with provider_without_override.override_locale('ru'):
            assert True
    except:
        assert True
    else:
        assert False

# Generated at 2022-06-13 23:53:55.040489
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Datetime
    datetime = Datetime()

    with datetime.override_locale('nl_NL'):
        datetime.date()

    with datetime.override_locale('ru_RU'):
        datetime.date()

# Generated at 2022-06-13 23:54:06.644761
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Testing method ``BaseDataProvider.override_locale``."""
    with pytest.raises(AttributeError,
                       match='has not locale dependent'):
        with BaseProvider().override_locale() as p:
            assert p is not None

    with pytest.raises(ValueError, match='is not supported'):
        with BaseDataProvider().override_locale('xx') as p:
            assert p is not None

    with BaseDataProvider().override_locale('uk') as p:
        assert p is not None
        assert p.locale == 'uk'

    assert p.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:54:14.167717
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class BaseDataProviderMock(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None):
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test.json'
            self.test_method = lambda: 'test'

    provider = BaseDataProviderMock()

    # Solution 1
    with provider.override_locale('ru') as provider_ru:
        provider_ru.get_current_locale()

# Generated at 2022-06-13 23:54:24.053089
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale."""
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    p = Person(locale='en')
    r = p.full_name(gender=None)
    assert r not in p.get_full_name(gender=Gender.MALE), r
    assert r not in p.get_full_name(gender=Gender.FEMALE), r
    assert p.get_full_name(gender=Gender.MALE) not in r, r
    assert p.get_full_name(gender=Gender.FEMALE) not in r, r

    p = Person(locale='ru')
    r = p.full_name(gender=None)
    assert r not in p.get_full_name(gender=Gender.MALE), r

# Generated at 2022-06-13 23:54:32.854762
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.person import Person
    person = Person()
    try:
        for _ in range(5):
            with person.override_locale('de'):
                assert person.get_current_locale() == 'de'
                assert person.get_full_name() in _get_de_real_full_names()
            assert person.get_current_locale() == 'en'
    except ValueError:
        print("Overriding locale is not supported. "
              "Unit test has been passed.")
        pass


# Generated at 2022-06-13 23:54:44.687958
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    class TestDataProvider(BaseDataProvider):
        """Test data provider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes for test data providers."""
            super().__init__(locale, seed)
            self._datafile = 'test.json'

        def _get_data(self) -> Dict[str, Any]:
            self._pull()
            return self._data

    provider = TestDataProvider(locale=locales.EN)
    en_locale = provider.get_current_locale()
    assert en_locale == 'en'

    with provider.override_locale(locales.RU):
        ru_loc

# Generated at 2022-06-13 23:54:51.665140
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test function override_locale of class BaseDataProvider.

    :return: None.
    """
    class TestBaseDataProvider(BaseDataProvider):
        """This is a base class for all data providers."""

        def test_func(self) -> Dict[str, str]:
            """Test function for demo.

            :return: Dictionary with locale of function.
            """
            return {'locale': self.get_current_locale()}

        def __str__(self) -> str:
            """Human-readable representation of locale."""
            return '{} <{}>'.format(self.__class__.__name__, self.locale)

    test = TestBaseDataProvider()
    assert test.test_func() == {'locale': 'en'}, 'locale is en'


# Generated at 2022-06-13 23:54:57.326782
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Create instance __main__.BaseDataProvider (seed = None)
    bdp = BaseDataProvider()
    # Check if exception is not raised in context manager
    with bdp.override_locale():
        pass
    # Check if exception is raised with message:
    # «{} has not locale dependent».format(self.__class__.__name__)
    try:
        with bdp.override_locale():
            pass
    except ValueError as ex:
        assert str(ex) == 'BaseDataProvider has not locale dependent'
    else:
        assert False

# Generated at 2022-06-13 23:55:04.099151
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

    p = TestProvider()
    with p.override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'
    assert p.get_current_locale() == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:55:44.484361
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass


# Generated at 2022-06-13 23:55:49.151360
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Testing method override_locale of class BaseDataProvider."""
    class TestClass(BaseDataProvider):
        locale = 'uk'

        def ukrainian_test(self):
            return self.locale

    t = TestClass()
    assert t.locale != 'ru'
    assert t.ukrainian_test() == 'uk'

    with t.override_locale('ru'):
        assert t.locale != 'ru'

    assert t.ukrainian_test() == 'uk'

# Generated at 2022-06-13 23:55:59.548962
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyDataProvider(BaseDataProvider):
        pass

    def _get_locale_test(provider):
        return provider.get_current_locale()

    provider_instance = MyDataProvider(locale='pl')
    locale = _get_locale_test(provider_instance)
    assert locale == 'pl'
    with provider_instance.override_locale(locale='en'):
        locale = _get_locale_test(provider_instance)
        assert locale == 'en'
    locale = _get_locale_test(provider_instance)
    assert locale == 'pl'
    with provider_instance.override_locale(locale='en'):
        locale = _get_locale_test(provider_instance)
        assert locale == 'en'
    locale = _get_

# Generated at 2022-06-13 23:56:06.582358
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Invoice
    from mimesis.enums import Gender
    from mimesis.exceptions import UnitNotInEnumError

    random.seed(1)
    builtin = Invoice()

    assert builtin.gender(Gender.FEMALE).gender == 'Женский'

    with builtin.override_locale('ru'):
        assert builtin.gender(Gender.FEMALE).gender == 'Женский'

    with builtin.override_locale('en'):
        assert builtin.gend

# Generated at 2022-06-13 23:56:12.747256
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""

    class Prov(BaseDataProvider):
        """A dummy class."""

        def __init__(self):
            """Initialize class."""
            super().__init__()

    prov = Prov()
    with prov.override_locale('en') as p:
        assert p.get_current_locale() == 'en'

# Generated at 2022-06-13 23:56:17.917296
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis import Address, Locale
    provider = Address(locale=Locale('en'))
    with provider.override_locale('ru'):
        assert provider.get_current_locale() == 'ru'
    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:56:22.806212
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    class TestClass(BaseDataProvider):
        'Test Class'

    obj = TestClass()
    with obj.override_locale():
        assert obj.locale == 'en'

# Generated at 2022-06-13 23:56:27.804933
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import All
    from mimesis.builtins import en
    
    from_provider = All().get_seed()
    from_context = None
    with All().override_locale(locale=en) as all_from_context:
        from_context = all_from_context.get_seed()
        assert en == all_from_context.get_current_locale()
    
    assert from_provider != from_context

# Generated at 2022-06-13 23:56:34.834524
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    class TestBaseDataProvider(BaseDataProvider):
        """Test class."""

        class Meta:
            """Class Meta."""

            locales = ['en', 'ru']

    bdp = TestBaseDataProvider()
    try:
        with bdp.override_locale('ru'):
            bdp.get_current_locale()
    except ValueError:
        raise AssertionError('This method not working.')

# Generated at 2022-06-13 23:56:40.832100
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.geography import Geography
    from mimesis.providers.datetime import Datetime

    geography = Geography()
    datetime = Datetime()

    with geography.override_locale() as g:
        c1 = geography.currency()
        nc1 = g.currency()
        assert c1 != nc1
        c2 = geography.currency()
        assert c1 == c2

    with datetime.override_locale() as dt:
        wd1 = datetime.weekday()
        nwd1 = dt.weekday()
        assert wd1 != nwd1
        wd2 = datetime.weekday()
        assert wd1 == wd2

# Generated at 2022-06-13 23:58:14.106426
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.enums import Gender, Titles

    class TestBaseDataProvider(BaseDataProvider):
        def __init__(self, locale='en', seed=None):
            datafile = 'builtin/test.json'
            super().__init__(locale=locale, seed=seed, datafile=datafile)

        def test(self, gender=None):
            return self._validate_enum(gender, Gender)

    p1 = TestBaseDataProvider()
    p1.test() # Gender.MALE

    p2 = TestBaseDataProvider(locale='ru')
    p2.test() # Gender.MALE

    with p1.override_locale(locale='ru'):
        p1.test() # Gender.FEMALE

    p1.test() # Gender.FEM

# Generated at 2022-06-13 23:58:22.541313
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Foo(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)
            self._data = {}
            self._datafile = ''
            self.locale = locale
            pass

    locale_bt = locales.BaseLocale()
    locale_bt._pull()
    locale_bt.set_locale(locales.DEFAULT_LOCALE + '_test')
    with locale_bt.override_locale(locales.EN):
        assert locale_bt.locale == locales.EN
    with locale_bt.override_locale(locales.EN):
        assert locale_bt.locale == locales.EN

# Generated at 2022-06-13 23:58:30.273581
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class SimpleProvider(BaseDataProvider):
        def get_data(self, key: str) -> Any:
            return self._data.get(key)

    provider = SimpleProvider()

    with provider.override_locale('ru') as russian_provider:
        assert russian_provider.get_data('providers.simple_provider.1') == 'Комманда 1'

    assert provider.get_data('providers.simple_provider.1') == 'Command 1'

# Generated at 2022-06-13 23:58:37.786409
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDp(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None):
            # Suppresses the warning:
            # "C:\Users\User\.virtualenvs\mimesis-JRhcV7Iu\lib\site-packages\
            # mimesis\helpers.py:68:
            # PendingDeprecationWarning: The default value for 'allow_nan'
            # will change to False in version 1.0.
            # It is recommended to pass an explicit value
            # to suppress this warning.
            # allow_nan=False (if omitted),
            # "
            super().__init__(locale, seed=seed)

        def ove(self, s: str) -> str:
            return 'ove' + s


# Generated at 2022-06-13 23:58:45.518426
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, seed: Seed = None)-> None:
            super().__init__(seed=seed)
            self._datafile = 'test_data.json'
            self._pull()
        def one(self) -> str:
            return 'one'

    test_provider = TestProvider()

    # Test the case when locale is supported
    assert test_provider.one() == 'one'
    with test_provider.override_locale(locale='ru') as provider:
        assert provider.one() == 'один'

    # Test the case when locale is unsupported
    with test_provider.override_locale(locale='xxx') as provider:
        assert provider.one() == 'one'

    # Test the case when locale is empty


# Generated at 2022-06-13 23:58:52.005496
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None):
            super().__init__(locale=locale,seed=seed)
        def my_data(self):
            return self._data
    p = FakeProvider(locale='en')
    p._pull(datafile='test.json')
    with p.override_locale('ru'):
        assert p.my_data()['test_key'] == 'test_value'

# Generated at 2022-06-13 23:59:04.992871
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    _BaseProvider = BaseProvider()
    _BaseProvider._pull = BaseDataProvider._pull
    _BaseProvider._override_locale = BaseDataProvider._override_locale
    _BaseProvider._update_dict = BaseDataProvider._update_dict
    _BaseProvider.get_current_locale = BaseDataProvider.get_current_locale

    # _BaseProvider.locale = 'ru'
    # with _BaseProvider.override_locale(locale='en') as provider:
    #     print(provider.get_current_locale())
    #
    # print(_BaseProvider.get_current_locale())

    _BaseProvider.locale = locales.EN

# Generated at 2022-06-13 23:59:11.602040
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider.

    :return: True if test was successful, False otherwise.
    :rtype: bool
    """
    from mimesis.builtins import Person
    person_en = Person()
    person_ru = Person(locale='ru')

    assert isinstance(person_en.name, str)
    assert isinstance(person_ru.name, str)

    with person_en.override_locale('ru') as p:
        assert p.name == person_ru.name

    try:
        with person_ru.override_locale('ru'):
            assert False
    except ValueError as e:
        assert str(e) == '«Person» has not locale dependent'

    return True

# Generated at 2022-06-13 23:59:20.328830
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Provider
    provider = Provider('en')

# Generated at 2022-06-13 23:59:26.324930
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    def check_locale(locale):
        """Check current locale (inside the context)."""
        assert num_provider.get_current_locale() == locale

    num_provider = BaseDataProvider(locale='en')
    with num_provider.override_locale(locale='ru'):
        check_locale('ru')

    check_locale('en')
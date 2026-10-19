

# Generated at 2022-06-13 23:50:41.350661
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    class P(BaseDataProvider):
        pass

    provider = P()

    with provider.override_locale(locales.EN) as p:
        assert p.get_current_locale() == locales.EN
        assert p.locale == locales.EN

    assert provider.locale == locales.DEFAULT_LOCALE
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:50:51.177788
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def _pull(self, datafile):
            self._data = {
                'test': 1,
                'test_two': 2,
                'test_three': 3,
            }

        def test(self):
            return self._data['test']

        def test_two(self):
            return self._data['test_two']

        def test_three(self):
            return self._data['test_three']

    test_one = TestProvider('en')
    test_two = TestProvider('uk')
    assert test_one.test() == 1
    assert test_two.test() == 2

    with test_one.override_locale('uk'):
        assert test_one.test() == 2


# Generated at 2022-06-13 23:51:01.342427
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Override locale using BaseDataProvider."""
    from mimesis.builtins.datetime import Datetime
    from mimesis.enums import Gender
    from mimesis.providers.person.en import Person

    locale = locales.RU
    # Define a context
    with Person().override_locale(locale) as provider:
        assert provider.get_current_locale() == locale
        assert provider.full_name() != provider.full_name(gender=Gender.MALE)

    assert Person().get_current_locale() != locale

    # Define a context
    with Datetime().override_locale(locale) as provider:
        assert provider.time() != provider.time()

# Generated at 2022-06-13 23:51:11.146781
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    class TestClass(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None):
            super().__init__(locale=locale, seed=seed)
            self._data = {
                'ru': {},
                'en': {},
            }
            self._datafile = 'test.json'
            self._pull()
    test = TestClass()
    with test.override_locale('ru'):
        assert test.locale == 'ru'
    assert test.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:16.432166
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Test if method override_locale returns Provider with the new locale
    from mimesis.builtins import Code

    assert Code().get_current_locale() == 'en'
    with Code().override_locale('ru') as provider:
        assert Code().get_current_locale() == 'ru'
    assert Code().get_current_locale() == 'en'


# Generated at 2022-06-13 23:51:20.406639
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    base = BaseDataProvider()
    with base.override_locale('es'):
        assert base.locale == 'es'
    assert base.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:29.255666
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test class BaseDataProvider."""
    class TestDataProvider(BaseDataProvider):
        """Data provider for tests."""

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

        def get_data(self) -> JSON:
            """Return data of provider."""
            return self._data


# Generated at 2022-06-13 23:51:40.930799
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DemoProvider(BaseDataProvider):
        """This is a class for demostration of method override_locale."""

        class Meta:
            name = 'demo_provider'

        def _pull(self, datafile: str = '') -> None:
            self._data = {'test': {'test': 'Hello, world!'}}

    provider = DemoProvider()
    with provider.override_locale('ru') as override_provider:
        assert override_provider.locale == 'ru'
        assert override_provider.get_current_locale() == 'ru'

    assert provider.locale == locales.DEFAULT_LOCALE
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:45.394904
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

    with provider.override_locale(locales.EN):
        assert provider.get_current_locale() == locales.EN

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:51:48.556469
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Sports

    with Sports().override_locale() as sports:
        assert sports.get_current_locale() == Sports.DEFAULT_LOCALE

        sports.seed(5)
        assert sports.team_member() == 'Fernando Medina'

# Generated at 2022-06-13 23:52:02.862454
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale='en')
    with provider.override_locale(locale='en'):
        assert provider.locale == 'en'

# Generated at 2022-06-13 23:52:13.632157
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class OverrideLocaleProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE):
            super().__init__(locale=locale)

        def test_function(self) -> str:
            return self.locale

    p = OverrideLocaleProvider()

    # Test for method override_locale output
    assert p.test_function() == locales.DEFAULT_LOCALE

    with p.override_locale(locales.EN) as new_p:
        assert new_p.locale == locales.EN

    # Test for method override_locale output
    assert p.test_function() == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:52:26.750478
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale.

    A full test is performed in the class :class:`mimesis.Person` and below
    is shown only a small part of it.
    """
    from mimesis import Person
    ru = Person(locale='ru')
    en = Person(locale='en')

    russian_surname = ru.surname()
    english_surname = en.surname()
    assert russian_surname != english_surname

    current_locale = ru.get_current_locale()
    assert current_locale == 'ru'

    with ru.override_locale('en') as new_ru:
        english_surname = new_ru.surname()
        assert english_surname != russian_surname
        current_

# Generated at 2022-06-13 23:52:34.109751
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test override_locale() method."""
    from mimesis.builtins import Person
    p1 = Person()
    with p1.override_locale('ru') as p2:
        assert isinstance(p2, Person)
        assert p2.locale == 'ru'
        assert p1.locale == 'en'
        assert p2.full_name() != p1.full_name()

# Generated at 2022-06-13 23:52:45.587283
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code
    from mimesis.enums import CodeType
    from mimesis.locales import IW, RU, UK

    code = Code()
    with code.override_locale(locale=RU) as provider:
        assert isinstance(provider, Code)
        assert provider.Locale.CODE in ('ru', 'uk')
        assert provider.get_current_locale() == RU
        assert isinstance(code.get_current_locale(), str)
        assert code.get_current_locale() == RU

    with provider.override_locale(locale=IW) as provider:
        assert isinstance(provider, Code)
        assert provider.get_current_locale() == IW

# Generated at 2022-06-13 23:52:55.775456
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyDataProvider(BaseDataProvider):
        def __init__(self, locale='en'):
            super().__init__(self, locale)
            self.datafile = 'example.json'

        def test(self):
            return self.provider_method()
    provider = MyDataProvider()

    with provider.override_locale('ru') as provider_ru:
        assert provider_ru.locale == 'ru'
        assert provider.provider_method() == 'en'
        assert provider_ru.provider_method() == 'ru'

    assert provider.locale == 'en'
    assert provider.provider_method() == 'en'



# Generated at 2022-06-13 23:53:04.634003
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for BaseDataProvider._override_locale method."""
    provider = BaseDataProvider()
    locale = locales.RU
    with provider.override_locale(locale) as p:
        assert p.get_current_locale() == locale
    assert provider.get_current_locale() == locale
    locale = locales.UK
    with provider.override_locale(locale) as p:
        assert p.get_current_locale() == locale
    assert provider.get_current_locale() == locale

# Generated at 2022-06-13 23:53:17.337606
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    locale = locales.EN
    data_provider = BaseDataProvider(locale, seed=None)

    def f1(data_provider):
        with data_provider.override_locale(locale) as data_provider:
            with data_provider.override_locale(locale) as data_provider:
                pass
            assert str(data_provider) == "BaseDataProvider <en>"

        assert str(data_provider) == "BaseDataProvider <en>"

    def f2(data_provider):
        with data_provider.override_locale(locale) as data_provider:
            pass
        assert str(data_provider) == "BaseDataProvider <en>"


# Generated at 2022-06-13 23:53:28.189361
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        """Test provider."""

        def __init__(self, locale, seed) -> None:
            super().__init__(locale=locale, seed=seed)
            self.DATA = (1, 2, 3)

    def test_override_locale(provider, locale):
        with provider.override_locale(locale) as overridden:
            assert overridden.get_current_locale() == locale
            assert overridden.choose() in provider.DATA

    provider = TestProvider(locales.EN, seed=42)
    test_override_locale(provider, locales.RU)
    test_override_locale(provider, locales.ES)
    test_override_locale(provider, locales.IT)

#

# Generated at 2022-06-13 23:53:30.837759
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert True

# Generated at 2022-06-13 23:53:51.416761
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FooProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None):
            super().__init__(locale, seed)
        def do_work(self):
            return 'foo'

    f1 = FooProvider('en')
    f2 = FooProvider('ru')
    assert f1.get_current_locale() == 'en'
    assert f2.get_current_locale() == 'ru'
    with f1.override_locale('ru') as f:
        assert f.get_current_locale() == 'ru'
    assert f1.get_current_locale() == 'en'
    with f2.override_locale('en') as f:
        assert f.get_current_locale() == 'en'


# Generated at 2022-06-13 23:53:54.983331
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    BaseDataProvider._pull = lambda self: 'data'
    BaseDataProvider._datafile = 'file.json'
    provider = BaseDataProvider()
    try:
        with provider.override_locale('__test__'):
            assert provider._datafile == 'file.json'
            assert provider._pull() == 'data'
    except Exception as err:
        raise err

# Generated at 2022-06-13 23:53:56.471558
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:54:10.257397
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.enums import Gender, PersonTitle
    from mimesis.providers import Person

    def _get_data(provider: BaseDataProvider,
                  value: str,
                  ) -> Any:
        data = getattr(provider, '_data')
        return data.get(value)

    person = Person()
    assert _get_data(person, 'PersonTitle')['male'] == PersonTitle.MR.value

    with person.override_locale(locales.RU):
        assert _get_data(person, 'PersonTitle')['male'] == PersonTitle.MR.value

    with person.override_locale(locales.UK):
        assert _get_data(person, 'PersonTitle')['male'] == PersonTitle

# Generated at 2022-06-13 23:54:13.346955
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert BaseDataProvider().override_locale(locale='en') is not None
    assert BaseDataProvider().override_locale(locale='ru') is not None
    assert BaseDataProvider().override_locale(locale='ua') is not None

# Generated at 2022-06-13 23:54:27.040516
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = 'en'):
            super().__init__(locale=locale)
            self._datafile = 'test_data.json'
            self._pull()


    data = {
        'a': 'test',
        'b': ['test', 'test', 'test'],
        'c': {
            'test': {
                'test': 'test'
            }
        }
    }

    provider = TestProvider(data)
    with provider.override_locale(locale='ru') as provider:
        assert provider.a() == 'test'
        assert provider.b() == 'test'
        assert provider.c()['test'] == 'test'

# Generated at 2022-06-13 23:54:39.837446
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def __init__(self, seed: Seed, locale: str = locales.DEFAULT_LOCALE,
                     **kwargs) -> None:
            super().__init__(seed=seed, locale=locale, **kwargs)
            self.field = 'test'

    dp = TestDataProvider(seed=0)
    with dp.override_locale('en'):
        assert dp.get_current_locale() == 'en'
        assert dp.field == 'test'
    dp = TestDataProvider(seed=0, locale='en')
    with dp.override_locale('en'):
        assert dp.get_current_locale() == 'en'
        assert dp.field == 'test'

# Generated at 2022-06-13 23:54:52.448642
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataProvider(BaseDataProvider):
        def greeting(self):
            return 'Hello, world!'

    dp = TestDataProvider(locale='ru')
    assert dp.greeting() == 'Привет, мир!'
    assert dp.get_current_locale() == 'ru'

    with dp.override_locale('ru-ru') as dp:
        assert dp.greeting() == 'Привет, мир!'
        assert dp.get_current_locale() == 'ru-ru'
    assert dp.greeting() == 'Привет, мир!'
    assert dp.get_current_locale() == 'ru'


# Generated at 2022-06-13 23:54:56.259217
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''
    Test the context manager of BaseDataProvider.
    '''
    bdp = BaseDataProvider()
    # Acccepted
    with bdp.override_locale("en"):
        assert True
    # Not accepted
    with bdp.override_locale("en"):
        assert not False


# Generated at 2022-06-13 23:55:03.888115
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Personal(BaseDataProvider):
        def __init__(self, locale='en'):
            super().__init__(locale)

        def get_fullname(self):
            return self.name(gender='female')

    p = Personal()
    assert p.get_current_locale() == 'en'
    with p.override_locale('ru'):
        assert p.get_current_locale() == 'ru'
        assert p.get_fullname() == 'Мария'
    assert p.get_current_locale() == 'en'

# Generated at 2022-06-13 23:55:28.215614
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Arrange
    provider = BaseDataProvider()
    expected = 'BaseDataProvider <ru>'

    # Act
    with provider.override_locale('ru'):
        result = provider.__str__()

    # Assert
    assert result == expected

# Generated at 2022-06-13 23:55:36.974175
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    from mimesis.providers.datetime import Datetime
    datetime_es = Datetime(seed=42)
    datetime_en = Datetime(seed=42)
    with pytest.raises(ValueError):
        with datetime_es.override_locale():
            print('Get time')
    with datetime_es.override_locale(locale='es'):
        print('Get time')
    assert datetime_es.time() == '17:39:12'
    datetime_en.time()
    assert datetime_en.time() == ' 05:39:12 pm.'

# Generated at 2022-06-13 23:55:44.882094
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class P(BaseDataProvider):
        def __init__(self, locale,
                     seed=None):
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test.json'  # type: str
            self._pull()

        def get_data(self, datafile):
            return self._data[datafile]

    with P(locales.EN, seed=1) as p:
        assert p.get_current_locale() == locales.EN
        assert p.get_data('foo') == 'bar'

        with p.override_locale(locales.RU):
            assert p.get_current_locale() == locales.RU
            assert p.get_data('foo') == 'baz'

        assert p.get_current_locale

# Generated at 2022-06-13 23:55:51.905969
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the method BaseDataProvider._override_locale."""
    from mimesis.builtins import Language
    from mimesis.schema import Field, Schema

    language = Language('pt_BR')
    language._override_locale('es')

    schema = Schema(
        Field('name', template='{{person.full_name}}'),
        Field('address', template='{{person.address}}'),
    )

    person = schema.create(seed=42)
    assert person.get('name') == 'Carmen Rodriguez'
    assert person.get('address') == 'Calle 558 1098, Santa Cruz de Tenerife'

# Generated at 2022-06-13 23:56:00.632080
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import BaseSpecProvider, BuiltinSpecProvider
    import pytest

    spec = BaseSpecProvider()
    spec.seed = 987654321
    random.seed(spec.seed)
    spec_ru = BuiltinSpecProvider('ru')
    spec_en = BuiltinSpecProvider('en')
    tmp_locale = 'ru'
    values = list()
    values.append(spec_en.address.street_name())
    values.append(spec_en.address.street_name())
    values.append(spec_en.address.street_name())
    init_hash = hash(tuple(values))

    with spec.override_locale(tmp_locale):
        values[0] = spec.address.street_name()
        values[1] = spec.address.street_name

# Generated at 2022-06-13 23:56:07.772084
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDictLocaleProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

        def get_data(self) -> Dict[str, Any]:
            """Get the data from provider.

            :return: Data from provider.
            """
            return self._data

    data = {
        'Test': 'Test',
        'Hello': {locales.EN: 'Hello', locales.RU: 'Привет'},
        'Name': {locales.EN: 'Name', locales.RU: 'Имя'}
    }

    test_provider = TestDictLocaleProvider()
    test_

# Generated at 2022-06-13 23:56:08.433963
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:56:12.359164
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    with provider.override_locale('ru') as pr:
        assert str(pr) == 'BaseDataProvider <ru>'

    assert str(provider) == 'BaseDataProvider <en>'


# Generated at 2022-06-13 23:56:21.833956
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis import Person
    p1 = Person()
    p2 = Person()
    with p1.override_locale('en'):
        assert p1.get_current_locale() == 'en'
        assert p2.get_current_locale() == 'ru'
        assert p1.full_name(gender='male') == 'Travis Wade'
    assert p1.get_current_locale() == 'ru'
    with p2.override_locale('en'):
        assert p1.get_current_locale() == 'ru'
        assert p2.get_current_locale() == 'en'
        assert p1.full_name(gender='male') == 'Анатолий Егоров'
        assert p2.full_

# Generated at 2022-06-13 23:56:31.784825
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.data import (
        Address,
        Code,
        Science,
    )
    from mimesis.exceptions import (
        NonEnumerableError,
        UnsupportedLocale,
    )

    # Creating a provider and changing locale
    addr_1 = Address(locale='en')
    addr_1.override_locale('en')
    assert addr_1.get_current_locale() == 'en'

    with addr_1.override_locale() as addr_2:
        assert addr_2.get_current_locale() == 'en'

    # It is forbidden to override locale with invalid locale

# Generated at 2022-06-13 23:57:21.538409
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.datetime import Datetime

    dt = Datetime(locale='en')
    data = {}
    for i in range(1000):
        with dt.override_locale('ru'):
            day = dt.date(start=1990, end=2000)
        data[day.year] = day.day
    years = sorted(set(data.keys()))
    assert all(data[year] == 29 for year in years)

# Generated at 2022-06-13 23:57:31.294850
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins.person import Person

    person = Person()
    with person.override_locale(locales.JA) as provider:
        assert 'ようこそ' == provider.title()

    with person.override_locale(locales.RU) as provider:
        assert 'Как дела?' == provider.greeting()
#
# def test_BaseDataProvider_override_locale_without_locale():
#     """Test for method override_locale of class BaseDataProvider."""
#     from mimesis.builtins.science import Science
#
#     science = Science()
#     with pytest.raises(ValueError) as e:
#         with science.override_

# Generated at 2022-06-13 23:57:40.950137
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Linux
    linux = Linux()
    with linux.override_locale('en'):
        assert linux.locale == 'en'
    assert linux.locale != 'en'
    with linux.override_locale('en'):
        assert linux.locale == 'en'
        with linux.override_locale('zh-tw') as l:
            assert l.locale == 'zh-tw'
        assert linux.locale == 'en'
    assert linux.locale != 'zh-tw'
    assert linux.locale != 'en'

# Generated at 2022-06-13 23:57:47.562022
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def get_data(self):
            return self._pull()

    t = TestProvider(locale='en')
    assert t.get_current_locale() == 'en'
    with t.override_locale('ru'):
        t.get_data()
        assert t.get_current_locale() == 'ru'
    assert t.get_current_locale() == 'en'

    with t.override_locale('it'):
        t.get_data()
        assert t.get_current_locale() == 'it'
    assert t.get_current_locale() == 'en'

    t = TestProvider()
    assert t.get_current_locale() == 'en'

# Generated at 2022-06-13 23:57:53.294989
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, *,
                     locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

    provider = TestProvider(locale='en')
    with provider.override_locale('ru'):
        assert provider.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:58:01.944026
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DataProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
        def __enter__(self):
            return self
    data_provider = DataProvider(locale=locales.EN, seed=42)
    with data_provider.override_locale(locales.RU):
        assert data_provider.locale == locales.RU


# Generated at 2022-06-13 23:58:11.481261
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.numbers import Numbers
    n = Numbers()

    n1 = n.override_locale()
    assert n.locale == locales.EN
    assert n1.locale == locales.EN
    assert n1.random == n.random

    n2 = n.override_locale(locales.RU)
    assert n.locale == locales.EN
    assert n2.locale == locales.RU
    assert n2.random == n.random

    n3 = n.override_locale(locales.EN)
    assert n.locale == locales.EN
    assert n3.locale == locales.EN
    assert n3.random == n.random

# Generated at 2022-06-13 23:58:17.889725
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def test(self):
            return self.locale
    
    provider = TestProvider('en')
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

    with provider.override_locale(locales.UK):
        assert provider.get_current_locale() == locales.UK
    assert provider.get_current_locale() == locales.EN



# Generated at 2022-06-13 23:58:22.201753
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):

        def personal_id(self) -> str:
            return self._data['personal_id']

    provider = TestProvider()
    # override_locale does not work if attribute locale is not defined.
    # So, we must not call next line before everything.
    provider._datafile = 'numbers.json'
    provider._pull()
    assert provider.personal_id() == 'Personal ID'
    with provider.override_locale('ru'):
        assert provider.personal_id() == 'Личный номер'

# Generated at 2022-06-13 23:58:29.698458
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for context manager which allows overriding current locale..

    The test must not raise exceptions
    """
    class Provider(BaseDataProvider):
        """Created for testing the method override_locale"""
    provider_obj = Provider(locale='pt')
    with provider_obj.override_locale(locale='en'):
        assert provider_obj.locale == 'en'
    assert provider_obj.locale == 'pt'

# Generated at 2022-06-14 00:00:18.820697
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test case for override_locale method of BaseDataProvider class.

    Test failures:
        (1) Exception raised in overridden locale context when
            attribute locale not found.
        (2) Second exception raised in overridden locale context when
            second attribute locale not found.
        (3) Exception raised when attribute locale not found.
    """

    # create instance for class BaseDataProvider
    provider = BaseDataProvider()
    # create context manager for method override_locale
    with provider.override_locale('ru') as p:
        # check that when overridden locale context started
        # provider was gotten
        assert p is provider
        # check that when overridden locale context started
        # provider has the same locale that passed to method override_locale
        assert p.locale == 'ru'
    # check that when overridden locale context ended
   
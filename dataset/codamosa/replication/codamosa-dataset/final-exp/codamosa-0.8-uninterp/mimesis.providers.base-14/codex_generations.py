

# Generated at 2022-06-13 23:50:47.298591
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    print('===================== Testing override_locale() of BaseDataProvider =====================')
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    person = Person('en')
    person_override = Person('en')
    with person_override.override_locale('ru'):
        assert person.get_current_locale() == 'en'
        assert person_override.get_current_locale() == 'ru'
    assert person.get_full_name(gender=Gender.FEMALE) == 'Barbara Padberg'
    assert person_override.get_full_name(gender=Gender.FEMALE) == 'Алина Комарова'

# Generated at 2022-06-13 23:50:50.167447
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    with BaseDataProvider.override_locale(locales.EN) as p:
        assert p.get_current_locale() == locales.EN
        assert p.get_currency_code() == 'USD'



# Generated at 2022-06-13 23:51:01.646811
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.address import Address
    from mimesis.providers.datetime import Datetime

    # Providers with locale dependent
    prov_address = Address(locale='en')
    prov_date = Datetime(locale='en')

    # Providers without locale dependent
    prov_random = BaseDataProvider()
    prov_person = BaseDataProvider()

    # Case 1:
    with prov_address.override_locale() as prov:
        assert prov == prov_address
    assert prov_address.locale == locales.DEFAULT_LOCALE

    # Case 2:
    with prov_date.override_locale('ru') as prov:
        assert prov == prov_date
    assert prov_date.locale == local

# Generated at 2022-06-13 23:51:13.389186
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    class TestDataProvider(BaseDataProvider):
        def __init__(self):
            self.locale = locales.DEFAULT_LOCALE

        def _pull(self):
            self._data = {}

        def test_method(self, gender: Gender = None) -> JSON:
            gender = self._validate_enum(gender, Gender)
            return self._data.get(gender)

    tdp = TestDataProvider()
    with tdp.override_locale(locales.DEFAULT_LOCALE):
        assert tdp.locale == locales.DEFAULT_LOCALE

    with tdp.override_locale(locales.RU):
        assert tdp.locale == locales.RU


# Generated at 2022-06-13 23:51:19.418701
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method _override_locale of class BaseDataProvider."""
    from mimesis.providers.person import Person
    from mimesis.enums import Gender

    person = Person(locale='en')
    assert person.full_name(gender=Gender.MALE) == 'Elvis Bennett'

    with person.override_locale('ru') as person_ru:
        assert (person_ru.full_name(gender=Gender.FEMALE) ==
                'Сара Голубева')

    assert person.full_name(gender=Gender.MALE) == 'Elvis Bennett'

# Generated at 2022-06-13 23:51:23.661001
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = 'ru'
    with BaseDataProvider(locale).override_locale() as p:
        assert str(p) == 'BaseDataProvider <ru>'
        assert p.get_current_locale() == 'ru'
    assert str(p) == 'BaseDataProvider <en>'



# Generated at 2022-06-13 23:51:29.672900
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider.override_locale."""
    # Arrange
    provider = BaseDataProvider()
    # We don't expect to raise any exception
    try:
        with provider.override_locale() as new_provider:
            pass
    except Exception as e:
        assert False


# Generated at 2022-06-13 23:51:36.868795
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import EnumProvider
    assert EnumProvider('ru').get_current_locale() == 'ru'
    with EnumProvider('ru') as provider:
        assert provider.get_current_locale() == 'ru'
    provider.get_current_locale() == 'ru'
    

# Generated at 2022-06-13 23:51:42.087960
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender, Person
    from mimesis.providers.geography import Geography

    provider = Geography(locale='ru')
    with provider.override_locale(locale='en'):
        assert provider.get_current_locale() == 'en'
        assert provider.get_another_country() != 'Австралия'
        assert provider.get_another_country() == 'Australia'

# Generated at 2022-06-13 23:51:48.475117
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        _datafile = 'test.json'

    provider = TestProvider()

    with provider.override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:03.279432
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test BaseDataProvider._override_locale()."""
    provider = BaseDataProvider('en')
    provider.override_locale('en')
    assert provider.get_current_locale() == 'en'



# Generated at 2022-06-13 23:52:07.502891
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    with pytest.raises(ValueError):
        with BaseDataProvider.override_locale():
            pass

# Generated at 2022-06-13 23:52:10.005447
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import mimesis.builtins
    provider = mimesis.builtins.BaseBuiltin
    with provider().override_locale() as provider:
        assert str(provider) == 'BaseBuiltin <en>'

# Generated at 2022-06-13 23:52:24.323899
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person(locale='en')
    with p.override_locale('ru') as pr:
        male = pr.name(gender=Gender.MALE)
        female = pr.name(gender=Gender.FEMALE)

        assert pr.locale == 'ru'
        assert male in pr.data['_ru']['names']['male']
        assert female in pr.data['_ru']['names']['female']

    assert p.locale == 'en'
    assert male not in p.data['_en']['names']['male']
    assert female not in p.data['_en']['names']['female']

    # Test exception
    import pytest


# Generated at 2022-06-13 23:52:32.751904
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the behavior of context manager `override_locale`.

    ------------------------------------------------------
    >>> with provider.override_locale('ru') as p:
    ...     p.get_current_locale()
    'ru'
    >>> provider.get_current_locale()
    'en'
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'provider': BaseDataProvider()})

# Generated at 2022-06-13 23:52:39.049345
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.providers.address import Address
    address = Address(seed=1)
    for lvl in ['prefecture', 'district', 'region']:
        assert getattr(address, lvl)(level=0) == 'Хабаровский край'
        with address.override_locale(locales.EN):
            assert getattr(address, lvl)(level=0) == 'Russia'


"""
Only for testing
"""

# Generated at 2022-06-13 23:52:45.398858
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None):
            super().__init__(locale, seed)

        def method(self):
            return self.locale

    provider = Provider()
    with provider.override_locale('ru') as p:
        assert p.method() == 'ru'

    assert provider.method() == 'en'

# Generated at 2022-06-13 23:52:56.823818
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MasterProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)
        def foo(self):
            return self.locale

    class LocaleProvider(MasterProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)

        def foo(self):
            return self.locale

    provider_base = MasterProvider()
    provider_locale = LocaleProvider(locales.EN)
    test_result_1 = provider_base.foo()
    test_result_2 = provider_locale.foo()

    assert test_result

# Generated at 2022-06-13 23:53:06.065195
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TempProvider(BaseDataProvider):
        def _pull(self, datafile: str = '') -> None:
            self._data = {}
        def _validate_enum(self, item: Any, enum: Any) -> Any:
            return item
        def get_data(self, *args, **kwargs) -> Dict[str, Any]:
            return self._data

    provider = TempProvider()
    assert provider.get_current_locale() == locales.EN
    assert provider.get_data() == {}

    with provider.override_locale(locales.RU):
        assert provider.get_current_locale() == locales.RU
        assert provider.get_data() == {}

# Generated at 2022-06-13 23:53:10.215321
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    x = BaseDataProvider()
    with x.override_locale('ru'):
        assert x.locale == 'ru'
    # End of Unit test

# Generated at 2022-06-13 23:53:26.725805
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.providers import Person, Address

    provider = Person(locale='ru')
    address = Address(locale='en')

    with provider.override_locale('de') as provider, address.override_locale('ru'):
        assert provider.get_current_locale() == 'de'
        assert address.get_current_locale() == 'ru'

    assert provider.get_current_locale() == 'ru'
    assert address.get_current_locale() == 'en'

# Generated at 2022-06-13 23:53:31.952284
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Business

    bp = Business()
    with bp.override_locale('ru') as provider:
        assert provider.get_current_locale() == 'ru'
        assert provider.locale == 'ru'

    assert bp.get_current_locale() == locales.DEFAULT_LOCALE
    assert bp.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:53:39.814567
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the method override_locale of the class BaseDataProvider."""
    from mimesis.providers.address import Address
    from mimesis.enums import Gender

    address = Address('en')
    with address.override_locale('ru') as new_address:
        assert new_address.full_name('male') in 'Элио Архипов Тимофеевич'
        assert new_address.full_name('female') in 'Софья Кролева Владимировна'


# Generated at 2022-06-13 23:53:51.057147
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Car(BaseDataProvider):

        def make(self) -> str:
            return self.random.choice(self._data['car']['make'])

        def model(self) -> str:
            return self.random.choice(self._data['car']['model'])

        def year(self) -> int:
            return self.random.randint(1915, 2019)

        def __str__(self) -> str:
            return '{}: {} {} ({})'.format(self.locale,
                                           self.make(),
                                           self.model(),
                                           self.year())

    car = Car()
    with car.override_locale('ru') as russian_car:
        assert isinstance(russian_car, Car)
        assert car is russian_car
        assert russian

# Generated at 2022-06-13 23:53:58.963351
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import datatypes
    print(datatypes)
    datatypes.DEFAULT_LOCALE = 'es'
    provider = datatypes.Datatypes(locale='es')
    print(provider.get_current_locale())
    print(provider.datetimestamp())
    assert provider.get_current_locale() == 'es'
    with datatypes.DataTypes.override_locale(locale='en'):
        assert provider.get_current_locale() == 'en'
        print(provider.get_current_locale())
        print(provider.datetimestamp())
    assert provider.get_current_locale() == 'es'
    print(provider.get_current_locale())
    print(provider.datetimestamp())


# Generated at 2022-06-13 23:54:00.633793
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    p = BaseDataProvider("ru")
    ctx_manager = p.override_locale("de")
    with ctx_manager as manager:
        assert manager



# Generated at 2022-06-13 23:54:13.204663
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from .. import Address
    from .. import Person

    prov = Address()
    prov_locale = Person()

    with prov_locale.override_locale('ru') as person_locale_ru:
        assert prov_locale.get_current_locale() == person_locale_ru.get_current_locale() == 'ru'

    with prov.override_locale('ru'):
        assert prov_locale.get_current_locale() == person_locale_ru.get_current_locale() == 'ru'
    #should raise error, because class Address is not locale dependent
    with pytest.raises(ValueError) as ex:
        with prov.override_locale('ru') as prov:
            pass

# Generated at 2022-06-13 23:54:28.070991
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider._override_locale method."""
    class SomeDataClass(BaseDataProvider):
        """Some data provider class."""

        def __init__(self) -> None:
            super().__init__()
            self._datafile = 'some.json'
            self._pull()

        @property
        def data(self) -> Dict[str, str]:
            """Get the data from JSON."""
            return self._data

    provider = SomeDataClass()
    assert provider.locale == locales.EN
    assert provider.data == {'en': 'en', 'ru': 'ru'}

    provider.locale = 'ru'
    assert provider.data == {'en': 'en', 'ru': 'ru'}


# Generated at 2022-06-13 23:54:35.612543
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def test(self) -> str:
            return self.random.choice(self._data['food'])

    foo = TestProvider()

    with foo.override_locale('ru') as f:
        assert f.test().endswith('о')
        assert foo.test().endswith('о')

    with foo.override_locale('en') as f:
        assert f.test().endswith('s')
        assert foo.test().endswith('s')

    assert foo.test().endswith('s')



# Generated at 2022-06-13 23:54:40.606742
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestBaseDataProvider(BaseDataProvider):
        pass

    provider = TestBaseDataProvider()

    with provider.override_locale('ru') as provider:
        assert provider == TestBaseDataProvider('ru')

    assert provider == TestBaseDataProvider('en')



# Generated at 2022-06-13 23:55:07.488468
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    def check_method(self):
        try:
            assert self.get_current_locale() == 'en'
        except AttributeError:
            raise ValueError('«{}» has not locale dependent'.format(
                self.__class__.__name__))

    check_method(BaseDataProvider())
    check_method(BaseDataProvider(locale='en'))

    with BaseDataProvider().override_locale() as provider:
        assert provider.get_current_locale() == 'en'

    with BaseDataProvider().override_locale(locale='ru') as provider:
        assert provider.get_current_locale() == 'ru'


# Generated at 2022-06-13 23:55:16.924828
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestClass(BaseDataProvider):
        # Unit test for method override_locale of class BaseDataProvider
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

            datafile = 'business.json'
            self.datafile = datafile
            self._pull(datafile)
    # Unit test for method override

# Generated at 2022-06-13 23:55:24.761076
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider."""
    class _BaseDataProvider(BaseDataProvider):
        def get_data(self, key: str) -> str:
            return key

    try:
        bdp = _BaseDataProvider()
        with bdp.override_locale('ru') as bdp:
            assert bdp.get_current_locale() == 'ru'
            assert bdp.get_data('foo') == 'foo'
        assert bdp.get_data('bar') == 'bar'
    except Exception as e:
        assert e.args[0] == '«get_data» is not a valid method'

# Generated at 2022-06-13 23:55:38.695068
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.address import Address
    from mimesis.enums import Gender

    address = Address(locale='fr')

    assert address.province() == 'British Columbia'

    with address.override_locale(locale='fr'):
        assert address.province() == 'Québec'

    assert address.province() == 'British Columbia'

    with address.override_locale(locale='fr'):
        assert address.province() == 'Québec'
        assert address.full_name(gender=Gender.MALE) == 'Jean-Baptiste Durand'
        with address.override_locale(locale='de'):
            assert address.province() == 'Nordrhein-Westfalen'

# Generated at 2022-06-13 23:55:45.636991
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestBaseDataProvider(BaseDataProvider):

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale,
                             seed=seed)
            self._datafile = 'test.json'

        def _pull(self, datafile: str = '') -> Dict:
            self._data = {
                'test': {
                    'one': 'one',
                    'two': 'two',
                    'three': 'three',
                },
                'test2': {
                    'one': 'one',
                    'two': 'two',
                    'three': 'three',
                }
            }

    p = TestBaseDataProvider()
    assert p.get_current_locale() == 'en'


# Generated at 2022-06-13 23:55:50.343301
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = locales.EN
    class TestDataProvider(BaseDataProvider):
        pass
    td = TestDataProvider(locale)
    assert td.get_current_locale() == locales.EN

    with td.override_locale(locale=locales.RU):
        assert td.get_current_locale() == locales.RU

    assert td.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:56:00.028309
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the override_locale contextmanager of BaseDataProvider.
    """
    from mimesis.builtins.numbers import Number
    base_locale = Number.get_current_locale()
    locale = 'be'
    with Number.override_locale(locale):
        assert locale == Number.get_current_locale()
    assert base_locale == Number.get_current_locale()
    base_locale = Number.get_current_locale()
    locale = 'zh'
    with Number.override_locale(locale):
        assert locale == Number.get_current_locale()
    assert base_locale == Number.get_current_locale()
    base_locale = Number.get_current_locale()
    locale = 'en'

# Generated at 2022-06-13 23:56:05.385771
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        pass
    provider = Test()
    loc = provider.get_current_locale()
    assert loc == 'en'

    with provider.override_locale(locale=locales.EN) as provider:
        provider_loc = provider.get_current_locale()
        assert provider_loc == 'en'

    loc = provider.get_current_locale()
    assert loc == 'en'

# Generated at 2022-06-13 23:56:14.437544
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for test_BaseDataProvider_override_locale."""
    from mimesis.builtins import Code
    for i in range(20):
        with Code().override_locale(locales.DEFAULT_LOCALE) as code:
            assert code.get_current_locale() == locales.DEFAULT_LOCALE
            assert code.get_random_color() != 'color'
        with Code().override_locale(locales.EN) as code:
            assert code.get_current_locale() == locales.EN
            assert code.get_random_color() == 'color'


# Generated at 2022-06-13 23:56:22.644675
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Foo(BaseDataProvider):
        def __init__(self, locale, seed):
            super(Foo, self).__init__(locale, seed)
            with self.override_locale(locale='ru'):
                self.data = self._data

        def __str__(self):
            return self.__class__.__name__
    f = Foo(locale='en', seed='1')
    assert str(f) == 'Foo'

# Generated at 2022-06-13 23:57:05.181763
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    pass # TODO



# Generated at 2022-06-13 23:57:12.962013
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    with BaseDataProvider().override_locale(locales.RU) as provider:
        assert provider.get_current_locale() == locales.RU
        assert provider.locale == locales.RU
    assert provider.get_current_locale() == locales.EN
    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:57:20.769353
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for ``BaseDataPrvider.override_locale`` method."""
    class LocaleExampleProvider(BaseDataProvider):

        @property
        def foo(self):
            return self._data['foo']

    provider = LocaleExampleProvider()
    with provider.override_locale('en-US') as p:
        assert p.foo == 'foo'

    assert provider.foo == 'bar'



# Generated at 2022-06-13 23:57:35.385873
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    path = "mimesis/providers/base.py"
    with open(path, "r") as source:
        lines = 0
        prev_line = ""
        for line in source:
            if line.find("def _setup_locale(self, locale: str") != -1:
                prev_line = line.strip()
            if line.find("def _pull(self, datafile: str = '')") != -1 and prev_line.find("def _setup_locale(self, locale: str") != -1:
                lines += 1
            if line.find("d = self._update_dict(d, get_data(locale))") != -1:
                lines += 1
    assert lines == 2


# Generated at 2022-06-13 23:57:42.340427
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data = {
        'Units': {
            'Area': {
                'miles²': 'square miles',
            }
        }
    }
    provider = BaseDataProvider()
    provider._data = data
    with provider.override_locale('en_US') as instance:
        assert instance._data == data
        assert instance.get_current_locale() == 'en_US'
    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:57:53.346828
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = locales.EN
    locale_other = locales.ZH
    provider = BaseDataProvider()
    provider_other = BaseDataProvider()

    assert provider.get_current_locale() == locale_other

    with provider.override_locale(locale):
        assert provider.get_current_locale() == locale

    assert provider.get_current_locale() == locale_other

    with provider_other.override_locale(locale) as pr:
        assert pr.get_current_locale() == locale
        assert provider_other.get_current_locale() == locale

# Generated at 2022-06-13 23:57:59.761471
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # create base provider
    base = BaseDataProvider()

    # create base provider with locale using "with"-statement
    with BaseDataProvider().override_locale('ru') as provider:
        provider.locale == 'ru'

    # create base provider with locale using "with"-statement
    with BaseDataProvider().override_locale() as provider:
        provider.locale == 'ru'

# Generated at 2022-06-13 23:58:09.982180
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for BaseDataProvider._override_locale."""
    from mimesis.builtins import Person
    person = Person(locale='en')
    with person.override_locale('ru'):
        assert person._pull.cache_info().hits == 0
        assert person.get_current_locale() == 'ru'
        assert person.full_name() == 'София Репина'
        assert person.full_name() == 'Петров Анатолий Григорьевич'
        assert person._pull.cache_info().hits == 2
    assert person._pull.cache_info().hits == 0
    assert person.get_current_locale() == 'en'


# Generated at 2022-06-13 23:58:20.750917
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.enums import AddressItem

    # Unit test for method override_locale of class BaseDataProvider.
    def test_new_locale():
        address = Address()
        with address.override_locale('ru') as test_address:
            state = test_address.get_state(AddressItem.STATE)
        with address.override_locale('en') as test_address:
            city = test_address.get_city()
        assert state == 'Алтайский край'
        assert city == 'Riverside'

    # Unit test for method override_locale of class BaseDataProvider.

# Generated at 2022-06-13 23:58:26.027569
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()

    with provider.override_locale('ru') as f:
        assert f.get_current_locale() == 'ru'

    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-14 00:00:14.237315
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)
        def get_current_locale(self) -> str:
            return self.locale
    tp = TestProvider('en')
    assert tp.get_current_locale() == 'en'
    with tp.override_locale('ru') as tp:
        assert tp.get_current_locale() == 'ru'
    assert tp.get_current_locale() == 'en'

# Generated at 2022-06-14 00:00:23.913905
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Address, time

    address_ru = Address(seed=20140715)
    with address_ru.override_locale(locales.RU):
        assert address_ru.get_current_locale() == locales.RU
        assert address_ru.get_timezone() == 'Europe/Moscow'

    time_ru = time.Time(seed=20140715)
    with time_ru.override_locale(locales.RU):
        assert time_ru.get_current_locale() == locales.RU
        assert time_ru.day_of_week() == 'Воскресенье'
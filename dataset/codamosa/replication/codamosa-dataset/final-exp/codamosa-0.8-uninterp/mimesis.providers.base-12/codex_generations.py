

# Generated at 2022-06-13 23:50:42.495926
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    p = BaseDataProvider()

    with p.override_locale(locales.DEFAULT_LOCALE):
        assert p._data == {}

    class NewProvider(BaseDataProvider):
        pass

    p_new = NewProvider()

    with p_new.override_locale(locales.DEFAULT_LOCALE):
        assert p_new._data == {}

# Generated at 2022-06-13 23:50:50.676838
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test functionality of ``override_locale`` method of class ``BaseDataProvider``."""
    # Initialization
    provider = BaseDataProvider()
    # Test something
    with provider.override_locale('ru'):
        override_locale = provider.get_current_locale()
    current_locale = provider.get_current_locale()
    # Assertions
    assert override_locale == 'ru'
    assert current_locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:50:59.883078
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code
    import pytest

    class TestProvider(Code):
        """Test provider."""

        SEED = None

        def __init__(self, seed: Seed = None) -> None:
            """Initialize attributes.

            :param seed: Seed. Defaults to None.
            """
            super().__init__(seed=seed)

    code = TestProvider()

    code.locale = locales.DEFAULT_LOCALE

    with pytest.raises(ValueError):
        with code.override_locale(locale=locales.EN):
            pass

# Generated at 2022-06-13 23:51:04.131385
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    assert provider.locale == locales.EN
    with provider.override_locale(locales.RU):
        assert provider.locale == locales.RU
    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:51:06.041167
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

if __name__ == '__main__':
    test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:51:13.296135
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass
#     import mimesis.providers.person as person
#     class Person(person.Person):
#         datafile = 'person.json'

#     person = Person()
#     with person.override_locale(locales.EN):
#         assert person.get_current_locale() == locales.EN
#         assert person.name() != person.name()
#         assert person.job_title() != person.job_title()

# Generated at 2022-06-13 23:51:16.589355
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        LOCALE_DEPENDENT = True

    provider = TestProvider('en')
    with provider.override_locale('ru') as _:
        assert provider.get_current_locale() == 'ru'

    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:51:27.103622
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert 'en' == BaseDataProvider().get_current_locale()
    assert 'ru' == BaseDataProvider('ru').get_current_locale()

    with BaseDataProvider().override_locale() as data_provider:
        assert 'en' == data_provider.get_current_locale()

    with BaseDataProvider('ru').override_locale('ru') as data_provider:
        assert 'ru' == data_provider.get_current_locale()

    with BaseDataProvider('ru').override_locale() as data_provider:
        assert 'en' == data_provider.get_current_locale()

    with BaseDataProvider('ru_RU').override_locale() as data_provider:
        assert 'en' == data_provider.get_current_locale

# Generated at 2022-06-13 23:51:33.364482
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = locales.EN
    locale_1 = locales.RU
    origin_locale = locales.DEFAULT_LOCALE
    try:
        with p.override_locale(locale):
            p.locale == locale
        with p.override_locale(locale_1):
            p.locale == locale_1
    except ValueError:
        print('«{}» has not locale dependent'.format(
            p.__class__.__name__))
    assert p.locale == origin_locale
    assert p.get_current_locale() == origin_locale


# Generated at 2022-06-13 23:51:37.756350
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from .builtins import Person
    from .builtins.address import Address
    p = Person()
    p.locale = "en"
    with p.override_locale('ru') as ru:
        assert ru.locale == 'ru'
    with p.override_locale() as ru:
        assert ru.locale == locales.EN
    with Address().override_locale('ru') as ru:
        assert ru.locale == 'ru'

# Generated at 2022-06-13 23:51:54.008003
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Person
    from mimesis.enums import Gender, Titles
    from mimesis.typing import GenderPayload

    provider = Person()
    origin_locale = provider.locale

    with provider.override_locale('de') as en_provider:
        assert en_provider.locale == 'de'

        assert en_provider.full_name(Gender.MALE) != \
            provider.full_name(Gender.MALE)

        assert en_provider.full_name(Gender.MALE) != \
            Person(locale='de').full_name(Gender.MALE)

    assert provider.locale == origin_locale

# Generated at 2022-06-13 23:52:02.820857
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''
    Test BaseDataProvider.override_locale()
    '''
    class TestProvider(BaseDataProvider):
        '''
        Test provider
        '''
        def random_element(self) -> Any:
            '''
            Test method
            '''
            return self._data

    provider = TestProvider()
    assert provider.random_element() == TestProvider().random_element()

    with TestProvider().override_locale(locales.UK) as new_provider:
        assert TestProvider().random_element() != \
               new_provider.random_element()



# Generated at 2022-06-13 23:52:07.453990
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    assert(str(BaseDataProvider.override_locale) == 'contextmanager object at 0x7f835298a4a8')


# Generated at 2022-06-13 23:52:15.574094
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test example for method override_locale of class BaseDataProvider.

    This example shows an override_locale function in action.

    """
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.person import Person
    from mimesis.providers.internet import Internet
    
    data_providers = [
        Person('ru'),
        Datetime('ru'),
        Internet('ru'),
    ]
    for p in data_providers:
        print(p.full_name())

    print('--------------')
    for p in data_providers:
        with p.override_locale('en'):
            print(p.full_name())

    print('--------------')
    for p in data_providers:
        print(p.full_name())

# Generated at 2022-06-13 23:52:27.687752
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for BaseDataProvider.override_locale

    The test checks that the context manager method ``override_locale()``
    overrides current locale and restores it after the context ended.
    """
    class TestDataProvider(BaseDataProvider):
        """Testing data provider."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes for data providers.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale, seed)
            self._datafile = 'test_data.json'
            self._pull()

        def get_data(self) -> JSON:
            """Return data

            :return: Data from JSON file
            """


# Generated at 2022-06-13 23:52:38.178346
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address, Language
    address = Address()
    lang = Language()
    with address.override_locale('ru'):
        assert address.locale == 'ru'
        assert address.get_full_name() == 'Иванов Иван Иванович'
    assert address.locale == locales.DEFAULT_LOCALE
    with address.override_locale('ru') as a:
        assert a.locale == 'ru'
        assert address.get_full_name() == 'Иванов Иван Иванович'
    assert address.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:43.281684
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Person
    # assert Person().override_locale().get_current_locale() == 'en'

if __name__ == '__main__':
    p = test_BaseDataProvider_override_locale(locale='ru')
    print(p)

# Generated at 2022-06-13 23:52:47.879771
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = "en"
    provider = BaseDataProvider(locale)
    result = provider.override_locale(locale)
    assert result.__class__.__name__ == str(provider)
    assert result.get_current_locale() == locale


# Generated at 2022-06-13 23:52:53.338697
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    for locale in locales.SUPPORTED_LOCALES:
        with provider.override_locale(locale) as p:
            assert p.get_current_locale() == locale
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:55.981372
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    with provider.override_locale(locales.JA) as p:
        assert p.locale == locales.JA
    assert provider.locale == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:53:23.985235
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    bdp = BaseDataProvider()
    locale = bdp.get_current_locale()
    assert locale == locales.DEFAULT_LOCALE
    with bdp.override_locale(locales.EN) as prov:
        assert prov.get_current_locale() == locales.EN
    assert bdp.get_current_locale() == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:53:34.485490
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.base import BaseDataProvider
    from mimesis.providers.person import Person
    from mimesis.providers.datetime import Datetime
    from mimesis.providers.code import Code

    locale = 'ru'

    class TestBaseDataProvider(BaseDataProvider):
        """Test class inherited from BaseDataProvder."""

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            """Initialize attributes for data providers.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'test.json'
            self._pull()


# Generated at 2022-06-13 23:53:40.860972
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Title, Data

    class MyData(Data):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)
            self.provider = Title(self.seed)

        def get_title(self) -> str:
            """Get title for the random class."""
            return self.provider.title()

    mydata = MyData(seed=42)
    assert mydata.get_title() == 'Technician'
    with mydata.override_locale('ru'):
        assert mydata.get_title() == 'Аббревиатура'
    assert mydata.get_title() == 'Technician'

# Generated at 2022-06-13 23:53:48.597563
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Geography
    from mimesis.enums import Locale

    class TestGeography(Geography):
        def __init__(self, locale: str = 'en', seed: Seed = None):
            super().__init__()

        with TestGeography().override_locale(Locale.RU):
            assert TestGeography().get_current_locale() == 'ru'

        assert TestGeography().get_current_locale() == 'en'

# Generated at 2022-06-13 23:53:54.168181
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    with provider.override_locale('ru_RU') as p:
        assert p.get_current_locale() == 'ru_ru'
        assert p.get_current_locale() == 'ru_RU'
    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:53:59.951029
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class A(BaseDataProvider):
        def get_data(self) -> str:
            return 'A'

    class B(BaseDataProvider):
        def get_data(self) -> str:
            return 'B'

    a = A()
    b = B()

    assert a.override_locale(locales.EN).get_data() == 'A'
    assert a.override_locale(locales.RU).get_data() == 'A'

    assert b.override_locale(locales.EN).get_data() == 'B'
    assert b.override_locale(locales.RU).get_data() == 'B'

# Generated at 2022-06-13 23:54:12.055151
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Example(BaseDataProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.path = Path(__file__).parent.parent.joinpath('data')
            self._file_path = self.path.joinpath('en', 'example.json')

        def get_json(self):
            """Returns path for en/example.json."""
            return self._file_path

    ex = Example()
    with ex.override_locale('ru') as ex_ru:
        path_ru = ex_ru.get_json()
    path_en = ex.get_json()
    assert not path_ru == path_en

# Generated at 2022-06-13 23:54:18.963154
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code
    en_code = Code()
    ru_code = Code('ru')
    with ru_code.override_locale():
        assert en_code.get_current_locale() == 'en'
        assert ru_code.get_current_locale() == 'en'
    assert en_code.get_current_locale() == 'en'
    assert ru_code.get_current_locale() == 'ru'


# Generated at 2022-06-13 23:54:26.251310
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):

        def __init__(self, locale: str, seed: Seed = None) -> None:
            super().__init__(locale, seed)

        def _pull(self, datafile):
            self._data = {'locale': self.get_current_locale()}

    with TestProvider('en').override_locale('ru') as data_provider:
        assert data_provider.get_current_locale() == 'ru'
        assert data_provider._data['locale'] == 'ru'

    assert data_provider.get_current_locale() == 'en'
    assert data_provider._data['locale'] == 'en'

# Generated at 2022-06-13 23:54:33.351867
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    test_provider = BaseDataProvider("en")

    with test_provider.override_locale("ru"):
        assert test_provider.locale == "ru"

    with test_provider.override_locale("en-US"):
        assert test_provider.locale == "en-us"

    with test_provider.override_locale("en-IN"):
        assert test_provider.locale == "en-in"

# Generated at 2022-06-13 23:55:21.951746
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """BaseDataProvider(override_locale)."""
    from . import builtins
    from .builtins import cars as _cars
    from .builtins import food as _food

    _car = builtins.Car()
    _food = builtins.Food()


# Generated at 2022-06-13 23:55:32.901062
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person

    person = Person('ru')
    with person.override_locale('en') as use_en_locale:
        assert use_en_locale.get_current_locale() == 'en'
        assert use_en_locale is person
        assert use_en_locale.full_name() != person.full_name()

    assert person.get_current_locale() == 'ru'
    assert person.full_name() != use_en_locale.full_name()
    assert person.full_name() == person.full_name()

# Generated at 2022-06-13 23:55:40.479489
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        """Tests."""
        pass

    provider = Test()
    assert provider.get_current_locale() == locales.EN
    with provider.override_locale(locales.DEFAULT_LOCALE) as provider:
        assert provider.get_current_locale() == locales.DEFAULT_LOCALE

    assert provider.get_current_locale() == locales.EN


# Generated at 2022-06-13 23:55:50.124703
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None):
            super().__init__(locale=locale, seed=seed)

    p_ru = MyProvider('ru')
    p_en = MyProvider()
    with p_ru.override_locale('en') as p:
        assert p is p_ru
        assert p.locale == 'en'
        assert p.get_current_locale() == 'en'
    assert p_ru.locale == 'ru'
    assert p_ru.get_current_locale() == 'ru'

    def raise_context_error():
        with p_en.override_locale('en') as p:
            raise ValueError


# Generated at 2022-06-13 23:55:57.094462
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''
    Method that tests BaseDataProvider override_locale
    '''
    data_provider = BaseDataProvider()
    data_provider._data = {'test': '123'}
    locale = locales.EN
    with data_provider.override_locale(locale) as data_provider:
        assert data_provider.get_current_locale() == locale
        assert data_provider._data.get('test') == '123'



# Generated at 2022-06-13 23:56:05.019768
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    from mimesis.providers.lorem import Lorem

    def test_gender(gender):
        assert isinstance(gender, Gender)
        assert gender in [Gender.MALE, Gender.FEMALE]

    def test_text(text):
        assert isinstance(text, str)
        assert text

    ru_lorem = Lorem(locale='ru')
    with ru_lorem.override_locale('en'):
        assert ru_lorem.locale == 'en'
        assert ru_lorem.text().startswith('Lorem ipsum dolor sit')
        test_text(ru_lorem.text())
        test_text(ru_lorem.paragraph())

# Generated at 2022-06-13 23:56:15.728288
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.enums import Gender, Person
    from mimesis.builtins.person import Person as PersonProvider
    from mimesis.builtins.person.info import PersonInfo

    pro = PersonProvider('en')

    assert pro.full_name() == 'Stacy Webb'
    assert pro.gender() == Gender.FEMALE.value
    assert pro.occupation() == 'Fiberglass laminator'
    assert pro.job_title() == 'Food scientist'
    assert pro.family_member() == Person.MOTHER.value

    assert pro.full_name(gender=Gender.MALE) == 'Louis Garner'
    assert pro.job_title(gender=Gender.MALE) == 'Financial analyst'

    with pro.override_locale('ru') as p:
        assert p.full_name

# Generated at 2022-06-13 23:56:26.919910
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Assert that AttributeError is raised if locale is not locale-dependent
    import re
    import pytest

    with pytest.raises(ValueError) as excinfo:
        with BaseDataProvider().override_locale('ru'):
            pass
    assert re.match("«.*» .*", str(excinfo.value))

    # Assert that method returns context manager
    from mimesis.builtins import String
    with String().override_locale('ru') as bdp:
        assert isinstance(bdp, String)

    # Assert that method overrides locale
    from mimesis.builtins import Structure
    bdp = Structure()
    assert bdp.get_current_locale() == 'en'
    with bdp.override_locale('ja'):
        assert bdp.get_current

# Generated at 2022-06-13 23:56:28.878104
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    assert isinstance(provider, BaseDataProvider)
    assert provider.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:56:34.761180
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    data_provider = BaseDataProvider()
    with data_provider.override_locale(locales.EN) as d:
        assert d.get_current_locale() == locales.EN
    assert data_provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:58:10.327218
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestDataGenerator(BaseDataProvider):
        _datafile = 'names.json'

        def get_full_name(self, gender: str = '',
                          with_last_name: bool = True):
            return self.random.choice(self._data[gender]['full_name'])

    gen = TestDataGenerator(locale='fr')
    with gen.override_locale(locale='en'):
        name = gen.get_full_name(gender='male')
        result = name in gen._data['male']['full_name']
    assert result

# Generated at 2022-06-13 23:58:14.308112
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    with provider.override_locale() as p:
        assert p.locale == 'en'



# Generated at 2022-06-13 23:58:20.364315
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyProvider(BaseDataProvider):
        def __init__(self, **kwargs):
            pass
        def get_current_locale(self):
            return self.locale

    provider = MyProvider(locale='es')
    locale = provider.get_current_locale()
    assert locale == 'es'

    with provider.override_locale('ru'):
        locale = provider.get_current_locale()
        assert locale == 'ru'

    locale = provider.get_current_locale()
    assert locale == 'es'



# Generated at 2022-06-13 23:58:31.380820
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.providers import (
        Address,
        Datetime,
        Person,
    )
    from mimesis.providers import helpers as h

    person = Person(locale='ru')
    address = Address(locale='ru')
    datetime = Datetime(locale='ru')

    assert isinstance(person._data, dict)
    assert isinstance(address._data, dict)
    assert isinstance(datetime._data, dict)

    # The initial locale is ``ru``
    assert person.get_current_locale() == 'ru'
    assert address.get_current_locale() == 'ru'
    assert datetime.get_current_locale() == 'ru'

    # Check ``ru`` locale in providers
   

# Generated at 2022-06-13 23:58:35.201730
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.providers.geography import Geography
    address = Address('en')
    with address.override_locale('ru') as address:
        assert address.random_zip_code() in Geography('ru').zip_codes()
    assert address.random_zip_code() in Geography('en').zip_codes()

# Generated at 2022-06-13 23:58:41.024600
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.geography import Geography

    geo = Geography()

    with geo.override_locale('uk') as g:
        assert g.get_current_locale() == 'uk'
        assert g.get_country_name() == 'Україна'



# Generated at 2022-06-13 23:58:49.539760
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unittest.
    Testing method override_locale.
    """
    
    from mimesis.providers.base import BaseDataProvider
    from mimesis.enums import Gender
    from mimesis.typing import Seed
    from mimesis.exceptions import UnsupportedLocale

    class SimpleProvider(BaseDataProvider):
        """Simple data provider."""

        def gender(self, gender: Gender = None) -> str:
            """Get gender in string form.

            :param gender: :class:`Gender` instance.
            :return: Gender.
            """
            return self._validate_enum(gender, Gender)

    seed = Seed(3)
    random = Random()

    provider = SimpleProvider('ru', seed)

    # if isinstance(self, BaseDataProvider): raise ValueError('«Allergy» has

# Generated at 2022-06-13 23:58:58.566267
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    if __name__=='__main__':
        from mimesis.providers.person import Person
        de = Person('de')
        with de.override_locale('it') as p:
            assert p.get_current_locale()=='it'
            assert p.name()=='Giulia'
        assert de.get_current_locale()=='de'
        assert de.name()=='Sabine'
# test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:59:08.497901
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender

    class TestProvider(BaseDataProvider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._data = {
                locales.DEFAULT_LOCALE: {
                    'male': {'first_name': 'John'},
                    'female': {'first_name': 'Jane'}},
                'ru': {
                    'male': {'first_name': 'Иван'},
                    'female': {'first_name': 'Анна'}},
            }
            self._datafile = 'test_data.json'


# Generated at 2022-06-13 23:59:11.479790
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    l = BaseDataProvider()
    l._datafile = 'base_data.json'
    l._pull()
    print(l.get_current_locale())
    with l.override_locale('ru') as provider:
        print(provider.get_current_locale())
    print(l.get_current_locale())
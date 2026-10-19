

# Generated at 2022-06-13 23:50:44.002257
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Bar(BaseDataProvider):
        def __init__(self, locale=locales.EN, seed=None):
            super().__init__(locale=locale, seed=seed)

    bar = Bar()

    with bar.override_locale(locale=locales.RU):
        assert(bar.locale == locales.RU)

    assert(bar.locale == locales.EN)



# Generated at 2022-06-13 23:50:50.021730
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person
    from mimesis.enums import Gender

    person = Person()

    with person.override_locale('ru'):
        assert person.get_full_name(gender=Gender.MALE) == 'Александр Пушкин'

    assert person.get_full_name(gender=Gender.MALE) == 'Jonh Doe'

# Generated at 2022-06-13 23:50:50.966727
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass

# Generated at 2022-06-13 23:50:55.852614
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bdp = BaseDataProvider()
    assert bdp._pull.cache_info().misses == 0
    with bdp.override_locale(locales.EN):
        assert bdp._pull.cache_info().misses == 1
    assert bdp._pull.cache_info().misses == 1

# Generated at 2022-06-13 23:51:01.031383
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def __init__(self):
            super().__init__(locale='en')

    provider = Provider()
    with provider.override_locale(locale='fr'):
        assert provider.get_current_locale() == 'fr'
    assert provider.get_current_locale() == 'en'

# Generated at 2022-06-13 23:51:05.609664
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # BaseDataProvider._pull() 
    # BaseDataProvider.get_current_locale() 
    provider = BaseDataProvider()
    # BaseDataProvider._override_locale()
    with provider.override_locale(locale='ru'):
        assert provider.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:51:15.170471
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider.

    :raise AttributeError: When provider has not locale dependent.
    """
    from mimesis.builtins import Address
    provider = Address()
    locale = 'en'
    locale_overrided = 'be'
    try:
        with provider.override_locale(locale_overrided):
            assert provider.locale == locale_overrided
        assert provider.locale == locale
    except AttributeError:
        raise ValueError('«{}» has not locale dependent'.format(
            provider.__class__.__name__))


# Generated at 2022-06-13 23:51:21.870420
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Person(BaseDataProvider):
        class Meta:
            name = 'person'
            locales = ['ru', 'en']

        def name(self) -> str:
            return self.random.choice(list(self._data.keys()))

    person = Person()
    person.name() == 'en'
    with person.override_locale('ru'):
        person.name() == 'ru'



# Generated at 2022-06-13 23:51:30.265694
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale.

    :return: Zero.
    """
    from mimesis.providers.person import Person
    from mimesis.providers.code import Code
    from mimesis.typing import CodeType

    p = Person('ru', seed=123)
    assert p.name() == 'Роман'

    with p.override_locale('en') as new_p:
        assert new_p.name() == 'Peter'

    assert p.name() == 'Роман'

    code = Code('ru', seed=123)
    assert code.code(code_type=CodeType.HEX_UPPER) == 'FFC0'


# Generated at 2022-06-13 23:51:40.175135
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from .person import Person
    rus_person = Person('ru')
    with rus_person.override_locale('ru') as person:
        assert person.locale == 'ru'
        assert person.full_name() == 'Максим Михайлов'
    assert rus_person.locale == 'ru'
    assert rus_person.full_name() == 'Максим Михайлов'


# Generated at 2022-06-13 23:51:51.802526
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """."""
    b = BaseDataProvider()
    b._pull = lambda: print('Hello')
    with b.override_locale('de'):
        pass
    with b.override_locale('ru'):
        pass
    
test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:51:55.609152
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class DummyProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE):
            super().__init__(locale)

    provider = DummyProvider()
    assert provider.locale == locales.DEFAULT_LOCALE

    with provider.override_locale(locales.EN):
        assert provider.locale == locales.EN

    assert provider.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:02.820608
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class testDataProvider(BaseDataProvider):
        locale = locales.DEFAULT_LOCALE
    class testProvider(BaseProvider):
        pass
    obj = testDataProvider()
    with obj.override_locale('en'):
        obj.locale = 'en'
    assert obj.locale == 'en'

    obj = testProvider()
    with obj.override_locale('en'):
        obj.locale = 'en'
    assert obj.locale == 'en'

# Generated at 2022-06-13 23:52:14.172398
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address.generic import Address
    from mimesis.providers.datetime import Datetime
    address = Address(locale=locales.RU)
    dt = Datetime(locale=locales.RU)
    with address.override_locale(locales.EN):
        assert address.province() != 'Новгородская'
        assert address.province() == 'New Hampshire'
        with dt.override_locale(locales.RU):
            assert dt.month(format_='dd') == '03'
            with address.override_locale(locales.RU):
                assert address.province() == 'Новгородская'

# Generated at 2022-06-13 23:52:19.772870
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale."""
    test_provider = BaseDataProvider(locale='en')
    test_provider._data = {'locale': 'en'}
    with test_provider.override_locale('ru'):
        assert test_provider._data == {'locale': 'ru'}

# Generated at 2022-06-13 23:52:27.286241
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        @property
        def test_property(self) -> int:
            return self.random.randint(100, 999)
    p = TestProvider()
    test_value = p.test_property
    with p.override_locale('ru') as q:
        assert p.locale == 'ru'
        assert test_value != q.test_property
    assert p.locale == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:52:37.062886
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data.builtin import RussiaSpecProvider
    rp = RussiaSpecProvider()

    assert rp.get_current_locale() == locales.EN
    rp.set_locale(locales.RU)
    assert rp.get_current_locale() == locales.RU

    rp.set_locale(locales.RU + '-RU')
    assert rp.get_current_locale() == locales.RU + '-RU'

    with rp.override_locale(locales.EN):
        assert rp.get_current_locale() == locales.EN

    assert rp.get_current_locale() == locales.RU + '-RU'


# Generated at 2022-06-13 23:52:42.440187
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Address

    address = Address(locale='en')
    with address.override_locale('ru') as address:
        assert str(address) == 'Address <ru>'
    assert str(address) == 'Address <en>'

    with address.override_locale('ja') as address:
        assert str(address) == 'Address <ja>'


# Generated at 2022-06-13 23:52:49.362587
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Button

    btn = Button()
    with btn.override_locale('de'):
        assert btn.locale == 'de'
        assert btn._data['button']['text'][1] == 'Spielen'

    assert btn.locale == locales.EN
    assert btn._data['button']['text'][1] == 'Play'



# Generated at 2022-06-13 23:52:58.307413
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.numbers import Numbers
    from mimesis.providers.geography import Geography
    from mimesis.enums import Gender

    with BaseDataProvider.override_locale('ru') as provider:
        assert isinstance(provider, Numbers)
        assert provider.format_int(123) == '123'

    with BaseDataProvider.override_locale('uk') as provider:
        assert isinstance(provider, Numbers)
        assert provider.format_int(123) == '123'

    with BaseDataProvider.override_locale('ru') as provider:
        assert isinstance(provider, Geography)
        assert provider._validate_enum(Gender.FEMALE, Gender) == 'женский'


# Generated at 2022-06-13 23:53:20.958179
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method ``override_locale`` of class ``BaseDataProvider``."""
    _ = BaseDataProvider()
    assert _.override_locale() is not None

# Generated at 2022-06-13 23:53:28.335191
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Child(BaseDataProvider):
        _datafile = 'test.json'
    bdp = Child()
    with bdp.override_locale('ru'):
        assert bdp.locale == 'ru'
        assert bdp._pull.cache_info().hits == 0
        assert bdp.get_current_locale() == 'ru'

    # Change locale back to default
    assert bdp.locale == locales.DEFAULT_LOCALE
    assert bdp.get_current_locale() == locales.DEFAULT_LOCALE
    assert bdp._pull.cache_info().hits == 1

# Generated at 2022-06-13 23:53:37.830916
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    def get_data_for_locale(locale):
        provider = BaseDataProvider(locale=locale)
        return provider._data

    en = get_data_for_locale(locales.EN)
    with BaseDataProvider(locale=locales.RU).override_locale(locales.FR):
        fr = get_data_for_locale(locales.FR)
        with BaseDataProvider(locale=locales.RU).override_locale(locales.ES):
            es = get_data_for_locale(locales.ES)
        assert fr == get_data_for_locale(locales.FR)
    assert en == get_data_for_locale(locales.EN)
    assert fr != get_data_for_locale(locales.FR)

# Generated at 2022-06-13 23:53:49.919570
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        """Class of provider."""

        class Meta:
            """Class of Meta."""

            locales = [locales.EN, locales.RU]

    tests = (
        (locales.EN, locales.RU, 'Здравствуй, Мир!', 'Hello, World!'),
        (locales.RU, locales.EN, 'Hello, World!', 'Здравствуй, Мир!'),
    )
    for origin_locale, override_locale, origin_text, override_text in tests:
        provider = TestProvider(origin_locale)
        with provider.override_locale(override_locale):
            assert provider.get_current_locale()

# Generated at 2022-06-13 23:53:56.440912
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Code
    from mimesis.enums import Gender

    bp = Code('en')
    with bp.override_locale('ru') as t:
        assert t.locale == 'ru'
        assert bp.locale == 'en'

    assert bp.locale == 'en'

    bp = Code()
    with bp.override_locale('ru') as t:
        assert t.locale == 'ru'
        assert bp.locale == 'en'

    assert bp.locale == 'en'

# Generated at 2022-06-13 23:54:07.867121
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    from mimesis.data import Address
    from mimesis.exceptions import UnsupportedLocale

    address = Address()
    # must be en
    assert address.get_current_locale() == 'en'

    with pytest.raises(UnsupportedLocale):
        address.override_locale('gibberish')

        with address.override_locale('ru') as _address:
            assert _address.get_current_locale() == 'ru'
            assert _address._data['country']['data'][0] == 'Россия'

        assert address.get_current_locale() == 'en'

# Generated at 2022-06-13 23:54:10.998378
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    dp = BaseDataProvider()

    with dp.override_locale('ru') as dp1:
        assert dp1.get_current_locale() == 'ru'
        assert dp.get_current_locale() == 'en'

    assert dp.get_current_locale() == 'en'



# Generated at 2022-06-13 23:54:18.700286
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person as p
    from mimesis.builtins.en import Person as p_en
    from mimesis.builtins.ru import Person as p_ru

    with p().override_locale('en') as new_locale:
        assert isinstance(new_locale, p_en)
    with p().override_locale('ru') as new_locale:
        assert isinstance(new_locale, p_ru)



# Generated at 2022-06-13 23:54:25.558751
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.automotive import LicensePlate
    import pytest

    @pytest.mark.parametrize('locale, license_plate', (
        ('en', LicensePlate(seed=123)),
        ('ru', LicensePlate(locale='ru', seed=123)),
    ))
    def test_override_locale(locale, license_plate):
        """Test generation of license plate with different locales."""
        with license_plate.override_locale(locale):
            result = license_plate.license_plate()

        assert isinstance(result, str)

    test_override_locale()

# Generated at 2022-06-13 23:54:36.234762
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from string import ascii_lowercase

    class DummyProvider(BaseDataProvider):
        """Example of dummy provider for test."""

        def __init__(self) -> None:
            super().__init__(locale=locales.EN)
            self._data = ascii_lowercase

        def get_fake(self) -> str:
            """Get fake."""
            return self._data

    provider = DummyProvider()  # English

    # English
    assert provider.get_current_locale() == locales.EN
    assert provider.get_fake() == ascii_lowercase

    with provider.override_locale(locale=locales.RU):
        # Russian
        assert provider.get_current_locale() == locales.RU
        assert provider.get_fake() == asci

# Generated at 2022-06-13 23:55:19.367059
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for a class BaseDataProvider."""
    from mimesis.providers import Person
    from mimesis.exceptions import NonEnumerableError

    p = Person()
    initial = p.full_name
    with p.override_locale('ru') as p:
        assert initial == p.full_name
    assert initial != p.full_name

    p.full_name(gender=None)
    assert initial == p.full_name

    with p.override_locale('ru'):
        assert initial != p.full_name

    p.full_name(gender='female')
    with p.override_locale('ru'):
        p.full_name(gender='female')


# Generated at 2022-06-13 23:55:27.393538
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Given

    class DummyProvider(BaseDataProvider):

        def __init__(self, locale, data='random', seed=None):
            super().__init__(locale, seed)
            self._data = {}
            self._datafile = ''
            self.data = data

        def __str__(self):
            return '{} ({})'.format(self.__class__.__name__, self.data)

    # When
    provider = DummyProvider(locales.EN, 'original')

    # Then
    assert provider.get_current_locale() == locales.EN

    override_en = provider.override_locale(locales.EN)
    assert override_en

    assert provider.get_current_locale() == locales.EN


# Generated at 2022-06-13 23:55:35.741544
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for BaseDataProvider.override_locale."""
    from mimesis.providers import Business

    biz = Business()
    with biz.override_locale() as new_biz:
        assert biz.get_current_locale() == new_biz.get_current_locale()

    with biz.override_locale('ru') as new_biz:
        assert new_biz.get_current_locale() == 'ru'



# Generated at 2022-06-13 23:55:44.116802
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)
            self._data = {'test': 'override'}

        def test_method(self) -> str:
            return self.locale

    provider = TestProvider(locales.EN)

    # Check that the method test_method() return the current locale
    # when the locale is not override
    assert provider.get_current_locale() == provider.test_method() == locales.EN

    # Check that the method test_method() return the overridden locale
    # when the locale is override

# Generated at 2022-06-13 23:55:53.006213
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import MacAddress

    mac = MacAddress()
    assert mac.get_current_locale() == locales.EN

    with mac.override_locale(locales.DE):
        assert mac.get_current_locale() == locales.DE
    assert mac.get_current_locale() == locales.EN

    with mac.override_locale(locales.ES_ES):
        assert mac.get_current_locale() == locales.ES_ES
    assert mac.get_current_locale() == locales.EN

    with mac.override_locale(locales.RU):
        assert mac.get_current_locale() == locales.RU
    assert mac.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:56:01.500814
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Currency

    locale = locales.EN
    origin_locale = getattr(Currency, 'locale', locales.DEFAULT_LOCALE)
    with Currency.override_locale(locale) as new_currency:
        assert Currency is new_currency
        assert Currency.get_current_locale() == locale
    assert Currency.get_current_locale() == origin_locale

# Generated at 2022-06-13 23:56:11.909049
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.enums import Gender

    class TestProvider(BaseDataProvider):
        """A test provider."""

        class Meta:
            """The name of data file."""

            name = 'test'

        def gender(self, gender: Gender = None) -> str:
            """Get random gender.

            :param gender: Gender.
            :return: The gender name.
            """
            value = self._validate_enum(gender, Gender)
            return get_random_item(self._data.get('gender', {}).get(value))

    provider = TestProvider()
    with provider.override_locale():
        assert provider.get_current_locale() == locales.EN

    assert provider.get_current_locale() == locales.EN

# Generated at 2022-06-13 23:56:16.833492
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():

    from mimesis.builtins import Person

    person = Person()
    with person.override_locale('ru') as p:
        assert getattr(p, 'locale') is 'ru'

    assert person.locale is 'en'



# Generated at 2022-06-13 23:56:21.891551
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider('en')
    with provider.override_locale('ru') as p:
        assert p.locale == 'ru'
    assert provider.locale == 'en'


# Generated at 2022-06-13 23:56:27.955266
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        """Test."""

        def __init__(self, locale: str = None) -> None:
            """Initialization.

            :param locale: Locale.
            """
            super(TestProvider, self).__init__(locale)

        def _pull(self) -> None:
            """Pull the content from the JSON and memorize one.
            """
            self._data = {
                'invalid': ['not_supported_locale', 'bad_locale'],
                'supported': ['en', 'ru'],
            }

    tp = TestProvider()

    with tp.override_locale('en') as t:
        assert t.locale == 'en'


# Generated at 2022-06-13 23:57:57.971055
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider()
    assert provider.get_current_locale() == 'en'

    class FakeProvider(BaseDataProvider):
        def __init__(self, locale='en', seed=None):
            super().__init__(locale, seed)

    provider = FakeProvider()

    with provider.override_locale('ru') as fake_provider:
        fake_provider.locale == 'ru'
    provider.locale == 'en'

    with provider.override_locale('ru') as fake_provider:
        fake_provider.locale == 'ru'
        with fake_provider.override_locale('uk') as fake_provider:
            fake_provider.locale == 'uk'
    provider.locale == 'en'

# Generated at 2022-06-13 23:58:05.631535
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins.enumerators import Gender
    from mimesis.builtins.locale import get_locale
    from mimesis.builtins.person import Person

    new_locale = 'ru'
    person_ru = Person(locale=new_locale)
    person_en = Person()

    person_en_male = person_en.full_name(gender=Gender.MALE)
    person_ru_male = person_ru.full_name(gender=Gender.MALE)

    person_en_female = person_en.full_name(gender=Gender.FEMALE)
    person_ru_female = person_ru.full_name(gender=Gender.FEMALE)

    assert person_ru_male != person_en_male
    assert person_ru_female != person_en_

# Generated at 2022-06-13 23:58:13.016948
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import os
    import sys
    import unittest
    sys.path.insert(0, os.path.abspath('..'))
    from mimesis.providers.science import (
        Biology as BiologyTest,
        Mathematics as MathematicsTest,
        Science as ScienceTest,
    )
    class TestBaseDataProvider(unittest.TestCase):

        def setUp(self):
            self.biology = BiologyTest()
            self.mathematics = MathematicsTest()
            self.science = ScienceTest()
            self.locale = 'ru'

        def test_context_manager(self):
            with self.biology.override_locale(self.locale):
                self.assertEqual(self.biology.locale, self.locale)

# Generated at 2022-06-13 23:58:16.213328
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class _Provider(BaseDataProvider):
        _datafile = '_Provider.json'

    provider = _Provider()
    with provider.override_locale():
        loc = provider.get_current_locale()

        assert loc != locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:58:25.290446
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import DRUGS
    from mimesis.enums import Gender
    from mimesis.providers import Person
    from mimesis.enums import DrugCategory

    # In this case the manager will execute the code in the context block,
    #  and then restore the value of the attribute.
    with Person().override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'
        assert p.full_name(Gender.MALE) in p.data['first_names']['male']
        assert p.drug_name(DrugCategory.ANALGESIC) in DRUGS

# Generated at 2022-06-13 23:58:27.721065
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address
    with Address().override_locale('ru') as address:
        assert address.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:58:35.206807
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Test for unsupported locale
    from mimesis.providers.person import Person

    person = Person()

    with person.override_locale('xx_XX') as person:
        assert person.get_current_locale() == 'en'

    # Test for correct locale
    with person.override_locale('ru_RU') as person:
        assert person.get_current_locale() == 'ru_RU'

    # Test for incorrect usage
    from mimesis.providers.person import Person

    person = Person()

    with person.override_locale('xx_XX') as person:
        assert person.get_current_locale() == 'en'

    # Test for correct locale
    with person.override_locale('ru_RU') as person:
        assert person.get_current_

# Generated at 2022-06-13 23:58:44.460685
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Principle of operation of the method override_locale."""
    from mimesis.providers.address import Address

    adr = Address()
    print('\nDefault locale:', adr.get_current_locale())
    with adr.override_locale(locales.JA):
        print('Locale in contextmanager:', adr.get_current_locale())
        print('Second call of override_locale:')
        with adr.override_locale(locales.RU):
            print('Locale in contextmanager:', adr.get_current_locale())
            print('Postcode:', adr.postal_code())
    print('Locale after exiting contextmanager:', adr.get_current_locale())

if __name__ == '__main__':
    test_

# Generated at 2022-06-13 23:58:53.797864
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """
    Override the current locale with passed and pull data for a new locale.
    """
    from mimesis.providers.base import BaseDataProvider

    class TestClass(BaseDataProvider):
        TEST_DATA = {
            'data': {
                'name': 'Test name',
                'age': 18,
            },
        }
        TEST_FILE = 'data.json'

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            super().__init__(locale, seed)
            self.locale = locale
            self._data = self.TEST_DATA
            self._datafile = self.TEST_FILE
            self._pull()


# Generated at 2022-06-13 23:58:59.163219
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method «override_locale» of class BaseDataProvider."""
    from mimesis.providers.base import BaseProvider
    provider = BaseProvider()

    try:
        with provider.override_locale():
            pass
    except ValueError:
        assert True
    else:
        assert False
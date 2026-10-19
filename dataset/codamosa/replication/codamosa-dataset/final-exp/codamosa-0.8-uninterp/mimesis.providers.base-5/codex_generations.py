

# Generated at 2022-06-13 23:50:47.732872
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of BaseDataProvider."""
    from mimesis.providers.address import Address
    from mimesis.providers.education import Education
    from mimesis.providers.internet import Internet
    from mimesis.providers.person import Person
    from mimesis.providers.phone import Phone
    from mimesis.providers.text import Text
    locale = 'et'

# Generated at 2022-06-13 23:50:59.884370
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.address import Address
    from mimesis.enums import Gender

    class ExampleProvider(Address):
        """Example of subclass from Address."""

        def get_cardinal(self, enum: Gender = Gender.MASCULINE) -> str:
            """Get a random cardinal."""
            return self._validate_enum(enum, Gender)

    provider = ExampleProvider(seed=1000)

    with provider.override_locale('ru'):
        assert provider.get_cardinal() == 'мужской'
        assert provider.get_cardinal() == 'мужской'
        assert provider.get_cardinal() == 'мужской'

    assert provider.get_cardinal() == 'male'
    assert provider.get_cardinal

# Generated at 2022-06-13 23:51:04.462613
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MyProvider(BaseDataProvider):
        pass

    p = MyProvider()
    with p.override_locale('ru') as provider:
        assert provider.locale == 'ru'
    assert p.locale == locales.DEFAULT_LOCALE



# Generated at 2022-06-13 23:51:15.707573
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Address, Names

    default_locale = locales.EN
    ru_locale = locales.RU
    ru_provider = Address(locale=ru_locale)
    ru_first_name = ru_provider.get_first_name()
    ru_last_name = ru_provider.get_last_name()

    en_first_name_ru = ru_first_name
    en_last_name_ru = ru_last_name

    en_provider = Names(locale=default_locale)
    with en_provider.override_locale(ru_locale) as ru:
        en_first_name_ru = ru.get_first_name()
        en_last_name_ru = ru.get_last_name()

    assert ru_

# Generated at 2022-06-13 23:51:26.403619
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.internet import Internet
    en_name: Any = Internet(seed=0).last_name()
    ru_name: Any = Internet(seed=0).last_name(gender=Gender.MALE)
    zh_name: Any = Internet(seed=0).last_name(gender=Gender.FEMALE)
    provider: Any = Internet(locale=locales.EN)
    with provider.override_locale(locales.RU) as ru:
        assert ru.locale == locales.RU
        assert ru.last_name(gender=Gender.MALE) == ru_name
    with provider.override_locale(locales.ZH) as zh:
        assert zh.locale == locales.ZH
       

# Generated at 2022-06-13 23:51:29.481574
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Person
    with Person().override_locale('ru') as p:
        assert p.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:51:37.839940
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.geography import Geography
    geo = Geography(seed=0)
    with geo.override_locale('ru'):
        assert geo.get_current_locale() == 'ru'
        assert geo.full_name(gender=Gender.MALE) == 'Илья Котельников'
        assert geo._pull.cache_info().hits == 1
    assert geo.get_current_locale() == locales.DEFAULT_LOCALE
    assert geo.full_name(gender=Gender.MALE) == 'John Richardson'
    assert geo._pull.cache_info().hits == 2

# Generated at 2022-06-13 23:51:46.879272
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Gender

    class Provider(BaseDataProvider):
        def __init__(self, seed=None):
            super().__init__(seed=seed)

        def get_sex(self, sex=None):
            sex = self._validate_enum(sex, Gender)
            return self._data['gender'][sex]

        def get_sex_ru(self, sex=None):
            with self.override_locale('ru'):
                return self.get_sex(sex=sex)

    seed = 0
    p = Provider(seed=seed)
    assert p.get_sex() == 'Male'
    assert p.get_sex_ru() == 'Мужской'
    assert p.get_sex(Gender.FEMALE) == 'Female'

# Generated at 2022-06-13 23:51:53.998659
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    
    # BaseDataProvider instance with seed 0
	p = BaseDataProvider(seed = 0)
	
	try:
		with p.override_locale(locale=locales.EN) as p1:
			print("p1.get_current_locale() : {}".format(p1.get_current_locale()))
			assert(p1.get_current_locale() == locales.EN)
	except ValueError:
		print("*** «{}» has not locale dependent".format("p"))
		

# Generated at 2022-06-13 23:52:03.371563
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.internet import Internet
    from mimesis.providers.address import Address

    with Internet('en').override_locale('ru') as int_:
        with Address('en').override_locale('ru') as addr:
            addr.get_region().lower() == 'санкт-петербург'
            addr.get_region().lower() == 'г. санкт-петербург'
            int_.get_email().lower() == 'федор@gmail.com'
            int_.get_email().lower() == 'anton44@yandex.ru'

# Generated at 2022-06-13 23:52:19.090073
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.date import DateTime
    provider = DateTime(locale='en')
    with provider.override_locale('ru'):
        assert provider.locale == 'ru'
        assert provider.province() != ''

# Generated at 2022-06-13 23:52:26.679602
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Init a new  BaseDataProvider instance
    provider = BaseDataProvider()
    # Test whether method ovveride_locale works
    with provider.override_locale('ru') as p:
        assert p._data == {'de': {'hello': 'hallo', 'world': 'Welt'},
                           'en': {'hello': 'hello', 'world': 'world'},
                           'ru': {'hello': 'Привет', 'world': 'мир'}}

# Generated at 2022-06-13 23:52:34.063214
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Punctuation(BaseDataProvider):
        def get_symbol(self) -> str:
            return ''

    with Punctuation().override_locale('ru-ru') as provider:
        assert provider.locale == 'ru-ru'

    with Punctuation().override_locale('ru') as provider:
        assert provider.locale == 'ru'



# Generated at 2022-06-13 23:52:47.808007
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address, Person, Processor
    from mimesis.enums import Gender

    en = Person('en')
    ru = Person('ru')

    assert en.full_name(gender=Gender.FEMALE) != ru.full_name(gender=Gender.FEMALE)
    assert en.address.country != ru.address.country

    with ru.override_locale('ru') as ru_override:
        ru_override.address  # ru.address is ru_override.address
        ru_override.full_name(gender=Gender.FEMALE) == ru.full_name(gender=Gender.FEMALE)
        ru_override.address.country == ru.address.country


# Generated at 2022-06-13 23:52:56.823441
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Payment
    from mimesis.builtins import __version__
    from mimesis.builtins import _datafile

    class ExtPayment(Payment):
        """Extend Payment for the test."""

        def __init__(self,
                     locale: str = locales.EN,
                     seed: Seed = None) -> None:
            super().__init__(locale=locale, seed=seed)

    c = ExtPayment()
    c._pull(_datafile)
    with c.override_locale(locales.RU) as _c:
        assert _c._pull(_datafile) == c._pull(_datafile)
# End of test

# Generated at 2022-06-13 23:53:06.851062
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class TestProvider(BaseDataProvider):
        def __init__(self, locale=locales.DEFAULT_LOCALE, seed=None):
            super().__init__(locale=locale, seed=seed)
            self.locale = 'en'
        def _pull(self, datafile=''):
            self._data = {'a': 'qwerty'}
    provider = TestProvider()
    assert provider.get_current_locale() == 'en'
    with provider.override_locale('fr') as fr:
        assert fr.get_current_locale() == 'fr'
    assert provider.get_current_locale() == 'en'
    with provider.override_locale('fr') as fr:
        assert fr.get_current_locale() == 'fr'
    assert provider.get

# Generated at 2022-06-13 23:53:15.683711
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: Seed = None):
            super().__init__(seed=seed, locale=locale)
            self._datafile = 'test.json'
            self._pull()
    test = Test('ru')
    with test.override_locale('en') as result:
        assert result.get_current_locale() == 'en'


# Generated at 2022-06-13 23:53:25.694942
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test method override_locale of class BaseDataProvider"""

    class TestLocaleDependent(BaseProvider):

        def __init__(self, locale="en", seed=None):
            super(TestLocaleDependent, self).__init__(seed=seed)
            self.locale = locale

        def __str__(self):
            return "{} <{}>".format(self.__class__.__name__, self.locale)

    with TestLocaleDependent().override_locale(locale="ru") as provider:
        assert str(provider) == "TestLocaleDependent <ru>"

# Generated at 2022-06-13 23:53:30.612071
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class MockProvider(BaseDataProvider):
        def __init__(self):
            super().__init__(locale='en', seed=100)
            self.locale = getattr(self, 'override_locale', None)

    provider = MockProvider()
    assert provider.locale is None

    provider.locale = getattr(provider, 'override_locale', None)
    assert provider.locale is not None

# Generated at 2022-06-13 23:53:33.667052
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Province
    locale = locales.EN
    new_province = functools.partial(Province, locale=locale, seed=1)
    with new_province().override_locale(locale=locales.RU) as prov:
        assert prov.province() == 'Мордовия'

# Generated at 2022-06-13 23:53:50.288566
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''This function verifies that the BaseDataProvider class
    method override_locale works correctly.
    If the method works correctly, the assertion runs without errors.
    '''
    from mimesis.builtins import Code
    from mimesis.enums import CodeType

    builtin_code = Code()
    assert builtin_code.code_type(CodeType.BITCOIN).startswith('1')

    with builtin_code.override_locale('ru'):
        assert builtin_code.code_type(CodeType.BITCOIN).startswith('3')


# Generated at 2022-06-13 23:53:53.795606
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    c = BaseDataProvider('ru')
    for locale in ['ru', 'en', 'de', 'es', 'fr', 'it', 'pt-br', 'zh']:
        with c.override_locale(locale):
            assert c.get_current_locale() == locale
    assert c.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:54:07.471112
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person.en import Person as Person_en
    from mimesis.providers.person.ru import Person as Person_ru

    # Create provider with default locale (English)
    p_en = Person_en()

    # Default locale is set to English
    assert p_en.locale == locales.EN

    # Get full name of male with default locale (English)
    assert p_en.full_name(gender=Gender.MALE) == 'John Smith'

    # Get full name of female with default locale (English)
    assert p_en.full_name(gender=Gender.FEMALE) == 'Jane Smith'

    # Create provider with Russian locale
    p_ru = Person_ru()

    # Russian locale is set to class attribute
    assert p

# Generated at 2022-06-13 23:54:13.085625
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    data = BaseDataProvider()

    with data.override_locale('aa'):
        assert data.locale == 'aa'

    with data.override_locale('ab'):
        assert data.locale == 'ab'

    try:
        with data.override_locale():
            assert False
    except ValueError:
        assert True

# Generated at 2022-06-13 23:54:17.617550
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Foo(BaseDataProvider):
        pass

    f = Foo()
    with f.override_locale('ru') as foo:
        assert foo.get_current_locale() == 'ru'

    assert f.get_current_locale() == 'en'


# Generated at 2022-06-13 23:54:32.120771
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    '''Unit test for method override_locale of class BaseDataProvider'''
    # print("\nProviders\n")

    class ProviderTest(BaseProvider):
        """Providers test."""

        def __init__(self, locale: str = locales.EN,
                     seed: Seed = None) -> None:
            """Initialize attributes and rules.

            :param locale: Current locale.
            :param seed: Seed to all the random functions.
            """
            super().__init__(seed=seed)

    p1 = ProviderTest(locale=locales.RU)
    p2 = ProviderTest(locale=locales.DEFAULT_LOCALE)

    assert p1.locale == locales.RU
    assert p2.locale == locales.DEFAULT_LOCALE


# Generated at 2022-06-13 23:54:35.768004
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Provider(BaseDataProvider):
        def get_data(self):
            return self._data

    instance = Provider()

    with instance.override_locale('ru'):
        assert instance.get_current_locale() == 'ru'
        assert instance.get_data()

    assert instance.get_current_locale() == locales.DEFAULT_LOCALE
    assert instance.get_data()

# Generated at 2022-06-13 23:54:46.347982
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    class TestProvider(BaseDataProvider):
        """Test provider."""

        class Meta:
            """Class Meta."""

            locales = ['en']
            provider_name = 'test_provider'
        def __init__(self, locale=locales.DEFAULT_LOCALE):
            """Initialize attributes for data providers.

            :param locale: Current locale.
            """
            super().__init__(locale=locale)

    class TestProviderWithoutLocale(BaseDataProvider):
        """Test provider without locale."""

        class Meta:
            """Class Meta."""

            provider_name = 'test_provider'


# Generated at 2022-06-13 23:54:52.691525
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for override_locale method of class BaseDataProvider."""
    class Provider(BaseDataProvider):
        def get_data(self):
            return self._data

    p = Provider()
    p._datafile = 'test.json'
    p._pull()

    # we should not be able to change locale for non locale-dependent ones
    with pytest.raises(ValueError) as e:
        with p.override_locale('ru'):
            pass
    assert str(e.value) == '«Provider» has not locale dependent'

    # locale-dependent provider
    class LocaleProvider(BaseDataProvider):
        def get_data(self):
            return self._data

    p = LocaleProvider()
    p._datafile = 'test.json'
    p._pull()

    # we can override locale for

# Generated at 2022-06-13 23:54:56.425271
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data import Address

    addr = Address(locale='ru')
    with addr.override_locale('en'):
        assert addr.get_current_locale() == 'en'

    with addr.override_locale('ru'):
        assert addr.get_current_locale() == 'ru'

# Generated at 2022-06-13 23:55:20.950927
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.education import Education

    edu = Education()
    with edu.override_locale() as provider:
        assert provider.get_current_locale() == locales.EN
        assert provider.get_faculty_full_name(
            gender=Gender.MALE) == 'Arts'
    assert edu.get_faculty_full_name(gender=Gender.MALE) == 'Гуманитарные науки'



# Generated at 2022-06-13 23:55:26.980650
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test BaseDataProvider.override_locale."""
    class SomeProvider(BaseDataProvider):
        pass

    provider = SomeProvider()

    assert provider.locale == locales.EN

    with provider.override_locale(locales.PT):
        assert provider.locale == locales.PT

    assert provider.locale == locales.EN

# Generated at 2022-06-13 23:55:31.861988
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Unit test for method override_locale of class BaseDataProvider."""
    from mimesis.builtins import Person
    with Person('en').override_locale('cs'):
        assert Person().locale == 'cs'

# Generated at 2022-06-13 23:55:41.574882
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Person

    p = Person()
    # Check initial instance
    assert p.get_current_locale() == 'en'
    assert p.full_name() == 'James Hu'

    # Override locale
    with p.override_locale('ru'):
        assert p.full_name() == 'Кирилл Сергеев'

    # Check instance after context manager
    assert p.get_current_locale() == 'en'
    assert p.full_name() == 'James Hu'



# Generated at 2022-06-13 23:55:46.941519
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for override_locale method."""
    from mimesis.builtins import Person

    with Person().override_locale('ru') as p:
        assert isinstance(p, Person)
        p.seed = 42
        assert p.seed == 42


if __name__ == '__main__':
    test_BaseDataProvider_override_locale()

# Generated at 2022-06-13 23:55:52.937523
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    bdp=BaseDataProvider()
    with bdp.override_locale(locale='ru') as provider:
        assert provider is bdp
        assert provider.get_current_locale() == 'ru'
    assert bdp.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:55:59.344997
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Override locale of provider."""
    class SomeProvider(BaseDataProvider):
        pass

    with SomeProvider() as provider:
        assert provider.get_current_locale() == locales.EN

    with SomeProvider().override_locale(locales.RU) as provider:
        assert provider.get_current_locale() == locales.RU

    with SomeProvider().override_locale(locales.JA) as provider:
        assert provider.get_current_locale() == locales.JA



# Generated at 2022-06-13 23:56:03.758141
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    # Initializing
    provider = BaseDataProvider()
    # Overriding locale
    provider.override_locale('fr')
    # Getting the current locale
    locale = provider.get_current_locale()
    # Checking that the locale is «fr»
    assert locale == locales.FR

# Generated at 2022-06-13 23:56:12.995030
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers.person import Person

    p = Person(locale='en')
    assert p.get_current_locale() == 'en'
    assert p.full_name() == 'Clayton Johnson'

    with p.override_locale(locale='ru'):
        assert p.get_current_locale() == 'ru'
        assert p.full_name() == 'Наталья Маркина'

    assert p.get_current_locale() == 'en'
    assert p.full_name() == 'Clayton Johnson'

# Generated at 2022-06-13 23:56:16.610725
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    provider = BaseDataProvider(locale="de")
    en_provider = provider.override_locale("en")
    assert en_provider is provider
    assert provider.get_current_locale() == "en"



# Generated at 2022-06-13 23:57:02.599395
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class FakeProvider(BaseDataProvider):

        def __init__(self, locale: str = locales.DEFAULT_LOCALE,
                     seed: Seed = None) -> None:
            self._data_dir = Path(__file__).parent.parent.joinpath('data')
            self._datafile = 'countries.json'
            super().__init__(seed=seed, locale=locale)


    provider = FakeProvider()

    with provider.override_locale(locales.RU):
        assert(provider.locale == locales.RU)

    assert(provider.locale == locales.EN)


# Generated at 2022-06-13 23:57:13.831797
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """BaseDataProvider.override_locale."""
    from mimesis.providers.datetime import DateTime
    import datetime
    with DateTime().override_locale('en') as date_time_manager:
        format_date = date_time_manager.format_date('')
    with DateTime().override_locale('ru') as date_time_manager:
        now = datetime.datetime.now()
        assert len(date_time_manager.format_date('')) < len(format_date)

    with DateTime().override_locale('ru') as date_time_manager:
        assert date_time_manager.format_date('').startswith('Понедельник')
        assert date_time_manager.format_date('').endsw

# Generated at 2022-06-13 23:57:23.996733
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test for method override_locale of class BaseDataProvider."""
    from mimesis.enums import Gender
    from mimesis.providers.name import Name
    with Name() as name:
        name.override_locale('ru')
        assert name.gender == Gender.MALE
        assert name.first_name(gender=None) == 'Геннадий'
        assert name.full_name() == 'Геннадий Прохоров'
    name = Name()
    with name.override_locale('ru') as name:
        assert name.gender == Gender.MALE
        assert name.first_name(gender=None) == 'Геннадий'

# Generated at 2022-06-13 23:57:25.089103
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    pass


# Generated at 2022-06-13 23:57:31.546026
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test function override_locale in class BaseDataProvider."""
    from mimesis.builtins import Person
    locale = 'En-us'
    person = Person()
    with person.override_locale(locale):
        assert person.locale == locale
    assert person.locale != locale

# Generated at 2022-06-13 23:57:33.843468
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    """Test the class BaseDataProvider."""
    BaseDataProvider.get_current_locale(BaseDataProvider().override_locale('nl'))

# Generated at 2022-06-13 23:57:40.725563
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    class Test(BaseDataProvider):
        def __init__(self):
            super().__init__(locale='en')
            print('Initialization')

    t = Test()
    print(t.get_current_locale())
    with t.override_locale('ru') as provider:
        print(provider.get_current_locale())
    print(t.get_current_locale())



# Generated at 2022-06-13 23:57:47.250752
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.providers import Business
    business = Business()

    def equal_locale(provider1: Business, provider2: Business) -> bool:
        """Check is locale of providers are equal.

        :param provider1: Provider.
        :param provider2: Provider.
        :return: ``True`` if providers have same locale, otherwise ``False``.
        """
        assert provider1.locale == provider2.locale

    with business.override_locale():
        equal_locale(business, business)

    with business.override_locale('ru'):
        equal_locale(business, business)

    with business.override_locale(locales.RU):
        equal_locale(business, business)

# Generated at 2022-06-13 23:57:54.603513
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    import pytest
    from mimesis.builtins import Person

    p = Person()
    with pytest.raises(ValueError):
        with p.override_locale('en'):
            pass  # Should raise ValueError

    with p.override_locale('ru'):
        assert p.get_current_locale() == 'ru'

    assert p.get_current_locale() == locales.DEFAULT_LOCALE

# Generated at 2022-06-13 23:58:05.464112
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = 'en'
    data = ['water', 'land', 'air', 'fire', 'time']
    class TestDataProvider(BaseDataProvider):
        def __init__(self, locale=locale, seed=None):
            super().__init__(locale=locale, seed=seed)
            self._datafile = 'data.json'
        @property
        def data(self):
            return data
    provider = TestDataProvider()
    provider._pull()
    with provider.override_locale(locale='und') as pr:
        assert pr.get_current_locale() == locale
    assert provider.get_current_locale() == 'und'
    with provider.override_locale(locale='ru') as pr:
        assert pr.get_current_locale() == 'ru'
   

# Generated at 2022-06-13 23:59:39.294083
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    locale = 'ru'
    locales.add_supported_locales(locale)
    provider_class = BaseDataProvider
    with provider_class.override_locale(locale):
        assert provider_class.get_current_locale() == locale
        assert provider_class.get_current_locale() == provider_class.locale ==\
                                                      locale == 'ru'
    assert provider_class.get_current_locale() == locales.DEFAULT_LOCALE == 'en'
    assert provider_class.get_current_locale() == provider_class.locale ==\
                                                  locales.DEFAULT_LOCALE == 'en'

# Generated at 2022-06-13 23:59:51.677015
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Address, Address
    from mimesis.enums import Gender
    from mimesis.typing import JSON

    address1 = Address('ru')
    with address1.override_locale('en'):
        result1 = address1.get_formatted_address()
    address2 = Address('en')
    with address2.override_locale('ru'):
        result2 = address2.get_formatted_address()

    assert isinstance(address1, BaseDataProvider)
    assert isinstance(address2, BaseDataProvider)
    assert len(result1) > 0
    assert len(result2) > 0

# Generated at 2022-06-14 00:00:01.136369
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.data_providers import Person
    from mimesis.enums import Gender
    from mimesis.enums.locales import Locales
    from mimesis.providers.base import BaseProvider

    p = Person()
    context = p.override_locale(Locales.EN)
    assert isinstance(context, BaseProvider)
    assert p.name(gender=Gender.FEMALE) == context.name(gender=Gender.FEMALE)
    assert context.get_current_locale() == Locales.EN
    assert p.locale == Locales.EN
    assert isinstance(context, BaseDataProvider)
    assert p.name(gender=Gender.MALE) == context.name(gender=Gender.MALE)

# Generated at 2022-06-14 00:00:16.744959
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    en_person = Person(locale='en')
    father = en_person.father_name(gender=Gender.MALE)
    assert father == 'Dana'
    son = en_person.son_name(gender=Gender.MALE)
    assert son == 'John'

    with en_person.override_locale('uk') as uk_person:
        father = uk_person.father_name(gender=Gender.MALE)
        assert father == 'Данило'
        son = uk_person.son_name(gender=Gender.MALE)
        assert son == 'Іван'

    father = en_person.father_name(gender=Gender.MALE)
   

# Generated at 2022-06-14 00:00:27.554214
# Unit test for method override_locale of class BaseDataProvider
def test_BaseDataProvider_override_locale():
    from mimesis.builtins import Food
    from mimesis.enums import Weekday
    from mimesis.typing import JSON

    food = Food()
    with food.override_locale('ru'):
        assert food.get_current_locale() == 'ru'
        assert food.vegetable() == 'помидоры'

    day = food.day_of_week()
    assert day == 'saturday'
    assert type(day) is str
    assert isinstance(day, Weekday)

    snacks = food.snack()
    assert isinstance(snacks, str)
    assert isinstance(food._data, JSON)

    countries = food.countries()
    assert isinstance(countries, list)
    assert isinstance(countries[0], str)

    fruits
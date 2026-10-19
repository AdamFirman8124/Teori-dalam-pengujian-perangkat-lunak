

# Generated at 2022-06-13 23:39:27.478239
# Unit test for function romanize
def test_romanize():
    assert 'abcABC123' == romanize()(lambda: 'abcABC123')
    assert 'abvGJE123' == romanize('ru')(lambda: 'абвГЙЭ123')
    assert 'abvHIE123' == romanize('uk')(lambda: 'абвГИЄ123')
    assert 'abvDYIE123' == romanize('kk')(lambda: 'абвДЫІЕ123')



# Generated at 2022-06-13 23:39:34.265219
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет, мир!') == 'Privet, mir!'
    assert romanize('uk')(lambda: 'Привіт, світ!') == 'Pryvit, svit!'
    assert romanize('kk')(lambda: 'Сәлем, дүние!') == 'Sälem, dünie!'



# Generated at 2022-06-13 23:39:39.825796
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.os import OperatingSystemSpecProvider

    os_ = OperatingSystemSpecProvider(locale=Locale.RUSSIAN)

    assert os_.operating_system() == \
        os_.operating_system().romanize(Locale.RUSSIAN)

# Generated at 2022-06-13 23:39:50.348227
# Unit test for function romanize
def test_romanize():
    # Russian locale code
    # romanized string
    rus_locale = 'ru'
    expected_result = 'vsegda progulivayu sobaku pochasche chem na polchasa'

    # Actual result
    str_local = 'transliteration'
    actual_result = str_local.romanize(rus_locale)
    assert expected_result == actual_result

    # Ukrainian locale code
    # romanized string
    ukr_locale = 'uk'
    expected_result = 'vsegda progulivaiu sobaku pochasche za polchasa'

    # Actual result
    str_local = 'transliteration'
    actual_result = str_local.romanize(ukr_locale)
    assert expected_result == actual_result

# Generated at 2022-06-13 23:40:00.921121
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda : 'Привет, мир!')() == 'Privet, mir!'
    assert romanize('uk')(lambda : 'Привіт, світ!')() == 'Pryvit, svit!'
    assert romanize('kk')(lambda : 'сәлем, дүние!')() == 'salem, dunie!'
    assert romanize('xx')(lambda : 'Привет, мир!')() == 'Привет, мир!'
    assert romanize()(lambda : 'Привет, мир!')() == 'Привет, мир!'

# Generated at 2022-06-13 23:40:05.651947
# Unit test for function romanize
def test_romanize():
    import mimesis
    r = mimesis.Personal('ru')

    @r.romanize(locale='ru')
    def romanize_func():
        return r.full_name()
    test_name = romanize_func()
    return test_name


# Generated at 2022-06-13 23:40:08.773919
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanize('ru')
    assert romanize('uk')
    assert romanize('kk')


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:40:11.933102
# Unit test for function romanize
def test_romanize():
    """Test function romanize"""
    romanized = romanize("ru")
    assert romanized is not None
    assert romanized("мы") == "my"

# Generated at 2022-06-13 23:40:16.819179
# Unit test for function romanize
def test_romanize():
    """Test for ``romanize``."""
    from mimesis.providers.utils import _romanize

    result = _romanize('Привет')
    assert result == 'Privet'



# Generated at 2022-06-13 23:40:30.429062
# Unit test for function romanize
def test_romanize():
    """Test romanize function

    Romanize should return latin alphabet string if locale is supported.
    """
    romanize_wrapper1 = romanize('ru')

    @romanize_wrapper1
    def romanize_deco1(locale):
        return 'привет Мир'

    assert romanize_deco1(locale='ru') == 'privet mir'

    romanize_wrapper2 = romanize('uk')

    @romanize_wrapper2
    def romanize_deco2(locale):
        return 'привіт Світ'

    assert romanize_deco2(locale='uk') == 'pryvit svit'

    romanize_wrapper3 = romanize('kk')


# Generated at 2022-06-13 23:40:36.425123
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:40:40.874603
# Unit test for function romanize
def test_romanize():
    assert romanize('en')(lambda: 'Тест')() == 'Tеst'
    assert romanize('ru')(lambda: 'Тест')() == 'Test'
    assert romanize('en')(lambda: 'Тест')() == 'Tеst'
    assert romanize('uk')(lambda: 'Тест')() == 'Tеst'
    assert romanize('kk')(lambda: 'Тест')() == 'Tеst'

# Generated at 2022-06-13 23:40:44.524801
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda x : 'Бандитский Петербург')('') == 'Banditskiy Peterburg'


# Generated at 2022-06-13 23:40:46.808169
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.person import Person as PersonProvider
    from ..person import Person
    from mimesis.providers.person.en import Person as PersonProvider
    provider = Person(locale='ru')
    romanized_provider = PersonProvider()
    full_name = provider.full_name
    romanized_provider.full_name

# Generated at 2022-06-13 23:40:54.182434
# Unit test for function romanize
def test_romanize():
    import random
    import unittest

    from mimesis.builtins.numbers import Numbers
    from mimesis.builtins.text import Text
    from mimesis.enums import Language

    _LANGUAGE_CODES = [
        Language.RUSSIAN.value,
        Language.UKRAINIAN.value,
        Language.KAZAKH.value,
    ]

    random.shuffle(_LANGUAGE_CODES)
    languages = _LANGUAGE_CODES[:1]

    for lang in languages:
        text_provider = Text(lang)
        number_provider = Numbers(lang)
        num = number_provider.random_int()

        for i in range(num):
            txt = text_provider.text()
            romanized = text

# Generated at 2022-06-13 23:41:04.968064
# Unit test for function romanize
def test_romanize():
    """Test romanization of some unicode characters."""

    @romanize('ru')
    def romanize_ru(symbol: str) -> str:
        return symbol

    russian = 'Форма образования представляет собой на данный момент ' \
              'потенциально самую важную задачу для страны! '


# Generated at 2022-06-13 23:41:11.117766
# Unit test for function romanize

# Generated at 2022-06-13 23:41:17.740417
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    class Test(Person):
        @romanized(locale='ru')
        def generate_full_name(self, *args, **kwargs):
            return super().full_name(*args, **kwargs)

    t = Test('ru')
    assert t.generate_full_name(gender=Gender.FEMALE) == \
        'София Альбертовна Дмитриева'
    assert t.last_name(gender=Gender.MALE) == 'Магомаев'

# Generated at 2022-06-13 23:41:19.665471
# Unit test for function romanize

# Generated at 2022-06-13 23:41:28.325987
# Unit test for function romanize
def test_romanize():
    """Test romanizer."""
    from mimesis.enums import Language
    from mimesis.providers.personal import Person

    langs = {
        Language.RUSSIAN: 'рус',
        Language.ENGLISH: 'eng',
        Language.KAZAKH: 'Қаз',
    }

    for lang, item in langs.items():
        person = Person(lang)
        name = person.full_name()
        assert name in [item, person.full_name()]
        assert len(name) == len(person.full_name())

# Generated at 2022-06-13 23:41:38.507495
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    def hello(lang: str = 'ru'):
        return lang

    romanized_hello = romanize(locale='ru')(hello)

    assert romanized_hello() == 'ru'

# Generated at 2022-06-13 23:41:40.985168
# Unit test for function romanize
def test_romanize():
    def func(locale):
        return locale
    assert romanize(locale='uk')(func)(locale='uk') == 'uk'

# Generated at 2022-06-13 23:41:47.812183
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.address import Address
    from mimesis.providers.text import Text

    t = Text(Language.RUSSIAN)
    r = Address(Language.RUSSIAN)

    assert repr(romanized('ru')(t.word)(3)) == repr(t.word(3))

    assert repr(romanized('ru')(t.word)(3)) != repr(r.address())

    assert repr(romanized('ru')(t.word)(3)) != repr(t.words(10, 5))

    assert repr(romanized('ru')(t.word)(3)) != repr(t.sentence(4))

    assert repr(romanized('ru')(t.word)(3)) != repr(t.sentences(3, 1))


# Generated at 2022-06-13 23:41:57.980844
# Unit test for function romanize
def test_romanize():
    assert romanized('kk')(lambda: 'Алтын')() == 'Altyn'
    assert romanized('ru')(lambda: 'Красная площадь')() == 'Krasnaya ploshchad'
    assert romanized('uk')(lambda: 'Привіт, Світ')() == 'Pryvit, Svit'
    # A test for the 'common letters'
    assert romanized('uk')(lambda: 'Звичайні люди')() == 'Zvychaìni liudy'



# Generated at 2022-06-13 23:42:06.494856
# Unit test for function romanize
def test_romanize():

    def test_func(*args, **kwargs):
        return 'Привет мир!'

    localized = romanized(locale='ru')(test_func)
    assert localized() == 'Privet mir!'

    localized = romanized(locale='uk')(test_func)
    assert localized() == 'Pryvit mir!'

    localized = romanized(locale='kk')(test_func)
    assert localized() == 'Привет мир!'

    localized = romanized()(test_func)
    assert localized() == 'Privet mir!'

# Generated at 2022-06-13 23:42:15.153217
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.builtins.text import Text

    @romanized(Locale.ENGLISH)
    def foo():
        t = Text()
        return t.text_rus(20)

    res = foo()
    assert len(res) == 20

# Generated at 2022-06-13 23:42:19.030623
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    """Unit test for function romanize."""
    txt = Text('de')
    txt2 = Text('de')
    assert txt.word() == txt2.word()

# Generated at 2022-06-13 23:42:29.437628
# Unit test for function romanize
def test_romanize():
    def test_romanize_locale_uk(locale=''):
        @romanize(locale)
        def ukrainian():
            return data.UKRAINIAN_LETTERS['cyrillic']
        assert ukrainian() == data.UKRAINIAN_LETTERS['latin']

    def test_romanize_locale_ru(locale=''):
        @romanize(locale)
        def russian():
            return data.RUSSIAN_LETTERS['cyrillic']
        assert russian() == data.RUSSIAN_LETTERS['latin']

    def test_romanize_locale_kk(locale=''):
        @romanize(locale)
        def kazakh():
            return data.KAZAKH_LETTERS['cyrillic']

# Generated at 2022-06-13 23:42:30.662475
# Unit test for function romanize
def test_romanize():
    """."""
    @romanize
    def foo():
        pass

    assert foo() == ''

# Generated at 2022-06-13 23:42:38.396031
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Жека и Булат')() == 'Zheka i Bulat'
    assert romanize('uk')(lambda: 'Жека и Булат')() == romanize('ru')(lambda: 'Жека и Булат')()
    assert romanize('kk')(lambda: 'Жека и Булат')() == romanize('ru')(lambda: 'Жека и Булат')()
    assert romanize('de')(lambda: 'Жека и Булат')() == 'Жека и Булат'

# Generated at 2022-06-13 23:42:50.902564
# Unit test for function romanize
def test_romanize():
    """Test to see if romanized text is returned.""" 
    assert True

# Generated at 2022-06-13 23:42:58.166434
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.data import ROMANIZATION_DICT
    from mimesis.enums import Language

    RussiaSpecProvider._validate_locale(Language.RUSSIAN)

    @romanize(locale='ru')
    def romanized_name():
        return RussiaSpecProvider.name()

    assert romanized_name() in ROMANIZATION_DICT[Language.RUSSIAN].values()

# Generated at 2022-06-13 23:42:58.950880
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:43:05.649720
# Unit test for function romanize
def test_romanize():

    @romanized('ru')
    def foo():
        return 'Привет, мир!'

    assert 'Privet, mir!' == foo()

    @romanize()
    def foo():
        return 'Привет, мир!'

    assert 'Privet, mir!' == foo()

# Generated at 2022-06-13 23:43:08.575681
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет, мир!') == 'Privet, mir!'



# Generated at 2022-06-13 23:43:11.690005
# Unit test for function romanize
def test_romanize():
    @romanize()
    def get_cyr():
        return "тест"
    assert get_cyr() == "test"



# Generated at 2022-06-13 23:43:13.998445
# Unit test for function romanize
def test_romanize():
    try:
        romanize(locale='ru')
    except UnsupportedLocale:
        assert False

# Generated at 2022-06-13 23:43:19.428323
# Unit test for function romanize
def test_romanize():
    # Test only romanized function

    def romanized_func():
        return 'Привет, друг!'

    romanized_func = romanize()(romanized_func)
    assert romanized_func() == 'Privet, drug!'


if __name__ == "__main__":
    test_romanize()

# Generated at 2022-06-13 23:43:24.817483
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider

    rsp = RussianSpecProvider()
    word = rsp.word()
    result = romanize('ru')(rsp.word)()
    assert len(result) == len(word)


# Generated at 2022-06-13 23:43:33.627305
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person

    p = Person()

    romanize_uk = romanize('uk')
    romanize_ru = romanize('ru')
    romanize_kk = romanize('kk')

    assert romanize_uk(p.first_name)
    assert romanize_ru(p.first_name)
    assert romanize_kk(p.first_name)

    try:
        assert romanize_uk(p.first_name)('no_locale')
    except UnsupportedLocale:
        pass

    assert romanized('uk')(p.first_name)

# Generated at 2022-06-13 23:43:56.207975
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text

    t = Text('ru')
    assert romanize(locale='ru')(t.cyrillic_text)
    assert romanize(locale='uk')(t.cyrillic_text)
    assert romanize(locale='kk')(t.cyrillic_text)

# Generated at 2022-06-13 23:44:05.244629
# Unit test for function romanize
def test_romanize():

    # Test romanize function
    assert romanize('ru')(lambda: 'проверка')() == 'proverka'

    # Test romanize function

# Generated at 2022-06-13 23:44:05.769240
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:44:13.218040
# Unit test for function romanize
def test_romanize():
    """Test for function romanize.
    """
    from mimesis.text import Text

    text = Text('ru')
    text.romanize = romanize('ru')(text.romanize)
    assert text.romanize('Одно из преимуществ текстов') == \
        'Odno iz preimushchestv tekstov'

# Generated at 2022-06-13 23:44:21.514349
# Unit test for function romanize
def test_romanize():
    def test(text):
        def func(x):
            return x
        @romanize()
        def func(x):
            return x + 'x'
        return func(text)
    assert test('Привет') == 'Privetx'
    assert test('Варгофф') == 'Vargoff'
    assert test('Анатолий') == 'Anatolij'
    assert test('Эверест') == 'Everest'
    assert test('Цулевальд') == 'Tsuleyval\'d'
    assert test('Шпицберген') == 'Shpitsbergen'

# Generated at 2022-06-13 23:44:25.764702
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda x: 'Привет')() == 'Privet'
    assert romanize()(lambda x: 'ПРИВЕТ')() == 'PRIVET'

# Generated at 2022-06-13 23:44:36.507949
# Unit test for function romanize
def test_romanize():
    from mimesis import Address

    with pytest.raises(UnsupportedLocale):
        Address(locale='p')

    rus = Address(locale='ru')
    assert rus.city() == rus.romanized.city()
    assert rus.country() == rus.romanized.country()

    uk = Address(locale='uk')
    assert uk.city() == uk.romanized.city()
    assert uk.country() == uk.romanized.country()

    kz = Address(locale='kk')
    assert kz.city() == kz.romanized.city()
    assert kz.country() == kz.romanized.country()

# Generated at 2022-06-13 23:44:40.851666
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    t = Text('ru')
    assert t._romanize('Test') == 'Test'
    assert t._romanize('привет') == 'privet'



# Generated at 2022-06-13 23:44:58.451358
# Unit test for function romanize
def test_romanize():
    assert romanize('uk')(lambda: 'Це є програма')() == 'Tse ye programa'
    assert romanize('ru')(lambda: 'Це є програма')() == 'Tse ye programa'
    assert romanize('kk')(lambda: 'Це є програма')() == 'Tse ye programa'

# Generated at 2022-06-13 23:45:06.946640
# Unit test for function romanize
def test_romanize():
    """Test for the function romanize."""
    from mimesis import Person, TabularData

    class RomanPerson(Person):

        @romanize('kk')
        def full_name(self) -> str:
            """Get romanized name."""
            return super().full_name()

    rp = RomanPerson('kk')
    assert 'Ospanov' in rp.full_name()

    class RomanTabular(TabularData):

        @romanize('kk')
        def value(self) -> str:
            """Get romanized value."""
            return super().value()

        @romanize('kk')
        def city(self) -> str:
            """Get romanized city."""
            return super().city()

    rt = RomanTabular('kk')
    assert 'Abaı' in rt

# Generated at 2022-06-13 23:46:11.062748
# Unit test for function romanize
def test_romanize():  # pragma: no cover
    @romanize(locale='ru')
    def ru(string: str = '') -> str:
        return string

    assert ru('Коты') == 'Koty'
    assert ru('Город') == 'Gorod'
    assert ru('Ноги') == 'Nogi'

    @romanize(locale='uk')
    def uk(string: str = '') -> str:
        return string

    assert uk('Річка') == 'Rіchka'
    assert uk('Скотина') == 'Skotyna'
    assert uk('Хлопець') == 'Khlopets'


# Generated at 2022-06-13 23:46:14.562450
# Unit test for function romanize
def test_romanize():
    assert romanized('kk')(lambda: 'байкал')() == 'baýqal'
    assert romanized('ru')(lambda: 'байкал')() == 'bajkal'
    assert romanized('uk')(lambda: 'байкал')() == 'bajkal'



# Generated at 2022-06-13 23:46:22.212133
# Unit test for function romanize
def test_romanize():
    """Test for ``romanize``."""
    from mimesis.enums import Language
    from mimesis.providers.lorem import Lorem

    l = Lorem(Language.RUSSIAN, seed=42)

    data = l.word(word_type='names')
    assert data == 'Полина'
    data = l.word(word_type='names', romanize=True)
    assert data == 'Polina'
    data = l.word(word_type='names', romanize_locale='kaz')
    assert data == 'Полина'



# Generated at 2022-06-13 23:46:27.625377
# Unit test for function romanize
def test_romanize():
    alphabet = ''.join(data.ROMANIZATION_DICT['ru'].keys())

    @romanize('ru')
    def create_text():
        return alphabet

    assert create_text() == ''.join(data.ROMANIZATION_DICT['ru'].values())



# Generated at 2022-06-13 23:46:28.460499
# Unit test for function romanize
def test_romanize():
    @romanize()
    def result():
        return 'hello'

    assert result() == 'hello'



# Generated at 2022-06-13 23:46:29.424022
# Unit test for function romanize
def test_romanize():
    assert romanize()('') == ''



# Generated at 2022-06-13 23:46:31.796869
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider as RSP
    provider = RSP(seed=1)
    assert provider.romanize() == 'fotografia'

# Generated at 2022-06-13 23:46:35.781534
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider

    russian = RussianSpecProvider(locale='ru')
    assert russian.romanized_text(pattern='dddd') == 'tovot'

# Generated at 2022-06-13 23:46:41.521899
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    @romanize()
    def cyrillic():
        """Cyrillic text."""
        return 'Привет, Мир!'

    assert cyrillic() == 'Privet, Mir!'

# Generated at 2022-06-13 23:46:49.917649
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.enums import Gender

    al = data.Address(Locale.ENGLISH)
    name = data.Name(Locale.ENGLISH, gender=Gender.FEMALE)

    # Russian
    alr = data.Address(Locale.RUSSIAN)
    namer = data.Name(Locale.RUSSIAN, gender=Gender.FEMALE)

    # Ukrainian
    alu = data.Address(Locale.UKRAINIAN)
    nameu = data.Name(Locale.UKRAINIAN, gender=Gender.FEMALE)

    # Kazakh
    alk = data.Address(Locale.KAZAKH)
    namek = data.Name(Locale.KAZAKH, gender=Gender.FEMALE)



# Generated at 2022-06-13 23:48:34.782211
# Unit test for function romanize
def test_romanize():
    import json
    import pytest

    with open('tests/testdata.json') as f:
        test_data = json.load(f)["romanize_testdata"]

    @romanize(locale='ru')
    def foo():
        return "Привет"

    @romanize(locale='kk')
    def bar():
        return "Привет"

    for i in test_data:
        if i['locale'] == 'ru':
            assert foo() == i["expected"]
        elif i['locale'] == 'kk':
            assert bar() == i["expected"]

# Generated at 2022-06-13 23:48:37.588007
# Unit test for function romanize
def test_romanize():
    """Test function romanize.
    """
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person('ja', gender=Gender.MALE)
    assert p.romanize() == p.last_name.romanize()

# Generated at 2022-06-13 23:48:45.269992
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda x: 'Привет!')(x='x') == 'Privet!'
    assert romanize(locale='ru')(lambda x: 'Привет, мир!')(x='x') == 'Privet, mir!'
    assert romanize(locale='ru')(lambda x: 'Прывiтанне!')(x='x') == 'Pryvitannie!'
    assert romanize(locale='ru')(lambda x: 'Привет!')(x='x') == 'Privet!'

# Generated at 2022-06-13 23:48:50.130273
# Unit test for function romanize
def test_romanize():
    romanize_test = romanize()(lambda: 'привет')
    assert romanize_test() == 'privet'



# Generated at 2022-06-13 23:48:58.358066
# Unit test for function romanize
def test_romanize():
    """Test that Ukrainian, Russian and Kazakh text can be romanized"""

    @romanize(locale='uk')
    def romanized_uk():
        """Generate random Ukrainian string"""
        return 'Каждому своє'

    @romanize(locale='ru')
    def romanized_ru():
        """Generate random Russian string"""
        return 'Всем привет'

    @romanize(locale='kk')
    def romanized_kk():
        """Generate random Kazakh string"""
        return 'Барлықға құрту'

    assert romanized_uk() == 'Kazhdomu svoe'
    assert romanized_ru() == 'Vsem privet'

# Generated at 2022-06-13 23:49:04.787464
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    @romanize('ru')
    def roman_words(*args, **kwargs):
        """Words to romanize."""
        return 'Государственный'

    assert roman_words() == 'Gosudarstvennyy'

# Generated at 2022-06-13 23:49:14.134228
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def to_roman(x: str) -> str:
        return x

    assert to_roman('Привет') == 'Privet'
    assert to_roman('Привет мир!') == 'Privet mir!'
    assert to_roman('Привет-мир!') == 'Privet-mir!'
    assert to_roman('Привет мир!') == 'Privet mir!'
    assert to_roman('Мама мыла раму.') == 'Mama myla ramu.'

# Generated at 2022-06-13 23:49:20.877506
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    provider = RussiaSpecProvider()
    romanized_name = provider.person.full_name()

    assert romanized_name != provider.person.full_name()


# Generated at 2022-06-13 23:39:44.989449
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text

    text = Text('ru')
    text._data = {'words': {
        'foo': 'сука-сука',
    }}

    @romanize('ru')
    def dummy_func() -> str:
        """Dummy function."""
        return text.word('foo')

    romanized_text = dummy_func()
    assert romanized_text == 'suka-suka'



# Generated at 2022-06-13 23:39:46.758922
# Unit test for function romanize
def test_romanize():
    assert romanized()('Привет Мир') == 'Privet Mir'

# Generated at 2022-06-13 23:39:51.072682
# Unit test for function romanize
def test_romanize():
    assert romanize()('навчаюся в київському харківському університеті') == 'navchyusya v kyivskomu kharkivskomu universyteti'



# Generated at 2022-06-13 23:39:52.269569
# Unit test for function romanize
def test_romanize():
    romanize('ru')

# Generated at 2022-06-13 23:40:06.892545
# Unit test for function romanize
def test_romanize():
    # romanize sample
    romanized_data = romanize('ru')
    assert romanized_data('Привет, Мир') == 'Privet, Mir'

    # romanize sample
    romanized_data = romanize('uk')
    assert romanized_data('Привіт, Світ') == 'Pryvit, Svit'

    # romanize sample
    romanized_data = romanize('kk')
    assert romanized_data('Сәлем, Дүние') == 'Sälem, Dünie'

    # romanize sample
    romanized_data = romanize('kk')

# Generated at 2022-06-13 23:40:10.080102
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_test():
        return 'Привет, мир!'

    assert romanize_test() == 'Privet, mir!'

# Generated at 2022-06-13 23:40:13.719486
# Unit test for function romanize
def test_romanize():
    text = 'Король Лев'
    txt = romanize(locale='ru')(lambda: text)()
    assert txt == 'Korol Lev'



# Generated at 2022-06-13 23:40:17.745742
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    person = Person('ru')

    assert person.romanize(person.full_name()) == 'Anatolii Kisliuk'

# Generated at 2022-06-13 23:40:23.767765
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'тест')() == 'test'
    assert romanize(locale='uk')(lambda: 'тест')() == 'test'
    assert romanize(locale='kk')(lambda: 'тест')() == 'test'

# Generated at 2022-06-13 23:40:27.979464
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    result = romanized('ru')(lambda x: 'Привет')
    assert result == 'Privet'

# Generated at 2022-06-13 23:40:47.665061
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    txt = Text('en')
    assert txt.romanize('Роботы всех стран, среднего размера, общего происхождения и прекрасных форм - соединяйтесь!') == 'Roboty vsekh stran, srednevo razmera, obshchevo proisxozhdeniya i prekrasnikh form - soedinjajtesj!'


# Generated at 2022-06-13 23:40:50.740690
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет Мир!')() == 'Privjet mir!'
    assert romanized('uk')(lambda: 'Привіт Світ!')() == 'Pryvit svit!'
    assert romanized('kk')(lambda: 'Сәлем Дүние!')() == 'Sælem Dúnie!'

# Generated at 2022-06-13 23:40:54.984342
# Unit test for function romanize
def test_romanize():
    assert 'привет мир' == romanize(locale = 'ru')(str)('привет мир')
    assert 'привіт світ' == romanize(locale = 'uk')(str)('привіт світ')
    assert 'привет свет' == romanize(locale = 'kk')(str)('привет свет')

# Generated at 2022-06-13 23:40:56.562524
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person

    p = Person()
    romanized_name = p.full_name(romanized=True)
    for letter in romanized_name:
        assert letter in ascii_letters + ' '

# Generated at 2022-06-13 23:41:02.204229
# Unit test for function romanize
def test_romanize():
    # Test for unsupported locale
    locale = 'test'
    romanize_deco = romanize(locale)

    def func(*args, **kwargs):
        return 'Привет, мир!'

    test_helper = romanize_deco(func)
    assert test_helper() == 'Privet, mir!'



# Generated at 2022-06-13 23:41:05.450182
# Unit test for function romanize
def test_romanize():
    # For example
    assert romanized('ru')(str)('Ф') == 'F'
    assert romanized('uk')(str)('Ф') == 'F'
    assert romanized('kk')(str)('Ф') == 'F'

# Generated at 2022-06-13 23:41:11.566520
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Это тест')() == 'Eto test'
    assert romanize('uk')(lambda: 'Это тест')() == 'Eto test'
    assert romanize('kk')(lambda: 'Это тест')() == 'Eto test'



# Generated at 2022-06-13 23:41:15.839709
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    rp = RussiaSpecProvider()
    assert rp.romanize('Как пройти экзамен?') == 'Kak projti ekzamen?'

# Generated at 2022-06-13 23:41:16.394632
# Unit test for function romanize
def test_romanize():
    assert True

# Generated at 2022-06-13 23:41:18.766595
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    from mimesis.builtins import RussiaSpecProvider

    ru = RussiaSpecProvider()
    assert ru.romanize(ru.name()) == ru.name()

# Generated at 2022-06-13 23:41:34.817948
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'
    assert romanize('uk')(lambda: 'Привіт')() == 'Pryvit'
    assert romanize('kk')(lambda: 'Сәлем')() == 'Sel\'em'
    assert romanize('fo')(lambda: 'Привет')() == 'Привет'

# Generated at 2022-06-13 23:41:41.500759
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.address import Address
    from unittest.mock import patch
    ad = Address(Language.RUSSIAN)
    with patch('mimesis.enums.Language.RUSSIAN', return_value='ru'):
        v = ad.address()
        assert isinstance(v, str)

# Generated at 2022-06-13 23:41:46.690251
# Unit test for function romanize
def test_romanize():
    # language is valid
    @romanized('ru')
    def get_name():
        return 'Привет, как дела?'

    name = get_name()

    assert name == 'Privet, kak dela?'

    # language is not valid
    @romanized('en')
    def get_name():
        return 'Hello, how are you?'

    name = get_name()

    assert name == 'Hello, how are you?'

# Generated at 2022-06-13 23:41:57.700068
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def roman():
        return 'Новосибирск'
    assert roman() == 'Novosibirsk'

    @romanize('uk')
    def roman():
        return 'Заднепровское'
    assert roman() == 'Zadneprovskoe'

    @romanize('kk')
    def roman():
        return 'Астана'
    assert roman() == 'Astana'

    @romanize('en')
    def roman():
        return 'Астана'
    assert roman() == ''



# Generated at 2022-06-13 23:41:59.459210
# Unit test for function romanize
def test_romanize():
    """Test case for romanize."""
    _romanize = romanize()
    assert callable(_romanize)

# Generated at 2022-06-13 23:42:07.589040
# Unit test for function romanize
def test_romanize():
    """Test for romanize decorator."""
    from mimesis.enums import Language

    @romanize(Language.UKRAINIAN)
    def _ukrainian() -> str:
        return 'дом'

    assert _ukrainian() == 'dom'

    @romanize(Language.KAZAKH)
    def _kazakh() -> str:
        return 'дом'

    assert _kazakh() == 'dom'

    @romanize(Language.POLISH)
    def _polish() -> str:
        return 'дом'

    assert _polish() == 'dom'

# Generated at 2022-06-13 23:42:08.148871
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:42:11.483416
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def test_func(locale):
        return 'сообщество'

    assert test_func('ru') == 'soobshhestvo'

# Generated at 2022-06-13 23:42:15.486819
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    spec = RussiaSpecProvider()
    assert spec._cyrillic('Иванов Иван') == 'Ivanov Ivan'

# Generated at 2022-06-13 23:42:17.727685
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda : 'Привет!')() == 'Privet!'

# Generated at 2022-06-13 23:42:32.205070
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет, Мир!')().lower() == 'privet, mir!'
    assert romanized('ru')(lambda: 'Привет, Мир!')().title() == 'Privet, Mir!'

# Generated at 2022-06-13 23:42:38.364153
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def get_name(*args, **kwargs):
        return 'Сергей'

    assert get_name() == 'Sergei'

    @romanize(locale='uk')
    def get_name(*args, **kwargs):
        return 'Сергій'

    assert get_name() == 'Serhii'

    @romanize(locale='kk')
    def get_name(*args, **kwargs):
        return 'Сергей'

    assert get_name() == 'Sergei'

# Generated at 2022-06-13 23:42:48.932741
# Unit test for function romanize
def test_romanize():
    """Test romanized decorator."""
    import pytest
    with pytest.raises(UnsupportedLocale,
                       match='UnsupportedLocale: `undefined`'):
        @romanize('undefined')
        def _(self):
            return 'Тестовый текст'

    class Test():
        @romanize('ru')
        def __init__(self):
            return 'Тестовый текст'

    assert Test().__init__() == 'Testovyy tekst'

# Generated at 2022-06-13 23:42:59.239806
# Unit test for function romanize
def test_romanize():
    """Test romanize()."""
    import string

    @romanize(locale='ru')
    def myfunc(mystring):
        """Romanize the cyrillic text."""
        return mystring

    # Test 1: Russian
    russian_cyrillic = 'Какое-такое традиционное изготовление шашек'
    russian_translit = 'Kakoye-takoye traditsionnoye izgotovleniye ' \
                       'shashek'
    assert myfunc(russian_cyrillic) == russian_translit

    # Test 2: Kazakh

# Generated at 2022-06-13 23:43:03.540261
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def _():
        return 'Привет мир'

    a = _()
    assert a == 'privet mir'



# Generated at 2022-06-13 23:43:10.351219
# Unit test for function romanize
def test_romanize():
    test_locale = 'ru'

    @romanize(test_locale)
    def romanized_txt(words):
        return ''.join([chr(i) for i in words])

    txt = romanized_txt([1100, 1108, 1077, 1096, 1103])
    assert txt == 'Привет'



# Generated at 2022-06-13 23:43:17.083066
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    @romanize('ru')
    def romanize_ru(x):
        """Romanized sample."""
        return x
    assert romanize_ru('привет, это тест') == 'privet, eto test'

# Generated at 2022-06-13 23:43:18.562475
# Unit test for function romanize
def test_romanize():
    assert romanized('ru') is not None
    assert romanized('ru') is not ''

# Generated at 2022-06-13 23:43:23.596668
# Unit test for function romanize
def test_romanize():
    @romanized('ru')
    def foo():
        return 'Привет, мир!'

    assert foo() == 'Privet, mir!'
    assert isinstance(foo, Callable)

# Generated at 2022-06-13 23:43:25.208192
# Unit test for function romanize
def test_romanize():
    assert romanize('')
    assert romanized('')


# Generated at 2022-06-13 23:43:57.601361
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers import BaseDataProvider
    from mimesis.providers.person import Person


    class MyDataProvider(BaseDataProvider):
        class Meta:
            locales = [Locale.EN, Locale.RU]

        def get_name(self):
            return self.random.choice(['Василий', 'Иван'])


    mp = MyDataProvider(locale=Locale.RU)
    person_ru = Person(locale=Locale.RU)
    person_en = Person(locale=Locale.EN)

    assert person_ru.name() == 'Василий'
    assert person_en.name() == 'Ivan'


# Generated at 2022-06-13 23:44:04.978189
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет, Мир!')() == 'Privet, Mir!'
    assert romanized('uk')(lambda: 'Привіт, Світ!')() == 'Pryvit, Svit!'
    assert romanized('kk')(lambda: 'Сәлем, Дүние!')() == 'Sälem, Dünie!'
    assert romanized('es')(lambda: 'Привет, Мир!')() == 'Привет, Мир!'

# Generated at 2022-06-13 23:44:13.470322
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет мир!')() == 'Privet mir!'
    assert romanize('uk')(lambda: 'Привіт світ!')() == 'Pryvit svit!'
    assert romanize('kk')(lambda: 'Мәліметтік мемлекеттер')() == 'Mәlimettiq memleqetter'  # noqa

# Generated at 2022-06-13 23:44:22.089871
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Processor
    import unittest

    class TestRomanize(unittest.TestCase):
        def setUp(self):
            self.processor = Processor()

        def test_romanize(self):
            word = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            word = word + word.lower()
            txt = ''.join([self.processor.text(word) for _ in range(2)])
            self.assertEqual(romanize('ru')(lambda x: txt)(self), txt)

    unittest.main()

# Generated at 2022-06-13 23:44:25.824469
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Привет')() == 'Privet'
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'

# Generated at 2022-06-13 23:44:37.192320
# Unit test for function romanize
def test_romanize():
    """Romanize."""
    from mimesis import Person, Address, Locale
    from mimesis.enums import Gender
    from mimesis.providers.currency import Currency

    # this will romanize the data from default locale
    person = Person('ru')
    assert person.full_name(gender=Gender.FEMALE) == 'Сара Шаляпина'
    assert person.full_name(gender=Gender.FEMALE,
                            romanize=True) == 'Sara Shaljapina'

    # this will romanize the data from `en` locale
    address = Address('en')
    assert address.street_name() == 'Duck Street'
    assert address.street_name(romanize=True) == 'Duck Street'

# Generated at 2022-06-13 23:44:58.524006
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Punctuation
    from mimesis.builtins import CyrillicText

    ru = CyrillicText(locale='ru')
    assert ru.romanized().lower() == ru.text().lower()

    ru = CyrillicText(locale='ru', punctuation=Punctuation.YES)
    assert ru.romanized().lower() == ru.text().lower()

    uk = CyrillicText(locale='uk')
    assert uk.romanized().lower() == uk.text().lower()

    uk = CyrillicText(locale='uk', punctuation=Punctuation.YES)
    assert uk.romanized().lower() == uk.text().lower()

    kk = CyrillicText(locale='kk')
    assert kk.romanized().lower

# Generated at 2022-06-13 23:45:02.151380
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""

    expected = "This is the roman text"

    @romanize('en-US')
    def func():
        return 'Это роман Текст'
    result = func()
    assert result == expected

# Generated at 2022-06-13 23:45:07.157688
# Unit test for function romanize
def test_romanize():
    assert romanized()(lambda: 'Привет')() == 'Privet'
    assert romanized(locale='ru')(lambda: 'Привет')() == 'Privet'
    assert romanized(locale='kk')(lambda: 'Привет')() == 'Privet'
    assert romanized(locale='uk')(lambda: 'Привет')() == 'Pryvit'

# Generated at 2022-06-13 23:45:18.373674
# Unit test for function romanize
def test_romanize():
    """Romanize test."""
    from mimesis.builtins import Enum
    from mimesis.data import (
        COMMON_LETTERS,
        COMMON_LETTERS_UK,
    )

    en = Enum('ru')
    result = en.romanized_word()
    alphabet = set(COMMON_LETTERS.values())
    assert all(i in alphabet for i in result)
    assert all(i in alphabet for i in en.romanized_text())

    en = Enum('uk')
    result = en.romanized_word()
    alphabet = set(COMMON_LETTERS_UK.values())
    assert all(i in alphabet for i in result)
    assert all(i in alphabet for i in en.romanized_text())

    en = Enum('kk')

# Generated at 2022-06-13 23:46:16.826809
# Unit test for function romanize
def test_romanize():
    """Test for ``romanize``."""
    from mimesis.enums import Language
    from mimesis.providers.person import Person
    import re

    p = Person('en')

    assert re.search(r'[А-Я]', p.full_name(), flags=re.UNICODE)
    assert not re.search(r'[А-Я]', p.romanized.full_name(), flags=re.UNICODE)

    p = Person(Language.ENGLISH)
    assert re.search(r'[А-Я]', p.full_name(), flags=re.UNICODE)
    assert not re.search(r'[А-Я]', p.romanized.full_name(), flags=re.UNICODE)

# Generated at 2022-06-13 23:46:25.249643
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda x: "Привет мир!") == "Privet mir!"
    assert romanize(locale="uk")(lambda x: "Привiт Свiт!") == "Pryvit Svit!"
    assert romanize(locale="kk")(lambda x: "Сәлем дүние!") == "Salem dünie!"
    assert romanize(locale="kk")(lambda x: "Сәлем ғасырлар!") == "Salem gasyryar!"

# Generated at 2022-06-13 23:46:28.327481
# Unit test for function romanize
def test_romanize():
    result = romanize('ru')(lambda x: 'Человек')
    assert(result=='Chelovek')

# Generated at 2022-06-13 23:46:31.796864
# Unit test for function romanize
def test_romanize():
    def ru_value():
        return 'Здравствуйте, друг'

    @romanize('ru')
    def ru_text():
        return ru_value()

    assert ru_text() == 'Zdravstvuite, drug'


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:46:37.067941
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda : 'привет')() == 'privet'
    assert romanize('uk')(lambda : 'привіт')() == 'pryvit'
    assert romanize('kk')(lambda : 'Сәлем!')() == 'Sälem!'

# Generated at 2022-06-13 23:46:47.629916
# Unit test for function romanize
def test_romanize():
    # Create instance of Mimesis
    m = Mimesis()

    # Cyrillic string can contain ascii
    # symbols, digits and punctuation.
    alphabet = {s: s for s in
                ascii_letters + digits + punctuation}
    alphabet.update({
        **data.ROMANIZATION_DICT[locale],
        **data.COMMON_LETTERS,
    })

    result = m.text()
    txt = ''.join([alphabet[i] for i in result if i in alphabet])

    assert isinstance(txt, str)
    assert len(txt) > 0

# Generated at 2022-06-13 23:46:58.020663
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda x: 'Привет мир!') == 'Privet mir!'
    assert romanize('ru')(lambda x: 'Привет мир!') == 'Privet mir!'
    try:
        romanized('fr')(lambda x: 'Привет мир!') is None
    except UnsupportedLocale:
        pass
    else:
        raise AssertionError(
            'Should raise an exception when locale is not supported.')

# Generated at 2022-06-13 23:46:59.062627
# Unit test for function romanize
def test_romanize():
    pass
test_romanize.__test__ = False

# Generated at 2022-06-13 23:47:02.624096
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda x: 'Привет!')() == 'Privet!'

# Generated at 2022-06-13 23:47:08.046532
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""

    @romanize(locale='ru')
    def romanized_txt() -> str:
        """Get romanized text."""
        return 'всё просто'

    result = romanized_txt()
    assert result == 'vsyo prosto'

# Generated at 2022-06-13 23:48:37.495379
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def rus():
        return ('Привет мир!')

    assert rus() == 'Privet mir!'

# Generated at 2022-06-13 23:48:44.412337
# Unit test for function romanize
def test_romanize():
    import mimesis.enums
    from mimesis.builtins.localization import English

    class EnglishRomanized(English):

        @data.dataproperty
        @romanize('en')
        def name(self) -> str:
            """Get a name.

            :return: Name.

            :Example:
                John, Adam.
            """
            return self.random.choice(data.NAMES_EN)

    data_provider = EnglishRomanized(mimesis.enums.Language.EN)

    text = data_provider.name()
    assert text in data.NAMES_EN

# Generated at 2022-06-13 23:48:49.569117
# Unit test for function romanize
def test_romanize():
    assert 'sovet respublikasi' == romanized('ru')('совет республикасы')
    assert 'ko' == romanized('ko')('ko')

# Generated at 2022-06-13 23:48:57.266329
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.person import Person

    ru = Person(Language.RUSSIAN)
    uk = Person(Language.UKRAINIAN)
    kk = Person(Language.KAZAKH)

    # romanization for ru language
    assert ru.full_name(romanize=True) == ru.full_name(romanize='ru')
    # romanization for uk language
    assert uk.full_name(romanize=True) == uk.full_name(romanize='uk')
    # romanization for kk language
    assert kk.full_name(romanize=True) == kk.full_name(romanize='kk')

# Generated at 2022-06-13 23:48:59.587691
# Unit test for function romanize
def test_romanize():
    @romanize()
    def roman(text):
        return text

    assert roman('привет') == 'privet'

# Generated at 2022-06-13 23:49:06.445239
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'АРБУЗ') == 'ARBUZ'
    assert romanized('uk')(lambda: 'ЦИКЛОН') == 'CYKLON'
    assert romanized('kk')(lambda: 'МЕДВЕДЬ') == 'MEDVED'

# Generated at 2022-06-13 23:49:11.544564
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo():
        return "Привет, мир!"

    assert foo() == 'Privet, mir!'

# Generated at 2022-06-13 23:49:16.825812
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет мир!')() == 'Privyet mir!'
    assert romanize('uk')(lambda: 'Привіт, світ!')() == 'Pryivyt, svit!'
    assert romanize('kk')(lambda: 'сәлем дүние!')() == 'sälem dünie!'

# Generated at 2022-06-13 23:49:20.877854
# Unit test for function romanize
def test_romanize():
    s = "кириллічний"
    assert romanize('')(s) == 'kirilličnyj'

# Generated at 2022-06-13 23:49:22.584986
# Unit test for function romanize
def test_romanize():
    assert romanize("ru")("Лорем") == "Lorem"
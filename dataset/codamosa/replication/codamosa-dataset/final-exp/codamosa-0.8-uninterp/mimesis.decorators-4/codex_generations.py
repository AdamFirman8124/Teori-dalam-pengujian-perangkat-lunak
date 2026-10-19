

# Generated at 2022-06-13 23:39:40.628728
# Unit test for function romanize
def test_romanize():
    def test_func(s):
        return s

    romanized_func = romanize(locale='uk')(test_func)
    assert romanized_func('тест') == 'test'



# Generated at 2022-06-13 23:39:43.946260
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def f():
        return 'Привет мир!'

    assert f() == 'Privet mir!'

# Generated at 2022-06-13 23:39:46.889662
# Unit test for function romanize
def test_romanize():
    @romanize()
    def romanized(s):
        return s

    assert romanized('Иванов Иван') == 'Ivanov Ivan'


# Generated at 2022-06-13 23:39:49.612336
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Привет!')() == 'Privet!'
    assert romanize()(lambda: 'Привет!')() == 'Privet!'

# Generated at 2022-06-13 23:39:54.332946
# Unit test for function romanize
def test_romanize():
    """Romanize.

    Expected TRUE or FALSE
    """
    from mimesis.providers.text import Text
    text = Text('ru')
    text1 = text.romanize(locale='ru')

    assert text1(10) is not None

# Generated at 2022-06-13 23:39:57.049972
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'

# Generated at 2022-06-13 23:40:04.056851
# Unit test for function romanize
def test_romanize():

    romanized_word = romanize(locale='ru')(lambda: 'Красный')

    assert romanized_word == 'Krasnyy'

    # KeyError: UnsupportedLocale
    try:
        _ = romanize(locale='ab')(lambda: 'Красный')
    except UnsupportedLocale:
        pass
    else:
        raise ValueError('UnsupportedLocale not raised.')

# Generated at 2022-06-13 23:40:06.431526
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian():
        return 'Россия'

    assert russian() == 'Rossiya'

# Generated at 2022-06-13 23:40:13.438295
# Unit test for function romanize
def test_romanize():
    """Test for the decorator romanize."""
    from mimesis import Person
    p = Person()
    assert p.full_name() == p.full_name(romanize=True)

    # Test for the special case
    from mimesis.enums import Gender
    name = p.name(gender=Gender.FEMALE, romanize=True)
    assert name.lower() == p.name(gender=Gender.FEMALE)



# Generated at 2022-06-13 23:40:16.469417
# Unit test for function romanize
def test_romanize():
    return romanize('ru')(lambda _: "Привет мир")()

# Generated at 2022-06-13 23:40:24.498906
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    locale = 'ru'

    def foo(locale=locale):
        return data.CYRILIC_LETTERS[locale]

    romanized_foo = romanize(locale)(foo)
    assert romanized_foo() == data.LATIN_LETTERS[locale]

# Generated at 2022-06-13 23:40:33.752844
# Unit test for function romanize
def test_romanize():
    import os
    import sys
    import unittest

    ROOT_DIR = os.path.dirname(__file__)
    sys.path.append(os.path.join(ROOT_DIR, '..'))

    from mimesis.enums import Locale
    from mimesis.providers.person import Person

    person = Person(locale=Locale.RU)

    @romanize('ru')
    def test_romanized() -> str:
        return person.full_name()

    assert test_romanized() == 'Viktor Alyoshin'

    class RomanizeTestCase(unittest.TestCase):

        def test_romanized(self):
            from mimesis.enums import Locale
            from mimesis.providers.person import Person


# Generated at 2022-06-13 23:40:40.704363
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Тестовый текст')('ru') == 'Testovyy tekst'
    assert romanize()(lambda: 'Тестовый текст')() == 'Testovyy tekst'
    assert romanize(locale='ru')(lambda: 'Тестовый текст')() == 'Testovyy tekst'
    assert romanize(locale='uk')(lambda: 'Тестовий текст')() == 'Testovyy tekst'

# Generated at 2022-06-13 23:40:50.886496
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda : 'А')() == 'A'
    assert romanized('ru')(lambda: 'Я')() == 'Ya'
    assert romanized('ru')(lambda: 'АИ')() == 'AI'
    assert romanized('ru')(lambda: 'Экспоненциальное развитие')() == 'Eksponentsialnoe razvitie'

# Generated at 2022-06-13 23:41:02.398652
# Unit test for function romanize
def test_romanize():
    assert romanize()(
        'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя'
    ) == 'AaBbVvHhGgDdEeYeYeZhZzYiIiYiYyKkLlMmNnOoPpRrSsTtUuFfXhXxPsChShSh``YuYuYaYa'




# Generated at 2022-06-13 23:41:10.168680
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: "А Б В Г Д Е ж з и Й к л М н о П р с т У ф х ц ч ш ъ ы ь э ю я")() == "A B V G D E zh z i J k l M n o P r s t U f kh ts ch sh '' y' e yu ya"

# Generated at 2022-06-13 23:41:19.827752
# Unit test for function romanize
def test_romanize():
    assert romanized(locale='ru')(lambda: 'Мама мыла раму')() == 'Mama myla ramu'
    assert romanized(locale='uk')(lambda: 'Мама мила раму')() == 'Mama myla ramu'
    assert romanized(locale='kk')(lambda: 'Мама мыла раму')() == 'Mama myla ramu'
    assert romanized(locale='kk')(lambda: 'Мама мила раму')() == 'Mama myla ramu'

# Generated at 2022-06-13 23:41:21.399788
# Unit test for function romanize
def test_romanize():
    assert romanize
    assert romanized
    assert romanized()
    assert romanized()(print)

# Generated at 2022-06-13 23:41:25.976518
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.internet import Internet

    for lang in [Language.RU, Language.UK, Language.KK]:
        internet = Internet(locale=lang)
        assert internet.domain_name()

# Generated at 2022-06-13 23:41:36.567738
# Unit test for function romanize
def test_romanize():
    import string

    romanize = romanized('ru')

    @romanize
    def text_generator(pattern='') -> str:
        return pattern

    assert text_generator(pattern='Переделать тест') == 'Peredelat test'

    assert text_generator(pattern='Переделать тест') == 'Peredelat test'
    assert text_generator(pattern='Привет, мир!') == 'Privet, mir!'
    assert text_generator(pattern='Язык Python.') == 'Yazyk Python.'
    assert text_generator(pattern='Москва') == 'Moskva'


# Generated at 2022-06-13 23:41:48.233479
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.person import Person

    def test_romanize(lang: Language):
        person = Person(lang)
        person.romanize = romanize(lang)
        ru = person.romanize('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
        en = person.romanize('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        ru_en = ru + en

# Generated at 2022-06-13 23:41:52.382142
# Unit test for function romanize
def test_romanize():
    romanizeString = data.ROMANIZATION_DICT['ru']
    for key in romanizeString.keys():
        assert romanize()(key) == romanizeString[key]

# Generated at 2022-06-13 23:42:00.533724
# Unit test for function romanize
def test_romanize():
    @romanize()
    def r(text):
        return text

    text1 = 'Привет, мир!'
    text2 = 'Привіт, світ!'
    text3 = 'Шаламен, мир!'

    assert text1 != text2
    assert text1 == r(text1)
    assert text2 == r(text2)
    assert text3 == r(text3)
    assert text1 != r(text2)
    assert text2 != r(text1)
    assert text3 != r(text1)

# Generated at 2022-06-13 23:42:06.162669
# Unit test for function romanize
def test_romanize():
    locale = 'uk'
    romanize_uk = romanize(locale)
    assert romanize_uk

    @romanize_uk
    def gimme_txt(length: int = 5) -> str:
        return 'Привіт мир'

    assert gimme_txt(12) == 'Pryvit mir'

if __name__ == "__main__":
    test_romanize()

# Generated at 2022-06-13 23:42:13.480065
# Unit test for function romanize
def test_romanize():
    key = 'test'
    # 'Тест' in Russian
    expected_value = 'tst'
    value = romanize('ru')(lambda x: x)(key)
    assert value == expected_value

    # 'Тест' in Ukrainian
    expected_value = 'tst'
    value = romanize('uk')(lambda x: x)(key)
    assert value == expected_value

    # 'Тест' in Kazakh
    expected_value = 'tst'
    value = romanize('kk')(lambda x: x)(key)
    assert value == expected_value

# Generated at 2022-06-13 23:42:16.140529
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    assert RussiaSpecProvider().full_name() == \
        RussiaSpecProvider().full_name(romanize=True)



# Generated at 2022-06-13 23:42:25.631454
# Unit test for function romanize
def test_romanize():
    """Tests for romanize."""
    assert romanize('ru')(lambda: 'Данные')() == 'Dannye'
    assert romanize('ru')(lambda: 'Пограничная охрана')() == 'Pogranichnaya okhrana'
    assert romanize('uk')(lambda: 'Служба безпеки України')() == 'Sluzhba bezpeky Ukrayiny'
    assert romanize('kk')(lambda: 'Қазақстан')() == 'Kazakstan'

# Generated at 2022-06-13 23:42:31.407898
# Unit test for function romanize
def test_romanize():
    import string

    @romanize()
    def romanized_text():
        text = string.ascii_letters + string.digits
        return text

    assert romanized_text() == 'abcdefghijklmnopqrstuvwxyz' \
                               'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                               '0123456789'

# Generated at 2022-06-13 23:42:33.237646
# Unit test for function romanize
def test_romanize():
    value = romanize()(lambda *args, **kwargs: 'e')()
    assert value == 'e'

# Generated at 2022-06-13 23:42:37.041185
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person

    p = Person()
    r_name = p.full_name('ru')
    romanize_name = romanize('ru')

    assert romanize_name(r_name) == 'Vasiliy Zolotov'

# Generated at 2022-06-13 23:42:57.076511
# Unit test for function romanize
def test_romanize():
    @romanize(locale='RU')
    def romanize_ru(*args, **kwargs):
        return 'Великий Константинопольский собор, Вселенский Синод'

    result = romanize_ru(locale='RU')
    assert result == 'Velikyj Konstantinopolʹskij sobor, Vselenskij sinod'

# Generated at 2022-06-13 23:43:09.296889
# Unit test for function romanize
def test_romanize():
    """Unit test for romanize."""
    def test_ru():
        @romanized('ru')
        def get_name():
            return 'Андрей'

        assert get_name() == 'Andrej'

    def test_uk():
        @romanized('uk')
        def get_name():
            return 'Андрій'

        assert get_name() == 'Andriy'

    def test_kk():
        @romanized('kk')
        def get_name():
            return 'Әндер'

        assert get_name() == 'Ánder'

    test_ru()
    test_uk()
    test_kk()

# Generated at 2022-06-13 23:43:12.398144
# Unit test for function romanize
def test_romanize():
    result = romanize('de')(lambda: 'привет')
    assert result == 'priwet'

# Generated at 2022-06-13 23:43:18.297853
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Тест')() == 'Test'
    assert romanize(locale='kk')(lambda: 'Тест')() == 'Test'
    assert romanize(locale='uk')(lambda: 'Тест')() == 'Test'

# Generated at 2022-06-13 23:43:31.304697
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Это русский текст')() == 'Это russskii tekst'
    assert romanize(locale='uk')(lambda: 'Це український текст')() == 'Ce ukraїns′kii tekst'
    assert romanize(locale='kk')(lambda: 'Бұл қазақ тексті')() == 'Bul qazaq teksti'

# Generated at 2022-06-13 23:43:36.064683
# Unit test for function romanize
def test_romanize():
    from random import random
    from mimesis import Person

    p = Person('ru')
    name = p.full_name()

    @romanize()
    def r():
        return name

    assert isinstance(r, str)
    assert len(r) > 0
    assert r.startswith(name[0].upper())



# Generated at 2022-06-13 23:43:38.575102
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Иванов Иван Иванович') == 'Ivanov Ivan Ivanovich'

# Generated at 2022-06-13 23:43:40.736010
# Unit test for function romanize
def test_romanize():
    assert romanized()('Весна приходит рано') == 'Vesna prikhodit rano'

# Generated at 2022-06-13 23:43:49.931884
# Unit test for function romanize
def test_romanize():
    result = romanize(locale='ru')(lambda: 'привет')
    assert result == 'privet'

    result = romanize(locale='en')(lambda: 'привет')
    assert result == 'privet'

    result = romanize(locale='uk')(lambda: 'привет')
    assert result == 'privet'

    result = romanize(locale='kk')(lambda: 'привет')
    assert result == 'privet'



# Generated at 2022-06-13 23:44:01.533009
# Unit test for function romanize

# Generated at 2022-06-13 23:44:31.385598
# Unit test for function romanize
def test_romanize():
    # Initialization
    from mimesis import Person

    p = Person()
    p.set_locale('ru')

    assert p.full_name() == 'Григорий Александр Пахомов'
    assert p.full_name(romanize=True) == 'Grigoriy Aleksandr Pakhomov'

# Generated at 2022-06-13 23:44:35.600621
# Unit test for function romanize
def test_romanize():
    @romanize(locale='uk')
    def get_ukrainian():
        return 'Добрий день, вітаю вас.'

    assert get_ukrainian() == 'Dobryy den, vitayu vas.'



# Generated at 2022-06-13 23:44:58.521754
# Unit test for function romanize
def test_romanize():
    import pytest
    from mimesis.enums import Locale

    romanizer = romanize(locale=Locale.RUSSIAN)
    romanize_deco = romanizer(romanize(locale=Locale.RUSSIAN))

    with pytest.raises(UnsupportedLocale):
        romanize(locale='foo')

    with pytest.raises(UnsupportedLocale):
        romanized(locale='foo')

    assert romanize_deco.__name__ == 'romanize'
    assert romanize_deco.__doc__ == romanize.__doc__
    assert romanize_deco(lambda: 'Юникод')() == 'Yunikod'

# Generated at 2022-06-13 23:45:03.615702
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanized_func(value):
        return value

    assert romanized_func('АБВГД') == 'ABVGD'



# Generated at 2022-06-13 23:45:04.279463
# Unit test for function romanize
def test_romanize():
    assert type(romanize(""))

# Generated at 2022-06-13 23:45:08.451091
# Unit test for function romanize
def test_romanize():
    assert romanized(locale='ru')(lambda: 'Петя')() == 'Petya'
    assert romanized(locale='uk')(lambda: 'Петя')() == 'Petia'
    assert romanized(locale='kk')(lambda: 'Петя')() == 'Peta'



# Generated at 2022-06-13 23:45:12.852266
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.person import Person

    person = Person('ru')
    name = person.full_name()
    expected = 'Ivan Ivanov'

    assert romanize(Language.RUSSIAN)(lambda: name)() == expected

# Generated at 2022-06-13 23:45:17.042396
# Unit test for function romanize
def test_romanize():
    @romanize('uk')
    def _(self):
        return self.random.choice(['Іван', 'Петро', 'Марія'])

    assert _(self='zh') == 'Ivan'

# Generated at 2022-06-13 23:45:21.826920
# Unit test for function romanize
def test_romanize():
    romanized_text = romanize('ru')(lambda: 'Привет, Мир!')
    assert romanized_text() == 'Privet, Mir!'

# Generated at 2022-06-13 23:45:35.233881
# Unit test for function romanize
def test_romanize():
    from collections import Counter

    @romanize(locale='ru')
    def russian(pattern=None):
        return data.RUSSIAN.get_cyrillic_letters(pattern)

    @romanize(locale='kk')
    def kazakh(pattern=None):
        return data.KAZAKH.get_cyrillic_letters(pattern)

    @romanize(locale='uk')
    def ukrainian(pattern=None):
        return data.UKRAINIAN.get_cyrillic_letters(pattern)

    # Count occurrences of letters
    cnt_ru = Counter(russian(pattern='фцдф').lower())
    cnt_uk = Counter(ukrainian(pattern='бщб').lower())

# Generated at 2022-06-13 23:46:33.280862
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    TEXT = 'здравствуй, мир'
    EXPECTED = 'zdrastvuy, mir'
    FUNC = romanize(locale='ru')

    @FUNC
    def hello_world():
        return TEXT

    assert hello_world() == EXPECTED

# Generated at 2022-06-13 23:46:38.943049
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Российская Федерация')() == \
        'Rossijskaya Federatsiya'

    assert romanize(locale='uk')(lambda: 'Україна')() == 'Ukraїna'

    assert romanize(locale='kk')(lambda: 'Қазақстан')() == 'Qazaqstan'

# Generated at 2022-06-13 23:46:45.793388
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Русский')() == 'Russkiy'
    assert romanize('uk')(lambda: 'українська')() == 'ukrayinska'
    assert romanize('kk')(lambda: 'қазақша')() == 'qazaqsha'

# Generated at 2022-06-13 23:46:58.018557
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')() == 'ABVGDEYŽZIYKIIMNOPRSTUFIKČČŠŠYIYEEYUYA'

test_romanize()

# Generated at 2022-06-13 23:46:59.417454
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanized()

# Generated at 2022-06-13 23:47:10.539280
# Unit test for function romanize
def test_romanize():
    # Sample text with cyrillic and ascii letters.
    text = 'У тебя чичира на сухаре?'
    # Function, that should add romanization for all cyrillic letters
    # to the original text.
    @romanize(locale='ru')
    def foo():
        return text
    # Function that shouldn't change the original text.
    @romanize(locale='en')
    def bar():
        return text

    results = [foo(), bar()]
    expected = ['U tebya chichira na suhare?', text]

    assert results == expected

# Generated at 2022-06-13 23:47:18.578640
# Unit test for function romanize
def test_romanize():
    import random

    chars = ''.join(data.ROMANIZATION_DICT['ru'].keys())
    chars += ''.join(data.COMMON_LETTERS.keys())
    chars += ''.join(data.COMMON_LETTERS_RU.keys())

    @romanize('ru')
    def foo(i: int) -> str:
        return ''.join(random.sample(chars, i))

    res = foo(10)
    assert isinstance(res, str)


# Case-insensitive alias

# Generated at 2022-06-13 23:47:22.986463
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Привет')() == 'Privet'
    assert romanize('uk')(lambda: 'Привіт')() == 'Pryvit'
    assert romanize('kk')(lambda: 'Сәлем')() == 'Sälem'

# Generated at 2022-06-13 23:47:25.584947
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def get_name():
        return 'Филиппов'

    assert get_name() == 'Filippov'

# Generated at 2022-06-13 23:47:26.515767
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')

# Generated at 2022-06-13 23:48:59.025684
# Unit test for function romanize
def test_romanize():
    assert 'Тест' == romanize('ru')(lambda: 'Тест')

# Generated at 2022-06-13 23:48:59.746099
# Unit test for function romanize
def test_romanize():
    assert romanized(locale='ru')

# Generated at 2022-06-13 23:49:03.462255
# Unit test for function romanize
def test_romanize():
    assert romanize
    assert romanized


# Generated at 2022-06-13 23:49:09.178717
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider

    ru = RussianSpecProvider(locale='ru')
    assert ru.romanize('Привет') == 'Privyet'
    assert ru.romanize('Привет, как дела?') == 'Privyet, kak dela?'
    assert ru.romanize('Привет!Как дела?') == 'Privyet!Kak dela?'
    assert ru.romanize('Когда твои глаза видят сны') ==\
        'Kogda tvoyi glaza vidyat sny'

# Generated at 2022-06-13 23:49:14.111237
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def get_romanized_string():
        return 'тестовая строка'

    assert get_romanized_string() == 'testovaya stroka'

# Generated at 2022-06-13 23:49:18.686644
# Unit test for function romanize
def test_romanize():
    result = romanize('ru')(lambda: 'Вася Пупкин')()
    assert result == 'Vasya Pupkin'

# Generated at 2022-06-13 23:49:29.655742
# Unit test for function romanize
def test_romanize():

    @romanize('ru')
    def generate_ru_text():
        return 'Привіт, як справи?'

    assert generate_ru_text() == 'Pryvit, yak spravy?'

    @romanize('uk')
    def generate_uk_text():
        return 'Привіт, як справи?'

    assert generate_uk_text() == 'Pryvit, yak spravy?'

    @romanize('kk')
    def generate_kk_text():
        return 'Сәлем, қалайсың?'

    assert generate_kk_text() == 'Salem, qalaısıñ?'


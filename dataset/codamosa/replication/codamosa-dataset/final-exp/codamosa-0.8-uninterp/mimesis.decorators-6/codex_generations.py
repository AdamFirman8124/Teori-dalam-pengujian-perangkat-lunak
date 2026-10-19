

# Generated at 2022-06-13 23:39:40.517215
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет, Мир')().split() == ['Privet', 'Mir']

# Generated at 2022-06-13 23:39:50.773679
# Unit test for function romanize
def test_romanize():
    str1 = 'Мама мыла раму'
    str2 = 'Баба мила Раму'
    str3 = 'Жена мила раму'
    str4 = 'Саша мила раму'

    from mimesis.providers import Person

    person = Person('ru')

    str1_romanized = person._romanize(str1)
    assert str1_romanized == 'Mama mïla ramu'

    str2_romanized = person._romanize(str2)
    assert str2_romanized == 'Baba mila Ramu'

    str3_romanized = person._romanize(str3)
    assert str3_romanized

# Generated at 2022-06-13 23:40:01.138370
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider
    from mimesis.enums import Gender

    r = RussianSpecProvider(
        locale='ru',
        gender=Gender.FEMALE,
    )

    assert romanize('ru')(r.full_name)() == 'Anna Nikolaevna Hlebutina'
    assert romanize('uk')(r.full_name)() == 'Anna Mykolayivna Hlebutina'
    assert romanize('kk')(r.full_name)() == 'Анна Николаевна Глебутина'

    r = RussianSpecProvider(
        locale='uk',
    )

# Generated at 2022-06-13 23:40:02.316708
# Unit test for function romanize
def test_romanize():
    # TODO: Add test
    pass

# Generated at 2022-06-13 23:40:06.091011
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_ru():
        return 'пример'

    assert romanize_ru() == 'primer'

# Generated at 2022-06-13 23:40:16.042075
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person

    person_ru = Person('ru')
    person_ru.romanize = romanize('ru')(person_ru.romanize)

    person_uk = Person('uk')
    person_uk.romanize = romanize('uk')(person_uk.romanize)

    person_kk = Person('kk')
    person_kk.romanize = romanize('kk')(person_kk.romanize)

    assert person_ru.romanize() == 'Ivanov Ivan Ivanovich'
    assert person_uk.romanize() == 'Петруха Петр Петрович'
    assert person_kk.romanize() == 'Неміс Неміс'

# Generated at 2022-06-13 23:40:17.932522
# Unit test for function romanize
def test_romanize():
    assert romanized == romanize



# Generated at 2022-06-13 23:40:21.558696
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def text():
        return 'Привет, мир!'

    assert text() == 'Privet, mir!'

# Generated at 2022-06-13 23:40:28.999126
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Как дела?')() == 'Kak dela?'
    assert romanize('uk')(lambda: 'Як справи?')() == 'Yak spravy?'
    assert romanize('kk')(lambda: 'Көкө қалдыңыз ба?')() == 'Kökö qaldıñız ba?'

# Generated at 2022-06-13 23:40:37.494041
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""
    from mimesis.enums import Locale
    from mimesis.builtins import RussianSpecProvider as rus
    from mimesis.builtins import UkrainianSpecProvider as ukr
    from mimesis.builtins import KazakhSpecProvider as kaz

    def __test_for_locales(locale):
        romanized_text = romanized(locale)(rus().person.full_name)()
        assert romanized_text.isascii()
        assert not romanized_text.isalpha()
        assert romanized_text

    __test_for_locales(Locale.RU)
    __test_for_locales(Locale.UK)
    __test_for_locales(Locale.KK)

# Generated at 2022-06-13 23:40:45.437793
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='kk')(lambda x: 'А қазақ тілі')() == 'A qazaq tili'

# Generated at 2022-06-13 23:40:48.969466
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def run_romanize(locale='ru'):
        return 'Привет...'

    assert run_romanize() == 'Privet...'

# Generated at 2022-06-13 23:40:54.782837
# Unit test for function romanize
def test_romanize():
    import random

    # Test for Ukrainian
    @romanize('uk')
    def romanize_uk():
        return 'Щастя на табі прибула!'

    assert romanize_uk() == 'Schastya na tabi prybula!'

    # Test for Russian
    @romanize('ru')
    def romanize_ru():
        return 'Счастье на столе прибыло!'

    assert romanize_ru() == 'Schastie na stole pribylo!'

    # Test for Kazakh

# Generated at 2022-06-13 23:40:57.335746
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'юнит-тест')() == 'yunit-test'

# Generated at 2022-06-13 23:41:00.424706
# Unit test for function romanize
def test_romanize():
    romanize_func = romanize('ru')
    assert romanize_func(lambda x: 'йцукен') == 'jctukeh'

# Generated at 2022-06-13 23:41:02.695528
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    t = Text('ru')
    assert t.romanize() == t.text()

# Generated at 2022-06-13 23:41:06.135671
# Unit test for function romanize
def test_romanize():
    # Can't test with locale, so use Russian locale
    test_str = 'Привет, мир'

    @romanize('ru')
    def test_func(a):
        return a

    assert test_func(test_str) == 'Privet, mir'



# Generated at 2022-06-13 23:41:17.905665
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.person import Person
    from mimesis.providers.address import Address

    en_person = Person(locale=Locale.ENGLISH)
    ru_person = Person(locale=Locale.RUSSIAN)
    ua_address = Address(locale=Locale.UKRAINIAN)
    kk_address = Address(locale=Locale.KAZAKH)

    # Test for locale ru
    assert ru_person.romanize() == ru_person.full_name()
    assert ru_person.romanize() != ru_person.full_name(gender=None)

    # Test for locale ua

# Generated at 2022-06-13 23:41:21.549902
# Unit test for function romanize
def test_romanize():
    from mimesis.schema import Field

    @romanize('uk')
    def _():
        return Field('person.full_name').create()

    assert _().isalpha()

# Generated at 2022-06-13 23:41:25.334104
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins.numbers as num
    assert num.integers.to_roman_numeral(456) == 'CDLVI'

# Generated at 2022-06-13 23:41:41.661484
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def something():
        return 'Привет, Мир!'
    assert something() == 'Privet, Mir!'

    @romanized('ru')
    def something():
        return 'Привет, Мир!'
    assert something() == 'Privet, Mir!'

# Generated at 2022-06-13 23:41:43.377921
# Unit test for function romanize
def test_romanize():
    assert romanized(locale='ru')(lambda: 'АБВГД')() == 'ABVGD'

# Generated at 2022-06-13 23:41:45.533345
# Unit test for function romanize
def test_romanize():
    a = romanized("ru")(lambda: "Сеньор Тормес")
    assert "Sen'or Tormes" == a

# Generated at 2022-06-13 23:41:46.033243
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:41:56.241335
# Unit test for function romanize
def test_romanize():
    """Test for the romanize."""
    romanized_result = romanize('ru')(lambda: 'Мимезис')
    assert romanized_result == 'Mimezis'
    romanized_result = romanize('kk')(lambda: 'Қызылорда')
    assert romanized_result == 'Qızılorda'
    romanized_result = romanize('uk')(lambda: 'Суми')
    assert romanized_result == 'Sumy'



# Generated at 2022-06-13 23:42:07.636754
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person
    from typing import List, Tuple
    from functools import reduce

    p = Person('ru')
    surname = p.surname(patronymic=True)
    name = p.name()

    assert romanized(p.surname())(p.surname)() == romanized(p.surname)()

    assert romanized(p.surname)() == romanize(p.surname)()

    assert p.surname(patronymic=True) == 'Некрасова'


# Generated at 2022-06-13 23:42:10.705580
# Unit test for function romanize
def test_romanize():
    b = romanize('ru')
    def test_func():
        return 'привет'
    assert b(test_func)() == 'privet'


# Generated at 2022-06-13 23:42:17.658907
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider

    @romanize(locale='ru')
    def text(self):
        return self.word(4, 10)

    russian_text = text(RussianSpecProvider())
    assert isinstance(russian_text, str)
    assert len(russian_text) > 10
    assert russian_text.isalpha()


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:42:27.983529
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider
    provider = RussiaSpecProvider
    rus = provider('ru')
    rus_romanized = romanize('ru')(provider)('ru')

    assert rus.code() == 'RU'
    assert rus_romanized.code() == 'RU'

    assert rus.preferences_name() == 'русский язык'
    assert rus_romanized.preferences_name() == 'russkij jazyk'

    assert rus.name() == 'Российская Федерация'
    assert rus_romanized.name() == 'Rossijskaja Federacija'


# Generated at 2022-06-13 23:42:36.559506
# Unit test for function romanize
def test_romanize():

    @romanize(locale='ru')
    def ru_str() -> str:
        return 'Россия'

    assert ru_str() == 'Rossiya'

    @romanize(locale='uk')
    def uk_str() -> str:
        return 'Україна'

    assert uk_str() == 'Ukrayina'

    @romanize(locale='kk')
    def kk_str() -> str:
        return 'Қазақстан'

    assert kk_str() == 'Qazaqstan'

    @romanize(locale='en')
    def fr_str() -> str:
        return 'France'

    assert fr_str() == 'France'

# Generated at 2022-06-13 23:43:04.035381
# Unit test for function romanize
def test_romanize():
    assert romanized('ru') is not None
    assert romanized('ru') is not None
    assert romanized('ru') is not None
    assert romanized('ru') is not None
    assert romanized('ru') is not None
    assert romanized('ru') is not None

# Generated at 2022-06-13 23:43:11.962757
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.datetime import Datetime
    assert Datetime().datetime(locale=Locale.RU, romanize=False) == "2019-07-04T17:29:11.799340"
    assert Datetime().datetime(locale=Locale.RU, romanize=True) == "2019-07-04T17:29:11.799340"

# Generated at 2022-06-13 23:43:13.585721
# Unit test for function romanize
def test_romanize():
    assert romanize()('Абвгд') == 'Abvgdy'

# Generated at 2022-06-13 23:43:17.417446
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def get_name():
        return 'Петр'

    assert get_name() == 'Petra'



# Generated at 2022-06-13 23:43:20.229479
# Unit test for function romanize
def test_romanize():
    @romanized()
    def romanize(text: str = '') -> str:
        return text

    assert romanize(text='Очень большой текст.') == 'Ochen bolshoy tekst.'

# Generated at 2022-06-13 23:43:31.558350
# Unit test for function romanize
def test_romanize():
    """
    Unit test for function romanize
    """
    @romanize(locale='ru')
    def ru(locale='ru'):  # type: ignore
        return 'Здравствуй, Мир! Как дела?'

    # test russian romanization
    assert ru() == 'Zdravstvuy, Mir! Kak dela?'
    # test english romanization
    @functools.wraps(ru)
    def en(locale='en'):
        return ru(locale='en')

    assert en() == 'Zdravstvuy, Mir! Kak dela?'


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:43:33.379294
# Unit test for function romanize
def test_romanize():
    """Test romanized decorator.

    :return: None
    """
    assert romanize()

# Generated at 2022-06-13 23:43:35.628800
# Unit test for function romanize
def test_romanize():
    @romanized()
    def r():
        return 'яблоко'

    assert r() == 'yabloko'

# Generated at 2022-06-13 23:43:37.939211
# Unit test for function romanize
def test_romanize():
    assert romanized() == romanize()
if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:43:44.587472
# Unit test for function romanize
def test_romanize():
    import os
    import sys
    from mimesis import Person

    @romanize()
    def get_name():
        return Person().full_name()
    assert get_name() != Person().full_name()

    @romanize('ru')
    def get_name():
        return Person().full_name()
    assert get_name() != Person().full_name()

    # test for "uk" locale
    sys.path.append(
        os.path.join(os.path.dirname(__file__), '../mimesis/locales'))
    from uk import personal

    p = Person(locale='uk', seed=1)
    result = p.full_name()
    assert result == 'Братень Борис'

# Generated at 2022-06-13 23:44:31.732453
# Unit test for function romanize
def test_romanize():
    """Test for romanization."""
    assert romanized(locale='ru')(lambda: 'Привет, мир!')() == 'Privet, mir!'

# Generated at 2022-06-13 23:44:35.781244
# Unit test for function romanize
def test_romanize():
    from random import choice
    from string import ascii_letters, digits, punctuation

    alphabet = list(data.ROMANIZATION_DICT['ru'].values()) + list(ascii_letters + digits + punctuation)
    assert romanize('ru')(lambda: choice(alphabet)) in alphabet

# Generated at 2022-06-13 23:44:37.583191
# Unit test for function romanize
def test_romanize():
    # TODO(roman_zen): Add test!
    pass

# Generated at 2022-06-13 23:44:41.844289
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""
    @romanize(locale='ru')
    def romanized_func(text):
        return text

    assert romanized_func('привет') == 'privet'

# Generated at 2022-06-13 23:44:58.521657
# Unit test for function romanize
def test_romanize():
    import random

    le = list(ascii_letters)
    le.extend(list(range(0,11)))

    import random
    class Foo:
        def __init__(self):
            self.locale = "ru"

        @romanize()
        def romanize(self, text: str) -> str:
            return text
    g = Foo()
    text = ''.join(str(random.choice(le)) for _ in range(10))
    txt = g.romanize(text)
    text.replace("1", "1")
    print(text)
    print(txt)
    assert type(txt) == type(str())
    text.replace("1", "1")
    txt.replace("1", "1")
    assert text == txt

# Generated at 2022-06-13 23:45:01.896745
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')('foo')('bar') == 'bar'
    assert romanize('ru')('русский язык') == 'russkiy yazik'

# Generated at 2022-06-13 23:45:03.326374
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanized()
    assert romanize.__doc__ and romanized.__doc__



# Generated at 2022-06-13 23:45:10.355769
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def text() -> str:
        return 'Строка в кириллице'

    assert text() == 'Stroka v kirillice'
    assert text() == 'Stroka v kirillice'

    @romanize(locale='uk')
    def text() -> str:
        return 'Рядок в кирилиці'

    assert text() == 'Ryadok v kirillitsi'
    assert text() == 'Ryadok v kirillitsi'

# Generated at 2022-06-13 23:45:14.595009
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Назовите ваше имя') == 'Nazovite vashe imya'

# Generated at 2022-06-13 23:45:15.475084
# Unit test for function romanize
def test_romanize():
    ...

# Generated at 2022-06-13 23:47:08.210592
# Unit test for function romanize
def test_romanize():
    import string, random
    import pytest

    # Randomly generate a string
    str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    @romanize()
    def romanize_func(str):
        return str

    assert romanize_func(str) == str

# Generated at 2022-06-13 23:47:13.705511
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    class User(RussiaSpecProvider):

        @romanize('ru')
        def username(self):
            return self.name(gender='male')

        @romanize('ru')
        def userlogin(self, token: str = '') -> str:
            return (self.username() + self.random_element(token)).lower()

    usr = User('ru')
    assert type(usr.username()) is str
    assert type(usr.userlogin()) is str

# Generated at 2022-06-13 23:47:17.014637
# Unit test for function romanize
def test_romanize():
    def romanize_with_deco(text: str) -> str:
        return text

    romanize_with_deco = romanize('ru')(romanize_with_deco)
    assert romanize_with_deco('АБВ') == 'ABV'

# Generated at 2022-06-13 23:47:20.322974
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanize('ru')
    assert romanize('uk')
    assert romanize('kk')
    assert romanized()
    assert romanized('ru')
    assert romanized('uk')
    assert romanized('kk')

# Generated at 2022-06-13 23:47:27.635472
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian_alphabet():
        return 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'

    russian_alphabet() == 'A B V G D E Yo Zh Z I Y K L M N O P R S T U F H ' \
                          'Ts Ch Sh Shch " Y ` E Yu Ya'

# Generated at 2022-06-13 23:47:34.132433
# Unit test for function romanize
def test_romanize():
    data = ['Привіт, світ!', 'Привет, мир!']
    expected = ['Pryvit, svit!', 'Privet, mir!']
    assert romanize()(lambda: data[0])().__eq__(expected[0])
    assert romanize()(lambda: data[1])().__eq__(expected[1])

# Generated at 2022-06-13 23:47:41.357937
# Unit test for function romanize
def test_romanize():
    try:
        import pytest
    except Exception:
        return

    @romanize('ru')
    def romanized_ru():
        return 'Русский'

    @romanize('uk')
    def romanized_uk():
        return 'Українська'

    @romanize('kk')
    def romanized_kk():
        return 'Қазақша'

    @romanize('es')
    def romanized_es():
        return 'Español'

    assert romanized_ru() == 'Russkiy'
    assert romanized_uk() == 'Ukraїnsʹka'
    assert romanized_kk() == 'Qazaqşa'


# Generated at 2022-06-13 23:47:44.687078
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def test_func():
        return "Привет мир!"

    result = test_func()
    assert result == 'Privet mir!'



# Generated at 2022-06-13 23:47:53.407990
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins as builtins
    b = builtins.CustomText(eng=True)
    assert b.__class__.__name__ == 'CustomText'
    assert b.romanize('ru')('привет мир!') == 'privet mir!'
    assert b.romanize('uk')('привіт світ!') == 'privit svit!'
    assert b.romanize('kk')('сәлем, дүние!') == 'salem, dünie!'

# Generated at 2022-06-13 23:47:56.412042
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Это функция')() == 'Eto funkciya'
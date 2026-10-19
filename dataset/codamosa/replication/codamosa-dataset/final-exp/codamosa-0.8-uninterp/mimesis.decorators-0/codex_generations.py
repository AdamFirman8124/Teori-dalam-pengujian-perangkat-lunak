

# Generated at 2022-06-13 23:39:41.908039
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Девчонка, как же я тебя разлюбил?')() == 'Devchonka, kak ze ya tebya razlyubil?'

# Generated at 2022-06-13 23:39:44.492438
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'



# Generated at 2022-06-13 23:39:46.977940
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет, Мир!')([]) == 'Privet, Mir!'



# Generated at 2022-06-13 23:39:54.261172
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.person import Person
    p = Person(locale=Locale.RU)
    assert p.full_name() == 'Айболит Караваев'
    assert p.full_name(romanize=True) == 'Aibolit Karavaev'

    p = Person(locale=Locale.UK)
    assert p.full_name() == 'Антуан Геніч'
    assert p.full_name(romanize=True) == 'Antuan Henich'

    p = Person(locale=Locale.KK)

# Generated at 2022-06-13 23:39:58.306058
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo(self, *args, **kwargs):
        return self.seed.choice(data.CYRILLIC_LETTERS['ru'])

    assert 'Т' == foo(None)
    assert 's' == foo(None, locale='ru')

# Generated at 2022-06-13 23:40:05.692334
# Unit test for function romanize
def test_romanize():
    """Unit test romanize."""
    r_str = 'Привіт, світ!'

    func = romanize('uk')(lambda: r_str)
    assert func() == 'Pryvit, svit!'

    func = romanize('ru')(lambda: r_str)
    assert func() == 'Privet, mir!'

    func = romanize('kk')(lambda: r_str)
    assert func() == 'Privet, mir!'

# Generated at 2022-06-13 23:40:09.533672
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Привет мир!')() == 'Privet mir!'
    assert romanize()(lambda: 'Привет мир!')() == 'Privet mir!'
    assert romanize('uk')(lambda: 'Привєт світ!')() == 'Pryviet svit!'
    assert romanize('kk')(lambda: 'Мұрағаттық қоғам')() == 'Mïraqattïq qoğam'

# Generated at 2022-06-13 23:40:18.490924
# Unit test for function romanize
def test_romanize():
    romanized_locale = 'ru'

    def romanize_test(locale: str = romanized_locale) -> Callable:
        """Romanize the cyrillic text.

        Transliterate the cyrillic script into the latin alphabet.

        :param locale: Locale code.
        :return: Romanized text.
        """


# Generated at 2022-06-13 23:40:21.071378
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет')() == 'Privet'

# Generated at 2022-06-13 23:40:30.427623
# Unit test for function romanize
def test_romanize():
    import random
    import mimesis.builtins
    b = mimesis.builtins.Builtins()

    if b.coin_flip():
        print(b.username(romanize=True))
    elif b.coin_flip():
        print(b.company_name(romanize=True))
    else:
        print(b.slug(romanize=True))

    random.seed(0)
    for i in range(30):
        print(b.username(romanize=True))


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:40:38.211265
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def fake():
        return 'Привет! Как дела?'

    txt = fake()
    assert txt == 'Privet! Kak dela?'


# Generated at 2022-06-13 23:40:44.313222
# Unit test for function romanize
def test_romanize():
    from mimesis import Generic
    gen = Generic('ru')

    @romanized()
    def get_name():
        return gen.person.name(gender='female')

    assert get_name() == 'Marina'


# Generated at 2022-06-13 23:40:53.477071
# Unit test for function romanize
def test_romanize():
    # In this test we will make sure that romanize decorator
    # romanizes the generated text as expected.
    from mimesis import Person
    from mimesis.enums import Gender
    from mimesis.builtins.uk import UkSpecProvider

    class MyPerson(Person):
        """Test class."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.spec = UkSpecProvider

        @romanize(locale='uk')
        def full_name(self, gender: Gender = None):
            """Get full name of the person."""
            return self.name(gender=gender)

    p = MyPerson('ru')

# Generated at 2022-06-13 23:40:57.487173
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_func(arg):
        return arg

    assert romanize_func('Фёдор') == 'Fyodor'

test_romanize()

# Generated at 2022-06-13 23:41:04.737142
# Unit test for function romanize
def test_romanize():
    text = 'Соделай так, чтобы функция возвращала романизованный текст.'
    expected = 'Sodelaj tak, chtoby funkcija vozvraschalas\' romanizovannyj ' \
               'tekst.'
    assert romanize(locale='ru')(text) == expected

# Generated at 2022-06-13 23:41:16.528361
# Unit test for function romanize

# Generated at 2022-06-13 23:41:27.701020
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='kk')('голод') == 'golod'

    assert romanize(locale='ru')('голод') == 'golod'

    assert romanize(locale='uk')('голод') == 'holod'

    assert romanize(locale='ru')('гнутенький') == 'gnuten\'kiy'

    assert romanize(locale='ru')('Голод') == 'Golod'

    assert romanize(locale='ru')('Голод!') == 'Golod!'


# Generated at 2022-06-13 23:41:28.604897
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:41:38.570021
# Unit test for function romanize
def test_romanize():
    from mimesis.providers import Personal
    assert Personal().get_full_name() == 'Ніколай Великодний'
    assert romanize('ru')(Personal().get_full_name)() == 'Nikolay Velikodniy'
    assert romanized('ru')(Personal().get_full_name)() == 'Nikolay Velikodniy'

if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:41:40.252741
# Unit test for function romanize
def test_romanize():
    assert romanized('test_function')() == 'test_function'

# Generated at 2022-06-13 23:41:50.186483
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    assert romanize('ru')(lambda: 'Красная площадь')() == 'Krasnaya ploschad'



# Generated at 2022-06-13 23:41:57.204951
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет мир!')() == 'Privet mir!'
    assert romanized('uk')(lambda: 'Привіт світ!')() == 'Pryvit svit!'
    assert romanized('kk')(lambda: 'Сәлем қазақстан!')() == 'Sälem qazaqstan!'

# Generated at 2022-06-13 23:42:03.351317
# Unit test for function romanize
def test_romanize():
    @romanize(locale='uk')
    def ukraine_text():
        return 'Чорнобиль'

    assert ukraine_text() == 'Čornobyl'

    @romanize
    def russian_text():
        return 'Санкт-Петербург'

    assert russian_text() == 'Sankt-Peterburg'

# Generated at 2022-06-13 23:42:04.425243
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    russian = RussiaSpecProvider()
    word = russian.romanize(russian.word())

    assert len(word) > 0

# Generated at 2022-06-13 23:42:10.486842
# Unit test for function romanize
def test_romanize():
    assert len(data.ROMANIZATION_DICT['ru']) == 33
    assert len(data.ROMANIZATION_DICT['uk']) == 27
    assert len(data.ROMANIZATION_DICT['kk']) == 14

    try:
        romanize(locale='de')
    except UnsupportedLocale as e:
        assert str(e) == 'de'

# Generated at 2022-06-13 23:42:17.826189
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Languages
    from mimesis.providers.person import Person
    from mimesis.utils import get_locale_class

    ru = get_locale_class(Languages.ENGLISH)

    @ru.romanize(locale=Languages.RUSSIAN.value)
    def f():
        p = Person(Languages.RUSSIAN)
        return p.full_name(gender='male')

    assert f().startswith('Mikhail') is True



# Generated at 2022-06-13 23:42:28.182770
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    from mimesis.providers.geography import Geography
    from mimesis.providers.person import Person

    address = Address(Locale.UKRAINIAN)
    geo = Geography(Locale.KAZAKH)
    person = Person(Locale.RUSSIAN)

    # Test Address
    address.address()
    address.address_line()
    address.intersection()
    address.neighborhood()
    address.street_name()

    # Test Geography
    geo.city()
    geo.city_name()
    geo.country()
    geo.country_code()
    geo.city_name_with_state()
    geo.state()
    geo.state_abbr()

# Generated at 2022-06-13 23:42:35.063959
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language

    assert romanize('ru')(lambda: 'Павел')() == 'Pavěl'
    assert romanize('kk')(lambda: 'Сатып')() == 'Satıp'
    assert romanize('uk')(lambda: 'Віктор')() == 'Viktor'
    assert romanize(Language.UKRAINIAN)(lambda: 'Віктор')() == 'Viktor'

# Generated at 2022-06-13 23:42:38.363601
# Unit test for function romanize
def test_romanize():
    assert romanize()('Всем привет') == 'Vsem privet'
    assert romanize()('Цена билета: 2000₽') == 'Cena bileta: 2000₽'


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:42:45.257444
# Unit test for function romanize
def test_romanize():
    assert romanized('greeting')('Hello') == 'Hello'
    assert romanized('greeting', 'ru')('Привет') == 'Privet'
    assert romanized('greeting', 'ru')('Привет') == 'Privet'



# Generated at 2022-06-13 23:42:58.098510
# Unit test for function romanize
def test_romanize():
    # Test if UnsupportedLocale raises
    try:
        test = romanize('test')(lambda: 'test')
        test()
    except UnsupportedLocale:
        assert True, 'UnsupportedLocale raises'
    else:
        assert False, 'UnsupportedLocale does not raise'

    # Test if romanization works
    @romanize('ru')
    def test():
        return 'Тест'

    assert test() == 'Test', 'Romanization does not work'

# Generated at 2022-06-13 23:43:04.457933
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins
    from mimesis.providers.text import Text

    text = Text('ru')
    text.romanize = romanize('ru')(text.romanize)
    string = text.romanize()
    assert isinstance(string, str)
    assert string



# Generated at 2022-06-13 23:43:18.105715
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins.numbers

    @romanize()
    def test():
        return 'Привет, мир!'

    assert test() == 'Privet, mir!'
    assert test.__name__ == 'test'

    @romanize(locale='uk')
    def test_uk():
        return 'Привiт, свiте!'

    assert test_uk() == 'Pryvity, svyte!'

    @romanize(locale='kk')
    def test_kk():
        return 'Сәлем, дүние!'

    assert test_kk() == 'Sälem, dünie!'

    # Test for backward compatibility

# Generated at 2022-06-13 23:43:31.215066
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.person import Person

    p = Person(Locale.UKRAINIAN)
    assert p.full_name().isalpha()
    assert p.full_name().islower()

    @romanize(locale='ru')
    def russian():
        """Return russian text."""
        return p.full_name()

    @romanize(locale='uk')
    def ukrainian():
        """Return ukrainian text."""
        return p.full_name()

    @romanize(locale='kk')
    def kazakh():
        """Return kazakh text."""
        return p.full_name()

    assert russian().isalpha()
    assert ukrainian().isalpha()
    assert kazakh

# Generated at 2022-06-13 23:43:41.358633
# Unit test for function romanize
def test_romanize():
    r = romanize('ru')(lambda: 'Привет')
    assert r == 'Privet'

    r = romanize('ru')(lambda: 'Как дела?')
    assert r == 'Kak dela?'

    r = romanize('ru')(lambda: 'Это пример текста.')
    assert r == 'Eto primer teksta.'

    r = romanize('uk')(lambda: 'Привіт')
    assert r == 'Pryvit'

    r = romanize('uk')(lambda: 'Як справи?')
    assert r == 'Yak spravy?'


# Generated at 2022-06-13 23:43:53.780933
# Unit test for function romanize
def test_romanize():
    def test_romanize(k: str, v: str):
        assert romanize('ru')(lambda: k)() == v

    test_romanize('А', 'A')
    test_romanize('Б', 'B')
    test_romanize('В', 'V')
    test_romanize('Г', 'G')
    test_romanize('Д', 'D')
    test_romanize('Е', 'E')
    test_romanize('Ё', 'Ë')
    test_romanize('Ж', 'Zh')
    test_romanize('З', 'Z')
    test_romanize('И', 'I')
    test_romanize('Й', 'J')
    test_romanize('К', 'K')

# Generated at 2022-06-13 23:44:03.473442
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    assert romanized('ru')(lambda: 'Привет')() == 'Privet'
    assert romanized('ru')(lambda: 'привет')() == 'privet'
    assert romanized('kk')(lambda: 'Привет')() == 'Privet'
    assert romanized('kk')(lambda: 'привет')() == 'privet'
    assert romanized('uk')(lambda: 'Привіт')() == 'Pryvit'
    assert romanized('uk')(lambda: 'привіт')() == 'pryvit'

# Generated at 2022-06-13 23:44:15.114817
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person
    import re
    person = Person('ru')
    person_data = person.full_name().split()
    first_name = person_data[1]
    last_name = person_data[0]
    patronymic_name = person.patronymic()

    def test_romanize_string(text: str) -> None:
        assert not re.search(r'[^a-zA-Z\s]', text)

    test_romanize_string(person.romanize(first_name))
    test_romanize_string(person.romanize(last_name))
    test_romanize_string(person.romanize(patronymic_name))
    test_romanize_string(person.romanize(str(person)))

# Generated at 2022-06-13 23:44:22.733015
# Unit test for function romanize
def test_romanize():
    import os
    import json
    import shutil
    import tempfile
    from mimesis.enums import Locale

    d = tempfile.mkdtemp()
    path = os.path.join(d, 'mimesis.json')
    data.DATABASE_FILE = path
    data.DATABASE_PATH = path


# Generated at 2022-06-13 23:44:32.264259
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Антон Драгомиров')() == 'Anton Dragomirov'
    assert romanize()(lambda: 'Алабай Нурали Казымбаев')() == 'Alabay Nurali Kazymbayev'
    assert romanize()(lambda: 'Жанглыова Алишера Алимбаев')() == 'Zhanglyova Alishera Alimbayev'

# Generated at 2022-06-13 23:44:38.711233
# Unit test for function romanize
def test_romanize():
    assert romanize()



# Generated at 2022-06-13 23:44:40.976951
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: "привет")() == "privet"

# Generated at 2022-06-13 23:44:58.451573
# Unit test for function romanize
def test_romanize():
    assert ascii_letters == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert digits == '0123456789'
    assert punctuation == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Generated at 2022-06-13 23:45:06.356093
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет')() == 'Privet'
    assert romanized('uk')(lambda: 'Привіт')() == 'Pryvit'
    assert romanized('kk')(lambda: 'Сәлем')() == 'Salem'

# Generated at 2022-06-13 23:45:11.026281
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Здравствуй, мир!')() == 'Zdravstvuy, mir!'

# Generated at 2022-06-13 23:45:19.492584
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    @romanize('ru')
    def romanize_ru():
        return 'Абырвалг'

    assert romanize_ru() == 'Abirvalg'

    @romanize('uk')
    def romanize_uk():
        return 'Абирвальг'

    assert romanize_uk() == 'Abirvalg'

    @romanized('ru')
    def romanize_ru():
        return 'Абырвалг'

    assert romanize_ru() == 'Abirvalg'

    @romanized('uk')
    def romanize_uk():
        return 'Абирвальг'

    assert romanize_

# Generated at 2022-06-13 23:45:22.732036
# Unit test for function romanize
def test_romanize():
    """Romanize test."""
    def foo(locale: str = ''):
        return 'Алфавит'

    bar = romanize(locale='ru')(foo)

    assert bar() == 'Alfavit'



# Generated at 2022-06-13 23:45:36.187290
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""

    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    en_alphabet = "aбвгдеёжзийклмнопрстуфхцчшщъыьэюya"
    assert romanize(locale='ru')(alphabet) == "abvgdeezhzijklmnoprstufhc'h'y'eeee"

# Generated at 2022-06-13 23:45:38.935565
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.person import Person

    p = Person(Locale.RUSSIAN)
    assert p.full_name.split()[0] == p.romanized.full_name.split()[0]

# Generated at 2022-06-13 23:45:44.573718
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: "python")() == 'python'
    assert romanize('uk')(lambda: "компьютер")() == 'kompiuter'
    assert romanize('kk')(lambda: "компьютер")() == 'kom’iuter'


# Generated at 2022-06-13 23:46:05.180651
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def _():
        return 'Привет мир!'

    assert _() == 'Privet mir!'



# Generated at 2022-06-13 23:46:13.942701
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def romanized_russian():
        return 'По жизни ходил на куски 2.'

    @romanize(locale='uk')
    def romanized_ukrainian():
        return 'По життю ходив на куски 2.'

    @romanized(locale='ru')
    def romanized_russian_with_alias():
        return 'Общая длина границы должна быть больше 3,00 мм.'


# Generated at 2022-06-13 23:46:20.768666
# Unit test for function romanize
def test_romanize():
    """Test for function :func:`mimesis.decorators.romanize`."""
    # python 3.5
    import sys

    import pytest

    if 'win' in sys.platform:
        pytest.skip('This test is not supported on Windows.')

    @romanize()
    def x(locale: str = 'ru') -> str:
        return data.ROMANIZATION_DICT[locale]

    assert x('kk')

    with pytest.raises(UnsupportedLocale):
        x('xx')

# Generated at 2022-06-13 23:46:24.599181
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_test(value):
        return 'Привет! Мир!'

    assert romanize_test() == 'Privet! Mir!'

# Generated at 2022-06-13 23:46:33.274192
# Unit test for function romanize
def test_romanize():
    alf = {
        'В': 'V',
        'л': 'l',
        'я': 'ia',
    }
    expected = {
        'Вля': 'Vlia',
        'Вля123': 'Vlia123',
        'Вля!': 'Vlia!',
    }
    alphabet = {s: s for s in ascii_letters + digits + punctuation}
    alphabet.update(**alf)
    alphabet.update({
        **data.ROMANIZATION_DICT['ru'],
        **data.COMMON_LETTERS,
    })

    for key, exp in expected.items():
        txt = ''.join([alphabet[i] for i in key if i in alphabet])
        assert txt == exp

# Generated at 2022-06-13 23:46:37.291251
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    from mimesis.enums import Language
    text = Text(Language.RUSSIAN)

    @romanize(locale=text.language)
    def foo():
        return text.word()

    assert isinstance(foo(), str)

# Generated at 2022-06-13 23:46:41.055425
# Unit test for function romanize
def test_romanize():
    @romanized()
    def say_hello():
        return 'Привет'
    assert say_hello() == "Privet"

# Generated at 2022-06-13 23:46:47.825462
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.text import Text

    for locale in data.LOCALIZATION.keys():
        provider = Text(locale=locale)

        for _ in range(5):
            string = provider._data['common']['syllable']
            romanized_string = provider.romanize(string)
            assert string.isalpha()
            assert romanized_string.isalpha()
            assert len(string) == len(romanized_string)



# Generated at 2022-06-13 23:46:52.801683
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person
    p = Person()
    romanized_name = p.name(locale='ru')
    assert romanize('ru')(p.name)(locale='ru') == romanized_name  # pylint: disable=E1120

# Generated at 2022-06-13 23:47:00.987748
# Unit test for function romanize
def test_romanize():
    """Test romanize from romanization_utils"""

    import random
    import string
    from mimesis.enums import Locale

    def test_random_str(str_length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(str_length))

    @romanize(locale=Locale.RU)
    def test_cyrillic_str(str_length=10):
        """Generate a cyrillic string of fixed length """
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Generated at 2022-06-13 23:47:15.708454
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    @romanize(locale='ru')
    def romanized_test(test_string):
        return test_string

    assert romanized_test('привет') == 'privet'

# Generated at 2022-06-13 23:47:20.499279
# Unit test for function romanize
def test_romanize():
    text = 'мемы'
    romanizer = romanize('ru')
    romanized_text = romanizer(lambda x: text)
    assert romanized_text == 'memy'

    romanizer = romanize('uk')
    romanized_text = romanizer(lambda x: text)
    assert romanized_text == 'memy'

test_romanize()

# Generated at 2022-06-13 23:47:23.071464
# Unit test for function romanize
def test_romanize():
    from mimesis import Generic

    g = Generic('ru')
    assert g.text.romanize() == g.text.romanized()

# Generated at 2022-06-13 23:47:26.001649
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def text():
        return 'Привет, Мир!'

    assert text() == 'Privet, Mir!'



# Generated at 2022-06-13 23:47:31.847117
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Address
    from mimesis.enums import Gender

    instance = Address('ru')
    assert instance.full_name(
        gender=Gender.FEMALE,
        romanized=True
    ) == 'Anna Ivanovna Ivanova'

# Generated at 2022-06-13 23:47:39.822791
# Unit test for function romanize
def test_romanize():
    import string

    import mimesis
    from mimesis.builtins.text import Text
    from mimesis.enums import Language

    t = Text(Language.EN)
    t.seed('test_romanize')

    alphabet = string.ascii_letters + string.digits + ' -'
    s = t.text(max_length=100)
    assert all(x in alphabet for x in s)
    assert s == mimesis.romanized(s)

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + \
              string.digits + ' -'

# Generated at 2022-06-13 23:47:42.044419
# Unit test for function romanize
def test_romanize():
    text = romanize('ru')(lambda: 'Кириллица')()
    assert text == 'Kirillica'

# Generated at 2022-06-13 23:47:44.990124
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def text():
        return 'Тест!'

    assert text() == 'Test!'
    assert text.__name__ == 'text'
    assert text.__doc__ is None

# Generated at 2022-06-13 23:47:51.126538
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.person import Person
    from mimesis.providers.text import Text
    p = Person('ru')
    t = Text(Language.RUSSIAN.value)
    assert p.full_name('first_name_male') in t.romanize(t.word())

# Generated at 2022-06-13 23:47:52.286455
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')('Привет, Мир!') == 'Privet, Mir!'

# Generated at 2022-06-13 23:48:23.239427
# Unit test for function romanize
def test_romanize():
    romanization_dict = {
        'ru': 'a b v g d e je jo zh z i j k l m n o p r s t u f kh '
              'ts ch sh sch y hard soft e yu ya',
        'uk': 'a b v h g d e je jo zh z i j k l m n o p r s t u f kh '
              'ts ch sh sch y hard soft e yu ya',
        'kk': 'a b v g d e je j yo zh z i j k l m n o p r s t u f kh '
              'ts ch sh shch y hard soft e yu ya',
    }

    for locale, text in romanization_dict.items():
        @romanize(locale)
        def test(text):
            return text

        assert test(text) == text

# Generated at 2022-06-13 23:48:31.464509
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def ru(text):
        return text

    assert ru('Привет') == 'Privet'
    assert ru('Новый текст.') == 'Novyj tekst.'
    assert ru('Текст на русском.') == 'Tekst na russkom.'

# Generated at 2022-06-13 23:48:34.043137
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'тддд')() == 'tttt'

# Generated at 2022-06-13 23:48:36.611734
# Unit test for function romanize
def test_romanize():
    romanize.romanize_deco(romanize)
    # If the assertion is working, it is ok

# Generated at 2022-06-13 23:48:42.845337
# Unit test for function romanize
def test_romanize():
    test_string = "Столица Украины Киев."
    romanized = romanize("uk")
    func = romanized(lambda: test_string)
    assert func() == "Stolitsa Ukraïny Kyïv."

# Generated at 2022-06-13 23:48:45.084803
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет мир!')() == 'Privet mir!'

# Generated at 2022-06-13 23:48:55.119391
# Unit test for function romanize
def test_romanize():
    # Test romanize: romanized text
    def __test():
        return 'Пример'

    __test = romanize('ru')(__test)
    assert __test() == 'Primer'

    # Test romanize: romanized text with some symbols
    def __test():
        return 'Пример!'

    __test = romanize('ru')(__test)
    assert __test() == 'Primer!'

    # Test romanize: romanized text with some digits
    def __test():
        return 'Пример 12.'

    __test = romanize('ru')(__test)
    assert __test() == 'Primer 12.'

# Generated at 2022-06-13 23:49:05.567204
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет, Мир!')() == 'Privet, Mir!'
    assert romanized('uk')(lambda: 'Вітаю, Світ!')() == 'Vitayu, Svit!'
    assert romanized('kk')(lambda: 'Сәлем, Түнікті құрал!')() == \
        'Salem, Tünikti qural!'

# Generated at 2022-06-13 23:49:11.150049
# Unit test for function romanize
def test_romanize():
    @romanize()
    def test_with_title():
        return 'Россия'
    assert test_with_title() == 'Rossiya'


# Generated at 2022-06-13 23:49:16.533333
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    @romanize(locale='ru')
    def romanize_name(x):
        """Romanize russian name."""
        return x

    res = romanize_name("Сергей")
    exp = "Sergei"
    assert res == exp

    res = romanize_name("Нікіта")
    exp = "Nikita"
    assert res == exp
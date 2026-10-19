

# Generated at 2022-06-13 23:39:37.778997
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:39:45.692798
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider as rs
    assert rs().romanize('Привет') == rs().romanize('Привет')
    assert rs().romanize('Привет') == 'Privet'
    assert rs().romanize('Привет') == rs().romanize('Привет')
    assert rs().romanize('Привет') == rs().romanize('Привет')

# Generated at 2022-06-13 23:39:53.515330
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def test():
        return "Привет, мир!"
    assert test() == 'Privet, mir!'

    @romanize('uk')
    def test():
        return "Привіт, світ!"
    assert test() == 'Pryvit, svit!'

    @romanize('kk')
    def test():
        return "Салам алейкум!"
    assert test() == 'Salam alejkum!'

    # Unicode letters
    @romanize('ru')
    def test():
        return "Салам алейкум!"
    assert test() == 'Salam alejkum!'

    # Punctuation

# Generated at 2022-06-13 23:40:02.376709
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    p = Person('ru')

    assert isinstance(p.romanize(p.full_name()), str)
    assert isinstance(p.romanize(p.surname()), str)
    assert isinstance(p.romanize(p.name()), str)
    assert isinstance(p.romanize(p.username()), str)
    assert isinstance(p.romanize(p.password()), str)



# Generated at 2022-06-13 23:40:08.481093
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import (
        the_hacker,
        russian,
        ukrainian,
        finnish,
    )

    def function():
        return the_hacker().password(8, 16)

    @romanize()
    def function_ru():
        return russian('personal').full_name()

    @romanize('uk')
    def function_uk():
        return ukrainian('personal').full_name()

    @romanized('kk')
    def function_kk():
        return finnish().person().full_name()

    assert function_ru() == function_uk() == function_kk() == function()
    assert function_ru() != function_uk() != function

# Generated at 2022-06-13 23:40:12.033108
# Unit test for function romanize
def test_romanize():
    assert romanize()("Привіт") == "Pryvit"
    assert romanize("uk")("Привіт") == "Pryvit"

# Generated at 2022-06-13 23:40:13.551780
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanized()

# Generated at 2022-06-13 23:40:25.831918
# Unit test for function romanize

# Generated at 2022-06-13 23:40:28.537148
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='uk')(lambda: 'Привіт, мир')() == 'Pryvit, myr'



# Generated at 2022-06-13 23:40:31.479261
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'настоящее')() == 'nastoyaschee'

# Generated at 2022-06-13 23:40:39.076107
# Unit test for function romanize
def test_romanize():
    assert romanize(locale=None)(lambda: 'hello')() == 'hello'



# Generated at 2022-06-13 23:40:42.570206
# Unit test for function romanize
def test_romanize():
    """Test romanize()."""
    # ToDo: Add test for romanize()
    pass

# Generated at 2022-06-13 23:40:47.481746
# Unit test for function romanize
def test_romanize():
    from mimesis.schema import Schema
    from mimesis.providers.address import Address

    s = Schema({'name': Address(locale='ru')})
    assert isinstance(s.generate(), dict)

# Generated at 2022-06-13 23:40:51.635295
# Unit test for function romanize
def test_romanize():
    # Also functions as a demo for use.
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    @romanize(locale='ru')
    def russian_name() -> str:
        return Person('ru').full_name(gender=Gender.FEMALE)

    assert russian_name() == 'Natalia Petrova'

# Generated at 2022-06-13 23:40:55.708856
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def romanize_ru():
        return 'Привет, Мир!'
    assert romanize_ru() == 'Privet, Mir!'

# Generated at 2022-06-13 23:41:04.048732
# Unit test for function romanize
def test_romanize():
    from mimesis import Text

    text = Text('ru')
    result = text.romanized.word(5)
    assert result == text.romanize.word(5)

    result = text.romanize.lowercase_word(3)
    assert result == 'naz'

    result = text.romanize.lowercase_word(3)
    assert result == 'naz'

    result = text.romanize.lowercase_word(3, 4)
    assert result == 'naz'

    result = text.romanize.lowercase_word(5, 5)
    assert result == 'bolno'

# Generated at 2022-06-13 23:41:13.842715
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    from mimesis.enums import Language

    from mimesis.builtins import Localization

    ru_localization = Localization(locale=Language.RU)

    @ru_localization.romanize()
    def roman_func():
        return 'Компания рада всем предложить свои услуги и товары.'

    assert roman_func() == 'Kompaniya rada vsem predlozhit' \
                           ' svoyu uslugi i tovary.'

# Generated at 2022-06-13 23:41:18.358813
# Unit test for function romanize
def test_romanize():
    @romanize()
    def roman():
        return 'привет'
    assert roman() == 'privet'

    @romanize(locale='ru')
    def roman():
        return 'привет'
    assert roman() == 'privet'

# Generated at 2022-06-13 23:41:29.951067
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import CharacterSet
    from mimesis.schema import Field, Schema
    from mimesis.typing import FieldType

    class FakeProvider(object):
        def __init__(self, locale: str = 'ru'):
            self._locale = locale

        @romanized(locale='ru')
        def get_swear_words(self, custom=None, count=1) -> str:
            return data.RuSwearWords.get_one(pattern=custom)

    # Get a field with custom pattern
    custom = 'fuck'
    f = romanized(locale='ru')(lambda x: data.RuSwearWords.get_one(pattern='fuck'))
    assert isinstance(f, Field)
    assert len(f(FakeProvider('ru'))) > 1

    #

# Generated at 2022-06-13 23:41:41.116775
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian_ru():
        return 'Привет, Мир!'

    assert russian_ru() == 'Privet, Mir!'

    @romanize(locale='uk')
    def ukrainian_uk():
        return 'Привіт, Світ!'

    assert ukrainian_uk() == 'Pryvit, Svit!'

    @romanize(locale='kk')
    def kazakh_kk():
        return 'Сәлем, Дүние!'

    assert kazakh_kk() == 'Sälem, Dünie!'


# Generated at 2022-06-13 23:41:56.042096
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.language import Language
    from mimesis.builtins import RussiaSpecProvider
    ru = Language('ru', RussiaSpecProvider)
    assert ru.romanize('Привет, мир!') == 'Privet, mir!'

# Generated at 2022-06-13 23:42:04.272167
# Unit test for function romanize
def test_romanize():
    """Test romanize with different arguments."""
    from mimesis.builtins.en import Letters

    letters = Letters()

    @romanize(locale='ru')
    def romanize_ru():
        return f'{letters.syllable()} {letters.syllable()}'

    @romanize(locale='en')
    def romanize_en():
        return f'{letters.syllable()} {letters.syllable()}'

    assert romanize_ru() != romanize_en()



# Generated at 2022-06-13 23:42:07.875429
# Unit test for function romanize
def test_romanize():
    assert romanize()('АБАЙҒҰЛЫ') == 'Abayǵuly'
    assert romanized()('БАҒДАТ') == 'Bagdat'

# Generated at 2022-06-13 23:42:15.866075
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def romanize_ru(string: str) -> str:
        return string

    assert romanize_ru('Бірегей теңіздердің қағаздарында') == \
           'Biregey teñizderdiń qağazdarynda'

    @romanize(locale='uk')
    def romanize_uk(string: str) -> str:
        return string

    assert romanize_uk('Попередний попередник') == 'Poperedniy poperednik'


# Generated at 2022-06-13 23:42:18.663406
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize(text):
        return text

    assert romanize('Россия') == 'Rossiya'

# Generated at 2022-06-13 23:42:21.170187
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def word():
        return 'Арбуз'

    assert word() == 'Arbuz'

# Generated at 2022-06-13 23:42:28.872772
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian_name():
        return 'Маша'

    assert russian_name() == 'Masha'

    @romanize(locale='uk')
    def ukrainian_name():
        return 'Степан'

    assert ukrainian_name() == 'Stepan'

    @romanize(locale='kk')
    def kazakh_name():
        return 'Дина'

    assert kazakh_name() == 'Dina'

# Generated at 2022-06-13 23:42:38.688012
# Unit test for function romanize
def test_romanize():
    def romanize_deco_test(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Cyrillic string can contain ascii
                # symbols, digits and punctuation.
                alphabet = {s: s for s in
                            ascii_letters + digits + punctuation}
                alphabet.update({
                    **data.ROMANIZATION_DICT['ru'],
                    **data.COMMON_LETTERS,
                })
            except KeyError:
                raise UnsupportedLocale(locale)

            result = func(*args, **kwargs)
            txt = ''.join([alphabet[i] for i in result if i in alphabet])
            return txt

        return wrapper


# Generated at 2022-06-13 23:42:44.409755
# Unit test for function romanize
def test_romanize():
    @romanize(locale='uk')
    def get_name(self):
        return 'Дмитро'

    assert get_name('') == 'Dmytro'
    assert 'Дмитро' != get_name('')



# Generated at 2022-06-13 23:42:47.820685
# Unit test for function romanize
def test_romanize():
    @romanize(locale='uk')
    def hello():
        return 'Доброго дня'

    assert hello() == 'Dobroho dnia'

# Generated at 2022-06-13 23:43:17.455983
# Unit test for function romanize
def test_romanize():
    from unittest import main

    from mimesis.data import ROMANIZATION_DICT
    from mimesis.enums import Language

    for lang in Language:
        word = ROMANIZATION_DICT[lang.code]['й']
        assert romanize(lang.code)(lambda: word)() == word

    assert romanized('ru')(lambda: 'й')() == 'y'
    assert main(module='test_romanize').defaultTestResult().wasSuccessful()

# Generated at 2022-06-13 23:43:22.173665
# Unit test for function romanize
def test_romanize():
    def test_func():
        return 'Сейчас что, у меня нет тут никакого кириллического текста!'

    assert romanize(locale='ru')(test_func) == \
        'Seichas chto, u menia net tut nikakovo kirillicheeskovo teksta!'

# Generated at 2022-06-13 23:43:27.988585
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    assert romanize()(lambda: 'Майкл')() == 'Michael'
    assert romanize(locale='uk')(lambda: 'Майкл')() == 'Majkl'
    assert romanize(locale='ru')(lambda: 'Майкл')() == 'Majkl'
    assert romanize(locale='kk')(lambda: 'Майкл')() == 'Maykl'
    assert romanize()(lambda: 'Дэн')() == 'Dan'
    assert romanize(locale='uk')(lambda: 'Дэн')() == 'Den'

# Generated at 2022-06-13 23:43:37.130476
# Unit test for function romanize
def test_romanize():
    # Russian locale
    @romanize('ru')
    def russian():
        return 'Выборг'

    assert russian() == 'Vyborg'

    # Ukrainian locale
    @romanize('uk')
    def ukrainian():
        return 'Виборг'

    assert ukrainian() == 'Viborg'

    # Kazakh locale
    @romanize('kk')
    def kazakh():
        return 'Выборг'

    assert kazakh() == 'Wyborğ'

# Generated at 2022-06-13 23:43:40.829660
# Unit test for function romanize
def test_romanize():
    def test_func(value):
        return value

    decorated_func = romanize(locale='ru')(test_func)
    test_str = 'Родина'
    assert test_str == test_func(test_str)

    assert 'Rodina' == decorated_func(test_str)

# Generated at 2022-06-13 23:43:51.578186
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda : 'привет')() == 'privet'
    assert romanize('uk')(lambda : 'привіт')() == 'pryvit'
    assert romanize('kk')(lambda : 'сәлем')() == 'salem'
    assert (romanize('ru')(lambda : 'дом')() == 'dom' and
            romanize('ru')(lambda : 'Дом')() == 'Dom')
    assert romanize('ru')(lambda : 'привет')() == 'privet'


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:44:02.869591
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    # Test locale is supported.
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'
    assert romanize('uk')(lambda: 'Привіт')() == 'Pryvit'
    assert romanize('kk')(lambda: 'Сәлем')() == 'Sälem'

    # Test cyrillic string can contain ascii symbols, digits and punctuation.
    assert romanize('ru')(lambda: 'Hello, Привет, 01!')() ==\
        'Hello, Privet, 01!'

    # Test with unsupported locale.

# Generated at 2022-06-13 23:44:05.684945
# Unit test for function romanize
def test_romanize():
    """Test for romanize function."""
    assert romanize(locale='ru')(lambda x: 'Привет, мир!')() == 'Privet, mir!'

# Generated at 2022-06-13 23:44:13.109933
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    person = Person('ru')
    name = person.full_name(gender=Gender.MALE)
    romanized_name = ''.join([
        person.first_name(gender=Gender.MALE),
        person.last_name(gender=Gender.MALE),
    ])
    assert name == romanized_name

# Generated at 2022-06-13 23:44:13.949849
# Unit test for function romanize
def test_romanize():
    assert 'получится' == 'получится'

# Generated at 2022-06-13 23:45:20.591559
# Unit test for function romanize
def test_romanize():
    def foo() -> str:
        return 'Смешанный'

    assert romanize(locale='ru')(foo)() == 'Smeshannyy'

    def bar() -> str:
        return 'Автомобіль'

    assert romanize(locale='uk')(bar)() == 'Avtomobil'

    def baz() -> str:
        return 'Автомобиль'

    assert romanize(locale='kk')(baz)() == 'Avtomobil'

# Generated at 2022-06-13 23:45:31.649226
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    import time, string

    @romanize('ru')
    def romanize_test(test_str: str) -> str:
        return test_str

    assert romanize_test('Привет!') == 'Privet!'
    assert romanize_test('Ссылка на сайт:') == 'Ssilka na sait:'
    assert romanize_test('Ссылка на сайт:') == 'Ssilka na sait:'
    assert romanize_test('Президент Америки Дональд Трамп') == 'Prezident Ameriki Donald Trump'

# Generated at 2022-06-13 23:45:35.976142
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    p = Person(Locale.ENGLISH)
    a = Address(Locale.ENGLISH)
    assert p.full_name() in a.street_name()
    assert p.full_name() not in a.address()

# Generated at 2022-06-13 23:45:39.642262
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет!')(locale='ru') == 'Privet!'
    assert romanize('uk')(lambda: 'Привіт!')(locale='uk') == 'Privit!'
    assert romanize('kk')(lambda: 'Сәлем!')(locale='kk') == 'Salem!'

# Generated at 2022-06-13 23:45:40.588711
# Unit test for function romanize
def test_romanize():
    assert romanized('locale')(lambda: "Вася")() == "VÃ¡sya"

# Generated at 2022-06-13 23:45:57.939438
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    from mimesis.builtins import RussiaSpecProvider

    rs = RussiaSpecProvider()
    assert rs._nationality(locale='ru') == romanize('ru')(rs._nationality)(locale='ru')
    assert rs._nationality(locale='uk') == romanize('uk')(rs._nationality)(locale='uk')
    assert rs._nationality(locale='kk') == romanize('kk')(rs._nationality)(locale='kk')

# Generated at 2022-06-13 23:46:09.982090
# Unit test for function romanize
def test_romanize():
    import pytest
    from mimesis.enums import Locale

    with pytest.raises(UnsupportedLocale) as e:
        @romanize(locale='pt')
        def test1(locale):
            return locale
        test1(locale=Locale.PT)
        assert e.value.args[0] == 'pt'

    @romanize(locale='uk')
    def test2(locale):
        return locale
    assert test2(locale=Locale.UK) == 'ukraїnsʹka'

    @romanize(locale='kk')
    def test3(locale):
        return locale
    assert test2(locale=Locale.KK) == 'қазақ тілі'


# Generated at 2022-06-13 23:46:15.122988
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider
    spec = RussianSpecProvider()

    @romanize(locale='ru')
    def get_full_name(formatted=False):
        return spec._full_name(formatted)

    assert isinstance(get_full_name(), str)
    assert get_full_name().isalpha()

    @romanize(locale='uk')
    def get_full_name(formatted=False):
        return spec._full_name(formatted)

    assert isinstance(get_full_name(), str)
    assert get_full_name().isalpha()

# Generated at 2022-06-13 23:46:18.876622
# Unit test for function romanize
def test_romanize():
    def foo(bar):
        return bar

    func = romanize()(foo)

    assert func("1234") == '1234'


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:46:26.539262
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'абв')() == 'abv'
    f = romanize('uk')(lambda: 'абв')
    assert f() == 'abv'

    f = romanize('kk')(lambda: 'абв')
    assert f() == 'abv'

    try:
        f = romanize('bak')(lambda: 'абв')
        f()
    except UnsupportedLocale as e:
        assert str(e) == 'The locale bak is not supported.'

    # Test with digits

# Generated at 2022-06-13 23:48:02.960868
# Unit test for function romanize
def test_romanize():
    """Test for romanize function"""
    assert romanize()



# Generated at 2022-06-13 23:48:05.824599
# Unit test for function romanize
def test_romanize():
    # 1から100までのルート
    def romanize(x, locale='ru'):
        @romanize(locale)
        def func(x):
            return str(x)

        return func(x)

    print(romanize(13))

# Generated at 2022-06-13 23:48:15.632559
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Съешь ещё этих мягких французских булочек '
                                   'да выпей чаю')() == \
        'Sješ eščö etih mjagkih francuzskih buloček da vypej čaju'



# Generated at 2022-06-13 23:48:20.875730
# Unit test for function romanize
def test_romanize():
    # pylint: disable=W0613
    @romanize()
    def test(locale: str = '') -> str:
        return "Привет, Мир"
    assert test("qwerty") == "Привет, Мир"

# Generated at 2022-06-13 23:48:26.154673
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    import mimesis.builtins.numbers as num

    romanized_numbers = romanize(locale='kk')(num.Integer._constructor) # noqa
    assert romanized_numbers(99999999999999999999) == 'kzkt kzkt kzkt kzkt kzkt kzkt kzkt kzkt kzkt kzkt'

# Generated at 2022-06-13 23:48:26.910699
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanized

# Generated at 2022-06-13 23:48:31.806959
# Unit test for function romanize
def test_romanize():
    import random
    import string

    TEST_LOCALE = 'ru'
    source = data.ROMANIZATION_DICT[TEST_LOCALE]

    def func(txt):
        return txt

    result = romanize(TEST_LOCALE)(func)
    text = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(3000)])
    assert result(text) == text

    # check for uniqueness of the romanization:
    # 1. all cyrillic letters are represented by roman characters
    # 2. every roman letter is unique and is used only once
    alphabet = [i for i in source.values() if len(i) == 1]
    assert set(alphabet) == set([i.lower() for i in alphabet])

    # 3. r

# Generated at 2022-06-13 23:48:37.482177
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'СайкаБар')().strip() == 'SaikaBar'
    assert romanize(locale='uk')(lambda: 'СайкаБар')().strip() == 'SaikaBar'
    assert romanize(locale='kk')(lambda: 'СайкаБар')().strip() == 'SaikaBar'

# Generated at 2022-06-13 23:48:40.678691
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Привет, мир!')() == 'Privet, mir!'

# Generated at 2022-06-13 23:48:44.276797
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda x: 'Привет')() == 'privet'
    assert romanize(locale='uk')(lambda x: 'Привіт')() == 'privyt'
    assert romanize(locale='kk')(lambda x: 'Салют')() == 'salut'
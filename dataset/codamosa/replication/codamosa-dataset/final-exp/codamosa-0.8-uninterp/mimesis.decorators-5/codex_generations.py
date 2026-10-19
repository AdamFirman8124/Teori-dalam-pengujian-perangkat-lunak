

# Generated at 2022-06-13 23:39:36.976464
# Unit test for function romanize
def test_romanize():
    assert ascii_letters in romanize()(None)
    assert digits in romanize()(None)
    assert punctuation in romanize()(None)

# Generated at 2022-06-13 23:39:46.172692
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    def text(locale='ru'):
        return 'Декораторы используются в функциональном программировании'

    assert romanize(locale='ru')(text)(locale='ru') == \
        'Dekoratory ispolzuyutsya v funkcionalnom programmirovanii'



# Generated at 2022-06-13 23:39:48.150481
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привет!')() == 'Privet!'

# Generated at 2022-06-13 23:40:00.318721
# Unit test for function romanize
def test_romanize():
    # pylint: disable=no-value-for-parameter
    @romanize()
    def romanize_func_no_param():
        return 'Что такое Россия?'

    assert romanize_func_no_param() == 'CHto takoe Rossiya?'

    @romanize('ru')
    def romanize_func_ru():
        return 'Что такое Россия?'

    assert romanize_func_ru() == 'CHto takoe Rossiya?'

    @romanize('uk')
    def romanize_func_uk():
        return 'Что такое Россия?'


# Generated at 2022-06-13 23:40:11.664712
# Unit test for function romanize
def test_romanize():
    import random
    import string

    cyrillic_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


# Generated at 2022-06-13 23:40:12.990932
# Unit test for function romanize
def test_romanize():
    pass



# Generated at 2022-06-13 23:40:14.123581
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')



# Generated at 2022-06-13 23:40:21.144375
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет')() == 'Privet'
    assert romanized('uk')(lambda: 'Привіт')() == 'Privit'
    assert romanized('kk')(lambda: 'Сәлем')() == 'Salem'

# Generated at 2022-06-13 23:40:30.466221
# Unit test for function romanize
def test_romanize():
    from mimesis import Person
    from mimesis.builtins import RussiaSpecProvider
    rus = Person(RussiaSpecProvider)
    _repr = repr(rus)
    assert _repr == f'<mimesis.Person(RussiaSpecProvider)>'
    _symbols = rus.symbols()
    assert _symbols == '№'
    _sex = rus.sex()
    assert _sex == 'male'
    _fullname = rus.full_name()
    assert isinstance(_fullname, str)



# Generated at 2022-06-13 23:40:34.454648
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def ru_text():
        return 'Андрей'
    assert ru_text() == 'Andrei'
    assert ru_text('literal') == 'Andrei'
    assert ru_text('literal', True) == 'Andrei'



# Generated at 2022-06-13 23:40:46.272068
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    def test(locale):
        for _ in range(1000):
            assert romanize(locale)(RussiaSpecProvider().full_name)() is not None

    test('ru')
    test('uk')
    test('kk')

# Generated at 2022-06-13 23:40:51.610142
# Unit test for function romanize
def test_romanize():
    print(romanize()(lambda: 'Саратов'))
    print(romanize()(lambda: 'საქართველო'))
    print(romanize()(lambda: 'Астана'))


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:40:54.683707
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    person = Person('ru')
    person.full_name()
    person.username()


test_romanize()

# Generated at 2022-06-13 23:41:05.307929
# Unit test for function romanize
def test_romanize():
    from mimesis.schema import Field, Schema
    from mimesis.enums import Gender

    schema = {
        'id': Field('uuid'),
         'name': Field('person.full_name', gender=Gender.MALE),
    }

    builder = Schema(schema)

    for _ in range(10):
        result = builder.create(locale='uk')
        print(result)

    # expected output:
    # {'id': '0d7b23c8-7737-5bf5-bef5-543e9c897dc5', 'name': 'Волощук Степан Леонідович'}
    # {'id': 'fd39f40f-4a4f-55

# Generated at 2022-06-13 23:41:15.554959
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.person import Person
    from mimesis.providers.internet import Internet
    from mimesis.providers.file import File
    from mimesis.providers.other import Address, Datetime
    from mimesis.providers.text import Text
    from mimesis.providers.code import Code
    from mimesis.providers.payment import \
        Payment

    provider_list = [Person, Internet, File, Address, Datetime, Text, Code, Payment]

    for p in provider_list:
        provider = p(locale='ru')
        assert provider.romanize('Стол') == 'Stol'


# Generated at 2022-06-13 23:41:18.357598
# Unit test for function romanize
def test_romanize():
    def romanize_func():
        return 'ээ ээ'

    result = romanize('ru')(romanize_func)()
    assert result == 'ee ee'

# Generated at 2022-06-13 23:41:19.308552
# Unit test for function romanize
def test_romanize():
    assert True

# Generated at 2022-06-13 23:41:30.150668
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    romanize_ru = romanize('ru')

    @romanize_ru
    def russian(self):
        return 'Лепсе мы не друзья.'

    text = russian('Test')
    assert text == 'Lepse my ne druzʹya.'
    assert isinstance(text, str)

    @romanize('uk')
    def ukrainian(self):
        return 'Лепсе ми не друзі.'

    text = ukrainian('Test')
    assert isinstance(text, str)
    assert text == 'Lepse my ne druzi.'



# Generated at 2022-06-13 23:41:32.714974
# Unit test for function romanize
def test_romanize():
    @romanize()
    def m():
        return "Как дела?"

    assert m() == "Kak dela?"



# Generated at 2022-06-13 23:41:37.739747
# Unit test for function romanize
def test_romanize():
    @romanized()
    def get_something():
        return 'Привет, мир!'

    actual = get_something()
    expected = 'Privet, mir!'

    assert actual == expected

# Generated at 2022-06-13 23:41:56.618058
# Unit test for function romanize
def test_romanize():
    """Test the function romanize."""
    romanize('ru')(lambda: "Код выполнится только в Python 3")()
    romanize('ru')(lambda: "Код выполнится только в Python 3")()
    romanized('ru')(lambda: "Код выполнится только в Python 3")()
    assert 0

# Generated at 2022-06-13 23:41:58.912373
# Unit test for function romanize
def test_romanize():
    assert romanize('en')(lambda: 'привет')() == 'privet'

# Generated at 2022-06-13 23:42:07.087919
# Unit test for function romanize
def test_romanize():
    assert romanized(locale='kk')(lambda: 'Салам кітап аламын')() == 'Salam kitap alamyn'
    assert romanized(locale='ru')(lambda: 'Салам китап аламын')() == 'Salam kitap alamyn'
    assert romanized(locale='uk')(lambda: 'Салам кітап аламын')() == 'Salam kitap alamyn'

# Generated at 2022-06-13 23:42:15.492557
# Unit test for function romanize
def test_romanize():
    import unittest
    from mimesis.enums import Locale

    @romanize('ru')
    def _cyrillic_text(locale: str = Locale.ENGLISH) -> str:
        """Generate a cyrillic text with the given locale."""
        return 'Привет, добрый день! Хорошего настроения.'

    assert _cyrillic_text() == 'Privet, dobryy den\'! Khoroshchego nastroeniya.'

    class MyTestCase(unittest.TestCase):
        def test_romanize(self):
            from mimesis.enums import Locale


# Generated at 2022-06-13 23:42:18.888178
# Unit test for function romanize
def test_romanize():
    """Test for romanize function."""
    @romanized()
    def test(locale):
        return 'Привет Мир'
    assert 'Privet Mir' == test('en')

# Generated at 2022-06-13 23:42:20.979518
# Unit test for function romanize
def test_romanize():
    @romanize
    def foo(bar):
        return bar

    assert foo('hello') == foo('привет')



# Generated at 2022-06-13 23:42:23.521313
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def some_function():
        return 'Привет Мир!'

    assert some_function() == 'Privet Mir!'

# Generated at 2022-06-13 23:42:33.792014
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    rur_gen = RussiaSpecProvider()
    assert rur_gen.romanize('Абракадабра') == 'Abrakadabra'
    assert rur_gen.romanize('Экстремальная глубина') == 'Ekstremal\'naya glubina'

    rur_gen = RussiaSpecProvider(locale='ru')
    assert rur_gen.romanize('Абракадабра') == 'Abrakadabra'

# Generated at 2022-06-13 23:42:36.270032
# Unit test for function romanize
def test_romanize():
    romanized(locale='ru')
    romanized(locale='uk')
    romanized(locale='kk')

# Generated at 2022-06-13 23:42:37.779094
# Unit test for function romanize
def test_romanize():
    assert romanize('de')(lambda: 'Hello, World!')() == 'Hello, World!'

# Generated at 2022-06-13 23:43:12.589746
# Unit test for function romanize
def test_romanize():
    """Test for romanize decorator."""
    str_1 = 'Добро пожаловать, друг!'
    assert romanized()(str_1) == 'Dobro pozhalovat, drug!'

    str_2 = 'Привет, мир!'
    assert romanized()(str_2) == 'Privet, mir!'

    str_3 = 'Дзень і мясце дзебальнай работы пакажэнне.'

# Generated at 2022-06-13 23:43:16.793846
# Unit test for function romanize
def test_romanize():
    result = romanize('ru')(lambda: 'АбвгдАбвгд')
    assert result == 'AabvgddAabvgdd'

# Generated at 2022-06-13 23:43:19.177451
# Unit test for function romanize
def test_romanize():
    romanized_str = romanize('ru')(lambda: 'привет')
    print('rom')


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:43:24.828001
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.builtins import Text

    word = Text(locale=Locale.RU)
    assert word.word() != romanized(locale=Locale.RU)(word.word)()

# Generated at 2022-06-13 23:43:32.303706
# Unit test for function romanize
def test_romanize():
    @romanized('ru')
    def romanized_ru():
        return 'Привет, Мир!'
    assert romanized_ru() == 'Privet, Mir!'

    @romanized('uk')
    def romanized_uk():
        return 'Привіт, Світ!'
    assert romanized_uk() == 'Pryvit, Svit!'

    @romanized('kk')
    def romanized_kk():
        return 'Сәлем, дүние!'
    assert romanized_kk() == 'Salem, dünie!'



# Generated at 2022-06-13 23:43:40.066387
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person, Generic

    person = Person('ru')
    person.romanize = romanize(locale='ru')(person.romanize)

    person.romanize()
    person.romanize(gender='male')

    person.romanize(gender='male')

    cls = type('Person', (Generic, Person,), {'__locale__': 'ru'})

    p = cls()

    p.romanize = romanize(locale='ru')(p.romanize)

    p.romanize()



# Generated at 2022-06-13 23:43:43.233213
# Unit test for function romanize
def test_romanize():
    @romanize()
    def test_func():
        return 'привет мир'

    assert test_func() == 'privet mir'



# Generated at 2022-06-13 23:43:55.730780
# Unit test for function romanize
def test_romanize():
    """Test for romanize function."""
    import mimesis.builtins

    # Test for romanize decorator
    localizer = mimesis.builtins.Locale(locale='ru')
    assert localizer.full_name() == 'Инокентий Константинович Павлов'
    assert localizer.full_name_male() == 'Андрей Андреевич Казаков'
    assert localizer.full_name_female() == 'Любовь Анатольевна Воробьева'

    # Test for romanized decorator
    assert local

# Generated at 2022-06-13 23:44:04.265346
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    assert Person().name() == 'Богдан'

    test_person = Person(locale='ru')

    assert test_person.name() == 'Богдан'
    assert test_person.romanized().name() == 'Bogdan'

    test_person = Person(locale='uk')
    assert test_person.name() == 'Богдан'
    assert test_person.romanized().name() == 'Bohdan'

    test_person = Person(locale='kk')
    assert test_person.name() == 'Богдан'
    assert test_person.romanized().name() == 'Bagdan'

# Generated at 2022-06-13 23:44:11.158787
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Кириллица')() == 'Kirillitsa'
    assert romanized('uk')(lambda: 'Кирилиця')() == 'Kyrylytsya'
    assert romanized('kk')(lambda: 'Кирилица')() == 'Kirilitsa'



# Generated at 2022-06-13 23:45:12.386932
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Новый год')().capitalize() == 'Novyi god'

# Generated at 2022-06-13 23:45:15.065610
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Война и мир')() == 'Voyna i mir'

# Generated at 2022-06-13 23:45:26.842491
# Unit test for function romanize
def test_romanize():
    """Unit tests for romanize."""
    from mimesis.builtins import CyrillicSpecProvider

    cyr = CyrillicSpecProvider('ru')

    assert cyr.romanize_text('Психология.') == 'Psikhologiya.'
    assert cyr.romanize_text('Символ в музыке') == 'Simvol v muzyke'
    assert cyr.romanize_text('Классификация данных.') == \
        'Klassifikatsiya dannykh.'
    assert cyr.romanize_text('Дроп таблица.') == 'Drop tablitsa.'
    assert c

# Generated at 2022-06-13 23:45:31.156376
# Unit test for function romanize
def test_romanize():
    data.ROMANIZATION_DICT['ru'] = {
        'Б': 'B',
        'б': 'b'
    }
    assert data.ROMANIZATION_DICT['ru'] == {'Б': 'B', 'б': 'b'}



# Generated at 2022-06-13 23:45:37.524528
# Unit test for function romanize
def test_romanize():
    from mimesis.generators import Address
    from mimesis.utils import get_locale

    address = Address(locale=get_locale())
    assert address.street_prefix == 'ул.'
    assert address.street_name == 'Зинаиды Борисовой'

    roman_address = Address(locale=get_locale(), romanized=True)
    assert roman_address.street_prefix == 'ul.'
    assert roman_address.street_name == 'Zinayidy Borisovoy'

# Generated at 2022-06-13 23:45:57.938095
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Привет мир!') == 'Privet mir!'
    assert romanize('ru')(lambda: 'Привет мир!') == 'Privet mir!'
    assert romanize('uk')(lambda: 'Привіт світ!') == 'Pryvit svit!'
    assert romanize('kk')(lambda: 'Сәлем дүние!') == 'Sälem dünie!'

# Generated at 2022-06-13 23:46:06.999042
# Unit test for function romanize
def test_romanize():
    alphabet = {s: s for s in
                ascii_letters + digits + punctuation}
    
    alphabet.update({
        **data.ROMANIZATION_DICT['ru'],
        **data.COMMON_LETTERS,
    })
    from mimesis.providers.address import Address
    a = Address('ru')
    result = a.address()
    txt = ''.join([alphabet[i] for i in result if i in alphabet])
    print('test_romanize', result, txt)

    
if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:46:08.131112
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:46:13.998282
# Unit test for function romanize
def test_romanize():  # pragma: no cover
    """Runs unit-test for function romanize."""
    import mimesis.builtins.text
    t = mimesis.builtins.text.Text('ru')
    assert t.romanize() == t.romanize('ru')
    assert t.romanized() == t.romanize()
    assert t.romanize('kk') == \
      'KazaHstan daIyrydarynda BarlyH tazaIynyH ' + \
      'kim boIyIsyH?'
    assert t.romanized('kk') == t.romanize('kk')

# Generated at 2022-06-13 23:46:23.065084
# Unit test for function romanize
def test_romanize():
    # Default romanization test
    @romanize('ru')
    def get_word(_):
        return 'Здравствуйте'
    s = get_word(0)
    assert s == 'Zdravstvujte'

    # Use of romanize decorator for Ukrainian
    @romanize('uk')
    def get_word_uk(_):
        return 'Вітаю'
    s = get_word_uk(0)
    assert s == 'Vitayu'

    # Use of romanize decorator for Kazakh
    @romanize('kk')
    def get_word_kk(_):
        return 'Сәлем'
    s = get_word_kk(0)
    assert s == 'Sälem'

# Generated at 2022-06-13 23:48:03.933726
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет')() == 'privet'
    assert romanized('ru')(lambda: 'Привет')() == 'privet'
    assert romanized('uk')(lambda: 'Привіт')() == 'pryvit'
    assert romanized('kk')(lambda: 'Привет')() == 'privet'
    assert romanized('zz')(lambda: 'Привет')() == 'privet'



# Generated at 2022-06-13 23:48:13.171239
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person
    from mimesis.enums import Gender

    p = Person('uk')
    assert p.full_name(gender=Gender.FEMALE).isalpha() is True
    assert p.full_name(gender=Gender.FEMALE).islower() is True
    assert p.full_name(gender=Gender.FEMALE) == 'Василь Куцик'

    assert p.full_name(gender=Gender.FEMALE, roman=True).isalpha() is True
    assert p.full_name(gender=Gender.FEMALE, roman=True).islower() is True
    assert p.full_name(gender=Gender.FEMALE, roman=True) == 'vasyl kutsik'

# Generated at 2022-06-13 23:48:27.449348
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language

    from .generic import Generic

    g = Generic(Language.RUSSIAN)
    text = g.text.cyrillic()
    # If a model does not have a romanization dictionary,
    # then the function should return the same text.
    assert romanize('ro')(lambda: text)() == text
    assert romanize('en')(lambda: text)() == text
    # If a model has a romanization dictionary,
    # then the function should return the romanized text.
    assert romanize('ru')(lambda: text)() != text
    assert romanize('uk')(lambda: text)() != text
    assert romanize('kk')(lambda: text)() != text

# Generated at 2022-06-13 23:48:34.689507
# Unit test for function romanize
def test_romanize():
    import sys

    assert sys.version_info >= (3, 7)

    class TestClass(object):

        @staticmethod
        @romanize('ru')
        def get_romanized(text: str) -> str:
            return text

    assert TestClass.get_romanized('здравствуйте') == 'zdravstvujte'

# Generated at 2022-06-13 23:48:38.787878
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def foo(seed):
        return 'СиСиКей'

    @romanize()
    def bar(seed):
        return 'СиСиКей'

    assert foo(seed=10) == 'SiSiKey'
    assert bar(seed=10) == 'SiSiKey'

# Generated at 2022-06-13 23:48:45.085315
# Unit test for function romanize
def test_romanize():
    def old_romanize(s):
        alphabet = {s: s for s in
                    ascii_letters + digits + punctuation}
        alphabet.update({
            **data.COMMON_LETTERS,
            **data.ROMANIZATION_DICT['ru'],
        })
        return ''.join([alphabet[i] for i in s if i in alphabet])

    romanize_ru = romanize('ru')

    assert romanize_ru(old_romanize('привет')) == 'privet'

# Generated at 2022-06-13 23:48:55.640799
# Unit test for function romanize
def test_romanize():
    from string import ascii_letters, digits, punctuation

    def cat(s): return s
    assert cat('абвгд') == 'абвгд'
    assert cat(12345) == 12345

    cat = romanized()(cat)
    assert cat('абвгд') == 'abvgd'
    assert cat(12345) == 12345

    cat = romanized('ru')(cat)
    assert cat('абвгд') == 'abvgd'
    assert cat(12345) == 12345

    cat = romanized('uk')(cat)
    assert cat('абвгд') == 'abvhd'
    assert cat(12345) == 12345

    cat = romanized('kk')(cat)
   

# Generated at 2022-06-13 23:48:58.876159
# Unit test for function romanize
def test_romanize():
    text = 'Привет мир!'
    assert romanized('ru')(lambda: text)() == 'Privet mir!'

# Generated at 2022-06-13 23:49:00.900010
# Unit test for function romanize
def test_romanize():
    assert 'test' == romanized()('test')



# Generated at 2022-06-13 23:49:08.744338
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    from mimesis.builtins import RussianSpecProvider

    class Romanized(RussianSpecProvider):
        @romanize()
        def get_fake(self) -> str:
            return 'Съешь же ещё этих мягких французских булок, да выпей чаю.'

    r = Romanized()
    assert r.get_fake() == 'Seezh uze eshchjo etikh mjagkikh frantcuzskikh \
bulkov, da vypej chaju.'
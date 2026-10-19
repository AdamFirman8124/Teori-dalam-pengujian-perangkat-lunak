

# Generated at 2022-06-13 23:39:38.149784
# Unit test for function romanize
def test_romanize():
    """Test romanized method."""
    assert romanize('ru')(lambda: '')() == ''
    assert romanize('uk')(lambda: '')() == ''
    assert romanize('kk')(lambda: '')() == ''

# Generated at 2022-06-13 23:39:43.273599
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foobar():
        return 'Добро пожаловать в мир Python!'

    assert foobar() == 'Dobro pozhalovatʹ v mir Python!'

# Generated at 2022-06-13 23:39:52.245564
# Unit test for function romanize

# Generated at 2022-06-13 23:39:53.560748
# Unit test for function romanize
def test_romanize():
    romanize('ru')

# Generated at 2022-06-13 23:39:55.094734
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanized()

# Generated at 2022-06-13 23:40:00.113942
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person('ru')
    assert p.full_name(gender=Gender.MALE) == 'Геннадий Петров'

    p = Person('en')
    assert p.full_name(gender=Gender.MALE) == 'Gennady Petrov'



# Generated at 2022-06-13 23:40:03.224647
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Кот за рыбой.')() == 'Kot za ryboj.'

# Generated at 2022-06-13 23:40:05.836193
# Unit test for function romanize
def test_romanize():
    @romanize()
    def rus_text():
        return 'Привет, Мир!'

    assert rus_text() == 'Privet, Mir!'

# Generated at 2022-06-13 23:40:15.852857
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def ru_name(seed=None):
        return 'Василий'

    assert ru_name() == 'Vasiliy'

    @romanize(locale='uk')
    def uk_name(seed=None):
        return 'Василь'

    assert uk_name() == 'Vasyl'

    @romanize(locale='kk')
    def kz_name(seed=None):
        return 'Батыр'

    assert kz_name() == 'Battir'

    @romanize(locale='en')
    def en_name(seed=None):
        return 'Василий'

    assert en_name() == 'Vasiliy'

# Generated at 2022-06-13 23:40:23.560508
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins.words

    plain_text = mimesis.builtins.words.Words('ru')

    words_plain = plain_text.word()

    @romanize()
    def romanize_word():
        return words_plain

    romanized_word = romanize_word()
    assert romanized_word != words_plain

# Generated at 2022-06-13 23:40:35.796776
# Unit test for function romanize
def test_romanize():
    assert 'ПРИВЕТ' == romanize()(lambda x: 'ПРИВЕТ')
    assert 'ПРИВЕТ' == romanized()(lambda x: 'ПРИВЕТ')
    assert 'PRIVET' == romanize('ru')(lambda x: 'ПРИВЕТ')
    assert 'PRIVET' == romanized('ru')(lambda x: 'ПРИВЕТ')

# Generated at 2022-06-13 23:40:45.307534
# Unit test for function romanize
def test_romanize():
    # For backward compatibility
    assert romanize == romanized
    assert romanize == romanize('')

    @romanize('')
    def romanize_word(word: str) -> str:
        return word

    # Russian
    text = 'Привет, мир!'
    assert romanize_word(text) == 'Privet, mir!'

    # Ukrainian
    text = 'Привіт, світ!'
    romanize_uk = romanize('uk')
    assert romanize_uk(romanize_word)(text) == 'Pryvit, svit!'

# Generated at 2022-06-13 23:40:48.800282
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person, PersonBase
    p = Person('ru')

    @romanize('ru')
    def test_romanize(text):
        return text

    assert test_romanize(p.full_name) == p.full_name_latin



# Generated at 2022-06-13 23:40:52.653345
# Unit test for function romanize
def test_romanize():
    def test_func(number):
        return f'{number}'

    @romanize()
    def test_func(number):
        return f'{number}'

    assert test_func(1) == '1'

    @romanize('uk')
    def test_func(number):
        return f'{number}'

    assert test_func(1) == '1'

# Generated at 2022-06-13 23:40:59.356745
# Unit test for function romanize
def test_romanize():
    assert 'test' == romanize('en')(lambda:'test')()
    assert 'тест' == romanize('ru')(lambda:'test')()
    assert '№123' == romanize('ru')(lambda:'№123')()
    assert '№123' == romanize('en')(lambda:'№123')()


# Generated at 2022-06-13 23:41:02.507912
# Unit test for function romanize
def test_romanize():
    @romanize()
    def generate_string():
        return 'Мне нравится'

    assert generate_string() == 'Mnye nravitsya'

# Generated at 2022-06-13 23:41:14.306002
# Unit test for function romanize

# Generated at 2022-06-13 23:41:17.776303
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def rus():
        return 'Привет, Мир!'

    assert rus() == 'Privet, Mir!'

# Generated at 2022-06-13 23:41:23.267202
# Unit test for function romanize
def test_romanize():
    @romanize()
    def test_func(x):
        return x

    result = test_func('Мимзис де роман іпсум долор сіт амет')
    assert result == 'Mimzis de roman ipsum dolor sit amet'

# Generated at 2022-06-13 23:41:35.396935
# Unit test for function romanize
def test_romanize():
    try:
        rom = romanize('ru')
        res = rom(lambda: "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!")
        assert res == "V chascah iugz zhil by tsitrus? Da, no falshivyy ekzempliar!"
    except UnsupportedLocale:
        assert True



# Generated at 2022-06-13 23:41:45.232384
# Unit test for function romanize
def test_romanize():
    class Provider:
        @romanize(locale='ru')
        def russian(self):
            return 'Привет, Мир!'

        @romanize(locale='kk')
        def kazakh(self):
            return 'Сәлем, Әлем!'

    provider = Provider()
    assert provider.russian() == 'Privet, Mir!'
    assert provider.kazakh() == 'Salem, Alem!'

# Generated at 2022-06-13 23:41:49.268457
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def text(value):
        return value

    assert text('До свидания') == 'Do svidaniya'

# Generated at 2022-06-13 23:42:00.339711
# Unit test for function romanize
def test_romanize():
    assert romanize('en')(lambda: '')() == ''
    assert romanize('ru')(lambda: 'Съешь же ещё этих мягких '
                          'французских булочек'
                          )() == 'S`esh` zhe yeshchyo etikh miagkikh ' \
                                 'frantsuzskikh bulochek'

# Generated at 2022-06-13 23:42:06.837313
# Unit test for function romanize
def test_romanize():
    # String: "Овој е еден тест на романски."
    expected = 'Ovoi e eden test na romanski.'
    s = lambda x: x
    transliterated = romanize('mk')(s)
    assert transliterated('Овој е еден тест на романски.') == expected



# Generated at 2022-06-13 23:42:11.365232
# Unit test for function romanize
def test_romanize():
    assert romanize_text('Привет, Мир!') == 'Privet, Mir!'
    assert romanize_text('Привет, Мир!', locale='blah') == 'Privet, Mir!'

# Test for backward compatibility

# Generated at 2022-06-13 23:42:18.148391
# Unit test for function romanize
def test_romanize():
    import random
    romanize_test = romanize('ru')
    random_cyrillic = ''.join([random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for x in range(50)])
    assert random_cyrillic == romanize_test(lambda : random_cyrillic)

# Generated at 2022-06-13 23:42:20.289626
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Каждый')() == 'Kazhdyi'

# Generated at 2022-06-13 23:42:28.347740
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет, мир!')() == 'Privet, mir!'
    assert romanize('uk')(lambda: 'Привіт, світ!')() == 'Pryvit, svit!'
    assert romanize('kk')(lambda: 'Қалайсың, дүние!')() == 'Qalaısıñ, dünie!'
    assert romanize('en')(lambda: 'Hello, world!')() == 'Hello, world!'

# Generated at 2022-06-13 23:42:35.671070
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.person import Person
    from mimesis.enums import Gender
    p = Person(locale='ru')
    assert p.full_name(gender=Gender.MALE) == 'Гаврила Зайцев'
    assert p.full_name(romanize=True, gender=Gender.MALE) == 'Gavryla Zaitsev'
    assert p.full_name(romanize=True, gender=Gender.MALE) != 'Gavryla Zaytsev'

# Generated at 2022-06-13 23:42:37.855103
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import CyrillicProvider

    a = CyrillicProvider()
    assert a.personal.full_name() == a.personal.full_name(romanize=True)

# Generated at 2022-06-13 23:42:58.580014
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def russify(txt):
        return txt

    assert russify('Привет, мир!') == 'Hello, world!'

    @romanize('uk')
    def ukrainify(txt):
        return txt

    assert ukrainify('Вітаю, світ!') == 'Vitayu, svit!'

    @romanize('kk')
    def kazakhify(txt):
        return txt

    assert kazakhify('Сәлем, дүние!') == 'Salem, dunie!'

# Generated at 2022-06-13 23:43:03.274310
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def get_name(seed: int = None) -> str:
        return 'Иванов'

    assert get_name() == 'Ivanov'

# Generated at 2022-06-13 23:43:09.956273
# Unit test for function romanize
def test_romanize():
    import mimesis.enums
    from mimesis.providers.person import Person

    person = Person('uk')
    person.get_full_name()
    person.get_full_name(gender=mimesis.enums.Gender.MALE)
    person.get_full_name(gender=mimesis.enums.Gender.FEMALE)

# Generated at 2022-06-13 23:43:17.827277
# Unit test for function romanize
def test_romanize():
    # This function is for testing the function romanize

    words = ['Кококошка', 'Главное́']

    # Create a closure that needs to be tested
    @romanize()
    def wrapper(*args, **kwargs):
        return args

    # Assertion
    assert romanized()(wrapper)(*words) == ['Kokokoshka', 'Glavnoe']

# Generated at 2022-06-13 23:43:30.929951
# Unit test for function romanize
def test_romanize():
    def check(s: str, t: str) -> bool:
        return s.isalpha() and (s != '' and t != '')

    import pytest
    from mimesis.builtins.en import Text

    t = Text()

    @romanize(locale='ru')
    def string_ru() -> str:
        return t.word(quantity=10, seed=666)

    @romanize(locale='uk')
    def string_uk() -> str:
        return t.word(quantity=10, seed=666)

    @romanize(locale='kk')
    def string_kk() -> str:
        return t.word(quantity=10, seed=666)

    assert check(string_ru(), t.romanize(string_ru(), locale='ru'))

# Generated at 2022-06-13 23:43:33.629854
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'Двигатель')() == 'Dvigatel'

# Generated at 2022-06-13 23:43:38.424016
# Unit test for function romanize
def test_romanize():
    # AssertionError
    romanize('_')

    @romanize()
    def _symbol():
        return '1'

    @romanize()
    def _letter():
        return 'а'

    assert _symbol() == '1'
    assert _letter() == 'a'

# Generated at 2022-06-13 23:43:41.359178
# Unit test for function romanize
def test_romanize():
    # Arrange
    def test_func() -> str:
        return 'Привіт'

    expected = 'Pryvit'

    # Act
    actual = romanize()(test_func)()

    # Assert
    assert expected == actual

# Generated at 2022-06-13 23:43:53.779434
# Unit test for function romanize
def test_romanize():
    """Test for romanize decorator."""
    from mimesis.builtins import MoscowSpecProvider
    from mimesis.enums import Gender
    from mimesis.providers.person.en import EnglishPerson

    moscow = MoscowSpecProvider(locale='ru')
    faker = EnglishPerson(locale='en')

    # Decorator with locale
    @romanize(locale='uk')
    def ukr(gender: Gender = Gender.FEMALE) -> str:
        return moscow.full_name(gender)

    uk = ukr()
    assert uk != moscow.full_name()
    assert uk.isalpha()
    assert uk.replace(' ', '').isalpha()

    # Decorator without locale

# Generated at 2022-06-13 23:44:00.711148
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis import Generic

    r = RussiaSpecProvider(None)
    g = Generic('ru')
    assert g.region_code() == 'Республика Марий Эл'
    assert r.region_code() == 'Республика Марий Эл'


test_romanize()

# Generated at 2022-06-13 23:44:26.456657
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda x: 'Hello my friend!')() == 'Hello my friend!'
    assert romanize()(lambda x: 'Привет мой друг!')() == 'Privet moy drug!'

# Generated at 2022-06-13 23:44:29.677283
# Unit test for function romanize
def test_romanize():
    # Should return True
    assert romanize('ru')(lambda: 'Солнце')() == 'Solnce'

# Generated at 2022-06-13 23:44:34.154611
# Unit test for function romanize
def test_romanize():
    @romanize('kk')
    def romanize_test():
        return 'Кәтiр-Қазақ'
    assert romanize_test() == 'Katir-Qazaq'

# Generated at 2022-06-13 23:44:36.908324
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda s: "Привет мир!") == 'Privet, mir!'

# Generated at 2022-06-13 23:44:40.790329
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'а')() == 'a'
    assert romanize()(lambda: 'б')() == 'b'
    assert romanize()(lambda: 'в')() == 'v'

# Generated at 2022-06-13 23:44:58.536264
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.numbers import Numbers
    from mimesis.enums import Language

    num = Numbers(Language.RU)
    assert isinstance(num.romanize('Тестовая строка'), str)

    num = Numbers(Language.UK)
    assert isinstance(num.romanize('Тестова рядок'), str)

    num = Numbers(Language.KK)
    assert isinstance(num.romanize('Тесттік жол'), str)

# Generated at 2022-06-13 23:45:09.329438
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'Привет')() == 'Privyet'
    assert romanize('kk')(lambda x: 'Привет')() == 'Pryvyet'
    assert romanize('uk')(lambda x: 'Привет')() == 'Pryvit'
    assert romanize('uk')(lambda x: 'Мир')() == 'Myry'

# Generated at 2022-06-13 23:45:20.218262
# Unit test for function romanize
def test_romanize():
    # Russian
    assert 'Привет, мир' == romanized('ru')(lambda: 'Privet, mir')
    # Ukrainian
    assert 'Привіт, світ' == romanized('uk')(lambda: 'Pryvit, svit')
    # Kazah
    assert 'Сәлем, дүние' == romanized('kk')(lambda: 'Salem, dunie')
    # Unsupported locale
    try:
        romanized('UnsupportedLocale')(lambda: 'Привет')
    except UnsupportedLocale as e:
        assert str(e) == 'UnsupportedLocale'

# Generated at 2022-06-13 23:45:30.700662
# Unit test for function romanize
def test_romanize():
    import doctest

    doc_test = """
    >>> from mimesis import Person
    >>> person = Person()
    >>> person.full_name(locale='ru')
    'Настюша Шумова'
    >>> person.full_name(locale='uk')
    'Софія Рахімюдзе'
    >>> person.full_name(locale='ru', romanize=True)
    'Nastyusa Shumova'

    """

    result = doctest.testmod(m=Person)
    assert result.failed == 0, result.failed

    result = doctest.testmod(m=doc_test)
    assert result.failed == 0, result.failed

# Generated at 2022-06-13 23:45:39.080260
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    ru = RussiaSpecProvider()
    ru.seed(1)

    romanized_text = ru.full_name()
    assert romanized_text == ru.romanize(ru.full_name())

    romanized_text = ru.custom_full_name(pattern='#P#B')
    assert romanized_text == ru.romanize(ru.custom_full_name(pattern='#P#B'))

    romanized_text = ru.custom_full_name(pattern='#P#B#P')
    assert romanized_text == ru.romanize(ru.custom_full_name(pattern='#P#B#P'))

    romanized_text = ru.full_name(pattern='#P#B#P')
    assert r

# Generated at 2022-06-13 23:46:39.468248
# Unit test for function romanize
def test_romanize():
    # Code before using decorator
    assert romanized('ru')('Привет') == 'Privet'

# Generated at 2022-06-13 23:46:45.626600
# Unit test for function romanize
def test_romanize():
    langs = ['ru', 'kk', 'uk', 'en']
    fake = data.Data(locale='ru')
    assert all([fake.words(10).romanize() == fake.words(10) for lang in langs])
    assert all([fake.words(10).romanize(lang) == fake.words(10) for lang in langs])

# Generated at 2022-06-13 23:46:58.212469
# Unit test for function romanize
def test_romanize():
    import string
    import random
    import inspect
    import unittest

    mimesis = __import__('mimesis')
    locales = inspect.getmembers(mimesis.data, inspect.isclass)

    class TestRomanize(unittest.TestCase):
        def setUp(self):
            self.allchars = string.printable
            self.idx = [x for x in range(len(self.allchars))]

        def test_create_random_text(self):
            for _ in range(100):
                text = ''
                for _ in range(100):
                    text += self.allchars[random.choice(self.idx)]

                self.assertTrue(len(text) > 0)


# Generated at 2022-06-13 23:46:58.862619
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:47:08.931090
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo():
        return 'Привет, Мир!'

    assert foo() == 'Privet, Mir!'

    @romanize('uk')
    def boo():
        return 'Привіт, Світ!'

    assert boo() == 'Pryvit, Svit!'

    @romanize('kk')
    def bar():
        return 'Қалай амансызбы?'

    assert bar() == 'Qalaı amansyzby?'

# Generated at 2022-06-13 23:47:17.224695
# Unit test for function romanize
def test_romanize():
    from string import ascii_letters, digits, punctuation

    def romanize_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            alphabet = {s: s for s in
                        ascii_letters + digits + punctuation}

            alphabet.update({
                **data.ROMANIZATION_DICT['en'],
                **data.COMMON_LETTERS,
            })

            result = func(*args, **kwargs)
            txt = ''.join([alphabet[i] for i in result if i in alphabet])
            return txt

        return wrapper

    @romanize_deco
    def foo():
        return 'привет, Киев!'


# Generated at 2022-06-13 23:47:19.542033
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    from mimesis.builtins import Cyrillic

    assert romanize('ru')(Cyrillic().word)()

# Generated at 2022-06-13 23:47:23.362840
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    p = Person('en')
    # TODO: add a romanization-capable provider in the future.
    p.vk = romanize('ru')(p.vk)
    assert isinstance(p.vk(), str)

# Generated at 2022-06-13 23:47:30.956396
# Unit test for function romanize
def test_romanize():
    """Tests for romanize."""
    assert romanized()(lambda: 'Привет, Мир!')() == 'Privet, Mir!'
    assert romanized()(lambda: 'АБВ')() == 'ABV'
    assert romanized('ru')(lambda : 'Привет, Мир!')() == 'Privet, Mir!'
    assert romanized('uk')(lambda : 'Привіт, світ!')() == 'Privit, svit!'
    assert romanized('kk')(lambda : 'Сәлем, дүние!')() == 'Salem, dunie!'

# Generated at 2022-06-13 23:47:39.253035
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    from mimesis.enums import Gender
    from mimesis.providers import Address

    addr = Address(locale='ru')

    @romanized('ru')
    def get_locale():
        return addr.locality()

    assert get_locale() == 'Александров'

    @romanized('ru')
    def get_city():
        return addr.city()

    assert get_city() == 'Александров'

    @romanized('ru')
    def get_country():
        return addr.country()

    assert get_country() == 'Россия'

    @romanized('ru')
    def get_street():
        return addr.street_name()

   

# Generated at 2022-06-13 23:49:17.069980
# Unit test for function romanize
def test_romanize():
    text = (
        'УТОЧНИТЕ, ПОЖАЛУЙСТА, ВАШИ ФАМИЛИЮ И ИМЯ ПО ПАСПОРТУ.'
        'Обязательно с ДЕФИСОМ!'
    )

# Generated at 2022-06-13 23:49:20.877534
# Unit test for function romanize
def test_romanize():
    result = romanize()
    assert result

if __name__ == '__main__':
    print(test_romanize())

# Generated at 2022-06-13 23:49:25.180547
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def text_generator(text: str = None):
        return text.lower()

    assert text_generator('Санкт-Петербург') == 'sankt-peterburg'

# Generated at 2022-06-13 23:49:28.359688
# Unit test for function romanize
def test_romanize():
    result = romanize('ru')(lambda: 'ПриветМир')
    assert result == 'PrivetMir'
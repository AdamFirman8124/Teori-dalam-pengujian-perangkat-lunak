

# Generated at 2022-06-13 23:39:30.618839
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'кот')() == 'kot'


# Generated at 2022-06-13 23:39:34.769319
# Unit test for function romanize
def test_romanize():
    def romanized_func():
        return 'привет'

    @romanized()
    def romanized_func_deco():
        return 'привет'

    assert romanized_func_deco() == 'privet'
    assert romanize()(romanized_func)() == 'privet'

# Generated at 2022-06-13 23:39:38.547346
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет!')() == 'Privet!'
    assert romanize('uk')(lambda: 'Привіт!')() == 'Pryvit!'

# Generated at 2022-06-13 23:39:40.082043
# Unit test for function romanize
def test_romanize():
    assert romanize is romanized

# Generated at 2022-06-13 23:39:45.139832
# Unit test for function romanize
def test_romanize():
    assert romanize()(str)().isascii()
    assert romanize(locale='ru')(str)().isascii()
    assert romanize(locale='uk')(str)().isascii()
    assert romanize(locale='kk')(str)().isascii()

# Generated at 2022-06-13 23:39:46.274225
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""
    assert romanize()

# Generated at 2022-06-13 23:39:53.818586
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def ru_func():
        return 'Съешь ещё этих мягких французских булок, да выпей чаю.'

    assert ru_func() == 'Sesh eshyo etikh myagkikh frantsuzskikh bulok, da ' \
                        'vypey chayu.'


# Generated at 2022-06-13 23:40:01.241538
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def get_rus_text():
        return 'Пример русского текста'

    txt = get_rus_text()
    assert txt == 'Primer russkogo teksta'

    @romanize
    def get_rus_text():
        return 'Пример русского текста'

    txt = get_rus_text()
    assert txt == 'Primer russkogo teksta'



# Generated at 2022-06-13 23:40:06.648105
# Unit test for function romanize
def test_romanize():
    assert (romanize('ru')(lambda: 'бирюк')()) == 'birük'
    assert (romanize('uk')(lambda: 'хиба'))() == 'khiba'
    assert (romanize('ru')(lambda: 'бирюк'))() == 'birük'



# Generated at 2022-06-13 23:40:16.432973
# Unit test for function romanize
def test_romanize():
    # Test for case when invalid locale provided

    # noinspection PyUnusedLocal
    @romanize(locale='xx')
    def romanize_test(*args, **kwargs):
        return 'test'

    try:
        romanize_test()
    except UnsupportedLocale:
        pass
    else:
        raise AssertionError('Unsupported locale')

    # Test for case when function returns non-cyrillic result

    # noinspection PyUnusedLocal
    @romanize(locale='ru')
    def romanize_test2(*args, **kwargs):
        return '123456!@#$%^&*()_+'

    result = romanize_test2()
    assert result == '123456!@#$%^&*()_+', 'Not expected result'

    # Test for

# Generated at 2022-06-13 23:40:28.616245
# Unit test for function romanize
def test_romanize():
    """Test for romanize()."""
    assert romanize()(lambda: 'Я люблю много сложных многосложных слов')() == \
        'Ya lyublyu mnogo slozhnykh mnogosloznykh slov'



# Generated at 2022-06-13 23:40:35.094055
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'проверка')() == 'proverka'
    assert romanize(locale='uk')(lambda: 'перевірка')() == 'pereverka'
    assert romanize(locale='kk')(lambda: 'тестілеу')() == 'testileu'
    assert romanize(locale='uz')(lambda: 'тестилаш')() == 'testilash'

# Generated at 2022-06-13 23:40:45.686410
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    import json
    import os
    from mimesis.providers.text import Text

    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(
        current_dir,
        '../mimesis/data/romanization.json')) as data_file:
        data = json.load(data_file)

    for code in data:
        test_object = Text(code)
        text = test_object.word()
        romanized_word = test_object.romanized(text)
        romanized_text = test_object.romanized()
        assert all([text, romanized_word, romanized_text])

# Generated at 2022-06-13 23:40:50.801992
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Text
    text = Text('ru')
    arabic = text.sentence(length=200)
    latin = romanize('ru')(lambda: arabic)()
    assert arabic != latin
    assert 'Заглавная буква' in arabic
    assert 'Zaglavnaya bukva' in latin

# Generated at 2022-06-13 23:40:53.124370
# Unit test for function romanize
def test_romanize():
    def test_func(test_string):
        return test_string

    assert romanize(locale='ru')(test_func)('Привет, Мир!') == 'Privet, Mir!'

# Generated at 2022-06-13 23:41:01.540551
# Unit test for function romanize
def test_romanize():
    assert romanize("ru")("тест") == "test"
    assert romanize("uk")("тест") == "test"
    assert romanize("kk")("тест") == "test"
    assert ascii_letters + digits + punctuation == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!""#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Generated at 2022-06-13 23:41:09.661593
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.random import Random
    from mimesis.providers.person import Person

    random = Random()
    random.set_locale('uk')

    person = Person(random=random)

    assert person.gender(gender=Gender.FEMALE) == 'жінка'
    assert person.username(gender=Gender.MALE) == 'ПавлоДолужний'
    assert person.text(quantity=10) == 'Хлопців Комзаков місце.'
    assert person.name(gender=Gender.MALE) == 'РоманОмелько'

# Generated at 2022-06-13 23:41:14.601555
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: True)() == 'true'
    assert romanize('ru')(lambda: False)() == 'false'
    assert romanize('ru')(lambda: 123)() == '123'
    assert romanize('ru')(lambda: 'hello world')() == 'hello world'



# Generated at 2022-06-13 23:41:19.965995
# Unit test for function romanize
def test_romanize():
    """Test function ``romanize``."""
    r_function = romanize('ru')

    @r_function
    def r(value):
        return value

    assert r('Привет, Мир!') == 'Privet, Mir!'

    r_function = romanize()

    @r_function
    def r(value):
        return value

    assert r('Привет, Мир!') == 'Priwet, Mir!'

# Generated at 2022-06-13 23:41:25.202866
# Unit test for function romanize
def test_romanize():
    def romanized_func():
        return "Привет, Мир!"

    romanized = romanize('ru')
    romanized_func = romanized(romanized_func)
    assert romanized_func() == 'Privet, Mir!'



# Generated at 2022-06-13 23:41:44.287936
# Unit test for function romanize
def test_romanize():
    def inner_romanize(locale=''):
        @romanize(locale=locale)
        def func():
            return 'Привет мир'

        return func()

    assert inner_romanize(locale='ru') == 'Privet mir'
    assert inner_romanize(locale='uk') == 'Pryvit svit'
    assert inner_romanize(locale='kk') == 'Salam dünya'
    assert inner_romanize(locale='undefined') == 'Privet svit'

# Generated at 2022-06-13 23:41:45.107850
# Unit test for function romanize
def test_romanize():
    assert romanize()



# Generated at 2022-06-13 23:41:51.456484
# Unit test for function romanize
def test_romanize():
    import time
    from mimesis.builtins.text import Text
    start_time = time.time()
    text = Text()
    for i in range(100):
        text.romanize(text='Привет мир')
    print("--- %s seconds ---" % (time.time() - start_time))

# Generated at 2022-06-13 23:42:01.687395
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    @romanize(locale='ru')
    def get_ru_text() -> str:
        """Get russian text."""
        return 'Привет мир!'

    assert get_ru_text() == 'Privet mir!'

    @romanize(locale='uk')
    def get_uk_text() -> str:
        """Get ukranian text."""
        return 'Веселе бурштину'

    assert get_uk_text() == 'Vesele burshtynu'

    @romanize(locale='kk')
    def get_kk_text() -> str:
        """Get kazakh text."""

# Generated at 2022-06-13 23:42:07.270238
# Unit test for function romanize
def test_romanize():
    def foo():
        return 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    # Should return latin string, not cyrillic
    assert romanize('ru')(foo)() != foo()

# Generated at 2022-06-13 23:42:15.566335
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    from mimesis.enums import Language

    def romanize_text(input: str, locale: str) -> str:
        @romanize(locale)
        def get_romanized(input):
            return input

        return get_romanized(input)

    assert romanize_text('这是一个测试', Language.EN) == '这是一个测试'
    assert romanize_text('Неща подобни на това', Language.BG) == 'Neshcha podobni na tova'

# Generated at 2022-06-13 23:42:16.885273
# Unit test for function romanize
def test_romanize():
    assert romanize.__doc__ is not None



# Generated at 2022-06-13 23:42:27.631161
# Unit test for function romanize
def test_romanize():
    import unittest
    from mimesis.enums import Language
    from mimesis.providers.lorem import Lorem

    lorem = Lorem(Language.ENGLISH)
    # Need to write some tests for romanize function
    assert lorem.text() == 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.'

# Generated at 2022-06-13 23:42:28.667507
# Unit test for function romanize
def test_romanize():
    assert not romanize()

test_romanize()

# Generated at 2022-06-13 23:42:34.702991
# Unit test for function romanize
def test_romanize():
    cases = ['Ночь.', 'Доброе утро, мир!',
             'Мы сегодня создадим текстовый процессор.']

    from mimesis import Generic
    gen = Generic('en')

    for case in cases:
        assert romanize(case) == gen.text.romanized(case)

# Generated at 2022-06-13 23:43:01.713925
# Unit test for function romanize
def test_romanize():
    # test with custom function to compare
    @romanized(locale='ru')
    def ru_roman(size: int = 6):
        return 'АПАРАТНЫЙ И ПРОГРАММНЫЙ'
    assert ru_roman(size=25) == 'APARATNYI I PROGRAMNYI'

    # test with custom function to compare
    @romanize(locale='ru')
    def ru_roman(size: int = 6):
        return 'АПАРАТНЫЙ И ПРОГРАММНЫЙ'

# Generated at 2022-06-13 23:43:06.894481
# Unit test for function romanize
def test_romanize():
    # example
    assert romanized('ru')(lambda: 'Съешь же ещё эти фасоли')() \
        == 'Syesh zhe yeshcho eti fasoli'

# Generated at 2022-06-13 23:43:08.772738
# Unit test for function romanize
def test_romanize():
    assert not romanize('en')(lambda: None)()



# Generated at 2022-06-13 23:43:18.448797
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'привет')().lower() == 'privet'
    assert romanize('uk')(lambda: 'привіт')().lower() == 'pryvit'
    assert romanize('kk')(lambda: 'сәлем')().lower() == 'salem'
    try:
        romanize('fr')(lambda: 'привет')()
    except UnsupportedLocale:
        assert True
    else:
        assert False

# Generated at 2022-06-13 23:43:26.201492
# Unit test for function romanize
def test_romanize():
    import unittest

    def test_romanize(self):
        # Test for romanize function
        self.assertEqual(romanize(locale='ru')(lambda: 'привет')(), 'privet')
        self.assertEqual(romanized(locale='ru')(lambda: 'привет')(), 'privet')

    unittest.main()

# Generated at 2022-06-13 23:43:37.036043
# Unit test for function romanize

# Generated at 2022-06-13 23:43:40.219496
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda : 'проверка')() == 'proverka'
    assert romanized()(lambda : 'проверка')() == 'proverka'

# Generated at 2022-06-13 23:43:45.356866
# Unit test for function romanize
def test_romanize():
    @romanize()
    def romanized_func():
        return 'Слюнявчик'

    assert romanized_func() == 'Slyunyavchik'


if __name__ == "__main__":
    test_romanize()

# Generated at 2022-06-13 23:43:50.841541
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def get_romanized_text():
        return 'Привет, Как дела? Как тебя зовут?'

    assert get_romanized_text() == 'Privet, Kak dela? Kak tebya zovut?'

# Generated at 2022-06-13 23:43:54.988133
# Unit test for function romanize
def test_romanize():
    text = 'русский язык'
    assert romanize(locale='ru')(lambda x: x)(text) == 'russkiy yazyk'



# Generated at 2022-06-13 23:44:58.522451
# Unit test for function romanize
def test_romanize():
    def f():
        return 'Думай как программист, пиши как дизайнер'
    f_romanized = romanize('ru')(f)
    assert f_romanized() == 'Dumaĭ kak programmist, piši kak dizajner'
    assert f_romanized('en_US') == 'Dumaĭ kak programmist, piši kak dizajner'
    assert f_romanized('ru') == 'Dumaĭ kak programmist, piši kak dizajner'


# Generated at 2022-06-13 23:45:03.419344
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    @romanize()
    def get_hello():
        return 'Привет'

    assert get_hello() == 'Privet'

    @romanize(locale='ru')
    def get_so_much():
        return 'Сколько времени?'

    assert get_so_much() == 'Skolko vremeni?'

# Generated at 2022-06-13 23:45:05.923694
# Unit test for function romanize
def test_romanize():
    """Test for romanize decorator."""
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('Successed.')

# Generated at 2022-06-13 23:45:12.210614
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'создание приложения на Python')() == \
           'sozdanie prilozheniya na Python'

# Generated at 2022-06-13 23:45:20.945394
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.english import English
    from mimesis.enums import Gender
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person

    person = Person('en')
    person.set_locale('ru')

    address = Address('en')
    address.set_locale('ru')

    english = English('en')
    english.set_locale('ru')

    assert english.slug()
    assert english.password(length=8)
    assert address.city()
    assert person.full_name(gender=Gender.MALE)

# Generated at 2022-06-13 23:45:27.900997
# Unit test for function romanize
def test_romanize():
    assert romanized('locale')(lambda x: 'Бухара')() == 'Bukhara'
    assert romanized('ru')(lambda x: 'Москва')() == 'Moskva'
    assert romanized('kk')(lambda x: 'Алматы')() == 'Almatı'
    assert romanized('uk')(lambda x: 'Київ')() == 'Kyiv'


# Generated at 2022-06-13 23:45:37.524003
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    from mimesis.enums import Gender
    t = Text(locale='ru')
    assert t._romanize_text('Строка') == 'Stroka'
    assert t._romanize_text('Строка') == 'Stroka'
    assert t._romanize_text('Строка', Gender.FEMALE) == 'Stroka'
    assert t._romanize_text('Строка', Gender.MALE) == 'Stroka'

    t = Text(locale='uk')
    assert t._romanize_text('Строка') == 'Stroka'

# Generated at 2022-06-13 23:45:42.409559
# Unit test for function romanize
def test_romanize():
    def foo(locale='ru'):
        return 'Привет, это тестовая строка!!!'

    foo = romanize(locale='ru')(foo)
    assert foo() == 'Privet, jeto testovaja stroka!!!'

# Generated at 2022-06-13 23:45:44.929834
# Unit test for function romanize
def test_romanize():
    assert romanize('uk')(lambda: 'Колодко')() == 'Kolodko'

# Generated at 2022-06-13 23:45:57.939088
# Unit test for function romanize
def test_romanize():
    # sample data in ukrainian
    sample = 'Тестовий текст українською мовою.'

    # romanization with default locale 'ru'
    @romanize()
    def romanize_func():
        return sample

    assert romanize_func() == 'Testovyi tekst' \
                              ' ukraїnsʹkoiu movoiu.'

    # romanization with explicitly defined locale 'uk'
    @romanize('uk')
    def romanize_func():
        return sample

    assert romanize_func() == 'Testovyi tekst ukraїnsʹkoiu movoiu.'

    # romanization with another explicitly defined locale 'kk'

# Generated at 2022-06-13 23:47:33.863274
# Unit test for function romanize
def test_romanize():
    @romanize()
    def func_test(text):
        return text

    print(func_test('Какой-то текст'))

# Generated at 2022-06-13 23:47:38.358886
# Unit test for function romanize
def test_romanize():
    @romanize("ru")
    def sample_cyrilic_to_latin(string: str) -> str:
        return string

    assert sample_cyrilic_to_latin("Привет, Мир") == "Privet, Mir"
    assert sample_cyrilic_to_latin("Здравствуй, Мир") == "Zdravstvuy, Mir"

# Generated at 2022-06-13 23:47:50.079717
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider
    from mimesis.enums import Gender
    from mimesis.exceptions import NonEnumerableError

    locale = 'ru'
    rp = RussianSpecProvider(locale)

    @romanized(locale)
    def romanize_text(
            text: str,
            gender: Gender = Gender.MALE,
            seed: int = None
    ) -> str:
        """Romanize the cyrillic text."""
        data = rp.random.seed(seed).choice(text)
        return data

    test_text = ['АБВГД', 'АБВГГГ']


# Generated at 2022-06-13 23:47:53.909803
# Unit test for function romanize
def test_romanize():
    """Test romanize() function."""
    from mimesis import Person

    person = Person('ru')
    assert len(''.join([i for i in person._romanized_cyrillic_name
                        if i.isalpha()])) == 30

    person = Person('uk')
    assert len(''.join([i for i in person._romanized_cyrillic_name
                        if i.isalpha()])) == 30

    person = Person('kk')
    assert len(''.join([i for i in person._romanized_cyrillic_name
                        if i.isalpha()])) == 30

# Generated at 2022-06-13 23:47:56.772975
# Unit test for function romanize
def test_romanize():
    for i in range(1):
        assert romanize()(lambda: 'Иванов Иван')() == 'Ivanov Ivan'

# Generated at 2022-06-13 23:48:05.964875
# Unit test for function romanize
def test_romanize():
    """Проверяем, что работает романизация текста.
    """
    import random
    from faker import Faker

    fake = Faker('ru_RU')
    fake.random.seed(42)

    number_of_tests = 100
    alphabet = ''.join(data.ROMANIZATION_DICT['ru'].keys())
    for _ in range(number_of_tests):
        s = fake.pystr(min_chars=1, max_chars=100)
        for char in s:
            if char in alphabet:
                break

# Generated at 2022-06-13 23:48:07.334173
# Unit test for function romanize
def test_romanize():
    import doctest
    doctest.testmod(extraglobs={"romanized": romanized})

# Generated at 2022-06-13 23:48:12.909081
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    r = romanize(locale='ru')(lambda: 'Привет')

    assert isinstance(r, str)
    assert r == 'Privet'

# Generated at 2022-06-13 23:48:13.680701
# Unit test for function romanize
def test_romanize():
    assert romanize


# Generated at 2022-06-13 23:48:22.768473
# Unit test for function romanize
def test_romanize():
    from mimesis.data import ROMANIZATION_DICT
    from mimesis.data import COMMON_LETTERS

    for locale, rdict in ROMANIZATION_DICT.items():
        romanized_letters = set(rdict.values())
        common_letters = set(COMMON_LETTERS.values())
        letters = set(ascii_letters + digits + punctuation)
        assert (romanized_letters | common_letters) - letters == set()

    @romanize('ru')
    def func():
        return 'Привет, Мир!'

    assert func() == 'Privet, Mir!'
    assert func.__name__ == 'func'
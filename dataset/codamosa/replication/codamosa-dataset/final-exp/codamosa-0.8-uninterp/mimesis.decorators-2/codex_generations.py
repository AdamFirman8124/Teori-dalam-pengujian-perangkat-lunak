

# Generated at 2022-06-13 23:39:38.594807
# Unit test for function romanize
def test_romanize():
    assert 'English' in dir(romanize)
    assert 'English' in romanized(locale='en')(str)('Англійська')

# Generated at 2022-06-13 23:39:47.933593
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    import mimesis.builtins.text as text

    txt = text.Text('en')
    result = romanize(locale='ru')(txt.word)()
    assert result
    assert isinstance(result, str)

    result = romanize(locale='uk')(txt.word)()
    assert result
    assert isinstance(result, str)

    result = romanize(locale='kk')(txt.word)()
    assert result
    assert isinstance(result, str)

    with UnsupportedLocale:
        romanize(locale='und')(txt.word)()

# Generated at 2022-06-13 23:39:52.415698
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет мир')() == 'Privet mir'
    assert romanized('uk')(lambda: 'Доброго ранку')() == 'Dobroho ranku'
    assert romanized('kk')(lambda: 'Әлеуметтік')() == 'Álewmettti'

# Generated at 2022-06-13 23:39:55.717646
# Unit test for function romanize
def test_romanize():
    # pylint: disable=redefined-outer-name
    assert romanize("ru")
    assert romanize("uk")
    assert romanize("kk")

# Generated at 2022-06-13 23:39:58.379886
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    def _func():
        return 'Мимисус'

    result = romanize('ru')(_func)()
    assert result == 'Mimisus'

# Generated at 2022-06-13 23:40:01.224695
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo():
        return 'Привет, мир!'

    assert foo() == 'Privet, mir!'

# Generated at 2022-06-13 23:40:09.606944
# Unit test for function romanize
def test_romanize():
	locale = 'ru'
	assert romanize(locale)(lambda test: 'ВАСЯ')('ВАСЯ') == 'VASYA'
	locale = 'uk'
	assert romanize(locale)(lambda test: 'ВАСЯ')('ВАСЯ') == 'VASYA'
	locale = 'kk'
	assert romanize(locale)(lambda test: 'ВАСЯ')('ВАСЯ') == 'VASYA'

# Generated at 2022-06-13 23:40:18.517871
# Unit test for function romanize
def test_romanize():
    """
    :return:
    """
    @romanize(locale='ru')
    def foo(text):
        return text
    assert foo('Разные названия того же знака') == 'Raznyye nazvaniya togo zhe znaka'

    @romanize(locale='uk')
    def foo1(text):
        return text
    assert foo1('Фізика химія біологія') == 'Fizyka khymiya biolohiia'

    @romanize(locale='kk')
    def foo2(text):
        return text

# Generated at 2022-06-13 23:40:22.189855
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda : 'Тест')() == 'Test'
    assert romanize('en')(lambda : 'Test')() == 'Test'

# Generated at 2022-06-13 23:40:25.778006
# Unit test for function romanize
def test_romanize():
    test_input = 'Слова тестовые'
    test_output = romanized('ru')(lambda: test_input)()
    assert test_output == 'Slova testovye'

# Generated at 2022-06-13 23:40:42.121816
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: '199')().encode(
        encoding='ascii', errors='strict') == b'199'
    assert romanize('ru')(lambda: 'как дела?')().encode(
        encoding='ascii', errors='strict') == b'kak dela?'
    assert romanized('uk')(lambda: '198*')().encode(
        encoding='ascii', errors='strict') == b'198*'
    assert romanize('uk')(lambda: 'Як діла?')().encode(
        encoding='ascii', errors='strict') == b'Yak dila?'

# Generated at 2022-06-13 23:40:51.351210
# Unit test for function romanize
def test_romanize():
    import datetime

    from mimesis.enums import Gender
    from mimesis.exceptions import UnsupportedLocale
    from mimesis.providers.person import Person

    p = Person('ru')
    assert p.full_name(gender=Gender.MALE) == 'Владилен Романов'

    p = Person(locale='ru', romanize=True)
    assert p.full_name(gender=Gender.MALE) == 'Vladilen Romanov'

    def test():
        return datetime.datetime.now().strftime('%d %B %Y года')

    assert test() == '18 марта 2020 года'

    @romanize(locale='ru')
    def test():
        return

# Generated at 2022-06-13 23:41:03.205204
# Unit test for function romanize
def test_romanize():
    """Test function."""
    import unittest

    class TestRomanize(unittest.TestCase):
        """Test Romanize."""

        def test_romanize_ru(self):
            """Test romanize with ru locale."""
            @romanize('ru')
            def rus_test():
                return 'поехали'

            assert rus_test() == 'poehali'

        def test_romanize_uk(self):
            """Test romanize with uk locale."""
            @romanize('uk')
            def uk_test():
                return 'починаю'

            assert uk_test() == 'počynaju'


# Generated at 2022-06-13 23:41:03.747500
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:41:15.554143
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    from mimesis.builtins.text import TextSpecifier
    from mimesis.providers.text import Text

    text_specifier = TextSpecifier(Text())
    romanize_test = romanize('ru')
    romanized_test = romanized('ru')

    assert isinstance(romanize_test, Callable)
    assert isinstance(romanized_test, Callable)

    assert romanize_test(text_specifier.words)
    assert romanize_test(text_specifier.text) is not None
    assert romanize_test(text_specifier.sentence) is not None
    assert romanize_test(text_specifier.title) is not None
    assert romanize_test(text_specifier.paragraph) is not None


# Generated at 2022-06-13 23:41:22.848515
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda : 'Как дела?\n')() == 'Kak dela?\n'
    assert romanize('ru')(lambda : 'Привет, Мир.')() == 'Privet, Mir.'

    assert romanize('uk')(lambda : 'Вітаю, Мир.')() == 'Vitayu, Mir.'
    assert romanize('uk')(lambda : 'Як справи?\n')() == 'Yak spravy?\n'

    assert romanize('kk')(lambda : 'Сәлем Әлем.')() == 'Sälem Älem.'

# Generated at 2022-06-13 23:41:37.008044
# Unit test for function romanize
def test_romanize():
    from mimesis.providers import Person
    p = Person()
    assert p.full_name(locale='ru') == 'Ангелина П. Калашникова'
    assert p.full_name(locale='uk') == 'Ніна Б. Дорошенко'
    assert p.full_name(locale='kk') == 'Айжан Е. Мамыр'
    # Without locale
    assert p.full_name() == 'Айжан Е. Мамыр'

# Generated at 2022-06-13 23:41:46.097307
# Unit test for function romanize
def test_romanize():
    import mimesis.enums
    print(mimesis.enums.Locale.UKRAINIAN.value)
    print(mimesis.enums.Locale.RUSSIAN.value)
    print(mimesis.enums.Locale.KAZAKH.value)
    from mimesis.providers.address import Address
    from mimesis.providers.lorem import Lorem

    adr = Address(locale='ru')
    string_ru = Lorem(locale='ru')
    string_uk = Lorem(locale='uk')
    string_kk = Lorem(locale='kk')

    print(string_ru.text(quantity=10))
    print(string_uk.text(quantity=10))
    print(string_kk.text(quantity=10))



# Generated at 2022-06-13 23:41:56.993622
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    from mimesis.providers import Person, Datetime
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider

    russian = RussiaSpecProvider()
    person = Person(russian)
    datetime = Datetime(russian)

    assert russian.romanize('Саша') == 'Sasha'
    assert person.full_name(gender=Gender.MALE) == 'Volodia Khristoforov'
    assert datetime.time(start='23:59', stop='00:05') == '00:01:15'

# Generated at 2022-06-13 23:42:07.734833
# Unit test for function romanize
def test_romanize():
    # pylint: disable=unused-variable
    @romanize()
    def roman_ru():
        return 'Привет, Мир!'

    assert roman_ru() == 'Privet, Mir!'

    @romanize('ru')
    def roman_ru():
        return 'Привет, Мир!'

    assert roman_ru() == 'Privet, Mir!'

    @romanize('uk')
    def roman_uk():
        return 'Привіт, Світ!'

    assert roman_uk() == 'Pryvit, Svit!'

    @romanize('kk')
    def roman_kk():
        return 'Сәлем, Дүние!'



# Generated at 2022-06-13 23:42:22.769163
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda _: 'Питер')() == 'Piter'
    assert romanize('uk')(lambda _: 'Саксонія')() == 'Saksaniia'
    assert romanize('kk')(lambda _: 'Қазақстан')() == 'Qazaqstan'

# Generated at 2022-06-13 23:42:32.858946
# Unit test for function romanize
def test_romanize():
    if __name__ != '__main__':
        return
    import unittest


    class RomanizeTestCase(unittest.TestCase):
        """Tests for romanize decorator."""

        def test_using_decorator(self):
            @romanize('ru')
            def get_text():
                return 'привет'

            expected = 'privet'
            self.assertEqual(expected, get_text())

        def test_using_decorator_with_unsupported_locale(self):
            @romanize('fr')
            def get_text():
                return 'привет'

            with self.assertRaises(UnsupportedLocale):
                get_text()

    unittest.main()

# Generated at 2022-06-13 23:42:37.627078
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'привет')() == 'privet'
    assert romanize(locale='uk')(lambda: 'привіт')() == 'pryvit'
    assert romanize(locale='kk')(lambda: 'Сәлем')() == 'Sälem'

# Generated at 2022-06-13 23:42:40.176349
# Unit test for function romanize
def test_romanize():
    assert isinstance(romanized, romanize)
    assert isinstance(romanized('ru'), romanized)
    assert isinstance(romanized('uk'), romanized)
    assert isinstance(romanized('kk'), romanized)

# Generated at 2022-06-13 23:42:54.353398
# Unit test for function romanize
def test_romanize():
    """Unit test for function :func:`~mimesis.decorators.romanize`."""
    # Test string, 0 - letters, 1 - digits, 2 - punctuation
    # 3 - cyrillic letters with Ё, 4 - cyrillic letters without Ё.
    # 5 - cyrillic letters with Ё, but with capital letters
    # 6 - cyrillic letters with Ё, but with lowercase letters.

# Generated at 2022-06-13 23:42:57.204776
# Unit test for function romanize
def test_romanize():
    romanized_text = romanize('ru')(lambda : 'Привет мир!')
    romanized_text()
    assert romanized_text() == 'Privet mir!'

# Generated at 2022-06-13 23:43:06.696156
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def test_text():
        return 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    assert test_text() == 'ABVGDEEJZIJKLMNOPRSTUFHCCHSHSCBYYEZYа'

# Generated at 2022-06-13 23:43:11.950865
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider

    rus = RussianSpecProvider()
    romanized_string = rus.romanize(rus.word())
    assert romanized_string
    assert type(romanized_string) is str



# Generated at 2022-06-13 23:43:21.976642
# Unit test for function romanize
def test_romanize():
    #Test for lowercase letters
    assert romanize('ru')('Мечтать') == 'mechtat'
    #Test for uppercase letters
    assert romanize('ru')('ГЕНЕРАТОР') == 'GENERATOR'
    assert romanize('ru')('Генератор') == 'Generator'
    #Test for mixed letters
    assert romanize('ru')('ГЕНЕратор') == 'GENErator'
    #Test for numbers
    assert romanize('ru')('Запрет на курение: 123') == 'zapret-na-kurenie-123'
   

# Generated at 2022-06-13 23:43:33.249186
# Unit test for function romanize
def test_romanize():
    """Test the romanize decorator."""
    @romanize(locale='ru')
    def romanizator():
        return "слушатель"
    assert romanizator() == "slushatel'"

    @romanize(locale='uk')
    def romanizator():
        return "катедра"
    assert romanizator() == "katedra"

    @romanize(locale='kk')
    def romanizator():
        return "жеткізуші"
    assert romanizator() == "jetkizshi"

    @romanize(locale='kk')
    def romanizator():
        return "королева"

# Generated at 2022-06-13 23:43:50.793229
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""

    @romanize('ru')
    def foo():
        return 'Мир снова пробуждается, мир утра поджигает.'

    r = foo()
    assert isinstance(r, str)
    assert r == 'Mir snova probuzhdaetsya, mir utra podzhigaet.'



# Generated at 2022-06-13 23:43:55.326463
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Мимесис')() == 'Mimesis'
    assert romanized('kk')(lambda: 'Мимесис')() == 'Mimesis'

# Generated at 2022-06-13 23:44:04.521521
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    alph = ''.join(data.ROMANIZATION_DICT['ru'].values())
    alph += ''.join(data.COMMON_LETTERS.values())

    @romanize('ru')
    def romanize_test(x: str) -> str:
        return x

    assert isinstance(romanize_test(alph), str)
    assert romanize_test(alph) == 'AaBbVvGgDdEeZhZzIiJjKkLlMmNnOoPpRrSsTtUuFfHhCcChShShtsch' \
                                  'Yy#&quot;YyEeYuYuYaYa'

# Generated at 2022-06-13 23:44:12.961726
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian(value: str) -> str:
        return value

    assert russian('мимими') == 'mimimi', 'Wrong conversion!'

    # Raise exception
    @romanize(locale='ru')
    def ukrainian(value: str) -> str:
        return value

    try:
        ukrainian('мимими')
    except UnsupportedLocale:
        pass
    except Exception:
        print('Error!')

# Generated at 2022-06-13 23:44:20.257892
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""
    assert romanize(locale='ru')(lambda x: 'вася чихнул') == 'vasya chihnul'
    assert romanize(locale='kk')(lambda x: 'дауыс') == 'daýys'
    assert romanize(locale='uk')(lambda x: 'вася хихнув') == 'vasya khykhnuv'
    assert romanize(locale='xy')(lambda x: 'вася хихнув') == 'vasya khykhnuv'

# Generated at 2022-06-13 23:44:23.185300
# Unit test for function romanize
def test_romanize():
    assert romanize()('Как тебя зовут?') == 'Kak tebya zovut?'

# Generated at 2022-06-13 23:44:29.803727
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    @romanize(locale='ru')
    def _get_name(locale='ru') -> str:
        person = Person(locale)
        return person.full_name()

    # Генри Форд
    assert _get_name() == 'Genri Ford'

# Generated at 2022-06-13 23:44:30.629885
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:44:37.639347
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    from mimesis.enums import Language
    ukr = Language.UKRAINIAN.value
    rus = Language.RUSSIAN.value
    kz = Language.KAZAKH.value
    @romanize(ukr)
    @romanize(rus)
    @romanize(kz)
    def func():
        return ('Алфавіт', 'Алфавит', 'Альфавит')

    assert func() == ('Alfavit', 'Alfavit', 'Al\'favit')

# Generated at 2022-06-13 23:44:41.472838
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.text import Text

    text = Text(Language.RUSSIAN)
    assert len(text.romanize()) > 0



# Generated at 2022-06-13 23:45:20.127140
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.datetime import Datetime

    dt = Datetime('ru')
    assert dt.date() == '30.08.2007'
    assert dt.full_date('ru') == '30.08.2007'

# Generated at 2022-06-13 23:45:30.935231
# Unit test for function romanize
def test_romanize():
    class Test(object):
        def __init__(self, locale):
            self.locale = locale

        @romanize(locale='ru')
        def foo(self):
            return self.locale.split(',')[0]

        @romanize(locale='uk')
        def bar(self):
            return self.locale.split(',')[1]

        @romanize(locale='kk')
        def baz(self):
            return self.locale.split(',')[2]

    t = Test('Привет,Привіт,Сәлем')
    assert t.foo() == 'privet'
    assert t.bar() == 'privit'
    assert t.baz() == 'salem'

# Generated at 2022-06-13 23:45:35.860101
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def text_ru(*args, **kwargs):
        return 'Привет, Мир!'

    @romanize(locale='ru')
    def text_en(*args, **kwargs):
        return 'Hello world!'

    assert text_ru() == 'Privet, Mir!'
    assert text_en() == 'Hello world!'

# Generated at 2022-06-13 23:45:40.158161
# Unit test for function romanize
def test_romanize():
    """Test for the decorator romanize."""
    # Example for Cyrillic to Latin
    assert romanized('ru')(lambda: 'Россия')() == 'Rossiya'

    # Example for Latin
    assert romanized('ru')(lambda: 'Russia')() == 'Russia'

    # For Arabic characters
    assert romanized('uk')(lambda: 'شماس محمد')() == 'Shamakh Mohamad'



# Generated at 2022-06-13 23:45:42.168236
# Unit test for function romanize
def test_romanize():
    assert romanize("ru")("Русский") == "Russkiy"

# Generated at 2022-06-13 23:45:55.610192
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Мы все живём в современном мире')() == \
        'My vsje zhyvjom v sovremennom mire'


# Generated at 2022-06-13 23:46:01.429994
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привет, мир!')() == 'Privet, mir!'

# Generated at 2022-06-13 23:46:05.180717
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def get_romanized_str(length: int = 10) -> str:
        return ''.join(data.CJK.create_tokens(length))

    result = get_romanized_str()
    assert result is not None

# Generated at 2022-06-13 23:46:09.271300
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def test(value):
        return value

    assert test('Мир') == 'Mir'
    assert test('Мир стал мирным') == 'Mir stal mirnym'

# Generated at 2022-06-13 23:46:15.634249
# Unit test for function romanize
def test_romanize():
    # Test for russian locale
    @romanize('ru')
    def get_ru_locale():
        return 'Привет, мороз!'

    assert get_ru_locale() == 'Privet, moroz!'

    # Test for ukrainian locale
    @romanize('uk')
    def get_uk_locale():
        return 'Вітаю, мороз!'

    assert get_uk_locale() == 'Vitaiu, moroz!'

    # Test for kazakh locale
    def get_kz_locale():
        return 'Сәлем, мороз!'

    assert romanize('kk')(get_kz_locale)() == 'Salem, moroz!'

   

# Generated at 2022-06-13 23:46:46.271731
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import (TextSpecProvider)
    import pytest

    data = TextSpecProvider(locale='ru')
    assert data.romanize() == ''

    @romanized(locale='ru')
    def f(n):
        return n

    assert f('Привет') == 'Privet'
    assert f('Привет, Мир!') == 'Privet, Mir!'

# Generated at 2022-06-13 23:46:58.438422
# Unit test for function romanize
def test_romanize():

    @romanize(locale='ru')
    def _test(n):
        return 'Привет, мир, я тестовая функция! (مرحبا بالعالم، أنا خاصية الاختبار !)' * n

    for i in range(1, 5):
        assert _test(i) == 'Privet, mir, ya testovaya funktsiya! (مرحبا بالعالم، أنا خاصية الاختبار !)' * i


# Generated at 2022-06-13 23:47:02.863187
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def f():
        return 'Привет, мир!'

    return f() == 'Privet, mir!'

# Generated at 2022-06-13 23:47:13.695639
# Unit test for function romanize
def test_romanize():
    # a_romanized = romanized()(lambda: "sdfsdf")
    # assert a_romanized == 'sdfsdf'

    a_romanized = romanized("ru")(lambda: "Привет Мир")
    assert a_romanized == 'Privet Mir'

    a_romanized = romanized("uk")(lambda: "Привіт Світ")
    assert a_romanized == 'Pryvit Svit'

    a_romanized = romanized("kk")(lambda: "Сәлем Дүние")
    assert a_romanized == 'Salem Duniye'

# Generated at 2022-06-13 23:47:19.677358
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    assert romanized()('Луна') == 'Luna'
    assert romanized()('Чайковский') == 'Chaykovskiy'
    assert romanized(locale='uk')('Якубович') == 'Yakubovych'
    assert romanized(locale='kk')('Тыныштық') == 'Tınıştıq'

# Generated at 2022-06-13 23:47:25.200367
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'привет')() == 'privet'
    assert romanize('uk')(lambda: 'привіт')() == 'pryvit'
    assert romanize('kk')(lambda: 'Саламатсыздар!')() == 'Salamatsyzdar!'

# Generated at 2022-06-13 23:47:31.676814
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.lorem import Lorem

    l_ru = Lorem(locale=Locale.RU)
    assert l_ru.word() == 'почти'
    assert l_ru.romanized().word() == 'pochti'
    assert l_ru.romanized(locale=Locale.RU).word() == 'pochti'
    assert l_ru.romanized(locale=Locale.UK).word() == 'pochti'
    assert l_ru.romanized(locale=Locale.UK).word() == 'pochti'


# Generated at 2022-06-13 23:47:35.935050
# Unit test for function romanize
def test_romanize():
    import pytest
    from mimesis.builtins import RussiaSpecProvider

    rp = RussiaSpecProvider()

    happy_path_tests = [
        [rp.person().full_name(), 'adgjmptw']
    ]

    for test in happy_path_tests:
        assert test[1] in romanize('ru')(lambda: test[0])()

# Generated at 2022-06-13 23:47:42.632120
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    assert romanize('ru')(lambda: 'abc')() == 'abc'  # type: ignore
    assert romanize('ru')(lambda: 'Привет')() == 'privet'  # type: ignore
    assert romanize('ru')(lambda: 'Лондон')() == 'london'  # type: ignore
    assert romanize('ru')(lambda: 'Сочи')() == 'sochi'  # type: ignore
    assert romanize('ru')(lambda: 'Москва')() == 'moskva'  # type: ignore

# Generated at 2022-06-13 23:47:43.193237
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:48:16.889432
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Крылов')() == 'Krylov'
    assert romanize('ru')(lambda: 'Крылов')() == 'Krylov'
    assert romanize('ru')(lambda: 'Антон')() == 'Anton'
    assert romanize('uk')(lambda: 'Словак')() == 'Slovak'
    assert romanize('uk')(lambda: 'Йосип')() == 'Iosyp'
    assert romanize('kk')(lambda: 'Сыр')() == 'Sır'

# Generated at 2022-06-13 23:48:23.655718
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет Мир')() == 'Privet Mir'
    assert romanize('uk')(lambda: 'Привіт, Світ')() == 'Pryvit, Svit'
    assert romanize('kz')(lambda: 'Сәлем, Дүние')() == 'Sälem, Dünie'



# Generated at 2022-06-13 23:48:27.178603
# Unit test for function romanize
def test_romanize():
    """Test method for romanize function."""
    from mimesis.numbers import Numbers
    from mimesis.providers.numbers import Number

    n = Numbers()
    number = Number()
    assert isinstance(n.romanize(number.random_int()), str)


# Generated at 2022-06-13 23:48:29.193838
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Я программист, а не программа!')() == 'Ya programmist, a ne programma!'

test_romanize()

# Generated at 2022-06-13 23:48:35.158637
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_ru():
        return 'Позвольте представиться: Анатолий Ермолин.'


# Generated at 2022-06-13 23:48:36.057855
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: ['Мимесис']) == 'Mimesis'

# Generated at 2022-06-13 23:48:37.775690
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Тест')() == 'Test'


# Generated at 2022-06-13 23:48:42.200719
# Unit test for function romanize
def test_romanize():
    romanized_text = romanize()(lambda: 'Привет, Мир!')
    assert isinstance(romanized_text(), str)
    assert 'Privet, Mir!' == romanized_text()

# Generated at 2022-06-13 23:48:51.806021
# Unit test for function romanize
def test_romanize():
    assert romanize()('привет') == 'privet'
    assert romanize()('Привет, Мир') == 'Privet, Mir'
    assert romanize()('Добро пожаловать в Россию!') == (
        'Dobro pozhalovat v Rossiyu!'
    )
    assert romanize()('Как дела?') == 'Kak dela?'
    assert romanize()('А теперь по-русски') == 'A teper po-russki'
    assert romanize()('Антон, не травь!')

# Generated at 2022-06-13 23:48:56.881765
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    # Test with default locale
    from mimesis.builtins import Person
    person = Person()
    full_name = person.full_name
    assert full_name != romanize()(full_name)

    # Test with locale 'ru'
    from mimesis.builtins import Localization
    localization = Localization('ru')
    full_name = localization.person.full_name
    assert full_name != romanize('ru')(full_name)


# Generated at 2022-06-13 23:39:38.875375
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.builtins import Person

    person = Person(Language.RUSSIAN)
    assert person.full_name() == 'Владимир Тимошенков'
    assert person.romanize().full_name() == 'Vladimir Timoshenko'

    assert 'Владимир Тимошенков' == person._full_name()


if __name__ == '__main__':
    test_romanize()
    print('Test romanize() successed!')

# Generated at 2022-06-13 23:39:40.200714
# Unit test for function romanize
def test_romanize():
    assert data.COMMON_LETTERS
    assert data.ROMANIZATION_DICT
    assert romanize(locale='ru')
    assert romanized(locale='ru')

# Generated at 2022-06-13 23:39:50.543963
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def russian():
        return 'Привет мир'

    assert russian() == 'Privet mir'

    @romanize('kk')
    def kazakh():
        return 'Сәлем'

    assert kazakh() == 'Sälem'

    @romanize('uk')
    def ukrainian():
        return 'Привіт світ'

    assert ukrainian() == 'Pryvit svit'

    @romanize('de')
    def german():
        return 'Hallo Welt'

    try:
        assert german()
    except UnsupportedLocale:
        assert True
    else:
        assert False


# Generated at 2022-06-13 23:40:01.068025
# Unit test for function romanize
def test_romanize():
    def romanized_func(locale):
        @romanize(locale)
        def func(text):
            return text
        return func

    func = romanized_func('ru')
    # Should not fail
    assert func('Hello world!') == 'Hello world!'
    assert func('Привет мир!') == 'Privet mir!'

    func = romanized_func('uk')
    # Should not fail
    assert func('Hello world!') == 'Hello world!'
    assert func('Привіт світ!') == 'Pryvit svit!'

    func = romanized_func('kk')
    # Should not fail
    assert func('Hello world!') == 'Hello world!'

# Generated at 2022-06-13 23:40:03.402875
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Тест')() == 'Test'

# Generated at 2022-06-13 23:40:08.920807
# Unit test for function romanize
def test_romanize():
    """Test for the romanize decorator."""
    from mimesis.builtins.text import TextSpecifier

    text_decorator = romanize('ru')

    @text_decorator
    def func():
        text = TextSpecifier('ru')
        return text.cyrillic()

    assert ' '.join(func().split()[:3]) == 'komandirovka'

# Generated at 2022-06-13 23:40:12.089463
# Unit test for function romanize
def test_romanize():
    @romanize()
    def generate_word(*args):
        return args[0]

    assert generate_word('Привет') == 'Privet'

# Generated at 2022-06-13 23:40:24.856324
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    @romanize('ru')
    def generator():
        return 'Еще «граф Нона» повертається з Молдавії, і він веселий, мудрий і сумний.'

    result = generator()
    assert result == 'Eshche «graf Nona» povertaetsya z Moldavii, i vin ' \
                     'veselyi, mudryi i sumnyi.'


# Generated at 2022-06-13 23:40:34.566571
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: "У лукоморья дуб зеленый")() == \
        "U lukomoria dub zelenyi"

    assert romanize('uk')(lambda: "У лютні жалостина барвинок")() == \
        "U liutni zhalostyna barvinok"


# Generated at 2022-06-13 23:40:38.045414
# Unit test for function romanize
def test_romanize():
    d = data.Data('ru')
    assert not d.person('full_name').isalpha()
    r_full_name = d.romanized.person('full_name')
    r_name = d.romanized.person('name')
    assert (' '.join([r_name, r_name, r_name])).isalpha()

# Generated at 2022-06-13 23:40:47.992159
# Unit test for function romanize
def test_romanize():
    from .text import Text

    t = Text('en')
    txt = t.text()
    assert len(txt) > 0
    # We romanize the original text.
    assert txt != romanized(locale='en')(lambda: txt)()

# Generated at 2022-06-13 23:40:54.612882
# Unit test for function romanize
def test_romanize():
    @romanize()
    def generator():
        yield 'К'
        yield 'и'
        yield 'е'
        yield 'в'
        yield ' '
        yield 'В'
        yield 'а'
        yield 'с'
        yield 'и'
        yield 'л'
        yield 'и'
        yield 'ч'
        yield '.'
    text = generator()
    assert text == 'Kiev Vasylich.'

    @romanize(locale='ru')
    def generator():
        yield 'К'
        yield 'и'
        yield 'е'
        yield 'в'
        yield ' '
        yield 'В'
        yield 'а'
        yield 'с'
        yield 'и'
        yield 'л'
        yield 'и'
        yield 'ч'
       

# Generated at 2022-06-13 23:40:57.585462
# Unit test for function romanize
def test_romanize():
    @romanize('en')
    def useless_function():
        return 'Привет, Мир!'

    assert useless_function() == 'Privet, Mir!'

# Generated at 2022-06-13 23:41:05.707589
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    # pylint: disable=unused-variable
    @romanize(locale='ru')
    def russian_text():
        """Generate russian text."""
        return 'Карл у Клары украл кораллы, а Клара у Карла украла кларнет.'

    assert russian_text() == (
        'Karl u Klary ukral korali, a Klara u Karla '
        'ukrala klarnet.')

# Generated at 2022-06-13 23:41:13.055542
# Unit test for function romanize
def test_romanize():
    """Test function 'romanize'."""
    assert romanized(locale='ru')(lambda: 'привет')() == 'privet'
    assert romanized(locale='uk')(lambda: 'добрий день')() == 'dobriy den'
    assert romanized(locale='kk')(lambda: 'құрылғын')() == 'kurylgyn'

# Generated at 2022-06-13 23:41:21.006122
# Unit test for function romanize
def test_romanize():
    @romanize(locale = 'ru')
    def romanized_ru(text: str = '') -> str:
        return text

    assert romanized_ru('Как дела?') == 'Kak dela?'
    assert romanized_ru('Как дела!') == 'Kak dela!'
    assert romanized_ru('Как дела, как дела, как дела?') == 'Kak dela, kak dela, kak dela?'

# Generated at 2022-06-13 23:41:24.641678
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    assert romanize("kk")("БЪЛГЪРИЯ") == "B'L'G'RIYA"

# Generated at 2022-06-13 23:41:33.575589
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    def _test_romanize(locale: str) -> str:
        @romanize(locale)
        def _test(locale: str):
            """Test function."""
            gen = data.Data(_locale=locale)
            return gen.datetime.random_datetime().strftime('%Y-%m-%d')

        return _test(locale)

    test_cases = (
        ('ru', '2006-09-22'),
        ('uk', '2006-09-22'),
        ('kk', '2006-09-22'),
    )

    for t in test_cases:
        assert _test_romanize(t[0]) == t[1]

# Generated at 2022-06-13 23:41:40.044944
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привет')(
    ) == 'privett'

    assert romanize(locale='uk')(lambda: 'Привіт')(
    ) == 'pryvit'

    assert romanize(locale='kk')(lambda: 'Сәлем')(
    ) == 'sälem'

# Generated at 2022-06-13 23:41:46.698105
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привет')() == 'Privet'
    assert romanize(locale='uk')(lambda: 'Привіт')() == 'Pryvit'
    assert romanize(locale='kk')(lambda: 'Сәлем')() == 'Salem'
    assert romanize(locale='my')(lambda: 'မင်္ဂလာပါ')() == 'Minglaba'
    assert romanize(locale='en')(lambda: 'Trade')() == 'Trade'

# Generated at 2022-06-13 23:42:00.697715
# Unit test for function romanize
def test_romanize():
    romanized_str = romanized(locale='ru')(lambda: 'Привет, Мир!')
    assert romanized_str() == 'Privet, Mir!'

# Generated at 2022-06-13 23:42:06.695470
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привіт, Мир!')() == 'Pryvit, Myr!'
    assert romanize('uk')(lambda: 'Привіт, Мир!')() == 'Pryvit, Mir!'
    assert romanize('kk')(lambda: 'Привіт, Мир!')() == 'Pryvit, Mir!'

# Generated at 2022-06-13 23:42:11.872778
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    try:
        @romanize('ru')
        def my_func():
            return 'Привет, мир!'

        assert my_func() == 'Privet, mir!'
    except Exception as err:
        assert False, 'Test failed, error: {0}'.format(err)



# Generated at 2022-06-13 23:42:20.720971
# Unit test for function romanize
def test_romanize():
    def test(result: str, arg: str, locale: str):
        assert romanize(locale)(lambda x: x)(arg) == result

    test('english', 'english', 'en')
    test('gazprom', 'газпром', 'ru')
    test('tekhnicheskaya', 'техническая', 'ru')
    test('pishchevaya', 'пищевая', 'ru')
    test('pishchevaya', 'пищевая', 'ru')
    test('sfera', 'сфера', 'ru')
    test('tekhnika', 'техника', 'ru')

# Generated at 2022-06-13 23:42:22.087445
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: None)() == ''

# Generated at 2022-06-13 23:42:32.256625
# Unit test for function romanize
def test_romanize():
    russian_string = "Строка для тестирования"
    assert romanized('ru')(lambda: russian_string)() == "Stroka dlya testirovaniya"
    ukrainian_string = "Стрічка для перевірки"
    assert romanized('uk')(lambda: ukrainian_string)() == "Strichka dlya peverky"
    kazakh_string = "Текст жүйесі"
    assert romanized('kk')(lambda: kazakh_string)() == "Tekst zhyyesi"

# Generated at 2022-06-13 23:42:37.157002
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.builtins import Python

    locale = Locale.RU
    py = Python(locale)
    q = py.code.random_choice()
    z = py.code.random_choice()
    assert q == 'q'
    assert z == 'z'

# Generated at 2022-06-13 23:42:42.932132
# Unit test for function romanize
def test_romanize():
    assert isinstance(romanize, Callable)

    assert isinstance(romanized, Callable)

    from mimesis import Person, Text
    from mimesis.builtins.person.data import NAME_DATA, LAST_NAME_DATA
    from mimesis.builtins.text.data import WORDS_DATA

    class CustomPerson(Person):
        class Meta:
            namespace = 'person.custom'
            data_dir = ''

        @romanize('ru')
        def full_name(self):
            return super().full_name()

    class CustomText(Text):
        class Meta:
            namespace = 'text.custom'
            data_dir = ''

        def words(self, *, locale: str = 'ru') -> str:
            return data.ALPHABET_DATA['ru']


# Generated at 2022-06-13 23:42:53.240057
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def foo():
        return 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    res = foo()
    assert res == 'ABVGDĖŽZIJKLMNOPRSTUFHCČŠŜʺYʹĖJUJA'



# Generated at 2022-06-13 23:43:00.775473
# Unit test for function romanize
def test_romanize():
    """Tests for romanize API."""
    import random
    import pytest
    _symbols = ascii_letters + digits + punctuation
    _cyrillic = 'бцдфгґхжзклмнпрстйваэ\
БЦДФГҐХЖЗКЛМНПРСТЙВАЭї'

    @romanize(locale='uk')
    def romanize_uk(symbols: str = '') -> str:
        """Generate a romanized text.

        :param symbols: Symbols pool.
        :return: Romanized text.
        """

# Generated at 2022-06-13 23:43:16.701867
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Пример')() in ['PRIMER', 'PRIMÉR']
    assert romanize('kk')(lambda: 'Сәлем')() == 'SÄLËM'
    assert romanize('uk')(lambda: 'Вітаю')() in ['VITAJU', 'VÏTAJÙ']
    assert romanize('tt')(lambda: 'Зграя')() in ['ZƣRAYA', 'ZƢRAYA']
    assert romanize('ch')(lambda: 'Иймен')() == 'Ijmen'

# Generated at 2022-06-13 23:43:19.933743
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'russian')() == 'russian'
    assert romanize('uk')(lambda: 'ukrainian')() == 'ukrainian'
    assert romanize('kk')(lambda: 'kazakh')() == 'kazakh'

# Generated at 2022-06-13 23:43:31.756775
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_test_ru():
        return 'Правильный текст'

    @romanize('uk')
    def romanize_test_uk():
        return 'Правильний текст'

    @romanize('kk')
    def romanize_test_kk():
        return 'Жақсы текст'

    assert romanize_test_ru() == 'Pravilʹnyĭ tekst'
    assert romanize_test_uk() == 'Pravylʹnyĭ tekst'
    assert romanize_test_kk() == 'Jaksy tekst'

# Generated at 2022-06-13 23:43:38.893588
# Unit test for function romanize
def test_romanize():
    def foo():
        pass

    assert foo.__doc__ == 'Romanize the cyrillic text.\n\n    Transliterate the cyrillic script into the latin alphabet.\n\n    .. note:: At this moment it works only for `ru`, `uk`, `kk`.\n\n    :param locale: Locale code.\n    :return: Romanized text.\n    '
    assert foo.__name__ == 'foo'
    assert foo.__annotations__ == {}



# Generated at 2022-06-13 23:43:45.906416
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda _: 'Привет')() == 'Privet'
    assert romanize(locale='uk')(lambda _: 'Привіт')() == 'Pryvit'
    assert romanize(locale='kk')(lambda _: 'Сәлем')() == 'Salem'

# Generated at 2022-06-13 23:43:52.295669
# Unit test for function romanize
def test_romanize():
    assert romanize()('Привет') == 'Privet'
    assert romanize('ru')('Привет') == 'Privet'
    assert romanize('uk')('Привет') == 'Pryvit'
    assert romanize('kk')('Привет') == 'Pryvet'

# Generated at 2022-06-13 23:43:58.124223
# Unit test for function romanize
def test_romanize():
    s = 'Украина'
    # Default romanize
    romanized_string = romanized()(s)
    assert romanized_string == 'Ukraina'

    # Custom locale romanize
    romanized_string = romanized('ru')(s)
    assert romanized_string == 'Ukraina'

# Generated at 2022-06-13 23:43:58.687922
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:44:02.039788
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanization_test():
        return 'АБВГД абвгд'

    assert romanization_test() == 'ABVGD abvgd'

# Generated at 2022-06-13 23:44:03.747935
# Unit test for function romanize
def test_romanize():
    assert romanize('ru');
    assert romanize('uk');
    assert romanize('kk');
    assert not romanize('en')

# Generated at 2022-06-13 23:44:15.262970
# Unit test for function romanize
def test_romanize():
    assert callable(romanize)
    assert callable(romanized)

# Generated at 2022-06-13 23:44:17.589850
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language

    t = Language(Language.RU)
    assert t.romanize('Привет') == 'privet'

# Generated at 2022-06-13 23:44:20.863952
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text

    t = Text()

    assert t.romanized('ru')(size=10)

# Generated at 2022-06-13 23:44:24.691224
# Unit test for function romanize
def test_romanize():
    assert romanized("ru")("Антон Павлович Чехов") == "Anton Pavlovich Chekhov"


# Generated at 2022-06-13 23:44:28.196586
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def bar():
        return 'тест'

    assert bar() == 'test'

# Generated at 2022-06-13 23:44:31.672578
# Unit test for function romanize
def test_romanize():
    """Unit test for romanize."""
    assert romanize('ru')(str)().lower().startswith('а')

# Generated at 2022-06-13 23:44:33.855590
# Unit test for function romanize
def test_romanize():
    romanize('ru')
    romanize('uk')
    romanize('kk')

# Generated at 2022-06-13 23:44:37.961164
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo():
        return 'Благодарю'

    result = foo()
    assert result == 'Blagodaryu'

# Generated at 2022-06-13 23:44:41.226761
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    from mimesis import Generic
    g = Generic()
    g.locale = 'ru'
    assert g.text(romanize=True)

# Generated at 2022-06-13 23:44:58.521360
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Мама мыла раму')() == 'Mama myla ramu'
    assert romanized('kk')(lambda: 'Мама мыла раму')() == 'Mama myla ramu'
    assert romanized('uk')(lambda: 'Мама мыла раму')() == 'Mama myla ramu'
    assert romanized('be')(lambda: 'Мама мыла раму')() == 'Mama myla ramu'

# Generated at 2022-06-13 23:45:34.030932
# Unit test for function romanize
def test_romanize():
    """Tests function romanize."""
    assert romanize('ru')(lambda: 'Любовь и Надежда')() == 'Lubov i Nadezhda'
    assert romanize('ru')(lambda: 'Это Москва.')() == 'Eto Moskva.'
    assert romanize('uk')(lambda: 'Любов і Надія')() == 'Lyubov i Nadiya'
    assert romanize('uk')(lambda: 'Любов і надія')() == 'Lyubov i nadiya'

# Generated at 2022-06-13 23:45:40.801020
# Unit test for function romanize
def test_romanize():
    obj = data._Data('en')
    assert obj._romanize('Большая Бронная Улица') == 'Bolshaya Bronnaya Ulitsa'

    obj = data._Data('ru')
    assert obj._romanize('Большая Бронная Улица') == 'Bolshaya Bronnaya Ulitsa'

    obj = data._Data('uk')
    assert obj._romanize('Большая Бронная Улица') == 'Bolshaya Bronnaya Ulitsa'

    obj = data._Data('kk')

# Generated at 2022-06-13 23:45:49.070947
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'abc')() == 'abc'
    assert romanized('ru')(lambda: 'йцукен')() == 'ytcken'
    assert romanized('uk')(lambda: 'йцукен')() == 'ytsuken'
    assert romanized('kk')(lambda: 'йцукен')() == 'itsuken'

# Generated at 2022-06-13 23:46:01.087697
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'Привет')() == 'Privet'

# Generated at 2022-06-13 23:46:03.115376
# Unit test for function romanize
def test_romanize():
    text = data.Data().rus.word()
    assert isinstance(text, str)

    romanize(locale='ru')(text)

# Generated at 2022-06-13 23:46:13.262992
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    import mimesis.builtins
    with mimesis.builtins._Random(seed=0) as rnd:
        assert rnd.person.full_name() == 'Абрам Фед'
        assert rnd.address.country() == 'Швейцарія'

    with mimesis.builtins._Random(locale='ru', seed=0) as rnd:
        assert rnd.person.full_name() == 'Абрам Фед'
        assert rnd.address.country() == 'Швейцария'

    with mimesis.builtins._Random(locale='uk', seed=0) as rnd:
        assert rnd.person

# Generated at 2022-06-13 23:46:14.646789
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Русский')() == 'russkiy'

# Generated at 2022-06-13 23:46:19.642951
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.identifier import Identifier

    assert type(romanized(locale='ru')(Identifier.uuid)) == str
    assert type(romanized(locale='uk')(Identifier.uuid)) == str
    assert type(romanized(locale='kk')(Identifier.uuid)) == str

# Generated at 2022-06-13 23:46:23.266532
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'привет')() == 'privet'
    assert romanize('ru')(lambda: 'привет')() == 'privet'
    assert romanize('ru')(lambda: 'Привет, Мир')() == 'Privet, Mir'



# Generated at 2022-06-13 23:46:27.625283
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    @romanize('uk')
    @romanize('kk')
    def get_romanize():
        return 'Кремль'

    assert get_romanize() == 'Kreml'

# Generated at 2022-06-13 23:47:21.856541
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider as SPD

    spd = SPD()
    print(spd.full_name())

    name = spd.full_name(gender=Gender.MALE)
    print(name)
    romanized_name = romanized(name)
    print(romanized_name)

# Generated at 2022-06-13 23:47:31.026493
# Unit test for function romanize
def test_romanize():
    import unittest
    from mimesis.enums import Gender


# Generated at 2022-06-13 23:47:36.036007
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.en import TextSpecification
    txt = TextSpecification()
    assert txt.word() == 'hilarity'
    assert txt.word(romanize='uk') == 'хіларіті'
    assert txt.word(romanize='ru') == 'хиларити'
    assert txt.word(romanize='zh') == 'hilarity'

# Generated at 2022-06-13 23:47:38.661484
# Unit test for function romanize
def test_romanize():
    assert romanize('')(lambda: 'Test1')() == 'Test1'
    assert romanize('ru')(lambda: 'Привет, мир!')() == 'priveht, mir!'

# Generated at 2022-06-13 23:47:41.401253
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda : 'Привет')() == 'Privet'

# Generated at 2022-06-13 23:47:45.386769
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.text import Text
    from mimesis.enums import Locale

    text = Text(locale=Locale.RU)
    romanized_text = romanize('ru')(text.text)
    assert romanized_text.isascii()

# Generated at 2022-06-13 23:47:53.143922
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""

    @romanize(locale='uk')
    def test_func(number: int) -> str:
        """Test func."""
        return str(number)

    assert test_func(55) == '55'

    # Aliases
    @romanized(locale='uk')
    def test_func_alias(number: int) -> str:
        """Test func."""
        return str(number)

    assert test_func_alias(555) == '555'

# Generated at 2022-06-13 23:48:04.310236
# Unit test for function romanize
def test_romanize():
    test_word = romanize('ru')(lambda x: 'Привет, Мир!')
    test_word2 = romanize('uk')(lambda x: 'Привіт, Світ!')
    test_word3 = romanize('kk')(lambda x: 'Сәлем, дүние!')
    assert 'Privet, Mir!' == test_word
    assert 'Pryvit, Svit!' == test_word2
    assert 'Salem, dunie!' == test_word3

# Generated at 2022-06-13 23:48:13.554211
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    rp = RussiaSpecProvider(locale='ru')
    assert rp.romanize('Жизнь') == 'Zhizn'

    rp = RussiaSpecProvider(locale='uk')
    assert rp.romanize('Життя') == 'Zhyttya'

    rp = RussiaSpecProvider(locale='kk')
    assert rp.romanize('Жизнь') == 'Жизнь'

# Generated at 2022-06-13 23:48:21.812268
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider

    russian = RussianSpecProvider('ru')

    name = russian.name()
    assert name == romanize()(russian.name)(), \
        'Romanize decorator is broken'

    surname = russian.surname()
    assert surname == romanize()(russian.surname)(), \
        'Romanize decorator is broken'


test_romanize()


# Generated at 2022-06-13 23:39:28.281006
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Колобок')() == 'KOLOBOK'

# Generated at 2022-06-13 23:39:29.871601
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    pass

# Generated at 2022-06-13 23:39:32.511467
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def foo(a, b):
        return '{}{}'.format(a, b)

    assert foo('б', 'а') == 'ba'



# Generated at 2022-06-13 23:39:40.073400
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender
    from mimesis.typing import Seed
    from mimesis.utils import gen_seed
    from string import ascii_lowercase

    sp = RussiaSpecProvider(seed=gen_seed('123', '456'))

    def _get_romanized(seed: Seed, locale: str = 'ru') -> str:
        """Get Romanized string."""
        locale = locale.lower()
        sp = RussiaSpecProvider(seed=seed)
        romanized = sp.romanized(locale=locale)
        return romanized

    str_ = sp.text(length=10, alphabet=ascii_lowercase)
    romanized_str = _get_romanized(seed=gen_seed(), locale='ru')


# Generated at 2022-06-13 23:39:43.482423
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: '')() == ''
    assert romanized('ru')(lambda: 'Федот')().isalpha() is True

# Generated at 2022-06-13 23:39:48.656796
# Unit test for function romanize
def test_romanize():
    """Unit test."""
    expected_result = 'Ключ к блоку новостей'
    with_romanize = romanized()(lambda x: expected_result)
    without_romanize = lambda x: expected_result
    assert with_romanize() == expected_result
    assert without_romanize() == expected_result

# Generated at 2022-06-13 23:39:53.540752
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привет, мир!')() == 'Privet, mir!'
    assert romanize(locale='uk')(lambda: 'Привіт, світе!')() == 'Pryvit, svite!'
    assert romanize(locale='kk')(lambda: 'Сәлем, дүние!')() == 'Sälem, dünie!'

# Generated at 2022-06-13 23:39:58.069859
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    expected_result = "sergej"
    result = romanize(locale="ru")(lambda: "Сергей")()
    message = "Function romanize does not work properly."
    assert result == expected_result, message

# Generated at 2022-06-13 23:40:09.817849
# Unit test for function romanize
def test_romanize():
    @romanized('en')
    def foo():
        return 'Йорк был застроен им на столько, что теперь он полностью' \
               ' теряет форму города.'

    assert foo() == 'York byl zastroen im na stolko, chto teper on' \
                     ' polnostyu teryaet formu goroda.'

# Generated at 2022-06-13 23:40:15.783875
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.geographic import Geographic
    from mimesis.providers.personal import Personal

    geo = Geographic(Locale.UK)
    assert geo.province() == 'Тернопільська область'

    p = Personal(Locale.UK)
    assert p.surname() == 'Аслям'

# Generated at 2022-06-13 23:40:26.253152
# Unit test for function romanize
def test_romanize():
    import mimesis.providers.person as person
    provider = person.Person('ru')
    result = provider.romanize(provider.full_name(), locale='ru')
    assert isinstance(result, str)
    assert result != provider.full_name()

# Generated at 2022-06-13 23:40:30.433453
# Unit test for function romanize
def test_romanize():
    data.ROMANIZATION_DICT['ru'] = {'А': 'A'}

    @romanize('ru')
    def test_string():
        return 'А'

    assert test_string() == 'A'



# Generated at 2022-06-13 23:40:36.292182
# Unit test for function romanize
def test_romanize():
    # Arrange
    from mimesis.builtins.cyrillic import Cyrillic

    cy = Cyrillic('ru')
    # Act
    result = cy.romanize(cy.full_name())
    # Assert
    assert result == "Kartashov Aleksandr Aleksandrovich"
    assert cy.romanize("Карташов Александр Александрович") == result

# Generated at 2022-06-13 23:40:38.762509
# Unit test for function romanize
def test_romanize():
    for locale in ['ru', 'uk', 'kk']:
        assert romanize(locale)(lambda: 'Тест')() == 'Test'

# Generated at 2022-06-13 23:40:51.959951
# Unit test for function romanize
def test_romanize():
    # Test with Russian locale
    @romanize('ru')
    def cyrillic_ru() -> str:
        return 'Привет, мир!'
    assert cyrillic_ru() == 'Privet, mir!'

    # Test with Ukrainian locale
    @romanize('uk')
    def cyrillic_uk() -> str:
        return 'Привіт, світ!'
    assert cyrillic_uk() == 'Pryvit, svit!'

    # Test with Kazakh locale
    @romanize('kk')
    def cyrillic_kk() -> str:
        return 'Сәлем, дүние!'
    assert cyrillic_kk() == 'Sälem, dünie!'

# Generated at 2022-06-13 23:40:54.733150
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo():
        return 'привет'

    assert foo() == 'privet'

# Generated at 2022-06-13 23:40:59.355721
# Unit test for function romanize
def test_romanize():
    print(romanize('ru')(lambda: 'Привет'))
    try:
        romanize('asda')(lambda: 'Привет')
    except UnsupportedLocale:
        print('Expected error message')

# Generated at 2022-06-13 23:41:03.208249
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    from mimesis.builtins.text import Text

    text = Text('ru')
    assert text.text() == text.romanize()()

    text = Text('uk')
    assert text.text() == text.romanize()()

# Generated at 2022-06-13 23:41:08.758917
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Case

    @romanize('ru')
    def fake_name(case: Case = Case.UPPER):
        return 'Иванов Иван Иванович'

    name = fake_name()
    expected_name = 'Ivanov Ivan Ivanovich'
    assert name == expected_name

# Generated at 2022-06-13 23:41:17.863939
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Locale
    from mimesis.builtins.text import Text

    t = Text(Locale.ENGLISH)
    result = t.romanize('кириллица — ещё один алфавит.')
    assert result == 'kirillitsa — eshchë odin alfavit.'

    t = Text(Locale.ENGLISH)
    result = t.romanize('Привет, Κόσμε!')
    assert result == 'Privet, Kósme!'

# Generated at 2022-06-13 23:41:32.863597
# Unit test for function romanize
def test_romanize():
    """Test the romanization of the cyrillic text."""
    r_text = 'Romanized text'

    def romanize_this(text: str = '') -> str:
        """Romanize this."""
        return text

    test_text = 'Романизованный текст'
    assert romanize(locale='ru')(romanize_this)(test_text) == r_text

# Generated at 2022-06-13 23:41:38.507492
# Unit test for function romanize
def test_romanize():
    romanize_function = romanize('ru')
    @romanize_function
    def romanize_text():
        return u'Привет!'
    actual = romanize_text()
    assert actual == 'Privet!'



# Generated at 2022-06-13 23:41:46.223488
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_locale():
        return 'строка'
    assert romanize_locale() == 'stroka'

    @romanize('uk')
    def romanize_locale():
        return 'строка'
    assert romanize_locale() == 'strôka'

    @romanize('kk')
    def romanize_locale():
        return 'строка'
    assert romanize_locale() == 'strwqa'

    @romanize('af')
    def romanize_locale():
        return 'строка'
    assert romanize_locale() == 'строка'

# Generated at 2022-06-13 23:41:50.125970
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda x: 'Солнце')(None) == 'Solntse'



# Generated at 2022-06-13 23:42:00.903806
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    # pylint: disable = missing-docstring, invalid-name, expression-not-assigned
    import mimesis as ms

    # Текст в кириллице
    text_cyrillic = 'Лопасти ветра, охватывают море, окутая его туманным покрывалом.'
    text_lat = 'Lopasti vetra, okhvatyvajut more, okhvataja ego tumannym '\
               'pokryvalom.'

    # Текст на ан

# Generated at 2022-06-13 23:42:03.338633
# Unit test for function romanize
def test_romanize():
    def foo(text):
        return text

    bar = romanize('ru')(foo)
    assert bar('Привет') == 'Privet'
    assert bar('Привет, мир') == 'Privet mir'

# Generated at 2022-06-13 23:42:06.742487
# Unit test for function romanize
def test_romanize():
    assert romanize()("БРАТЬЯ") == "BRAT'JA"
    assert romanize("uk")("ПРИВІТ") == "PRIVIT"

# Generated at 2022-06-13 23:42:11.603197
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Кузьма')() == 'Kuzma'
    assert romanized('uk')(lambda: 'Галина')() == 'Halyna'
    assert romanized('kk')(lambda: 'Құралдан')() == 'Quraldan'

# Generated at 2022-06-13 23:42:15.316884
# Unit test for function romanize
def test_romanize():
    romanized_kazakh = romanize('kk')('Абай')
    assert romanized_kazakh == 'Abаy'

# Generated at 2022-06-13 23:42:25.929415
# Unit test for function romanize
def test_romanize():
    def ru_func():
        return 'привет'

    def uk_func():
        return 'привіт'

    def kk_func():
        return 'сәлем'

    @romanize(locale='ru')
    def ru_deco_func():
        return 'привет'

    @romanize(locale='uk')
    def uk_deco_func():
        return 'привіт'

    @romanize(locale='kk')
    def kk_deco_func():
        return 'сәлем'

    assert ru_func() == ru_deco_func()
    assert uk_func() == uk_deco_func()
    assert kk_func()

# Generated at 2022-06-13 23:42:36.917564
# Unit test for function romanize
def test_romanize():
    assert romanize()



# Generated at 2022-06-13 23:42:39.863826
# Unit test for function romanize
def test_romanize():
    transliterated = romanize('ru')
    @transliterated
    def test():
        return 'ЪъъъъъъъъЯяЬь'
    assert test() == 'yyyyyyyyya'

# Generated at 2022-06-13 23:42:47.936909
# Unit test for function romanize
def test_romanize():
    @romanize()
    def test(locale):
        return {locale: 'Привет, мир!'}
    assert test('ru') == 'Privyet, mir!'

    @romanized()
    def test(locale):
        return {locale: 'Привет, мир!'}
    assert test('ru') == 'Privyet, mir!'

# Generated at 2022-06-13 23:42:56.114125
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')('Россия') == 'Rossiya'
    assert romanize('ru')('Россия') == 'Rossiya'
    assert romanize('kk')('Казахстан') == 'Qazaqstan'
    assert romanize('uk')('Україна') == 'Ukrayina'

# Generated at 2022-06-13 23:42:58.324790
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Сложный пример 123')() == 'Slozhnyy primer 123'

# Generated at 2022-06-13 23:43:01.825683
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""
    assert romanize()('кириллица') == 'kirillica'

# Generated at 2022-06-13 23:43:06.433919
# Unit test for function romanize
def test_romanize():
    @romanize()
    def get_text() -> str:
        return 'Текст латиницей'

    assert get_text() == 'Tekst latinicey'

# Generated at 2022-06-13 23:43:15.949335
# Unit test for function romanize
def test_romanize():
    """Test romanize function in mimesis.base.
    """

    @romanize('ru')
    def romanize_ru(size: int = 8) -> str:
        """Get a romanized random string.

        :param size: Size of string.
        :return: Romanized string.
        """
        letters = (
            data.CYRILLIC_ALPHABET.get('ru') +
            data.COMMON_LETTERS.get('ru')
        )
        return data.create_token(size, letters)

    assert romanize_ru(5)
    assert len(romanize_ru(10)) == 10

    romanize_uk = romanize('uk')(romanize_ru)
    assert romanize_uk(5)

# Generated at 2022-06-13 23:43:17.664651
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'

# Generated at 2022-06-13 23:43:19.069182
# Unit test for function romanize
def test_romanize():
    result = romanized()
    assert callable(result), "Decorator is not callable"

# Generated at 2022-06-13 23:43:34.523696
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.address import Address
    from mimesis.providers.geography import Geography

    address = Address('ru')
    geography = Geography('ru')

    assert address.address(use_romanization=True)  # noqa: WPS421
    assert geography.country(use_romanization=True)  # noqa: WPS421

# Generated at 2022-06-13 23:43:41.357230
# Unit test for function romanize
def test_romanize():
    from mimesis import Person
    person = Person('ru')
    assert isinstance(person.full_name, str)
    assert person.full_name() != person.full_name(romanize=True)
    assert person.full_name(romanize=True) != person.full_name(romanize=False)
    assert person.full_name(romanize=False) == person.full_name()
    assert person.full_name(romanize=True) != person.full_name(romanize='UK_UK')


# Generated at 2022-06-13 23:43:44.495621
# Unit test for function romanize
def test_romanize():
    assert 'beef' == romanize(locale='en')
    assert 'beef' == romanized(locale='en')

# Generated at 2022-06-13 23:43:47.295874
# Unit test for function romanize
def test_romanize():
    from . import en
    assert en.Person().full_name_ru == en.Person().full_name_ru_Latin



# Generated at 2022-06-13 23:43:49.988096
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person
    p = Person()
    assert p.full_name(locale='ru') == p.full_name(locale='ru')

# Generated at 2022-06-13 23:43:53.267262
# Unit test for function romanize
def test_romanize():
    assert 'Hello world!' == romanize('ru')(lambda: 'Привет мир!'), \
        'It should be Hello world!'

# Generated at 2022-06-13 23:44:03.679690
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""
    assert romanize().romanize_deco(lambda *args, **kwargs: 'Привет, Мир!')() == 'Pryvit, Mir!'
    assert romanize('ru').romanize_deco(lambda *args, **kwargs: 'Привет, Мир!')() == 'Privet, Mir!'
    assert romanize('uk').romanize_deco(lambda *args, **kwargs: 'Привіт, Світ!')() == 'Pryvit, Svit!'

# Generated at 2022-06-13 23:44:15.313804
# Unit test for function romanize
def test_romanize():
    """Test romanization."""
    assert romanize()(lambda: 'Съешь же ещё этих мягких французских булок')() == 'Sʺeshʹ zhe yeshchë etikh myagkikh frantsuzskikh bulok'

# Generated at 2022-06-13 23:44:22.878858
# Unit test for function romanize
def test_romanize():
    """Test romanize()"""
    from mimesis.enums import Locale
    from mimesis.providers.person import Person


    def romanized_func(locale, cls):

        @romanize(locale=locale)
        def romanize_deco(cls):
            return cls.name(locale=locale)

        return romanize_deco


    romanized_func = romanized_func(Locale.UKRAINIAN, Person(Locale.UKRAINIAN))
    assert romanized_func(Person(Locale.UKRAINIAN)) == 'Yevhen Mykytenko'

    romanized_func_1 = romanized_func(Locale.RUSSIAN, Person(Locale.RUSSIAN))
    assert romanized

# Generated at 2022-06-13 23:44:33.898454
# Unit test for function romanize
def test_romanize():
    """Check that romanization works as expected."""
    assert romanize('uk')('Привіт') == 'Pryvit'
    assert romanized('ru')('Привет') == 'Privet'
    assert romanized('kk')('Сәлем') == 'Salem'
    assert romanized('ru')('ё') == 'yo'
    assert romanized('ru')('ёа') == 'yoa'
    assert romanized('ru')('аё') == 'ayo'

# Generated at 2022-06-13 23:44:58.521820
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def x(a):
        return a

    assert x('абвгдеё') == 'abvgdee'
    assert x('АБВГДЕЁ') == 'ABVGDEE'
    assert x('мобильный') == 'mobilnyi'
    assert x('мобильный.') == 'mobilnyi.'
    assert x('мобильный!') == 'mobilnyi!'
    assert x('мобильный,') == 'mobilnyi,'
    assert x('мобильный?') == 'mobilnyi?'


# Generated at 2022-06-13 23:45:02.258810
# Unit test for function romanize
def test_romanize():
    @romanized()
    def romanize_test() -> str:
        return 'Гай'
    assert romanize_test()

# Generated at 2022-06-13 23:45:03.871884
# Unit test for function romanize
def test_romanize():
    romanized = romanize(locale='ru')(str)
    assert romanized('Феникс') == 'Fenikx'

# Generated at 2022-06-13 23:45:12.963308
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет, как дела?')() == 'Privet, kak dela?'
    assert romanize('uk')(lambda: 'Привіт, як справи?')() == 'Pryvit, yak spravy?'
    assert romanize('kk')(lambda: 'Сәлем, күнің келесі күні сайын ба?')() == \
        'Salem, künĭng kelesi künĭ saıyn ba?'

    # Test common chars (e.g. spaces, punctuation)

# Generated at 2022-06-13 23:45:15.772763
# Unit test for function romanize
def test_romanize():
    assert (romanize(locale='ru')(lambda : 'моё слово'))('моё слово') == 'myo slovo'

# Generated at 2022-06-13 23:45:21.187207
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.person import Person

    p = Person

    assert romanize is not None
    assert romanized is not None
    assert p.romanize is not None
    assert p.romanized is not None

    assert p.romanize('Привет!') == 'Priviet!'
    assert isinstance(p.romanize('Привет!'), str) is True
    assert isinstance(p.romanize('Привет!', 'ru'), str) is True

    try:
        p.romanize('Привет!', 'zz')
    except UnsupportedLocale:
        assert True
    else:
        assert False


test_romanize()

# Generated at 2022-06-13 23:45:24.379338
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def rus():
        return 'привет, мир!'
    assert rus() == 'privet, mir!'

# Generated at 2022-06-13 23:45:34.578460
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.data import romanization_dict
    romanize_ru = romanize('ru')
    assert romanize_ru('Просто прекрасно!') == "Prosto prekrasno!"
    assert romanize_ru('Москва́') == "Moskva"
    assert romanize_ru('Миша') == 'Misha'
    assert romanize_ru('Южная Корея') == 'Yuzhnaya Koreya'
    assert romanize_ru('пжэх') == 'pzhjakh'

    romanize_uk = romanize('uk')

# Generated at 2022-06-13 23:45:36.194741
# Unit test for function romanize
def test_romanize():
    assert romanized()(lambda: 'Иванов')() == 'Ivanov'

# Generated at 2022-06-13 23:45:37.304131
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider


# Generated at 2022-06-13 23:46:06.269013
# Unit test for function romanize
def test_romanize():
    import mimesis
    ru = mimesis.Generic('ru')
    ru.romanize()
    ru.romanize

    ru.romanize('ru')
    ru.romanize(locale='ru')

    ru.romanize('uk')
    ru.romanize(locale='uk')

    ru.romanize('kk')
    ru.romanize(locale='kk')

    ru.romanize('some_locale')
    ru.romanize(locale='some_locale')

# Generated at 2022-06-13 23:46:13.971428
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian_text():
        return 'Привет, мир!'

    assert russian_text() == 'Privet, mir!'

    @romanize(locale='uk')
    def ukrainian_text():
        return 'Привіт, світ!'

    assert ukrainian_text() == 'Pryvit, svit!'

    @romanize(locale='kk')
    def kazakh_text():
        return 'Қалайсың?'

    assert kazakh_text() == 'Qalaısıñ?'



# Generated at 2022-06-13 23:46:19.239592
# Unit test for function romanize
def test_romanize():
    from mimesis import Person
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider

    person = Person(RussiaSpecProvider)
    name = person.full_name(gender=Gender.MALE)
    assert romanized(locale='ru')(name)

COUNT = 0
EQUAL = 1


# Generated at 2022-06-13 23:46:21.828341
# Unit test for function romanize
def test_romanize():
 
    @romanize('ru')
    def romanize_some_russian_text():
        return "Привет, Мир!"

    assert romanize_some_russian_text() == "Privet, Mir!"

# Generated at 2022-06-13 23:46:24.675379
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Jfönk') == 'Jfönk'
    assert romanize(locale='')(lambda: 'Jfönk') == 'Jfönk'

# Generated at 2022-06-13 23:46:26.251288
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:46:29.064709
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: "КРАКЕН ЛИЛИТ") == "KROKEN LILIT"

# Generated at 2022-06-13 23:46:31.796871
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def foo(foo_data):
        return foo_data

    assert foo('Здравствуйте!') == 'Zdravstvujte!'

# Generated at 2022-06-13 23:46:39.011007
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    # Simple test
    @romanize('ru')
    def gen_name():
        return 'Алексей'

    romanized_txt = gen_name()
    assert romanized_txt == 'Aleksey'

    # Chaining decorators
    @romanize('ru')
    @romanize('uk')
    def gen_name():
        return 'Алексей'

    romanized_txt = gen_name()
    assert romanized_txt == 'Aleksey'

# Generated at 2022-06-13 23:46:42.042238
# Unit test for function romanize
def test_romanize():
    assert romanized()("Привет, Мир!") == "Privet, Mir!"

# Generated at 2022-06-13 23:47:17.762286
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет, мир!')() == 'Privet, mir!'
    assert romanize('ru')(lambda: 'Привет, мир! А вот и пунктуация, '
                                  'тире, и знак собачки: @')() == \
        'Privet, mir! A vot i punktuatsiya, tire, i znak sobacki: @'


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:47:20.385842
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    @romanize('uk')
    def f():
        return "Привіт, світ!"

    assert f() == "Pryvit, svit!"

# Generated at 2022-06-13 23:47:26.350986
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    assert romanize(locale='ru')(lambda: 'россия') == 'rossiya'
    assert romanize(locale='kk')(lambda: 'казахстан') == 'qazaqstan'
    assert romanize(locale='uk')(lambda: 'україна') == 'ukrayina'

# Generated at 2022-06-13 23:47:37.374828
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender

    from .person import Person

    tr = Person(locale='tr')
    ru = Person(locale='ru')

    assert ru.full_name(gender=Gender.MALE) == 'Павел Семёнов'

    assert ru.full_name(gender=Gender.MALE,
                        romanize=True) == 'Pavel Semënov'

    assert ru.full_name(gender=Gender.MALE,
                        romanize='ru') == 'Pavel Semënov'

    assert ru.full_name(gender=Gender.MALE,
                        romanize='uk') == 'Павел Семёнов'


# Generated at 2022-06-13 23:47:42.164230
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    assert romanize('ru')(lambda: 'Привет, Мимесис!'.lower()) == 'privet, mimesis!'
    assert romanize('uk')(lambda: 'Привіт, Мімесіс!'.lower()) == 'pryvit, mimesis!'
    assert romanize('kk')(lambda: 'Сәлем Мимесис!'.lower()) == 'salem mimesis!'

# Generated at 2022-06-13 23:47:43.625720
# Unit test for function romanize
def test_romanize():
    """Tests for function romanize."""
    @romanize('ru')
    def data_from_ru():
        return data.CYRILLIC_LETTERS['ru']

    assert data_from_ru() == ascii_letters

# Generated at 2022-06-13 23:47:53.879879
# Unit test for function romanize
def test_romanize():
    # Test for Russian locale
    assert romanize('ru')(lambda: 'Привет, мир!')() == 'Privet, mir!'

    # Test for Ukrainian locale
    assert romanize('uk')(lambda: 'Привіт, світ!')() == 'Pryvit, svit!'

    # Test for Kazakh locale
    assert romanize('kk')(lambda: 'Сәлем, дүние!')() == 'Sälem, dünie!'

    # Test for wrong locale
    assert romanize('en')(lambda: 'Привет, мир!')() == ''

# Generated at 2022-06-13 23:47:57.951335
# Unit test for function romanize
def test_romanize():
    import doctest

    doctest.testmod(data, verbose=False,
                    optionflags=doctest.ELLIPSIS |
                    doctest.NORMALIZE_WHITESPACE | doctest.REPORT_NDIFF)

# Generated at 2022-06-13 23:47:58.602229
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:47:59.969754
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanized()

# Generated at 2022-06-13 23:48:43.886945
# Unit test for function romanize
def test_romanize():
    # This is a test for romanize
    print(romanize())

# Generated at 2022-06-13 23:48:47.708742
# Unit test for function romanize
def test_romanize():
    assert romanize.romanize_deco("test") == "test"
    assert romanize.romanize_deco("привет") == "privet"

# Generated at 2022-06-13 23:48:56.589734
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider
    cyrillic = RussiaSpecProvider()

    @russianize(locale='ru')
    def f():
        return cyrillic.full_name()

    @russianize(locale='ru')
    def f2():
        return cyrillic.full_name() + " " + cyrillic.full_name()

    @russianize(locale='uk')
    def f3():
        return cyrillic.full_name() + " " + cyrillic.full_name()

    @russianize(locale='kk')
    def f4():
        return cyrillic.full_name() + " " + cyrillic.full_name()

    f()
    f2()
    f3()
    f4

# Generated at 2022-06-13 23:48:58.953217
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def func():
        return 'Привет, мир!'

    assert func() == 'Privet, mir!'

# Generated at 2022-06-13 23:49:07.440244
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def mock_ru():
        return 'Тестовая строка.'

    @romanize('uk')
    def mock_uk():
        return 'Тестова стрічка.'

    @romanize('kk')
    def mock_kk():
        return 'Тесттік мәтін.'

    assert mock_ru == 'Testovaya stroka.'
    assert mock_uk == 'Testova strochka.'
    assert mock_kk == 'Testtik mәtin.'

# Generated at 2022-06-13 23:49:13.711486
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'привет')() == 'privet'
    assert romanize('ru')(lambda x: 'Привет')() == 'Privet'

# Generated at 2022-06-13 23:49:20.877629
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'строка') == 'stróka'
    assert romanize(locale='uk')(lambda: 'строка') == 'stróka'
    assert romanize(locale='kk')(lambda: 'строка') == 'stróka'
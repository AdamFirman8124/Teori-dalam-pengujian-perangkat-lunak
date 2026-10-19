

# Generated at 2022-06-13 23:39:34.051962
# Unit test for function romanize
def test_romanize():
    assert romanize()('Привет, Мими') == 'Privet, Mimi'
    assert romanize()('Привет, Мимизики') == 'Privet, Mimiiziki'

# Generated at 2022-06-13 23:39:46.331168
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    ru = RussiaSpecProvider

    assert ru.romanize('Привет!') == 'Privet!'
    assert ru.romanize('Как дела?') == 'Kak dela?'
    assert ru.romanize('Вон вы негодяи.') == 'Von vy negodyai.'

    # Test for backward compatibility
    assert ru.romanized('Привет!') == 'Privet!'
    assert ru.romanized('Как дела?') == 'Kak dela?'
    assert ru.romanized('Вон вы негодяи.') == 'Von vy negodyai.'

# Generated at 2022-06-13 23:39:53.238066
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def get_rus_name():
        return 'Вася Пупкин'

    assert get_rus_name() == 'Vasya Pupkin'

    @romanize('kk')
    def get_kaz_name():
        return 'Болат Байбахтыр'

    assert get_kaz_name() == 'Bolat Baïbatır'

    @romanize('uk')
    def get_ukr_name():
        return 'Петро Шевченко'

    assert get_ukr_name() == 'Petro Shevchenko'

# Generated at 2022-06-13 23:40:01.764196
# Unit test for function romanize
def test_romanize():
    def _func(*args, **kwargs):
        return 'Какой-то текст на кириллице'

    trans_func = romanize('ru')(_func)
    assert trans_func() == 'Kakoy-to tekst na kirillice'

    trans_func_uk = romanize('uk')(_func)
    assert trans_func_uk() == 'Kakoy-to tekst na kirillitsi'

    trans_func_kk = romanize('kk')(_func)
    assert trans_func_kk() == 'Kaqoy-to tekst na kirillíce'

# Generated at 2022-06-13 23:40:08.482045
# Unit test for function romanize
def test_romanize():
    # Decorating of the function.
    @romanize('ru')
    def get_number(seed: int = None) -> str:
        return '1'

    assert get_number() == '1'

    # Calling the get_number() will return '1'.
    assert get_number.__name__ == 'get_number'
    assert get_number.__doc__ == 'Romanize the cyrillic text.\n\n    ' \
                                 'Transliterate the cyrillic script into ' \
                                 'the latin alphabet.\n\n    ' \
                                 '.. note:: At this moment it works only ' \
                                 'for `ru`, `uk`, `kk`.\n\n    :param ' \
                                 'locale: Locale code.\n    :return: ' \
                

# Generated at 2022-06-13 23:40:09.856607
# Unit test for function romanize
def test_romanize():
    romanize(locale='ru')(lambda: 'asd')()

# Generated at 2022-06-13 23:40:13.438525
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def func(): return 'Очень длинное слово'
    assert func() == 'Ochen\' dlinnoe slovo'

# Generated at 2022-06-13 23:40:25.724810
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Person
    # Russian locale
    romanize_ru = Person('ru')
    assert romanize_ru.full_name() == 'Николай Степанович Рудаков'

    romanized_ru = Person('ru', romanize=True)
    assert romanized_ru.full_name() == 'Nikolai Stepanovich Rudakov'

    # Ukrainian locale
    romanize_uk = Person('uk')
    assert romanize_uk.full_name() == 'Василь Іванович Мисирний'

    romanized_uk = Person('uk', romanize=True)
    assert romanized

# Generated at 2022-06-13 23:40:29.330850
# Unit test for function romanize
def test_romanize():
    assert romanize()(
        lambda: 'поехали на отдых')(
    ) == 'poekhali na otdykh'

# Generated at 2022-06-13 23:40:31.640007
# Unit test for function romanize
def test_romanize():
    """Test for romanize decorator."""
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:40:38.440637
# Unit test for function romanize
def test_romanize():
    assert isinstance(romanize, Callable)

# Generated at 2022-06-13 23:40:45.038944
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.utils import lowercase
    from mimesis.enums import Gender

    class Person(object):
        def __init__(self, gender):
            self._gender = gender
            self._name = lowercase('name', gender=gender)

        @romanize()
        def name(self):
            """

            :return: 
            """
            return self._name

    assert Person(Gender.FEMALE).name()

# Generated at 2022-06-13 23:40:53.650615
# Unit test for function romanize
def test_romanize():
    """Test for romanize function."""
    from mimesis.providers.identity import Identity
    from mimesis.providers.misc import Misc
    from mimesis.providers.person import Person

    romanize_list = ['ru', 'uk', 'kk']
    misc = Misc(locale='uk')
    person = Person(locale='uk')
    identity = Identity(locale='uk')
    for locale in romanize_list:
        print('\nTesting romanize for {}'.format(locale))
        assert romanize(locale)(misc.word)() != ''
        assert romanize(locale)(person.full_name)() != ''
        assert romanize(locale)(identity.passport_number)() != ''

# Generated at 2022-06-13 23:41:02.496587
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'Китай')(' ') == 'Kitaj'
    assert romanize('ru')(lambda x: 'Россия')(' ') == 'Rossiya'
    assert romanize('uk')(lambda x: 'Україна')(' ') == 'Ukraina'
    assert romanize('kk')(lambda x: 'Қазақстан')(' ') == 'Qazaqstan'


# Generated at 2022-06-13 23:41:06.538954
# Unit test for function romanize
def test_romanize():
    uk = romanize(locale='uk')(lambda: 'тест')
    rus = romanize(locale='ru')(lambda: 'тест')
    kk = romanize(locale='kk')(lambda: 'сын')
    assert uk == 'test'
    assert rus == 'test'
    assert kk == 'syn'

# Generated at 2022-06-13 23:41:09.988339
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import TextSpecifier

    assert TextSpecifier('en').latinify('Привет!') == 'Privet!'

# Generated at 2022-06-13 23:41:14.176074
# Unit test for function romanize
def test_romanize():
    @romanize(locale='uk')
    def test(parameter):
        return parameter

    assert test('Васин різдвяний козак') == 'Vasin rizdvyanyj kozak'

# Generated at 2022-06-13 23:41:16.311588
# Unit test for function romanize
def test_romanize():
    assert ('проверка' == romanize('ru')('проверка')) is True

# Generated at 2022-06-13 23:41:22.048074
# Unit test for function romanize
def test_romanize():
    """Romanize Test."""
    from mimesis.enums import Gender

    import mimesis.builtins
    kz = mimesis.builtins.Kazakh(locale='kk')
    kz.seed(123)
    assert kz.person.full_name(gender=Gender.FEMALE) == 'Ажайдан Аққөрқызы'
    assert kz.person.full_name(gender=Gender.FEMALE,
                               romanized=True) == 'Ajajdan Akkorkyzy'

# Generated at 2022-06-13 23:41:27.757117
# Unit test for function romanize
def test_romanize():
    locale = 'ru'
    @romanize(locale)
    def test():
        return "Кто тут? Я, Супермен!"

    assert test() == 'Kto tut? Ya, Superman!'

# Generated at 2022-06-13 23:41:39.679426
# Unit test for function romanize
def test_romanize():
    lst = ['ВИСОКОЕ', 'ВИСОКОЕ', 'ВИСОКОЕ', 'ВИСОКОЕ']
    decorated_romanized = romanize()(lambda x: x)

    for i in lst:
        assert decorated_romanized(i) == 'VISOKOE'

# Generated at 2022-06-13 23:41:42.621078
# Unit test for function romanize
def test_romanize():
    #return mimesis.__version__
    from mimesis.providers.person import Person
    import mimesis
    p = Person(locale='ru')
    assert p.full_name() == mimesis.__version__

# Generated at 2022-06-13 23:41:48.721866
# Unit test for function romanize
def test_romanize():
    # This is a test function
    assert romanize('ru')(lambda: 'Я люблю блинчики с творогом')().startswith('YA')
    assert romanize('uk')(lambda: 'Я люблю блинчики с творогом')().startswith('YA')
    assert romanize('kk')(lambda: 'Я люблю блинчики с творогом')().startswith('YA')

# Generated at 2022-06-13 23:41:52.697130
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def get_some_data() -> str:
        return "Привет мир!"

    assert get_some_data() == 'Privet mir!'



# Generated at 2022-06-13 23:41:55.828293
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    @romanize(locale='ru')
    def generator():
        return 'привет'

    assert generator() == 'privet'



# Generated at 2022-06-13 23:42:00.066358
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussianSpecProvider

    russia = RussianSpecProvider()
    assert romanize('ru')(russia.name) == 'Peter Ivanov'

# Generated at 2022-06-13 23:42:03.047828
# Unit test for function romanize
def test_romanize():
    r = romanized('ru')(lambda: 'Привет, Как дела?')()
    assert r == 'Privet, Kak dela?'

# Generated at 2022-06-13 23:42:11.205182
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda x: 'Ребят, как дела?')() == 'Reybyat, kak dela?'
    assert romanize()(lambda x: 'Так вот он то кому благосклонность выдаёт')() == \
        'Tak vot on to komu blagosklonnost vydaët'


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:42:17.744281
# Unit test for function romanize
def test_romanize():
    romanize('ru')(lambda x: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')() == 'ABVGDEEZHZIYKLMNOPRSTUFHCCHSHCH""Y""E&IU&IA'

# Generated at 2022-06-13 23:42:20.656507
# Unit test for function romanize
def test_romanize():
    romanized_string = romanize()(lambda: 'Как тебя зовут?')()
    assert romanized_string == 'Kak tebya zovut?'

# Generated at 2022-06-13 23:42:28.922548
# Unit test for function romanize
def test_romanize():
    pass
    # if not romanize("ru")(lambda: "artem") == "artem":
    #     raise AssertionError("Incorrect romanization.")

# Generated at 2022-06-13 23:42:33.047096
# Unit test for function romanize
def test_romanize():
    # Given
    input_str = 'Здравствуй мир'

    # When
    romanized_str = romanized('ru')(lambda: input_str)()

    # Then
    assert romanized_str == 'Zdràvstvuy mir'

# Generated at 2022-06-13 23:42:33.551455
# Unit test for function romanize
def test_romanize():
    pass

# Generated at 2022-06-13 23:42:38.099075
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'
    assert romanize('ru')(lambda: 'Привет')() == 'Privet'
    assert romanize('uk')(lambda: 'Привет')() == 'Pryvit'
    assert romanize('kk')(lambda: 'Привет')() == 'Prıvet'

# Generated at 2022-06-13 23:42:42.897013
# Unit test for function romanize
def test_romanize():
    import pytest
    from mimesis.builtins.numbers import Numbers

    @romanize('ru')
    def romanize_number(number: int) -> str:
        num = Numbers()
        return num.random_int(min_value=number, max_value=number + 9)

    assert romanize_number(1) != '1'
    assert romanize_number(5) == '5'
    with pytest.raises(UnsupportedLocale):
        @romanize('pl')
        def romanize_number(number: int) -> str:
            num = Numbers()
            return num.random_int(min_value=number, max_value=number + 9)

# Generated at 2022-06-13 23:42:44.736725
# Unit test for function romanize
def test_romanize():
    cases = []
    assert romanize()(cases) == ''

# Generated at 2022-06-13 23:42:57.942912
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: "Привет")() == 'Privet'
    assert romanize(locale='ru')(lambda: "Здравствуйте, это тест")() == 'Zdravstvujte, eto test'
    assert romanize(locale='uk')(lambda: "Привіт")() == 'Pryvit'
    assert romanize(locale='uk')(lambda: "Вітання, це тест")() == 'Vitannya, ce test'
    assert romanize(locale='kk')(lambda: "Hello")() == 'Hәllә'
    assert r

# Generated at 2022-06-13 23:43:02.033122
# Unit test for function romanize
def test_romanize():
    assert romanized()('Привіт') == 'Privit'
    assert romanized()('Привет') == 'Privet'

# Generated at 2022-06-13 23:43:16.626742
# Unit test for function romanize
def test_romanize():
    def romanized_word(word: str) -> str:
        return romanize()(lambda: word)()

    assert romanized_word('Яблоко') == 'Yabloko'
    assert romanized_word('курица') == 'kuritsa'
    assert romanized_word('яблоко') == 'yabloko'
    assert romanized_word('пиво') == 'pivo'
    assert romanized_word('картофель') == 'kartofel'
    assert romanized_word('женщина') == 'zhenschina'
    assert romanized_word('машина') == 'mashina'
    assert r

# Generated at 2022-06-13 23:43:19.036376
# Unit test for function romanize
def test_romanize():
    """Test romanize."""
    assert romanized('ru')(lambda: 'привет')() == 'privet'


if __name__ == "__main__":
    test_romanize()

# Generated at 2022-06-13 23:43:31.671094
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def r_test(text: str) -> str:
        return text

    assert r_test(text='Мама мила раму.') == 'Mama mila ramu.'

    @romanized(locale='ru')
    def test(text: str) -> str:
        return text

    assert test(text='Мама мила раму.') == 'Mama mila ramu.'

# Generated at 2022-06-13 23:43:33.100507
# Unit test for function romanize
def test_romanize():
    assert romanized()(lambda: 'hello')() == 'hello'

# Generated at 2022-06-13 23:43:34.465485
# Unit test for function romanize
def test_romanize():
    assert isinstance(romanize, object)
    assert callable(romanize)

# Generated at 2022-06-13 23:43:39.651613
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins
    from mimesis.enums import Gender

    person = mimesis.builtins.Person('ru')

    assert person.full_name(gender=Gender.MALE, romanize=True) == \
        person.full_name(gender=Gender.MALE, romanize=False)

# Generated at 2022-06-13 23:43:44.212341
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')('Море') == 'More'
    assert romanized('uk')('Море') == 'More'
    assert romanized('kk')('Море') == 'More'

# Generated at 2022-06-13 23:43:55.782213
# Unit test for function romanize
def test_romanize():
    class Romanized(object):
        @romanize(locale="ru")
        def romanize_ru(self, arg):
            return arg

        @romanize(locale="uk")
        def romanize_uk(self, arg):
            return arg

        @romanize(locale="kk")
        def romanize_kk(self, arg):
            return arg

    r = Romanized()

    assert r.romanize_ru("Русский") == "Russkiy"
    assert r.romanize_uk("Українська") == "Ukrainska"
    assert r.romanize_kk("Қазақша") == "Qazaqsha"

# Generated at 2022-06-13 23:43:59.022176
# Unit test for function romanize
def test_romanize():
    assert romanized(func=lambda x: 'Тестовая функция', locale='ru')() == 'Testovaya funktsiya'  # noqa

# Generated at 2022-06-13 23:44:02.667479
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.enums import Locale
    from mimesis.providers.personal import Personal
    p = Personal('ru')
    assert p._romanize('Дима') == 'Dima'

# Generated at 2022-06-13 23:44:06.877597
# Unit test for function romanize
def test_romanize():
    # GIVEN
    from mimesis.builtins import RussiaSpecProvider as RS
    rs = RS()

    # WHEN
    text = rs.address.city()
    romanized_text = rs.address.romanized.city()

    # THEN
    assert romanize(locale='ru')(lambda: text)() == romanized_text

# Generated at 2022-06-13 23:44:14.763827
# Unit test for function romanize
def test_romanize():
    @romanize(locale='kk')
    def test_ru(seed):
        return 'Алғашқы Россия Біріккен Советтік Республикасының'

    assert test_ru(1) == 'Algashqy Rossiya Birikken Sovettik Respublikasynyn'

# Generated at 2022-06-13 23:44:37.242989
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    import random
    import pytest
    from mimesis.enums import Locale
    from mimesis.builtins import Text


    # Test for supported locales
    @romanized(locale=Locale.RU)
    def test_string_1():
        text = Text()
        return text.text(length=random.randint(1, 100))

    @romanized(locale=Locale.UK)
    def test_string_2():
        text = Text()
        return text.text(length=random.randint(1, 100))

    @romanized(locale=Locale.KK)
    def test_string_3():
        text = Text()
        return text.text(length=random.randint(1, 100))

    assert test_string

# Generated at 2022-06-13 23:44:38.539502
# Unit test for function romanize
def test_romanize():
    """Test romanize function."""
    pass

# Generated at 2022-06-13 23:44:41.687635
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    person = Person('ru')
    assert person.romanize(person.full_name()) == person.full_name()

# Generated at 2022-06-13 23:44:58.623455
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.text import Text

    text_ru = Text(Language.RUSSIAN)

    @romanize('ru')
    def romanize_test():
        return text_ru.word()

    assert romanize_test()

# Generated at 2022-06-13 23:45:06.522650
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person

    p = Person('ru')

    @romanize('ru')
    def romanized_name():
        return p.full_name(gender=Gender.MALE)

    assert romanized_name() in data.ROMANIZATION_DICT['ru']

# Generated at 2022-06-13 23:45:15.402758
# Unit test for function romanize
def test_romanize():
    data = {
        'ru': 'Привет, мир!',
        'uk': 'Привiт, свiте!',
        'kk': 'Сәлем, дүние!',
    }
    for key, value in data.items():
        assert romanize(key)(lambda: value)() == 'Privet, mir!'

# Generated at 2022-06-13 23:45:27.076041
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_test(txt: str) -> str:
        return txt

    assert romanize_test("Привет") == "Privet"
    assert romanize_test("ПРИВЕТ") == "PRIVET"
    assert romanize_test("ТЕСТ") == "TEST"
    assert romanize_test("Привет мир!") == "Privet mir!"
    assert romanize_test("Привет мир! Как дела?") == "Privet mir! Kak dela?"

# Generated at 2022-06-13 23:45:30.106248
# Unit test for function romanize
def test_romanize():
    expected = romanized('ru')(lambda x: 'привет, мир!')()
    assert expected == 'privet, mir!'

# Generated at 2022-06-13 23:45:33.953941
# Unit test for function romanize
def test_romanize():
    import mimesis
    r = mimesis.Personal('ru')

    assert (r.full_name(romanize=True) == r.full_name(romanize='ru'))
    assert (r.full_name(romanize='kk') == r.full_name(romanize='kk'))

# Generated at 2022-06-13 23:45:36.185018
# Unit test for function romanize
def test_romanize():
  @romanized('en')
  def get_a_string():
    return 'Хай'

  assert get_a_string() == 'Xai'

# Generated at 2022-06-13 23:46:20.311915
# Unit test for function romanize
def test_romanize():
    """Test function romanize.

    For more information see the docstring.
    """

    from mimesis import Person
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender

    address_ru = RussiaSpecProvider()

    p = Person('ru')

    # test with all data
    output = p.full_name()
    print(output)
    assert output

    # test with only first name
    output = p.first_name(gender=Gender.MALE)
    print(output)
    assert output

    # test with first and last name
    output = p.name(gender=Gender.MALE)
    print(output)
    assert output

    # test with getting full name of person
    output = p.full_name(gender=Gender.MALE)

# Generated at 2022-06-13 23:46:30.447425
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def romanizer(text: str) -> str:
        return text

    assert romanizer('Объект') == "Ob'ekt"
    assert romanizer('Объём') == "Ob'yom"

    @romanized(locale='ru')
    def romanizer(text: str) -> str:
        return text

    assert romanizer('Объект') == "Ob'ekt"
    assert romanizer('Объём') == "Ob'yom"

# Generated at 2022-06-13 23:46:36.662025
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет, Мимесис! Как дела?')() == \
        'Privet, Mimesis! Kak dela?'
    assert romanize('uk')(lambda: 'Привіт, Мимесис! Як справи?')() == \
        'Pryvit, Mimesis! Yak spravy?'
    assert romanize('kk')(lambda: 'Сәлем, Mimesis! Күнің көрсеткіші?')() == \
        'Sälem, Mimesis! Küniñ körsetkişi?'

# Generated at 2022-06-13 23:46:43.055042
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def _romanize(locale):
        return 'Добро пожаловать в Москву!'
    assert _romanize('ru') == 'Dobro pozhalovatʹ v Moskvu!'

# Generated at 2022-06-13 23:46:46.612917
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo():
        return 'Привет Мир'
    assert foo() == 'Privet Mir'


# Generated at 2022-06-13 23:46:49.776881
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привеыто мир')() == 'Priveyto mir'

# Generated at 2022-06-13 23:46:58.019285
# Unit test for function romanize
def test_romanize():
    import doctest
    # Ignore warnings in doctests
    doctest.testmod(mimesis.locales.ru, optionflags=doctest.IGNORE_EXCEPTION_DETAIL)


if __name__ == '__main__':
    test_romanize()

# Generated at 2022-06-13 23:47:10.872708
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person
    from mimesis.providers.text import Text

    address = Address(Language.RUSSIAN)
    person = Person(Language.RUSSIAN)
    text = Text(Language.RUSSIAN)

    assert address.address().islower()
    assert person.full_name().islower()
    assert pytest.is_str(address.address())
    assert pytest.is_str(person.full_name())
    assert pytest.is_str(person.surname(gender=None))

    assert pytest.is_str(text.words(quantity=1, with_punctuation=True))

# Generated at 2022-06-13 23:47:17.150146
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Съешь ещё этих мягких булок, да выпей чаю')() == 'Seś eščë etih mâgkih bulok, da vypej čaju'

# Generated at 2022-06-13 23:47:19.230149
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привет!') == 'Privet!'


# Generated at 2022-06-13 23:48:03.311628
# Unit test for function romanize
def test_romanize():
    romanize('ru')
    romanize('uk')
    romanize('kk')

# Generated at 2022-06-13 23:48:09.899794
# Unit test for function romanize
def test_romanize():
    # Strings for assert
    russian_test = 'Привет, программист!'
    ukrainian_test = 'Гей, програмісте!'
    kazakh_test = 'Сәлем, бағдарламашы!'
    # English languages
    en_US = 'Privet, programmist!'
    en_GB = 'Privet, programmist!'
    en_CA = 'Privet, programmist!'
    en_AU = 'Privet, programmist!'
    en_NZ = 'Privet, programmist!'
    # Other languages
    de_DE = 'Privet, programmist!'

# Generated at 2022-06-13 23:48:20.232254
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    ru = RussiaSpecProvider

    assert ru.code() == 'ru'

    assert ru.postal_index() == ru.postal_index(romanize='only')
    assert ru.passport_number() == ru.passport_number(romanize='only')
    assert ru.itn() == ru.itn(romanize='only')

    assert ru.postal_index(romanize=True) == ru.postal_index(romanize='only')
    assert ru.passport_number(romanize=True) == ru.passport_number(
        romanize='only'
    )
    assert ru.itn(romanize=True) == ru.itn(romanize='only')


# Generated at 2022-06-13 23:48:25.943194
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Данный декоратор преобразует кириллицу')() == 'Dannыi dekorator preobrazuet kirillitsu'
    assert romanize('ru')(lambda: 'Юрьев')() == 'Yuriev'


# Generated at 2022-06-13 23:48:34.266499
# Unit test for function romanize
def test_romanize():
    locales = ['ru', 'uk', 'kk', 'en']

# Generated at 2022-06-13 23:48:37.423355
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Дмитрий')() == 'Dmitriy'

# Generated at 2022-06-13 23:48:52.144500
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Languages
    from mimesis.providers.address import Address
    from mimesis.providers.person import Person
    from mimesis.providers.misc import Misc

    address = Address(Locales.UKRAINIAN)
    person = Person(Locales.UKRAINIAN)
    misc = Misc(Locales.UKRAINIAN)

    def decorated_method():
        return address.building_number()

    assert decorated_method() == '3'

    def decorated_method():
        return person.full_name()

    assert decorated_method() == 'Каріна Тетяна Казякова'

    def decorated_method():
        return misc.random_int()

    assert decorated_method() == '5'

# Generated at 2022-06-13 23:48:54.214452
# Unit test for function romanize
def test_romanize():
    assert ascii('Some строка') == 'Some stroka'

# Generated at 2022-06-13 23:49:02.319128
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Русский')() == 'Russkii'
    assert romanize(locale='uk')(lambda: 'Руський')() == 'Rouskii'
    assert romanize(locale='kk')(lambda: 'Қазақ')() == 'Qazaq'



# Generated at 2022-06-13 23:49:15.372891
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет мир!')() == 'Privet mir!'
    assert romanize('uk')(lambda: 'Привіт світ!')() == 'Pryvit svit!'
    assert romanize('kk')(lambda: 'Сәлем қазақстан!')() == 'Sälem qazaqstan!'
    assert romanize('uk')(lambda: 'Софія')() == 'Sofiya'
    assert romanize('uk')(lambda: 'Винниченко')() == 'Vynnychenko'
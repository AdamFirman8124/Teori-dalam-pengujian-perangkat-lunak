

# Generated at 2022-06-13 23:39:44.351337
# Unit test for function romanize
def test_romanize():
    def my_generator():
        uk_alphabet = data.ROMANIZATION_DICT['uk']
        my_alphabet = {**uk_alphabet, **data.COMMON_LETTERS}

        txt = ''.join(sorted(data.CYRILLIC_ALPHABET))
        txt = txt.replace('Ё', 'Е')
        res = ''.join([my_alphabet[i] for i in txt
                       if i in my_alphabet])
        return res

    assert my_generator() == 'ABCDEFGHIYJKLMNOPQRSTUVWXZ'

# Generated at 2022-06-13 23:39:51.244743
# Unit test for function romanize
def test_romanize():
    @romanized()
    def get_text(locale):
        return data.CYRILLIC_ALPHABET[locale]

    assert get_text("ru") == \
           data.ROMANIZATION_DICT["ru"].values()

    assert get_text("uk") == \
           data.ROMANIZATION_DICT["uk"].values()

    assert get_text("kk") == \
           data.ROMANIZATION_DICT["kk"].values()

# Generated at 2022-06-13 23:39:54.873187
# Unit test for function romanize
def test_romanize():
    """Test romanize."""

    @romanize('ru')
    def gender() -> str:
        return 'женский'

    assert gender() == "zhenskii"

# Generated at 2022-06-13 23:40:04.687582
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    rus = RussiaSpecProvider()

    txt_1 = rus.full_name(gender='male')
    txt_2 = rus.full_name(gender='female')
    assert romanized('ru')(rus.full_name)(gender='male') == txt_1
    assert romanized('ru')(rus.full_name)(gender='female') == txt_2
    assert romanized(locale='ru')(rus.full_name)(gender='male') == txt_1
    assert romanized(locale='ru')(rus.full_name)(gender='female') == txt_2

# Generated at 2022-06-13 23:40:10.576229
# Unit test for function romanize
def test_romanize():
    def foo():
        return 'функция возвращает русский текст'

    func = romanize()(foo)
    assert func() == 'функция возвращает русский текст'
    locales = ['ru', 'uk', 'kk']
    for locale in locales:
        romanized_func = romanize(locale)(foo)
        assert romanized_func() == 'тункция возвращает русский текст'

# Generated at 2022-06-13 23:40:23.731933
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize."""
    @romanize('ru')
    def rus():
        return 'Привет!'

    @romanize('uk')
    def ukr():
        return 'Привіт!'

    @romanize('kk')
    def kaz():
        return 'Сәлем!'

    @romanized('kk')
    def kazb():
        return 'Сәлем!'

    actual = ukr()
    expected = 'Pryvit!'
    assert actual == expected

    actual = rus()
    expected = 'Privet!'
    assert actual == expected

    actual = kaz()
    expected = 'Sälem!'
    assert actual == expected

    actual = kazb()

# Generated at 2022-06-13 23:40:33.477338
# Unit test for function romanize
def test_romanize():
    # English
    assert romanize()('Test') == 'Test'
    # Chinese (supported by mimesis)
    assert romanize('zh')('测试') == '测试'
    # Russian with romanized
    assert romanized('ru')('Тест') == 'Test'
    # Ukrainian with romanized
    assert romanized('uk')('Тест') == 'Test'
    # Kazakh with romanized
    assert romanized('kk')('Тест') == 'Test'
    # Korean (not supported by mimesis)
    assert romanized('ko')('테스트') == '테스트'
    # Macedonian (not supported by mimesis)
    assert r

# Generated at 2022-06-13 23:40:39.200096
# Unit test for function romanize
def test_romanize():
    # locale is 'ru' by default.
    assert romanize('')(lambda: 'Привет')() == 'Privet'

    assert romanize('uk')(lambda: 'Вітаю')() == 'Vitayu'
    assert romanize('uk')(lambda: 'Привет')() == 'Priviet'

    assert romanize('kk')(lambda: 'Сәлем')() == 'Salem'
    assert romanize('kk')(lambda: 'привет')() == 'priviet'

# Generated at 2022-06-13 23:40:51.533062
# Unit test for function romanize
def test_romanize():
    """Test romanization of the russian and ukrainian text."""
    from mimesis.builtins import RussiaSpecProvider
    rus = RussiaSpecProvider()

    @romanized('ru')
    def romanize_ru():
        return rus.full_name()

    text = romanize_ru()
    assert text == 'Иванов Иван Иванович'

    @romanized('uk')
    def romanize_uk():
        return rus.full_name(locale='uk')

    text = romanize_uk()
    assert text == 'Іванов Іван Іванович'

# Generated at 2022-06-13 23:41:03.487528
# Unit test for function romanize
def test_romanize():
    import pytest
    from mimesis.enums import Locale
    from mimesis.providers.datetime import Datetime

    dt = Datetime('ru')

    with pytest.raises(UnsupportedLocale):
        dt.day_of_week(locale='gibberish')

    assert dt.day_of_week(locale='ru') == 'пятница'

    with pytest.raises(UnsupportedLocale):
        dt.day_of_week(locale='gibberish', romanize=True)

    assert dt.day_of_week(locale='ru',
                          romanize=True) == 'pyatnica'


# Generated at 2022-06-13 23:41:19.903953
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.names import Names

    @romanize()
    def romanize_name(gen: Names):
        return gen.name(Language.RUSSIAN)

    assert romanize_name('Петр') == 'Петр'
    assert romanize_name('Петр Петрович') == 'Петр Петрович'
    assert romanize_name('Александр') == 'Александр'
    assert romanize_name('Иванов Иван') == 'Иванов Иван'
    assert romanize_

# Generated at 2022-06-13 23:41:20.731518
# Unit test for function romanize
def test_romanize():
    assert romanize  # Use your favorite assert here.

# Generated at 2022-06-13 23:41:25.730943
# Unit test for function romanize
def test_romanize():
    """Test for function romanize"""
    @romanize(locale='ru')
    def display_romanize(value):
        """Get romanize value"""
        return value

    assert display_romanize('Привет') == 'privet'

# Generated at 2022-06-13 23:41:36.214933
# Unit test for function romanize
def test_romanize():
    """Unit test for function romanize"""
    r = romanize('ru')
    assert r(lambda: 'Украина') == 'Ukraina'
    r = romanize('uk')
    assert r(lambda: 'Україна') == 'Ukrajina'
    r = romanize('kk')
    assert r(lambda: 'Қазақстан') == 'Qazaqstan'



# Generated at 2022-06-13 23:41:37.582721
# Unit test for function romanize
def test_romanize():
    assert romanize()



# Generated at 2022-06-13 23:41:40.060995
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'привет')() == 'privet'

# Generated at 2022-06-13 23:41:43.758517
# Unit test for function romanize
def test_romanize():
    romanize = romanized(locale='ru')

    assert romanize('Нурмет') == 'NURMET'

# Generated at 2022-06-13 23:41:49.810699
# Unit test for function romanize
def test_romanize():
    def func(string):
        return string

    assert func('foo') == romanize('kk')(func)('foo')
    assert func('как тот черт') == romanize('kk')(func)('как тот черт')
    assert func('foo') == romanize('ru')(func)('foo')
    assert func('как тот черт') == romanize('ru')(func)('как тот черт')
    assert func('foo') == romanize('uk')(func)('foo')

# Generated at 2022-06-13 23:41:54.593307
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'ыа')() == 'ya'
    assert romanize()(lambda: 'ЫА')() == 'YA'
    assert romanize()(lambda: 'ЫАЫА')() == 'YAYA'

# Generated at 2022-06-13 23:42:02.658813
# Unit test for function romanize
def test_romanize():
    "Assert decorator `romanize` is working as expected."
    assert romanized('ru')(lambda: 'Бородино')() == 'Borodino'
    assert romanized('kk')(lambda: 'Бородино')() == 'Borodino'
    assert romanized('uk')(lambda: 'Габарит')() == 'Gabarit'
    assert romanized('de')(lambda: 'Бородино')() == 'Бородино'

# Generated at 2022-06-13 23:42:12.137190
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def get_romanized_name(seed: int = None) -> str:
        return "Александра"

    assert get_romanized_name() == "Aleksandra"

# Generated at 2022-06-13 23:42:20.783601
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'абвгдежзийклмнопрстуфхцчшщъыьэюя')() == 'abvgdeezijklmnoprstufhcchshschyieyuya'
    assert romanize(locale='uk')(lambda: 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')() == 'abvhgdeezhzijjijklimnoprstufhcchschyieyuya'

# Generated at 2022-06-13 23:42:31.306861
# Unit test for function romanize
def test_romanize():
    """Test romanize"""
    @romanize('ru')
    def get_romanized(pattern: str = '') -> str:
        """Get romanized text."""
        return pattern

    txt = get_romanized(pattern="Тест")
    assert txt == "Test"

    txt = get_romanized(pattern="Юникод")
    assert txt == "Yunikod"

    txt = get_romanized(pattern="Символ")
    assert txt == "Simvol"

    txt = get_romanized(pattern="Крючок")
    assert txt == "Kryuchok"

    txt = get_romanized(pattern="латиница")

# Generated at 2022-06-13 23:42:32.993703
# Unit test for function romanize
def test_romanize():
    assert romanized()("привіт") == 'pryvit'

# Generated at 2022-06-13 23:42:36.200833
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Что делает то, что можно сделать?')() == \
        'Chto delaet to, chto mozhno sdelat\'?'

# Generated at 2022-06-13 23:42:39.498649
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'Привет')() == 'Privet'
    assert romanize('uk')(lambda x: 'Привіт')() == 'Pryvit'
    assert romanize('kk')(lambda x: 'Сәлем')() == 'Sälem'

# Generated at 2022-06-13 23:42:41.983072
# Unit test for function romanize
def test_romanize():
    """Tests for function romanize."""
    pass



# Generated at 2022-06-13 23:42:55.969408
# Unit test for function romanize
def test_romanize():
    # Check romanization of simple sentences
    def romanize_word(word, locale):
        def romanized_func(): return word
        return romanize(locale)(romanized_func)()

    assert romanize_word('Мохамад', 'ru') == 'Mohammad'
    assert romanize_word('Алдар', 'ru') == 'Aldar'
    assert romanize_word('Курман', 'ru') == 'Kurman'

    assert romanize_word('Гажали', 'kk') == 'Ghazhali'
    assert romanize_word('Кадир', 'kk') == 'Kadir'
    assert romanize_word('Марат', 'kk')

# Generated at 2022-06-13 23:42:59.254817
# Unit test for function romanize
def test_romanize():
    example = ['Пример', 'Приклад']
    result = romanize(locale='ru')(lambda: example[0])
    assert result == 'Primer'

    result = romanize(locale='uk')(lambda: example[1])
    assert result == 'Pryklad'



# Generated at 2022-06-13 23:43:01.769392
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'Романизация')() == 'Romanizatsiya'

# Generated at 2022-06-13 23:43:21.399533
# Unit test for function romanize
def test_romanize():
    # Simple romanization
    assert romanize()(lambda: 'Привет')() == 'Privet'
    assert romanize()(lambda: 'Пётр')() == 'Pyotr'
    assert romanize()(lambda: 'Пётр')() == 'Pyotr'
    assert romanize()(lambda: 'Прощай')() == 'Proshchai'

    # Extended alphabet
    assert romanize('ru')() == 'Privet'

    # Incorrect locale
    romanize_incorrect = romanize('incorrect')
    assert romanize_incorrect



# Generated at 2022-06-13 23:43:29.056846
# Unit test for function romanize
def test_romanize():
    # Fail
    try:
        romanize('ab')
    except Exception:
        pass

    @romanize(locale='ru')
    def foo():
        return 'Привет, мир!'

    assert foo() == 'Privet, mir!'

    @romanize(locale='uk')
    def foo():
        return 'Привіт, світ!'

    assert foo() == 'Pryvit, svit!'

# Generated at 2022-06-13 23:43:32.257147
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    t = Text('ru')
    assert t.title(romanize=True) == t.title(romanize=True)

# Generated at 2022-06-13 23:43:40.333350
# Unit test for function romanize
def test_romanize():
    from mimesis.generators import Generic
    from mimesis.enums import Gender
    from mimesis.builtins import Person

    class Wrapper(Generic):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._person = Person(self.locale)

        @romanize('ru')
        def name(self, gender: Gender = None):
            return self._person.name(gender=gender)

    gen = Wrapper()
    result = gen.name(gender=Gender.MALE)
    assert isinstance(result, str)

# Generated at 2022-06-13 23:43:48.477420
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет, Мир!')() == 'Privet, Mir!'
    assert romanize('uk')(lambda: 'Привіт, Світ!')() == 'Pryvit, Svit!'
    assert romanize('kk')(lambda: 'Сәлем, Әлем!')() == 'Sälem, Älem!'

# Generated at 2022-06-13 23:43:50.222141
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    assert isinstance(romanize()(lambda: '')(), str)

# Generated at 2022-06-13 23:44:01.790678
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender

    from mimesis.providers.personal import Personal

    personal = Personal('ru')

    person_arthur = personal.get_full_name(gender=Gender.MALE)
    assert person_arthur == romanized("ru")(person_arthur)
    person_dave = personal.get_full_name(gender=Gender.MALE)
    assert person_dave == romanized("ru")(person_dave)
    person_hong = personal.get_full_name(gender=Gender.MALE)
    assert person_hong == romanized("ru")(person_hong)

    person_yun = personal.get_full_name(gender=Gender.FEMALE)

# Generated at 2022-06-13 23:44:06.411861
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: "Миру мир")() == 'Miru mir'
    assert romanize('uk')(lambda: "Миру мир")() == 'Miru mir'
    assert romanize('kk')(lambda: "Миру мир")() == 'Miru mir'
    assert romanize('en')(lambda: "Миру мир")() == 'Миру мир'

# Generated at 2022-06-13 23:44:17.333181
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda self: 'Привет, Мир!') == 'Privet, Mir!'
    assert romanize(locale='ru')(lambda self: 'Привет, Мир!') == 'Privet, Mir!'
    assert romanize(locale='uk')(lambda self: 'Образа минулого') == 'Obrazy minuloho'
    assert romanize(locale='kk')(lambda self: 'Кирилл алфавитіне қарсыласы') == 'Kirill alfavitine karsylasy'

# Generated at 2022-06-13 23:44:20.582407
# Unit test for function romanize
def test_romanize():
    @romanize
    def func():
        return 'Мимесис'
    assert func() == 'Mimesis'

# Generated at 2022-06-13 23:44:58.521359
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'йцукен')() == 'jcvken'

# Generated at 2022-06-13 23:45:02.257699
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def r():
        return 'привет'

    assert r() == 'privet'

# Generated at 2022-06-13 23:45:15.101574
# Unit test for function romanize
def test_romanize():
    from .datetime import Datetime

    dt = Datetime('ru')
    date = dt.date(datetime_format='full')
    assert ' ' not in date

    dt = Datetime('uk')
    date = dt.date(datetime_format='full')
    assert ' ' not in date

    dt = Datetime('kk')
    date = dt.date(datetime_format='full')
    assert ' ' not in date

    dt = Datetime('en')
    date = dt.date(datetime_format='full')
    assert ' ' not in date

# Generated at 2022-06-13 23:45:26.843526
# Unit test for function romanize
def test_romanize():
    assert romanized()(lambda: 'Привет, Мир!')() == 'Privet, Mir!'
    assert romanized(locale='uk')(lambda: 'Привіт, Світ!')() == 'Pryvit, Svit!'
    assert romanized(locale='kk')(lambda: 'Сәлем, Дүние!')() == 'Sälem, Dünie!'
    assert romanized(locale='ru')(lambda: 'Здравствуйте, Мир!')() == 'Zdravstvyite, Mir!'

# Generated at 2022-06-13 23:45:31.193961
# Unit test for function romanize
def test_romanize():
    exp = 'Privet, rebiaty i devochki'
    i = 'Привет, ребята и девочки'
    result = romanize(locale='ru')(i)
    print(result)
    assert result == exp

# Generated at 2022-06-13 23:45:39.358118
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Language
    from mimesis.providers.address import Address
    from mimesis.providers.internet import Internet

    i = Internet()
    a = Address(Language.RU)

    assert i.domain_name() == 'popcorn.ru'
    assert a.street_name() == 'Красный проспект'
    assert a.street_address() == 'Красный проспект, 5'

    assert i.domain_name(romanized=True) == 'popcorn.ru'
    assert a.street_name(romanized=True) == 'Krasnyy prospekt'

# Generated at 2022-06-13 23:45:42.002846
# Unit test for function romanize
def test_romanize():
    assert isinstance(romanize, object)
    assert hasattr(romanize, '__call__')
    assert callable(romanized)
    assert romanize('ru')

# Generated at 2022-06-13 23:45:42.867052
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:45:55.610182
# Unit test for function romanize
def test_romanize():
    """Test the decorator romanize."""
    assert romanize('ru')(lambda: 'Привет, мир')() == 'Privet, mir'

    try:
        assert romanize('bb')(lambda: 'Привет, мир')() == 'Privet, mir'
    except:
        return True
    assert False

# Generated at 2022-06-13 23:46:09.982329
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.providers import Names

    en = Names('en')
    ru = Names('ru')
    uk = Names('uk')
    kk = Names('kk')

    romanized_en = romanize('en')(en.name)
    assert romanized_en('John', Gender.MALE) == 'John'
    assert romanized_en('Анжелика', Gender.FEMALE) == 'Anzhelika'

    romanized_ru = romanize('ru')(ru.name)
    assert romanized_ru('Джон', Gender.MALE) == 'Dzhon'
    assert romanized_ru('Анжелика', Gender.FEMALE)

# Generated at 2022-06-13 23:47:09.545948
# Unit test for function romanize
def test_romanize():
    """Test romanization."""
    rus_string = "Привет, как дела?"

    @romanize(locale='ru')
    def rus_text():
    # type: () -> str
        """Romanize rus text."""
        return rus_string

    assert rus_text() == "Privet, kak dela?"



# Generated at 2022-06-13 23:47:13.662138
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.geography import Geography

    assert Geography('ru').postal_code() == '191241'
    assert Geography('ua').postal_code() == '41045'
    assert Geography('kz').postal_code() == '100817'
    assert Geography('ru').bank_account_number() == '51950'
    assert Geography('ua').bank_account_number() == '4769'
    assert Geography('kz').bank_account_number() == '3753'

# Generated at 2022-06-13 23:47:14.664266
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')

# Generated at 2022-06-13 23:47:16.415865
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Привет мир!')() == 'Privet mir!'

# Generated at 2022-06-13 23:47:22.196039
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def romanize_text():
        return 'Съешь ещё этих мягких французских булок, да выпей же чаю'

    assert romanize_text() == (
        'Sesh eshche etikh myagkikh frantsuzskikh bulok, da vypei zhe chayu'
    ), 'Romanize function test failed'

# Generated at 2022-06-13 23:47:28.732318
# Unit test for function romanize
def test_romanize():
    import random
    import string

    # Creating a random text.
    text = ''.join(random.choice(string.ascii_letters) for i in range(20))

    # Creating a function and romanize()-decorator
    def romanize_test(text):
        return text.casefold()

    @romanize()
    def romanize_test_deco(text):
        return text.casefold()

    # Check if romanize()-decorator works
    assert romanize_test_deco(text) != romanize_test(text)

# Generated at 2022-06-13 23:47:35.696333
# Unit test for function romanize
def test_romanize():
    # TODO: Fix test.
    assert romanize('ru')(lambda: 'Съешь ещё этих мягких французских булок, да выпей чаю.')() == 'Sesh eshchyo etikh mjagkikh francuzskikh bulok, da vypey chaju.'

# Generated at 2022-06-13 23:47:39.182882
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins
    assert mimesis.builtins.Address.address(locale='uk', romanize=True)
    assert mimesis.builtins.Text.text(locale='ru', romanize=True)
    assert mimesis.builtins.Address.city(locale='ru', romanize=True)

# Generated at 2022-06-13 23:47:40.850231
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def roman():
        return 'тест'

    expected = 'test'
    actual = roman()
    assert expected == actual

# Generated at 2022-06-13 23:47:51.037547
# Unit test for function romanize
def test_romanize():
    import mimesis.builtins

    @romanize()
    def to_latin(text):
        return text

    result = to_latin('Привет')
    assert result == 'Priviet'

    @romanize(locale='kk')
    def lang(text):
        return text

    result = lang('Привет')
    assert result == 'Privet'

    @romanize(locale='uk')
    def lang(text):
        return text

    result = lang('Привет')
    assert result == 'Pryvit'

    @romanize()
    def lang(text):
        return text

    result = lang('Привет')
    assert result == 'Priviet'


# Generated at 2022-06-13 23:49:29.257148
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='uk')(lambda: 'Тест')() == 'Test'
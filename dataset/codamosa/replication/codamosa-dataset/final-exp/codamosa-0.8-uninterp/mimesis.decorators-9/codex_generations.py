

# Generated at 2022-06-13 23:39:40.414818
# Unit test for function romanize
def test_romanize():
    def foo(text: str) -> str:
        return text

    assert romanize()(foo)('Данный текст необходимо романизировать.') == 'Danniy tekst neobkhodimo romanizirovat.'

# Generated at 2022-06-13 23:39:44.594923
# Unit test for function romanize
def test_romanize():
    result = romanize()(lambda: 'Це просто перевірка 123')()
    assert result == 'Ce prosto pevеrkа 123'



# Generated at 2022-06-13 23:39:47.456237
# Unit test for function romanize
def test_romanize():
    """TestRomanize."""
    assert romanize()(lambda: 'Привет, как дела?') == 'Privet, kak dela?'

# Generated at 2022-06-13 23:39:50.774233
# Unit test for function romanize
def test_romanize():

    @romanize(locale='ru')
    def test(foo: str) -> str:
        return foo

    txt = test('Русский Язык')
    assert txt == 'Russkiy Yazyk'



# Generated at 2022-06-13 23:39:52.371376
# Unit test for function romanize
def test_romanize():
    assert romanize()('test_romanize') == 'test_romanize'

# Generated at 2022-06-13 23:40:01.527934
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian_name_romanize(name: str) -> str:
        return name

    assert russian_name_romanize('Афанасий') == 'Afanasiy'

    @romanize(locale='uk')
    def ukrainian_name_romanize(name: str) -> str:
        return name

    assert ukrainian_name_romanize('Опанас') == 'Opanas'

    @romanize(locale='kk')
    def kazakh_name_romanize(name: str) -> str:
        return name

    assert kazakh_name_romanize('Алия') == 'Aliya'

# Generated at 2022-06-13 23:40:03.450098
# Unit test for function romanize
def test_romanize():
    assert romanize is romanize
    assert romanize is romanized

# Generated at 2022-06-13 23:40:14.198239
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    from mimesis.enums import Locale

    rus = 'Лето подходит к концу.'
    ukr = 'Літо зближається до свого завершення.'
    kaz = 'Күнделікті аяқтауда...'

    assert rus == romanize('ru')(rus)
    assert ukr == romanize('uk')(ukr)
    assert kaz == romanize('kk')(kaz)

# Generated at 2022-06-13 23:40:26.403693
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Сто двадцать три')() == 'Sto dvadcat tri'
    assert romanize('uk')(lambda: 'Сто двадцать три')() == 'Sto dvadcat tri'
    assert romanize('kk')(lambda: 'Сто двадцать три')() == 'Sto dvadcat tri'
    assert romanize('kk')(lambda: 'Кітаптық көлемі: 100')() == 'Kitaptik kölemini: 100'

# Generated at 2022-06-13 23:40:30.808179
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def _(x):
        return {
            's': u'сх'.encode('utf-8').decode(),
        }[x]
    assert _('s') == 'skh'



# Generated at 2022-06-13 23:40:42.668295
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def ru_func():
        return 'Съешь ещё этих мягких французских булок!'

    assert ru_func() == 'Syesh eshyo etikh myagkikh frantsuzskikh bulok!'



# Generated at 2022-06-13 23:40:45.645334
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def cyrillic_test():
        return 'Привет мир!'

    assert cyrillic_test() == 'Privet mir!'

# Generated at 2022-06-13 23:40:53.565683
# Unit test for function romanize
def test_romanize():
    """Test for function romanize"""
    from mimesis.enums import Locale
    from mimesis.providers.generic import Generic
    from mimesis.providers.identifier import Identifier

    generic = Generic(Locale.RUSSIAN)
    identifier = Identifier(Locale.RUSSIAN)

    test_string = generic.text(max_length=10)
    test_regex = r'[a-zA-Z0-9{}]'.format(punctuation)

    assert generic._space(15) == ' ' * 15
    assert test_string
    assert len(test_string) <= 10
    assert identifier._romanize(test_string)

# Generated at 2022-06-13 23:41:04.930575
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: ('Сравнительное таблица')) == 'Sravnitel'\
                                                                 'noe tablica'

    assert romanized('uk')(lambda: ('Наближена переводиться таблиця')) ==\
        'Nabližena peredovydiatʹsia tablitsia'


# Generated at 2022-06-13 23:41:06.308498
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Тест')() == 'Test'

# Generated at 2022-06-13 23:41:08.812046
# Unit test for function romanize
def test_romanize():

    @romanize('ru')
    def one():
        return 'дом'

    assert one() == 'dom'

# Generated at 2022-06-13 23:41:11.113456
# Unit test for function romanize
def test_romanize():
    assert romanize()('Александр') == 'Aleksandr'



# Generated at 2022-06-13 23:41:20.093668
# Unit test for function romanize
def test_romanize():
    anchor = 'АБВГҐДЕЁЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    assert len(anchor) == 33

    alphabet = {s: s for s in ascii_letters + digits + punctuation}
    alphabet.update({
        **data.ROMANIZATION_DICT['ru'],
        **data.COMMON_LETTERS,
    })

    for letter in anchor:
        assert alphabet[letter]

# Generated at 2022-06-13 23:41:31.732548
# Unit test for function romanize
def test_romanize():
    assert romanize('en')(lambda: 'Привет, как дела?')() == \
        romanize()(lambda: 'Привет, как дела?')() == \
        romanize('ru')(lambda: 'Привет, как дела?')() == \
        romanize('uk')(lambda: 'Привет, как дела?')() == \
        romanize('kk')(lambda: 'Привет, как дела?')() == \
        'Privet, kak dela?'


# Generated at 2022-06-13 23:41:34.334231
# Unit test for function romanize
def test_romanize():
    def test_function(a):
        return a

    wrapped = romanize(locale='uk')(test_function)
    result = wrapped('привіт мир')
    assert result == 'pryvit myr'

# Generated at 2022-06-13 23:41:45.796264
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(str)('Привет') == 'privet'

# Generated at 2022-06-13 23:41:58.333502
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    from mimesis.builtins import RussiaSpecProvider

    provider = RussiaSpecProvider

    @provider.romanize()
    def test_romanize_uk():
        """Test romanize ukrainian locale."""
        return 'Шановний Незнайомець!'

    assert test_romanize_uk() == 'Shanovnij Nеznajomеc’!'

    @provider.romanize()
    def test_romanize_ru():
        """Test romanize russian locale."""
        return 'Добрый День!'

    assert test_romanize_ru() == 'Dobryj Dеn’!'


# Generated at 2022-06-13 23:41:59.355519
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')

# Generated at 2022-06-13 23:42:03.481262
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Давай писать функциональный стиль')() == 'Davaj pisat functionalnij stil'

# Generated at 2022-06-13 23:42:07.315600
# Unit test for function romanize
def test_romanize():
    from mimesis.providers.datetime import Datetime

    dt = Datetime(locale='ru')
    assert dt.month_name() == 'января'
    assert dt.month_romanized() == 'yanvarya'

# Generated at 2022-06-13 23:42:10.058841
# Unit test for function romanize
def test_romanize():
    """Unit test for ``romanize()`` method."""
    assert romanize()
    assert romanized



# Generated at 2022-06-13 23:42:15.230561
# Unit test for function romanize
def test_romanize():

    @romanize(locale='ru')
    def x():
        return 'Как приятно познакомиться'

    assert x() == 'Kak priyatno poznakomit\'sya'

# Generated at 2022-06-13 23:42:20.655890
# Unit test for function romanize
def test_romanize():
    romanize_function = romanize()

    @romanize_function
    def get_random_text():
        return "Ступай, не ступай, ступай!"

    assert get_random_text() == 'Stupay, ne stupay, stupay!'

# Generated at 2022-06-13 23:42:30.745849
# Unit test for function romanize
def test_romanize():
    assert romanize()('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
                      'абвгдеёжзийклмнопрстуфхцчшщъыьэюя') == \
           'ABVGDEYOZHZIYKLMNOPRSTUFXCCHWYIZYEZUIYa' \
           'bvgdeyozhziyklmnoprstufxcchwyizyezuiya'

# Generated at 2022-06-13 23:42:40.116307
# Unit test for function romanize
def test_romanize():
    import re
    import random
    from mimesis.builtins.numbers import Number
    
    number = Number()
    locales = number.locales
    choice = random.choice(locales)

# Generated at 2022-06-13 23:43:13.473696
# Unit test for function romanize
def test_romanize():

    def romanized_uk_func(*args, **kwargs):
        return u'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

    romanized_uk = romanize('uk')(romanized_uk_func)


# Generated at 2022-06-13 23:43:20.296713
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def get_ru():
        return "Привет"

    assert get_ru() == "Privet"

    @romanize('uk')
    def get_uk():
        return "Привіт"

    assert get_uk() == "Pryvit"

    @romanize('kk')
    def get_kk():
        return "Сәлем"

    assert get_kk() == "Sälem"

# Generated at 2022-06-13 23:43:22.996768
# Unit test for function romanize
def test_romanize():
    assert romanize()
    assert romanize(locale='ru')


# Generated at 2022-06-13 23:43:34.054138
# Unit test for function romanize
def test_romanize():
    """Test Romanize function."""
    with open("test_file.txt", "r") as f:
        text = f.read()
        f.close()

    ru = text.splitlines()[0]
    uk = text.splitlines()[1]
    kk = text.splitlines()[2]

    @romanize('ru')
    def romanize_ru():
        return ru

    @romanize('uk')
    def romanize_uk():
        return uk

    @romanize('kk')
    def romanize_kk():
        return kk

    assert romanize_ru() == 'привет'
    assert romanize_uk() == 'привіт'
    assert romanize_kk() == 'сәлем'

# Generated at 2022-06-13 23:43:42.531046
# Unit test for function romanize
def test_romanize():
    from mimesis import Person

    assert romanize('ru')(Person('ru').full_name) == 'Иванов Сергей Петрович'
    assert romanize('uk')(Person('uk').full_name) == 'Іванов Сергій Петрович'
    assert romanize('kk')(Person('kk').full_name) == 'Әйтпесов Сергей Петрович'
    assert romanize('en')(Person('en').full_name) == \
        'Baldwin-Holmes Evan Audley-Hall'

# Generated at 2022-06-13 23:43:47.124956
# Unit test for function romanize
def test_romanize():
    assert romanize()(str)(locale="ru") == 'Кириллица'
    assert romanize()('Кириллица') == 'Kyrillitsa'

# Generated at 2022-06-13 23:43:53.348418
# Unit test for function romanize

# Generated at 2022-06-13 23:43:56.930891
# Unit test for function romanize
def test_romanize():
    # Tests for the function romanize
    result = romanize(locale='ru')(lambda: 'Привет, Мир!')
    assert result == 'Privet, Mir!'

# Generated at 2022-06-13 23:44:02.749873
# Unit test for function romanize
def test_romanize():
    # To generate a random romanized name
    @romanize(locale='ru')
    def roman_name(self):
        return self['person'].full_name()

    # To generate a random romanized sentence
    @romanize()
    def roman_sentence(self):
        return self['text'].sentence()

    assert roman_name(locale='ru')
    assert roman_sentence()

# Generated at 2022-06-13 23:44:05.231906
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    assert romanize(locale='ru')
    assert romanize(locale='uk')
    assert romanize(locale='kk')

# Generated at 2022-06-13 23:45:08.514680
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: 'привет')() == 'privet'
    assert romanize('uk')(lambda x: 'привіт')() == 'pryvit'
    assert romanize('kk')(lambda x: 'сәлем')() == 'salem'
    assert romanize('ru')(lambda x: 'привет, мир!')() == 'privet, mir!'
    assert romanize('uk')(lambda x: 'привіт, світ!')() == 'pryvit, svit!'

# Generated at 2022-06-13 23:45:11.901981
# Unit test for function romanize
def test_romanize():
    @romanize()
    def some_func(r):
        return 'Привет, мир!'

    assert some_func('ru') == 'Privet, mir!'

# Generated at 2022-06-13 23:45:15.170346
# Unit test for function romanize
def test_romanize():
    from mimesis import Address, Person

    person = Person('en')
    address = Address('ru')
    assert person.address.full_address() == address.full_address()

# Generated at 2022-06-13 23:45:15.772269
# Unit test for function romanize
def test_romanize():
    assert romanize()

# Generated at 2022-06-13 23:45:16.675633
# Unit test for function romanize
def test_romanize():
    assert romanize()  # noqa: WPS432

# Generated at 2022-06-13 23:45:32.175735
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'Тут тоже самое, но это не важно.') == 'Tut tozhe same, no eto ne vazhno.'
    assert romanize()(lambda: 'Хер с этим!') == 'Kher s etym!'
    assert romanize()(lambda: 'Не хочу в мою сторону.') == 'Ne khochu v moyu storonu.'
    assert romanize('kk')(lambda: 'Сабақтар') == 'Sabaktar'

# Generated at 2022-06-13 23:45:36.521959
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda x: 'Абвгд')() == 'Abvgdd'
    assert romanize('uk')(lambda x: 'Абвгд')() == 'Abvhdd'
    assert romanize('kk')(lambda x: 'Абвгд')() == 'Abwgwd'



# Generated at 2022-06-13 23:45:38.456906
# Unit test for function romanize
def test_romanize():
    assert romanized(locale='ru_RU')(lambda: 'Дарова, сука') == 'Darova, suka'

# Generated at 2022-06-13 23:45:41.554234
# Unit test for function romanize
def test_romanize():
    def foo():
        return 'Тест пройден'

    r = romanize('ru')(foo)
    assert r() == 'Test proidën'

# Generated at 2022-06-13 23:45:57.937448
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.providers.person import Person
    assert Person(Locale.UK)
    assert Person(Locale.UK).username()
    assert Person(Locale.UK).name()
    assert Person(Locale.UK).full_name()
    assert Person(Locale.UK).last_name()
    assert Person(Locale.UK).date_of_birth()
    assert Person(Locale.UK).birthday()
    assert Person(Locale.UK).age()
    assert Person(Locale.UK).phone_number()
    assert Person(Locale.UK).email()

# Generated at 2022-06-13 23:47:38.473355
# Unit test for function romanize
def test_romanize():
    import string
    import random
    import pytest
    generator = data.Data('en')
    test_word = generator.word(length=random.choice(range(1, 4)))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    possible_test_word = test_word + ''.join(
        [random.choice(alphabet) for i in range(4)])

    @romanize()
    def foo(word):
        return word

    assert foo(test_word) == test_word
    assert foo(possible_test_word) == test_word

    test_text = generator.text(quantity=1, quantity_range=(1, 4),
                               length=random.choice(range(1, 5)))

# Generated at 2022-06-13 23:47:45.506299
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def russian_string(seed: int = None) -> str:
        return 'Если б мне платили каждый раз, когда я думаю о тебе.'

    russian_string(seed=1)
    russian_string(seed=100)
    assert callable(romanize)

# Generated at 2022-06-13 23:47:50.280297
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def test(text):
        return text


    assert test('ты в порядке') == 'ty v poryadke'
    assert test('Ты в порядке') == 'Ty v poryadke'

# Generated at 2022-06-13 23:47:52.337847
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.builtins.user import User

    @romanize(locale=Locale.RU)
    def f():
        return User('ru').address.street_name()

    assert f() != ''

# Generated at 2022-06-13 23:47:56.047932
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: "мимими")() == 'mimimi'

# Generated at 2022-06-13 23:48:00.013034
# Unit test for function romanize
def test_romanize():
    @romanized(locale='ru')
    def get_random_name():
        return 'Привет мир!'

    assert get_random_name() == 'Privet mir!'



# Generated at 2022-06-13 23:48:04.420604
# Unit test for function romanize
def test_romanize():
    romanize('ru')

# Generated at 2022-06-13 23:48:10.720546
# Unit test for function romanize
def test_romanize():
    """Test romanize decorator."""
    assert data.Ocean(locale='ru').name() == 'Атлантический океан'
    assert data.Ocean(locale='en').name() == 'Atlantic Ocean'

# Generated at 2022-06-13 23:48:15.258153
# Unit test for function romanize
def test_romanize():

    @romanize()
    def get_word(length: int = 0) -> str:
        return 'Привет'

    assert get_word() == 'Privet'

    @romanize(locale='kk')
    def get_word(length: int = 0) -> str:
        return 'Привет'

    assert get_word() == 'Pryvet'

# Generated at 2022-06-13 23:48:18.959629
# Unit test for function romanize
def test_romanize():
    assert romanized('locale')(lambda x: 'Привіт Світ')() == 'Pryvit Svit'
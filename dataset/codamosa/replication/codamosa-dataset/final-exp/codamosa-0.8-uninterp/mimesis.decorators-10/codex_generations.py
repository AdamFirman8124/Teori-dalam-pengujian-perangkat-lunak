

# Generated at 2022-06-13 23:39:47.847920
# Unit test for function romanize
def test_romanize():
    """Test for romanize function.
    """
    # Test for romanize decorator.
    @romanize(locale='ru')
    def _romanize_test(test_str):
        """Romanize test.
        """
        # Cyrillic string can contain ascii
        # symbols, digits and punctuation.
        alphabet = {s: s for s in
                    ascii_letters + digits + punctuation}
        alphabet.update({
            **data.ROMANIZATION_DICT['ru'],
            **data.COMMON_LETTERS,
        })

        result = ''.join([alphabet[i] for i in test_str if i in alphabet])
        return result

    # Test for custom locale.
    assert _romanize_test('Tëst Тест') == 'Test Test'

# Generated at 2022-06-13 23:39:51.709426
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Яблоко')() == 'Yabloko'

# Generated at 2022-06-13 23:40:06.309925
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda : 'Как ваши дела?') == 'Kak vashi dela?'
    assert romanize(locale='ru')(
        lambda : 'Новая библиотека, которая быстро растёт.') == \
        'Novaya biblioteka, kotoraya bystro rastyot.'

# Generated at 2022-06-13 23:40:16.196133
# Unit test for function romanize
def test_romanize():
    assert romanize(locale='ru')(lambda: 'Возьмите холодильник и приготовьте суп')() == 'Vozmite kholodilnik i prigotovite sup'
    assert romanize(locale='uk')(lambda: 'Сьогодні вечір, як і в Києві, теплий і сонечком')() == 'Sogódńi vechír, iák i v Kyiévi, teplýi i sonechkom'

# Generated at 2022-06-13 23:40:22.117914
# Unit test for function romanize
def test_romanize():
    assert callable(romanize())
    assert callable(romanized())
    romanizer = romanize()
    romanizer_deco = romanizer(lambda: 'тест')
    assert romanizer_deco() == 'test'


# for backward compatibility

# Generated at 2022-06-13 23:40:24.665492
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import Address
    assert "Moskva" in Address().city(language='ru')

# Generated at 2022-06-13 23:40:27.523054
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda x: x)('Привет, Мир!') == 'Privet, Mir!'

# Generated at 2022-06-13 23:40:30.808729
# Unit test for function romanize
def test_romanize():
    @romanize()
    def test():
        return 'Тестовая строка'

    assert callable(test)
    assert test() == 'Testovaya stroka'

# Generated at 2022-06-13 23:40:33.171112
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет мир') == 'Privet mir'

# Generated at 2022-06-13 23:40:48.152106
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def roman_russian(c):
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    assert roman_russian(1) == 'abvgdeezzziklmnoprstufkhccchshshyieua'

    @romanize('uk')
    def roman_ukrainian(c):
        return 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'


# Generated at 2022-06-13 23:41:04.623196
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Привет Мир')() == 'Privet Mir'
    assert romanized('uk')(lambda: 'Привіт Світ')() == 'Pryvit Svit'
    assert romanized('kk')(lambda: 'Сәлем Дүние')() == 'Sәlem Dөnie'
    assert romanized('kk')(lambda: 'Ақ жолу, қасық қолданбай біздер.')() == \
        'Aq jolu, qasıq qoldanbay bızder.'

# Generated at 2022-06-13 23:41:09.565033
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Здравствуйте, меня зовут Андрей.')() ==\
        'Zdravstvuy, menya zovut Andrey.'

# Generated at 2022-06-13 23:41:20.439510
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def _ru():
        return 'Какой то текст на русском.'

    @romanize('kk')
    def _kk():
        return 'Кайталы текст пин казакша.'

    @romanize('uk')
    def _uk():
        return 'Якийсь текст мовою українською.'

    assert _ru() == 'Kakoj to tekst na russkom.'
    assert _kk() == 'Kaytaly tekst pin kazaksha.'

# Generated at 2022-06-13 23:41:22.925882
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Привет')() == 'Priviet'

# Generated at 2022-06-13 23:41:33.022948
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')() == \
        'ABVGDEEJZIJKLMNOPRSTUFHCX4XWQYWQEUQA'



# Generated at 2022-06-13 23:41:45.246636
# Unit test for function romanize
def test_romanize():
    r = mimesis.Person(locale='ru')
    assert 'Иван' in r.full_name()
    assert 'М' in r.username(romanize=False)

    r_ru = mimesis.Person(locale='ru')
    assert 'Ivan' in r_ru.full_name(romanize=True)
    assert 'M' in r_ru.username()

    uk = mimesis.Person(locale='uk')
    assert 'Кислиця' in uk.full_name()
    assert 'М' in uk.username(romanize=False)

    uk_ru = mimesis.Person(locale='uk')
    assert 'Kyslytsia' in uk_ru.full_name(romanize=True)


# Generated at 2022-06-13 23:41:53.004913
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'абв')().lower() == 'abv'
    assert romanize('uk')(lambda: 'україна')().lower() == 'ukrayina'
    assert romanize('kk')(lambda: 'Қазақстан')().lower() == 'qazaqstan'

# Generated at 2022-06-13 23:42:02.442819
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Ядро дерева')() == 'Yadro dereva'
    assert romanize('uk')(lambda: 'Ядро дерева')() == 'Yadro dereva'
    assert romanize('kk')(lambda: 'Ядро дерева')() == 'Yadro dereva'
    assert romanize('ru')(lambda: 'Компьютер')() == 'Kompyuter'
    assert romanize('uk')(lambda: 'Компьютер')() == 'Kompyuter'
    assert romanize('kk')(lambda: 'Компьютер')()

# Generated at 2022-06-13 23:42:03.693218
# Unit test for function romanize
def test_romanize():
    """Test the function `romanize`."""
    assert romanize()

# Generated at 2022-06-13 23:42:04.655386
# Unit test for function romanize
def test_romanize():
    assert romanized is romanize



# Generated at 2022-06-13 23:42:10.683450
# Unit test for function romanize
def test_romanize():
    pass



# Generated at 2022-06-13 23:42:20.281547
# Unit test for function romanize

# Generated at 2022-06-13 23:42:22.042499
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda x: x)('привет') == 'privet'

# Generated at 2022-06-13 23:42:32.570993
# Unit test for function romanize

# Generated at 2022-06-13 23:42:35.240730
# Unit test for function romanize
def test_romanize():
    assert romanized('yy')('Привет, Мир!') == 'Pryvit, Mir!'



# Generated at 2022-06-13 23:42:37.779869
# Unit test for function romanize
def test_romanize():
    text = 'здравствуй'
    assert romanized(locale='ru')(lambda: text)() == 'zdravstvuj'



# Generated at 2022-06-13 23:42:39.413836
# Unit test for function romanize
def test_romanize():
    result = romanize(locale='ru')(lambda: 'Привет')
    expected = 'Privet'
    assert result == expected



# Generated at 2022-06-13 23:42:53.963721
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins.text import Text
    import mimesis

    text = Text()
    text_ru = Text('ru')
    text_uk = Text('uk')

    data_ru = text_ru._data['ru']['transliteration']
    data_uk = text_uk._data['uk']['transliteration']

    assert text.romanize(locale='ru') in data_ru
    assert text.romanize(locale='uk') in data_uk

    # Cyrillic string can contain ascii
    # symbols, digits and punctuation.
    alphabet_ru = {s: s for s in mimesis.ASCII_LETTERS
                   + mimesis.DIGITS + mimesis.PUNCTUATION}

# Generated at 2022-06-13 23:43:01.009003
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender
    from mimesis.providers.address import Address

    rp = RussiaSpecProvider()
    # Test for romanize(locale)
    assert Address.postal_code(locale='ru') == '010000'
    assert Address.postal_code(locale='ru') == '010000'
    assert Address.postal_code(locale='ru') == '010000'

    assert RussiaSpecProvider.patronymic(locale='ru') == 'Вадимович'
    assert RussiaSpecProvider.patronymic(locale='ru') == 'Вадимович'
    assert RussiaSpecProvider.patronym

# Generated at 2022-06-13 23:43:15.027092
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Locale
    from mimesis.numbers import Integer
    from mimesis.providers.numbers import Numbers
    from mimesis.typing import DataDict

    def prepare_data(*args, **kwargs) -> DataDict:
        return {
            'max_value': kwargs['max_value'],
        }

    @romanize()
    def get_data(**kwargs):
        return prepare_data(**kwargs)

    kwargs = {
        'max_value': Integer(1, 5).generate(),
        'locale': Locale.RU,
    }
    nm = Numbers(**kwargs)
    id_ = nm.integer()

    assert isinstance(id_, int)

# Generated at 2022-06-13 23:43:30.374624
# Unit test for function romanize
def test_romanize():
    from mimesis.providers import Address
    a = Address()
    assert a._get_city(locale='ru') == 'Магнитогорск'
    assert a.city(locale='ru', romanized=True) == 'Magnitogorsk'

# Generated at 2022-06-13 23:43:32.630829
# Unit test for function romanize
def test_romanize():
    """Test function romanize."""
    assert romanized('ru')(lambda: 'hello')() == 'привет'

# Generated at 2022-06-13 23:43:38.177464
# Unit test for function romanize
def test_romanize():
    from string import ascii_letters, digits, punctuation
    
    alphabet = {s: s for s in
                ascii_letters + digits + punctuation}
    alphabet.update({
            **data.ROMANIZATION_DICT['ru'],
            **data.COMMON_LETTERS,
        })
    
    assert romanize()
    assert romanized()

# Generated at 2022-06-13 23:43:40.516510
# Unit test for function romanize
def test_romanize():
    def func(*args, **kwargs):
        return 'привет'
    assert romanize('ru')(func)(None) == 'privet'



# Generated at 2022-06-13 23:43:48.183962
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def test():
        return 'тест'

    assert test() == 'test'

    @romanize(locale='uk')
    def test():
        return 'тест'

    assert test() == 'test'

    @romanize(locale='kk')
    def test():
        return 'тест'

    assert test() == 'test'



# Generated at 2022-06-13 23:43:49.937341
# Unit test for function romanize
def test_romanize():
    """Test for romanize function."""
    assert romanize()
    assert romanized()

# Generated at 2022-06-13 23:43:52.708894
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')('Привет, мир') == 'Privet, mir'

# Generated at 2022-06-13 23:43:57.095003
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    romanized_str = romanized('ru')(lambda x: 'Привет, Привет!')
    assert romanized_str == 'Privet, Privet!'

# Generated at 2022-06-13 23:43:59.430181
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'Мультиварка').__name__ == 'romanize'

# Generated at 2022-06-13 23:44:02.372310
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider

    rp = RussiaSpecProvider('ru')

    assert rp.cyrillic_string() == romanized('ru')(rp.cyrillic_string())

# Generated at 2022-06-13 23:44:31.458184
# Unit test for function romanize
def test_romanize():
    from mimesis.enums import Gender
    from mimesis.providers.person import Person
    p = Person('ru')
    _name = p.full_name(gender=Gender.MALE)
    romanized_name = p.romanize(_name)
    assert _name != romanized_name
    assert romanized_name == 'Kumar Jauketti'

# Generated at 2022-06-13 23:44:35.038295
# Unit test for function romanize
def test_romanize():
    def romanize_function():
        return 'Здравствуйте'

    expected = 'Zdrаvstvuite'
    assert romanized('ru')(romanize_function)() == expected

# Generated at 2022-06-13 23:44:39.960168
# Unit test for function romanize
def test_romanize():
    assert romanize()(lambda: 'пиво')() == 'pivo'
    assert romanize()(lambda: 'ПИВО')() == 'PIVO'



# Generated at 2022-06-13 23:44:42.346093
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Тест')() == 'Test'

# Generated at 2022-06-13 23:44:58.451573
# Unit test for function romanize
def test_romanize():
    """Test for function romanize."""
    from mimesis.enums import Locales
    from mimesis.providers.internet import Internet
    from mimesis.providers.address import Address, AddressItem

    address_ru = Address(Locales.RU)
    address_uk = Address(Locales.UK)
    address_kk = Address(Locales.KZ)

    internet = Internet()
    assert internet.domain_zone_code() == 'ru'
    assert internet.domain_zone_code(locale='ru') == 'ru'

    assert address_ru.region() == 'Читинская'
    assert address_uk.region() == 'Івано-Франківська'

# Generated at 2022-06-13 23:45:03.361678
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')(lambda: 'АБВГДЕЖ')() == 'ABVGDEG'
    assert romanize('uk')(lambda: 'АБВГДЕЖ')() == 'ABVGDEG'
    assert romanize('kk')(lambda: 'АБВГДЕЖ')() == 'ABVGDEG'



# Generated at 2022-06-13 23:45:12.172301
# Unit test for function romanize
def test_romanize():
    @romanize('uk')
    def roman_uk():
        return 'Абонента не знайдено'

    @romanize('ru')
    def roman_ru():
        return 'а б а к м а г о ж о'

    @romanize('kk')
    def roman_kk():
        return 'барлық жазбалар алдында'

    assert roman_uk() == 'Abonentu ne znajdeno'
    assert roman_ru() == 'a b a k m a g o z h o'

    # Cyrillic text can contain ASCII characters

# Generated at 2022-06-13 23:45:16.957485
# Unit test for function romanize
def test_romanize():
    @romanize(locale="ru")
    def russian_text():
        return "Привет! Меня зовут Маша."

    assert russian_text() == "Privet! Menya zovut Masha."



# Generated at 2022-06-13 23:45:20.131064
# Unit test for function romanize
def test_romanize():
    assert romanize()('Лоськов Юрий Олегович') == 'Loskov Yuriy Olegovich'

# Generated at 2022-06-13 23:45:22.344485
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian():
        return 'Привет'

    assert russian() == 'Privet'

# Generated at 2022-06-13 23:46:19.158663
# Unit test for function romanize
def test_romanize():
    @romanize('ru')
    def foo():
        return 'Люблю котов. Кто тебя создал?'

    assert foo().isalpha()
    assert len(foo()) == 32

# Generated at 2022-06-13 23:46:20.901809
# Unit test for function romanize
def test_romanize():
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-13 23:46:23.319995
# Unit test for function romanize
def test_romanize():
    assert romanize('ru')
    assert romanized('ru')

# Generated at 2022-06-13 23:46:26.151807
# Unit test for function romanize
def test_romanize():
    assert romanize()('Господи помилуй.') == 'Gospodi pomiluy.'

# Generated at 2022-06-13 23:46:31.796863
# Unit test for function romanize
def test_romanize():
    t = u'Вероятность выигрыша для бандита {}'
    result = romanize('ru')(lambda: t)
    assert callable(result)
    assert result() == 'Veroyatnost'\
                       ' vyigrysha dlya bandita {}'

# Generated at 2022-06-13 23:46:40.703229
# Unit test for function romanize
def test_romanize():
    assert 'ЭТО БЫЛО БЫ ФИНАЛЬНОЕ РЕШЕНИЕ' == romanized(locale='kk')(
            lambda: 'Это было бы финальное решение',
        )

    assert 'это было бы финальное решение' == romanized(locale='uk')(
            lambda: 'Это было бы финальное решение',
        )


# Generated at 2022-06-13 23:46:52.877012
# Unit test for function romanize
def test_romanize():
    """Unit test for romanize.
    """

    @romanize(locale="ru")
    def foo(count):
        return count

    assert foo(count='китай') == 'kitay'

    @romanize(locale='kk')
    def foo2(count):
        return count

    assert foo2(count='еуразия') == 'eyraziya'

    @romanize(locale='uk')
    def foo3(count):
        return count

    assert foo3(count='украина') == 'ukrayina'

    @romanize(locale='uk')
    def foo4(count):
        return count

    assert foo4(count='гугль') == 'hug\'l'

# Generated at 2022-06-13 23:47:00.097302
# Unit test for function romanize
def test_romanize():
    """Function romanize."""

    # Test for wrong locale
    bad_locale = 'fsdjfj'
    func = romanize(locale=bad_locale)

    @func
    def get_text():
        return 'Привет, мир!'

    with pytest.raises(UnsupportedLocale):
        get_text()

    # Test for right locale
    func = romanize(locale='uk')

    @func
    def get_text():
        return 'Привет, мир!'

    assert get_text() == 'Pryvit, svit!'

# Generated at 2022-06-13 23:47:04.492220
# Unit test for function romanize
def test_romanize():
    dummy_func = romanize('ru')(lambda x: 'Привет')
    assert dummy_func('') == 'Privet'

# Generated at 2022-06-13 23:47:07.990777
# Unit test for function romanize
def test_romanize():
    text = 'Слово'

    @romanize('ru')
    def get_text():
        return text

    assert get_text() == 'Slovo'


# Generated at 2022-06-13 23:48:48.386643
# Unit test for function romanize
def test_romanize():

    class Test:
        def __init__(self):
            self.counter = 0

        @romanize('ru')
        def romanize_ru(self, text: str) -> str:
            self.counter += 1
            return text

        @romanize('uk')
        def romanize_uk(self, text: str) -> str:
            self.counter += 1
            return text

        @romanize('kk')
        def romanize_kk(self, text: str) -> str:
            self.counter += 1
            return text

    test = Test()
    text = 'Русский текст языка, що застосовується в Україні.'


# Generated at 2022-06-13 23:48:51.355620
# Unit test for function romanize
def test_romanize():
    """Test for romanize."""
    assert romanized()(lambda: 'привет')() == 'privet'



# Generated at 2022-06-13 23:48:53.226506
# Unit test for function romanize
def test_romanize():
    assert romanized()('Это простой тест.') == 'Eto prostoy test.'

# Generated at 2022-06-13 23:49:05.492839
# Unit test for function romanize
def test_romanize():
    assert romanize.romanize('ru')('привет') == 'privet'
    assert romanize.romanize('uk')('привіт') == 'privit'
    assert romanize.romanize('kk')('сәлем') == 'salem'

    assert romanized('ru')('привет') == 'privet'
    assert romanized('uk')('привіт') == 'privit'
    assert romanized('kk')('сәлем') == 'salem'

# Generated at 2022-06-13 23:49:10.394591
# Unit test for function romanize
def test_romanize():
    assert romanized('ru')(lambda: 'Балбалайхан')() == 'Balbalajhan'

# Generated at 2022-06-13 23:49:18.135024
# Unit test for function romanize
def test_romanize():
    """Test for decorator romanize().

    :return: None
    """
    txt = 'Строка, которая будет переведена в романизированную версию.'

    def fake_generator(locale: str, *args, **kwargs) -> str:
        if locale == 'ru':
            return txt
        elif locale == 'uk':
            return 'Стрічка, яка буде переведена в романізовану версію.'

# Generated at 2022-06-13 23:49:23.065319
# Unit test for function romanize
def test_romanize():
    from mimesis.builtins import RussiaSpecProvider
    assert RussiaSpecProvider.romanized() != RussiaSpecProvider().full_name()
    assert RussiaSpecProvider.romanized() in \
           RussiaSpecProvider.romanize(locale='ru')(
               RussiaSpecProvider().full_name())

# Generated at 2022-06-13 23:49:32.508598
# Unit test for function romanize
def test_romanize():
    @romanize(locale='ru')
    def russian_source():
        return 'привет'

    assert russian_source() == 'privet'

    @romanize(locale='kz')
    def kazakh_source():
        return 'сәлем'

    assert kazakh_source() == 'salem'

    @romanized(locale='uk')
    def ukrainian_source():
        return 'привіт'

    assert ukrainian_source() == 'pryvit'
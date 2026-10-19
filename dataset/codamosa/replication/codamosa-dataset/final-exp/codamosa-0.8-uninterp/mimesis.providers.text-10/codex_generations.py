

# Generated at 2022-06-14 00:52:26.091580
# Unit test for constructor of class Text
def test_Text():
    """Unit test for constructor of class Text"""
    text = Text()
    alphabet = text.alphabet(lower_case=True)
    # Test 1
    assert len(alphabet) > 26

    # Test 2
    assert isinstance(text.level(), str)

    # Test 3
    assert isinstance(text.color(), str)

    # Test 4
    assert isinstance(text.hex_color(), str)

    # Test 5
    assert isinstance(text.rgb_color(safe=True), tuple)

    # Test 6
    assert isinstance(text.rgb_color(safe=True), tuple)

    # Test 7
    assert isinstance(text.rgb_color(safe=False), tuple)

    # Test 8
    assert isinstance(text.answer(), str)

    # Test 9

# Generated at 2022-06-14 00:52:30.331515
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    rng = random.Random()
    rng.seed(12345)
    instance = Text(seed=rng)
    result = instance.hex_color()
    expected = '#0c0d0e'
    assert result == expected


# Generated at 2022-06-14 00:52:32.853143
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    t = Text()
    print(t.alphabet(lower_case = False))
    print(t.alphabet(lower_case = True))



# Generated at 2022-06-14 00:52:38.073375
# Unit test for method quote of class Text
def test_Text_quote():
    text = Text()
    quotes = [
        "The sea was angry that day, my friends - like an old man trying "
        "to send back soup in a deli.",
        "You've gotta ask yourself one question: 'Do I feel lucky?' Well, "
        "do ya, punk?",
    ]
    for _ in range(10):
        assert text.quote() in quotes

# Generated at 2022-06-14 00:52:41.010563
# Unit test for method text of class Text
def test_Text_text():
    t = Text()
    result = t.text()
    print(result)
    assert len(result.split()) >= 5


# Generated at 2022-06-14 00:52:45.469296
# Unit test for method words of class Text
def test_Text_words():
    """Get a random answer in current language."""
    
    text = Text()
    ans = text.words()
    assert ans != '', "Text.words() fail"
    print("Text.words() pass")

if __name__ == '__main__':
    
    test_Text_words()

# Generated at 2022-06-14 00:52:51.597914
# Unit test for method level of class Text
def test_Text_level():
    from mimesis.enums import Locale

    t = Text(locale=Locale.EN)
    assert t.level() in [
        'critical',
        'emergency',
        'alert',
        'error',
        'warning',
        'notice',
        'info',
        'debug',
    ]


# Generated at 2022-06-14 00:52:53.735718
# Unit test for method color of class Text
def test_Text_color():
    text = Text()
    color = text.color()
    assert color in text._data['color']

# Generated at 2022-06-14 00:52:57.874669
# Unit test for method title of class Text
def test_Text_title():
    x = Text()
    y = Text(locale="ru")
    a = x.title()
    b = y.title()
    assert a != b


# Generated at 2022-06-14 00:53:01.240685
# Unit test for method sentence of class Text
def test_Text_sentence():
    """Test for method sentence of class Text."""
    text = Text()
    result = text.sentence()
    assert isinstance(result, str)
    assert len(result) > 0


# Generated at 2022-06-14 00:56:08.728709
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    assert isinstance(text.word(), str)
    assert text.word() in text._data['words']['normal']


# Generated at 2022-06-14 00:56:09.955481
# Unit test for constructor of class Text
def test_Text():
    t = Text()
    print(t.color())

# Generated at 2022-06-14 00:56:13.462251
# Unit test for method level of class Text
def test_Text_level():
    from mimesis.enums import Locale

    level = Text(locale=Locale.PT_BR.value).level()
    assert type(level) is str

# Generated at 2022-06-14 00:56:20.704853
# Unit test for method words of class Text
def test_Text_words():
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider
    custom_gender = Gender.FEMALE
    russia_data_provider = RussiaSpecProvider(gender=custom_gender)
    text = russia_data_provider.text.words(quantity=3)
    assert isinstance(text, list)
    assert len(text) == 3

# Generated at 2022-06-14 00:56:23.972359
# Unit test for method level of class Text
def test_Text_level():
    text = Text()
    result = text.level()
    assert result in ['low', 'normal', 'high', 'critical']



# Generated at 2022-06-14 00:56:27.184149
# Unit test for method title of class Text
def test_Text_title():
    text = Text()
    assert text.title() == "Maizter, J. S. (2002). Who's Hiring Whom? Gender and Racial Bias in the Market for New Economics Ph.D."


# Generated at 2022-06-14 00:56:29.341844
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    r = Text()
    r.rgb_color()
    r.rgb_color(safe=True)

# Generated at 2022-06-14 00:56:33.792748
# Unit test for method color of class Text
def test_Text_color():
    t = Text()
    color = t.color()
    assert len(color) > 3


# Generated at 2022-06-14 00:56:36.713412
# Unit test for method sentence of class Text
def test_Text_sentence():
    from mimesis.enums import Gender
    from mimesis.builtins import USA
    mock = USA()
    assert 'Have a nice day'  == mock.text.sentence()


# Generated at 2022-06-14 00:56:45.443426
# Unit test for method color of class Text
def test_Text_color():
    t = Text()
    assert t.color() in ["Red","Green","Blue","Yellow","Orange","Purple","Pink","Brown","Grey","Black","White","Aquamarine","Azure","Beige","Chartreuse","Chocolate","Coral","Cyan","Emerald","Fuchsia","Gold","Indigo","Ivory","Khaki","Lavender","Maroon","Navy blue","Olive","Orchid","Pale green","Plum","Raspberry","Scarlet","Silver","Turquoise","Violet","White","Yellow green"]

# Generated at 2022-06-14 00:59:41.663016
# Unit test for constructor of class Text
def test_Text():
    t = Text()
    assert t


# Generated at 2022-06-14 00:59:42.904903
# Unit test for constructor of class Text
def test_Text():
    t = Text()
    Text()
    Text()


# Generated at 2022-06-14 00:59:44.952921
# Unit test for method word of class Text
def test_Text_word():
    t = Text()
    w = t.word()
    print("Random word: ", w)


# Generated at 2022-06-14 00:59:47.549028
# Unit test for method sentence of class Text
def test_Text_sentence():
    for i in range(5):
        test_text = Text().sentence()
        assert isinstance(test_text, str)


# Generated at 2022-06-14 00:59:58.761849
# Unit test for method quote of class Text
def test_Text_quote():
    from mimesis.enums import Gender
    from datetime import datetime
    from mimesis.exceptions import NonEnumerableError, UnsupportedLocale

    # Creating Text
    text = Text()

    # Checking existing locales
    locales = text.locales()
    assert isinstance(locales, list)
    assert len(locales) > 0

    # Checking setted locale
    locale = text.locale
    assert isinstance(locale, str)
    assert len(locale) > 0

    # Checking setted seed
    seed = text.seed
    assert isinstance(seed, int)
    assert seed > 0

    # Checking setted gender
    gender = text.gender
    assert isinstance(gender, Gender)
    assert gender.value in ('M', 'F', 'N')

    # Checking setted dat

# Generated at 2022-06-14 01:00:00.890482
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    text = Text()
    assert len(text.rgb_color()) == 3


# Generated at 2022-06-14 01:00:09.141274
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    # Test uppercase
    assert Text().alphabet() == [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Test lowercase

# Generated at 2022-06-14 01:00:12.025097
# Unit test for method level of class Text
def test_Text_level():
    t = Text()
    print(t.level())


# Generated at 2022-06-14 01:00:14.842395
# Unit test for method words of class Text
def test_Text_words():
    text = Text()
    assert len(text.words(quantity=10)) == 10

# Generated at 2022-06-14 01:00:19.603675
# Unit test for method title of class Text
def test_Text_title():
    from mimesis.enums import Gender
    from mimesis.builtins import RussiaSpecProvider
    ru = RussiaSpecProvider(gender=Gender.MALE)
    assert ru.text.title() in ru.data('text', 'text')

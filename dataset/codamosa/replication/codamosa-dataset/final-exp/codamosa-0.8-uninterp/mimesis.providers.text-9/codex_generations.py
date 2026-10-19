

# Generated at 2022-06-14 00:52:11.897122
# Unit test for constructor of class Text

# Generated at 2022-06-14 00:52:15.452992
# Unit test for method word of class Text
def test_Text_word():
    from mimesis.enums import Locales
    from mimesis.providers.text import Text
    text = Text(locale=Locales.EN)
    word = text.word()
    word_list = text.words()
    assert isinstance(word, str)
    assert isinstance(word_list, list)
    assert len(word_list) == 5


# Generated at 2022-06-14 00:52:18.901569
# Unit test for method sentence of class Text
def test_Text_sentence():
    from mimesis.builtins import RussiaSpecProvider

    text = Text(RussiaSpecProvider)

    assert type(text.sentence()) == str


# Generated at 2022-06-14 00:52:20.094019
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    text = Text()
    res = text.swear_word()
    assert res != ""

# Generated at 2022-06-14 00:52:23.307687
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    t = Text()
    assert isinstance(t.alphabet(), list)
    assert isinstance(t.alphabet(lower_case=True), list)


# Generated at 2022-06-14 00:52:24.824837
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    t = Text()
    assert t.alphabet() != None



# Generated at 2022-06-14 00:52:29.372514
# Unit test for method quote of class Text
def test_Text_quote():
    t = Text()
    quote_length = 0
    for i in range(1000):
        quote = t.quote()
        quote_test = quote.split()
        if len(quote_test) > quote_length:
            quote_length = len(quote_test)
    return quote_length


# Generated at 2022-06-14 00:52:33.664785
# Unit test for method word of class Text
def test_Text_word():
    from mimesis.providers.text import Text
    obj = Text()
    x = obj.word()
    match = re.findall("[\\w']+", x)
    assert(len(x) == len(match[0]))


# Generated at 2022-06-14 00:52:39.900044
# Unit test for method word of class Text
def test_Text_word():
    from mimesis.enums import Language
    text = Text(Language.ENGLISH)
    word = text.word()
    import random
    assert word == random.choice(text._data['words']['normal'])
    assert isinstance(word, str)
    assert len(word) > 0


# Generated at 2022-06-14 00:52:41.482255
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    assert Text.rgb_color(Text()) != Text.rgb_color(Text())

# Generated at 2022-06-14 00:53:54.356445
# Unit test for method words of class Text
def test_Text_words():
    p = Text()
    x = p.words()
    assert len(x) == 5, "The length of list isn't equal to 5"



# Generated at 2022-06-14 00:53:58.580842
# Unit test for method word of class Text
def test_Text_word():
    '''
    test method word
    '''
    a = Text()
    assert a.word() == 'science'


# Generated at 2022-06-14 00:54:07.339180
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    t = Text()
    t.seed(1)
    assert t.swear_word() == 'Shit'
    assert t.swear_word() == 'Fuck'
    assert t.swear_word() == 'Hell'
    assert t.swear_word() == 'Damn'
    assert t.swear_word() == 'Bastard'
    t.seed(2)
    assert t.swear_word() == 'Hell'
    assert t.swear_word() == 'Bastard'
    assert t.swear_word() == 'Shit'
    assert t.swear_word() == 'Hell'
    assert t.swear_word() == 'Shit'


# Generated at 2022-06-14 00:54:08.616039
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    color = Text()
    assert color.hex_color(safe=True) in SAFE_COLORS

# Generated at 2022-06-14 00:54:11.727955
# Unit test for method words of class Text
def test_Text_words():
    text = Text()
    words = text.words()
    assert (len(words) == 5)
    assert all(isinstance(word, str) for word in words)


# Generated at 2022-06-14 00:54:14.980188
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    """Unit test for method hex_color of class Text.
    
    """
    testObject = Text()
    result = testObject.hex_color(safe=False)
    assert len(result) == 7
    assert result[0] == '#'


# Generated at 2022-06-14 00:54:17.043744
# Unit test for constructor of class Text
def test_Text():
    text = Text()
    assert isinstance(text, Text)


# Generated at 2022-06-14 00:54:31.669431
# Unit test for method sentence of class Text
def test_Text_sentence():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender
    r = RussiaSpecProvider(seed=4)
    test_cases = [
        ('ru', Gender.MALE, 'В Индонезии, основной и именно направлением концерта, и от театра биологической достоверности.')
    ]

    for lang, gender, expected in test_cases:
        r.set_locale(lang)
        r.set_gender(gender)

# Generated at 2022-06-14 00:54:35.004977
# Unit test for method answer of class Text
def test_Text_answer():
    t = Text('en')
    answer = t.answer()
    assert len(answer) > 0
test_Text_answer()


# Generated at 2022-06-14 00:54:38.554945
# Unit test for method level of class Text
def test_Text_level():
    text = Text('en')
    levels = ['critical', 'normal', 'debug']
    for _ in range(1000):
        assert text.level() in levels

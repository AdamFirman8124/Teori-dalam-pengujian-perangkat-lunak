

# Generated at 2022-06-14 00:52:10.713820
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    t = Text()
    al = t.alphabet(lower_case=True)
    assert isinstance(al, list) and al is not None


# Generated at 2022-06-14 00:52:14.616722
# Unit test for method word of class Text
def test_Text_word():
    t = Text()
    assert t.word() in t.words()

# Generated at 2022-06-14 00:52:16.674758
# Unit test for method text of class Text
def test_Text_text():
    provider = Text()
    result = provider.text()
    assert isinstance(result, str)


# Generated at 2022-06-14 00:52:23.081255
# Unit test for method level of class Text
def test_Text_level():
    from mimesis.enums import Locale
    t = Text(locale=Locale.JAPANESE)
    for i in range(1000):
        level = t.level()
        assert level in ['danger', 'critical', 'non-critical'], "Unit test failed."


# Generated at 2022-06-14 00:52:31.012200
# Unit test for method quote of class Text
def test_Text_quote():
    from mimesis.enums import Locale
    from mimesis.meta import ProviderMetadata
    from mimesis.providers.base import BaseProvider
    from mimesis.providers.text import Text
    p = Text(locale=Locale.RU)
    assert isinstance(p.quote(), str)
    assert p.quote() in p._data['quotes']
    assert isinstance(p.quote(), str)
    assert p.quote() in p._data['quotes']

# Generated at 2022-06-14 00:52:32.350427
# Unit test for method title of class Text
def test_Text_title():
    text = Text()
    assert text.title()


# Generated at 2022-06-14 00:52:34.110108
# Unit test for method answer of class Text
def test_Text_answer():
    txt = Text()
    assert txt.answer() in txt._data['answers']


# Generated at 2022-06-14 00:52:38.072931
# Unit test for constructor of class Text
def test_Text():
    print('# Constructor')
    t = Text('en')
    assert isinstance(t,Text)


# Generated at 2022-06-14 00:52:46.428268
# Unit test for method sentence of class Text
def test_Text_sentence():
    g = Text()
    print(g.sentence())
    print(g.alphabet())
    print(g.alphabet(lower_case=True))
    print(g.level())
    print(g.text())
    print(g.title())
    print(g.words())
    print(g.word())
    print(g.swear_word())
    print(g.quote())
    print(g.hex_color())
    print(g.rgb_color())
    print(g.color())
    print(g.answer())

# test_Text_sentence()

# Generated at 2022-06-14 00:52:49.911683
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    t = Text()
    result = t.rgb_color()
    assert isinstance(result, tuple)

# Generated at 2022-06-14 00:53:11.189106
# Unit test for method alphabet of class Text
def test_Text_alphabet():

	text = Text()
	result = text.alphabet()
	print(result)


# Generated at 2022-06-14 00:53:12.214569
# Unit test for method answer of class Text
def test_Text_answer():
    text = Text()

    assert len(text.answer()) > 0


# Generated at 2022-06-14 00:53:13.454422
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    assert Text(seed=1).hex_color() == '#8d4444'


# Generated at 2022-06-14 00:53:16.283180
# Unit test for method word of class Text
def test_Text_word():
    """Test for method word of class Text."""
    text = Text()
    word = text.word()
    assert isinstance(word, str)


# Generated at 2022-06-14 00:53:19.370201
# Unit test for constructor of class Text
def test_Text():
    # init the variables
    provider = Text(seed=12345678)
    assert provider.seed == 12345678
    assert provider.locale == 'en'



# Generated at 2022-06-14 00:53:20.683528
# Unit test for method answer of class Text
def test_Text_answer():
    text = Text()
    answer = text.answer()
    assert type(answer) == str

# Generated at 2022-06-14 00:53:22.851407
# Unit test for method sentence of class Text
def test_Text_sentence():
    t = Text()
    assert t.sentence() in t._data['text']

# Generated at 2022-06-14 00:53:26.404390
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    text = Text()
    rgb_color_string = text.rgb_color()
    print(rgb_color_string)


# Generated at 2022-06-14 00:53:29.893351
# Unit test for method answer of class Text
def test_Text_answer():
    # Get random answer
    answer = Text().answer()
    # Check if answer is a string
    print(answer)
    assert isinstance(answer, str)

# Generated at 2022-06-14 00:53:33.017143
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    from mimesis.builtins import Text
    from mimesis.enums import SafeColors
    color = Text()
    assert color.rgb_color() == color._hex_to_rgb(color.hex_color())
    assert color.rgb_color(safe=True) == color._hex_to_rgb(SafeColors.AMBER)

# Generated at 2022-06-14 00:54:13.179396
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    ab = Text()
    for i in range(0,100):
        assert isinstance(ab.alphabet(), list)


# Generated at 2022-06-14 00:54:25.940758
# Unit test for constructor of class Text
def test_Text():
    from mimesis.enums import Locales
    t = Text(locale = Locales.ENGLISH)
    print(t.quote())
    print(t.word())
    print(t.title())
    print(t.hex_color())
    print(t.rgb_color())
    print(t.text())
    print(t.color())
    print(t.alphabet(lower_case = False))
    print(t.level())
    print(t.answer())
    print(t.words())
    print(t.swear_word())


# Generated at 2022-06-14 00:54:28.125347
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    text = Text()
    print(text.swear_word())
    # result -> {'bad': ['damn', 'fuck', 'shit']}
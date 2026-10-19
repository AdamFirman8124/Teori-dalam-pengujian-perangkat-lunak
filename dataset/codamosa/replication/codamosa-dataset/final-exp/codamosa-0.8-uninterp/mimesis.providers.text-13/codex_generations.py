

# Generated at 2022-06-14 00:52:13.703468
# Unit test for method answer of class Text
def test_Text_answer():
    text = Text()
    answer = text.answer()
    assert answer in ['Yes', 'Not really', 'Of course', 'No', 'I do not know',
                      'It depends', 'Maybe', 'I am sure', 'It can be', 'Is this a question?']

# Generated at 2022-06-14 00:52:16.115912
# Unit test for method text of class Text
def test_Text_text():
    t = Text()
    assert t.text()
    assert len(t.text()) > 0


# Generated at 2022-06-14 00:52:19.473988
# Unit test for method quote of class Text
def test_Text_quote():
    text = Text('en')
    quote = text.quote()
    assert quote == "You know what they say about revenge."
    assert isinstance(quote, str)


# Generated at 2022-06-14 00:52:20.671228
# Unit test for method level of class Text
def test_Text_level():
    text_provider = Text()
    text_provider.level()


# Generated at 2022-06-14 00:52:24.226795
# Unit test for method text of class Text
def test_Text_text():
    txt = Text()
    res = txt.text()
    # print(res)
    assert isinstance(res, str)
    assert len(res) > 0

# Generated at 2022-06-14 00:52:26.304361
# Unit test for method sentence of class Text
def test_Text_sentence():
    from random import Random
    text = Text(Random())
    assert text.sentence() in text._data['text']


# Generated at 2022-06-14 00:52:27.649011
# Unit test for method quote of class Text
def test_Text_quote():
    t = Text()
    assert t.quote() in t._data['quotes']


# Generated at 2022-06-14 00:52:32.704462
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    '''
    This functions test a random hex color
    '''
    t = Text()
    x = t.hex_color()
    assert isinstance(x, str), 'x is not a string'
    assert x[0] == '#', 'x does not start with #'
    assert len(x) == 7, 'x does not have 7 characters'


# Generated at 2022-06-14 00:52:37.280007
# Unit test for method word of class Text
def test_Text_word():
    """Test for method word of class Text"""
    from mimesis.enums import Locale
    from mimesis.providers.text import Text

    text = Text(locale=Locale.ENGLISH)
    result = text.word()
    # It should be a string
    assert type(result) is str
    # It should be a word
    assert len(result) > 0


# Generated at 2022-06-14 00:52:46.985037
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    """Test method Text.rgb_color()."""
    from mimesis.providers.text import Text
    t = Text()
    # Normal
    for i in range(10):
        rgb_color = t.rgb_color()
        assert len(rgb_color) == 3
        for item in rgb_color:
            assert isinstance(item, int)
            assert 0 <= item <= 256
    # Safe
    for i in range(10):
        rgb_color = t.rgb_color(safe=True)
        assert len(rgb_color) == 3
        for item in rgb_color:
            assert isinstance(item, int)
            assert 0 <= item <= 256

# Generated at 2022-06-14 00:55:14.808307
# Unit test for method text of class Text
def test_Text_text():
    t = Text()
    assert len(t.text(5).split(" ")) == 5



# Generated at 2022-06-14 00:55:16.314094
# Unit test for method sentence of class Text
def test_Text_sentence():
    text = Text()
    print(text.sentence())

# Generated at 2022-06-14 00:55:20.560033
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    # Initialization of Text class
    text = Text()
    # Call method swear_word
    answer = text.swear_word()
    # Check for a valid answer
    assert type(answer) == str

# Generated at 2022-06-14 00:55:28.485717
# Unit test for method text of class Text
def test_Text_text():
    from random import seed
    from mimesis.builtins import RussiaSpecProvider
    seed(0)
    rus = RussiaSpecProvider(seed=0)
    assert rus.text() == u'Северный полюс поместили под тонкое стекло.'

# Generated at 2022-06-14 00:55:32.389654
# Unit test for method swear_word of class Text
def test_Text_swear_word():
        """Test method swear_word() of class Text."""
        test_Text = Text()
        test_result = test_Text.swear_word()
        assert test_result in test_Text._data['words']['bad']


# Generated at 2022-06-14 00:55:35.662781
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    #locales = ['en', 'ru', 'zh']
    #for ln in locales:
    ln = 'en'
    text = Text()
    content = text.swear_word()
    print(content)
    assert len(content) > 3

if __name__ == '__main__':
    test_Text_swear_word()

# Generated at 2022-06-14 00:55:38.047158
# Unit test for method answer of class Text
def test_Text_answer():
	print(Text().answer())


# Generated at 2022-06-14 00:55:39.934162
# Unit test for constructor of class Text
def test_Text():
    text = Text()
    print(text.level())


# Generated at 2022-06-14 00:55:42.214113
# Unit test for method sentence of class Text
def test_Text_sentence():
    text = Text()
    text.sentence()
#test_Text_sentence()


# Generated at 2022-06-14 00:55:47.497970
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    """Unit test for method hex_color of class Text."""
    # we tested this methond with 15 times, so we make sure that the
    # generated color is the same.
    text = Text(seed=123)
    for _ in range(15):
        assert text.hex_color(safe=True) == "#0088cc"
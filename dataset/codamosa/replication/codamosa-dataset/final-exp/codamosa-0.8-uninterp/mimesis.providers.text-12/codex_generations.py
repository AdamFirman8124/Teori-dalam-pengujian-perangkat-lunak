

# Generated at 2022-06-14 00:52:23.691077
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    """Test for method alphabet of class Text."""
    text = Text()
    alphabet = text.alphabet()
    assert len(alphabet) == 26
    assert text.alphabet(lower_case=True) != ''


# Generated at 2022-06-14 00:52:24.394471
# Unit test for method sentence of class Text
def test_Text_sentence():
    Text().sentence()

# Generated at 2022-06-14 00:52:25.747836
# Unit test for method title of class Text
def test_Text_title():
    t = Text('fr')
    print(t.title())


# Generated at 2022-06-14 00:52:27.152824
# Unit test for method level of class Text
def test_Text_level():
    t = Text()
    a = t.level()
    assert isinstance(a, str)


# Generated at 2022-06-14 00:52:29.900704
# Unit test for method title of class Text
def test_Text_title():
    t = Text()
    title = t.title()
    assert title is not None


# Generated at 2022-06-14 00:52:32.161761
# Unit test for method quote of class Text
def test_Text_quote():
    answerKey = "I’ll be back."
    text = Text(seed=0)
    assert (text.quote() == answerKey)

# Generated at 2022-06-14 00:52:34.838351
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    words = text.word()
    print(words)
    assert len(words)>=5
    assert words[0]>='A' and words[0]<='Z'

# Generated at 2022-06-14 00:52:40.392059
# Unit test for method answer of class Text
def test_Text_answer():
    from mimesis.enums import Language
    from mimesis.providers.text import Text
    rus = Text(Language.RU)
    en = Text(Language.EN)
    assert type(rus.answer()) == str
    assert type(en.answer()) == str


# Generated at 2022-06-14 00:52:43.317246
# Unit test for method text of class Text
def test_Text_text():
    """Test method text of class Text."""
    t = Text(seed=123456789)
    assert t.text() == 'I can prove this.'



# Generated at 2022-06-14 00:52:45.235238
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    word = text.word()
    assert len(word) > 0
    assert " " not in word
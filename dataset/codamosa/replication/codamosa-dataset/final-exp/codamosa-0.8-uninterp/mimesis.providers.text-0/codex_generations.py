

# Generated at 2022-06-14 00:52:11.877334
# Unit test for method title of class Text
def test_Text_title():
    print("Start test_Text_title()")
    provider = Text()
    title = provider.title()
    assert not isinstance(title, list)
    assert isinstance(title, str)
    print("Finish test_Text_title()")


# Generated at 2022-06-14 00:52:16.384675
# Unit test for method word of class Text
def test_Text_word():
    t = Text()
    w = t.word()
    assert isinstance(w, str)
    assert len(w) > 0


# Generated at 2022-06-14 00:52:22.903192
# Unit test for method text of class Text
def test_Text_text():
    # TEST 1, CREATION OF A CLASS
    t = Text()

    result = type(t) == Text
    assert result, "Cannot create a class of type Text."
    # TEST 2, CREATING A TEXT
    result = type(t.text()) == str
    assert result, "Cannot create a text."

    # Unit test for method word of class Text

# Generated at 2022-06-14 00:52:24.041844
# Unit test for method level of class Text
def test_Text_level():
    text = Text()
    assert (text.level() in text._data['level'])


# Generated at 2022-06-14 00:52:28.928087
# Unit test for method level of class Text
def test_Text_level():
    # GIVEN a class Text
    text = Text()

    # WHEN level method is used
    result = text.level()

    # THEN the result is a string
    from mimesis.enums import DataField
    assert isinstance(result, str)
    assert result in text.field_choices[DataField.LEVEL]


# Generated at 2022-06-14 00:52:31.924039
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    import random
    random.seed(0)
    a = Text()
    assert a.hex_color() == '#ba3e49'



# Generated at 2022-06-14 00:52:35.172429
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    class_name = "Text"
    method_name = "alphabet"
    alphabet = globals()[class_name]().alphabet(lower_case=True) # get alphabet
    print(alphabet)
    assert(len(alphabet)==26)



# Generated at 2022-06-14 00:52:38.073636
# Unit test for method level of class Text
def test_Text_level():
    return Text().level()


# Generated at 2022-06-14 00:52:41.474977
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    text = Text()
    for i in range(10):
        assert len(set(text.hex_color())) == 7
        assert len(set(text.hex_color(safe=True))) == 7

# Generated at 2022-06-14 00:52:43.811989
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    sentence = text.word()
    assert type(sentence) == str
    print(sentence)

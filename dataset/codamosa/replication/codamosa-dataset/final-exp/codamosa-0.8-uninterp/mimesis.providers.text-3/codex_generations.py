

# Generated at 2022-06-14 00:52:09.086793
# Unit test for method words of class Text
def test_Text_words():
    text_provider = Text()
    word_list = text_provider.words()
    assert word_list != None

# Generated at 2022-06-14 00:52:10.491766
# Unit test for method level of class Text
def test_Text_level():
    print(Text().level())


# Generated at 2022-06-14 00:52:11.707338
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    data = Text()
    print(data.swear_word())


# Generated at 2022-06-14 00:52:14.210890
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    t = Text()
    assert t.hex_color(safe=True) in SAFE_COLORS
    assert t.hex_color(safe=False) != t.hex_color(safe=True)


# Generated at 2022-06-14 00:52:16.271860
# Unit test for method sentence of class Text
def test_Text_sentence():
    text = Text()
    a = text.sentence()
    print(a)


# Generated at 2022-06-14 00:52:28.520208
# Unit test for method words of class Text
def test_Text_words():
    """Unit test for method words of class Text."""
    # Provide result
    result = ['animal', 'station', 'inquiry',
              'yes','star', 'country', 'island',
              'robot','cigar', 'game', 'window',
              'bottle', 'system', 'frog', 'coffee',
              'hand', 'sugar', 'rock', 'language',
              'professor', 'box', 'investigation',
              'creature', 'student', 'university',
              'goose', 'baby', 'hundred', 'game',
              'carriage', 'love', 'pumpkin', 'machine',
              'carpenter', 'hair', 'honey']
    # Create text instance and test method
    text = Text()
    text_words = text.words(quantity=50)
    assert text_

# Generated at 2022-06-14 00:52:31.746100
# Unit test for method words of class Text
def test_Text_words():
    t = Text()
    assert len(t.words()) == 5
    assert len(t.words(quantity=10)) == 10
    assert isinstance(t.words(), list)


# Generated at 2022-06-14 00:52:33.580945
# Unit test for constructor of class Text
def test_Text():
    from mimesis.builtins import Text
    l = Text('ru')
    l.countries


# Generated at 2022-06-14 00:52:46.081640
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    """Tests for Text.alphabet"""
    t = Text(seed=0)
    assert t.alphabet(lower_case=True) == ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                           'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                           'o', 'p', 'q', 'r', 's', 't', 'u',
                                           'v', 'w', 'x', 'y', 'z']

# Generated at 2022-06-14 00:52:49.912138
# Unit test for method title of class Text
def test_Text_title():
    text = Text()
    assert isinstance(text.title(), str) == True


# Generated at 2022-06-14 00:53:20.828163
# Unit test for method answer of class Text
def test_Text_answer():
    """
    Test method answer of class Text.
    """
    class Test_text:
        """
        Test class.
        """
        def __init__(self):
            """
            Initialise test class.
            """
            self.text = Text('en')

        def test_answer(self):
            """
            Test method answer.
            """
            ans = self.text.answer()
            if ans not in self.text._data['answers']:
                raise AssertionError('"answer" method of "Text" class does not return a value from "text.json"!')

    test_text_obj = Test_text()
    test_text_obj.test_answer()

# Generated at 2022-06-14 00:53:23.443474
# Unit test for method color of class Text
def test_Text_color():
    text = Text()
    color = text.color()
    assert isinstance(color, str)
    assert color != ''

# Generated at 2022-06-14 00:53:24.491530
# Unit test for method word of class Text
def test_Text_word():
    pass

# Generated at 2022-06-14 00:53:27.781565
# Unit test for method text of class Text
def test_Text_text():
    """
    test_Text_text()
    """
    print(dir(Text))

    provider = Text('en')
    print(provider.text())



# Generated at 2022-06-14 00:53:30.705732
# Unit test for method quote of class Text
def test_Text_quote():
    """Test for method quote of class Text."""
    text = Text()
    return text.quote()

# Generated at 2022-06-14 00:53:33.204869
# Unit test for method level of class Text
def test_Text_level():
    text = Text()
    assert text.level() in ['critical', 'high', 'medium', 'low']


# Generated at 2022-06-14 00:53:36.041814
# Unit test for method title of class Text
def test_Text_title():
    t = Text()
    a = t.title()
    assert isinstance(a, str)



# Generated at 2022-06-14 00:53:37.635088
# Unit test for method color of class Text
def test_Text_color():
    text = Text()
    result = text.color()
    assert result is not None

# Generated at 2022-06-14 00:53:40.061057
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    text = Text()
    print(text.swear_word())


# Generated at 2022-06-14 00:53:41.783997
# Unit test for method answer of class Text
def test_Text_answer():
    obj = Text('en')
    r1 = obj.answer()
    assert r1 in ['Yes', 'No', 'Maybe']
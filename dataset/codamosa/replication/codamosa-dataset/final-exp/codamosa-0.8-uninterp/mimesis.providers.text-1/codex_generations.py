

# Generated at 2022-06-14 00:52:07.833716
# Unit test for method answer of class Text
def test_Text_answer():
    a = Text().answer()
    assert a in ('Yes', 'No', 'I don\'t know', 'I know')

# Generated at 2022-06-14 00:52:11.471571
# Unit test for method sentence of class Text
def test_Text_sentence():
  from mimesis.builtins import Text
  from mimesis.enums import Gender
  t = Text('en')
  assert t.sentence()!=t.sentence()

#Unit test for method title of class Text

# Generated at 2022-06-14 00:52:13.971058
# Unit test for method quote of class Text
def test_Text_quote():
    t = Text(seed=42)
    q = t.quote()
    assert q == '"You can\'t finish a test without a ball, that\'s no way to live."'


# Generated at 2022-06-14 00:52:17.480592
# Unit test for method quote of class Text
def test_Text_quote():
    """ Testing the quote method of class Text """
    test_obj = Text()
    result = test_obj.quote()
    print(result)


# Generated at 2022-06-14 00:52:19.326219
# Unit test for method level of class Text
def test_Text_level():
    assert Text().level() == 'critical'

# Generated at 2022-06-14 00:52:20.525324
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    assert Text().rgb_color() in set(Text().rgb_color())

# Generated at 2022-06-14 00:52:24.491374
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    text = Text(locale='en')
    a = text.alphabet()
    b = text.alphabet(lower_case=True)
    print(a, b)


# Generated at 2022-06-14 00:52:28.327326
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    """Test rgb_color is successfully call."""
    # Test
    result = Text.rgb_color()
    # Assertions
    assert type(result) is tuple
    assert len(result) == 3
    assert result < (256, 256, 256)

# Generated at 2022-06-14 00:52:29.105492
# Unit test for method level of class Text
def test_Text_level():
    txt = Text()


# Generated at 2022-06-14 00:52:30.945193
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    assert len(text.word()) > 0

# Generated at 2022-06-14 00:52:58.522831
# Unit test for method color of class Text
def test_Text_color():
    
    def test_text():
        t = Text()
        return t.color()

    assert len(test_text()) > 0


# Generated at 2022-06-14 00:53:00.916629
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    assert text.word() in text._data['words'].get('normal')

# Generated at 2022-06-14 00:53:03.176746
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    from mimesis.builtins import Text
    t = Text()
    for i in range(100):
        assert len(t.hex_color()) == 7

# Generated at 2022-06-14 00:53:05.940735
# Unit test for method color of class Text
def test_Text_color():
    # Given
    t = Text()

    # When
    result = t.color()

    # Then
    assert result in t._data["color"], "Result is not valid"

# Generated at 2022-06-14 00:53:10.113761
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    word = text.word()
    print('Random word is: %s' % word)


# Generated at 2022-06-14 00:53:15.107146
# Unit test for method sentence of class Text
def test_Text_sentence():

    from mimesis.builtins import Text
    #from mimesis.enums import Gender

    text = Text()
    #print(text.text())
    #print(text.title())
    #print(text.words())
    #print(text.word())
    #print(text.swear_word())
    #print(text.quote())
    #print(text.color())
    #print(text.hex_color())
    #print(text.rgb_color())
    print(text.answer())

if __name__ == '__main__':
    test_Text_sentence()

# Generated at 2022-06-14 00:53:18.641315
# Unit test for method color of class Text
def test_Text_color():
    text = Text()
    color = text.color()
    assert(type(color) == str)

# Generated at 2022-06-14 00:53:23.349288
# Unit test for method sentence of class Text
def test_Text_sentence():
    # Create an object of class Text
    text_obj = Text()
    
    # Get a random sentence of text
    sentence = text_obj.sentence()
    
    # Check that sentence is a string 
    assert isinstance(sentence, str) 


# Generated at 2022-06-14 00:53:25.548318
# Unit test for method quote of class Text
def test_Text_quote():
    # TODO: write unit test for method quote of class Text
    pass

# Generated at 2022-06-14 00:53:28.094117
# Unit test for method color of class Text
def test_Text_color():
    t=Text()
    color=t.color()
    print(color)
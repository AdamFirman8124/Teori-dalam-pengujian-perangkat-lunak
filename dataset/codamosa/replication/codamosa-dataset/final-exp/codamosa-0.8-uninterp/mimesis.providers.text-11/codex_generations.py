

# Generated at 2022-06-14 00:52:08.969646
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    text = Text()
    color = text.hex_color()
    assert len(color) == 7
    assert color[0] == "#"

# Generated at 2022-06-14 00:52:11.106634
# Unit test for method level of class Text
def test_Text_level():
    txt = Text()
    assert txt.level() in ['critical', 'high', 'medium', 'low']

# Generated at 2022-06-14 00:52:13.661610
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    """Unit test for method hex_color of class Text."""
    temp = Text('en')
    print("Test for method hex_color of class Text:\n", temp.hex_color())


# Generated at 2022-06-14 00:52:16.116468
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    t = Text()
    assert isinstance(t.rgb_color(), Tuple[int, ...])

# Generated at 2022-06-14 00:52:19.077565
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    """Unit test for method swear_word of class Text."""
    text = Text()
    assert text.swear_word() is not None

# Generated at 2022-06-14 00:52:22.762196
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    # Given
    text = Text()
    # When
    result = text.hex_color()
    # Then
    assert len(result) == 7
    assert result[0] == '#'


# Generated at 2022-06-14 00:52:26.440341
# Unit test for method answer of class Text
def test_Text_answer():
    """Unit test for method answer of class Text."""
    t = Text()
    print(t.answer())



# Generated at 2022-06-14 00:52:30.367244
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    # Generate a random rgb color tuple
    txt_obj = Text()
    result = txt_obj.rgb_color()

    print(result)
if __name__ == '__main__':
    test_Text_rgb_color()

# Generated at 2022-06-14 00:52:33.310408
# Unit test for method text of class Text
def test_Text_text():
    print('Test method text of class Text: ')
    p = Text()
    print(p.text())
# Test method text of class Text
# test_Text_text()


# Generated at 2022-06-14 00:52:36.591931
# Unit test for method color of class Text
def test_Text_color():
    text = Text(seed=0)
    assert text.color() == 'Red'


# Generated at 2022-06-14 00:52:52.337902
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    t = Text()
    print(t.swear_word())

# Generated at 2022-06-14 00:52:54.058836
# Unit test for method text of class Text
def test_Text_text():
    text_class = Text()
    text_class.text()

# Generated at 2022-06-14 00:53:02.947220
# Unit test for constructor of class Text

# Generated at 2022-06-14 00:53:05.940839
# Unit test for method answer of class Text
def test_Text_answer():
    test_obj = Text()
    test_obj.answer()
if __name__ == '__main__':
    test_Text_answer()


# Generated at 2022-06-14 00:53:08.356916
# Unit test for method words of class Text
def test_Text_words():
    text = Text()
    x = text.words(quantity=1)
    print(x)

# Generated at 2022-06-14 00:53:11.192473
# Unit test for method answer of class Text
def test_Text_answer():
    for _ in range(100):
        assert Text().answer() in Text()._data['answers']

# Generated at 2022-06-14 00:53:16.299421
# Unit test for constructor of class Text
def test_Text():
    assert issubclass(Text, BaseDataProvider)

    # Constructor of class Text
    text = Text()

    assert isinstance(text.data, dict)
    assert text.data
    assert isinstance(text.random, BaseDataProvider)
    assert isinstance(text.seed, int)
    assert isinstance(text.provider_name, str)
    assert text.provider_name == 'text'
    assert text.locale
    assert hasattr(text, '_data')
    assert isinstance(text._data, dict)
    assert text._data
    assert hasattr(text, '_datafile')
    assert text._datafile == 'text.json'



# Generated at 2022-06-14 00:53:22.749064
# Unit test for method level of class Text
def test_Text_level():
    text = Text()
    values = text.level()
    assert values == 'critical' or values == 'info' or values == 'normal' or values == 'alert' or values == 'danger'


# Generated at 2022-06-14 00:53:25.642602
# Unit test for method sentence of class Text
def test_Text_sentence():
    texts = [Text() for _ in range(100)]
    assert all(isinstance(t.sentence(), str) for t in texts)

# Generated at 2022-06-14 00:53:30.365117
# Unit test for method answer of class Text
def test_Text_answer():
    for _ in range(1000):
        answer = Text(seed=_).answer()
        assert type(answer) == str  #check example
        assert len(answer) > 0  # check example


# Generated at 2022-06-14 00:53:59.242575
# Unit test for method color of class Text
def test_Text_color():
    text = Text()
    color = text.color()
    assert len(color) > 0


# Generated at 2022-06-14 00:54:01.840340
# Unit test for method quote of class Text
def test_Text_quote():
    text = Text()
    t = text.quote()
    assert t



# Generated at 2022-06-14 00:54:06.048584
# Unit test for method word of class Text
def test_Text_word():
    from mimesis import Text
    for i in range(10):
        text = Text('en')
        word = text.word()
        print(word)


# Generated at 2022-06-14 00:54:09.295207
# Unit test for method answer of class Text
def test_Text_answer():
    """Test answer method of class Text.

    :return: None.
    """
    text_test = Text(seed=1000)
    result = text_test.answer()
    expected_result = 'No'
    assert result == expected_result


# Generated at 2022-06-14 00:54:16.062890
# Unit test for method word of class Text
def test_Text_word():
    from mimesis.providers.text import Text
    from mimesis.enums import Providers

    t = {
        Providers.TEXT: Text,
    }

    def get_result(local):
        for provider_package, provider_class in t.items():
            print(provider_package)
            item = provider_class(local)

            print(item.word())
        print()

    local_list = ['en', 'de', 'sv', 'pt-BR', 'zh']
    for local in local_list:
        get_result(local)

# Generated at 2022-06-14 00:54:19.519019
# Unit test for method word of class Text
def test_Text_word():
    """Test method word of class Text."""
    print(Text().word())


# Generated at 2022-06-14 00:54:22.584240
# Unit test for method words of class Text
def test_Text_words():
    text = Text(seed=123)
    words = ' '.join(text.words())
    assert words == 'food garden crowd price suit'

# Generated at 2022-06-14 00:54:26.142189
# Unit test for constructor of class Text
def test_Text():
    """
    Test for constructor of Text class.
    
    """
    text_generator = Text()
    assert isinstance(text_generator, Text)


# Generated at 2022-06-14 00:54:27.242103
# Unit test for method title of class Text
def test_Text_title():
    t = Text()
    print(t.title())

# Generated at 2022-06-14 00:54:29.040664
# Unit test for method text of class Text
def test_Text_text():
    Text().text(quantity=1)

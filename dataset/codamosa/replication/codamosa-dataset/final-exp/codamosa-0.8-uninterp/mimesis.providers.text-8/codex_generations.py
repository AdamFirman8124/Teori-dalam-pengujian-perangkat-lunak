

# Generated at 2022-06-14 00:53:31.313507
# Unit test for method color of class Text
def test_Text_color():
	t = Text()
	c = t.hex_color()
	return c


# Generated at 2022-06-14 00:53:32.678283
# Unit test for method answer of class Text
def test_Text_answer():
    assert Text().answer()

# Generated at 2022-06-14 00:53:35.135658
# Unit test for method word of class Text
def test_Text_word():
    t = Text()
    #we have to create a generator object from text generator
    assert t.word() == 'Bugs'
    

# Generated at 2022-06-14 00:53:38.204889
# Unit test for constructor of class Text
def test_Text():
    """Unit-test for Text.

    :return: True if test passed.
    """
    text = Text()
    assert text.text(quantity=3) == 'test hello world'

# Generated at 2022-06-14 00:53:41.582274
# Unit test for method words of class Text
def test_Text_words():
    text = Text()
    words = text.words(4)

    assert len(words) == 4

    words = text.words()

    assert len(words) == 5

# Generated at 2022-06-14 00:53:48.062514
# Unit test for method word of class Text

# Generated at 2022-06-14 00:53:51.132655
# Unit test for method level of class Text
def test_Text_level():
    expected_result = 'critical'
    result = Text().level()
    assert result == expected_result


# Generated at 2022-06-14 00:53:54.976345
# Unit test for method title of class Text
def test_Text_title():
    """Return the result of a test.

    :return: True
    """
    t = Text()
    title = t.title()
    assert title, 'title must be not empty'
    assert len(title) <= 10, 'title must be equal or less than 10'

# Generated at 2022-06-14 00:53:57.117250
# Unit test for method words of class Text
def test_Text_words():
    text = Text()
    assert isinstance(text.words()[0], str) is True


# Generated at 2022-06-14 00:54:03.788592
# Unit test for method answer of class Text
def test_Text_answer():
    """Test function for unit test"""
    from mimesis.enums import Locale
    from mimesis.builtins import Text
    expected = 'No'
    text = Text(locale=Locale.ENGLISH)
    result = text.answer()
    assert result in expected
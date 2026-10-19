

# Generated at 2022-06-14 00:52:49.921074
# Unit test for method text of class Text
def test_Text_text():
    text = Text()
    text.text()
    # print('Text: ', text)



# Generated at 2022-06-14 00:52:56.300906
# Unit test for method color of class Text
def test_Text_color():
    from mimesis.enums import Locale
    from mimesis.providers.base import BaseProvider

    class A(BaseProvider):
        class Meta:
            name = 'B'

        text = Text(Locale.ENGLISH)

    a = A()
    print(a.text.color())
    print(a.text.hex_color())
    print(a.text.rgb_color())


# Generated at 2022-06-14 00:52:57.449109
# Unit test for method quote of class Text
def test_Text_quote():
    a = Text()
    result = a.quote()
    assert result

# Generated at 2022-06-14 00:53:00.027797
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    instance = Text()
    result = instance.alphabet()
    assert isinstance(result, list)
    assert len(result) == 26


# Generated at 2022-06-14 00:53:02.714048
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    from mimesis.enums import Language
    from mimesis.localization import get_formatter
    my_text = Text(Language.ENGLISH)
    assert my_text.swear_word() in get_formatter('en').bad_words

# Generated at 2022-06-14 00:53:05.940701
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    for _ in range(100):
        assert len(Text().rgb_color()) == 3


# Generated at 2022-06-14 00:53:08.978950
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    #
    x = Text()
    #
    r = x.rgb_color()
    #
    print(r)
    #


# Generated at 2022-06-14 00:53:11.270783
# Unit test for method level of class Text
def test_Text_level():
    t = Text()
    level = t.level()
    assert level in t._data['level']



# Generated at 2022-06-14 00:53:15.134681
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    text = Text()
    alphabet = text.alphabet()
    # print(alphabet)  # output: ['A', 'B', 'C', ...]
    assert alphabet is not None
    assert len(alphabet) == 26
    alphabet = text.alphabet(lower_case=True)
    # print(alphabet)  # output: ['a', 'b', 'c', ...]
    assert alphabet is not None
    assert len(alphabet) == 26


# Generated at 2022-06-14 00:53:18.360650
# Unit test for method title of class Text
def test_Text_title():
    t = Text()
    assert isinstance(t.title(), str)


# Generated at 2022-06-14 00:53:36.490077
# Unit test for method color of class Text
def test_Text_color():
    text = Text()
    color = text.color()
    assert color



# Generated at 2022-06-14 00:53:37.949404
# Unit test for method sentence of class Text
def test_Text_sentence():
    for i in range(10):
        assert Text().sentence().__class__ == str

# Generated at 2022-06-14 00:53:41.525467
# Unit test for method sentence of class Text
def test_Text_sentence():
    print("Testing: Text.sentence")
    text = Text()
    print(text.sentence())
    print("Success!")

if __name__ == "__main__":
    test_Text_sentence()

# Generated at 2022-06-14 00:53:45.412740
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    '''TESTING:
    - (150, 190, 200)
    '''
    from mimesis.builtins import Text
    from pprint import pprint
    results = Text().rgb_color(safe=True)
    pprint(results)

if __name__ == "__main__":
    test_Text_rgb_color()

# Generated at 2022-06-14 00:53:47.845833
# Unit test for constructor of class Text
def test_Text():
    t = Text()
    return t

# Generated at 2022-06-14 00:53:56.519589
# Unit test for method title of class Text
def test_Text_title():
    # This function uses the function title of class Text to test if it works properly
    # The expected output is a random title, but it has to start with a capital letter
    # The test is performed 100 times and the output is checked against the criteria
    # If all the times the output is as expected, the test passes, in any other case, it fails
    for i in range(100):
        t = Text()
        title = t.title()
        if ord(title[0]) >= 65 and ord(title[0]) <= 90:
            continue
        else:
            assert False
    assert True

# Generated at 2022-06-14 00:54:07.158692
# Unit test for constructor of class Text
def test_Text():
    t = Text()
    print('text title: ' + t.title())
    print('text words: ' + ' '.join(t.words(4)))
    print('text sentence: ' + t.sentence())
    print('text swear word: ' + t.swear_word())
    print('text word: ' + t.word())
    print('text quote: ' + t.quote())
    print('text color: ' + t.color())
    print('text hex color: ' + t.hex_color())
    print('text rgb color: ' + str(t.rgb_color()))
    print('text answer: ' + t.answer())
    print('text alphabet: ' + ''.join(t.alphabet()))
    print('text level: ' + t.level())
    
test_Text()

# Generated at 2022-06-14 00:54:08.786423
# Unit test for method color of class Text
def test_Text_color():
    t = Text('en')
    c = t.color()

    assert c in t._data['color']

# Generated at 2022-06-14 00:54:10.161435
# Unit test for constructor of class Text
def test_Text():
    text = Text()
    assert isinstance(text, Text)

# Generated at 2022-06-14 00:54:14.680561
# Unit test for method alphabet of class Text
def test_Text_alphabet():

    # Initialize class
    text_class = Text()

    # Generate data
    data = text_class.alphabet()

    # Print result
    print(data)



# Generated at 2022-06-14 00:57:12.348018
# Unit test for method title of class Text
def test_Text_title():
    text = Text().title()
    assert isinstance(text, str)



# Generated at 2022-06-14 00:57:13.996141
# Unit test for method level of class Text
def test_Text_level():
    t = Text()
    assert t.level() in ["superhuman", "hard", "not bad", "simple", "easy"]

# Generated at 2022-06-14 00:57:18.720356
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    from . import text

    assert len(text.alphabet()) == len(text.alphabet(True))

# Generated at 2022-06-14 00:57:29.424642
# Unit test for method answer of class Text
def test_Text_answer():
    t = Text()
    a = t.answer()
    # Symbol has 4 possible values: +, -, 0, blank
    assert a in ["Да","Нет","Предварительно могу ответить лишь на основании бумажных документов.","Я повредил свой компьютер.", "Обращайтесь к моему специалисту по поддержке."]

# Generated at 2022-06-14 00:57:34.087411
# Unit test for method words of class Text
def test_Text_words():
    # GIVEN an instance of class Text
    t = Text(seed=42)
    # WHEN result of method words is requested
    result = t.words()
    # THEN is should equal given list
    assert result == ['octopus', 'science', 'professor', 'ocean', 'love']


# Generated at 2022-06-14 00:57:34.921765
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    text = Text()
    assert 'A' in text.alphabet()


# Generated at 2022-06-14 00:57:40.220775
# Unit test for method word of class Text
def test_Text_word():
    t = Text()
    print(t.word())


# Generated at 2022-06-14 00:57:46.856673
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    """Test for method alphabet of class Text."""
    text = Text()

    assert len(text.alphabet()) > 0
    assert len(text.alphabet(lower_case=True)) > 0



# Generated at 2022-06-14 00:57:49.443622
# Unit test for method word of class Text
def test_Text_word():
    text = Text(locale='en')
    text.word()


# Generated at 2022-06-14 00:57:53.990566
# Unit test for method title of class Text
def test_Text_title():
    from mimesis.enums import Locale
    t1 = Text(Locale.ENGLISH)
    t2 = Text(Locale.CHINESE)
    assert t1.title() != t2.title()
    
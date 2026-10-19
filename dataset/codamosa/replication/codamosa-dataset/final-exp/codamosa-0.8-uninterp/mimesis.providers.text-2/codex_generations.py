

# Generated at 2022-06-14 00:52:07.847079
# Unit test for method answer of class Text
def test_Text_answer():
    _text = Text()
    assert _text.answer() in ["Yes", "No", "Maybe"]

# Generated at 2022-06-14 00:52:15.963034
# Unit test for method quote of class Text
def test_Text_quote():
    """Method for testing method quote of class Text."""
    import os, sys
    try:
        from mimesis.builtins import BrazilSpecProvider
        from mimesis.enums import Gender
    except:
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            p = os.path.abspath(os.path.join(dir_path,'..','..'))
            if p not in sys.path:    
                sys.path.append(p)
            from mimesis.builtins import BrazilSpecProvider
            from mimesis.enums import Gender
        except:
            print('Can not find mimesis library')
            sys.exit()
    text = Text(BrazilSpecProvider)
    quote = text.quote();

# Generated at 2022-06-14 00:52:22.903837
# Unit test for method word of class Text
def test_Text_word():
    from mimesis.enums import Language
    seed = 8
    class_name = 'Text'
    method_name = 'word'
    parameters = {
        'seed' : seed,
    }
    output = 'bike'
    text_class = globals()[class_name](Language.ENGLISH, **parameters)
    result = text_class.word()
    assert result == output

# Generated at 2022-06-14 00:52:29.035819
# Unit test for method words of class Text
def test_Text_words():
    #Let's get some random words in English
    Words=Text(locale='en').words()

    #Let's get some random words in German
    WordsDe=Text(locale='de').words()

    #Let's get some random words in Ukrainian
    WordsUkr=Text(locale='uk').words()

    #Let's get some random words in Spanish
    WordsSp=Text(locale='es').words()


# Generated at 2022-06-14 00:52:35.086727
# Unit test for method text of class Text
def test_Text_text():
    t = Text()
    # the number of words in a sentence is between 5 and 10
    c = 0
    for _ in range(200):
        if len(t.text().split(' ')) <= 10 and len(t.text().split(' ')) >= 5:
            c += 1
    assert c >= 100
    # the text has the number of sentences equal to quantity
    for _ in range(100):
        assert len(t.text(3).split('.')) == 3



# Generated at 2022-06-14 00:52:40.443033
# Unit test for method sentence of class Text
def test_Text_sentence():
    text = Text(seed=123)
    assert text.sentence() == 'Ниже на слайде вы видите три число, признак'


# Generated at 2022-06-14 00:52:41.591958
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    return Text().swear_word()


# Generated at 2022-06-14 00:52:43.461045
# Unit test for method level of class Text
def test_Text_level():
    t=Text()
    t.level()
    print("We are testing method level of class Text")


# Generated at 2022-06-14 00:52:44.581076
# Unit test for method word of class Text
def test_Text_word():
    assert Text(seed=7).word() == 'network'

# Generated at 2022-06-14 00:52:47.635131
# Unit test for method color of class Text
def test_Text_color():
    """Unit test for method color of class Text."""
    text = Text()
    colors = text.color()
    color_list = colors.split(', ')
    assert len(color_list) > 0
    for color in color_list:
        assert color in colors

# Generated at 2022-06-14 00:53:59.530142
# Unit test for method answer of class Text
def test_Text_answer():
    """Test answer() method of class Text."""
    from mimesis.enums import Locale
    text = Text(locale=Locale.RUSSIAN)
    for i in range(100):
        print (text.answer())
    print(text.answer())


# Generated at 2022-06-14 00:54:03.783727
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    text = Text()
    for i in range(0,10):
        assert len(text.rgb_color()) == 3

# Generated at 2022-06-14 00:54:05.911404
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    # created instance of Text class
    t = Text()

    # call alphabet() method, with next arguments:
    t.alphabet()



# Generated at 2022-06-14 00:54:09.262745
# Unit test for method answer of class Text
def test_Text_answer():
    texts = Text('en')
    for _ in range(50):
        assert texts.answer() in texts.random.choice(texts._data['answers'])

# Generated at 2022-06-14 00:54:11.495144
# Unit test for method quote of class Text
def test_Text_quote():
    t = Text()

    assert isinstance(t.quote(), str)



# Generated at 2022-06-14 00:54:14.690451
# Unit test for method answer of class Text
def test_Text_answer():
    t = Text()
    assert t.answer() in t._data['answers']


# Generated at 2022-06-14 00:54:19.770914
# Unit test for method quote of class Text
def test_Text_quote():
    text = Text('en')
    for _ in range(100):
        assert isinstance(text.quote(), str)


# Generated at 2022-06-14 00:54:23.560199
# Unit test for method text of class Text
def test_Text_text():
    t = Text()
    text1 = t.text(quantity=1)
    text2 = t.text(quantity=2)
    assert text1 != text2

# Generated at 2022-06-14 00:54:25.529070
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    t = Text()
    x = t.rgb_color()
    assert len(x) == 3
    

# Generated at 2022-06-14 00:54:27.796023
# Unit test for method sentence of class Text
def test_Text_sentence():
    # Arrange
    text = Text()
    # Act
    result = text.sentence()
    # Assert
    assert isinstance(result, str)
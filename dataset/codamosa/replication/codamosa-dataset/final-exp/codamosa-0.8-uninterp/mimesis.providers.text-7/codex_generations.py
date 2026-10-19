

# Generated at 2022-06-14 00:52:07.708786
# Unit test for method level of class Text
def test_Text_level():
    text = Text()
    # Check type of result
    assert isinstance(text.level(), str)


# Generated at 2022-06-14 00:52:10.620775
# Unit test for method quote of class Text
def test_Text_quote():
    text = Text()
    quote = text.quote()
    assert isinstance(quote, str)
    assert len(quote) > 0
    assert quote != text.quote()



# Generated at 2022-06-14 00:52:11.820764
# Unit test for constructor of class Text
def test_Text():
    text = Text()
    assert text is not None


# Generated at 2022-06-14 00:52:14.278668
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    text = Text()
    swear_word = text.swear_word()
    assert swear_word != None
    assert type(swear_word) == str
    # this function is normal case


# Generated at 2022-06-14 00:52:19.474380
# Unit test for method sentence of class Text
def test_Text_sentence():
    print("test_Text_sentence")
    dp = Text(seed=100)

    sentence = dp.sentence()
    print(sentence)
    assert sentence == 'Even though half of the city runs on lasers and micro ' \
                       'chips, the other half still runs on donuts.'


# Generated at 2022-06-14 00:52:20.671719
# Unit test for method quote of class Text
def test_Text_quote():
    text = Text()
    assert text.quote() in text._data['quotes']

# Generated at 2022-06-14 00:52:25.424007
# Unit test for method words of class Text
def test_Text_words():
    for i in range(10):
        assert len(Text().words()) == 5
        assert len(Text().words(2)) == 2
        assert len(Text().words(1)) == 1
        assert len(Text().words(10)) == 10


# Generated at 2022-06-14 00:52:29.332338
# Unit test for method title of class Text
def test_Text_title():
    # Test 1: Test title method when locale is en & ru
    t = Text(locale='en')
    assert t.title() != None
    t = Text(locale='ru')
    assert t.title() != None


# Generated at 2022-06-14 00:52:31.245816
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    # Base
    text = Text()
    assert text.alphabet() == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Generated at 2022-06-14 00:52:33.446793
# Unit test for method words of class Text
def test_Text_words():
    test = Text()
    assert type(test.words()) is list
    assert len(test.words()) == 5



# Generated at 2022-06-14 00:52:12.241186
# Unit test for method word of class Text
def test_Text_word():
    """Unit test for method word of class Text."""
    __text = Text('en')
    assert len(__text.word()) <= 8



# Generated at 2022-06-14 00:52:20.637904
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    # test_Text_hex_color_00
    l = Text(seed=0)
    assert l.hex_color() == '#ee4a4a'
    # test_Text_hex_color_01
    l = Text(seed=1)
    assert l.hex_color() == '#076d2e'
    # test_Text_hex_color_02
    l = Text(seed=2)
    assert l.hex_color() == '#026a38'
    # test_Text_hex_color_safe_00
    l = Text(seed=0)
    assert l.hex_color(safe=True) == '#989898'
    # test_Text_hex_color_safe_01
    l = Text(seed=1)

# Generated at 2022-06-14 00:52:26.485860
# Unit test for method color of class Text
def test_Text_color():
    """Unit test for method color of class Text."""
    t = Text()
    color_1 = t.color()
    assert isinstance(color_1, str)
    assert color_1 == 'Red'
    color_2 = t.color()
    assert isinstance(color_2, str)
    assert color_2 == 'Green'


# Generated at 2022-06-14 00:52:27.516255
# Unit test for method words of class Text
def test_Text_words():
    assert len(Text().words(quantity=5)) == 5


# Generated at 2022-06-14 00:52:30.021389
# Unit test for method quote of class Text
def test_Text_quote():
    t = Text()
    r = t.quote()
    assert r != None

# Generated at 2022-06-14 00:52:31.788226
# Unit test for method text of class Text
def test_Text_text():
    t = Text()
    assert t.text()
    assert t.text(2)

# Generated at 2022-06-14 00:52:33.952943
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    txt = Text()
    hexColor = txt.hex_color()
    assert len(hexColor) == 7


# Generated at 2022-06-14 00:52:39.899410
# Unit test for method quote of class Text
def test_Text_quote():
    print ("testing Text quote()")
    from mimesis.builtins import Text
    text = Text()
    quote = text.quote()
    print (quote)
    #assert quote != None
    #assert True  # TODO: implement your test here


# Generated at 2022-06-14 00:52:49.913099
# Unit test for method title of class Text
def test_Text_title():
    """Test for method title of class Text"""
    rnd = Text()
    results = {}
    size = 10000
    for i in range(size):
        result = rnd.title()
        if result not in results:
            results[result] = 0
        results[result] += 1
    print('\nTest title')
    print(f'Размер выборки: {size}')
    print('-'*10)
    for result in results:
        print(f'Слово "{result}" встретилось {results[result]/size:.2%}')

test_Text_title()

# Generated at 2022-06-14 00:52:53.634354
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    """Unit test method rgb_color of class Text"""
    text = Text()
    rgb = text.rgb_color()
    assert isinstance(rgb, tuple)



# Generated at 2022-06-14 00:53:17.796439
# Unit test for method sentence of class Text
def test_Text_sentence():
    text = Text()
    print(text.sentence())

# Generated at 2022-06-14 00:53:20.249903
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    for i in range(0, 100):
        if (Text().swear_word() in Text()._data['words'].get('bad')):
            continue
        else:
            return False
    return True


# Generated at 2022-06-14 00:53:21.605004
# Unit test for method title of class Text
def test_Text_title():
    t = Text()
    assert len(t.title()) > 0


# Generated at 2022-06-14 00:53:22.851414
# Unit test for method words of class Text
def test_Text_words():
    print()
    text = Text()
    print(text.words())


# Generated at 2022-06-14 00:53:25.916794
# Unit test for method color of class Text
def test_Text_color():
    t = Text()
    print("color(" + t.color() + ")")


# Generated at 2022-06-14 00:53:30.195594
# Unit test for method text of class Text
def test_Text_text():
    from mimesis.builtins import Text
    text = Text()
    t = text.text()
    upp = t.isupper()
    assert not upp


# Generated at 2022-06-14 00:53:32.696811
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    assert Text().rgb_color() == (173, 215, 96)

# Generated at 2022-06-14 00:53:36.087615
# Unit test for method title of class Text
def test_Text_title():
    text_test = Text(seed=1234567890)
    text_test.seed = 1234567890
    res = text_test.title()
    assert res == "on the other side of the"

# Generated at 2022-06-14 00:53:40.207571
# Unit test for method words of class Text
def test_Text_words():
    assert len(Text.words()) == 5
    assert len(Text.words(quantity=10)) == 10
    assert len(Text.words(quantity=0)) == 0
# End of unit test


# Generated at 2022-06-14 00:53:41.600274
# Unit test for method color of class Text
def test_Text_color():
    t = Text()
    color = t.color()
    assert isinstance(color, str)
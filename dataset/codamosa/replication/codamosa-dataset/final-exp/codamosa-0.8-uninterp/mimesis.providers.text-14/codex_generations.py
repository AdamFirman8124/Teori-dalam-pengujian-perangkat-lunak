

# Generated at 2022-06-14 00:52:08.812370
# Unit test for method hex_color of class Text
def test_Text_hex_color():
    t = Text()
    assert t.hex_color()


# Generated at 2022-06-14 00:52:10.575342
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    t = Text()
    assert t.swear_word() == 'damn'

# Generated at 2022-06-14 00:52:12.402813
# Unit test for method word of class Text
def test_Text_word():
    text = Text()
    result = text.word()
    assert result in text._data['words']['normal']


# Generated at 2022-06-14 00:52:19.079707
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    print("\n######################")
    print("Testing method alphabet in class Text")
    print("######################\n")
    txt = Text()
    print(txt.alphabet(lower_case=True))
    print(txt.alphabet(lower_case=False))


# Generated at 2022-06-14 00:52:20.313655
# Unit test for method sentence of class Text
def test_Text_sentence():
    sentence = Text().sentence()
    assert sentence is not None

# Generated at 2022-06-14 00:52:31.977325
# Unit test for constructor of class Text
def test_Text():
    text = Text()
    result = text.alphabet()
    assert type(result) is list
    assert len(result) == 26
    result = text.alphabet(True)
    assert type(result) is list
    assert len(result) == 26
    result = text.level()
    assert type(result) is str
    result = text.text()
    assert type(result) is str
    result = text.title()
    assert type(result) is str
    result = text.words()
    assert type(result) is list
    result = text.word()
    assert type(result) is str
    result = text.swear_word()
    assert type(result) is str
    result = text.quote()
    assert type(result) is str
    result = text.color()

# Generated at 2022-06-14 00:52:33.080400
# Unit test for method title of class Text
def test_Text_title():
    n = Text()
    print(n.title())

# Generated at 2022-06-14 00:52:34.599969
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    assert Text().rgb_color() in [(252, 85, 32), (216, 53, 107)]

# Generated at 2022-06-14 00:52:38.072965
# Unit test for method word of class Text
def test_Text_word():
    from mimesis.text import Text
    word = Text('en').word()
    print(word)
    assert len(word) > 0

# Generated at 2022-06-14 00:52:40.241077
# Unit test for method color of class Text
def test_Text_color():
    text = Text()
    answer = text.color()
    assert isinstance(answer, str)


# Generated at 2022-06-14 00:52:56.953372
# Unit test for method swear_word of class Text
def test_Text_swear_word():
    from mimesis.enums import Language
    # Init provider
    prov = Text(Language.ENGLISH)
    # Check
    assert prov.swear_word() in ['damn', 'fuck', 'shit', 'ass']

# Generated at 2022-06-14 00:52:59.322912
# Unit test for method rgb_color of class Text
def test_Text_rgb_color():
    t = Text()
    color = t.rgb_color(safe=True)
    assert color in SAFE_COLORS



# Generated at 2022-06-14 00:53:01.956291
# Unit test for method title of class Text
def test_Text_title():
    cls = Text()
    pattern = r'\w{1,10}'
    assert re.match(pattern, cls.title())

# Generated at 2022-06-14 00:53:03.945509
# Unit test for method alphabet of class Text
def test_Text_alphabet():
    """Unit test for method alphabet of class Text."""
    text = Text()
    list = text.alphabet()
    assert len(list) == 26
    list = text.alphabet(lower_case=True)
    assert len(list) == 26


# Generated at 2022-06-14 00:53:05.940306
# Unit test for method level of class Text
def test_Text_level():
    text = Text('zh')
    res = text.level()
    assert isinstance(res, str)

# Generated at 2022-06-14 00:53:10.123952
# Unit test for method color of class Text
def test_Text_color():
    color = Text().color()
    assert len(color.split()) == 1
    assert isinstance(color, str)


# Generated at 2022-06-14 00:53:11.311052
# Unit test for method word of class Text
def test_Text_word():
    a = Text()
    assert(len(a.word()) > 0)

# Generated at 2022-06-14 00:53:12.949178
# Unit test for method text of class Text
def test_Text_text():
    text = Text()

    print(text.text())
    print(text.text())
    print(text.text())


# Generated at 2022-06-14 00:53:17.141844
# Unit test for method sentence of class Text
def test_Text_sentence():
    from mimesis.enums import Gender
    text = Text('en-US', seed=456)
    for _ in range(10):
        sentence = text.sentence()
        assert sentence is not None
        assert len(sentence)
        assert isinstance(sentence, str)

# Generated at 2022-06-14 00:53:18.650324
# Unit test for method text of class Text
def test_Text_text():
    """Unit test for method text of class Text"""
    text = Text(seed=123123123)
    x = text.text()
    assert x == 'Project libraries, forums, and blogs.'
    assert type(x) is str

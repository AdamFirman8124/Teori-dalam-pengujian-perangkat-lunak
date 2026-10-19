

# Generated at 2022-06-14 12:05:21.933449
# Unit test for function linkify
def test_linkify():
    assert '<a href="http://www.example.com/">www.example.com</a>' == linkify('www.example.com')
test_linkify()

# Generated at 2022-06-14 12:05:24.706474
# Unit test for function url_unescape
def test_url_unescape():
    url_unescape("ciao")
    url_unescape(b"ciao")
    url_unescape("ciao", encoding="utf-8")



# Generated at 2022-06-14 12:05:31.209001
# Unit test for function utf8
def test_utf8():
    assert utf8("foobar") == b"foobar"
    assert utf8(b"foobar") == b"foobar"
    assert utf8(u"foobar") == b"foobar"


_TO_UNICODE_TYPES = (unicode_type, type(None))

if not isinstance(b"", unicode_type):

    @typing.overload
    def to_unicode(value: str) -> unicode_type:
        ...



# Generated at 2022-06-14 12:05:35.272349
# Unit test for function url_unescape
def test_url_unescape():
    assert url_unescape(b'%3F') == b'?'
    assert url_unescape(b'%3F', encoding='ascii') == '?'



# Generated at 2022-06-14 12:05:38.145264
# Unit test for function linkify
def test_linkify():
    assert linkify('foo') == 'foo'
    assert linkify('http://example.com') == '<a href="http://example.com">http://example.com</a>'

# Generated at 2022-06-14 12:05:47.272799
# Unit test for function utf8
def test_utf8():
    def assert_utf8(value, expected_result, encoding='utf-8'):
        assert utf8(value) == expected_result
    assert_utf8(b"ascii", b"ascii")
    assert_utf8(u"Iñtërnâtiôn\xe4lizætiøn", b"I\xc3\xb1t\xc3\xbbrn\xc3\xa2ti\xc3\xb4n\xc3\xa4liz\xc3\xa6ti\xc3\xb8n")
    assert_utf8(None, None)
    try:
        utf8(42)
        assert False
    except TypeError:
        pass


_TO_UNICODE_TYPES = (unicode_type, type(None))



# Generated at 2022-06-14 12:06:01.027682
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""
    assert linkify("a") == "a"
    assert linkify("a b") == "a b"
    assert linkify("a b http://example.com") == 'a b <a href="http://example.com">http://example.com</a>'
    assert linkify("a b http://example.com c") == 'a b <a href="http://example.com">http://example.com</a> c'

    assert linkify("a www.example.com b") == 'a <a href="http://www.example.com">www.example.com</a> b'

# Generated at 2022-06-14 12:06:12.351449
# Unit test for function utf8
def test_utf8():
    assert(utf8("a") == "a")
    assert(utf8("あ") == "あ")
    assert(utf8("aあ") == "aあ")
    assert(utf8("あa") == "あa")
    assert(utf8("aあa") == "aあa")
    assert(utf8("あaあ") == "あaあ")


_TO_UNICODE_TYPES = (unicode_type, type(None))



# Generated at 2022-06-14 12:06:16.129282
# Unit test for function linkify
def test_linkify():
    s = "Hello http://tornadoweb.org/, http://example.org/"
    s = linkify(s, shorten=True)
    assert (s == (
        'Hello <a href="http://tornadoweb.org/" title="http://tornadoweb.org/">'
        'http://tornadoweb.org/</a>, '
        '<a href="http://example.org/" title="http://example.org/">'
        'http://example.org/</a>'
    )), "%r != %r" % (s, _test_linkify_result)



# Generated at 2022-06-14 12:06:26.291306
# Unit test for function linkify
def test_linkify():
    output = linkify("Hello http://tornadoweb.org!")
    assert output == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    output = linkify("Hello https://www.youtube.com/watch?v=oHg5SJYRHA0&list=RDsbZ6dA1YNDw&index=2! This is a crazy link", shorten=True)

# Generated at 2022-06-14 12:06:43.217800
# Unit test for function linkify
def test_linkify():
    assert linkify('http://www.tornadoweb.org') == '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>' 
    assert linkify('http://www.tornadoweb.org/') == '<a href="http://www.tornadoweb.org/">http://www.tornadoweb.org/</a>'

# Generated at 2022-06-14 12:06:47.757929
# Unit test for function url_unescape
def test_url_unescape():
    url_unescape('utf-8')
    url_unescape('utf-8', plus=False)
    url_unescape('', encoding='utf-8')
    url_unescape('', encoding='utf-8', plus=False)
    url_unescape(b'')
    url_unescape(b'', plus=False)



# Generated at 2022-06-14 12:07:00.146038
# Unit test for function linkify
def test_linkify():
    assert(linkify("Hello http://tornadoweb.org!") == 
           "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
    assert(linkify("Hello http://tornadoweb.org!", shorten = True) == 
          "Hello <a href=\"http://tornadoweb.org\" title=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
    assert(linkify("Hello http://tornadoweb.org!", shorten = True, extra_params = "class = \"foo\"") == 
          "Hello <a href=\"http://tornadoweb.org\" class = \"foo\" title=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
    # test_linkify_callback

# Generated at 2022-06-14 12:07:11.064711
# Unit test for function linkify
def test_linkify():
    """A function to test function linkify"""
    assert linkify("http://www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'
    assert linkify("www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    assert linkify("Hello http://www.tornadoweb.org") == 'Hello <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'
    assert linkify("Hello www.tornadoweb.org") == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'

# Generated at 2022-06-14 12:07:15.567356
# Unit test for function linkify
def test_linkify():
    assert linkify(r"www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify(r"http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify(r"http://www.example.com/foo/bar?a=b&c=d") == '<a href="http://www.example.com/foo/bar?a=b&c=d">http://www.example.com/foo/bar?a=b&c=d</a>'

# Generated at 2022-06-14 12:07:16.655089
# Unit test for function url_unescape
def test_url_unescape():
    url_unescape("test")
    url_unescape("test", encoding=None)
    url_unescape("test", plus=True)
    url_unescape("test", encoding=None, plus=True)


# Generated at 2022-06-14 12:07:25.395916
# Unit test for function linkify
def test_linkify():
    assert (
        linkify(
            "Hello http://tornadoweb.org!",
            extra_params='rel="nofollow" class="external"',
            permitted_protocols=["http", "https"],
        )
        == 'Hello <a href="http://tornadoweb.org" rel="nofollow" class="external">http://tornadoweb.org</a>!'
    )

    assert (
        linkify(
            "Hello http://tornadoweb.org!",
            extra_params="rel='nofollow' class='external'",
            permitted_protocols=["http", "https"],
        )
        == 'Hello <a href="http://tornadoweb.org" rel=\'nofollow\' class=\'external\'>http://tornadoweb.org</a>!'
    )


# Generated at 2022-06-14 12:07:29.874165
# Unit test for function linkify
def test_linkify():
    text = """Hello https://github.com!"""
    print(linkify(text))

test_linkify()

# from https://github.com/openresty/lua-nginx-module#ngxstringbytelength

# Generated at 2022-06-14 12:07:39.842404
# Unit test for function linkify
def test_linkify():
    assert linkify('') == ''
    assert linkify('Hello World!') == 'Hello World!'
    assert linkify('<b>Hello World!</b>') == '&lt;b&gt;Hello World!&lt;/b&gt;'

    assert linkify('Go to http://www.example.com') == \
            'Go to <a href="http://www.example.com">http://www.example.com</a>'
    assert linkify('Go to www.example.com') == \
            'Go to <a href="http://www.example.com">www.example.com</a>'

# Generated at 2022-06-14 12:07:51.639081
# Unit test for function linkify
def test_linkify():
    assert(linkify(""), "")
    assert(linkify("without protocol"), "without protocol")
    assert(linkify("without protocol", require_protocol=True), "without protocol")
    assert(linkify("with http://protocol.com"), 'with <a href="http://protocol.com">http://protocol.com</a>')
    assert(
        linkify("with http://protocol.com", require_protocol=True),
        'with <a href="http://protocol.com">http://protocol.com</a>'
    )
    assert(
        linkify("with www.protocol.com", require_protocol=True),
        "with www.protocol.com"
    )

# Generated at 2022-06-14 12:08:23.708140
# Unit test for function linkify
def test_linkify():
    text = "www.google.com"
    assert(linkify(text) == u'<a href="http://www.google.com">www.google.com</a>')

test_linkify()

# Generated at 2022-06-14 12:08:34.463288
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com") == '<a href="http://foo.com">http://foo.com</a>'
    assert linkify("foo.com") == '<a href="http://foo.com">foo.com</a>'
    assert linkify("<foo.com>") == '<a href="http://foo.com">&lt;foo.com&gt;</a>'
    assert linkify("no link") == "no link"
    assert linkify("http://foo.com/a?b=c") == '<a href="http://foo.com/a?b=c">http://foo.com/a?b=c</a>'

# Generated at 2022-06-14 12:08:36.787364
# Unit test for function linkify
def test_linkify():
    assert linkify('hello world') == 'hello world'
    assert linkify('hello http://www.google.com') == u'hello <a href="http://www.google.com">http://www.google.com</a>'


# Generated at 2022-06-14 12:08:41.653710
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org! www.google.com"
    print(linkify(text))
    text = "Hello http://tornadoweb.org! www.google.com"
    print(linkify(text, shorten=True))

# Generated at 2022-06-14 12:08:52.001596
# Unit test for function linkify
def test_linkify():
    # Using a plain string as input
    assert linkify("Hello World, visit http://www.tornadoweb.org/en/stable/") == \
        'Hello World, visit <a href="http://www.tornadoweb.org/en/stable/">http://www.tornadoweb.org/en/stable/</a>'
    # Using bytes as input
    assert linkify(b"Hello World, visit http://www.tornadoweb.org/en/stable/") == \
        'Hello World, visit <a href="http://www.tornadoweb.org/en/stable/">http://www.tornadoweb.org/en/stable/</a>'
    # Using unicode as input

# Generated at 2022-06-14 12:08:53.213201
# Unit test for function linkify
def test_linkify():
    import doctest
    doctest.testmod(linkify)

# Generated at 2022-06-14 12:09:02.327171
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    extra_params = "target='_blank'"
    require_protocol = False
    permitted_protocols = ["http", "https"]
    result = linkify(
        text,
        shorten=False,
        extra_params=extra_params,
        require_protocol=require_protocol,
        permitted_protocols=permitted_protocols,
    )
    print(result)


if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:09:10.136913
# Unit test for function linkify
def test_linkify():
    print('test_linkify')
    # Test cases from the original Ruby version

# Generated at 2022-06-14 12:09:18.719573
# Unit test for function linkify
def test_linkify():
    _URL_RE = re.compile(
        to_unicode(
            r"""\b((?:([\w-]+):(/{1,3})|www[.])(?:(?:(?:[^\s&()]|&amp;|&quot;)*(?:[^!"#$%&'()*+,.:;<=>?@\[\]^`{|}~\s]))|(?:\((?:[^\s&()]|&amp;|&quot;)*\)))+)"""  # noqa: E501
        )
    )
    text = linkify("Hello http://tornadoweb.org!")
    assert text == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    text = linkify("www.facebook.com")


# Generated at 2022-06-14 12:09:26.671796
# Unit test for function linkify
def test_linkify():
    r = linkify(
        "The Tornado project: http://www.tornadoweb.org"
    )
    assert r == 'The Tornado project: <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'
    r = linkify(
        "The Tornado project: http://www.tornadoweb.org",
        extra_params='rel="foo"',
    )
    assert r == 'The Tornado project: <a href="http://www.tornadoweb.org" rel="foo">http://www.tornadoweb.org</a>'

# Generated at 2022-06-14 12:09:47.137348
# Unit test for function linkify
def test_linkify():  
    URI_REGEX_STRING = r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))'''
    URI_REGEX = re.compile(URI_REGEX_STRING)

# Generated at 2022-06-14 12:09:56.555430
# Unit test for function linkify
def test_linkify():
    text = "http://www.baidu.com/hello.html"
    href = linkify(text)
    print(href)
    assert href == '<a href="http://www.baidu.com/hello.html">http://www.baidu.com/hello.html</a>'

if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:10:06.922158
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://www.google.com!'
    assert linkify(text) == u'Hello <a href=\"http://www.google.com\">http://www.google.com</a>!'
    assert linkify(text, shorten=True) == 'Hello <a href="http://www.google.com">http://www.google.com</a>!'
    assert linkify(text, extra_params='') == u'Hello <a href=\"http://www.google.com\">http://www.google.com</a>!'
    assert linkify(text, require_protocol=False) == u'Hello <a href=\"http://www.google.com\">www.google.com</a>!'

# Generated at 2022-06-14 12:10:15.345029
# Unit test for function linkify
def test_linkify():
    assert linkify('I love @tornadoweb') == 'I love @tornadoweb'
    assert linkify('@tornadoweb is the tornado\'s weibo') == '@tornadoweb is the tornado\'s weibo'
    text = 'linkify should not http://t.cn/RUv7LPx touch urls in attributes'
    assert linkify(text) == text
    text = 'linkify should correctly handle strange characters'
    assert linkify(text) == text
    assert linkify('@tornadoweb is the tornado\'s weibo') 
assert linkify('I love @tornadoweb') == 'I love @tornadoweb'
assert linkify('@tornadoweb is the tornado\'s weibo') == '@tornadoweb is the tornado\'s weibo'

# Generated at 2022-06-14 12:10:19.078798
# Unit test for function linkify
def test_linkify():
    """Unit test"""
    assert linkify("http://example.com/hello_world") == '<a href="http://example.com/hello_world">http://example.com/hello_world</a>'


# Generated at 2022-06-14 12:10:28.334274
# Unit test for function linkify
def test_linkify():
    assert (
        linkify("http://www.google.com")
        == '<a href="http://www.google.com">http://www.google.com</a>'
    )
    assert (
        linkify("www.google.com")
        == '<a href="http://www.google.com">www.google.com</a>'
    )
    assert (
        linkify("http://www.google.com.", True)
        == '<a href="http://www.google.com" title="http://www.google.com">http://www.google.com...</a>'  # noqa: E501
    )
    assert linkify("http://www.google.com.", False) == "http://www.google.com."

# Generated at 2022-06-14 12:10:39.961264
# Unit test for function linkify
def test_linkify():
    assert linkify('linkify "http://www.google.com"') == 'linkify <a href="http://www.google.com">http://www.google.com</a>'
    assert linkify('linkify "http://www.google.com:1234"') == 'linkify <a href="http://www.google.com:1234">http://www.google.com:1234</a>'
    assert linkify('linkify "http://www.google.com:1234/a/b/c"') == 'linkify <a href="http://www.google.com:1234/a/b/c">http://www.google.com:1234/a/b/c</a>'

# Generated at 2022-06-14 12:10:50.436013
# Unit test for function linkify
def test_linkify():
    # Check conversion
    text = b"Hello http://tornadoweb.org!"
    result = linkify(text)
    assert(result == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!')

    # Check protocol
    text = b"Hello www.tornadoweb.org!"
    result = linkify(text)
    assert(result == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!')

    # Check protocol and policy
    text = b"Hello https://tornadoweb.org!"
    result = linkify(text,require_protocol=True,permitted_protocols=["https"])

# Generated at 2022-06-14 12:10:57.042834
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))

#test_linkify()



# Generated at 2022-06-14 12:11:03.417093
# Unit test for function linkify
def test_linkify():
    #test_linkify
    print(linkify("Hello http://tornadoweb.org!"))
    #test_linkify
    print(linkify("Hello www.tornadoweb.org!"))
    #test_linkify
    print(linkify("Hello http://tornadoweb.org!", shortten=True))
    #test_linkify
    print(linkify("Hello www.tornadoweb.org!", require_protocol=True))
    #test_linkify
    print(linkify("Hello http://tornadoweb.org!", permitted_protocols=["http"]))
    #test_linkify
    print(linkify("Hello https://tornadoweb.org!", permitted_protocols=["http"]))
    #test_linkify

# Generated at 2022-06-14 12:11:27.921379
# Unit test for function linkify
def test_linkify():
    text = "Hello http://example.com! It is http://www.example.com/ ."
    result = "Hello <a href=\"http://example.com\">http://example.com</a>! It is <a href=\"http://www.example.com/\">http://www.example.com/</a> ."
    assert linkify(text) == result


# Inlined from urlparse for compatibility with Python < 2.5
# See http://hg.python.org/cpython/file/7b3f355086da/Lib/urlparse.py#l106
# Avoid using regex's for simplicity and to allow for future changes

# Generated at 2022-06-14 12:11:31.242783
# Unit test for function linkify
def test_linkify():
    a='http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=218.4.255.255'
    a=linkify('Hello http://tornadoweb.org!')
    print(a)


# Generated at 2022-06-14 12:11:41.765906
# Unit test for function linkify
def test_linkify():
    """
    Testing some conditions exist in linkify
    """
    expected = '<a href="http://www.google.com" >www.google.com</a>'
    url = 'www.google.com'
    result = linkify(url)
    assert result == expected, "Wrong"


# Generated at 2022-06-14 12:11:50.047626
# Unit test for function linkify
def test_linkify():
    assert(linkify("www.Yahoo.com") == '<a href="http://www.Yahoo.com">www.Yahoo.com</a>')
    assert(linkify("Hello! http://google.com") == 'Hello! <a href="http://google.com">http://google.com</a>')
    assert(linkify("Hello! www.google.com") == 'Hello! <a href="http://www.google.com">www.google.com</a>')
    assert(linkify("http://google.com - Websites") == '<a href="http://google.com">http://google.com</a> - Websites')
    assert(linkify("Hello! http://google.com World!") == 'Hello! <a href="http://google.com">http://google.com</a> World!')


# Generated at 2022-06-14 12:11:59.548056
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""
    assert linkify("foo bar") == "foo bar"
    assert linkify("foo bar http://www.facebook.com") == 'foo bar <a href="http://www.facebook.com">http://www.facebook.com</a>'
    assert linkify("http://www.facebook.com/foo") == '<a href="http://www.facebook.com/foo">http://www.facebook.com/foo</a>'
    assert linkify("foo bar https://www.facebook.com/foo") == 'foo bar <a href="https://www.facebook.com/foo">https://www.facebook.com/foo</a>'

# Generated at 2022-06-14 12:12:09.526797
# Unit test for function linkify
def test_linkify():
    """
    assert(
        linkify("http://www.t.com") ==
        u'<a href="http://www.t.com">http://www.t.com</a>'
    )
    """
    assert(
        linkify("http://www.t.com") ==
        '<a href="http://www.t.com">http://www.t.com</a>'
    )


# Generated at 2022-06-14 12:12:14.099358
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello https://tornadoweb.org!"))
    print(linkify("Hello http://twitter.com/tornado_zhtw!"))
    print(linkify("Hello http://www.google.com!"))
    print(linkify("Hello www.facebook.com!"))


# Generated at 2022-06-14 12:12:25.672277
# Unit test for function linkify
def test_linkify():
    data = [
        ("Hello http://tornadoweb.org!",
         "Hello <a href=\"http://tornadoweb.org\" "
                     ">http://tornadoweb.org</a>!"),
        ("Hello http://tornadoweb.org/?x=&y=",
         "Hello <a href=\"http://tornadoweb.org/\" "
                     ">http://tornadoweb.org/</a>?"
                     "x=&amp;y="),
        ("www.facebook.com", "www.facebook.com"),
    ]
    for test, expected in data:
        result = linkify(test)
        print(result)
        assert result == expected

test_linkify()

# Generated at 2022-06-14 12:12:29.023885
# Unit test for function linkify
def test_linkify():
    test_text = "Hello http://tornadoweb.org!"
    test_link = linkify(test_text)
    test_link = "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"


# Generated at 2022-06-14 12:12:41.057122
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.facebook.com/") == '<a href="http://www.facebook.com/">http://www.facebook.com/</a>'
    assert linkify("www.facebook.com/") == '<a href="http://www.facebook.com/">www.facebook.com/</a>'
    assert linkify("http://www.facebook.com/", require_protocol=True) == '<a href="http://www.facebook.com/">http://www.facebook.com/</a>'
    assert linkify("http://www.facebook.com/", require_protocol=False) == '<a href="http://www.facebook.com/">http://www.facebook.com/</a>'

# Generated at 2022-06-14 12:13:19.994803
# Unit test for function linkify

# Generated at 2022-06-14 12:13:32.832735
# Unit test for function linkify
def test_linkify():
    assert linkify('http://example.com') == '<a href="http://example.com">http://example.com</a>'
    assert linkify('http://example.com/') == '<a href="http://example.com/">http://example.com/</a>'
    assert linkify('http://example.com:5000') == '<a href="http://example.com:5000">http://example.com:5000</a>'
    assert linkify('Hello http://tornadoweb.org!') == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify('Hello <http://tornadoweb.org>!') == 'Hello &lt;<a href="http://tornadoweb.org">http://tornadoweb.org</a>&gt;!'

# Generated at 2022-06-14 12:13:43.784923
# Unit test for function linkify
def test_linkify():
    format_urls = (
    "Please visit http://example.com/",
    "Please visit http://www.example.com/",
    "Please visit www.example.com/",
    "Please visit www.example.com:8000/foo/bar",
    "Please visit rd.example.com/c?rid=521&amp;cid=1002",
    "Please visit example.com/foo.php?bar=baz&quot;&gt;&lt;script&gt;alert&#40;'hax'&#41;;&lt;/script&gt;",
    )


# Generated at 2022-06-14 12:13:52.845253
# Unit test for function linkify
def test_linkify():
    assert linkify('http://www.tornadoweb.org/') == '<a href="http://www.tornadoweb.org/">http://www.tornadoweb.org/</a>'
    assert linkify('https://www.tornadoweb.org/') == '<a href="https://www.tornadoweb.org/">https://www.tornadoweb.org/</a>'
    assert linkify('http://www.tornadoweb.org/', shorten=True) == '<a href="http://www.tornadoweb.org/">http://www.tornadoweb.org/</a>'

# Generated at 2022-06-14 12:13:57.161574
# Unit test for function linkify
def test_linkify():
    s=linkify('Hello http://www.baidu.com, https://www.baidu.com, and ftp://www.baidu.com')
    print(s)
# test_linkify()

QUOTES_RE = re.compile(r"&#39;|&quot;")



# Generated at 2022-06-14 12:14:03.939330
# Unit test for function linkify
def test_linkify():
    assert linkify('hello http://tornadoweb.org') == 'hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    assert linkify('hello http://tornadoweb.org, ok') == 'hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>, ok'
test_linkify()

import decimal
import math
import sys



# Generated at 2022-06-14 12:14:06.058646
# Unit test for function linkify
def test_linkify():
    text = "http://storm.apache.org http://www.baudi.com/"
    print(linkify(text))



# Generated at 2022-06-14 12:14:17.571436
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""
    assert linkify("hello") == "hello"
    assert linkify("hello http://www.world.com") == 'hello <a href="http://www.world.com">http://www.world.com</a>'
    assert linkify("hello http://www.world.com hello") == 'hello <a href="http://www.world.com">http://www.world.com</a> hello' # noqa

# Generated at 2022-06-14 12:14:26.402620
# Unit test for function linkify
def test_linkify():
    text = ("https://en.wikipedia.org/wiki/%E4%B8%AD%E6%96%87_(%E8%A8%80%E8%99%9F) "
            "Hello http://tornadoweb.org!")

# Generated at 2022-06-14 12:14:41.418071
# Unit test for function linkify
def test_linkify():
    test_string = '<script> hola </script>'
    assert(linkify(test_string) == '&lt;script&gt; hola &lt;/script&gt;')

    test_string = 'www.google.com'
    assert(linkify(test_string) == u'<a href="http://www.google.com">www.google.com</a>')

    test_string = 'http://www.google.com'
    assert(linkify(test_string) == u'<a href="http://www.google.com">http://www.google.com</a>')

    test_string = 'http://www.google.com'
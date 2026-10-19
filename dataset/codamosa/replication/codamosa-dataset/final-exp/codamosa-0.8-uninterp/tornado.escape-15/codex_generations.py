

# Generated at 2022-06-14 12:05:19.061426
# Unit test for function linkify
def test_linkify():
    text = "Hello https://tornadoweb.org! www.example.com www.example.com"
    print(linkify(text))

test_linkify()

#Unit test for function json_encode

# Generated at 2022-06-14 12:05:25.601811
# Unit test for function linkify
def test_linkify():
   assert linkify('i like this photo http://example.com/p/123') == 'i like this photo <a href="http://example.com/p/123">http://example.com/p/123</a>'
   assert linkify('i like this photo http://example.com/p/123 this is the end') == 'i like this photo <a href="http://example.com/p/123">http://example.com/p/123</a> this is the end'

# Generated at 2022-06-14 12:05:33.492633
# Unit test for function linkify
def test_linkify():
    assert linkify("www.example.com") == 'www.example.com'
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("https://example.com") == '<a href="https://example.com">https://example.com</a>'
    assert linkify("mailto:foo@example.com") == 'mailto:foo@example.com'
    assert linkify("user@host") == 'user@host'
    assert linkify("https://github.com/tornadoweb/tornado") == '<a href="https://github.com/tornadoweb/tornado">https://github.com/tornadoweb/tornado</a>'
    assert linkify("(http://foo)")

# Generated at 2022-06-14 12:05:37.475146
# Unit test for function linkify
def test_linkify():
    if not linkify("http://www.baidu.com"):
        print("succeed")
    else:
        print("failed")


_MULTIPLE_SPACES = re.compile(r"\ {2,}")



# Generated at 2022-06-14 12:05:46.888734
# Unit test for function linkify
def test_linkify():
    def check(text, expected):
        actual = linkify(text, extra_params='class="foo"')
        assert actual == expected, (
            "linkify(%r) == %r != %r" % (text, actual, expected))

    check(
        'hello http://tornadoweb.org',
        'hello <a href="http://tornadoweb.org" class="foo">http://tornadoweb.org</a>'
    )
    check('http://invalid domain', 'http://invalid domain')
    check('http://exam-ple.com', 'http://exam-ple.com')
    check('www.example.com', '<a href="http://www.example.com" class="foo">www.example.com</a>')

# Generated at 2022-06-14 12:06:01.037326
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""
    assert linkify("Hello") == "Hello"
    assert linkify("Hello www.google.com") == """Hello <a href="http://www.google.com">www.google.com</a>"""
    assert linkify("Check out http://www.tornadoweb.org/") == """Check out <a href="http://www.tornadoweb.org/">http://www.tornadoweb.org/</a>"""
    assert linkify("http://www.tornadoweb.org/ is awesome") == """<a href="http://www.tornadoweb.org/">http://www.tornadoweb.org/</a> is awesome"""

# Generated at 2022-06-14 12:06:19.396380
# Unit test for function linkify

# Generated at 2022-06-14 12:06:28.101797
# Unit test for function linkify
def test_linkify():
    def assert_identical(text):
        assert text == linkify(text)

    assert_identical("hello")  # doesn't blow up
    assert_identical("hello http://world")

    assert linkify("hello http://world") == (
        u'hello <a href="http://world">http://world</a>'
    )
    # valid url with trailing punctuation
    assert linkify("hello http://world.") == (
        u'hello <a href="http://world">http://world</a>.'
    )
    # link without a protocol
    assert linkify("hello www.world.com") == (
        u'hello <a href="http://www.world.com">www.world.com</a>'
    )
    # link with a protocol

# Generated at 2022-06-14 12:06:41.244889
# Unit test for function utf8
def test_utf8():
    assert utf8(None) is None
    assert utf8("") == b""
    assert utf8(b"") == b""
    assert utf8("Hello World") == b"Hello World"
    assert utf8(u"Hello World") == b"Hello World"
    assert utf8(u"") == b""
    assert utf8(u"\u3042") == b"\xe3\x81\x82"
    assert utf8(u"A\u3042\u3044") == b"A\xe3\x81\x82\xe3\x81\x84"


_TO_UNICODE_TYPES = (unicode_type, type(None))



# Generated at 2022-06-14 12:06:48.101197
# Unit test for function linkify
def test_linkify():
    assert linkify('http://google.com').__eq__(
        '<a href="http://google.com">http://google.com</a>')
    assert linkify('www.google.com').__eq__(
        '<a href="http://www.google.com">www.google.com</a>')
    assert linkify('google.com').__eq__(
        '<a href="http://google.com">google.com</a>')
    assert linkify('<p>http://google.com</p>').__eq__(
        '<p><a href="http://google.com">http://google.com</a></p>')

# Generated at 2022-06-14 12:07:15.545638
# Unit test for function recursive_unicode
def test_recursive_unicode():
    assert recursive_unicode(b"1") == "1"
    assert recursive_unicode(["1", "2"]) == ["1", "2"]
    assert recursive_unicode((b"1", "2")) == ("1", "2")
    assert recursive_unicode({"1": "2"}) == {"1": "2"}
    assert recursive_unicode({"1": {"3": [b"4", {"5": "6"}]}}) == \
        {"1": {"3": ["4", {"5": "6"}]}}



# Generated at 2022-06-14 12:07:24.599706
# Unit test for function recursive_unicode
def test_recursive_unicode():
    def assertIsUnicode(obj):
        assert isinstance(obj, str)
        assert not isinstance(obj, bytes)

    assertIsUnicode(recursive_unicode(u"foo"))
    assertIsUnicode(recursive_unicode("foo"))
    assertIsUnicode(recursive_unicode(b"foo"))
    assertIsUnicode(recursive_unicode({"k1": u"v1", "k2": "v2"}))
    assertIsUnicode(recursive_unicode(["k1", "k2"]))
    assertIsUnicode(recursive_unicode((u"k1", "k2")))

# join_url was copied from six.moves
# The fact that they can be either str or bytes is an implementation detail.
# Please see https://github

# Generated at 2022-06-14 12:07:35.880689
# Unit test for function linkify

# Generated at 2022-06-14 12:07:48.090097
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com").startswith("<a href=")
    assert linkify("http://foo.com") == '<a href="http://foo.com">http://foo.com</a>'
    assert linkify("foo@example.com") == '<a href="mailto:foo@example.com">foo@example.com</a>'
    assert linkify("http://example.com/some/path?foo=bar&baz=raz") == '<a href="http://example.com/some/path?foo=bar&amp;baz=raz">http://example.com/some/path?foo=bar&amp;baz=r...</a>'

# Generated at 2022-06-14 12:07:52.992790
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("http://www.example.com/foo/bar") == '<a href="http://www.example.com/foo/bar">http://www.example.com/foo/bar</a>'
    assert linkify("http://www.example.com/foo/bar/") == '<a href="http://www.example.com/foo/bar/">http://www.example.com/foo/bar/</a>'
    assert linkify("https://www.example.com/foo/") == '<a href="https://www.example.com/foo/">https://www.example.com/foo/</a>'

# Generated at 2022-06-14 12:08:03.709766
# Unit test for function linkify
def test_linkify():
    """Unit test for linkify()"""

# Generated at 2022-06-14 12:08:11.007512
# Unit test for function url_unescape
def test_url_unescape():
    assert url_unescape(b"http%3A%2F%2Fwww.tornadoweb.org%2F") == "http://www.tornadoweb.org/"
    assert url_unescape(b"http%3A%2F%2Fwww.tornadoweb.org%2F", encoding="ascii") == "http://www.tornadoweb.org/"
    assert url_unescape(b"%E2%98%83", encoding="utf-8") == "☃"
    assert url_unescape(b"%E2%98%83", encoding="ascii") == "%E2%98%83"
    try:
        url_unescape(b"%E2%98%83")
        assert False  # This shouldn't happen
    except UnicodeDecodeError:
        pass
    assert url

# Generated at 2022-06-14 12:08:19.935970
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("hello http://example.com") == 'hello <a href="http://example.com">http://example.com</a>'
    assert linkify("hello http://example.com, how are you") == 'hello <a href="http://example.com">http://example.com</a>, how are you'
    assert linkify("go to http://example.com") == 'go to <a href="http://example.com">http://example.com</a>'

# Generated at 2022-06-14 12:08:23.209122
# Unit test for function recursive_unicode
def test_recursive_unicode():
    assert recursive_unicode({"a": 1, "b": b"1"}) == {"a": 1, "b": "1"}
    assert recursive_unicode([1, b"123"]) == [1, "123"]
    assert recursive_unicode((1, b"123")) == (1, "123")



# Generated at 2022-06-14 12:08:34.078972
# Unit test for function linkify

# Generated at 2022-06-14 12:08:56.104649
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com")== '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("Hello http://www.example.com")== 'Hello <a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("www.example.com")== '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("http://example.com")== '<a href="http://example.com">http://example.com</a>'
    assert linkify("https://example.com")== '<a href="https://example.com">https://example.com</a>'

# Generated at 2022-06-14 12:09:06.989627
# Unit test for function linkify

# Generated at 2022-06-14 12:09:17.729423
# Unit test for function url_unescape
def test_url_unescape():
    assert url_unescape(b'Hello%20World') == 'Hello World'
    assert url_unescape(b'Hello+World') == 'Hello World'
    assert url_unescape(b'Hello+World', plus = False) == 'Hello+World'
    assert url_unescape(b'Hello%20World', plus = False) == 'Hello%20World'

    assert url_unescape('Hello%20World') == 'Hello World'
    assert url_unescape('Hello+World') == 'Hello World'
    assert url_unescape('Hello+World', plus = False) == 'Hello+World'
    assert url_unescape('Hello%20World', plus = False) == 'Hello%20World'
    assert url_unescape('Hello%20World', encoding = None) == b'Hello World'
    assert url_unescape

# Generated at 2022-06-14 12:09:29.616086
# Unit test for function url_unescape
def test_url_unescape():
    url_unescape("%61")
    url_unescape("a", encoding=None)


# When dealing with the standard library across python 2 and 3 it is
# sometimes useful to have a direct conversion to the native string type
if str is unicode_type:

    def native_str(s, encoding="ascii"):
        # type: (Union[str, bytes], str) -> str
        if isinstance(s, str):
            return s
        assert isinstance(s, bytes)
        return s.decode(encoding, "replace")
else:

    def native_str(s, encoding="ascii"):
        # type: (Union[str, bytes], str) -> bytes
        if isinstance(s, bytes):
            return s
        assert isinstance(s, str)

# Generated at 2022-06-14 12:09:39.863673
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert linkify("") == ""
    assert linkify("foo bar") == "foo bar"
    assert linkify(u"foo bar") == "foo bar"
    assert linkify(42) == "42"

# Generated at 2022-06-14 12:09:44.440467
# Unit test for function url_unescape
def test_url_unescape():
    assert url_unescape(b"%3F", "utf-8") == "?"
    assert url_unescape(b"%3F", None) == b"?"
    assert url_unescape(b"%3F", "ascii") == "?"
    assert url_unescape(b"%3F", "ascii", plus=False) == "%3F"


# Generated at 2022-06-14 12:09:59.167797
# Unit test for function linkify
def test_linkify():
    assert(linkify("Hello") == "Hello")
    assert(linkify("Hello http://tornadoweb.org!", shorten = True) \
           == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!')
    assert(linkify("Hello www.tornadoweb.org!", shorten = True) \
           == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!')
    assert(linkify("Hello http://t.co/0JG5Mcq", shorten = True) \
           == 'Hello <a href="http://t.co/0JG5Mcq">http://t.co/0JG5Mcq</a>')

# Generated at 2022-06-14 12:10:09.473880
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.com")=='http://www.google.com'
    assert linkify("www.google.com")=='<a href="http://www.google.com">www.google.com</a>'
    assert linkify("Hello http://www.google.com!")=='Hello <a href="http://www.google.com">www.google.com</a>!'
    assert linkify("Hello http://www.google.com/!")=='Hello <a href="http://www.google.com/">www.google.com/</a>!'
    assert linkify("Hello www.google.com/!")=='Hello <a href="http://www.google.com/">www.google.com/</a>!'

# Generated at 2022-06-14 12:10:13.157287
# Unit test for function linkify
def test_linkify():
    assert(linkify("hello www.domain.com") == 'hello <a href="http://www.domain.com">www.domain.com</a>')
    assert(linkify("hello @user") == 'hello @user')
    assert(linkify("hello http://domain.com") == 'hello <a href="http://domain.com">http://domain.com</a>')
    assert(linkify("hello ftp://domain.com") == 'hello <a href="ftp://domain.com">ftp://domain.com</a>')



# Generated at 2022-06-14 12:10:18.752142
# Unit test for function linkify
def test_linkify():
    import unittest
    import re
    import sys

    class LinkifyTest(unittest.TestCase):
        def test_linkify(self):
            # simple case
            self.assertEqual(
                linkify("http://www.friendpaste.com/"),
                '<a href="http://www.friendpaste.com/">http://www.friendpaste.com/</a>',
            )
            # some text
            self.assertEqual(
                linkify("Hi there http://www.google.com"),
                'Hi there <a href="http://www.google.com">http://www.google.com</a>',
            )
            # trailing punctuations

# Generated at 2022-06-14 12:10:48.792012
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://tornadoweb.org/!'
    print(linkify(text))


# escape.py
# Copyright (c) 2008-2019 by Hsiaoming Yang

_xml_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
}



# Generated at 2022-06-14 12:10:51.165454
# Unit test for function linkify
def test_linkify():
    assert linkify("foo http://www.facebook.com/ bar") == 'foo <a href="http://www.facebook.com/">http://www.facebook.com/</a> bar'

# Generated at 2022-06-14 12:10:55.630461
# Unit test for function linkify
def test_linkify():
    url = 'something like www.google.com or https://www.google.com or www.yahoo.com/more/or/less or http://127.0.0.1:8888'
    print(linkify(url))
    url = 'something like www.google.com or https://www.google.com or www.yahoo.com/more/or/less or http://127.0.0.1:8888 or https://docs.python.org/3/library/re.html'
    print(linkify(url))
    print(linkify(url, shorten=True))


# Generated at 2022-06-14 12:11:02.908533
# Unit test for function linkify
def test_linkify():
    assert linkify(b'') == ''
    assert linkify('') == ''
    assert linkify(b'Hello there') == 'Hello there'
    assert linkify('Hello there') == 'Hello there'
    assert (linkify('Hello there http://world') ==
            'Hello there <a href="http://world">http://world</a>')
    assert (linkify('Hello there http://world:8080') ==
            'Hello there <a href="http://world:8080">http://world:8080</a>')
    assert (linkify('Hello there http://world:8080/') ==
            'Hello there <a href="http://world:8080/">http://world:8080/</a>')

# Generated at 2022-06-14 12:11:06.775936
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com/blah_blah") == '<a href="http://foo.com/blah_blah">http://foo.com/blah_blah</a>'



# Generated at 2022-06-14 12:11:16.463972
# Unit test for function linkify
def test_linkify():
    assert linkify(u'http://example.com') == '<a href="http://example.com">http://example.com</a>'
    assert linkify(u'https://example.com') == '<a href="https://example.com">https://example.com</a>'
    assert linkify(u'http://example.com/foo') == '<a href="http://example.com/foo">http://example.com/foo</a>'
    assert linkify(u'http://exämple.com/') == '<a href="http://exämple.com/">http://exämple.com/</a>'
    assert linkify(u'www.example.com') == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify

# Generated at 2022-06-14 12:11:28.885135
# Unit test for function linkify
def test_linkify():
    test_str = '''
    Google https://www.google.com
    Yahoo http://www.yahoo.com/
    Bing http://www.bing.com
    '''
    assert linkify(test_str) == '''
    Google <a href="https://www.google.com">https://www.google.com</a>
    Yahoo <a href="http://www.yahoo.com/">http://www.yahoo.com/</a>
    Bing <a href="http://www.bing.com">http://www.bing.com</a>
    ''', 'linkify'
    print('test_linkify ... ok')
test_linkify()


# I originally used the regex from
# http://daringfireball.net/2010/07/improved_regex_for_matching_urls
# but it gets

# Generated at 2022-06-14 12:11:35.943280
# Unit test for function linkify
def test_linkify():
    assert linkify(
        "http://www.example.com",
        extra_params='title="Link"'
    ) == u'<a href="http://www.example.com" title="Link">http://www.example.com</a>'
    assert linkify(
        "nothing"
    ) == u"nothing"
    assert linkify(
        "<script>http://www.example.com</script>",
        extra_params=lambda link: 'target="_blank" rel="nofollow"'
    ) == '<script><a href="http://www.example.com" target="_blank" rel="nofollow">http://www.example.com</a></script>'
    assert linkify(
        "nothing"
    ) == u"nothing"

# Generated at 2022-06-14 12:11:41.934632
# Unit test for function linkify
def test_linkify():
    text = "Hello http://example.com/ some more text"
    assert linkify(text) == (
        "Hello <a href=\"http://example.com/\">http://example.com/</a> some more text"
    )



# Generated at 2022-06-14 12:11:50.158341
# Unit test for function linkify
def test_linkify():
    text = "Hello www.example.com and http://example.com/ and mailto:a@b.com"
    assert linkify(text) == "Hello <a href=\"http://www.example.com\">www.example.com</a> and <a href=\"http://example.com/\">http://example.com/</a> and <a href=\"mailto:a@b.com\">mailto:a@b.com</a>"
    assert linkify(text, require_protocol=True) == "Hello www.example.com and <a href=\"http://example.com/\">http://example.com/</a> and <a href=\"mailto:a@b.com\">mailto:a@b.com</a>"

# Generated at 2022-06-14 12:12:33.362002
# Unit test for function linkify
def test_linkify():
    if not linkify("hello world"):
        raise Exception("linkify() failed")


# The following lines are modified from code in the Python stdlib, licensed
# under the Python Software Foundation License.  See the static/LICENSE file
# for more details.

# This code was originally written by Simon Willison (see
# http://code.activestate.com/recipes/303668/) and re-licensed under the
# PSF license.  It was then modified to handle unicode strings correctly by
# David McNab.

_HTTP_VALUE_QUOTE_RE = re.compile(r"[\x00-\x1f\"\\]")
_HTTP_VALUE_ESCAPE_RE = re.compile(r"\"")



# Generated at 2022-06-14 12:12:37.196897
# Unit test for function linkify
def test_linkify():
    output=linkify("Hello http://tornadoweb.org")
    assert output=='Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>'



# Generated at 2022-06-14 12:12:49.474205
# Unit test for function linkify

# Generated at 2022-06-14 12:13:01.636997
# Unit test for function linkify
def test_linkify():
    assert linkify(
        "http://www.tornadoweb.org/en/stable/") == '<a href="http://www.tornadoweb.org/en/stable/">http://www.tornadoweb.org/en/stable/</a>'  # noqa: E501
    assert linkify(
        "http://www.tornadoweb.org/en/stable/#hello-world") == '<a href="http://www.tornadoweb.org/en/stable/#hello-world">http://www.tornadoweb.org/en/stable/#hello-world</a>'  # noqa: E501

# Generated at 2022-06-14 12:13:08.739897
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'
    assert linkify("HTTP://www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">HTTP://www.tornadoweb.org</a>'
    assert linkify("Hello www.tornadoweb.org!") == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!'
    assert linkify("http://www.tornadoweb.org/ is great") == '<a href="http://www.tornadoweb.org/">http://www.tornadoweb.org/</a> is great'

# Generated at 2022-06-14 12:13:19.365269
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))
    print(linkify("Hello www.tornadoweb.org!"))
    print(linkify("Hello http://www.tornadoweb.org!"))
    print(linkify("Hello http://www.tornadoweb.org:80/!"))
    print(linkify("Hello http://www.tornadoweb.org/path/to/file.txt!"))
    print(linkify("Hello http://www.tornadoweb.org/path/to/file.txt?key1=value1&key2=value2!"))
    print(linkify("Hello http://www.tornadoweb.org/path/to/file.txt#Anchor!"))

# Generated at 2022-06-14 12:13:32.833418
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""
    assert linkify("hello") == "hello"
    assert linkify("hello http://www.tornadoweb.org/en/stable/") == 'hello <a href="http://www.tornadoweb.org/en/stable/">http://www.tornadoweb.org/en/stable/</a>'  # noqa: E501
    assert linkify("http://www.tornadoweb.org/en/stable/") == '<a href="http://www.tornadoweb.org/en/stable/">http://www.tornadoweb.org/en/stable/</a>'  # noqa: E501

# Generated at 2022-06-14 12:13:38.532980
# Unit test for function linkify
def test_linkify():
    assert not linkify("hello")
    assert linkify("http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("hello http://www.google.com world") == 'hello <a href="http://www.google.com">http://www.google.com</a> world'
    assert linkify("http://www.google.com/hello-world_how-are-you?") == '<a href="http://www.google.com/hello-world_how-are-you?">http://www.google.com/hello-world_how-are-you?</a>'

# Generated at 2022-06-14 12:13:50.048267
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("foo@example.com") == '<a href="mailto:foo@example.com">foo@example.com</a>'
    assert linkify("http://example.com/foo?bar=baz&ding=dong") == '<a href="http://example.com/foo?bar=baz&amp;ding=dong">http://example.com/foo?bar=baz&amp;ding=dong</a>'  # noqa: E501

# Generated at 2022-06-14 12:13:54.283554
# Unit test for function linkify
def test_linkify():
    try:
        import lxml.html
        # If lxml is installed, check that our linkify function behaves
        # the same as lxml's auto-linker
        text = "Hello http://world.com/"
        our_result = linkify(text)
        lxml_result = lxml.html.fromstring("<p>%s</p>" % text).text_content()
        assert our_result == lxml_result
    except ImportError:
        pass



# Generated at 2022-06-14 12:14:19.697397
# Unit test for function linkify

# Generated at 2022-06-14 12:14:27.364846
# Unit test for function linkify
def test_linkify():
    text = "hello, http://www.example.com/world.html"
    r = linkify(text)
    assert isinstance(r, str), "str"
    assert r == 'hello, <a href="http://www.example.com/world.html">http://www.example.com/world.html</a>'

    text = "hello, http://www.example.com/world.html"
    r = linkify(text, shorten=True)
    assert isinstance(r, str), "str"
    assert r == 'hello, <a href="http://www.example.com/world.html">http://www.example.com/worl...</a>'

    text = "hello, http://www.example.com/world.html"
    r = linkify(text, require_protocol=True)

# Generated at 2022-06-14 12:14:30.291315
# Unit test for function linkify
def test_linkify():
    assert linkify('http://example.com/abc') == '<a href="http://example.com/abc">http://example.com/abc</a>'



# Generated at 2022-06-14 12:14:42.634705
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornado.org"
    html = linkify(text)
    assert html == u'Hello <a href="http://tornado.org">http://tornado.org</a>'

    url = "http://test.test/?test=test&test2=test2&test2=test3"
    html = linkify(url)
    assert html == u'<a href="http://test.test/?test=test&amp;test2=test2&amp;test2=test3">http://test.test/?test=test&amp;test2=test2&amp;test2=test3</a>'



# Generated at 2022-06-14 12:14:47.563099
# Unit test for function linkify
def test_linkify():
    assert linkify('<b>http://www.example.com</b>') == '<b><a href="http://www.example.com">http://www.example.com</a></b>'



# Generated at 2022-06-14 12:14:59.085247
# Unit test for function linkify
def test_linkify():
    assert linkify("http://abc.com") == '<a href="http://abc.com">http://abc.com</a>'
    assert linkify("http://abc.com/a?b=c" ) == '<a href="http://abc.com/a?b=c">http://abc.com/a?b=c</a>'
    assert linkify("abc.com") == '<a href="http://abc.com">abc.com</a>'
    assert linkify("(http://abc.com)") == '(<a href="http://abc.com">http://abc.com</a>)'
    assert linkify("<a href='http://abc.com'>http://abc.com</a>") == "<a href='http://abc.com'>http://abc.com</a>"


# Generated at 2022-06-14 12:15:00.662124
# Unit test for function linkify
def test_linkify():
    print(linkify(u'Hello http://www.google.com!'))


# Generated at 2022-06-14 12:15:06.349667
# Unit test for function linkify
def test_linkify():
    assert linkify(text="", shorten=True, extra_params="", require_protocol=False, permitted_protocols=["http", "https"]) == ''
    assert linkify(text="Hello http://tornadoweb.org!", shorten=True, extra_params="", require_protocol=False, permitted_protocols=["http", "https"]) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
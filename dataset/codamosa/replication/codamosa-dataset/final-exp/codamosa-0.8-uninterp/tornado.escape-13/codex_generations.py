

# Generated at 2022-06-14 12:05:42.811250
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com/") == '<a href="http://foo.com/">http://foo.com/</a>'
    assert linkify("foo@example.com") == '<a href="mailto:foo@example.com">foo@example.com</a>'
    assert linkify("foo@yahoo.com") == '<a href="mailto:foo@yahoo.com">foo@yahoo.com</a>'
    assert linkify("foo@me.com") == '<a href="mailto:foo@me.com">foo@me.com</a>'
    assert linkify("www.foo.com") == '<a href="http://www.foo.com">www.foo.com</a>'

# Generated at 2022-06-14 12:05:56.686975
# Unit test for function linkify
def test_linkify():
    text = "text1 http://www.baidu.com?q=hello%20world text2"
    expect = 'text1 <a href="http://www.baidu.com?q=hello%20world">http://www.baidu.com?q=hello%20world</a> text2'
    assert linkify(text) == expect
    text = "<html> text1 http://www.baidu.com?q=hello%20world&apos; text2 </html>"
    expect = '<html> text1 <a href="http://www.baidu.com?q=hello%20world&apos;">http://www.baidu.com?q=hello%20world&apos;</a> text2 </html>'
    assert linkify(text) == expect

# Generated at 2022-06-14 12:06:06.767092
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo") == '<a href="http://foo">http://foo</a>'
    assert linkify("www.foo.com") == '<a href="http://www.foo.com">www.foo.com</a>'
    assert linkify("http://foo/foo?bar=baz&bing=bong") == u'<a href="http://foo/foo?bar=baz&bing=bong">http://foo/foo?bar=baz&amp;bing=bong</a>'  # noqa: E501
    assert linkify("http://foo/foo?bar=baz&bing=bong", shorten=True) == '<a href="http://foo/foo?bar=baz&bing=bong">http://foo/...</a>'  # noqa: E501


# Generated at 2022-06-14 12:06:23.328990
# Unit test for function linkify
def test_linkify():
    assert(linkify("http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>')
    assert(linkify("https://www.google.com") == '<a href="https://www.google.com">https://www.google.com</a>')
    assert(linkify("www.google.com") == '<a href="http://www.google.com">www.google.com</a>')
    assert(linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!')

# Generated at 2022-06-14 12:06:39.580609
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.co.jp") == '<a href="http://www.google.co.jp">http://www.google.co.jp</a>'
    assert linkify("Hello http://tornadoweb.org !") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a> !'
    assert linkify("Google Reader: http://www.google.com/reader") == 'Google Reader: <a href="http://www.google.com/reader">http://www.google.com/reader</a>'

# Generated at 2022-06-14 12:06:49.834319
# Unit test for function linkify
def test_linkify():
    assert linkify('http://example.com') == u'<a href="http://example.com">http://example.com</a>'
    assert linkify('http://example.com/path') == u'<a href="http://example.com/path">http://example.com/path</a>'
    assert linkify('http://example.com/path?foo=bar&baz=blah&buz') == u'<a href="http://example.com/path?foo=bar&amp;baz=blah&amp;buz">http://example.com/path?foo=bar&amp;baz=blah&amp;buz</a>'

# Generated at 2022-06-14 12:06:57.071938
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://tornadoweb.org!, www.baidu.com'
    assert 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!, <a href="http://www.baidu.com">www.baidu.com</a>' == linkify(text)


# Generated at 2022-06-14 12:07:01.550638
# Unit test for function linkify
def test_linkify():
    text = '不要忘記關注電腦玩物 https://www.facebook.com/technews'
    assert linkify(text) == '不要忘記關注電腦玩物 <a href="https://www.facebook.com/technews">https://www.facebook.com/technews</a>'

test_linkify()



# Generated at 2022-06-14 12:07:12.837119
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert linkify("") == ""
    assert linkify("hello") == "hello"
    assert linkify("hello http://www.tornadoweb.org") == 'hello <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'

    assert linkify("hello www.tornadoweb.org", require_protocol=False) == 'hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    assert linkify("hello www.tornadoweb.org", require_protocol=True) == 'hello www.tornadoweb.org'


# Generated at 2022-06-14 12:07:23.064810
# Unit test for function linkify
def test_linkify():
    assert linkify('hello http://example.com') == 'hello <a href="http://example.com">http://example.com</a>'  # noqa: E501
    assert linkify('hello http://example.com:8080/path') == 'hello <a href="http://example.com:8080/path">http://example.com:8080/path</a>'  # noqa: E501
    assert linkify('hello http://example.com:8080/path?key=val') == 'hello <a href="http://example.com:8080/path?key=val">http://example.com:8080/path?key=val</a>'  # noqa: E501

# Generated at 2022-06-14 12:07:40.015932
# Unit test for function linkify
def test_linkify():
    # a list of text samples and the results we expect
    samples = [
        ("see http://example.com",
         "see <a href=\"http://example.com\">http://example.com</a>"),
        ("http://example.com/test?param=1&boo=bar",
         "<a href=\"http://example.com/test?param=1&amp;boo=bar\">http://example.com/test?param=1&amp;boo=bar</a>"),

    ]

    for sample in samples:
        print(sample[0], "=>", linkify(sample[0]))
        assert_equal(linkify(sample[0]), sample[1])


# Generated at 2022-06-14 12:07:51.856110
# Unit test for function linkify
def test_linkify():
    import re
    pat = re.compile(r'<a\s+href="([^"]+)"\s*>(.+)</a>')
    def test_linkify_assert(s, expected=s):
        assert expected == linkify(s)
    # Test with shortened urls
    test_linkify_assert("Hello http://www.tornadoweb.org/en/stable/")
    test_linkify_assert(
        "Hello http://www.tornadoweb.org/en/stable/?longquery=x" * 10)
    test_linkify_assert(
        "Hello www.tornadoweb.org/en/stable/?longquery=x" * 10)
    test_linkify_assert("http://foo.com/blah_blah",
                                "http://foo.com/blah_...")

# Generated at 2022-06-14 12:07:56.776608
# Unit test for function linkify
def test_linkify():
    text = '<a href="www.facebook.com" >www.facebook.com</a>'
    assert linkify(text,extra_params="target='_blank'") == '<a href="http://www.facebook.com" target=\'_blank\'>www.facebook.com</a>'
 


# Generated at 2022-06-14 12:08:04.810629
# Unit test for function linkify
def test_linkify():
    text = "Yale University's the home of the Bulldogs, but it also has the" \
           " world's largest university press. http://yalepress.yale.edu/"
    assert "href=\"http://yalepress.yale.edu/\"" in linkify(text)
    assert "href=\"http://www.google.com/\" rel=\"nofollow\"" in linkify(text,
                                                                        extra_params=lambda url: "rel=\"nofollow\"")


# for backward compatibility; can be removed in a future version
_url_escape = url_escape
_url_unescape = url_unescape



# Generated at 2022-06-14 12:08:11.841263
# Unit test for function linkify

# Generated at 2022-06-14 12:08:20.062107
# Unit test for function linkify

# Generated at 2022-06-14 12:08:25.435868
# Unit test for function linkify

# Generated at 2022-06-14 12:08:32.067855
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    assert linkify(text) == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"

test_linkify()

# This singleton can be used as a dummy function for
# :func:`ObjectDict.setdefault` when you don't want to use
# ``dict.setdefault``.
_MISSING = object()



# Generated at 2022-06-14 12:08:44.754505
# Unit test for function linkify
def test_linkify():
    assert (linkify("http://www.google.com") ==
            '<a href="http://www.google.com">http://www.google.com</a>')
    assert (linkify("hello http://www.google.com goodbye") ==
            'hello <a href="http://www.google.com">http://www.google.com</a> goodbye')
    assert (linkify("hello http://www.google.com/something goodbye") ==
            'hello <a href="http://www.google.com/something">http://www.google.com/something</a> goodbye')

# Generated at 2022-06-14 12:08:54.243294
# Unit test for function linkify
def test_linkify():
  assert linkify('http://google.com') == '<a href="http://google.com">http://google.com</a>'
  assert linkify('http://google.com/foo ') == '<a href="http://google.com/foo">http://google.com/foo</a> '
  assert linkify('https://google.com/foo') == '<a href="https://google.com/foo">https://google.com/foo</a>'
  assert linkify('http://google.com foo') == '<a href="http://google.com">http://google.com</a> foo'

# Generated at 2022-06-14 12:09:06.303257
# Unit test for function linkify
def test_linkify():
    print("===Test linkify()===")
    text = "This is a link to google.com"
    print(linkify(text))
    print("Test Completed!\n\n")

test_linkify()


# Generated at 2022-06-14 12:09:17.767838
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == '<a href="http://google.com">http://google.com</a>'
    assert linkify("http://google.com/") == '<a href="http://google.com/">http://google.com/</a>'
    assert linkify("http://google.com/?foo=bar") == '<a href="http://google.com/?foo=bar">http://google.com/?foo=bar</a>'
    assert linkify("http://google.com/#foo=bar") == '<a href="http://google.com/#foo=bar">http://google.com/#foo=bar</a>'

# Generated at 2022-06-14 12:09:20.807863
# Unit test for function linkify
def test_linkify():
    text = 'hello world'
    text2 = linkify(text)
    assert text2 == 'hello world'

if __name__ == '__main__':
    test_linkify()

# Generated at 2022-06-14 12:09:24.663102
# Unit test for function linkify
def test_linkify():
    if linkify("Hello http://tornadoweb.org!") == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!":
        print("success!")
if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:09:36.095665
# Unit test for function linkify
def test_linkify():
    # This test doesn't make a lot of sense in Python 3
    if sys.version_info[0] >= 3:
        return
    text = b"http://www.example.com"
    assert linkify(text) == b'<a href="http://www.example.com">www.example.com</a>'
    text = b'<a href="http://www.example.com">www.example.com</a>'
    assert linkify(text) == b'<a href="http://www.example.com">www.example.com</a>'
    text = b"Hello http://www.example.com!"
    assert (
        linkify(text)
        == b'Hello <a href="http://www.example.com">http://www.example.com</a>!'
    )
    text = b

# Generated at 2022-06-14 12:09:45.522487
# Unit test for function linkify
def test_linkify():
    # linkify() should be idempotent for normal html
    for x in ["", "<b>", "<b>foo", "foo <b>", "foo", "foo &gt;"]:
        assert linkify(x) == linkify(linkify(x))
        assert linkify(x) == linkify(linkify(linkify(linkify(linkify(x)))))

    # Non-ascii characters should not break things
    assert linkify(u"☃") == u"☃"
    assert linkify(u"☃☃☃") == u'☃☃☃'
    assert linkify(u"☃foo☃") == u'☃foo☃'

# Generated at 2022-06-14 12:10:00.206693
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert linkify('some plain text') == 'some plain text'
    assert linkify(
        'a link: http://foo.com') == 'a link: <a href="http://foo.com">http://foo.com</a>'
    assert linkify(
        'a link: uhttp://foo.com') == 'a link: uhttp://foo.com'

# Generated at 2022-06-14 12:10:09.123276
# Unit test for function linkify
def test_linkify():
    text = "www.google.com www.sina.com.cn http://www.sina.com.cn http://www.sina.com.cn:8080 https://www.baidu.com"
    print(linkify(text))
# test_linkify()


# _URL_RE is sometimes used directly because it's already unicode
URL_RE = _URL_RE

_HTML_UNSAFE = re.compile(r"[<>&\"\x00-\x20]+")
_HTML_REPLACE_RE = re.compile(r"([<>&\"\x00-\x20])|(\n+)")



# Generated at 2022-06-14 12:10:16.609001
# Unit test for function linkify
def test_linkify():
    assert (linkify("http://www.tornadoweb.org")
            == '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>')
    assert linkify("http://www.tornadoweb.org extra") == (
        '<a href="http://www.tornadoweb.org">'
        'http://www.tornadoweb.org</a> extra'
    )
    assert (
        linkify("Hello http://www.tornadoweb.org!")
        == 'Hello <a href="http://www.tornadoweb.org">'
        'http://www.tornadoweb.org</a>!'
    )

# Generated at 2022-06-14 12:10:21.282777
# Unit test for function linkify
def test_linkify():
    assert linkify(u'Hello http://tornadoweb.org!') == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
test_linkify()

_UTF8_TYPES = (bytes, type(None))



# Generated at 2022-06-14 12:10:42.154359
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == u'<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/foo&bar=baz&ding=dong") == u'<a href="http://example.com/foo&amp;bar=baz&amp;ding=dong">http://example.com/foo&amp;bar=baz&amp;ding=dong</a>'
    assert linkify("http://example.com/foo?bar=baz&amp;ding=dong") == u'<a href="http://example.com/foo?bar=baz&amp;ding=dong">http://example.com/foo?bar=baz&amp;ding=dong</a>'

# Generated at 2022-06-14 12:10:46.614997
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    expected = "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!" 
    return linkify(text) == expected
test_linkify()


# Generated at 2022-06-14 12:10:49.375930
# Unit test for function linkify
def test_linkify():
    assert linkify('Hello http://tornadoweb.org!') == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"

test_linkify()

# Generated at 2022-06-14 12:10:56.092538
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))
    urls = ("http://example.com", "http://example.com/foo/bar",
            "http://example.com/foo/bar?a=b&c=d",
            "http://example.com/foo/bar?a=b&c=d#section")
    for url in urls:
        print(linkify(url))
    print(linkify("Hello http://example.com", shorten=True))
    print(linkify("http://example.com/foo/bar?a=b&c=d#section", shorten=True))
    print(linkify("http://example.com/foo/bar?a=b&c=d#section", extra_params="rel=\"nofollow\""))
    # linkify(text, extra_params='

# Generated at 2022-06-14 12:11:06.929981
# Unit test for function linkify
def test_linkify():
    # Standard
    assert linkify("http://www.example.com") == \
        '<a href="http://www.example.com">http://www.example.com</a>'

    # With extra params
    assert linkify("http://www.example.com",
                   extra_params='rel="nofollow" class="external"') == \
        '<a href="http://www.example.com" rel="nofollow" class="external">' \
        'http://www.example.com</a>'
    # With multiple params

# Generated at 2022-06-14 12:11:13.243729
# Unit test for function linkify
def test_linkify():
    text = 'Hello <b>www.tornadoweb.org</b>!'
    print(linkify(text))
    text = 'Hello www.tornadoweb.org!'
    print(linkify(text, require_protocol=False))
    text = 'www.tornadoweb.org'
    print(linkify(text, require_protocol=False))
    print(linkify(text, require_protocol=False, shorten=True))

# Generated at 2022-06-14 12:11:15.570533
# Unit test for function linkify
def test_linkify():
    output = linkify("Hello http://www.google.com")
    assert "google" in output
    assert "<a" in output
# END unit test for function linkify



# Generated at 2022-06-14 12:11:27.753182
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert linkify("") == ""
    assert linkify("Hello") == "Hello"
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://example.com!") == 'Hello <a href="http://example.com">http://example.com</a>!'
    assert linkify("http://localhost:3000") == '<a href="http://localhost:3000">http://localhost:3000</a>'

# Generated at 2022-06-14 12:11:35.260556
# Unit test for function linkify
def test_linkify():
    assert linkify("text only") == "text only"
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/foo bar/baz") == '<a href="http://example.com/foo bar/baz">http://example.com/foo bar/baz</a>'
    assert linkify("http://example.com/foo+bar/baz") == '<a href="http://example.com/foo+bar/baz">http://example.com/foo+bar/baz</a>'
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'

# Generated at 2022-06-14 12:11:41.362146
# Unit test for function linkify
def test_linkify():
    assert "&lt;script&gt;" not in linkify(u"<script>")
    assert (
        '<a href="http://example.com/" rel="nofollow">http://example.com/</a>'
        == linkify("http://example.com/", extra_params="rel=\"nofollow\"")
    )
    assert (
        '<a href="http://example.com/" class="external">http://example.com/</a>'
        == linkify(
            "http://example.com/", extra_params=lambda url: 'class="external"'
        )
    )

# Generated at 2022-06-14 12:11:57.924168
# Unit test for function linkify
def test_linkify():
    assert linkify("www.example.com") ==  '<a href="http://www.example.com">www.example.com</a>'


# Generated at 2022-06-14 12:12:01.132857
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    result = linkify(text)
    expected = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'

    assert(result == expected)
test_linkify()




# Generated at 2022-06-14 12:12:05.811270
# Unit test for function linkify
def test_linkify():
    text = 'Hello www.tornadoweb.org!'
    assert linkify(text) == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!'
    text = 'Hello http://tornadoweb.org!'
    assert linkify(text) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    text = 'And, hello again: http://tornadoweb.org/!'
    assert linkify(text) == 'And, hello again: <a href="http://tornadoweb.org/">http://tornadoweb.org/</a>!'

# Generated at 2022-06-14 12:12:16.559934
# Unit test for function linkify

# Generated at 2022-06-14 12:12:27.766603
# Unit test for function linkify
def test_linkify():
    """
    Testing linkify function
    """
    def extra_params_cb(url):
      if url.startswith("http://example.com"):
          return 'class="internal"'
      else:
          return 'class="external" rel="nofollow"'
    text = 'Hello http://tornadoweb.org and example.com'
    assert(linkify(text) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a> and example.com')
    assert(linkify(text, extra_params='rel="nofollow" class="external"') == 'Hello <a rel="nofollow" class="external" href="http://tornadoweb.org">http://tornadoweb.org</a> and example.com')

# Generated at 2022-06-14 12:12:38.628972
# Unit test for function linkify
def test_linkify():
    #assert linkify('') == '', "should handle empty string"
    #assert linkify('foo') == 'foo', "should not any non-url"
    #assert linkify('foo.com') == 'foo.com', "should not linkify a trailing dot"
    assert linkify('Hello http://tornadoweb.org!') == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!', "simple http link"
    #assert linkify('Hello www.tornadoweb.org!') == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!', "simple www link"
    #assert linkify('Hello <a href="www.tornadoweb.org">www.tornadoweb.org</a>!') == 'Hello <

# Generated at 2022-06-14 12:12:50.522350
# Unit test for function linkify

# Generated at 2022-06-14 12:12:57.575349
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == '<a href="http://google.com">http://google.com</a>'
    assert linkify("hello http://google.com") == 'hello <a href="http://google.com">http://google.com</a>'
    assert linkify("http://google.com hello") == '<a href="http://google.com">http://google.com</a> hello'
    assert linkify("Hello google.com!") == 'Hello <a href="http://google.com">google.com</a>!'
    assert linkify("google.com/some/path") == '<a href="http://google.com/some/path">google.com/some/path</a>'

# Generated at 2022-06-14 12:13:06.972802
# Unit test for function linkify
def test_linkify():
    assert linkify("www.google.com") == (
        '<a href="http://www.google.com">www.google.com</a>'
    )
    assert linkify("http://www.google.com") == (
        '<a href="http://www.google.com">http://www.google.com</a>'
    )
    assert linkify("http://google.com") == (
        '<a href="http://google.com">http://google.com</a>'
    )
    assert linkify("https://www.google.com") == (
        '<a href="https://www.google.com">https://www.google.com</a>'
    )

# Generated at 2022-06-14 12:13:18.795864
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("http://www.example.com", shorten=True) == '<a href="http://www.example.com">http://www.examp...</a>'
    assert linkify("http://www.example.com", shorten=False) == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("http://www.example.com/index.php?a=1&b=2") == '<a href="http://www.example.com/index.php?a=1&b=2">http://www.example.com/index.php?a=1&b=2</a>'

# Generated at 2022-06-14 12:13:41.867812
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("http://www.google.com/") == '<a href="http://www.google.com/">http://www.google.com/</a>'
    assert linkify("https://www.google.com") == '<a href="https://www.google.com">https://www.google.com</a>'
    assert linkify("http://www.google.com:80/") == '<a href="http://www.google.com:80/">http://www.google.com:80/</a>'

# Generated at 2022-06-14 12:13:51.869941
# Unit test for function linkify
def test_linkify():
    """ Test linkify with different inputs.
    """
    text = "facebook.com"
    assert linkify(text) == 'facebook.com'
    text = "link: http://www.facebook.com/ and text"
    assert linkify(text) == 'link: <a href="http://www.facebook.com/">http://www.facebook.com/</a> and text'
    text = "link: http://www.facebook.com/?id=123 and text"
    assert linkify(text) == 'link: <a href="http://www.facebook.com/?id=123">http://www.facebook.com/?id=123</a> and text'
    text = "link: http://www.facebook.com/?id=123&subid=456 and text"

# Generated at 2022-06-14 12:14:02.942464
# Unit test for function linkify
def test_linkify():
    assert (linkify("http://www.example.com") ==
            '<a href="http://www.example.com">http://www.example.com</a>')
    assert (linkify('foo@example.com') ==
            '<a href="mailto:foo@example.com">foo@example.com</a>')
    assert (linkify(
            'foo@example.com bar@example.com') ==
            '<a href="mailto:foo@example.com">foo@example.com</a> '
            '<a href="mailto:bar@example.com">bar@example.com</a>')

# Generated at 2022-06-14 12:14:13.603848
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'  # noqa: E501
    assert linkify("http://example.com/foo") == '<a href="http://example.com/foo">http://example.com/foo</a>'  # noqa: E501
    assert linkify("http://example.com/foo?bar=baz") == '<a href="http://example.com/foo?bar=baz">http://example.com/foo?bar=baz</a>'  # noqa: E501

# Generated at 2022-06-14 12:14:23.063737
# Unit test for function linkify
def test_linkify():
    if linkify("Hello http://tornadoweb.org!")!="Hello <a href='http://tornadoweb.org'>http://tornadoweb.org</a>!":
        print("error: linkify()")
    if linkify("Hello http://tornadoweb.org!", shorten=True)!="Hello <a href='http://tornadoweb.org'>http://tornadoweb.org</a>!":
        print("error: linkify(), shorten=True")
    if linkify("Hello http://tornadoweb.org!", shorten=True, extra_params="rel='nofollow'")!="Hello <a href='http://tornadoweb.org' rel='nofollow'>http://tornadoweb.org</a>!":
        print("error: linkify(), shorten=True, extra_params='rel='nofollow''")

# Generated at 2022-06-14 12:14:26.040383
# Unit test for function linkify
def test_linkify():
    print(linkify('Hello http://tornadoweb.org!'))
    print(linkify('Hello http://tornadoweb.org!',shorten=True))
    print(linkify('Hello http://tornadoweb.org!', extra_params="rel='nofollow'"))



# Generated at 2022-06-14 12:14:41.226441
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert linkify("") == ""
    assert linkify("hello") == "hello"
    assert linkify("hello http://tornadoweb.org") == "hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>"
    assert linkify("hello www.tornadoweb.org") == "hello <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>"
    assert linkify("hello http://www.tornadoweb.org") == "hello <a href=\"http://www.tornadoweb.org\">http://www.tornadoweb.org</a>"

# Generated at 2022-06-14 12:14:52.251667
# Unit test for function linkify
def test_linkify():
    assert linkify('<div>http://example.org&quot;</div>') == '<div>http://example.org&quot;</div>'
    assert linkify('hello <a href="http://example.org">http://example.org</a>') == 'hello <a href="http://example.org">http://example.org</a>'
    assert linkify('hello www.example.org') == 'hello <a href="http://www.example.org">www.example.org</a>'
    assert linkify('hello http://example.org') == 'hello <a href="http://example.org">http://example.org</a>'

# Generated at 2022-06-14 12:15:02.527832
# Unit test for function linkify
def test_linkify():
    assert linkify("Hi there www.facebook.com, test@test.com",
                   extra_params='rel="nofollow"',
                   require_protocol = False,
                   permitted_protocols = ['http', 'https', 'mailto']) == \
           'Hi there <a href="http://www.facebook.com" ' + \
           'rel="nofollow">www.facebook.com</a>, ' + \
           '<a href="mailto:test@test.com" rel="nofollow">' + \
           'test@test.com</a>'

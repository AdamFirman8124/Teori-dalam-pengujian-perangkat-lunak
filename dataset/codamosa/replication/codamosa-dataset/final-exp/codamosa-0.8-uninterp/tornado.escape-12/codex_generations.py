

# Generated at 2022-06-14 12:05:25.118536
# Unit test for function url_unescape
def test_url_unescape():
    assert url_unescape("a+b%20c") == "a+b c"
    assert url_unescape(b"a+b+c") == "a b c"
    assert url_unescape(b"a+b+c", plus=False) == "a+b+c"
    assert url_unescape(b"a%2Bb+c", encoding=None, plus=False) == b"a+b c"
    assert url_unescape(b"a%2Bb+c") == "a+b c"
    assert url_unescape("a%2Bb+c") == "a+b c"



# Generated at 2022-06-14 12:05:27.643323
# Unit test for function linkify
def test_linkify():
    assert 'a <a href="http://www.google.com">www.google.com</a>' == linkify('a www.google.com')

# Generated at 2022-06-14 12:05:38.135614
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'

    assert "example.com" not in linkify("example.com")
    assert linkify("example.com", require_protocol=False) == '<a href="http://example.com">example.com</a>'

    assert "mailto:user@domain.com" not in linkify("user@domain.com")
    assert linkify("user@domain.com", require_protocol=False) == '<a href="mailto:user@domain.com">user@domain.com</a>'

    assert linkify("foo http://example.com bar") == "foo <a href=\"http://example.com\">http://example.com</a> bar"

# Generated at 2022-06-14 12:05:44.671551
# Unit test for function linkify
def test_linkify():
    texts = [
        "http://www.facebook.com/",
        "www.facebook.com/",
        "http://www.baidu.com/",
        "www.baidu.com/",
        "http://www.google.com/",
        "www.google.com/",
        "http://www.bilibili.com/",
        "www.bilibili.com/"
    ]
    for text in texts:
        print(linkify(text))


# Generated at 2022-06-14 12:05:59.709003
# Unit test for function linkify
def test_linkify():
    def extra_params_cb(url):
        if url.startswith("http://example.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    value = '<a href="http://www.example.com/blah.html" class="external" rel="nofollow">http://www.example.com/blah.html</a>'
    assert linkify(value) == value

    value1 = '<a href="http://www.example.com/blah.html" class="internal">http://www.example.com/blah.html</a>'
    assert linkify(value, extra_params=extra_params_cb) == value1

    assert linkify('foo@example.com') == 'foo@example.com'
    assert linkify

# Generated at 2022-06-14 12:06:03.610214
# Unit test for function url_unescape
def test_url_unescape():
    assert url_unescape(b"url%E6%B5%8B%E8%AF%95", encoding="utf-8")
    assert url_unescape(b"url%E6%B5%8B%E8%AF%95", encoding=None)



# Generated at 2022-06-14 12:06:07.339772
# Unit test for function linkify
def test_linkify():
  test_string = "test http://example.com/test.html is\nwww.example.com/test"
  linkified_string = linkify(test_string)
  assert "http://example.com" in linkified_string
  assert "www.example.com" in linkified_string
  assert "http://www.example.com" not in linkified_string


# Generated at 2022-06-14 12:06:23.731899
# Unit test for function linkify
def test_linkify():
    import unittest
    import doctest
    unittest.TestCase.assertEqual = lambda s,a,b: doctest.OutputChecker.check_output(s,a,b,True)

# Generated at 2022-06-14 12:06:39.631032
# Unit test for function linkify
def test_linkify():
    url = "http://example.com"
    assert(linkify(url) ==
           u'<a href="http://example.com">http://example.com</a>')
    assert(linkify(url, require_protocol=False) ==
           u'<a href="http://example.com">example.com</a>')
    assert(linkify(url, shorten=True) ==
           u'<a href="http://example.com">example.com</a>')
    assert(linkify(url, extra_params='rel="nofollow" class="external"') ==
           u'<a href="http://example.com" rel="nofollow" class="external">http://example.com</a>')

# Generated at 2022-06-14 12:06:49.890170
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://tornadoweb.org!'
    assert linkify(text) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert '<p>' in linkify('<p>')
    text = 'Hello http://tornadoweb.org! www.tornadoweb.org'
    print(linkify(text))
    assert linkify(text) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>! <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    text = 'Hello http://tornadoweb.org! www.tornadoweb.org'
    print(linkify(text, require_protocol=True))

# Generated at 2022-06-14 12:07:02.493252
# Unit test for function linkify
def test_linkify():
    '''
        this function tests the linkify function
    '''

    # testing to see if it returns the same string when there is no URL
    assert linkify('Hello') == 'Hello'

    # testing to see if it returns an html a tag when there is a URL
    assert linkify('http://google.com') == \
         '<a href="http://google.com">http://google.com</a>'



# Generated at 2022-06-14 12:07:14.165119
# Unit test for function linkify
def test_linkify():
    text = "http://www.google.com"
    assert linkify(text)=='<a href="http://www.google.com">http://www.google.com</a>'
    text = "Hello www.google.com"
    assert linkify(text)=='Hello <a href="http://www.google.com">www.google.com</a>'
    text = "Hello www.google.com Hello https://www.google.com"
    assert linkify(text)=='Hello <a href="http://www.google.com">www.google.com</a> Hello <a href="https://www.google.com">https://www.google.com</a>'
    text = "Hello http://www.google.com Hello http://www.google.com"

# Generated at 2022-06-14 12:07:23.681486
# Unit test for function linkify
def test_linkify():
    assert linkify(u"http://example.com") == u'<a href="http://example.com">http://example.com</a>'
    assert linkify(u"http://example.com/\u2713") == u'<a href="http://example.com/&#x2713;">http://example.com/&#x2713;</a>'
    assert linkify(u"http://example.com/foo?bar=baz") == u'<a href="http://example.com/foo?bar=baz">http://example.com/foo?bar=baz</a>'

# Generated at 2022-06-14 12:07:35.839102
# Unit test for function linkify
def test_linkify():
    a=linkify('hello world www.google.com.test this')
    assert a=='hello world <a href="http://www.google.com">www.google.com</a>.test this'
    print(a)
    b=linkify('hello world https://www.google.com.test this')
    assert b=='hello world <a href="https://www.google.com">https://www.google.com</a>.test this'
    print(b)
    c=linkify('hello http://www.baidu.com/s?wd=hello%20world world')
    assert c=='hello <a href="http://www.baidu.com/s?wd=hello%20world">http://www.baidu.com/s?wd=hello%20world</a> world'

# Generated at 2022-06-14 12:07:42.569490
# Unit test for function linkify
def test_linkify():
    # Test for linkify
    url1 = 'This is a test url http://www.yahoo.com'
    url2 = 'This is a test url http://www.yahoo.com/index.html'
    url3 = 'This is a test url http://www.yahoo.com/index.html#test'
    url4 = 'This is a test url http://www.yahoo.com/index.html?name=asd&test=test#test'
    url5 = 'This is a test url http://www.yahoo.com/index.html?name=asd&test=test#test2&test=test'
    url6 = 'This is a test url http://test.test.test.test.test.test.test.com/'


# Generated at 2022-06-14 12:07:53.901457
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.msn.com") == '<a href="http://www.msn.com">http://www.msn.com</a>'
    assert linkify("www.facebook.com") == '<a href="http://www.facebook.com">www.facebook.com</a>'
    assert linkify("http://www.msn.com?a=b") == '<a href="http://www.msn.com?a=b">http://www.msn.com?a=b</a>'
    assert linkify("http://www.msn.com?a=b") == '<a href="http://www.msn.com?a=b">http://www.msn.com?a=b</a>'

# Generated at 2022-06-14 12:08:04.526618
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == (
        '<a href="http://example.com" title="http://example.com">'
        "http://example.com</a>"
    )
    assert linkify("http://example.com", shorten=True) == (
        '<a href="http://example.com" title="http://example.com">'
        "http://example.com</a>"
    )
    assert linkify("foo@example.com") == "foo@example.com"
    assert linkify("foo@example.com", require_protocol=True) == "foo@example.com"

# Generated at 2022-06-14 12:08:11.596211
# Unit test for function linkify

# Generated at 2022-06-14 12:08:12.677697
# Unit test for function linkify
def test_linkify():
    text = "hello http://www.abc.com/sina/world/"
    print(linkify(text))


# Generated at 2022-06-14 12:08:15.574534
# Unit test for function linkify
def test_linkify(): # noqa: F811
    assert linkify("Hell http://www.google.com") == 'Hell <a href="http://www.google.com">http://www.google.com</a>'



# Generated at 2022-06-14 12:08:30.707405
# Unit test for function linkify
def test_linkify():
    assert linkify("abc") == "abc"
    assert linkify("http://x.com") == '<a href="http://x.com">http://x.com</a>'
    assert linkify("www.x.com") == '<a href="http://www.x.com">www.x.com</a>'
    assert linkify("x.com") == '<a href="http://x.com">x.com</a>'
    assert linkify("http://x.y.com") == '<a href="http://x.y.com">http://x.y.com</a>'
    assert linkify("x") == 'x'
    assert linkify("x.y") == 'x.y'

# Generated at 2022-06-14 12:08:38.422388
# Unit test for function linkify
def test_linkify():
    # Test cases come from http://www.noah.org/wiki/RegEx_Python#Examples
    linkify_test_cases = [] # type: List[typing.Tuple[str, str]]
    linkify_test_cases.append(('http://foo.com/blah_blah', '<a href="http://foo.com/blah_blah">http://foo.com/blah_blah</a>'))
    linkify_test_cases.append(('http://foo.com/blah_blah/', '<a href="http://foo.com/blah_blah/">http://foo.com/blah_blah/</a>'))

# Generated at 2022-06-14 12:08:49.962394
# Unit test for function linkify
def test_linkify():
    assert linkify('http://example.com') == '<a href="http://example.com">http://example.com</a>'
    assert linkify('http://example.com/index.html') == '<a href="http://example.com/index.html">http://example.com/index.html</a>'
    assert linkify('http://example.com/index.html?x=y') == '<a href="http://example.com/index.html?x=y">http://example.com/index.html?x=y</a>'

# Generated at 2022-06-14 12:09:04.910176
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.google.com") == \
           '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("http://www.args.com",
                   shorten=True) == \
           '<a href="http://www.args.com">http://www.args.com</a>'
    assert linkify("http://www.args.com/a_long_url",
                   shorten=True) == \
           '<a href="http://www.args.com/a_long_url">http://www.args.com/a_long_url</a>'

# Generated at 2022-06-14 12:09:08.803426
# Unit test for function linkify
def test_linkify():
    text = linkify('http://www.facebook.com')
    text = linkify('http://www.facebook.com', shorten=True)
    text = linkify('http://www.facebook.com', shorten=False)
    text = linkify('http://www.facebook.com', extra_params="class='external'")
    text = linkify('http://www.facebook.com', require_protocol=False)
    text = linkify('www.facebook.com', require_protocol=False)
    text = linkify('www.facebook.com', require_protocol=True)
    text = linkify('http://www.facebook.com', permitted_protocols=['http', 'ftp'])




# Generated at 2022-06-14 12:09:17.871755
# Unit test for function linkify
def test_linkify():
    assert linkify("hi") == "hi"
    assert linkify("hi http://there") == 'hi <a href="http://there">http://there</a>'
    assert linkify("hi http://there/") == 'hi <a href="http://there/">http://there/</a>'
    assert (
        linkify("hi https://there/") == 'hi <a href="https://there/">https://there/</a>'
    )
    assert (
        linkify("hi www.there.com") == 'hi <a href="http://www.there.com">www.there.com</a>'
    )

# Generated at 2022-06-14 12:09:20.481592
# Unit test for function linkify
def test_linkify():
    linkify_test = linkify('Hello http://tornadoweb.org!')
    print(linkify_test)
#test_linkify()


# Generated at 2022-06-14 12:09:26.486854
# Unit test for function linkify
def test_linkify():
    def _test_links(text, expected, **kwargs):
        assert linkify(text, **kwargs) == expected

    # Test simple case
    _test_links(
        "www.example.com",
        '<a href="http://www.example.com">www.example.com</a>',
        require_protocol=False,
    )

    _test_links(
        "Check out www.example.com!",
        'Check out <a href="http://www.example.com">www.example.com</a>!',
        require_protocol=False,
    )


# Generated at 2022-06-14 12:09:37.038097
# Unit test for function linkify
def test_linkify():
    """ Unit test for function linkify """
    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'  # noqa: E501
    assert linkify("Hello www.tornadoweb.org!") == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!'  # noqa: E501
    assert linkify("Hello ftp://ftp.tornadoweb.org!") == 'Hello <a href="ftp://ftp.tornadoweb.org">ftp://ftp.tornadoweb.org</a>!'  # noqa: E501

test_linkify()
# -- end of linkify() --



# Generated at 2022-06-14 12:09:46.070683
# Unit test for function linkify
def test_linkify():
    test_str_1 = "convert me http://tornadoweb.org/en/stable/?name=first&a=1&b=2"
    test_str_2 = "http://user:passwd@host.com:8080/p/a/t/h;p?query=string#hash"
    test_str_3 = "java`script:alert(\"gotcha\")"
    test_str_4 = "HTTP://WWW.EXAMPLE.COM/Foo"
    test_str_5 = "http://www.example.com:80/foo"
    test_str_6 = "www.example.com"
    test_str_7 = "example.com"
    test_str_8 = "one.two.three.com"

# Generated at 2022-06-14 12:09:52.440643
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    linkified = linkify(text)
    assert linkified == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"

# Generated at 2022-06-14 12:09:56.814711
# Unit test for function linkify
def test_linkify():
    # Test Unicode 
    given = r"fr?n?ais"
    _URL_RE.sub(make_link, given)
if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:10:00.710496
# Unit test for function linkify
def test_linkify():
    assert linkify('http://localhost:8000') == '<a href="http://localhost:8000">http://localhost:8000</a>'
    assert linkify('www.baidu.com') == '<a href="http://www.baidu.com">www.baidu.com</a>'



# Generated at 2022-06-14 12:10:11.073328
# Unit test for function linkify
def test_linkify():
    l = linkify('http://1.com/p?a=1&b=2')
    assert l == '<a href="http://1.com/p?a=1&amp;b=2">http://1.com/p?a=1&amp;b=2</a>'
    #
    l = linkify('http://1.com/p?a=1&b=2', extra_params='title="test"')
    assert l == '<a href="http://1.com/p?a=1&amp;b=2" title="test">http://1.com/p?a=1&amp;b=2</a>'
    #

# Generated at 2022-06-14 12:10:17.682521
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com/foo")=="<a href=\"http://example.com/foo\">http://example.com/foo</a>","http://example.com/foo"
    assert linkify("hello http://example.com/")=="hello <a href=\"http://example.com/\">http://example.com/</a>","hello http://example.com/"
    assert linkify("http://example.com/foo?arg=value")=="<a href=\"http://example.com/foo?arg=value\">http://example.com/foo?arg=value</a>","http://example.com/foo?arg=value"

# Generated at 2022-06-14 12:10:27.535157
# Unit test for function linkify
def test_linkify():
    test_cases = [
        # (test_input, test_expect)
        ("elao", "elao"),
        ("hello www.elao.com", 'hello <a href="http://www.elao.com">www.elao.com</a>'),
        ("hello http://www.elao.com", 'hello <a href="http://www.elao.com">http://www.elao.com</a>'),
        ("hello http://www.elao.com/salut/tout/le/monde", 'hello <a href="http://www.elao.com/salut/tout/le/monde">http://www.elao.com/salut/tout/le/mon...</a>'),
    ]

# Generated at 2022-06-14 12:10:29.663570
# Unit test for function linkify
def test_linkify():
    a=linkify("www.baidu.com")
    print(a)
    print(type(a))
    return a


# Generated at 2022-06-14 12:10:41.409154
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com") == '<a href="http://foo.com">http://foo.com</a>'
    assert linkify("foo@bar.com") == '<a href="mailto:foo@bar.com">foo@bar.com</a>'
    assert linkify("mailto:foo@bar.com") == '<a href="mailto:foo@bar.com">mailto:foo@bar.com</a>'
    assert linkify("google.com") == '<a href="http://google.com">google.com</a>'
    assert linkify("hello:world") == 'hello:world'
    assert linkify("hello:world", require_protocol=True) == 'hello:world'
    assert linkify("hello:world", permitted_protocols=["mailto"])

# Generated at 2022-06-14 12:10:50.759130
# Unit test for function linkify
def test_linkify():
    msg = '''This is an example of a long link:
    http://example.com/blog/post/1/a-very-nice-blog-post-indeed?
    query=yes&another_query=true
    '''
    assert linkify(msg) == '''This is an example of a long link:
    <a href="http://example.com/blog/post/1/a-very-nice-blog-post-indeed?"
    query=yes&amp;another_query=true>
    http://example.com/blog/post/1/a-very-nice-blog-post-indeed?
    query=yes&amp;another_query...
    </a>
    '''



# Generated at 2022-06-14 12:10:54.147359
# Unit test for function linkify
def test_linkify():
    """
    >>> test_linkify()
    '<a href="http://tornadoweb.org">http://tornadoweb.org</a> <a href="http://zh.wikipedia.org">http://zh.wikipedia.org</a>'
    """
    return linkify("Hello http://tornadoweb.org! http://zh.wikipedia.org")

# end unit test



# Generated at 2022-06-14 12:11:10.904804
# Unit test for function linkify

# Generated at 2022-06-14 12:11:17.264327
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com extra") == '<a href="http://example.com">http://example.com</a> extra'
    assert linkify("go to http://example.com") == 'go to <a href="http://example.com">http://example.com</a>'

    # Don't linkify if there is no protocol
    assert linkify("go to www.example.com", require_protocol=True) == 'go to www.example.com'
    assert linkify("go to www.example.com", require_protocol=False) == 'go to <a href="http://www.example.com">www.example.com</a>'

    # Don't link

# Generated at 2022-06-14 12:11:29.358690
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    short_url = "http://www.facebook.com/l/7AQE65h7V/1.usa.gov/wfLQtf"
    long_url = "http://example.webscraping.com/places/default/view/Aland-Islands-2"
    text_linkified = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    short_linkified = '<a href="http://www.facebook.com/l/7AQE65h7V/1.usa.gov/wfLQtf" title="http://www.facebook.com/l/7AQE65h7V/1.usa.gov/wfLQtf">http://www...</a>'

# Generated at 2022-06-14 12:11:34.657785
# Unit test for function linkify
def test_linkify():
    input = "http://example.com https://example2.com example3.com/foo/bar www.example4.com"
    output = linkify(input)
    expected = '<a href="http://example.com">http://example.com</a> <a href="https://example2.com">https://example2.com</a> <a href="http://example3.com/foo/bar">example3.com/foo/bar</a> <a href="http://www.example4.com">www.example4.com</a>'
    assert output == expected



# Generated at 2022-06-14 12:11:47.994898
# Unit test for function linkify
def test_linkify():
    assert linkify("foo") == "foo"
    assert linkify("foo http://www.example.com/blah blah blah blah blah blah blah blah blah blah") == "foo <a href=\"http://www.example.com/blah\">http://www.example.com/blah</a> blah blah blah blah blah blah blah blah blah"
    # https://github.com/tornadoweb/tornado/issues/1373
    assert linkify("foo example.com") == "foo example.com"
    assert linkify("foo <example.com>") == "foo &lt;example.com&gt;"
    assert linkify("foo https://example.com") == "foo <a href=\"https://example.com\">https://example.com</a>"

# Generated at 2022-06-14 12:11:58.860110
# Unit test for function linkify
def test_linkify():
    assert linkify('hello') == 'hello'
    assert linkify('hello there http://www.example.com') == 'hello there <a href="http://www.example.com">http://www.example.com</a>'
    assert linkify('hello there http://www.example.com/') == 'hello there <a href="http://www.example.com/">http://www.example.com/</a>'
    assert linkify('hello there http://www.example.com?test=1') == 'hello there <a href="http://www.example.com?test=1">http://www.example.com?test=1</a>'

# Generated at 2022-06-14 12:12:13.974576
# Unit test for function linkify
def test_linkify():
    text = """
    This is an example of linkify http://example.com,
    www.example.com and sub1.example.com/page,
    as well as a mailto:test@example.com.
    """
    result = 'This is an example of linkify <a href="http://example.com">http://example.com</a>,\n' \
             '<a href="http://www.example.com">www.example.com</a> and <a href="http://sub1.example.com/page">sub1.example.com/page</a>,\n' \
             'as well as a <a href="mailto:test@example.com">mailto:test@example.com</a>.'
    assert result == linkify(text)


if __name__ == "__main__":
    test

# Generated at 2022-06-14 12:12:18.828238
# Unit test for function linkify
def test_linkify():
    assert 'golang' in linkify(u'http://golang.org')
    assert linkify('/foo/') == '/foo/'
test_linkify()



# Generated at 2022-06-14 12:12:26.937379
# Unit test for function linkify
def test_linkify():
    text = 'hello http://www.google.com'
    result = linkify(text)
    print(result)
    text = 'hello https://blog.lilydjwg.me/2013/03/25/escape-html-in-python.14376.html'
    result = linkify(text)
    print(result)
    text = 'hello https://blog.lilydjwg.me/2013/03/25/escape-html-in-python.14376.html and https://www.google.com'
    result = linkify(text)
    print(result)


# Generated at 2022-06-14 12:12:37.760260
# Unit test for function linkify
def test_linkify():
    assert(linkify("foo") == "foo")
    assert(linkify("foo http://foo.com bar") == 'foo <a href="http://foo.com">http://foo.com</a> bar')
    assert(linkify("foo http://foo.com bar", require_protocol=True) == 'foo http://foo.com bar')
    assert(linkify("foo http://foo.com bar", require_protocol=True, permitted_protocols=["http"]) == 'foo <a href="http://foo.com">http://foo.com</a> bar')

# Generated at 2022-06-14 12:12:52.672947
# Unit test for function linkify

# Generated at 2022-06-14 12:13:04.633636
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == \
        '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("http://www.example.com/foo?bar=baz&blah=%20") == \
        '<a href="http://www.example.com/foo?bar=baz&blah=%20">http://www.example.com/foo?bar=baz&blah=%20</a>'

# Generated at 2022-06-14 12:13:15.696500
# Unit test for function linkify
def test_linkify():
    text = """Hello, linkify
    @someone, http://example.com, https://example.com,
    http://www.example.com, http://example.com/bar, http://example.com/baz#quux,
    http://example.com/a%20b, http://foo.example.com/
    http://example.com/a?a=b&c=d,
    http://user:pass@example.com/
    http://example.com/a#!b
    Please mail foo@example.com
    """

# Generated at 2022-06-14 12:13:21.628179
# Unit test for function linkify
def test_linkify():
    text = 'this is a link http://example.com/'
    result = 'this is a link <a href="http://example.com/">http://example.com/</a>'
    assert linkify(text) == result

# Generated at 2022-06-14 12:13:32.698895
# Unit test for function linkify
def test_linkify():
    test_cases = [
        ("http://www.tornadoweb.org", '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'),
        (
            "Hello http://www.tornadoweb.org world",
            'Hello <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a> world',
        ),
        ("Hello www.tornadoweb.org world", 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a> world')
    ]
    for arg, expected in test_cases:
        assert linkify(arg) == expected



# Generated at 2022-06-14 12:13:43.617240
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == (
        u'<a href="http://example.com">http://example.com</a>'
    )
    assert linkify("http://example.com", shorten=True) == (
        u'<a href="http://example.com" title="http://example.com">'
        u'http://example.com</a>'
    )
    assert linkify("http://example.com/foo/bar") == (
        u'<a href="http://example.com/foo/bar">'
        u'http://example.com/foo/bar</a>'
    )

# Generated at 2022-06-14 12:13:46.150484
# Unit test for function linkify
def test_linkify():
    text = "http://twitter.com/twitter"
    assert linkify(text) == "http://twitter.com/twitter"



# Generated at 2022-06-14 12:13:54.109523
# Unit test for function linkify
def test_linkify():
    assert linkify(b'Hello World!') == 'Hello World!', "linkify(b'Hello World!')"
    assert linkify(u'Hello World!') == u'Hello World!', "linkify(u'Hello World!')"
    assert (
        linkify('Go to <a href="http://www.google.com">www.google.com</a>') ==
        'Go to <a href="http://www.google.com">www.google.com</a>',
        "linkify('Go to <a href=\"http://www.google.com\">www.google.com</a>')"
    )

# Generated at 2022-06-14 12:14:02.704383
# Unit test for function linkify
def test_linkify():
    print(linkify('http://baidu.com'))
    print(linkify('www.baidu.com'))
    print(linkify('www.baidu.com', require_protocol=True))
    print(linkify('66tms.com', require_protocol=True))
    print(linkify('66tms.com'))
    print(linkify('&lt;66tms.com&gt;'))
    print(linkify('<66tms.com>'))


# Shortcut for string substitution and logging commonly-used messages
# (accesses settings as a global)

# Generated at 2022-06-14 12:14:13.369287
# Unit test for function linkify

# Generated at 2022-06-14 12:14:26.586785
# Unit test for function linkify
def test_linkify():
    assert linkify('normal text') == 'normal text'
    assert linkify('http://example.com/') == '<a href="http://example.com/">http://example.com/</a>'
    assert linkify('http://example.com/') == '<a href="http://example.com/">http://example.com/</a>'
    assert linkify('http://example.com/', shorten=True) == '<a href="http://example.com/">http://exa...</a>'
    assert linkify('http://example.com/long-path/') == '<a href="http://example.com/long-path/">http://example.com/long-path/</a>'

# Generated at 2022-06-14 12:14:41.613580
# Unit test for function linkify
def test_linkify():
    text = 'Link: http://www.tornadoweb.org/en/stable/'
    assert linkify(text) == 'Link: <a href="http://www.tornadoweb.org/en/stable/">http://www.tornadoweb.org/en/stable/</a>'
    text = 'Link: http://www.tornadoweb.org/en/stable/#hello-world'
    assert linkify(text) == 'Link: <a href="http://www.tornadoweb.org/en/stable/#hello-world">http://www.tornadoweb.org/en/stable/#hello-world</a>'
    text = 'Link: http://www.tornadoweb.org/en/stable/#hello-world and http://www.tornadoweb.org/en/stable/#other-stuff'

# Generated at 2022-06-14 12:14:49.073578
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com/foo&bar") == '<a href="http://www.example.com/foo&amp;bar">http://www.example.com/foo&amp;bar</a>'
    assert linkify("www.example.com/foo&bar") == '<a href="http://www.example.com/foo&amp;bar">www.example.com/foo&amp;bar</a>'
    assert linkify("foo&bar") == 'foo&amp;bar'
    assert linkify('<a href="http://www.example.com/">http://www.example.com/</a>') == '<a href="http://www.example.com/">http://www.example.com/</a>'

# Generated at 2022-06-14 12:15:00.747344
# Unit test for function linkify
def test_linkify():
    import pytest
    from tornado.util import linkify
    ## Testcases input

# Generated at 2022-06-14 12:15:08.501633
# Unit test for function linkify
def test_linkify():
    text = "See https://tools.ietf.org/html/rfc7231#section-6.5.14"
    assert linkify(text) == 'See <a href="https://tools.ietf.org/html/rfc7231#section-6.5.14">https://tools.ietf.org/html/rfc7231#section-6.5.14</a>'


# When dealing with the standard library across python 2 and 3 it is
# sometimes useful to have a direct conversion to the native string type
if bytes is not str:  # python 2
    native_str = to_unicode
else:
    native_str = to_basestring


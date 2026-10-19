

# Generated at 2022-06-14 12:05:30.191298
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    g  = linkify(text)
    assert g == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"

# Generated at 2022-06-14 12:05:42.810875
# Unit test for function linkify
def test_linkify():
    try:
        import unittest.mock as mock
    except ImportError:
        import mock
    import mock

    def test_urls(urls):
        for url in urls:
            yield url, url

    def test_urls_extra_params(urls, extra_params):
        for url in urls:
            expected = url
            if extra_params:
                expected = url[:-1] + " " + extra_params + ">"
            yield url, expected

    def test_urls_extra_params_cb(urls, extra_params_cb):
        for url in urls:
            expected = url
            href = url[url.find('"') + 1 : url.rfind('"')]  # extract href
            if extra_params_cb:
                extra_params = extra_params_

# Generated at 2022-06-14 12:05:56.686997
# Unit test for function linkify
def test_linkify():
    assert linkify('http://www.google.com') == '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify('<a href="http://www.google.com">http://www.google.com</a>') == '&lt;a href=&quot;http://www.google.com&quot;&gt;http://www.google.com&lt;/a&gt;'
    assert linkify('<a href="http://www.google.com">google</a>') == '&lt;a href=&quot;http://www.google.com&quot;&gt;google&lt;/a&gt;'

# Generated at 2022-06-14 12:06:06.766324
# Unit test for function linkify
def test_linkify():
    # linkify 
    text = linkify("Hello http://tornadoweb.org!")
    assert text=='Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    # test extra_params
    text = linkify("Hello www.tornadoweb.org!", extra_params='rel="nofollow" class="external"')
    assert text=='Hello <a href="http://www.tornadoweb.org" rel="nofollow" class="external">www.tornadoweb.org</a>!'
    # test require_protocol
    text = linkify("Hello www.tornadoweb.org!", extra_params='rel="nofollow" class="external"',require_protocol=True)
    assert text=='Hello www.tornadoweb.org!'
    # test permitted_

# Generated at 2022-06-14 12:06:18.174471
# Unit test for function linkify
def test_linkify():
    assert linkify('http://example.com') == '<a href="http://example.com">http://example.com</a>'
    assert linkify('hello http://example.com') == 'hello <a href="http://example.com">http://example.com</a>'
    assert linkify('hello <a href="http://example.com">http://example.com</a>') == 'hello <a href="http://example.com">http://example.com</a>'



# Generated at 2022-06-14 12:06:27.099705
# Unit test for function linkify
def test_linkify():
    # Test with require_protocol=False
    assert linkify("mydomain.com") == '<a href="http://mydomain.com">mydomain.com</a>'
    assert linkify("www.mydomain.com") == '<a href="http://www.mydomain.com">www.mydomain.com</a>'
    assert linkify("//mydomain.com") == '<a href="http://mydomain.com">mydomain.com</a>'
    assert linkify("http://mydomain.com") == '<a href="http://mydomain.com">http://mydomain.com</a>'
    assert linkify("https://mydomain.com") == '<a href="https://mydomain.com">https://mydomain.com</a>'
    assert linkify("mydomain.com/mypath")

# Generated at 2022-06-14 12:06:33.921429
# Unit test for function linkify
def test_linkify():
    text = "python is great http://www.google.com"
    assert '<a href="http://www.google.com">' in linkify(text)
    assert '<a href="https://www.google.com">' in linkify(text,permitted_protocols=["http","https"] )
    text = "python is great www.google.com"
    assert '<a href="http://www.google.com">' in linkify(text,require_protocol=True)
    assert len(linkify(text))> len(text)
    assert len(linkify(text,shorten=True))< len(text)
    assert '<a href="http://www.google.com">' in linkify(text,permitted_protocols=["http","https"])


# Generated at 2022-06-14 12:06:44.732574
# Unit test for function linkify
def test_linkify():
    assert(linkify("Hello http://tornadoweb.org!") == \
        "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
    assert(linkify("Hello https://tornadoweb.org!") == \
        "Hello <a href=\"https://tornadoweb.org\">https://tornadoweb.org</a>!")
    assert(linkify("Hello www.tornadoweb.org!") == \
        "Hello <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>!")
    assert(linkify("Hello http://www.tornadoweb.org!") == \
        "Hello <a href=\"http://www.tornadoweb.org\">http://www.tornadoweb.org</a>!")

# Generated at 2022-06-14 12:06:57.679034
# Unit test for function linkify
def test_linkify():
    assert (
        linkify(
            "Hello https://tornadoweb.org/en/stable/#hello-world!",
            extra_params='rel="nofollow"',
        )
        == 'Hello <a href="https://tornadoweb.org/en/stable/#hello-world!" rel="nofollow">https://tornadoweb.org/en/stable/#hello-world!</a>'
    )

# Generated at 2022-06-14 12:07:00.791080
# Unit test for function linkify
def test_linkify():
    s = "<p>You can get more information at <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>.</p>"
    assert linkify("You can get more information at www.tornadoweb.org.") == s


# Generated at 2022-06-14 12:07:11.063706
# Unit test for function linkify
def test_linkify():
    assert linkify("http://x.co") == u'<a href="http://x.co">http://x.co</a>'
# end unit test and testing code
#assert test_linkify() == None



# Generated at 2022-06-14 12:07:21.436213
# Unit test for function linkify
def test_linkify():
    assert (
        linkify(to_unicode("http://www.google.com"))
        == u'<a href="http://www.google.com">http://www.google.com</a>'
    )
    assert linkify(to_unicode("www.google.com")) == u'<a href="http://www.google.com">www.google.com</a>'
    assert (
        linkify(to_unicode("Hello http://www.google.com!"))
        == u'Hello <a href="http://www.google.com">http://www.google.com</a>!'
    )

# Generated at 2022-06-14 12:07:28.819162
# Unit test for function linkify
def test_linkify():
    text = "asdfasdf http://example.com/ asdfasdf"
    assert(
        linkify(text) == 'asdfasdf <a href="http://example.com/">http://example.com/</a> asdfasdf'
    )
    assert(
        linkify(text, shorten=True) == 'asdfasdf <a href="http://example.com/">http://example.com/</a> asdfasdf'
    )
    assert(
        linkify(text, shorten=True, extra_params="rel='nofollow'")
        == "asdfasdf <a href='http://example.com/' rel='nofollow'>http://example.com/</a> asdfasdf"
    )



# Generated at 2022-06-14 12:07:38.667386
# Unit test for function linkify

# Generated at 2022-06-14 12:07:43.398263
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    desired_result = "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    assert desired_result == linkify(text) == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"


# Generated at 2022-06-14 12:07:55.504800
# Unit test for function linkify
def test_linkify():
    text=linkify(
        "Hello http://tornadoweb.org!",
        shorten=False,
        extra_params=None,
        require_protocol=False,
        permitted_protocols=None,
    )
    text2=linkify(
        "Hello http://tornadoweb.org!",
        shorten=True,
        extra_params='rel="nofollow" class="external"',
        require_protocol=True,
        permitted_protocols=["http", "https"],
    )
    text3 = linkify(
        "Hello http://tornadoweb.org!",
        shorten=False,
        extra_params=None,
        require_protocol=True,
        permitted_protocols=["http", "https"],
    )

# Generated at 2022-06-14 12:08:05.271318
# Unit test for function linkify
def test_linkify():
    assert linkify(u"http://www.facebook.com") == u'<a href="http://www.facebook.com">http://www.facebook.com</a>'
    assert linkify(u"http://www.facebook.com/abc") == u'<a href="http://www.facebook.com/abc">http://www.facebook.com/abc</a>'
    assert linkify(u"http://www.facebook.com/abc?a=123") == u'<a href="http://www.facebook.com/abc?a=123">http://www.facebook.com/abc?a=123</a>'

# Generated at 2022-06-14 12:08:12.139559
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""

    text = "http://www.example.com"
    assert linkify(text) == u'<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify(text, shorten=True) == u'<a href="http://www.example.com">http://www.example.c...</a>'

    text = "hello http://www.example.com world"
    assert linkify(text) == u'hello <a href="http://www.example.com">http://www.example.com</a> world'

    text = "http://www.example.com/foo?bar=baz&ding=dong#quux"

# Generated at 2022-06-14 12:08:18.876885
# Unit test for function linkify
def test_linkify():
    assert linkify("foo http://www.facebook.com/ bar") == 'foo <a href="http://www.facebook.com/">http://www.facebook.com/</a> bar'
    assert linkify("foo https://www.facebook.com/ bar") == 'foo <a href="https://www.facebook.com/">https://www.facebook.com/</a> bar'
    assert linkify("foo www.facebook.com/ bar") == 'foo <a href="http://www.facebook.com/">www.facebook.com/</a> bar'
    assert linkify("foo http://www.facebook.com/#!/foo bar") == 'foo <a href="http://www.facebook.com/#!/foo">http://www.facebook.com/#!/foo</a> bar'

# Generated at 2022-06-14 12:08:24.794658
# Unit test for function linkify
def test_linkify():
    # 调用linkify函数
    print(linkify("Hello www.tornadoweb.org!", shorten=True))
    # print(linkify("Hello www.tornadoweb.org"))
    # print(linkify("Hello www.tornadoweb.org", short=True))
    # assert linkify("w3c") == "w3c"
    # assert linkify("http://w3c") == "<a href='http://w3c'>http://w3c</a>"
    # assert linkify("www.w3c") == "<a href='http://w3c'>http://w3c</a>"
    # assert linkify("http://w3c.org?param=1") == "<a href='http://w3c.org?param=1'>http://w3c.org?param=1

# Generated at 2022-06-14 12:08:36.323575
# Unit test for function linkify
def test_linkify():
    text = "http://www.google.com/ GOOGLE http://www.baidu.com/"
    res = linkify(text)
    print(res)
    assert res == '<a href="http://www.google.com/">http://www.google.com/</a> GOOGLE <a href="http://www.baidu.com/">http://www.baidu.com/</a>'



# Generated at 2022-06-14 12:08:41.505521
# Unit test for function linkify
def test_linkify():
    assert(linkify("hello, world") == "hello, world")
    assert(linkify("hello, http://www.world.com/") == "hello, <a href=\"http://www.world.com/\">http://www.world.com/</a>")
    assert(linkify("http://www.world.com/") == "<a href=\"http://www.world.com/\">http://www.world.com/</a>")
    assert(linkify("http://www.world.com/index.html") == "<a href=\"http://www.world.com/index.html\">http://www.world.com/index.html</a>")
test_linkify()



# Generated at 2022-06-14 12:08:51.848107
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("https://www.example.com") == '<a href="https://www.example.com">https://www.example.com</a>'
    assert linkify("Hello http://www.example.com") == 'Hello <a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("<p>http://www.example.com</p>") == '<p><a href="http://www.example.com">http://www.example.com</a></p>'

# Generated at 2022-06-14 12:08:58.249835
# Unit test for function linkify
def test_linkify():
    def assert_linkify(text, expected):
        assert linkify(text) == expected
        assert linkify(' <"%s"> ' % text, extra_params='rel="nofollow"') == (' <a href="%s" rel="nofollow">%s</a> ' % (text, text))
        assert linkify(text, short_url = False) == expected

    assert_linkify('http://x/', '<a href="http://x/">http://x/</a>')
    assert_linkify('abc http://x/', 'abc <a href="http://x/">http://x/</a>')
    assert_linkify('http://example.com/~user', '<a href="http://example.com/~user">http://example.com/~user</a>')
    assert_link

# Generated at 2022-06-14 12:09:07.748961
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'
    assert linkify("www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    assert linkify("Hello http://www.tornadoweb.org!") == 'Hello <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>!'
    assert linkify("Visit http://www.tornadoweb.org/ today!") == 'Visit <a href="http://www.tornadoweb.org/">http://www.tornadoweb.org/</a> today!'

# Generated at 2022-06-14 12:09:13.257015
# Unit test for function linkify
def test_linkify():
  s = '对，就是这么高效 http://www.baidu.com'
  assert linkify(s) == '对，就是这么高效 <a href="http://www.baidu.com">http://www.baidu.com</a>'



# Generated at 2022-06-14 12:09:23.940385
# Unit test for function linkify
def test_linkify():
    assert linkify('hello http://example.com') == 'hello <a href="http://example.com">http://example.com</a>'
    # linkify doesn't mess up at ampersands
    assert linkify('go to http://example.com/foo?bar=baz&alt=quux') == \
        'go to <a href="http://example.com/foo?bar=baz&amp;alt=quux">http://example.com/foo?bar=baz&amp;alt=quux</a>'
    # linkify doesn't linkify email addresses
    assert linkify('send to foo@example.com') == \
        'send to <a href="mailto:foo@example.com">foo@example.com</a>'

# Generated at 2022-06-14 12:09:35.589895
# Unit test for function linkify
def test_linkify():
    text = "My twitter http://twitter.com/myaccount"
    expected = "My twitter <a href=\"http://twitter.com/myaccount\">http://twitter.com/myaccount</a>"
    assert(linkify(text, shorten=True)) == expected
    assert(linkify(text)) == expected
    text = "My twitter http://twitter.com/myaccount and my instagram http://instagram.com/myaccount"
    expected = "My twitter <a href=\"http://twitter.com/myaccount\">http://twitter.com/myaccount</a> and my instagram <a href=\"http://instagram.com/myaccount\">http://instagram.com/myaccount</a>"
    assert(linkify(text, shorten=True)) == expected
    assert(linkify(text)) == expected

# Generated at 2022-06-14 12:09:45.121861
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ''
    assert linkify('') == ''
    assert linkify('Hello') == 'Hello'
    assert (linkify('Hello http://tornadoweb.org!') ==
            'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!')
    assert (linkify('http://example.com') ==
            '<a href="http://example.com">http://example.com</a>')
    assert (linkify('Hello www.tornadoweb.org nice to meet you!') ==
            'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
            ' nice to meet you!')

# Generated at 2022-06-14 12:09:48.096772
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))


_NON_WORD_RE = re.compile(r"[^\w\- ]+")



# Generated at 2022-06-14 12:10:14.138597
# Unit test for function linkify
def test_linkify():
    assert(linkify("www.example.com") == u'<a href="http://www.example.com">www.example.com</a>')
    assert(linkify("Hello http://tornadoweb.org!") == u'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!')
    assert(linkify('<a href="faq.html">FAQ</a>') == u'&lt;a href=&quot;faq.html&quot;&gt;FAQ&lt;/a&gt;')

# Generated at 2022-06-14 12:10:25.606964
# Unit test for function linkify
def test_linkify():
    assert linkify("foo http://example.com bar") == 'foo <a href="http://example.com">http://example.com</a> bar'
    assert linkify("hello www.google.com") == 'hello <a href="http://www.google.com">www.google.com</a>'
    assert linkify("hello www.google.com") == 'hello <a href="http://www.google.com">www.google.com</a>'
    assert linkify("hello example.com") == 'hello <a href="http://example.com">example.com</a>'
    assert linkify("hi ftp://example.com") == 'hi <a href="ftp://example.com">ftp://example.com</a>'

# Generated at 2022-06-14 12:10:36.191400
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify('test www.example.com test') == 'test <a href="http://www.example.com">www.example.com</a> test'
    test_example_dot_com = 'test <a href="http://www.example.com">www.example.com</a> test'
    assert linkify('test www.example.com test', require_protocol=True) == test_example_dot_com
    assert linkify('test www.example.com test', permitted_protocols=["http", "https"]) == test_example_dot_com

# Generated at 2022-06-14 12:10:40.836964
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://www.google.com"))
    print(linkify("Hello http://www.google.com", extra_params=lambda url: "target=_blank"))


if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:10:51.133681
# Unit test for function linkify
def test_linkify():
    assert (
        linkify("http://example.com/")
        == '<a href="http://example.com/" rel="nofollow">http://example.com/</a>'
    )
    assert linkify("Hello www.example.com") == 'Hello <a href="http://www.example.com" rel="nofollow">www.example.com</a>'
    assert linkify("Do not http://www.example.com") == 'Do not <a href="http://www.example.com" rel="nofollow">http://www.example.com</a>'
    assert linkify("Testing https://www.example.com") == 'Testing <a href="https://www.example.com" rel="nofollow">https://www.example.com</a>'

# Generated at 2022-06-14 12:10:57.161706
# Unit test for function linkify
def test_linkify():
    # Test make_link
    x = linkify('http://foo.com')
    assert x == '<a href="http://foo.com">http://foo.com</a>', x
    x = linkify('www.foo.com')
    assert x == '<a href="http://www.foo.com">www.foo.com</a>', x
    x = linkify('www.foo.com', require_protocol=True)
    assert x == 'www.foo.com', x
    x = linkify('http://foo.com/foo?bar=1')
    assert x == '<a href="http://foo.com/foo?bar=1">http://foo.com/foo?bar=1</a>', x

# Generated at 2022-06-14 12:10:59.824532
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://tornadoweb.org!'
    result = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify(text) == result


# Generated at 2022-06-14 12:11:11.421415
# Unit test for function linkify
def test_linkify():
    test = "Text with a link: https://www.tornadoweb.org/"
    assert "Text with a link: " in test
    assert "https://www.tornadoweb.org/" in test
    assert linkify(test) == 'Text with a link: <a href="https://www.tornadoweb.org/">https://www.tornadoweb.org/</a>'  # noqa: E501
    test = "Text with a link: (www.tornadoweb.org)"
    assert "Text with a link: " in test
    assert "(www.tornadoweb.org)" in test
    assert linkify(test) == 'Text with a link: (<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>)'  # noqa: E501

# Generated at 2022-06-14 12:11:23.267674
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("test http://www.example.com/foo bar") == 'test <a href="http://www.example.com/foo">http://www.example.com/foo</a> bar'
    assert """test <a href="http://www.example.com/foo">http://www.example.com/foo</a> bar""" == linkify("test http://www.example.com/foo bar")

# Generated at 2022-06-14 12:11:32.384744
# Unit test for function linkify
def test_linkify():
    import time
    import re

# Generated at 2022-06-14 12:12:09.174642
# Unit test for function linkify
def test_linkify():
    text = "@hello @world"
    before = text
    after = linkify(text)
    assert len(after) > len(before)
    assert re.search(r"@hello.*?<a href=.*?>world</a>", after)




# Generated at 2022-06-14 12:12:18.046911
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == u'<a href="http://google.com">http://google.com</a>'
    assert linkify("www.google.com") == u'<a href="http://www.google.com">www.google.com</a>'
    assert linkify("https://google.com") == u'<a href="https://google.com">https://google.com</a>'
    assert linkify("foo@bar.com") == u'<a href="mailto:foo@bar.com">foo@bar.com</a>'
    assert linkify("http://google.com?x=\u00a2") == u'<a href="http://google.com?x=\u00a2">http://google.com?x=\u00a2</a>'


# Generated at 2022-06-14 12:12:28.470285
# Unit test for function linkify
def test_linkify():
    assert linkify(
        "http://example.com"
    ) == '<a href="http://example.com">http://example.com</a>'

    assert linkify(
        "http://example.com?q=test"
    ) == '<a href="http://example.com?q=test">http://example.com?q=test</a>'
    assert linkify(
        "http://example.com?q=test", shorten=True
    ) == '<a href="http://example.com?q=test">http://example.com?q=...</a>'


# Generated at 2022-06-14 12:12:39.376407
# Unit test for function linkify
def test_linkify():
    _test_text = "Go to http://www.google.com/\n"
    _test_text += "Go to http://www.google.com/ #hello\n"
    _test_text += "Go to http://www.google.com/?hello=world\n"
    _test_text += "Go to https://www.google.com/?hello=world\n"
    _test_text += "Go to http://www.google.com/?hello=world#something\n"
    _test_text += "Go to http://www.google.com/search?q=this+is+a+search+query\n"
    _test_text += "Go to www.google.com\n"

# Generated at 2022-06-14 12:12:51.114043
# Unit test for function linkify
def test_linkify():
    x = linkify('Hello http://tornadoweb.org!')
    assert x == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!', x
    x = linkify('Hello <http://tornadoweb.org>!')
    assert x == 'Hello &lt;<a href="http://tornadoweb.org">http://tornadoweb.org</a>&gt;!', x
    x = linkify('Go to http://www.facebook.com/events/327365550643657/')
    assert '<a href="http://www.facebook.com/events/327365550643657/">http://www.facebook.com/events/327365550643657/</a>' in x, x

# Generated at 2022-06-14 12:12:57.894982
# Unit test for function linkify
def test_linkify():
    #print(linkify(text))
    text = "Check out http://tornadoweb.org"
    assert linkify(text) == u'Check out <a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    text = "http://tornadoweb.org is a Python library."
    assert linkify(text) == u'<a href="http://tornadoweb.org">http://tornadoweb.org</a> is a Python library.'
    text = "http://twitter.com/hoverbird"
    assert linkify(text) == u'<a href="http://twitter.com/hoverbird">http://twitter.com/hoverbird</a>'
    text = "www.wikipedia.org"

# Generated at 2022-06-14 12:13:06.999275
# Unit test for function linkify
def test_linkify():
    # Simple case.
    text = linkify("Hello http://tornadoweb.org!")
    assert text == (
        'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    )

    # Test with a custom extra param.
    text = linkify("Hello http://tornadoweb.org!", extra_params='rel="nofollow"')
    assert text == (
        'Hello <a href="http://tornadoweb.org" rel="nofollow">'
        "http://tornadoweb.org</a>!"
    )

    # Test with a custom callable extra param.
    def extra_params_cb(url):
        if url.startswith("http://tornadoweb.org"):
            return 'class="internal"'

# Generated at 2022-06-14 12:13:18.807856
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    assert( linkify(text) == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
    text = "Hello www.tornadoweb.org!"
    assert( linkify(text) == "Hello <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>!")
    text = "Hello http://www.tornadoweb.org!"
    assert( linkify(text) == "Hello <a href=\"http://www.tornadoweb.org\">http://www.tornadoweb.org</a>!")
    text = "Hello http://www.tornadoweb.org!"

# Generated at 2022-06-14 12:13:32.709414
# Unit test for function linkify
def test_linkify():
    print(linkify(text = "My blog is http://www.example.com/", shorten = False))
    print(linkify(text = "My blog is http://www.example.com/", shorten = True))
    print(linkify(text = "My blog is www.example.com", shorten = True))
    print(linkify(text = "My blog is www.example.com", shorten = False))
    print(linkify(text = "My blog is https://www.example.com/", shorten = True))
    print(linkify(text = "My blog is http://www.example.com/", shorten = False, require_protocol = False))
    print(linkify(text = "My blog is http://www.example.com/", shorten = True, require_protocol = False))

# Generated at 2022-06-14 12:13:38.533842
# Unit test for function linkify
def test_linkify():
    result = tornado.escape.linkify(u"Hello http://tornadoweb.org!")
    assert result == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'

    result = tornado.escape.linkify(u"Hello www.tornadoweb.org!", require_protocol=False)
    assert result == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!'

    result = tornado.escape.linkify(u"Hello http://www.tornadoweb.org!")
    assert result == 'Hello <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>!'


# Generated at 2022-06-14 12:14:53.280949
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))
    print(linkify("Hello www.tornadoweb.org!", require_protocol=True))
    print(linkify("Hello http://github.com/tornadoweb", shorten=True))
    print(linkify("Hello http://github.com/tornadoweb", require_protocol=True, shorten=True))
    print(linkify("Hello http://github.com/tornadoweb", require_protocol=True, shorten=True, extra_params='rel="nofollow"'))
    print(linkify("Hello http://github.com/tornadoweb", require_protocol=True, shorten=True, extra_params='rel="nofollow" class="external"'))

# Generated at 2022-06-14 12:15:03.304546
# Unit test for function linkify
def test_linkify():
    assert '<a href="http://www.yahoo.com/">http://www.yahoo.com/</a>' == linkify("http://www.yahoo.com/")
    assert '<a href="http://www.yahoo.com/">www.yahoo.com</a>' == linkify("www.yahoo.com")
    assert '<a href="http://www.yahoo.com/">Yahoo</a>' == linkify("Yahoo (http://www.yahoo.com/)")
    assert '<a href="http://www.yahoo.com/">http://www.yahoo.com/</a>' == linkify("<http://www.yahoo.com/>")
    # Be careful with '#' in links
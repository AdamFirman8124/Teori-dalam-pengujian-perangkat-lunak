

# Generated at 2022-06-14 12:05:24.193113
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.foxnews.com") == '<a href="http://www.foxnews.com">http://www.foxnews.com</a>'
    assert linkify("http://www.foxnews.com/") == '<a href="http://www.foxnews.com/">http://www.foxnews.com/</a>'
    assert linkify("www.foxnews.com") == '<a href="http://www.foxnews.com">www.foxnews.com</a>'
    assert linkify("http://www.foxnews.com/foo") == '<a href="http://www.foxnews.com/foo">http://www.foxnews.com/foo</a>'

# Generated at 2022-06-14 12:05:32.960802
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'  # noqa: E501
    assert linkify("http://www.example.com/") == '<a href="http://www.example.com/">http://www.example.com/</a>'  # noqa: E501
    assert linkify("http://www.example.com:8000/foo") == '<a href="http://www.example.com:8000/foo">http://www.example.com:8000/foo</a>'  # noqa: E501
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'  # noqa: E501
    assert linkify

# Generated at 2022-06-14 12:05:37.883289
# Unit test for function linkify
def test_linkify():
    expect = '<a href="http://www.example.com">www.example.com</a>'
    actual = linkify('www.example.com')
    assert expect == actual
    
test_linkify()


# peekable is a backport of itertools.peekable, available in python 3.1+

# Generated at 2022-06-14 12:05:47.117709
# Unit test for function linkify
def test_linkify():
    global linkify

    text = "http://example.com"
    assert linkify(text) == "<a href=\"http://example.com\">http://example.com</a>"

    text = "http://example.com/"
    assert linkify(text) == "<a href=\"http://example.com/\">http://example.com/</a>"

    text = "Example text with no link"
    assert linkify(text) == "Example text with no link"

    text = "Example text with no link and http://example.com"
    assert linkify(text) == "Example text with no link and <a href=\"http://example.com\">http://example.com</a>"

    text = "Example text with no link, a http://example.com and http://another.example.com"

# Generated at 2022-06-14 12:06:01.029209
# Unit test for function url_unescape
def test_url_unescape():
    assert url_unescape("simple") == "simple"
    assert url_unescape("a+b") == "a b"
    assert url_unescape("a+b", plus=False) == "a+b"
    assert url_unescape("%7Easdf") == "~asdf"
    assert url_unescape("%7Easdf", encoding=None) == b"~asdf"
    assert url_unescape("%E4%BD%A0%E5%A5%BD") == u"你好"
    assert url_unescape("%E4%BD%A0%E5%A5%BD", encoding="utf-8") == u"你好"
    assert url_unescape("%E4%BD%A0%E5%A5%BD", encoding="gbk")

# Generated at 2022-06-14 12:06:12.350255
# Unit test for function linkify
def test_linkify():
    text="""
    check this out: http://www.google.com
    and this: https://python.org
    and even ftp://localhost.
    javascript:alert('hello'); is not a link!
    """
    print("original: %s" % text)
    result = linkify(text)
    print("linkified: %s" % result)
    assert type(result)==type("")

if __name__ == '__main__':
    test_linkify()


# Escaping

# Generated at 2022-06-14 12:06:25.860118
# Unit test for function recursive_unicode
def test_recursive_unicode():
  a = bytes("this is string", encoding="utf-8")
  b = bytes("this is another string", encoding="utf-8")
  c = bytes("this is another string", encoding="utf-8")
  dict1 = {a: a, "b": b}
  list1 = [a, b, c]
  tuple1 = (a, b, c)
  assert recursive_unicode(dict1) == {a: a, "b": b}
  assert recursive_unicode(list1) == [a, b, c]
  assert recursive_unicode(tuple1) == (a, b, c)
  assert recursive_unicode(None) == None


# Generated at 2022-06-14 12:06:41.569537
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello www.facebook.com!"))
    print(linkify("Hello http://www.facebook.com!"))
    print(linkify("Hello https://www.facebook.com!"))
    # print(linkify("Hello http://www.tornadoweb.org!"))
    # print(linkify("Hello javascript:alert('hi');"))
    # print(linkify("Hello <javascript:alert('hi');>", True))
    # print(linkify("Hello javascript:alert('hi');", True, permitted_protocols=["http", "javascript"]))
    # print(linkify("http://www.tornadoweb.org.cn/en/stable/faq.html", shorten = True, extra_params = "rel='nofollow'"))

# test_linkify()

_EMAIL_RE = re.comp

# Generated at 2022-06-14 12:06:43.421985
# Unit test for function linkify
def test_linkify():
    print('Begin test_linkify...')
    text = 'Hello http://tornadoweb.org!'
    print(linkify(text))

if __name__ == '__main__':
    test_linkify()

# Generated at 2022-06-14 12:06:46.903571
# Unit test for function recursive_unicode
def test_recursive_unicode():
    assert recursive_unicode([b"foo", b"bar"]) == ["foo", "bar"]
    assert recursive_unicode(("foo", "bar")) == ("foo", "bar")
    assert recursive_unicode({"foo": "bar", "baz": b"quux"}) == {"foo": "bar", "baz": "quux"}



# Generated at 2022-06-14 12:07:03.230517
# Unit test for function linkify
def test_linkify():
    text = "Hello http://www.tornadoweb.org! https://github.com/tornadoweb/tornado"
    print(linkify(text))
test_linkify()

_email_address_re = re.compile(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,6}")



# Generated at 2022-06-14 12:07:10.720881
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == u"<a href=\"http://www.example.com\">http://www.example.com</a>"
    text = u"Hello http://www.example.com/ foo@bar.com"
    assert (
        linkify(text)
        == u"Hello <a href=\"http://www.example.com/\">http://www.example.com/</a> <a href=\"mailto:foo@bar.com\">foo@bar.com</a>"
    )

# Generated at 2022-06-14 12:07:21.219276
# Unit test for function linkify

# Generated at 2022-06-14 12:07:28.923166
# Unit test for function linkify
def test_linkify():
    print("test func linkify")
    def test_linkify_text(text):
        print("input text: " + text)
        print("output text: " + linkify(text))

    text = r"http://tornadoweb.org  https://tornadoweb.org https://tornadoweb.org/en/stable/tutorial.html#hello-world https://tornadoweb.org/en/stable/tutorial.html?a=1&b=2 "
    text += r"https://zh.m.wikipedia.org/zh-cn/%E7%B6%B2%E8%B7%AF%E7%A8%8B%E5%BC%8F%E5%A4%A7%E6%88%98"

# Generated at 2022-06-14 12:07:33.133060
# Unit test for function linkify
def test_linkify():
    text = "http://www.sina.com.cn"
    assert linkify(text) == u'<a href="http://www.sina.com.cn">http://www.sina.com.cn</a>'

test_linkify()

# test "http://t.cn/RBE5vzr"

# Generated at 2022-06-14 12:07:34.428191
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))

# Generated at 2022-06-14 12:07:41.860464
# Unit test for function linkify
def test_linkify():
    assert(linkify("Hello http://tornadoweb.org!") ==
           "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!")
    assert(linkify("Hello http://tornadoweb.org! Should not linkify www.google.com.") ==
           "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>! Should not linkify www.google.com.")
    assert(linkify("Hello http://tornadoweb.org! Should not linkify http://www.google.com.") ==
           "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>! Should not linkify <a href=\"http://www.google.com\">http://www.google.com</a>.")

# Generated at 2022-06-14 12:07:46.878813
# Unit test for function linkify
def test_linkify():
    assert (
        linkify("http://www.facebook.com/")
        == '<a href="http://www.facebook.com/" rel="nofollow">http://www.facebook.com/</a>'
    )



# Generated at 2022-06-14 12:07:57.635951
# Unit test for function linkify
def test_linkify():
    assert linkify('http://www.facebook.com') == '<a href="http://www.facebook.com">http://www.facebook.com</a>'
    assert linkify('https://www.facebook.com') == '<a href="https://www.facebook.com">https://www.facebook.com</a>'
    assert linkify('www.facebook.com') == '<a href="http://www.facebook.com">www.facebook.com</a>'
    assert linkify('Test http://www.facebook.com Test') == 'Test <a href="http://www.facebook.com">http://www.facebook.com</a> Test'
    assert linkify('www.facebook.com Test') == '<a href="http://www.facebook.com">www.facebook.com</a> Test'

# Generated at 2022-06-14 12:08:00.570952
# Unit test for function linkify
def test_linkify():
    text = "Hello www.tornadoweb.org!"
    assert linkify(text) == "Hello <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>!"



# Generated at 2022-06-14 12:08:11.539013
# Unit test for function linkify
def test_linkify():
    assert linkify("Hello http://tornadoweb.org") == \
        'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>'

    assert linkify("Hello http://tornadoweb.org", shorten=True) == \
        'Hello <a href="http://tornadoweb.org" title="http://tornadoweb.org">http://tornadoweb.org</a>'

    assert linkify("Hello https://tornadoweb.org and http://google.com", shorten=True) == \
        'Hello <a href="https://tornadoweb.org" title="https://tornadoweb.org">https://tornadoweb.org</a> and <a href="http://google.com" title="http://google.com">http://google.com</a>'


# Generated at 2022-06-14 12:08:15.000508
# Unit test for function linkify
def test_linkify():
    url = "http://www.example.com"
    url_text = "http://www.example.com"
    assert linkify(url) == "<a href=\"%s\">%s</a>" % (url,url_text)



# Generated at 2022-06-14 12:08:19.148852
# Unit test for function linkify
def test_linkify():
    assert linkify(u"http://example.com/") == u'<a href="http://example.com/">http://example.com/</a>'
    assert linkify(u"http://example.com/foo&bar") == u'<a href="http://example.com/foo&amp;bar">http://example.com/foo&amp;bar</a>'

# Generated at 2022-06-14 12:08:22.670231
# Unit test for function linkify
def test_linkify():
    test = linkify("Hi, visit http://example.com/ and say hello to fred@example.com")
    assert test == 'Hi, visit <a href="http://example.com/">http://example.com/</a> and say hello to <a href="mailto:fred@example.com">fred@example.com</a>'



# Generated at 2022-06-14 12:08:33.631214
# Unit test for function linkify
def test_linkify():
    print("Test linkify")
    text = "abc@gmail.com"
    params = " " + " ".strip()

    def make_link(m):
        url = m.group(1)
        proto = m.group(2)
        if not proto:
            href = "http://" + url  # no proto specified, use http

        if callable(params):
            params = " " + params(href).strip()
        else:
            params = params

        return '<a href="%s"%s>%s</a>' % (href, params, url)

    # First HTML-escape so that our strings are all safe.
    # The regex is modified to avoid character entites other than &amp; so
    # that we won't pick up &quot;, etc.

# Generated at 2022-06-14 12:08:38.348892
# Unit test for function linkify
def test_linkify():
    s = "Please see https://docs.python.org/3/reference/grammar.html#ambiguous-grammars."
    r = linkify(s)
    print(r)


# Generated at 2022-06-14 12:08:49.923803
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""
    assert linkify("Hello") == "Hello"
    assert (
        linkify(
            "http://example.com/foo&bar=baz&quux=spam",
            extra_params="rel='nofollow'",
        )
        == '<a href="http://example.com/foo&amp;bar=baz&amp;quux=spam" rel=\'nofollow\'>http://example.com/foo&amp;bar=baz&amp;quux=spam</a>'
    )

# Generated at 2022-06-14 12:08:58.337544
# Unit test for function linkify
def test_linkify():
    text = 'I love you http://www.baidu.com'
    assert 'I love you <a href="http://www.baidu.com">http://www.baidu.com</a>' == linkify(text) 
test_linkify()

# Generated at 2022-06-14 12:09:06.114589
# Unit test for function linkify
def test_linkify():
    print(linkify("http://www.baidu.com"))
    print(linkify("www.baidu.com"))
    print(linkify("www.baidu.com",require_protocol=True))
    print(linkify("http://www.baidu.com",permitted_protocols=["http","ftp"]))


# Set up a logger for this module.  We don't want to rely on the
# configuration of the application, so set up the logger here
# using basicConfig.  We only want error messages.
logger = logging.getLogger('tornado.util')

# Generated at 2022-06-14 12:09:12.618596
# Unit test for function linkify
def test_linkify():
    print(
        linkify(
            """Hello http://www.tornadoweb.org/, and
    http://www.grameenfoundation.org!""",
            shorten=True,
        )
    )
    print(
        linkify(
            "www.google.com http://www.facebook.com",
            require_protocol=False,
            permitted_protocols=["http", "https"],
        )
    )
    print(
        linkify(
            """www.google.com http://www.facebook.com
    https://github.com""",
            require_protocol=True,
            permitted_protocols=["http", "https"],
        )
    )

# Generated at 2022-06-14 12:09:22.376757
# Unit test for function linkify
def test_linkify():
    """Assert that the  linkify method works fine"""
    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'

# Generated at 2022-06-14 12:09:33.722955
# Unit test for function linkify
def test_linkify():
    assert linkify("a http://www.b.com") == "a <a href=\"http://www.b.com\">http://www.b.com</a>"
    assert linkify("a http://www.b.com b") == "a <a href=\"http://www.b.com\">http://www.b.com</a> b"
    assert linkify("") == ""
    assert linkify("http://www.b.com") == "<a href=\"http://www.b.com\">http://www.b.com</a>"
    assert linkify("a http://www.b.com b", shorten=True) == "a <a href=\"http://www.b.com\">http://www.b.com</a> b"

# Generated at 2022-06-14 12:09:42.400628
# Unit test for function linkify
def test_linkify():
    text = linkify(
    "This is a test http://example.com/?foo=bar&baz=blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
)
    print(text)
    assert(text == 'This is a test <a href="http://example.com/?foo=bar&baz=blah" title="http://example.com/?foo=bar&baz=blah">http://example.com/?foo=bar&baz=blah...</a> blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah')

# test_linkify()



# Generated at 2022-06-14 12:09:46.726373
# Unit test for function linkify
def test_linkify():
    url = "http://www.baidu.com"
    assert linkify(url) == '<a href="http://www.baidu.com">http://www.baidu.com</a>'
# test_linkify()



# Generated at 2022-06-14 12:09:53.103777
# Unit test for function linkify
def test_linkify():
    strs = "Hello http://www.baidu.com,www.qq.com?"
    print(linkify(strs))


if __name__ == '__main__':
    test_linkify()

# Generated at 2022-06-14 12:10:04.155805
# Unit test for function linkify
def test_linkify():
    assert (
        linkify("http://www.google.com")
        == '<a href="http://www.google.com">http://www.google.com</a>'
    )
    assert (
        linkify("Hello http://www.example.com")
        == 'Hello <a href="http://www.example.com">http://www.example.com</a>'
    )
    assert (
        linkify(
            "Visit http://tornadoweb.org for more info."
        )
        == 'Visit <a href="http://tornadoweb.org">http://tornadoweb.org</a> for more info.'
    )
    # common case of link already surrounded by punctuation

# Generated at 2022-06-14 12:10:13.845206
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/") == '<a href="http://example.com/">http://example.com/</a>'
    assert linkify("http://example.com/foo") == '<a href="http://example.com/foo">http://example.com/foo</a>'
    assert linkify("http://example.com:8888/foo") == '<a href="http://example.com:8888/foo">http://example.com:8888/foo</a>'
    assert linkify("https://example.com") == '<a href="https://example.com">https://example.com</a>'

# Generated at 2022-06-14 12:10:25.478556
# Unit test for function linkify
def test_linkify():
    assert (linkify("http://example.com/", shorten=False)) == '<a href="http://example.com/">http://example.com/</a>'
    assert (linkify("http://example.com/", shorten=True)) == '<a href="http://example.com/" title="http://example.com/">http://example.com/</a>'
    assert (linkify("http://example.com/path/here?and=query", shorten=False)) == '<a href="http://example.com/path/here?and=query">http://example.com/path/here?and=query</a>'

# Generated at 2022-06-14 12:10:35.964758
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""
    assert linkify("hello") == "hello"
    assert linkify(u"hello") == "hello"
    assert linkify("hello http://www.google.com") == 'hello <a href="http://www.google.com">http://www.google.com</a>'  # noqa: E501, E501
    assert linkify("hello http://www.google.com, and http://www.facebook.com/foo") == 'hello <a href="http://www.google.com">http://www.google.com</a>, and <a href="http://www.facebook.com/foo">http://www.facebook.com/foo</a>'  # noqa: E501, E501

# Generated at 2022-06-14 12:10:47.937479
# Unit test for function linkify
def test_linkify():
    """
    _linkify_test(input, output)

    Unit tests for _linkify.
    """
    _linkify_test(
        "Hello http://www.facebook.com!",
        'Hello <a href="http://www.facebook.com">http://www.facebook.com</a>!',
    )
    _linkify_test(
        "Hello http://www.facebook.com/",
        'Hello <a href="http://www.facebook.com/">www.facebook.com/</a>',
    )
    _linkify_test(
        "Hello http://www.facebook.com:8080/foo",
        'Hello <a href="http://www.facebook.com:8080/foo">www.facebook.com:8080/foo</a>',
    )

# Generated at 2022-06-14 12:10:59.063131
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == '<a href="http://google.com">http://google.com</a>'
    assert linkify("https://google.com") == '<a href="https://google.com">https://google.com</a>'
    assert linkify("www.google.com") == '<a href="http://www.google.com">www.google.com</a>'
    assert linkify("foo@google.com") == '<a href="mailto:foo@google.com">foo@google.com</a>'
    assert linkify("foo bar http://google.com") == 'foo bar <a href="http://google.com">http://google.com</a>'


# Generated at 2022-06-14 12:11:10.861612
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == '<a href="http://google.com">http://google.com</a>'
    assert linkify("http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("https://www.google.com") == '<a href="https://www.google.com">https://www.google.com</a>'
    assert linkify("www.google.com") == '<a href="http://www.google.com">www.google.com</a>'
    assert linkify("foo.com") == '<a href="http://foo.com">foo.com</a>'

# Generated at 2022-06-14 12:11:20.471452
# Unit test for function linkify
def test_linkify():
    assert(linkify("http://example.com")=='<a href="http://example.com">http://example.com</a>')
    assert(linkify("example.com")=='<a href="http://example.com">example.com</a>')
    assert(linkify("www.example.com")=='<a href="http://www.example.com">www.example.com</a>')
    assert(linkify("www.example.com/123")=='<a href="http://www.example.com/123">www.example.com/123</a>')
print("Running tests for utils.py")
test_linkify()


# Generated at 2022-06-14 12:11:29.401637
# Unit test for function linkify
def test_linkify():
    text = """Hello http://abc.com, http://abc.com/hi/there, http://abc.com/hi/there?a=b"""
    output = linkify(text)
    expected = """Hello <a href="http://abc.com">http://abc.com</a>, <a href="http://abc.com/hi/there">http://abc.com/hi/there</a>, <a href="http://abc.com/hi/there?a=b">http://abc.com/hi/there?a=b</a>"""

    if output != expected:
        raise Exception("test_linkify failed")
if __name__ == '__main__':
    test_linkify()

# Generated at 2022-06-14 12:11:36.271721
# Unit test for function linkify

# Generated at 2022-06-14 12:11:48.325190
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == (
        '<a href="http://www.example.com">http://www.example.com</a>'
    )
    assert linkify("http://www.example.com", shorten=True) == (
        '<a href="http://www.example.com">example.com</a>'
    )
    assert linkify("example.com", require_protocol=False) == (
        '<a href="http://example.com">example.com</a>'
    )
    assert linkify("foo.com/blah_blah") == (
        '<a href="http://foo.com/blah_blah">foo.com/blah_blah</a>'
    )

# Generated at 2022-06-14 12:11:58.891127
# Unit test for function linkify
def test_linkify():
    text = "Example www.example.com http://example.com 中文测试 hello@example.com "
    url = linkify(text)
    print(url)
    assert url == '<a href="http://www.example.com">www.example.com</a><a href="http://example.com">http://example.com</a> 中文测试 <a href="mailto:hello@example.com">hello@example.com</a> '
    text = "Example www.example.com http://example.com hello@example.com "
    url = linkify(text, False)
    print(url)

# Generated at 2022-06-14 12:12:05.180374
# Unit test for function linkify
def test_linkify():
    text = "hello http://google.com and http://google.com again"
    print("text = ", text)
    print("linkify = ", linkify(text))


# Generated at 2022-06-14 12:12:09.474943
# Unit test for function linkify
def test_linkify():
    test_string = "Hello http://tornadoweb.org and https://www.baidu.com"
    print(linkify(test_string))


if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:12:16.621946
# Unit test for function linkify
def test_linkify():
    # First HTML-escape so that our strings are all safe.
    # The regex is modified to avoid character entites other than &amp; so
    # that we won't pick up &quot;, etc.
    text = _unicode(xhtml_escape('Hello http://tornadoweb.org!'))
    return _URL_RE.sub(make_link, text)
    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'



# Generated at 2022-06-14 12:12:30.276825
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") ==  '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/") == '<a href="http://example.com/">http://example.com/</a>'
    assert linkify("http://example.com/foo") == '<a href="http://example.com/foo">http://example.com/foo</a>'
    assert linkify("http://example.com/foo/bar") == '<a href="http://example.com/foo/bar">http://example.com/foo/bar</a>'

# Generated at 2022-06-14 12:12:42.776698
# Unit test for function linkify
def test_linkify():
    assert linkify(u'foo http://example.com bar') == u'foo <a href="http://example.com">http://example.com</a> bar'
    assert linkify(u'foo https://example.com bar') == u'foo <a href="https://example.com">https://example.com</a> bar'
    assert linkify(u'foo http://127.0.0.1:8080 bar') == u'foo <a href="http://127.0.0.1:8080">http://127.0.0.1:8080</a> bar'
    # non-ASCII domain names

# Generated at 2022-06-14 12:12:52.877638
# Unit test for function linkify
def test_linkify():
    print("test_linkify()")
    #基本用法
    print("test case 1:",linkify("Hello http://tornadoweb.org!"))
    #设置shorten属性
    print("test case 2:",linkify("Hello http://tornadoweb.org!",shorten=True))
    #设置extra_params属性
    print("test case 3:",linkify("Hello http://tornadoweb.org!",extra_params='rel="nofollow" class="external"'))

    #设置require_protocol属性
    print("test case 4:",linkify("Hello www.baidu.com", require_protocol=True))
    #设置permitted_protocols

# Generated at 2022-06-14 12:12:58.481918
# Unit test for function linkify
def test_linkify():
    # given
    text = 'This is my site http://www.alo7.com, check it out!'
    # when
    result = linkify(text)
    # then
    print (result)

test_linkify()

# Generated at 2022-06-14 12:13:07.217582
# Unit test for function linkify
def test_linkify():
    """ docstring """
    #print(linkify("<a href='http://localhost/' </a>"))
    #print(linkify("<a href='http://localhost/'> </a>"))
    #print(linkify("<a href='http://localhost/'> </a>", require_protocol=True))
    #print(linkify("<script>http://localhost/'</script>"))
    #print(linkify("<a href='http://localhost/'> </a>", require_protocol=False))
    #print(linkify("<script>http://localhost/'</script>", require_protocol=False))
    #print(linkify("<a href='http://localhost/'> </a>", require_protocol=True))
    #print(linkify("<script>http://localhost/'</script>", require

# Generated at 2022-06-14 12:13:18.796326
# Unit test for function linkify
def test_linkify():
    assert linkify(
        u'hello http://example.com', require_protocol=True
    ) == u'hello <a href="http://example.com">http://example.com</a>'
    assert linkify(u'hello http://example.com, https://example.com') == u'hello <a href="http://example.com">http://example.com</a>, <a href="https://example.com">https://example.com</a>'
    assert linkify(
        u'hello http://example.com:8000', require_protocol=True
    ) == u'hello <a href="http://example.com:8000">http://example.com:8000</a>'

# Generated at 2022-06-14 12:13:32.655509
# Unit test for function linkify
def test_linkify():
    assert linkify(u"https://foo.bar") == u'<a href="https://foo.bar">https://foo.bar</a>'
    assert linkify(u"https://foo.bar", extra_params="rel='nofollow'") == u'<a href="https://foo.bar" rel=\'nofollow\'>https://foo.bar</a>'
    assert linkify(u"https://foo.bar", extra_params=lambda url: "rel='nofollow'") == u'<a href="https://foo.bar" rel=\'nofollow\'>https://foo.bar</a>'
    assert linkify(u"https://foo.bar", require_protocol=True) == u'<a href="https://foo.bar">https://foo.bar</a>'

# Generated at 2022-06-14 12:13:43.564497
# Unit test for function linkify

# Generated at 2022-06-14 12:13:50.098356
# Unit test for function linkify
def test_linkify():
    text_in = """
    hi, I like www.facebook.com, www.youtube.com, https://www.apple.com,
    https://www.instagram.com, http://www.google.com,
    """
    text_out = linkify(text_in)
    print(text_out)

import re
import os
import sys
import json
import subprocess
import pkg_resources
import hashlib
from typing import List
from pathlib import Path

import PIL.Image


# Generated at 2022-06-14 12:13:56.496974
# Unit test for function linkify
def test_linkify():
    if linkify("Hello http://tornadoweb.org!") != "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!":
        return False
    if linkify("Hello https://tornadoweb.org!") != "Hello <a href=\"https://tornadoweb.org\">https://tornadoweb.org</a>!":
        return False
    return True


# Filters from Jinja2
# This code is derived from Jinja2 (MIT licensed), copyright the Pallets
# team. It was modified for Tornado's quote() and linkify() filters.



# Generated at 2022-06-14 12:14:11.176341
# Unit test for function linkify
def test_linkify():
    print(linkify("http://example.com"))
    print(linkify("http://example.com/foo"))
    print(linkify("Hello http://example.com"))
    print(linkify("Hello http://example.com/foo"))
    print(linkify("Hello http://example.com/foo_bar"))
    print(linkify("Hello http://example.com/foo_bar_baz"))
    print(linkify("Hello http://example.com/foo_bar_baz_quux"))
    print(linkify("Hello http://example.com/foo_bar_baz_quux!"))
    print(linkify("Hello http://example.com/foo_bar_baz/quux!"))

# Generated at 2022-06-14 12:14:21.020322
# Unit test for function linkify
def test_linkify():
    text = "Hello www.test.com!"
    print(linkify(text, shorten=False, require_protocol=False))
    text = "Hello test.com/test"
    print(linkify(text, shorten=False, require_protocol=False))
    text = "Hello test.com/test.html"
    print(linkify(text, shorten=False, require_protocol=False))
    text = "Hello test.com/test.html?a=1&b=2"
    print(linkify(text, shorten=False, require_protocol=False))
    text = "Hello test.com/test.html?a=1&b=2"
    print(linkify(text, shorten=True, require_protocol=False))
    text = "Hello https://test.com/test"

# Generated at 2022-06-14 12:14:28.293427
# Unit test for function linkify
def test_linkify(): 
    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify("Hello www.tornadoweb.org!") == 'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!'
    assert linkify("Hello https://tornadoweb.org!") == 'Hello <a href="https://tornadoweb.org">https://tornadoweb.org</a>!'
    assert linkify("Hello http://tornadoweb.org:8080!") == 'Hello <a href="http://tornadoweb.org:8080">http://tornadoweb.org:8080</a>!'

# Generated at 2022-06-14 12:14:42.827187
# Unit test for function linkify
def test_linkify():
    def test_linking():
        assert linkify("http://www.tornadoweb.org/en/stable/#hello-world") == (
            '<a href="http://www.tornadoweb.org/en/stable/#hello-world"'
            '>http://www.tornadoweb.org/en/stable/#hello-world</a>'
        )
        assert linkify("http://www.tornadoweb.org:8080/en/stable/") == (
            '<a href="http://www.tornadoweb.org:8080/en/stable/">'
            "http://www.tornadoweb.org:8080/en/stable/</a>"
        )

# Generated at 2022-06-14 12:14:53.216568
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    expected = "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    assert linkify(text) == expected
    
    text = "www.example.com/path?query"
    expected = "<a href=\"http://www.example.com/path?query\">www.example.com/path?query</a>"
    assert linkify(text) == expected
    
    text = "www.example.com/path?query"
    expected = "<a href=\"http://www.example.com/path?query\" rel=\"nofollow\">www.example.com/path?query</a>"
    assert linkify(text, extra_params='rel="nofollow"') == expected
    

# Generated at 2022-06-14 12:15:03.223729
# Unit test for function linkify
def test_linkify():
    assert linkify("http://xkcd.com") == '<a href="http://xkcd.com">http://xkcd.com</a>'
    assert linkify("www.xkcd.com") == '<a href="http://www.xkcd.com">www.xkcd.com</a>'
    assert linkify("xkcd.com") == '<a href="http://xkcd.com">xkcd.com</a>'
    assert linkify("http://www.xkcd.com/353/") == '<a href="http://www.xkcd.com/353/">http://www.xkcd.com/353/</a>'

# Generated at 2022-06-14 12:15:07.237408
# Unit test for function linkify
def test_linkify():
    text = "http://sdfsdfsdfsdf.com http://sdfsdfsdf.com/?12312321=asdsadasd http://sdfsdfsdf.com/test/test/test?12312321=asdsadasd safdasdfasfds"
    print(linkify(text))


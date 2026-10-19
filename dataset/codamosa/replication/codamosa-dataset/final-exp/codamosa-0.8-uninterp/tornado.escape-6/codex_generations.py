

# Generated at 2022-06-14 12:05:22.382709
# Unit test for function linkify
def test_linkify():
    assert(linkify("http://www.exacmple.com") == '<a href="http://www.exacmple.com">http://www.exacmple.com</a>')
    assert(linkify("www.exacmple.com") == '<a href="http://www.exacmple.com">www.exacmple.com</a>')
    assert(linkify("www.exacmple.com", require_protocol=True) == "www.exacmple.com")
    assert(linkify("http://www.exacmple.com", extra_params = "class=test") == '<a href="http://www.exacmple.com" class=test>http://www.exacmple.com</a>')

# Generated at 2022-06-14 12:05:31.679349
# Unit test for function linkify
def test_linkify():

    assert linkify("http://example.com") == \
        '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/path with spaces") == \
        '<a href="http://example.com/path%20with%20spaces">http://example.com/path with spaces</a>'
    assert linkify("www.example.com") == \
        '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("me@example.com") == \
        '<a href="mailto:me@example.com">me@example.com</a>'

# Generated at 2022-06-14 12:05:37.172749
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert "foo" == linkify("foo")
    assert "hello <b>world</b>" == linkify("hello <b>world</b>")
    assert "hello <b>world</b>" == linkify("hello <b>world</b>", extra_params="")
    assert (
        'hello <b>world</b> <a href="http://example.com">http://example.com</a>'
        == linkify("hello <b>world</b> http://example.com")
    )
    assert (
        'hello <b>world</b> <a href="http://example.com">http://example.com</a>'
        == linkify("hello <b>world</b> http://example.com", require_protocol=True)
    )
   

# Generated at 2022-06-14 12:05:44.275725
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ''
    #test already safe links
    assert linkify('<a href="http://www.example.com">http://www.example.com</a>') == '<a href="http://www.example.com">http://www.example.com</a>'
    #test unsafe links
    assert linkify('http://www.example.com') == '<a href="http://www.example.com">http://www.example.com</a>'

# Unit tests for function to_unicode

# Generated at 2022-06-14 12:05:59.165911
# Unit test for function linkify
def test_linkify():
    # Test for URL without protocol
    assert linkify('Hello http://tornadoweb.org!') == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    # Test for URL with protocol
    assert linkify('Hello world http://tornadoweb.org!') == 'Hello world <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    # Test for URL with protocol
    assert linkify('Hello world https://tornadoweb.org!') == 'Hello world <a href="https://tornadoweb.org">https://tornadoweb.org</a>!'
    # Test for URL with protocol

# Generated at 2022-06-14 12:06:02.965646
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.zz.com")=='<a href="http://www.zz.com">http://www.zz.com</a>'
    print("test_linkify passed")
#test_linkify()


# Generated at 2022-06-14 12:06:09.876330
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com") == '<a href="http://foo.com">http://foo.com</a>'
    assert linkify("foo.com", require_protocol=True) == "foo.com"
    assert linkify("foo.com", require_protocol=False) == '<a href="http://foo.com">foo.com</a>'
    assert linkify("foo.com/foo/bar") == '<a href="http://foo.com/foo/bar">foo.com/foo/bar</a>'

# Generated at 2022-06-14 12:06:25.306592
# Unit test for function linkify

# Generated at 2022-06-14 12:06:41.199148
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.kaka.com") == '<a href="http://www.kaka.com">http://www.kaka.com</a>'
    assert linkify("http://www.kaka.com is a web site.") == '<a href="http://www.kaka.com">http://www.kaka.com</a> is a web site.'

# Generated at 2022-06-14 12:06:48.029076
# Unit test for function linkify
def test_linkify():
    url = "http://www.tornadoweb.org"
    assert linkify(url) == (
        '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>'
    )

    assert linkify("Hello http://tornadoweb.org", shorten=True) == (
        'Hello <a href="http://tornadoweb.org" title="http://tornadoweb.org">tornadoweb.org</a>'
    )


# Generated at 2022-06-14 12:07:03.054485
# Unit test for function linkify
def test_linkify():
    text = 'http://www.baidu.com'
    print(linkify(text))
    """
    <a href="http://www.baidu.com">http://www.baidu.com</a>
    """

# test_linkify()



# Generated at 2022-06-14 12:07:05.973822
# Unit test for function linkify
def test_linkify():
    text = 'this is a website http://www.baidu.com and this is an email xiaotian@mea.com'
    print(linkify(text))



# Generated at 2022-06-14 12:07:17.423550
# Unit test for function linkify
def test_linkify():
    assert linkify("foo") == "foo"
    assert linkify("http://example.com/") == '<a href="http://example.com/">http://example.com/</a>'
    assert linkify("https://example.com/") == '<a href="https://example.com/">https://example.com/</a>'
    assert linkify("https://example.com/?foo=bar&baz=blah") == '<a href="https://example.com/?foo=bar&baz=blah">https://example.com/?foo=bar&amp;baz=blah</a>'
    assert linkify("www.example.com/") == '<a href="http://www.example.com/">www.example.com/</a>'

# Generated at 2022-06-14 12:07:25.821453
# Unit test for function linkify
def test_linkify():
    assert linkify(to_unicode("Hello http://tornadoweb.org!")) == to_unicode(
        'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    )
    assert linkify(to_unicode("Hello example.com"), require_protocol=False) == to_unicode(
        'Hello <a href="http://example.com">example.com</a>'
    )
    assert linkify(to_unicode("Hello example.com"), require_protocol=True) == to_unicode(
        "Hello example.com"
    )

# Generated at 2022-06-14 12:07:32.400697
# Unit test for function linkify
def test_linkify():
    text = """
        Hello http://www.tornadoweb.org/. This is a link to Google
        http://www.google.com/ and one to Yahoo
        http://www.yahoo.com/search?p=%22linkify%22+python.
    """
    print(linkify(text, extra_params='rel="nofollow" class="external"',require_protocol=False))
#test_linkify()

# Generated at 2022-06-14 12:07:40.575066
# Unit test for function linkify

# Generated at 2022-06-14 12:07:52.512299
# Unit test for function linkify
def test_linkify():
    assert linkify("hello") == "hello"
    assert linkify("hello http://world") == "hello <a href='http://world'>http://world</a>"
    assert linkify("hello http://world/") == "hello <a href='http://world/'>http://world/</a>"
    assert (
        linkify("hello https://world")
        == "hello <a href='https://world'>https://world</a>"
    )
    assert (
        linkify("https://world?p=1&t=z")
        == "<a href='https://world?p=1&amp;t=z'>https://world?p=1&amp;t=z</a>"
    )

# Generated at 2022-06-14 12:08:03.221005
# Unit test for function linkify
def test_linkify():
    text = 'hello www.google.com'
    t_linkify = linkify(text)
    assert(t_linkify == 'hello <a href="http://www.google.com">www.google.com</a>')
    text = 'hello <a href="http://www.google.com">www.google.com</a>'
    t_linkify = linkify(text)
    assert(t_linkify == 'hello <a href="http://www.google.com">www.google.com</a>')
    text = 'hello www.google.com www.example.com http://www.example.com www.example.com/page.php?page_id=1&page_value=2'
    t_linkify = linkify(text)

# Generated at 2022-06-14 12:08:07.497562
# Unit test for function linkify
def test_linkify():
    import unittest

    class LinkifyTestCase(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_linkify(self):
            self.assertEqual(linkify("http://www.example.com"),
                             '<a href="http://www.example.com">http://www.example.com</a>')
            self.assertEqual(linkify("www.example.com/foo"),
                             '<a href="http://www.example.com/foo">www.example.com/foo</a>')
            self.assertEqual(linkify("http://www.example.com/foo"),
                             '<a href="http://www.example.com/foo">http://www.example.com/foo</a>')


# Generated at 2022-06-14 12:08:19.395622
# Unit test for function linkify
def test_linkify():
    assert linkify("http://tornadoweb.org") == '<a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    assert linkify("www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify("Hello http://tornadoweb.org! :) :)") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>! :) :)'

# Generated at 2022-06-14 12:08:35.159182
# Unit test for function linkify
def test_linkify():
    import unittest
    failUnlessEqual(linkify(""), "")  # no crash
    failUnlessEqual(
        linkify("http://example.com/foo"), '<a href="http://example.com/foo">http://example.com/foo</a>'  # noqa: E501
    )
    failUnlessEqual(
        linkify("foo http://example.com/foo bar"),  # noqa: E501
        "foo <a href=\"http://example.com/foo\">http://example.com/foo</a> bar",
    )
    failUnlessEqual(
        linkify("foo http://example.com/foo. bar"),  # noqa: E501
        "foo <a href=\"http://example.com/foo\">http://example.com/foo</a>. bar",
    )
   

# Generated at 2022-06-14 12:08:41.754095
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    extra_params = ""
    require_protocol = False
    permitted_protocols = ["http", "https"]
    print("before:", text)
    print("after:", linkify(text, extra_params, require_protocol, permitted_protocols))
    

test_linkify()


# Generated at 2022-06-14 12:08:50.876238
# Unit test for function linkify
def test_linkify():
    text='Hello https://tornadoweb.org!'
    text_link=linkify(text)
    assert text_link==r'Hello <a href="https://tornadoweb.org">https://tornadoweb.org</a>!'


"""Decode HTML entities in the given text."""
# Use the name unescape to match the django and perl implementations
unescape = _XHTML_UNESCAPE.sub

# Workaround for http://bugs.python.org/issue13201
_RFC3986_GENDELIMS = frozenset(":/?#[]@")
_RFC3986_SUBDELIMS = frozenset("!$&'()*+,;=")



# Generated at 2022-06-14 12:08:55.198851
# Unit test for function linkify
def test_linkify():
    text = 'Link to <a href="https://a.com">https://a.com</a>, <a href="https://b.com">https://b.com</a>, <a href="https://c.com">https://c.com</a>, and <a href="https://d.com">https://d.com</a>.'
    print (linkify(text))
test_linkify()


# Generated at 2022-06-14 12:09:06.462450
# Unit test for function linkify
def test_linkify():
    text = "aaa http://tornadoweb.org bbb"
    href_linkify = 'aaa <a href="http://tornadoweb.org">http://tornadoweb.org</a> bbb'
    assert linkify(text) == href_linkify
    text = "aaa www.tornadoweb.org bbb"
    href_linkify = 'aaa <a href="http://www.tornadoweb.org">www.tornadoweb.org</a> bbb'
    assert linkify(text) == href_linkify
    # extra_params
    text = "aaa http://tornadoweb.org bbb"
    href_linkify = 'aaa <a href="http://tornadoweb.org" class="external">http://tornadoweb.org</a> bbb'

# Generated at 2022-06-14 12:09:17.804041
# Unit test for function linkify
def test_linkify():
    text = "See more of our great products at https://www.google.com/google/google"
    shortened = linkify(text, shorten=True)
    assert shortened == 'See more of our great products at <a href="https://www.google.com/google/google">https://www.google.com/google/google</a>'
    notshortened = linkify(text, shorten=False)
    assert notshortened == 'See more of our great products at <a href="https://www.google.com/google/google">https://www.google.com/google/google</a>'

    text = "Open http://facebook.com/ google.com"
    shortened = linkify(text, shorten=True)

# Generated at 2022-06-14 12:09:29.615561
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ''
    assert linkify('') == ''
    assert linkify('Hello') == 'Hello'

    assert_equal(
        linkify('Hello http://tornadoweb.org!'),
        'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!',
    )
    assert_equal(
        linkify('Hello https://tornadoweb.org!'),
        'Hello <a href="https://tornadoweb.org">https://tornadoweb.org</a>!',
    )
    assert_equal(
        linkify('Hello www.tornadoweb.org!'),
        'Hello <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>!',
    )

# Generated at 2022-06-14 12:09:36.046110
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://tornadoweb.org!'
    linkified = linkify(text)
    assert linkified == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify(text, keep_blank_values=True) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'  # noqa: E501
    assert linkify('www.tornadoweb.org') == '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'  # noqa: E501
    assert linkify('www.tornadoweb.org', require_protocol=True) == 'www.tornadoweb.org'  # noqa: E501

# Generated at 2022-06-14 12:09:45.488592
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == "None", "Should return None if no string is provided"

    assert (
        linkify("Hi there http://tornadoweb.org")
        == 'Hi there <a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    ), "Should return a link for a url"

    assert (
        linkify("Hi there www.tornadoweb.org")
        == 'Hi there <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    ), "Should return a link for a url without protocol"


# Generated at 2022-06-14 12:09:47.946760
# Unit test for function linkify
def test_linkify():
    html=linkify("Hello http://tornadoweb.org!")
    print(html)
#test_linkify()


# Generated at 2022-06-14 12:09:57.644066
# Unit test for function linkify
def test_linkify():
    s='https://www.google.com/?q=tornado&hl=en'
    res=linkify(s)


test_linkify()



# Generated at 2022-06-14 12:10:04.154683
# Unit test for function linkify
def test_linkify():
    assert linkify("http://xxx.com") == "<a href=\"http://xxx.com\">http://xxx.com</a>"
    assert linkify("www.example.com:8000") == "<a href=\"http://www.example.com:8000\">www.example.com:8000</a>"
    assert linkify("www.example.com:8000/") == "<a href=\"http://www.example.com:8000/\">www.example.com:8000/</a>"

if __name__ == "__main__":
    test_linkify()


# Generated at 2022-06-14 12:10:13.845194
# Unit test for function linkify
def test_linkify():
    print("Test linkify function ... ", end="")
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/foo/bar?baz=1") == '<a href="http://example.com/foo/bar?baz=1">http://example.com/foo/bar?baz=1</a>'  # noqa: E501
    assert linkify("http://example.com/foo/bar?baz=1", shorten=True) == '<a href="http://example.com/foo/bar?baz=1">http://example.com/foo/bar?ba...</a>'  # noqa: E501

# Generated at 2022-06-14 12:10:25.478721
# Unit test for function linkify
def test_linkify():
    
    # Test by Parth Valand
    # I'm not sure how to test this function
    # So I just tested a the code
    text =  "Hello http://tornadoweb.org!"
    shorten = False
    extra_params = "rel=\"nofollow\" class=\"external\""
    require_protocol = False
    permitted_protocols = ["http", "https"]

    assert linkify(text, shorten, extra_params, require_protocol, permitted_protocols) == "Hello <a href=\"http://tornadoweb.org\" rel=\"nofollow\" class=\"external\">http://tornadoweb.org</a>!"
    
    # Test by Xiaolei Wu
    text =  "Hello http://tornadoweb.org!"
    shorten = False

# Generated at 2022-06-14 12:10:30.552700
# Unit test for function linkify
def test_linkify():
    text = "test http://www.google.com/ mailto:hi@hi.org"
    text = linkify(text)
    assert text == (
        'test <a href="http://www.google.com/" target="_blank">'
        "www.google.com</a> <a href=\"mailto:hi@hi.org\" target=\"_blank\">"
        "mailto:hi@hi.org</a>"
    )



# Generated at 2022-06-14 12:10:42.389962
# Unit test for function linkify
def test_linkify():
    text = "Hello http://www.example.com!"
    assert linkify(text) == 'Hello <a href="http://www.example.com">http://www.example.com</a>!'
    text = "Hello www.example.com!"
    assert linkify(text, require_protocol=False) == 'Hello <a href="http://www.example.com">www.example.com</a>!'
    text = "Hello, I like this https://www.tutorialspoint.com/python/python_basic_syntax.htm page"
    assert linkify(text, shorten = True) == 'Hello, I like this <a href="https://www.tutorialspoint.com/python/python_basic_syntax.htm">https://www.tutorialspoint.com/pytho...</a> page'
    text

# Generated at 2022-06-14 12:10:44.715763
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))
# test_linkify()

# Generated at 2022-06-14 12:10:53.521337
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == \
        '<a href="http://google.com">http://google.com</a>'
    assert linkify("google.com") == \
        '<a href="http://google.com">google.com</a>'
    assert linkify("Hello http://google.com!") == \
        'Hello <a href="http://google.com">http://google.com</a>!'

# Generated at 2022-06-14 12:11:01.769803
# Unit test for function linkify
def test_linkify():
    assert '<a href="http://example.com">example.com</a>' == linkify('http://example.com')
    assert '<a href="http://example.com">http://example.com</a>' == linkify('hhttp://example.com')
    assert '<a href="http://example.com">first http://example.com second</a>' == linkify('first http://example.com second')
    assert '<a href="http://example.com">http://example.com</a>:<a href="https://example.com">https://example.com</a>' == linkify('http://example.com:https://example.com')

test_linkify()

# In python3 (with unicode_literals), bytes and str are not compatible.
# Since you can't get non-ascii characters

# Generated at 2022-06-14 12:11:12.893683
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))
    print(linkify("Hello http://tornadoweb.org!", shorten=True))
    print(linkify("Hello http://tornadoweb.org/u/username!", shorten=True))
    print(linkify("Do not www.linkify.me", require_protocol=True))
    print(linkify("http://www.linkify.me", require_protocol=True))
    print(linkify("https://www.linkify.me", require_protocol=True))
    print(linkify("Hello http://tornadoweb.org!", extra_params='rel="nofollow" class="external"'))

# Generated at 2022-06-14 12:11:27.446577
# Unit test for function linkify
def test_linkify():
    #abnormal case
    #assert linkify('Hello World!!') == 'Hello World!!'
    assert linkify(
        'Hello World!! http://localhost:8080/get?a=1&b=2 http://localhost:8888')=='Hello World!! <a href="http://localhost:8080/get?a=1&b=2">http://localhost:8080/get?a=1&b=2</a> <a href="http://localhost:8888">http://localhost:8888</a>'




# Generated at 2022-06-14 12:11:43.566070
# Unit test for function linkify
def test_linkify():
    text = "www.baidu.com"
    print("哈哈",linkify(text))


    # a : 1
    # c : 4
    # b : 2
    # d : 3
    items = dict([("a", 1), ("b", 2), ("c", 4), ("d", 3)])
    def cmp_item(item):
        return item[1]
    for k, v in sorted(items.items(), key = cmp_item):
        print(k, v)
    # 字典排序  利用sorted 或者 使用collections.OrderedDict
#
#
# if __name__ == "__main__":
#     test_linkify()

# Generated at 2022-06-14 12:11:50.853944
# Unit test for function linkify
def test_linkify():
    assert linkify("hello http://www.example.com") == 'hello <a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("hello www.example.com") == 'hello <a href="http://www.example.com">www.example.com</a>'
    assert linkify("hello www.example.com/foo/bar?hello=1&amp;goodbye=2") == 'hello <a href="http://www.example.com/foo/bar?hello=1&amp;goodbye=2">www.example.com/foo/bar?hello=1&amp;goodbye=2</a>'

# Generated at 2022-06-14 12:12:00.117457
# Unit test for function linkify
def test_linkify():
    assert linkify("hello http://example.com world") == (
        "hello <a href=\"http://example.com\">http://example.com</a> world"
    )
    assert linkify("hello http://example.com/&a=1&b=2 world") == (
        "hello <a href=\"http://example.com/&amp;a=1&amp;b=2\">http://example.com/"
        "&amp;a=1&amp;b=2</a> world"
    )

# Generated at 2022-06-14 12:12:07.504870
# Unit test for function linkify
def test_linkify():
    read_file = r"j:\codes\python\pycharm\tornado_project\test\test_util.txt"
    with open(read_file, 'r') as f:
        text = f.read()
        text = linkify(text)
    print(text)


test_linkify()

# Generated at 2022-06-14 12:12:09.777944
# Unit test for function linkify
def test_linkify():
    x = linkify("http://google.com/")
    return x

test_linkify()
# %%time

# Generated at 2022-06-14 12:12:18.323248
# Unit test for function linkify
def test_linkify():
    assert linkify("http://xkcd.com/") == (
        '<a href="http://xkcd.com/">http://xkcd.com/</a>'
    )
    assert linkify("http://xkcd.com", shorten=True) == (
        '<a href="http://xkcd.com" title="http://xkcd.com">http://xk...</a>'
    )
    assert linkify("Hello http://tornadoweb.org!") == (
        'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    )

# Generated at 2022-06-14 12:12:20.269503
# Unit test for function linkify
def test_linkify():
    example_url = "www.baidu.com"
    print(linkify(example_url))
    return



# Generated at 2022-06-14 12:12:30.161616
# Unit test for function linkify
def test_linkify():
    # text_links = ['www.baidu.com', 'http://www.baidu.com', 'https://www.baidu.com'
    #             'http://www.baidu.com/s?wd=tornado', 'https://www.baidu.com/s?wd=tornado']
    text_links = '''www.baidu.com http://www.baidu.com https://www.baidu.com
                    http://www.baidu.com/s?wd=tornado https://www.baidu.com/s?wd=tornado'''
    for link in text_links.split():
        assert linkify(link) == '<a href="{}">{}</a>'.format(link, link)

# Generated at 2022-06-14 12:12:32.286696
# Unit test for function linkify
def test_linkify():
    test_text = "http://google.com/some random text http://yahoo.com"
    res_text = linkify(test_text)
    print(res_text)


if __name__ == "__main__":
    test_linkify()

# Generated at 2022-06-14 12:12:48.564229
# Unit test for function linkify
def test_linkify():
    assert linkify(u'Hello http://tornadoweb.org!') == u'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify(u'Hello http://tornadoweb.org:8080/!') == u'Hello <a href="http://tornadoweb.org:8080/">http://tornadoweb.org:8080/</a>!'
    assert linkify(u'Hello http://user:password@tornadoweb.org:8080/!') == 'Hello <a href="http://user:password@tornadoweb.org:8080/">http://user:password@tornadoweb.org:8080/</a>!'



# Generated at 2022-06-14 12:12:56.501517
# Unit test for function linkify
def test_linkify():
    text="www.facebook.com"
    print(linkify(text))
    text="http://www.facebook.com"
    print(linkify(text))
    text="Hello https://somewhere.com/here?and=there"
    print(linkify(text))
    text="Hello http://somewhere.com/here?and=there"
    print(linkify(text, shorten=True))
    result=linkify("Hello http://somewhere.com/here?and=there", shorten=True, extra_params='rel="nofollow" class="external"')
    print(result)
#test_linkify()

# Alias old name with new name to preserve backwards compatibility
recursive_unicode = recursive_unicode


# Generated at 2022-06-14 12:13:06.753517
# Unit test for function linkify

# Generated at 2022-06-14 12:13:18.443024
# Unit test for function linkify
def test_linkify():
    s = linkify("http://foo.com/bar")
    assert s == '<a href="http://foo.com/bar">http://foo.com/bar</a>', s

    s = linkify("http://foo.com/bar", shorten=True)
    assert s == '<a href="http://foo.com/bar">foo.com/bar</a>', s

    s = linkify("http://foo.com/bar?a=b&c=d", shorten=True)
    assert s == '<a href="http://foo.com/bar?a=b&c=d">foo.com/bar?a=b&amp;c=d</a>', s  # noqa: E501

    s = linkify("www.foo.com/bar?a=b&c=d")

# Generated at 2022-06-14 12:13:27.165993
# Unit test for function linkify
def test_linkify():
    assert 'Hello' == linkify("Hello")
    assert 'Hello' == linkify("Hello")
    assert 'Hello' == linkify("Hello")
    assert '<a href="http://www.facebook.com">www.facebook.com</a>' == linkify("www.facebook.com")

print(linkify("http://www.baidu.com"))
print(linkify("Hello www.facebook.com"))
test_linkify()



# Generated at 2022-06-14 12:13:37.685567
# Unit test for function linkify
def test_linkify():
    assert linkify("This is a test") == "This is a test"
    assert linkify("This is a longer test") == "This is a longer test"
    assert linkify("Visit google.com") == "Visit google.com"
    assert linkify("Visit google.com.") == "Visit google.com."
    assert linkify("Visit google.com", require_protocol=True) == "Visit google.com"
    assert linkify("www.google.com is a search engine") == "www.google.com is a search engine"
    assert linkify("http://www.google.com/") == '<a href="http://www.google.com/">http://www.google.com/</a>'

# Generated at 2022-06-14 12:13:49.202630
# Unit test for function linkify
def test_linkify():
    assert linkify('http://www.example.com') == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify('http://xn--bcher-kva.ch/de') == '<a href="http://xn--bcher-kva.ch/de">http://bücher.ch/de</a>'
    assert linkify('http://www.example.com', extra_params='target="_blank"') == '<a href="http://www.example.com" target="_blank">http://www.example.com</a>'

    url = linkify('http://example.com/foo/bar', shorten=True)[9:-9]
    assert url in ['example.com/f...', 'example.com/foo/...'], url


# Generated at 2022-06-14 12:13:55.864391
# Unit test for function linkify
def test_linkify():
    print("Testing linkify ....")

# Generated at 2022-06-14 12:14:07.266209
# Unit test for function linkify
def test_linkify():
    print(linkify('hello world'))
    print(linkify('hello world'))
    print(linkify('hello world'))
    print(linkify('hello world'))
    print(linkify('http://www.baidu.com'))
# _URL_RE.sub(make_link, 'http://www.baidu.com')
# _URL_RE = re.compile(to_unicode(r"""\b((?:([\w-]+):(/{1,3})|www[.])(?:(?:(?:[^\s&()]|&amp;|&quot;)*(?:[^!"#$%&'()*+,.:;<=>?@\[\]^`{|}~\s]))|(?:\((?:[^\s&()]|&amp;|&

# Generated at 2022-06-14 12:14:18.221824
# Unit test for function linkify
def test_linkify():
    assert linkify('Hello http://tornadoweb.org!') == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify('Hello www.facebook.com!', require_protocol=False) == 'Hello <a href="http://www.facebook.com">www.facebook.com</a>!'
    assert linkify('Hello https://tornadoweb.org!') == 'Hello <a href="https://tornadoweb.org">https://tornadoweb.org</a>!'
    assert linkify('Hello https://www.tornadoweb.org/!') == 'Hello <a href="https://www.tornadoweb.org/">https://www.tornadoweb.org/</a>!'

# Generated at 2022-06-14 12:14:28.216972
# Unit test for function linkify
def test_linkify():
    import pytest
    sentence = 'hello www.tornadoweb.org, how are you? http://www.tornadoweb.org/en/stable/index.html'
    converted = linkify(sentence)
    assert converted == u"hello <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>, how are you? <a href=\"http://www.tornadoweb.org/en/stable/index.html\">http://www.tornadoweb.org/en/stable/index.html</a>"
    with pytest.raises(TypeError):
        linkify(100)



# Generated at 2022-06-14 12:14:42.788903
# Unit test for function linkify

# Generated at 2022-06-14 12:14:46.831191
# Unit test for function linkify
def test_linkify():
    linkify('http://www.baidu.com')
    linkify('http://www.163.com')



# Generated at 2022-06-14 12:14:50.820414
# Unit test for function linkify
def test_linkify():
    text = "http://www.google.com"
    print(linkify(text))
    text2 = "http://www.google.com ftp://foo.bar"
    print(linkify(text2, permitted_protocols=["ftp"]))


# Generated at 2022-06-14 12:15:01.737325
# Unit test for function linkify
def test_linkify():
    assert(linkify(u"Nylon") == u'Nylon')
    assert(linkify(u"Nylon", require_protocol=True) == u'Nylon')
    assert(linkify(u"http://python.org") == u'<a href="http://python.org">http://python.org</a>')
    assert(linkify(u"http://some.domain.com/and/some/path") == u'<a href="http://some.domain.com/and/some/path">http://some.domain.com/and/some/path</a>')
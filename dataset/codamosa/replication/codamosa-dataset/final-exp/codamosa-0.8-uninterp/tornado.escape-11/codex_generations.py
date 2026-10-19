

# Generated at 2022-06-14 12:05:19.619921
# Unit test for function linkify
def test_linkify():
    tests = [
        ("hello http://www.google.com", "hello <a href='http://www.google.com'>http://www.google.com</a>"),
        ("google.com", "google.com"),
        ("google.com and http://google.com", "google.com and <a href='http://google.com'>http://google.com</a>")
    ]
    for link, expected in tests:
        assert expected == linkify(link), link


# Generated at 2022-06-14 12:05:25.959220
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert (
        linkify(
            "A test http://example.com/ with a link and some text http://example.org/"
            "afterwards"
        )
        == 'A test <a href="http://example.com">http://example.com</a> with a link and some text '
        '<a href="http://example.org">http://example.org</a>afterwards'
    )

# Generated at 2022-06-14 12:05:35.221821
# Unit test for function linkify
def test_linkify():
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("mailto:me@example.com") == '<a href="mailto:me@example.com">mailto:me@example.com</a>'
test_linkify()

# to_basestring is used for ensuring that all byte strings in URL patterns
# are decoded before attempting a match with a regular expression.
# It should guaranteed that the byte string is decoded to unicode
# in the end.

_TO_UNICODE_TYPES = (unicode_type, type(None))



# Generated at 2022-06-14 12:05:45.121518
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.example.com") == '<a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("http://www.example.com/") == '<a href="http://www.example.com/">http://www.example.com/</a>'
    assert linkify("mailto:user@example.com") == '<a href="mailto:user@example.com">mailto:user@example.com</a>'
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("example.com") == '<a href="http://example.com">example.com</a>'

# Generated at 2022-06-14 12:05:57.914051
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    assert linkify(text, extra_params='') == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    text = "Hello http://用户@xn--fiq228c.example.com:8080!"
    assert linkify(text, extra_params='') == "Hello <a href=\"http://用户@xn--fiq228c.example.com:8080\">http://用户@xn--fiq228c.example.com:8080</a>!"
test_linkify()


# Generated at 2022-06-14 12:06:00.487549
# Unit test for function linkify
def test_linkify():
    print(linkify("Hello http://tornadoweb.org!"))

test_linkify()



# Generated at 2022-06-14 12:06:04.386598
# Unit test for function linkify
def test_linkify():
    input_text = 'Hello http://tornadoweb.org!'
    expected_text = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    actual_text = linkify(input_text)
    assert expected_text == actual_text


# Generated at 2022-06-14 12:06:22.676225
# Unit test for function linkify
def test_linkify():
    # return linkify('<script>http://www.baidu.com</script>','','',True)
    return linkify('<script>http://www.baidu.com</script>')
    # return linkify('<script>http://www.baidu.com</script>', '', '', True, ['http'])
    # return linkify('<script>http://www.baidu.com</script>', '', '', True, ['https'])
    # return linkify('<script>http://www.baidu.com</script>', '', '', False, ['https'])
    # return linkify('<script>www.baidu.com</script>', '', '', False, ['https'])
    # return linkify('<script>www.baidu.com</script>',

# Generated at 2022-06-14 12:06:38.702249
# Unit test for function linkify
def test_linkify():
    assert linkify("www.google.com") == '<a href="http://www.google.com">www.google.com</a>'
    assert linkify("hello www.google.com ok www.google.com") == 'hello <a href="http://www.google.com">www.google.com</a> ok <a href="http://www.google.com">www.google.com</a>'
    assert linkify("hello http://www.google.com/ ok") == 'hello <a href="http://www.google.com/">http://www.google.com/</a> ok'

# Generated at 2022-06-14 12:06:42.198449
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    assert linkify(text) == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'



# Generated at 2022-06-14 12:07:14.531162
# Unit test for function linkify
def test_linkify():
    # Check for basic functionality:
    assert linkify("Hi there!") == "Hi there!"
    assert "http://www.tornadoweb.org" in linkify("Hi http://www.tornadoweb.org")
    assert "http://www.tornadoweb.org" in linkify("Hi www.tornadoweb.org")

    # Check that we're not generating malformed HTML:
    assert linkify("<") == "&lt;"
    assert linkify("a < b") == "a &lt; b"

    # Check that we handle ampersands:
    assert linkify("a && b") == "a &amp;&amp; b"

# Generated at 2022-06-14 12:07:23.949231
# Unit test for function linkify
def test_linkify():
    assert linkify('http://www.baidu.com/') == '<a href="http://www.baidu.com/">http://www.baidu.com/</a>'
    assert linkify('http://www.baidu.com/', extra_params = 'rel="nofollow"') == '<a href="http://www.baidu.com/" rel="nofollow">http://www.baidu.com/</a>'
    assert linkify('www.baidu.com', require_protocol = True) == 'www.baidu.com'
    assert linkify('www.baidu.com', require_protocol = False) == '<a href="http://www.baidu.com">www.baidu.com</a>'

# Generated at 2022-06-14 12:07:28.399100
# Unit test for function linkify
def test_linkify():
  assert linkify('http://example.com/') == '<a href="http://example.com/">http://example.com/</a>'

# Character encoding aliases and common incorrect spellings

# Generated at 2022-06-14 12:07:32.749572
# Unit test for function linkify
def test_linkify():
    assert linkify("https://www.tornadoweb.org/en/stable/") != None
    assert linkify("https://www.tornadoweb.org/en/stable/").startswith("<a href=")
    assert linkify("https://www.tornadoweb.org/en/stable/").endswith("</a>")


# Generated at 2022-06-14 12:07:40.811031
# Unit test for function linkify
def test_linkify():
    assert linkify(
        "http://example.com"
    ) == '<a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert linkify("http://tornadoweb.org is awesome!") == '<a href="http://tornadoweb.org">http://tornadoweb.org</a> is awesome!'
    assert linkify("http://" + "x" * 500) == '<a href="http://' + "x" * 500 + '">http://' + "x" * 496 + "...</a>"

# Generated at 2022-06-14 12:07:50.234536
# Unit test for function linkify
def test_linkify():
    assert linkify("http://www.facebook.com",extra_params='rel="nofollow" class="external"') =='<a href="http://www.facebook.com" rel="nofollow" class="external">http://www.facebook.com</a>'
    assert linkify("www.baidu.com") == '<a href="http://www.baidu.com">www.baidu.com</a>'
    assert linkify("www.baidu.com", require_protocol=True) == 'www.baidu.com'



# Generated at 2022-06-14 12:07:52.188818
# Unit test for function linkify

# Generated at 2022-06-14 12:07:56.433240
# Unit test for function linkify
def test_linkify():
    """ Test content of the unit test for linkify
    >>> test_linkify()
    Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!
    """
    print(linkify('Hello http://tornadoweb.org!'))


# Generated at 2022-06-14 12:08:00.395583
# Unit test for function linkify
def test_linkify():
    print("test_linkify()")
    # we must invoke linkify, since it compiles a regex to get the correct results
    linkify("http://www.sony.co.jp", shorten=True)
    print("test_linkify() passed")

# Generated at 2022-06-14 12:08:08.890787
# Unit test for function linkify
def test_linkify():
    text = "some text http://www.facebook.com/ and http://t.co/blahblah"
    assert linkify(text, shorten=False) == 'some text <a href="http://www.facebook.com/">http://www.facebook.com/</a> and <a href="http://t.co/blahblah">http://t.co/blahblah</a>'
    assert linkify(text, shorten=True) == 'some text <a href="http://www.facebook.com/">facebook.com/</a> and <a href="http://t.co/blahblah">t.co/blah...</a>'
    text = "some text www.facebook.com/ and http://t.co/blahblah"

# Generated at 2022-06-14 12:08:23.903228
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == (
        '<a href="http://example.com">http://example.com</a>'
    )

    assert linkify('Try <a href="http://example.com">example.com</a>') == (
        'Try <a href="http://example.com">example.com</a>'
    )

    assert linkify('Try example.com') == (
        'Try <a href="http://example.com">example.com</a>'
    )

    assert linkify(
        'Try example.com', False) == 'Try example.com'
    assert linkify('Try www.example.com') == (
        'Try <a href="http://www.example.com">www.example.com</a>'
    )


# Generated at 2022-06-14 12:08:27.250621
# Unit test for function linkify
def test_linkify():
    print('linkify:')
    print(linkify('myurl https://www.baidu.com/'))
    print(linkify('Hello http://tornadoweb.org!'))
    return


# Generated at 2022-06-14 12:08:36.540526
# Unit test for function linkify
def test_linkify():
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("http://example.com/foo") == '<a href="http://example.com/foo">http://example.com/foo</a>'
    assert linkify("http://example.com/foo?bar=baz") == '<a href="http://example.com/foo?bar=baz">http://example.com/foo?bar=baz</a>'
    assert linkify("http://example.com/foo?bar=baz&quot;") == '<a href="http://example.com/foo?bar=baz">http://example.com/foo?bar=baz</a>&quot;'
    assert linkify("www.example.com")

# Generated at 2022-06-14 12:08:48.059191
# Unit test for function linkify
def test_linkify():
    assert linkify(1) == '1'
    assert linkify("") == ""
    assert linkify("test") == "test"

    assert linkify("test www.example.com") == 'test <a href="http://www.example.com">www.example.com</a>'
    assert linkify("www.example.com") == '<a href="http://www.example.com">www.example.com</a>'
    assert linkify("test http://www.example.com") == 'test <a href="http://www.example.com">http://www.example.com</a>'
    assert linkify("http://www.example.com/~user") == '<a href="http://www.example.com/~user">http://www.example.com/~user</a>'

# Generated at 2022-06-14 12:08:56.220326
# Unit test for function linkify
def test_linkify():
    """Test function linkify."""
    assert linkify("http://google.com") == '<a href="http://google.com">http://google.com</a>'
    assert linkify("www.google.com") == '<a href="http://www.google.com">www.google.com</a>'
    assert linkify("http://google.com", extra_params='target="_blank"') == '<a href="http://google.com" target="_blank">http://google.com</a>'
    assert linkify("http://google.com", extra_params=lambda link: 'target="_blank"') == '<a href="http://google.com" target="_blank">http://google.com</a>'

# Generated at 2022-06-14 12:08:59.910116
# Unit test for function linkify
def test_linkify():
    assert linkify("foo http://example.com bar") == 'foo <a href="http://example.com">http://example.com</a> bar'



# Generated at 2022-06-14 12:09:05.448899
# Unit test for function linkify
def test_linkify():
    def test_linkify_fail():
        try:
            linkify("Hello http://tornadoweb.org!")
        except:
            return False
        return True

    try:
        assert test_linkify_fail() == True
        print(" linkify: OK")
    except Exception as e:
        print(e)
        print(" linkify: ERROR")

test_linkify()


# Generated at 2022-06-14 12:09:09.310054
# Unit test for function linkify
def test_linkify():
    text = '''
        This is some text with a link in it http://example.com and
        some more http://example.com/foo?bar=baz&x=y#z.
    '''
    linkified = '''
        This is some text with a link in it <a href="http://example.com">http://example.com</a>
        and some more <a href="http://example.com/foo?bar=baz&amp;x=y#z">http://example.com/foo?bar=baz&amp;x=y#z</a>.
    '''
    assert linkify(text) == linkified



# Generated at 2022-06-14 12:09:18.133891
# Unit test for function linkify
def test_linkify():
    assert linkify(b"http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify(u"http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify(b"http://example.com/foo?bar=baz&ding=dong") == '<a href="http://example.com/foo?bar=baz&amp;ding=dong">http://example.com/foo?bar=baz&amp;ding=dong</a>'
    assert linkify(b"http://example.com/two words") == '<a href="http://example.com/two%20words">http://example.com/two words</a>'

# Generated at 2022-06-14 12:09:29.704250
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    assert linkify(text) == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"

    text = "Hello https://tornado.readthedocs.io!"
    assert linkify(text) == "Hello <a href=\"https://tornado.readthedocs.io\">https://tornado.readthedocs.io</a>!"

    text = "Hello www.tornadoweb.org!"
    assert linkify(text) == "Hello <a href=\"http://www.tornadoweb.org\">www.tornadoweb.org</a>!"

    text = "Hello https://t.co/zKuc3qYMbz!"

# Generated at 2022-06-14 12:09:41.912224
# Unit test for function linkify
def test_linkify():
    test = "Hello http://tornadoweb.org!"
    expect = "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"
    real = linkify(test)
    assert expect == real



# Generated at 2022-06-14 12:09:48.407480
# Unit test for function linkify
def test_linkify():
    assert linkify("http://tornadoweb.org") == \
        '<a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    assert linkify("www.tornadoweb.org") == \
        '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    assert linkify("Hello http://tornadoweb.org!") == \
        'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert (linkify("Visit www.tornadoweb.org/en/stable/") ==
            'Visit <a href="http://www.tornadoweb.org/en/stable/">'
            'www.tornadoweb.org/en/stable/</a>')

# Generated at 2022-06-14 12:09:57.998601
# Unit test for function linkify
def test_linkify():
    def extra_params_cb(url):
        if url.startswith("http://example.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    text = 'Hello http://tornadoweb.org!'
    linkify(text, extra_params=extra_params_cb)

    

# Generated at 2022-06-14 12:09:59.952468
# Unit test for function linkify

# Generated at 2022-06-14 12:10:04.322884
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify("") == ""

    text = "Hello http://www.google.com!"
    result = linkify(text)
    expected = 'Hello <a href="http://www.google.com">http://www.google.com</a>!'
    assert result == expected, "got %r" % result

    text = "Visit http://www.google.com/."
    result = linkify(text)
    expected = 'Visit <a href="http://www.google.com/">http://www.google.com/</a>.'
    assert result == expected, "got %r" % result

    text = "Visit http://www.google.com/."
    result = linkify(text, shorten=True)

# Generated at 2022-06-14 12:10:12.748649
# Unit test for function linkify
def test_linkify():
    """Unit test for function linkify"""
    html = linkify("hello")
    assert html == "hello"
    html = linkify("Check out http://www.tornadoweb.org")
    print(html)
    html = linkify("Check out www.tornadoweb.org")
    print(html)
    html = linkify("Check out www.twitch.tv/{1}/profile")
    print(html)
    html = linkify("Check out www.twitch.tv/{1}")
    print(html)
    html = linkify("Check out http://www.twitch.tv/{1}")
    print(html)


# Stolen from django

# Generated at 2022-06-14 12:10:18.559485
# Unit test for function linkify
def test_linkify():
    ok = linkify("http://tornadoweb.org") == '<a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    ok = linkify("http://tornadoweb.org/") == '<a href="http://tornadoweb.org/">http://tornadoweb.org/</a>'
    ok = linkify("www.tornadoweb.org") == '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>'
    ok = linkify("Hello http://tornadoweb.org!") == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'

# Generated at 2022-06-14 12:10:28.132771
# Unit test for function linkify
def test_linkify():
    print(linkify(
        "Hello http://www.example.com!\n"
        "http://www.example.com/foo/bar.html\n"
        "Hello http://example.com/foo/bar.html?some=query\n"
        "Hello https://example.com/some#fragment\n"
    ))
    # Hello <a href="http://www.example.com">http://www.example.com</a>!
    # <a href="http://www.example.com/foo/bar.html">http://www.example.com/foo/bar.html</a>
    # Hello <a href="http://example.com/foo/bar.html?some=query">http://example.com/foo/bar.html?some=query</a>
    # Hello <a href="https://

# Generated at 2022-06-14 12:10:38.803609
# Unit test for function linkify
def test_linkify():
    test = "http://tornadoweb.org"
    assert linkify(test) == '<a href="http://tornadoweb.org">http://tornadoweb.org</a>'
    test = "http://tornadoweb.org/en/stable/index.html"
    assert linkify(test) == '<a href="http://tornadoweb.org/en/stable/index.html">http://tornadoweb.org/en/stabl...</a>'
    test = "https://login.live.com/oauth20_authorize.srf?client_id=000000004C12E68D&scope=wl.basic%20wl.signin%20wl.emails&response_type=code&redirect_uri=https://login.live.com/oauth20_desktop.srf"
    assert linkify

# Generated at 2022-06-14 12:10:43.569937
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    result = linkify(text)
    print(result)
    assert result == 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'

test_linkify()


# Generated at 2022-06-14 12:10:55.168280
# Unit test for function linkify
def test_linkify():
    s = 'This is a test <a href="http://www.baidu.com">http://www.baidu.com</a>'
    assert (s == linkify(s))
    s = 'This is a test http://www.baidu.com'
    assert (s == linkify(s,True))


# Generated at 2022-06-14 12:11:02.737168
# Unit test for function linkify
def test_linkify():
    assert linkify("test")=="test"
    assert linkify("test http://www.google.com/")=="test <a href=\"http://www.google.com/\">http://www.google.com/</a>"
    assert linkify("test",shorten=True) == "test"
    assert linkify("test http://www.google.com/",shorten=True)=="test <a href=\"http://www.google.com/\">http://www.goo...</a>"
    assert linkify("test",extra_params="extra")=="test"
    assert linkify("test http://www.google.com/",extra_params="extra")=="test <a href=\"http://www.google.com/\" extra>http://www.google.com/</a>"

# Generated at 2022-06-14 12:11:13.880243
# Unit test for function linkify
def test_linkify():
    assert linkify("hello http://www.google.com") == u'hello <a href="http://www.google.com">http://www.google.com</a>'
    assert linkify("hello http://google.com", require_protocol=False) == u'hello <a href="http://google.com">google.com</a>'
    assert linkify("hello http://www.google.com:8000/foo") == u'hello <a href="http://www.google.com:8000/foo">http://www.google.com:8000/foo</a>'
    assert linkify("hello http://www.google.com/foo/bar/") == u'hello <a href="http://www.google.com/foo/bar/">http://www.google.com/foo/bar/</a>'

# Generated at 2022-06-14 12:11:16.111444
# Unit test for function linkify
def test_linkify():
    text='This is a test for Tornado/web.py. http://www.oschina.net/p/tornado'
    print(linkify(text))


# Generated at 2022-06-14 12:11:22.341585
# Unit test for function linkify
def test_linkify():
    text= "Hello http://tornadoweb.org!"
    require_protocol= False
    permitted_protocols=["http", "https"]
    print(linkify(text,require_protocol= require_protocol,permitted_protocols= permitted_protocols))


# Generated at 2022-06-14 12:11:26.413214
# Unit test for function linkify
def test_linkify():
    result = linkify('test http://yunxin.163.com/doc/', shorten = True)
    assert result == 'test <a href="http://yunxin.163.com/doc/">http://yunxin.163.com/doc/</a>'

# Generated at 2022-06-14 12:11:31.167706
# Unit test for function linkify
def test_linkify():
    # The original linkify method use to encode `&`, this method was changed to support
    # &amp; style escaping instead.
    text = 'This is a <a href="http://www.example.com/">link</a> for some site and &amp;'
    assert linkify(text, shorten=True, extra_params='rel="nofollow" class="external"') == text


# TODO: improve tests

# Generated at 2022-06-14 12:11:47.400141
# Unit test for function linkify
def test_linkify():
    assert linkify(None) is None
    assert linkify("") == ""
    assert linkify("Hello") == "Hello"
    assert linkify("http://example.com") == '<a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://example.com") == 'Hello <a href="http://example.com">http://example.com</a>'
    assert linkify("Hello http://example.com, and http://foo.com") == 'Hello <a href="http://example.com">http://example.com</a>, and <a href="http://foo.com">http://foo.com</a>'

# Generated at 2022-06-14 12:11:58.850518
# Unit test for function linkify
def test_linkify():
    assert linkify(u"http://x.co/path") == '<a href="http://x.co/path">http://x.co/path</a>'
    assert linkify(u"http://x.co/path?a=b&c=d") == '<a href="http://x.co/path?a=b&c=d">http://x.co/path?a=b&c=d</a>'
    assert linkify(u"http://x.co/path?a=b&c=d", shorten=True) == '<a href="http://x.co/path?a=b&c=d">http://x.co/p...</a>'

# Generated at 2022-06-14 12:12:13.974522
# Unit test for function linkify
def test_linkify():
    assert linkify("Do you like www.tornadoweb.org?") == 'Do you like <a href="http://www.tornadoweb.org">www.tornadoweb.org</a>?'
    assert '<a href="http://www.tornadoweb.org">www.tornadoweb.org</a>' in linkify("Do you like www.tornadoweb.org?")
    assert linkify("Do you like http://www.tornadoweb.org?") == 'Do you like <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>?'
    assert '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>' in linkify("Do you like http://www.tornadoweb.org?")

# Generated at 2022-06-14 12:12:31.326646
# Unit test for function linkify
def test_linkify():
    def test_linkify_with(text, expected, **kwargs):
        actual = linkify(text, **kwargs)
        if actual != expected:
            print("linkify(%r) => %r != %r" % (text, actual, expected))
            assert False

    test_linkify_with("http://www.google.com", '<a href="http://www.google.com">http://www.google.com</a>')
    test_linkify_with("http://www.tornadoweb.org.", '<a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a>.')

# Generated at 2022-06-14 12:12:38.342814
# Unit test for function linkify
def test_linkify():
    # pylint: disable=protected-access
    assert linkify(u"http://www.google.com") == '<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify(u"http://www.google.com", shorten=True) == u'<a href="http://www.google.com">http://www.google.com</a>'
    assert linkify(u"http://www.mötörhead.com") == u'<a href="http://www.mötörhead.com">http://www.mötörhead.com</a>'

# Generated at 2022-06-14 12:12:43.157644
# Unit test for function linkify
def test_linkify():
    text = 'Hello http://tornadoweb.org!'
    result = linkify(text)
    expected = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert result == expected

# Generated at 2022-06-14 12:12:47.256912
# Unit test for function linkify
def test_linkify():
    text = linkify(b'Hello http://tornadoweb.org!')
    correct_result = 'Hello <a href="http://tornadoweb.org">http://tornadoweb.org</a>!'
    assert text == correct_result

# Generated at 2022-06-14 12:12:54.857749
# Unit test for function linkify
def test_linkify():
    url_text = "Hello http://tornadoweb.org! https://github.com/tornadoweb/tornado"
    assert linkify(url_text) == "Hello <a href='http://tornadoweb.org'>http://tornadoweb.org</a>! <a href='https://github.com/tornadoweb/tornado'>https://github.com/tornadoweb/tornado</a>"
    assert linkify(url_text, shorten=True) == "Hello <a href='http://tornadoweb.org'>http://tornadoweb.org</a>! <a href='https://github.com/tornadoweb/tornado'>https://github.com...</a>"

test_linkify()



# Generated at 2022-06-14 12:13:05.845736
# Unit test for function linkify
def test_linkify():
    assert linkify(None) == ""
    assert linkify(42) is 42
    assert linkify("") == ""
    assert linkify("Hello") == "Hello"
    assert linkify("Hello www.world.com!") == (
        'Hello <a href="http://www.world.com">www.world.com</a>!'
    )
    assert linkify("Go to http://www.world.com") == (
        'Go to <a href="http://www.world.com">http://www.world.com</a>'
    )
    assert linkify("Go to www.world.com, it's great") == (
        'Go to <a href="http://www.world.com">www.world.com</a>, it&#39;s great'
    )

# Generated at 2022-06-14 12:13:17.417968
# Unit test for function linkify
def test_linkify():
    text = "I do not like www.google.com or www.google.org"
    linkified = linkify(text, require_protocol = False)
    assert "www.google.com" in linkified
    assert "www.google.org" in linkified
    assert "<a href=\"http://www.google.com\"" in linkified
    assert "<a href=\"http://www.google.org\"" in linkified
    # linkify can take a function that develops extra parameters for the links
    def extra_params_cb(url):
        if "google" in url:
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    linkified = linkify(text, require_protocol = False, extra_params = extra_params_cb)

# Generated at 2022-06-14 12:13:31.890853
# Unit test for function linkify
def test_linkify():
    assert linkify('http://www.google.com/') == u'<a href="http://www.google.com/">http://www.google.com/</a>'
    assert linkify('http://www.google.com/') == '<a href="http://www.google.com/">http://www.google.com/</a>'
    assert linkify('http://www.google.com/', shorten=True) == '<a href="http://www.google.com/">http://www...</a>'
    assert linkify('http://www.google.com/', shorten=True, extra_params="rel='nofollow'") == "<a href=\"http://www.google.com/\" rel='nofollow'>http://www...</a>"

# Generated at 2022-06-14 12:13:42.530430
# Unit test for function linkify
def test_linkify():
    assert linkify("http://foo.com") == '<a href="http://foo.com">http://foo.com</a>'
    assert linkify("foo http://foo.com bar") == 'foo <a href="http://foo.com">http://foo.com</a> bar'
    assert linkify("foo http://foo.com") == 'foo <a href="http://foo.com">http://foo.com</a>'
    assert linkify("http://foo.com bar") == '<a href="http://foo.com">http://foo.com</a> bar'
    assert linkify("foo http://foo.com/bar.html bar") == 'foo <a href="http://foo.com/bar.html">http://foo.com/bar.html</a> bar'

# Generated at 2022-06-14 12:13:46.547558
# Unit test for function linkify
def test_linkify():
    text = "Hello http://tornadoweb.org!"
    text_linkified = linkify(text)
    assert text_linkified == "Hello <a href=\"http://tornadoweb.org\">http://tornadoweb.org</a>!"

# Generated at 2022-06-14 12:14:05.852367
# Unit test for function linkify
def test_linkify():
    assert linkify("http://google.com") == u'<a href="http://google.com">http://google.com</a>'  # noqa: E501
    assert linkify("http://google.com", shorten=True) == u'<a href="http://google.com">http://google...</a>'  # noqa: E501
    assert linkify("http://google.com", require_protocol=True) == u'<a href="http://google.com">http://google.com</a>'  # noqa: E501
    assert linkify("google.com") == u'<a href="http://google.com">google.com</a>'  # noqa: E501
    assert linkify("google.com", require_protocol=True) == u'google.com'  # noqa: E

# Generated at 2022-06-14 12:14:17.303920
# Unit test for function linkify
def test_linkify():
    import unittest
    import time
    import numpy as np
    from tornado.util import linkify
    class TestLinkify(unittest.TestCase):

        def test_linkify(self):
            # print(linkify('ok'))
            a = linkify('http://www.baidu.com')
            self.assertEqual(a,'<a href="http://www.baidu.com">http://www.baidu.com</a>')

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkify)

    unittest.main()
test_linkify()

# An email address is of the form:
#     local-part@domain
#     local-part@[IPv6:domain]
# (see RFC 5322, sec. 3.4.

# Generated at 2022-06-14 12:14:19.768401
# Unit test for function linkify
def test_linkify():
    # minimal test to make sure it doesn't crash or throw exceptions
    linkify("http://example.com")
    linkify("http://example.com", shorten=True)



# Generated at 2022-06-14 12:14:27.394030
# Unit test for function linkify
def test_linkify():
    assert linkify(
        "A simple test.", require_protocol=False
    ) == u"A simple test."
    assert linkify(
        "A test with a www.url.com/foo link in it, and another http://url.com/bar link",
        require_protocol=False,
    ) == u'A test with a <a href="http://www.url.com/foo">www.url.com/foo</a> link in it, and another <a href="http://url.com/bar">http://url.com/bar</a> link'

# Generated at 2022-06-14 12:14:42.046125
# Unit test for function linkify

# Generated at 2022-06-14 12:14:49.482693
# Unit test for function linkify
def test_linkify():
    assert (
        linkify(u"http://example.com")
        == u'<a href="http://example.com">http://example.com</a>'
    )
    assert (
        linkify(u"www.example.com")
        == u'<a href="http://www.example.com">www.example.com</a>'
    )
    assert linkify(u"sftp://example.com") == u'sftp://example.com'
    assert linkify(u"http://example.com", require_protocol=False) == u'<a href="http://example.com">http://example.com</a>'

# Generated at 2022-06-14 12:15:01.364862
# Unit test for function linkify
def test_linkify():
    def check(text: str, expected: str) -> None:
        output = linkify(text)
        assert output == expected, (repr(output), repr(expected), text)

    check('A simple http://www.tornadoweb.org link',
          'A simple <a href="http://www.tornadoweb.org">http://www.tornadoweb.org</a> link')
    check('http://tornadoweb.org/foo/bar',
          '<a href="http://tornadoweb.org/foo/bar">http://tornadoweb.org/foo/bar</a>')

# Generated at 2022-06-14 12:15:09.920392
# Unit test for function linkify
def test_linkify():
    url = "http://www.google.com/"
    link = "<a href=\"http://www.google.com/\">http://www.google.com/</a>"
    assert linkify(url) == link
    assert linkify(url, True) == link
    assert linkify(url, False) == link
    assert linkify(url, False, '') == link
    assert linkify(url, False, '') == link
    assert linkify(url, False, '') == link
    assert linkify(url, False, '') == link, "FAILED"
    assert linkify(url, False, '') == link
    assert linkify(url, False, '') == link
    assert linkify(url, False, '') == link
    assert linkify(url, False, '') == link
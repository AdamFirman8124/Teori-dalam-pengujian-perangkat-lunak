

# Generated at 2022-06-13 12:23:28.123296
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode(to_text('abc')) == 'abc'
    assert unicode_urldecode('a%20b%20c') == 'a b c'
    assert unicode_urldecode(to_text('a%20b%20c')) == 'a b c'
    assert unicode_urldecode('a+b+c') == 'a+b+c'
    assert unicode_urldecode(to_text('a+b+c')) == 'a+b+c'


# Generated at 2022-06-13 12:23:39.173852
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('http://foo.bar/') == u"http%3A%2F%2Ffoo.bar%2F"
    assert do_urlencode('http://foo.bar/test') == u"http%3A%2F%2Ffoo.bar%2Ftest"
    assert do_urlencode('http://foo.bar/?test') == u"http%3A%2F%2Ffoo.bar%2F%3Ftest"
    assert do_urlencode('http://foo.bar/?test=1') == u"http%3A%2F%2Ffoo.bar%2F%3Ftest%3D1"

# Generated at 2022-06-13 12:23:41.007086
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Hello+World%21') == u'Hello World!'



# Generated at 2022-06-13 12:23:47.564865
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    tests = (
        ('', ''),
        (' ', ' '),
        ('foo', 'foo'),
        ('%20', ' '),
        ('foo%20bar', 'foo bar'),
        ('%20foo%20bar', ' foo bar'),
        ('%2520', '%20'),
        ('%252520', '%2520'),
    )

    for t in tests:
        assert unicode_urldecode(t[0]) == t[1]


# Generated at 2022-06-13 12:23:52.901123
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test with a unicode string
    assert u'Unicode string: 文' == unicode_urldecode(u'Unicode%20string%3A%20%E6%96%87')

    # Test with a byte string
    assert u'Byte string: 文' == unicode_urldecode('Byte%20string%3A%20%E6%96%87')



# Generated at 2022-06-13 12:23:57.153928
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo') == u'foo'
    assert unicode_urlencode(u'foo/bar') == u'foo%2Fbar'
    assert unicode_urlencode(u'foo bar') == u'foo+bar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == u'foo+bar'
    assert unicode_urlencode([u'foo', u'bar']) == u'foo&bar'
    assert unicode_urlencode({u'foo': u'bar'}) == u'foo=bar'
    assert unicode_urlencode({u'foo': [u'one', u'two']}) == u'foo%5B0%5D=one&foo%5B1%5D=two'
    assert unicode

# Generated at 2022-06-13 12:24:06.806704
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json
    import os

    assert do_urldecode(u'%3A%2F%2F%3F%3D%26%25') == u'://?=&%'
    assert do_urlencode(u'://?=&%') == u'%3A%2F%2F%3F%3D%26%25'
    assert do_urlencode({u'aa': {u'bb': u'cc'}}) == u'aa=%7B%27bb%27%3A+%27cc%27%7D'
    assert do_urlencode([u'aa', {u'bb': u'cc'}]) == u'0=aa&1=%7B%27bb%27%3A+%27cc%27%7D'

    fm = FilterModule

# Generated at 2022-06-13 12:24:14.724112
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''
    Test urldecode
    '''
    module = FilterModule()

    assert module.filters()['urldecode']('%E9%98%BF%E8%8E%89%E7%89%B9%E8%8A%B1%E5%8D%A1') == \
           'éééééééééééééé'

    if not HAS_URLENCODE:
        assert module.filters()['urlencode']('éééééééééééééé') == \
               '%E9%98%BF%E8%8E%89%E7%89%B9%E8%8A%B1%E5%8D%A1'

# Generated at 2022-06-13 12:24:19.984614
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    orig = '%E2%9C%93'
    encoded = '%25E2%259C%2593'
    decoded = '%E2%9C%93'
    assert to_text(orig) == unicode_urldecode(encoded)
    assert to_text(orig) == unicode_urldecode(decoded)


# Generated at 2022-06-13 12:24:24.324610
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('test%20me') == 'test me'
    assert do_urlencode('test me') == 'test+me'
    assert do_urlencode({'k': 'v', 'k2': 'v2'}) == 'k=v&k2=v2'

# Generated at 2022-06-13 12:24:29.041171
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Create instance of FilterModule() class
    fm = FilterModule()

    # Test case(s)
    # Test urldecode filter
    pass



# Generated at 2022-06-13 12:24:38.380819
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('https://duckduckgo.com?q=raspberr') == u'https://duckduckgo.com?q=raspberr'
    assert unicode_urlencode('https://duckduckgo.com?q=raspberr', for_qs=True) == u'https://duckduckgo.com?q=raspberr'
    assert unicode_urlencode('http://www.example.com/query?foo=bar&foo=baz') == u'http://www.example.com/query?foo=bar&foo=baz'

# Generated at 2022-06-13 12:24:41.614591
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%20(b)%20c%20%26%20d%21') == u'a (b) c & d!'
    assert unicode_urldecode('FR%C3%89JUS') == u'FRÉJUS'


# Generated at 2022-06-13 12:24:45.817406
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    obj = FilterModule()
    filters = obj.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters
    assert len(filters) == 2


# Generated at 2022-06-13 12:24:58.575833
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Abc/%2F/def') == 'Abc//def'  # No change
    if PY3:
        assert type(unicode_urldecode('Abc/%2F/def')) is str  # Stay a str
    else:
        assert type(unicode_urldecode('Abc/%2F/def')) is unicode  # Stay a unicode
    assert unicode_urldecode(b'Abc/%2F/def') == 'Abc//def'  # Decoded
    if PY3:
        assert type(unicode_urldecode(b'Abc/%2F/def')) is str  # Become a str

# Generated at 2022-06-13 12:25:05.833581
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import sys
    import unittest

    if sys.version_info.major == 2:
        from backports.functools_lru_cache import lru_cache
    else:
        from functools import lru_cache

    # Test cases taken from https://docs.djangoproject.com/en/1.10/ref/unicode/#url-quoting
    @lru_cache(maxsize=None)
    def urlquoting(string, safe=b''):
        """Our own version of urlunquote taken from
        https://docs.djangoproject.com/en/1.10/ref/unicode/#url-quoting
        """
        if isinstance(string, str):
            string = string.encode('utf-8')
        if not safe:
            safe = b''
        string

# Generated at 2022-06-13 12:25:10.579165
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    assert unicode_urldecode("abc") == "abc"

    assert unicode_urldecode("777") == "777"

    assert unicode_urldecode("a%41bc") == "aAbc"

    print("unicode_urldecode PASS")
test_unicode_urldecode()


# Generated at 2022-06-13 12:25:21.129661
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Test unicode urlencode
    assert unicode_urlencode(u'http://example.com/') == u'http%3A//example.com/'
    assert unicode_urlencode(u'http://example.com/') == b'http%3A//example.com/'
    assert unicode_urlencode(u'http://example.com/') == b'http%3A//example.com/'
    assert unicode_urlencode(u'http://example.com/') == b'http%3A//example.com/'
    assert unicode_urlencode(u'http://example.com/') == b'http%3A//example.com/'

# Generated at 2022-06-13 12:25:26.802620
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_string = "http://example.com/test?a=b"
    test_cases = [
        (test_string, "http%3A//example.com/test%3Fa%3Db"),
        (u'\xe9', "%C3%A9"),
        (u"\u00e9", "%C3%A9"),
        (u"a+b", "a%2Bb"),
        (u"a b", "a+b"),
    ]

    for (string, result) in test_cases:
        assert unicode_urlencode(string) == result
        assert unicode_urlencode(string, for_qs=True) == result


# Generated at 2022-06-13 12:25:35.253531
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    unicode_data = u'\u043e\u0433\u043e\u0440\u043d\u0438\u043a\u0430\u043b\u043d\u043e\u0435 \u0441\u043b\u043e\u0432\u043e'
    str_data = unicode_data.encode('utf-8')

    # Test urldecode
    assert do_urldecode(unicode_data) == unicode_data
    assert do_urldecode(str_data).encode('utf-8') == str_data


# Generated at 2022-06-13 12:25:38.625958
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule.filters(FilterModule)

if __name__=="__main__":
    test_FilterModule_filters()

# Generated at 2022-06-13 12:25:43.502673
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json

    _filter = FilterModule()
    _filters = _filter.filters()

    # Only test urlencode if Jinja2 is older than v2.7
    if not HAS_URLENCODE:
        assert _filters['urldecode']('http%3A%2F%2Fwww.example.com%3Fid%3D123') == 'http://www.example.com?id=123'
        assert _filters['urldecode']('http%3A%2F%2Fwww.example.com%3Fid%3D123%26name%3Dfoo+bar') == 'http://www.example.com?id=123&name=foo+bar'

# Generated at 2022-06-13 12:25:50.135891
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # test for Python 2 and 3
    test_input = "a%2Fb+c%40d"
    expected = "a/b c@d"
    actual = unicode_urldecode(test_input)
    assert actual == expected
    # test for Python 2
    test_input = to_bytes("a%2Fb+c%40d")
    expected = to_bytes("a/b c@d")
    actual = unicode_urldecode(test_input)
    assert actual == expected


# Generated at 2022-06-13 12:25:53.597996
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] == do_urldecode
    assert filters['urlencode'] == do_urlencode

# Unit tests for do_urldecode

# Generated at 2022-06-13 12:25:57.292236
# Unit test for function do_urlencode
def test_do_urlencode():
    # this is a free-text encoding test
    assert do_urlencode("@#$%^&") == "@%23%24%25%5E%26"

    # this is a hard-coded test for a known transformation
    assert do_urlencode({"a": "b"}) == "a=b"



# Generated at 2022-06-13 12:26:01.374254
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module_filters = FilterModule().filters()

    assert module_filters['urldecode']('https%3A%2F%2Fwww.google.com%2F') == 'https://www.google.com/'

    if not HAS_URLENCODE:
        assert module_filters['urlencode']('https://www.google.com') == 'https%3A//www.google.com'


# Generated at 2022-06-13 12:26:05.898760
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    p = FilterModule()
    filters = p.filters()
    assert filters['urlencode'] == do_urlencode
    assert filters['urldecode'] == do_urldecode



# Generated at 2022-06-13 12:26:14.936958
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%7E') == '~'
    assert unicode_urldecode('%E3%81%82') == u'あ'
    assert unicode_urldecode('%2F') == u'/'
    assert unicode_urldecode('%25') == u'%'
    assert unicode_urldecode('%80') == u'\x80'
    assert unicode_urldecode('%7F') == u'\x7f'
    assert unicode_urldecode('%25') == u'%'


# Generated at 2022-06-13 12:26:15.768195
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()


# Generated at 2022-06-13 12:26:25.055541
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import doctest
    doctest.testmod(verbose=True)
    if PY3:
      print("Py3: %s" % (unicode_urlencode(u'https://www.google.com/search?q=Модульные тесты в Ансибл')))

# Generated at 2022-06-13 12:26:36.258746
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # http://www.w3schools.com/tags/ref_urlencode.asp
    assert unicode_urldecode('https://en.wikipedia.org/wiki/URL_encode') == 'https://en.wikipedia.org/wiki/URL_encode'
    assert unicode_urldecode('https://en.wikipedia.org/wiki/URL_encode%3F') == 'https://en.wikipedia.org/wiki/URL_encode?'
    assert unicode_urldecode('https://en.wikipedia.org/wiki/URL_encode?%26') == 'https://en.wikipedia.org/wiki/URL_encode?&'



# Generated at 2022-06-13 12:26:41.764708
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("a%2Bb%2Bc") == u"a+b+c"
    assert unicode_urldecode("a%2bB%2Bc") == u"a+B+c"

    assert unicode_urldecode("%C3%A5") == u"å"
    assert unicode_urldecode("%c3%A5") == u"å"

    assert unicode_urldecode("%c3%a5") == u"å"

# Generated at 2022-06-13 12:26:44.224873
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' Method filters of class FilterModule '''

    filters = FilterModule().filters()

    assert filters['urldecode']('abc%20def') == 'abc def'

    if not HAS_URLENCODE:
        assert filters['urlencode']('abc def') == 'abc%20def'



# Generated at 2022-06-13 12:26:52.515352
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils.basic import AnsibleModule
    assert unicode_urlencode('/') == u'/'
    assert unicode_urlencode('/', for_qs=True) == u'%2F'
    assert unicode_urlencode('foo') == u'foo'
    assert unicode_urlencode('foo', for_qs=True) == u'foo'



# Generated at 2022-06-13 12:26:59.265746
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """Basic tests for class."""
    fm = FilterModule()

    assert fm.filters()['urldecode']('%2C') == ',', 'urldecode'

    if not HAS_URLENCODE:
        assert fm.filters()['urlencode']('%!') == '%25%21', 'urlencode'



# Generated at 2022-06-13 12:27:04.538646
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert(unicode_urlencode('&') == '%26')
    assert(unicode_urlencode('&', True) == '%26')
    assert(unicode_urlencode('/') == '%2F')
    assert(unicode_urlencode('/', True) == '%2F')
    assert(unicode_urlencode('foo') == 'foo')
    assert(unicode_urlencode('foo', True) == 'foo')
    assert(unicode_urlencode('foo bar') == 'foo+bar')
    assert(unicode_urlencode('foo bar', True) == 'foo+bar')

# Generated at 2022-06-13 12:27:14.685294
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'%20') == u' '
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(b'%61') == u'a'
    assert unicode_urldecode(u'%61') == u'a'
    assert unicode_urldecode(b'%u20AC') == u'\u20ac'
    assert unicode_urldecode(u'%u20AC') == u'\u20ac'
    assert unicode_urldecode(b'%F0%9F%92%A9') == u'\U0001f4a9'

# Generated at 2022-06-13 12:27:19.691594
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert 'Hello World!' == unicode_urldecode('Hello%20World%21')
    assert 'Hello World!' == unicode_urldecode('Hello World!')
    assert 'Hello World!' == unicode_urldecode(b'Hello%20World%21')


# Generated at 2022-06-13 12:27:22.834540
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('%25%27') == '%\''
    else:
        assert unicode_urldecode('%25%27') == u'%\''


# Generated at 2022-06-13 12:27:28.631575
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('abc') == 'abc'
    assert unicode_urlencode('x y') == 'x%20y'
    assert unicode_urlencode('x y', for_qs=True) == 'x+y'
    assert unicode_urlencode('x/y') == 'x%2Fy'


# Generated at 2022-06-13 12:27:46.951156
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('http%3A%2F%2Fexample%2Eorg%2F') == 'http://example.org/'
    assert unicode_urldecode('%3F%26%3D%2C%2F%3A') == '?&=,/:'
    assert unicode_urldecode('%E2%80%99%C2%B4%E2%80%99%C2%B4%E2%80%99') == '\u2019\u00b4\u2019\u00b4\u2019'
    assert unicode_urldecode('%E2%80%A6') == '\u2026'

# Generated at 2022-06-13 12:27:54.730129
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode("foo%20bar") == "foo bar"
    assert do_urlencode("foo") == "foo"
    assert do_urlencode("foo bar") == "foo%20bar"
    assert do_urlencode("foo+bar") == "foo%2Bbar"
    assert do_urlencode("foo?bar") == "foo%3Fbar"
    assert do_urlencode("foo bar+baz?") == "foo%20bar%2Bbaz%3F"
    assert do_urlencode("foo=bar") == "foo%3Dbar"
    assert do_urlencode("foo=bar&baz=qux") == "foo%3Dbar&baz%3Dqux"

# Generated at 2022-06-13 12:28:00.748014
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    def test(value, is_query=False):
        actual = unicode_urlencode(value, for_qs=is_query)
        expected = do_urlencode(value)
        if actual != expected:
            raise AssertionError("%r != %r" % (actual, expected))

    test('abc')
    test('abc@example.org')
    test('http://www.example.org:80/')
    test('a+b c')
    test('a b c')
    test({'a': 'b c'}, is_query=True)
    test(['a', 'b c'], is_query=True)

# Generated at 2022-06-13 12:28:12.848746
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import jinja2
    from ansible.module_utils.six.moves.urllib.parse import parse_qsl, urlparse
    from ansible.module_utils.six.moves.urllib.parse import urlencode as urllib_urlencode

    # Create a jinja2 environment with our custom filters and tests
    env = jinja2.Environment(loader=jinja2.DictLoader({}), trim_blocks=True, lstrip_blocks=True)
    env.filters.update(FilterModule().filters())

    def assert_template_result(template, expected, **kwargs):
        result = env.from_string(template).render(kwargs).strip()
        # Assert that a template does result in the expected value (after trimming whitespace)
        assert expected == result

    #

# Generated at 2022-06-13 12:28:28.022645
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:28:29.866602
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'f%C3%B6%C3%B6') == u'föö'


# Generated at 2022-06-13 12:28:33.320662
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3A%2F%2Ffoo%2Fbar%2F') == u'http://foo/bar/'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'


# Generated at 2022-06-13 12:28:36.385116
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%25') == u'%'
    # Python 2.7 (or higher) urllib.unquote_plus is not encoding safe
    if PY3:
        assert unicode_urldecode('%25%25') == u'%%'



# Generated at 2022-06-13 12:28:41.711727
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'one=1&two=2' == unicode_urldecode('one%3D1%26two%3D2')
    assert u'one=1&two=2&two=3' == unicode_urldecode('one%3D1%26two%3D2%26two%3D3')



# Generated at 2022-06-13 12:28:47.980571
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # test FilterModule.filters
    filtersModule = FilterModule()
    filters = filtersModule.filter()

    # test FilterModule.filters['urldecode']
    assert filters['urldecode']('key1=value1&key2=value2') == 'key1=value1&key2=value2'

    # test FilterModule.filters['urlencode']
    if HAS_URLENCODE:
        assert filters['urlencode']('key1=value1&key2=value2') == 'key1=value1&key2=value2'


# Generated at 2022-06-13 12:29:02.729506
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('') == u''
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('ABC') == u'ABC'
    assert unicode_urldecode('%3A%3a') == u'::'
    assert unicode_urldecode('%3a%3A') == u'::'
    assert unicode_urldecode('%26') == u'&'
    assert unicode_urldecode('%3d') == u'='
    assert unicode_urldecode('%3D') == u'='
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%2B') == u'+'
    assert unicode_urld

# Generated at 2022-06-13 12:29:04.127954
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode(u'foo%2Fbar') == u'foo/bar'

# Generated at 2022-06-13 12:29:10.835001
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'  ' == unicode_urldecode('+%20+')
    assert u'中文' == unicode_urldecode('%E4%B8%AD%E6%96%87')
    assert u'?&=' == unicode_urldecode('%3F%26%3D')


# Generated at 2022-06-13 12:29:24.800863
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys
    import unittest

    class TestUrldecode(unittest.TestCase):

        def test_urldecode(self):

            if sys.version_info[0] == 2:
                self.assertEqual(unicode_urldecode(u'%F1'), u'\xf1')

            self.assertEqual(unicode_urldecode(u'%25%2B%25'), u'%+%')
            self.assertEqual(unicode_urldecode(u'%25%2B%25'), u'%+%')

            self.assertEqual(unicode_urldecode(u'++++'), u'++++')

# Generated at 2022-06-13 12:29:29.608740
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('url%20encode%20me%40example.com') == u'url encode me@example.com'
    assert unicode_urldecode('url+encode+me+%40+example.com') == u'url encode me @ example.com'

# Generated at 2022-06-13 12:29:39.791597
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert do_urlencode(u'http://foo/bar?a=b%20c&d=e') == u'http%3A%2F%2Ffoo%2Fbar%3Fa%3Db%2520c%26d%3De'
    assert do_urlencode(u'foo+') == u'foo%2B'  # RFC 1738
    assert do_urlencode(u'foo+', for_qs=True) == u'foo%2B'
    assert do_urlencode(u'foo ') == u'foo%20'  # RFC 1738
    assert do_urlencode(u'foo ', for_qs=True) == u'foo+'
    assert do_urlencode(u'foo/') == u'foo%2F'  # RFC 1738
    assert do

# Generated at 2022-06-13 12:29:48.777361
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('abc') == 'abc'
    assert do_urlencode(u'abc') == 'abc'

    assert do_urlencode('abc def') == 'abc%20def'
    assert do_urlencode(u'abc def') == 'abc%20def'

    assert do_urlencode('abc/def') == 'abc%2Fdef'
    assert do_urlencode(u'abc/def') == 'abc%2Fdef'

    assert do_urlencode({'q': 'abc def'}) == 'q=abc%20def'
    assert do_urlencode({u'q': 'abc def'}) == 'q=abc%20def'


# Generated at 2022-06-13 12:29:55.720152
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    filters = module.filters()

    assert do_urldecode(b'foo%20bar') == u'foo bar'
    assert do_urldecode('foo%20bar') == u'foo bar'

    if not HAS_URLENCODE:
        assert do_urlencode(b'foo bar') == 'foo%20bar'
        assert do_urlencode(u'foo bar') == 'foo%20bar'
        assert do_urlencode({'a': 'b c', 'd': 'e'}) == 'a=b%20c&d=e'
        assert do_urlencode(['foo', 'bar']) == 'foo&bar'

# Generated at 2022-06-13 12:29:58.838656
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Test unicode_urldecode function with ascii values
    '''
    input_string = u'%E2%82%AC%20%E2%82%AC'
    assert unicode_urldecode(input_string) == u'€ €'


# Generated at 2022-06-13 12:30:00.225196
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('hello world') == 'hello world'
    assert unicode_urldecode('hello%20world') == 'hello world'



# Generated at 2022-06-13 12:30:13.008783
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("john&bob") == "john%26bob"
    assert unicode_urlencode("/foo?bar=baz") == "%2Ffoo%3Fbar%3Dbaz"
    assert unicode_urlencode("john&bob", True) == "john%26bob"
    assert unicode_urlencode("/foo?bar=baz", True) == "%2Ffoo%3Fbar%3Dbaz"

# Generated at 2022-06-13 12:30:15.761944
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('dag%20wieers') == u'dag wieers'
    assert unicode_urldecode('dag+wieers') == u'dag wieers'


# Generated at 2022-06-13 12:30:23.607599
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a+%20b+%20c') == 'a b c'
    assert unicode_urldecode('a%2B1+%2B20') == 'a+1 +20'
    assert unicode_urldecode('%7B%22branch%22%3A%22master%22%7D') == '{"branch":"master"}'
    assert unicode_urldecode('%7b%22branch%22%3a%22master%22%7d') == '{"branch":"master"}'


# Generated at 2022-06-13 12:30:35.517207
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest

    # Create an instance of FilterModule
    filters = FilterModule().filters()

    # Test urldecode_string
    actual = filters['urldecode']('https%3A%2F%2Fgithub.com%2F%25B0%25E1%25BF%25C1%25C2%25B8%25F3%25D3%25BB%25F3%25B3%25B9%25C9%25F0%25CF%25D2%25C7%25D6%25B7%25FC%25A2%25D4%25B1%25BE%25C0')

# Generated at 2022-06-13 12:30:39.964953
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter = FilterModule()
    assert filter.filters()['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filter.filters()['urlencode'] == do_urlencode
    else:
        assert 'urlencode' not in filter.filters()


# Generated at 2022-06-13 12:30:44.673321
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('foo') == 'foo'
    assert do_urlencode('foo/bar') == 'foo%2Fbar'
    assert do_urlencode(['foo', 'bar']) == 'foo&bar'
    assert do_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert do_urlencode({'foo': 'bar', 'test': 'value'}) == 'foo=bar&test=value'

# Generated at 2022-06-13 12:30:46.732406
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys
    u_phrase = u'urldecode test phrase'
    code = unicode_urldecode(u_phrase)
    assert u_phrase == code


# Generated at 2022-06-13 12:30:50.436911
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/') == b'/'
    assert unicode_urlencode('/', for_qs=True) == b'%2F'
    assert unicode_urlencode('foo+bar') == b'foo+bar'
    assert unicode_urlencode('foo+bar', for_qs=True) == b'foo%2Bbar'

# Generated at 2022-06-13 12:30:52.414349
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    data = f.filters()
    assert data['urldecode'] == do_urldecode
    assert data['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:30:56.072195
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert(unicode_urldecode(u"foo") == u"foo")
    assert(unicode_urldecode(u"foo+bar") == u"foo bar")
    assert(unicode_urldecode(u"foo%20bar") == u"foo bar")
    assert(unicode_urldecode(u"foo%26bar") == u"foo&bar")
    assert(unicode_urldecode(u"foo%30bar") == u"foo0bar")


# Generated at 2022-06-13 12:31:07.989626
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7B%7D') == u'{}'
    assert unicode_urldecode('%7B%7D:%7B%7D') == u'{}:{}'



# Generated at 2022-06-13 12:31:17.296112
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%F0%9F%92%A9%F0%9F%92%A9%F0%9F%92%A9') == u'💩💩💩'
    assert unicode_urldecode(b'%F0%9F%92%A9%F0%9F%92%A9%F0%9F%92%A9') == u'💩💩💩'
    assert unicode_urldecode(u'%F0%9F%92%A9%2B%2B%2B') == u'💩+++'
    assert unicode_urldecode(u'%F0%9F%92%A9+%2B+') == u'💩 +++'

# Generated at 2022-06-13 12:31:20.423869
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule().filters()
    assert 'urldecode' in f
    assert f['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert 'urlencode' in f
        assert f['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:31:29.327004
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    expected_result_1 = u"This is a simple text"
    expected_result_2 = u"This%20is%20a%20simple%20text"

    result_1 = unicode_urldecode(expected_result_1)
    result_2 = unicode_urldecode(expected_result_2)

    assert expected_result_1 == result_1
    assert expected_result_1 == result_2


# Generated at 2022-06-13 12:31:38.151463
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()

    def assert_equal(a, b):
        assert(a == b)

    # Test: urldecode
    if not HAS_URLENCODE:
        assert_equal(fm.filters()['urldecode']('a%3D1%26b%3D2'), u'a=1&b=2')
    else:
        assert_equal(fm.filters()['urldecode']('a%3D1%26b%3D2'), u'a=1&b=2')
    if not HAS_URLENCODE:
        assert_equal(fm.filters()['urldecode'](u'a%3D1%26b%3D2'), u'a=1&b=2')

# Generated at 2022-06-13 12:31:41.768938
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    for string in ('%20', '%2f', '%2F', '%C2%A9', '%e2%82%ac'):
        assert unicode_urldecode(string) == unquote_plus(string)


# Generated at 2022-06-13 12:31:46.031174
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys
    if sys.version_info[0] == 2:
        from ansible.module_utils import basic
        assert unicode_urldecode(b'%27') == u"'"
        assert basic.urllib_error is not None


# Generated at 2022-06-13 12:31:53.150687
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # 1. Test bytes
    assert unicode_urldecode(b'TEST') == u'TEST'

    # 2. Test text
    assert unicode_urldecode(u'TEST') == u'TEST'

    # 3. Test text
    assert unicode_urldecode(u'TEST%20TEST') == u'TEST TEST'
    assert unicode_urldecode(u'TEST+TEST') == u'TEST TEST'

    # 4. Test bytes
    assert unicode_urldecode(b'TEST%20TEST') == u'TEST TEST'
    assert unicode_urldecode(b'TEST+TEST') == u'TEST TEST'



# Generated at 2022-06-13 12:31:58.234895
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters.get("urldecode") is not None
    if not HAS_URLENCODE:
        assert filters.get("urlencode") is not None


# Test for class FilterModule

# Generated at 2022-06-13 12:32:05.122786
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'abcABC') == 'abcABC'
    assert unicode_urlencode(u'abc%1ABC') == 'abc%251ABC'
    assert unicode_urlencode(u'abc+1ABC') == 'abc%2B1ABC'
    assert unicode_urlencode(u'abc+1ABC', True) == 'abc%2B1ABC'
    assert unicode_urlencode(u'abc+1ABC', False) == 'abc+1ABC'


# Generated at 2022-06-13 12:32:30.413938
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import unittest

    class TestModule(unittest.TestCase):
        def test_unicode_urlencode_dict(self):
            expected = u'a=1&b=2%2C3&c=4%2C%205%26'
            actual = unicode_urlencode({'a': '1', 'b': ['2', '3'], 'c': ['4', ' 5&']})
            self.assertEqual(expected, actual)

        def test_do_urlencode_dict(self):
            expected = u'a=1&b=2%2C3&c=4%2C%205%26'
            actual = do_urlencode({'a': '1', 'b': ['2', '3'], 'c': ['4', ' 5&']})

# Generated at 2022-06-13 12:32:31.853211
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '



# Generated at 2022-06-13 12:32:34.241271
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filters = FilterModule().filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:32:41.627839
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' Test unquote_plus on utf8 string '''
    if PY3:
        assert unicode_urldecode(b'foo%C3%A4') == 'fooä'
        assert unicode_urldecode('foo%C3%A4') == 'fooä'
    else:
        assert unicode_urldecode(b'foo%C3%A4') == u'fooä'
        assert unicode_urldecode('foo%C3%A4') == u'fooä'


if __name__ == '__main__':
    test_unicode_urldecode()

# Generated at 2022-06-13 12:32:48.120333
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    result = unicode_urlencode(u'http://example.org/中文')
    assert result == u'http%3A%2F%2Fexample.org%2F%E4%B8%AD%E6%96%87'
    result = unicode_urlencode(u'http://example.org/中文', for_qs=True)
    assert result == u'http%3A%2F%2Fexample.org%2F%E4%B8%AD%E6%96%87'


# Generated at 2022-06-13 12:32:52.173770
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20%D0%BF%D1%80%D0%B8-%D0%B2%D0%B5%D1%89%D0%B5%20') == u' при-веще '

# Generated at 2022-06-13 12:32:56.022142
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'has space' == unicode_urldecode('has%20space')
    assert u'@+,/' == unicode_urldecode('%40%2B%2C%2F')
    assert u'\x00' == unicode_urldecode('%00')
    assert u'\u2603' == unicode_urldecode('%E2%98%83')
    assert u'\u00e9' == unicode_urldecode('%C3%A9')
    assert u'\U0001f4a9' == unicode_urldecode('%F0%9F%92%A9')



# Generated at 2022-06-13 12:32:57.490237
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filterModule = FilterModule()
    filters = filterModule.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters

# Generated at 2022-06-13 12:33:01.510576
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'I%27m%20a%20little%20tekky') == u"I'm a little tekky"



# Generated at 2022-06-13 12:33:04.203286
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode


# Generated at 2022-06-13 12:23:22.521198
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm is not None



# Generated at 2022-06-13 12:23:35.841736
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.six.moves.urllib.parse import quote, quote_plus
    import sys


# Generated at 2022-06-13 12:23:44.362164
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Default:
    assert unicode_urlencode(u'http://localhost/') == u'http%3A//localhost/'
    assert unicode_urlencode(u'http://localhost/', for_qs=True) == u'http%3A%2F%2Flocalhost%2F'

    # Unicode:
    assert unicode_urlencode(u'http://localhost/δοκιμή') == u'http%3A//localhost/%CE%B4%CE%BF%CE%BA%CE%B9%CE%BC%CE%AE'

# Generated at 2022-06-13 12:23:47.100541
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('test1') == u'test1'
    assert unicode_urldecode('test%20+%2B') == u'test ++'



# Generated at 2022-06-13 12:23:55.572243
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    testcases = (
        (u'+abcd', u' abcd'),
        (u'%3fabcd', u'%3fabcd'),
        (u'%abcd', u'%abcd'),
        (u'%3a%3fabcd', u':%3fabcd'),
    )
    for test in testcases:
        msg = u"Error: unicode_urldecode(%s) returned %s instead of %s"
        assert unicode_urldecode(test[0]) == test[1], msg % (test[0], unicode_urldecode(test[0]), test[1])


# Generated at 2022-06-13 12:24:05.553696
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(u'%3D') == u'='
    assert unicode_urldecode(u'%09') == u'\t'
    assert unicode_urldecode(u'%E6%96%87') == u'文'
    assert unicode_urldecode(u'%2B%25%3D%09%E6%96%87') == u'+%=\t文'
    # Test plus sign
    assert unicode_urldecode(u'+') == u'+'
    assert unicode_urldecode(u'%2B') == u

# Generated at 2022-06-13 12:24:08.562821
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    data = u'%s' % (chr(174) * 256)
    assert unicode_urldecode(unicode_urlencode(data)) == data

# Generated at 2022-06-13 12:24:19.299597
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys
    import copy
    import pytest

    f = FilterModule()

    filters = f.filters()

    assert filters['urldecode'](u'привет') == u'привет'

    if not HAS_URLENCODE:
        assert filters['urlencode'](u'привет') == u'%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82'

    assert filters['urldecode'](filters['urlencode'](u'привет')) == u'привет'

# Generated at 2022-06-13 12:24:24.755515
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test invalid data
    try:
        unicode_urldecode(None)
    except Exception:
        pass
    else:
        assert False, "unicode_urldecode returns None for invalid data"

    # Test basic decoding
    assert unicode_urldecode('x') == u'x'
    assert unicode_urldecode('%20') == u' '



# Generated at 2022-06-13 12:24:35.533995
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import unittest

    class Test(unittest.TestCase):
        def test_unicode_urlencode(self):
            self.assertEqual(unicode_urlencode(u'User %'), u'User%20%25')
            self.assertEqual(unicode_urlencode(u'User %', for_qs=True), u'User%20%25')
            self.assertEqual(unicode_urlencode({'foo': u'User %', 'bar': u'User %'}),
                             u'foo=User%20%25&bar=User%20%25')
            self.assertEqual(unicode_urlencode(u'/var/log/auth.log'), u'/var/log/auth.log')

    suite = unittest.TestLoader().loadTestsFromTestCase

# Generated at 2022-06-13 12:24:45.243152
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://localhost/føø') == 'http%3A%2F%2Flocalhost%2Ff%C3%B8%C3%B8'
    assert unicode_urlencode('/føø/bar') == '%2Ff%C3%B8%C3%B8%2Fbar'
    assert unicode_urlencode('/føø/bar?abc=xyz') == '%2Ff%C3%B8%C3%B8%2Fbar%3Fabc%3Dxyz'

# Generated at 2022-06-13 12:24:56.832158
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(to_bytes(u'abcd')) == u'abcd'
    assert unicode_urldecode(u'abcd') == u'abcd'
    assert unicode_urldecode(to_bytes(u'%25')) == u'%'
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(to_bytes(u'%25%25')) == u'%%'
    assert unicode_urldecode(u'%25%25') == u'%%'


# Generated at 2022-06-13 12:25:04.935881
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('& /:?#') == '%26%20%2F%3A%3F%23'
    assert do_urlencode('Cats & dogs') == 'Cats%20%26%20dogs'
    assert do_urlencode(['Cats & dogs']) == 'Cats%20%26%20dogs'
    assert do_urlencode(['Cats', '&', 'dogs']) == 'Cats&%26&dogs'
    assert do_urlencode({'one': 'Cats', 'two': '&', 'three': 'dogs'}) == 'one=Cats&two=%26&three=dogs'

# Generated at 2022-06-13 12:25:09.803314
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    module = FilterModule()

    assert module.filters()['urldecode']("%2Fetc%2Fmotd") == u"/etc/motd"

    if not HAS_URLENCODE:
        assert module.filters()['urlencode'](u"/etc/motd") == u"%2Fetc%2Fmotd"

# Generated at 2022-06-13 12:25:20.351333
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    """
    Test cases for unicode_urlencode
    """
    assert unicode_urlencode("") == u""
    assert unicode_urlencode("/") == u"%2F"
    assert unicode_urlencode("?") == u"?"
    assert unicode_urlencode("/?") == u"%2F?"
    assert unicode_urlencode("/?") == u"%2F?"
    assert unicode_urlencode("foo bar") == u"foo+bar"
    assert unicode_urlencode("foo bar", for_qs=True) == u"foo%20bar"
    assert unicode_urlencode({"x": "foo bar"}) == u"x=foo+bar"

# Generated at 2022-06-13 12:25:28.256599
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('') == u''
    assert unicode_urlencode('abc') == u'abc'
    assert unicode_urlencode('abc @') == u'abc%20%40'
    assert unicode_urlencode('abc @', True) == u'abc%20%40'
    assert unicode_urlencode('abc !@#$%^&*()_+=/') == u'abc%20!%40%23%24%25%5E%26*()_+%3D%2F'
    assert unicode_urlencode('abc !@#$%^&*()_+=/', True) == u'abc+!%40%23%24%25%5E%26%2A%28%29_%2B%3D%2F'
    assert unicode_

# Generated at 2022-06-13 12:25:29.595012
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%BC') == u'\xfc'
    assert unicode_urldecode(u'%FC') == u'\xfc'


# Generated at 2022-06-13 12:25:34.533555
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Python 3.x unicode
    assert unicode_urldecode('%C3%A9') == u'é'
    # Python 2.x unicode
    assert unicode_urldecode('%C3%A9') == u'é'
    # Python 3.x unicode
    assert unicode_urldecode('%C3%A9') == u'é'
    # Python 2.x unicode
    assert unicode_urldecode('%C3%A9') == u'é'


# Generated at 2022-06-13 12:25:36.851494
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"http%3A%2F%2Fmy.domain.com%2Ffoo%2Fbar%2Fbaz") == u"http://my.domain.com/foo/bar/baz"


# Generated at 2022-06-13 12:25:40.151922
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'hello') == u'hello'
    assert unicode_urlencode(u'hello / world') == u'hello%20%2F%20world'
    assert unicode_urlencode(u'hello / world', for_qs=True) == u'hello+%2F+world'


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 12:25:44.368163
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc%3D') == 'abc='

# Generated at 2022-06-13 12:25:50.018801
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('foo') == u'foo'
    assert unicode_urlencode('foo bar') == u'foo%20bar'
    assert unicode_urlencode('foo+bar') == u'foo%2Bbar'
    assert unicode_urlencode('foo/bar') == u'foo%2Fbar'
    assert unicode_urlencode('foo/bar', for_qs=True) == u'foo%2Fbar'


# Generated at 2022-06-13 12:25:58.433972
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest

    # Get a FilterModule object
    fm = FilterModule()
    assert fm is not None

    # Test with Jinja2 version with urlencode filter
    filters = fm.filters()
    assert len(filters) == 1
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode

    # Test with Jinja2 version without urlencode filter
    filters = fm.filters()
    assert len(filters) == 2
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    assert 'urlencode' in filters
    assert filters['urlencode'] == do_urlencode

    # Test urldecode filter

# Generated at 2022-06-13 12:26:00.861534
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'é'
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('+') == u' '



# Generated at 2022-06-13 12:26:04.972907
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    assert filter_module.filters() == {'urldecode': do_urldecode}



# Generated at 2022-06-13 12:26:13.078715
# Unit test for function do_urlencode
def test_do_urlencode():
    unencoded = 'http://localhost:9200/query?q=name:中国企业'
    assert do_urldecode(do_urlencode(unencoded)) == unencoded
    unencoded = {'q': 'name:中国企业'}
    assert do_urldecode(do_urlencode(unencoded)) == 'q=name%3A%E4%B8%AD%E5%9B%BD%E4%BC%81%E4%B8%9A'


# Generated at 2022-06-13 12:26:14.547846
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7E%60') == u'~`'


# Generated at 2022-06-13 12:26:23.369940
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils.urls import open_url
    response, info = open_url('https://www.google.com/')
    assert unicode_urlencode('Hello world!') == 'Hello%20world%21'
    assert unicode_urlencode('Hello world!', for_qs=True) == 'Hello+world%21'
    assert unicode_urlencode(u'Hello world!') == b'Hello%20world%21'
    assert unicode_urlencode(u'Hello world!', for_qs=True) == b'Hello+world%21'
    assert unicode_urlencode({'hello': 'world!'}) == 'hello=world%21'
    assert unicode_urlencode(('hello', 'world!')) == 'hello=world%21'
    assert unicode_url

# Generated at 2022-06-13 12:26:26.718341
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%A1') == 'á'
    assert unicode_urldecode(u'foo%20bar') == 'foo bar'



# Generated at 2022-06-13 12:26:30.712696
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils.six import u

    assert unicode_urldecode('%21%23%25%2B%7E%5E%7C%5C') == u('!#%+~^|\\')
    assert unicode_urldecode('%00') == u('\x00')


if __name__ == '__main__':
    test_unicode_urldecode()

# Generated at 2022-06-13 12:26:42.196933
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('& A') == u'%26%20A'
    assert do_urlencode('A=1') == u'A%3D1'
    assert do_urlencode(['A=1']) == u'A%3D1'
    assert do_urlencode('http://foo/?a=1+2&b=3%20x') == u'http%3A%2F%2Ffoo%2F%3Fa%3D1%2B2%26b%3D3%20x'
    assert do_urlencode({'A': 1, 'B': 'C'}) == u'A=1&B=C'

# Generated at 2022-06-13 12:26:50.635564
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Test String
    assert unicode_urlencode('Ying & Yang') == 'Ying%20%26%20Yang'
    assert unicode_urlencode('http://localhost/Ying & Yang') == 'http%3A//localhost/Ying%20%26%20Yang'
    assert unicode_urlencode('http://localhost/Ying & Yang', True) == 'http%3A%2F%2Flocalhost%2FYing%20%26%20Yang'
    assert unicode_urlencode('http://localhost/Ying & Yang', True) == 'http%3A%2F%2Flocalhost%2FYing%20%26%20Yang'
    assert unicode_urlencode(['Ying', 'Yang', 'Yong']) == 'Ying&Yang&Yong'
    assert unic

# Generated at 2022-06-13 12:26:53.899094
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode('abc%2Fdef') == 'abc/def'
    assert unicode_urldecode('abc+def') == 'abc def'
    assert unicode_urldecode('abc%20def') == 'abc def'
    assert unicode_urldecode('abc%21def') == 'abc!def'


# Generated at 2022-06-13 12:27:00.883179
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # The b'' in this Python 3 line is really needed.
    assert unicode_urldecode(b'%E5%A4%A7%E9%BB%84%E5%B0%8F%E9%A3%9F%E8%8A%B1') == u'\u5927\u9ec4\u5c0f\u98df\u8349'


# Generated at 2022-06-13 12:27:04.401901
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    input = '%E9%9F%B3%E6%A5%BD'
    expected_output = u'音楽'
    output = unicode_urldecode(input)
    assert output == expected_output



# Generated at 2022-06-13 12:27:14.574076
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test with Jinja2 version < v2.7
    old_filters = FilterModule().filters()
    assert old_filters == {'urldecode': do_urldecode, 'urlencode': do_urlencode}
    assert old_filters['urldecode'](u'foo+bar') == u'foo bar'
    assert old_filters['urlencode'](u'foo bar') == u'foo+bar'
    assert old_filters['urlencode'](u'foo+bar') == u'foo%2Bbar'
    assert old_filters['urlencode']({'foo': 'bar'}) == u'foo=bar'

# Generated at 2022-06-13 12:27:19.926983
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert type(filters['urldecode']) == type(do_urldecode)
    assert 'urlencode' in filters
    assert type(filters['urlencode']) == type(do_urlencode)

# Generated at 2022-06-13 12:27:24.784839
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_dict = {
        "foo": "foo&bar",
        "bar": "foo=bar",
        "spam": "/foo/bar",
        "eggs": "foo+bar",
    }

    assert unicode_urlencode(test_dict) == u'eggs=foo%2Bbar&foo=foo%26bar&bar=foo%3Dbar&spam=%2Ffoo%2Fbar'

# Generated at 2022-06-13 12:27:31.925914
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode('abc+') == 'abc '
    assert unicode_urldecode('abc%20') == 'abc '
    assert unicode_urldecode('abc%26') == 'abc&'
    assert unicode_urldecode('abc%26def') == 'abc&def'
    # FIXME: This should also work
    # assert unicode_urldecode('abc%26def%3D') == 'abc&def='



# Generated at 2022-06-13 12:27:34.849996
# Unit test for function do_urlencode
def test_do_urlencode():
    arg = {'key1': u'val1',
           'key2': u'val2'}
    expected = u'key1=val1&key2=val2'
    assert do_urlencode(arg) == expected


# Generated at 2022-06-13 12:27:42.534247
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"b%C3%BCcher") == u"bücher"
    assert unicode_urldecode(u"b%C3%BCcher") == u"bücher"


# Generated at 2022-06-13 12:27:50.216529
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9lan') == u'élan'
    assert unicode_urldecode('%2Ftmp') == u'/tmp'
    assert unicode_urldecode('%2Ftmp%2F') == u'/tmp/'
    assert unicode_urldecode('%2Ftmp%2F%C3%A9lan') == u'/tmp/élan'
    assert unicode_urldecode('%2Ftmp%2F%2F') == u'/tmp//'
    assert unicode_urldecode('%2Ftmp%2F%2F%C3%A9lan') == u'/tmp//élan'


# Generated at 2022-06-13 12:27:53.396106
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    s = "%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87"
    assert unicode_urldecode(s) == "简体中文"



# Generated at 2022-06-13 12:27:59.666622
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    class MockModule():
        def __init__(self):
            self.params = {}
        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')
        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

    module = MockModule()
    fm = FilterModule()
    filters = fm.filters()
    # do_urldecode
    assert filte

# Generated at 2022-06-13 12:28:05.172181
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()

    # Test urldecode
    assert filters['urldecode']('%20') == ' '

    # Test urlencode without Jinja2 2.7 or later
    assert filters['urlencode'](' ') == '%20'

# Generated at 2022-06-13 12:28:11.770019
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if not PY3:
        assert unicode_urlencode(u'føø bår') == 'f%C3%B8%C3%B8%20b%C3%A5r'
    assert unicode_urlencode('føø bår') == 'f%C3%B8%C3%B8%20b%C3%A5r'


# Generated at 2022-06-13 12:28:17.250437
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"test%C3%A4") == u"testä"
    assert unicode_urldecode(u"test%C3%A4%C3%A4") == u"testää"
    assert unicode_urldecode(u"test%C3%A4%C3%A4%2F") == u"testää/"
    assert unicode_urldecode(u"test%C3%A4%C3%A4%2F%C3%A4%C3%A4") == u"testää/ää"
    assert unicode_urldecode(u"test%2F%2F%2F") == u"test///"

# Generated at 2022-06-13 12:28:22.054782
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test 1 - FilterModule.filters
    print("Test 1 - FilterModule.filters")
    fm = FilterModule()
    filters = fm.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters


if __name__ == '__main__':
    import sys
    import os

    LOCAL_FILTER_PLUGIN_PATH = os.path.join(os.path.dirname(__file__), '..', 'filter_plugins')

    test_FilterModule_filters()

    sys.exit(0)

# Generated at 2022-06-13 12:28:23.091210
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()

# Generated at 2022-06-13 12:28:29.396642
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    class FakeModule(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
    module = FakeModule(spec=['arguments'])

    f = FilterModule()
    assert f.filters()['urldecode'](u'foo%20bar+baz%20spam') == u'foo bar+baz spam'
    assert f.filters()['urlencode'](u'foo bar+baz spam') == u'foo%20bar%2Bbaz%20spam'

# Generated at 2022-06-13 12:28:36.821871
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # NOTE: This is a Python 3 only test
    assert unicode_urldecode('abc+def') == 'abc def'
    assert unicode_urldecode('abc%20def') == 'abc def'



# Generated at 2022-06-13 12:28:39.008599
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%B6') == u'ö'



# Generated at 2022-06-13 12:28:48.363710
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Examples from https://en.wikipedia.org/wiki/Percent-encoding
    assert unicode_urlencode('Ladies + Gentlemen') == 'Ladies%20%2B%20Gentlemen'
    assert unicode_urlencode('An encoded string!') == 'An%20encoded%20string%21'
    assert unicode_urlencode('Dogs, Cats & Mice') == 'Dogs%2C%20Cats%20%26%20Mice'
    assert unicode_urlencode('☃') == '%E2%98%83'


# Generated at 2022-06-13 12:28:53.546023
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    s = u'日本語'
    expected = u'%E6%97%A5%E6%9C%AC%E8%AA%9E'
    assert unicode_urlencode(s) == expected

# Generated at 2022-06-13 12:28:56.315609
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # create a instance of class FilterModule
    x = FilterModule()
    # make sure the returned object is a dictionary
    assert isinstance(x.filters(), dict)

# Generated at 2022-06-13 12:29:02.509857
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"/?#[]@!$&'()*+,;= abc123") == '/%3F%23%5B%5D%40%21%24%26%27%28%29%2A%2B%2C%3B%3D%20abc123'
    assert unicode_urlencode(u"/?#[]@!$&'()*+,;= abc123", for_qs=True) == '/%3F%23%5B%5D%40%21%24%26%27%28%29%2A%2B%2C%3B%3D+abc123'


# Generated at 2022-06-13 12:29:03.843163
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == 'é'


# Generated at 2022-06-13 12:29:12.866047
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # for doctest
    utf8_str = b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'
    unicode_str = utf8_str.decode('utf-8')

    assert unicode_urldecode(utf8_str) == unicode_str, 'utf-8 byte string decode error.'



# Generated at 2022-06-13 12:29:24.261748
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'\u0410\u0401\u0402' == unicode_urldecode('%D0%90%D0%81%D0%82')
    assert u'\u0410\u0401\u0402' == unicode_urldecode('%d0%90%d0%81%d0%82')
    assert u'АБВ' == unicode_urldecode('%D0%90%D0%91%D0%92')
    assert u'АБВ' == unicode_urldecode('%d0%90%d0%91%d0%92')
    assert u'A B' == unicode_urldecode('A+B')

# Generated at 2022-06-13 12:29:26.081822
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()
    assert 'urldecode' in filters



# Generated at 2022-06-13 12:29:34.742167
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'/test') == u'/test'
    assert unicode_urlencode({'test': 'ing'}) == u'test=ing'
    assert unicode_urlencode({'test': 'Øing'}) == u'test=%C3%98ing'


# Generated at 2022-06-13 12:29:38.489525
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('foo%20bar') == 'foo bar'
    else:
        assert unicode_urldecode('foo%20bar') == u'foo bar'



# Generated at 2022-06-13 12:29:43.551144
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = '%E6%82%AA%E5%BF%B5%E5%88%A9%E5%93%A1'
    assert unicode_urldecode(string) == u'悪念利員'


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 12:29:52.950797
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'Привет') == u'Привет'
    assert unicode_urldecode(u'%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82') == u'Привет'
    assert unicode_urldecode(u'%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82') == u'Привет'
    assert unicode_urldecode(u'hello%20ansible') == u'hello ansible'

# Generated at 2022-06-13 12:29:57.689361
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'fôo') == u'f%C3%B4o'
    assert unicode_urlencode(u'fôo', True) == u'f%C3%B4o'
    assert unicode_urlencode({u'user': u'fôo', u'password': u'bar'}) == u'user=f%C3%B4o&password=bar'


# Generated at 2022-06-13 12:30:03.912490
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:30:12.972735
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    print("Testing urldecode")
    assert unicode_urldecode("%E1%88%B4%E1%8A%95+%E1%88%9B%E1%8B%8D+%E1%89%A5%E1%8B%95%E1%88%B5%E1%8A%95") == u'\u1234 \u1234+\u1234 \u1234 \u1234 \u1234'

# Generated at 2022-06-13 12:30:22.653130
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/') == '/'
    assert unicode_urlencode('/a/b/c') == '/a/b/c'
    assert unicode_urlencode('a=b') == 'a%3Db'
    assert unicode_urlencode('a=b&c=d') == 'a%3Db%26c%3Dd'
    assert unicode_urlencode('/a/b/c?a=b&c=d') == '/a/b/c%3Fa%3Db%26c%3Dd'
    assert unicode_urlencode('/a/b/c?a=b&c=d', for_qs=True) == '/a/b/c?a%3Db%26c%3Dd'


# Generated at 2022-06-13 12:30:28.169762
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json
    f = FilterModule()
    filters = f.filters()
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    assert (filters['urldecode']('my%20string%20with%20spaces') ==
            'my string with spaces')
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert filters['urlencode'] == do_urlencode
        assert (filters['urlencode']('my string with spaces') ==
                'my+string+with+spaces')

# Generated at 2022-06-13 12:30:39.174102
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']('Hello%20World%21') == 'Hello World!'

    if not HAS_URLENCODE:
        assert FilterModule().filters()['urlencode']('Hello World!') == 'Hello%20World%21'
        assert FilterModule().filters()['urlencode']('Hello World!') != 'Hello World!'
        assert FilterModule().filters()['urlencode']('Hello World!') != 'Hello+World%21'
        assert FilterModule().filters()['urlencode']('Hello World!') != 'Hello+World!'
    else:
        assert FilterModule().filters()['urlencode']('Hello World!') == 'Hello+World%21'

# Generated at 2022-06-13 12:30:52.594383
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'x') == u'x'
    assert unicode_urldecode(u'+') == u' '
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(b'x') == u'x'
    assert unicode_urldecode(b'+') == u' '
    assert unicode_urldecode(b'%2B') == u'+'


# Generated at 2022-06-13 12:30:55.657911
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = '%C3%A9%26%C3%A0%C3%A7%20%C3%A7%C3%A0%C3%A9%C3%A0%C3%A7'
    assert unicode_urldecode(string) == u'é&àç àçàéàç'


# Generated at 2022-06-13 12:31:06.623236
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' Unit test for FilterModule.filters method '''
    test_data = {'test_data': '{{ urlencode(test_data) }}'}
    module = FilterModule()
    filters = module.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters
    assert filters['urldecode'](test_data['test_data']) == 'test_data'
    assert filters['urlencode'](test_data['test_data']) == '%7B%7B%20urlencode(test_data)%20%7D%7D'

# Generated at 2022-06-13 12:31:14.826277
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'dag%40wieers.com') == u'dag@wieers.com'
    assert unicode_urldecode(u'dag%7Ewieers.com') == u'dag~wieers.com'
    assert unicode_urldecode(u'%C3%A9%C3%A9%C3%A9') == u'\xe9\xe9\xe9'
    assert unicode_urldecode(u'%7B%7B%20ansible_hostname%20%7D%7D') == u'{{ ansible_hostname }}'



# Generated at 2022-06-13 12:31:24.695024
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test_string = 'äöüÄÖÜß€'
    encoded_string = '%C3%A4%C3%B6%C3%BC%C3%84%C3%96%C3%9C%C3%9F%E2%82%AC'
    assert unicode_urldecode(encoded_string) == test_string
    assert unicode_urldecode(test_string) == test_string


# Generated at 2022-06-13 12:31:31.485112
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('/') == '/'
    assert do_urlencode('foo') == 'foo'
    assert do_urlencode('foo bar') == 'foo+bar'
    assert do_urlencode('foo+bar') == 'foo%2Bbar'
    assert do_urlencode('foo%2Bbar') == 'foo%252Bbar'
    assert do_urlencode('foo&bar') == 'foo%26bar'

    assert do_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert do_urlencode([('foo', 'bar')]) == 'foo=bar'
    assert do_urlencode([('foo', 'bar', 'baz')]) == 'foo=bar&foo=baz'

# Generated at 2022-06-13 12:31:36.529315
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.common.collections import ImmutableDict
    assert FilterModule().filters() == ImmutableDict({
        'urldecode': do_urldecode,
    })
    assert FilterModule().filters() == ImmutableDict({
        'urldecode': do_urldecode,
        'urlencode': do_urlencode,
    })



# Generated at 2022-06-13 12:31:47.574445
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'unicode_urlencode') == u'unicode_urlencode'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == u'foo+bar'
    assert unicode_urlencode(u'foo+bar', for_qs=True) == u'foo%2Bbar'
    assert unicode_urlencode(u'foo+bar') == u'foo%2Bbar'
    assert unicode_urlencode(u'foo/bar') == u'foo%2Fbar'
    assert unicode_urlencode(u'foo/bar', for_qs=True) == u'foo%2Fbar'
    assert unicode_urlen

# Generated at 2022-06-13 12:31:54.660287
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%22%2B%2F%3D%3F%3A%3B") == '"+/=?:;'
    assert unicode_urldecode("%E8%BF%99%E6%98%AF%E4%B8%AD%E6%96%87") == u'\u8fd9\u662f\u4e2d\u6587'
    if PY3:
        assert isinstance(unicode_urldecode("%E8%BF%99%E6%98%AF%E4%B8%AD%E6%96%87"), str)

# Generated at 2022-06-13 12:32:04.274090
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    results = {
        b'/': b'%2F',
        b':': b'%3A',
        u'/': u'%2F',
        u':': u'%3A',
        u'a/b:c': u'a%2Fb%3Ac',
        u'a/b:c': u'a%2Fb%3Ac',
    }

    for d in results.keys():
        r = unicode_urlencode(d)
        if PY3:
            assert isinstance(r, str)
        else:
            assert isinstance(r, unicode)
        assert r == results[d]



# Generated at 2022-06-13 12:32:24.866386
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%21%23%3F') == u'!#?'
    if PY3:
        assert unicode_urldecode('%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%99%E0%B8%A7%E0%B8%A2%E0%B9%84%E0%B8%97%E0%B8%A2') == u'การเนื้อไทย'

# Generated at 2022-06-13 12:32:34.383852
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo') == u'foo'
    assert unicode_urldecode('foo+bar') == u'foo bar'
    assert unicode_urldecode('foo%2Bbar') == u'foo+bar'
    assert unicode_urldecode('foo%2bbar') == u'foo+bar'
    assert unicode_urldecode('foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'foo%2Bbar') == u'foo+bar'

# Generated at 2022-06-13 12:32:39.349943
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('bar') == 'bar'
    assert do_urlencode('foo bar') == 'foo+bar'
    assert do_urlencode([1, 2, 3]) == '1&2&3'
    assert do_urlencode(u'bar') == 'bar'
    assert do_urlencode(u'foo bar') == 'foo+bar'
    assert do_urlencode((1, 2, 3)) == '1&2&3'
    assert do_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert do_urlencode({'foo': 'bar', 'baz': 'zoo'}) == 'foo=bar&baz=zoo'


# Generated at 2022-06-13 12:32:45.639367
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Test non-ASCII
    assert unicode_urlencode(u'\u0411\u0435\u043b\u0430\u0440\u0443\u0441') == u'%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81'
    # Test reserved characters
    assert unicode_urlencode(u"/?:@-._~!$&'()*+,=;%") == u"/?:@-._~!$&'()*+,=;%"
    # Test non-reserved characters
    assert unicode_urlencode(u"aA1:") == u"aA1:"
    # Test unicode

# Generated at 2022-06-13 12:32:50.440803
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo') == 'foo'
    assert unicode_urlencode(u'foo/bar') == 'foo%2Fbar'
    assert unicode_urlencode(u'foo/bar', for_qs=True) == 'foo%2Fbar'
    assert unicode_urlencode(u'foo bar') == 'foo+bar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == 'foo+bar'
    assert unicode_urlencode(u'foo++bar') == 'foo%2B%2Bbar'
    assert unicode_urlencode(u'foo++bar', for_qs=True) == 'foo%2B%2Bbar'


# Generated at 2022-06-13 12:32:54.028482
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    obj = FilterModule()

    filters = obj.filters()
    assert filters['urldecode'] == do_urldecode

    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:33:04.082866
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    fm = FilterModule()
    fm_filters = fm.filters()

    assert fm_filters['urldecode']('foo%20bar') == 'foo bar'
    assert fm_filters['urldecode']('foo+bar') == 'foo bar'
    assert fm_filters['urldecode']('foo bar') == 'foo bar'
    assert fm_filters['urldecode'](to_text('foo%20bar')) == 'foo bar'
    assert fm_filters['urldecode'](to_bytes('foo%20bar')) == 'foo bar'


# Generated at 2022-06-13 12:33:05.917241
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%A9+') == u'é '


# Generated at 2022-06-13 12:33:09.611788
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("test") == "test"
    assert unicode_urlencode("test1 test2") == "test1+test2"
    assert unicode_urlencode("test1 test2", for_qs=True) == "test1%20test2"


# Generated at 2022-06-13 12:33:19.341085
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('/var/run/docker.sock') == '/var/run/docker.sock'
    assert do_urlencode('/a space/') == '/a%20space/'
    assert do_urlencode('k=v&k2=v2') == 'k=v&k2=v2'
    assert do_urlencode({'k': 'v', 'k2': 'v2'}) == 'k=v&k2=v2'
    assert do_urlencode([('k', 'v'), ('k2', 'v2')]) == 'k=v&k2=v2'


# Generated at 2022-06-13 12:23:34.719713
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import six
    assert unicode_urlencode(u'abc') == u'abc'
    assert unicode_urlencode(six.b('abc')) == u'abc'
    assert unicode_urlencode(u'http://example.net/foo/bar?a=1&b=2') == u'http%3A//example.net/foo/bar%3Fa%3D1%26b%3D2'
    assert unicode_urlencode(six.b('http://example.net/foo/bar?a=1&b=2')) == u'http%3A//example.net/foo/bar%3Fa%3D1%26b%3D2'

# Generated at 2022-06-13 12:23:37.961817
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'foo%20bar%3F') == u'foo bar?'
    assert unicode_urldecode(u'foo%20bar%3F') == u'foo bar?'


# Generated at 2022-06-13 12:23:41.474737
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'flowers%20are%20beautiful') == 'flowers are beautiful'
    assert unicode_urldecode(u'flowers%2Fare%2Fbeautiful') == 'flowers/are/beautiful'



# Generated at 2022-06-13 12:23:46.333407
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters
    assert filters['urldecode'] is do_urldecode
    assert filters['urlencode'] is do_urlencode or HAS_URLENCODE



# Generated at 2022-06-13 12:23:52.970241
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'Test%20String') == u'Test String'
    assert unicode_urldecode(u'Test String') == u'Test String'
    if PY3:
        assert unicode_urldecode(b'Test%20String') == u'Test String'
    else:
        assert unicode_urldecode(b'Test%20String') == u'Test%20String'


# Generated at 2022-06-13 12:23:56.633381
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils import basic
    assert unicode_urldecode(u'http://localhost:8080/path/to/file%2Fwith/%252525/%25252525') == u'http://localhost:8080/path/to/file%2Fwith/%25/%2525'
    assert unicode_urldecode(u'http://localhost:8080/path/to/file%2Fwith/%252525/%25252525'.encode('utf-8')) == u'http://localhost:8080/path/to/file%2Fwith/%25/%2525'



# Generated at 2022-06-13 12:24:06.418862
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json

    fm = FilterModule()
    assert fm.filters()['urldecode']('key%20with%20spaces') == 'key with spaces'
    assert fm.filters()['urldecode']('multiple%20keys%20with%20spaces') == 'multiple keys with spaces'
    assert fm.filters()['urldecode']('%20') == ' '
    assert fm.filters()['urldecode']('%20+%20') == '  '
    assert fm.filters()['urldecode']('%26%23x478%3B%26%23x439%3B%26%23x43A%3B') == json.dumps('имя'.encode('utf-8'), ensure_ascii=False)

# Generated at 2022-06-13 12:24:09.683179
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('%40%40') == '@@'
    if not HAS_URLENCODE:
        assert do_urlencode('@@') == '%40%40'


# Generated at 2022-06-13 12:24:14.113635
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('c%2Fo') == u'c/o'
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%E2%82%AC%20') == u'\u20ac '



# Generated at 2022-06-13 12:24:24.679269
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('') == ''
    assert unicode_urlencode('a') == 'a'
    assert unicode_urlencode('b') == 'b'
    assert unicode_urlencode('c') == 'c'
    assert unicode_urlencode(u'a') == 'a'
    assert unicode_urlencode(u'b') == 'b'
    assert unicode_urlencode(u'c') == 'c'
    assert unicode_urlencode(u'ab') == 'ab'
    assert unicode_urlencode(u'abc') == 'abc'

# Generated at 2022-06-13 12:24:28.195465
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'hello world' == unicode_urldecode('hello%20world')



# Generated at 2022-06-13 12:24:33.784329
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3A%2F%2Ffoo%2Eexample%2Ecom%2F') == u'http://foo.example.com/'
    assert unicode_urldecode(u'test') == u'test'
    assert unicode_urldecode(10) == u'10'



# Generated at 2022-06-13 12:24:40.698877
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode']('abc+def') == 'abc def'
    assert filters['urldecode']('abc%20def') == 'abc def'
    assert filters['urldecode']('abc+%20def') == 'abc  def'
    if not HAS_URLENCODE:
        assert filters['urlencode']('abc def') == 'abc+def'
        assert filters['urlencode']('abc  def') == 'abc++def'
    params = {'name': 'Harry', 'age': 30}
    assert filters['urlencode'](params) == 'name=Harry&age=30'

# Generated at 2022-06-13 12:24:45.135306
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'é'
    assert unicode_urldecode('%7E') == u'~'


# Generated at 2022-06-13 12:24:51.692396
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foobar') == u'foobar'
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo%2fbar') == u'foo/bar'



# Generated at 2022-06-13 12:25:00.986888
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    urls = {
        'http%3A%2F%2Fwww.example.com%2Fdag%2F%2F%2F%2F%2F%2F%2F%2F': 'http://www.example.com/dag//////',
        'http%3A%2F%2Fwww.example.com%2F%3Fdag%3D12%26hans%3D45%26jens%3D34%26jan%3D67': 'http://www.example.com/?dag=12&hans=45&jens=34&jan=67',
        '%E2%82%AC300.00': u'€300.00',
        '%E2%82%AC0.0': u'€0.0',
    }


# Generated at 2022-06-13 12:25:10.019169
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('test.txt') == 'test.txt'
    assert do_urldecode('test%2Etxt') == 'test.txt'
    assert do_urldecode('test%2etxt') == 'test.txt'
    assert do_urlencode('test.txt') == 'test.txt'
    assert do_urlencode('test/txt') == 'test%2Ftxt'
    assert do_urlencode('test+txt') == 'test%2Btxt'
    assert do_urlencode('test txt') == 'test+txt'
    assert do_urlencode({'foo': 'bar'}) == 'foo=bar'


# Generated at 2022-06-13 12:25:11.362734
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('+') == ' '



# Generated at 2022-06-13 12:25:14.669042
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    actual = FilterModule().filters()

    assert 'urldecode' in actual
    assert actual.get('urldecode') == do_urldecode
    assert 'urlencode' not in actual or actual.get('urlencode') == do_urlencode



# Generated at 2022-06-13 12:25:24.583281
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('abc') == 'abc'
        assert unicode_urldecode('abc+') == 'abc+'
        assert unicode_urldecode('%2C+%2C') == '%2C+%2C'
        assert unicode_urldecode('a%2C+%2C') == 'a%2C+%2C'
        assert unicode_urldecode('a%2C+b') == 'a, b'
        assert unicode_urldecode('a%2C+b%2C') == 'a, b%2C'
        assert unicode_urldecode('a%2C+b+%2C') == 'a, b+%2C'

# Generated at 2022-06-13 12:25:27.773986
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A1=') == u'á='


# Generated at 2022-06-13 12:25:34.785004
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test method not implemented
    fm = FilterModule()
    assert not hasattr(fm, 'test_FilterModule_filters')

    # Test urldecode
    fm = FilterModule()
    tests = (
        ('', ''),
        ('Hello', 'Hello'),
        ('Hello+World', 'Hello World'),
        ('Hello%21%20World', 'Hello! World'),
        ('Hello%2C+World', 'Hello, World'),
        ('2%2B2+%3D+4', '2+2 = 4'),
        ('foo%20+%20bar%20+%20baz', 'foo  bar  baz'),
        ('H%C3%A9llo', 'H\xe9llo'),
    )

# Generated at 2022-06-13 12:25:36.606938
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    # just testing the absence of an exception
    f.filters()

# Generated at 2022-06-13 12:25:37.860783
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert(unicode_urldecode('%C3%B1') == u'\xf1')


# Generated at 2022-06-13 12:25:39.870931
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filterModule = FilterModule()
    filterModule.filters()

# Generated at 2022-06-13 12:25:49.899976
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    from ansible.module_utils import basic

    import sys
    import copy
    import unittest
    import json

    #for python2.6 we can use the unittest2 library, otherwise
    #we use the backport in the tests/unittest2 directory
    if sys.version_info < (2, 7):
        import tests.unittest2 as unittest
    else:
        import unittest

    class TestFilterModuleClass(unittest.TestCase):

        def test_FilterModule_method_decoding(self):

            # Make sure we get a unicode back
            actual = FilterModule().filters()['urldecode']('hello%20world')
            expected = u'hello world'
            self.assertTrue(isinstance(actual, unicode))

# Generated at 2022-06-13 12:25:58.340442
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if not PY3:
        import sys
        # Python 2.X
        assert unicode_urlencode(u'ab/cd') == 'ab%2Fcd'
        assert unicode_urlencode(u'ab/cd', for_qs=True) == 'ab%2Fcd'
        assert unicode_urlencode('ab/cd') == 'ab%2Fcd'
        assert unicode_urlencode(b'ab/cd') == 'ab%2Fcd'
        assert unicode_urlencode(u'ab/cd'.encode('utf-8')) == 'ab%2Fcd'
        assert unicode_urlencode(2) == '2'
        assert unicode_urlencode(sys.maxsize) == str(sys.maxsize)

# Generated at 2022-06-13 12:25:59.696261
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    x = u'hi+there'
    y = u'hi there'
    assert unicode_urldecode(x) == y
    assert unicode_urldecode(y) == y


# Generated at 2022-06-13 12:26:06.535185
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%3Chtml%3E') == u'<html>'
    assert unicode_urldecode(u'%3Chtml%3E') == u'<html>'
    assert unicode_urldecode(u'<html>') == u'<html>'



# Generated at 2022-06-13 12:26:16.197334
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%20b%20c') == 'a b c'
    assert unicode_urldecode('a+b+c') == 'a+b+c'
    assert unicode_urldecode('%7B%7B%20ansible_date_time.epoch%20%7D%7D') == '{{ ansible_date_time.epoch }}'
    assert unicode_urldecode('%7B%7B%20ansible_date_time.iso8601_micro%20%7D%7D') == '{{ ansible_date_time.iso8601_micro }}'

# Generated at 2022-06-13 12:26:27.347606
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common.dictpath import DictPath

    # Create an object of our FilterModule class
    filtermodule = FilterModule()

    # Get the filters from that object
    filters = filtermodule.filters()

    # Make sure we get a DictPath object back
    assert isinstance(filters, DictPath)

    # Make sure we get the right number of filters back
    assert len(filters) == 2

    # Make sure we have a urldecode and urlencode filter
    assert 'urldecode' in filters
    assert 'urlencode' in filters

    # Make sure urldecode is a function
    assert callable(filters.urldecode)

    # Make sure

# Generated at 2022-06-13 12:26:36.626038
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import text_type

    assert unicode_urlencode(u'abc') == u'abc'
    assert unicode_urlencode(u'abc def') == u'abc%20def'
    assert unicode_urlencode(u'abc+def') == u'abc%2Bdef'
    assert unicode_urlencode(u'abc/def') == u'abc%2Fdef'

    # Test byte strings
    assert unicode_urlencode(b'abc') == u'abc'
    assert unicode_urlencode(b'abc def') == u'abc%20def'
    assert unicode_urlencode(b'abc+def') == u'abc%2Bdef'
    assert unicode

# Generated at 2022-06-13 12:26:39.056863
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest
    filt = FilterModule().filters()
    assert 'urldecode' in filt
    assert filt['urldecode'] == do_urldecode



# Generated at 2022-06-13 12:26:45.768330
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == 'test'
    assert unicode_urlencode('test with spaces') == 'test%20with%20spaces'
    assert unicode_urlencode('test+with+spaces') == 'test+with+spaces'
    assert unicode_urlencode('/test/with/spaces/') == '/test/with/spaces/'
    assert unicode_urlencode('/test/with/spaces/?a[]=1&a[]=2') == '/test/with/spaces/?a%5B%5D=1&a%5B%5D=2'

# Generated at 2022-06-13 12:26:52.284591
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('dag') == u'dag', 'Not decoded URL'
    assert unicode_urldecode('dag+wieers') == u'dag wieers', 'Not decoded URL'
    assert unicode_urldecode('dag%20wieers') == u'dag wieers', 'Not decoded URL'
    assert unicode_urldecode('dag+') == u'dag+', 'Not decoded URL'
    assert unicode_urldecode('dag+ ') == u'dag+', 'Not decoded URL'


# Generated at 2022-06-13 12:27:00.001765
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # first test the function
    import random

    assert unicode_urldecode("hello%20world") == "hello world"
    assert unicode_urldecode("hello%2Bworld") == "hello%2Bworld"
    assert unicode_urlencode("hello world") == "hello+world"
    assert unicode_urlencode("hello+world") == "hello%2Bworld"
    assert unicode_urlencode("hello world", for_qs=True) == "hello+world"
    assert unicode_urlencode("hello+world", for_qs=True) == "hello%2Bworld"
    assert unicode_urlencode({"xx": "hello world"}) == "xx=hello+world"

# Generated at 2022-06-13 12:27:04.433093
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    data = {
        u"foo": u"bar",
        u"baz": u"føø",
        u"blah": u"漢語",
    }

    result = unicode_urlencode(data)

    if result != u'baz=f%C3%B8%C3%B8&blah=%E6%BC%A2%E8%AA%9E&foo=bar':
        print("Invalid result found: %s" % (result))
        exit(1)


# Generated at 2022-06-13 12:27:08.864060
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7E%21%40%23%24%25%5E%26%2A%28%29_%2B%20%3D%2F') == u'~!@#$%^&*()_+ =/'


# Generated at 2022-06-13 12:27:15.706185
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode']('%7B%22a%22%3A1%2C%22b%22%3A2%7D') == '{"a":1,"b":2}'
    assert fm.filters()['urldecode']('foo+bar') == 'foo bar'
    assert fm.filters()['urldecode']('foo%20bar') == 'foo bar'

# Generated at 2022-06-13 12:27:20.403980
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('http%3a%2f%2fexample.com%2f%7euser%2f%3ftag=%20%23%20%25%26') == u'http://example.com/~user/?tag= # %&'


# Generated at 2022-06-13 12:27:26.829400
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''
    This method should return a dict with the following structure:
    {
        '<name of the filter>': <filter method,
    }
    '''
    fm = FilterModule()
    assert isinstance(fm.filters(), dict)


# Generated at 2022-06-13 12:27:30.394342
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = '%E8%A5%BF%E7%93%A6' # means "Xuzhou" in Chinese
    assert unicode_urldecode(string) == u'西瓦'


# Generated at 2022-06-13 12:27:38.278919
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    """
    Function unicode_urlencode() should return a unicode representation of the value
    using url encoding.

    :return: no return value
    :rtype: None
    """
    assert unicode_urlencode('abc') == 'abc'
    assert unicode_urlencode(u'abc') == 'abc'
    assert unicode_urlencode(b'abc') == 'abc'
    assert unicode_urlencode(u'123') == '123'
    assert unicode_urlencode(b'123') == '123'
    assert unicode_urlencode(u'|') == '%7C'
    assert unicode_urlencode(b'|') == '%7C'
    assert unicode_urlencode(u'abc|123') == 'abc%7C123'
   

# Generated at 2022-06-13 12:27:43.151549
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u' ' == unicode_urldecode('+')
    assert u' ' == unicode_urldecode('%20')
    assert u'\u00f6' == unicode_urldecode('%C3%B6')
    assert u'\N{LATIN SMALL LETTER O WITH DIAERESIS}' == unicode_urldecode('%C3%B6')


# Generated at 2022-06-13 12:27:51.884487
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' Ensure urldecode returns an unicode string '''
    assert unicode_urldecode('%3A%2F%2F') == u'://'
    assert unicode_urldecode('%3A%2F%2F') == u'://'
    assert unicode_urldecode('%23%2F%2F') == u'#//'
    assert unicode_urldecode('%2523%252F%252F') == u'%23%2F%2F'
    assert unicode_urldecode('%3A%2F%2F') == u'://'
    assert unicode_urldecode('%3A%2F%2F') == u'://'
    assert unicode_urldecode('%3A%2F%2F')

# Generated at 2022-06-13 12:27:56.885933
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filters = FilterModule().filters()
    assert isinstance(filters, dict)
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert filters['urlencode'] == do_urlencode


# ======
# Tests
# ======


# Generated at 2022-06-13 12:28:04.220503
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('') == ''
    assert unicode_urldecode('+') == '+'
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('abc%41def') == 'abcAdef'
    assert unicode_urldecode('abc%Zdef') == 'abc%Zdef'



# Generated at 2022-06-13 12:28:12.563127
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%25') == u'%'
    assert unicode_urldecode('%2B') == u'+'
    assert unicode_urldecode('%7E') == u'~'
    assert unicode_urldecode('%E3%82%A2') == u'\u30a2'
    assert unicode_urldecode('%e3%82%a2') == u'\u30a2'


# Generated at 2022-06-13 12:28:18.700404
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('hello+world') == 'hello world'
    assert do_urldecode('hello') == 'hello'
    assert do_urldecode(u'hello+world') == 'hello world'
    assert do_urldecode(u'hello') == 'hello'
    assert do_urldecode(b'hello+world') == 'hello world'
    assert do_urldecode(b'hello') == 'hello'

# Generated at 2022-06-13 12:28:23.916228
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('foo') == 'foo'
    assert unicode_urlencode('foo bar') == 'foo%20bar'
    assert unicode_urlencode('foo+bar') == 'foo+bar'
    assert unicode_urlencode('fra nçais') == 'fra%20n%C3%A7ais'
    assert unicode_urlencode('/path/to/file') == '/path/to/file'
    assert unicode_urlencode('/path/to/file', for_qs=True) == '%2Fpath%2Fto%2Ffile'

# Generated at 2022-06-13 12:28:31.231846
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    for test in [
        (u'a+b', u'a b'),
        (u'a%20b', u'a b'),
        (u'a%21b', u'a!b'),
        (u'a%2Bb', u'a+b'),
        (u'a%25b', u'a%b'),
        (u'a%E2%82%ACb', u'a\u20acb'),
    ]:
        assert unicode_urldecode(test[0]) == test[1]



# Generated at 2022-06-13 12:28:37.357648
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode']('abc%20def%3Dhi%26there%3Dyou') == 'abc def=hi&there=you'

    if not HAS_URLENCODE:
        assert fm.filters()['urlencode']('abc def=hi&there=you') == 'abc+def%3Dhi%26there%3Dyou'
        assert fm.filters()['urlencode']({'abc' : 123, 'def':'hi & there'}) == 'abc=123&def=hi+%26+there'

# Generated at 2022-06-13 12:28:41.505626
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%5C') == u'\\'
    assert unicode_urldecode(b'%5C') == u'\\'

# Unit tests for function do_urldecode

# Generated at 2022-06-13 12:28:48.977055
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://www.öäü.de/föö-bär?foo=fää&bar=böö') == u'http%3A%2F%2Fwww.%C3%B6%C3%A4%C3%BC.de%2Ff%C3%B6%C3%B6-b%C3%A4r%3Ffoo%3Df%C3%A4%C3%A4%26bar%3Db%C3%B6%C3%B6'

# Generated at 2022-06-13 12:29:00.268500
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils.six.moves.urllib.parse import quote, quote_plus, unquote, unquote_plus
    assert unicode_urlencode(u'unicode string') == to_text(quote(b'unicode string'))
    # unicode_urlencode returns a unicode string, so we test its repr
    assert repr(unicode_urlencode(u'unicode string')) == repr(quote('unicode string'))
    if not PY3:
        assert unicode_urlencode('byte string') == quote('byte string')
    assert unicode_urlencode({'unicode': u'value', 'byte': b'value'}) == to_text(quote(b'unicode=value&byte=value'))

# Generated at 2022-06-13 12:29:10.418919
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("foo") == u"foo"
    assert unicode_urldecode("foo%20bar") == u"foo bar"
    assert unicode_urldecode("hello%09world") == u"hello\tworld"
    assert unicode_urldecode("hello%0Aworld") == u"hello\nworld"
    assert unicode_urldecode("hello%0Dworld") == u"hello\rworld"
    assert unicode_urldecode("hello%21world") == u"hello!world"
    assert unicode_urldecode("hello%40world") == u"hello@world"
    assert unicode_urldecode("hello%23world") == u"hello#world"

# Generated at 2022-06-13 12:29:22.427117
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('foo') == 'foo'
    assert unicode_urlencode('foo bar') == 'foo%20bar'
    assert unicode_urlencode('foo bar', for_qs=True) == 'foo+bar'
    assert unicode_urlencode('foo bar/baz') == 'foo%20bar/baz'
    assert unicode_urlencode('foo bar/baz', for_qs=True) == 'foo+bar%2Fbaz'
    assert unicode_urlencode('/foo bar') == '/foo%20bar'
    assert unicode_urlencode('/foo bar', for_qs=True) == '%2Ffoo+bar'
    assert unicode_urlencode('/foo@bar:baz') == '/foo%40bar:baz'
   

# Generated at 2022-06-13 12:29:24.907910
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E5%96%9C%E5%89%87') == u'喜則'


# Generated at 2022-06-13 12:29:35.365446
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    # Check if method filters of class FilterModule exists
    fm = FilterModule()
    assert hasattr(fm, 'filters'), "Class FilterModule has no method 'filters'"
    assert callable(fm.filters), "Method 'filters' of class FilterModule is not callable"

    # Check if there exists the key 'urldecode' in the return value of the call to method filters
    assert 'urldecode' in fm.filters(), "Return value of call to method 'filters' has no key 'urldecode'"

    # Check if we obtain a dictionary by calling method filters of class FilterModule
    assert isinstance(fm.filters(), dict), "Return value of call to method 'filters' is not a dictionary"

    # Check if method urldecode exists and is callable

# Generated at 2022-06-13 12:29:43.191855
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'a b c' == unicode_urldecode('a+b+c')
    assert u'a b c' == unicode_urldecode('a%20b%20c')
    assert u'a b c' == unicode_urldecode('a%2Bb%2Bc')
    assert u'a+b+c' == unicode_urldecode('a%2b%62%2Bc')
    assert u'a b c' == unicode_urldecode('a%252Bb+c')


# Generated at 2022-06-13 12:29:52.573116
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"abc%20abc") == u"abc abc"
    assert unicode_urldecode(u"abc+abc") == u"abc abc"
    assert unicode_urldecode(u"%E2%98%83") == u"☃"
    assert unicode_urldecode(u"%E2%98%83%20%E2%98%83") == u"☃ ☃"
    assert unicode_urldecode(u"%E2%98%83%2B%E2%98%83") == u"☃+☃"


# Generated at 2022-06-13 12:30:00.331800
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import ansible.module_utils.six as six

    try:
        # If either Python 2 or Python 3, we could deal with utf-8 string,
        # on Python 2 it will be utf-8 encoded str
        utf_string = six.u('\u4eca\u65e5\u306f\u4e16\u754c')
        utf_string_escaped = native_urlencode(utf_string)
        # Decoding str on Python 2
        utf_string_escaped_decoded = utf_string_escaped.decode('utf-8')
    except AttributeError:
        # Python 3 only
        utf_string = six.u('\u4eca\u65e5\u306f\u4e16\u754c')
        utf_string_escaped

# Generated at 2022-06-13 12:30:03.348708
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # TODO: Figure out how to test this method
    # ansible.module_utils.core.filter_plugins.FilterModule.filters
    pass

# Generated at 2022-06-13 12:30:05.225470
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7B') == '{'


# Generated at 2022-06-13 12:30:13.915243
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import unittest
    from ansible.module_utils.six import PY3

    class FilterModuleTest(unittest.TestCase):
        """ Unit test for ansible.module_utils.jinja2_annotations.FilterModule """

        def test_FilterModule(self):
            # We are not interested in testing functionality that is already
            # tested because it comes from Jinja2
            if PY3 or HAS_URLENCODE:
                return

            # do_urlencode
            self.assertEqual(do_urlencode(b'abcdef'), 'abcdef')
            self.assertEqual(do_urlencode('abcdef'), 'abcdef')
            self.assertEqual(do_urlencode({'foo': 'bar'}), 'foo=bar')

# Generated at 2022-06-13 12:30:16.226202
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%41+%42%2B%43') == 'A B+C'


# Generated at 2022-06-13 12:30:19.530805
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
  val = { 'ansible': '1' }
  ansible_1_filters_res = 'ansible=1'
  assert FilterModule.filters(val) == ansible_1_filters_res

# Generated at 2022-06-13 12:30:26.551896
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"%EC%99%94%EB%A7%9C%EB%A7%A8%20%EC%82%AC%EA%B4%80%20%EC%B2%98%EB%9D%BC%20%EC%8B%A0%EC%B2%B4%20%EC%B0%A8%EA%B2%BD%20%EC%A3%BC%EC%8B%AC") == u"왔만맨 사관 처라 신체 차경 주심"



# Generated at 2022-06-13 12:30:36.572501
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('blah%20blah') == u'blah blah'
    assert unicode_urldecode('blah+blah') == u'blah blah'
    assert unicode_urldecode('blah%2Bblah') == u'blah+blah'
    assert unicode_urldecode('blah%21%23%24%25%26%27%28%29%2A%2B%2C%2F%3A%3B%3D%3F%40%5B%5D') == u"blah!#$%&'()*+,-/:;=?@[]"


# Generated at 2022-06-13 12:30:42.174585
# Unit test for function do_urlencode
def test_do_urlencode():
    test_cases = [
        (u'abc', u'abc'),
        (u'abc def', u'abc+def'),
        (u'abc def/ghi', u'abc+def%2Fghi'),
        (u'dict test', {u'abc': u'def', u'ghi': u'jkl'}, u'abc=def&ghi=jkl'),
    ]
    for case, expected in test_cases:
        result = do_urlencode(case)
        assert result == expected

# Generated at 2022-06-13 12:30:50.595206
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    ansible_python_interpreter = '/usr/bin/python'
    ansible_module_name = 'ping'
    ansible_module_args = 'ping'
    ansible_module_executable = '/home/wanted/ansible/hacking/testdata/module_utils/basic.py'
    ansible_module_path = '/home/wanted/ansible/hacking/testdata/module_utils'
    ansible_module_args_json = '[1, 2, 3]'
    module_name = 'ping'
    module_args = 'ping'
    module_executable = '/home/wanted/ansible/hacking/testdata/module_utils/basic.py'
    module_path = '/home/wanted/ansible/hacking/testdata/module_utils'
    module_args_

# Generated at 2022-06-13 12:30:57.271582
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import os
    import sys
    import unittest

    from ansible.errors import AnsibleError

    from ansible.module_utils.six import u

    from ansible.module_utils.six.moves.urllib.parse import unquote_plus

    from ansible.utils.unicode import to_bytes

    from ansible.module_utils.common.collections import is_sequence

    filter_module = FilterModule()
    filters = filter_module.filters()

    class TestFilterModuleFilters(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass


# Generated at 2022-06-13 12:31:02.723299
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    assert filter_module.filters() == {'urldecode': do_urldecode, 'urlencode': do_urlencode}

# Generated at 2022-06-13 12:31:11.174025
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Quitiveys
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(u'%2B') == u'+'

    # Invalid hex
    assert unicode_urldecode(u'%') == u'%'
    assert unicode_urldecode(u'%0') == u'%0'
    assert unicode_urldecode(u'%0A') == u'%0A'
    assert unicode_urldecode(u'%0Q') == u'%0Q'
    assert unicode_urldecode(u'%G0') == u'%G0'

# Generated at 2022-06-13 12:31:15.796277
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%266%3F%3D%26') == '&6?=&'
    assert unicode_urldecode('%C3%A6%20bar') == u'æ bar'
    assert unicode_urldecode('%66%6f%6f%62%61%72') == 'foobar'



# Generated at 2022-06-13 12:31:18.649614
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'\u00e9'

# Generated at 2022-06-13 12:31:30.722834
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'/') == u'/'
    assert unicode_urldecode(u'/usr/bin') == u'/usr/bin'
    assert unicode_urldecode(u'/usr/bin/') == u'/usr/bin/'
    assert unicode_urldecode(u'/usr/bin/?') == u'/usr/bin/?'
    assert unicode_urldecode(u'/usr/bin/?foo=bar') == u'/usr/bin/?foo=bar'
    # Handle utf-8 using the surrogateescape error handler (the default error
    # handler in Python 3)

# Generated at 2022-06-13 12:31:36.328989
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six import assertRegexpMatches, assertRaisesRegexp
    from ansible.module_utils.six.moves.urllib.parse import quote, quote_plus, unquote_plus

    # Test urldecode
    assert urldecode(quote_plus('test+test')) == u'test test'
    assert urldecode(quote_plus('test+test%20test')) == u'test test test'
    assert urldecode(quote_plus('test%2Btest')) == u'test+test'

    # Test urlencode
    assert urlencode(u'test test') == quote_plus('test test')
    assert urlencode(u'test test test') == quote_plus('test test test')

# Generated at 2022-06-13 12:31:39.814763
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert 'a+b' == unicode_urldecode('a%2Bb')
    assert 'a b' == unicode_urldecode('a+b')



# Generated at 2022-06-13 12:31:44.893513
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('abc%20def') == u'abc def'
    assert unicode_urldecode('abc%26def') == u'abc&def'
    assert unicode_urldecode('abc%2Bdef') == u'abc+def'



# Generated at 2022-06-13 12:31:52.479388
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'') == u''
    assert unicode_urldecode(u'abc') == u'abc'
    assert unicode_urldecode(u'%21') == u'!'
    assert unicode_urldecode(u'%40') == u'@'
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%2F') == u'/'
    assert unicode_urldecode(u'a%2Fb') == u'a/b'



# Generated at 2022-06-13 12:31:56.060871
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' Unit test for method filters of class FilterModule '''

    # Test imports and constants
    assert HAS_URLENCODE
    assert FilterModule.filters.__name__ == 'filters'



# Generated at 2022-06-13 12:32:03.696629
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        test_obj = {
            '': '',
            'unicode_string': 'unicode_string',
            '%20unicode%20string': ' unicode string',
            'unicode_string%20': 'unicode_string ',
            'unicode_string%2520': 'unicode_string%20',
        }
        for input, output in iteritems(test_obj):
            assert unicode_urldecode(input) == output



# Generated at 2022-06-13 12:32:06.959495
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo') == u'foo'
    assert unicode_urldecode('foo+') == u'foo '
    assert unicode_urldecode('foo%20') == u'foo '
    assert unicode_urldecode('%') == u''
    assert unicode_urldecode('%2') == u''
    assert unicode_urldecode('%2z') == u'%2z'



# Generated at 2022-06-13 12:32:12.334266
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'](u'https://github.com/ansible/ansible/issues/15626') == u'https://github.com/ansible/ansible/issues/15626'
    assert filters['urlencode'](u'https://github.com/ansible/ansible/issues/15626') == u'https%3A//github.com/ansible/ansible/issues/15626'

# Generated at 2022-06-13 12:32:16.051562
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'sample%20test') == u'sample test'
    assert unicode_urldecode(u'%20%3C%3E%23%25%26%27%40%2F%3B%22%28%29%2C%2F%3F') == u' <>#%&\'@/;"(),/?'


# Generated at 2022-06-13 12:32:27.726955
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:32:28.581394
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()

# Generated at 2022-06-13 12:32:37.691632
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('') == u''
    assert unicode_urldecode('a') == u'a'
    assert unicode_urldecode('%') == u'%'
    assert unicode_urldecode('%a') == u'%a'
    assert unicode_urldecode('%1') == u'%1'
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('+') == u' '
    assert unicode_urldecode('a+') == u'a '
    assert unicode_urldecode('a%20') == u'a '



# Generated at 2022-06-13 12:32:40.637268
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('http%3A%2F%2Fwww.redhat.com%3A8080%2F') == 'http://www.redhat.com:8080/'


# Generated at 2022-06-13 12:32:45.540290
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%20string') == u'a string'


# Generated at 2022-06-13 12:32:48.513787
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%E4%B8%8D%E5%90%83%E6%88%91%E5%8F%AF%E4%BB%A5") == "不吃我可以"


# Generated at 2022-06-13 12:32:57.554693
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils.six import BytesIO

    def serialize_compare(value, expected, method):
        output = AnsibleLoader(BytesIO(to_bytes(value, errors='surrogate_or_strict')), None).get_single_data()
        filtered = FilterModule().filters()[method](output)
        if type(expected) == str:
            expected = u"{0}".format(expected)
        if type(filtered) == str:
            filtered = u"{0}".format(filtered)
        assert expected == filtered


# Generated at 2022-06-13 12:33:06.337028
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'привет') == u'%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82'
    assert unicode_urlencode(u'~') == u'~'
    assert unicode_urlencode(u"/~?&='") == u'%2F~%3F&%3D\''
    assert unicode_urlencode(u"/~?&='", for_qs=True) == u'%2F%7E%3F%26%3D%27'

# Generated at 2022-06-13 12:33:08.734978
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters


# Generated at 2022-06-13 12:33:18.421834
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/', for_qs=False) == '/'
    assert unicode_urlencode('/', for_qs=True) == '%2F'
    assert unicode_urlencode('foo:bar', for_qs=False) == 'foo:bar'
    assert unicode_urlencode('foo:bar', for_qs=True) == 'foo:bar'

    assert unicode_urlencode('/foo/bar', for_qs=False) == '/foo/bar'
    assert unicode_urlencode('/foo/bar', for_qs=True) == '%2Ffoo%2Fbar'
    assert unicode_urlencode('foo/bar', for_qs=False) == 'foo/bar'

# Generated at 2022-06-13 12:33:26.226342
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils.six import u
    assert u("hello+world%21") == unicode_urldecode("hello%20world%21")
    assert u("Ω≈ç√∫˜µ≤≥÷") == unicode_urldecode("%CE%A9%E2%89%88%C3%A7%E2%88%9A%E2%88%AB%CB%98%C2%B5%E2%89%A4%E2%89%A5%C3%B7")
    assert u("null") == unicode_urldecode("null")
    assert u("") == unicode_urldecode("")

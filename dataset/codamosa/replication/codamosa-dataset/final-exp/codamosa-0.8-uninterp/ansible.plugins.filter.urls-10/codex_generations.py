

# Generated at 2022-06-13 12:23:29.652374
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Static imports
    import ansible.module_utils.six as six
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus
    # Setup
    test_object = FilterModule()
    # Exercise
    assertion = lambda x: six.assertEqual(test_object.filters()[x], getattr(unquote_plus, x))
    assertion("__call__")

# Generated at 2022-06-13 12:23:35.693713
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:23:43.709132
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foobar') == u'foobar'
    assert unicode_urlencode(u'foobar/') == u'foobar%2F'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == u'foo+bar'
    assert unicode_urlencode(u'foo=bar') == u'foo%3Dbar'
    assert unicode_urlencode(u'foo=bar', for_qs=True) == u'foo%3Dbar'
    assert unicode_urlencode(u'a+b') == u'a%2Bb'


# Generated at 2022-06-13 12:23:53.340878
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six.moves.urllib.parse import parse_qsl, urlparse
    import json

    for (inp, outp) in [
        ('test', 'test'),
        ('test one', 'test+one'),
        ('test+one', 'test%2Bone'),
        ('test one+two', 'test+one%2Btwo'),
        ('?test', '%3Ftest'),
        ('&test', '%26test'),
        ('?', '%3F'),
        ('&', '%26'),
    ]:
        assert do_urldecode(inp) == outp
        assert do_urlencode(inp) == outp
        assert do_urlencode({'one': inp}) == 'one=' + outp

# Generated at 2022-06-13 12:24:03.662592
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('utf8_föö_bar') == 'utf8_f%C3%B6%C3%B6_bar'
    assert unicode_urlencode('utf8_föö_bar', True) == 'utf8_f%C3%B6%C3%B6_bar'
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode('/', True) == '%2F'
    assert unicode_urlencode({'a': 'b'}) == 'a=b'
    assert unicode_urlencode({'a': 'b c'}) == 'a=b+c'

# Generated at 2022-06-13 12:24:10.894873
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://\u043f\u0440\u0438\u043c\u0435\u0440/test?a=%20+#') == 'http%3A//%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80/test%3Fa%3D%20%2B%23'

# Generated at 2022-06-13 12:24:16.650682
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six import iteritems

    expected_filters = {
        "urldecode": do_urldecode,
    }
    if not HAS_URLENCODE:
        expected_filters["urlencode"] = do_urlencode

    fm = FilterModule()
    assert iteritems(expected_filters) == iteritems(fm.filters())


# Generated at 2022-06-13 12:24:26.438309
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'abc') == u'abc'
    assert unicode_urlencode(u'abc def') == u'abc+def'
    assert unicode_urlencode(u'abc def~') == u'abc+def%7E'

    assert unicode_urlencode(u'abc', for_qs=True) == u'abc'
    assert unicode_urlencode(u'abc def', for_qs=True) == u'abc+def'
    assert unicode_urlencode(u'abc def~', for_qs=True) == u'abc+def%7E'

    assert unicode_urlencode(u'abc/def') == u'abc%2Fdef'

# Generated at 2022-06-13 12:24:32.482562
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('http%3A%2F%2Fansible.com%2F') == u'http://ansible.com/'
    assert unicode_urldecode('http%3A%2F%2Fansible.com%2Ffoo%3Fname%3Djoe%26state%3Dpresent') == u'http://ansible.com/foo?name=joe&state=present'

# Generated at 2022-06-13 12:24:35.092021
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%21') == u'!'
    assert unicode_urldecode(b'%21') == u'!'



# Generated at 2022-06-13 12:24:41.459014
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:24:49.174371
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('foo%20bar') == 'foo bar'
        assert unicode_urldecode(u'foo%20bar') == 'foo bar'
    else:
        assert unicode_urldecode('foo%20bar') == u'foo bar'
        assert unicode_urldecode(u'foo%20bar') == u'foo bar'


# Generated at 2022-06-13 12:24:55.423804
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Hello+World%21') == 'Hello World!'
    assert unicode_urldecode('%C3%A9') == u'é'
    assert unicode_urldecode('%26') == '&'
    assert unicode_urldecode('%3D') == '='



# Generated at 2022-06-13 12:24:57.021115
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    a = FilterModule()
    assert 'urldecode' in a.filters()
    assert 'urlencode' in a.filters()



# Generated at 2022-06-13 12:25:03.125096
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'\u1234') == u'%E1%88%B4'
    assert unicode_urlencode(u'\xe9') == u'%C3%A9'
    assert unicode_urlencode(u'/') == u'/'
    assert unicode_urlencode(u'\u1234', True) == u'%E1%88%B4'
    assert unicode_urlencode(u'\xe9', True) == u'%C3%A9'


# Generated at 2022-06-13 12:25:05.301155
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%E2%9C%93") == u'✓'



# Generated at 2022-06-13 12:25:15.769180
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_inputs = {
        u'abc': u'abc',
        u'abc@def': u'abc%40def',
        u'abc def': u'abc+def',
        u'abc\u2019def': u'abc%E2%80%99def',
        u'abc/def': u'abc%2Fdef',
        u'abc/def': u'abc/def',
        u'abc/def': u'abc/def',
        u'abc/def': u'abc/def',
        u'abc/def': u'abc/def',
        u'abc/def': u'abc/def',
        u'abc/def': u'abc/def',
        u'abc/def': u'abc/def',
    }


# Generated at 2022-06-13 12:25:17.779899
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    cls = FilterModule()
    assert hasattr(cls, 'filters')


# Generated at 2022-06-13 12:25:22.050358
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo%2Fbar/biz') == u'foo/bar/biz'


# Generated at 2022-06-13 12:25:25.089542
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a%20b') == u'a b'
    assert unicode_urldecode(u'a+b') == u'a b'
    assert unicode_urldecode(u'a+b') == u'a b'

# Generated at 2022-06-13 12:25:28.725731
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    value = 'a%2Fb'
    expected = 'a/b'
    result = unicode_urldecode(value)
    assert result == expected


# Generated at 2022-06-13 12:25:29.965966
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20%3f%26') == ' ?&'


# Generated at 2022-06-13 12:25:44.866874
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Function unicode_urlencode must be able to encode unicode strings in python2 and python3
    if PY3:
        assert unicode_urlencode('\u00e9') == '%C3%A9'
    else:
        assert unicode_urlencode('\u00e9') == '%E9'

    # Function must encode a unicode non ascii string
    assert unicode_urlencode('\u2014') == '%E2%80%94'

    # Function must encode a string like a dictionary
    assert unicode_urlencode('a=b&b=c') == 'a%3Db%26b%3Dc'

    # Function must encode a dictionary

# Generated at 2022-06-13 12:25:51.887687
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('%61%62%63') == u'abc'
    assert unicode_urldecode('%61+%62+%63') == u'a b c'
    assert unicode_urldecode(b'%61') == u'a'
    assert unicode_urldecode(b'%61') == u'a'
    assert unicode_urldecode(u'%61') == u'a'
    assert unicode_urldecode(u'%61') == u'a'


# Generated at 2022-06-13 12:26:00.001310
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_bytes, to_text
    assert unicode_urlencode(u"a") == u'a'
    assert unicode_urlencode(u"A") == u'A'
    assert unicode_urlencode(u"a/") == u'a%2F'
    assert unicode_urlencode(u"/a") == u'%2Fa'
    assert unicode_urlencode(u"a b") == u'a+b'
    assert unicode_urlencode(to_text(to_bytes('\xe9'))) == u'%C3%A9'
    assert unicode_urlencode(u"\u03b1") == u'%CE%B1'

# Generated at 2022-06-13 12:26:06.645482
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Simple string
    assert unicode_urldecode('hello+world') == 'hello world'

    # ASCII encoding
    assert unicode_urldecode('%41%42') == 'AB'

    # UTF-8 encoding
    assert unicode_urldecode('%E2%82%AC') == u'€'

# Generated at 2022-06-13 12:26:13.876279
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # sys.stderr.write("Testing %s\n" %(unicode_urldecode.__name__))

    assert unicode_urldecode('') == ''
    assert unicode_urldecode('a') == 'a'
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('+') == ' '
    assert unicode_urldecode('%%%') == '%%'
    assert unicode_urldecode('%252F') == '/'



# Generated at 2022-06-13 12:26:19.001583
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc%5Bdef') == u'abc[def'
    assert unicode_urldecode('abc%5Bdef%5D') == u'abc[def]'
    assert unicode_urldecode('abc%5Bdef%5D%5Bghi%5D') == u'abc[def][ghi]'
    assert unicode_urldecode('abc%20def') == u'abc def'


# Generated at 2022-06-13 12:26:24.260411
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.module_utils.facts.system import distribution
    import pytest
    from os.path import dirname, join
    from ctypes.util import find_library
    import ctypes

    # Verify we have a SO we can load
    so_path = find_library(distribution.DISTRO_NAME_LIBRARY[0])
    assert so_path is not None
    assert isinstance(so_path, str)
    assert so_path == distribution.DISTRO_NAME_LIBRARY[1]
    assert isinstance(ctypes.CDLL(so_path), ctypes.CDLL)
    # Create a Distribution instance
    dist = Distribution()
   

# Generated at 2022-06-13 12:26:31.897573
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from base64 import b64encode
    from string import printable
    for x in printable:
        if x in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.~':
            assert unicode_urldecode(x) == x
            assert unicode_urldecode(x) == unicode_urldecode(unicode_urlencode(x))
        else:
            assert unicode_urldecode(x) != x
            assert unicode_urldecode(x) == unicode_urlencode(x)
    assert unicode_urldecode(b64encode(u'ä'.encode('utf-8'))) == u'ä'
    assert unicode_urldecode

# Generated at 2022-06-13 12:26:42.096933
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import ansible.module_utils.common.json
    assert unicode_urlencode(u'&=') == '%26%3D'
    assert unicode_urlencode(u'&=', for_qs=True) == '%26%3D'
    assert unicode_urlencode({u'&': u'='}) == '%26=%3D'
    assert unicode_urlencode([u'&', u'=']) == '%26&%3D'
    assert unicode_urlencode(u'http://localhost') == 'http%3A//localhost'

# Generated at 2022-06-13 12:26:46.572256
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%C3%A6") == u"æ"
    assert unicode_urldecode("%2F") == u"/"
    assert unicode_urldecode("%2c") == u","
    assert unicode_urldecode("%30") == u"0"
    assert unicode_urldecode("%0a") == u"\n"

# Generated at 2022-06-13 12:26:50.344696
# Unit test for function do_urlencode
def test_do_urlencode():
    # Use a dict with both text and bytes keys and values
    d = dict(a=1, b=2, c=3, d="hello", e=b"world")
    assert do_urlencode(d) == u'a=1&b=2&c=3&d=hello&e=world'



# Generated at 2022-06-13 12:26:54.462542
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'test%25') == u'test%'
    assert unicode_urldecode(u'test%25') == u'test%'
    assert unicode_urldecode(u'test%') == u'test%'
    assert unicode_urldecode(b'test%') == u'test%'


# Generated at 2022-06-13 12:26:58.376633
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    assert module.filters()["urldecode"] is do_urldecode
    if not HAS_URLENCODE:
        assert module.filters()["urlencode"] is do_urlencode

# Generated at 2022-06-13 12:27:00.138734
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert hasattr(FilterModule, 'filters')


# Generated at 2022-06-13 12:27:05.749873
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'https://docs.ansible.com/ansible/latest/plugins/lookup/fileglob.html') == u'https://docs.ansible.com/ansible/latest/plugins/lookup/fileglob.html'
    assert unicode_urldecode(u'https://docs.ansible.com/ansible/latest/plugins/lookup/fileglob.html?q=1%3D1') == u'https://docs.ansible.com/ansible/latest/plugins/lookup/fileglob.html?q=1=1'
    assert unicode_urldecode(u'https://docs.ansible.com/ansible/latest/plugins/lookup/fileglob.html?q=1%3D1&p%3D1') == u

# Generated at 2022-06-13 12:27:08.608128
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%21') == '!'
    assert unicode_urldecode(u'%21') == u'!'



# Generated at 2022-06-13 12:27:17.838038
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://localhost/a/b/c') == u'http%3A//localhost/a/b/c'
    assert unicode_urlencode(u'http://localhost/a/b/c', for_qs=True) == u'http%3A%2F%2Flocalhost%2Fa%2Fb%2Fc'
    assert unicode_urlencode(u'http://localhost/a/b/c', for_qs='should be bool') == u'http%3A%2F%2Flocalhost%2Fa%2Fb%2Fc'



# Generated at 2022-06-13 12:27:26.213662
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('%41%42') == 'AB'
    assert do_urldecode('%5B%20%5D') == '[ ]'
    assert do_urldecode('%E2%9C%93') == '\u2713'
    assert do_urldecode('%F0%9F%90%8D') == '\U0001f44d'
    assert do_urldecode('%F0%9F%92%A9') == '\U0001f6a9'
    assert do_urldecode('%F0%9F%93%81') == '\U0001f681'
    assert do_urldecode('%F0%9F%93%82') == '\U0001f682'

# Generated at 2022-06-13 12:27:29.424148
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode'](u"a+b") == u"a b"
    assert FilterModule().filters()['urlencode'](u"a=b c") == u"a%3Db+c"

# Generated at 2022-06-13 12:27:30.917829
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert 'urldecode' in fm.filters()

# Generated at 2022-06-13 12:27:31.729058
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()

# Generated at 2022-06-13 12:27:39.253496
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode("python & jinja2") == "python+%26+jinja2"
    assert do_urlencode("/path/to/file") == "/path/to/file"
    assert do_urlencode("/path/to/file?key=value") == "/path/to/file?key=value"
    assert do_urlencode("/path/to/file#key=value") == "/path/to/file#key=value"
    assert do_urlencode(["foo", "bar", "baz"]) == "foo&bar&baz"
    assert do_urlencode(("foo", "bar", "baz")) == "foo&bar&baz"

# Generated at 2022-06-13 12:27:41.377614
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = u'%C3%BC'
    assert unicode_urldecode(string) == u'ü'



# Generated at 2022-06-13 12:27:50.137349
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible_collections.community.general.tests.unit.compat.mock import patch
    from .unicode_proxy import UnicodeProxy

    # Test function with a Unicode string
    assert unicode_urldecode('%20') == u' '

    # Test function with a Byte string
    assert unicode_urldecode(b'%20') == u' '

    # Test function with an empty string
    assert unicode_urldecode('') == u''
    assert unicode_urldecode(b'') == u''

    # Test function with a UnicodeProxy
    assert unicode_urldecode(UnicodeProxy('%20'),) == u' '

    # Test function with an iterable

# Generated at 2022-06-13 12:27:53.999307
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    __import__('pdb').set_trace()
    filter = FilterModule()
    result = filter.filters()

    test_result = {'urldecode' : do_urldecode, 'urlencode' : do_urlencode}

    assert result == test_result


# Generated at 2022-06-13 12:28:00.291410
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abcd') == 'abcd'
    assert unicode_urldecode('%5C') == '\\'
    assert unicode_urldecode('%E4') == u'ä'
    assert unicode_urldecode('%E4%B8%96%E7%95%8C') == u'世界'
    assert unicode_urldecode('%E4%B8%96%E7%95%8C%23%E4%BA%AC%E9%83%BD') == u'世界#京都'


# Generated at 2022-06-13 12:28:12.361555
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # urldecode
    assert u'foo' == FilterModule().filters()['urldecode'](u'foo')
    assert u'foo bar' == FilterModule().filters()['urldecode'](u'foo%20bar')
    assert u'foo bar' == FilterModule().filters()['urldecode'](u'foo+bar')
    assert u'foo?bar' == FilterModule().filters()['urldecode'](u'foo%3Fbar')
    assert u'foo/bar' == FilterModule().filters()['urldecode'](u'foo/bar')
    assert u'foo@bar' == FilterModule().filters()['urldecode'](u'foo%40bar')

# Generated at 2022-06-13 12:28:17.816805
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    class filter_module(object):
        def filters(self):
            return {'urldecode': do_urldecode}
    filter_module.__name__ = 'filter_module'

    import inspect
    import sys
    jinja2 = sys.modules[FilterModule.__module__]
    ansible_modules = sys.modules[filter_module.__module__]

    if inspect.getmodule(jinja2.filters) == inspect.getmodule(ansible_modules.FilterModule):
        ansible_modules = sys.modules[FilterModule.__module__]
        jinja2 = sys.modules[FilterModule.__module__]

    assert jinja2.filters.urldecode == ansible_modules.FilterModule.filters(filter_module())['urldecode']

# Unit tests

# Generated at 2022-06-13 12:28:28.567035
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://foo/bar?baz=qux1&baz=qux2') == 'http%3A//foo/bar%3Fbaz%3Dqux1%26baz%3Dqux2'
    assert unicode_urlencode('http://foo/bar/baz') == 'http%3A//foo/bar/baz'
    assert unicode_urlencode({'k1': 'v1', 'k2': 'v2'}) == 'k2=v2&k1=v1'
    assert unicode_urlencode(('k1', 'v1')) == 'k1=v1'
    assert unicode_urlencode('string') == 'string'

# Generated at 2022-06-13 12:28:32.911342
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u'%20'
    assert unicode_urldecode('%C3%A1') == u'á'


# Generated at 2022-06-13 12:28:39.897452
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('%3C%3E') == u'<>'
    assert do_urldecode('<>') == u'<>'
    assert do_urlencode('<>') == u'%3C%3E'
    assert do_urlencode(u'<>') == u'%3C%3E'
    assert do_urlencode([u'<', u'>']) == u'%3C&%3E'
    assert do_urlencode({u'<': u'>'}) == u'%3C=%3E'
    assert do_urlencode(u'<>', for_qs=True) == u'%3C%3E'

# Generated at 2022-06-13 12:28:43.167055
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = u'a%26b'
    result = unicode_urldecode(string)
    assert result == u'a&b', "Expected u'a&b', got: %s" % result


# Generated at 2022-06-13 12:28:48.058020
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo+bar%2Fbaz') == u'foo bar/baz'
    assert unicode_urldecode(u'foo+bar+%22baz') == u'foo bar "baz'
    assert unicode_urldecode(u'foo+bar%2Fbaz%3Dbang') == u'foo bar/baz=bang'


# Generated at 2022-06-13 12:28:52.131913
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abcd') == u'abcd'
    assert unicode_urldecode('~abcd') == u'~abcd'
    assert unicode_urldecode('%7Eabcd') == u'~abcd'
    assert unicode_urldecode('%7Eabcd%3B%3A%2F%3F%3D%26') == u'~abcd;:/?=&'



# Generated at 2022-06-13 12:29:01.720097
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from collections import namedtuple
    from ansible.module_utils import basic

    class DummyModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args['failed'] = True
            raise Exception('FAILED: {0}'.format(kwargs['msg']))

        def exit_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args['failed'] = False

    if PY3:
        unicode_string = 'abc'
    else:
        unicode_string = 'abc'.decode('ascii')
    DummyModule.run_command = basic.run_command

    # Case

# Generated at 2022-06-13 12:29:04.976727
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('https%3A%2F%2Fgithub.com%2Fansible%2Fansible%2Farchive%2Fdevel.tar.gz') == u'https://github.com/ansible/ansible/archive/devel.tar.gz'


# Generated at 2022-06-13 12:29:14.509124
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six.moves.urllib.parse import parse_qs
    from ansible.compat.tests.mock import patch

    with patch('ansible.module_utils.six.moves.urllib.parse.quote') as mock_quote:
        with patch('ansible.module_utils.six.moves.urllib.parse.quote_plus') as mock_quote_plus:
            with patch('ansible.module_utils.six.moves.urllib.parse.unquote_plus') as mock_unquote_plus:
                # Test that the urldecode filter works correctly
                assert FilterModule().filters()['urldecode']('test') == 'test'

                # Test that the urlencode filter works correctly
                mock_quote.return_value = b'bar'

# Generated at 2022-06-13 12:29:25.495014
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3A%2F%2Fexample.org%2F%3Ftest=test%26test=test') == u'http://example.org/?test=test&test=test'
    assert unicode_urldecode(u'http%3a%2f%2fexample.org%2f%3ftest=test%26test=test') == u'http://example.org/?test=test&test=test'
    assert unicode_urldecode(u'http:/example.org/?test=test&test=test') == u'http:/example.org/?test=test&test=test'

# Generated at 2022-06-13 12:29:37.297597
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode(u'http://example.org/') == 'http%3A//example.org/'
        assert unicode_urlencode(u'http://example.org/path/sub?a=&b=') == 'http%3A//example.org/path/sub%3Fa%3D%26b%3D'
        assert unicode_urlencode(u'some_stringify_unicode_string', for_qs=True) == 'some_stringify_unicode_string'
    else:
        assert unicode_urlencode(u'http://example.org/') == 'http%3A%2F%2Fexample.org%2F'

# Generated at 2022-06-13 12:29:39.405173
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()
    print(filters)


# Generated at 2022-06-13 12:29:44.254173
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("") == ""
    assert unicode_urldecode("a") == "a"
    assert unicode_urldecode("%20") == " "
    assert unicode_urldecode("a+") == "a "
    assert unicode_urldecode("%c3%a9") == "é"


# Generated at 2022-06-13 12:29:53.545368
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from datetime import date
    from jinja2 import Environment
    env = Environment(extensions=[FilterModule])

    # test urldecode
    urlencoded_value = 'key+%C3%A0%C3%A1%C3%A2%C3%A4%C3%A3+key2+%C3%A8%C3%A9%C3%AA%C3%AB%C3%AC'
    (value, type) = env.parse('{{ value | urldecode }}', mode='eval')
    assert 'key àáâäã key2 èéêëì' == env.filters['urldecode'](value, urlencoded_value)


# Generated at 2022-06-13 12:29:57.058125
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test_string = "This+test+string%2C+%7B%22key%22%3A%22value%22%7D"
    expected = "This test string, {\"key\":\"value\"}"
    assert unicode_urldecode(test_string) == expected



# Generated at 2022-06-13 12:30:01.305377
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/%') == '/%25'
    assert unicode_urlencode('/%', for_qs=True) == '%2F%25'
    assert unicode_urlencode('/tést%') == '/t%C3%A9st%25'
    assert unicode_urlencode('/tést%', for_qs=True) == '%2Ft%C3%A9st%25'


# Generated at 2022-06-13 12:30:11.265590
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ansible_jinja2_filters = FilterModule().filters()
    #print(ansible_jinja2_filters)
    assert isinstance(ansible_jinja2_filters, dict)
    assert ansible_jinja2_filters['urldecode'].__name__ == 'do_urldecode'
    assert ansible_jinja2_filters['urldecode'].__doc__ ==  unicode_urldecode.__doc__
    assert ansible_jinja2_filters['urldecode']('A%20space') == 'A space'
    assert ansible_jinja2_filters['urldecode']('\u20AC') == '€'

# Generated at 2022-06-13 12:30:18.186811
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('foo%20bar') == 'foo bar'

    assert do_urlencode('foo bar') != 'foo+bar'
    assert do_urlencode('foo bar') == 'foo%20bar'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'foo': 'bar', 'spam': 'eggs'}) == 'foo=bar&spam=eggs'
    assert do_urlencode([('foo', 'bar'), ('spam', 'eggs')]) == 'foo=bar&spam=eggs'
    assert do_urlencode({'key': ['value1', 'value2']}) == 'key=value1&key=value2'

# Generated at 2022-06-13 12:30:21.232213
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert isinstance(unicode_urldecode(b'foo+bar'), str)
    assert unicode_urldecode(b'foo+bar') == 'foo bar'



# Generated at 2022-06-13 12:30:23.764934
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    obj = FilterModule()
    assert obj.filters() == {
        'urldecode': do_urldecode,
        'urlencode': do_urlencode,
    }


# Generated at 2022-06-13 12:30:39.686898
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test case 1: The urldecode filter method
    # that decodes a URL-encoded string.
    # Input:
    #   an encoded string
    # Expected result:
    #   the decoded string
    url = 'http%3A%2F%2Fwww.python.org%2F'
    decoded_url = 'http://www.python.org/'
    objFilter = FilterModule()
    assert objFilter.filters()['urldecode'](url) == decoded_url

    # Test case 2: The urldecode filter method
    # that decodes a URL-encoded string.
    # Input:
    #   an string
    # Expected result:
    #   the input string
    url = 'http://www.python.org/'

# Generated at 2022-06-13 12:30:41.009748
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()


# Generated at 2022-06-13 12:30:45.447824
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('hey%20guys%21') == u'hey guys!'
    assert unicode_urldecode('hey+guys%21') == u'hey guys!'
    assert unicode_urldecode('%F0%9F%98%B3') == u'😳'
    assert unicode_urldecode('%E6%B5%B7%E5%A4%96') == u'海外'


# Generated at 2022-06-13 12:30:47.500458
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%2A%3F%26%3D%5B%5D%25%20%C3%A9') == u'*?&=[]% \xe9'



# Generated at 2022-06-13 12:30:52.595453
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' Test urldecode filter'''
    from ansible.module_utils.basic import AnsibleModule
    text = u"this is a test: b%C3%A9b%C3%A9"
    module = AnsibleModule(
        argument_spec=dict(
            text=dict(type=u'unicode', required=True),
        ),
    )

    assert text == module.urldecode(u"this%20is%20a%20test%3A%20b%C3%A9b%C3%A9")
    assert text == module.urldecode(u"this+is+a+test%3A+b%C3%A9b%C3%A9")


# Generated at 2022-06-13 12:30:59.012554
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    res = unicode_urldecode('foo')
    assert res == u'foo'
    res = unicode_urldecode('foo%2Fbar%3Bbaz')
    assert res == u'foo/bar;baz'
    res = unicode_urldecode('foo%2Fbar+baz%40bla')
    assert res == u'foo/bar baz@bla'
    if PY3:
        res = unicode_urldecode('foo%2Fbar+baz%40bla'.encode('utf-8'))
        assert res == u'foo/bar baz@bla'
    else:
        res = unicode_urldecode(u'foo%2Fbar+baz%40bla')

# Generated at 2022-06-13 12:31:09.776284
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'dag åge') == u'dag%20%C3%A5ge'
    assert unicode_urlencode(u'dag åge', for_qs=True) == u'dag+%C3%A5ge'
    assert unicode_urlencode(u'http://example.com/%s?k=v&foo=bar') == u'http%3A//example.com/%25s%3Fk%3Dv%26foo%3Dbar'
    assert unicode_urlencode(u'/foo/bar/') == u'/foo/bar/'

# Generated at 2022-06-13 12:31:18.488958
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"example.com") == u"example.com"
    assert unicode_urldecode(u"example.com/foo bar") == u"example.com/foo bar"
    assert unicode_urldecode(u"example.com/foo%20bar") == u"example.com/foo bar"
    assert unicode_urldecode(u"example.com/foo+bar") == u"example.com/foo bar"
    assert unicode_urldecode(u"example.com/foo%2Bbar") == u"example.com/foo+bar"
    assert unicode_urldecode(u"example.com/foo%2bbar") == u"example.com/foo+bar"


# Generated at 2022-06-13 12:31:24.954142
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("This is a test") == "This is a test"
    assert unicode_urldecode("This%20is%20a%20test") == "This is a test"
    assert unicode_urldecode("%2B") == "+"
    assert unicode_urldecode("%30") == "0"
    assert unicode_urldecode("%31") == "1"
    assert unicode_urldecode("%32") == "2"
    assert unicode_urldecode("%33") == "3"
    assert unicode_urldecode("%34") == "4"
    assert unicode_urldecode("%35") == "5"
    assert unicode_urldecode("%36") == "6"
    assert unic

# Generated at 2022-06-13 12:31:30.045723
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo+bar') == 'foo bar'
    assert unicode_urldecode('foo%20bar') == 'foo bar'
    assert unicode_urldecode('foo+%20bar') == 'foo  bar'
    assert unicode_urldecode('foo%2Bbar') == 'foo+bar'
    assert unicode_urldecode('foo++bar') == 'foo  bar'
    assert unicode_urldecode('foo%2B%20%2Bbar') == 'foo+  bar'


# Generated at 2022-06-13 12:31:38.721108
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    m = FilterModule()
    filters = m.filters()

    # Assert that all filters are implemented
    assert sorted(filters.keys()) == sorted(('urldecode', 'urlencode'))

    # Assert that filters are properly implemented
    assert filters['urldecode']('this+is%20some%26test%3Dtrue') == u'this is some&test=true'
    assert filters['urldecode']('foo%26bar%3D') == u'foo&bar='
    assert filters['urldecode']('foo%3Dbar%26baz%3D') == u'foo=bar&baz='

    # Assert that basic urlencode works

# Generated at 2022-06-13 12:31:49.132003
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'Hello World') == 'Hello%20World'
    assert unicode_urlencode(u'Hello World', for_qs=True) == 'Hello+World'

    assert unicode_urlencode(u'/') == '%2F'
    assert unicode_urlencode(u'/', for_qs=True) == '%2F'

    assert unicode_urlencode(u'http://192.168.0.1') == 'http%3A%2F%2F192.168.0.1'
    assert unicode_urlencode(u'http://192.168.0.1', for_qs=True) == 'http%3A%2F%2F192.168.0.1'


# Generated at 2022-06-13 12:31:58.516901
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode(u'hello world') == u'hello+world'
    assert do_urlencode(u'hello world %') == u'hello+world+%25'
    assert do_urlencode(u'hello world /') == u'hello+world+%2F'
    assert do_urlencode(u'hello/world') == u'hello%2Fworld'
    assert do_urlencode([u'hello', u'world']) == u'hello&world'
    assert do_urlencode({u'hello': u'world'}) == u'hello=world'

# Generated at 2022-06-13 12:32:06.735507
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Test function unicode_urldecode
    '''

    # Test normal ASCII
    value = 'a-z0-9'
    result = unicode_urldecode(value)
    assert result == u'a-z0-9'

    # Test ASCII and UTF8
    value = 'a-z0-9\xc3\x81'
    result = unicode_urldecode(value)
    assert result == u'a-z0-9\xc3\x81'

    # Test ASCII and UTF16
    value = 'a-z0-9\xff\xfe\x01\x00'
    result = unicode_urldecode(value)
    assert result == u'a-z0-9\U00010000'



# Generated at 2022-06-13 12:32:10.782998
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Test+Stuff') == 'Test Stuff'

    if PY3:
        assert unicode_urldecode(to_text(b'Test+Stuff')) == 'Test Stuff'
    else:
        assert unicode_urldecode(to_bytes('Test+Stuff')) == 'Test Stuff'



# Generated at 2022-06-13 12:32:17.398662
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('I%20am%20Dag%2C%20and%20I%20%C3%A9njoy%20%C3%A0%20bon%20Queso%28%29%3B%3A%26%2333%3B') == u'I am Dag, and I énjoy à bon Queso();:&#33;'

# Generated at 2022-06-13 12:32:21.464389
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E6%97%A5%E6%9C%AC%E8%AA%9E') == u'\u65e5\u672c\u8a9e'


# Generated at 2022-06-13 12:32:28.883989
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"%2F%2F%2F") == u"///"
    assert unicode_urldecode(u"%2F%2F%2F%2F") == u"///"
    assert unicode_urldecode(u"%2f%2f%2f") == u"///"
    assert unicode_urldecode(u"%2f%2f%2f%2f") == u"///"


# Generated at 2022-06-13 12:32:32.791619
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ansible_module_util_FilterModule = FilterModule()
    print("Filters are :")
    print(ansible_module_util_FilterModule.filters())

if __name__ == "__main__":
    test_FilterModule_filters()

# Generated at 2022-06-13 12:32:40.334042
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("abc") == "abc"
    assert unicode_urlencode("a+b") == "a%2Bb"
    assert unicode_urlencode("a b") == "a%20b"
    assert unicode_urlencode("a b") == "a%20b"
    assert unicode_urlencode("/a b") == "%2Fa%20b"
    assert unicode_urlencode("a b", for_qs=True) == "a%20b"
    assert unicode_urlencode("a+b", for_qs=True) == "a%2Bb"

# Generated at 2022-06-13 12:32:51.727792
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('abc') == u'abc'
    assert do_urldecode('%41%42%43') == u'ABC'
    assert do_urldecode('%41%42%43%') == u'ABC%'
    assert do_urldecode('%ad%ae%af') == u'\xad\xae\xaf'
    assert do_urldecode('%AD%AE%AF') == u'\xad\xae\xaf'
    assert do_urldecode('%') == u'%'

    assert do_urlencode('abc') == u'abc'
    assert do_urlencode('ABC') == u'ABC'
    assert do_urlencode('ABC%') == u'ABC%25'

# Generated at 2022-06-13 12:32:58.964491
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode(u'http://www.example.com/my%20dir/my file.html') == u'http%3A//www.example.com/my%20dir/my%20file.html'
    assert do_urlencode(u'http://www.example.com/my file.html') == u'http%3A//www.example.com/my%20file.html'
    assert do_urlencode(u'http://www.example.com/my_dir/my file.html') == u'http%3A//www.example.com/my_dir/my%20file.html'
    assert do_urlencode(u'/this is/my_dir/my file.html') == u'/this%20is/my_dir/my%20file.html'
    assert do_

# Generated at 2022-06-13 12:33:05.337363
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('unicode string') == 'unicode%20string'
    assert unicode_urlencode('unicode_string') == 'unicode_string'
    assert unicode_urlencode('unicode+string') == 'unicode+string'
    assert unicode_urlencode('unicode/string') == 'unicode/string'
    assert unicode_urlencode('unicode@string') == 'unicode%40string'
    assert unicode_urlencode('unicode?string') == 'unicode%3Fstring'


# Generated at 2022-06-13 12:33:18.006293
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%2B") == "+"
    assert unicode_urldecode("%2b") == "+"
    assert unicode_urldecode("%F6") == "ö"
    assert unicode_urldecode("%f6") == "ö"
    assert unicode_urldecode("%2B%2B") == "++"
    assert unicode_urldecode("%2b%2b") == "++"
    assert unicode_urldecode("%F6%F6") == "öö"
    assert unicode_urldecode("%f6%f6") == "öö"



# Generated at 2022-06-13 12:33:23.896820
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils._text import to_bytes
    module = FilterModule()
    assert(module.filters()['urldecode']("%3D") == "=")
    assert(module.filters()['urldecode']("%3D") == "=")
    if not HAS_URLENCODE:
        assert(to_bytes(module.filters()['urlencode']("=")) == to_bytes("%3D"))
        assert(to_bytes(module.filters()['urlencode']("=")) == to_bytes("%3D"))


# Generated at 2022-06-13 12:23:21.669767
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7B%22foo%22%3A%20%22bar%22%7D') == '{"foo": "bar"}'

# Generated at 2022-06-13 12:23:34.718599
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from jinja2 import Environment, StrictUndefined, Template

    env = Environment(undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    env.filters = (FilterModule().filters())
    template = Template('Hello World')
    assert template.render(env).strip() == 'Hello World'

    template = Template('{{ [1, 2, 3]|urlencode }}')
    assert template.render(env).strip() == '1=2&2=3&3='

    template = Template('{{ { "a": 1, "b": 2 }|urlencode }}')
    assert template.render(env).strip() == 'a=1&b=2'

    template = Template('{{ { "a": 1, "b": 2 }|to_json|urlencode }}')
   

# Generated at 2022-06-13 12:23:40.764526
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestUnicodeUrldecode(unittest.TestCase):

        @patch('ansible.module_utils.six.PY3', False)
        def test_urldecode_python2(self):
            self.assertEqual(unicode_urldecode(u'%20'), u' ')
            self.assertEqual(unicode_urldecode(u'%26'), u'&')
            self.assertEqual(unicode_urldecode(u'%2B'), u'+')
            self.assertEqual(unicode_urldecode(u'%3D'), u'=')


# Generated at 2022-06-13 12:23:49.823060
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode(u'foo') == '/foo'
        assert unicode_urlencode(u'foo bar') == '/foo%20bar'
        assert unicode_urlencode(u'foo bar/') == '/foo%20bar%2F'
        assert unicode_urlencode(u'foo?bar') == '/foo%3Fbar'
        assert unicode_urlencode(u'foo?bar/') == '/foo%3Fbar%2F'

        assert unicode_urlencode(u'fóo') == '/f%C3%B3o'
        assert unicode_urlencode(u'fóo bar') == '/f%C3%B3o%20bar'

# Generated at 2022-06-13 12:23:59.700499
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' Test the ansible.module_utils.urls.unicode_urldecode function '''

    test_cases = [
        # Test an empty string
        ('', ''),

        # Test typical URL patterns
        ('a=b&c=d', 'a=b&c=d'),
        ('a=b%26c%3Dd', 'a=b&c=d'),
        ('a=b%26c=%3Dd', 'a=b&c==d'),

        # Test a unicode string
        ('b%C3%A4r', u'bär'),
    ]

    for (data, expected) in test_cases:
        result = unicode_urldecode(data)
        assert result == expected



# Generated at 2022-06-13 12:24:05.084193
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Unit test for function urldecode
    '''
    assert unicode_urldecode(u'foo') == 'foo'
    assert unicode_urldecode(u'foo%20bar') == 'foo bar'
    assert unicode_urldecode(u'foo+bar') == 'foo bar'
    assert unicode_urldecode(u'foo%7ebar') == 'foo~bar'
    assert unicode_urldecode(u'foo%7Ebar') == 'foo~bar'
    assert unicode_urldecode(u'foo%%20bar') == 'foo% bar'
    assert unicode_urldecode(u'foo%%bar') == 'foo%bar'

# Generated at 2022-06-13 12:24:08.919952
# Unit test for function do_urlencode
def test_do_urlencode():
    # Base function
    assert do_urlencode('foo') == 'foo'

    # List
    assert do_urlencode(['foo', 'bar', 'baz']) == 'foo&bar&baz'

    # Dict
    assert do_urlencode({'foo': 'bar', 'baz': 'meh'}) == 'foo=bar&baz=meh'

# Generated at 2022-06-13 12:24:16.600973
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'string') == u'string'
    assert unicode_urldecode(u'str%20ing') == u'str ing'
    assert unicode_urldecode(u'str%2Bing') == u'str+ing'
    assert unicode_urldecode(u'str%2B%20ing') == u'str+ ing'
    assert unicode_urldecode(u'str%2B%20ing%2B') == u'str+ ing+'


# Generated at 2022-06-13 12:24:20.818066
# Unit test for function do_urlencode
def test_do_urlencode():
    test_data = {
        'test': 'value',
        'test2': 'value2',
    }
    data = do_urlencode(test_data)
    assert type(data) == unicode
    assert data == u'test=value&test2=value2'

# Generated at 2022-06-13 12:24:28.867441
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foobar') == u'foobar'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'?') == u'%3F'
    assert unicode_urlencode(u'&') == u'%26'
    assert unicode_urlencode(u' ') == u'%20'
    assert unicode_urlencode(u'/') == u'%2F'
    assert unicode_urlencode(u'foo/bar') == u'foo%2Fbar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == u'foo%20bar'
    assert unicode_urlencode(u'?', for_qs=True) == u

# Generated at 2022-06-13 12:24:38.716259
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from sys import version_info
    if version_info.major == 2:
        assert unicode_urlencode(u'http://example.com/?foo=bar+baz') == 'http%3A%2F%2Fexample.com%2F%3Ffoo%3Dbar%2Bbaz'
        assert unicode_urlencode(u'http://example.com/?foo=bar+baz', for_qs=True) == 'http%3A%2F%2Fexample.com%2F%3Ffoo%3Dbar%2Bbaz'

# Generated at 2022-06-13 12:24:47.102461
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''Unit test for method filters of class FilterModule'''

    fmd = FilterModule()
    filters = fmd.filters()
    assert filters is not None
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert filters['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:24:50.241951
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert dict == type(FilterModule.filters(None))
    assert 2 == len(FilterModule.filters(None))



# Generated at 2022-06-13 12:24:52.153610
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    assert f.filters()


# Generated at 2022-06-13 12:24:58.065742
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    # Testing unicode_urldecode with ascii
    ascii_value = 'abcdefg'
    assert unicode_urldecode(ascii_value) == ascii_value

    # Testing unicode_urldecode with unicode
    unicode_value = 'سيكون لأي شخص'
    encoded_unicode_value = '%D8%B3%D9%8A%D9%83%D9%88%D9%86%20%D9%84%D8%A3%D9%8A%20%D8%B4%D8%AE%D8%B5'
    assert unicode_urldecode(encoded_unicode_value) == unicode_value



# Generated at 2022-06-13 12:25:05.489048
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert to_text(quote_plus(to_bytes('a=1&b=2'))) == unicode_urlencode('a=1&b=2')
    assert to_text(quote_plus(to_bytes('a=1&b=2'), b'')) == unicode_urlencode('a=1&b=2', False)
    assert to_text(quote(to_bytes('a=1&b=2'))) == unicode_urlencode('a=1&b=2', False)
    assert to_text(quote(to_bytes('/'))) == unicode_urlencode('/', False)
    assert to_text(quote_plus(to_bytes('/'))) != unicode_urlencode('/')



# Generated at 2022-06-13 12:25:15.986747
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    print("Running unittest_FilterModule_filters")

    import jinja2
    env = jinja2.Environment()

    # test urldecode filters
    test_string = "a"
    # should be an empty string - string should not be altered
    assert FilterModule.filters().get('urldecode')(test_string) == test_string
    test_string = "/etc/passwd"
    # should be an empty string - string should not be altered
    assert FilterModule.filters().get('urldecode')(test_string) == test_string
    test_string = "variable"
    # should be an empty string - string should not be altered
    assert FilterModule.filters().get('urldecode')(test_string) == test_string
    test_string = "var?iable"

# Generated at 2022-06-13 12:25:22.092457
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"%22%27%2f%5Ccut%5Cp%5Cn%5Ct") == "'/\\cut\\p\\n\\t"
    assert unicode_urldecode(u"%22%27%2f%5Ccu%74%5Cp%5Cn%5Ct") == "'/\\cu\\t\\p\\n\\t"



# Generated at 2022-06-13 12:25:29.509480
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from sys import version_info
    if version_info < (2, 7):
        from nose.plugins.skip import SkipTest
        raise SkipTest("Python >= 2.7 is needed for urllib.parse.quote()")
    import urllib

    def url_quote(string, safe=b''):
        safe = b'' if safe == '/' else safe
        if PY3:
            return urllib.parse.quote(string, safe)
        return to_text(urllib.parse.quote(to_bytes(string), safe))

    def url_quote_plus(string, safe=b''):
        safe = b'' if safe == '/' else safe
        if PY3:
            return urllib.parse.quote_plus(string, safe)

# Generated at 2022-06-13 12:25:38.395164
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('a/b c') == 'a%2Fb%20c'
    assert unicode_urlencode('a/b c', for_qs=True) == 'a%2Fb+c'
    assert unicode_urlencode(['a', 'b']) == 'a&b'
    assert unicode_urlencode({'a': 'b', 'c': 'd'}) == 'a=b&c=d'


# Generated at 2022-06-13 12:25:44.316109
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20%21%22%23%24%25%26%27%28%29%2a%2b%2c%2d%2e%2f%30') == ' !"#$%&\'()*+,-./0'


# Generated at 2022-06-13 12:25:47.567393
# Unit test for method filters of class FilterModule

# Generated at 2022-06-13 12:25:51.780193
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys
    if PY3:
        assert unicode_urldecode('%E4%B8%AD%E6%96%87') == '中文'
    else:
        assert unicode_urldecode('%E4%B8%AD%E6%96%87') == unicode('中文', 'utf-8')


# Generated at 2022-06-13 12:25:59.896843
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"http://www.example.com") == u"http://www.example.com"
    assert unicode_urlencode(u"http://www.example.com/foo bar") == u"http://www.example.com/foo%20bar"
    assert unicode_urlencode(u"http://www.example.com/?foo bar") == u"http://www.example.com/?foo+bar"
    assert unicode_urlencode(u"http://www.example.com/?foo&bar") == u"http://www.example.com/?foo&bar"
    assert unicode_urlencode(u"http://www.example.com/?foo=bar") == u"http://www.example.com/?foo%3Dbar"

# Generated at 2022-06-13 12:26:03.403758
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filterModule = FilterModule()
    assert isinstance(filterModule.filters(), dict)



# Generated at 2022-06-13 12:26:09.881526
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('dag%20wieers') == 'dag wieers'
    assert unicode_urldecode('dag+wieers') == 'dag wieers'
    assert unicode_urldecode('%CE%94%CE%B9%CE%B5%CF%85%CF%83') == u'Διευσ'
    assert unicode_urldecode('%F0%9F%99%8F') == u'\U0001f38f'


# Generated at 2022-06-13 12:26:18.614830
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%20%21%22%23%24%25%26%27%28%29%2A%2B%2C%2F%30%31%32%33%34%35%36%37%38%39%3A%3B%3D%3F') == u' !"#$%&\'()*+,-/0123456789:;=?'
    assert unicode_urldecode('%C2%A9') == u'©'
    assert unicode_urldecode('%C2%A9%20%E2%84%A2') == u'© ™'
    assert unicode_urldecode('%C3%A9') == u'é'
   

# Generated at 2022-06-13 12:26:23.412471
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3A%2F%2Ffoo%20bar%2F') == u'http://foo bar/'
    assert unicode_urldecode(b'http%3A%2F%2Ffoo%20bar%2F') == u'http://foo bar/'
    assert unicode_urldecode(None) == u''


# Generated at 2022-06-13 12:26:26.402390
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('abc%20def') == u'abc def'


# Generated at 2022-06-13 12:26:35.738929
# Unit test for function do_urlencode
def test_do_urlencode():
    from ansible.module_utils.six.moves.urllib.parse import urlencode

# Generated at 2022-06-13 12:26:44.203258
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    urldecode = filters.get('urldecode')
    assert urldecode('https://www.itg.ias.edu/content/export/ROOT-Switch-Guide.pdf') == 'https://www.itg.ias.edu/content/export/ROOT-Switch-Guide.pdf'
    assert urldecode('https%3A%2F%2Fwww.itg.ias.edu%2Fcontent%2Fexport%2FROOT-Switch-Guide.pdf') == 'https://www.itg.ias.edu/content/export/ROOT-Switch-Guide.pdf'
    assert urldecode('https://www.itg.ias.edu/content/export/ROOT-Switch-Guide.pdf?e=1')

# Generated at 2022-06-13 12:26:56.497906
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils._text import to_bytes
    assert unicode_urldecode("%E4%B8%AD%E6%96%87") == "\xe4\xb8\xad\xe6\x96\x87"

    # Test that unicode_urldecode decodes a byte string to text
    assert isinstance(unicode_urldecode("%E4%B8%AD%E6%96%87"), unicode)
    assert unicode_urldecode(to_bytes("%E4%B8%AD%E6%96%87", encoding="utf-8")) == "\xe4\xb8\xad\xe6\x96\x87"

# Generated at 2022-06-13 12:27:00.680074
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = u'http://www.example.com:8080/uri?a=b%20c#d e'
    assert unicode_urldecode(string) == u'http://www.example.com:8080/uri?a=b c#d e'



# Generated at 2022-06-13 12:27:05.057236
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Create an instance of FilterModule
    fm = FilterModule()

    # Check that urlencode is correctly implemented.
    assert fm.filters()['urlencode'] == do_urlencode

    # Check that urldecode is correctly implemented.
    assert fm.filters()['urldecode'] == do_urldecode


# Generated at 2022-06-13 12:27:09.156562
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()

    assert 'urldecode' in filters

    if not HAS_URLENCODE:
        assert 'urlencode' in filters
    else:
        assert 'urlencode' not in filters

# Generated at 2022-06-13 12:27:12.466860
# Unit test for function do_urlencode
def test_do_urlencode():
    value = {'a': 1, 'b': 2, 'c': 3}
    result = do_urlencode(value)
    assert result == 'a=1&b=2&c=3'



# Generated at 2022-06-13 12:27:17.741156
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%40%2F%3F%23%3D%3A%3B%24') == '@/?#=:;$'
    assert unicode_urldecode('%E8%B0%B7%E6%AD%8C') == u'谷歌'.encode('utf-8')


# Generated at 2022-06-13 12:27:20.195068
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%C3%A9") == u'\u00e9'



# Generated at 2022-06-13 12:27:23.262968
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """
    >>> test_FilterModule_filters()
    {'urldecode': <function do_urldecode at 0x10455e488>}
    """
    o = FilterModule()
    return o.filters()

# Generated at 2022-06-13 12:27:28.162512
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a+b') == u'a b'
    assert unicode_urldecode('a%20b') == u'a b'
    assert unicode_urldecode('/a%2Bb/') == u'/a+b/'



# Generated at 2022-06-13 12:27:31.613537
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert not fm.filters()['urldecode'] is None
    assert not fm.filters()['urlencode'] is None

# Generated at 2022-06-13 12:27:39.158035
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode(None) == 'None'
        assert unicode_urlencode('None') == 'None'
        assert unicode_urlencode('None') == 'None'
        assert unicode_urlencode(b'None') == 'Tm9uZQ%3D%3D'
        assert unicode_urlencode([None]) == 'None'
        assert unicode_urlencode({None}) == 'None'
        assert unicode_urlencode('None', for_qs=False) == 'None'
        assert unicode_urlencode('None', for_qs=True) == 'None'
        assert unicode_urlencode('foo/bar', for_qs=False) == 'foo%2Fbar'

# Generated at 2022-06-13 12:27:48.617184
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%2Bb%2Bc') == u'a+b+c'
    assert unicode_urldecode('%e2%82%ac') == u'\u20ac'
    assert unicode_urldecode('%2F%2F%2F') == u'///'
    assert unicode_urldecode('%2F') == u'/'
    assert unicode_urldecode('%2f') == u'/'
    assert unicode_urldecode('%0A') == u'\n'
    assert unicode_urldecode('%2F1%2F2%2F3%2F4') == u'/1/2/3/4'


# Generated at 2022-06-13 12:27:55.820878
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import u, b
    filt = FilterModule()
    assert isinstance(filt.filters(), Mapping)
    for name, func in iteritems(filt.filters()):
        assert hasattr(func, '__call__')

# Generated at 2022-06-13 12:28:03.881716
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # We should be able to safely urldecode a string
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%A3') == u'\xa3'
    assert unicode_urldecode('%E2%82%AC') == u'\u20ac'
    assert unicode_urldecode('/abc/') == u'/abc/'



# Generated at 2022-06-13 12:28:13.687347
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # The input is a single Unicode character
    # The output is the same character, decoded
    assert unicode_urldecode(u'%C3%A4') == u'\u00E4'

    # The input is a Unicode string
    # The output is the same string, decoded
    assert unicode_urldecode(u'abc%20def') == u'abc def'

    # The input is a bytestring where the character values are percent-encoded
    # The output is the same string, decoded
    assert unicode_urldecode(b'%41%42%43') == u'ABC'

    # The input is a bytestring with utf-8 character values
    # The output is the same string, decoded

# Generated at 2022-06-13 12:28:18.993963
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    print("\nTest unicode_urldecode()")
    print("The result should be %s" % "%E2%82%AC")
    print("The result is %s" % unicode_urldecode("%E2%82%AC"))
    print("The result should be %s" % "€")
    print("The result is %s" % unicode_urldecode("%E2%82%AC"))


# Generated at 2022-06-13 12:28:28.240717
# Unit test for function do_urlencode
def test_do_urlencode():
    test_cases = [
        ('/', '/'),
        ('/path with spaces', '/path%20with%20spaces'),
        ('/path?foo=bar&baz=faz', '/path%3Ffoo%3Dbar%26baz%3Dfaz'),
        (['/path', {'key': 'value with spaces'}], '/path&key=value%20with%20spaces'),
        ({'foo': 'bar', 'baz': 'faz'}, 'baz=faz&foo=bar'),
        ('/path with spaces?foo=bar', '/path%20with%20spaces%3Ffoo%3Dbar'),
        ('/path?foo=bar with spaces', '/path%3Ffoo%3Dbar%20with%20spaces'),
    ]


# Generated at 2022-06-13 12:28:35.995587
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' Test unicode_urldecode function '''

    assert 'A B' == unicode_urldecode(b'A+B')
    assert 'A B' == unicode_urldecode('A+B')
    assert 'A B' == unicode_urldecode(to_bytes(u'A+B'))
    assert 'A B' == unicode_urldecode(to_text(b'A+B'))
    assert 'A B' == unicode_urldecode(unquote_plus(b'A+B'))
    assert u'A B' == unicode_urldecode(u'A+B')
    assert u'A B' == unicode_urldecode(to_bytes(u'A+B'))
    assert u'A B' == unic

# Generated at 2022-06-13 12:28:44.900840
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test1') == 'test1'
    assert unicode_urlencode('test space') == 'test%20space'
    assert unicode_urlencode('test+plus') == 'test%2Bplus'
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode('/', True) == '/'
    assert unicode_urlencode('test1', True) == 'test1'
    assert unicode_urlencode('test space', True) == 'test+space'
    assert unicode_urlencode('test+plus', True) == 'test%2Bplus'


# Generated at 2022-06-13 12:28:59.076441
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest
    from ansible.module_utils.jinja2 import AnsibleJ2Module
    test_module = AnsibleJ2Module()
    fm = FilterModule()
    fm.filters()
    filt = test_module.from_template('{{ "http://example.com/foo bar/?a=b&c=d" | urldecode }}')
    assert filt == 'http://example.com/foo bar/?a=b&c=d'
    filt = test_module.from_template('{{ { "a": "b", "c" : "d" } | urlencode }}')
    assert filt == 'a=b&c=d'

# Generated at 2022-06-13 12:29:03.087224
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import os
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    FilterModule_obj = FilterModule()
    filters = FilterModule_obj.filters()
    for fname, f in iteritems(filters):
        print("fname: %s" % fname)
        print("%s: %s" % (fname, repr(fname)))




# Generated at 2022-06-13 12:29:13.269809
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    ''' Unit test for function unicode_urlencode '''

    def assert_unicode_urlencode(expected, value):
        ''' Helper function to assert an expected urlencode value '''

        actual = unicode_urlencode(value)
        if actual != expected:
            raise AssertionError('Expected %s (%s) but got %s (%s)' % (expected, type(expected), actual, type(actual)))

    # Test normal strings
    assert_unicode_urlencode('string', 'string')
    assert_unicode_urlencode('%2Fstring', u'/string')
    assert_unicode_urlencode('%E5%B0%8F+%E5%A4%AA%C2%B0', u'小 太°')

    # Test unicode strings
   

# Generated at 2022-06-13 12:29:24.378562
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%20b+c') == 'a b c'
    assert unicode_urldecode('a%20b%2Bc') == 'a b+c'
    assert unicode_urldecode('a%20b%40c') == 'a b@c'
    assert unicode_urldecode('a%20b%24c') == 'a b$c'
    assert unicode_urldecode('a%20b%26c') == 'a b&c'
    assert unicode_urldecode('a%20b%3Dc') == 'a b=c'
    assert unicode_urldecode('a%20b%2Fc') == 'a b/c'

# Generated at 2022-06-13 12:29:31.518625
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils._text import to_bytes, to_text
    assert unicode_urldecode(None) == ''
    assert unicode_urldecode('') == ''
    assert unicode_urldecode('%02') == '%02'  # illegal hex
    assert unicode_urldecode('%2') == '%2'  # illegal hex
    assert unicode_urldecode('%a') == '%a'  # illegal hex
    assert unicode_urldecode('%') == '%'  # illegal hex
    assert unicode_urldecode('%2a') == '*'
    assert unicode_urldecode('%2A') == '*'
    assert unicode_urldecode('%7E') == '~'
    assert unic

# Generated at 2022-06-13 12:29:35.613372
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'foo%2Fbar') == u'foo/bar'
    assert unicode_urldecode(u'foo%2fbar') == u'foo/bar'



# Generated at 2022-06-13 12:29:43.806130
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()
    assert filters['urldecode'](u'foo+bar%20baz') == u'foo bar baz'
    assert filters['urldecode'](u'foo+bar%20baz') == u'foo bar baz'
    if not HAS_URLENCODE:
        assert filters['urlencode'](u'foo bar baz') == u'foo+bar+baz'
        assert filters['urlencode']({'a': 'foo', 'b': 'bar baz'}) == u'a=foo&b=bar+baz'

# Generated at 2022-06-13 12:29:53.204955
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E2%82%AC%20%2b%20%E2%82%AC') == u'€ + €'
    assert unicode_urldecode('%E2%82%AC%2B%E2%82%AC') == u'€+€'
    assert unicode_urldecode('%E2%82%AC%2b%E2%82%AC') == u'€+€'
    assert unicode_urldecode('%e2%82%ac%20%2B%20%e2%82%ac') == u'€ + €'
    assert unicode_urldecode('%e2%82%ac%2B%e2%82%ac') == u'€+€'

# Generated at 2022-06-13 12:30:00.855853
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    assert unicode_urldecode("%") == u"%"
    assert unicode_urldecode("%0") == u"%0"
    assert unicode_urldecode("%1") == u"%1"
    assert unicode_urldecode("%a") == u"%a"
    assert unicode_urldecode("%A") == u"%A"

    assert unicode_urldecode("%2%2") == u"%%"
    assert unicode_urldecode("%25") == u"%"

    assert unicode_urldecode("%2c") == u","
    assert unicode_urldecode("%3a") == u":"
    assert unicode_urldecode("%3A") == u":"
    assert unicode_urldecode

# Generated at 2022-06-13 12:30:04.010929
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
  module = FilterModule()
  assert module.filters() == { 'urldecode': do_urldecode, 'urlencode': do_urlencode }

# Generated at 2022-06-13 12:30:16.841989
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"my/path") == u"my%2Fpath"
    assert unicode_urlencode(u"my/path", for_qs=True) == u"my%2Fpath"
    assert unicode_urlencode(u"http://www.google.com/search?q=python+URL+encode") == u"http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dpython%2BURL%2Bencode"

# Generated at 2022-06-13 12:30:20.245481
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'dag%3F%3D%3Fwieers%3F%3D%3Fcom') == u'dag?=?wieers?=?com'



# Generated at 2022-06-13 12:30:23.555301
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'one+two+three') == u'one+two+three'
    assert unicode_urldecode(u'one%20two') == u'one two'
    assert unicode_urldecode(u'one+two%20three') == u'one+two three'
    assert unicode_urldecode(b'one+two+three') == u'one+two+three'
    assert unicode_urldecode(b'one%20two') == u'one two'
    assert unicode_urldecode(b'one+two%20three') == u'one+two three'


# Generated at 2022-06-13 12:30:28.942248
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("""%E9%A6%96%E9%A1%B5""") == """首页"""
    assert unicode_urldecode("""Привет мир""") == """Привет мир"""



# Generated at 2022-06-13 12:30:31.883784
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'fake+to+%c3%b6re+%c3%a5%c3%b8re+%c3%a5+%c3%b8') == u'fake to öre åøre å ø'



# Generated at 2022-06-13 12:30:41.670513
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    testcases = [
        # Given, Return
        ('test', 'test'),
        (u'test', u'test'),
        ('%20', u' '),
        ('%2B', u'+'),
        ('%25', u'%'),
        ('a+b', u'a+b'),
        ('a%20b', u'a b'),
        ('%C3%A1+b', u'á b'),
        ('%C3%A1%20b', u'á b'),
    ]

    for given, expected in testcases:
        got = unicode_urldecode(given)
        assert got == expected, "For %s expected %s, got %s" % (given, expected, got)



# Generated at 2022-06-13 12:30:43.804450
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'{}' == unicode_urldecode('%7B%7D')
    assert u'{}' == unicode_urldecode('%7b%7d')



# Generated at 2022-06-13 12:30:46.322284
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"Hello%20There%21") == u"Hello There!"
    assert unicode_urldecode(u"Hello%2BThere%21") == u"Hello+There!"


# Generated at 2022-06-13 12:30:47.391478
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'abc%20def') == 'abc def'



# Generated at 2022-06-13 12:30:49.604961
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ff = FilterModule()
    assert ff is not None
    assert hasattr(ff, 'filters')
    aa = ff.filters()
    assert aa is not None
    # assert len(aa) == 5

# Generated at 2022-06-13 12:31:00.399160
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils.six import StringIO
    fm = FilterModule()
    assert callable(fm.filters)
    out = StringIO()
    basic._ANSIBLE_ARGS = None
    for k,v in fm.filters().items():
        if callable(v):
            basic.ANSIBLE_MODULE_STUB=basic.AnsibleModuleStub({"filter":k},out)
            v()
    basic.ANSIBLE_MODULE_STUB=None
    out.seek(0)

# Generated at 2022-06-13 12:31:03.258087
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'abc%20def') == u'abc def'

# Generated at 2022-06-13 12:31:06.070873
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode'] == do_urldecode

# Generated at 2022-06-13 12:31:15.627765
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import ansible.module_utils.basic
    # We will encode and then decode that string. If we get the same string
    # as result, the function works as expected.
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(u'%3D') == u'='
    assert unicode_urldecode(u'abc%20def') == u'abc def'
    assert unicode_urldecode(u'%26') == u'&'
    assert unicode_urldecode(u'%253D') == u'%3D'
    # Non-ASCII bytes should be left as-is
    assert unicode_urldecode(u'%C3%A4') == u'%C3%A4'

# Generated at 2022-06-13 12:31:30.015758
# Unit test for function do_urlencode
def test_do_urlencode():
    # NOTE: This test should be moved to integration tests with Ansible
    from ansible.utils.unicode import to_unicode
    from ansible.module_utils.six.moves.urllib.parse import urlencode, unquote_plus, quote_plus
    unquoted = to_unicode('a=1&b=2&c=a+b')
    assert unquoted == u'a=1&b=2&c=a+b'
    quoted = quote_plus(unquoted)
    assert quoted == u'a%3D1%26b%3D2%26c%3Da%2Bb'
    unquoted2 = unquote_plus(quoted)
    assert unquoted == unquoted2

# Generated at 2022-06-13 12:31:35.798779
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'FOO%20BAR') == u'FOO BAR'
    assert unicode_urldecode(u'FOO+BAR') == u'FOO BAR'
    assert unicode_urldecode(u'%24') == u'$'


# Generated at 2022-06-13 12:31:42.615670
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'abc') == 'abc'
    assert unicode_urldecode(u'a+a') == 'a a'
    assert unicode_urldecode(u'a%20a') == 'a a'
    assert unicode_urldecode(u'a%20a') == 'a a'
    assert unicode_urldecode(u'a%20a%20a') == 'a a a'


# Generated at 2022-06-13 12:31:51.762638
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys
    import types
    import jinja2

    # Test with an empty FilterModule object
    fm = FilterModule()
    filters = fm.filters()

    # Test all filters
    for name, function in iteritems(filters):
        # Test filter name and function type
        assert isinstance(name, str)
        assert isinstance(function, types.FunctionType)

        # Test filter with no parameters
        try:
            function()
        except Exception as e:
            assert False, "Filter %s() raised an exception: %s" % (name, e)

    # Test urldecode filter with a standard tuple (k, v) item
    assert filters['urldecode']('%5C') == '\\'

    # Test urlencode filter with a non-standard tuple (k, v) item
   

# Generated at 2022-06-13 12:31:58.634558
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test if we have urlencode in jinja2 only when jinja2 supports it
    FilterModule().filters()

    # Test that do_urlencode does basic urlencode
    assert do_urlencode('foo bar') == 'foo%20bar'

    # Test that do_urldecode does basic urldecode
    assert do_urldecode('foo bar') == 'foo bar'



# Generated at 2022-06-13 12:32:06.781967
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("-._~") == "%2D.%5F%7E"
    assert unicode_urlencode("A/Z") == "A%2FZ"
    assert unicode_urlencode("A/Z", for_qs=True) == "A%2FZ"
    assert unicode_urlencode("A/Z?#") == "A%2FZ%3F%23"
    assert unicode_urlencode("A/Z?#", for_qs=True) == "A%2FZ%3F%23"
    assert unicode_urlencode("A/Z? #") == "A%2FZ%3F+%23"

# Generated at 2022-06-13 12:32:28.846835
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import sys

    if sys.version_info < (3,0):
        if PY3 is True:
            assert False, "PY3 is True but it shouldn't be"

        if do_urlencode('http://www.example.com/param1=value1/param2=value2') != 'http%3A//www.example.com/param1%3Dvalue1/param2%3Dvalue2':
            assert False, "Test 1 failed"
    else:
        if PY3 is False:
            assert False, "PY3 is False but it shouldn't be"


# Generated at 2022-06-13 12:32:32.424597
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo%40bar') == 'foo@bar'
    assert unicode_urldecode('foo%2Fbar') == 'foo/bar'


# Generated at 2022-06-13 12:32:35.383324
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Ansible core jinja2 filters - Ansible core jinja2 filters
    # Prepare mocks

    # Invoke method
    result = FilterModule().filters()
    # Check result
    assert isinstance(result, dict)



# Generated at 2022-06-13 12:32:43.399167
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six.moves.urllib.parse import unquote
    import pytest
    # Basic test for urldecode filter
    assert unquote('%C3%A4') == do_urldecode('%C3%A4')
    assert unquote('%20%C3%A4%20') == do_urldecode('%20%C3%A4%20')
    assert unquote('%C3%A4%20') == do_urldecode('%C3%A4%20')
    assert unquote('%C3%A4') == do_urldecode('%C3%A4')
    # No urlencode filter available

# Generated at 2022-06-13 12:32:46.888171
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    filters = module.filters()

    assert filters.get('urldecode') == do_urldecode
    if not HAS_URLENCODE:
        assert filters.get('urlencode') == do_urlencode

# Generated at 2022-06-13 12:32:49.305983
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc+def%2Fghi') == 'abc def/ghi'


# Generated at 2022-06-13 12:32:51.083537
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'foo bar' == unicode_urldecode(b'foo+bar')



# Generated at 2022-06-13 12:32:58.659437
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%2B') == u'+'
    assert unicode_urldecode('%2b') == u'+'
    assert unicode_urldecode('%25') == u'%'
    assert unicode_urldecode('%2F') == u'/'
    assert unicode_urldecode('%2f') == u'/'
    assert unicode_urldecode('%5E') == u'^'
    assert unicode_urldecode('%5E') == u'^'
    assert unicode_urldecode('%5e') == u'^'
    assert unicode_urldecode('%60') == u'`'
    assert unicode_

# Generated at 2022-06-13 12:33:06.642381
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('/a/b/c') == '/a/b/c'
    assert unicode_urldecode('/a/b/c?%F6%E4%FC%C4%D6%DF%2F%2E%5F%2D%21%40%23%24%25%5E%26%2A%28%29') == '/a/b/c?öäüÄÖß/._-!@#$%^&*()'

# Generated at 2022-06-13 12:33:09.929490
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    x = FilterModule()
    assert hasattr(x, 'filters'), "no filters attribute"
    assert isinstance(x.filters, dict), "wrong filters attribute"
    assert 0 < len(x.filters), "empty filters attribute"


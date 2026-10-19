

# Generated at 2022-06-13 12:23:22.084213
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"H%C3%A9l%C3%B3 w%C3%B3rld") == u"Héló wórld"

# Generated at 2022-06-13 12:23:29.110584
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Arrange
    fm = FilterModule()

    # Act
    result = fm.filters()

    # Assert
    assert result is not None, "FilterModule returns result of filters()"
    assert 'urldecode' in result, "urldecode not in filters()"
    assert 'urlencode' in result, "urlencode not in filters()"


# Generated at 2022-06-13 12:23:36.270608
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('ABCD') == 'ABCD'
    assert unicode_urldecode('%41BCD') == 'ABCD'
    assert unicode_urldecode('abcd%E0%B8%99') == u'abcd\u0e99'
    assert unicode_urldecode('abcd%F0%90%8C%BC') == u'abcd\U0001030c'


# Generated at 2022-06-13 12:23:46.908865
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(u'%2525') == u'%%'
    assert unicode_urldecode(u'%00') == u'\x00'
    assert unicode_urldecode(u'%0A') == u'\n'
    assert unicode_urldecode(u'%3F') == u'?'
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(u'a%25b') == u'a%b'
    assert unicode_urldecode(u'a%25b%2B%2Bc') == u'a%b++c'
    assert unicode_urldec

# Generated at 2022-06-13 12:23:49.624121
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%2Bb+%2Bc') == u'a+b ++c'



# Generated at 2022-06-13 12:23:57.801572
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    testcases = [
        {'input': u'\u4f60\u597d',
         'expected': b'%E4%BD%A0%E5%A5%BD'},
        {'input': u'/',
         'expected': b'/%2F'}

    ]

    for testcase in testcases:
        if isinstance(testcase['expected'], bytes):
            assert unicode_urlencode(testcase['input']) == testcase['expected']
        else:
            assert to_text(unicode_urlencode(testcase['input'])) == testcase['expected']



# Generated at 2022-06-13 12:24:07.299631
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' Unit test for method filters of class FilterModule. '''

    import ansible.module_utils.common.unsafe_proxy

    class Mock(object):
        def __init__(self, **kwargs):
            for key, value in iter(kwargs.items()):
                setattr(self, key, value)

    class MockJinja2(object):
        def __init__(self, **kwargs):
            pass

        def urlencode(self, **kwargs):
            pass

    class MockModule_utils_common(object):
        def __init__(self, **kwargs):
            pass

        def unsafe_proxy(self, **kwargs):
            return MockJinja2(**kwargs)

    mock = Mock(unsafe_proxy=MockModule_utils_common())

    obj = FilterModule

# Generated at 2022-06-13 12:24:11.722650
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    assert unicode_urldecode('dag%20wieers') == 'dag wieers'
    assert unicode_urldecode('dag+wieers') == 'dag wieers'
    assert unicode_urldecode('dag%2Bwieers') == 'dag+wieers'

# Generated at 2022-06-13 12:24:22.699886
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert unicode_urldecode(u'http%3A%2F%2Fexample.com%2Fquery%3Fkey%3Dvalue') == u'http://example.com/query?key=value'
    assert unicode_urldecode(u'foo bar') == u'foo bar'
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    if PY3:
        assert unicode_urlencode(u'http://example.com/query?key=value') == u'http%3A%2F%2Fexample.com%2Fquery%3Fkey%3Dvalue'
        assert unicode_urlencode(u'foo bar') == u

# Generated at 2022-06-13 12:24:34.121981
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode(u'http://foo.bar/a[b]c?x=y&x=z') == 'http%3A%2F%2Ffoo.bar%2Fa%5Bb%5Dc%3Fx%3Dy%26x%3Dz'
    assert do_urlencode(u'http://foo.bar/a') == 'http%3A%2F%2Ffoo.bar%2Fa'
    assert do_urlencode(u'http://foo.bar/a/') == 'http%3A%2F%2Ffoo.bar%2Fa%2F'

# Generated at 2022-06-13 12:24:39.131923
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('user=admin&password=admin') == 'user=admin&password=admin'
    assert do_urlencode('user=admin&password=admin') == 'user%3Dadmin%26password%3Dadmin'



# Generated at 2022-06-13 12:24:40.482953
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()

# Generated at 2022-06-13 12:24:53.542284
# Unit test for function do_urlencode
def test_do_urlencode():
    assert 'hello%20world' == unicode_urlencode('hello world')
    assert 'hello%20world' == unicode_urlencode(u'hello world')
    assert 'hello%20world' == unicode_urlencode('hello world', for_qs=True)
    assert 'hello%20world' == unicode_urlencode(u'hello world', for_qs=True)
    assert 'hello%2Bworld' == unicode_urlencode('hello+world', for_qs=True)
    assert 'hello%2Bworld' == unicode_urlencode(u'hello+world', for_qs=True)
    assert 'https%3A%2F%2Fexample.com' == unicode_urlencode('https://example.com', for_qs=False)

# Generated at 2022-06-13 12:24:59.399078
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    class Mock:

        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    fm = FilterModule()
    assert fm.filters() == {u'urldecode': do_urldecode}

    fm = FilterModule(**{u'_ansible_version': Mock(full=u'2.9.9')})
    assert fm.filters() == {u'urldecode': do_urldecode}

    fm = FilterModule(**{u'_ansible_version': Mock(full=u'2.9.0')})
    assert fm.filters() == {u'urldecode': do_urldecode, u'urlencode': do_urlencode}


# Generated at 2022-06-13 12:25:05.803521
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%22%2d%2d%20%2d%2d%20%2d%2d%20%2d%2d%20%2d%2d%22') == u'"-- -- -- -- --"'
    assert unicode_urldecode(b'%22%2d%2d%20%2d%2d%20%2d%2d%20%2d%2d%20%2d%2d%22') == u'"-- -- -- -- --"'



# Generated at 2022-06-13 12:25:16.172249
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'') == u''
    assert unicode_urlencode(u' ') == u'+'
    assert unicode_urlencode(u'hello there') == u'hello+there'
    assert unicode_urlencode(u'/') == u'/'
    assert unicode_urlencode(u'/', for_qs=True) == u'%2F'
    assert unicode_urlencode(u'%') == u'%25'
    assert unicode_urlencode(u'%', for_qs=True) == u'%25'
    assert unicode_urlencode(u'a/b') == u'a/b'
    assert unicode_urlencode(u'a/b', for_qs=True) == u'a%2Fb'

# Generated at 2022-06-13 12:25:20.695267
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if not PY3:
        return
    assert unicode_urlencode("foo") == "foo"
    assert unicode_urlencode("foo bar") == "foo%20bar"
    assert unicode_urlencode("foo bar", for_qs=True) == "foo+bar"

# Generated at 2022-06-13 12:25:24.323169
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3A%2F%2Fwww.w3schools.com%2F%3Fq%3D%26t%3Dp') == u'http://www.w3schools.com/?q=&t=p'



# Generated at 2022-06-13 12:25:30.787707
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    val = u'test'
    assert(unicode_urldecode(val) == val)
    assert(unicode_urldecode(unicode_urlencode(val)) == val)
    assert(unicode_urldecode(unicode_urlencode(u'foo+bar')) == u'foo+bar')
    assert(unicode_urldecode(unicode_urlencode(u'foo bar')) == u'foo bar')
    assert(unicode_urldecode(unicode_urlencode(u'/foo')) == u'/foo')
    assert(unicode_urldecode(unicode_urlencode(u'foo/bar')) == u'foo/bar')


# Generated at 2022-06-13 12:25:45.534576
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('%09%0A%0D%20%21%22%23%24%25%26%27%28%29%2A%2B%2C%2F%3A%3B%3D%3F%40%5B%5D') == to_text(b'\t\n\r !"#$%&\'()*+,/:;=?@[]')
    assert do_urldecode('%26') == '&'
    assert do_urldecode('%26') == '&'
    assert do_urldecode(u'%3D%3D') == u'=='
    assert do_urldecode(u'%3D%3D') == u'=='

# Generated at 2022-06-13 12:25:51.771055
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode']('foo%20bar') == 'foo bar'


# Unit tests for method unicode_urldecode of class FilterModule

# Generated at 2022-06-13 12:25:59.897973
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils.six.moves.urllib.parse import parse_qs, parse_qsl
    from ansible.module_utils.six.moves.urllib.parse import urlencode, urlencode as urlencode_ecma, unquote_plus
    from ansible.module_utils._text import to_bytes, to_text
    import random

    if PY3:
        # The test example is copied from urllib.parse.urlencode() docstring.
        s = 'foo = bar &baz = spam'
        assert unicode_urlencode(s) == 'foo%20%3D%20bar%20%26baz%20%3D%20spam'
        quote_func = quote_plus

# Generated at 2022-06-13 12:26:10.546426
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test unicode_urldecode with normal dictionary
    assert unicode_urldecode('mark%20as%20read%20') == u'mark as read '
    assert unicode_urldecode('hello%2Fworld') == u'hello/world'
    assert unicode_urldecode('hello%2Fworld%2F') == u'hello/world/'
    # Test unicode_urldecode with unicode dictionary
    assert unicode_urldecode(u'%D0%B0%D0%B9%D0%B4%D0%B5%D0%B3%D0%BE%D0%BD') == u'айдегон'

# Generated at 2022-06-13 12:26:16.768184
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('Hello World') == 'Hello%20World'
    assert unicode_urlencode(u'Hello World') == 'Hello%20World'
    assert unicode_urlencode(u'/etc/passwd') == '%2Fetc%2Fpasswd'
    assert unicode_urlencode(b'/etc/passwd') == '%2Fetc%2Fpasswd'
    assert unicode_urlencode((u'/etc/', u'passwd')) == '%2Fetc%2F&passwd'


# Generated at 2022-06-13 12:26:26.314908
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Provide the initial values
    data = {'ifconfig': {'address': '192.168.1.1', 'network': '192.168.1.0'}}
    network = '192.168.1.0'
    filters = FilterModule().filters()
    assert filters['default'](data, 'ttt', 'ttt_default') is 'ttt_default'
    assert filters['default'](data, 'ifconfig', 'ttt_default') == data['ifconfig']
    assert filters['ipaddr'](network, 'netmask', 24) == '255.255.255.0'
    assert filters['ipaddr'](network, 'network') == '192.168.1.0'
    assert filters['ipaddr'](network, 'broadcast') == '192.168.1.255'

# Generated at 2022-06-13 12:26:32.458402
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if not HAS_URLENCODE:
        assert unicode_urlencode('/') == u'/'
        assert unicode_urlencode('/', for_qs=True) == u'%2F'
        assert unicode_urlencode(u'é') == u'%C3%A9'
        assert unicode_urlencode(u'é', for_qs=True) == u'%C3%A9'
        assert unicode_urlencode('foo bar') == u'foo%20bar'
        assert unicode_urlencode('foo bar', for_qs=True) == u'foo+bar'


# Generated at 2022-06-13 12:26:40.538127
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://example.com:80/~foo/') == u'http%3A%2F%2Fexample.com%3A80%2F~foo%2F'
    assert unicode_urlencode(u'föö') == u'f%C3%B6%C3%B6'
    assert unicode_urlencode('föö') == 'f%C3%B6%C3%B6'
    assert unicode_urlencode(u'http://example.com:80/~foo/?a=b&c=d') == u'http%3A%2F%2Fexample.com%3A80%2F~foo%2F%3Fa%3Db%26c%3Dd'

# Generated at 2022-06-13 12:26:43.641111
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_string = u'Dag Wieers'
    assert do_urlencode(test_string) == unicode_urlencode(test_string)

# Generated at 2022-06-13 12:26:56.369662
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    j = basic.AnsibleModule(argument_spec={}).params.copy()

    assert j['urldecode']('foo%2Fbar%3Dbaz') == 'foo/bar=baz'
    assert j['urlencode']('foo/bar=baz') == 'foo%2Fbar%3Dbaz'
    assert j['urlencode']('foo/bar=baz') == 'foo%2Fbar%3Dbaz'

    if PY3:
        assert j['urldecode']('foo%2Fbar%3Dbaz') == 'foo/bar=baz'

# Generated at 2022-06-13 12:27:05.741287
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'abc') == u'abc'
    assert unicode_urlencode(u'abc def') == u'abc%20def'
    assert unicode_urlencode(u'abc+def') == u'abc%2Bdef'
    assert unicode_urlencode(u'abc def', for_qs=True) == u'abc+def'
    assert unicode_urlencode(u'abc+def', for_qs=True) == u'abc%2Bdef'
    assert unicode_urlencode(u'abc/def') == u'abc%2Fdef'
    assert unicode_urlencode(u'abc/def', for_qs=True) == u'abc%2Fdef'
    # Note: Jinja2 filters do_urlencode(dict) and

# Generated at 2022-06-13 12:27:11.187230
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%89') == u'\xc3\x89'
    assert unicode_urldecode('%E9') == u'\xe9'
    assert unicode_urldecode('%E9%80%80') == u'\xe9\u8004'


# Generated at 2022-06-13 12:27:12.466911
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()

# Generated at 2022-06-13 12:27:19.212699
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # urldecode
    assert do_urldecode('%2F') == '/'
    assert do_urldecode('%2Fz') == '/z'
    assert do_urldecode('%2Faz') == '/az'
    assert do_urldecode('2%2Faz') == '2/az'
    assert do_urldecode('%2F%2F') == '//'
    assert do_urldecode('%2F%2Fz') == '//z'
    assert do_urldecode('%2F%2Faz') == '//az'
    assert do_urldecode('%2F%2F2%2Faz') == '//2/az'
    assert do_urldecode('%2F%2F%2F')

# Generated at 2022-06-13 12:27:26.715914
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(b'a%20space') == u'a space'
    assert unicode_urldecode(u'a%20space') == u'a space'
    assert unicode_urldecode(u'%E4%B8%AD%E6%96%87') == u'\u4e2d\u6587'
    assert unicode_urldecode(u'%C3%A4%C3%B6%C3%BC') == u'\u00e4\u00f6\u00fc'
    assert unicode_urldecode(b'%C3%A4%C3%B6%C3%BC') == u'\u00e4\u00f6\u00fc'

# Generated at 2022-06-13 12:27:30.587455
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'Lärm' == unicode_urldecode('L%C3%A4rm')
    assert u'你好' == unicode_urldecode('%E4%BD%A0%E5%A5%BD')


# Generated at 2022-06-13 12:27:36.230278
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import ansible.utils.module_docs as module_docs
    fm = FilterModule()
    assert 'urldecode' in fm.filters()
    assert 'urlencode' in fm.filters()
    assert 'urlencode' == fm.filters()['urlencode'].__name__
    assert 'urldecode' == fm.filters()['urldecode'].__name__
    assert module_docs.get_docstring(FilterModule, method='filters')


# Generated at 2022-06-13 12:27:41.323325
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('dag') == u'dag'
    assert do_urlencode('dag wieers') == u'dag+wieers'
    assert do_urlencode({'name': 'Dag Wieers', 'email': 'dag@wieers.com'}) == u'name=Dag+Wieers&email=dag%40wieers.com'
    assert do_urlencode(['a', 'b', 'c']) == u'a&b&c'
    assert do_urlencode((('a', 'b'), ('c', 'd'))) == u'a=b&c=d'



# Generated at 2022-06-13 12:27:45.724061
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.common.text.render import filter_plugin_filters
    f = FilterModule()
    assert filter_plugin_filters(f)['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filter_plugin_filters(f)['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:27:46.528689
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()

# Generated at 2022-06-13 12:27:52.712125
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    assert module.filters()["urldecode"]("%7e") == "~"
    assert module.filters()["urlencode"]("~") == "%7E"
    assert module.filters()["urlencode"]("~", True) == "%7E"
    assert module.filters()["urlencode"]("~", False) == "%7E"
    assert module.filters()["urlencode"]({"a" : "b", "c" : "d"}) == "a=b&c=d"

# Generated at 2022-06-13 12:28:01.619363
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%2F') == u'/'
    assert unicode_urldecode('%C3%A9') == u'é'

if __name__ == '__main__':
    test_unicode_urldecode()

# Generated at 2022-06-13 12:28:13.220380
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('%20') == '%2520'
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode('/', for_qs=True) == '%2F'
    assert unicode_urlencode('/?') == '%2F%3F'
    assert unicode_urlencode('/=') == '%2F%3D'
    assert unicode_urlencode('%') == '%25'
    assert unicode_urlencode('%', for_qs=True) == '%25'
    assert unicode_urlencode('&') == '%26'
    assert unicode_urlencode('&', for_qs=True) == '%26'

# Generated at 2022-06-13 12:28:18.054425
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    module = FilterModule()
    assert module.filters()['urldecode'] is do_urldecode
    if not HAS_URLENCODE:
        assert module.filters()['urlencode'] is do_urlencode



# Generated at 2022-06-13 12:28:33.136013
# Unit test for method filters of class FilterModule

# Generated at 2022-06-13 12:28:40.065263
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    result = unicode_urlencode('http://www.example.com/path/to/file?a=1&b=2')
    assert result == 'http%3A%2F%2Fwww.example.com%2Fpath%2Fto%2Ffile%3Fa%3D1%26b%3D2'

    result = unicode_urlencode('/hello world/')
    assert result == '%2Fhello%20world%2F'

    result = unicode_urlencode('/hello world/', for_qs=True)
    assert result == '%2Fhello+world%2F'

    result = unicode_urlencode('hello+world')
    assert result == 'hello%2Bworld'

    result = unicode_urlencode('hello+world', for_qs=True)

# Generated at 2022-06-13 12:28:43.864412
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    expected = 'https%3A%2F%2Fgithub.com%2Fdagwieers'
    actual = unicode_urlencode('https://github.com/dagwieers')
    assert expected == actual, (
        'should be able to urlencode unicode string'
        )
    expected = ''
    actual = unicode_urlencode(expected)
    assert expected == actual, (
        'should be able to handle empty string'
        )
    expected = '%25'
    actual = unicode_urlencode(expected)
    assert expected == actual, (
        'should be able to handle specific edgecase'
        )


# Generated at 2022-06-13 12:28:47.408065
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert unicode_urldecode('hello%20world') == u'hello world'
    assert unicode_urlencode(u'hello world') == 'hello+world'
    assert unicode_urlencode(u'hello world', for_qs=True) == 'hello%20world'



# Generated at 2022-06-13 12:28:48.845455
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo%20bar%20') == u'foo bar '



# Generated at 2022-06-13 12:29:00.236289
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import re

    def test_urlencode(value, result):
        assert do_urlencode(value) == result.encode('utf-8'), \
            u"urlencode failed for: '%s'; encoding is %s, got %s instead of %s" % \
            (value, do_urlencode(value), type(do_urlencode(value)), type(result))

        assert re.match(r'.*%2(F|D).*', do_urlencode(value)), \
            "urlencode failed to urlencode space character"

    tests = ['test 1', 'test 2', 'test 3', 'test 4', 'test 5', 'test 6']
    test_urlencode(tests, 'test+1&test+2&test+3&test+4&test+5&test+6')

# Generated at 2022-06-13 12:29:10.375674
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_native
    assert unicode_urlencode("foo bar") == u'foo%20bar'
    assert unicode_urlencode("a&b", for_qs=True) == u'a%26b'
    assert unicode_urlencode("a&b") == u'a%26b'
    assert unicode_urlencode("a?b") == u'a%3Fb'
    assert unicode_urlencode("a=b") == u'a%3Db'
    assert unicode_urlencode("a=b", for_qs=True) == u'a%3Db'
    assert unicode_urlencode("a?b", for_qs=True) == u'a%3Fb'

# Generated at 2022-06-13 12:29:24.492799
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%21') == u'!'
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(u'%7e') == u'~'
    assert unicode_urldecode(u'a%20space') == u'a space'
    assert unicode_urldecode(u'a%20%21%25%7e') == u'a !%~'
    assert unicode_urldecode(u'a+space') == u'a space'
    assert unicode_urldecode(u'a+%21+%25+%7e') == u'a !%~'
    assert unicode

# Generated at 2022-06-13 12:29:31.601031
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import unittest

    # Test the urlencode module-level functions
    class TestUrlEncode(unittest.TestCase):
        # pylint: disable=invalid-name
        def test_unicode_urlencode(self):
            self.assertEqual(unicode_urlencode('abcd'), 'abcd')
            self.assertEqual(unicode_urlencode('/abcd'), '/abcd')
            self.assertEqual(unicode_urlencode('/abcd/'), '/abcd/')
            self.assertEqual(unicode_urlencode('/abcd/e'), '/abcd/e')
            self.assertEqual(unicode_urlencode('/abcd/e/'), '/abcd/e/')

            # Characters that require urlencoding

# Generated at 2022-06-13 12:29:33.371203
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters() == {'urldecode': do_urldecode}



# Generated at 2022-06-13 12:29:43.846824
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus, quote_plus

    # initializing FilterModule class
    f = FilterModule()
    # calling its filters method() to get the dict
    # of the jinja2 filters
    filters = f.filters()

    assert filters is not None
    assert 'urldecode' in filters
    if PY3:
        assert filters['urldecode'] == unquote_plus
    else:
        assert filters['urldecode'] == to_text(unquote_plus(to_bytes('')))

    if not HAS_URLENCODE:
        assert filters['urlencode'] == to

# Generated at 2022-06-13 12:29:47.450330
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()

    if HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

    assert filters['urldecode'] == do_urldecode

# Generated at 2022-06-13 12:29:50.042947
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3a%2f%2fexample.com%2f') == u'http://example.com/'


# Generated at 2022-06-13 12:29:54.879338
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus
    import ansible.module_utils.core as core_utils

    fm = core_utils.FilterModule()

    for key, value in fm.filters().items():
        if key == 'urldecode':
            assert isinstance(value, type(unquote_plus))
        elif key == 'urlencode':
            assert isinstance(value, type(quote_plus))
        else:
            raise ValueError

# Generated at 2022-06-13 12:29:58.441587
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"hello%2C%20world") == u"hello, world"
    assert unicode_urldecode("hello%2C%20world") == u"hello, world"
    assert unicode_urldecode("hello%2C%20world") == u"hello, world"


# Generated at 2022-06-13 12:29:59.993443
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc+-A%25D1') == u'abc+-A%D1'


# Generated at 2022-06-13 12:30:01.443908
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = 'foo+bar'
    result = unicode_urldecode(string)
    assert result == u'foo bar'



# Generated at 2022-06-13 12:30:08.195085
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo%2F%3D%2B%2Bbar') == u'foo/=++bar'
    assert unicode_urldecode(u'foo%C3%BCbar') == u'fooübar'

# Generated at 2022-06-13 12:30:09.725725
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''FilterModule.filters()'''
    assert FilterModule().filters()


# Generated at 2022-06-13 12:30:13.439933
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'abc') == u'abc'

    assert unicode_urlencode(u'abc?efg') == u'abc%3Fefg'
    assert unicode_urlencode(u'abc/efg') == u'abc/efg'

    assert unicode_urlencode(u'abc?efg', for_qs=True) == u'abc%3Fefg'
    assert unicode_urlencode(u'abc/efg', for_qs=True) == u'abc%2Fefg'


# Generated at 2022-06-13 12:30:17.886927
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = b'http%3A%2F%2Fdelicious.com%2Fwp%2F%25B2%25A8%25B2%25B6'
    assert unicode_urldecode(string) == u'http://delicious.com/wp/\u2026'


# Generated at 2022-06-13 12:30:20.882556
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%E2%80%99') == u'’'


# Generated at 2022-06-13 12:30:23.768507
# Unit test for function do_urlencode

# Generated at 2022-06-13 12:30:35.690474
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    basic._ANSIBLE_ARGS = None
    assert unicode_urldecode(u'a%2Fb') == 'a/b'
    if PY3:
        assert unicode_urldecode(u'a%2Fb') == 'a/b'
        assert unicode_urldecode(b'a%2Fb') == 'a/b'
        assert unicode_urldecode(b'a%2Fb'.decode('utf-8')) == 'a/b'
        assert unicode_urldecode(b'a%2Fb'.decode('utf-8')) == 'a/b'

# Generated at 2022-06-13 12:30:43.002295
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # No decoding needed
    assert unicode_urldecode(u'foo') == u'foo'

    # Standard decoding
    assert unicode_urldecode(u'foo%40bar') == u'foo@bar'

    # Unicode decoding
    assert unicode_urldecode(u'foo%C3%A9') == u'fooé'

    # Mixed-case decoding
    assert unicode_urldecode(u'foo%C3%A9') == u'fooé'
    assert unicode_urldecode(u'foo%c3%a9') == u'fooé'



# Generated at 2022-06-13 12:30:44.976385
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = b'J%C3%BAlkaus%5C'
    assert unicode_urldecode(string) == u'J\u00fclkaus\\'


# Generated at 2022-06-13 12:30:50.814139
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:30:57.920109
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()

    assert fm.filters()['urldecode']('U2VuZGZsYXZl') == 'Sendflare'
    assert fm.filters()['urldecode']('W3sjIGFuc3dlcnMvZGVsZXRlX2Fuc3dlcl9lc3RhdHVzIH19ID0gc3RhdHVz') == '{{ answers/delete_answer_estatus }} = status'

# Generated at 2022-06-13 12:31:01.480916
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('`') == '%60'


# Generated at 2022-06-13 12:31:08.234738
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3a%2f%2fwww.example.com%2f') == u'http://www.example.com/'
    assert unicode_urldecode(b'http%3a%2f%2fwww.example.com%2f') == u'http://www.example.com/'
    assert unicode_urldecode('http%3a%2f%2fwww.example.com%2f') == u'http://www.example.com/'


# Generated at 2022-06-13 12:31:13.583413
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert "%2F" == unicode_urldecode("%252F")
    assert "/" == unicode_urldecode("%252F")
    assert "!" == unicode_urldecode("!")
    assert "!" == unicode_urldecode("%21")
    assert "%2F" == unicode_urldecode("%2F")

# Generated at 2022-06-13 12:31:21.079244
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_bytes
    to_bytes_utf8 = lambda x, y=None: to_bytes(x, encoding='utf-8')

# Generated at 2022-06-13 12:31:31.227934
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """Test functionality of FilterModule method filters
    """
    from ansible.module_utils.six import StringIO

    output = StringIO()

    f = FilterModule()
    assert(f.filters().keys() == ['urldecode'])

    if HAS_URLENCODE:
        assert(u"%2Fpath%2Fto%2Fresource" == f.filters()['urldecode'](u"%2Fpath%2Fto%2Fresource"))
        assert(u"/path/to/resource" == f.filters()['urldecode'](u"/path/to/resource"))

# Generated at 2022-06-13 12:31:35.937153
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a') == u'a'
    assert unicode_urldecode('+') == u' '
    assert unicode_urldecode('%2B') == u'+'
    assert unicode_urldecode(to_bytes('%2B')) == u'+'


# Generated at 2022-06-13 12:31:47.069538
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys
    import platform
    import pytest
    from ansible.module_utils.six import PY3, StringIO
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils.six.moves.urllib.parse import quote_plus
    #from ansible.module_utils.six.moves.urllib.parse import quote
    if PY3:
        builtins_module = 'builtins'
    else:
        builtins_module = '__builtin__'
    sys.modules['ansible.module_utils.six'].builtins_module = builtins_module

    def Mock_iteritems(d):
        return iter(d.items())

    def Mock_iter(o):
        return iter(o)


# Generated at 2022-06-13 12:31:54.364023
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    assert do_urldecode('abc%20def') == 'abc def'
    assert do_urldecode('%40%40') == u'@@'

    urlencode_result = 'full%20urlencoded%20string'
    assert do_urlencode('full urlencoded string') == urlencode_result
    assert do_urlencode('full urlencoded string') == 'full%20urlencoded%20string'
    assert do_urlencode(b'full urlencoded string') == urlencode_result
    assert do_urlencode({'k1': 'v1', 'k2': 'v2'}) == 'k1=v1&k2=v2'
    assert  do_urlencode('/path?query=string') == '/path%3Fquery%3Dstring'


# Generated at 2022-06-13 12:32:05.541068
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20%21%22%23') == ' !"#'
    assert unicode_urldecode('%2f%2F%2c') == '//,'
    assert unicode_urldecode('%2F%2F%2C') == '//,'
    assert unicode_urldecode(u'%2F%2F%2C') == '//,'
    assert unicode_urldecode(u'%2f%2F%2c') == '//,'
    assert unicode_urldecode(u'%2F%2F%2C') == '//,'
    assert unicode_urldecode(u'%2f%2F%2c') == '//,'

# Generated at 2022-06-13 12:32:12.779900
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()

    assert 'urldecode' in filters
    assert 'urlencode' in filters

# Generated at 2022-06-13 12:32:16.343627
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    data = dict(
        abc='def ghi',
        jkl='mno pqr',
    )

    result = unicode_urlencode(data)
    if result != 'abc=def%20ghi&jkl=mno%20pqr':
        raise AssertionError("Encoding of %s failed. Got: %s" % (data, result))



# Generated at 2022-06-13 12:32:20.624687
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filter_methods = fm.filters()

    assert filter_methods['urldecode'] == do_urldecode
    assert filter_methods['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:32:25.716884
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    # TODO: This needs to be test_FilterModule_filters_urldecode
    #       Also: put this in a TestCase class
    assert fm.filters()['urldecode']('1+1%3D%3D2') == '1+1==2'



# Generated at 2022-06-13 12:32:35.646434
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo') == b'foo'
    assert unicode_urlencode(b'foo') == b'foo'
    assert unicode_urlencode(u'/foo') == b'/foo'
    assert unicode_urlencode(b'/foo') == b'/foo'
    assert unicode_urlencode(u'foo bar') == b'foo%20bar'
    assert unicode_urlencode(b'foo bar') == b'foo%20bar'
    assert unicode_urlencode(u'/foo bar') == b'/foo%20bar'
    assert unicode_urlencode(b'/foo bar') == b'/foo%20bar'
    assert unicode_urlencode(u'foo+bar') == b'foo+bar'
    assert unicode_urlencode

# Generated at 2022-06-13 12:32:39.709520
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo+space') == u'foo space'
    assert unicode_urldecode(u'foo%20space') == u'foo space'
    assert unicode_urldecode(u'foo%2520space') == u'foo%20space'


# Generated at 2022-06-13 12:32:43.743338
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%E6%B1%89%E5%AD%97") == "汉字"



# Generated at 2022-06-13 12:32:51.821881
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode('foo') == 'foo'
    assert unicode_urldecode(u'B%C3%A6') == u'B\xc3\xa6'
    assert unicode_urldecode('B%C3%A6') == u'B\xc3\xa6'
    assert unicode_urldecode(u'%f0%9f%8d%b2') == u'\U0001f35a'
    assert unicode_urldecode('%f0%9f%8d%b2') == u'\U0001f35a'

# Generated at 2022-06-13 12:32:55.087518
# Unit test for function do_urlencode
def test_do_urlencode():
    def test(value, expected):
        actual = do_urlencode(value)
        assert actual == expected, ('%r != %r (expected)' % (actual, expected))
    test('string', 'string')
    test('/string', '%2Fstring')
    test(['list of strings'], 'list+of+strings')
    test({'foo': 'bar'}, 'foo=bar')
    test({'foo': 'bar', 'baz': 'bax'}, 'foo=bar&baz=bax')


# Generated at 2022-06-13 12:33:04.442258
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    t = FilterModule()

    filters = [
        'urldecode',
    ]

    if not HAS_URLENCODE:
        filters.append('urlencode')

    expected_filters = {}
    first_filter_name = None
    for filter_name in filters:
        expected_filters[filter_name] = getattr(t.filters(), filter_name)
        if first_filter_name is None:
            first_filter_name = filter_name

    actual_filters = t.filters()
    assert len(expected_filters) == len(actual_filters)
    assert expected_filters[first_filter_name] == actual_filters[first_filter_name]

# Generated at 2022-06-13 12:33:14.026532
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E4%B8%AD%E6%96%87') == u'\u4e2d\u6587'
    assert unicode_urldecode('%C3%9C') == u'\xdc'


# Generated at 2022-06-13 12:33:23.212752
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%21%2B%2A%7E%40%23%24%25%5E%26%2A%28%29') == u'!+*~@#%24%25^&*()'
    assert unicode_urldecode(u'%21%2B%2A%7E%40%23%24%25%5E%26%2A%28%29'.encode('utf-8')) == u'!+*~@#%24%25^&*()'
    assert unicode_urldecode('%21%2B%2A%7E%40%23%24%25%5E%26%2A%28%29') == u'!+*~@#%24%25^&*()'

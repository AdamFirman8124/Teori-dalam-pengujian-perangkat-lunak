

# Generated at 2022-06-13 12:23:25.340627
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_ = FilterModule()
    filters = filter_.filters()

    assert filters.get('urldecode') == do_urldecode
    assert filters.get('urlencode') == do_urlencode

# Generated at 2022-06-13 12:23:35.413698
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()

    assert filters['urldecode'](u'Hello%20World') == u'Hello World'
    assert filters['urldecode'](u'Hello World') == u'Hello World'
    assert filters['urldecode'](u'Hello%20%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82') == u'Hello Привет'

    if not HAS_URLENCODE:
        assert filters['urlencode'](u'Hello World') == u'Hello%20World'

# Generated at 2022-06-13 12:23:39.275009
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    assert module.filters()['urldecode']('%20') == ' '
    assert module.filters()['urldecode']('%3D') == '='
    assert module.filters()['urldecode']('%2B') == '+'



# Generated at 2022-06-13 12:23:45.433800
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('a%20%3A%3D%3F%40%26%3D%2B') == 'a :=?@&=+'
    else:
        assert unicode_urldecode('a%20%3A%3D%3F%40%26%3D%2B') == u'a :=?@&=+'



# Generated at 2022-06-13 12:23:56.016040
# Unit test for function do_urlencode
def test_do_urlencode():
    # Basic test
    assert do_urlencode('http://example.com/test?this=that') == u'http%3A%2F%2Fexample.com%2Ftest%3Fthis%3Dthat'

    # Test iterable
    assert do_urlencode(['foo', 'bar']) == u'foo&bar'
    assert do_urlencode(['foo', 'bar', 'baz']) == u'foo&bar&baz'
    assert do_urlencode(['foo', 'bar', 'baz', 'one', 'two']) == u'foo&bar&baz&one&two'

    # Test dictionary
    assert do_urlencode({'foo': 'this'}) == u'foo=this'

# Generated at 2022-06-13 12:23:57.896176
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fixture = FilterModule()
    assert fixture.filters() == {'urldecode': do_urldecode}

# Generated at 2022-06-13 12:24:01.374498
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%C3%A9') == 'aé'
    assert unicode_urldecode('%3F') == '?'

# Unit tests for function unicode_urlencode

# Generated at 2022-06-13 12:24:09.639602
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Sourced from https://docs.python.org/2/library/urllib.html#url-quoting
    assert unicode_urldecode(u'http://www.example.com/~user/%7Efoobar/') == u'http://www.example.com/~user/~foobar/'
    assert unicode_urldecode(u'http://www.example.com/%7Euser/~foobar/') == u'http://www.example.com/~user/~foobar/'
    assert unicode_urldecode(u'http://www.example.com/%7euser/~foobar/') == u'http://www.example.com/~user/~foobar/'


# Generated at 2022-06-13 12:24:19.141290
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import urllib
    pure_ascii_string = 'qwertyuiop1234567890'
    encoded = urllib.quote_plus(pure_ascii_string)
    assert unicode_urldecode(encoded) == pure_ascii_string

    unicode_string = u'йцукенгшщзхъфывапролджэячсмитьбю'
    encoded = urllib.quote_plus(unicode_string.encode('utf-8'))
    assert unicode_urldecode(encoded) == unicode_string


# Generated at 2022-06-13 12:24:28.026283
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:24:38.667399
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert '⠊' == unicode_urldecode('%E2%A0%8A'), u'urldecode filtering %E2%A0%8A (from Jinja2 test, in the Unicode encoding section) failed'
    assert '’' == unicode_urldecode('%E2%80%99'), u'urldecode filtering %E2%80%99 (from Jinja2 test, in the Unicode encoding section) failed'
    assert '?' == unicode_urldecode('%3F'), u'urldecode filtering %3F (from Jinja2 test, in the percent encoding section) failed'
    assert '?' == unicode_urldecode('%3f'), u'urldecode filtering %3f (from Jinja2 test, in the percent encoding section) failed'

# Generated at 2022-06-13 12:24:41.383226
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' Unit test for method filters of class FilterModule '''
    assert FilterModule().filters() is not None

# Generated at 2022-06-13 12:24:44.108112
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%2ftest%2b') == u'/test+'


# Generated at 2022-06-13 12:24:50.241966
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A5') == u'\xe5'
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode(u'%20') == u' '


# Generated at 2022-06-13 12:24:53.645000
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    _FilterModule = FilterModule()
    assert hasattr(_FilterModule, 'filters')
    assert callable(_FilterModule.filters)
    assert isinstance(_FilterModule.filters(), dict)


# Generated at 2022-06-13 12:24:57.135383
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # The encoded string '%E5%B0%8F%E7%B1%B38' is UTF-8 encoded and
    # decodes to '小米8'
    string = u'%E5%B0%8F%E7%B1%B38'
    decoded = unicode_urldecode(string)
    assert decoded == u'小米8'



# Generated at 2022-06-13 12:24:59.183553
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo%2Fbar') == 'foo/bar'



# Generated at 2022-06-13 12:25:07.095778
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('https%3A%2F%2Fwww.w3schools.com%2Ftags%2Fref_urlencode.asp') == 'https://www.w3schools.com/tags/ref_urlencode.asp'
    assert do_urlencode('https://www.w3schools.com/tags/ref_urlencode.asp') == 'https%3A%2F%2Fwww.w3schools.com%2Ftags%2Fref_urlencode.asp'
    assert do_urlencode('{"fname":"John","lname":"Doe"}') == 'fname=John&lname=Doe'

# Generated at 2022-06-13 12:25:12.948119
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%2C') == ','
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%41') == 'A'
    assert unicode_urldecode('%A1') == u'\u00a1'
    assert unicode_urldecode(u'%A1') == u'\u00a1'


# Generated at 2022-06-13 12:25:16.168669
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/test%') == '%2Ftest%25'
    assert unicode_urlencode('/test%', for_qs=True) == '%2Ftest%25'

# Generated at 2022-06-13 12:25:23.114150
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' FilterModule filters() returns dict of filters '''
    fm = FilterModule()
    result = fm.filters()
    assert 'urldecode' in result
    assert result['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert 'urlencode' in result
        assert result['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:25:24.843332
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E4%B8%AD%E6%96%87') == u'中文'



# Generated at 2022-06-13 12:25:28.858562
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'foo+%2B+bar') == u'foo ++ bar'
    assert unicode_urldecode(u'foo%2B%2Bbar') == u'foo++bar'


# Generated at 2022-06-13 12:25:35.798935
# Unit test for function do_urlencode
def test_do_urlencode():
    """Test the function do_urlencode"""

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # test: encode a string
    assert do_urlencode('x') == u'x'
    assert do_urlencode(u'x') == u'x'
    assert do_urlencode(b'x') == u'x'
    assert do_urlencode(u' ') == u'+'
    assert do_urlencode(b' ') == u'+'
    assert do_urlencode(u'+') == u'%2B'
    assert do_urlencode(b'+') == u'%2B'
    assert do_urlencode(u'&') == u'%26'
    assert do_urlencode(b'&') == u

# Generated at 2022-06-13 12:25:46.274630
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/~me/') == u'/~me/'
    assert unicode_urlencode('éà') == u'%C3%A9%C3%A0'
    assert unicode_urlencode('äß') == u'%C3%A4%C3%9F'
    assert unicode_urlencode('\u2013') == u'%E2%80%93'
    assert unicode_urlencode('/~me/?my=áà&your=ß') == u'/~me/?my=%C3%A1%C3%A0&your=%C3%9F'


# Generated at 2022-06-13 12:25:59.215491
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo') == u'foo'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo bar', True) == u'foo+bar'
    assert unicode_urlencode(u'foo/bar') == u'foo%2Fbar'
    assert unicode_urlencode(u'foo/bar', True) == u'foo%2Fbar'
    assert unicode_urlencode(u'foo,bar') == u'foo,bar'
    assert unicode_urlencode(u'foo,bar', True) == u'foo%2Cbar'


# Generated at 2022-06-13 12:26:04.415503
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'foo[bar]=baz' == unicode_urldecode('foo%5Bbar%5D=baz')
    assert u'foo%5Bbar%5D=baz' == unicode_urldecode('foo%255Bbar%255D=baz')
    assert u'foo[bar]%3Dbaz' == unicode_urldecode('foo%5Bbar%5D%3Dbaz')
    assert u'foo%3Dbar' == unicode_urldecode('foo%3Dbar')
    assert u'foo%3dbar' == unicode_urldecode('foo%3dbar')

# Generated at 2022-06-13 12:26:12.246303
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == u'test'
    assert unicode_urlencode('test test') == u'test%20test'
    assert unicode_urlencode('test+test') == u'test%2Btest'
    assert unicode_urlencode('/test/test/') == u'/test/test/'
    assert unicode_urlencode('/test/test+/') == u'/test/test+/'
    assert unicode_urlencode(u'/test/test/') == u'/test/test/'
    assert unicode_urlencode(u'/test/test+/') == u'/test/test+/'
    assert unicode_urlencode(u'test') == u'test'

# Generated at 2022-06-13 12:26:15.446776
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%2F') == u'/'
    assert unicode_urldecode(u'%40') == u'@'


# Generated at 2022-06-13 12:26:24.553113
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("http://my.url/?x=1&y=2/a=3") == u'http%3A//my.url/%3Fx%3D1%26y%3D2%2Fa%3D3'
    assert unicode_urlencode("http://my.url/?x=1&y=2/a=3", for_qs=True) == u'http%3A%2F%2Fmy.url%2F%3Fx%3D1%26y%3D2%2Fa%3D3'

    # We have to set these values as bytes in python2 as we
    # always get back unicode strings
    assert unicode_urlencode(b"\xc3\xa9") == u'%C3%A9'
    assert unicode_url

# Generated at 2022-06-13 12:26:30.988785
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    expected_result = 'https%3A%2F%2Fwww.example.com'
    assert expected_result == filter_module.filters()['urlencode']('https://www.example.com')

# Generated at 2022-06-13 12:26:39.320514
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_bytes, to_text
    import sys
    import pytest

    # Unicode strings
    if sys.version_info[0] > 2:
        string = 'https://www.example.com/api/v1/cmdb/network/vlan/1/'
        true_result = 'https%3A%2F%2Fwww.example.com%2Fapi%2Fv1%2Fcmdb%2Fnetwork%2Fvlan%2F1%2F'
        if string == unicode_urlencode(string) and true_result == unicode_urlencode(string, for_qs=True):
            assert True
        else:
            assert False

    # Bytearrays

# Generated at 2022-06-13 12:26:47.354047
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'Hello\nWorld') == u'Hello%0AWorld'
    assert unicode_urlencode(u'Hello\nWorld', for_qs=True) == u'Hello%0AWorld'
    assert unicode_urlencode(u'Hello\nWorld ', for_qs=True) == u'Hello%0AWorld+'
    assert unicode_urlencode(u'Hello\nWorld/', for_qs=True) == u'Hello%0AWorld%2F'
    assert unicode_urlencode(u'Hello\nWorld/ ', for_qs=True) == u'Hello%0AWorld%2F+'

# Generated at 2022-06-13 12:26:54.943555
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if not HAS_URLENCODE:
        assert unicode_urlencode('foo bar') == 'foo%20bar'
        assert unicode_urlencode('foo bar', for_qs=True) == 'foo%20bar'
        assert unicode_urlencode(unicode('foo bar', 'utf-8')) == 'foo%20bar'
        assert unicode_urlencode(u'foo bar 中文') == 'foo%20bar%20%E4%B8%AD%E6%96%87'
        assert unicode_urlencode(u'foo bar 中文', for_qs=True) == 'foo%20bar%20%E4%B8%AD%E6%96%87'


# Generated at 2022-06-13 12:27:05.087971
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import jinja2
    # With Python 2, the Jinja2 default for autoescape is False
    env = jinja2.Environment(autoescape=True)
    test = u'https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html'
    assert unicode_urlencode(test) == u'https%3A//docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html'
    assert unicode_urlencode(test, for_qs=True) == u'https%3A%2F%2Fdocs.ansible.com%2Fansible%2Flatest%2Fuser_guide%2Fplaybooks_filters.html'

# Generated at 2022-06-13 12:27:06.090259
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    FilterModule = __import__('FilterModule').FilterModule
    assert FilterModule.filters(FilterModule) is not None

# Generated at 2022-06-13 12:27:09.239573
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('http%3A%2F%2Fwww.ansible.com%2F') == 'http://www.ansible.com/'



# Generated at 2022-06-13 12:27:18.376766
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import sys
    if PY3:
        return
    if sys.version_info < (2, 6):
        return
    assert unicode_urlencode('føø') == 'f%C3%B8%C3%B8'
    assert unicode_urlencode(u'føø') == 'f%C3%B8%C3%B8'
    assert unicode_urlencode('føø') == unicode_urlencode(u'føø')
    assert unicode_urlencode('føø', for_qs=True) == 'f%C3%B8%C3%B8'


# Generated at 2022-06-13 12:27:22.343230
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7B%22name%22%3A%20%22joe%22%2C%20%22age%22%3A%2020%7D') == '{"name": "joe", "age":  20}'



# Generated at 2022-06-13 12:27:32.080386
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%E0%A4%B5%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%82%E0%A4%97') == u'वीडिंग'
    assert unicode_urldecode(u'vimium%20%E2%9C%93') == u'vimium ✓'
    assert unicode_urldecode(u'%E2%9C%93%20vimium') == u'✓ vimium'
    assert unicode_urldecode(u'test%2B+%2Btest') == u'test+ ++test'


# Generated at 2022-06-13 12:27:37.459992
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'foo%2B') == u'foo+'


# Generated at 2022-06-13 12:27:47.607894
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert to_text(type(unicode_urlencode(u'@'))) is to_text(type(to_bytes()))
    assert unicode_urlencode(u'@') == u'@'
    assert unicode_urlencode(u'@/') == u'@%2F'
    assert unicode_urlencode(u'@', for_qs=True) == u'@'
    assert unicode_urlencode(u'@/', for_qs=True) == u'@%2F'
    assert unicode_urlencode(u'a=a') == u'a%3Da'
    assert unicode_urlencode(u'a=a', for_qs=True) == u'a%3Da'
    assert unicode_urlencode(u'@%2F')

# Generated at 2022-06-13 12:27:55.173926
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(None) == 'None'
    assert unicode_urlencode(True) == 'True'
    assert unicode_urlencode(False) == 'False'
    assert unicode_urlencode(42) == '42'
    assert unicode_urlencode('\n') == '%0A'
    assert unicode_urlencode(' foo bar ') == '+foo+bar+'
    assert unicode_urlencode('/foo/bar/') == '%2Ffoo%2Fbar%2F'
    assert unicode_urlencode({'foo': 'bar', 'baz': '42'}) == 'foo=bar&baz=42'

    # Test that a list cannot be iterated.

# Generated at 2022-06-13 12:27:56.140358
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()

# Generated at 2022-06-13 12:28:04.804543
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'abc' == unicode_urldecode('abc')
    assert u'abc def' == unicode_urldecode('abc%20def')
    assert u'abc def' == unicode_urldecode('abc+def')
    assert u'åéîöü' == unicode_urldecode('%C3%A5%C3%A9%C3%AE%C3%B6%C3%BC')


# Generated at 2022-06-13 12:28:06.066126
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters() is not None

# Generated at 2022-06-13 12:28:14.828004
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'dag%2bwieers') == 'dag%252bwieers'
    assert unicode_urlencode(u'http://localhost/a b') == 'http%3A//localhost/a%20b'
    assert unicode_urlencode(u'http://localhost/a b', for_qs=True) == 'http%3A%2F%2Flocalhost%2Fa+b'
    assert unicode_urlencode(u'http://localhost/a b', for_qs=True) == 'http%3A%2F%2Flocalhost%2Fa+b'

# Generated at 2022-06-13 12:28:21.175600
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%E4%B8%AD%E6%96%87') == u'中文'
    assert unicode_urldecode(u'%E4%B8%AD%26%E6%96%87') == u'中&文'
    assert unicode_urldecode(u'%E4%B8%AD%2B%E6%96%87') == u'中+文'
    assert unicode_urldecode(u'%E4%B8%AD%2E%E6%96%87') == u'中.文'



# Generated at 2022-06-13 12:28:21.671370
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    pass

# Generated at 2022-06-13 12:28:27.979790
# Unit test for function do_urlencode
def test_do_urlencode():
    lst = ['foo', 'bar', 'baz', 'do it!']
    lst_expected = 'foo&bar&baz&do+it%21'
    lst_result = do_urlencode(lst)
    assert lst_result == lst_expected
    
    dct = {'foo': 'bar', 'baz': 42}
    dct_expected = 'baz=42&foo=bar'
    dct_result = do_urlencode(dct)
    assert dct_result == dct_expected

# Generated at 2022-06-13 12:28:38.592940
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' Filters can be loaded and used'''

    FILTERMODULE = FilterModule()
    filters = FILTERMODULE.filters()
    assert len(filters) > 0, "No filters defined"
    assert len(filters) == 2 or len(filters) == 3, "Filters defined has wrong amount of keys"
    assert 'urldecode' in filters, "urldecode filter missing"
    assert filters['urldecode'] == do_urldecode, "urldecode filter has wrong value"
    assert 'urlencode' in filters, "urlencode filter missing"
    assert filters['urlencode'] == do_urlencode or filters['urlencode'] == do_urlencode,\
        "urlencode filter has wrong value"



# Generated at 2022-06-13 12:28:46.113849
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test = [
        ('a%20b+c%20d', u'a b c d'),
        ('aYbYcYd', u'aYbYcYd'),
    ]
    for (test_input, test_output) in test:
        assert unicode_urldecode(test_input) == test_output, \
            u"unicode_urldecode() test failed for '{0}': expected '{1}', got '{2}'".format(test_input, test_output, unicode_urldecode(test_input))


# Generated at 2022-06-13 12:28:48.678389
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()["urldecode"](u"an%3Fd") == u"an?d"
    assert FilterModule().filters()["urlencode"](u"an?d") == u"an%3Fd"



# Generated at 2022-06-13 12:28:56.360873
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # make sure we get a dict back from filters
    filters = FilterModule().filters()
    assert isinstance(filters, dict)

    # make sure all the filters were loaded
    assert filters['urldecode'] == do_urldecode

    # make sure that urlencode is present when Jinja2 is old
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:28:58.387389
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Hello%20World') == 'Hello World'
    assert unicode_urldecode('Hello+World') == 'Hello World'


# Generated at 2022-06-13 12:29:03.467584
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo%00bar') == u'foo\x00bar'
    assert unicode_urldecode(u'foo%0Abar') == u'foo\nbar'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'foo%2Bbar') == u'foo+bar'
    assert unicode_urldecode(u'%242%2C500') == u'$2,500'


# Generated at 2022-06-13 12:29:09.588411
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if not PY3:
        assert unicode_urldecode('%AD') == to_text('\xb4')
        assert unicode_urldecode('%C3%A9') == to_text('\xc3\xa9')
    assert unicode_urldecode('%2F') == '/'

# Generated at 2022-06-13 12:29:12.838401
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # urldecode fails with trailing + and no padding
    assert unicode_urldecode(u'%00') == u'\x00'
    assert unicode_urldecode(u'%2B') == u'+'



# Generated at 2022-06-13 12:29:24.261749
# Unit test for function do_urlencode
def test_do_urlencode():
    from ansible.utils import jsonify
    from ansible.module_utils import basic

    test_cases = [{
        'input_string': {'a': 1, 'b': 2},
        'expected_string': u'a=1&b=2',
    }, {
        'input_string': {'a': 1, 'b': [1, 2, 3]},
        'expected_string': u'a=1&b=1%2C+2%2C+3',
    }, {
        'input_string': 'abc',
        'expected_string': u'abc',
    }, {
        'input_string': u'abà',
        'expected_string': u'ab%C3%A0',
    }]

    for test_case in test_cases:
        result = do_urlen

# Generated at 2022-06-13 12:29:31.474208
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://example.com/') == u'http%3A//example.com/'
    assert unicode_urlencode('http://example.com/', for_qs=True) == u'http%3A%2F%2Fexample.com%2F'
    assert unicode_urlencode('example.com') == u'example.com'
    assert unicode_urlencode(u'example.com') == u'example.com'
    assert unicode_urlencode(u'http://example.com/') == u'http%3A//example.com/'
    assert unicode_urlencode(u'http://example.com/', for_qs=True) == u'http%3A%2F%2Fexample.com%2F'

# Generated at 2022-06-13 12:29:40.186900
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'dag%20wieers' == unicode_urldecode('dag%20wieers')


# Generated at 2022-06-13 12:29:47.160318
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test_string = 'test string'
    assert unicode_urldecode(test_string) == test_string
    test_string = 'test%20string'
    assert unicode_urldecode(test_string) == 'test string'
    test_string = 'test%2520string'
    assert unicode_urldecode(test_string) == 'test%20string'
    test_string = 'test%252520string'
    assert unicode_urldecode(test_string) == 'test%2520string'


# Generated at 2022-06-13 12:29:51.113867
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("A%20Z") == "%20"
    assert unicode_urlencode("A%20Z") == "%20"
    assert unicode_urlencode("A+Z") == "+"
    assert unicode_urlencode("A+Z") == "+"


# Generated at 2022-06-13 12:29:58.877197
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'') == u'%2F'
    assert unicode_urlencode(u'/') == u'%2F'
    assert unicode_urlencode(u'/', for_qs=True) == u'%2F'
    assert unicode_urlencode(u'a/b') == u'a%2Fb'
    assert unicode_urlencode(u'a/b', for_qs=True) == u'a%2Fb'
    assert unicode_urlencode(u'a&b') == u'a%26b'
    assert unicode_urlencode(u'a&b', for_qs=True) == u'a%26b'

# Generated at 2022-06-13 12:30:03.511265
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode('&/?%+=') == '%26%2F%3F%25%2B%3D'
        assert unicode_urlencode('&/?%+=', for_qs=True) == '%26%2F%3F%25%2B%3D'
    else:
        assert unicode_urlencode(u'&/?%+=') == '%26%2F%3F%25%2B%3D'
        assert unicode_urlencode(u'&/?%+=', for_qs=True) == '%26%2F%3F%25%2B%3D'


# Generated at 2022-06-13 12:30:07.665886
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"foo") == u"foo"
    assert unicode_urldecode(u"foo+bar") == u"foo bar"
    assert unicode_urldecode(u"foo%20bar") == u"foo bar"


# Generated at 2022-06-13 12:30:11.146354
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    F = FilterModule()
    f = F.filters()
    assert 'urldecode' in f
    assert 'urlencode' in f
    assert f['urldecode'] is do_urldecode
    assert f['urlencode'] is do_urlencode


# Generated at 2022-06-13 12:30:13.344907
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('€') == u'%E2%82%AC'
    assert unicode_urlencode('%2') == u'%252'


# Generated at 2022-06-13 12:30:14.912171
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters() == {
        'urldecode': do_urldecode,
    }

# Generated at 2022-06-13 12:30:22.766591
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils._text import to_bytes, to_text

    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%2A') == u'*'
    assert unicode_urldecode(u'%2a') == u'*'
    assert unicode_urldecode(u'%2A') == u'*'
    assert unicode_urldecode(to_bytes(u'%2A')) == to_text(u'*')



# Generated at 2022-06-13 12:30:37.947299
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == u'test'
    assert unicode_urlencode(u'€') == u'%E2%82%AC'
    assert unicode_urlencode(u'€', for_qs=True) == u'%E2%82%AC'
    assert unicode_urlencode({'a': 'test', 'b': 'test'}) == u'a=test&b=test'
    assert unicode_urlencode([('a', 'test'), ('b', 'test')]) == u'a=test&b=test'


# Generated at 2022-06-13 12:30:40.519537
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('foo%20bar%20baz') == u'foo bar baz'
    assert do_urldecode('%7B%7D') == u'{}'

# Generated at 2022-06-13 12:30:42.803986
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert isinstance(fm.filters(), dict)
    assert isinstance(fm.filters()['urldecode'], types.FunctionType)
    return fm.filters()

# Generated at 2022-06-13 12:30:45.768114
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    fm = FilterModule()
    assert fm.filters()['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode'] == do_urlencode
    else:
        assert fm.filters()['urlencode']



# Generated at 2022-06-13 12:30:46.721663
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode({"foo": "bar"}) == u"foo=bar"

# Generated at 2022-06-13 12:30:49.885552
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Test that unicode_urldecode decodes what it encodes
    '''

    string = u'THIS IS THE INPUT STRING'
    coded = unicode_urlencode(string)
    decoded = unicode_urldecode(coded)
    assert decoded == string


# Generated at 2022-06-13 12:30:54.216181
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'abc') == u'abc'

    # unquote_plus can't handle unicode
    if not PY3:
        assert unicode_urldecode(u'%E2%9D%A4') == u'♥'
    else:
        from urllib.parse import unquote_plus
        assert unicode_urldecode(u'%E2%9D%A4') == unquote_plus(u'%E2%9D%A4')



# Generated at 2022-06-13 12:30:58.159486
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    # Create the class
    filter_module = FilterModule()

    #
    # urldecode
    #
    assert filter_module.filters()['urldecode']('hello+world%21') == 'hello world!'
    assert filter_module.filters()['urldecode']('foo%20bar') == 'foo bar'

    #
    # urlencode
    #
    assert filter_module.filters()['urlencode']('hello world!') == 'hello+world%21'
    assert filter_module.filters()['urlencode']('foo bar') == 'foo+bar'



# Generated at 2022-06-13 12:31:05.471063
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'&') == '%26'
    assert unicode_urlencode(u'&', for_qs=True) == '%26'
    assert unicode_urlencode(u'&') == '%26'
    assert unicode_urlencode(u'&', for_qs=True) == '%26'


# Generated at 2022-06-13 12:31:15.285290
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(u'+++') == u'+++'
    assert unicode_urldecode(u'%2F') == u'/'
    assert unicode_urldecode(u'///') == u'///'
    assert unicode_urldecode(u'%25a') == u'%a'
    assert unicode_urldecode(u'%a') == u'%a'
    assert unicode_urldecode(u'%f0%9f%8f%a3') == u'\U000fe33b'
    assert unicode_urldecode(u'\U000fe33b') == u'\U000fe33b'


# Generated at 2022-06-13 12:31:37.309627
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six.moves.urllib.parse import quote, quote_plus

    # Test safe
    assert unicode_urlencode('Hello World', for_qs=False) == quote('Hello World')
    assert unicode_urlencode('Hello World/', for_qs=False) == quote('Hello World/')

    # Test unsafe
    assert unicode_urlencode('Hello World', for_qs=True) == quote_plus('Hello World')
    assert unicode_urlencode('Hello World/', for_qs=True) == quote_plus('Hello World/')
    assert unicode_urlencode('Hello World/?', for_qs=True) == quote_plus('Hello World/?')
    assert unicode_url

# Generated at 2022-06-13 12:31:44.803458
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('f%00%1F') == u'f%00%1F'
    assert unicode_urlencode('fö') == u'f%C3%B6'
    assert unicode_urlencode('fö', for_qs=True) == u'f%C3%B6'
    assert unicode_urlencode('f/') == u'f%2F'
    assert unicode_urlencode('f/', for_qs=True) == u'f%2F'


# Generated at 2022-06-13 12:31:48.132133
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # We do not run the filter tests unless they are more complete
    import ansible.module_utils.network.common.urls
    ansible.module_utils.network.common.urls.test()

# Generated at 2022-06-13 12:32:00.980560
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    # url shortcuts
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'].__name__ == 'do_urldecode'
    assert filters['urldecode']('%40') == '@'

    # for param: for_qs=True
    assert filters['urlencode']('@') == '%40'
    assert filters['urlencode']('/') == '%2F'
    assert filters['urlencode'](42) == '42'
    assert filters['urlencode']({'foo': 'bar'}) == 'foo=bar'
    assert filters['urlencode']({'foo bar': 'bar baz'}) == 'foo%20bar=bar%20baz'

# Generated at 2022-06-13 12:32:07.099033
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test without Jinja2 urlencode
    obj1 = FilterModule()
    res1 = obj1.filters()
    assert res1["urldecode"] == do_urldecode
    assert res1["urlencode"] == do_urlencode

    # Test with Jinja2 urlencode
    obj2 = FilterModule()
    res2 = obj2.filters()
    assert res2["urldecode"] == do_urldecode



# Generated at 2022-06-13 12:32:15.048277
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # create instance of FilterModule
    fm = FilterModule()
    # call method filters
    filters = fm.filters()

    # test urldecode
    assert filters['urldecode']('%20') == ' '

    # test urlencode
    assert filters['urlencode']('å') == '%C3%A5', 'filter urlencode doesn\'t work with non ascii characters'
    assert filters['urlencode']('é') == '%C3%A9', 'filter urlencode doesn\'t work with non ascii characters'
    assert filters['urlencode'](u'å') == '%C3%A5', 'filter urlencode doesn\'t work with non ascii characters'

# Generated at 2022-06-13 12:32:26.684307
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('key1=value1&key2=value2') == 'key1=value1&key2=value2'
    assert do_urlencode(['key1=value1', 'key2=value2']) == 'key1%3Dvalue1&key2%3Dvalue2'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'
    assert do_urlencode({'key1': 'value1'}) == 'key1=value1'
    assert do_urlencode('key1=value1,key2=value2') == 'key1%3Dvalue1%2Ckey2%3Dvalue2'

# Generated at 2022-06-13 12:32:34.353418
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test default filters
    assert FilterModule().filters() == {'urldecode': do_urldecode}

    # Test when Jinja2 does not have urlencode
    old_imports = FilterModule.__dict__.get('__imports__', None)
    try:
        # First, change jinja2 to an older version
        FilterModule.__imports__ = {'do_urlencode': False}
        filters = FilterModule().filters()

        # Now we must make sure they also contain the custom urlencode
        assert do_urlencode == filters['urlencode']
        assert do_urldecode == filters['urldecode']
    finally:
        # Finally, restore the jinja2 imports
        if old_imports:
            FilterModule.__imports__ = old_im

# Generated at 2022-06-13 12:32:42.887791
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    def tval(var):
        if PY3:
            return var
        return to_bytes(var)
    assert unicode_urldecode("hello+world") == "hello world"
    assert unicode_urldecode("hello%20world") == "hello world"
    assert unicode_urldecode("hello%2Bworld") == "hello+world"
    assert unicode_urldecode("hello+%2B+world") == "hello  + world"
    assert unicode_urldecode("hello+%2F+world") == "hello  / world"
    assert unicode_urldecode("hello%2Fworld") == \
        unicode_urldecode("hello%2Fworld",) == "hello/world"

# Generated at 2022-06-13 12:32:51.382172
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:33:24.421832
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six.moves.urllib.parse import urlencode
    from ansible.module_utils._text import to_bytes

    assert urlencode({'a': '1'}) == 'a=1'
    assert urlencode({'a': '1', 'b': '2'}) == 'a=1&b=2'
    assert urlencode({'a': '1+2', 'b': '3 4'}) == 'a=1%2B2&b=3+4'

    assert urlencode(u'a=1') == 'a%3D1'
    assert urlencode(u'a=1 b=2') == 'a%3D1+b%3D2'

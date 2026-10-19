

# Generated at 2022-06-13 12:23:26.131437
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%E2%82%AC%2B%20%C2%B1%C3%A9%21%40') == u'€+ ±é!@'



# Generated at 2022-06-13 12:23:29.486859
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filters = FilterModule().filters()
    for key, method in iteritems(filters):
        assert key in globals()
        assert globals()[key] == method

# Generated at 2022-06-13 12:23:39.071252
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test the urldecode filters
    assert unicode_urldecode(u'Innocent%20p%c3%b8tat%c3%b8%3d%20') == u'Innocent pøtatø= '
    assert unicode_urldecode(u'Innocent%20p%c3%b8tat%c3%b8%3d%20', safe=u'') == u'Innocent pøtatø= '
    assert unicode_urldecode(u'Innocent%20p%c3%b8tat%c3%b8=%20', safe=u'/') == u'Innocent pøtatø= '

# Generated at 2022-06-13 12:23:47.285994
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('t%C3%A9st') == u't\xe9st'
    assert unicode_urldecode(b't%C3%A9st') == u't\xe9st'
    assert unicode_urldecode(u't%C3%A9st') == u't\xe9st'
    assert unicode_urldecode(u'%EF%BF%BD') == u'\ufffd'  # unrepresented byte sequence
    assert unicode_urldecode(u'%E2%89%A0') == u'\u2260'  # ASCII equivalent



# Generated at 2022-06-13 12:23:49.532442
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter = FilterModule()
    assert filter.filters() == {'urldecode': do_urldecode}

# Generated at 2022-06-13 12:23:54.295422
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert '%2d' == unicode_urldecode(u'%2d')
    assert '%2d' == unicode_urldecode(b'%2d')
    assert u'-2' == unicode_urldecode(u'%2d')
    assert u'-2' == unicode_urldecode(b'%2d')



# Generated at 2022-06-13 12:24:01.555462
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Test non-string types
    assert unicode_urlencode({"a": 1, "b": 2, "c": 3}) == u'a=1&b=2&c=3'
    assert unicode_urlencode(["a", "b", "c"]) == u'a&b&c'
    assert unicode_urlencode(123) == u'123'

    # Test string types
    assert unicode_urlencode(u'a=1&b=2') == u'a%3D1%26b%3D2'
    assert unicode_urlencode(u'abcdefghijklmnopqrstuvwxyz') == u'abcdefghijklmnopqrstuvwxyz'

# Generated at 2022-06-13 12:24:06.371285
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Import module and create test instance
    import ansible.utils
    import ansible.errors
    fm = FilterModule()

    # Create jinja2 environment
    jenv = ansible.utils.jinja2.Environment()
    jenv.filters = fm.filters()

    # Tests for urldecode filter
    assert jenv.from_string(u"{{ 'key=value' | urldecode }}").render() == u'key=value'
    assert jenv.from_string(u"{{ 'key%20%3D%20value' | urldecode }}").render() == u'key = value'
    assert jenv.from_string(u"{{ 'key=one%2Ctwo%2Cthree' | urldecode }}").render() == u'key=one,two,three'

# Generated at 2022-06-13 12:24:10.929603
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('string') == 'string'
    assert do_urlencode('string with spaces') == 'string%20with%20spaces'
    assert do_urlencode('string with äöü') == 'string%20with%20%C3%A4%C3%B6%C3%BC'


# Generated at 2022-06-13 12:24:21.871984
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'a b') == u'a%20b'
    assert unicode_urlencode(u'a b', for_qs=True) == u'a+b'
    assert unicode_urlencode(u'python with space') == u'python%20with%20space'
    assert unicode_urlencode(u'python with space', for_qs=True) == u'python+with+space'
    assert unicode_urlencode(u'python/with/slash') == u'python%2Fwith%2Fslash'
    assert unicode_urlencode(u'python/with/slash', for_qs=True) == u'python%2Fwith%2Fslash'

# Generated at 2022-06-13 12:24:25.901374
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']('a%20b') == 'a b'

# Generated at 2022-06-13 12:24:36.103541
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test 'urldecode' filter.
    fm = FilterModule()
    filters = fm.filters()
    url_encoded_value = 'c=%27%21%23%24%25%5E%26*%28%29_%2B-'
    url_decoded_value = "'!#$%^&*()_+-"
    assert filters['urldecode'](url_encoded_value) == url_decoded_value
    # Test 'urlencode' filter.
    url_encoded_value = 'c=%27%21%23%24%25%5E%26*%28%29_%2B-'
    encoded_value = filters['urlencode']({'c': "'!#$%^&*()_+-"})
    assert encoded_value == url_encoded

# Generated at 2022-06-13 12:24:38.071486
# Unit test for function do_urlencode
def test_do_urlencode():
    value = {'test': 'one+two'}
    expected = 'test=one%2Btwo'
    assert do_urlencode(value) == expected

# Generated at 2022-06-13 12:24:41.434880
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Test unicode_urldecode function
    '''
    res = unicode_urldecode(u'%C3%A9')
    assert res == u'é'
    assert type(res) == unicode

    res = unicode_urldecode(u'%2F')
    assert res == u'/'
    assert type(res) == unicode



# Generated at 2022-06-13 12:24:54.336769
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.compat import json
    from ansible.module_utils.six.moves.urllib.parse import urlencode
    from ansible.module_utils.six.moves.urllib.parse import unquote
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text

    test_obj = FilterModule()
    test_filters = test_obj.filters()

    # Test the method urlencode

# Generated at 2022-06-13 12:24:58.706512
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import ansible.utils.template as template

    assert template.urldecode('hello%20world') == 'hello world'

    assert template.urlencode('foo bar') == 'foo+bar'
    assert template.urlencode({'foo': 'bar', 'dag': 'wieers'}) == 'foo=bar&dag=wieers'

# Generated at 2022-06-13 12:25:00.747881
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'x=1,y=2' == unicode_urldecode(u'x%3D1%2Cy%3D2')



# Generated at 2022-06-13 12:25:08.858976
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a+b') == u'a b'
    assert unicode_urldecode(u'a%20b') == u'a b'
    assert unicode_urldecode(u'a%2Bb') == u'a+b'
    assert unicode_urldecode(u'%7Ba%20b%7D') == u'{a b}'
    assert unicode_urldecode(u'%7B%22a%22%3A%20%22b%22%7D') == u'{"a": "b"}'


# Generated at 2022-06-13 12:25:11.248860
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://foo') == 'http%3A//foo'
    assert unicode_urlencode('http:/foo') == 'http%3A/foo'
    assert unicode_urlencode('http://foo?foo=http://bar') == 'http%3A//foo%3Ffoo%3Dhttp%3A//bar'


# Generated at 2022-06-13 12:25:21.870375
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('ab%0Acd') == 'ab\ncd'
    assert unicode_urldecode('ab%0acd') == 'ab\ncd'
    assert unicode_urldecode('ab%2Fcd') == 'ab/cd'
    assert unicode_urldecode('ab%2fcd') == 'ab/cd'
    assert unicode_urldecode('ab%2bcd') == 'ab+cd'
    assert unicode_urldecode('ab%2BCd') == 'ab+Cd'
    assert unicode_urldecode('ab%26cd') == 'ab&cd'
    assert unicode_urldecode('ab%26cd') == 'ab&cd'

# Generated at 2022-06-13 12:25:31.037007
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils._text import to_bytes, to_text

    # Unicode string that are not in the ASCII range are quoted
    assert unicode_urldecode(u'\u0123') == u'\u0123'

    # ASCII string are not quoted
    assert unicode_urldecode(u'a') == u'a'

    # Backslash are quoted
    assert unicode_urldecode(u'\\') == u'\\'

    # Backslash are quoted
    assert unicode_urldecode(u'\\') == u'\\'

    # Space are quoted
    assert unicode_urldecode(u' ') == u' '

    # Quote are quoted
    assert unicode_urldecode(u'\'') == u'\''

    # Double quote

# Generated at 2022-06-13 12:25:33.549441
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    # Test for urldecode/urlencode
    f = FilterModule()
    assert f.filters()['urldecode']('%20') == ' '


test_FilterModule_filters()

# Generated at 2022-06-13 12:25:37.886958
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'\u05d0\u05d1\u05d2 abc' == unicode_urldecode('%d7%90%d7%91%d7%92+abc')


# Generated at 2022-06-13 12:25:39.621641
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('hello+world') == 'hello world'
    assert do_urlencode(dict(x='hello world')) == 'x=hello+world'

# Generated at 2022-06-13 12:25:44.315266
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'\u00e9'
    assert unicode_urldecode('%C3%A9%20%C3%A9') == u'\u00e9 \u00e9'


# Generated at 2022-06-13 12:25:49.724620
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert u'h%C3%A9h%C3%A9h%C3%A9' == unicode_urlencode(u'h\xe9h\xe9h\xe9')
    assert u'slash%2F' == unicode_urlencode(u'slash/')
    assert u'slash%2F' == unicode_urlencode(u'slash/', for_qs=True)



# Generated at 2022-06-13 12:25:51.925688
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    assert 'urldecode' in f.filters()
    assert 'urlencode' in f.filters()


# Generated at 2022-06-13 12:25:55.158794
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.utils.unicode import to_unicode
    assert unicode_urlencode(to_unicode(b"foo;bar?")) == "%s" % to_unicode(u"foo%3Bbar%3F")

# Generated at 2022-06-13 12:26:08.228873
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''FilterModule unit tests'''
    filter = FilterModule()
    filters = filter.filters()
    assert filters['urlencode']('http://example.com/foo') == 'http%3A%2F%2Fexample.com%2Ffoo'
    assert filters['urldecode']('http%3A%2F%2Fexample.com%2Ffoo') == 'http://example.com/foo'
    assert filters['urlencode']('http://example.com/foo?bar=baz') == 'http%3A%2F%2Fexample.com%2Ffoo%3Fbar%3Dbaz'

# Generated at 2022-06-13 12:26:14.426000
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7E') == u'~'
    assert unicode_urldecode('%E3%83%86%E3%82%B9%E3%83%88') == u'テスト'
    assert unicode_urldecode('%E3%83%86%E3%82%B9%E3%83%88%20%E3%83%86%E3%82%B9%E3%83%88') == u'テスト テスト'


# Generated at 2022-06-13 12:26:20.629824
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    # test urldecode
    assert filters['urldecode']('https%3A%2F%2Fgoogle.com') == 'https://google.com'
    # test urlencode
    if not HAS_URLENCODE:
        assert filters['urlencode']('https://google.com') == 'https%3A%2F%2Fgoogle.com'

# Generated at 2022-06-13 12:26:29.983617
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('c%C3%B5ki%20ch%C3%B5%20kn%C3%BAg%C3%AD') == u'cõki chô knúgí'
    assert unicode_urldecode('c%F5ki%20ch%F4%20kn%FAg%ED') == u'cõki chô knúgí'

# Generated at 2022-06-13 12:26:38.458736
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode('abc+def') == 'abc def'
    assert unicode_urldecode('abc%2Bdef') == 'abc+def'

    assert unicode_urldecode(u'abc') == u'abc'
    assert unicode_urldecode(u'abc+def') == u'abc def'
    assert unicode_urldecode(u'abc%2Bdef') == u'abc+def'

    assert unicode_urldecode(b'abc') == u'abc'
    assert unicode_urldecode(b'abc+def') == u'abc def'
    assert unicode_urldecode(b'abc%2Bdef') == u'abc+def'

# Generated at 2022-06-13 12:26:46.019514
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:26:54.351150
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:27:04.877854
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils.six.moves.urllib.parse import quote_plus, unquote_plus
    import sys

    fm = FilterModule()
    p = basic.AnsibleModule(
        argument_spec = dict()
    )
    filter_plugin = fm.filters()

    # Test urlencode/urldecode
    if sys.version_info >= (3,):
        assert filter_plugin["urldecode"]("foo%20bar%2Bbaz") == "foo bar+baz"
    else:
        assert filter_plugin["urldecode"]("foo%20bar%2Bbaz") == u"foo bar+baz"

# Generated at 2022-06-13 12:27:14.755294
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('http://192.168.1.1/') == 'http%3A//192.168.1.1/'
    assert do_urlencode('http://192.168.1.1/?foo=bar') == 'http%3A//192.168.1.1/%3Ffoo%3Dbar'
    assert do_urlencode('http://192.168.1.1/?foo=bar&test=123') == 'http%3A//192.168.1.1/%3Ffoo%3Dbar%26test%3D123'

# Generated at 2022-06-13 12:27:23.341256
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://foo/bar') == 'http%3A//foo/bar'
    assert unicode_urlencode('http://foo/bar', for_qs=True) == 'http%3A%2F%2Ffoo%2Fbar'
    assert unicode_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert unicode_urlencode(['a', 'b']) == 'a&b'
    assert unicode_urlencode('a') == 'a'

if __name__ == '__main__':
    test_unicode_urlencode()

# Generated at 2022-06-13 12:27:33.351456
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('string') == u'string'
    assert unicode_urlencode('string', for_qs=True) == u'string'
    assert unicode_urlencode({'key': 'value'}) == u'key=value'
    assert unicode_urlencode(['key', 'value']) == u'key&value'
    assert unicode_urlencode(('key', 'value')) == u'key&value'
    assert unicode_urlencode(u'ŠĐĆŽćžšđ') == u'%C5%A0%C4%90%C4%86%C5%BD%C4%87%C5%BE%C5%A1%C4%91'

# Generated at 2022-06-13 12:27:40.520841
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"Dag Ånnestad") == u'Dag%20%C3%85nnestad'
    assert unicode_urlencode(u"Dag Ånnestad", for_qs=True) == u'Dag%20%C3%85nnestad'
    assert unicode_urlencode(u"Dag Ånnestad", for_qs=True) == u'Dag%20%C3%85nnestad'

# Generated at 2022-06-13 12:27:51.627142
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # These are some of the test cases
    tests = {
        b'Hi%26there+you%27ve+got+%C3%A4+%F0%9F%87%BA+%F0%9F%87%B8': u'Hi&there you\'ve got \xe4 \U0001f57a \U0001f578',  # noqa
        b'There+are+%3C%3E+some+%3C%25+things%25%26+here': u'There are <> some <% things%& here',
    }
    # Iterate over tests
    for key, value in tests.items():
        # Do the test
        assert(unicode_urldecode(key) == value)



# Generated at 2022-06-13 12:27:55.810440
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%2C%2C') == u',,'
    assert unicode_urldecode('%2C%2C') == u',,'
    assert unicode_urldecode('%E9%81%B8%E6%8A%9E') == u'選択'


# Generated at 2022-06-13 12:28:09.086801
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('param1=value1&param2=value2') == u'param1=value1&param2=value2'
    assert unicode_urldecode('param1=value1&param2=value2@') == u'param1=value1&param2=value2@'
    assert unicode_urldecode('param1=value1&param2=value2@') == u'param1=value1&param2=value2@'
    assert unicode_urldecode('param1@=value1&param2@=value2') == u'param1@=value1&param2@=value2'

# Generated at 2022-06-13 12:28:16.629996
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from collections import OrderedDict
    assert unicode_urlencode('foo') == 'foo'
    assert unicode_urlencode('foo1 foo2') == 'foo1%20foo2'
    assert unicode_urlencode('/bar') == '%2Fbar'
    assert unicode_urlencode('/bar', for_qs=True) == '%2Fbar'
    assert unicode_urlencode(u'ÿ') == '%C3%BF'
    assert unicode_urlencode(u'ÿ', for_qs=True) == '%C3%BF'
    assert unicode_urlencode({'foo': 'bar'}) == 'foo=bar'

# Generated at 2022-06-13 12:28:19.137312
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    mod = FilterModule()
    filters = mod.filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:28:28.349256
# Unit test for function unicode_urlencode
def test_unicode_urlencode():

    # Base
    assert 'a' == unicode_urlencode('a')
    assert '%C3%A0' == unicode_urlencode('à')
    assert '%20' == unicode_urlencode(' ')
    assert '%3Cbr%3E' == unicode_urlencode('\n')
    assert '%2F' == unicode_urlencode('/')
    assert 'foo%2Fbar%2Fbaz' == unicode_urlencode('foo/bar/baz')

    # For querystring
    assert 'foo%2Fbar%2Fbaz' == unicode_urlencode('foo/bar/baz', for_qs=True)

# Generated at 2022-06-13 12:28:33.921284
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    ''' Test unicode_urlencode '''
    from ansible.module_utils import basic

    assert unicode_urlencode('http://foo/?a b') == u'http%3A//foo/%3Fa%20b'
    assert unicode_urlencode({'a': 'b', 'c': 'd'}) == u'a=b&c=d'
    assert unicode_urlencode(['a', 'b', 'c']) == u'a&b&c'



# Generated at 2022-06-13 12:28:40.683419
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert 'Hello, World!' == unicode_urldecode('Hello%20%2C%20World%21')
    assert 'Hello, World!' == unicode_urldecode('Hello%20%2c%20World%21')
    assert '/' == unicode_urldecode('/')
    assert '?' == unicode_urldecode('?')
    assert '#' == unicode_urldecode('#')
    assert '!' == unicode_urldecode('!')
    assert ' ' == unicode_urldecode('%20')
    assert ' ' == unicode_urldecode('%20')
    assert ' ' == unicode_urldecode('+')
    assert ' ' == unicode_urldecode('+')
    assert ' ' == unicode_urld

# Generated at 2022-06-13 12:28:46.610063
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'+') == u' '
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(b'+') == u' '
    assert unicode_urldecode(b'%20') == u' '
    # This is expected behaviour: it is not the basis for a test failure
    if PY3:
        assert unicode_urldecode(b'+') == u' '
    else:
        assert unicode_urldecode(b'+') == b' '


# Generated at 2022-06-13 12:28:49.796906
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('abc%23%20def') == u'abc# def'
    assert unicode_urldecode('abc+def%2Bxyz') == u'abc def+xyz'


# Generated at 2022-06-13 12:29:03.432194
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.common.collections import ImmutableDict

    class test_FilterModule(FilterModule):
        pass

    f = test_FilterModule()
    assert isinstance(f.filters(), dict)

    # Since ansible_vault_password is set, the vault_secret_key is not None
    # So the vault_secret_key will not be returned by the FilterModule filters.
    # By the way, the vault_secret_key is used by the get_hash function
    # which is called by the to_nice_yaml function to lookup the vault_secret_key.
    ansible_vault_password = None
    if ansible_vault_password is not None:
        vault_secret_key = None

    # Test for the urldecode filter

# Generated at 2022-06-13 12:29:18.398166
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest
    from ansible import errors

    test_filters = FilterModule().filters()
    assert type(test_filters) == dict

    test_urlencode_string = test_filters.get('urlencode')
    if not test_urlencode_string:
        pytest.skip('This test was written for ansible versions prior to 2.7')

    assert test_urlencode_string('string') == 'string'
    assert test_urlencode_string('mysearch?string=a+space') == 'mysearch%3Fstring%3Da+space'
    assert test_urlencode_string(u'mysearch?string=a+space') == u'mysearch%3Fstring%3Da+space'

    # Dictionary

# Generated at 2022-06-13 12:29:21.249124
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # The test is valid to verify the existence of the filters.
    fm = FilterModule()
    assert isinstance(fm.filters(), dict)

# Generated at 2022-06-13 12:29:25.466986
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()
    assert filters['urldecode'] == do_urldecode
    if HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode
    else:
        assert filters['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:29:29.445524
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'проверка') == u'проверка'



# Generated at 2022-06-13 12:29:39.601391
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # We use 'from ansible.module_utils.urls import *'
    # so we can not use 'from ansible.module_utils.urls import FilterModule'
    from ansible.module_utils.urls import FilterModule

    fm = FilterModule()
    filters = fm.filters()

    # Since jinja2 2.7, the builtin urlencode filter is available,
    # and we will use it by default.
    assert 'urldecode' in filters

    # Only if jinja2 is older than 2.7,
    # we provide a custom urlencode filter.
    if not HAS_URLENCODE:
        assert 'urlencode' in filters

    urldecode = filters['urldecode']
    assert urldecode('foo') == 'foo'
    assert urld

# Generated at 2022-06-13 12:29:42.617668
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    FilterModule.filters = FilterModule.filters.__func__
    assert FilterModule.filters(None)['urldecode'] == do_urldecode
    del FilterModule.filters

# Generated at 2022-06-13 12:29:46.480376
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    output = unicode_urldecode(u'%E4%B8%AD%E6%96%87')
    assert output == u'中文'

    output = unicode_urldecode(u'%2F')
    assert output == u'/'



# Generated at 2022-06-13 12:29:53.606880
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo') == 'foo'
    assert unicode_urldecode('foo%20bar') == 'foo bar'
    assert unicode_urldecode('foo+bar') == 'foo bar'
    assert unicode_urldecode('foo%2Fbar') == 'foo/bar'
    assert unicode_urldecode('foo%2fbar') == 'foo/bar'
    assert unicode_urldecode('foo%252Fbar') == 'foo%2Fbar'
    assert unicode_urldecode('foo%2Bbar') == 'foo%2Bbar'


# Generated at 2022-06-13 12:30:01.189533
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import pytest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from six import PY3, text_type

    m = FilterModule()
    f = m.filters()

    assert f['urldecode']('%20') == ' '

    if not HAS_URLENCODE:
        assert f['urlencode']('!') == '%21'
        assert f['urlencode']('foo') == 'foo'
        assert f['urlencode']('foo bar') == 'foo+bar'
        assert f['urlencode']('foo+bar') == 'foo%2Bbar'
        assert f['urlencode']('foo%20bar') == 'foo%20bar'
        assert f['urlencode']('foo bar%20') == 'foo+bar%20'

# Generated at 2022-06-13 12:30:15.415891
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo') == 'foo'
    assert unicode_urlencode(u'foo bar') == 'foo%20bar'
    assert unicode_urlencode(u'foo:bar') == 'foo:bar'
    assert unicode_urlencode(u'foo bar', True) == 'foo+bar'
    assert unicode_urlencode(u'foo+bar', True) == 'foo%2Bbar'
    assert unicode_urlencode(u'foo bar', True) == u'foo+bar'
    assert unicode_urlencode(u'foo+bar', True) == u'foo%2Bbar'
    assert unicode_urlencode(u'foo:bar', True) == 'foo:bar'

# Generated at 2022-06-13 12:30:21.646180
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a%2Bb') == u'a+b'
    assert unicode_urldecode(b'a%2Bb') == u'a+b'
    assert unicode_urldecode(u'a%2Bb') == 'a+b'
    assert unicode_urldecode(b'a%2Bb') == 'a+b'


# Generated at 2022-06-13 12:30:33.108521
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils._text import to_bytes, to_text

    fm = FilterModule()
    filters = fm.filters()

    # urldecode()
    # ==================
    assert filters['urldecode']('') == ''
    assert filters['urldecode']('%20') == u' '
    assert filters['urldecode']('%3a%2f%2f') == u'://'
    assert filters['urldecode']('%3a%2f%2f%20') == u':// '
    assert filters['urldecode']('%3a%2f%2f%20%2f') == u':// /'

# Generated at 2022-06-13 12:30:42.981435
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Simple test
    assert unicode_urlencode(u'foo') == u'foo'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo+bar') == u'foo%2Bbar'
    assert unicode_urlencode(u'foo.bar') == u'foo.bar'
    assert unicode_urlencode(u'/foo.bar') == u'/foo.bar'

    # Special characters
    assert unicode_urlencode(u'I ♥ Ansible') == u'I%20%E2%99%A5%20Ansible'

    # Non-ASCII characters
    assert unicode_urlencode(u'welkom') == u'welkom'

    # Tuples,

# Generated at 2022-06-13 12:30:45.680356
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import Mapping
    assert isinstance(FilterModule.filters(None), Mapping)
    assert isinstance(basic.AnsibleModule(argument_spec={}).params, Mapping)

# Generated at 2022-06-13 12:30:48.023426
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    string = u'www.foo.tld/' + unichr(300) + unichr(350)
    assert 'www.foo.tld/%C3%84%C2' in unicode_urlencode(string)


# Generated at 2022-06-13 12:30:50.436804
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert filters['urldecode'] == do_urldecode
    assert filters.get('urlencode', None) == do_urlencode

# Generated at 2022-06-13 12:30:56.287243
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('foo/bar') == 'foo%2Fbar'
    assert unicode_urlencode('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    assert unicode_urlencode('!"()*') == '%21%22%28%29%2A'
    assert unicode_urlencode('foo bar') == 'foo+bar'
    assert unicode_urlencode('foo+bar') == 'foo%2Bbar'
    assert unicode_urlencode('foo?bar') == 'foo%3Fbar'
    assert unicode

# Generated at 2022-06-13 12:31:01.908844
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%A4%C3%B6%C3%BC') == u'äöü'


# Generated at 2022-06-13 12:31:05.024703
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('%27%C2%B8') == "Ƹ"
    else:
        assert unicode_urldecode('%27%C2%B8') == u"Ƹ"



# Generated at 2022-06-13 12:31:15.145547
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = u'%2Ffoo%2Fbar%2Fbaz'
    v = unicode_urldecode(string)
    assert v == u'/foo/bar/baz'
    if not PY3:
        assert isinstance(v, unicode)


# Generated at 2022-06-13 12:31:29.883442
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'/') == to_text('/')
    assert unicode_urlencode(u'/') != '/'
    assert unicode_urlencode(u'/', for_qs=True) == to_text('/')
    assert unicode_urlencode(u'/', for_qs=True) != '/'

    from ansible.module_utils._text import to_native
    assert unicode_urlencode(u'你好') == to_native('%E4%BD%A0%E5%A5%BD')
    assert unicode_urlencode(u'你好') != to_native(u'你好')

# Generated at 2022-06-13 12:31:38.196881
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%27') == u'\''
    assert unicode_urldecode('%27foo') == u'\'foo'
    assert unicode_urldecode('foo%27') == u'foo\''
    assert unicode_urldecode('%27foo%27') == u'\'foo\''
    assert unicode_urldecode('foo%27foo') == u'foo\'foo'
    assert unicode_urldecode('fo%27o%27foo') == u'fo\'o\'foo'
    assert unicode_urldecode('fo%2Fo%2Ffoo') == u'fo/o/foo'
    assert unicode_urldecode('fo%2fo%2ffoo') == u'fo/o/foo'
    assert unicode

# Generated at 2022-06-13 12:31:48.740956
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("this is a test") == "this%20is%20a%20test"
    assert unicode_urlencode("this is a test", for_qs=True) == "this+is+a+test"
    assert unicode_urlencode("this is a / test") == "this%20is%20a%20%2F%20test"
    assert unicode_urlencode("this is a / test", for_qs=True) == "this+is+a+%2F+test"
    assert unicode_urlencode("this is a ? test") == "this%20is%20a%20%3F%20test"
    assert unicode_urlencode("this is a ? test", for_qs=True) == "this+is+a+%3F+test"


# Generated at 2022-06-13 12:32:00.684166
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Test the urldecode function so that it always returns a unicode object
    '''
    strings = {
        '%20': u' ',
        '%CE%A9': u'Ω',
        '%CE%A9%20for%20life': u'Ω for life',
        '%2F': u'/',
        '%CF%86%CE%B1%CE%B9%CE%B1': u'φαια',
        '%25': u'%',
        '%2F%2F': u'//',
        '%': u'%',
    }
    for (urlencoded, text) in iteritems(strings):
        assert unicode_urldecode(urlencoded) == text


# Generated at 2022-06-13 12:32:07.351957
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if not PY3:
        assert unicode_urlencode(to_text(u"foo")) == to_text(u"foo")
        assert unicode_urlencode(to_bytes(u"foo")) == to_text(u"foo")
    else:
        assert unicode_urlencode(u"foo") == u"foo"
    assert unicode_urlencode({'a': 'b'}) == u'a=b'
    assert unicode_urlencode([1, 2, 3]) == u'1&2&3'
    assert unicode_urlencode(u"foo bar") == u'foo+bar'
    assert unicode_urlencode(u"foo bar", True) == u'foo%20bar'



# Generated at 2022-06-13 12:32:10.417422
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('sample text') == 'sample%20text'
    assert do_urlencode(['foo', 'bar z']) == 'foo&bar%20z'
    assert do_urlencode({'foo': 'bar z'}) == 'foo=bar%20z'

# Generated at 2022-06-13 12:32:17.189136
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # The following tests are from the Jinja2 tests
    assert unicode_urlencode(u'\xf6\xe4\xfc') == '%C3%B6%C3%A4%C3%BC'
    assert unicode_urlencode(u'\xf6\xe4\xfc', True) == '%C3%B6%C3%A4%C3%BC'
    assert unicode_urlencode(u'\n') == '%0A'
    assert unicode_urlencode(u'\n', True) == '%0A'
    assert unicode_urlencode(u'/') == '%2F'
    assert unicode_urlencode(u'/', True) == '%2F'

# Generated at 2022-06-13 12:32:28.810328
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('') == u''
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('a+b') == u'a+b'
    assert unicode_urldecode('a%20b') == u'a b'
    assert unicode_urldecode('a%2Bb') == u'a+b'
    assert unicode_urldecode('a%2bb') == u'a+b'
    assert unicode_urldecode('a%2c') == u'a,'
    assert unicode_urldecode('a%3D') == u'a='
    assert unicode_urldecode('a%3d') == u'a='

# Generated at 2022-06-13 12:32:39.101604
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode(u'abc') == 'abc'
    assert do_urlencode(u'a b c') == 'a%20b%20c'
    assert do_urlencode(u'a+b+c') == 'a%2Bb%2Bc'
    assert do_urlencode(u'http://www.example.com/?a=a+b&c=d+e') == 'http%3A%2F%2Fwww.example.com%2F%3Fa%3Da%2Bb%26c%3Dd%2Be'

# Generated at 2022-06-13 12:32:58.082907
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode(u'http://dag.wieers.com/foo?a=1&b=2') == 'http%3A%2F%2Fdag.wieers.com%2Ffoo%3Fa%3D1%26b%3D2'
    else:
        assert unicode_urlencode(u'http://dag.wieers.com/foo?a=1&b=2') == 'http%3A%2F%2Fdag.wieers.com%2Ffoo%3Fa%3D1%26b%3D2'


# Generated at 2022-06-13 12:33:06.601785
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus
    from ansible.module_utils._text import to_text, to_bytes
    s = u'a%s' % (unquote_plus(u'%C3%B6'),)
    if PY3:
        assert isinstance(s, str)
        assert s == unicode_urldecode(u'a%C3%B6')
        assert u'a\xf6' == unicode_urldecode(to_bytes(u'a%C3%B6'))
        assert u'a\xf6' == unicode_urldecode(to_bytes(u'a%c3%b6'))

# Generated at 2022-06-13 12:33:12.509886
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    assert f.filters()['urldecode'].__name__ == do_urldecode.__name__
    if not HAS_URLENCODE:
        assert f.filters()['urlencode'].__name__ == do_urlencode.__name__


# Generated at 2022-06-13 12:33:23.670016
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test functionality
    assert unicode_urldecode(u'%27%28%29%3b') == u"';()"

    # Test ASCII-compatibility
    assert unicode_urldecode(b'%27%28%29%3b') == u"';()"
    assert unicode_urldecode(u'%27%28%29%3b') == u"';()"
    assert unicode_urldecode(to_bytes('%27%28%29%3b')) == u"';()"
    assert unicode_urldecode(to_text('%27%28%29%3b')) == u"';()"

    # Test UTF-8-compatibility
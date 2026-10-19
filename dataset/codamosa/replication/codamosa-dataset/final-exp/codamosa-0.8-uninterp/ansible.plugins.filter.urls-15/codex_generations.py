

# Generated at 2022-06-13 12:23:22.663412
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%42') == u'B'
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(u'%C3%BC') == u'\xfc'
    assert unicode_urldecode(u'%26') == u'&'
    assert unicode_urldecode(u'%2F') == u'/'
    assert unicode_urldecode(u'%25') == u'%'


# Generated at 2022-06-13 12:23:36.049619
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys
    import platform
    import os
    os_env = dict(os.environ)

    # Force a UTF-8 locale to make sure that tests that deal with
    # non-ASCII chars will always be executed
    #
    # We do this rather than use unicode_literals to avoid breaking
    # non-UTF-8 aware builds on Python 2
    os_env['LC_CTYPE'] = 'en_US.UTF-8'
    os_env['LC_ALL'] = 'en_US.UTF-8'
    fm = FilterModule()
    assert fm.filters()['urldecode']('foo') == 'foo'
    assert isinstance(fm.filters()['urldecode']('foo'), string_types)


# Generated at 2022-06-13 12:23:44.476643
# Unit test for function do_urlencode
def test_do_urlencode():
    """
    Function do_urlencode converts special chars and unicode characters
    """
    r3 = do_urlencode("log:a&b")
    assert r3 == "log%3Aa%26b"
    r4 = do_urlencode("log:a&b, хинта")
    assert r4 == "log%3Aa%26b%2C%20%D1%85%D0%B8%D0%BD%D1%82%D0%B0"
    r5 = do_urlencode([1, 2, 3, 'хинта', 'a', 'b', 'c'])

# Generated at 2022-06-13 12:23:48.613724
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    m = FilterModule()
    filters = m.filters()

    assert filters['urldecode']('%3F%3D') == '?='
    assert filters['urlencode']('?=') == '%3F%3D'

# Generated at 2022-06-13 12:23:58.761775
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys
    # test unquoted
    assert u'abcd' == unicode_urldecode('abcd')
    # test quoted
    assert u'abcd' == unicode_urldecode('ab%20cd')
    if sys.version_info >= (3,0):
        assert u'abcd' == unicode_urldecode('ab%20cd')
    # test quoted and unquoted mixed
    assert u'abcd' == unicode_urldecode('ab%20cd%2c=')
    # test unicode
    if sys.version_info < (3,0):
        assert u'abcd\u20ac' == unicode_urldecode('abcd%E2%82%AC')
    else:
        assert u'abcd\u20ac' == unicode

# Generated at 2022-06-13 12:23:59.932952
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters() != None



# Generated at 2022-06-13 12:24:05.233051
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # From https://en.wikipedia.org/wiki/Percent-encoding#Types_of_percent-encoding
    assert unicode_urldecode(u'%41%42') == u'AB'
    assert unicode_urldecode(u'%41%42%43') == u'ABC'
    assert unicode_urldecode(u'%41+%42+%43') == u'A B C'
    assert unicode_urldecode(u'%41%42%43+%3d+') == u'ABC='
    assert unicode_urldecode(u'%41%42%43') == u'ABC'
    assert unicode_urldecode(u'%41') == u'A'
    assert unicode_urldecode(u'%41%42%43')

# Generated at 2022-06-13 12:24:11.796602
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('foo') == 'foo'
    assert do_urlencode('foo bar') == 'foo%20bar'
    assert do_urlencode('foo+bar') == 'foo%2Bbar'
    assert do_urlencode(dict(a='b c', d='e f')) == 'a=b%20c&d=e%20f'
    assert do_urlencode(dict(a='b c', d='e f')) == 'a=b%20c&d=e%20f'
    assert do_urlencode([['a', 'b c'], ['d', 'e f']]) == 'a=b%20c&d=e%20f'
    assert do_urlencode('foo bar') == 'foo%20bar'
    assert do_urlencode

# Generated at 2022-06-13 12:24:15.888831
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'aBc123') == u'aBc123'
    assert unicode_urldecode(u'a+Bc%21%40%23') == u'a Bc!@#'



# Generated at 2022-06-13 12:24:19.839851
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%20b%20c') == 'a b c'
    assert unicode_urldecode('a%2b%2Bb%2Bc%2b') == 'a++b+c+'


# Generated at 2022-06-13 12:24:25.389046
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('caf%C3%A9') == 'café'
    else:
        assert unicode_urldecode('caf%C3%A9') == b'caf\xc3\xa9'.decode(encoding='ascii')



# Generated at 2022-06-13 12:24:35.842320
# Unit test for function do_urlencode
def test_do_urlencode():
    from ansible.module_utils._text import to_bytes, to_text

    got = do_urlencode([1, 2, 3])
    assert isinstance(got, str)
    assert got == '1=%201&2=%202&3=%203'

    got = do_urlencode('foo')
    assert isinstance(got, str)
    assert got == 'foo'

    got = do_urlencode({'foo': 'bar'})
    assert isinstance(got, str)
    assert got == 'foo=bar'

    got = do_urlencode({'foo': 'bar', 'baz': 'qux'})
    assert isinstance(got, str)
    assert got == 'foo=bar&baz=qux'


# Generated at 2022-06-13 12:24:36.977131
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()


# Generated at 2022-06-13 12:24:40.151220
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.utils.urls import url_query_parameter
    value = url_query_parameter('https://example.com/a/b/c?a=b&c=d', 'a')
    assert value == "b"


# Generated at 2022-06-13 12:24:53.210551
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("/") == "%2F"
    assert unicode_urlencode("/test/") == "%2Ftest%2F"
    assert unicode_urlencode("test") == "test"
    assert unicode_urlencode("test with space") == "test+with+space"
    assert unicode_urlencode("test with space") == "test+with+space"
    assert unicode_urlencode("test+with+plus") == "test%2Bwith%2Bplus"
    assert unicode_urlencode("test  with  multiple spaces") == "test++with++multiple+spaces"
    # verify that unicode strings are handled correctly
    assert unicode_urlencode(u"/test/") == "%2Ftest%2F"
    assert unicode_urlen

# Generated at 2022-06-13 12:24:57.528557
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert filters['urldecode'].__name__ == 'do_urldecode'
    assert not HAS_URLENCODE or filters['urlencode'].__name__ == 'do_urlencode'

# Generated at 2022-06-13 12:25:05.487743
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Patching os.path
    FilterModule_filters_os_path = 'ansible.module_utils.six.moves.urllib.parse.quote_plus'
    FilterModule_filters_unicode_os_path = 'ansible.module_utils.six.moves.urllib.parse.quote'
    with mock.patch(FilterModule_filters_os_path) as MockClass2:
        MockClass2.return_value = 'test_quote_plus'
        with mock.patch(FilterModule_filters_unicode_os_path) as MockClass3:
            MockClass3.return_value = 'test_quote'
            m = FilterModule()
            assert m.filters()['urldecode']('test_urldecode') == 'test_urldecode'
            assert m

# Generated at 2022-06-13 12:25:11.064885
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']('http%3A%2F%2Fwww.example.com') == 'http://www.example.com'
    if not HAS_URLENCODE:
        assert FilterModule().filters()['urlencode']({'key1': 'value1', 'key2': 'value2'}) == 'key2=value2&key1=value1'

# Generated at 2022-06-13 12:25:21.677892
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Ansible recognizes "FilterModule" as a core filter plugin
    assert 'FilterModule' in __loader__.name
    # jinja2 instantiates "FilterModule"
    assert isinstance(__loader__.filters, FilterModule)
    # jinja2 passes 'filters' method to Ansible
    assert hasattr(__loader__.filters, 'filters')
    # Ansible uses 'filters' method to register filters at runtime
    assert callable(__loader__.filters.filters)

    # Ansible passes ansible.module_utils.six to jinja2
    assert hasattr(ansible.module_utils.six, 'string_types')

    # Verify that url filters are implemented by Jinja2
    filters = __loader__.filters.filters()
    assert isinstance(filters, dict)


# Generated at 2022-06-13 12:25:28.604182
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    class DummyModule(object):
        def __init__(self, params):
            self.params = params

    class DummyPlugin(object):
        def get_option(self, option):
            return self.options.get(option)

        def set_options(self, options):
            self.options = options

        def filters(self):
            return {
                'myfilter': lambda x: x,
            }

    fmodule = FilterModule()
    filters = fmodule.filters()

    assert 'urldecode' in filters

    assert filters['urldecode'].__name__ == \
        do_urldecode.__name__

# Generated at 2022-06-13 12:25:39.834931
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:25:49.898370
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    a_dict = {'key_1': 'value_1',
              'key_2': 'value_2',
              'key_3': 'value_3'}

    a_list = ['value_1', 'value_2', 'value_3']

    a_string = 'value_1'

    # test urldecode
    assert unicode_urldecode(a_string) == do_urldecode(a_string)
    assert unicode_urldecode(a_list) == do_urldecode(a_list)
    assert unicode_urldecode(a_dict) == do_urldecode(a_dict)

    # test urlencode
    assert unicode_urlencode(a_string) == do_urlencode(a_string)
    assert unicode

# Generated at 2022-06-13 12:25:58.340492
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'parameters%5B0%5D%5Bname%5D=path') == u'parameters[0][name]=path'
    assert unicode_urldecode(u'parameters%5B0%5D%5Bvalue%5D=%2Fhome%2Fbob%2Fpublic_html%2Ftest.php') == u'parameters[0][value]=/home/bob/public_html/test.php'
    assert unicode_urldecode(u'jvm') == u'jvm'
    assert unicode_urldecode(u'%2Fopt%2Fapps%2Ftomcat%2Fwebapps%2Fmanager') == u'/opt/apps/tomcat/webapps/manager'
    assert unicode_ur

# Generated at 2022-06-13 12:25:59.683575
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%2F%2F") == "/%2F"


# Generated at 2022-06-13 12:26:01.736190
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode('%20') == '%20'
    else:
        assert unicode_urldecode('%20') == u'%20'



# Generated at 2022-06-13 12:26:11.016190
# Unit test for function do_urlencode
def test_do_urlencode():
    # test strings
    value = 'This string should be URL encoded'
    value_utf8 = u'パスワード'

    # test dict
    value_dict = {'key': 'value', 'a key': 'a value'}
    value_dict_utf8 = {u'パスワード': u'パスワード'}

    # test list
    value_list = ['key', 'a key']
    value_list_utf8 = [u'パスワード', u'パスワード']

    # test tuple
    value_tuple = ('key', 'a key')
    value_tuple_utf8 = (u'パスワード', u'パスワード')

    # value tests

# Generated at 2022-06-13 12:26:14.405197
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://www.example.com?x=1&y=2') == 'http%3A//www.example.com%3Fx%3D1%26y%3D2'
    assert unicode_urlencode('http://www.example.com?x=1&y=2', for_qs=True) == 'http%3A%2F%2Fwww.example.com%3Fx%3D1%26y%3D2'
    assert unicode_urlencode({'x': '1', 'y': '2'}) == 'x=1&y=2'

# Generated at 2022-06-13 12:26:23.328918
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    def check(s, e):
        result = unicode_urlencode(to_text(s))
        assert result == e, "encoding of %s failed, expected %s but got %s" % (s, e, result)

    check('', '')
    check('abc', 'abc')
    check('abc def', 'abc%20def')
    check('abc+def', 'abc%2Bdef')
    check('abc/def', 'abc%2Fdef')
    check('abc?def', 'abc%3Fdef')
    check('http://www.example.com', 'http%3A%2F%2Fwww.example.com')
    check('http://www.example.com/sp ace', 'http%3A%2F%2Fwww.example.com%2Fsp%20ace')


# Generated at 2022-06-13 12:26:33.347318
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://example.org/~user') == u'http%3A//example.org/~user'
    assert unicode_urlencode(u'http://example.org/~user', for_qs=True) == u'http%3A%2F%2Fexample.org%2F%7Euser'
    assert unicode_urlencode(u'http://example.org/~user/') == u'http%3A//example.org/%7Euser/'
    assert unicode_urlencode(u'http://example.org/~user/', for_qs=True) == u'http%3A%2F%2Fexample.org%2F%7Euser%2F'

# Generated at 2022-06-13 12:26:41.328970
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json
    import sys
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str'),
            am_i_python2=dict(type='bool'),
            before=dict(type='bool'),
            encoded=dict(type='bool'),
        ),
        supports_check_mode=True,
    )
    data = module.params.get('data')
    am_i_python2 = module.params.get('am_i_python2')
    before = module.params.get('before')
    encoded = module.params.get('encoded')

    if PY3:
        assert data is None
    else:
        if before is True:
            data = do_urlencode(data)

# Generated at 2022-06-13 12:26:49.988417
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc123') == 'abc123'
    assert unicode_urldecode('%26%2F%3D%3F%23%5B%5D') == '&/=?#[]'


# Generated at 2022-06-13 12:26:55.561828
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    test = FilterModule()
    assert test.filters()['urldecode']('%20') == ' '
    assert test.filters()['urldecode']('%7B%22a%22%3A%22b%22%7D') == '{"a":"b"}'
    assert test.filters()['urldecode']('%7B%22a%22%3A%5B%22b%22%5D%7D') == '{"a":["b"]}'
    assert test.filters()['urldecode']('%7B%22a%22%3A%5B%22b%22%2C%22c%22%5D%7D') == '{"a":["b","c"]}'

# Generated at 2022-06-13 12:27:05.415353
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('hello+world') == u'hello world'
    assert unicode_urldecode('this+%2B+that') == u'this + that'
    assert unicode_urldecode(u'unicode+%3D+%E2%9C%93') == u'unicode = ✔'
    assert unicode_urldecode('utf8+%3D+%E2%9C%93') == u'utf8 = ✔'
    assert unicode_urldecode('utf16+%3D+%FE%FF%00%E2%00%9C%00%93') == u'utf16 = \u2713'

# Generated at 2022-06-13 12:27:15.006131
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''Test function unicode_urldecode'''

    def test_case(string, expected):
        '''Run single test case'''
        actual = unicode_urldecode(string)
        assert actual == expected, 'unexpected result: %s != %s (type: %s != %s)' % (
            actual, expected, type(actual), type(expected))

    try:
        test_case(u'abc%20def', u'abc def')
        test_case(u'abc+def', u'abc def')
        test_case(u'abc%20def%2Bghi', u'abc def+ghi')
        test_case(u'abc def', u'abc def')
    except Exception as err:
        print('Test failed: %s' % err)


# Generated at 2022-06-13 12:27:19.221504
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    # PY3
    if PY3:
        assert unicode_urldecode('abc') == 'abc'
    # PY2
    else:
        assert unicode_urldecode('abc') == u'abc'



# Generated at 2022-06-13 12:27:26.715391
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test cases from RFC 3986
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode('abc/def') == 'abc/def'
    assert unicode_urldecode('abc/def/') == 'abc/def/'
    assert unicode_urldecode('hello%2Dworld%21') == 'hello-world%21'
    assert unicode_urldecode('alice%2Cbob%2Crex') == 'alice,bob,rex'
    assert unicode_urldecode('/var/log//messages') == '/var/log//messages'
    assert unicode_urldecode('') == ''
    assert unicode_urldecode(None) is None


# Generated at 2022-06-13 12:27:28.999484
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filt = FilterModule()
    assert 'urldecode' in filt.filters()


# Generated at 2022-06-13 12:27:33.626400
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    """
    Check if unicode_urldecode, or do_urldecode, returns the
    expected result for ASCII strings
    """
    strings = [
        u'',
        u'hola',
        u'hola+amigo',
        u'hola%20amigo',
    ]
    for string in strings:
        assert unicode_urldecode(string) == string


# Generated at 2022-06-13 12:27:41.455725
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    filters = module.filters()
    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode
    assert isinstance(filters['urldecode']('test+test'), string_types)
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert filters['urlencode'] == do_urlencode
        assert isinstance(filters['urlencode']('test test'), string_types)



# Generated at 2022-06-13 12:27:49.277552
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%2B%C3%B6%C3%BC%C3%A4%C3%9F%24%C3%A4') == u'+öüäß$ä'
    assert unicode_urldecode(u'%40%40%40') == u'@@@'
    assert unicode_urldecode(u'%40%20%40') == u'@ @'
    assert unicode_urldecode(u'%40+%40') == u'@+@'
    assert unicode_urldecode(u'%40%2B%40') == u'@+@'



# Generated at 2022-06-13 12:27:57.507199
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Hello%2C+World%21') == 'Hello, World!'
    assert unicode_urldecode('Hello%2C+World%!') == 'Hello%2C+World%!'


# Generated at 2022-06-13 12:28:06.487396
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    try:
        import jinja2
    except ImportError:
        return
    assert unicode_urlencode(u'abc') == u'abc'
    assert unicode_urlencode([u'a=a', u'b=b']) == u'a%3Da&b%3Db'
    assert unicode_urlencode({u'a': u'a', u'b': u'b'}) == u'a%3Da&b%3Db'


# Generated at 2022-06-13 12:28:09.947001
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    expected_filters = {
        'urldecode': do_urldecode,
    }

    if not HAS_URLENCODE:
        expected_filters['urlencode'] = do_urlencode

    assert FilterModule().filters() == expected_filters

# Generated at 2022-06-13 12:28:14.324704
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%AB') == u'\xeb', 'unicode_urldecode() failed'
    assert unicode_urldecode('foo%2Fbar') == u'foo/bar', 'unicode_urldecode() failed'
    assert unicode_urldecode('foo+bar') == u'foo bar', 'unicode_urldecode() failed'


# Generated at 2022-06-13 12:28:21.802541
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%20b') == 'a b'
    assert unicode_urldecode('a+b') == 'a b'
    assert unicode_urldecode('a+b%20foo%26bar') == 'a b foo&bar'
    assert unicode_urldecode(u'a+b%20foo%26bar') == 'a b foo&bar'
    assert unicode_urldecode(b'a+b%20foo%26bar') == 'a b foo&bar'
    assert unicode_urldecode('a+b%3Dfoo%3Db%26bar') == 'a b=foo=b&bar'
    assert unicode_urldecode('a+b%3Dfoo%26bar') == 'a b=foo&bar'


# Generated at 2022-06-13 12:28:29.178507
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('abc%2F') == u'abc%2F'
    assert unicode_urldecode('abc%2F%253F') == u'abc%2F%3F'
    assert unicode_urldecode('abc%2F%3F') == u'abc%2F?'
    assert unicode_urldecode('abc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F') == u'abc//'


# Generated at 2022-06-13 12:28:31.689110
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/%3Fabc/') == '%2F%253Fabc%2F'
    assert unicode_urlencode({'a': 'b', 'c': 'd'}) == 'a=b&c=d'

# Generated at 2022-06-13 12:28:39.154817
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    class Dummy:
        def __iter__(self, *args, **kwargs):
            yield ('a', 'b')
            yield ('c', 'd')

    assert unicode_urlencode('a') == u'a'
    assert unicode_urlencode('a+') == u'a%2B'
    assert unicode_urlencode('a%') == u'a%25'
    assert unicode_urlencode('a/') == u'a%2F'
    assert unicode_urlencode('a ') == u'a'
    assert unicode_urlencode('a+', True) == u'a%2B'
    assert unicode_urlencode('a%', True) == u'a%25'

# Generated at 2022-06-13 12:28:44.925653
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    res = unicode_urldecode('%E6%B8%A9%E8%A9%A6')
    if res != u'温試':
        print('Error: urldecode for zh-CN failed')
    res = unicode_urldecode('%C5%BD')
    if res != u'Ž':
        print('Error: urldecode for cs-CZ failed')


# Generated at 2022-06-13 12:28:46.519237
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:28:59.201172
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u"a%2Bb") == u"a+b"
    assert unicode_urldecode(u"a%%2Bb") == u"a%2Bb"


# Generated at 2022-06-13 12:29:01.409013
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode'] is do_urldecode
    assert fm.filters()['urlencode'] is do_urlencode



# Generated at 2022-06-13 12:29:07.216611
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Test with strings
    assert unicode_urlencode(u'string with spaces') == 'string%20with%20spaces'
    assert unicode_urlencode(u'string with special chars: äéèç') == 'string%20with%20special%20chars:%20%C3%A4%C3%A9%C3%A8%C3%A7'
    assert unicode_urlencode(u'string with special chars: äéèç', for_qs=True) == 'string%20with%20special%20chars:%20%C3%A4%C3%A9%C3%A8%C3%A7'
    # Test with lists

# Generated at 2022-06-13 12:29:10.608743
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A4%20%C3%BC%20%C3%9F') == u'ä ü ß'

# Generated at 2022-06-13 12:29:21.141078
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%A4') == u'ä'
    assert unicode_urldecode(u'%C3%A4%C3%B6') == u'äö'
    assert unicode_urldecode(u'%C3%A4%C3%B6%C3%BC') == u'äöü'
    assert unicode_urldecode(u'%C3%A4%C3%B6%C3%BC%40%C3%84%C3%96%C3%9C') == u'äöü@ÄÖÜ'


# Generated at 2022-06-13 12:29:29.196656
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import unittest

    class FilterModule_filters_TestCase(unittest.TestCase):
        ''' Test case for FilterModule::filters() '''
        def test_FilterModule_filters_exists(self):
            ''' Ensure FilterModule::filters() exists'''
            extension = FilterModule()
            self.assertTrue(hasattr(extension, 'filters'))

        def test_FilterModule_filters_no_urldecode(self):
            ''' Ensure FilterModule::filters() doesn't have urldecode'''
            extension = FilterModule()
            filters = extension.filters()
            self.assertIsInstance(filters, dict)
            self.assertNotIn(b'urldecode', filters)


# Generated at 2022-06-13 12:29:35.322662
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    assert filter_module.filters()['urldecode']('an+example') == 'an example'
    if not HAS_URLENCODE:
        assert filter_module.filters()['urlencode']('/tmp/a b.c') == '%2Ftmp%2Fa%20b.c'
        assert filter_module.filters()['urlencode']({'a': 42, 'b': 43}) == 'a=42&b=43'

# Generated at 2022-06-13 12:29:37.285459
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A4') == u'\xe4'


# Generated at 2022-06-13 12:29:39.791858
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode(u'&=') == u'%26=', 'urlencode failed'



# Generated at 2022-06-13 12:29:48.777938
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    from ansible.compat.tests.mock import MagicMock
    from ansible.module_utils import basic

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus

    # Declare a simple module
    fm = FilterModule()
    class ModuleTest(AnsibleModule):
        def __init__(self, args):
            super(ModuleTest, self).__init__(
                argument_spec=(
                    {
                        'name': {'required': False, 'default': ''},
                    }
                )
            )
            self.params = args

# Generated at 2022-06-13 12:30:01.798676
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    for string, expected in [
        ('foo%20bar', 'foo bar'),
        ('foo+bar', 'foo bar'),
        ('foo%2Bar', 'foo+ar'),
        ('foo%2bar', 'foo+ar'),
    ]:
        yield check_unicode_urldecode, string, expected



# Generated at 2022-06-13 12:30:05.855817
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # PY2
    assert unicode_urldecode(u'a+b') == u'a b'

    # PY3
    assert unicode_urldecode('a+b') == 'a b'


# Generated at 2022-06-13 12:30:14.414468
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = 'a%20string%20with%20%2B%20encoded%20chars'
    assert unicode_urldecode(string) == 'a string with + encoded chars'
    string = u'a%20string%20with%20%2B%20encoded%20chars'
    assert unicode_urldecode(string) == 'a string with + encoded chars'
    string = 'a%20string%20with%20%2B%20encoded%20chars'
    assert unicode_urldecode(string) == 'a string with + encoded chars'
    string = 'a string with + encoded chars'
    assert unicode_urldecode(string) == 'a string with + encoded chars'
    string = 'a+string+with++encoded+chars'
    assert unic

# Generated at 2022-06-13 12:30:20.674114
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a+b') == u'a b'
    assert unicode_urldecode(u'c%2Bd') == u'c+d'

    assert unicode_urldecode(u'a%20b') == u'a b'
    assert unicode_urldecode(u'c+d') == u'c d'


# Generated at 2022-06-13 12:30:26.964282
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''Test for urldecode and urlencode filters defined in FilterModule class'''
    # Test for urldecode
    assert do_urldecode('/a/b/c') == '/a/b/c', 'Output should be "/a/b/c"'
    # Test for urlencode
    assert do_urlencode('/a/b/c') == '/a%2Fb%2Fc', 'Output should be "/a%2Fb%2Fc"'
    assert do_urlencode('/a:b/c') == '/a%3Ab/c', 'Output should be "/a%3Ab/c"'

# Generated at 2022-06-13 12:30:31.226853
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%20%21%2a%26%3d%3b%40%23") == u' !*&=;@#'



# Generated at 2022-06-13 12:30:39.597708
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo') == u'foo'
    assert unicode_urldecode('%40') == u'@'
    assert unicode_urldecode('%F0%9F%92%A9') == u'\U0001f4a9'
    assert unicode_urldecode('%E2%80%BC') == u'\u20bc'
    assert unicode_urldecode('%3A') == u':'
    assert unicode_urldecode('%3a') == u':'


# Generated at 2022-06-13 12:30:45.943898
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%2Fb%3Bc%3Dd') == u'a/b;c=d'
    assert unicode_urldecode('a%E2%82%ACb') == u'a\u20ACb'
    assert unicode_urldecode('a%E2%82%ACb') == u'a\u20ACb'
    assert unicode_urldecode('a%3A%3Bc%3Dd') == u'a:;c=d'
    assert unicode_urldecode('a%3Fb%3Dc%3Bd') == u'a?b=c;d'


# Generated at 2022-06-13 12:30:48.054786
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C2%B1') == u'±'
    assert unicode_urldecode('a+b') == u'a b'


# Generated at 2022-06-13 12:30:51.748210
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    cases = dict(
        empty='',
        string='string',
        ustring=u'string',
        quote='a%20space',
        xy='a%20space',
        xyslash='a%20space/',
        xyfor='a%20space',
    )
    for test in cases:
        got = unicode_urlencode(cases[test])
        assert got == cases[test]

# Generated at 2022-06-13 12:31:05.092589
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    fm = FilterModule()
    filters = fm.filters()

    assert filters['urldecode']('a%2Bb') == 'a+b'

    assert filters['urlencode']('a+b') == 'a%2Bb'
    assert filters['urlencode']('a b') == 'a+b'
    assert filters['urlencode']({'a': 'b', 'c': 'd'}) == (
        'a=b&c=d'
    )
    assert filters['urlencode'](['a', 'b']) == 'a&b'


# Generated at 2022-06-13 12:31:15.251552
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Default action
    assert unicode_urlencode(u'a&b') == u'a%26b'

    # No safe characters
    assert unicode_urlencode(u'a&b', for_qs=True) == u'a%26b'

    # String
    assert unicode_urlencode(u'a/b') == u'a%2Fb'

    # Unicode
    assert isinstance(unicode_urlencode(u'a/b'), str)

    # Dictionary
    assert unicode_urlencode({'a': 'b'}) == u'a=b'
    assert unicode_urlencode({'a': u'b&c'}) == u'a=b%26c'
    assert unicode_urlencode({u'a': u'b&c'}) == u

# Generated at 2022-06-13 12:31:28.094886
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert unicode_urldecode("a+%20b") == "a b"
    assert unicode_urldecode("a+b") == "a b"
    assert unicode_urldecode("a%2Bb") == "a+b"
    assert unicode_urlencode("a b") == "a+b"
    assert unicode_urlencode("a b", for_qs=True) == "a+b"
    assert unicode_urlencode("a+b") == "a%2Bb"
    assert unicode_urlencode("a+b", for_qs=True) == "a%2Bb"

# Generated at 2022-06-13 12:31:30.017921
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert isinstance(filters['urldecode'], type(do_urldecode))


# Generated at 2022-06-13 12:31:35.734964
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # unicode_urldecode
    assert unicode_urldecode('%E4%BD%A0%E5%A5%BD') == u'你好'
    assert unicode_urldecode('%20%21%22%23%24%25%26%27%28%29%2A%2B%2C%2D%2E%2F%30') == u' !"#$%&\'()*+,-./0'
    assert unicode_urldecode('%E4%BD%A0%E5%A5%BD%F0%9F%99%84') == u'你好🙄'
    assert unicode_urldecode('+') == u'+'
    assert unicode_urldecode('%21') == u'!'


# Generated at 2022-06-13 12:31:40.034931
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('one two') == u'one+two'
    assert do_urlencode('/ /') == u'/+/'
    assert do_urlencode('/?/') == u'/?/'
    assert do_urlencode('/foo?/') == u'/foo?/'
    assert do_urlencode('/foo?bar/') == u'/foo%3Fbar/'
    assert do_urlencode({'a': 1, 'b': 2}) == u'a=1&b=2'
    assert do_urlencode(dict(a=1, b=2)) == u'a=1&b=2'
    assert do_urlencode([('a', 1), ('b', 2)]) == u'a=1&b=2'

# Generated at 2022-06-13 12:31:42.700807
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'\xe9', u'failed to decode utf-8'



# Generated at 2022-06-13 12:31:49.327546
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm
    assert fm.filters
    filters = fm.filters()
    assert filters
    assert dict == type(filters)
    assert len(filters) >= 1
    assert filters.get('urldecode')
    assert 'urldecode' in filters
    not_filters = ['non_existing_filter', '!', 'Tests']
    for not_filter in not_filters:
        assert not not_filter in filters


# Generated at 2022-06-13 12:31:57.209424
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    if not PY3:
        assert u"/a/b/c" == unicode_urldecode(u"%2Fa%2Fb%2Fc")
        assert u"/a/b/c" == unicode_urldecode(to_bytes(u"%2Fa%2Fb%2Fc"))
    else:
        assert u"/a/b/c" == unicode_urldecode(b"%2Fa%2Fb%2Fc")


# Generated at 2022-06-13 12:32:03.458317
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'abc123') == u'abc123'
    assert unicode_urldecode(u'abc+123') == u'abc 123'
    assert unicode_urldecode(u'abc%2B123') == u'abc+123'
    assert unicode_urldecode(u'abc%20def') == u'abc def'


# Generated at 2022-06-13 12:32:16.497965
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('some string %2B another string') == 'some string + another string'
    assert do_urlencode('some string + another string') == 'some+string+%2B+another+string'

# Generated at 2022-06-13 12:32:28.188868
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://example.org/foo') == u'http%3A%2F%2Fexample.org%2Ffoo'
    assert unicode_urlencode('http://example.org/foo', for_qs=True) == u'http%3A%2F%2Fexample.org%2Ffoo'
    assert unicode_urlencode('http://example.org/foo bar') == u'http%3A%2F%2Fexample.org%2Ffoo%20bar'
    assert unicode_urlencode('http://example.org/foo bar', for_qs=True) == u'http%3A%2F%2Fexample.org%2Ffoo+bar'
    assert unicode_urlencode(dict(a='b')) == u'a=b'


# Generated at 2022-06-13 12:32:33.842824
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # In Python 2, these are not unicode or byte strings
    string = "Il y a de l'espoir%21"
    assert unicode_urldecode(string) == "Il y a de l'espoir!"
    string = "%C3%A9l%C3%A9phant"
    assert unicode_urldecode(string) == u'éléphant'

# Generated at 2022-06-13 12:32:40.746228
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("foo") == b"foo"
    assert unicode_urlencode("foo bar") == b"foo%20bar"
    assert unicode_urlencode("foo+bar") == b"foo%2Bbar"
    assert unicode_urlencode("foo%20bar") == b"foo%20bar"
    assert unicode_urlencode("foo%2Fbar") == b"foo/bar"
    assert unicode_urlencode("foo/bar", for_qs=True) == b"foo%2Fbar"

# Generated at 2022-06-13 12:32:48.230044
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode([1, 2, 3]) == '1&2&3'
    assert do_urlencode('abcd') == 'abcd'
    assert do_urlencode(u'abcde') == u'abcde'
    assert do_urlencode({'a': b'b', 'c': 'd'}) == 'a=b&c=d'
    assert do_urlencode({'a': {'a': 'b'}, 'd': 'e'}) == 'a=a%3Db&d=e'


# Generated at 2022-06-13 12:32:57.393686
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    args = {
        'string': 'ansible',
        'value': {
            'k1': 'v1',
            'k2': 'v2'
        },
        'urlencode':{
            'None': None,
            'Empty list': [],
            'Empty tuple': (),
            'Empty set': set([]),
            'Empty dict': {}
        }
    }
    expected = {
        'urldecode': 'ansible',
        'urlencode': {
            'None': 'None',
            'Empty list': '',
            'Empty tuple': '',
            'Empty set': '',
            'Empty dict': ''
        }
    }
    fm = FilterModule()
    data = fm.filters()
    assert 'urldecode' in data

    result = data

# Generated at 2022-06-13 12:32:59.247277
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()

# Generated at 2022-06-13 12:33:01.907258
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import doctest
    import sys
    results = doctest.testmod(sys.modules[__name__])
    assert results.failed == 0

# Generated at 2022-06-13 12:33:04.499076
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%BC%3D%3d') == u'\xfc=='


# Generated at 2022-06-13 12:33:08.170461
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('') == ''
    assert unicode_urldecode('abc123') == 'abc123'
    assert unicode_urldecode('%41%42%43%31%32%33') == 'ABC123'


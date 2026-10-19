

# Generated at 2022-06-13 12:23:28.424977
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%31') == '1'
    assert unicode_urldecode('%31%32') == '12'
    assert unicode_urldecode('%31%32%33') == '123'
    assert unicode_urldecode('%25') == '%'
    assert unicode_urldecode('%2531') == '%1'


# Generated at 2022-06-13 12:23:33.152069
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' Return decoded unicode strings '''

    assert unicode_urldecode(u'abc') == u'abc'
    assert unicode_urldecode(u'abc+') == u'abc '
    assert unicode_urldecode(u'%C3%84') == u'Ä'


# Generated at 2022-06-13 12:23:43.184638
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == u'test'
    assert unicode_urlencode('test/') == u'test%2F'
    assert unicode_urlencode('test/') == u'test%2F'
    assert unicode_urlencode('test/') == u'test%2F'
    assert unicode_urlencode(u'test') == u'test'
    assert unicode_urlencode(u'test') == u'test'
    assert unicode_urlencode(u'test/') == u'test%2F'
    assert unicode_urlencode(u'test/') == u'test%2F'
    assert unicode_urlencode(u'test/') == u'test%2F'

# Generated at 2022-06-13 12:23:46.787155
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    res = f.filters()
    assert len(res) == 2
    assert res['urlencode'] == do_urlencode
    assert res['urldecode'] == do_urldecode


# Generated at 2022-06-13 12:23:57.517444
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'') == u''
    assert unicode_urlencode(u'hi there') == u'hi%20there'
    assert unicode_urlencode(u'this&that') == u'this%26that'
    assert unicode_urlencode(u'this&that', for_qs=True) == u'this%26that'
    assert unicode_urlencode(u'http://example.com/some/path') == u'http%3A//example.com/some/path'
    assert unicode_urlencode(u'http://example.com/some/path', for_qs=True) == u'http%3A%2F%2Fexample.com%2Fsome%2Fpath'

# Generated at 2022-06-13 12:24:07.075638
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert(unicode_urldecode('foobar') == u'foobar')
    assert(unicode_urldecode('foo+bar') == u'foo bar')
    assert(unicode_urldecode('foo%2B%20bar') == u'foo+ bar')
    assert(unicode_urldecode('%7B%22a%22%3A%22b%22%7D') == u'{"a":"b"}')
    assert(unicode_urldecode('%7B%22a%22%3A%22b%22%7D'.encode('utf-8')) == u'{"a":"b"}')
    assert(unicode_urldecode(b'foo+bar') == u'foo bar')

# Generated at 2022-06-13 12:24:11.572855
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    l = FilterModule().filters()
    assert l['urldecode']('%s %s' % (chr(0x2665), chr(0x2764))) == u'♥ ❤'
    assert l['urlencode']('♥ ❤') == '%E2%99%A5+%E2%9D%A4'

# Generated at 2022-06-13 12:24:15.636428
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert isinstance(fm, object)
    assert isinstance(fm.filters, object)
    assert 'urldecode' in fm.filters()
    assert 'urlencode' in fm.filters()


# Generated at 2022-06-13 12:24:20.816674
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ''' Unit test for method filters of class FilterModule '''
    # Create the object under test
    obj = FilterModule()

    # Verify that the method returns the correct dictionary
    assert obj.filters() == {
        'urldecode': do_urldecode,
        'urlencode': do_urlencode,
    }

# Generated at 2022-06-13 12:24:24.794370
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_string = 'this is a test'
    assert unicode_urlencode(test_string) == 'this%20is%20a%20test'
    assert unicode_urlencode(test_string, for_qs=True) == 'this+is+a+test'



# Generated at 2022-06-13 12:24:29.952764
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    assert filter_module.filters()['urldecode'] == do_urldecode
    assert filter_module.filters()['urldecode']('%3D') == '='

# Generated at 2022-06-13 12:24:36.934379
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%40') == '@'
    assert unicode_urldecode('%5E') == '^'
    assert unicode_urldecode('%60') == '`'
    assert unicode_urldecode('%7B') == '{'
    assert unicode_urldecode('%7C') == '|'
    assert unicode_urldecode('%7D') == '}'
    assert unicode_urldecode('%7E') == '~'

# Generated at 2022-06-13 12:24:42.725673
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%26%25%2B') == '&%+'
    assert unicode_urldecode('%25%21%40%24%25%5E%26*%28%29%3D%5B%5D%3B%2C%2F%3F%3E%3A%27%22%23%7C%5C%7E%60%20%5C%25') == '%!@$%^&*()=[];,/?>:\'\"#|\\~` \\%'


# Generated at 2022-06-13 12:24:53.803518
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert quote_plus(u'%') == u'%25' # special case
    assert unicode_urlencode(u'%') == u'%25' # special case

    assert quote_plus(u'\u0123') == u'%E1%88%A3' # ASCII
    assert unicode_urlencode(u'\u0123') == u'%E1%88%A3' # ASCII

    assert quote_plus(u'\u20ac') == u'%E2%82%AC' # non-ASCII
    assert unicode_urlencode(u'\u20ac') == u'%E2%82%AC' # non-ASCII


# Generated at 2022-06-13 12:24:55.683664
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%E5%85%B1%E5%92%8C%E5%9B%BD') == u'共和国'


# Generated at 2022-06-13 12:25:02.504007
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # list of possible parameters for method FilterModule.filters
    arguments = [None]

    # create the object
    f = FilterModule()
    for arg in arguments:
        print('Testing FilterModule.filters (arg={})'.format(arg))

        # prepare a new namespace
        namespace = {}

        # call the method
        result = f.filters(arg)
        namespace['result'] = result

        # retrieve the specific result we are looking for
        expected = namespace['result']

        # check if we got the expected result
        if result != expected:
            raise Exception('FilterModule.filters(arg={}) != {} (expected)'.format(arg, expected))


# Generated at 2022-06-13 12:25:12.949082
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/:?#[]@!$&\'()*+,;=%s' % chr(0xE9)) == u'/:?#[]@!$&\'()*+,;=%C3%A9'
    assert unicode_urlencode('/:?#[]@!$&\'()*+,;=%s' % chr(0xE9), True) == u'/:?#[]@!$&\'()*+,;=%C3%A9'

# Generated at 2022-06-13 12:25:23.400904
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json

    # Print the filter dictionary
    filter_obj = FilterModule()
    filter_method = filter_obj.filters()
    print("%s" % filter_method)
    print("%s"% filter_method.keys())

    filter_method_urlencode = filter_method.get("urlencode")
    if filter_method_urlencode:
        data = {
            'name': 'foo bar',
            'age': '12',
            'interest': ['movie', 'music'],
        }
        print("%s" % filter_method_urlencode(data))

    filter_method_urldecode = filter_method.get("urldecode")

# Generated at 2022-06-13 12:25:25.423632
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test = unicode_urldecode('hello%20world%21')
    assert test == u'hello world!'



# Generated at 2022-06-13 12:25:27.693332
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("80%2Ftcp") == "80/tcp"
    assert unicode_urldecode("80/udp") == "80/udp"


# Generated at 2022-06-13 12:25:36.158056
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.jinja2.filters.tests.test_urldecode import TestUrldecode
    from ansible.module_utils.jinja2.filters.tests.test_urlencode import TestUrlencode

    t1 = TestUrldecode()
    for test_name, test in iteritems(t1.test_raw):
        if not test.expected == do_urldecode(test.raw):
            print('urldecode filter is broken with test "%s"' % test_name)

    if HAS_URLENCODE:
        print("urlencode filter is not tested because Jinja2 has a native implementation")
    else:
        t2 = TestUrlencode()

# Generated at 2022-06-13 12:25:37.275237
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('dag%40wieers.com') == 'dag@wieers.com'


# Generated at 2022-06-13 12:25:38.700510
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E2%96%91%E2%96%90%E2%96%92%E2%96%8F%E2%96%8E') == u'\u256b\u2570\u256d\u2573\u2572'


# Generated at 2022-06-13 12:25:40.114692
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'abc%20def' == unicode_urldecode('abc+def')
    assert u'abc+' == unicode_urldecode('abc%2B')
    assert u'abc+def' == unicode_urldecode('abc+def')


# Generated at 2022-06-13 12:25:49.961006
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode']('foo%20bar') == 'foo bar'
    assert fm.filters()['urldecode']('foo+bar') == 'foo bar'
    assert fm.filters()['urldecode']('foo+bar%20') == 'foo bar '

    if not HAS_URLENCODE:
        assert fm.filters()['urlencode']('foo bar') == 'foo+bar'
        assert fm.filters()['urlencode']('foo bar ') == 'foo+bar+'
        assert fm.filters()['urlencode']('foo/bar') == 'foo%2Fbar'
        assert fm.filters()['urlencode']('foo bar') == 'foo+bar'

# Generated at 2022-06-13 12:25:58.403568
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('%2Fb') == u'/b'
    assert unicode_urldecode('%2F') == u'/'
    assert unicode_urldecode('%3d') == u'='
    assert unicode_urldecode('a%3db') == u'a=b'
    assert unicode_urldecode('a%2Fb') == u'a/b'
    assert unicode_urldecode('a%2F%3d%3Db%3D%3Dc') == u'a/=/=b==c'
    assert unicode_urldecode('%2F%2F%2F') == u'///'
    assert unicode_urldecode

# Generated at 2022-06-13 12:26:04.226384
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode']('a%20b') == 'a b'
    assert fm.filters()['urldecode']('a+b') == 'a b'
    assert fm.filters()['urldecode']('a/b') == 'a/b'
    assert fm.filters()['urldecode']('a%3Ab') != 'a%3Ab'
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode']('a b') == 'a+b'
        assert fm.filters()['urlencode']('a:b') == 'a%3Ab'

# Generated at 2022-06-13 12:26:05.596794
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()


# Generated at 2022-06-13 12:26:15.866394
# Unit test for function do_urlencode
def test_do_urlencode():
    from ansible.module_utils.six.moves.urllib.parse import (
        urlencode as std_urlencode,
        quote_plus as std_quote_plus,
    )
    for for_qs in (False, True):
        for u_string in (u'this string', True, None, 1, 1.0, [1], [1, 2], {1: 2}, {1: 2, 3: 4}):
            enc = std_urlencode(u_string) if for_qs else std_quote_plus(std_urlencode(u_string))
            assert do_urlencode(u_string) == enc


# Generated at 2022-06-13 12:26:25.203950
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    uarr = lambda *args: list(map(to_text, args))
    u = unicode_urlencode
    assert uarr(u(u('a b'))) == uarr('a%20b')
    assert uarr(u(u('a+b'))) == uarr('a%2Bb')
    assert uarr(u(u('a+b'), for_qs=True)) == uarr('a+b')
    assert uarr(u(u('a b'), for_qs=True)) == uarr('a+b')
    assert uarr(u(u('a b', for_qs=True))) == uarr('a+b')
    assert uarr(u(u('a b', for_qs=True), for_qs=True)) == uarr('a+b')

# Generated at 2022-06-13 12:26:33.580935
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Test that we have a urlencode filter
    fm = FilterModule()
    filters = fm.filters()
    assert 'urlencode' in filters

    # Test that we don't have a urldecode filter if it's not imported in lib/ansible/module_utils
    if not HAS_URLENCODE:
        assert 'urldecode' in filters

    # Test that we have a urldecode filter if it's imported in lib/ansible/module_utils
    if HAS_URLENCODE:
        assert 'urldecode' not in filters

# Generated at 2022-06-13 12:26:39.094806
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        s = u'%C3%85sterg%C3%B6tland'
        assert unicode_urldecode(s) == u'\u00c5sterg\u00f6tland'
    else:
        s = '%C3%85sterg%C3%B6tland'
        assert unicode_urldecode(s) == u'\xc5sterg\xf6tland'



# Generated at 2022-06-13 12:26:41.879851
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('') == u''
    assert unicode_urldecode('%26%23%27%20%21%20%25%20%26%20%27') == u"&#' ! % & '"


# Generated at 2022-06-13 12:26:42.698351
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%2F') == '/'


# Generated at 2022-06-13 12:26:51.526577
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # See: https://tools.ietf.org/html/rfc3986#page-12
    assert unicode_urldecode('my/uri') == u'my/uri'
    assert unicode_urldecode('my%2Furi') == u'my/uri'
    assert unicode_urldecode('my/uri%3B') == u'my/uri;'
    assert unicode_urldecode('my/uri%3b') == u'my/uri;'

    # See: https://tools.ietf.org/html/rfc3986#page-14
    assert unicode_urldecode('my/uri?query') == u'my/uri?query'

# Generated at 2022-06-13 12:26:59.314829
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'\u5929\u6d25\u5e02\u667a\u80fd\u6570\u7801\u90e8\u7f72') == '%E5%A4%A9%E6%B4%A5%E5%B8%82%E6%99%BA%E8%83%BD%E6%95%B0%E7%A0%81%E9%83%A8%E7%BD%B2'

# Generated at 2022-06-13 12:27:02.965765
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    '''Test for FilterModule class method filters'''
    assert FilterModule().filters()['urldecode'] == do_urldecode
    # NOTE: We implement urlencode when Jinja2 is older than v2.7
    if not HAS_URLENCODE:
        assert FilterModule().filters()['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:27:13.235350
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'dag') == u'dag'
    assert unicode_urlencode(u'http://www.example.org/') == u'http%3A%2F%2Fwww.example.org%2F'
    assert unicode_urlencode(u'http://www.example.org/') == u'http%3A%2F%2Fwww.example.org%2F'
    assert unicode_urlencode(u'dag/wieers') == u'dag%2Fwieers'
    assert unicode_urlencode(u'dag/wieers', for_qs=True) == u'dag%2Fwieers'



# Generated at 2022-06-13 12:27:17.400917
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule.filters(None)['urldecode']('Hello%20World%21') == 'Hello World!'
    if not HAS_URLENCODE:
        assert FilterModule.filters(None)['urlencode']('Hello World!') == 'Hello+World%21'

# Generated at 2022-06-13 12:27:19.486005
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import doctest

    results = doctest.testmod()
    assert results.failed == 0, results.__dict__

# Generated at 2022-06-13 12:27:24.619475
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode'] == do_urldecode
    # If Jinja2 has support for urlencode, do not add urlencode filter
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:27:30.198248
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fmod = FilterModule()
    filters = fmod.filters()

    assert 'urldecode' in filters
    assert filters['urldecode'] is do_urldecode

    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert filters['urlencode'] is do_urlencode
    else:
        assert 'urlencode' not in filters



# Generated at 2022-06-13 12:27:38.113318
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes, to_native, to_text
    # Converts unicode string to binary string
    if PY2:
        @to_native
        def to_native(text, errors='strict'):
            if isinstance(text, unicode):
                return text.encode('utf-8', errors)
            return text
    fm = FilterModule()
    # Test urlencode
    assert 'a%20b%20c' == fm.filters()['urlencode']('a b c')
    assert 'a%20b%20c%26' == fm.filters()['urlencode']('a b c&')

# Generated at 2022-06-13 12:27:43.062876
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('abc') == u'abc'
    assert unicode_urlencode(u'spam & eggs') == u'spam%20%26%20eggs'  # u'&'
    assert unicode_urlencode('€') == u'%E2%82%AC'
    assert unicode_urlencode(u'€') == u'%E2%82%AC'



# Generated at 2022-06-13 12:27:51.848803
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('%E4%BD%A0%E5%A5%BD') == u'你好'

# Generated at 2022-06-13 12:27:59.884616
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test decoding a non-unicode string
    assert unicode_urldecode('abc') == u'abc'

    # Test decoding an unicode string (a non-ascii character)
    assert unicode_urldecode(u'abç') == u'abç'

    # Test decoding a unicode string with a non-ascii character encoded
    # (Python 2)
    assert unicode_urldecode(u'ab%C3%A7') == u'abç'

    # Test decoding a unicode string with a non-ascii character encoded
    # (Python 3)
    assert unicode_urldecode('ab%C3%A7') == u'abç'

    # Test decoding a byte string with a non-ascii character encoded

# Generated at 2022-06-13 12:28:12.081677
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        func = unquote_plus
        inputs = [
            ('abc', 'abc'),
            ('abc_def', 'abc_def'),
            ('abc%40', 'abc@'),
            ('abc%40def', 'abc@def'),
            ('abc%40def%5Eghi%2Fjkl', 'abc@def^ghi/jkl'),
        ]
    else:
        func = to_text

# Generated at 2022-06-13 12:28:17.551541
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a=1&b=2') == u'a=1&b=2'
    assert unicode_urldecode(u'%41%3d%31%26%62%3d%32') == u'A=1&b=2'
    assert unicode_urldecode(u'%41%3D%31%26%62%3D%32') == u'A=1&b=2'
    assert unicode_urldecode(u'A=1&b=2') == u'A=1&b=2'
    assert unicode_urldecode(u'A=1&b=2') == u'A=1&b=2'

# Generated at 2022-06-13 12:28:19.521031
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A4%C3%B6%C3%BC') == u'äöü'


# Generated at 2022-06-13 12:28:24.156589
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Simple decoding
    assert unicode_urldecode('abcd') == 'abcd'

    # Unicode
    assert unicode_urldecode('%C3%BC') == u'ü'

    # Unicode + quoting
    assert unicode_urldecode('%25C3%25BC') == '%ü'



# Generated at 2022-06-13 12:28:31.196587
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%A4') == u'ä'
    assert unicode_urldecode(u'%C3%A4%C3%B6') == u'äö'
    assert unicode_urldecode(u'%C3%A4%C3%B6%C3%BC') == u'äöü'


# Generated at 2022-06-13 12:28:34.826002
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'') == u''
    assert unicode_urldecode(u'%') == u'%'
    assert unicode_urldecode(u'%2F') == u'/'
    assert unicode_urldecode(u'%25') == u'%'

# Generated at 2022-06-13 12:28:43.511830
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(None) == ""
    assert unicode_urldecode("") == ""
    assert unicode_urldecode("foo") == "foo"
    assert unicode_urldecode("foo+") == "foo "
    assert unicode_urldecode("foo%20") == "foo "
    assert unicode_urldecode("foo%25") == "foo%"
    assert unicode_urldecode("foo%255") == "foo%5"
    assert unicode_urldecode("+") == " "
    assert unicode_urldecode("%20") == " "



# Generated at 2022-06-13 12:28:44.887508
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filterModule = FilterModule()
    filterModule.filters()


# Generated at 2022-06-13 12:28:52.130133
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils._text import to_bytes

    fm = FilterModule()

    # test_urldecode
    assert fm.filters()['urldecode']('Dag') == 'Dag'
    assert fm.filters()['urldecode']('Dag&') == 'Dag&'
    assert fm.filters()['urldecode']('Dag%26') == 'Dag&'
    assert fm.filters()['urldecode']('Dag%20Wieers') == 'Dag Wieers'
    assert fm.filters()['urldecode']('%7Ba%20string%20value%7D') == '{a string value}'

    # test_urlencode
    if not HAS_URLENCODE:
        assert f

# Generated at 2022-06-13 12:29:00.128620
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode({'a': 1, 'b': 2}) == 'a=1&b=2'
    assert do_urlencode({'a': [1, 2]}) == 'a=1&a=2'
    assert do_urlencode(['a', 'b']) == 'a=b'
    assert do_urlencode('a=b&c') == 'a%3Db%26c'
    assert do_urlencode({}) == ''
    assert do_urlencode('') == ''
    assert do_urlencode(None) == ''
    assert do_urlencode(1) == '1'

# Generated at 2022-06-13 12:29:06.350952
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("") == u""
    assert unicode_urlencode("?") == u"%3F"
    assert unicode_urlencode("&") == u"%26"
    assert unicode_urlencode(";") == u"%3B"
    assert unicode_urlencode("/") == u"/"
    assert unicode_urlencode("=") == u"%3D"
    assert unicode_urlencode("%") == u"%25"
    assert unicode_urlencode("+") == u"%2B"
    assert unicode_urlencode(":") == u"%3A"
    assert unicode_urlencode("#") == u"%23"
    assert unicode_urlencode("[") == u"%5B"
   

# Generated at 2022-06-13 12:29:08.382028
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%F6") == u"ö"


# Generated at 2022-06-13 12:29:12.229129
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert isinstance(unicode_urldecode('a+b'), string_types)
    assert unicode_urldecode('a+b') == 'a+b'
    assert unicode_urldecode('%2B') == '+'



# Generated at 2022-06-13 12:29:16.986628
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    s = u'+'
    result = unicode_urldecode(s)
    # python2.6
    assert result == u' '

    s = u'%26'
    result = unicode_urldecode(s)
    assert result == u'&'

# Generated at 2022-06-13 12:29:32.085244
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import ansible.module_utils.basic
    from ansible.module_utils.six import assertRaisesRegex
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus
    from ansible.module_utils._text import to_bytes, to_native, to_text

    # Basic function tests for FilterModule.filters
    class TestBasicFilters(object):
        def test_urldecode(self):
            assert unquote_plus(to_bytes('%2F')) == to_native('/')
            assert unquote_plus(to_text('%2F')) == '/'
            assert unquote_plus('%2F') == '/'


# Generated at 2022-06-13 12:29:35.820077
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc%20def') == 'abc def'
    assert unicode_urldecode('abc%20def%20') == 'abc def '
    assert unicode_urldecode('%20') == ' '


# Generated at 2022-06-13 12:29:38.715825
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3A%2F%2Fexample.com') == 'http://example.com'



# Generated at 2022-06-13 12:29:45.058020
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'foo%2Fbar') == u'foo/bar'
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo%25bar') == u'foo%bar'



# Generated at 2022-06-13 12:29:48.077106
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == u'foo+bar'


# Generated at 2022-06-13 12:29:51.233877
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """ Tests FilterModule class filters function """
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters


# Generated at 2022-06-13 12:29:52.731182
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Hello%2C%20World%21') == u'Hello, World!'


# Generated at 2022-06-13 12:29:57.761655
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():  # pylint: disable=invalid-name,redefined-outer-name
    """
    Test FilterModule.filters()
    """

    # pylint: disable=missing-docstring
    import ansible.plugins.filter.core
    assert FilterModule.filters == ansible.plugins.filter.core.FilterModule.filters
    assert FilterModule.filters.__module__ == ansible.plugins.filter.core.FilterModule.filters.__module__

# Generated at 2022-06-13 12:30:03.358936
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo') == u'foo'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo+bar') == u'foo%2Bbar'
    assert unicode_urlencode(u'foo/bar') == u'foo/bar'
    assert unicode_urlencode(u'foo/bar', for_qs=True) == u'foo%2Fbar'
    assert unicode_urlencode(u'foo/bar/') == u'foo/bar/'
    assert unicode_urlencode(u'foo/bar/', for_qs=True) == u'foo%2Fbar%2F'
    assert unicode_urlencode(u'foo/bar?') == u

# Generated at 2022-06-13 12:30:07.215481
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('abc=') == u'abc%3D'
    assert do_urlencode({'a': 'b'}) == u'a=b'
    assert do_urlencode(['b', 'c']) == u'b&c'

# Generated at 2022-06-13 12:30:19.254906
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E2%82%AC%20rate') == '€ rate'
    assert unicode_urldecode('%E3%82%A2%E3%83%AA%E3%82%B8%E3%83%8A%E4%BB%8B%E7%B4%B9') == 'アリジナ介紹'
    assert unicode_urldecode('例如，%E7%A8%8B%E5%BA%8F%E5%91%98%E7%9A%84%E7%B8%A6%E5%8F%B7') == '例如，程序员的縦号'
    assert unicode_ur

# Generated at 2022-06-13 12:30:24.779482
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%7B%7B%20ansible_hostname%20%7D%7D') == u'{{ ansible_hostname }}'
    assert unicode_urldecode(u'%7B%7B%20ansible_hostname%20%7D%7D') == u'{{ ansible_hostname }}'


# Generated at 2022-06-13 12:30:36.690685
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic

    f = FilterModule()
    assert 'urldecode' in f.filters()

    assert f.filters()['urldecode']('http%3A%2F%2Fwww.exam%2Fle.com') == 'http://www.exam/le.com'
    assert do_urldecode('http%3A%2F%2Fwww.exam%2Fle.com') == 'http://www.exam/le.com'

    if not HAS_URLENCODE:
        assert 'urlencode' in f.filters()
        assert f.filters()['urlencode']('http://www.exam/le.com') == 'http%3A%2F%2Fwww.exam%2Fle.com'
        assert do_

# Generated at 2022-06-13 12:30:44.580235
# Unit test for function do_urlencode
def test_do_urlencode():
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus


# Generated at 2022-06-13 12:30:49.144772
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    def compare(expected, actual):
        if expected != actual:
            raise Exception('Expected %s, got %s.' % (expected, actual))

    compare(u'foo', unicode_urldecode(u'foo'))
    compare(u'foo bar', unicode_urldecode(u'foo+bar'))
    compare(u'foo bar', unicode_urldecode(u'foo%20bar'))
    compare(u'foo bar', unicode_urldecode(u'foo+%20bar'))



# Generated at 2022-06-13 12:30:50.482466
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%84') == u'Ä'



# Generated at 2022-06-13 12:30:56.332560
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urldecode('key%3Dval') == 'key=val'
    assert do_urldecode('key=val') == 'key=val'
    assert do_urldecode('key+val') == 'key val'
    assert do_urldecode('key+val%3D%26') == 'key val=&'

    assert do_urlencode('key=val') == 'key%3Dval'
    assert do_urlencode('key val') == 'key+val'
    assert do_urlencode('key val=&') == 'key+val%3D%26'
    assert do_urlencode({'key': 'val'}) == 'key=val'

# Generated at 2022-06-13 12:31:06.698750
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'f%C3%B6%C3%B6') == u'föö'
    assert unicode_urldecode(u'foo+%C3%B6') == u'foo ö'
    assert unicode_urldecode(u'foo+%E2%82%AC') == u'foo €'


# Generated at 2022-06-13 12:31:16.270332
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    string = u'https://github.com/ansible/ansible/\u2026/tree/devel/lib/ansible/plugins/filter'
    assert unicode_urlencode(string) == u'https://github.com/ansible/ansible/%E2%80%A6/tree/devel/lib/ansible/plugins/filter'
    assert unicode_urlencode(string, True) == u'https%3A%2F%2Fgithub.com%2Fansible%2Fansible%2F%E2%80%A6%2Ftree%2Fdevel%2Flib%2Fansible%2Fplugins%2Ffilter'

    string = 'https://github.com/ansible/ansible/\u2026/tree/devel/lib/ansible/plugins/filter'
   

# Generated at 2022-06-13 12:31:20.487283
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    url1 = 'http://www.example.com/path/%E8%87%AA%E7%94%B1?%E8%87%AA%E7%94%B1'
    url2 = 'http://www.example.com/path/自由?自由'
    assert unicode_urldecode(url1) == url2, 'Failed to unicode_urldecode'


# Generated at 2022-06-13 12:31:27.254184
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'


# Generated at 2022-06-13 12:31:33.436914
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils.six.moves.urllib.parse import unquote_plus as urldecode
    filtermod = FilterModule()
    assert isinstance(filtermod, basic.AnsibleModule)
    assert 'urldecode' in filtermod.filters()
    assert 'urlencode' in filtermod.filters()
    assert do_urldecode("%20") == " "
    assert do_urldecode("test%20it%21") == 'test it!'
    assert urldecode("test%20it%21") == 'test it!'
    assert do_urldecode("test+it+%28again%29%21") == 'test it (again)!'

# Generated at 2022-06-13 12:31:44.144673
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7B%22foo%22%3A%22bar%20%26%20baz%22%7D') == '{"foo":"bar & baz"}'
    assert unicode_urldecode('%7B%22foo%22%3A%22bar%20%26%20baz%22%7D', decode_plus=False) == '%7B%22foo%22%3A%22bar%20%26%20baz%22%7D'
    assert unicode_urldecode('%7B%22foo%22%3A%22bar%20%26%20baz%22%7D', decode_plus=True) == '{"foo":"bar & baz"}'



# Generated at 2022-06-13 12:31:48.539273
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%A4') == u'ä'
    assert unicode_urldecode(u'%F6') == u'ö'
    assert unicode_urldecode(u'%E4') == u'ä'


# Generated at 2022-06-13 12:32:01.097582
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'Basic%20dGVzdDp0ZXN0') == to_text(b'Basic dGVzdDp0ZXN0')
    assert unicode_urldecode(u'Basic%20dGVzdDp0ZXN0') == to_text(b'Basic dGVzdDp0ZXN0')
    assert unicode_urldecode(u'Basic%20%C3%A0%20%C3%A9%20%C3%AB%20%C3%A7') == to_text(b'Basic \xc3\xa0 \xc3\xa9 \xc3\xab \xc3\xa7')

# Generated at 2022-06-13 12:32:10.351892
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a+b') == u'a b'
    assert unicode_urldecode(u'a%20b') == u'a b'
    assert unicode_urldecode(u'a+%23+b') == u'a # b'
    assert unicode_urldecode(u'a%20%23%20b') == u'a # b'
    assert unicode_urldecode(u'%EA%B0%80%EC%88%98%EA%B8%B0') == u'가수기'
    assert unicode_urldecode(u'%xA1%xA2%xA3%xA4') == u'¡¢£¤'
    assert unicode_urldec

# Generated at 2022-06-13 12:32:15.369594
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filename = 'test_FilterModule_filters.py'
    fm = FilterModule()
    filters = fm.filters()

    load_name = 'AnsibleUndefined'
    for name, function in iteritems(filters):
        if name == 'urlencode' and HAS_URLENCODE:
            assert function == do_urlencode
        elif not hasattr(function, load_name):
            assert function == globals()['do_' + name]



# Generated at 2022-06-13 12:32:26.725486
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test Unicode bytes strings
    u_string = u'\u043f\u0440\u0438\u0432\u0435\u0442'
    u_string_bytes = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
    assert unicode_urldecode(u_string_bytes) == u_string

    # Test Unicode
    assert unicode_urldecode(u_string) == u_string

    # Test bytestring
    assert unicode_urldecode(u_string_bytes.decode('utf-8')) == u_string

    # Test empty string
    assert unicode_urldecode(u'') == u''

    # Test non-string
   

# Generated at 2022-06-13 12:32:30.652718
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"a/b+c?") == u"a%2Fb%2Bc%3F"
    assert unicode_urlencode(u"a/b+c?", for_qs=True) == u"a%2Fb%2Bc%3F"


# Generated at 2022-06-13 12:32:38.750706
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'unicode') == u'unicode'
    assert unicode_urlencode(u'unicode with spaces') == u'unicode+with+spaces'
    assert unicode_urlencode(u'unicode/with/slashes') == u'unicode%2Fwith%2Fslashes'
    assert unicode_urlencode(u'unicode with spaces/slashes') == u'unicode+with+spaces%2Fslashes'
    assert unicode_urlencode(u'unicode with spaces/slashes', for_qs=True) == u'unicode+with+spaces%2Fslashes'

# Generated at 2022-06-13 12:32:52.442664
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils.six import text_type
    if PY3:
        assert isinstance(unicode_urlencode('foo'), str)
    else:
        assert isinstance(unicode_urlencode('foo'), text_type)
    assert unicode_urlencode('foo') == 'foo'
    assert unicode_urlencode('foo/bar') == 'foo%2Fbar'
    assert unicode_urlencode('foo/bar', for_qs=True) == 'foo%2Fbar'
    assert unicode_urlencode(3) == '3'

    foo = {'a': 'b', 'c': 'd'}
    assert unicode_urlencode(foo) == 'a=b&c=d'

    foo = ['a', 'b', 'c']

# Generated at 2022-06-13 12:32:58.666759
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Example from https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL
    assert unicode_urldecode('https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FLearn%2FCommon_questions%2FWhat_is_a_URL') == 'https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL'

    # Example from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent

# Generated at 2022-06-13 12:33:06.643017
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'dag') == 'dag'
    assert unicode_urlencode(u'http://dag.wieers.com/') == 'http%3A%2F%2Fdag.wieers.com%2F'
    assert unicode_urlencode(u'http://dag.wieers.com/', for_qs=True) == 'http%3A%2F%2Fdag.wieers.com%2F'
    assert unicode_urlencode(u'http://dag.wieers.com/ © 2012') == 'http%3A%2F%2Fdag.wieers.com%2F%20%C2%A9%202012'

# Generated at 2022-06-13 12:33:14.563272
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode("%40%22%25%3b%27%3d%26") == "@\"%;'=&"
    assert do_urlencode("@\"%;'=&") == "%40%22%25%3b%27%3d%26"
    assert do_urlencode([("@", "\"%;'=&"), ("x", 1)]) == "%40=%22%25%3b%27%3d%26&x=1"
    assert do_urlencode({"@": "\"%;'=&", "x": 1}) == "%40=%22%25%3b%27%3d%26&x=1"

# Generated at 2022-06-13 12:33:17.683736
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert filters["urldecode"] == do_urldecode
    assert not HAS_URLENCODE or filters["urlencode"] == do_urlencode

# Generated at 2022-06-13 12:33:18.983075
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('a%20b%2Bc%2520d+e') == 'a b+c%20d e'


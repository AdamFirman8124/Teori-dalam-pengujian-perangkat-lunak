

# Generated at 2022-06-13 12:23:35.033776
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()

    assert filters['urldecode']('foo+bar+baz') == 'foo bar baz'

    if not HAS_URLENCODE:
        assert filters['urlencode']('foo bar') == 'foo+bar'
        assert filters['urlencode']('foo bar baz') == 'foo+bar+baz'
        assert filters['urlencode']('foo,bar,baz') == 'foo%2Cbar%2Cbaz'
        assert filters['urlencode']('foo bar baz') == 'foo+bar+baz'
        assert filters['urlencode']('foo%bar%baz') == 'foo%25bar%25baz'

# Generated at 2022-06-13 12:23:43.825281
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(b'%20') == b' '
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(b'%2B') == b'+'
    assert unicode_urldecode(u'%252B') == u'%2B'
    assert unicode_urldecode(b'%252B') == b'%2B'
    assert unicode_urldecode(u'%25252B') == u'%252B'
    assert unicode_urldecode(b'%25252B') == b'%252B'
    assert unicode_urldecode(u'%00') == u

# Generated at 2022-06-13 12:23:52.516571
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/') == '/'
    assert unicode_urlencode('/foo bar/') == '/foo%20bar/'
    assert unicode_urlencode('/foo?bar/') == '/foo%3Fbar/'
    assert unicode_urlencode('/foo+bar/') == '/foo%2Bbar/'
    assert unicode_urlencode('/foo bar/', for_qs=True) == '/foo+bar/'
    assert unicode_urlencode('/foo?bar/', for_qs=True) == '/foo%3Fbar/'
    assert unicode_urlencode('/foo+bar/', for_qs=True) == '/foo%2Bbar/'



# Generated at 2022-06-13 12:24:02.776324
# Unit test for function do_urlencode
def test_do_urlencode():
    import pytest

    def f(t, expected, for_qs=False):
        actual = do_urlencode(t)
        assert expected == actual

    # Test with empty string
    f(u'', u'')
    f(b'', b'')
    f('', '')

    # Test with string type
    f(u'a', u'a')
    f(b'a', b'a')
    f('a', 'a')

    # Test with a single byte
    f(u'\u00e9', u'%C3%A9')
    f(b'\u00e9', b'%C3%A9')
    f(b'\xc3\xa9', b'%C3%A9')

    # Test with a unicode string

# Generated at 2022-06-13 12:24:10.744058
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # function "unicode_urldecode" is placed in FilterModule,
    # so we need to reassign it
    global FilterModule
    FilterModule.unicode_urldecode = staticmethod(unicode_urldecode)
    FilterModule.unicode_urlencode = staticmethod(unicode_urlencode)

    module = FilterModule()
    filters = module.filters()
    assert "urldecode" in filters

    if not HAS_URLENCODE:
        assert "urlencode" in filters

# Generated at 2022-06-13 12:24:16.990863
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo+bar') == u'foo+bar'
    assert unicode_urldecode(u'foo%2Bbar') == u'foo+bar'
    assert unicode_urldecode(u'foo%2bbar') == u'foobar'



# Generated at 2022-06-13 12:24:18.850408
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("Hello%20World") == "Hello World"



# Generated at 2022-06-13 12:24:23.671818
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'f%C3%B6%C3%B6') == u'föö'
    assert unicode_urldecode(u'f%C3%B6%C3%B6'.encode('utf-8')) == u'föö'



# Generated at 2022-06-13 12:24:25.458128
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert '&' == unicode_urldecode('%26')


# Generated at 2022-06-13 12:24:31.303718
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Create an instance of FilterModule class.
    my_obj = FilterModule()

    en_str = "dag_wieers"
    url_en_str = my_obj.filters()['urlencode'](en_str)
    url_de_str = my_obj.filters()['urldecode'](url_en_str)
    assert (url_de_str == en_str)

# Generated at 2022-06-13 12:24:35.162762
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()


# Generated at 2022-06-13 12:24:40.175724
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test foo') == 'test%20foo'
    assert unicode_urlencode(1) == '1'
    assert unicode_urlencode(['t', 'e', 's', 't']) == 't&e&s&t'
    assert unicode_urlencode({'test': 'foo'}) == 'test=foo'
    assert unicode_urlencode({'test': 'foo=bar'}) == 'test=foo%3Dbar'


# Generated at 2022-06-13 12:24:49.589852
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo') == u'foo'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'http://example.com/foo/bar/') == u'http://example.com/foo/bar'
    assert unicode_urlencode(u'http://example.com/foo/bar/', for_qs=True) == u'http%3A//example.com/foo/bar'



# Generated at 2022-06-13 12:24:52.021551
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a+b') == u'a b'



# Generated at 2022-06-13 12:25:00.208964
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Testing bytes in Python 2
    if not PY3:
        assert unicode_urldecode(b'a%2Fb') == u'a/b'

    # Testing bytes in Python 3
    assert unicode_urldecode('a%2Fb') == u'a/b'

    # Testing non-ASCII unicode string
    # No matter the string is Python 2 unicode or Python 3 unicode,
    # when it's encoded by Python, it will be in the same form.
    assert unicode_urldecode('%E4%B8%AD%E6%96%87') == u'中文'



# Generated at 2022-06-13 12:25:06.556487
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_inputs = [
        (u'abc', u'abc'),
        (u'/abc/def/?', u'%2Fabc%2Fdef%2F%3F'),
        (u'/abc/def/?', u'%2Fabc%2Fdef%2F%3F'),
        (u'/abc/def/?', u'%2Fabc%2Fdef%2F%3F'),
        ({u'foo': u'bar'}, u'foo=bar'),
        ({u'foo': u'bar baz'}, u'foo=bar%20baz'),
        ((u'foo', u'bar'), u'foo=bar'),
        ([u'foo', u'bar'], u'foo=bar'),
    ]

    for input_value, expected_output in test_inputs:
        actual_

# Generated at 2022-06-13 12:25:09.643921
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']('a%2Fb%2Fc') == u'a/b/c'
    assert FilterModule().filters()['urldecode']('a%2Fb%2Fc') == u'a/b/c'

# Generated at 2022-06-13 12:25:20.158586
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # We expect to_text on the literals to succeed on Python 2 as well as Python 3
    for c in b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10':
        assert c not in to_text(unicode_urlencode('abc'))
        assert c not in to_text(unicode_urlencode(u'abc'))
    assert '%00' not in to_text(unicode_urlencode('abc'))
    assert '%00' not in to_text(unicode_urlencode(u'abc'))
    assert 'hello world' in to_text(unicode_urldecode('hello+world'))


# Generated at 2022-06-13 12:25:27.881302
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'é'
    assert unicode_urldecode('%2F') == u'/'
    assert unicode_urldecode('%2F/%2F') == u'///'
    assert unicode_urldecode('%2F%5C%2F') == u'//\\/'
    assert unicode_urldecode('%3Fa%3D1%26b%3D2') == u'?a=1&b=2'
    assert unicode_urldecode('%3Fa%3D1%26b%3D2%26c%3D3') == u'?a=1&b=2&c=3'


# Generated at 2022-06-13 12:25:28.604019
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # TODO
    pass



# Generated at 2022-06-13 12:25:32.461273
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('/a%20space/') == '/a space/'


# Generated at 2022-06-13 12:25:33.736085
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == '\u00e9'


# Generated at 2022-06-13 12:25:39.808306
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils import basic

    obj = basic.AnsibleModule(argument_spec=dict())
    assert unicode_urldecode(u'%20%21%2A%3B%3A%40%26%3D%2B%24%2C%2F%3F%25%23%5B%5D') == u' !*;:@&=+$,/?%#[]'
    assert unicode_urldecode(u'%2E%2E') == u'..'
    assert unicode_urldecode(u'%2F%5C') == u'/\\'
    assert unicode_urldecode(u'%2F%2F') == u'//'
    assert unicode_urldecode(u'/za%c4%bcan/')

# Generated at 2022-06-13 12:25:43.204012
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A9') == u'é'
    assert unicode_urldecode('%C3%A9%2B%2F') == u'é+/'


# Generated at 2022-06-13 12:25:51.691736
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('foo') == 'foo'
    assert unicode_urlencode(u'föo') == u'f%C3%B6o'
    assert unicode_urlencode(u'spåm') == u'sp%C3%A5m'
    assert unicode_urlencode(u'föo/bär') == u'f%C3%B6o/b%C3%A4r'
    assert unicode_urlencode(u'spåm/båz') == u'sp%C3%A5m/b%C3%A5z'
    assert unicode_urlencode(u'föo?bär') == u'f%C3%B6o%3Fb%C3%A4r'

# Generated at 2022-06-13 12:25:59.828958
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    # Simple test
    test_string = u"/var/log/suricata/eve.log"
    assert unicode_urldecode(test_string) == u"/var/log/suricata/eve.log"

    # Simple test with spaces
    test_string = u"/var/log/suricata/eve.log with spaces"
    assert unicode_urldecode(test_string) == u"/var/log/suricata/eve.log with spaces"

    # Test with urlencoded parts
    test_string = u"/var/log/suricata/eve.log with%20spaces"
    assert unicode_urldecode(test_string) == u"/var/log/suricata/eve.log with spaces"

    # Complex test with urlencoded parts
   

# Generated at 2022-06-13 12:26:03.974502
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("https%3A//www.ansible.com") == "https://www.ansible.com"


# Generated at 2022-06-13 12:26:11.727360
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('foo') == 'foo'
    assert unicode_urlencode('foo bar') == 'foo%20bar'
    assert unicode_urlencode('foo+bar') == 'foo%2Bbar'
    assert unicode_urlencode('foo+bar/foo') == 'foo%2Bbar%2Ffoo'
    assert unicode_urlencode('foo bar/foo') == 'foo%20bar%2Ffoo'
    assert unicode_urlencode('foo?bar=foo') == 'foo%3Fbar%3Dfoo'

    assert unicode_urlencode('foo', for_qs=True) == 'foo'
    assert unicode_urlencode('foo bar', for_qs=True) == 'foo+bar'

# Generated at 2022-06-13 12:26:13.409174
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter = FilterModule()
    assert filter.filters()['urldecode'] == do_urldecode

# Generated at 2022-06-13 12:26:16.502290
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'+') == u' '
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%%') == u'%%'


# Generated at 2022-06-13 12:26:23.359476
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # In:
    #   {'urlencode': 'urlencode', 'urldecode': 'urldecode'}
    # Out:
    #   {'urldecode': <function do_urldecode at 0x7f3f3bcb1de8>, 'urlencode': <function do_urlencode at 0x7f3f3bcb1f28>}
    fm = FilterModule()
    assert fm.filters() == {'urldecode': do_urldecode,
                            'urlencode': do_urlencode}


# Generated at 2022-06-13 12:26:29.873770
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert u'abc%26123=xyz%2B456' == unicode_urlencode({u'abc&123': u'xyz+456'})
    assert u'abc%26123=xyz%2B456' == unicode_urlencode([(u'abc&123', u'xyz+456')])
    assert u'12%2634%3D56' == unicode_urlencode(u'12&34=56')



# Generated at 2022-06-13 12:26:38.352301
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import pytest
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'
    assert unicode_urlencode(u'foo+bar') == u'foo%2Bbar'
    assert unicode_urlencode(u'foo&bar') == u'foo%26bar'
    assert unicode_urlencode(u'foo bar', True) == u'foo+bar'
    assert unicode_urlencode(u'foo+bar', True) == u'foo%2Bbar'
    assert unicode_urlencode(u'foo&bar', True) == u'foo%26bar'


# Generated at 2022-06-13 12:26:51.918781
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('foo bar') == 'foo%20bar'
    assert unicode_urlencode('foo+bar') == 'foo%2Bbar'
    assert unicode_urlencode('foo@bar') == 'foo%40bar'
    assert unicode_urlencode('foo bar', True) == 'foo+bar'
    assert unicode_urlencode(['foobar', 1, 2, 3]) == 'foobar&1&2&3'
    assert unicode_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert unicode_urlencode({'foo': 'bar', 'baz': 42}) == 'foo=bar&baz=42'

# Generated at 2022-06-13 12:26:58.169071
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if not HAS_URLENCODE:
        assert unicode_urlencode(u'http://example.com/path/') == u'http%3A//example.com/path/'
        assert unicode_urlencode(u'http://example.com/path/?foo=bar') == u'http%3A//example.com/path/%3Ffoo%3Dbar'
        assert unicode_urlencode(u'http://example.com/path/?foo=bar&key=value') == u'http%3A//example.com/path/%3Ffoo%3Dbar%26key%3Dvalue'



# Generated at 2022-06-13 12:27:04.712448
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Dumb test of urlencode
    from os import environ
    from sys import version_info

    if version_info < (2, 7):
        old = {}
        for key, value in environ.items():
            if not isinstance(value, unicode):
                old[key] = value
        environ.update(old)

    for key, value in environ.items():
        assert unicode_urlencode(key + value) == unicode_urldecode(do_urlencode(key + value))

# Generated at 2022-06-13 12:27:14.718293
# Unit test for function do_urlencode
def test_do_urlencode():
    basic_tests_string = {'foo bar': 'foo+bar', '???': '%3F%3F%3F'}
    basic_tests_dict = {'foo bar': 'foo+bar', '???': '%3F%3F%3F'}
    basic_tests_list = {'foo bar': 'foo+bar', '???': '%3F%3F%3F'}

    for k, v in iteritems(basic_tests_string):
        assert do_urlencode(k) == v
    for k, v in iteritems(basic_tests_dict):
        assert do_urlencode(dict([(k, v)])) == ('%s=%s' % (v, v))
    for k, v in iteritems(basic_tests_list):
        assert do_url

# Generated at 2022-06-13 12:27:24.734627
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test unicode_urldecode with a unicode string with 1 byte chars
    ret = unicode_urldecode(u'%C3%B6')
    assert ret == u'ö'

    # Test unicode_urldecode with a plain string with 1 byte chars
    if PY3:
        ret = unicode_urldecode(b'%C3%B6')
    else:
        ret = unicode_urldecode(str('%C3%B6'))
    assert ret == u'ö'

    # Test unicode_urldecode with a unicode string with 2 byte chars
    ret = unicode_urldecode(u'%E6%97%A5%E6%9C%AC%E8%AA%9E')

# Generated at 2022-06-13 12:27:29.033819
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] is do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] is do_urlencode


# Generated at 2022-06-13 12:27:30.509796
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'foo bar' == unicode_urldecode('foo+bar')

# Generated at 2022-06-13 12:27:41.571467
# Unit test for function do_urlencode
def test_do_urlencode():
    assert to_text(b'foo%3Dbar') == do_urlencode('foo=bar')
    assert to_text(b'foo%3Dbar') == do_urlencode(to_text(b'foo=bar'))
    assert to_text(b'foo%3Dbar') == do_urlencode(to_bytes(u'foo=bar'))
    assert to_text(b'foo%3Dbar%26baz%3Dbam') == do_urlencode('foo=bar&baz=bam')
    assert to_text(b'foo%3Dbar%26baz%3Dbam') == do_urlencode({'foo': 'bar', 'baz': 'bam'})
    assert to_text(b'foo%3Dbar%26baz%3Dbam')

# Generated at 2022-06-13 12:27:50.535709
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    filter_class = FilterModule()
    filters = filter_class.filters()

    assert filters['urldecode']('xyz%2Babc%2Fdef') == 'xyz+abc/def'
    assert filters['urldecode'](u'xyz%2Babc%2Fdef') == u'xyz+abc/def'
    assert filters['urldecode'](b'xyz%2Babc%2Fdef') == u'xyz+abc/def'

    assert filters['urldecode'](AnsibleUnsafeText('xyz%2Babc%2Fdef')) == 'xyz+abc/def'


# Generated at 2022-06-13 12:27:52.556061
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import warnings
    warnings.filterwarnings('always')

    print(repr(FilterModule().filters()))



# Generated at 2022-06-13 12:28:00.377136
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%C3%A9") == u"\u00e9"
    assert unicode_urldecode("%e3%83%a9%e3%83%bc%e3%83%a0+%e5%bc%95%e6%95%b0") == u"\u30e9\u30fc\u30e0 \u5f15\u6570"
    assert unicode_urldecode("%E3%83%A9%E3%83%BC%E3%83%A0+%E5%BC%95%E6%95%B0") == u"\u30e9\u30fc\u30e0 \u5f15\u6570"

# Generated at 2022-06-13 12:28:12.359810
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.text_utils import sha_hash
    import json

    with open('../../lib/ansible/module_utils/basic.py') as f:
        contents = f.read()

    # object to be hashed
    class Dummy(object):
        def __init__(self, text):
            self.text = text

    obj = Dummy(text=contents)

    # quick arbitrary test
    assert sha_hash(obj) == '0ad416e52f0cda1a1b36e1d8a2822c37135cbd85'

    # import filters within scope
    fm = FilterModule()
    filters = fm.filters()

    # test of sha_hash method within filters

# Generated at 2022-06-13 12:28:18.608274
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'hello world') == 'hello%20world'
    # Python 2 on Travis/Azure is not able to handle unicode_urlencode
    # assert unicode_urlencode(u'привет мир') == '%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82%20%D0%BC%D0%B8%D1%80'
    assert unicode_urlencode({'k1': 'v1', 'k2': 'v2'}) == 'k1=v1&k2=v2'
    assert unicode_urlencode(['k1', 'v1']) == 'k1&v1'

# Generated at 2022-06-13 12:28:19.382338
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()


# Generated at 2022-06-13 12:28:23.986496
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('http://example.org/?a=+%2F&b=%20+c%20+d') == 'http%3A%2F%2Fexample.org%2F%3Fa%3D%2B%252F%26b%3D%2520%2Bc%2520%2Bd'

# Generated at 2022-06-13 12:28:26.576565
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']('test%20test') == 'test test'
    assert FilterModule().filters()['urlencode']('test test') == 'test%20test'

# Generated at 2022-06-13 12:28:34.765990
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Dummy class
    class DummyClass(object):
        pass


# Generated at 2022-06-13 12:28:43.374218
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%C3%A4%C3%B6%C3%BC%C3%9F%C3%84%C3%96%C3%9C') == u'äöüßÄÖÜ'



# Generated at 2022-06-13 12:28:51.244243
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # test string types
    assert unicode_urlencode('https://www.ansible.com/') == to_text(b'https%3A//www.ansible.com/')
    assert unicode_urlencode('https://www.ansible.com/', for_qs=True) == to_text(b'https%3A%2F%2Fwww.ansible.com%2F')
    assert unicode_urlencode('/') == to_text(b'%2F')
    assert unicode_urlencode('/', for_qs=True) == to_text(b'%2F')

    # sequence types
    assert unicode_urlencode([1, 2, 3]) == to_text(b'1&2&3')

# Generated at 2022-06-13 12:29:00.968856
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves.urllib.parse import quote_plus
    assert FilterModule().filters()['urldecode']('a%20+%20%22quoted%22%20%26+an%26encoded%3D%3Dstring') == u'a   "quoted" & an&encoded==string'
    assert FilterModule().filters()['urldecode']('%F0%9F%98%B1') == u'\U0001f431'
    assert FilterModule().filters()['urldecode']('%F0%9F%98%B1%E2%82%AC') == u'\U0001f431\u20ac'

# Generated at 2022-06-13 12:29:03.873235
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """Unit test for method filters of class FilterModule"""
    module = FilterModule()
    assert isinstance(module.filters(), dict)
    for key in module.filters():
        assert callable(module.filters()[key])

# Generated at 2022-06-13 12:29:16.501325
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert u"%40%3A%2F%3F%23%5B%5D%40%21%24%26%27%28%29%2A%2B%2C%3B" == unicode_urlencode(u"@:/?#[]@!$&'()*+,;")
    else:
        assert u"%40%3A%2F%3F%23%5B%5D%40%21%24%26%27%28%29%2A%2B%2C%3B" == unicode_urlencode(u"@:/?#[]@!$&'()*+,;")

# Generated at 2022-06-13 12:29:23.810622
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if PY3:
        assert unicode_urldecode(b"foobar") == "foobar"
        assert unicode_urldecode("%E9%9D%9E%E5%A4%96%E9%83%A8%E5%85%B1%E8%AE%B8%E8%80%85") == u"éééééééé"
    else:
        assert unicode_urldecode(b"foobar") == u"foobar"

# Generated at 2022-06-13 12:29:33.534093
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Do not quote '/'
    assert unicode_urlencode(u'/a/b') == u'/a/b'
    # Do quote '+'
    assert unicode_urlencode(u'a+b') == u'a%2Bb'
    # Do quote non-alphanumeric
    assert unicode_urlencode(u'a&b=%') == u'a%26b%3D%25'
    # Do quote ' '
    assert unicode_urlencode(u' a ') == u'%20a%20'
    assert unicode_urlencode(u' a ', for_qs=True) == u'+a+'
    # Do quote '%' in query string

# Generated at 2022-06-13 12:29:43.930897
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import unittest

    class UnicodeUrlencodeTestMethods(unittest.TestCase):

        def test_unicode_urlencode(self):

            # test for unicode_urlencode function
            self.assertEqual(unicode_urlencode(to_text('/path/秘密/', 'utf-8')), '/path/%E7%A7%98%E5%AF%86/')
            self.assertEqual(unicode_urlencode(to_text('/path/秘密/', 'utf-8'), for_qs=True), '/path/%E7%A7%98%E5%AF%86/')

# Generated at 2022-06-13 12:29:53.313119
# Unit test for function do_urlencode
def test_do_urlencode():
    from ansible.module_utils import six
    if six.PY3:
        assert do_urlencode('hello world') == u'hello+world'
    else:
        assert do_urlencode('hello world') == u'hello%20world'
    assert do_urlencode(u'hello world') == u'hello+world'
    assert do_urlencode(u'hello@world') == u'hello%40world'
    assert do_urlencode(u'helloą') == u'hello%C4%85'
    assert do_urlencode(u'helloą'.encode('utf-8')) == u'hello%C4%85'
    assert do_urlencode(dict(a=1, b=2)) == u'a=1&b=2'
    assert do_

# Generated at 2022-06-13 12:29:59.398403
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    urldecode_tests = (
        ('Dag%20Wieers', u'Dag Wieers'),
        ('H%E5kan', u'H\xe5kan'),
        ('%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82', u'\u043f\u0440\u0438\u0432\u0435\u0442'),
    )

    for (u, v) in urldecode_tests:
        assert unicode_urldecode(u) == v



# Generated at 2022-06-13 12:30:13.419759
# Unit test for function unicode_urlencode
def test_unicode_urlencode():

    assert u'Hello%20World%21' == unicode_urlencode(u'Hello World!')
    assert u'hello%20world%21' == unicode_urlencode(u'hello world!')
    assert u'%E4%BD%A0%E5%A5%BD%EF%BC%8C%E4%B8%96%E7%95%8C' == unicode_urlencode(u'你好，世界')
    assert u'%E4%BD%A0%E5%A5%BD%EF%BC%8C%E4%B8%96%E7%95%8C' == unicode_urlencode(u'你好，世界'.encode('utf-8'))

# Generated at 2022-06-13 12:30:23.285383
# Unit test for function do_urlencode
def test_do_urlencode():
    from ansible.utils import _urlencode
    assert do_urlencode(None) == _urlencode(None)
    assert do_urlencode('foo') == _urlencode('foo')
    assert do_urlencode('foo/bar') == _urlencode('foo/bar')
    assert do_urlencode('foo bar') == _urlencode('foo bar')
    assert do_urlencode('foo+bar') == _urlencode('foo+bar')
    assert do_urlencode('foo%bar') == _urlencode('foo%bar')
    assert do_urlencode({'foo': 'bar'}) == _urlencode({'foo': 'bar'})

# Generated at 2022-06-13 12:30:35.232288
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo%3Abar') == u'foo:bar'
    assert unicode_urldecode(u'foo%3abar') == u'foo:bar'
    assert unicode_urldecode(to_bytes('foo+bar')) == u'foo bar'
    assert unicode_urldecode(to_bytes('foo%20bar')) == u'foo bar'
    assert unicode_urldecode(to_bytes('foo%3abar')) == u'foo:bar'

# Generated at 2022-06-13 12:30:39.092787
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("a%3Db") == "a=b"
    assert unicode_urldecode("http%3A%2F%2Fwww.example.com%2F") == "http://www.example.com/"



# Generated at 2022-06-13 12:30:43.276695
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''
    Test function unicode_urldecode
    '''
    string = u'a%20b%5Cc%5C%27d%5C%27%27%3Bxxx'
    res = unicode_urldecode(string)
    assert res == u'a b\\c\\\'d\\\'\';xxx'



# Generated at 2022-06-13 12:30:47.103255
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(u'foo%20bar') == u'foo bar'
    assert unicode_urldecode(u'foo+bar') == u'foo bar'
    assert unicode_urldecode(u'foo%2Bbar') == u'foo+bar'


# Generated at 2022-06-13 12:30:47.955126
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    test = FilterModule()
    assert test.filters()

# Generated at 2022-06-13 12:30:51.894016
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%21%23%26%27%28%29%2A%2B%2C%2F%3A%3B%3D%3F%40%5B%5D") == "!#&'()*+,/:;=?@[]"
    assert unicode_urldecode("%E6%B0%B4%E6%9E%9C") == "水果"

# Generated at 2022-06-13 12:30:55.471058
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%2F%2B%2F") == '/+/'
    assert unicode_urldecode("%2B") == '+'
    assert unicode_urldecode("a") == 'a'
    assert unicode_urldecode("%2Fa%2F%2B") == "/a/+"
    assert unicode_urldecode("/a/%2B") == "/a/+"


# Generated at 2022-06-13 12:31:07.055792
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # test_urldecode
    expected = "This & that"
    actual = do_urldecode("This+%26+that")
    assert expected == actual, "'%s' != '%s'" % (expected, actual)

    # test_urlencode
    expected = "This+%26+that"
    actual = do_urlencode("This & that")
    assert expected == actual, "'%s' != '%s'" % (expected, actual)
    expected = "This%26that"
    actual = do_urlencode("This&that")
    assert expected == actual, "'%s' != '%s'" % (expected, actual)

# Generated at 2022-06-13 12:31:25.449694
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%C3%A9") == u"\u00E9"
    assert unicode_urldecode("test1+test2+test3") == u"test1+test2+test3"
    assert unicode_urldecode("test1%2Btest2%2Btest3") == u"test1+test2+test3"


# Generated at 2022-06-13 12:31:28.501198
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%E4%B8%AD%E6%96%87') == u'中文'
    assert unicode_urldecode(b'%E4%B8%AD%E6%96%87') == u'中文'



# Generated at 2022-06-13 12:31:37.726238
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    #### url encode filter tests
    filter_module = FilterModule()
    assert do_urlencode(u'http://foo.bar/') == u'http%3A%2F%2Ffoo.bar%2F'
    assert do_urlencode(u'http://foo.bar/~user') == u'http%3A%2F%2Ffoo.bar%2F~user'
    assert do_urlencode(u'http://foo.bar/?foo=bar') == u'http%3A%2F%2Ffoo.bar%2F%3Ffoo%3Dbar'

# Generated at 2022-06-13 12:31:47.745241
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'urlencode+') == u'urlencode%2B'
    assert unicode_urlencode(u'urlencode ') == u'urlencode%20'
    assert unicode_urlencode(u'urlencode/') == u'urlencode%2F'
    assert unicode_urlencode(u'urlencode+', for_qs=True) == u'urlencode%2B'
    assert unicode_urlencode(u'urlencode ', for_qs=True) == u'urlencode+'
    assert unicode_urlencode(u'urlencode/', for_qs=True) == u'urlencode%2F'



# Generated at 2022-06-13 12:31:54.775626
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert not hasattr(FilterModule, 'test_FilterModule_filters')
    assert not HAS_URLENCODE
    assert FilterModule.filters()['urlencode'] == do_urlencode
    assert FilterModule.filters()['urldecode'] == do_urldecode
    assert FilterModule.filters()['urlencode']('abcd') == 'abcd'
    assert FilterModule.filters()['urldecode']('abcd') == 'abcd'
    assert FilterModule.filters()['urlencode']('http://www.example.com/') == 'http%3A//www.example.com/'
    assert FilterModule.filters()['urldecode']('http%3A//www.example.com/') == 'http://www.example.com/'

# Generated at 2022-06-13 12:32:02.150463
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert(unicode_urlencode('foo bar') == 'foo%20bar')
    assert(unicode_urlencode('foo bar', for_qs=True) == 'foo+bar')
    assert(unicode_urlencode({'foo': 'bar'}) == 'foo=bar')
    assert(unicode_urlencode({'foo': 'bar', 'bar': 'baz'}) == 'bar=baz&foo=bar')

# Generated at 2022-06-13 12:32:03.896333
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    text = "%C3%A9"
    assert unicode_urldecode(text) == u"é"



# Generated at 2022-06-13 12:32:12.899035
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('example.com/test') == 'example.com/test'
    assert unicode_urldecode('example.com/%7Etest') == 'example.com/~test'
    assert unicode_urldecode('example.com/%7Etest/test%5E') == 'example.com/~test/test^'
    assert unicode_urldecode('example.com/%7Etest/test%5E%26') == 'example.com/~test/test^&'
    assert unicode_urldecode('example.com/test%26%26test') == 'example.com/test&&test'

# Generated at 2022-06-13 12:32:18.302448
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Unit test for function unicode_urldecode
    assert unicode_urldecode('%C3%B6%20%C3%A4%20%C3%BC%20%C3%9F') == u'ö ä ü Ÿ'
    assert unicode_urldecode('%c3%b6%20%c3%a4%20%c3%bc%20%c3%9f') == u'ö ä ü Ÿ'
    assert unicode_urldecode('%FC%F6%20%DC%E4%20%C4%D6%20%DF') == u'Üö üä ÄÖ ß'

# Generated at 2022-06-13 12:32:25.441404
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    '''To run test with pytest:
    pip install pytest
    py.test test_unicode_urlencode.py
    '''
    assert unicode_urlencode('/') == '/'
    assert unicode_urlencode('/', for_qs=True) == '%2F'
    assert unicode_urlencode('/') != '%2F'
    assert unicode_urlencode('/', for_qs=True) != '/'


# Generated at 2022-06-13 12:32:41.840520
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'\u6709\u52b9') == b'%E6%9C%89%E5%8A%B9'
    assert unicode_urlencode(u'\u6709\u52b9', for_qs=True) == b'%E6%9C%89%E5%8A%B9'
    assert unicode_urlencode(u'foo bar') == b'foo%20bar'
    assert unicode_urlencode(u'foo bar', for_qs=True) == b'foo+bar'



# Generated at 2022-06-13 12:32:46.453262
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%C3%A9+%C3%A8') == u'é è'
    assert unicode_urldecode(u'%C3%A9+%C3%A8'.encode('utf-8')) == u'é è'


# Generated at 2022-06-13 12:32:48.997624
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%E2%82%AC") == u"€"
    assert unicode_urldecode("invalid+escape%++encoding") == u"invalid+escape%++encoding"


# Generated at 2022-06-13 12:32:55.777488
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:33:00.648765
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%20') == u'%20'
    assert unicode_urldecode(u'%25') == u'%'
    assert unicode_urldecode(u'%2B') == u'+'
    assert unicode_urldecode(u'%26') == u'&'
    assert unicode_urldecode(u'%3D') == u'='
    assert unicode_urldecode(u'%2F') == u'/'
    assert unicode_urldecode(u'%26') == u'&'
    assert unicode_urldecode(u'%3F') == u'?'


# Generated at 2022-06-13 12:33:04.410100
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert unicode_urldecode('%F6%E9') == 'öé'
    assert unicode_urlencode('öé') == '%C3%B6%C3%A9'
    assert unicode_urlencode('öé', for_qs=True) == '%C3%B6%C3%A9'

# Generated at 2022-06-13 12:33:13.861038
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_str = "http://www.example.com/foo bar/baz.html?arg=value使用可能な文字"
    test_str_unicode = u"http://www.example.com/foo bar/baz.html?arg=value使用可能な文字"
    result_str = "http%3A%2F%2Fwww.example.com%2Ffoo%20bar%2Fbaz.html%3Farg%3Dvalue%E4%BD%BF%E7%94%A8%E5%8F%AF%E8%83%BD%E3%81%AA%E6%96%87%E5%AD%97"
    assert unicode_urlencode(test_str) == result_str
    assert unic

# Generated at 2022-06-13 12:33:18.784276
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Arrange
    expected_filters = {
        'urldecode': do_urldecode,
    }

    if not HAS_URLENCODE:
        expected_filters['urlencode'] = do_urlencode

    # Act
    fm = FilterModule()
    filters = fm.filters()

    # Assert
    assert filters == expected_filters

# Generated at 2022-06-13 12:33:23.772944
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    # Input parameters to the method
    test_filter_module = FilterModule()

    # Get the method under test
    test_filter_module_filters_method = test_filter_module.filters()

    # Testing if the method returns expected value on passing valid parameters
    assert(test_filter_module_filters_method['urldecode'] == do_urldecode)
    #assert(test_filter_module_filters_method['urlencode'] == do_urlencode)
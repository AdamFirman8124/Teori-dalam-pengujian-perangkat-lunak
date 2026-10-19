

# Generated at 2022-06-13 12:23:25.825835
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filt = FilterModule()
    filters = filt.filters()

    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode



# Generated at 2022-06-13 12:23:37.679781
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    for test, expected in [
            # Already decoded
            ('a', 'a'),
            # Space
            ('a+b', 'a b'),
            ('a%20b', 'a b'),
            # Backslash
            ('a\+b', 'a+b'),
            ('a%2Bb', 'a+b'),
            # Percent sign
            ('a%25b', 'a%b'),
            # Other characters
            ('a+%81%82%83b', 'a+\u3041\u3042\u3043b'),
            ('a%E3%81%82%E3%81%84b', 'a\u3042\u3044b'),
            ]:
        assert unicode_urldecode(test) == expected


# Generated at 2022-06-13 12:23:45.484939
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://example.com/') == u'http%3A//example.com/'
    assert unicode_urlencode(u'http://example.com/', for_qs=True) == u'http%3A%2F%2Fexample.com%2F'
    assert unicode_urlencode({'a': 'b', 'c': 'd'}, for_qs=True) == u'a=b&c=d'
    assert unicode_urlencode([['a', 'b'], ['c', 'd']], for_qs=True) == u'a=b&c=d'


if __name__ == '__main__':
    # Unit test this module
    import pytest


# Generated at 2022-06-13 12:23:49.769861
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filters = FilterModule().filters()
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode
    assert filters['urldecode'] == do_urldecode

# Unit tests for method do_urldecode

# Generated at 2022-06-13 12:23:55.218554
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()

    assert 'urldecode' in filters
    assert filters['urldecode'] == do_urldecode

    assert 'urlencode' in filters
    if HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode
    else:
        assert filters['urlencode'] != do_urlencode


# Generated at 2022-06-13 12:23:58.472017
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('test%2ftest') == u'test/test'
    assert unicode_urldecode('test%2ftest') == u'test/test'



# Generated at 2022-06-13 12:24:02.333541
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'foo bar' == unicode_urldecode('foo%20bar')
    assert u'foo+bar' == unicode_urldecode('foo+bar')
    assert u'foo bar' == unicode_urldecode('foo+bar')


# Generated at 2022-06-13 12:24:04.805059
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('http%3A%2F%2Fexample.org%2Fexample') == 'http://example.org/example'



# Generated at 2022-06-13 12:24:09.458203
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # check if unquote_plus works correct
    assert unicode_urldecode(b'%2B') == b'+'
    assert unicode_urldecode('%2B') == '+'

    # check if the character is unicode
    assert unicode_urldecode(u"%2B") == u"+"
    assert unicode_urldecode(u"%E3%81%82") == u"あ"



# Generated at 2022-06-13 12:24:20.490632
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'123') == u'123'
    assert unicode_urlencode(u'a b') == u'a%20b'
    assert unicode_urlencode(u'a+b') == u'a%2Bb'
    assert unicode_urlencode(u'a/b') == u'a%2Fb'
    assert unicode_urlencode(u'a:b') == u'a:b'
    assert unicode_urlencode(u'a:b', for_qs=True) == u'a%3Ab'

    assert unicode_urlencode(1) == u'1'
    assert unicode_urlencode(1.2) == u'1.2'

# Generated at 2022-06-13 12:24:28.039164
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # method filters of class FilterModule with arguments
    filters = FilterModule().filters()
    assert filters['urldecode'].__name__ == 'do_urldecode'

    # urlencode
    if not HAS_URLENCODE:
        assert filters['urlencode'].__name__ == 'do_urlencode'



# Generated at 2022-06-13 12:24:30.488479
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'test%20example%20string') == u'test example string'



# Generated at 2022-06-13 12:24:38.825496
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo') == u'foo'
    assert unicode_urldecode('foo%20bar') == u'foo bar'
    assert unicode_urldecode('%C3%A0%C3%A8%C3%B2%C3%B9%20bar') == u'àèòù bar'
    assert unicode_urldecode(u'%C3%A0%C3%A8%C3%B2%C3%B9%20bar') == u'àèòù bar'

# Generated at 2022-06-13 12:24:51.410564
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test_cases = (
        (u'', u''),
        (u'%', u'%'),
        (u'+', u' '),
        (u'A', u'A'),
        (u'A%', u'A%'),
        (u'A%2', u'A%2'),
        (u'A%2B', u'A+'),
        (u'A%2b', u'A+'),
        (u'A%2Bc', u'A+c'),
        (u'A%26c', u'A&c'),
    )

    for test_input, test_output in test_cases:
        assert unicode_urldecode(test_input) == test_output


# Generated at 2022-06-13 12:25:00.852613
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:25:06.170039
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()

    assert filters['urldecode']('%3Ctag%3E%3C/tag%3E') == u'<tag></tag>'
    if not HAS_URLENCODE:
        assert filters['urlencode']('<tag></tag>') == u'%3Ctag%3E%3C%2Ftag%3E'

# Generated at 2022-06-13 12:25:09.757983
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic

    # Needed for the basic module object for argspec
    filters = FilterModule().filters()
    assert filters['urldecode'] == do_urldecode



# Generated at 2022-06-13 12:25:19.813492
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Tests filters from class FilterModule
    import json

    # For convenience, we define a few test parameters
    data = u'a=b&c=d'

    # Tests for do_urldecode method
    assert 'a' in do_urldecode(data)
    assert 'b' in do_urldecode(data)
    assert 'c' in do_urldecode(data)
    assert 'd' in do_urldecode(data)

    # Tests for do_urlencode method
    assert 'a=b' in do_urlencode(data)
    assert 'c=d' in do_urlencode(data)
    assert 'a=b&c=d' in do_urlencode(json.loads(data))

# Generated at 2022-06-13 12:25:22.739762
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%7B%22json%22%3A%20%22obj%22%7D') == u'{"json": "obj"}'


# Generated at 2022-06-13 12:25:26.133219
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc123') == u'abc123'
    assert unicode_urldecode('abc%20def') == u'abc%20def'
    assert unicode_urldecode('%E2%82%AC%20Euro%20symbol') == u'€ Euro symbol'


# Generated at 2022-06-13 12:25:29.252138
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E3%81%82') == u'あ'



# Generated at 2022-06-13 12:25:36.157605
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("a b c &") == u'a%20b%20c%20%26'
    assert unicode_urldecode("a%20b%20c%20%26") == u"a b c &"
    assert unicode_urldecode("a+b+c+%26") == u"a b c &"

    assert unicode_urlencode("a b c &", for_qs=True) == u'a+b+c+%26'
    assert unicode_urldecode("a+b+c+%26") == u"a b c &"
    assert unicode_urldecode("a%20b%20c%20%26") == u"a b c &"

    # Trailing plus sign

# Generated at 2022-06-13 12:25:37.495434
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%C3%A6") == u"æ"


# Generated at 2022-06-13 12:25:41.917497
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    data = {'urlencode': 'foo bar  baz', 'urldecode': 'foo%20bar%20%20baz'}
    f = FilterModule().filters()
    assert f['urlencode'](data['urlencode']) == 'foo+bar++baz'
    if not HAS_URLENCODE:
        assert f['urldecode'](data['urldecode']) == data['urlencode']
    else:
        assert f['urldecode'](data['urldecode']) == data['urlencode']


# Generated at 2022-06-13 12:25:51.196109
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    from ansible.module_utils import basic
    from ansible.module_utils.facts import is_collection

    fm = FilterModule()
    for name, f in iteritems(fm.filters()):
        if not is_collection(f):
            fm.assertTrue(callable(f))

    # We can safely test urldecode with any text as it is a one way function
    # Here we test that the one way function is actually working
    # https://tools.ietf.org/html/rfc3986#section-2.2
    # Any octet may be percent-encoded
    assert '+' == do_urldecode('%2B')
    assert '1' == do_urldecode('%31')
    assert '<' == do_urldecode('%3C')

# Generated at 2022-06-13 12:26:06.386716
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'abcABC123') == u'abcABC123'
    assert unicode_urlencode(u'abc:ABC:123') == u'abc%3AABC%3A123'
    assert unicode_urlencode(u'abc:ABC:123', for_qs=True) == u'abc%3AABC%3A123'
    assert unicode_urlencode(u'abc:ABC:123/') == u'abc%3AABC%3A123%2F'
    assert unicode_urlencode(u'abc:ABC:123/', for_qs=True) == u'abc%3AABC%3A123%2F'

# Generated at 2022-06-13 12:26:16.196470
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('foo;bar') == 'foo%3Bbar'
    assert do_urlencode('foo bar') == 'foo+bar'
    assert do_urlencode('foo:bar') == 'foo:bar'

    assert do_urlencode({'foo': 'bar;foo'}) == 'foo=bar%3Bfoo'
    assert do_urlencode({'foo;bar': 'foo:bar'}) == 'foo%3Bbar=foo:bar'

    assert do_urlencode(['foo','bar','foo','bar']) == 'foo&bar&foo&bar'
    assert do_urlencode(('foo','bar','foo','bar')) == 'foo&bar&foo&bar'

# Generated at 2022-06-13 12:26:18.082352
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%2F%2Fetc%2Fpasswd') == u'//etc/passwd'

# Generated at 2022-06-13 12:26:26.589592
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('test') == 'test'
    assert unicode_urldecode('%5Ctest') == '%5Ctest'
    assert unicode_urldecode('%2520') == '%2520'
    assert unicode_urldecode('%252520') == '%252520'
    assert unicode_urldecode('%252520%252520') == '%252520%252520'
    assert unicode_urldecode('%25252520') == '%25252520'
    assert unicode_urldecode('%2525252520') == '%2525252520'



# Generated at 2022-06-13 12:26:35.894555
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%7B%22foo%22%3A%20%22bar%22%7D') == '{"foo": "bar"}'
    assert unicode_urldecode('%C3%88%C3%A3foo%C2%A9%C3%89%C3%AA') == 'ÈÃfoo©ÉÊ'
    assert unicode_urldecode(unicode_urldecode('%7B%22foo%22%3A%20%22bar%22%7D')) == '{"foo": "bar"}'

# Generated at 2022-06-13 12:26:51.096277
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'src=openldap') == u'src=openldap'
    assert unicode_urldecode(u'src=openldap%2copenldap') == u'src=openldap,openldap'
    assert unicode_urldecode(u'src%3dopenldap%2copenldap') == u'src=openldap,openldap'
    assert unicode_urldecode(u'src%3dopenldap%2copenldap%26dst%3dcustomer') == u'src=openldap,openldap&dst=customer'



# Generated at 2022-06-13 12:26:58.145034
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'hello+world') == u'hello world'
    assert unicode_urldecode(u'hello+%F0%9F%98%83') == u'hello \U0001f603'
    assert unicode_urldecode(u'hello+%F0%9F%98%83'.encode('utf-8')) == u'hello \U0001f603'


# Generated at 2022-06-13 12:27:03.526388
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Hello%20World%21') == 'Hello World!'
    assert unicode_urldecode('%E6%88%91%E7%88%B1%E4%BD%A0') == '我爱你'
    assert unicode_urldecode('%20') == ' '


# Generated at 2022-06-13 12:27:09.851440
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    example = 'User: John Doe, password: Secr3t!'
    expected = 'User%3A%20John%20Doe%2C%20password%3A%20Secr3t%21'

    fm = FilterModule()
    assert fm.filters()['urldecode'](expected) == example
    assert fm.filters()['urlencode'](example) == expected

# Generated at 2022-06-13 12:27:20.693831
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode("abcdefg") == "abcdefg"
    assert unicode_urlencode("abcd/efg") == "abcd%2Fefg"
    assert unicode_urlencode("abcd/efg", for_qs=True) == "abcd%2Fefg"
    assert unicode_urlencode("abcd?efg") == "abcd%3Fefg"
    assert unicode_urlencode("abcd?efg", for_qs=True) == "abcd%3Fefg"
    assert unicode_urlencode("abcd&efg") == "abcd%26efg"
    assert unicode_urlencode("abcd&efg", for_qs=True) == "abcd%26efg"
    assert unicode_urlen

# Generated at 2022-06-13 12:27:23.639563
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    args = {
        'string': 'foo+%C3%A9%C3%A9',
        'result': 'foo éé',
    }
    assert unicode_urldecode(args['string']) == args['result']

# Generated at 2022-06-13 12:27:33.542397
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('string1,string2') == u'string1%2Cstring2'
    assert unicode_urlencode('string1,string2', for_qs=True) == u'string1%2Cstring2'
    assert unicode_urlencode(u'한국어/조선말') == u'%ED%95%9C%EA%B5%AD%EC%96%B4%2F%EC%A1%B0%EC%84%A0%EB%A7%90'

# Generated at 2022-06-13 12:27:38.768234
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import doctest
    import os
    import shutil
    import tempfile

    env_dict = {
        'm1': FilterModule()
    }

    try:
        tmpdir = tempfile.mkdtemp()
        result = doctest.testfile('test_FilterModule.txt',
                                  globs=env_dict,
                                  verbose=False,
                                  optionflags=doctest.ELLIPSIS)
        assert result.failed == 0
    finally:
        if os.path.exists(tmpdir):
            shutil.rmtree(tmpdir)

# Generated at 2022-06-13 12:27:46.162497
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc%3D123%26foo%3Dbar') == 'abc=123&foo=bar'
    assert unicode_urldecode('ansible+rocks') == 'ansible rocks'
    assert unicode_urldecode('ansible%21rocks') == 'ansible!rocks'
    assert unicode_urldecode('ansible%2Arocks') == 'ansible*rocks'
    assert unicode_urldecode('ansible%26rocks') == 'ansible&rocks'



# Generated at 2022-06-13 12:27:54.209043
# Unit test for function do_urlencode
def test_do_urlencode():
    str_dict = {'key1': ['value1', 'value2'], 'key2': ['value1', 'value2'], 'key3': ['value3', 'value4']}
    full_test = (u'key1=value1&key1=value2&key2=value1&key2=value2&key3=value3&key3=value4')
    full_test_dict = (u'key1=%5B%27value1%27%2C+%27value2%27%5D&key2=%5B%27value1%27%2C+%27value2%27%5D&key3=%5B%27value3%27%2C+%27value4%27%5D')

# Generated at 2022-06-13 12:28:06.008897
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Note: This method will be used for JUnit testing

    # Create an instance of FilterModule
    instance = FilterModule()

    # Get the filters from the class
    filters = instance.filters()

    # Check that the urlencode filter is properly implemented
    assert filters['urldecode']('https%3A%2F%2Fgithub.com%2Fjotaen') == 'https://github.com/jotaen'

# Generated at 2022-06-13 12:28:14.807148
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode({u'name': u'André', u'jojo': False}) == 'jojo=False&name=Andr%C3%A9'
    assert do_urlencode({'jojo': False, 'name': 'André'}) == 'jojo=False&name=Andr%C3%A9'
    assert do_urlencode([(u'jojo', False), (u'name', u'André')]) == 'jojo=False&name=Andr%C3%A9'
    assert do_urlencode([('jojo', False), ('name', 'André')]) == 'jojo=False&name=Andr%C3%A9'

# Generated at 2022-06-13 12:28:22.031381
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'foo/bar') == 'foo%2Fbar'
    assert unicode_urlencode(u'foo/bar', for_qs=True) == 'foo%2Fbar'
    assert unicode_urlencode(u'foo?bar') == 'foo%3Fbar'
    assert unicode_urlencode(u'foo?bar', for_qs=True) == 'foo%3Fbar'
    assert unicode_urlencode(u'foo&bar') == 'foo%26bar'
    assert unicode_urlencode(u'foo&bar', for_qs=True) == 'foo%26bar'
    assert unicode_urlencode(u'foo+bar') == 'foo%2Bbar'

# Generated at 2022-06-13 12:28:30.348930
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test special cases
    assert u'' == unicode_urldecode(u'')
    assert u'' == unicode_urldecode(u' ')

    # Test some printable characters
    for i in range(0x22, 0x7f):
        assert unichr(i) == unicode_urldecode(unichr(i))

    # Test some unprintable characters
    for i in range(0x05, 0x21):
        assert unichr(i) == unicode_urldecode(u'%{0:02x}'.format(i))

    # Test some special characters
    assert u'"' == unicode_urldecode(u'%22')
    assert u'' == unicode_urldecode(u'%00')
    assert u'\x20'

# Generated at 2022-06-13 12:28:36.802116
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys

    # test python 2
    if sys.version[0] == '2':
        assert unicode_urldecode("%2F") == u"/"

        assert unicode_urldecode("%2F%2F") == u"//"

        assert unicode_urldecode("a+b") == u"a b"

    # test python 3
    if sys.version[0] == '3':
        assert unicode_urldecode("%2F") == "/"

        assert unicode_urldecode("%2F%2F") == "//"

        assert unicode_urldecode("a+b") == "a b"

    return True


# Generated at 2022-06-13 12:28:46.979453
# Unit test for function do_urlencode
def test_do_urlencode():
    testcases = [
        (u'foo', u'foo'),
        (u'one+two', u'one%2Btwo'),
        (u'one & two', u'one%20%26%20two'),
        (u'&', u'%26'),
        (u'one=two&three=four', u'one%3Dtwo%26three%3Dfour'),
        (u'one&two', u'one%26two'),
        (u'', u''),
        (u' ', u'%20'),
        ({u'a': u'b', u'c': u'd'}, u'a=b&c=d'),
        ([u'a', u'b'], u'a&b'),
    ]

    for input, expected in testcases:
        assert expected == do_urlencode

# Generated at 2022-06-13 12:28:48.990834
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20%21%22%23%24%25%26%27') == ' !"#$%&\''



# Generated at 2022-06-13 12:28:57.365720
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import string
    assert unicode_urldecode("öäü") == "öäü"
    assert unicode_urldecode("http://www.google.com/search?q=python%20urllib%20parse%20urlencode%20example") == "http://www.google.com/search?q=python urllib parse urlencode example"
    assert unicode_urldecode("") == ""
    for c in string.printable:
        assert unicode_urldecode(c) == c


# Generated at 2022-06-13 12:29:03.087754
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == 'test'
    assert unicode_urlencode('test', for_qs=True) == 'test'
    assert unicode_urlencode('test test') == 'test%20test'
    assert unicode_urlencode('test test', for_qs=True) == 'test+test'
    assert unicode_urlencode('/test/test/') == '%2Ftest%2Ftest%2F'
    assert unicode_urlencode('/test/test/', for_qs=True) == '%2Ftest%2Ftest%2F'


# Generated at 2022-06-13 12:29:05.636909
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    fm.filters() == {
        'urldecode': do_urldecode,
        'urlencode': do_urlencode
    }

# Generated at 2022-06-13 12:29:16.306594
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    u = unicode('/path/to/my%file')

    assert unicode_urlencode(u) == b'/path/to/my%25file'
    assert unicode_urlencode(u, for_qs=True) == b'/path/to/my%25file'

    u = 1.0

    assert unicode_urlencode(u) == b'1.0'
    assert unicode_urlencode(u, for_qs=True) == b'1.0'

    u = [1.0, 1.0]

    assert unicode_urlencode(u) == b'1.0&1.0'
    assert unicode_urlencode(u, for_qs=True) == b'1.0&1.0'


# Generated at 2022-06-13 12:29:18.904638
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E8%8D%89') == u'草'


# Generated at 2022-06-13 12:29:22.351766
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    url = b"http%3A%2F%2Ffoo%20bar%2F"
    assert(unicode_urldecode(url) == u"http://foo bar/")


# Generated at 2022-06-13 12:29:27.701059
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    class MockArgs(object):
        pass

    result = FilterModule().filters()

    assert 'urldecode' in result
    assert result['urldecode'](u'%F0%9F%98%82') == u'🤂'

    args = MockArgs()
    args.urlencode = True
    assert 'urlencode' in result
    assert result['urlencode'](u'🤂') == u'%F0%9F%A4%82'

# Generated at 2022-06-13 12:29:30.561443
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter = FilterModule()
    filters = filter.filters()
    assert 'urldecode' in filters
    if not HAS_URLENCODE:
        assert 'urlencode' in filters


# Generated at 2022-06-13 12:29:39.300257
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%2520') == '%20'
    assert unicode_urldecode('%3d') == '='
    assert unicode_urldecode('%253d') == '%3d'
    assert unicode_urldecode('%26') == '&'
    assert unicode_urldecode('%2526') == '%26'
    assert unicode_urldecode('abc%20def') == 'abc def'
    assert unicode_urldecode('abc%2520def') == 'abc%20def'



# Generated at 2022-06-13 12:29:40.989395
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%s') == u' '



# Generated at 2022-06-13 12:29:49.804230
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode(u'para/meter') == u'para%2Fmeter'
        assert unicode_urlencode(u'para/meter', True) == u'para%2Fmeter'
        assert unicode_urlencode(b'para/meter') == u'para%2Fmeter'
        assert unicode_urlencode(b'para/meter', True) == u'para%2Fmeter'
    else:
        assert unicode_urlencode(u'para/meter') == u'para%2Fmeter'
        assert unicode_urlencode(u'para/meter', True) == u'para%2Fmeter'

# Generated at 2022-06-13 12:29:50.828792
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
  filterModule = FilterModule()
  filterModule.filters()

# Generated at 2022-06-13 12:29:58.544183
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert "hi there" == unicode_urldecode("hi%20there")
    assert "hi there" == unicode_urldecode(b"hi%20there")
    assert u"hi there" == unicode_urldecode(u"hi%20there")
    assert "*Dag" == unicode_urldecode("*Dag")
    assert "%20Dag" == unicode_urldecode("%20Dag")
    assert "Dag%202" == unicode_urldecode("Dag%202")
    assert "Dag%2" == unicode_urldecode("Dag%2")
    assert "unicode %3F in %2F" == unicode_urldecode(u"unicode %3F in %2F")

# Generated at 2022-06-13 12:30:12.317803
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    print("Testing FilterModule_filters ...")
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    filters = FilterModule().filters()
    m = AnsibleModule(
        argument_spec=dict(
            value=dict(type='raw', required=True)
        )
    )
    m.fail_json = basic.fail_json
    str_value = b'hello world'
    # urldecode
    if 'urldecode' in filters:
        urldecode = filters['urldecode']
        print("Test urldecode:")
        print(" value={}, type={}".format(str_value, type(str_value)))

# Generated at 2022-06-13 12:30:18.820236
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Test if a string is properly encoded and decoded
    test = unicode_urlencode(u'test')
    assert test == u'test'
    test = unicode_urldecode(test)
    assert test == u'test'

    # Test if a unicode string is properly encoded
    test = unicode_urlencode(u'øæå!')
    assert test == u'%C3%B8%C3%A6%C3%A5%21'
    test = unicode_urldecode(test)
    assert test == u'øæå!'

    # Test if a list is properly encoded
    test = unicode_urlencode([u'øæå!', u'test'])

# Generated at 2022-06-13 12:30:27.205003
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("") == u''
    assert unicode_urldecode("%") == u'%'
    assert unicode_urldecode("%25") == u'%'
    assert unicode_urldecode("%%25") == u'%%25'
    assert unicode_urldecode("%25%") == u'%%'
    assert unicode_urldecode("%25%25") == u'%%'
    assert unicode_urldecode("%a") == u'%a'
    assert unicode_urldecode("%0") == u'%0'
    assert unicode_urldecode("%s") == u'%s'
    assert unicode_urldecode("%2") == u'%2'
    assert unicode_ur

# Generated at 2022-06-13 12:30:34.841529
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(to_bytes(u'my+string')) == u'my string'
    assert unicode_urldecode(to_bytes('my+string')) == u'my string'
    assert unicode_urldecode('my+string') == u'my string'
    assert unicode_urldecode(u'my+string') == u'my string'



# Generated at 2022-06-13 12:30:43.893728
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils.six import unichr

    f = FilterModule()
    filt = f.filters()
    test_str = u'ąbc'
    test_str_plus = unicode_urlencode(test_str)
    test_str_perc = unicode_urlencode(test_str, for_qs=True)
    test_dict = basic.json_dict({'a': test_str, 'b': test_str}, True)
    test_dict_qs = basic.json_dict({'a': test_str, 'b': test_str}, True)

    # test urldecode
    assert test_str == filt['urldecode'](test_str)

# Generated at 2022-06-13 12:30:50.186785
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert(do_urlencode('') == u'')
    assert(do_urlencode('some string') == u'some%20string')
    assert(do_urlencode(u'à') == u'%C3%A0')
    assert(do_urlencode('/') == u'/')
    assert(do_urlencode(u'\u2603') == u'%E2%98%83')
    assert(do_urlencode('http://foo') == u'http://foo')
    assert(do_urlencode('http://föö') == u'http://f%C3%B6%C3%B6')

# Generated at 2022-06-13 12:30:56.991027
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from ansible.module_utils import six
    from ansible.module_utils.six.moves.urllib.parse import parse_qsl, urlparse

    def check(url):
        # we drop the fragment, it's not supported by urlparse
        if '#' in url:
            url, frag = url.split('#', 1)
        else:
            url, frag = url, ''

        # parse the url into a result set
        parts = urlparse(url)
        u = parts.geturl()
        qs = parts.query
        qsl = parse_qsl(qs) if qs else []

        # test that it works as an url parse
        assert url == u

        # test that it works as a custom urldecode
        decoded = unicode_urldecode(url)
        assert dec

# Generated at 2022-06-13 12:31:07.750710
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(unicode_urldecode('abc')[::-1]) == 'abc'
    assert unicode_urldecode(unicode_urldecode('abc/def')[::-1]) == 'abc/def'
    if not PY3:
        assert unicode_urldecode(unicode_urldecode(b'abc')[::-1]) == b'abc'
        assert unicode_urldecode(unicode_urldecode(b'abc/def')[::-1]) == b'abc/def'
    print('Tests passed.')


# Generated at 2022-06-13 12:31:15.875235
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert unicode_urldecode(u'test%20string') == u'test string'
    assert unicode_urlencode(u'test string') == u'test%20string'
    assert unicode_urlencode(u'test string', for_qs=True) == u'test+string'

    # Nothing changes when encrypted
    fm = FilterModule()
    assert fm.filters()['urldecode'](u'test%20string') == u'test string'
    assert fm.filters()['urldecode'](u'https://user:password@www.example.com/') == u'https://user:password@www.example.com/'

# Generated at 2022-06-13 12:31:21.904321
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_data = [
        # Unquoted string should be unchanged
        ('!', '!'),
        # Unsafe characters should be quoted
        ('!#$&()*+,:;=?@[] ', '%21%23%24%26%28%29%2A%2B%2C%3A%3B%3D%3F%40%5B%5D+'),
        # Python2 encodes strings as latin-1 and returns bytes
        (u'é', b'%C3%A9'),
    ]

    for input, expected in test_data:
        check(unicode_urlencode, input, expected)



# Generated at 2022-06-13 12:31:32.197791
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%3A+%3D+%3F') == u': = ?'
    assert unicode_urldecode(u'%26') == u'&'
    assert unicode_urldecode(u'%2B') == u'+'


# Generated at 2022-06-13 12:31:35.177159
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert 'urldecode' in fm.filters()
    assert 'urlencode' in fm.filters()


# Generated at 2022-06-13 12:31:46.488790
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter = FilterModule().filters()
    assert filter['urldecode']('%2F') == '/'
    assert filter['urldecode']('%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest') == '/test/test/test/test/test'
    assert filter['urldecode']('%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest%2') == '/test/test/test/test/test%2'
    assert filter['urldecode']('%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest%2Ftest') == '/test/test/test/test/test/test/test/test/test/test/test'

# Generated at 2022-06-13 12:31:49.440842
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%2B') == u'+'



# Generated at 2022-06-13 12:32:01.156240
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    def do_test(text, expected, for_qs=False):
        assert unicode_urlencode(text, for_qs=for_qs) == expected

    do_test(u'hello@world.com', u'hello%40world.com')
    do_test(u'hello@world.com', u'hello%40world.com', for_qs=True)
    do_test(u'hello world?', u'hello%20world%3F')
    do_test(u'hello world?', u'hello+world%3F', for_qs=True)
    do_test(u'hello/world', u'hello%2Fworld')
    do_test(u'hello/world', u'hello%2Fworld', for_qs=True)

# Generated at 2022-06-13 12:32:05.621143
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert not HAS_URLENCODE

    f = FilterModule()
    filters = f.filters()

    assert 'urldecode' in filters
    assert 'urlencode' in filters
    assert do_urldecode('a%20b%20c') == 'a b c'
    assert do_urlencode('a b c') == 'a+b+c'

# Generated at 2022-06-13 12:32:11.717887
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert u'foo%20bar' == unicode_urlencode('foo bar')
    assert u'foo%20bar%00' == unicode_urlencode('foo bar\x00')
    assert u'foo%20bar%00' == unicode_urlencode('foo bar\x00', for_qs=True)
    assert u'foo%20bar' == unicode_urlencode('foo bar', for_qs=True)
    assert u'foo+bar' == unicode_urlencode('foo bar', for_qs=True)

# Generated at 2022-06-13 12:32:12.469509
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%C3%A0") == u"à"


# Generated at 2022-06-13 12:32:13.512234
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    s = "toto.%20tata"
    t = "toto. tata"
    assert unicode_urldecode(s) == t


# Generated at 2022-06-13 12:32:14.850014
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert(unicode_urlencode('?/?/') == '%3F/%3F/')

# Generated at 2022-06-13 12:32:23.612428
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://foo/bar') == 'http%3A//foo/bar'
    assert unicode_urlencode('http://foo/bar', for_qs=True) == 'http%3A%2F%2Ffoo%2Fbar'

# Generated at 2022-06-13 12:32:32.090092
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    '''
    >>> test_unicode_urlencode()
    True
    '''

    # For Python 2.6 and base_compat.to_text(safe_url)
    import sys
    if sys.version_info[0] == 2 and sys.version_info[1] <= 6:
        sys.modules['__builtin__'].unicode = unicode

    safe_url = u'http://ansible.com%20/foo@example.com/api/v2/jobs/12345/'
    assert unicode_urlencode(safe_url) == u'http%3A%2F%2Fansible.com%2520%2Ffoo%40example.com%2Fapi%2Fv2%2Fjobs%2F12345%2F'

# Generated at 2022-06-13 12:32:40.598829
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a+b+c') == u'a b c'
    assert unicode_urldecode(u'a%20b%20c') == u'a b c'
    assert unicode_urldecode(u'a+%3db+%25c') == u'a =b %c'
    assert unicode_urldecode(u'%u0434%u0435%u0449%u0430') == u'деща'
    assert unicode_urldecode(u'%D0%B4%D0%B5%D1%89%D0%B0') == u'деща'


# Generated at 2022-06-13 12:32:45.376999
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # We test with a version of Jinja2 that does not have urlencode
    f = FilterModule()
    assert f.filters()['urldecode'] == do_urldecode
    assert f.filters()['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:32:50.191607
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # test_FilterModule_filters() defined for FilterModule class must always
    # returns dictionary, where key is filter name and value is filter
    # implementation (function).
    fm = FilterModule()
    assert isinstance(fm.filters(), dict)
    for name, func in iteritems(fm.filters()):
        # Filter name is a string, and filter implementation is callable.
        assert isinstance(name, string_types)
        assert callable(func)

# Generated at 2022-06-13 12:32:57.305590
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc%20def') == 'abc def'
    assert unicode_urldecode('abc+def') == 'abc def'
    assert unicode_urldecode('abc def') == 'abc def'
    assert unicode_urldecode('abc%C3%84def') == 'abcÄdef'
    assert unicode_urldecode(u'abc def') == u'abc def'
    assert unicode_urldecode(u'abc+def') == u'abc def'
    assert unicode_urldecode(u'abc%20def') == u'abc def'


# Generated at 2022-06-13 12:33:02.099604
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert FilterModule().filters()['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:33:12.076367
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/a/b/c') == '/a/b/c'
    assert unicode_urlencode('a-b') == 'a-b'
    assert unicode_urlencode('a b') == 'a%20b'
    assert unicode_urlencode('a+b') == 'a+b'
    assert unicode_urlencode('a b', True) == 'a+b'
    assert unicode_urlencode('a b=c d', True) == 'a+b%3Dc+d'
    assert unicode_urlencode('a b=c d') == 'a%20b=c%20d'

# Generated at 2022-06-13 12:33:23.559625
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six import iteritems
    from ansible.module_utils._text import to_bytes, to_text

    def test_unicode_urldecode(s1, s2):
        return to_text(unicode_urldecode(to_bytes(s1))) == to_text(s2)

    assert test_unicode_urldecode(u'&amp;', u'&'), 'urldecode must decode &amp; as &'
    assert test_unicode_urldecode(u'+', u' '), 'urldecode must decode + as space'
    assert test_unicode_urldecode(u'%5F', u'_'), 'urldecode must decode %5F as _'

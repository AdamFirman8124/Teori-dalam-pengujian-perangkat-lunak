

# Generated at 2022-06-13 12:23:31.395882
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # NOTE: The original definition used quote_plus, but that function is
    # broken in Python3. The (python3) unquote_plus function works with both
    # values encoded with quote_plus and with the legacy urllib.quote_plus

    assert unicode_urldecode('Zoo+Gorilla') == u'Zoo Gorilla'
    assert unicode_urldecode('Zoo+Gorilla%27s+are+cool') == u"Zoo Gorilla's are cool"
    assert unicode_urldecode('Zoo+Gorilla%27s+are%3F+really%3F+%2B+cool%21') == u"Zoo Gorilla's are? really? + cool!"


# Generated at 2022-06-13 12:23:37.169563
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert u'foo%20bar' == unicode_urlencode(u'foo bar')
    assert u'foo%20bar' == unicode_urlencode(u'foo bar', for_qs=True)
    assert u'foo/bar' == unicode_urlencode(u'foo/bar')



# Generated at 2022-06-13 12:23:39.648513
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert '/dev/null' == unicode_urlencode(unicode_urldecode('/dev/null'))


# Generated at 2022-06-13 12:23:45.712496
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'') == u''
    assert unicode_urldecode(u'%') == u'%'
    assert unicode_urldecode(u'%2') == u'%2'
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode(u'%2F') == u'/'



# Generated at 2022-06-13 12:23:49.073436
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filters = FilterModule().filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:23:59.346756
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    try:
        filters = fm.filters()
    except TypeError as ex:
        fail_json(msg="FilterModule.filters raised exception. %s" % ex)
    assert filters is not None, "FilterModule.filters returned None"
    current_filters = [k for k in filters.keys()]
    expected_filters = [
            'urldecode',
            'urlencode',
            ]
    assert set(expected_filters) <= set(current_filters),\
            "FilterModule.filters returned unexpected filters %s"\
            % set(current_filters) ^ set(expected_filters)
    assert filters['urldecode'] == do_urldecode,\
            "FilterModule.filters returned unexpected urldecode"
   

# Generated at 2022-06-13 12:24:08.321204
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec=dict(),
    )
    assert module.urldecode("http%3A%2F%2Fwww.example.org%3Fa%3Db%26c%3Dd%26e%3Df") == u"http://www.example.org?a=b&c=d&e=f"
    assert module.urldecode("http:/www.example.org?a=b&c=d&e=f") == "http:/www.example.org?a=b&c=d&e=f"

    # Regression tests for this specific issue

# Generated at 2022-06-13 12:24:15.546715
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    '''
    Test to ensure the output of unicode_urlencode is equal to the output of
    the python 2 and 3 urllib.quote_plus function.
    '''
    import urllib.parse


# Generated at 2022-06-13 12:24:19.091562
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    assert module.filters()['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert module.filters()['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:24:25.496546
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert(unicode_urlencode('http://example.com/path/?name=value') == u'http%3A%2F%2Fexample.com%2Fpath%2F%3Fname%3Dvalue')
    assert(unicode_urlencode('http://example.com/path/?name=value', for_qs=True) == u'http%3A%2F%2Fexample.com%2Fpath%2F%3Fname%3Dvalue')


# Generated at 2022-06-13 12:24:29.902786
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    assert f.filters()['urldecode']('foo%3Dbar') == 'foo=bar'

# Generated at 2022-06-13 12:24:38.666858
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    # This test only makes sense in Python 2.x
    if PY3:
        return

    # Unicode characters
    uri = u"http://example.org/?\u5e97\u94fa=\u5e97\u94fa"
    expected = u"http://example.org/?%E5%BA%97%E9%94%FA=%E5%BA%97%E9%94%FA"
    result = unicode_urlencode(uri, for_qs=True)
    if result != expected:
        print("Expected: '%s', instead got: '%s'" % (expected, result))
        raise AssertionError()

    result = unicode_urldecode(result)

# Generated at 2022-06-13 12:24:52.204972
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test ascii
    assert unicode_urldecode('test') == u'test'
    # Test unicode
    assert unicode_urldecode(u'test') == u'test'
    # Test unicode escaped
    assert unicode_urldecode(u'test with spaces') == u'test with spaces'
    # Test unicode escaped
    assert unicode_urldecode(u'test+with+spaces') == u'test with spaces'
    # Test unicode escaped
    assert unicode_urldecode(u'test%20with%20spaces') == u'test with spaces'
    # Test unicode escaped
    assert unicode_urldecode(u'test%2Bwith%2Bspaces') == u'test+with+spaces'



# Generated at 2022-06-13 12:24:53.188817
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert type(FilterModule.filters) == type(FilterModule.__dict__['filters'])


# Generated at 2022-06-13 12:24:58.850095
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    import sys

    class TestUnicodeUrldecode(unittest.TestCase):
        """Unit test for function unicode_urldecode
        """
        def test_urldecode(self):
            output = unicode_urldecode(u"https://server.fqdn/path%20with%20spaces/file.txt?foo=bar%20with%20spaces")
            self.assertEqual(output, u"https://server.fqdn/path with spaces/file.txt?foo=bar with spaces")

        def test_empty(self):
            output = unicode_urldecode(u"")
            self.assertEqual(output, u"")

        # test

# Generated at 2022-06-13 12:25:02.681058
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode('%2B') == '+'
    assert unicode_urldecode('%40') == '@'
    assert unicode_urldecode('%7E') == '~'
    assert unicode_urldecode('%25') == '%'

# Generated at 2022-06-13 12:25:13.106694
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import unittest
    class UnicodeUrlDecode(unittest.TestCase):
        def test(self):
            # http://docs.python.org/2/library/unittest.html
            # https://docs.python.org/3/library/unittest.html
            self.assertEqual(unicode_urldecode('abc'), 'abc')
            self.assertEqual(unicode_urldecode('a%2Bc'), 'a+c')
            self.assertEqual(unicode_urldecode('a%2bC'), 'a+C')
            self.assertEqual(unicode_urldecode('a%2bc%2bD'), 'a+c+D')

# Generated at 2022-06-13 12:25:23.558140
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode('abc') == 'abc'
        assert unicode_urlencode('abc def') == 'abc%20def'
        assert unicode_urlencode('abc def', for_qs=True) == 'abc+def'

    else:
        assert unicode_urlencode(u'abc') == 'abc'
        assert unicode_urlencode('abc') == 'abc'
        assert unicode_urlencode(u'abc def') == 'abc%20def'
        assert unicode_urlencode('abc def') == 'abc%20def'
        assert unicode_urlencode(u'abc def', for_qs=True) == 'abc+def'
        assert unicode_urlencode('abc def', for_qs=True) == 'abc+def'

# Generated at 2022-06-13 12:25:27.186412
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # When a simple string is supplied, it should be properly encoded
    assert unicode_urlencode("我") == "%E6%88%91"

    # When an iterable is supplied, it should be encoded
    assert unicode_urlencode(["我", "foo", "bar"]) == "%E6%88%91&foo&bar"

# Generated at 2022-06-13 12:25:41.943001
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.urltools import open_url
    import copy
    import sys

    encoding = sys.getdefaultencoding() or 'UTF-8'
    module_name = 'FiltersModule_test'
    module_path = '%s.py' % module_name

    with open(module_path, 'w') as module_file:
        module_file.write(u"#!/usr/bin/python\n")
        module_file.write(u"# -*- coding: utf-8 -*-\n")
        module_file.write(u"\n")
        module_file.write(u"import sys\n")
        module_file.write(u"import traceback\n")

# Generated at 2022-06-13 12:25:46.070613
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'http%3A//example.org/') == u'http://example.org/'


# Generated at 2022-06-13 12:25:59.509621
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo') == u'foo'
    assert unicode_urldecode(b'foo') == u'foo'
    assert unicode_urldecode(u'B%C3%A5b%C3%A5') == u'Båbå'
    assert unicode_urldecode(b'B%C3%A5b%C3%A5') == u'Båbå'
    assert unicode_urldecode(u'B%E5b%E5') == u'Båbå'
    assert unicode_urldecode(b'B%E5b%E5') == u'Båbå'


# Generated at 2022-06-13 12:26:01.609681
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'abc%20def') == u'abc def'
    assert unicode_urldecode(u'abc+def') == u'abc+def'


# Generated at 2022-06-13 12:26:10.987158
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%E2%80%82') == u' '
    assert unicode_urldecode('%E2%80%83') == u' '
    assert unicode_urldecode('%E2%80%8A') == u' '
    assert unicode_urldecode('%E2%80%8B') == u' '
    assert unicode_urldecode('%E2%80%8C') == u'‌'
    assert unicode_urldecode('%E2%80%8D') == u'‍'
    assert unicode_urldecode('%E2%80%8E') == u'‎'
    assert unic

# Generated at 2022-06-13 12:26:17.324779
# Unit test for function do_urlencode
def test_do_urlencode():

    assert do_urlencode({'a': 1, 'b': 2}) == u'a=1&b=2'
    assert do_urlencode({'a': 'aa', 'b': 'bb'}) == u'a=aa&b=bb'
    assert do_urlencode({'a': 'aa', 'b': 'bb'}) == u'a=aa&b=bb'
    assert do_urlencode({'a': ['aa', 'bb']}) == u'a=aa&a=bb'
    assert do_urlencode('foo') == u'foo'

# Generated at 2022-06-13 12:26:19.424347
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("%25%26%2B%2F%3D") == '%&+/='



# Generated at 2022-06-13 12:26:24.395569
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('one%20two%3Dthree') == u'one two=three'
    assert isinstance(unicode_urldecode('one%20two%3Dthree'), unicode)  # noqa E501


# Generated at 2022-06-13 12:26:32.008297
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%2B') == '+'
    assert unicode_urldecode('%2b') == '+'
    assert unicode_urldecode('%2f') == '/'
    assert unicode_urldecode('%2F') == '/'
    assert unicode_urldecode('%3d') == '='
    assert unicode_urldecode('%3D') == '='
    assert unicode_urldecode('%26') == '&'
    assert unicode_urldecode('%40') == '@'
    assert unicode_urldecode('%23') == '#'
    assert unicode_urldecode('%3a') == ':'
    assert unicode_urldecode('%3A') == ':'

# Generated at 2022-06-13 12:26:35.574510
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc%3Ddef+x%2Fy') == u'abc=def x/y'
    assert unicode_urldecode('abc%3Ddef+x%2Fy'.encode('utf-8')) == u'abc=def x/y'


# Generated at 2022-06-13 12:26:40.537801
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    testlist = {
        u'test': u'test',
        u'%20test': u' test',
        u'test%20': u'test ',
        u'%2Ftest': u'/test',
        u'%2Ftest%2F': u'/test/',
        u'%2Ftest%2F%2F': u'/test//',
    }

    for test in testlist:
        assert unicode_urldecode(test) == testlist[test]


# Generated at 2022-06-13 12:26:44.979609
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    instance = FilterModule()
    result = instance.filters()
    assert (result['urldecode'] == do_urldecode)


# Generated at 2022-06-13 12:26:50.210427
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'{}') == u'%7B%7D'
    assert unicode_urlencode({u'a': u'A'}, for_qs=True) == u'a=A'

# Generated at 2022-06-13 12:26:55.146510
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a%20simple%20string') == u'a simple string'
    assert unicode_urldecode(u'a+simple+string') == u'a simple string'


# Generated at 2022-06-13 12:27:05.172472
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']['_ansible_tmp.xml'] == '_ansible_tmp.xml'
    assert FilterModule().filters()['urldecode']['_ansible_tmp%2Exml'] == '_ansible_tmp.xml'

    assert FilterModule().filters()['urldecode']['_ansible_tmp+xml'] == '_ansible_tmp xml'
    assert FilterModule().filters()['urldecode']['_ansible_tmp%2Bxml'] == '_ansible_tmp+xml'

    assert FilterModule().filters()['urldecode']['_ansible_tmp%25xml'] == '_ansible_tmp%xml'

# Generated at 2022-06-13 12:27:09.197730
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    filters = f.filters()
    assert filters['urldecode'] == do_urldecode

    # urlencode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:27:12.063174
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('%C3%B6') == u'ö'


# Generated at 2022-06-13 12:27:16.745754
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # my_filter is not really a filter but a set of filters
    from ansible.module_utils.common.collections import is_sequence
    my_filter = FilterModule()
    assert is_sequence(my_filter.filters())
    return (0, "OK")


# Testcases for module-utils.common.filter_plugins.urlencode

# Generated at 2022-06-13 12:27:25.778677
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filters = FilterModule().filters()

    assert 'urldecode' in filters
    assert filters['urldecode'].__name__ == 'do_urldecode'

    assert filters['urldecode']("https%3A%2F%2Fgithub.com%2Fansible%2Fansible%2Fpull%2F18063") == u"https://github.com/ansible/ansible/pull/18063"

    try:
        from jinja2.filters import do_urlencode
        assert filters['urldecode'].__name__ == 'do_urlencode'
    except ImportError:
        assert 'urlencode' in filters
        assert filters['urlencode'].__name__ == 'do_urlencode'


# Generated at 2022-06-13 12:27:34.979145
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import json
    import jinja2
    env = jinja2.Environment()
    env.filters.update(FilterModule().filters())
    assert env.filters['urldecode']('http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dansible') == 'http://www.google.com/search?q=ansible'
    assert json.loads(env.filters['urldecode']('%7B%22a%22%3A+%22b%22%7D')) == {u'a': u'b'}

# Generated at 2022-06-13 12:27:41.248729
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from units.compat import unittest
    from units.compat.mock import patch

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six.moves.urllib.parse import quote_plus
    from ansible.module_utils.urls import urlencode

    class TestFilterModule(unittest.TestCase):
        ''' Test filters of class FilterModule '''


# Generated at 2022-06-13 12:27:50.969420
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    if PY3:
        assert unicode_urlencode('http://localhost/api/v1/a%20b') == 'http%3A//localhost/api/v1/a%20b'
    else:
        assert unicode_urlencode('http://localhost/api/v1/a%20b') == u'http%3A%2F%2Flocalhost%2Fapi%2Fv1%2Fa%20b'
    assert unicode_urlencode('a&b') == 'a%26b'


# Generated at 2022-06-13 12:27:59.025600
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # In python2 the input of urldecode() must be a bytestring, while
    # in python3 it could be any binary. Test python2 case
    if not PY3:
        input_data = [
            # Expected result, input
            ('foo', 'foo'),
            ('föö', 'f%C3%B6%C3%B6'),
            ('Abc Xyz', 'Abc%20Xyz'),
            ('f++oo', 'f%2B%2Boo'),
            ('foo+bar', 'foo+bar'),
            ('foo+bar+', 'foo+bar+'),
        ]
        for expect, value in input_data:
            assert unicode_urldecode(value) == expect



# Generated at 2022-06-13 12:28:09.342824
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode(123) == '123'
    assert do_urlencode('foo') == 'foo'
    assert do_urlencode('foo bar') == 'foo+bar'
    assert do_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert do_urlencode({'foo': ['bar', 'baz']}) == 'foo=bar&foo=baz'
    assert do_urlencode(['foo', {'bar': 'baz'}]) == 'foo&bar=baz'
    assert do_urlencode(['foo', ['bar', 'baz']]) == 'foo&bar&baz'


# Generated at 2022-06-13 12:28:12.406009
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == u' '
    assert unicode_urldecode('+') == u' '


if __name__ == '__main__':
    # Some tests
    test_unicode_urldecode()

# Generated at 2022-06-13 12:28:13.748523
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%2Fetc%2Fpasswd') == u'/etc/passwd'



# Generated at 2022-06-13 12:28:21.672687
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils import six
    # Unicode string
    unicode_string = six.u('ø∆˜çß∂')
    assert unicode_string == unicode_urldecode(unicode_urlencode(unicode_string))
    # Unicode string with non-ascii characters
    unicode_non_ascii = six.u('ø∆˜çß∂')
    assert unicode_non_ascii == unicode_urldecode(unicode_urlencode(unicode_non_ascii))
    # Unicode string with non-ascii characters and spaces
    unicode_non_ascii_spaces = 'ø∆˜çß ∂'

# Generated at 2022-06-13 12:28:24.045666
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # unicode_urldecode is tested by util.powershell.to_native
    # and util.powershell.to_unicode
    pass

# Generated at 2022-06-13 12:28:32.268319
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # Case 1, simple string
    assert unicode_urlencode("this is a test") == 'this%20is%20a%20test'
    # Case 2, string with lots of chars
    assert unicode_urlencode("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") == '!%22%23$%25&%27()*%2B%2C-.%2F%3A%3B%3C%3D%3E%3F%40%5B%5C%5D%5E_%60%7B%7C%7D~'
    # Case 3, unicode string

# Generated at 2022-06-13 12:28:33.884885
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert isinstance(fm.filters(), dict)


# Generated at 2022-06-13 12:28:39.486476
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    string = u'http://hello.com/?lang=en_US&a=2&b=3&c=&c=&c'
    encoded = u'http%3A%2F%2Fhello.com%2F%3Flang%3Den_US%26a%3D2%26b%3D3%26c%3D%26c%3D%26c'
    decoded = u'http://hello.com/?lang=en_US&a=2&b=3&c=&c=&c'

    filter_module = FilterModule()
    filters = filter_module.filters()

    assert encod

# Generated at 2022-06-13 12:28:47.590818
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert 'foo%20bar' == unicode_urlencode(u'foo bar')
    assert 'foo%3Abar' == unicode_urlencode(u'foo:bar')
    assert '%E2%82%AC%20%E2%82%AC' == unicode_urlencode(u'\u20ac \u20ac')


# Generated at 2022-06-13 12:28:54.136260
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('string') == 'string'
    assert do_urlencode('/path/to/file') == '/path/to/file'
    assert do_urlencode(u'/path/to/fi\u00EBle') == '/path/to/fi%C3%ABle'

    assert do_urlencode({'k': 'v'}) == 'k=v'
    assert do_urlencode({'k': 'v', 'k2': 'v2'}) == 'k=v&k2=v2'
    assert do_urlencode(['k', 'v']) == 'k=v'
    assert do_urlencode([('k', 'v'), ('k2', 'v2')]) == 'k=v&k2=v2'

# Generated at 2022-06-13 12:29:03.043802
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import unittest

    class TestUrlencode(unittest.TestCase):
        test_type = 'unicode'

        # Test the unicode_urlencode function
        def test_unicode_urlencode(self):
            # Test Unicode strings
            string = u'foo bar123'
            if PY3:
                self.assertEqual(unicode_urlencode(string), u'foo%20bar123')
                self.assertEqual(unicode_urlencode(string, for_qs=True), u'foo+bar123')
            else:
                self.assertEqual(unicode_urlencode(string), u'foo%20bar123')
                self.assertEqual(unicode_urlencode(string, for_qs=True), u'foo%20bar123')

            # Test as

# Generated at 2022-06-13 12:29:05.892644
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%25ABC') == u'%ABC'
    assert unicode_urldecode(u'%C3%89') == u'É'
    assert unicode_urldecode(u'%C3%89') == u'É'
    assert unicode_urldecode(u'%40%40') == u'@@'

# Generated at 2022-06-13 12:29:14.976278
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils._text import to_text
    assert unicode_urlencode('') == ''
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode(u'/') == '%2F'
    assert unicode_urlencode(u'ab%c3%a9') == 'ab%25c3%25a9'
    assert unicode_urlencode(u'ab£') == 'ab%25C2%25A3'


# Generated at 2022-06-13 12:29:25.829368
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == 'test'
    assert unicode_urlencode('test+test') == 'test%2Btest'
    assert unicode_urlencode('test/test') == 'test/test'
    assert unicode_urlencode('test&test') == 'test%26test'
    assert unicode_urlencode('test?test') == 'test%3Ftest'
    assert unicode_urlencode('test#test') == 'test%23test'
    assert unicode_urlencode('test test') == 'test+test'
    assert unicode_urlencode('test+test', for_qs=True) == 'test%2Btest'
    assert unicode_urlencode('test/test', for_qs=True) == 'test%2Ftest'

# Generated at 2022-06-13 12:29:30.847546
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    assert unicode_urldecode('%20') == ' '

    assert unicode_urldecode('%2B') == '+'

    assert unicode_urldecode('%2B%2B') == '++'

    assert unicode_urldecode('%2B++') == '++'



# Generated at 2022-06-13 12:29:37.371282
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # filter enabled
    filter_module = FilterModule()

    if HAS_URLENCODE:
        # core urlencode
        assert(filter_module.filters()['urlencode'] == do_urlencode)
    else:
        # custom urlencode
        assert(filter_module.filters()['urlencode'] == do_urlencode)

    # filter disabled
    assert(filter_module.filters()['urldecode'] == do_urldecode)


# Generated at 2022-06-13 12:29:40.271546
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E4%F6%FC') == u'äöü', 'unicode_urldecode() failed'


# Generated at 2022-06-13 12:29:45.940911
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode']("a%2Fb") == "a/b"
    # Jinja2 v2.7 urlencode filter is supposed to be better.
    # So if it is available, we don't test our filters.
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode']("a b") == "a+b"

# Generated at 2022-06-13 12:29:56.881013
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('/') == '/'
    assert unicode_urlencode('/foo') == '/foo'
    assert unicode_urlencode('/foo bar') == '/foo%20bar'
    assert unicode_urlencode('/foo bar', for_qs=True) == '/foo+bar'
    assert unicode_urlencode('/foo+') == '/foo%2B'
    assert unicode_urlencode('/foo+', for_qs=True) == '/foo%2B'
    assert unicode_urlencode(u'/foo+') == '/foo%2B'
    assert unicode_urlencode(u'/foo+', for_qs=True) == '/foo%2B'


# Generated at 2022-06-13 12:29:58.837544
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert 'test' == unicode_urldecode('test')
    assert 'test test' == unicode_urldecode('test%20test')



# Generated at 2022-06-13 12:30:01.099948
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    import sys
    if not sys.version_info.major == 2:
        assert unicode_urldecode("%C3%A9") == "é"
    assert unicode_urldecode("%25") == "%"


# Generated at 2022-06-13 12:30:05.132833
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' unicode_urldecode should decode a unicode string '''
    assert unicode_urldecode(u'T%C3%BCrgi%C3%9F') == u'Türgiß'



# Generated at 2022-06-13 12:30:12.665582
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic

    # Setup
    filter_module = FilterModule()

    assert 'urldecode' in filter_module.filters()

    if not HAS_URLENCODE:
        assert 'urlencode' in filter_module.filters()
    else:
        assert 'urlencode' not in filter_module.filters()

    # Review
    assert filter_module.filters()['urldecode']('Path%20Name') == 'Path Name'

    if not HAS_URLENCODE:
        assert filter_module.filters()['urlencode']('Path Name') == 'Path%20Name'


# Generated at 2022-06-13 12:30:14.647820
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ansible_filters = FilterModule().filters()
    assert 'urldecode' in ansible_filters
    assert 'urlencode' in ansible_filters


# Generated at 2022-06-13 12:30:24.887345
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    value = "%C3%B8l"
    expected_result = "øl"
    result = unicode_urldecode(value)
    assert result == expected_result, "Test1: Got '%s' instead of '%s' " % (result, expected_result)
    value = "abc+xyz"
    expected_result = "abc xyz"
    result = unicode_urldecode(value)
    assert result == expected_result, "Test2: Got '%s' instead of '%s' " % (result, expected_result)
    value = "abc%2Cdef"
    expected_result = "abc,def"
    result = unicode_urldecode(value)

# Generated at 2022-06-13 12:30:32.241458
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode
    elif 'urlencode' in filters:
        assert filters['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:30:42.230430
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert unicode_urldecode('abc') == u'abc'
    assert unicode_urldecode('%27c%27') == u"'c'"
    assert unicode_urldecode('%27c%27') == u"'c'"
    assert unicode_urldecode(u'%27c%27') == u"'c'"

    assert unicode_urlencode(u'abc') == u'abc'
    assert unicode_urlencode(u'%c') == u'%25c'
    assert unicode_urlencode(u'abc/xyz') == u'abc%2Fxyz'
    assert unicode_urlencode(u'abc', for_qs=True) == u'abc'
    assert unicode_urlencode(u'%c', for_qs=True)

# Generated at 2022-06-13 12:30:43.691005
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']('hello%20world') == 'hello world'



# Generated at 2022-06-13 12:30:49.571742
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert hasattr(filters, 'urldecode')
    assert hasattr(filters, 'urlencode')

# Generated at 2022-06-13 12:30:55.677951
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    result = unicode_urldecode("name=David%20Wagner&age=28")
    # name=David Wagner&age=28
    if result != u'name=David Wagner&age=28':
        raise AssertionError("unicode_urldecode(name=David%20Wagner&age=28)")
    result = unicode_urldecode("%32%65%67%30%2E%30%37%33%37%30%36%32%31%37%39%32%36%30%30%31%37%38%33%36%2E%36%31%38%33%37%2E%34%38%38%31%2E%33%38%36%38%29")
    # (2eg0.07370621"

# Generated at 2022-06-13 12:31:05.222855
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' urldecode - test urldecode function '''
    assert unicode_urldecode('test+test') == 'test test'
    assert unicode_urldecode('test%20test') == 'test test'
    assert unicode_urldecode('%0Atest') == '\ntest'
    assert unicode_urldecode('%0D%0Atest') == '\r\ntest'


# Generated at 2022-06-13 12:31:12.623611
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    from ansible.module_utils.six import b
    from sys import version_info

    if version_info.major == 2 and version_info.minor == 6:
        return

    assert unicode_urlencode('test string') == 'test%20string'
    assert unicode_urlencode('test string') == 'test%20string'
    assert unicode_urlencode(u'test string') == 'test%20string'
    assert unicode_urlencode('test string') == 'test%20string'

    if version_info.major == 2:
        assert unicode_urlencode(b('test string')) == 'test%20string'
        assert unicode_urlencode(b('test string')) == 'test%20string'

# Generated at 2022-06-13 12:31:28.400951
# Unit test for function do_urlencode
def test_do_urlencode():
    import pytest
    from ansible.module_utils.six.moves.urllib.parse import quote, quote_plus, unquote_plus

    assert do_urlencode('foo') == quote('foo')
    assert do_urlencode('foo bar') == quote('foo bar')
    assert do_urlencode('foo+bar') == quote('foo+bar')
    assert do_urlencode('foo,bar') == quote('foo,bar')
    assert do_urlencode('foo/bar') == quote('foo/bar')
    assert do_urlencode(u'foo\u2122') == quote(u'foo\u2122')


# Generated at 2022-06-13 12:31:29.911221
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    print("=> test_FilterModule_filters()")


# Generated at 2022-06-13 12:31:30.807750
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    f = FilterModule()
    assert f.filters() != None


# Generated at 2022-06-13 12:31:37.502018
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert(unicode_urldecode('%E6%B5%B7%E8%B4%BC%E7%B2%89') ==
           u'海贼粉')
    assert(unicode_urldecode('%E6%B5%B7%E8%B4%BC%E7%B2%89%20%E5%A4%A9%E8%B0%83%E7%9A%84%E8%B1%86') ==
           u'海贼粉 天调的豆')


# Generated at 2022-06-13 12:31:41.817345
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Create instance of class FilterModule
    fm = FilterModule()
    # Assert filters() returns expected dictionary
    assert fm.filters() == {
        'urldecode': do_urldecode,
        'urlencode': do_urlencode,
    }

# Generated at 2022-06-13 12:31:50.096178
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%3A') == ':'
    assert unicode_urldecode('%3a') == ':'
    assert unicode_urldecode('%3Aa%2Fb') == ':a/b'
    assert unicode_urldecode('%3aa%2fb') == ':a/b'
    assert unicode_urldecode('%3Aa%2Fb%3Fc%3Dd') == ':a/b?c=d'
    assert unicode_urldecode('%3aa%2fb%3fc%3dd') == ':a/b?c=d'


# Generated at 2022-06-13 12:32:08.020435
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'foo bar') == u'foo bar'
    assert unicode_urldecode(u'%E2%98%83%F0%9F%90%B6%E2%98%83') == u'\u2603\U0001f306\u2603'
    assert unicode_urldecode(u'%E2%98%83%F0%9F%90%B6%E2%98%83', encoding='latin1') == u'\u2603\U0001f306\u2603'
    assert unicode_urldecode(u'%E2%98%83%F0%9F%90%B6%E2%98%83', errors='replace') == u'\u2603\ufffd\u2603'

# Generated at 2022-06-13 12:32:15.730345
# Unit test for function unicode_urldecode

# Generated at 2022-06-13 12:32:26.805629
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    val = basic._URLencode(b'a&b')
    assert val.encode('ascii') == b'a%26b'

    val = basic._URLencode(u'a&b')
    assert val == u'a%26b'

    val = basic._URLencode(u'a+b')
    assert val == u'a%2Bb'

    val = basic._URLencode(u'a b')
    assert val == u'a%20b'

    val = basic._URLencode(u'a/b')
    assert val == u'a%2Fb'

    val = basic._URLencode(u'a/b', for_qs=True)

# Generated at 2022-06-13 12:32:33.548152
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('~:+') == '~%3A%2B'

    assert do_urlencode({'a': 'b', 'c': ['d', 'e']}) == 'a=b&c=d&c=e'

    assert do_urlencode('~:+') == do_urlencode({'~:+': None})

    assert do_urlencode(None) == 'None'

    assert do_urlencode('/') == '%2F'

# Generated at 2022-06-13 12:32:37.733662
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.module_utils import basic

    fm = FilterModule()
    assert 'urldecode' in fm.filters()

    # Since Jinja2 v2.7 we should have urlencode
    assert 'urlencode' in fm.filters()



# Generated at 2022-06-13 12:32:41.688966
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('test') == 'test'
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%2F') == '/'
    assert unicode_urldecode('%25') == '%'
    assert unicode_urldecode('%3A') == ':'



# Generated at 2022-06-13 12:32:46.055669
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()
    assert fm.filters()['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:32:48.803166
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("hello") == u"hello"
    assert unicode_urldecode("hello+world") == u"hello world"
    assert unicode_urldecode("hello%20world") == u"hello world"
    assert unicode_urldecode("hello%2Bworld") == u"hello+world"



# Generated at 2022-06-13 12:32:54.804585
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"hi there") == u"hi%20there"
    assert unicode_urlencode(u"hi there", for_qs=True) == u"hi+there"
    assert unicode_urlencode(u"/") == u"%2F"
    assert unicode_urlencode(u"/", for_qs=True) == u"%2F"



# Generated at 2022-06-13 12:32:59.422636
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test_str = 'The quick brown fox jumps over the lazy dog'
    from ansible.module_utils.six.moves.urllib.parse import quote
    encoded = quote(test_str)

    assert unicode_urldecode(encoded) == test_str

# Generated at 2022-06-13 12:33:17.296169
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fi = FilterModule()
    filters = fi.filters()
    assert filters['urldecode']('%20') == ' '
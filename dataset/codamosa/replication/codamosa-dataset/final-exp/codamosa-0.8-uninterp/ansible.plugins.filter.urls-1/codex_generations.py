

# Generated at 2022-06-13 12:23:22.559549
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('abcd efgh') == 'abcd%20efgh'
    assert unicode_urlencode({'k': 'abcd efgh'}) == 'k=abcd%20efgh'
    assert unicode_urlencode({'k': 'abcd efgh', 'l': 'ijkl'}) == 'k=abcd%20efgh&l=ijkl'
    assert unicode_urlencode([{'k': 'abcd efgh'}, {'l': 'ijkl'}]) == 'k=abcd%20efgh&l=ijkl'



# Generated at 2022-06-13 12:23:29.109234
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%20') == ' '
    assert unicode_urldecode(b'%20') == ' '
    assert unicode_urldecode(b'%C3%B6') == u'ö'
    assert unicode_urldecode(b'%C3%B6') == u'ö'


# Generated at 2022-06-13 12:23:37.620580
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    test_strings = {
        b'foobar': u'foobar',
        b'Hello%20World': u'Hello World',
        b'%7e': u'~',
        u'foobar': u'foobar',
        u'Hello%20World': u'Hello World',
        u'%7e': u'~',
    }
    for test_value in test_strings:
        assert unicode_urldecode(test_value) == test_strings[test_value]



# Generated at 2022-06-13 12:23:47.897691
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u"this is a test") == u"this+is+a+test"
    assert unicode_urlencode(u"this is a test", for_qs=True) == u"this%20is%20a%20test"

    assert u'%E2%98%83' == unicode_urlencode(u'\u2603')
    assert u'%E2%98%83' == unicode_urlencode(u'\\u2603')

    assert unicode_urlencode(u'/') == u'/'
    assert unicode_urlencode(u'//') == u'%2F%2F'
    assert unicode_urlencode(u'///') == u'%2F%2F%2F'

# Generated at 2022-06-13 12:23:52.564926
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters()['urldecode']('a+b') == 'a b'
    assert FilterModule().filters()['urldecode']('a%20b') == 'a b'
    assert FilterModule().filters()['urldecode']('a%2Bb') == 'a+b'



# Generated at 2022-06-13 12:23:55.985028
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert(unicode_urlencode("foo bar") == "%s foo bar" % '%20')
    assert(unicode_urlencode("foo/bar") == "foo%sbar" % '%2F')



# Generated at 2022-06-13 12:24:05.921511
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('www.server.com') == 'www.server.com'
    assert unicode_urldecode('www.server.com/path') == 'www.server.com/path'
    assert unicode_urldecode('www.server.com/path?arg') == 'www.server.com/path?arg'
    assert unicode_urldecode('www.server.com/path?arg=value') == 'www.server.com/path?arg=value'

    assert unicode_urldecode('www.server.com%2Fpath') == 'www.server.com/path'
    assert unicode_urldecode('www.server.com/path%3Farg') == 'www.server.com/path?arg'
    assert unicode_urldecode

# Generated at 2022-06-13 12:24:12.849298
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    string = u'foo/bar%3Fa%3D1%26b%3D2'
    assert string == unicode_urldecode(string)

    string = b'foo/bar%3Fa%3D1%26b%3D2'
    assert string == unicode_urldecode(string)

    string = u'foo/bar?a=1&b=2'
    assert string == unicode_urldecode(string)

    string = b'foo/bar?a=1&b=2'
    assert string == unicode_urldecode(string)


# Generated at 2022-06-13 12:24:15.583528
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Zm9vJTI1YmFyJTI1YmF6') == u'foo%bar%baz'



# Generated at 2022-06-13 12:24:17.944127
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'dag%40wieers.com') == u'dag@wieers.com'



# Generated at 2022-06-13 12:24:21.301005
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    fm.filters()



# Generated at 2022-06-13 12:24:23.840877
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    _filter = FilterModule()
    result_filters = {"urldecode":FilterModule.filters}

    assert result_filters == _filter.filters()


# Generated at 2022-06-13 12:24:27.748654
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('\u20ac') == u'%E2%82%AC'
    assert unicode_urlencode('\u20ac', for_qs=True) == u'%E2%82%AC'



# Generated at 2022-06-13 12:24:32.221790
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    value = '%C3%A9'
    expected = u'é'
    result = unicode_urldecode(value)
    assert expected == result

if __name__ == '__main__':
    import sys
    sys.exit(test_unicode_urldecode())

# Generated at 2022-06-13 12:24:33.953814
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # TODO: Implement me!
    assert True


# Generated at 2022-06-13 12:24:37.922943
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    try:
        unicode_urldecode('%')
        raise AssertionError('unicode_urldecode should fail')
    except TypeError:
        pass
    assert unicode_urldecode(u'%20') == u' '
    assert unicode_urldecode('%20') == u' '



# Generated at 2022-06-13 12:24:45.295178
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:24:51.298013
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    m = FilterModule()
    filters = m.filters()
    assert filters['urldecode'] == do_urldecode
    assert filters['urlencode'] == do_urlencode if not HAS_URLENCODE else do_urlencode


# Generated at 2022-06-13 12:25:00.824472
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys
    import unittest
    import tempfile
    import shutil


# Generated at 2022-06-13 12:25:05.207340
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
  assert unicode_urlencode("foo") == u'foo'
  assert unicode_urlencode("foo/bar") == u'foo/bar'
  assert unicode_urlencode("foo bar") == u'foo%20bar'
  assert unicode_urlencode("foo bar", 1) == u'foo+bar'


# Generated at 2022-06-13 12:25:12.394221
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    test_string = u'"quoted" \'string\''
    expected = u'"quoted"+%27string%27'
    result = unicode_urlencode(test_string, for_qs=True)
    print(u"input {0} encoded to {1}, expected {2}".format(test_string, result, expected))
    if result != expected:
        raise ValueError(u"Error encoding {0}: Received {1} but expected {2}".format(test_string, result, expected))


# Generated at 2022-06-13 12:25:19.567799
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fmod = FilterModule()
    filters = fmod.filters()
    import os
    import sys
    if os.path.exists('/tmp/ansible_urldecode.ret'):
        os.remove('/tmp/ansible_urldecode.ret')
    if os.path.exists('/tmp/ansible_urlencode.ret'):
        os.remove('/tmp/ansible_urlencode.ret')

    # Unit test for urldecode filter.
    #
    # echo "testdata" > /tmp/ansible_urldecode.in
    # python jinja2 filters/core.py test_FilterModule_filters urldecode
    # diff /tmp/ansible_urldecode.in /tmp/ansible_urldecode.ret
   

# Generated at 2022-06-13 12:25:22.534315
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urlencode({'key': 'value'}) == u'key=value'
    assert do_urldecode(u'Ansible%20is%20awesome') == u'Ansible is awesome'

# Generated at 2022-06-13 12:25:26.740163
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    ansible_base.ANSIBLE_MODULE_ARGS = {'ANSIBLE_MODULE_ARGS': '{"foo":"bar"}'}
    module_name = 'FilterModule'
    class_name = 'FilterModule'
    method_name = 'filters'
    ansible_base.moduletest(module_name, class_name, method_name,
                            os.path.join(test_folder, 'tests'))

# Generated at 2022-06-13 12:25:29.600245
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello+world'
    assert do_urlencode({'a': 'hello', 'b': 'world'}) == 'a=hello&b=world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'

# Generated at 2022-06-13 12:25:39.649684
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc') == 'abc'
    assert unicode_urldecode('%2F') == '/'
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%3A') == ':'
    assert unicode_urldecode('%2F%3A%20') == '/: '
    assert unicode_urldecode('a%2F%3A%20b') == 'a/:  b'



# Generated at 2022-06-13 12:25:44.725767
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'Hello%20World%21') == u'Hello World!'
    assert unicode_urldecode(u'Hello%2BWorld%21') == u'Hello+World!'
    assert unicode_urldecode(u'Hello%252BWorld%2521') == u'Hello%2BWorld%21'

# Generated at 2022-06-13 12:25:53.599289
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%2A') == '*'
    assert unicode_urldecode('%252A') == '%2A'
    assert unicode_urldecode('%7E') == '~'
    assert unicode_urldecode('%24') == '$'
    assert unicode_urldecode('%25') == '%'
    assert unicode_urldecode('%3C') == '<'
    assert unicode_urldecode('%3E') == '>'
    assert unicode_urldecode('%26') == '&'
    assert unicode_urldecode('%23') == '#'

# Generated at 2022-06-13 12:26:07.534133
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"

# Generated at 2022-06-13 12:26:12.759094
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()

    assert isinstance(filters, dict)
    assert len(filters) == 2

    if HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode
    else:
        assert filters['urlencode'] == do_urlencode

    assert filters['urldecode'] == do_urldecode

# Generated at 2022-06-13 12:26:15.865449
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    assert unicode_urldecode('%E2%82%AC') == '€'



# Generated at 2022-06-13 12:26:20.220147
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%25') == '%'
    assert unicode_urldecode('%25A') == '%A'
    assert unicode_urldecode('%25A%20') == '%A '
    assert unicode_urldecode('%25A%20%20b') == '%A  b'

# Generated at 2022-06-13 12:26:29.893659
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://foo.com/bar') == u'http%3A%2F%2Ffoo.com%2Fbar'
    assert unicode_urlencode(u'http://foo.com/bar#baz') == u'http%3A%2F%2Ffoo.com%2Fbar%23baz'
    assert unicode_urlencode(u'http://foo.com/bar?a&b=c') == u'http%3A%2F%2Ffoo.com%2Fbar%3Fa%26b%3Dc'

# Generated at 2022-06-13 12:26:36.587716
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('100%25%2B') == u'100%+'

    if not HAS_URLENCODE:
        assert do_urlencode('100%+') == u'100%25%2B'
        assert do_urlencode({'a': '1', 'b': '2'}) == u'a=1&b=2'
    else:
        assert do_urlencode({'a': '1', 'b': '2'}) == u'a=1&b=2'


if __name__ == '__main__':
    import pytest

    pytest.main()

# Generated at 2022-06-13 12:26:39.291496
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    """
    Unit test for method filters of class FilterModule
    """
    obj = FilterModule()
    method = getattr(obj, "filters")
    result = method()
    assert isinstance(result, dict)



# Generated at 2022-06-13 12:26:41.626883
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    value = u'a string with spaces'
    assert do_urlencode(value) == 'a+string+with+spaces'
    assert do_urldecode(do_urlencode(value)) == value

# Generated at 2022-06-13 12:26:42.652859
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    obj = FilterModule()
    print(obj.filters())


# Generated at 2022-06-13 12:26:48.176200
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    assert unicode_urldecode('a+b&c=d') == 'a b&c=d'
    assert unicode_urldecode('+') == ' '
    assert unicode_urldecode('a%20b') == 'a b'
    assert unicode_urldecode('%5C%5C') == '\\\\'
    assert unicode_urldecode('%5c%5c') == '\\\\'



# Generated at 2022-06-13 12:26:50.535183
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E5%AE%A2%E6%88%B7%E7%A0%81') == u'客户码'


# Generated at 2022-06-13 12:26:58.512832
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from jinja2 import Environment
    import os
    import sys

    # Set PYTHONPATH for testing
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

    from ansible.module_utils.common.collections import is_iterable

    jinja_env = Environment()


# Generated at 2022-06-13 12:27:03.842996
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert 'urldecode' in filters
    assert 'urlencode' in filters
    assert filters['urldecode'] == do_urldecode
    assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:27:11.117880
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert filters['urldecode']('a%20b%3Cc%3E') == 'a b<c>'
    assert filters['urldecode']('abc') == 'abc'
    if not HAS_URLENCODE:
        assert filters['urlencode']('a1b2c3') == 'a1b2c3'
        assert filters['urlencode']('a1 b2 c3') == 'a1%20b2%20c3'

# Generated at 2022-06-13 12:27:21.742915
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.compat.tests import unittest

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught by the test case"""
        pass

    def exit_json(*args, **kwargs):
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        kwargs['failed'] = True
        raise AnsibleFailJson(kwargs)

    def get_bin_path(arg, required=False):
        return

# Generated at 2022-06-13 12:27:32.422053
# Unit test for function unicode_urldecode
def test_unicode_urldecode():

    test_str1 = (
        "If you want to encode special characters, such as spaces, you can replace"
        " space with '%20' or '+' depending on the needs of your application."
    )

# Generated at 2022-06-13 12:27:39.484692
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('?&=') == to_text(quote_plus(b'?&='))
    assert unicode_urlencode(None) == to_text(quote_plus(b'None'))
    assert unicode_urlencode('123') == to_text(quote_plus(b'123'))
    assert unicode_urlencode(u'123') == to_text(quote_plus(b'123'))
    assert unicode_urlencode({'a': 'a', 'b': 'b'}) == to_text(quote_plus(b'a=a&b=b'))
    assert unicode_urlencode(['a', 'b']) == to_text(quote_plus(b'a&b'))



# Generated at 2022-06-13 12:27:45.025631
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    # filter is new in Ansible 2.5
    # filter was modified in Ansible 2.7
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] == do_urldecode
    if HAS_URLENCODE:
        assert filters['urlencode'] != do_urlencode
    else:
        assert filters['urlencode'] == do_urlencode



# Generated at 2022-06-13 12:27:53.272223
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import os
    import sys
    import unittest
    import ansible.module_utils.basic

    class TestClass(unittest.TestCase):
        def setUp(self):
            self.filtermodule = FilterModule()

        @unittest.skipIf(HAS_URLENCODE, 'Not applicable')
        def test_urlencode(self):
            for s in [u'', u':', u'::', u'*']:
                expected = quote_plus(s)
                actual = self.filtermodule.filters()['urlencode'](s)
                self.maxDiff = None
                self.assertEqual(actual, expected)

        def test_urldecode(self):
            for s in [u'', u':', u'::', u'*']:
                expected = unquote_plus

# Generated at 2022-06-13 12:27:56.597888
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert filters['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filters['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:28:09.601845
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():  # pylint: disable=too-many-statements
    import os
    import imp
    import sys

    # Find our path
    path = os.path.join(os.path.dirname(__file__), '..')
    path = os.path.abspath(path)

    # Make sure we import the right plugin
    libdir = os.path.join(path, 'lib')
    sys.path.insert(0, libdir)

    #
    f = imp.load_source('_filter_module', os.path.join(path, 'plugins/filter/core.py'))
    FilterModule = f.FilterModule
    # Import our plugin and get it ready to test
    f = FilterModule()
    (success, results) = f.filters()


# Generated at 2022-06-13 12:28:14.283550
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Prepare mocks
    results = dict()

    # Run method
    obj = FilterModule()
    filters = obj.filters()

    # Check
    assert len(results) == 0, "Method FilterModule.filters has not been called."
    assert isinstance(filters, dict)
    assert set(filters) == set(['urldecode', 'urlencode'])
    assert filters['urldecode'] == do_urldecode


# Generated at 2022-06-13 12:28:18.678561
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    assert fm.filters()['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert fm.filters()['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:28:25.799806
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode(u'http://example.com/') == u'http%3A//example.com/' # noqa: E501
    assert unicode_urlencode(u'http://example.com/:') == u'http%3A//example.com/%3A' # noqa: E501
    assert unicode_urlencode(u'http://example.com/', for_qs=True) == u'http%3A%2F%2Fexample.com%2F' # noqa: E501
    assert unicode_urlencode(u'http://example.com/:', for_qs=True) == u'http%3A%2F%2Fexample.com%2F%3A' # noqa: E501

# Generated at 2022-06-13 12:28:29.975448
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    if not PY3:
        assert unicode_urldecode('%20') == to_text(unquote_plus(to_bytes('%20')))
    else:
        assert unicode_urldecode('%20') == unquote_plus('%20')



# Generated at 2022-06-13 12:28:37.106086
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('https://www.example.com/testing?param=1&param=2') == u'https%3A%2F%2Fwww.example.com%2Ftesting%3Fparam%3D1%26param%3D2'
    assert unicode_urlencode('https://www.example.com/testing?param=1&param=2', True) == u'https%3A%2F%2Fwww.example.com%2Ftesting%3Fparam%3D1%26param%3D2'
    assert unicode_urlencode('https://www.example.com/testing/foo bar') == u'https%3A%2F%2Fwww.example.com%2Ftesting%2Ffoo%20bar'

# Generated at 2022-06-13 12:28:44.396347
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    from urllib import quote_plus
    test_values = ('string with spaces', 'string with plus signs+', 'string with %20')
    for value in test_values:
        expected = unicode(unquote_plus(quote_plus(value)))
        actual = unicode_urldecode(quote_plus(value))
        assert expected == actual, "failed to encode and decode '%s' correctly" % value

if __name__ == '__main__':
    test_unicode_urldecode()
    print("PASSED")

# Generated at 2022-06-13 12:28:51.895918
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert('本日は晴天なり' == unicode_urldecode('%E6%9C%AC%E6%97%A5%E3%81%AF%E6%99%B4%E5%A4%A9%E3%81%AA%E3%82%8A'))
    assert('오늘은 맑음' == unicode_urldecode('%EC%98%A4%EB%8A%98%EC%9D%80%20%EB%A7%91%EC%9D%8C'))

# Generated at 2022-06-13 12:28:56.003566
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    result = fm.filters()
    assert result
    assert result['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert result['urlencode'] == do_urlencode


# Generated at 2022-06-13 12:28:58.387463
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert isinstance(filters, dict)

    assert 'urldecode' in filters
    assert 'urlencode' in filters



# Generated at 2022-06-13 12:29:04.997462
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    # from http://tools.ietf.org/html/rfc3986#section-2
    # and http://tools.ietf.org/html/rfc3986#section-2.1
    assert unicode_urlencode(u'foo') == u'foo'
    assert unicode_urlencode(u'foo bar') == u'foo%20bar'

    assert unicode_urlencode(u'foo*') == u'foo*'
    assert unicode_urlencode(u'foo+') == u'foo+'
    assert unicode_urlencode(u'foo bar', for_qs=True) == u'foo+bar'
    assert unicode_urlencode(u'foo/') == u'foo%2F'
    assert unicode_urlencode(u'foo?') == u

# Generated at 2022-06-13 12:29:14.537264
# Unit test for function do_urlencode
def test_do_urlencode():
    # function do_urlencode should return a string.  The string
    # is expected to be the result of urlencoding the input.
    # Intentionally test edge cases to verify the urlencoding is correct.
    # Also test that even if we use unicode as input we return a string type.

    # First test that we correctly handle unicode string inputs:
    urls_to_try = [u'http://www.test.com/with space']
    for url in urls_to_try:
        # urls_to_try contains unicode strings.
        assert isinstance(url, str)
        assert isinstance(do_urlencode(url), str)

    # Test that we correctly encode non-ascii urls:

# Generated at 2022-06-13 12:29:20.212408
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    filters = fm.filters()
    assert 'urlencode' in filters
    # TODO: find simple and reliable test for do_urlencode
    #assert 'urldecode' in filters


# Generated at 2022-06-13 12:29:28.685227
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://foo.com/') == 'http%3A//foo.com/'
    assert unicode_urlencode('http://foo.com/', for_qs=True) == 'http%3A%2F%2Ffoo.com%2F'
    assert unicode_urlencode('http://foo.com/?id=1&num=2') == 'http%3A%2F%2Ffoo.com%2F%3Fid%3D1%26num%3D2'
    assert unicode_urlencode('http://foo.com/?id=1&num=2', for_qs=True) == 'http%3A%2F%2Ffoo.com%2F%3Fid%3D1%26num%3D2'



# Generated at 2022-06-13 12:29:38.722272
# Unit test for function do_urlencode
def test_do_urlencode():
    assert '/' == do_urlencode('/')
    assert '%2F' == do_urlencode('/', for_qs=True)
    assert 'some+key' == do_urlencode('some key')
    assert 'some%20key' == do_urlencode('some key', for_qs=True)
    assert 'some+key%3Dsome+value' == do_urlencode({'some key': 'some value'})
    assert 'a=b+c=d' == do_urlencode(['a', 'b c=d'])
    assert 'a=b+c=d' == do_urlencode(('a', 'b c=d'))

# Generated at 2022-06-13 12:29:48.167024
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Valid cases
    assert unicode_urldecode("Hello World!") == "Hello World!"
    assert unicode_urldecode("Hello+World!") == "Hello World!"
    assert unicode_urldecode("Hello%20World!") == "Hello World!"
    assert unicode_urldecode("Hello%2BWor%6cd!") == "Hello+Wor ld!"
    assert unicode_urldecode("%F0%9F%98%82") == u"\U0001F602"
    # Invalid cases
    assert unicode_urldecode("%F0") == u"%F0"
    assert unicode_urldecode("%FG") == u"%FG"
    assert unicode_urldecode("%%FG") == u"%%FG"

# Unit

# Generated at 2022-06-13 12:29:50.001390
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule().filters() is not None  # will fail if it is None


# Generated at 2022-06-13 12:29:57.690179
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('string') == 'string'
    assert unicode_urldecode('%20') == ' '
    assert unicode_urldecode('%2520') == '%20'
    assert unicode_urldecode('%25') == '%'
    assert unicode_urldecode('%2525') == '%25'
    assert unicode_urldecode('%E3%81%82') == u'あ'
    assert unicode_urldecode('x%E3%81%82') == u'xあ'
    assert unicode_urldecode('%E3%81x') == u'あx'
    assert unicode_urldecode('%E3%81%82x') == u'あx'
    assert unicode_urld

# Generated at 2022-06-13 12:30:03.267833
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    import unittest
    class TestUrlencode(unittest.TestCase):

        def test_none(self):
            assert unicode_urlencode(None) == ''

        def test_string(self):
            assert unicode_urlencode('foo') == 'foo'

        def test_unicode_string(self):
            assert unicode_urlencode(u'föo') == u'f%C3%B6o'

        def test_dict(self):
            assert unicode_urlencode({'foo': u'föo', 'bar': 'baz'}) == u'foo=f%C3%B6o&bar=baz'


# Generated at 2022-06-13 12:30:06.249628
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert do_urlencode(u"¿ ї і") == u"%C2%BF%20%D1%97%20%D1%96"



# Generated at 2022-06-13 12:30:08.416947
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'a%40b%20c') == u'a@b c'
    assert unicode_urldecode(to_bytes(u'a%40b%20c')) == u'a@b c'


# Generated at 2022-06-13 12:30:12.278730
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('Donald+Knuth') == 'Donald Knuth'
    assert unicode_urldecode('Donald%2BKnuth') == 'Donald%2BKnuth'
    assert unicode_urldecode('Donald+Knuth%26Donald+Knuth') == 'Donald Knuth&Donald Knuth'


# Generated at 2022-06-13 12:30:23.884565
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import ansible.module_utils.six as six

    # Test urldecode

# Generated at 2022-06-13 12:30:28.825519
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'foo/bar' == unicode_urldecode(u'foo%2Fbar')
    assert u'foo bar' == unicode_urldecode(u'foo+bar')
    assert u'foo:bar' == unicode_urldecode(u'foo:bar')


# Generated at 2022-06-13 12:30:35.352942
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    import sys, inspect
    if sys.version_info[0] < 3:
        reload(sys)
        sys.setdefaultencoding('utf-8')
    if sys.version_info[0] == 2:
        assert unicode_urldecode('foo%20bar%2Fbaz') == 'foo bar/baz'
        assert unicode_urlencode('foo bar/baz') == 'foo%20bar/baz'
        assert unicode_urlencode('foo bar/baz', for_qs=True) == 'foo+bar%2Fbaz'
        assert unicode_urlencode({'foo bar/baz': 'foo+bar/baz'}) == 'foo%20bar%2Fbaz=foo%2Bbar%2Fbaz'

# Generated at 2022-06-13 12:30:44.176933
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # If Jinja2 v2.7 is available, we assume the urlencode filter works
    if HAS_URLENCODE:
        url_filters = [
            'urldecode',
            'urlencode'
        ]
        assert url_filters == FilterModule.filters(FilterModule)

    else:
        # Unit test FilterModule.filters() with Jinja2 v2.6 and older
        class FauxFilterModule(FilterModule):
            def filters(self):
                return FilterModule.filters(FilterModule)

        # Unit test urldecode
        assert 'ansible' == FauxFilterModule.filters(FauxFilterModule)['urldecode']('ansible')

        # Unit test urlencode

# Generated at 2022-06-13 12:30:46.729457
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    # Test valid operations
    assert unicode_urldecode("test%20space") == u"test space"
    assert unicode_urldecode("test+plus") == u"test+plus"
    assert unicode_urldecode("%2B") == u"+"


# Generated at 2022-06-13 12:30:52.915316
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('http://foo/bar') == 'http%3A//foo/bar'
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode('/') == '%2F'
    assert unicode_urlencode('foo+bar') == 'foo%2Bbar'
    assert unicode_urlencode('foo+bar') == 'foo%2Bbar'
    assert unicode_urlencode('foo bar') == 'foo+bar'
    assert unicode_urlencode({'foo': 'bar'}) == 'foo=bar'
    assert unicode_urlencode(['foo', 'bar']) == 'foo=bar'

# Generated at 2022-06-13 12:30:55.098892
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%E6%97%A5%E6%9C%AC%E8%AA%9E') == u'\u65e5\u672c\u8a9e'



# Generated at 2022-06-13 12:31:00.580823
# Unit test for function do_urlencode

# Generated at 2022-06-13 12:31:06.503808
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    # Create class 'FilterModule'
    fm = FilterModule()
    # Verify 'urldecode' filter
    assert fm.filters().get('urldecode') == do_urldecode

    if not HAS_URLENCODE:
        # Verify 'urlencode' filter
        assert fm.filters().get('urlencode') == do_urlencode

# Generated at 2022-06-13 12:31:14.724371
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'Привет Мир!') == 'Привет Мир!'
    assert unicode_urldecode(u'Hello%20World%21') == 'Hello World!'
    assert unicode_urldecode(u'abc%3A%3F%23') == 'abc:?#'
    assert unicode_urldecode(u'%E3%81%82%E3%81%84%E3%81%86%E3%81%88%E3%81%8A') == \
           u'あいうえお'


# Generated at 2022-06-13 12:31:25.449546
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fltr = FilterModule()
    assert fltr.filters()['urldecode']('%7E') == '~'
    assert fltr.filters()['urldecode']('%7e') == '~'
    assert fltr.filters()['urldecode']('%7E') == '~'
    assert fltr.filters()['urldecode']('%7e') == '~'

# Generated at 2022-06-13 12:31:26.894673
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode('dag%20wieers') == 'dag wieers'


# Generated at 2022-06-13 12:31:31.794762
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%3D%3D%3D') == '==='
    assert unicode_urldecode(u'%3D%3D%3D') == u'==='
    assert unicode_urldecode(b'%3D%3D%3D') == '==='
    assert unicode_urldecode('%3D%3D%3D'.encode('utf-8')) == '==='
    assert unicode_urldecode('%3D%3D%3D'.encode('ascii')) == '==='


# Generated at 2022-06-13 12:31:37.139785
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('abc123') == u'abc123'
    assert unicode_urldecode('%3C%3E') == u'<>'
    assert unicode_urldecode('%3E%3C') == u'><'
    assert unicode_urldecode('%25') == u'%'
    assert unicode_urldecode('%2B') == u'+'
    assert unicode_urldecode('%3D') == u'='
    assert unicode_urldecode('/%25/%2B/%3D') == u'/%/+/='
    assert unicode_urldecode('/%253C/%252B/%253D') == u'/%3C/+/%3D'



# Generated at 2022-06-13 12:31:41.876741
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Unit test for class FilterModule with method filters
    ##########################################################################
    # FilterModule.filters()
    test_obj = FilterModule()
    assert test_obj.filters() == {'urldecode': do_urldecode, 'urlencode': do_urlencode}


# Generated at 2022-06-13 12:31:46.126741
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode(u'%20%2F%40%21%3F') == u' /@!?', \
        repr(unicode_urldecode(u'%20%2F%40%21%3F'))


# Generated at 2022-06-13 12:31:48.840761
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode("a+%20test%2B%2F%C3%A5%C3%A5") == "a test+/åå"



# Generated at 2022-06-13 12:31:56.064013
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert FilterModule.filters(None)['urldecode'](
        'a%2Bb%2Bc%2Bd%2Be%2Bf%2Bg%2Bh%2Bi%2Bj') == 'a+b+c+d+e+f+g+h+i+j'
    assert FilterModule.filters(None)['urldecode']('a+b+c') == 'a b c'

# Generated at 2022-06-13 12:32:01.075555
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert u'foo bar' == unicode_urldecode(u'foo+bar')
    assert u'François&Jacques' == unicode_urldecode(u'Fran%C3%A7ois%26Jacques')


# Generated at 2022-06-13 12:32:03.864177
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    frm = FilterModule()
    assert hasattr(frm, 'filters')
    assert callable(frm.filters)
    assert len(frm.filters()) > 0


# Generated at 2022-06-13 12:32:14.214795
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():

    FILTERS = FilterModule().filters()

    # dict
    assert FILTERS['urldecode']({'a': 1}) == 'a=1'
    assert FILTERS['urldecode']({'a': 'b'}) == 'a=b'
    assert FILTERS['urldecode']({'a': b'b'}) == 'a=b'
    assert FILTERS['urldecode']({'a': 'b', 'c': 'd'}) == 'a=b&c=d'
    assert FILTERS['urldecode']({'a': 'b', 'c': 'd', 'e': 'f'}) == 'a=b&c=d&e=f'

# Generated at 2022-06-13 12:32:14.725219
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    pass

# Generated at 2022-06-13 12:32:26.476651
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    module = FilterModule()
    filters = module.filters()
    assert filters is not None
    assert hasattr(filters, 'urldecode')
    assert filters.urldecode('%3C') == u'<'
    assert filters.urldecode.__name__ == 'urldecode'
    assert filters.urldecode.__doc__ == (
        'Returns a string that has been decoded from URL-encoding.')
    assert hasattr(filters, 'urlencode')
    assert filters.urlencode(u'<') == '%3C'
    assert filters.urlencode.__name__ == 'urlencode'
    assert filters.urlencode.__doc__ == (
        'Returns a string that has been URL-encoded.')


# Generated at 2022-06-13 12:32:29.231741
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    assert do_urldecode("hello%20world") == "hello world"
    if not HAS_URLENCODE:
        assert do_urlencode("hello world") == "hello%20world"

# Generated at 2022-06-13 12:32:39.495972
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('string') == u'string'
    assert do_urlencode({'k': 'v'}) == u'k=v'
    assert do_urlencode(['key=value']) == u'key%3Dvalue'
    assert do_urlencode(u'абракадабра') == u'%D0%B0%D0%B1%D1%80%D0%B0%D0%BA%D0%B0%D0%B4%D0%B0%D0%B1%D1%80%D0%B0'
    assert do_urlencode(u'☃') == u'%E2%98%83'
    assert do_urlencode(u'/') == u'%2F'

# Generated at 2022-06-13 12:32:44.343138
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('test') == 'test'
    assert unicode_urlencode('test/test/test') == 'test%2Ftest%2Ftest'
    assert unicode_urlencode('test_test_test') == 'test_test_test'
    assert unicode_urlencode('test test test') == 'test+test+test'
    assert unicode_urlencode('test&test=test') == 'test%26test%3Dtest'
    assert unicode_urlencode('test&test=test', True) == 'test%26test%3Dtest'


# Generated at 2022-06-13 12:32:46.055463
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('%5B%5D') == u'[]'


# Generated at 2022-06-13 12:32:52.443082
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('foo') == 'foo'
    assert unicode_urldecode('foo+bar') == 'foo bar'
    assert unicode_urldecode('foo%20bar') == 'foo bar'
    if PY3:
        assert unicode_urldecode(b'foo+bar') == 'foo+bar'
        assert unicode_urldecode(b'foo%20bar') == 'foo%20bar'
    else:
        assert unicode_urldecode(b'foo+bar') == u'foo bar'
        assert unicode_urldecode(b'foo%20bar') == u'foo bar'

# Generated at 2022-06-13 12:32:58.668947
# Unit test for function unicode_urlencode

# Generated at 2022-06-13 12:33:00.749550
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    (filter_module, filter_module_name) = (fm.filters(), 'filters')
    assert filter_module['urldecode'] == do_urldecode
    if not HAS_URLENCODE:
        assert filter_module['urlencode'] == do_urlencode

# Generated at 2022-06-13 12:33:07.401954
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    ''' Test unicode_urldecode function '''
    assert unicode_urldecode('%41%20%41') == u'A A'
    assert unicode_urldecode('%2B') == u'+'
    assert unicode_urldecode(b'%2B') == u'+'


# Generated at 2022-06-13 12:33:14.517320
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    '''Returns the decoded string.'''
    assert unicode_urldecode('fran%C3%A7ois') == u'fran\xe7ois'
    assert unicode_urldecode('fran%c3%a7ois') == u'fran\xe7ois'
    assert unicode_urldecode('fran%20c3%20a7ois') == u'fran c3 a7ois'
    assert unicode_urldecode('fran%20c3%20a7ois', 'utf-8') == u'fran c3 a7ois'


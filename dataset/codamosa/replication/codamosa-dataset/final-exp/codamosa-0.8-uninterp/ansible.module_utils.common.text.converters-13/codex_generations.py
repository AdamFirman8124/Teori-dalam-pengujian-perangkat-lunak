

# Generated at 2022-06-12 23:38:24.978017
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 1}) == '{"a": 1}'
    assert jsonify({u'\xe4': 1}) == '{"ä": 1}'
    assert jsonify({u'\u8349': 1}) == '{"草": 1}'
    assert jsonify({u'\u8349': 1}) == '{"草": 1}'
    assert jsonify({u'\u8349': 1}) == '{"草": 1}'
    assert jsonify([u'\u8349']) == '["草"]'
    assert jsonify([1, u'\u8349']) == '[1, "草"]'

# Generated at 2022-06-12 23:38:31.614225
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({u'foo\u1234': u'bar\u2345'}) == u'{"foo\u1234": "bar\u2345"}'
    assert jsonify({u'foo\u1234': u'bar\u2345'}, encoding='latin-1') == u'{"foo\\u1234": "bar\\u2345"}'



# Generated at 2022-06-12 23:38:40.078806
# Unit test for function to_native
def test_to_native():
    # need to use mock module - otherwise this tries to serialize the whole module
    # and mock module is not compatible with the serialization
    try:
        # mock module was introduced in Python 3.3
        # to support Python 2.6/7 and Python 3.3+ we need different approach
        from unittest import mock
    except ImportError:
        try:
            import mock
        except ImportError:
            # even if we don't have mock module we should be able to continue
            pass

    from ansible.module_utils._text import to_native

    # test identity cases
    x = b'4'
    assert x is to_native(x)
    x = '4'
    assert x is to_native(x)

    # test decoding of bytes to strings
    x = b'4'
    assert u'4' == to

# Generated at 2022-06-12 23:38:51.092234
# Unit test for function to_bytes
def test_to_bytes():
    # Note: These tests are written so that the string's encoding is obvious
    # in the test description.  I.e. to_bytes('\xe9') is a test of converting
    # the latin-1 string '\xe9' to a byte string.

    # Test byte strings
    assert to_bytes('\xe9', nonstring='passthru') == '\xe9'

    # Test mixed strings
    assert to_bytes(u'abc\xe9', encoding='latin-1') == 'abc\xe9'
    assert to_bytes(u'abc\xe9', encoding='utf-8') == 'abc\xc3\xa9'
    assert to_bytes(u'abc\xe9', encoding='utf-8', errors='replace') == 'abc?\xc3\xa9'

# Generated at 2022-06-12 23:38:56.940260
# Unit test for function to_native
def test_to_native():
    assert isinstance(to_native('hello', encoding='latin-1'), text_type)
    assert isinstance(to_native('hello', encoding='ascii'), text_type)
    assert isinstance(to_native(b'hello', encoding='ascii'), text_type)
    assert isinstance(to_native(b'hello\xFF', encoding='ascii', errors='strict'), text_type)
    assert isinstance(to_native(b'hello\xFF', encoding='ascii', errors='ignore'), text_type)
    assert isinstance(to_native(b'hello\xFF', encoding='ascii', errors='replace'), text_type)
    assert isinstance(to_native(b'hello\xFF', encoding='ascii', errors='surrogateescape'), text_type)

# Generated at 2022-06-12 23:38:59.300885
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"f": [0, "a\u20ac"]}) == '{"f": [0, "a\\u20ac"]}'
    assert jsonify({"f": [0, "a\u20ac"]}, ensure_ascii=False) == '{"f": [0, "a\u20ac"]}'



# Generated at 2022-06-12 23:39:04.993249
# Unit test for function to_bytes
def test_to_bytes():
    assert b'Hello' == to_bytes('Hello')
    assert b'Hello' == to_bytes(u'Hello')
    assert b'\xd0\x9f' == to_bytes(u'\u043f', encoding='koi8-r')
    assert b'\xd0\x9f' == to_bytes(u'\u043f', encoding='koi8-r')
    assert b'\xd1\x80' == to_bytes(u'\u0440', encoding='koi8-r')
    assert b'\xd0\xbf' == to_bytes(u'\u043f', encoding='koi8-u')
    assert b'\xd0\xbf' == to_bytes(u'\u043f', encoding='koi8-u')

# Generated at 2022-06-12 23:39:15.730414
# Unit test for function jsonify
def test_jsonify():
    orig_data = dict(
        name=u'foo',
        more_names=[u'bar', u'baz'],
        foo=Set([u'bar', u'baz']),
        time=datetime.datetime.utcnow(),
        foo_bytes=b'\xe9'

    )
    data = dict((to_native(k), v) for (k, v) in iteritems(orig_data))
    ret = jsonify(data)
    assert isinstance(ret, binary_type)
    data = json.loads(ret)
    assert isinstance(data['foo'], list)
    assert data['foo'] == ['bar', 'baz']

    # This is necessary to make tests pass on py33

# Generated at 2022-06-12 23:39:26.672148
# Unit test for function jsonify
def test_jsonify():
    #test jsondump b'str' and u'str'
    assert jsonify(b"str") == ""
    assert jsonify(b"str") == ""
    assert jsonify(b"str", sort_keys=True) == ""
    assert jsonify(b"str", sort_keys=True) == ""
    assert jsonify(u"str") == ""
    assert jsonify(u"str") == ""

    #test jsondump int
    assert jsonify(0) == "0"
    assert jsonify(0, sort_keys=True) == "0"
    assert jsonify(-1) == "-1"
    assert jsonify(-1, sort_keys=True) == "-1"

    #test jsondump list
    assert jsonify([]) == "[]"

# Generated at 2022-06-12 23:39:34.018497
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_bytes
    from ansible.compat.tests import unittest

    class TestJsonify(unittest.TestCase):
        json_data = {u'unicode_key': u'unicode_value'}
        json_str = to_bytes(u'{"unicode_key": "unicode_value"}')

        def test_unicode_json_data(self):
            self.assertEqual(jsonify(self.json_data), self.json_str)

        def test_bytes_json_data(self):
            self.assertEqual(jsonify(self.json_str), self.json_str)

    unittest.main()



# Generated at 2022-06-12 23:40:18.625033
# Unit test for function to_bytes
def test_to_bytes():

    assert b'\xe9\x9d\x92\xe6\xa5\xbd' == to_bytes('\u9d92\u6a5b')

    try:
        assert b'\xe9\x9d\x92\x00\xe6\xa5\xbd' == to_bytes('\u9d92\u6a5b', 'ascii')
    except UnicodeEncodeError:
        pass

    try:
        assert u'\u9d92\u6a5b'.encode(errors='surrogate_or_replace') == to_bytes(u'\u9d92\u6a5b', errors='surrogate_or_replace')
    except AttributeError:
        pass


# Generated at 2022-06-12 23:40:21.740892
# Unit test for function to_native
def test_to_native():
    """
    Test to see if the to_native function returns the correct
    type and values. If a unicode string is passed in and python3 is used,
    we should return a string and drop the u prefix.
    """
    s = to_native("Test string")
    assert isinstance(s, str)

    s = to_native(u"Test string")
    assert isinstance(s, str)
    assert s == "Test string"


# Generated at 2022-06-12 23:40:23.724413
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"foo": u"\u2713"}) == '{"foo": "\\u2713"}'



# Generated at 2022-06-12 23:40:30.192504
# Unit test for function to_native
def test_to_native():
    assert to_native(b'foo') == b'foo'
    assert to_native(u'foo') == b'foo'
    assert to_native(1) == 1
    assert to_native(1.5) == 1.5
    # Note: None is used here to represent a no-op when combining encoders.  We want
    # to check that to_native is idempotent and not returning the same memory address
    # as the object that is passed in.
    assert to_native(None) is None
    # Make sure that we don't over-do it
    assert to_native('foo') == u'foo'
    assert to_native(u'foo') == u'foo'
    assert to_native(b'foo') == b'foo'
    assert to_native(1) == 1
    assert to_

# Generated at 2022-06-12 23:40:36.301163
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        return
    tb = to_bytes
    # We don't test that everything compiles because we want to use
    # obj.encode(encoding, errors) to avoid exception tracebacks.
    from ansible.module_utils._text import to_bytes as _to_bytes
    _to_bytes._to_bytes = to_bytes
    _to_bytes.test_all()



# Generated at 2022-06-12 23:40:47.432993
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'\u043f\u0440\u0438\u0432\u0456\u0442') == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82'
    assert to_bytes(u'\u043f\u0440\u0438\u0432\u0456\u0442', 'ascii', 'surrogate_or_replace') == b'????????'
    assert to_bytes(u'\u043f\u0440\u0438\u0432\u0456\u0442', 'ascii', 'replace') == b'????????'

# Generated at 2022-06-12 23:40:58.169568
# Unit test for function to_bytes
def test_to_bytes():

    assert b'abc' == to_bytes('abc')
    assert b'abc' == to_bytes(u'abc')
    assert b'123' == to_bytes(123)
    assert b'123' == to_bytes(123.0)
    assert b'<type dict>' == to_bytes({})
    assert b'\xe5\xe4\xf6' == to_bytes(u'\xe5\xe4\xf6')
    assert b'\xe5\xe4\xf6' == to_bytes(b'\xe5\xe4\xf6')
    assert b'\xe5\xe4\xf6' == to_bytes('\xe5\xe4\xf6', errors='surrogateescape')

# Generated at 2022-06-12 23:41:05.371374
# Unit test for function jsonify
def test_jsonify():

    assert jsonify({}) == "{}"
    assert jsonify({"k": 1}) == '{"k": 1}'
    assert jsonify({"k": 1}, sort_keys=True) == '{"k": 1}'
    assert jsonify({"k": 1}, sort_keys=True) == '{"k": 1}'
    assert jsonify({"k": 1}, sort_keys=True, indent=4) == "{\n    \"k\": 1\n}"
    assert jsonify({u"k": 1}) == '{"k": 1}'
    assert jsonify({u"k": 1}, sort_keys=True) == '{"k": 1}'
    assert jsonify({u"k": 1}, sort_keys=True) == '{"k": 1}'

# Generated at 2022-06-12 23:41:10.260353
# Unit test for function to_native
def test_to_native():
    assert to_native(b'abc') == 'abc'
    assert to_native('abc') == 'abc'
    assert to_native(u'abc') == 'abc'
    assert to_native(18) == '18'
    assert to_native(datetime.datetime(2014, 1, 14, 14, 18, 22)) == '2014-01-14 14:18:22.000000'

# Generated at 2022-06-12 23:41:13.237039
# Unit test for function jsonify
def test_jsonify():
    result = {'Content': u'\U0001d120'}
    assert json.loads(jsonify(result)) == {u'Content': u'\U0001d120'}
    assert json.loads(jsonify(u'\U0001d120')) == u'\U0001d120'



# Generated at 2022-06-12 23:41:34.082418
# Unit test for function jsonify
def test_jsonify():
    def _test(data, utf8_clean, latin1_clean):
        assert jsonify(data, ensure_ascii=False) == utf8_clean
        assert jsonify(data, ensure_ascii=True) == latin1_clean
        assert jsonify(data, ensure_ascii=False, encoding='utf-8') == utf8_clean
        assert jsonify(data, ensure_ascii=True, encoding='utf-8') == latin1_clean
        assert jsonify(data, ensure_ascii=False, encoding='latin-1') == utf8_clean
        assert jsonify(data, ensure_ascii=True, encoding='latin-1') == latin1_clean
    # test that utf-8 encoded json works (with ensure_ascii=True and

# Generated at 2022-06-12 23:41:35.702067
# Unit test for function jsonify
def test_jsonify():
    # jsonify is tested in the template module
    pass



# Generated at 2022-06-12 23:41:42.215424
# Unit test for function jsonify
def test_jsonify():
    d = {b'a': 1, 'b': u'c'}
    result = jsonify(d, sort_keys=True)
    assert result == '{"a": 1, "b": "c"}'
    # test with ansible_facts
    d = {'ansible_facts': {'b': u'c', b'a': 1}}
    result = jsonify(d, sort_keys=True)
    assert result == '{"ansible_facts": {"a": 1, "b": "c"}}'


# Generated at 2022-06-12 23:41:47.942774
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\u7f51\u7edc') == u'"\u7f51\u7edc"'
    assert jsonify(u'\u7f51\u7edc'.encode('utf-8')) == u'"\u7f51\u7edc"'
    assert jsonify(u'\u7f51\u7edc'.encode('latin-1')) == u'"\u7f51\u7edc"'
    assert jsonify(u'\u7f51\u7edc'.encode('utf-16')) == u'"\u7f51\u7edc"'
    assert jsonify(u'\u01ce') == u'"\u01ce"'
    assert jsonify([u'\u7f51\u7edc']) == u

# Generated at 2022-06-12 23:41:59.036885
# Unit test for function to_bytes
def test_to_bytes():
    # PY3 -  str -> bytestr, bytes -> bytestr
    assert to_bytes('asciistring') == b'asciistring'
    assert to_bytes('my ascii\xffstring') == b'my ascii\xffstring'
    assert to_bytes(u'my unicode\u1234string') == b'my unicode\xe1\x88\xb4string'

    # PY2 -  str -> bytestr, bytes -> bytestr, unicode -> bytestr
    # Using hexlify to compare because \xe1\x88\xb4 looks like three
    # separate characters above
    assert to_bytes('asciistring') == b'asciistring'
    assert to_bytes('my ascii\xffstring') == b'my ascii\xffstring'

# Generated at 2022-06-12 23:42:03.159620
# Unit test for function jsonify
def test_jsonify():
    assert jsonify([u'\u20ac']) == '["\xe2\x82\xac"]'
    assert jsonify('\xe2\x82\xac') == '"\\"\\\\xe2\\\\x82\\\\xac\\""'



# Generated at 2022-06-12 23:42:10.040788
# Unit test for function to_native
def test_to_native():
    assert to_native(1) is 1
    assert to_native(1.2) == 1.2
    assert to_native(u'foo') == u'foo'
    assert to_native(b'foo') == b'foo'
    assert to_native(u'\u2713') == u'\u2713'
    assert to_native(b'\xe2\x9c\x93') == u'\u2713'

# Generated at 2022-06-12 23:42:18.740352
# Unit test for function to_native
def test_to_native():
    def _test(value, expected):
        result = to_native(value)
        assert result == expected, 'Expected %s but got %s' % (expected, result)

    _test(True, 'True')
    _test(False, 'False')
    _test(42, '42')
    _test(42.00001, '42.00001')
    _test({'foo': 'bar'}, "{'foo': 'bar'}")
    _test(['foo'], "['foo']")
    _test(('foo',), "('foo',)")
    _test(set(['foo']), "set(['foo'])")

# Generated at 2022-06-12 23:42:23.326448
# Unit test for function jsonify
def test_jsonify():
    tests = (
        ({"a": "a"}, '{"a": "a"}'),
        ({"a": u"\xdd\xdd"}, '{"a": "\\udddd"}'),
        ({"a": u"\udddd"}, '{"a": "\\udddd"}'),
        )
    for i, o in tests:
        assert jsonify(i) == o



# Generated at 2022-06-12 23:42:25.197521
# Unit test for function jsonify
def test_jsonify():
    data = {u'field': u"f\u00f6\u00f6"}
    print(jsonify(data))



# Generated at 2022-06-12 23:42:42.188892
# Unit test for function jsonify
def test_jsonify():
    # test jsonify with valid utf-8 encoded data
    data =  {b'a': b'\xc3\xa4'}
    try:
        json_data = jsonify(data)
    except UnicodeDecodeError:
        assert False
    # test jsonify with invalid utf-8 encoded data
    data =  {b'a': b'\x81\x80'}
    try:
        json_data = jsonify(data)
        assert False
    except UnicodeDecodeError:
        pass
    # test jsonify(data, ensure_ascii=True)
    data =  {b'a': b'\xc3\xa4'}
    try:
        json_data = jsonify(data, ensure_ascii=True)
    except UnicodeDecodeError:
        assert False


# Generated at 2022-06-12 23:42:52.002328
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    from ansible.module_utils._text import to_text
    assert to_native(None) == 'None'
    assert to_native(True) == 'True'
    assert to_native(False) == 'False'
    assert to_native(123) == '123'
    assert to_native(123.123) == '123.123'
    assert to_native('test') == 'test'
    assert to_native(b'test') == 'test'
    assert to_native(u'test') == 'test'
    assert to_native(bytearray(b'test')) == 'test'
    assert to_native([u'test']) == '[u\'test\']'

# Generated at 2022-06-12 23:43:00.013996
# Unit test for function to_native

# Generated at 2022-06-12 23:43:10.798148
# Unit test for function to_native
def test_to_native():
    print("Running Test Case for function: to_native")
    assert to_native(u'foo') == u'foo'
    assert to_native(u'foo'.encode('utf-8')) == u'foo'
    assert to_native(u'\xe9') == u'\xe9'
    assert to_native(u'\xe9'.encode('utf-8')) == u'\xe9'
    assert to_native(u'\0') == u'\0'
    assert to_native(b'\0') == u'\0'
    assert to_native(b'\xe9') == u'\xe9'
    assert to_native(b'a\xe9') == u'a\xe9'
    assert not isinstance(to_native(u'foo'), bytes)

# Generated at 2022-06-12 23:43:11.781721
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\u2013') == '"\\u2013"'


# Generated at 2022-06-12 23:43:20.679426
# Unit test for function to_bytes
def test_to_bytes():
    def get_bytes(value):
        if isinstance(value, binary_type):
            return value
        if isinstance(value, text_type):
            return value.encode('utf-8')
        if isinstance(value, int):
            return str(value).encode('utf-8')
        if isinstance(value, float):
            return str(value).encode('utf-8')
        if isinstance(value, set):
            return str(value).encode('utf-8')
        if isinstance(value, datetime.datetime):
            return str(value).encode('utf-8')
        if isinstance(value, datetime.timedelta):
            return str(value).encode('utf-8')
        raise TypeError('Invalid type for bytes: %s' % type(value))

    strings

# Generated at 2022-06-12 23:43:28.949269
# Unit test for function jsonify
def test_jsonify():
    try:
        jsonify({'foo': u'\u2713'}, ensure_ascii=False)
    except UnicodeDecodeError:
        assert False, "test_jsonify didn't handle unicode properly."


if PY3:
    def boolean(arg):
        return arg.lower() not in ('no', 'false', '0', '', 'none')

else:
    def boolean(arg):
        return arg.lower() in ('yes', 'true', '1', 'on', 'y')



# Generated at 2022-06-12 23:43:30.060119
# Unit test for function jsonify
def test_jsonify():
    jsonify({"a":"b"})



# Generated at 2022-06-12 23:43:39.362748
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('abc') == b'abc'
    assert to_bytes(u'abc') == b'abc'
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(b'abc', errors='replace') == b'abc'
    assert to_bytes(u'\u2713', encoding='ascii') == b'?'
    assert to_bytes(u'\u2713', encoding='ascii', errors='replace') == b'?'
    assert to_bytes(u'\u2713', encoding='ascii', errors='surrogate_or_strict') == b'?'

    assert to_bytes(u'\u2713', encoding='ascii', errors='surrogate_or_replace') == b'?'

    # surrogate_then_replace is ignored on PY

# Generated at 2022-06-12 23:43:43.811193
# Unit test for function jsonify
def test_jsonify():
    test_dict = {'a': 'simple'}
    assert(jsonify(test_dict) == '{"a": "simple"}')
    test_dict = {'a': Set(['simple'])}
    assert(jsonify(test_dict) == '{"a": ["simple"]}')
    try:
        test_dict = {'a': {'b': 'simple'}}
        jsonify(test_dict)
        assert False, 'should have thrown exception'
    except TypeError:
        pass



# Generated at 2022-06-12 23:44:05.507498
# Unit test for function to_bytes
def test_to_bytes():
    to_bytes("test")
    if PY3:
        assert to_bytes("test", nonstring='strict')
    else:
        assert not to_bytes(u"test", nonstring='strict')
    assert not to_bytes("test", encoding='utf-8', errors='strict')
    assert not to_bytes("test", encoding='utf-16', errors='strict')
    assert not to_bytes("test", encoding='utf-8', errors='surrogate_or_strict')
    assert not to_bytes("test", encoding='utf-16', errors='surrogate_or_strict')
    assert not to_bytes("test", encoding='utf-8', errors='surrogate_or_replace')
    assert not to_bytes("test", encoding='utf-16', errors='surrogate_or_replace')

# Generated at 2022-06-12 23:44:07.345158
# Unit test for function to_bytes
def test_to_bytes():
    raise NotImplementedError()



# Generated at 2022-06-12 23:44:17.840851
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    default_text = to_native(b'foo')
    assert isinstance(default_text, text_type)
    assert default_text == u'foo'

    latin1_text = to_native(b'foo', encoding='latin-1')
    assert isinstance(latin1_text, text_type)
    assert latin1_text == u'foo'

    unicode_text = to_native(u'\u2713')
    assert isinstance(unicode_text, text_type)
    assert unicode_text == u'\u2713'

    default_bytes = to_native(u'foo', retain_bytes=True)
    assert isinstance(default_bytes, binary_type)
    assert default_bytes == b'foo'



# Generated at 2022-06-12 23:44:25.328326
# Unit test for function jsonify
def test_jsonify():
    data = [{'foo': ['bar', 'baz']},
            {'file': '/foo/bar/baz'},
            {'file_with_host': '/foo/bar/baz|magic'},
            {'file_with_host_and_delim': '/foo/bar/baz|magic:magic'},
            {'url': 'http://foo.bar/#baz'}, ]
    encoded_data = jsonify(data)
    # Verify that the encoded data is still valid json
    json.loads(encoded_data)



# Generated at 2022-06-12 23:44:32.010896
# Unit test for function to_native
def test_to_native():
    assert b'foo' == to_bytes('foo')
    assert u'bar' == to_text(b'bar')
    assert u'baz' == to_text('baz')
    assert b'qux' == to_bytes(u'qux')

# Generated at 2022-06-12 23:44:44.449142
# Unit test for function to_native
def test_to_native():
    assert to_native(b'foo', 'utf-8') == u'foo'

    # Some corner case tests for python2
    if not PY3:
        assert to_native(b'\xe9', 'ascii', 'strict') == u'\uFFFD'
        assert to_native(b'\xe9', 'ascii', 'surrogateescape') == u'\uFFFD'
        assert to_native(b'\xe9', 'ascii', 'surrogate_or_strict') == u'\uFFFD'
        assert to_native(b'\xe9', 'ascii', 'surrogate_or_replace') == u'\ufffd'
        assert to_native(b'\xe9', 'ascii', 'surrogate_then_replace') == u

# Generated at 2022-06-12 23:44:51.227355
# Unit test for function jsonify
def test_jsonify():
    # simple test
    data = {
        u'foo': u'bar',
    }
    try:
        jsonify(data)
    except UnicodeDecodeError:
        assert False, u'Failed to jsonify data'

    # test with non-ascii characters
    data = {
        u'foo': u'\xab',
    }
    try:
        jsonify(data)
    except UnicodeDecodeError:
        assert False, u'Failed to jsonify data'

    # test with non-ascii characters
    data = {
        u'foo': u'\xab',
        u'bar': [u'\xde\xad\xbe\xef', u'foo\xab']
    }

# Generated at 2022-06-12 23:45:00.337943
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({"a": "b\u0080", u"c": u"d\u0080"})
    assert json.loads(result) == {u"a": u"b\u0080", u"c": u"d\u0080"}

    result = jsonify({"a": "b\u0080", u"c": u"d\u0080", "e": {"f": "g"}})
    assert json.loads(result) == {u"a": u"b\u0080", u"c": u"d\u0080", u"e": {u"f": u"g"}}

    result = jsonify({"a": "b\u0080", u"c": u"d\u0080", "e": {"f": "g"}}, sort_keys=True)


# Generated at 2022-06-12 23:45:09.414978
# Unit test for function to_bytes
def test_to_bytes():
    """Testing function - to_bytes
    """
    assert to_bytes(True) == b'true'
    assert to_bytes(False) == b'false'
    assert to_bytes(2) == b'2'
    assert to_bytes(2.2) == b'2.2'
    assert to_bytes(to_text(b'\xff', 'iso-8859-1')) == b'\xff'
    assert to_bytes(u'\uffff') == b'\xef\xbf\xbf'
    assert to_bytes(u'\uffff', nonstring='strict') == b'\xef\xbf\xbf'
    assert to_bytes(u'\uffff', nonstring='empty') == b''

    # Check that we can handle non-string obj types

# Generated at 2022-06-12 23:45:11.599440
# Unit test for function jsonify
def test_jsonify():
    json_data = jsonify({"key": "\u6211\u662f"})
    assert json_data == '{"key": "\\u6211\\u662f"}'



# Generated at 2022-06-12 23:45:23.810872
# Unit test for function jsonify
def test_jsonify():
    data = {'foo': 'bar', 'spam': b'egg'}
    assert jsonify(data) == '{"spam": "egg", "foo": "bar"}'



# Generated at 2022-06-12 23:45:34.386985
# Unit test for function to_bytes
def test_to_bytes():
    # Empty strings
    assert b'{}' == to_bytes('')
    assert b'{}' == to_bytes(u'')
    assert b'{}' == to_bytes(b'', nonstring='passthru')
    assert b'{}' == to_bytes(u'', nonstring='passthru')

    # Non-strings
    assert b'1' == to_bytes(1)
    assert b'1' == to_bytes(1, nonstring='passthru')
    assert b'{}' == to_bytes(1, nonstring='empty')
    if not PY3:
        assert b'<type \'int\'>' == to_bytes(1, encoding='ascii', errors='replace')

# Generated at 2022-06-12 23:45:42.549315
# Unit test for function jsonify
def test_jsonify():
    data = {
        'ascii': 'abc123',
        'unicode_str': u'this is a unicode \u2019 string',
        'unicode_str_as_str': 'this is a unicode \xe2\x80\x99 string',
        'byte_str': b'decoded \xe2\x80\x99 this is a unicode string',
        'byte_str_as_str': 'decoded \xe2\x80\x99 this is a unicode string',
        'obj': {
            'key': u'unicode value'
        }
    }

# Generated at 2022-06-12 23:45:52.262451
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=b'foo', b=u'b\u1234r')) == '{"a": "foo", "b": "b\xe1\x88\xb4r"}'
    assert jsonify(dict(a=[b'foo', u'bar'], b=1)) == '{"a": ["foo", "bar"], "b": 1}'
    assert jsonify(dict(a=[b'foo', [u'f\u1234o', [u'bar']]], b=1)) == '{"a": ["foo", ["f\xe1\x88\xb4o", ["bar"]]], "b": 1}'



# Generated at 2022-06-12 23:45:58.141022
# Unit test for function jsonify
def test_jsonify():
    # Setup
    data = { 'key': 'value', 'list': [1, 2, 3, 'a', 'b', 'c'], 'set': set([1, 2, 3]) }
    output = jsonify(data)

    # Verify
    assert output == '{"key": "value", "list": [1, 2, 3, "a", "b", "c"], "set": [1, 2, 3]}'


# Generated at 2022-06-12 23:46:09.989786
# Unit test for function to_native
def test_to_native():
    # Verify that nonascii unicode strings decode to ascii strings
    # We don't care about fancy casing here.  The important thing is that we get
    # out the same string that we put in
    assert to_native(u'\u00e9\u20ac\u0121') == u'\u00e9\u20ac\u0121'

    # Verify that we can take a binary string and encode with an encoding that
    # will produce a nonascii unicode string and get the correct unicode
    # string as a result
    assert to_native(b'\xc3\xa9\xe2\x82\xac\xc4\xa1', encoding='utf-8') == u'\u00e9\u20ac\u0121'

    # Verify that we can put in a nonascii

# Generated at 2022-06-12 23:46:10.571638
# Unit test for function to_bytes
def test_to_bytes():
    pass



# Generated at 2022-06-12 23:46:14.347998
# Unit test for function to_native
def test_to_native():

    assert to_native(1) == '1'

    # these don't work on 2.6
    if PY3 or sys.version_info[1] > 6:
        assert to_native(b'1') == u'1'
        assert to_native(u'1') == u'1'



# Generated at 2022-06-12 23:46:25.778298
# Unit test for function to_native
def test_to_native():
    """
    Test to_native
    """
    # TODO: Remove when to_native is no longer present
    from ansible.module_utils._text import to_native
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text

    # Test NULL bytes
    assert to_native(b"\x00") == "\x00"

    # Test non-string input
    assert to_native(100) == "100"
    assert to_native(None) == "None"
    assert to_native([1, 2, 3]) == "[1, 2, 3]"
    assert to_native({"foo": "bar"}) == "{u'foo': u'bar'}"
    assert to_native(u'\u00e9') == u'\u00e9'

# Generated at 2022-06-12 23:46:26.371745
# Unit test for function to_bytes
def test_to_bytes():
    pass



# Generated at 2022-06-12 23:46:56.102742
# Unit test for function to_native
def test_to_native():
    assert to_native(u"unicode") == u"unicode"
    assert to_native(u"unicode".encode("utf-8")) == u"unicode"

    # Test with custom text encoding
    assert to_native(u"unicode".encode("utf-16"), encoding="utf-16") == \
        "unicode"

    # Test with bytes that are not valid in the specified encoding
    # Output will be the repr of the bytes as a text string
    assert to_native(u"unicode".encode("utf-16"), encoding="utf-8") == \
        "b'\\xff\\xfeu\\x00n\\x00i\\x00c\\x00o\\x00d\\x00e\\x00'"



# Generated at 2022-06-12 23:47:06.735552
# Unit test for function jsonify
def test_jsonify():
    """
    Test function jsonify

    :return: Nothing
    """
    data_dict = {}
    data_dict['foo'] = 'bar'
    data_dict['boo'] = u'baz'
    data_dict['moo'] = 1
    data_dict['zoo'] = [1,2,3,4,5]
    data_dict['poo'] = {u'a':1, u'b':2 , u'c':3}
    data_dict['soo'] = Set([1,2,3,4,5,6,7,8,9,10])
    data_dict['doo'] = datetime.datetime.now()

# Generated at 2022-06-12 23:47:14.601425
# Unit test for function to_native
def test_to_native():
    assert to_native(u'text') == u'text'
    assert to_native('bytestring', errors='surrogate_or_replace') == 'bytestring'
    assert to_native(True) is True
    assert to_native(False) is False
    assert to_native(u'text', nonstring='empty') == u''
    assert to_native('bytestring', errors='surrogate_or_replace', nonstring='empty') == ''
    assert to_native(True, nonstring='empty') == ''
    assert to_native(False, nonstring='empty') == ''
    assert to_native(12345) == u'12345'
    assert to_native(set([u'foo', u'bar'])) == u'bar'

# Generated at 2022-06-12 23:47:25.351782
# Unit test for function to_bytes
def test_to_bytes():
    # We have different code paths for 2.4 so we have to test 2.4 separately
    if (2, 4) <= sys.version_info < (2, 5):
        expected = b'This is a unicode string'
        given = u'This is a unicode string'
        assert(to_bytes(given) == expected)

        expected = b'This is a non-unicode string'
        given = 'This is a non-unicode string'
        assert(to_bytes(given) == expected)

        expected = b''
        given = None
        assert(to_bytes(given, nonstring='empty') == expected)

        expected = None
        given = None
        assert(to_bytes(given, nonstring='passthru') == expected)

        expected = b''
        given = None

# Generated at 2022-06-12 23:47:34.913660
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'foobar') == b'foobar'
    assert to_bytes(b'foobar') == b'foobar'
    assert to_bytes(u'foobar', 'latin-1') == b'foobar'
    assert to_bytes(u'\u2665') == b'\xe2\x99\xa5'
    assert to_bytes(u'\u2665', 'latin-1') == b'?'
    assert to_bytes(u'\u2665', 'latin-1', 'replace') == b'?'
    assert to_bytes(u'\u2665', 'ascii', 'replace') == b'?'
    assert to_bytes(u'z\u2665', 'ascii') == b'z?'

# Generated at 2022-06-12 23:47:43.602784
# Unit test for function to_bytes
def test_to_bytes():
    # Make sure we can transform every possible character into a byte string
    # with utf-8
    for i in range(0x110000):
        c = unichr(i)
        to_bytes(c)

    # Check that surrogate_then_replace handles things properly
    not_utf8 = u'\u6c49\u5b57\U0001d6db'
    retval = to_bytes(not_utf8, 'latin-1')
    assert retval == b'\xe6\x92\x99\xe5\xad\x97\xef\xb8\xbb\xef\xb8\xbb'

    # Check that surrogate_or_strict and surrogate_or_replace differ
    # in python2

# Generated at 2022-06-12 23:47:49.879395
# Unit test for function to_bytes

# Generated at 2022-06-12 23:48:01.532315
# Unit test for function jsonify

# Generated at 2022-06-12 23:48:09.230475
# Unit test for function to_native
def test_to_native():
    # NOTE: We should try to use a codec that has multiple bytes per character
    # but that's not available on all Python versions
    encoded_string = b'\xc3\xb1\xc3\x91'
    assert to_bytes(encoded_string, 'iso-8859-1') == encoded_string
    assert to_bytes(encoded_string, 'utf-8') == encoded_string.decode('utf-8').encode('utf-8')

    # Test input is a text string

    # utf-8 to utf-8
    assert to_bytes('ñÑ', 'utf-8') == b'\xc3\xb1\xc3\x91'
    # iso-8859-1 to utf-8
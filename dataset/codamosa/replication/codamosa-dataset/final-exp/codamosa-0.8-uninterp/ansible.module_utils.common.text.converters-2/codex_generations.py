

# Generated at 2022-06-12 23:38:25.401669
# Unit test for function jsonify
def test_jsonify():
    data = {
        1: u'foo',
        2: u'bar',
        3: [u'foo', u'bar'],
        4: {u'foo': u'bar', u'bar': u'baz'},
        5: Set([u'foo', u'bar']),
        6: datetime.datetime(1955, 11, 5),
        7: datetime.datetime(1960, 3, 2, 10, 2, tzinfo=datetime.timezone.utc),
    }

# Generated at 2022-06-12 23:38:36.493085
# Unit test for function to_bytes
def test_to_bytes():
    from random import randint

    # Using surrogates
    # avoid using django.utils.encoding.force_text to prevent cross-contamination

# Generated at 2022-06-12 23:38:46.028225
# Unit test for function to_native
def test_to_native():
    """Test that the to_native function works as expected
    """
    assert to_native(b'bytes', 'utf-8') == u'bytes'
    assert to_native(b'bytes', 'latin-1') == u'bytes'
    assert to_native(u'unicode') == u'unicode'
    assert to_native(b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e', 'euc-jp') == u'\u65e5\u672c\u8a9e'



# Generated at 2022-06-12 23:38:54.339229
# Unit test for function to_bytes
def test_to_bytes():
    def test_error_handler(handlers, expected):
        if handlers == 'surrogate_then_replace':
            return to_bytes(u"\udc80\udc80", errors=handlers)
        for handler in handlers:
            for i in range(3):
                text = u"\udc80" * i
                result = to_bytes(text, errors=handler)
                if handler == 'surrogate_or_strict':
                    handler = 'strict'
                elif handler == 'surrogate_or_replace':
                    handler = 'replace'
                assert result == (text.encode('utf-8', handler) if not i else b'')
                assert isinstance(result, binary_type)
        assert to_bytes(u"\udc80\udc80", errors=handlers) == expected

# Generated at 2022-06-12 23:38:57.243290
# Unit test for function jsonify
def test_jsonify():
    import pytest
    obj = Set([1,2,3])
    obj1 = {"a":"b"}
    obj2 = u"abc"
    assert jsonify(obj) == "[1, 2, 3]"
    assert jsonify(obj1) == '{"a": "b"}'
    assert jsonify(obj2) == '"abc"'
    pytest.raises(Exception, jsonify, obj, encoding='utf-8')


# Generated at 2022-06-12 23:39:07.633589
# Unit test for function to_native
def test_to_native():

    class Test_Object:
        def __init__(self, obj):
            self.obj = obj

        def __str__(self):
            if self.obj == 'pass_obj':
                return self.obj
            else:
                raise UnicodeError

        def __repr__(self):
            if self.obj == 'simplerepr':
                return self.obj
            else:
                raise UnicodeError

    assert to_native(u'\u2713') == u'\u2713'
    assert to_native(u'\u2713'.encode('utf-8'), errors='surrogateescape') == u'\u2713'
    assert to_native(u'\u2713'.encode('ascii', 'replace'), errors='surrogateescape') == u'\ufffd'
    assert to_native

# Generated at 2022-06-12 23:39:14.164518
# Unit test for function jsonify
def test_jsonify():
    assert jsonify("abc") == '"abc"'
    assert jsonify(b"\xc3\x9c") == '"\\u00dc"'
    assert jsonify(b"\xe2\x82\xac") == '"\\u20ac"'
    assert jsonify(["a", b"\xc3\x9c", b"\xe2\x82\xac", "b"]) == '["a", "\\u00dc", "\\u20ac", "b"]'
    assert jsonify(["a", b"\xe2\x82\xac", b"\xc3\x9c", "b"]) == '["a", "\\u20ac", "\\u00dc", "b"]'

# Generated at 2022-06-12 23:39:24.522821
# Unit test for function to_bytes
def test_to_bytes():
    # Test that we convert unicode to the correct encoding
    when = datetime.datetime.now()
    isoformat = when.isoformat()
    utf8_expect = to_bytes(isoformat, 'utf-8')
    ascii_expect = to_bytes(isoformat, 'ascii')
    utf8_got = to_bytes(when, 'utf-8', 'surrogate_then_replace')
    ascii_got = to_bytes(when, 'ascii', 'surrogate_then_replace')

    try:
        assert utf8_expect == utf8_got
    except AssertionError as e:
        raise AssertionError('%s: %s != %s' % (when, utf8_expect, utf8_got))


# Generated at 2022-06-12 23:39:32.284499
# Unit test for function to_bytes
def test_to_bytes():
    # These tests are located in the to_bytes() unit test file because the
    # to_bytes() logic is required to test to_text()

    # FIXME: Write tests for these functions.
    #
    # FIXME: Test the various encoding and errors combinations.
    # FIXME: Test that surrogate then replace and surrogate or replace work
    #
    # FIXME: Test that to_text and to_bytes with the surrogate_or_strict and
    # surrogate_or_replace error handlers works on python3 and test that it
    # works on python2 if codecs.lookup_error('surrogateescape') has been
    # called.

    #
    #
    pass



# Generated at 2022-06-12 23:39:41.453459
# Unit test for function to_native
def test_to_native():
    # Test function with non-string parameter nonstring='simplerepr'
    assert to_native(123.45) == '123.45'
    assert to_native(dict([('key', 'value')])) == "{'key': 'value'}"

    # Test function with non-string parameter nonstring='passthru'
    assert to_native(123.45, nonstring='passthru') == 123.45
    assert to_native(dict([('key', 'value')]), nonstring='passthru') == dict([('key', 'value')])

    # Test function with non-string parameter nonstring='empty'
    assert to_native(123.45, nonstring='empty') == ''
    assert to_native(dict([('key', 'value')]), nonstring='empty') == ''

    # Test function with non-string parameter nonstring

# Generated at 2022-06-12 23:39:50.321402
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(argument_spec=dict(string=dict(type='str')))

    m.exit_json(string=m.params['string'])

# Generated at 2022-06-12 23:39:58.542973
# Unit test for function to_bytes
def test_to_bytes():
    def cmp_func(val, exp):
        got = to_bytes(val)
        assert got == exp, (val, exp, got)


# Generated at 2022-06-12 23:40:03.063374
# Unit test for function jsonify
def test_jsonify():
    data = {'a': {'b': 'this is a string'}, 'c': ['a', 'b'], 'd': 'this is another string'}
    assert(jsonify(data)) == '{"a": {"b": "this is a string"}, "c": ["a", "b"], "d": "this is another string"}'

# Generated at 2022-06-12 23:40:08.646020
# Unit test for function to_native
def test_to_native():
    tests = [
        # idx, input_obj, expected output
        (1, u'abc', u'abc'),
        (2, b'abc', u'abc'),
        (3, {u'abc': u'def'}, u"{u'abc': u'def'}"),
        (4, {u'abc': b'def'}, u"{u'abc': u'def'}"),
    ]
    for (idx, inp, expected_out) in tests:
        if PY3:
            assert to_native(inp) == expected_out
        else:
            assert to_native(inp) == to_bytes(expected_out)



# Generated at 2022-06-12 23:40:19.722890
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils._text import to_bytes
    assert to_bytes(u'\u043f\u0440\u0438\u0432\u0435\u0442') == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
    assert to_bytes(b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82') == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# Generated at 2022-06-12 23:40:27.905116
# Unit test for function to_bytes
def test_to_bytes():
    def check_nonstring(value, nonstring, expected_type=binary_type):
        actual = to_bytes(value, nonstring=nonstring)

        assert isinstance(actual, expected_type)

    for null in (b'', u'', u'\ufffd'):
        assert to_bytes(null) == b''

    # Verify that we're doing type checking against the type of the value and
    # not what's stored in the variable
    assert to_bytes(u'', nonstring='empty') == b''
    assert to_bytes(u'', nonstring='passthru') is u''
    check_nonstring(u'', 'strict', TypeError)

    # Test that we tolerate the unicode to string coercion

# Generated at 2022-06-12 23:40:39.175802
# Unit test for function to_bytes
def test_to_bytes():
    import unittest

    class ToBytesTestCase(unittest.TestCase):
        def assertUnicode(self, value):
            self.assertTrue(isinstance(value, text_type), '%s is not unicode' % value)

        def assertBytes(self, value):
            self.assertTrue(isinstance(value, binary_type))


        def test_to_bytes_text(self):
            self.assertEqual(to_bytes(u'\u1234\u5678abcd'),
                    u'\u1234\u5678abcd'.encode('utf-8'))

# Generated at 2022-06-12 23:40:42.189245
# Unit test for function to_native
def test_to_native():
    '''
    Test the module's to_native function
    '''
    # Case 1
    assert to_native('hello') is 'hello'



# Generated at 2022-06-12 23:40:49.504818
# Unit test for function jsonify
def test_jsonify():
    # Test for valid input
    my_data = dict(foo="bar", frog=[1, 2, 3, 4])
    assert jsonify(my_data) == '{"foo": "bar", "frog": [1, 2, 3, 4]}'
    # Test for invalid input
    my_data = dict(foo=u"\u4e00")
    raised = False
    try:
        jsonify(my_data)
    except UnicodeError:
        raised = True
    assert raised is True

# Test for function jsonify_unsafe

# Generated at 2022-06-12 23:41:00.161623
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('abc') == b'abc'
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(b'abc', nonstring='passthru') == b'abc'
    assert to_bytes(b'abc', nonstring='simplerepr') == b'abc'
    assert to_bytes(b'abc', nonstring='empty') == b''
    assert to_bytes(u'This is a unicode string') == b'This is a unicode string'
    # utf-16 encoding
    assert hasattr(u'\u05d0', 'encode')
    assert to_bytes(u'\u05d0'.encode('utf-16')) == b'\xff\xfe\xd0\x05'
    # utf-32 encoding

# Generated at 2022-06-12 23:41:13.288321
# Unit test for function jsonify
def test_jsonify():
    json_object = {
        u'foo': u'bar',
        u'baz': (b'hello', 123),
        b'unicode': u'oh noes!'
    }
    json_data = jsonify(json_object)
    assert isinstance(json_data, text_type)
    assert jsonify(json_object, ensure_ascii=False) == u'{"baz": ["hello", 123], "foo": "bar", "unicode": "oh noes!"}'
    assert jsonify(json_object, sort_keys=True) == u'{"baz": ["hello", 123], "foo": "bar", "unicode": "oh noes!"}'


# Generated at 2022-06-12 23:41:19.076843
# Unit test for function to_native
def test_to_native():
    expected_native_value = u'bar'
    expected_native_type = unicode
    native_value = to_native("bar", encoding=u'ascii')
    assert native_value == expected_native_value
    assert isinstance(native_value, expected_native_type)

    expected_native_type = bytes
    expected_native_value = b'bar'
    native_value = to_native("bar", encoding=u'ascii', nonstring='passthru')
    assert native_value == expected_native_value
    assert isinstance(native_value, expected_native_type)

    expected_native_type = unicode
    expected_native_value = u'bar'
    native_value = to_native("bar", encoding=u'ascii', nonstring='strict')
    assert native_value

# Generated at 2022-06-12 23:41:29.328481
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'This is an ascii bytestring') == b'This is an ascii bytestring'
    assert to_bytes(u'This is a unicode string') == b'This is a unicode string'
    assert to_bytes(u'This is a unicode string', errors='replace') == b'This is a unicode string'
    assert to_bytes(u'This is a unicode string', errors='surrogate_or_replace') == b'This is a unicode string'
    assert to_bytes(u'This is a unicode string', errors='surrogate_or_strict') == b'This is a unicode string'
    assert to_bytes(u'This is a unicode string', errors='surrogate_then_replace') == b'This is a unicode string'

# Generated at 2022-06-12 23:41:40.097138
# Unit test for function to_native
def test_to_native():
    assert to_native('foo') == 'foo'
    assert to_native(True) is True
    assert to_native(25) == 25
    assert to_native(25, nonstring='passthru') == 25
    assert to_native(25, nonstring='strict') == '25'
    assert to_native(u'\xed\xa0\x80') == u'\uD800'
    assert to_native(u'\xed\xa0\x80', nonstring='passthru') == u'\uD800'
    try:
        to_native(u'\xed\xa0\x80', nonstring='strict')
        assert False, 'should fail on strict for non-string'
    except TypeError:
        pass

# Generated at 2022-06-12 23:41:42.399210
# Unit test for function to_native
def test_to_native():
    assert to_native(u"\u2713") == u"\u2713"
    assert to_native(b"\xe2\x9c\x93") == u"\u2713"



# Generated at 2022-06-12 23:41:54.957829
# Unit test for function jsonify
def test_jsonify():
    assert to_text(jsonify(dict(name=u'foo', age=5, alive=True))) == b'{"age": 5, "name": "foo", "alive": true}'
    assert to_text(jsonify(dict(name=u'foo\xe9bar', age=5, alive=True))) == b'{"age": 5, "name": "foo\\xe9bar", "alive": true}'
    assert to_text(jsonify(dict(name=u'foo\xe9bar', age=5, alive=True), sort_keys=True)) == b'{"age": 5, "alive": true, "name": "foo\\xe9bar"}'
    assert to_text(jsonify([u'foo\xe9bar', 5, True])) == b'["foo\\xe9bar", 5, true]'

# Generated at 2022-06-12 23:42:03.680785
# Unit test for function jsonify
def test_jsonify():
    assert '"foo"' == jsonify('foo')
    assert '["foo"]' == jsonify(['foo'])
    assert '{"foo":42}' == jsonify({'foo': 42})
    assert '{"foo":"\u4e01\u4e02\u4e03"}' == jsonify({'foo': u'\u4e01\u4e02\u4e03'})
    assert '["\u4e01\u4e02\u4e03"]' == jsonify([u'\u4e01\u4e02\u4e03'])
    assert '{"foo":0,"bar":1,"baz":2}' == jsonify({'foo': 0, 'bar': 1, 'baz': 2})

# Generated at 2022-06-12 23:42:13.225812
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('hi') == b'hi'
    assert to_bytes(u'hi') == b'hi'
    assert to_bytes(u'h\xed') == b'h\xc3\xad'
    assert to_bytes(u'hí', encoding='latin-1') == b'h\xed'
    assert to_bytes(b'hi') == b'hi'
    assert to_bytes(1) == b'1'
    assert to_bytes(None) == b''
    assert to_bytes(b'h\xc3\xad'.decode('utf-8', 'surrogateescape'), encoding='latin-1') == b'h\xc3\xad'

# Generated at 2022-06-12 23:42:20.801721
# Unit test for function jsonify
def test_jsonify():
    data = {u'key': u'\u0080'}
    assert jsonify(data) == '{"key": "\\u0080"}'
    data = {u'key': u'\u0081'}
    assert jsonify(data) == '{"key": "\\u0081"}'
    data = {u'key': u'\u00ff'}
    assert jsonify(data) == '{"key": "\\u00ff"}'
    data = {u'key': u'\u0100'}
    assert jsonify(data) == '{"key": "\\u0100"}'
    data = {u'key': u'\uffff'}
    try:
        assert jsonify(data) == '{"key": "\\ufffd"}'
    except UnicodeDecodeError:
        pass



# Generated at 2022-06-12 23:42:27.484640
# Unit test for function jsonify
def test_jsonify():
    # Test that valid encode charset will pass
    data = b'{"foo": "\xe2\x99\xa5"}'
    assert data == jsonify(data, encoding='utf-8')

    # Test that invalid charset will raise
    data = b'{"foo": "\xff"}'
    try:
        jsonify(data, encoding='utf-8')
    except UnicodeDecodeError:
        assert True
    else:
        assert False

    # Test that setting default encoding will pass
    data = b'{"foo": "\xe2\x99\xa5"}'
    assert data == jsonify(data)

    # Test that fallback encoding will pass
    data = b'{"foo": "\xe2\x99\xa5"}'
    assert data == jsonify(data, encoding='ascii')


# Compatibility functions so that

# Generated at 2022-06-12 23:42:48.707319
# Unit test for function jsonify
def test_jsonify():
    jsonify_data = {"key1":"value1", "key2":"value2","key3":"value3"}
    jsonify_result = jsonify(jsonify_data)
    assert isinstance(jsonify_result, str)
    json_data = json.loads(jsonify_result)
    assert isinstance(json_data, dict)
    assert len(json_data) == 3
    for key, value in iteritems(json_data):
        assert key in ("key1","key2","key3")
        assert value in ("value1","value2","value3")



# Generated at 2022-06-12 23:42:57.882068
# Unit test for function to_native
def test_to_native():
    class A(object):
        def __str__(self):
            return u'K'
        def __repr__(self):
            return u'K'

    assert to_native(u'\u2113') == '\u2113'
    assert to_native(b'\xe2\x84\x93', encoding='ascii') == '\u2113'
    assert to_native(A()) == '\u2113'
    assert to_native(A(), errors='surrogate_then_replace') == '\ufffd\ufffd'
    # Test nonstring passthru
    assert to_native(A(), nonstring='passthru') == A()
    assert to_native(A(), nonstring='empty') == ''
    assert to_native(A(), nonstring='strict')

# Generated at 2022-06-12 23:43:08.554168
# Unit test for function to_bytes
def test_to_bytes():
    # pylint: disable=too-many-branches,too-many-statements,too-many-return-statements
    from ansible.module_utils.six import u

    # Test surrogate_then_replace error handler (the default)
    result = to_bytes(u('\udcff'))
    expected = b'?'
    assert result == expected, 'to_bytes failed on surrogate_then_replace with basic unicode character: got %s' % result

    result = to_bytes(u('\udcff'), encoding='shift_jis')
    expected = b'?'
    assert result == expected, 'to_bytes failed on surrogate_then_replace with unicode character and encoding: got %s' % result

    result = to_bytes(u('\udcff'), errors='surrogate_then_replace')
    expected

# Generated at 2022-06-12 23:43:18.819483
# Unit test for function to_native
def test_to_native():
    # Test default values
    assert to_native(u'foo') == 'foo'
    assert to_native(b'foo') == 'foo'
    assert to_native(b'foo', errors='surrogate_or_strict') == 'foo'
    assert to_native(b'foo', errors='surrogate_or_replace') == 'foo'
    assert to_native(b'foo', errors='surrogate_then_replace') == 'foo'
    assert to_native(b'foo', errors='surrogate_or_strict', nonstring='strict') == 'foo'
    assert to_native(b'foo', errors='surrogate_or_replace', nonstring='strict') == 'foo'

# Generated at 2022-06-12 23:43:24.716022
# Unit test for function to_native
def test_to_native():
    # FIXME: Add tests to ensure that the "other" types are going through to_text and to_bytes
    # First, test that we use surrogateescape when surrogateescape exists.
    if HAS_SURROGATEESCAPE:
        # surrogateescape tests -- surrogateescape should be available to us
        # unicode surrogate
        # u"\udcff".encode("utf-8", "ignore")
        b = b'\xed\xb3\xbf'
        assert codecs.decode(b, 'utf-8', 'surrogateescape') == u'\udcff'
        assert to_text(b, errors='surrogateescape') == u'\udcff'
        assert to_text(b, errors='surrogate_or_replace') == u'\udcff'

# Generated at 2022-06-12 23:43:35.559600
# Unit test for function to_bytes
def test_to_bytes():
    """Unit test for :py:func:`to_bytes`."""
    assert to_bytes(1.0) == b'1.0'
    assert to_bytes(u'test') == b'test'
    assert to_bytes(u'test', encoding='latin-1') == b'test'
    assert to_bytes(u't&st') == b't&st'
    assert to_bytes(u'\u00a2', encoding='latin-1') == b'\xa2'
    assert to_bytes(u'\u00a2', encoding='utf-8') == b'\xc2\xa2'
    assert to_bytes(u'\u00a2', encoding='ascii', errors='surrogate_or_strict') == b'\xc2\xa2'
    assert to_

# Generated at 2022-06-12 23:43:47.356500
# Unit test for function to_bytes
def test_to_bytes():
    from six import unichr
    from ansible.module_utils.six import MAXSIZE
    from ansible.module_utils.six.moves import xrange

    for obj in ('a', u'a'):
        assert isinstance(to_bytes(obj), binary_type)
        assert to_bytes(obj, nonstring='strict') == b'a'
        assert to_bytes(obj, nonstring='passthru') == 'a'
        assert to_bytes(obj, nonstring='empty') == b''
        assert to_bytes(obj, nonstring='simplerepr') == b'a'
        assert to_bytes(obj, errors='strict') == b'a'
        assert to_bytes(obj, encoding='utf-16') == b'\xff\xfea\x00'

# Generated at 2022-06-12 23:43:52.553276
# Unit test for function jsonify
def test_jsonify():
    test_term = u'\x17Test\x17'
    test_json_term = u'"\\u0017Test\\u0017"'

    if test_json_term != json.dumps(test_term):
        raise AssertionError('test_json_term fail')

    if jsonify(test_term) != json.dumps(test_term):
        raise AssertionError('jsonify is not equal to json.dumps')



# Generated at 2022-06-12 23:43:55.888024
# Unit test for function jsonify
def test_jsonify():
    data = {b'test1': 1, b'test2': b'abc'}
    assert jsonify(data) == '{"test1": 1, "test2": "abc"}'

    data = {u'test1': 1, u'test2': u'abc'}
    assert jsonify(data) == '{"test1": 1, "test2": "abc"}'



# Generated at 2022-06-12 23:44:07.355398
# Unit test for function to_bytes
def test_to_bytes():
    try:
        codecs.lookup_error('surrogate_or_replace')
    except LookupError:
        pass
    try:
        codecs.lookup_error('surrogate_then_replace')
    except LookupError:
        pass
    try:
        codecs.lookup_error('surrogate_or_strict')
    except LookupError:
        pass

    assert u'Dive in'.encode('ascii') == to_bytes(u'Dive in')
    assert u'Dive in'.encode('ascii') == to_bytes(u'Dive in'.encode('utf-8').decode('utf-8'))
    # This doesn't raise on linux but does on OSX
    #assert u'Dive in'.encode('ascii') == to_

# Generated at 2022-06-12 23:44:28.151055
# Unit test for function to_native
def test_to_native():
    # Test the basic function first
    class Test(object):
        to_text_returns_text = True

        def __str__(self):
            return u'This is a test'
    assert to_text(Test()) == u'This is a test'

    # Test that we can force the function to return a byte string instead of a text
    # string
    class Test(object):
        to_text_returns_text = False

        def __str__(self):
            return u'This is a test'
    assert to_text(Test()) == 'This is a test'

    # Test that we can force the function to return a byte string instead of a text
    # string with a surrogate in it
    class Test(object):
        to_text_returns_text = False

        def __str__(self):
            return u

# Generated at 2022-06-12 23:44:33.179069
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'\xff') == b'\xff'
    assert to_bytes(u'\u1234') == u'\u1234'.encode('utf-8')
    assert to_bytes(u'\u1234'.encode('latin-1')) == u'\u1234'.encode('latin-1')
    assert to_bytes(u'\u1234'.encode('utf-8')) == u'\u1234'.encode('utf-8')
    assert to_bytes(datetime.datetime.now(), nonstring='empty') == b''



# Generated at 2022-06-12 23:44:45.174616
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({u'foo' : u'bar'}) == '{"foo": "bar"}'
    assert jsonify({u'foo' : u'bar'}, sort_keys=True) == '{"foo": "bar"}'
    assert jsonify({u'foo' : [u'bar', u'baz']}, sort_keys=True) == '{"foo": ["bar", "baz"]}'
    assert jsonify({u'foo' : [u'bar', u'baz']}) == '{"foo": ["bar", "baz"]}'
    assert jsonify({u'foo' : [u'bar', u'baz', 2]}) == '{"foo": ["bar", "baz", 2]}'

# Generated at 2022-06-12 23:44:49.099120
# Unit test for function jsonify
def test_jsonify():
    data = {'a': {'b': 'c'}}
    result = jsonify(data)
    assert result.encode('utf-8') == json.dumps(data).encode('utf-8')



# Generated at 2022-06-12 23:44:59.377266
# Unit test for function to_bytes
def test_to_bytes():
    # Because we're only checking that a standard text string can be turned
    # into a byte string, we can use the simplest tests, the unit tests for
    # to_unicode will test the more complicated non-string options

    # Correct transformations
    assert to_bytes('hello') == b'hello'
    assert to_bytes('κόσμε') == b'\xce\xba\xe1\xbd\xb9\xcf\x83\xce\xbc\xce\xb5'
    assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    assert to_bytes(u'\ud800') == b'\xed\xa0\x80'
    assert to_bytes(b'\xc3\xae') == b'\xc3\xae'

# Generated at 2022-06-12 23:45:08.627824
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        # Basic check for surrogateescape
        assert to_bytes('ascii', 'ascii', 'surrogateescape') == b'ascii'
        assert to_bytes('\ud7ff', 'ascii', 'surrogateescape') == b'\xed\x9f\xbf'

    # Basic check for surrogate_then_replace
    assert to_bytes('\ud7ff', 'ascii', 'surrogate_then_replace') == b'?'

    # Basic check for surrogate_or_replace
    assert to_bytes('\ud7ff', 'ascii', 'surrogate_or_replace') == b'?'

    # Basic check for surrogate_or_strict

# Generated at 2022-06-12 23:45:16.850523
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'{"foo": "bar"}') == u'{"foo": "bar"}'
    assert jsonify(b'{"foo": "bar"}') == u'{"foo": "bar"}'
    assert jsonify(u'{"fôō": "bar"}') == u'{"fôō": "bar"}'
    assert jsonify(b'{"f\xc3\xb4\xc3\xb2": "bar"}') == u'{"fôō": "bar"}'

    obj = dict(a=u'\u2019', b=u'\u20ac')
    assert jsonify(obj) == '{"a": "\u2019", "b": "\u20ac"}'

# Generated at 2022-06-12 23:45:28.308629
# Unit test for function jsonify
def test_jsonify():
    class Dummy(object):
        def __repr__(self):
            return 'foo'
    try:
        import simplejson
        HAVE_SIMPLEJSON=True
    except ImportError:
        HAVE_SIMPLEJSON=False

    # json.dumps raises an error on unsupported types like Dummy()
    assert jsonify(Dummy()) == '"foo"'

    if HAVE_SIMPLEJSON:
        # simplejson does not have an encoding option
        data={'one':1, 'two':2}
        assert jsonify(data) == json.dumps(data, default=_json_encode_fallback)
        data = {'one': 1, 'two': u'caf\xe9'}
        assert jsonify(data) == json.dumps(data, default=_json_encode_fallback)

   

# Generated at 2022-06-12 23:45:38.469003
# Unit test for function jsonify
def test_jsonify():
    d1 = dict({"a": "b", "c": "d", u"\u20ac": u"a"})
    d1_json = jsonify(d1)
    try:
        json.loads(d1_json)
    except ValueError:
        assert False, "Failed to jsonify valid data ('%s')" % d1_json
    # KeyError is raised when the encoding is invalid
    d2 = dict({"a": "b", u"c": u"d", u"\xe9": u"a"})
    d2_json = jsonify(d2)
    try:
        json.loads(d2_json)
        assert False, "Succeeded to jsonify invalid data ('%s')" % d2_json
    except ValueError:
        pass
    d3 = dict

# Generated at 2022-06-12 23:45:44.603334
# Unit test for function to_native
def test_to_native():
    assert to_native('simple string') == 'simple string'
    assert to_native(b'simple bytes string') == 'simple bytes string'
    assert to_native(u'simple unicode string') == 'simple unicode string'
    assert to_native(b'\xe2\x98\x83') == '☃'
    assert to_native(u'\u2603') == '☃'
    assert to_native(u"kaléïdoscopique") == "kaléïdoscopique"


# Generated at 2022-06-12 23:46:06.324390
# Unit test for function jsonify
def test_jsonify():
    unit_test_data = {u'key1': u'value1', u'key2': {u'key2a': u'value2a', u'key2b': [u'value2b1', u'value2b2']}}
    unit_test_obj = Set([u'value1', u'value2'])
    unit_test_data_with_set = {u'key1': u'value1', u'key2': {u'key2a': u'value2a', u'key2b': unit_test_obj}}

    assert jsonify(unit_test_data).encode('utf-8') == b'{"key1": "value1", "key2": {"key2a": "value2a", "key2b": ["value2b1", "value2b2"]}}'
    assert json

# Generated at 2022-06-12 23:46:11.021885
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify({1:2}) == '{"1": 2}')
    assert(jsonify({1:2}, sort_keys=False) == '{"1": 2}')
    assert(jsonify({1:2}, sort_keys=True) == '{"1": 2}')



# Generated at 2022-06-12 23:46:18.269340
# Unit test for function to_bytes
def test_to_bytes():
    import sys
    if sys.version_info[0] == 3:
        assert to_bytes(None, 'ascii') == to_bytes(None)
    else:
        assert to_bytes(None, 'ascii') == 'None'

    class Bogus(object):
        def __str__(self):
            raise UnicodeError("foo")
        def __repr__(self):
            raise UnicodeError("bar")

    assert to_bytes("šđčćž") == b's\xc5\xbe\xc4\x91\xc4\x8d\xc4\x87\xc5\xbe'
    assert to_bytes("šđčćž", 'latin-1') == b's\xdf\xb4\xe8\xe6\xfe'
    assert to_bytes

# Generated at 2022-06-12 23:46:28.351235
# Unit test for function to_native
def test_to_native():
    # to_native() should pass through strings by default
    assert 'some string' == to_native('some string')
    # to_native() should only convert objects if they are not already strings
    obj = object()
    assert to_native(obj) == repr(obj)
    # to_native() should convert set() to list
    assert to_native(set([1, 2, 3])) == [1, 2, 3]
    # to_native() should convert frozenset() to list
    assert to_native(frozenset([1, 2, 3])) == [1, 2, 3]
    # to_native() should convert Set() to list
    assert to_native(Set([1, 2, 3])) == [1, 2, 3]


# Generated at 2022-06-12 23:46:38.334610
# Unit test for function to_native
def test_to_native():
    # utf8-encoded-unicode-string as input
    assert to_native(b'\xc3\xbc') == 'ü', 'to_native with utf8-encoded-unicode-string as input, should be umlaut "ü"'
    # utf8-encoded-ascii-string as input
    assert to_native(b'foo') == 'foo', 'to_native with utf8-encoded-ascii-string as input, should be "foo"'
    # unicode string as input
    assert to_native(u'\xc3\xbc') == 'ü', 'to_native with unicode string as input, should be umlaut "ü"'
    # ascii string as input

# Generated at 2022-06-12 23:46:41.084022
# Unit test for function jsonify
def test_jsonify():
    import sys
    import json

    if sys.version_info.major < 3:
        assert jsonify("value") == '"value"'
    else:
        assert jsonify("value") == '"value"'



# Generated at 2022-06-12 23:46:44.330758
# Unit test for function jsonify
def test_jsonify():
    try:
        import simplejson as json
    except ImportError:
        pass

    data = dict(
        foo='bar',
        baz=u'y\xe2\x80\xa8',
    )

    json_data = jsonify(data)
    assert '"\\u00e2"' in json_data
    if not PY3:
        json_data = jsonify(data, ensure_ascii=False)
        assert '\xe2' in json_data


# Generated at 2022-06-12 23:46:55.671168
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native(u'foo') == 'foo'
    assert to_native(b'foo') == 'foo'
    assert to_native(b'foo', errors='surrogate_then_replace') == 'foo'
    assert to_native(b'\xc3\xa9', errors='surrogate_then_replace') == u'\xe9'
    assert to_native(b'fo\xc3', errors='surrogate_then_replace') == u'fo\ufffd'
    assert to_native(b'fo\xc3o', errors='surrogate_then_replace') == u'fo\ufffdo'

# Generated at 2022-06-12 23:47:02.636564
# Unit test for function jsonify
def test_jsonify():
    data = '{"test": "\u0c85"}'
    assert jsonify(data) == '{"test": "\u0c85"}'
    data = u'{"test": "\u0c85"}'
    assert jsonify(data) == '{"test": "\u0c85"}'
    data = b'{"test": "\xe0\xb2\x85"}'
    assert jsonify(data) == '{"test": "\u0c85"}'



# Generated at 2022-06-12 23:47:07.806834
# Unit test for function to_native
def test_to_native():
    for method in ('surrogate_then_replace', 'surrogate_or_strict', 'surrogate_or_replace', None):
        # test ascii
        text_ascii = to_text(b'abcd', errors=method)
        assert text_ascii == u'abcd'
        # test utf-8
        text_utf8 = to_text(u'abcd\u2013'.encode('utf-8'), errors=method)
        assert text_utf8 == u'abcd\u2013'
        text_utf8 = to_text(u'abcd\u2013'.encode('utf-8'), errors=method, encoding='ascii')
        assert text_utf8 == u'abcd\uFFFD'

# Generated at 2022-06-12 23:47:24.869843
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('foobar') == '"foobar"'
    assert jsonify('fòôbâr') == '"fòôbâr"'
    assert jsonify(b'foobar') == '"foobar"'
    assert jsonify(b'f\xc3\xb2\xc3\xb4b\xc3\xa2r') == '"fòôbâr"'



# Generated at 2022-06-12 23:47:34.560361
# Unit test for function to_bytes
def test_to_bytes():
    # Python2
    if not PY3:
        assert to_bytes(u'ÁÇÊ') == b'\xc3\x81\xc3\x87\xc3\x8a'
        assert to_bytes(u'ÁÇÊ', errors='ignore') == b''
        assert to_bytes(u'ÁÇÊ', errors='replace') == b'???'
        assert to_bytes(u'ÁÇÊ', nonstring='empty') == b''
        assert to_bytes(u'ÁÇÊ', nonstring='passthru') == u'ÁÇÊ'

        assert to_bytes(u'from . import foo') == b'from . import foo'


# Generated at 2022-06-12 23:47:43.360514
# Unit test for function to_native
def test_to_native():
    from importlib import import_module
    from ansible.module_utils._text import to_native


# Generated at 2022-06-12 23:47:47.600216
# Unit test for function jsonify
def test_jsonify():
    test_data = {u'this': u'latin-1-value', b'bytes': b'utf-8-value'}
    assert jsonify(test_data) == '{"bytes": "utf-8-value", "this": "latin-1-value"}'
    assert jsonify(test_data, sort_keys=True) == '{"bytes": "utf-8-value", "this": "latin-1-value"}'


# Generated at 2022-06-12 23:47:48.113476
# Unit test for function to_native
def test_to_native():
    pass



# Generated at 2022-06-12 23:47:59.353466
# Unit test for function to_native
def test_to_native():
    """
    Ensure that the values are correctly transformed to native datatypes
    """
    # Test when value is a text string
    assert to_native('text') == u'text'
    # Test when value is a byte string
    assert to_native('text'.encode('utf-8')) == u'text'
    # Test when value is a integer
    assert to_native(10) == 10
    # Test when value is a complex number
    assert to_native(1+1j) == 1+1j
    # Test when value is a tuple
    assert to_native(('a', 'b', 'c')) == ('a', 'b', 'c')
    # Test when value is a boolean
    assert to_native(True) is True
    # Test when value is a list

# Generated at 2022-06-12 23:48:07.640525
# Unit test for function to_bytes
def test_to_bytes():
    # Verify that calling with a byte string returns a byte string
    # This will fail with Python2.4 so we skip it
    if getattr(str, 'encode', False):
        assert isinstance(to_bytes(str()), str)

    # Verify that if we pass unicode in, we get a byte string out
    assert isinstance(to_bytes(text_type()), binary_type)

    # Verify that it will handle a surrogates in unicode
    assert isinstance(to_bytes(text_type('\udcff')), binary_type)
    assert isinstance(to_bytes(text_type('\udcff'), errors='surrogate_or_replace'), binary_type)
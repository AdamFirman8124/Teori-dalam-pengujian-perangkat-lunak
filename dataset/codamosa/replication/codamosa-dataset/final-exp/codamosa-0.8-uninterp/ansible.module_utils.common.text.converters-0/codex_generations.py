

# Generated at 2022-06-12 23:38:27.869254
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'123', nonstring='strict') == b'123'
    assert to_bytes(u'123') == b'123'
    if PY3:
        assert to_bytes(u'\u1234', nonstring='strict') == b'\xe1\x88\xb4'
        assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    else:
        assert to_bytes(u'\u1234', nonstring='strict') == b'\xc4\x8c\xb4'
        assert to_bytes(u'\u1234') == b'\xc4\x8c\xb4'
    assert to_bytes(b'123', nonstring='strict') == b'123'

# Generated at 2022-06-12 23:38:38.282989
# Unit test for function jsonify
def test_jsonify():
    if PY3:
        expected = '{"foo": "\\xc3\\xa9"}'
    else:
        expected = '{"foo": "\\u00e9"}'

    utf8_data = {u'foo': u'é'}
    assert jsonify(utf8_data) == expected

    latin1_data = {'foo': 'é'.encode('latin-1')}
    assert jsonify(latin1_data) == expected

    ascii_data = {'foo': 'e\xcc\x81'.encode('ascii')}
    assert jsonify(ascii_data) == '{"foo": "e\\u0303"}'

    # Test that we can jsonify non-string/bytes types

# Generated at 2022-06-12 23:38:50.172334
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native(None) == 'None'
    assert to_native(True) == 'True'
    assert to_native(False) == 'False'
    assert to_native(u'foobar') == 'foobar'
    assert to_native('foobar') == 'foobar'
    assert to_native(u'Unicode: тест') == 'Unicode: тест'
    assert to_native('Unicode: тест') == 'Unicode: тест'
    # Confirm that we can handle JSON output
    test_dict = {'test': True}
    assert to_native(test_dict) == json.dumps(test_dict)

# Generated at 2022-06-12 23:39:00.363591
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'foo', errors='replace') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'foo', errors='strict') == b'foo'
    assert to_bytes(u'foo', errors='surrogate_or_strict') == b'foo'
    assert to_bytes(u'foo', errors='surrogate_or_replace') == b'foo'
    assert to_bytes(u'foo', errors='surrogate_then_replace') == b'foo'
    assert to_bytes(u'\u07ff') == b'\xe1\x9f\xbf'

# Generated at 2022-06-12 23:39:06.874450
# Unit test for function jsonify
def test_jsonify():
    from .misc import jsonify
    data = {"a": u'\u2019'}
    assert jsonify(data) == '{"a": "\\u2019"}'
    class Foo(object):
        def __repr__(self):
            return u'\u2019'.encode('utf-8')
    assert jsonify(Foo()) == '"\\xe2\\x80\\x99"'


# Generated at 2022-06-12 23:39:17.703994
# Unit test for function to_native
def test_to_native():
    '''
    Test for the function to_native() in module_utils.text
    '''

    # obj is a string; expect return to be the same obj
    obj = 'some string'
    result = to_native(obj)
    assert result == obj

    # obj is an integer; expect return to be an empty string
    obj = 1
    result = to_native(obj)
    assert result == '1'

    # obj is a list; expect return to be a JSON string
    obj = ['some', 'list']
    result = to_native(obj)
    assert result == '[u\'some\', u\'list\']'

    # obj is a dictionary; expect return to be a JSON string
    obj = {'some': 'string', 'is': 'json'}
    result = to_native(obj)
    assert result

# Generated at 2022-06-12 23:39:22.643248
# Unit test for function jsonify
def test_jsonify():
    # Test for function "jsonify"
    # set test data
    data = {"A": b"A", "B": u"B", "C": "C"}
    # run test
    result = jsonify(data)

    # assert result
    assert isinstance(result, text_type)



# Generated at 2022-06-12 23:39:31.997110
# Unit test for function to_native
def test_to_native():
    #no_arg
    assert to_native() == ""
    #str
    assert to_native("str") == "str"
    #unicode
    assert to_native(u"unicode") == u"unicode"
    #bytes
    assert to_native(b"bytes") == b"bytes"
    #int
    assert to_native(1) == 1

# Generated at 2022-06-12 23:39:37.612638
# Unit test for function to_native
def test_to_native():
    '''
    Test function to_native
    '''
    # Test with non printable ASCII characters in the string
    x = to_text(u'\x80ab')
    assert x == u'\uFFFDab'
    # Test with non printable non-ASCII characters in the string
    x = to_text(u'\u2713ab')
    assert x == u'\u2713ab'



# Generated at 2022-06-12 23:39:44.886675
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('a', nonstring='empty') == b''
    assert to_bytes('a', errors='ignore', nonstring='empty') == b''
    assert to_bytes('a', errors='replace', nonstring='empty') == b''
    assert to_bytes('a', errors='surrogate_or_replace', nonstring='empty') == b''
    assert to_bytes('a', errors='surrogate_or_strict', nonstring='empty') == b''
    assert to_bytes('a', errors='surrogate_then_replace', nonstring='empty') == b''
    assert to_bytes('a', errors='xmlcharrefreplace', nonstring='empty') == b''
    assert to_bytes('a', errors='backslashreplace', nonstring='empty') == b''
    # The following tests all PY3 specific

# Generated at 2022-06-12 23:40:03.887119
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    from datetime import timedelta
    from collections import deque, OrderedDict, Counter

    assert(b'foo' == to_native(b'foo'))
    assert(u'foo' == to_native(u'foo'))

    # Test non-string types
    assert(b'True' == to_native(True))
    assert(b'1' == to_native(1))
    assert(b'1.2' == to_native(1.2))
    # Should this be a string with the object's repr?
    assert(b'[1, 2]' == to_native([1, 2]))

    # Ensure we can handle datetime.datetime, datetime.date and datetime.timedelta objects

# Generated at 2022-06-12 23:40:16.765925
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify function '''
    if PY3:
        TEST_STRING = b'\xed\xa0\x95'
    else:
        TEST_STRING = b'\xe5\xaf\xa9'
    TEST_UNICODE = TEST_STRING.decode('utf-8')
    TEST_DICT = {TEST_UNICODE: 0}

    TEST_STRING_2 = b'\xe7\xbc\x96'
    TEST_UNICODE_2 = TEST_STRING_2.decode('utf-8')
    TEST_DICT_2 = {TEST_UNICODE_2: 1}

    TEST_STRING_3 = b'\xf2\x92\x8b'
    TEST_UNICODE_3 = TEST_STRING_3

# Generated at 2022-06-12 23:40:26.060556
# Unit test for function to_native
def test_to_native():
    class TestTextWrapper(object):
        def __str__(self):
            return u"string_repr"

    assert to_native(u"žluťoučký kůň") == u"žluťoučký kůň"
    assert to_native(b"\xc5\xbelu\xc5\xa5ou\xc4\x8dk\xc3\xbd k\xc5\xaf\xc5\x88") == u'žluťoučký kůň'

# Generated at 2022-06-12 23:40:37.958592
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils.six import text_type
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_native
    # On Python 2, str == bytes.
    if PY2:
        assert(isinstance(to_native(u'string'), str))
        assert(isinstance(to_native('string'), str))
        assert(isinstance(to_native(u'unicode_\u018e'), str))
        assert(isinstance(to_native('bytes_\xc3\x8e'), str))
        assert(to_native(u'string') == b'string')
        assert(to_native('string') == b'string')

# Generated at 2022-06-12 23:40:49.178550
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'abc') == b'abc'
    assert to_bytes('abc') == b'abc'
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(1) == b'1'
    x = object()
    assert to_bytes(x) == repr(x).encode()
    assert to_bytes(u'\xa3', 'ascii', nonstring='strict') == b'\xa3'
    assert to_bytes(u'\xa3', 'ascii', 'strict', nonstring='strict') == b'?'
    x = u'\U0001f4a9'
    assert to_bytes(x) == b'\xf0\x9f\x92\xa9'

# Generated at 2022-06-12 23:40:56.166997
# Unit test for function to_native
def test_to_native():
    for obj in [
        u"unicode",
        b"byte string",
        bytearray(b"byte array"),
        1024,
        None,
        True,
        False,
        3.141592653589793,
        Set(),
        datetime.datetime(2016, 8, 17, 20, 18, 19),
        datetime.timedelta(seconds=1),
        json.dumps,
    ]:
        assert isinstance(to_native(obj), str)



# Generated at 2022-06-12 23:41:04.541217
# Unit test for function jsonify
def test_jsonify():
    # Test unicode
    assert jsonify(u'\u7f51\u9875') == json.dumps(u'\u7f51\u9875', encoding='utf-8', default=_json_encode_fallback)

    # Test container
    assert jsonify({"a": "1",
                    "b": "b",
                    "c": u"\u7f51\u9875",
                    "d": 123
                   }) == json.dumps({"a": "1",
                                     "b": "b",
                                     "c": u"\u7f51\u9875",
                                     "d": 123
                                    }, encoding='utf-8', default=_json_encode_fallback)
    # Test no string

# Generated at 2022-06-12 23:41:13.359448
# Unit test for function to_native
def test_to_native():
        assert to_native(u'foo') == u'foo'
        assert to_native(b'foo') == u'foo'
        assert to_native('foo') == u'foo'
        if not PY3:
            assert to_native(buffer('foo')) == u'foo'
        # Check surrogate_or_replace
        assert to_native(b'\xff') == u'\ufffd'
        assert to_native(b'\xff', errors='strict') == u'\ufffd'
        assert to_native(b'\xff', errors='replace') == u'\ufffd'
        assert to_native(b'\xff', errors='surrogate_or_replace') == u'\ufffd'

# Generated at 2022-06-12 23:41:24.676790
# Unit test for function to_bytes
def test_to_bytes():
    # Just a single value to test
    testval = u'⚡'
    # We're not interested in the exception that comes back because
    # to_bytes doesn't support the encoding, this just makes sure that the
    # exception isn't something unexpected
    try:
        to_bytes(testval, 'en_ZA')
    except UnicodeEncodeError:
        pass
    else:
        assert False, 'UnicodeEncodeError should have been raised.'

    # Make sure we can get to_bytes to use surrogateescape
    if HAS_SURROGATEESCAPE:
        testval = testval.encode('utf-8').decode('ascii', 'surrogateescape')
        assert to_bytes(testval, 'utf-8', errors='surrogate_or_replace') == u'⚡'.encode

# Generated at 2022-06-12 23:41:35.570899
# Unit test for function to_bytes
def test_to_bytes():
    # to_bytes is a general purpose function, but it's also used in md5
    # calculations so we need to make sure that it's deterministic and
    # consistent across python versions.
    # These tests are really testing the interaction between to_bytes and
    # the various codecs.

    # String types
    assert to_bytes(u'spam') == b'spam'
    assert to_bytes(u'\xe9') == b'\xc3\xa9'
    assert to_bytes(u'\U00025973') == b'\xe2\x96\xb3'

    # Non-string types
    assert to_bytes(5, nonstring='strict') == b'5'
    assert to_bytes(5, nonstring='simplerepr') == b'5'

# Generated at 2022-06-12 23:41:55.005020
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_text
    item = {
        'data': to_text(u'\u0627\u0644\u0648\u0637\u0646 \u0648\u0627\u0644\u0633\u0639\u0631 \u0648\u0627\u0644\u0627\u0646\u062a\u062e\u0627\u0628')
    }

# Generated at 2022-06-12 23:41:58.759838
# Unit test for function to_native
def test_to_native():
    # Check if function exits
    print("[INFO] Executing test_to_native")
    assert to_native is not None
    # check the variable types
    assert isinstance(to_native, object)
    print("[PASS] Function to_native is not None")



# Generated at 2022-06-12 23:42:04.546232
# Unit test for function jsonify
def test_jsonify():
    data_str = u"{'a': '中文a', 'b': ['中文,中文'], 'c': ['中文,中文']}"
    data = json.loads(data_str)
    json_str = jsonify(data)
    new_data = json.loads(json_str)
    assert len(new_data["b"]) == 1
    assert new_data == {u"a": u"中文a", u"c": [u"中文,中文"], u"b": [u"中文,中文"]}



# Generated at 2022-06-12 23:42:15.378112
# Unit test for function to_bytes
def test_to_bytes():
    import sys
    import random
    import string

    random.seed(0)

    for ascii_str in ('', ' '):
        assert to_bytes(ascii_str) == to_bytes(ascii_str, 'utf-8')
        assert to_bytes(ascii_str, 'utf-8') == to_bytes(ascii_str, 'utf-16')

    for unicode_str in (u'a', u'€', u'\U0001F638'):
        assert to_bytes(unicode_str) == to_bytes(unicode_str, 'utf-8')
        assert to_bytes(unicode_str, 'utf-8') == to_bytes(unicode_str, 'utf-16')

# Generated at 2022-06-12 23:42:21.957983
# Unit test for function jsonify
def test_jsonify():
    my_dict = {u'foo': u'bar',u'baz': u'x\x8F'}
    assert jsonify(my_dict) == json.dumps(my_dict, encoding='utf-8', default=_json_encode_fallback)
    my_dict = {b'foo': b'bar', b'baz': b'x\x8F'}
    assert jsonify(my_dict) == json.dumps(my_dict, encoding='latin-1', default=_json_encode_fallback)



# Generated at 2022-06-12 23:42:28.825225
# Unit test for function to_bytes
def test_to_bytes():
    import random
    import string
    import sys
    import traceback

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    def _check_common_cases(obj, result, encoding='utf-8', errors=None, nonstring='simplerepr'):
        assert to_bytes(obj, encoding, errors, nonstring) == result
        if encoding == 'utf-8' and errors in ('surrogate_or_strict', 'surrogate_or_replace',
                                              'surrogate_then_replace'):
            assert to_bytes(obj, encoding, errors, nonstring) == result


# Generated at 2022-06-12 23:42:34.708929
# Unit test for function to_native
def test_to_native():
    # Test default encoding for to_native
    assert to_native(to_bytes('', 'utf-8')) == ''
    # Test explicit encoding for to_native
    assert to_native(to_bytes('', 'utf-8'), encoding='utf-8') == ''
    # Test non-UTF-8 input with default encoding
    assert to_native(to_bytes('', 'latin-1')) == ''

# Generated at 2022-06-12 23:42:42.434560
# Unit test for function to_native

# Generated at 2022-06-12 23:42:52.230754
# Unit test for function to_bytes

# Generated at 2022-06-12 23:42:59.926158
# Unit test for function to_bytes
def test_to_bytes():
    """Ensure that we can pass around byte strings and text strings"""
    assert to_bytes('abc123') == b'abc123'
    assert to_bytes(u'abc123') == b'abc123'
    assert to_bytes(u'\xe9') == b'\xc3\xa9'
    assert to_bytes('\xe9') == b'\xe9'
    assert to_bytes(u'\u2603') == b'\xe2\x98\x83'
    assert to_bytes('\xe9', errors='surrogate_then_replace') == b'?'
    assert to_bytes(bytearray(b'abc123')) == b'abc123'
    assert to_bytes(b'abc123') == b'abc123'



# Generated at 2022-06-12 23:43:17.142270
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_unicode, to_bytes
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import Set
    # Given
    data = to_unicode('fööbär')
    assert to_text(data) == to_text('fööbär')
    assert to_bytes(data) == to_bytes('fööbär')
    # When
    json_encoded_data = jsonify(data)
    # Then
    assert json_encoded_data == '"f\\u00f6\\u00f6b\\u00e4r"'

    # Given
    data = to_bytes('fööbär')
    assert to_text(data) == to_

# Generated at 2022-06-12 23:43:24.387944
# Unit test for function to_bytes
def test_to_bytes():
    import pytest
    assert to_bytes(u'\u043c\u0438\u0440') == b'\xd0\xbc\xd0\xb8\xd1\x80'
    assert to_bytes(to_text(b'\xd0\xbe\xd0\xbd\xd0\xbe\xd1\x87')) == b'\xd0\xbe\xd0\xbd\xd0\xbe\xd1\x87'
    assert to_bytes(object()) == b'<object object at 0x7f709cec1a40>'
    assert to_bytes(object(), nonstring='passthru') == object()
    assert to_bytes(object(), nonstring='empty') == b''

# Generated at 2022-06-12 23:43:35.273689
# Unit test for function jsonify
def test_jsonify():
    data = "<129b>-string"
    json_data = jsonify(data)
    assert(json_data == '"<129b>-string"')
    data = u"<129b>-string"
    json_data = jsonify(data)
    assert(json_data == '"<129b>-string"')
    from ansible.module_utils.six import BytesIO
    data = BytesIO()
    data.name = 'test'
    json_data = jsonify(data)
    assert(json_data == '{"name": "test"}')
    data = None
    json_data = jsonify(data)
    assert(json_data == 'null')
    data = "string"
    json_data = jsonify(data)
    assert(json_data == '"string"')


# Generated at 2022-06-12 23:43:43.005294
# Unit test for function to_native
def test_to_native():
    assert to_native(1) == 1
    assert isinstance(to_native(1), int)

    assert to_native(to_bytes('hello')) == 'hello'
    try:
        to_native(to_bytes('hello'), nonstring='strict')
        assert False, 'should have raised error'
    except TypeError:
        pass
    assert isinstance(to_native(to_bytes(u'hello')), text_type)

    assert to_native(u'hello') == u'hello'
    try:
        to_native(u'hello', nonstring='strict')
        assert False, 'should have raised error'
    except TypeError:
        pass
    assert isinstance(to_native(u'hello'), text_type)


# Generated at 2022-06-12 23:43:52.391470
# Unit test for function jsonify

# Generated at 2022-06-12 23:43:55.472244
# Unit test for function to_native
def test_to_native():
    for in_val, out_val in get_examples():
        assert to_native(in_val) == out_val


# Generated at 2022-06-12 23:44:07.071231
# Unit test for function to_native

# Generated at 2022-06-12 23:44:17.557286
# Unit test for function to_bytes
def test_to_bytes():
    assert isinstance(to_bytes(u'foo'), binary_type)

    assert isinstance(to_bytes(u'ü'), binary_type)
    assert isinstance(to_bytes(u'ü', u'latin-1'), binary_type)
    assert isinstance(to_bytes(u'ü'.encode('utf-8')), binary_type)
    assert isinstance(to_bytes(u'ü'.encode('utf-8'), encoding='ascii'), binary_type)

    if PY3:
        # most things should be unicode by default
        assert isinstance(to_bytes(123), binary_type)
        assert isinstance(to_bytes(u'ü'.encode('utf-8'), encoding='ascii'), binary_type)

        # ensure bytes are still encoded as desired

# Generated at 2022-06-12 23:44:22.274223
# Unit test for function jsonify
def test_jsonify():
    data = {
        'a': 1,
        'b': 2,
        'set1': Set([1, 2, 3]),
        'set2': Set([2, 3, 4]),
        'datetime': datetime.datetime(2014, 2, 3, 5, 6)
    }
    result = jsonify(data)
    print(result)
test_jsonify()

# Generated at 2022-06-12 23:44:28.787900
# Unit test for function jsonify
def test_jsonify():
    data = {
        'a': b'\xe3',
        'b': u'\u732b',
        'c': u'\u8001\u9f20',
    }
    assert jsonify(data) == """{
  "b": "\u732b",
  "c": "\u8001\u9f20",
  "a": "\\u00e3"
}"""



# Generated at 2022-06-12 23:44:57.038742
# Unit test for function jsonify
def test_jsonify():
    # Test data
    data1 = dict(a=1, b=2)
    data2 = dict(a=1, b=dict(a=1, b=2))
    data3 = dict(a=[dict(a=1, b=2), dict(a=2, b=3)])
    data4 = dict(a=1, b=u'\u2714')
    data5 = dict(a=u'\u2714', b=u'\u2714')

    # Test with container_to_text is False
    result = jsonify(data1)
    #print result
    assert result == '{"a": 1, "b": 2}'

    result = jsonify(data2)
    #print result

# Generated at 2022-06-12 23:45:06.174822
# Unit test for function jsonify
def test_jsonify():
    # Test for string type
    assert jsonify('{"foo": "bar"}') == '"{\\"foo\\": \\"bar\\"}"'
    assert jsonify(b'{"foo": "bar"}') == '"{\\"foo\\": \\"bar\\"}"'
    assert jsonify(u'{"foo": "bar"}') == '"{\\"foo\\": \\"bar\\"}"'

    # Test for non-string type
    assert jsonify(['foo', 'bar']) == '["foo", "bar"]'
    assert jsonify({'foo': 'bar', 'zing': 'zang'}) == '{"foo": "bar", "zing": "zang"}'

# Test for function jsonify
test_jsonify()


# Generated at 2022-06-12 23:45:14.915471
# Unit test for function to_bytes
def test_to_bytes():
    try:
        # Register the surrogateescape handler on Python2
        codecs.register_error('surrogateescape', codecs.surrogateescape_error)
    except NameError:
        pass

    assert to_bytes('foo') == b'foo'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes('foo'.encode('latin-1'), errors='surrogateescape') == b'foo'
    assert to_bytes('foo', errors='surrogateescape') == b'foo'
    assert to_bytes('\ufffd') == b'?'

    # Python 2

# Generated at 2022-06-12 23:45:26.646033
# Unit test for function to_native
def test_to_native():

    for value in [
        None,
        True,
        123,
        1.23,
        b'bytes',
        bytearray(b'bytearray'),
        set([1, 2]),
        [1, 2],
        (1, 2),
        u'unicode',
        datetime.datetime(1, 1, 1),
        datetime.timedelta(1, 1, 1),
        datetime.date(1, 1, 1),
        datetime.time(1, 1, 1),
    ]:
        assert to_native(value) == text_type(value)

    # json_dict is an OrderedDict specifically because we want to test the
    # proper order of items coming out of json.dumps (json.dumps does not
    # guarantee the order of output).  This means

# Generated at 2022-06-12 23:45:36.760406
# Unit test for function to_bytes
def test_to_bytes():
    text_type('\r\n').encode('utf-8')
    # Nonstrings:
    #    - SimpleRepr should return a bytes version of the simple repr of the object
    #      simple repr is str in python3 and unicode in python2
    #    - passthru should return the object
    #      Note: While both simplerepr and passthru will work with most types, we
    #      can't test using it with types that don't have a str/repr and isinstance
    #      doesn't give false positives on these types
    #    - empty and strict shouldn't be tested as they raise an exception
    for nonstring in ('simplerepr', 'passthru'):
        # Test with empty string
        assert to_bytes(u'', nonstring=nonstring) == b''

        # Test with unicode string
       

# Generated at 2022-06-12 23:45:44.094120
# Unit test for function to_native
def test_to_native():
    # Check that to_native converts a text string to unicode on Python2 and
    # keeps it as text on Python3.
    if PY3:
        assert isinstance(to_native(u'text'), str)
        assert u'text' == to_native(u'text')
    else:
        assert isinstance(to_native(u'text'), unicode)
        assert u'text' == to_native(u'text')
        # And now to make sure that text strings become unicode
        assert isinstance(to_native(str(u'text')), unicode)
        assert u'text' == to_native(str(u'text'))

    # Check that to_native converts a byte string to unicode on Python2 and
    # keeps it as byte on Python3
    if PY3:
        assert isinstance

# Generated at 2022-06-12 23:45:54.218866
# Unit test for function to_native
def test_to_native():
    assert to_native(b'bytes') == u'bytes'
    assert to_native(u'unicode') == u'unicode'
    assert to_native(u'\u00f8') == u'\u00f8'
    assert to_native(1) == '1'
    assert to_native(1.1) == '1.1'
    assert to_native(None) == ''
    assert to_native(NotImplemented) == ''
    assert to_native(Ellipsis) == ''

    # Test fallback
    assert to_text(b'\xff', nonstring='passthru') == u''
    assert to_text(b'\xff', nonstring='simplerepr') == u"''"
    assert to_text(b'\xff', nonstring='empty') == u''
   

# Generated at 2022-06-12 23:46:03.412479
# Unit test for function jsonify
def test_jsonify():
    assert '"test"' == jsonify(u'test')
    assert '1' == jsonify(1)
    assert 'true' == jsonify(True)
    assert '"\\ud83d\\ude00\\u2665\\ud83d\\ude00"' == jsonify(u'\U0001f600\u2665\U0001f600')
    assert 'true' == jsonify(True)
    assert '{"a": "test"}' == jsonify({'a': u'test'})
    assert '["test", "test2"]' == jsonify([u'test', u'test2'])



# Generated at 2022-06-12 23:46:13.919007
# Unit test for function jsonify
def test_jsonify():
    # testing jsonify function with ascii value
    ascii_val = 'I am a string with ascii characters only.'
    expected_data = '"I am a string with ascii characters only."'
    assert jsonify(ascii_val) == expected_data
    # testing jsonify function with unicode value
    unicode_val = u'I am a string with unicode characters å'
    expected_data = '"I am a string with unicode characters \\u00e5"'
    assert jsonify(unicode_val) == expected_data
    data_dict = {
        'unicode_val': unicode_val,
        'ascii_val': ascii_val
    }

# Generated at 2022-06-12 23:46:18.456630
# Unit test for function jsonify
def test_jsonify():
    data = {"abc": [{"def": u"\u6d4b\u8bd5"}]}
    assert jsonify(data) == '{"abc": [{"def": "\\u6d4b\\u8bd5"}]}'



# Generated at 2022-06-12 23:46:43.688168
# Unit test for function to_bytes
def test_to_bytes():
    for encoded_string in (b'I am binary', u'I am unicode', u'I am unicode with \U0001f4a9',
                           u'I am unicode with surrogate \udc17',
                           # This byte sequence is invalid utf-8.  It's the byte representation
                           # of a surrogate in utf-8 form
                           b'\xed\xb1\x87',
                           # Two codepoints that don't map to anything in latin1
                           u'\U0001f4a9\U0001f4a9',
                           u'\uF09F\u9C88',
                           ):
        assert isinstance(to_bytes(encoded_string), binary_type)

# Generated at 2022-06-12 23:46:51.340175
# Unit test for function jsonify
def test_jsonify():
    complex_dict = dict(a=dict(b=[dict(c='d', e=[1,2]),
                          dict(f='g', h=dict(i='j'))]))

    complex_dict = jsonify(complex_dict)
    assert complex_dict == '{"a": {"b": [{"c": "d", "e": [1, 2]}, {"f": "g", "h": {"i": "j"}}]}}'


# Generated at 2022-06-12 23:47:01.932948
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native(b'foo', errors='strict') == 'foo'
    assert to_native('\xff', encoding='ascii', errors='strict') == '\ufffd'
    assert to_native(b'foo', errors='surrogate_or_strict') == 'foo'
    assert to_native('\xff', encoding='ascii', errors='surrogate_or_strict') == '\ufffd'
    assert to_native(b'foo', errors='surrogate_or_replace') == 'foo'
    assert to_native('\xff', encoding='ascii', errors='surrogate_or_replace') == '?'
    assert to_native(b'foo', errors='surrogate_then_replace') == 'foo'

# Generated at 2022-06-12 23:47:05.553896
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": {1: "ö"}, 2: u"ö", 3: [u"ö"]}) == '{"2": "\\u00f6", "3": ["\\u00f6"], "a": {"1": "\\u00f6"}}'



# Generated at 2022-06-12 23:47:12.231811
# Unit test for function to_native
def test_to_native():
    # Strings are passed through
    assert to_native(b'foo') == 'foo'
    assert to_native(u'foo') == 'foo'

    # Except on py26.  There str() on a unicode object returns a bytestring
    if PY3:
        assert to_native(u'\u1234') == '\u1234'

    # Non strings are type coerced
    assert to_native(b'foo') == 'foo'
    assert to_native(123) == '123'

    # None is a special case
    assert to_native(None) is None



# Generated at 2022-06-12 23:47:21.786492
# Unit test for function to_native
def test_to_native():
    # Verify that no exceptions gets raised
    assert to_native(datetime.datetime(2010, 2, 8, 15, 23, 42)) == u'2010-02-08T15:23:42'
    assert to_native(datetime.datetime(2010, 2, 8, 15, 23, 42, 100000)) == u'2010-02-08T15:23:42.100000'
    assert to_native(datetime.datetime(2010, 2, 8, 15, 23, 42, 100000)) == to_native(datetime.datetime(2010, 2, 8, 15, 23, 42))
    assert to_native(datetime.datetime(2010, 2, 8, 15, 23, 42, 100000)) == to_native(datetime.datetime(2010, 2, 8, 15, 23, 42, 100001))

# Generated at 2022-06-12 23:47:32.065092
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"key": "val" + chr(233)}, sort_keys=True) == '{"key": "val\xc3\xa9"}'
    assert jsonify({"key": "val" + chr(233)}, sort_keys=True, ensure_ascii=False) == '{"key": "valé"}'
    assert jsonify({"key": "val" + chr(233)}, sort_keys=True, ensure_ascii=False, encoding='latin1') == '{"key": "val\xe9"}'
    assert jsonify({"key": "val" + chr(233)}, sort_keys=True, ensure_ascii=False, encoding='ascii') == '{"key": "val\xc3\xa9"}'



# Generated at 2022-06-12 23:47:40.515598
# Unit test for function jsonify
def test_jsonify():
    # Check for normal unicode strings
    assert jsonify(u'hello') == '"hello"'
    # Check for non-ascii unicode strings
    assert jsonify(u'\u1234') == '"\\u1234"'
    # Check for unicode strings with surrogateescape
    assert jsonify(u'\udc80\udcff') == '"\\udc80\\udcff"'
    # Check for unicode strings with surrogatepair
    assert jsonify(u'\ud800\udc00') == '"\\ud800\\udc00"'
    # Check for byte strings
    assert jsonify(b'\x80') == '"\\u0080"'
    # Check for byte strings with surrogateescape

# Generated at 2022-06-12 23:47:48.079564
# Unit test for function to_native
def test_to_native():
  '''

     Test for function to_native
  '''
  utc_datetime = datetime.datetime(2014, 8, 1, 10, 18, 18, 0, tzinfo=None)

  # 1. Test with str and bytes type
  # 1.1 empty str
  s_str_url = ""
  s_bytes_url = b""
  r_str_url = to_native(s_str_url, errors='surrogate_or_strict')
  r_bytes_url = to_native(s_bytes_url, errors='surrogate_or_strict')
  assert s_str_url == r_str_url
  assert s_bytes_url == r_bytes_url

  # 1.2  str

# Generated at 2022-06-12 23:47:59.315776
# Unit test for function to_native
def test_to_native():
    # pylint: disable=redefined-outer-name
    from ansible.module_utils._text import to_native
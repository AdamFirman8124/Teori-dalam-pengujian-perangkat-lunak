

# Generated at 2022-06-12 23:38:23.447356
# Unit test for function to_native
def test_to_native():
    from datetime import datetime
    assert to_native(dict(test=None)) == dict(test=None)
    assert to_native(None) == None
    assert to_native(1) == 1
    assert to_native(datetime.fromtimestamp(1)) == '1970-01-01 00:00:01'

    # Datetime objects should be serialized
    assert to_native(dict(when=datetime.fromtimestamp(1))) == dict(when='1970-01-01 00:00:01')

    # UUID objects should be serialized
    import uuid

# Generated at 2022-06-12 23:38:35.423526
# Unit test for function to_native
def test_to_native():

    assert to_native(b'foo') == 'foo'
    assert to_native(u'foo') == 'foo'
    assert to_native(b'foo', errors='surrogate_or_strict') == u'foo'
    assert to_native(u'foo', errors='surrogate_or_replace') == 'foo'

    assert to_native(u'♥') == u'♥'
    assert to_native(u'♥'.encode('utf-8')) == u'♥'
    assert to_native(u'♥'.encode('utf-8'), errors='surrogate_or_strict') == u'♥'
    assert to_native(u'♥'.encode('utf-8'), errors='surrogate_or_replace') == u'♥'


# Generated at 2022-06-12 23:38:47.400939
# Unit test for function to_native
def test_to_native():
    assert to_native(10) == 10
    assert to_native(10.5) == 10.5
    assert to_native(u"hello") == "hello"
    assert to_native(u"привет") == "привет"
    assert to_native(u"привет", encoding="cp1252") == "Ð¿ÑÐ¾Ð²ÐµÑ"
    assert to_native(b"hello") == "hello"

# Generated at 2022-06-12 23:38:57.377484
# Unit test for function to_native
def test_to_native():
    def run(obj):
        print("to_native('%r'): %r" % (obj, to_native(obj)))

    run(u'\u1234')
    run(b'\xe1\x88\xb4')
    run(1)
    run(1.1)
    run(None)
    run(u'{"a":2}')
    run({u'a': 2})
    run(u'foo')
    run(b'bar')
    run([u'foo', u'bar'])
    run({u'a': 2, 'b': 3})
    run([{u'a': 2, 'b': 3}, {'c': 4, 'd': 5}])
    run(u'\u1234'.encode('utf-16-be'))

# Generated at 2022-06-12 23:39:07.798043
# Unit test for function to_bytes
def test_to_bytes():
    import sys
    import warnings

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from ansible.module_utils.six import BytesIO
    from io import StringIO

    class TestToBytes(unittest.TestCase):
        def setUp(self):
            warnings.filterwarnings('error')

        def tearDown(self):
            warnings.resetwarnings()

        def test_b_string_passthru(self):
            value = b'foobar'
            result = to_bytes(value, nonstring='passthru')
            self.assertEqual(result, value)
            self.assertIs(type(result), binary_type)

        def test_text_string_utf8(self):
            value = u

# Generated at 2022-06-12 23:39:17.766978
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native('\xc3\x80') == u'À'
    assert to_native('\xc3\x80'.encode('utf8')) == u'À'
    assert to_native(u'\xc3\x80') == u'À'
    assert to_native(u'\xc3\x80'.encode('utf8')) == u'À'
    assert to_native('\xa1') == u'¡'
    assert to_native('\xa1'.encode('latin1')) == u'¡'
    assert to_native(u'\xa1') == u'¡'

# Generated at 2022-06-12 23:39:24.115167
# Unit test for function jsonify
def test_jsonify():
    def _json_encode_fallback(obj):
        if isinstance(obj, Set):
            return list(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError("Cannot json serialize %s" % to_native(obj))
    from datetime import datetime
    from collections import Set
    import json
    import unittest
    import time

# Generated at 2022-06-12 23:39:33.095561
# Unit test for function to_bytes

# Generated at 2022-06-12 23:39:42.200178
# Unit test for function to_native
def test_to_native():
    print("### to_native() ###")
    str1 = 'abc'
    print("str1=" + to_native(str1))
    bytes1 = b'abc'
    print("bytes1=" + to_native(bytes1))
    dict1 = {'key1': 'val1', 'key2': 'val2'}
    print("dict1=" + to_native(dict1))
    list1 = ['val1', 'val2']
    print("list1=" + to_native(list1))
    set1 = Set(['val1', 'val2', 'val3'])
    print("set1=" + to_native(set1))
    time1 = datetime.datetime(2015,1,1,14,12,1)
    print("time1=" + to_native(time1))
    print

# Generated at 2022-06-12 23:39:53.260041
# Unit test for function to_native
def test_to_native():
    # Make sure that text is returned as unicode and bytes as bytestrings
    assert isinstance(to_native(b'ascii'), binary_type)
    assert isinstance(to_native(u'ascii'), text_type)
    # Make sure that other types are passed through unchanged
    assert to_native(5) == 5
    assert to_native(Set()) == Set()
    # Make sure that JSON serialization works
    assert to_native(datetime.datetime(2009, 5, 15, 22, 27)) == '2009-05-15T22:27:00'
    assert to_native(datetime.date(2009, 5, 15)) == '2009-05-15'
    assert to_native(datetime.time(22, 27, 21)) == '22:27:21'

# Generated at 2022-06-12 23:40:15.524061
# Unit test for function to_bytes
def test_to_bytes():
    def test_fails(obj, encoding='utf-8', errors='surrogate_or_replace', nonstring='simplerepr'):
        try:
            to_bytes(obj, encoding, errors, nonstring)
            raise AssertionError('%r with parameters (encoding=%r, errors=%r, nonstring=%r) '
                                 'did not fail' % (obj, encoding, errors, nonstring))
        except (UnicodeEncodeError, TypeError):
            pass


# Generated at 2022-06-12 23:40:24.276074
# Unit test for function jsonify
def test_jsonify():
    data = {'hello': 'world'}
    assert jsonify(data) == json.dumps(data, default=_json_encode_fallback)

    data = {'hello': 'world'.decode('latin-1')}
    assert jsonify(data) == json.dumps(data, default=_json_encode_fallback)

    for k, v in iteritems(data):
        data[k] = v.encode('utf-16')
    assert jsonify(data) == json.dumps(data, default=_json_encode_fallback)

    data = {'hello': 'world'.decode('latin-1').encode('utf-16')}
    assert jsonify(data) == json.dumps(data, default=_json_encode_fallback)


# Generated at 2022-06-12 23:40:27.922716
# Unit test for function jsonify
def test_jsonify():
    data = {"a": u"\u1111"}
    import json
    try:
        json.dumps(data)
    except UnicodeEncodeError:
        pass
    jsonify(data)


# Generated at 2022-06-12 23:40:39.213748
# Unit test for function to_bytes
def test_to_bytes():
    """
    Test to_bytes function.
    """
    def check(text, bytes_, encoding='utf-8', errors='surrogate_then_replace', nonstring='simplerepr'):
        """
        Verify to_bytes returns the expected bytes.

        :arg text: The text string to use as input.  Any encoding errors
            should be fixed first.
        :arg bytes_: The expected bytes returned.
        :kwarg encoding: The encoding to use when converting to bytes.
        :kwarg errors: The error handler to use if ``text`` is not encodable
            using the specified encoding.
        """
        assert (to_bytes(text, encoding, errors, nonstring) == bytes_)
        assert (to_bytes(text, encoding, errors, nonstring) == bytes_)

# Generated at 2022-06-12 23:40:49.984383
# Unit test for function to_bytes
def test_to_bytes():
    # Only do the test if we have surrogateescape
    if HAS_SURROGATEESCAPE:
        assert to_bytes(u'\uDC80', 'ascii', errors='surrogate_or_strict') == b'\x80'
        assert to_bytes(u'\uDC80', 'ascii', errors='surrogate_or_replace') == b'?'
        assert to_bytes(u'\\uDC80', 'ascii', errors='surrogate_or_replace') == b'?'
        assert to_bytes(u'\\uDC80', 'ascii', errors='surrogate_then_replace') == b'?\\uDC80'

# Generated at 2022-06-12 23:41:00.464417
# Unit test for function jsonify
def test_jsonify():
    data = {
        'unicode': u'\u2665',
        'bytes': 'Within quotes',
        'str': "Within quotes",
        'list': [u'\u2665', 'bytes', "str"],
        'dict': {
            u'unicode': u'\u2665',
            'bytes': 'Within quotes',
            'str': "Within quotes",
            'nested': {
                u'unicode': u'\u2665',
                'bytes': 'Within quotes',
                'str': "Within quotes"
            },
            'list': [u'\u2665', 'bytes', "str"]
        },
    }
    def check_type(data):
        assert isinstance(data, text_type), type(data)

# Generated at 2022-06-12 23:41:06.704171
# Unit test for function to_native
def test_to_native():
    # (type, value, result)
    data = [(text_type, u'foo', 'foo'), (binary_type, b'foo', u'foo')]
    if not PY3:
        data.append((binary_type, b'\xc3\xb1', u'\xf1'))
    for type_, value, result in data:
        assert to_native(type_(value)) == result



# Generated at 2022-06-12 23:41:14.972591
# Unit test for function to_bytes
def test_to_bytes():
    # Tests for converting a text string to bytes

    # We want to build the control string one code point at a time so that we
    # can test how the codecs can handle encoding problems with each
    # individual code point.
    # We build it as a list of code points because that's easier to reason
    # about than a list of Python-escaped utf-8 bytes.
    c = []  # control bytes

    # We start with some easy ascii
    c.extend(map(ord, u'abc'))

    # Now we'll put in some latin-1
    c.append(0xC0)  # Invalid because it's over long
    c.append(0xA9)  # copywrite symbol
    c.append(0xFF)  # Invalid because it's over long

    # Now some 2 byte utf-

# Generated at 2022-06-12 23:41:26.868948
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\u2713') == u'"\u2713"'
    assert jsonify([u'\u2713']) == u'["\u2713"]'
    assert jsonify({'foo': [u'\u2713']}) == u'{"foo": ["\u2713"]}'
    assert jsonify({u'\u2713': 'foo'}) == u'{"\u2713": "foo"}'
    assert jsonify({'foo': {u'\u2713': 'foo'}}) == u'{"foo": {"\u2713": "foo"}}'
    assert ((jsonify(datetime.datetime(2001, 2, 3, 4, 5, 6, 7))) ==
            u'"2001-02-03T04:05:06.000007"')

# Generated at 2022-06-12 23:41:36.850453
# Unit test for function jsonify
def test_jsonify():
    data = {u'\u1234': 'value'}
    assert jsonify(data) == '{"\\u1234": "value"}'
    # Use simplejson on old systems
    import sys
    default_json = sys.modules['json']
    sys.modules['json'] = __import__('simplejson')
    assert jsonify(data) == '{"\\u1234": "value"}'
    sys.modules['json'] = default_json
    # Encoding to latin-1
    data = {u'\u1234': u'\uffff'}
    assert jsonify(data) == '{"\\xe1\\x88\\xb4": "\\xff"}'



# Generated at 2022-06-12 23:41:48.504177
# Unit test for function jsonify
def test_jsonify():
    data = {'a': '中文', 'b': '中文'.encode('latin-1'), 'c':2}
    result = jsonify(data)
    print(result)


# Generated at 2022-06-12 23:41:59.531742
# Unit test for function jsonify
def test_jsonify():
    # Integer test.
    data = 1
    assert jsonify(data) == '1'

    # Unicode string test.
    data = u'\u6d4b\u8bd5'
    assert jsonify(data) == '"\\u6d4b\\u8bd5"'

    # Unicode dict test.
    data = {u'\u6d4b\u8bd5': u'\u6d4b\u8bd5'}
    assert jsonify(data) == '{"\\u6d4b\\u8bd5": "\\u6d4b\\u8bd5"}'

    # list test.
    data = [1, 2, 3, 4]
    assert jsonify(data) == '[1, 2, 3, 4]'

    # set test.

# Generated at 2022-06-12 23:42:10.203765
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common._collections_compat import from_bytes

    assert to_native(u'\u1234') == u'\u1234'
    assert to_native(u'\u1234', charset='latin-1') == u'\u1234'

    # We can't test binary because we don't know what the terminal supports
    #assert to_native(b'foo') == u'foo'

    assert to_native(b'foo', errors='strict') == 'foo'
    assert to_native(b'foo', errors='surrogatepass') == 'foo'
    assert to_native(b'foo', errors='surrogate_or_strict') == 'foo'

# Generated at 2022-06-12 23:42:13.761540
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify([1, 2, [3]]) == '[1, 2, [3]]'
    assert jsonify({u'foo': [{u'bar': u'baz'}]}) == '{"foo": [{"bar": "baz"}]}'



# Generated at 2022-06-12 23:42:23.485996
# Unit test for function jsonify
def test_jsonify():
    # test jsonify encode exception
    with pytest.raises(UnicodeDecodeError) as excinfo:
        jsonify('\u3718')
    # test jsonify encode other exception
    with pytest.raises(TypeError) as excinfo:
        jsonify(dict(a=1, b=2))
    # test jsonify encode byte string
    try:
        jsonify({b'a':b'\xd0\xbf'})
    except Exception as e:
        pytest.fail("test jsonify encode byte string failed")
    # test jsonify encode unicode string
    try:
        jsonify({u'a':u'\u041f', u'b':u'\u0440'})
    except Exception as e:
        pytest.fail("test jsonify encode unicode string failed")
    #

# Generated at 2022-06-12 23:42:29.709807
# Unit test for function to_native
def test_to_native():
    """Unit test cases for to_native function"""

    assert(to_bytes("Hello World") == b'Hello World')
    assert(to_text("Hello World") == u"Hello World")

    assert(to_bytes(b"Hello World") == b'Hello World')
    assert(to_text(b"Hello World") == u"Hello World")

    assert(to_bytes(u"Hello World") == b'Hello World')
    assert(to_text(u"Hello World") == u"Hello World")

    assert(to_bytes("Héllö Wörld", errors='strict') == b'H\xc3\xa9ll\xc3\xb6 W\xc3\xb6rld')

# Generated at 2022-06-12 23:42:39.575529
# Unit test for function to_bytes
def test_to_bytes():
    # Make sure that text values are converted to byte strings.
    # We use repr to limit the number of failure points.
    if PY3:
        # Don't use repr for this case as it's locale dependent in 3.2
        assert to_bytes(text_type(u'bytes', 'utf-8')) == b'bytes'
    else:
        # 2.6-2.7 repr of unicode is b'bytes'
        assert to_bytes(repr(text_type(u'bytes', 'utf-8'))) == b'bytes'

    # Make sure nonstrings are handled properly
    for nonstring in ('empty', 'simplerepr', 'passthru'):
        assert to_bytes(True, nonstring=nonstring) == to_bytes(b'true', nonstring=nonstring)

# Generated at 2022-06-12 23:42:46.329840
# Unit test for function to_native
def test_to_native():
    assert 'unicode' == to_native(to_text(u'unicode'))
    assert 'str' == to_native(to_bytes(u'str'))
    assert u'unicode' == to_native(u'unicode')
    assert 'str' == to_native('str')
    if PY3:
        assert 'bytes' == to_native(b'bytes')
    else:
        assert 'bytes' == to_native(b'bytes')



# Generated at 2022-06-12 23:42:55.835013
# Unit test for function to_bytes
def test_to_bytes():
    # Test encodings
    for e in ('ascii', 'utf-8', 'utf-16', 'utf-32'):
        foo = u'\u00fc'
        bar = to_bytes(foo, encoding=e)
        assert isinstance(bar, binary_type)
        assert bar == codecs.getencoder(e)(foo)[0]

    # Test non-string handling
    assert to_bytes(1, nonstring='simplerepr') == b'1'
    assert to_bytes(b'foo', nonstring='simplerepr') == b'foo'
    assert to_bytes(u'foo', nonstring='simplerepr') == b'foo'
    assert to_bytes(u'\u00fc', nonstring='simplerepr') == b'\xc3\xbc'
    assert to_bytes

# Generated at 2022-06-12 23:43:06.720557
# Unit test for function jsonify
def test_jsonify():
    # utf-8 and ascii unicode
    data = {'foo': '\xe5\xae\xb6\xe7\xba\xa7\xe5\x8e\x9f\xe5\x9b\xa0'}
    assert jsonify(data) == '{"foo": "\\u5bb6\\u7ead\\u53f0\\u539f\\u56e0"}'

    # latin-1 unicode
    data = {'foo': '\xe1\x8a\xa0\xe1\x88\x9d\xe1\x88\xad'}
    assert jsonify(data) == '{"foo": "\\u1ca0\\u12dd\\u128d"}'

    # utf-8 and latin-1 unicode mixed, utf-

# Generated at 2022-06-12 23:43:25.702799
# Unit test for function jsonify
def test_jsonify():
    data = dict(key1 = "value1", key2 = u"value2")
    assert jsonify(data) == '{"key1": "value1", "key2": "value2"}'



# Generated at 2022-06-12 23:43:36.528506
# Unit test for function jsonify
def test_jsonify():
    # Test the jsonify function using the provided data.
    import sys
    if sys.version_info.major == 2:
        unicode_class = unicode
    else:
        unicode_class = str

# Generated at 2022-06-12 23:43:47.968029
# Unit test for function to_bytes
def test_to_bytes():
    text = u'\u043a\u0438\u0440\u0438\u043b\u043b\u0438\u0446\u0430'
    ascii_encoded = b'\xd0\xba\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbb\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0'
    utf8_encoded = b'\xd0\xba\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbb\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0'

# Generated at 2022-06-12 23:43:55.830685
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        text = '你好'
        bytes_ = text.encode('utf-8')
    else:
        text = ('你好').decode('utf-8')
        bytes_ = ('你好').decode('utf-8')

    try:
        codecs.lookup_error('surrogateescape')
        has_surrogateescape = True
    except LookupError:
        has_surrogateescape = False

    # Test surrogates
    assert to_bytes(text, encoding='utf-8', errors='surrogate_then_replace') == b'\xe4\xbd\xa0\xe5\xa5\xbd'


# Generated at 2022-06-12 23:44:07.294121
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six import BytesIO

    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'B\xe9po', 'ascii') == b'Be\xcc\x81po'
    assert to_bytes(u'B\xe9po', 'latin-1') == b'B\xe9po'
    assert to_bytes(u'B\xe9po', 'utf-8') == b'B\xc3\xa9po'
    assert to_bytes(u'B\xe9po') == b'B\xc3\xa9po'
    assert to_bytes(u'B\u0303\u0308po') == b'B\xc3\xa9po'

# Generated at 2022-06-12 23:44:17.800498
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b"foo") == b"foo"
    assert to_bytes(b"foo", nonstring="passthru") is b"foo"
    assert to_bytes(b"foo", encoding="latin-1") == b"foo"
    assert to_bytes(u"f\xf6\xf6", encoding="latin-1") == b"f\xf6\xf6"
    assert to_bytes(u"f\xf6\xf6", encoding="latin-1", errors='surrogate_or_strict') == b"f\xf6\xf6"
    assert to_bytes(u"f\xf6\xf6", encoding="latin-1", errors='surrogate_or_replace') == b"f\xf6\xf6"

# Generated at 2022-06-12 23:44:23.371899
# Unit test for function to_native
def test_to_native():
    assert to_native(1) == "1"
    assert to_native([1]) == "[1]"
    assert to_native({"a": [1]}) == '{"a": [1]}'
    assert to_native(to_bytes(u"ü", errors='surrogate_or_replace')) == "\\xfc"
    assert to_native(to_bytes(u"ü", errors='surrogate_or_replace'), nonstring='passthru') == u"\xfc"
    assert to_native(to_bytes(u"ü", errors='surrogate_or_replace'), nonstring='strict') == "\\xfc"



# Generated at 2022-06-12 23:44:32.534318
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    try:
        # On python2, str() is not unicode-safe
        to_native(u'\u2019')
        assert False, "to_native for unicode input should fail on python2"
    except UnicodeEncodeError as e:
        pass

    u = u'\u2019'
    s = to_native(u, nonstring='passthru')
    assert u is s, "to_native should return the identical object if it's passed a unicode string"

    b = b'\xe2\x80\x99'
    s = to_native(b, encoding='utf-8')
    assert s == u, "to_native should return the correct unicode string"

# Generated at 2022-06-12 23:44:45.090247
# Unit test for function jsonify
def test_jsonify():
    def test_req(d, **kwargs):
        assert jsonify(d, **kwargs) == json.dumps(d, **kwargs)

    test_req({})
    test_req(dict(a=1, b=2))
    test_req(dict(a=1, b=2, c=dict(a=1, b=2)))

    # Test nested container_to_text
    test_req(dict(a=1, b=2, c=dict(a=1, b=dict(a=1, b=dict(a=1, b=2)))))

# Generated at 2022-06-12 23:44:57.034063
# Unit test for function to_bytes
def test_to_bytes():
    """
    This test is more complex than most of the others.  We'll do what we can
    to not assume that the current locale is utf-8.
    """
    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes('foo', 'latin-1') == b'foo'
    assert to_bytes(u'foo', 'latin-1') == b'foo'
    assert to_bytes('fòô') == b'f\xc3\xb2\xc3\xb4'
    assert to_bytes(u'fòô') == b'f\xc3\xb2\xc3\xb4'

# Generated at 2022-06-12 23:45:23.240402
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native('123') == '123'
    assert to_native(u'123') == '123'
    assert to_native(b'123') == '123'
    assert to_native(bytearray(b'123')) == '123'
    assert to_native(None) == ''
    assert to_native(True) == 'True'
    assert to_native(False) == 'False'
    assert to_native(int(123)) == '123'
    assert to_native(float(123)) == '123.0'
    assert to_native(datetime.datetime(2017,1,1)) == '2017-01-01 00:00:00'

# Generated at 2022-06-12 23:45:29.647952
# Unit test for function jsonify
def test_jsonify():
    test_data = {'a': 'b', u'в': u'д', u'日本語': u'にほんご', 2: 'c', 'list': ['tuple', (1, 2, 3), 'set', set([4, 5, 6]), datetime.datetime(2013, 7, 25, 12, 45, 38)], 'b': 'd'}
    test_json = jsonify(test_data)
    assert json.loads(test_json) == test_data



# Generated at 2022-06-12 23:45:39.762702
# Unit test for function jsonify
def test_jsonify():
    import ansible
    builtin_str = __builtins__['str']
    for encoding in ('utf-8', 'latin-1'):
        # check flat list
        str =  u"Hello!\xbc"
        data = [builtin_str(str, encoding)]
        assert json.loads(jsonify(data)) == data
        # check nested list
        data = [builtin_str(str, encoding), data]
        assert json.loads(jsonify(data)) == data
        # check flat dict
        data = {builtin_str(str, encoding): str}
        assert json.loads(jsonify(data)) == data
        # check nested dict
        data = {builtin_str(str, encoding): {builtin_str(str, encoding): str, 'inner_list': data}}
        assert json.loads

# Generated at 2022-06-12 23:45:50.414761
# Unit test for function to_native
def test_to_native():
    def test_with_str(str_):
        if PY3:
            first = str(str_)
        else:
            first = str(str_).encode('utf-8')
        assert(to_bytes(str_) == first)
        assert(to_text(str_) == str(str_))

    test_with_str('aaa')
    test_with_str('ЯЯЯ')

    def test_with_bytes(byte_str):
        assert(to_bytes(byte_str) == byte_str)
        if PY3:
            assert(to_text(byte_str) == byte_str.decode('utf-8'))
        else:
            assert(to_text(byte_str) == byte_str)
    test_with_bytes(b'aaa')


# Generated at 2022-06-12 23:45:57.032976
# Unit test for function to_bytes
def test_to_bytes():
    # Test surrogateescape when possible
    if HAS_SURROGATEESCAPE:
        byte_string_1 = to_bytes('\uDC00\uDC01', errors='surrogate_then_replace')
        assert byte_string_1 == b'\xED\xB0\x80\xED\xB0\x81'
        byte_string_2 = to_bytes('\uDC00\uDC01', errors='surrogate_or_replace')
        assert byte_string_2 == b'\xED\xB0\x80\xED\xB0\x81'

    # test_nonstring_passthru
    class FailRepr(object):
        def __repr__(self):
            raise Exception('I am the evil sentinel')

    obj = FailRepr()

# Generated at 2022-06-12 23:46:09.092184
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native

    # Test the input for non-string, non-bytes data
    test_input_non_str = [
        {'dict': {'key': 'value'}},
        {'list': ['item1', 'item2']},
        {'set': {'item1', 'item2'}}
    ]

    for data in test_input_non_str:
        for key, value in iteritems(data):
            if isinstance(value, (list, set)):
                assert value == to_native(value)
            else:
                assert json.loads(to_native(value)) == value
    # Test the input for non-string, non-bytes data

# Generated at 2022-06-12 23:46:17.170129
# Unit test for function jsonify
def test_jsonify():
    assert jsonify([u'öäü', u'ß']) == u'["öäü", "ß"]'
    assert jsonify([u'öäü', u'ß'], ensure_ascii=False) == u'["öäü", "ß"]'
    assert jsonify({u'öäü': u'ß'}) == u'{"öäü": "ß"}'
    assert jsonify({u'öäü': u'ß'}, ensure_ascii=False) == u'{"öäü": "ß"}'
    assert u'\u2713' in jsonify({u'msg': {u'ä': u'\u2713'}})

# Generated at 2022-06-12 23:46:24.180252
# Unit test for function jsonify
def test_jsonify():
    data = [{'a': 'b', u'c': u'\u20ac', 'd': {u'e': u'f'}}]
    ret = jsonify(data)
    assert isinstance(ret, text_type), 'return value should be text'
    assert ret == u'[{"a": "b", "c": "\\u20ac", "d": {"e": "f"}}]', 'jsonify encodes data incorrectly'



# Generated at 2022-06-12 23:46:28.225015
# Unit test for function to_native
def test_to_native():
    assert to_native(u'foo') == 'foo'
    assert to_native('foo') == 'foo'
    assert to_native(b'foo') == 'foo'
    assert to_native(1) == '1'
    assert to_native(True) == 'True'



# Generated at 2022-06-12 23:46:38.334648
# Unit test for function jsonify
def test_jsonify():
    class TimeObj(object):
        def __init__(self, time):
            self.time = time
        def __str__(self):
            return self.time
    def test_true(value):
        assert value is True

# Generated at 2022-06-12 23:47:02.632639
# Unit test for function jsonify
def test_jsonify():
    class Foo(object):
        def __repr__(self):
            return u"{u'\xe9': u'\xe9'}"

    data = {u"foo": [u"bar", u"baz"], u"\xe9": [u"\xe9"], u"foo2": [5, 6],
            u"foo3": {u"foo": u"bar"}, u"foo4": Foo(),
            u"foo5": set([u"a", u"b"])}

    result = jsonify(data)

# Generated at 2022-06-12 23:47:11.572411
# Unit test for function to_native
def test_to_native():
    assert to_native(u'text') == u'text'
    assert to_native(b'bytes') == b'bytes'
    assert to_native([u'unicode', b'bytes']) == [u'unicode', b'bytes']
    assert to_native(['text', b'bytes']) == [u'text', b'bytes']
    assert to_native(('text', b'bytes')) == (u'text', b'bytes')
    assert to_native({u'unicode': 'text', b'bytes': b'bytes'}) == {u'unicode': u'text', b'bytes': b'bytes'}
    assert to_native({u'unicode': u'text', 'text': b'bytes'}) == {u'unicode': u'text', u'text': b'bytes'}
   

# Generated at 2022-06-12 23:47:14.792335
# Unit test for function jsonify
def test_jsonify():
    dict_data = {'k1': 'v1'}
    list_data = ['k1', 'v1']
    set_data = set(['k1', 'v1'])
    for data in (dict_data, list_data, set_data):
        jsonify(data)



# Generated at 2022-06-12 23:47:22.832026
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native

    expect = '\u1234'
    assert to_native(text_type(expect)) == expect

    expect = b'\xe1\x88\xb4'
    assert to_native(expect) == expect.decode('utf-8')

    assert to_native(1) == repr(1)

    assert to_native(datetime.datetime.utcnow()) == repr(datetime.datetime.utcnow())

    # ensure we can convert dicts to native types
    assert to_native({}) == '{}'



# Generated at 2022-06-12 23:47:25.785675
# Unit test for function jsonify
def test_jsonify():
    for value in (1, "two", b"byte", u"unicode"):
        assert jsonify(value) == json.dumps(value)



# Generated at 2022-06-12 23:47:29.939671
# Unit test for function to_native
def test_to_native():
    assert to_native(u'\u6240\u6709') == u'所有'
    assert to_native(b'\xe6\x89\x80\xe6\x9c\x89') == u'所有'



# Generated at 2022-06-12 23:47:36.626730
# Unit test for function jsonify
def test_jsonify():
  utf8_data = dict(name=u'Simpl\u00edci\u00f3n', age=37)
  latin1_data = dict(name=u'H\xe9l\xe8ne', age=37)
  try:
    assert jsonify(utf8_data) == json.dumps(utf8_data, encoding="utf-8")
    assert jsonify(latin1_data) == json.dumps(latin1_data, encoding="latin-1")
  except AssertionError:
    print(jsonify(utf8_data))
    print(json.dumps(utf8_data, encoding="utf-8"))



# Generated at 2022-06-12 23:47:45.135598
# Unit test for function to_native
def test_to_native():
    assert to_native(u'\u2713') == '\\xe2\\x9c\\x93'
    assert to_native(u'\xe9') == '\\xc3\\xa9'
    assert to_native(u'\u20ac') == '\\xe2\\x82\\xac'
    assert to_native(u'\U0001f4a9') == '\\xf0\\x9f\\x92\\xa9'
    assert to_native(b'\xe2\x9c\x93') == '\\xe2\\x9c\\x93'
    assert to_native(b'\xc3\xa9') == '\\xc3\\xa9'
    assert to_native(b'\xe2\x82\xac') == '\\xe2\\x82\\xac'

# Generated at 2022-06-12 23:47:50.753099
# Unit test for function to_native
def test_to_native():

    # Ensure that we can encode to utf-8
    s = '\xe4\xf6\xfc\xc4\xd6\xdc\xdf'
    expected = b'\xc3\xa4\xc3\xb6\xc3\xbc\xc3\x84\xc3\x96\xc3\x9c\xc3\x9f'
    assert to_bytes(s) == expected

    # Ensure that we can encode to latin-1
    expected = b'\xe4\xf6\xfc\xc4\xd6\xdc\xdf'
    assert to_bytes(s, encoding='latin-1') == expected

    # Ensure that we properly do surrogates
    s = '\udcff'
    expected = b'\xed\xb3\xbf'

# Generated at 2022-06-12 23:48:02.405473
# Unit test for function jsonify
def test_jsonify():

    class Foo(object):
        def __init__(self, s):
            self.s = s
        def __repr__(self):
            return "Foo(%s)" % self.s

    # Test encoding
    err_msg = ("Cannot serialize b'foo' (type %r). It must be converted to unicode")
    try:
        jsonify(b"foo")
    except TypeError as e:
        assert to_bytes(err_msg) in to_bytes(e)
    else:
        raise AssertionError("Unicode serialization error not caught")

    # Test handling non-serializable items
    err_msg = "Cannot json serialize %s"
    try:
        jsonify(Foo("bar"))
    except TypeError as e:
        assert to_bytes(err_msg)
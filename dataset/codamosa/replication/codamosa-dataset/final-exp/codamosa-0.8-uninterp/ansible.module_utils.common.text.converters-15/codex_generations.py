

# Generated at 2022-06-12 23:38:25.328334
# Unit test for function to_bytes
def test_to_bytes():
    pass

# Generated at 2022-06-12 23:38:36.493269
# Unit test for function to_native
def test_to_native():
    assert to_native(None) is None
    assert to_native(1) == 1
    assert to_native(True) is True
    assert isinstance(to_native(to_text('foo')), text_type)
    assert isinstance(to_native(to_bytes('foo')), text_type)
    assert to_native(u'foo') == u'foo'
    assert to_native('foo') == u'foo'
    now = datetime.datetime.utcnow()
    assert to_native(now) == str(now)
    assert to_native(set((1, 2, 3))) == set([1, 2, 3])
    assert to_native(dict(one=1)) == dict(one=1)
    assert to_native(1, errors='strict') == 1

# Generated at 2022-06-12 23:38:48.623838
# Unit test for function to_native
def test_to_native():
    assert to_native(0) == 0
    assert to_native(1) == 1
    assert to_native(2.0) == 2.0
    assert to_native(True) == True
    assert to_native(False) == False
    assert to_native(None) == None

    unicode_str = to_text(b'unicode \xe2\x8a\xaf', errors='surrogate_or_replace')
    assert to_native(unicode_str) == unicode_str

    assert to_native(b'bytes') == b'bytes'
    assert to_native(u'unicode') == u'unicode'
    assert to_native(u'\xbd') == u'\xbd'

    # this is different from the behavior of to_text and to_bytes
    # which use surrogate

# Generated at 2022-06-12 23:38:59.232842
# Unit test for function to_bytes
def test_to_bytes():
    # We can't use py3bytes because that would be recursive
    def py3_byte_string(value):
        if isinstance(value, text_type):
            return value.encode('utf-8')
        return value

    # We can't use to_text because that would be recursive
    def to_text_string(value, encoding=None, errors=None):
        if isinstance(value, binary_type):
            return value.decode(encoding, errors)
        return value

    # Python2 requires the str call to make the boolean a basestring
    if PY3:
        assert to_bytes(True, 'ascii') == b'True'
    else:
        assert to_bytes(str(True), 'ascii') == b'True'

    assert to_bytes(None, 'ascii')

# Generated at 2022-06-12 23:39:09.748697
# Unit test for function to_native
def test_to_native():
    def env_error(encoding):
        if HAS_SURROGATEESCAPE:
            return 'surrogateescape'
        else:
            return 'replace'


# Generated at 2022-06-12 23:39:17.558770
# Unit test for function to_native
def test_to_native():
    assert to_native(b'\xc5\x93') == text_type('\xc5\x93', 'latin-1')
    assert to_native('\xe7\x8a\xac') == text_type('\xe7\x8a\xac')
    assert to_native(b'\xe7\x8a\xac') == text_type('\xe7\x8a\xac', 'utf-8')
    assert to_native(text_type('\xe7\x8a\xac')) == text_type('\xe7\x8a\xac')



# Generated at 2022-06-12 23:39:28.681450
# Unit test for function to_native
def test_to_native():
    unicode_string = u'ℝεα∂ Διsקℓαιмεя: Ansible modules are standalone scripts'
    byte_string = unicode_string.encode('utf-8')
    assert to_native(unicode_string, encoding='utf-8') == unicode_string
    assert to_native(byte_string, encoding='utf-8') == byte_string
    with pytest.raises(UnicodeError):
        to_native(byte_string, encoding='ascii')

    assert to_native(
        byte_string, encoding='ascii', errors='surrogateescape') == unicode_string
    assert to_native(
        byte_string, encoding='ascii', errors='surrogate_or_strict') == unicode_string
    assert to_

# Generated at 2022-06-12 23:39:38.640611
# Unit test for function to_bytes
def test_to_bytes():
    '''
    Unit test for to_bytes
    '''
    assert to_bytes('some text',
                    encoding='utf-8',
                    errors='surrogateescape') == b'some text'
    assert to_bytes('some text',
                    encoding='ascii',
                    errors='surrogateescape') == b'some text'
    assert to_bytes('some text',
                    encoding='ascii',
                    errors='surrogate_or_replace') == b'some text'
    assert to_bytes('some text',
                    encoding='ascii',
                    errors='surrogate_or_strict') == b'some text'
    assert to_bytes('some text',
                    encoding='ascii',
                    errors='surrogate_then_replace') == b'some text'


# Generated at 2022-06-12 23:39:45.433152
# Unit test for function to_bytes
def test_to_bytes():
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-statements
    if not PY3:
        raise AssertionError('python2 to_bytes tests can only be run on python2')

    # Make sure that py2 handles surrogates correctly
    # In py3 this is fixed as part of the codecs module
    def surrogateescape2_handler(error):
        """Handle surrogate escapes"""
        if error.reason == 'surrogates not allowed':
            del error.reason
            return int(error.object[error.start:error.end], 16).to_bytes(2, 'little', signed=True)
        error.start += 1
        return u'\ufffd'


# Generated at 2022-06-12 23:39:55.989135
# Unit test for function jsonify
def test_jsonify():
    data = {"key": "value", "list": [1, 2, 3], "dict": {"a": "A", "b": "b"}}
    assert jsonify(data) == '{"key": "value", "list": [1, 2, 3], "dict": {"a": "A", "b": "b"}}'
    data = {"key": "value", "list": [1, 2, 3], "dict": {"a": "A", "b": "b"}, "set": Set([1, 2, 3])}
    assert jsonify(data) == '{"key": "value", "list": [1, 2, 3], "dict": {"a": "A", "b": "b"}, "set": [1, 2, 3]}'

# Generated at 2022-06-12 23:40:15.046917
# Unit test for function jsonify
def test_jsonify():
    import sys

    import pytest

    if sys.version_info < (2, 7):
        pytest.skip("json.dumps() kwargs not supported in python-2.6")

    try:
        import simplejson
    except ImportError:
        pytest.skip("simplejson not installed")

    # In python3, the simplejson module in the standard library
    # doesn't support the encoding parameter
    if (not hasattr(simplejson, '__version__') or
            (hasattr(simplejson, '__version__') and simplejson.__version__ == '2.1.6')):
        pytest.skip("simplejson does not support encoding in python3")

    # Old simplejson module does not support encoding keyword

# Generated at 2022-06-12 23:40:23.504548
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic

    assert to_bytes('x') == b'x'
    assert to_bytes('\xf8') == b'\xc3\xb8'
    assert to_bytes('\xf8', errors='surrogate_then_replace') == b'\xe2\x80\xa0'

    assert to_text(b'x') == 'x'
    assert to_text(b'\xc3\xb8') == '\xf8'
    assert to_text(b'\xe2\x80\xa0', errors='surrogate_then_replace') == '\ufffd'

    mgr = basic.AnsibleModule(argument_spec={'s': dict(type='str')})
    assert mgr.json

# Generated at 2022-06-12 23:40:36.094584
# Unit test for function jsonify
def test_jsonify():
    # Test with a valid unicode
    data = {u"spécial": u"caractères", u"simple": u"test"}
    assert jsonify(data) == '{"simple": "test", "sp\u00e9cial": "caract\u00e8res"}'

    # Text data are not handled the same depending on Python version.
    # On Python2, the default encoding used to decode bytes is ASCII,
    # while it is UTF-8 on Python3.
    if PY3:
        data = {u"spécial": b"caract\xc3\xa8res", u"simple": b"test"}
        assert jsonify(data) == '{"simple": "test", "sp\u00e9cial": "caract\u00e8res"}'

# Generated at 2022-06-12 23:40:47.197640
# Unit test for function jsonify
def test_jsonify():
    # text is utf-8
    text = '\u6771\u4eac'
    if PY3:
        assert jsonify(to_native(text)) == '"\u6771\u4eac"' 
    else:
        assert jsonify(to_native(text)) == '"\\u6771\\u4eac"'

    # text is latin-1
    text = u'\u6771\u4eac'.encode('latin-1')
    if PY3:
        assert jsonify(to_native(text)) == '"\\u6771\\u4eac"'
    else:
        assert jsonify(to_native(text)) == '"\\u6771\\u4eac"'

    # text is not unicode

# Generated at 2022-06-12 23:40:58.117466
# Unit test for function to_bytes
def test_to_bytes():
    # Raw strings should be returned as-is
    assert to_bytes(b'raw string') == b'raw string'

    # Unicode strings should be encoded
    assert to_bytes('\u00f1') == b'\xc3\xb1'

    # Non-string objects should be transformed to strings and then encoded
    assert to_bytes({'a': 1}) == b"{'a': 1}"
    assert to_bytes(b'\xff'.decode('latin-1')) == b'\xc3\xbf'

    # We shouldn't be able to create unexpected types by using nonstring
    assert isinstance(to_bytes(1, nonstring='passthru'), int)
    assert isinstance(to_bytes(b'raw string', nonstring='passthru'), binary_type)

# Generated at 2022-06-12 23:41:08.245150
# Unit test for function to_bytes
def test_to_bytes():
    # Test that if we start with a byte string, we don't change it
    # Test that if the byte string has surrogates, we don't change it
    bs = u'<value>\uD83D\uDCA9</value>'.encode('utf-8', 'surrogateescape')
    assert to_bytes(bs) == bs

    # Test that if we're given a text string with good encoding, we use it
    s = u'<value>\uD83D\uDCA9</value>'
    assert to_bytes(s) == b'<value>\xed\xa0\xbd\xed\xb2\xa9</value>'

# Generated at 2022-06-12 23:41:16.011850
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"key": "value"}) == '{"key": "value"}'
    assert jsonify({"key": u"value"}) == '{"key": "value"}'
    assert u'{"key": "value"}' == to_text(jsonify({"key": u"value"}))
    assert jsonify([{"key": u"value"}]) == '[{"key": "value"}]'
    assert jsonify([{"key": u"value"}]) == '[{"key": "value"}]'
    assert jsonify([{"key": u"value"}]) == '[{"key": "value"}]'
    assert u'[{"key": "value"}]' == to_text(jsonify([{"key": u"value"}]))

# Generated at 2022-06-12 23:41:27.803448
# Unit test for function to_bytes
def test_to_bytes():
    test_cases = [
        ({}, b'{}'),
        ({1: 2}, b"{1: 2}"),
        ((1, 2), b'(1, 2)'),
        (Set([1, 2]), b'{1, 2}'),
        (1, b'1'),
        (1.0, b'1.0'),
        (None, b'None'),
        (b'\xF0\x9F\x98\x8D', b'\xF0\x9F\x98\x8D'),
        (u'\U0001F40D', b'\xF0\x9F\x90\x8D'),
    ]

    assert to_bytes(u'\u2019') == b"\xe2\x80\x99"


# Generated at 2022-06-12 23:41:31.836838
# Unit test for function to_native
def test_to_native():
    assert to_native('foo') == b'foo'
    assert to_native(b'foo') == b'foo'
    assert to_native(u'foo') == b'foo'


# Generated at 2022-06-12 23:41:41.941893
# Unit test for function to_bytes
def test_to_bytes():
    # namedtuple has a __str__ that doesn't return a text string in Python 2
    from collections import namedtuple
    try:
        str(namedtuple('Foo', 'foo'))
    except TypeError:
        nt_str = repr
    else:
        nt_str = str
    nt_instance = namedtuple('Foo', 'foo')(u'\N{SNOWMAN}')

    # We can't use b'...' literal syntax in Python2 because it'll be converted
    # to the native str which may be bytes or text.  To make sure we use
    # the Python3 bytes literal syntax consistently, we use to_bytes.  This
    # will make sure we're always checking bytes on Python3 as well where b''
    # is a byte string already.

# Generated at 2022-06-12 23:42:00.406350
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'foo', errors='strict') == b'foo'
    assert to_bytes(u'foo', errors='surrogate_or_replace') == b'foo'
    assert to_bytes(u'foo', errors='surrogate_or_strict') == b'foo'
    assert to_bytes(u'foo\udcff') == b'foo?'
    assert to_bytes(u'foo\udcff', errors='surrogate_or_replace') == b'foo?'
    assert to_bytes(u'foo\udcff', errors='surrogate_then_replace') == b'foo\ufffd'

# Generated at 2022-06-12 23:42:10.628168
# Unit test for function to_native
def test_to_native():
    # Default usage
    assert to_native(u'\u2713') == '\xe2\x9c\x93'
    assert to_native(b'\xe2\x9c\x93') == '\xe2\x9c\x93'
    # Default usage with 'replace' error handler
    assert to_native(u'\u2716') == '\ufffd'
    assert to_native(b'\xff') == '\ufffd'
    # Default usage with 'strict' error handler
    assert to_native(u'\u2713', errors='strict') == '\xe2\x9c\x93'
    assert to_native(b'\xe2\x9c\x93', errors='strict') == '\xe2\x9c\x93'
    # Default

# Generated at 2022-06-12 23:42:19.105793
# Unit test for function jsonify
def test_jsonify():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestJsonify(unittest.TestCase):

        @patch('ansible.module_utils._text.json')
        def test_jsonify_encoding_failure(self, mock_json):
            mock_json.dumps = Mock(side_effect=TypeError)
            mock_json.dumps().decode.side_effect = UnicodeDecodeError
            test_dict = dict(test=u'test')
            self.assertRaises(UnicodeError, jsonify, test_dict)

        def test_jsonify(self):
            test_str = u'test'
            test_dict = dict(test=test_str)

# Generated at 2022-06-12 23:42:27.029331
# Unit test for function jsonify
def test_jsonify():
    # This function test the function jsonify.
    # It first tests a simple case, data is jsonifiable and there is no problem
    # with encoding. Then tests when data is not jsonifiable and encoding is
    # default and last tests when data is not jsonifiable and encoding is
    # changed.

    # test for simple case, first create a test data set
    test_data = {
        "name":"Ansible",
        "Coffee?":"No, beer please."
    }
    # then try to jsonify it
    try:
        test_data_json = jsonify(test_data)
    # if the jsonify does not work, the test fails
    except Exception as e:
        print("test_jsonify failed, jsonify does not work.")
        print("error:"+str(e))

# Generated at 2022-06-12 23:42:37.869829
# Unit test for function to_bytes
def test_to_bytes():
    # Need to use a codec that will encode '\x80' with a multi-byte sequence
    # so we have a non-BMP character
    encoding = 'utf-16-be'

    # Ensure surrogates are only introduced when asked
    assert u'\uDCFF'.encode(encoding, 'surrogateescape') == b'\xdc\xff'
    assert u'\uDCFF'.encode(encoding, 'strict') == b'\xff\xfd'
    assert u'\uDCFF'.encode(encoding, 'ignore') == b''
    assert u'\uDCFF'.encode(encoding, 'replace') == b'?'

    # Encoded strings
    assert to_bytes(b'foo', encoding) == b'foo'

# Generated at 2022-06-12 23:42:42.239279
# Unit test for function jsonify
def test_jsonify():
    new_data = jsonify({'key': {'check': 'test'}})
    print(new_data)
    assert json.loads(new_data) == {'key': {'check': 'test'}}



# Generated at 2022-06-12 23:42:44.326583
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'key': 'value'}) == '{"key": "value"}'
    assert jsonify("value") == '"value"'



# Generated at 2022-06-12 23:42:54.147266
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import _json_compat as json_compat
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    assert jsonify({"str": "str"}) == '{"str": "str"}'
    assert jsonify({"unicode": u"Iñtërnâtiônàlizætiøn☃💩"}) == '{"unicode": "I\\u00f1t\\u00ebrn\\u00e2ti\\u00f4n\\u00e0liz\\u00e6ti\\u00f8n\\u2603\\ud83d\\udca9"}'

# Generated at 2022-06-12 23:42:59.752957
# Unit test for function to_native
def test_to_native():
    assert to_native(u'foobar') == u'foobar'
    assert to_native('foobar') == u'foobar'

    # using ASCII range to avoid possibility of UTF8 encoding issues.
    assert to_native(b'\x00\x01\x02\x7f') == b'\x00\x01\x02\x7f'
    assert to_native(bytearray([0, 1, 2, 127])) == b'\x00\x01\x02\x7f'

    # Test for bug: https://github.com/ansible/ansible/issues/9303
    assert to_native(datetime.datetime(2014, 4, 29, 11, 38, 39)) == u'2014-04-29 11:38:39'

# Generated at 2022-06-12 23:43:10.639466
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils.six import text_type
    import datetime
    # Test for code in function
    assert isinstance(jsonify({'foo': {'bar': text_type('foo')}}, sort_keys=True, indent=2), text_type)
    assert isinstance(jsonify({'foo': to_bytes('foo')}, sort_keys=True, indent=2), text_type)
    assert isinstance(jsonify({'foo': to_bytes('foo')}, sort_keys=True, indent=2), text_type)
    assert isinstance(jsonify({'foo': text_type('foo')}, sort_keys=True, indent=2), text_type)
    assert isinstance(jsonify({'foo': {'bar': text_type('foo')}}, sort_keys=True), text_type)


# Generated at 2022-06-12 23:43:30.680558
# Unit test for function jsonify
def test_jsonify():
    json_object = {"a": 1, "b": "test", "c": u"\x80"}
    json_string = jsonify(json_object)
    assert isinstance(json_string, text_type)
    assert json.loads(json_string) == container_to_text(json_object)



# Generated at 2022-06-12 23:43:31.236330
# Unit test for function to_bytes
def test_to_bytes():
    pass



# Generated at 2022-06-12 23:43:34.693137
# Unit test for function jsonify
def test_jsonify():
    data = u'some unicode string'
    json_data = jsonify(data)
    assert isinstance(json_data, text_type)
    assert u'some unicode string' == json.loads(json_data)



# Generated at 2022-06-12 23:43:38.995184
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': to_bytes('\xe0')}) == '{"a": "\\u00e0"}'
    assert jsonify({'a': to_bytes('\xe0')}, encoding="latin-1") == '{"a": "\\xe0"}'
    assert jsonify({'a': to_bytes('\xe0')}, encoding="ascii")



# Generated at 2022-06-12 23:43:49.302541
# Unit test for function to_bytes
def test_to_bytes():
    def _test_str(str, expected, encoding='utf-8', errors='surrogateescpe'):
        actual = to_bytes(str, encoding=encoding, errors=errors)
        assert actual == expected

    if HAS_SURROGATEESCAPE:
        # Test strings that are already valid in the encoding
        _test_str(u'\x00\xbd', b'\x00\xbd')
        _test_str(u'\x00\xc3\xbf', b'\x00\xc3\xbf')
        _test_str(u'\x00\xc3\xae', b'\x00\xc3\xae')
        _test_str(u'\x00\xc3\xbe', b'\x00\xc3\xbe')
        _test_

# Generated at 2022-06-12 23:43:54.004128
# Unit test for function jsonify
def test_jsonify():
    foo = 'foo'
    assert jsonify(foo) == json.dumps(foo)
    assert jsonify({'a': 1, u'b': 'foo'}) == json.dumps({u'a': 1, u'b': 'foo'})
    assert jsonify({b'a': 1, b'b': 'foo'}) == json.dumps({u'a': 1, u'b': u'foo'})


# Generated at 2022-06-12 23:43:58.953248
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_text
    assert jsonify({"a": to_text("b")}) == '{"a": "b"}'
    assert jsonify({"a": [to_text("b"), 1]}) == '{"a": ["b", 1]}'



# Generated at 2022-06-12 23:44:02.109111
# Unit test for function jsonify
def test_jsonify():
    jsonify(u'吴', ensure_ascii=False)



# Generated at 2022-06-12 23:44:06.631429
# Unit test for function jsonify
def test_jsonify():
    class Set(set):
        pass

    data = {'foo': Set([2, 3, 4])}

    result = {u'foo': [2, 3, 4]}
    assert jsonify(data) == json.dumps(result)

    assert '"foo": 2' in jsonify({"foo": 2}, sort_keys=True)



# Generated at 2022-06-12 23:44:17.228217
# Unit test for function to_bytes
def test_to_bytes():
    '''
    This is an autogenerated function to test the function to_bytes.
    '''
    import sys
    import tempfile
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.six import PY3

    def _to_bytes_assert(obj, expected):
        # we need to import here for test collection
        from ansible.module_utils.common._collections_compat import MutableMapping
        from ansible.module_utils.six import PY3

        result = to_bytes(obj)

        if isinstance(obj, MutableMapping):
            assert result == expected, 'Got %r, expected %r' % (result, expected)

# Generated at 2022-06-12 23:44:37.341270
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('{"foo": "bar"}')
    assert jsonify(b'{"foo": "bar"}')
    assert jsonify(u'{"foo": "bar"}')
    assert jsonify(u'{"foo": "b\u1234r"}')
    assert jsonify(u'{"foo": "b\u1234r"}'.encode('utf-16'))
    assert jsonify(u'{"foo": "b\u1234r"}'.encode('utf-16').decode('utf-16'))
    try:
        jsonify('{"foo": "b\xa3r"}')
        assert False, "should have raised UnicodeDecodeError"
    except UnicodeDecodeError:
        pass
    assert jsonify('{"foo": "b\xa3r"}'.encode('latin-1'))

# Generated at 2022-06-12 23:44:47.233458
# Unit test for function to_bytes
def test_to_bytes():
    # These values were taken from the example in http://www.unicode.org/versions/corrigendum1.html
    original = codecs.decode('ed ab be c0', 'hex')

    # Text with surrogates
    expected = original.encode('utf-8', 'surrogateescape')

    # Text without surrogates
    expected_nosurrogates = codecs.decode('ed ab be ef bf bd', 'hex').encode('utf-8')

    # Same surrogate string as an encoded byte string
    expected_bytes = codecs.decode('ed ba be c0', 'hex')

    encoded = to_bytes(original)
    assert encoded == expected
    assert isinstance(encoded, binary_type)
    assert not isinstance(encoded, text_type)

    # Same string but no surrogates


# Generated at 2022-06-12 23:44:58.344289
# Unit test for function to_bytes
def test_to_bytes():
    # This test just checks that to_bytes(text_type) works in Python2 and Python3
    def_errors = to_bytes('abc', errors='surrogate_then_replace')
    assert(isinstance(def_errors, binary_type))
    assert(def_errors == b'abc')

    utf8_errors = to_bytes('abc', 'utf-8', errors='surrogate_then_replace')
    assert(isinstance(utf8_errors, binary_type))
    assert(utf8_errors == b'abc')

    # Make sure surrogates don't get encoded in surrogates
    utf8_errors_surrogate = to_bytes('\uDC80', 'utf-8', errors='surrogate_then_replace')
    assert(isinstance(utf8_errors_surrogate, binary_type))

# Generated at 2022-06-12 23:45:07.711247
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'

    # Note: We're using decode('raw_unicode_escape') instead of u'foo' because
    # u'foo' will automatically perform unicode normalization which will change
    # the string from 'foo' to u'foo' internally.  We don't have this problem
    # with decode because it takes the \u literal values.
    assert to_bytes(u'f\u00f6\u00f6'.encode('raw_unicode_escape').decode('utf-8'),
                    encoding='ascii', errors='surrogateescape') == b'foo'

# Generated at 2022-06-12 23:45:15.898509
# Unit test for function to_native
def test_to_native():
    assert to_text(b'string') == u'string'
    assert to_text(b'\xe3\x81\x82') == u'\u3042'
    assert to_text(u'string') == u'string'
    assert to_text(u'\u3042') == u'\u3042'
    assert to_text(u'\u3042', errors='surrogate_or_replace') == u'\u3042'
    assert to_text(u'\u3042', errors='surrogate_or_strict') == u'\u3042'
    # This tests surrogate_or_replace.  If surrogateescape is registered we
    # probably don't want to test it.  If we do, we should mock it out.

# Generated at 2022-06-12 23:45:27.821082
# Unit test for function to_bytes
def test_to_bytes():
    # Invalid values for nonstring
    for nonstring in ('invalid', 23):
        try:
            to_bytes(object(), nonstring=nonstring)
        except TypeError:
            pass
        else:
            raise AssertionError('to_bytes failed to raise TypeError with invalid nonstring value %r' % nonstring)

    # Invalid value for errors
    for errors in ('invalid', object()):
        try:
            to_bytes(object(), errors=errors)
        except TypeError:
            pass
        else:
            raise AssertionError('to_bytes failed to raise TypeError with invalid errors value %r' % errors)

    # Invalid value for encoding
    for encoding in ('invalid', object()):
        try:
            to_bytes(object(), encoding=encoding)
        except TypeError:
            pass
       

# Generated at 2022-06-12 23:45:32.785055
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    obj = set(["foo", "bar"])

    jsonified = jsonify(obj, sort_keys=True)
    result = json.loads(jsonified)
    module.exit_json(msg="set jsonification succeeded", changes=result)


# Generated at 2022-06-12 23:45:41.740382
# Unit test for function jsonify
def test_jsonify():
    # Make sure that jsonify does not mutate data
    try:
        import simplejson as json
    except ImportError:
        import json
    data = {'a': 'b'}
    encoded = jsonify(data)
    assert(data['a'] == 'b')
    # Make sure that jsonify does not mutate data when called with a dict
    encoded = jsonify(data, sort_keys=True)
    assert(data['a'] == 'b')
    # Make sure that non-standard data types can be dumped
    encoded = jsonify(Set([1, 2, 3]))
    assert(encoded == '[1, 2, 3]')
    # Make sure that datetime.datetime fields are properly dumped
    now = datetime.datetime.now()
    encoded = jsonify(now)

# Generated at 2022-06-12 23:45:52.863904
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six.moves import StringIO

    # First test that the default works for valid unicode
    if PY3:
        # Every text string is unicode in Python 3
        assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
        assert to_bytes(u'\u1234', errors='surrogate_or_strict') == b'\xe1\x88\xb4'
        assert to_bytes(u'\u1234', errors='surrogate_or_replace') == b'\xe1\x88\xb4'
        assert to_bytes(u'\u1234', errors='surrogate_then_replace') == b'\xe1\x88\xb4'

# Generated at 2022-06-12 23:46:04.336766
# Unit test for function to_bytes
def test_to_bytes():
    import sys

    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'foo'.encode('utf-16')) == b'foo'
    assert to_bytes(u'føo'.encode('utf-16')) == b'f\xc3\xb8o'
    assert to_bytes(u'føo') == b'f\xc3\xb8o'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'f\xc3\xb8o') == b'f\xc3\xb8o'
    assert to_bytes(u'Ÿ'.encode('latin-1')) == b'\x9f'

# Generated at 2022-06-12 23:46:47.081414
# Unit test for function to_native
def test_to_native():
    """
    Test for function to_native()
    """

    assert to_native("", errors='surrogate_or_strict') == ""
    assert to_native("", errors='surrogate_or_replace') == ""
    assert to_native("", errors='surrogate_then_replace') == ""
    assert to_native("", nonstring='strict') == ""
    assert to_native("", nonstring='empty') == ""
    assert to_native("", nonstring='passthru') == ""
    assert to_native("", nonstring='simplerepr') == ""
    assert to_native(None, nonstring='strict') == ""
    assert to_native(None, nonstring='empty') == ""
    assert to_native(None, nonstring='passthru') == ""

# Generated at 2022-06-12 23:46:57.615624
# Unit test for function to_native
def test_to_native():
    # pylint: disable=redefined-outer-name,too-many-branches,too-many-statements
    '''
    Test to native method,it can convert different type of string to native
    :return:
    '''
    def assert_to_native(args):
        # pylint: disable=too-many-function-args
        '''
        assert function to_native,it can convert different type of string to
        native
        :param args:
        :return:
        '''
        assert isinstance(to_native(args, nonstring=None, terse=True),
                          type(args))
    # pylint: disable=line-too-long
    # unicode string
    assert_to_native(u'中文')
    # bytes string

# Generated at 2022-06-12 23:47:02.279332
# Unit test for function to_native
def test_to_native():
    assert to_native(u'unicode', 'utf-8') == u'unicode'
    assert to_native('str', 'utf-8') == 'str'
    assert to_native(b'bytes', 'utf-8') == u'bytes'



# Generated at 2022-06-12 23:47:11.384342
# Unit test for function to_native
def test_to_native():
    """
    arg: value
    kwargs: {'encoding', 'errors'}
    return: str
    """
    # to_native(object)::
    assert to_native("test_str") == "test_str"
    assert to_native("test_str".encode("utf-8")) == "test_str"
    assert to_native("test_str".encode("utf-8"), "utf-8") == "test_str"
    assert to_native("test_str".encode("utf-8"), "utf-8", "strict") == "test_str"
    assert to_native("test_str".encode("utf-8"), "utf-8", "ignore") == "test_str"

# Generated at 2022-06-12 23:47:20.774767
# Unit test for function to_native
def test_to_native():
    import pytest

    assert to_native("string") is "string"
    assert to_native("string") == "string"

    if PY3:
        assert to_native(b"bytestring") == u"bytestring"
        assert to_native(b"bytestring") is not b"bytestring"
        assert to_native(b"bytestring") is not "bytestring"
        assert to_native(u"unicodestring") == u"unicodestring"
        assert to_native(u"unicodestring") is not b"unicodestring"
        assert to_native(u"unicodestring") is not "unicodestring"

        assert to_native(None) == u"None"
        assert to_native(1) == u"1"
        assert to_native

# Generated at 2022-06-12 23:47:31.490371
# Unit test for function jsonify
def test_jsonify():
    data = {"foo": "bar"}
    # If encoding is utf-8 and default=_json_encode_fallback, will be passed and return a string.
    assert isinstance(jsonify(data, encoding="utf-8"), str)
    # If encoding is utf-8 and default=_json_encode_fallback, will be passed and return a string.
    assert isinstance(jsonify(data, encoding="latin-1"), str)
    # If encoding is utf-8 and no default=_json_encode_fallback, will be passed and return a string.
    assert isinstance(json.dumps(data, encoding="utf-8"), str)
    # If encoding is utf-8 and no default=_json_encode_fallback, will be passed and return a string.

# Generated at 2022-06-12 23:47:40.107382
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils.common._collections_compat import OrderedDict
    import sys

    if PY3:
        str_type = str
    else:
        str_type = unicode

    values = [
        'some string',
        u'some\u1234 unicode',
        dict(a='b', c='d'),
        OrderedDict([('a', 'b'), ('c', 'd')]),
        [1, 2, 3, 4],
        (1, 2, 3, 4),
        True,
        False,
        42,
        42.1,
        datetime.datetime.now(),
        bytearray(b'foo'),
        sys,
        None,
        NotImplemented,
        Ellipsis,
    ]


# Generated at 2022-06-12 23:47:47.798171
# Unit test for function to_bytes
def test_to_bytes():
    # Python3 doesn't have a .has_key method
    #assert not to_bytes.__code__.co_varnames.has_key('kwargs')
    #assert to_bytes.__defaults__ == ('utf-8', None, 'simplerepr')

    assert to_bytes(b'test') == b'test'
    # Python3 doesn't have a unicode type
    assert isinstance(to_bytes(u'test'), binary_type)

    assert to_bytes(u'test') == b'test'
    assert to_bytes(u'test', errors='strict') == b'test'
    assert to_bytes(u'test', errors='ignore') == b''
    assert to_bytes(u'test', errors='replace') == b'test'

    assert to_bytes(1) == b'1'

# Generated at 2022-06-12 23:47:55.922345
# Unit test for function to_native
def test_to_native():
    assert to_native(1) == 1
    assert to_native(b'foo') == 'foo'
    assert to_native(u'foo') == u'foo'
    assert to_native(b'foo', errors='surrogate_or_strict') == u'foo'
    assert to_native(u'foo', errors='surrogate_or_strict') == u'foo'
    assert to_native(b'foo', errors='surrogate_or_replace') == u'foo'
    assert to_native(u'foo', errors='surrogate_or_replace') == u'foo'



# Generated at 2022-06-12 23:48:01.287864
# Unit test for function jsonify
def test_jsonify():
    assert jsonify("foo") == '"foo"'
    assert jsonify("foo".encode("latin-1")) == '"foo"'
    if PY3:
        assert jsonify("foo".encode("utf-8")) == '"foo"'
    else:
        assert jsonify("foo".encode("utf-8")) == u'"foo"'


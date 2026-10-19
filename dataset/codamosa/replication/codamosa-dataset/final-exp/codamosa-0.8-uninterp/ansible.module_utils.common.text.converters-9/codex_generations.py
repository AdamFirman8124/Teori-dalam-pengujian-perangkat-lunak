

# Generated at 2022-06-12 23:38:25.548005
# Unit test for function to_native
def test_to_native():
    # Check that to_native does not change unicode objects
    assert to_native(u'7') == u'7'
    assert to_native(u'7') is not '7'
    # Check that int objects are returned as is
    assert to_native(7) == 7
    assert to_native(7) is not '7'
    # Check that to_native coerces str to unicode
    assert to_native('7') == u'7'
    assert to_native('7') is not '7'
    assert to_native('7') is not u'7'


# Generated at 2022-06-12 23:38:32.184714
# Unit test for function jsonify
def test_jsonify():
    # test on empty dict
    assert(jsonify({}) == '{}')
    # test on empty list
    assert(jsonify([]) == '[]')
    # test on string
    assert(jsonify('"abc"') == '"\\"abc\\""')
    assert(jsonify("abc") == '"abc"')
    # test on json.dumps
    assert(jsonify(json.dumps("abc")) == '"abc"')
    # test on list
    assert(jsonify(["abc",["def",1234]]) == '["abc", ["def", 1234]]')
    # test on dict
    assert(jsonify({"a": "b", "c": [1,2,3]}) == '{"a": "b", "c": [1, 2, 3]}')
    # test on set


# Generated at 2022-06-12 23:38:43.333096
# Unit test for function to_bytes
def test_to_bytes():
    # Make sure byte strings are left alone
    assert b'foo' == to_bytes(b'foo')
    # Make sure valid text strings are left alone
    assert b'\xc3\xa9' == to_bytes(u'\xc3\xa9')

    # We'll end up using surrogateescape on these.  python3 can't directly
    # encode them to latin-1, and python2 can't directly decode them from
    # latin-1.  This is a good test because it's the same code in both python2
    # and python3
    assert b'\x0d' == to_bytes(u'\r', encoding='latin-1')

    # Check error and nonstring handling
    assert b'foo' == to_bytes(b'foo', nonstring='passthru')
    assert b'foo' == to

# Generated at 2022-06-12 23:38:52.976271
# Unit test for function to_native
def test_to_native():
    """Return the string representation of an object for the current python
    version

    In Python2 this is a ``str`` whose contents are the same as the
    Python3 ``str``
    In Python3 this is a ``str``

    :arg obj: The object to get a string representation of

    :returns: The string representation of the object.  The type of this
        depends on the python version
    """
    def test_obj(obj, expected_py3, expected_py2):
        assert to_native(obj) == expected_py3
        assert to_native(obj, errors='surrogate_or_strict') == expected_py3
        assert to_native(obj, errors='surrogate_or_replace') == expected_py3
        assert to_native(obj, errors='surrogate_then_replace') == expected_py

# Generated at 2022-06-12 23:38:58.516801
# Unit test for function jsonify
def test_jsonify():
    try:
        import simplejson as json
    except ImportError:
        pass
    assert jsonify({"a": 1}) == b'{"a": 1}'
    assert jsonify({"a": to_bytes(u'\u2603')}) == b'{"a": "\\u2603"}'
    assert jsonify({"a": to_text(b'\xe2\x98\x83')}) == b'{"a": "\\u2603"}'



# Generated at 2022-06-12 23:39:08.985080
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('abc', nonstring='strict') == 'abc'
    assert to_bytes('abc') == 'abc'
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(u'abc') == 'abc'
    assert to_bytes('abc', errors='surrogateescape') == 'abc'
    assert to_bytes(u'\u00FF') == '\xC3\xBF'
    assert to_bytes(u'\u00FF', errors='surrogateescape') == '\xC3\xBF'
    assert to_bytes(u'\u00FF', errors='surrogate_or_replace') == '\xC3\xBF'

# Generated at 2022-06-12 23:39:18.393442
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\u2713') == u'"\u2713"'
    assert jsonify(u'\u2713', ensure_ascii=False) == u'"\u2713"'
    assert jsonify(u'\u2713', sort_keys=True) == u'"\u2713"'
    assert jsonify(u'\u2713', ensure_ascii=False, sort_keys=True) == u'"\u2713"'
    assert jsonify({u'\u2713': u'\u2713'}) == u'{"\u2713": "\u2713"}'
    assert jsonify({u'\u2713': u'\u2713'}, ensure_ascii=False) == u'{"\u2713": "\u2713"}'

# Generated at 2022-06-12 23:39:28.757544
# Unit test for function to_native
def test_to_native():

    # Test ints
    x = 1
    assert x
    assert x == 1
    assert to_native(x) == 1
    # Test floats
    x = 1.1
    assert x
    assert x == 1.1
    assert to_native(x) == 1.1
    # Test booleans
    x = False
    assert not x
    assert x == False
    assert to_native(x) is False

    # Test strings
    x = u'hello'
    assert x
    assert x == u'hello'
    assert to_native(x) == 'hello'
    x = b'hello'
    assert x
    assert x == b'hello'
    assert to_native(x) == b'hello'

    # Test lists
    x = [1, 2, 3]
    assert x

# Generated at 2022-06-12 23:39:33.884766
# Unit test for function to_native
def test_to_native():
    assert to_native('a') == 'a'
    assert to_native(1) == 1
    assert to_native(['1', '2']) == ['1', '2']
    assert to_native(['1', b'2']) == ['1', '2']
    assert to_native(b'1') == '1'
    assert to_native(u'1') == '1'


# Generated at 2022-06-12 23:39:42.793218
# Unit test for function jsonify
def test_jsonify():
    data = {u"spam": u"eggs", u"foo": u"bar"}
    json_str = jsonify(data)
    assert isinstance(json_str, text_type)
    assert json_str == '{"spam": "eggs", "foo": "bar"}'
    assert json_str == jsonify(data)

    data = {u"spam": Set([u"eggs", u"ham"]), u"foo": u"bar"}
    json_str = jsonify(data)
    assert isinstance(json_str, text_type)
    assert json_str == '{"spam": ["eggs", "ham"], "foo": "bar"}'
    assert json_str == jsonify(data)


# Generated at 2022-06-12 23:40:05.883529
# Unit test for function to_bytes
def test_to_bytes():
    import unittest.mock as mock
    from ansible.module_utils import basic

    def _test_to_bytes_simple_repr_passthru_empty_strict(test, obj):
        text_type_test = basic.AnsibleModule(**test.module_args)
        text_type_test.exit_json = _call_exit_json
        text_type_test.fail_json = _call_fail_json


# Generated at 2022-06-12 23:40:18.667429
# Unit test for function to_bytes
def test_to_bytes():
    # Note: Tests to_bytes and the simplerepr nonstring strategy
    class Foo:
        def __str__(self):
            return u'Foo'

        def __repr__(self):
            return Foo()

    foo_obj = Foo()

    foo_utf8 = to_bytes(foo_obj)
    assert foo_utf8 == b'Foo'
    assert isinstance(foo_utf8, binary_type)

    foo_latin1 = to_bytes(foo_obj, 'latin-1')
    assert foo_latin1 == b'Foo'
    assert isinstance(foo_latin1, binary_type)
    foo_latin1 = to_bytes(foo_obj, 'iso-8859-15')
    assert foo_latin1 == b'Foo'
    assert isinstance

# Generated at 2022-06-12 23:40:25.879005
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'fóo') == b'f\xc3\xb3o'
    assert to_bytes(u'fóo', encoding='latin-1') == b'f\xf3o'
    assert to_bytes(b'bar') == b'bar'
    assert to_bytes(123) == b'123'
    assert to_bytes(u'fóo', nonstring='empty') == b''
    assert to_bytes(u'fóo', nonstring='simplerepr') == b"u'f\\xf3o'"
    assert to_bytes(u'fóo', nonstring='passthru') is u'fóo'

# Generated at 2022-06-12 23:40:37.822272
# Unit test for function to_bytes
def test_to_bytes():
    from nose.tools import assert_equal
    from nose.tools import assert_true
    from ansible.module_utils.six import PY3

    # Make sure that a byte string is passed through unchanged
    assert to_bytes(b'foo') == b'foo'

    # Make sure that a text string is encoded properly
    assert to_bytes(u'foo') == b'foo'

    # Make sure that non-ascii text strings are encoded properly
    assert to_bytes(u'føo') == u'føo'.encode('utf-8')

    # Make sure that surrogate pairs are treated properly
    assert to_bytes(u'f\U0001d120o', encoding='utf-32') == u'f\U0001d120o'.encode('utf-32')

    # Make sure that surrogates work with the surrogateescape

# Generated at 2022-06-12 23:40:49.179677
# Unit test for function jsonify

# Generated at 2022-06-12 23:41:00.070850
# Unit test for function to_native
def test_to_native():
    '''Unit test for function ansible.module_utils._text.to_native'''

    # This is a strange case but this should not fail
    assert to_text(b'\x00\xff') == u'\x00\ufffd'

    assert to_text(u'\xe9') == u'\xe9'
    assert to_text(u'abcd\xea') == u'abcd\xea'

    # This is a string with a character that cannot be encoded with latin-1
    # - it's a CJK ideograph
    assert to_text(u'abcd\u4e9c', encoding='latin-1') == u'abcd\ufffd'

    # We can encode this with latin-1 if we use surrogateescape

# Generated at 2022-06-12 23:41:07.354576
# Unit test for function jsonify
def test_jsonify():
    data = {'unicode': "D\xe9monstration", 'bytestring': to_bytes("D\xe9monstration"), 'list': [1, 2, 3], 'tuple': (1, 2, 3), 'dict': {'one': 1, 'two': 2}, 'int': 1, 'float': 1.1, 'none': None, 'datetime': datetime.datetime.utcnow()}
    json.dumps(data)
    jsonify(data, sort_keys=True)


# Generated at 2022-06-12 23:41:14.687709
# Unit test for function jsonify
def test_jsonify():
    # Test with ascii string
    asciiStr = "i am text"
    jsonAsciiText = jsonify(asciiStr)
    assert jsonAsciiText == '"i am text"'

    # Test with pure UTF-8 string, there will be no encoding exception
    utf8Str = "中国是个好国家"
    jsonUtf8Text = jsonify(utf8Str)
    assert jsonUtf8Text == '"中国是个好国家"'

    # Test with mal-formatted UTF-8 string, there will be encoding exception
    malformattedUtf8Str = b"\xe4\xb8\xad\xe5\x9b\xbd" # this is the binray format of "中国"

# Generated at 2022-06-12 23:41:26.405678
# Unit test for function to_native
def test_to_native():
    from ansible.utils.unicode import to_text

    # Ensure that bytes are converted to unicode (and not flat out ignored)
    assert isinstance( 'Test'.encode('utf-8'), binary_type )
    assert isinstance( to_text( 'Test'.encode('utf-8') ), text_type )

    # Ensure that unicode returns unicode
    assert isinstance( u'Test', text_type )
    assert isinstance( to_text( u'Test' ), text_type )

    # Ensures that ints are not just returned as is
    assert isinstance( to_text(1), text_type )

    # Make sure that we cannot encode surrogate strings using utf-8

# Generated at 2022-06-12 23:41:38.021196
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": "b"}) == b'{"a": "b"}'
    assert jsonify({"a": "b"}, indent=2, sort_keys=True) == b'{\n  "a": "b"\n}'
    # Test for python-simplejson with no kwargs
    class _JSONEncoder(json.JSONEncoder):
        def default(self, obj):
            return _json_encode_fallback(obj)
    assert json.dumps({"a": "b"}, cls=_JSONEncoder) == b'{"a": "b"}'
    assert json.dumps({"a": "b"}, indent=2, sort_keys=True, cls=_JSONEncoder) == b'{\n  "a": "b"\n}'



# Generated at 2022-06-12 23:41:58.118723
# Unit test for function to_bytes
def test_to_bytes():
    # pylint: disable=too-many-branches,too-many-statements
    # pylint: disable=unexpected-keyword-arg
    import sys
    import unittest

    if PY3:
        # If we're in python3, we already know that surrogateescape works.
        # We've imported ansible.module_utils.basic at this point and it
        # registers surrogateescape as an error handler.
        surrogateescape_working = True
    else:
        try:
            codecs.lookup_error('surrogateescape')
            surrogateescape_working = True
        except LookupError:
            surrogateescape_working = False

    difficult_text_string = u'\U0001F4A9'
    latin_string = u'\u00E9'

    # On Python2 the default encoding is

# Generated at 2022-06-12 23:42:08.817791
# Unit test for function to_native
def test_to_native():
    import pytest
    from ansible.module_utils._text import to_native


# Generated at 2022-06-12 23:42:18.082806
# Unit test for function jsonify
def test_jsonify():
    # Valid tests
    jsonify({'a': 'b'})
    jsonify([u'\xe9'])
    jsonify({'a': u'\xe9'})
    jsonify({'a': u'\xe9'}, sort_keys=True)
    jsonify([u'\xe9'], sort_keys=True)
    jsonify([u'\xe9'], indent=4, sort_keys=True)
    jsonify(u'\xe9')
    # Test invalid encodings
    try:
        jsonify({'a': 'b'}, encoding='invalid')
        assert 0 == 1
    except TypeError:
        pass
    # Test invalid types
    try:
        jsonify(object())
        assert 0 == 1
    except TypeError:
        pass



# Generated at 2022-06-12 23:42:23.992990
# Unit test for function jsonify
def test_jsonify():
    assert "\"A string\"" == jsonify("A string")
    assert "\"A \"string\" with quotes\"" == jsonify("A \"string\" with quotes")
    assert "[42, 43]" == jsonify([42, 43])
    assert "null" == jsonify(None)
    assert "42" == jsonify(42)
    assert "42.5" == jsonify(42.5)
    assert "{\"a\": 42, \"b\": \"43\"}" == jsonify({"a": 42, "b": "43"})



# Generated at 2022-06-12 23:42:29.965750
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'\u20ac', nonstring='strict') == b'\xe2\x82\xac'
    assert to_bytes(u'\u20ac') == b'\xe2\x82\xac'
    assert to_bytes(b'\xe2\x82\xac') == b'\xe2\x82\xac'
    assert to_bytes(b'\xe2\x82\xac', nonstring='strict') == b'\xe2\x82\xac'
    assert to_bytes(b'\xe2\x82\xac', errors='strict', nonstring='strict') == b'\xe2\x82\xac'
    assert to_bytes(1) == b'1'

# Generated at 2022-06-12 23:42:38.307981
# Unit test for function jsonify
def test_jsonify():
    data1 = {'str': 'foo'}
    data2 = {'str': {'utf8': 'foo'}}

    assert jsonify(data1) == '{"str": "foo"}'
    assert jsonify(data2) == '{"str": {"utf8": "foo"}}'

    data3 = u'\xef\xbb\xbf{"foo": "bar"}'
    data4 = '\xef\xbb\xbf{"foo": "bar"}'

    assert jsonify(data3) == '{"foo": "bar"}'
    assert jsonify(data4) == '{"foo": "bar"}'



# Generated at 2022-06-12 23:42:48.930369
# Unit test for function to_bytes
def test_to_bytes():

    class C(object):
        bar = b'bar'
        def __str__(self):
            return to_text(self.bar)
        def __repr__(self):
            return to_text(self.bar)

    # If we don't have surrogateescape, these tests won't be able to
    # test all the error handler modes, but they will still test the majority of the code.
    if not HAS_SURROGATEESCAPE:
        errorhandler_tests = {
            'surrogate_or_replace': False,
            'surrogate_or_strict': False,
            'surrogate_then_replace': False,
        }

# Generated at 2022-06-12 23:42:58.052539
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('hello') == b'hello'
    assert to_bytes(u'hello') == b'hello'
    assert to_bytes('\xe9') == b'\xc3\xa9'
    assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    assert to_bytes(u'\u1234', errors='strict') == b'\xe1\x88\xb4'
    assert to_bytes(u'\u1234'.encode('utf-8')) == b'\xe1\x88\xb4'
    assert to_bytes(u'\xff') == b'\xc3\xbf'
    assert to_bytes(u'\uffff') == b'\xef\xbf\xbf'

# Generated at 2022-06-12 23:42:59.547852
# Unit test for function jsonify
def test_jsonify():
    data = '\x80'
    assert jsonify(data)



# Generated at 2022-06-12 23:43:10.468845
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo') == b'foo'
    assert to_bytes(b'foo') == b'foo'

    # Test surrogateescape
    if PY3:
        # PY3 has surrogateescape by default
        assert to_bytes('\udcff') == b'\xed\xb3\xbf'
        assert to_bytes('\udcff', errors='surrogate_or_replace') == b'\xed\xb3\xbf'
        assert to_bytes('\udcff', errors='surrogate_or_strict') == b'\xed\xb3\xbf'
        assert to_bytes('\udcff', errors='surrogate_then_replace') == b'\xed\xb3\xbf'

        # Bytes that can't be decoded in utf-

# Generated at 2022-06-12 23:43:24.255725
# Unit test for function jsonify
def test_jsonify():
    # A dict with byte string, unicode string and a list with byte string
    test_data = dict()
    test_data[b'key_byte'] =  b'value_byte'
    test_data[u'key_unicode'] = u'value_unicode'
    test_data[123] = [b'unicode_list_byte', u'unicode_list_unicode']
    # A set with byte string, unicode and a list with byte string
    test_data_set = Set()
    test_data_set.add(b'byte_byte')
    test_data_set.add(u'byte_unicode')
    test_data_set.add([b'unicode_list_byte', u'unicode_list_unicode'])
    # A list with byte string, unicode string and a

# Generated at 2022-06-12 23:43:29.102393
# Unit test for function jsonify
def test_jsonify():
    data = {
        u'bytes': b'\xe9',
        u'str': u'\xe9'
    }
    result = jsonify(data, sort_keys=True)
    assert result == '{"bytes": "\\u00e9", "str": "\\u00e9"}'



# Generated at 2022-06-12 23:43:35.725866
# Unit test for function to_bytes
def test_to_bytes():
    # Note: most of the to_bytes() functionality is tested in
    # test/units/module_utils/basic.py:TestBasic.test_to_bytes()
    assert to_bytes(u'\u1234') == binary_type(b'\xe1\x88\xb4')
    assert to_bytes(u'\u1234'.encode('utf-8'), errors='surrogate_then_replace') == binary_type(b'\xff\xfd\x34')



# Generated at 2022-06-12 23:43:43.241398
# Unit test for function to_bytes
def test_to_bytes():
    """
    >>> test_to_bytes()
    True
    """
    # py3 doesn't have a b'' literal
    empty_byte_string = to_bytes('')

    if PY3:
        byte_string_type = bytes
    else:
        byte_string_type = str

    assert not isinstance(to_bytes(b'bytes'), text_type)
    assert isinstance(to_bytes(b'bytes'), byte_string_type)
    assert to_bytes(b'bytes') == b'bytes'
    assert to_bytes(u'unicode') == b'unicode'
    assert to_bytes(1, 'latin-1') == b'1'
    assert to_bytes(1, 'ascii') == b'1'

# Generated at 2022-06-12 23:43:48.746227
# Unit test for function to_bytes
def test_to_bytes():
    # check basic ascii to bytes
    assert to_bytes('test') == b'test'
    # check bytes passthru
    assert to_bytes(b'test') == b'test'
    # check unicode
    assert to_bytes(u'test') == b'test'
    assert to_bytes(u't\u1234') == b't\xe1\x88\xb4'
    assert to_bytes(u't\u1234', errors='strict') == b't\xe1\x88\xb4'
    assert to_bytes(u't\u1234', errors='ignore') == b't'
    assert to_bytes(u't\u1234', errors='replace') == b't?'

# Generated at 2022-06-12 23:43:56.316339
# Unit test for function jsonify
def test_jsonify():
    data = {
        to_bytes("nasty"): to_bytes("\xe9"),
        to_bytes("ansible"): to_bytes("\xe9"),
        "list": [1, 2, 3, 4],
        "dict": {
            to_bytes("nasty"): to_bytes("\xe9"),
            to_bytes("ansible"): to_bytes("\xe9"),
        },
        "set": set(['foo', 'bar']),
        "datetime": datetime.datetime(2014, 1, 29, 7, 1, 51, 280573),
    }

    output = jsonify(data)
    assert '"nasty": "\xc3\xa9"' in output
    assert '"ansible": "\xc3\xa9"' in output

# Generated at 2022-06-12 23:44:05.226367
# Unit test for function jsonify
def test_jsonify():
    test_dictionary = {u'foo': u'bar',
                       u'asdf': u'jkl;'}

    # simplejson does not support the encoding parameter so skip if it's not
    # present
    try:
        from simplejson import dumps
    except ImportError:
        dumps = None

    if dumps is not None:
        if not hasattr(dumps, 'encoding'):
            return

    assert jsonify(test_dictionary) == '{"asdf": "jkl;", "foo": "bar"}'



# Generated at 2022-06-12 23:44:12.849282
# Unit test for function to_native
def test_to_native():
    assert to_native(b'foo', errors='surrogate_or_strict') == 'foo'
    assert to_native(u'\ufffd', errors='surrogate_or_strict') == u'\ufffd'

_RESERVED_CHARACTERS = frozenset(u'{}[]|')
_NEEDS_QUOTING_CHARACTERS = frozenset(u' \t\n') | _RESERVED_CHARACTERS



# Generated at 2022-06-12 23:44:16.109558
# Unit test for function to_native
def test_to_native():
    # Test for proper text type
    assert to_native(u'spam', encoding='ascii') == 'spam'

    # Test for proper byte type
    assert to_native('spam', encoding='ascii') == 'spam'


# Generated at 2022-06-12 23:44:20.567268
# Unit test for function jsonify
def test_jsonify():
    for encoding in ("utf-8", "latin-1"):
        # Test Date
        data = {"data": datetime.datetime.today()}
        jsonify(data)
        # Test set
        data = {"data": set([1, 1, 2])}
        jsonify(data)
        # Test unicode
        data = {"data":text_type("中文")}
        jsonify(data, encoding=encoding)


# Generated at 2022-06-12 23:44:38.931366
# Unit test for function to_bytes
def test_to_bytes():
    """
    This is the unit test for the function ``to_bytes``.

    This function is indirectly tested by the unit tests for ``to_native`` and
    ``to_text``.
    """
    from io import BytesIO
    import ansible.module_utils.basic
    import ansible.module_utils.six

    #################################################
    #
    # Testing nonstring parameter
    #
    #################################################

    # Test with nonstring='simplerepr'.  This is the default so we'll
    # test it exhaustively to try to catch any additional bugs.
    # nonstring='simplerepr' should be the same as nonstring=None
    assert ansible.module_utils.basic.to_bytes(1) == b'1'

# Generated at 2022-06-12 23:44:48.420319
# Unit test for function jsonify
def test_jsonify():
  import unittest
  class TestJsonify(unittest.TestCase):
    def test_jsonify(self):
      import json
      self.maxDiff = None
      string_data = u'\u0402\u0403\u0404'
      list_data = [u'\u0402\u0403\u0404']
      set_data = set([u'\u0402\u0403\u0404'])
      dict_data = {u'\u0402\u0403\u0404': u'\u0405\u0406\u0407'}
      data = dict()
      data['string'] = string_data
      data['list'] = list_data
      data['set'] = set_data
      data['dict'] = dict_data
      self.assertE

# Generated at 2022-06-12 23:44:59.098922
# Unit test for function jsonify
def test_jsonify():
    data = {"test": "abc"}
    assert(jsonify(data) == '{"test": "abc"}')
    assert(jsonify(data, sort_keys=True) == '{"test": "abc"}')
    assert(jsonify(data, indent=4, sort_keys=True) == '{\n    "test": "abc"\n}')
    assert(jsonify([data]) == '[{"test": "abc"}]')
    assert(jsonify({"date": datetime.datetime.now()}) == '{"date": "2017-12-06T14:03:17.352614"}')
    assert(jsonify({"set": set([1,2,3])}) == '{"set": [1, 2, 3]}')

# Generated at 2022-06-12 23:45:03.777304
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'test': 'jsonify', 'unicode_test': u'\u4f60\u597d\u4e16\u754c'}) == '{"test": "jsonify", "unicode_test": "\\u4f60\\u597d\\u4e16\\u754c"}'


# Generated at 2022-06-12 23:45:11.306390
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils._text import to_bytes, to_text

    assert to_bytes(u'Hello World') == b'Hello World'
    assert to_bytes('Hello World') == b'Hello World'
    assert to_bytes(b'Hello World') == b'Hello World'
    assert to_bytes(None) == b''

    class Foo(object):
        def __str__(self):
            return u'uñîçø∂ê'

        def __repr__(self):
            return u'rep: uñîçø∂ê'

    assert to_bytes(Foo()) == b'u\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8\xe2\x88\x82\xc3\xaa'

# Generated at 2022-06-12 23:45:18.813400
# Unit test for function to_bytes
def test_to_bytes():
    assert isinstance(to_bytes(''), binary_type)
    assert isinstance(to_bytes('hello'), binary_type)
    assert isinstance(to_bytes(u'hello'), binary_type)

    assert to_bytes('hello') == b'hello'
    assert to_bytes(b'hello') == b'hello'
    assert to_bytes(u'hello') == b'hello'

    assert to_bytes(b'hello', nonstring='passthru') == b'hello'
    assert to_bytes(b'hello', nonstring='empty') == b''
    assert to_bytes(b'hello', nonstring='strict') == b'hello'
    assert to_bytes(b'hello', nonstring='simplerepr') == b"b'hello'"


# Generated at 2022-06-12 23:45:28.673227
# Unit test for function to_native
def test_to_native():
    """
    This function tests if the to_native function

    :return: None
    """
    # Test bytes type as input
    assert to_native(b'ansible') == 'ansible'

    # Test text type as input
    assert to_native(u'ansible') == 'ansible'

    # Test error handling if input is not string
    # Test int as input
    try:
        to_native(123)
    except TypeError as e:
        assert 'Non-string value' in to_text(e)
    except Exception as e:
        assert False, 'Invalid exception: %s' % to_text(e)
    else:
        assert False, 'Exception not raised for invalid input'



# Generated at 2022-06-12 23:45:38.791399
# Unit test for function to_bytes
def test_to_bytes():
    def from_json(s):
        return json.loads(s, object_hook=_from_json_hook)

    def _from_json_hook(data):
        return {
            text_type(k): v
            for k, v in iteritems(data)
        }

    def assert_convertable(obj, expected=None, encoding='utf-8',
                           errors=None, nonstring='simplerepr'):
        obj_bytes = to_bytes(obj, encoding=encoding, errors=errors,
                             nonstring=nonstring)
        if expected is None:
            expected = to_bytes(to_text(obj))


# Generated at 2022-06-12 23:45:45.071096
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import u
    from ansible.module_utils.six.moves import cStringIO

    # Test surrogate_or_replace error handler when surrogateescape is present
    codecs.register_error('strict', codecs.strict_errors)
    codecs.register_error('surrogateescape', codecs.surrogateescape_errors)
    assert to_native(b'foo', errors='surrogate_or_strict') == u('foo')
    assert to_native(b'foo', errors='surrogate_or_replace') == u('foo')
    assert to_native(b'foo', errors='surrogate_then_replace') == u('foo')

# Generated at 2022-06-12 23:45:49.125051
# Unit test for function to_bytes
def test_to_bytes():
    """
    Test: to_bytes
    """
    import os
    import sys
    import six
    from ansible.module_utils._text import _compat_b, to_bytes

    # versions of python which don't have surrogateescape
    NO_SURROGATEESCAPE = (2,)
    if not (sys.version_info[0] == 3 and sys.version_info[1] < 3):
        NO_SURROGATEESCAPE = NO_SURROGATEESCAPE + (3,)

    if HAS_SURROGATEESCAPE and sys.version_info[0] in NO_SURROGATEESCAPE:
        codecs.register_error('surrogateescape', codecs.surrogateescape_error)

    if sys.version_info[0] == 2:
        surrogate_error

# Generated at 2022-06-12 23:46:06.867363
# Unit test for function to_native
def test_to_native():
    '''
    Test to_native function.
    '''
    from ansible.module_utils._text import to_native

    assert to_native(u'abcdABCD') == u'abcdABCD'
    assert to_native('abcdABCD') == 'abcdABCD'
    assert to_native(b'abcdABCD') == b'abcdABCD'
    assert to_native(b'\x80abcdABCD') == '\x80abcdABCD'
    assert to_native(b'\xc3\xbcabcdABCD') == u'\xfcabcdABCD'
    assert to_native(b'\xc3\xbcabcdABCD', errors='strict') == u'\xfcabcdABCD'

# Generated at 2022-06-12 23:46:16.231756
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.common.text.formatters import to_bytes

    # surrogateescape is a surrogate pair that isn't valid utf8.
    surrogateescape = to_bytes(u"\udcc3\udca9", encoding='utf-8')

    # This is that same surrogate pair that *is* valid utf8 because it is the
    # utf8 encoding of the unicode character U+23A9
    utf82 = to_bytes(u"\u23a9", encoding='utf-8')

    # This is the utf8 encoding of a unicode character that can't be encoded
    # as utf8.  We'll use it to trigger a non-surrogate traceback
    bork = to_bytes(u"\udca9", encoding='utf-8', errors='surrogateescape')


# Generated at 2022-06-12 23:46:23.281029
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'x') == b'x'
    assert to_bytes(b'x', nonstring='empty') == b''
    assert to_bytes(b'x', nonstring='passthru') == b'x'
    assert to_bytes(b'x', nonstring='simplerepr') == b'x'
    assert to_bytes(b'x', nonstring='strict') == b'x'


# Generated at 2022-06-12 23:46:32.028979
# Unit test for function to_native
def test_to_native():
    assert to_native(u'example') == u'example'
    assert to_native('example') == 'example'

    class Foo(object):
        def __str__(self):
            return u'example'

    assert to_native(Foo()) == u'example'

    # On Python 2, __str__ is expected to return bytes.
    if not PY3:
        class Bar(object):
            def __str__(self):
                return u'example'.encode('utf-8')

            def __repr__(self):
                return u'repr'

        assert to_native(Bar()) == u'example'

    class Baz(object):
        def __repr__(self):
            return u'repr'

    assert to_native(Baz()) == u'repr'

# Unit tests for function to_

# Generated at 2022-06-12 23:46:42.587983
# Unit test for function to_native
def test_to_native():
    """Test to_native function"""
    from ansible.module_utils._text import to_text
    from ansible.module_utils._text import to_bytes
    assert(to_bytes(to_text(u'abc')) == b'abc')
    assert(to_bytes(to_text(u'abc'), errors='surrogate_or_replace') == b'abc')
    assert(to_bytes(to_text(b'abc')) == b'abc')
    assert(to_bytes(to_text(b'abc'), errors='surrogate_or_replace') == b'abc')
    assert(to_bytes(to_text(123)) == b'123')
    assert(to_bytes(to_text(123), nonstring='strict') == b'123')

# Generated at 2022-06-12 23:46:54.386841
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        data = {
            u'': b'',
            1: b'1',
            u'\x00': b'\x00',
            u'\u2603': b'\xe2\x98\x83',
            b'\x00': b'\x00',
            b'\xe2\x98\x83': b'\xe2\x98\x83',
            u'\udc80': None,
            u'\udc80\udc80': None,
            u'\udc80\udcff': None,
            u'\udc80\udc80\udc80': None,
        }

# Generated at 2022-06-12 23:47:05.028846
# Unit test for function to_bytes
def test_to_bytes():
    import codecs
    codecs.register_error('strict', codecs.strict_errors)
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestToBytes(unittest.TestCase):
        def test_bytes(self):
            self.assertEqual(to_bytes('abcd'), b'abcd')

        def test_text(self):
            self.assertEqual(to_bytes('abcd', 'utf-8'), b'abcd')

        def test_nonstring(self):
            self.assertEqual(to_bytes(b'abcd', 'utf-8'), b'abcd')


# Generated at 2022-06-12 23:47:13.486814
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('Hello World') == b'Hello World'
    assert to_bytes(u'Hi there') == b'Hi there'
    assert to_bytes(u'\u2603') == b'\xe2\x98\x83'

    # UnicodeEncodeError with strict - no change in 2.3
    with pytest.raises(UnicodeEncodeError):
        to_bytes(u'\u2603', errors='strict')

    # UnicodeEncodeError with surrogate_or_strict - no change in 2.3
    with pytest.raises(UnicodeEncodeError):
        to_bytes(u'\u2603', errors='surrogate_or_strict')

    # UnicodeEncodeError with surrogate_then_replace - no change in 2.3
    # should be a "?"

# Generated at 2022-06-12 23:47:24.011815
# Unit test for function to_bytes
def test_to_bytes():
    '''
    This function is used to unit test the various to_bytes permutations.
    Each row of the data parameter is a tuple representing a permutation of
    the method to test.  It should have 3 parameters:

    - `0`: The string to convert
    - `1`: The encoding to use.  None is a synonym for 'utf-8'
    - `2`: The error strategy to use.  None is a synonym for 'strict'
    - `3`: The nonstring strategy to use.  None is a synonym for 'simplerepr'

    Each row of the expected_result parameter should have a single parameter:
        - `0`: The expected result
    '''

# Generated at 2022-06-12 23:47:33.820087
# Unit test for function to_bytes
def test_to_bytes():
    # Test just to make sure that surrogates are handled the way we expect
    # and that surrogates in the string don't affect the choices of
    # fallback error handler
    try:
        to_bytes(u'\udced', errors='ignore')
    except UnicodeEncodeError:
        pass
    else:
        raise AssertionError('Surrogate not ignored')

    try:
        to_bytes(u'\udced', errors='replace')
    except UnicodeEncodeError:
        raise AssertionError('Surrogate should have been replaced')

    try:
        to_bytes(u'\udced', errors='strict')
    except UnicodeEncodeError:
        pass
    else:
        raise AssertionError('Surrogate should have caused strict error')


# Generated at 2022-06-12 23:47:49.316266
# Unit test for function to_native
def test_to_native():
    assert to_native(b'hello') == u'hello'
    assert to_native(u'hello') == u'hello'


if PY3:
    _native_type = binary_type
else:
    _native_type = text_type



# Generated at 2022-06-12 23:48:00.959835
# Unit test for function to_bytes
def test_to_bytes():
    # function defined in above section
    assert isinstance(to_bytes(b'hello world'), binary_type)
    assert isinstance(to_bytes('hello world'), binary_type)
    assert to_bytes(1) == b'1'
    try:
        to_bytes(1, nonstring='strict')
        assert False  # Shouldn't get here
    except TypeError:
        pass
    assert isinstance(to_bytes(1, nonstring='passthru'), int)
    assert to_bytes(1, nonstring='empty') == b''

    # surrogate_or_replace
    assert to_bytes(u'hello world', errors='surrogate_or_replace') == b'hello world'

# Generated at 2022-06-12 23:48:08.855973
# Unit test for function jsonify
def test_jsonify():
    dic = {
        'str': u'\u4e16\u754c',
        'byte_str': b'\xe4\xb8\x96\xe7\x95\x8c',
        'int': 234,
        'float': 3.14,
        'bool': True,
        'list_': [1, 2, 3],
        'dict_': {'hello': 'world'},
    }

    dic_w_set = {}
    dic_w_set.update(dic)
    dic_w_set.update({'set_': set([1, 2, 3])})

    dic_w_datetime = {}
    dic_w_datetime.update(dic)
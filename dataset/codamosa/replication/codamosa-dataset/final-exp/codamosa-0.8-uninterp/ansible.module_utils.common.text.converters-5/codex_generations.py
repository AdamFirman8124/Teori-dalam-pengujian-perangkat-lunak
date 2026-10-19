

# Generated at 2022-06-12 23:38:25.361590
# Unit test for function jsonify
def test_jsonify():
    data = {u"ø": "ascii"}
    assert jsonify(data)
    # Test for old simplejson module.
    assert jsonify(data, skipkeys=True, ensure_ascii=False)
    assert jsonify(data, skipkeys=True, ensure_ascii=True)



# Generated at 2022-06-12 23:38:32.828224
# Unit test for function to_native
def test_to_native():
    """
    Test to_native method
    Test can be executed with: python -c "import ansible.module_utils._text; ansible.module_utils._text.test_to_native()"
    """
    assert to_native(b'foo') == 'foo'
    assert to_native(u'strings') == 'strings'
    assert to_native(1) == '1'
    assert to_native(u'\xe9') == '\xe9'



# Generated at 2022-06-12 23:38:34.379372
# Unit test for function to_bytes
def test_to_bytes():
    """
    Basic test for to_bytes
    """
    pass



# Generated at 2022-06-12 23:38:36.048564
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=u"b")) == '{"a": "b"}'



# Generated at 2022-06-12 23:38:38.282831
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(data={"a":u'\xf6'}) == '{"a": "\\u00f6"}'



# Generated at 2022-06-12 23:38:50.173208
# Unit test for function to_native
def test_to_native():
    # we can only test for the unicode string value being returned on python2 and not for
    # the bytes value being returned on python3

    # Test for str/unicode input
    assert to_native("Hello World") == u'Hello World'
    assert to_native(u"Hello World") == u'Hello World'

    # Test for integer input
    assert to_native(0) == u'0'

    # Test for float input
    assert to_native(0.01) == u'0.01'

    # Test for list input
    assert to_native([1, 2, 3]) == u'[1, 2, 3]'

    # Test for dict input
    assert to_native({'a': 1, 'b': 2}) == u"{'a': 1, 'b': 2}"

    # Test for complex input

# Generated at 2022-06-12 23:38:58.136294
# Unit test for function jsonify
def test_jsonify():
    data = {
        u'unicode': u'\u2713',
        b'bytes': b'\xE2\x9C\x93'
    }
    jsonified_data = jsonify(data)
    assert jsonified_data == '{"unicode": "\\u2713", "bytes": "\\u2713"}', jsonified_data
    jsonified_data = jsonify(data, sort_keys=True)
    assert jsonified_data == '{"bytes": "\\u2713", "unicode": "\\u2713"}', jsonified_data



# Generated at 2022-06-12 23:39:01.345816
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('\u8d85\u7ea7\u7528\u6237') == '"\\ud85c\\udea7\\ud751\\udd8f\\ud7d9\\ud6d7"'
    assert jsonify(b'\u8d85\u7ea7\u7528\u6237') == '"\\ud85c\\udea7\\ud751\\udd8f\\ud7d9\\ud6d7"'



# Generated at 2022-06-12 23:39:10.946376
# Unit test for function to_bytes
def test_to_bytes():
    def _test_to_bytes_helper(obj, encoding='utf-8', errors=None, nonstring='simplerepr'):
        # Use byte string for repr
        if PY3 and isinstance(obj, text_type):
            real_obj = obj.encode('utf-8', 'surrogateescape')
        else:
            real_obj = obj
        expected = b'%s,%s,%s,%s' % (real_obj,
                                     codecs.encode(to_bytes(encoding, 'ascii', 'strict'), 'ascii'),
                                     to_bytes(errors, 'ascii', 'strict'),
                                     to_bytes(nonstring, 'ascii', 'strict'))

        # Test that to_bytes works as expected

# Generated at 2022-06-12 23:39:18.642340
# Unit test for function to_bytes

# Generated at 2022-06-12 23:39:34.174304
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('ok') == '"ok"'
    assert jsonify(b'ok') == '"ok"'
    assert jsonify('\xc3\xbf') == '"\ufffd"'
    assert jsonify(u'\xc3\xbf') == '"\ufffd"'
    assert jsonify(u'\xc3\xbf'.encode('utf-8')) == '"\xc3\xbf"'
    assert jsonify(u'\xc3\xbf'.encode('latin-1')) == '"\xc3\xbf"'
    assert jsonify({u'\xc3\xbf'.encode('utf-8'): u'\xc3\xbf'.encode('utf-8')}) == '{"\xc3\xbf": "\xc3\xbf"}'
    assert jsonify

# Generated at 2022-06-12 23:39:42.827848
# Unit test for function to_bytes
def test_to_bytes():
    # Make sure that ascii decodes properly
    assert to_bytes('abc', '') == b'abc'
    assert to_bytes('abc', None) == b'abc'
    assert to_bytes('abc', errors='surrogate_or_replace') == b'abc'
    assert to_bytes('abc', errors='surrogate_or_strict') == b'abc'
    assert to_bytes('abc', errors='surrogate_then_replace') == b'abc'
    assert to_bytes('abc', 'ascii') == b'abc'
    assert to_bytes('abc', encoding='ascii') == b'abc'
    assert to_bytes('abc', errors='surrogate_or_replace', encoding='ascii') == b'abc'

# Generated at 2022-06-12 23:39:45.183518
# Unit test for function jsonify
def test_jsonify():
    return jsonify(dict(ansible_all_ipv4_addresses=dict(default=['10.20.30.40'])))



# Generated at 2022-06-12 23:39:55.821284
# Unit test for function jsonify
def test_jsonify():
    # Test string value with utf-8 encoding
    foo_utf8 = to_bytes(u'foo')
    assert jsonify(foo_utf8) == u'foo'
    # Test string value with latin-1 encoding
    foo_latin1 = to_bytes(u'foo', encoding='latin-1')
    assert jsonify(foo_latin1) == u'foo'
    # Test utf-8 encoded unicode
    bar_utf8 = to_bytes(u'bar')
    assert jsonify(bar_utf8) == u'bar'
    # Test latin-1 encoded unicode
    bar_latin1 = to_bytes(u'bar', encoding='latin-1')
    assert jsonify(bar_latin1) == u'bar'
    # Test invalid unicode string
    bad_

# Generated at 2022-06-12 23:40:05.108735
# Unit test for function jsonify
def test_jsonify():
    # dict with utf-8 data
    data = {u'key1': u'\u4f60\u597d', u'key2': u'how are you'}
    assert jsonify(data) == '{"key1": "\xe4\xbd\xa0\xe5\xa5\xbd", "key2": "how are you"}'
    # dict with Latin-1 data
    data = {u'key1': u'\xf0\x9f\x91\x88', u'key2': u'\xc7\xd0\xca\xc2\xd4\xd8'}

# Generated at 2022-06-12 23:40:12.082092
# Unit test for function jsonify
def test_jsonify():
    s = "{'a': 1, 'b': 'c'}"
    assert jsonify(eval(s)) == s

    s = [1, 2, {'a': 'b'}]
    assert jsonify(s) == '[1, 2, {"a": "b"}]'

    assert jsonify(Set([1, 2])) == '[1, 2]'



# Generated at 2022-06-12 23:40:21.553877
# Unit test for function jsonify
def test_jsonify():
    # Verify that jsonify returns a json string
    data = {b'foo\xe9': u'bar\u20ac'}
    assert isinstance(jsonify(data), str)

    # Verify that jsonify supports utf-8 data
    data = {b'foo\xc3\xa9'.decode('utf-8'): u'bar\u20ac'}
    assert isinstance(jsonify(data), str)

    # Verify that jsonify supports latin-1 data
    data = {b'foo\xe9'.decode('latin-1'): u'bar\u20ac'}
    assert isinstance(jsonify(data), str)

    # Verify that jsonify throws an exception if no valid unicode encoding can be found

# Generated at 2022-06-12 23:40:29.036108
# Unit test for function jsonify
def test_jsonify():
    class DummyFile(object):
        def __init__(self, value):
            self.value = value
            self.closed = False

        def __iter__(self):
            return iter(self.value)

    d = {
        'a': 1,
        'b': [1, '2', u'\u043f\u0440\u0438\u0432\u0435\u0442'],
        'c': u'abc\u043a\u0438',
        'd': {
            'a': 5,
            'b': 6
        },
        'f': {
            'a': 'a',
            'b': DummyFile('{"a": "b"}')
        }
    }
    d['e'] = d

# Generated at 2022-06-12 23:40:39.957703
# Unit test for function to_native
def test_to_native():
    assert to_native(u"foo") == u"foo"
    assert to_native(b"foo") == u"foo"
    assert to_native(b"foo\xff") == u"foo\ufffd"
    assert to_native(b"foo", errors='surrogate_or_replace') == u"foo\ufffd"
    assert to_native(b"foo", errors='surrogate_or_strict') == u"foo"
    assert to_native(b"foo\xed\xa0\x80\xed\xb0\x80", errors='surrogate_or_replace') == u"foo\ufffd\ufffd"

# Generated at 2022-06-12 23:40:50.458758
# Unit test for function to_bytes
def test_to_bytes():
    """# -*- coding: utf-8 -*-
    """
    import sys
    if sys.version_info[0] < 3:
        text_type = unicode
        binary_type = str

    def _is_bytes(string):
        if PY3:
            return isinstance(string, bytes)
        else:
            return isinstance(string, str)

    def _is_text(string):
        if PY3:
            return isinstance(string, str)
        else:
            return isinstance(string, unicode)

    encoded_string = to_bytes('café', 'latin-1')
    assert _is_bytes(encoded_string)
    assert not _is_text(encoded_string)
    assert encoded_string == b'caf\xe9'

    encoded

# Generated at 2022-06-12 23:41:08.286731
# Unit test for function jsonify
def test_jsonify():
    new_data = {b'a': u'a', u'b': b'b', 'c': 123, 'd': [{b'e': u'f'}]}
    assert jsonify(new_data) == '{"a": "a", "c": 123, "b": "b", "d": [{"e": "f"}]}'


# Generated at 2022-06-12 23:41:15.607210
# Unit test for function to_bytes
def test_to_bytes():
    import sys
    import io
    import re

    def _check_string(value, expected_string, expected_type=binary_type, encoding='utf-8', errors=None, nonstring='simplerepr'):
        new_value = to_bytes(value, encoding=encoding, errors=errors, nonstring=nonstring)
        assert isinstance(new_value, expected_type)
        assert new_value == expected_string
        return new_value

    def _check_bytes_exception(value, encoding, errors, exc_pattern):
        if PY3:
            # Python3's exception messages changed
            exc_pattern = re.sub(br'\\x[0-9a-z]{2}', br'\\\\x..', exc_pattern)

# Generated at 2022-06-12 23:41:27.523526
# Unit test for function to_bytes
def test_to_bytes():
    class Test(object):
        def __repr__(self):
            return u'Test repr\u1234'

        def __str__(self):
            return u'Test str\u1234'

    try:
        to_bytes('foo', encoding='ascii')
        _assert(False, 'Did not detect invalid encoding')
    except LookupError:
        pass
    _assert(to_bytes(u'foo') == b'foo', 'Direct conversion from unicode to bytes failed')
    _assert(to_bytes(u'fóo') == b'f\xc3\xb3o', 'Direct conversion from unicode to bytes with accents failed')

# Generated at 2022-06-12 23:41:39.533769
# Unit test for function to_bytes
def test_to_bytes():
    # test the basic uses of to_bytes
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'foo', nonstring='passthru') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'foo', 'latin-1') == b'foo'

    # test nonstring
    assert to_bytes([1, 2], nonstring='passthru') == [1, 2]
    try:
        to_bytes([1, 2], nonstring='strict')
    except TypeError:
        pass
    else:
        assert False, 'to_bytes accepted a nonstring without strict'
    assert to_bytes(datetime.datetime.now(), nonstring='simplerepr')

# Generated at 2022-06-12 23:41:46.118056
# Unit test for function to_bytes
def test_to_bytes():
    # Default behavior
    # Text string is encoded to UTF-8
    assert to_bytes('abc') == b'abc'
    # Non-text string is passed through
    assert to_bytes(5) == 5
    # Non-text strings are coerced to a string before being encoded
    assert to_bytes([1, 2, 3]) == b'[1, 2, 3]'
    # Non-text strings for which str() or repr() raise an exception are coerced to an empty string
    from cStringIO import StringIO
    class BadRepr(object):
        def __repr__(self):
            raise UnicodeError('no way')
    assert to_bytes(BadRepr()) == b''
    assert to_bytes(StringIO('abc')) == b''
    # Using surrogateescape
    # Surrogates in the string are escaped (and do not

# Generated at 2022-06-12 23:41:57.894652
# Unit test for function to_native
def test_to_native():
    class Foo:
        pass

    # bytestrings
    assert to_native(b'foo') == u'foo'
    assert to_native(b'foo\xe2\x89\xa2') == u'foo\u2262'
    assert to_native(b'foo\xe2\x89\xa2', errors='strict') == u'foo\u2262'
    assert to_native(b'foo\xe2\x89\xa2', errors='surrogateescape') == u'foo\ud87e\udca2'

    # textstrings
    assert to_native(u'foo') == u'foo'
    assert to_native(u'foo\u2262') == u'foo\u2262'

# Generated at 2022-06-12 23:42:08.307611
# Unit test for function to_bytes
def test_to_bytes():
    # Make sure the function works for default cases
    assert to_bytes(u'text') == b'text'
    assert to_bytes(b'binary') == b'binary'
    assert to_bytes(b'm\x80x') == b'm\x80x'

    # Make sure strings with surrogates are handled
    assert to_bytes(u'surrogate:\uDC80') == b'surrogate:\xed\xb2\x80'

    # Make sure non-string types are handled appropriately
    assert to_bytes(u'non-string', nonstring='simplerepr') == b'non-string'

# Generated at 2022-06-12 23:42:18.004743
# Unit test for function to_native
def test_to_native():
    import sys
    # We can't always put the BOM.  With sys.stdout's encoding we'd
    # get the following error:
    #   UnicodeEncodeError: 'utf-8' codec can't encode character '\ufeff' in position 0:
    #   surrogates not allowed
    # This can happen when the console is set to a single bytestring encoding
    # like ISO-8859-7.
    #
    # Additionally: Some terminal emulators (like iTerm2) refuse to display
    # BOMs.
    #
    # So we setup the BOM handling here depending on the environment and then
    # test.
    if sys.stdout.encoding in ('utf-8', 'UTF-8', 'utf8'):
        bom = '\\ufeff'
    else:
        bom = ''

    # Test

# Generated at 2022-06-12 23:42:26.170581
# Unit test for function to_bytes
def test_to_bytes():
    from ansible_collections.ansible.community.plugins.module_utils._text import to_bytes

    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes('foo') is not 'foo'
    assert to_bytes('foo') is not u'foo'

    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'foo') is not u'foo'
    assert to_bytes(b'foo') is not 'foo'

    assert to_bytes(u'foo', errors='replace') == b'foo'
    assert to_bytes(u'foo', errors='surrogate_then_replace') == b'foo'
    assert to_bytes(u'foo', errors='surrogate_then_replace')

# Generated at 2022-06-12 23:42:36.915999
# Unit test for function to_bytes
def test_to_bytes():
    # Can't test the speed of this because we don't have access to timeit or
    # profile in the unit tests but we can at least check that it returns the
    # same value as the full blown code path.
    import six
    if six.PY2:
        from ansible.compat.tests import unittest
        from ansible.compat import text_type

        class TestToBytes(unittest.TestCase):
            def test_to_bytes(self):
                self.assertEqual(to_bytes(u'foobar'), b'foobar')
                self.assertEqual(to_bytes(u'foobar', nonstring='simplerepr'), b"u'foobar'")
                self.assertEqual(to_bytes(u'foobar', nonstring='strict'), b'foobar')

# Generated at 2022-06-12 23:43:20.862956
# Unit test for function to_native
def test_to_native():

    assert to_native('foo') == 'foo'
    assert to_native(u'foo') == 'foo'
    assert to_native(u'Ω') == '\xc2\x8e'
    assert to_native(b'foo') == 'foo'
    assert to_native(b'\xc2\x8e') == '\xc2\x8e'



# Generated at 2022-06-12 23:43:26.734208
# Unit test for function to_native
def test_to_native():
    assert to_native('foo') == u'foo'
    assert to_native(u'foo') == u'foo'
    assert to_native(b'foo') == u'foo'
    assert to_native('foo'.encode('ascii')) == u'foo'
    assert to_native(b'foo', encoding='utf-16') == u'foo'
    assert to_native(u'\u5317\u4EB0', encoding='utf-8') == u'\u5317\u4EB0'
    assert to_native(('\u5317', u'\u4EB0'), encoding='utf-8') == (u'\u5317', u'\u4EB0')

# Generated at 2022-06-12 23:43:36.874475
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        assert to_bytes('a') == b'a'
    else:
        assert to_bytes(b'a') == b'a'
        assert to_bytes(u'葉') == b'\xe8\x91\x89'
    assert to_bytes(b'a', nonstring='passthru') == b'a'
    assert to_bytes(None, nonstring='passthru') is None
    assert to_bytes('a', errors='replace') == b'a'
    assert to_bytes(u'葉', errors='replace') == b'?', to_bytes(u'葉', errors='replace')

# Generated at 2022-06-12 23:43:46.011796
# Unit test for function jsonify
def test_jsonify():
    # jsonify should return a unicode value
    assert isinstance(jsonify({'a': u'b'}), text_type)
    # jsonify should not fail on non-utf-8 encoded string
    assert jsonify({u'unicode': 'a\x92\x93\x94\x95'.decode('latin-1')})
    # jsonify should handle set
    assert jsonify(Set([1, 2])) == '[1, 2]'
    # jsonify should handle datetime
    assert jsonify({'a': datetime.datetime(2012, 12, 2, 19, 1, 0)})



# Generated at 2022-06-12 23:43:52.589029
# Unit test for function jsonify
def test_jsonify():
    ''' Test proper behavior of the jsonify function '''
    input_data = {u'foo': {u'bar': [u'baz']}}

    # no unicode
    assert jsonify(input_data) == '{"foo": {"bar": ["baz"]}}'

    # unicode
    input_data[u'fo\xf6'] = u'fo\xf6'
    assert jsonify(input_data) == ('{"foo": {"bar": ["baz"]}, "fo\\u00f6": "fo\\u00f6"}')



# Generated at 2022-06-12 23:43:56.078756
# Unit test for function to_native
def test_to_native():
    ''' test to_native()'''
    for value in map(chr, range(255)):
        assert to_native(value) == value



# Generated at 2022-06-12 23:44:07.449672
# Unit test for function to_bytes
def test_to_bytes():
    def _test_to_bytes(obj, **kwargs):
        kwargs.setdefault('encoding', 'utf-8')
        kwargs.setdefault('errors', 'surrogate_then_replace')
        kwargs.setdefault('nonstring', 'simplerepr')
        return to_bytes(obj, **kwargs)

    assert b'byte string' == _test_to_bytes(b'byte string')
    assert b'unicode string' == _test_to_bytes(u'unicode string')
    assert b'unicode string with surrogates: \udcec' == _test_to_bytes(u'unicode string with surrogates: \udcec')


# Generated at 2022-06-12 23:44:17.919869
# Unit test for function to_bytes
def test_to_bytes():
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    """Ensure to_bytes handles all scenarios correctly"""

    import sys

    # We can't support surrogateescape in Python2 but we can
    # fake it by encoding to utf-8, decoding with surrogateescape and then
    # encoding to the original encoding.  This would preserve the encoded
    # bytes in the string but the user would have to keep track of what
    # encoding the bytes in their string were encoded with.  So instead
    # we just test if surrogateescape is available.

    if PY3:
        surrogateescape_error_handler = 'surrogateescape'
    else:
        surrogateescape_error_handler = None

    # We're using a non-UTF8 encoding (latin-1) to test that to_bytes()

# Generated at 2022-06-12 23:44:20.526169
# Unit test for function to_native
def test_to_native():
    result = to_native(b'foo')
    assert isinstance(result, text_type)
    result = to_native(u'foo')
    assert isinstance(result, text_type)


# Generated at 2022-06-12 23:44:31.129644
# Unit test for function jsonify
def test_jsonify():
    import json
    import sys
    from datetime import datetime

    j = jsonify({
        "foo": u"bar",
        "snowman": u"\u2603".encode("latin-1"),
        "baz": u"qux",
        "now": datetime(2014, 12, 10, 21, 22, 25, 0),
        "list": [1, u"foo", u"bar"],
        "dict": {1: u"foo", "baz": "qux"},
        "set": set([1, 2, 3]),
    })
    if sys.version_info >= (3, 0):
        assert isinstance(j, str), \
            "jsonify returned a value of type %s, but str was expected" % type(j)

# Generated at 2022-06-12 23:45:24.599728
# Unit test for function to_bytes
def test_to_bytes():
    # Test basics
    assert to_bytes('abcdef', 'utf-8') == b'abcdef'
    assert to_bytes('\xc3\xa9', 'utf-8') == b'\xc3\xa9'
    # Test surrogate_or_strict
    assert to_bytes('\xc3\xa9', 'latin-1', errors='surrogate_or_strict') == b'\xc3\xa9'
    # Test surrogate_or_replace
    assert to_bytes('\xc3\xa9', 'latin-1', errors='surrogate_or_replace') == b'?'
    # Test surrogate_then_replace
    assert to_bytes('\xc3\xa9', 'latin-1', errors='surrogate_then_replace') == b'?\n'
    # Test surrogate_

# Generated at 2022-06-12 23:45:35.084599
# Unit test for function to_native
def test_to_native():

    assert to_text(b'Hello World', nonstring='passthru') == b'Hello World'
    assert to_text(b'Hello World') == u'Hello World'

    # Like to_text, this should return an empty unicode string
    assert to_text(None) == u''

    assert to_bytes(None) == b''

    # The function doesn't inspect the string to see if it's valid in the given
    # encoding so this doesn't raise an error
    assert to_bytes(u'\u2603', 'ascii') == b'?'

    assert to_bytes(u'\u2603') == b'\xe2\x98\x83'
    assert to_bytes(u'Hello World') == b'Hello World'

    # The function doesn't inspect the string to see if it's valid in the given

# Generated at 2022-06-12 23:45:42.952906
# Unit test for function to_native
def test_to_native():
    '''Unit test for function to_native.'''
    expected_result = 'some result'

    def _to_native(obj):
        '''Pass-through mock for to_native.'''
        return obj

    # No error
    assert to_native(_to_native(expected_result)) == expected_result

    # Non-string result
    assert to_native(_to_native(7)) == 7

    # Non-string result, non-string module_name
    assert to_native(_to_native(7), module_name=1) == 7

    # TypeError
    try:
        to_native(_to_native(7), module_name='foo')
    except TypeError as type_error:
        assert 'foo' in to_native(type_error)
    else:
        assert False, 'TypeError not raised'



# Generated at 2022-06-12 23:45:53.832087
# Unit test for function to_bytes
def test_to_bytes():
    """
    :rtype: str
    """
    bb = binary_type
    b = lambda x: bb(x, encoding='latin-1')
    u = lambda x: text_type(x, encoding='latin-1')

    # These will pass straight through
    assert to_bytes(b('simple'), nonstring='passthru') == b('simple')
    assert to_bytes(u('simple'), nonstring='passthru') == u('simple')

    # Testing 'simplerepr' with bytes
    assert to_bytes(b('simple')) == b('simple')
    assert to_bytes(b('лошадь')) == b('лошадь')

# Generated at 2022-06-12 23:46:05.499103
# Unit test for function jsonify
def test_jsonify():
    data = {'foo': ['bar', 42, {'baz': True}]}
    assert jsonify(data) == '{"foo":["bar",42,{"baz":true}]}'
    assert jsonify(data, ensure_ascii=False) == '{"foo":["bar",42,{"baz":true}]}'
    data = {'foo': ['bar', 42, {'baz': True}], u'f\xf6\xf6': 'f\xe4\xe4'}
    assert jsonify(data) == '{"foo":["bar",42,{"baz":true}],"föö":"fää"}'
    assert jsonify(data, ensure_ascii=False) == '{"foo":["bar",42,{"baz":true}],"föö":"fää"}'

# Generated at 2022-06-12 23:46:15.390082
# Unit test for function to_bytes
def test_to_bytes():
    # Test nonstring behaviour
    assert to_bytes(42, nonstring='simplerepr') == b'42'
    assert to_bytes(42, nonstring='passthru') == 42
    assert to_bytes(42, nonstring='empty') == b''
    # Allowed to pass in text
    assert to_bytes(u'\u043f', 'utf-8') == b'\xd0\xbf'
    # Allowed to pass in a bytestring that decodes to valid text
    assert to_bytes(b'\xd0\xbf', 'utf-8') == b'\xd0\xbf'

    # Can't pass in a bytestring for something that could be unicode

# Generated at 2022-06-12 23:46:26.507027
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native('foo') == 'foo'
    assert to_native(b'foo') == 'foo'
    assert to_native(b'foo\xc3\xa9') == u'foo\xe9'
    assert to_native(b'foo\xc3\xa9'.decode('utf-8', 'surrogateescape')) == u'foo\xe9'
    assert isinstance(to_native(b'foo\xc3\xa9'), text_type)
    # Now test surrogate_or_replace
    assert to_native(b'foo\xff') == u'foo\ufffd'
    assert to_native(b'foo\xff'.decode('utf-8', 'surrogateescape')) == u'foo\ufffd'

# Generated at 2022-06-12 23:46:34.374253
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({ 'foo': 'bar' }) == '{"foo": "bar"}'
    assert jsonify([ 1, 2, 3 ]) == '[1, 2, 3]'

    assert jsonify({ to_bytes(u'foo'): to_bytes(u'bar') }) == '{"foo": "bar"}'
    assert jsonify([ u'1', u'3', u'3' ]) == '["1", "3", "3"]'

    assert type(jsonify({ u'foo': u'bar' })) == text_type
    assert type(jsonify([ 1, 2, 3 ])) == text_type

    assert jsonify({ u'foo': u'bar' }, ensure_ascii=False) == u'{"foo": "bar"}'

# Generated at 2022-06-12 23:46:42.551992
# Unit test for function jsonify
def test_jsonify():
    test_data = {u'a': u'a', u'b': u'b'}
    test_data = container_to_text(test_data, encoding=None)
    json_string = jsonify(test_data)
    assert json_string == '{"a": "a", "b": "b"}'
    test_data = {u'a_\u3053': u'b_\u3053'}
    test_data = container_to_text(test_data, encoding="unicode_escape")
    json_string = jsonify(test_data)
    assert json_string == '{"a_\\\\u3053": "b_\\\\u3053"}'



# Generated at 2022-06-12 23:46:54.299192
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six import u

    class TestStr(text_type):
        pass

    class TestBytes(binary_type):
        pass

    class TestNonString(object):
        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return self.value

    class TestNonStringUnicode(object):
        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return self.value

    class TestNonStringBrokenUnicode(object):
        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return self.value

    # We have to use separate functions because they each have to have their
    # own globals. 

# Generated at 2022-06-12 23:47:46.825855
# Unit test for function to_bytes
def test_to_bytes():
    # Test text strings
    assert to_bytes('sømë tëxt') == b's\xc3\xb8m\xc3\xab t\xc3\xabxt'
    assert to_bytes(u'sømë tëxt') == b's\xc3\xb8m\xc3\xab t\xc3\xabxt'
    assert to_bytes(u's\xf8m\xeb t\xebxt') == b's\xc3\xb8m\xc3\xab t\xc3\xabxt'
    assert to_bytes(u's\u00F8m\u00EB t\u00EBxt') == b's\xc3\xb8m\xc3\xab t\xc3\xabxt'

# Generated at 2022-06-12 23:47:52.362558
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.common._collections_compat import StringIO
    import sys

    if PY3:
        if sys.version_info[1] >= 5:
            print("Running to_bytes tests from Python 3.5")
            test_to_bytes_35()
        else:
            print("Running to_bytes tests from Python 3.4")
            test_to_bytes_34()
    else:
        print("Running to_bytes tests from Python 2")
        test_to_bytes_2()

    def jsondump(obj):
        saveout = sys.stdout
        try:
            sys.stdout = StringIO()
            json.dump(obj, sys.stdout, sort_keys=True)
            return sys.stdout.getvalue()
        finally:
            sys.stdout = save

# Generated at 2022-06-12 23:48:03.104034
# Unit test for function to_bytes
def test_to_bytes():
    # For all the tests that specify an encoding, we use both the encoding and
    # None (which defaults to utf-8).  We use None as a convenience to users
    # who have no other specifiers as it allows them to call this without
    # quoting arguments
    assert b'123' == to_bytes(123)
    assert b'123' == to_bytes(123, encoding='latin-1')
    assert b'123' == to_bytes(123, 'latin-1')
    assert b'123' == to_bytes(123, errors='surrogate_or_replace')
    assert b'123' == to_bytes(123, encoding='latin-1', errors='surrogate_or_replace')
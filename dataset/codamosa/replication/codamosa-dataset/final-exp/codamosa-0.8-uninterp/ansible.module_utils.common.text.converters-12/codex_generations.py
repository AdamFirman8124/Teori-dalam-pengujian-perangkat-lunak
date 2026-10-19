

# Generated at 2022-06-12 23:38:26.467509
# Unit test for function jsonify
def test_jsonify():
    """Test jsonify() function."""
    from ansible.module_utils import basic

    data_dict = dict(
            str_item='text',
            int_item=10,
            list_item=[1, 2],
            dict_item=dict(a=1, b=2),
        )
    if not PY3:
        data_dict['unicode_item'] = unicode('unicode test')
    data_dict['bytestring_item'] = basic.to_bytes(b"bytestring test")
    data_dict['set_item'] = set([1, 2])
    data = jsonify(data_dict)

    import json
    # json.loads() works only with text
    if not PY3:
        data = basic.to_text(data)
    data = json.loads(data)

# Generated at 2022-06-12 23:38:37.144629
# Unit test for function jsonify
def test_jsonify():
    # Ensure we can dump a string with unicode utf-8
    assert jsonify('\xfc') == u'"\xfc"'
    # Ensure we can dump a string with unicode latin-1
    assert jsonify('\xfc'.decode('latin-1')) == u'"\xfc"'
    # Ensure we can dump a dictionary with unicode utf-8
    assert jsonify({'\xc3\xbc': 1}) == u'{"\xc3\xbc": 1}'
    # Ensure we can dump a dictionary with unicode latin-1
    assert jsonify({'\xfc': 1}.items()) == u'[["\xfc", 1]]'
    # UnicodeDecodeError should not be thrown since our last resort is to
    # use latin-1

# Generated at 2022-06-12 23:38:43.129841
# Unit test for function to_native
def test_to_native():
    """
    This function checks if the function to_native() works properly
    """
    try:
        import __builtin__
        to_native(__builtin__, nonstring='simplerepr')
    except AttributeError:
        to_native(__builtins__, nonstring='simplerepr')
    return True


# Generated at 2022-06-12 23:38:52.845550
# Unit test for function to_native
def test_to_native():
    """
    >>> from collections import namedtuple
    >>> Record = namedtuple('Record', ['x', 'y'])
    >>> record = Record(1, 2)
    >>> to_native(record, nonstring='simplerepr')
    "Record(x=1, y=2)"
    >>> to_native(record, nonstring='passthru') is record
    True
    >>> to_native(record, nonstring='empty')
    ''
    >>> to_native(record, nonstring='strict')
    Traceback (most recent call last):
    ...
    TypeError: obj must be a string type
    >>> to_native(record, nonstring='bad value')
    Traceback (most recent call last):
    ...
    TypeError: Invalid value bad value for to_native's nonstring parameter
    """

# Unit test

# Generated at 2022-06-12 23:38:55.293311
# Unit test for function to_native
def test_to_native():
    expected_result = 'ascii'
    test_input = u'ascii'
    assert to_native(test_input) == expected_result


# Generated at 2022-06-12 23:38:58.369032
# Unit test for function to_native
def test_to_native():
    assert to_native(u'text') == u'text'
    assert to_native(u'text'.encode('utf-8')) == u'text'


# Generated at 2022-06-12 23:39:03.523691
# Unit test for function jsonify
def test_jsonify():
    class Foo(object):
        def __repr__(self):
            return "foo"

    # dict
    assert jsonify({3: 2}) == '{"3": 2}'
    assert jsonify({3.0: 2}) == '{"3.0": 2}'
    assert jsonify({'a': 2}) == '{"a": 2}'
    assert jsonify({u'a': 2}) == '{"a": 2}'
    assert jsonify({3: 'a'}) == '{"3": "a"}'
    assert jsonify({3: u'a'}) == '{"3": "a"}'
    assert jsonify({'a': u'a'}) == '{"a": "a"}'
    assert jsonify({'a': None}) == '{"a": null}'

# Generated at 2022-06-12 23:39:11.823113
# Unit test for function to_bytes
def test_to_bytes():
    def tb(instr, encoding, errors='surrogate_or_replace', nonstring='simplerepr'):
        instr = instr + 'àßç'
        if PY3:
            instr = instr.encode('utf-8').decode('latin-1')
        else:
            if isinstance(instr, text_type):
                instr = instr.encode('latin-1')

        return to_bytes(instr, encoding=encoding, errors=errors, nonstring=nonstring)

    assert tb('hello', 'utf-8') == b'hello\xe0\xdf\xe7'
    assert tb('hello', 'latin-1') == b'hello\xe0\xdf\xe7'

    # Now we'll have surrogates

# Generated at 2022-06-12 23:39:16.327933
# Unit test for function jsonify
def test_jsonify():
    # Test for jsonify function
    x = {u'foo': u'hello world'}
    print("jsonify(x) : ", jsonify(x))
    print("jsonify(x, sort_keys=True) : ", jsonify(x, sort_keys=True))

test_jsonify()

# Generated at 2022-06-12 23:39:27.409363
# Unit test for function to_native
def test_to_native():
    # Note: We can't test for equality because the type of the return value
    # may be either a string or a unicode string.
    #
    # For the purposes of unit tests we'll assume that unicode on py2 and
    # str on py3 are stdlib docstrings.
    #
    # This should be valid for both py2 and py3
    assert 'foo' in to_text(to_bytes('foo'))
    assert 'foo' in to_text(to_bytes('foo'), encoding='ascii')
    assert 'føø' in to_text(to_bytes('føø'), encoding='latin-1')
    # This should throw on py2 and py3

# Generated at 2022-06-12 23:39:43.245064
# Unit test for function to_native
def test_to_native():
    def to_text_test(transformation, input_data, exp_output, exp_errors=None,
                     encoding='utf-8', errors=None, nonstring='simplerepr'):
        if exp_errors is None:
            exp_errors = {}

        if transformation == 'text':
            value = to_text(input_data, encoding, errors, nonstring)
        elif transformation == 'bytes':
            value = to_bytes(input_data, encoding, errors, nonstring)
        else:
            raise Exception('invalid transformation_type requested')

        if value != exp_output:
            print('to_%s(%r, %r, %r, %r) returned %r expected %r'
                  '' % (transformation, input_data, encoding, errors, nonstring, value, exp_output))


# Generated at 2022-06-12 23:39:54.402112
# Unit test for function to_bytes
def test_to_bytes():
    # Use a different encoding to check that encoding is done
    original_encoding = 'utf-8'
    expected_encoding = 'latin-1'

    # These examples should be valid utf-8

# Generated at 2022-06-12 23:40:03.887539
# Unit test for function to_bytes
def test_to_bytes():
    assert b'hello' == to_bytes(u'hello')
    assert b'\x92' == to_bytes(u'\u2019')
    assert b'\xe2\x80\x99' == to_bytes(u'\u2019', 'ascii', 'surrogate_or_replace')
    assert b'\xe2\x80\x99' == to_bytes(b'\xe2\x80\x99')
    assert b'\xe2\x80\x99' == to_bytes(b'\xe2\x80\x99', 'ascii', 'surrogate_or_replace')
    assert u'\N{SNOWMAN}'.encode('utf-8') == to_bytes(u'\N{SNOWMAN}')

# Generated at 2022-06-12 23:40:06.999967
# Unit test for function to_native
def test_to_native():
    '''
    format dict, list and int to json string
    '''
    assert to_native({"name": "xiaoming"}) == '{"name": "xiaoming"}'
    assert to_native(["name", "xiaoming"]) == '["name", "xiaoming"]'
    assert to_native(1) == '1'


# Generated at 2022-06-12 23:40:19.035510
# Unit test for function to_bytes

# Generated at 2022-06-12 23:40:26.904728
# Unit test for function to_bytes
def test_to_bytes():
    unicode_test = u'K∈ℌ'
    bytes_test = unicode_test.encode('utf-16')

    # unicode_test is unicode, no errors
    result = to_bytes(unicode_test)
    assert isinstance(result, binary_type)
    assert result == unicode_test.encode('utf-8')

    # bytes_test is bytes, no errors
    result = to_bytes(bytes_test)
    assert isinstance(result, binary_type)
    assert result == bytes_test

    # unicode test is unicode, unicode to utf-8 errors
    result = to_bytes(unicode_test, errors='surrogate_or_replace')
    assert isinstance(result, binary_type)

# Generated at 2022-06-12 23:40:38.526258
# Unit test for function to_native
def test_to_native():
    # to_native(obj, encoding='utf-8', nonstring='simplerepr')
    # assertEquals(self, first, second, msg=None)
    x = u'\u6d4b\u8bd5\u5b57\u7b26\u4e32'
    assertEquals(to_native(x),
        b'\xe6\xb5\x8b\xe8\xaf\x95\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2')

# Generated at 2022-06-12 23:40:49.585309
# Unit test for function jsonify
def test_jsonify():
    r = jsonify(dict(a=list(range(3)), b='a'))
    assert r == '{"a": [0, 1, 2], "b": "a"}'
    assert jsonify(dict(a=2, b='a', c={'c1': 'foo', 'c2': 'bar'}, d=dict(d1='foo', d2='bar'))) == '{"a": 2, "c": {"c1": "foo", "c2": "bar"}, "b": "a", "d": {"d1": "foo", "d2": "bar"}}'

# Generated at 2022-06-12 23:40:55.406009
# Unit test for function to_bytes
def test_to_bytes():
    # Note: We intentionally test bytes as strings to verify that we can pass
    # them through.  We also test nonstrings to verify that they work
    try:
        codecs.lookup_error('surrogateescape')
    except LookupError:
        surrogateescape_available = False
    else:
        surrogateescape_available = True

    def b(v):
        if surrogateescape_available:
            return v.encode('utf-8', 'surrogateescape').decode('utf-8', 'surrogateescape')
        else:
            # We can't use surrogateescape so we have to refer to it by name
            return v.encode('utf-8', 'surrogateescape').decode('utf-8', 'surrogateescape')


# Generated at 2022-06-12 23:41:04.124670
# Unit test for function to_bytes
def test_to_bytes():
    # We only test the 2.6 version of to_bytes
    from ansible.module_utils.basic import AnsibleFallbackNotUTF8Encoded

    # This is a shortcut to make sure that we have a surrogateescape error handler.
    # Otherwise the tests are skipped.
    if not HAS_SURROGATEESCAPE:
        raise AnsibleFallbackNotUTF8Encoded

    to_bytes('abc', 'utf-8')
    to_bytes('abc', 'utf-8', 'surrogateescape')
    to_bytes('abc', 'utf-8', 'surrogate_or_replace')
    to_bytes(b'abc')
    to_bytes(u'abc', 'utf-8')
    to_bytes(u'\u1234', 'utf-8')

# Generated at 2022-06-12 23:41:18.414006
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_text
    # Case: test with normal data
    data = {b'a': 1}
    assert jsonify(data) == '{"a": 1}'

    # Case: test with normal data
    data = {u'a': 1}
    assert jsonify(data) == '{"a": 1}'

    # Case: test with normal data
    data = {b'a': [u'b']}
    assert jsonify(data) == '{"a": ["b"]}'

    # Case: test with normal data
    data = {u'a': [b'b']}
    assert jsonify(data) == '{"a": ["b"]}'

    # Case: test with normal data
    data = {b'a': 1, u'b': 2}

# Generated at 2022-06-12 23:41:28.921662
# Unit test for function jsonify
def test_jsonify():
    #test bytes object
    input_data = b'{"test_key": "test_value"}'
    output_data = b'{"test_key": "test_value"}'
    assert jsonify(input_data) == output_data

    #test str object
    input_data = '{"test_key": "test_value"}'
    output_data = b'{"test_key": "test_value"}'
    assert jsonify(input_data) == output_data

    #test list container
    input_data = ['test_value', 'test_key']
    output_data = b'["test_value", "test_key"]'
    assert jsonify(input_data) == output_data

    #test tuple container
    input_data = ('test_value', True)

# Generated at 2022-06-12 23:41:40.056412
# Unit test for function jsonify
def test_jsonify():
    class simple_obj:
        def __init__(self, arg1, arg2, arg3):
            self.arg1 = arg1
            self.arg2 = arg2
            self.arg3 = arg3

        def __repr__(self):
            return "simple_obj(%s, %s, %s)" % (self.arg1, self.arg2, self.arg3)

    class complex_obj:
        def __init__(self):
            self.arg1 = {"a": "b",
                         "c": ["d", "e", "f"]}
            self.arg2 = "arg2"
            self.arg3 = [1, 2, 3]


# Generated at 2022-06-12 23:41:51.824444
# Unit test for function jsonify
def test_jsonify():
    import json
    import datetime
    # json.dumps() will return str on py2, str on py3
    expected = json.dumps('test').encode('utf-8')
    # This should be the same string as above
    result = jsonify('test')
    assert isinstance(result, bytes)
    assert result == expected

    # If we pass in something that is not unicode, it should be converted
    # and encoded to bytes
    expected = json.dumps('foobarbaz').encode('utf-8')
    result = jsonify(b'foobarbaz')
    assert isinstance(result, bytes)
    assert result == expected

    # If any of the keys or values are unicode, it should be decoded
    # and re-encoded to UTF8 bytes

# Generated at 2022-06-12 23:41:56.974323
# Unit test for function jsonify
def test_jsonify():
    # A tuple, list and set with ascii, latin1 and unicode characters.
    data = (('abc', 123), ['abc', 123], set(['abc', 123]))
    assert jsonify(data) == '[["abc", 123], ["abc", 123], ["abc", 123]]'
    assert jsonify(data, sort_keys=True) == '[["abc", 123], ["abc", 123], ["abc", 123]]'

    data = (('ábc', 123), ['ábc', 123], set(['ábc', 123]))
    assert jsonify(data) == '[["\\u00e1bc", 123], ["\\u00e1bc", 123], ["\\u00e1bc", 123]]'

# Generated at 2022-06-12 23:42:04.190538
# Unit test for function jsonify
def test_jsonify():
    # Test with 'normal' utf-8 string
    utf8_str = '{"foo": "bar"}'
    utf8_str_decoded = {"foo": "bar"}
    utf8_str_json = jsonify(utf8_str_decoded)
    assert utf8_str_json == utf8_str

    # Test involving a string with bad encoding
    bad_utf8_str = '{"foo": "bar", "baz": "föö"}'
    bad_utf8_except = False
    try:
        jsonify(bad_utf8_str)
    except UnicodeError:
        bad_utf8_except = True
    assert bad_utf8_except is True



# Generated at 2022-06-12 23:42:13.614157
# Unit test for function to_bytes
def test_to_bytes():
    # pylint: disable=too-many-locals
    import string

    try:
        u''.encode('utf-16')
        can_encode_utf16 = True
    except LookupError:
        # Some pythons have codecs that are incomplete
        can_encode_utf16 = False

    # Cribbed from /usr/share/dict/words

# Generated at 2022-06-12 23:42:17.983506
# Unit test for function jsonify
def test_jsonify():
    json_str = jsonify(['foo', {'bar': ('baz', None, 1.0, 2)}])
    assert json_str == '["foo", {"bar": ["baz", null, 1.0, 2]}]'


# JSON cannot handle set

# Generated at 2022-06-12 23:42:25.620663
# Unit test for function jsonify
def test_jsonify():
    dict_data = dict(a=to_bytes(u'\u2713'), b=[to_bytes(u'\u2713'), to_bytes(u'\U0001F68C')], c={'foo': to_bytes(u'\u2713')})
    assert u'\u2713' == json.loads(jsonify(dict_data))['a']
    assert u'\u2713' == json.loads(jsonify(dict_data))['b'][0]
    assert u'\U0001F68C' == json.loads(jsonify(dict_data))['b'][1]
    assert u'\u2713' == json.loads(jsonify(dict_data))['c']['foo']



# Generated at 2022-06-12 23:42:36.268263
# Unit test for function to_native
def test_to_native():
    """Sanity check the to_native function"""
    # The goal for to_native is to be the default encoding for python.  We
    # want it to be the same as str in both py2 and py3.  If you're reading
    # this and it's not true, please add a test case for your python version
    # and check it in with your test case.
    if PY3:
        expected_string = 'u\u001b[1;31municode\u001b[0m'
        expected_bytes = b'str'
    else:
        expected_string = u'unicode'
        expected_bytes = 'str'

    class Foo(object):
        def __str__(self):
            return expected_string

    foo = Foo()

    assert to_native(foo) == expected_string
    assert to

# Generated at 2022-06-12 23:42:52.231008
# Unit test for function to_native
def test_to_native():
    if PY3:
        assert (to_native(b'foo') == 'foo')
        assert (to_native(u'foo') == u'foo')
        assert (isinstance(to_native('foo'), str))
    else:
        assert (to_native(b'foo') == b'foo')
        assert (to_native(u'foo') == u'foo')
        assert (isinstance(to_native('foo'), unicode))
try:
    # For python >v3.3
    from json.encoder import JSONEncoder
    from json import JSONDecodeError
except ImportError:
    try:
        # For python v3.2
        from json import encoder
        JSONEncoder = encoder.JSONEncoder
        JSONDecodeError = ValueError
    except ImportError:
        pass



# Generated at 2022-06-12 23:42:54.325852
# Unit test for function jsonify
def test_jsonify():
    assert (jsonify({'foo':"\xe9"}) == '{"foo": "\\u00e9"}')
    assert (jsonify({'foo':'\xe9'}, ensure_ascii=False) == '{"foo": "\xe9"}')



# Generated at 2022-06-12 23:42:59.936382
# Unit test for function jsonify
def test_jsonify():
    """
    Test that the jsonify() function properly format the data in a JSON format,
    utf-8 as default, in unicode format.
    """
    test_input = {"str": "test", "other_str": "\xc3\xbcmlaut"}
    test_output = u'{"str": "test", "other_str": "\\u00fcmlaut"}'

    if PY3:
        assert jsonify(test_input, ensure_ascii=False) == test_output
    else:
        assert jsonify(test_input, ensure_ascii=False, encoding='latin-1') == test_output


#: :py:func:`container_to_text`
#:      Transforms a container (such as dictionaries) recursively to text.
#:      This is different than to_

# Generated at 2022-06-12 23:43:06.942793
# Unit test for function to_native
def test_to_native():
    assert to_native(b'asdf') == 'asdf'
    assert to_native('asdf') == 'asdf'
    assert to_native(5) == '5'
    assert to_native(u'\u043f\u0440\u0438\u0432\u0435\u0442') == u'\u043f\u0440\u0438\u0432\u0435\u0442'


# Generated at 2022-06-12 23:43:17.274903
# Unit test for function jsonify

# Generated at 2022-06-12 23:43:17.851824
# Unit test for function jsonify
def test_jsonify():
    pass


# Generated at 2022-06-12 23:43:23.792712
# Unit test for function to_bytes
def test_to_bytes():
    class Nonstring(object):
        def __repr__(self):
            return 'foo'
    class BadRepr(object):
        def __repr__(self):
            return '\u00bd'

    assert b'' == to_bytes(Nonstring(), nonstring='empty')
    assert b'foo' == to_bytes(Nonstring(), nonstring='simplerepr')
    assert Nonstring() == to_bytes(Nonstring(), nonstring='passthru')
    assert Nonstring() == to_bytes(Nonstring(), nonstring='passthru')
    raises(TypeError, to_bytes, Nonstring(), nonstring='strict')

    assert b'' == to_bytes(False, nonstring='empty')
    assert b'False' == to_bytes(False, nonstring='simplerepr')

# Generated at 2022-06-12 23:43:34.655112
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1, "b": "foo"}) == '{"a": 1, "b": "foo"}'
    assert jsonify([1, {"a": "foo"}]) == '[1, {"a": "foo"}]'
    assert jsonify({"a": 1, "b": ["foo", "bar"]}) == '{"a": 1, "b": ["foo", "bar"]}'
    assert jsonify(Set([1, 2, 3])) == '[1, 2, 3]'
    assert jsonify(datetime.datetime(2017, 11, 9, 8, 37, 48, 815353)) == '"2017-11-09T08:37:48.815353"'

# Generated at 2022-06-12 23:43:42.576253
# Unit test for function to_native
def test_to_native():
    test_str = u'\xc6\xa1'
    test_str_bytes = test_str.encode('utf-8')

# Generated at 2022-06-12 23:43:47.049605
# Unit test for function jsonify
def test_jsonify():
    assert isinstance(jsonify({'a': u'\u2603'}), text_type)
    assert isinstance(jsonify({'a': 'Montréal'}), text_type)
    assert isinstance(jsonify({'a': u'\u2603', 'b': 'Montréal'}), text_type)



# Generated at 2022-06-12 23:44:05.950452
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes('foo') == b'foo'
    assert to_bytes('foo'.encode('utf-16'), encoding='utf-8') == b'foo'
    assert to_bytes('foo'.encode('utf-16le'), encoding='utf-8') == b'foo'
    assert to_bytes(b'foo'.decode('latin-1')) == b'foo'
    assert to_bytes('foo'.encode('ascii'), encoding='latin-1', errors='surrogate_or_replace') == b'foo'
    assert to_bytes('foo'.encode('ascii'), encoding='ascii', errors='surrogate_or_replace') == b'foo'

# Generated at 2022-06-12 23:44:14.527550
# Unit test for function jsonify
def test_jsonify():
    assert to_bytes(jsonify({u'\u041b': u'\u0423\u0440'}), encoding='utf-8', errors='surrogate_then_replace') == b'{"\u041b": "\u0423\u0440"}'
    assert to_bytes(jsonify({u'\u041b': u'\u0423\u0440'}), encoding='iso-8859-1', errors='surrogate_then_replace') == b'{"\xc1\xcb": "\xcb\xe8\xf0"}'



# Generated at 2022-06-12 23:44:22.201272
# Unit test for function to_native
def test_to_native():
    """Make sure that a string is a text string on both py2 and py3."""
    if PY3:
        assert u'foo' == to_text(b'foo')
        assert u'foo' == to_text(u'foo')
        assert u'foo' == to_text(b'foo', errors='surrogate_then_replace')
        assert u'foo' == to_text(b'foo', errors='surrogate_or_strict')
        assert u'foo' == to_text(u'foo', errors='surrogate_then_replace')
        assert u'foo' == to_text(u'foo', errors='surrogate_or_strict')
        assert u'\udc80' == to_text(b'\x80', errors='surrogateescape')

# Generated at 2022-06-12 23:44:31.595266
# Unit test for function jsonify
def test_jsonify():

    class Person:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    data = {
        "nickname": "全栈",
        "name": "ansible",
        "age": 18,
        "person": Person("Person"),
        "job": "{'name': 'it'}",
        "list": ['中文', 'list'],
        "dict": {"key": "中文"},
        "se": Set([1, 2, 3]),
        "datetime": datetime.datetime.now(),
    }
    print(jsonify(data))
# test_jsonify()



# Generated at 2022-06-12 23:44:37.198250
# Unit test for function jsonify
def test_jsonify():
    data = {b"key": u"value"}
    data_out = {"key": "value"}
    data_json = '{"key": "value"}'
    assert jsonify(data) == data_json
    assert json.loads(jsonify(data)) == data_out


# Generated at 2022-06-12 23:44:47.085819
# Unit test for function to_bytes
def test_to_bytes():
    # Applies a surrogate pair
    assert to_bytes(u'\U0001F603', 'ascii', 'surrogate_then_replace') == b'\xf0\x9f\x98\x83'
    # BMP character
    assert to_bytes(u'\u03bc', 'ascii', 'surrogate_then_replace') == b'\xcf\xbc'
    # UTF-16 surrogate
    assert to_bytes(u'\udc81', 'ascii', 'surrogate_then_replace') == b'\xef\xbf\xbd'
    # Invalid UTF-8 encoded bytes

# Generated at 2022-06-12 23:44:58.264656
# Unit test for function to_native
def test_to_native():
    assert to_native(1, errors='surrogate_or_strict') == 1
    assert to_native(1, errors='surrogate_or_replace') == 1
    encoding = 'utf-16'
    if PY3:
        # Necessary for Python 3 as utf-16-le and utf-16-be don't have
        # a BOM and thus get decoded as utf-16
        encoding = 'utf-16-le'

    assert to_native('\u043f\u0440\u0438\u0432\u0456\u0442'.encode(encoding), encoding, 'surrogate_or_strict') == u'привіт'

# Generated at 2022-06-12 23:45:03.180857
# Unit test for function jsonify
def test_jsonify():
    assert '["couple", "family"]' == jsonify(Set(['couple', 'family']))
    x = {"1": Set(['couple', 'family'])}
    assert '{"1": ["couple", "family"]}' == jsonify(x)
    assert '["couple", "family"]' == jsonify(['couple', 'family'])



# Generated at 2022-06-12 23:45:10.992723
# Unit test for function to_bytes
def test_to_bytes():
    try:
        codecs.lookup_error('surrogateescape')
        HAS_SURROGATEESCAPE = True
    except LookupError:
        HAS_SURROGATEESCAPE = False
    if not HAS_SURROGATEESCAPE:
        surrogateescape_tests = set(('surrogate_or_strict',
                                     'surrogate_or_replace',
                                     'surrogate_then_replace'))
    else:
        surrogateescape_tests = set(('surrogateescape',))

# Generated at 2022-06-12 23:45:19.346916
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'key': 'value'}) == '{"key": "value"}'
    assert jsonify({'key': [1, 2, 3]}) == '{"key": [1, 2, 3]}'
    assert jsonify({'key': u'\u2603'}) == '{"key": "\\u2603"}'
    assert jsonify({u'\u2603': u'\u2603'}) == '{"\u2603": "\u2603"}'
    assert jsonify({u'\u2603': u'\u2603'}, ensure_ascii=False) == u'{"\u2603": "\u2603"}'



# Generated at 2022-06-12 23:45:33.218769
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({u"mykey": u"myvalue"}) == u'{"mykey": "myvalue"}'
    assert jsonify(u"myvalue") == u'"myvalue"'
    assert jsonify(u"myvalue") == u'"myvalue"'
    assert jsonify([1, 2, 3]) == u'[1, 2, 3]'
    assert jsonify(u"my\u20acvalue") == u'"my\u20acvalue"'
    assert jsonify({"mykey": u"my\u20acvalue"}) == u'{"mykey": "my\u20acvalue"}'


# Generated at 2022-06-12 23:45:41.971453
# Unit test for function to_native
def test_to_native():
    assert to_native('test', errors='surrogate_or_replace') == 'test'
    assert to_native(u'test\u1234', errors='surrogate_or_replace') == u'test\u1234'
    assert to_native(b'test\xe4\xbd\xa0', errors='surrogate_or_replace') == u'test\u4f60'
    assert to_native(b'test\x80\xe4\xbd\xa0', errors='surrogate_or_replace') == u'test\ufffd\u4f60'

    assert to_native('test', errors='surrogate_or_strict') == 'test'

# Generated at 2022-06-12 23:45:52.780948
# Unit test for function jsonify
def test_jsonify():
    assert isinstance(jsonify({'a': 'b'}), str)
    assert isinstance(jsonify({'a': 'b', u'b': u'c'}), str)
    assert isinstance(jsonify({b'a': b'b'}), str)
    assert isinstance(jsonify({b'a': b'b', u'b': u'c'}), str)
    assert isinstance(jsonify({u'a': u'b'}), str)
    assert isinstance(jsonify({u'a': u'b', u'b': u'c'}), str)
    assert isinstance(jsonify(u"\u2122"), str)
    assert isinstance(jsonify(b"\xe2\x84\xa2"), str)



# Generated at 2022-06-12 23:46:04.185599
# Unit test for function to_bytes
def test_to_bytes():
    for obj in (b'foo', 'foo'):
        assert to_bytes(obj) == b'foo'
    if PY3:
        assert to_bytes(text_type('\U0001f4a9')) == b'\xf0\x9f\x92\xa9'
    else:
        assert to_bytes(text_type('\U0001f4a9')) == b'\xef\xbf\xbd'
    assert to_bytes(2, nonstring='empty') == b''
    assert to_bytes(2, nonstring='passthru') == 2

# Generated at 2022-06-12 23:46:14.496662
# Unit test for function to_native
def test_to_native():

    # the goal of to_native is to make sure that we can consistently represent
    # a unicode string as an encoded bytestring
    s = u'snowman: ☃'

    # though no explicit encoding is used, default encoding is used to encode the unicode
    assert to_bytes(s) == b'snowman: \xe2\x98\x83'

    # here we explicitly tell to_native to utf-8 encode the string
    assert to_bytes(s, encoding='utf-8') == b'snowman: \xe2\x98\x83'

    # but the real magic is when we pass an encoded bytestring and an encoding
    assert to_bytes(to_bytes(s, encoding='utf-8'), encoding='utf-8') == b'snowman: \xe2\x98\x83'

    # if

# Generated at 2022-06-12 23:46:18.270655
# Unit test for function jsonify
def test_jsonify():
    obj = Set([1, 2])
    jstr = jsonify(obj)
    assert jstr == '["1", "2"]'

    class A:
        def __repr__(self):
            return u'\u2019'

    obj = A()
    jstr = jsonify(obj)
    assert jstr == '"\u2019"'
    jstr = jsonify(obj, ensure_ascii=False)
    assert jstr == u'"\u2019"'



# Generated at 2022-06-12 23:46:26.882456
# Unit test for function jsonify
def test_jsonify():
    '''
    jsonify should be able to take a unicode string and encode it.
    '''
    assert jsonify(u'test') == u'"test"'
    assert jsonify(u'\xe9') == u'"\\u00e9"'

    # Old systems using old simplejson module does not support encoding keyword.
    assert jsonify(b"\xc3\xb3") == u'"\\u00f3"'

    # Invalid unicode should fail.
    try:
        jsonify(u"\ufffd")
    except UnicodeError:
        pass
    else:
        assert False, "jsonify should have raised a UnicodeError"



# Generated at 2022-06-12 23:46:32.492591
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1, "b": "hello"}) == '{"a": 1, "b": "hello"}'
    assert jsonify({"a": 1, "b": "привіт"}) == '{"a": 1, "b": "привіт"}'
    assert jsonify({"a": 1, "b": u"привіт"}) == '{"a": 1, "b": "привіт"}'



# Generated at 2022-06-12 23:46:42.668245
# Unit test for function to_native
def test_to_native():
    # Test str() result
    assert to_native(u'привет, мир') == u'привет, мир'
    assert to_native('привет, мир') == u'привет, мир'
    assert to_native(1) == u'1'

    # Test repr() result
    assert to_native(u'привет\x85') == u'привет\\x85'
    assert to_native('привет\xc3') == u'привет\\xc3'

    # Test to_bytes() result

# Generated at 2022-06-12 23:46:54.517023
# Unit test for function to_bytes

# Generated at 2022-06-12 23:47:14.023867
# Unit test for function to_native
def test_to_native():
    # Test to_native's special handling of json_dicts and datetime.datetime
    if PY3:
        assert to_text(to_bytes('\u1234', encoding='ascii', errors='surrogateescape'),
                       encoding='ascii', errors='surrogateescape') == u'\ufffd'
    else:
        assert to_text(to_bytes('\u1234', encoding='ascii', errors='surrogateescape'),
                       encoding='ascii', errors='surrogateescape') == u'\u1234'
        # regression: to_text with surrogateescape should not be codepoint
        # sensitive for PY2

# Generated at 2022-06-12 23:47:24.698212
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_bytes, to_text


    # container_to_text should convert text and/or bytes in containers to text
    # and leave everything else unchanged.

    # Test list and tuple case
    assert jsonify([[1, 2], (to_bytes('foo'), 'bar')]) == '[["1", "2"], ["foo", "bar"]]'

    # Test set case
    assert jsonify(Set([to_bytes('foo'), 'bar'])) == '["foo", "bar"]'

    # Test dictionary case
    assert jsonify({'a': to_bytes('foo'), 'b': 'bar'}) == '{"a": "foo", "b": "bar"}'

    # Test dictionary with list of tuples case

# Generated at 2022-06-12 23:47:34.407589
# Unit test for function to_bytes
def test_to_bytes():
    u_normal = u'abcdé☃'
    b_normal = 'abcdé☃'
    u_surrogate = u'abcdé\udcba'
    b_surrogate = 'abcdé\udcba'
    u_surrogate_escaped = u'abcdé\\udcba'
    b_surrogate_escaped = 'abcdé\\udcba'
    u_invalid = u'abcdé\udcba'
    b_invalid_replace = 'abcdé\ufffd'
    # b_invalid_strict = 'abcdé\udcba'  # u'abcdé\udcba'.encode('utf8', 'strict')


# Generated at 2022-06-12 23:47:43.171130
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'bytes') == b'bytes'
    assert to_bytes(binary_type(b'bytes')) == b'bytes'
    assert to_bytes(u'unicode') == b'unicode'
    assert to_bytes(text_type(u'unicode')) == b'unicode'

    class UnicodeSubclass(text_type):
        pass

    assert to_bytes(UnicodeSubclass(u'unicode')) == b'unicode'

    class BinarySubclass(binary_type):
        pass

    assert to_bytes(BinarySubclass(b'bytes')) == b'bytes'

    assert to_bytes(UnicodeSubclass(u'\u8859')) == b'\xe8\xa1\x59'

# Generated at 2022-06-12 23:47:50.068908
# Unit test for function jsonify
def test_jsonify():
    type_test_data = [u'\xe9\x9d\xa2\xe5\x85\xb7\xe6\x9c\xba', 'test_str', 123]
    for each_data in type_test_data:
        try:
            assert jsonify(each_data)
        except UnicodeDecodeError:
            assert False
    assert jsonify(type_test_data) == jsonify(type_test_data)
    assert jsonify(
        {'test_str': 'test_str', 'test_none': None}, sort_keys=True) == jsonify(
        {'test_str': 'test_str', 'test_none': None}, sort_keys=True, indent=1)

# Generated at 2022-06-12 23:48:01.697282
# Unit test for function to_native
def test_to_native():

    assert to_native(u'value') == u'value'
    assert to_native(u'value'.encode('utf-8')) == u'value'
    assert to_native(u'value'.encode('utf-16')) == u'value'

    # non-ascii string
    assert to_native(u'\u2013'.encode('utf-8')) == u'\u2013'

    # non-string
    assert to_native([u'value']) == [u'value']
    assert to_native([u'value']) != ['value']
    assert to_native(['value']) == ['value']
    assert to_native({u'key': u'value'}) == {u'key': u'value'}

# Generated at 2022-06-12 23:48:09.314814
# Unit test for function to_bytes
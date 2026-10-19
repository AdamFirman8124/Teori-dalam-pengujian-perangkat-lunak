

# Generated at 2022-06-12 23:38:23.527318
# Unit test for function to_native
def test_to_native():
    # tests that to_native correctly produces a native string
    assert u'strings are already native' == to_native(u'strings are already native')
    assert u'bytes get converted to unicode' == to_native(b'bytes get converted to unicode')
    assert u'integers get converted as well' == to_native(123)
    # tests that to_native correctly handles encoding and decoding, ascribing errors to the
    # specified error handler
    assert u'caf\xe9' == to_native(b'caf\xc3\xa9', errors='surrogate_or_strict')
    assert u'caf\xfffd' == to_native(b'caf\xc3\xe9', errors='surrogate_or_strict')

# Generated at 2022-06-12 23:38:30.678888
# Unit test for function jsonify
def test_jsonify():
    # test utf-8 encoding
    assert jsonify({"a": "é"}, sort_keys=True) == '{"a": "\\u00e9"}'
    # test latin-1 encoding
    assert jsonify({"a": b"\xe9"}, sort_keys=True) == '{"a": "\\u00e9"}'
    # test complex object
    assert jsonify({"b": set([1, 2])}, sort_keys=True) == '{"b": [1, 2]}'
    # test datetime
    assert jsonify({"c": datetime.datetime(2017, 1, 4, 10, 11, 12, 0)}, sort_keys=True) == '{"c": "2017-01-04T10:11:12"}'



# Generated at 2022-06-12 23:38:33.603106
# Unit test for function jsonify
def test_jsonify():
    test_data = dict(a=b'\x80\x81\x82\x83', b=0x84, c=0x85)
    jsonify(test_data)


# Generated at 2022-06-12 23:38:36.360081
# Unit test for function to_native
def test_to_native():
    assert to_native(1) == '1'
    assert to_native(u'\u4321') == '\u4321'
    assert to_native(None) == 'None'


# Generated at 2022-06-12 23:38:48.473858
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": "b", b"c": "d", 3: "c"}) == '{"a": "b", "3": "c", "c": "d"}'
    assert jsonify({"a": "b", b"c": "d", "3": "c"}) == '{"a": "b", "3": "c", "c": "d"}'
    assert jsonify({"a": "b", b"c": b"d", "3": "c"}) == '{"a": "b", "3": "c", "c": "d"}'
    assert jsonify({3: "b", b"c": "d", "3": "c"}) == '{"3": "c", "c": "d"}'

# Generated at 2022-06-12 23:38:51.755455
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(42, nonstring='strict') == TypeError
    assert to_bytes(42, nonstring='passthru') == 42



# Generated at 2022-06-12 23:39:00.774255
# Unit test for function to_native
def test_to_native():
    encoding = 'utf-8'

    class FakeBytes:
        def __str__(self):
            return '👍'
        def encode(self, *args, **kwargs):
            return str(self).encode(*args, **kwargs)
    class FakeText:
        def __str__(self):
            return '👍'
        def encode(self, *args, **kwargs):
            raise Exception("FakeText.encode should not be called when to_text is called")
        def decode(self, *args, **kwargs):
            return str(self).encode(*args, **kwargs).decode(*args, **kwargs)

    assert to_text(b'', encoding=encoding).encode(encoding) == b''
    assert to_text('', encoding=encoding).encode(encoding)

# Generated at 2022-06-12 23:39:10.849333
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('',) == b''
    assert to_bytes('test') == b'test'
    assert to_bytes(b'test') == b'test'

    assert to_bytes(u'\u1234', encoding='utf-8') == b'\xe1\x88\xb4'
    assert to_bytes(u'\u1234', encoding='latin-1') == b'\xe1\x88\xb4'

    if HAS_SURROGATEESCAPE:
        assert to_bytes(u'\u1234', encoding='latin-1', errors='surrogateescape') == b'\udcc4'

# Generated at 2022-06-12 23:39:19.579833
# Unit test for function to_native

# Generated at 2022-06-12 23:39:29.853255
# Unit test for function jsonify
def test_jsonify():
    # test for utf-8 encoding
    inp_data = {u'a': u'\xf1'}
    out_data = jsonify(inp_data)
    out_data = json.loads(out_data)
    assert inp_data == out_data
    # test for iso-8859-1 encoding
    inp_data = {u'a': u'\xf1'}
    out_data = jsonify(inp_data)
    out_data = json.loads(out_data)
    assert inp_data == out_data
    # test for non-encodable data
    inp_data = {u'a': {u'b': 1}}

# Generated at 2022-06-12 23:39:43.856199
# Unit test for function to_native
def test_to_native():
    """
    :py3_only:
    """
    stream = io.StringIO()
    try:
        sys.stdout = stream
        stdout = io.StringIO()
        sys.stdout.write(b'foo\n')
    except:
        pass
    else:
        raise AssertionError("sys.stdout.write of a byte string should have raised a TypeError")
    finally:
        sys.stdout = sys.__stdout__

    stream = io.StringIO()
    try:
        sys.stdout = stream
        stdout = io.StringIO()
        sys.stdout.write('foo\n')
    except:
        raise AssertionError("sys.stdout.write of a text string should not have raised a TypeError")

# Generated at 2022-06-12 23:39:48.145493
# Unit test for function jsonify
def test_jsonify():
    data = {'a': 'b', 'c': None}
    text = jsonify(data)
    assert text == u'{"a": "b", "c": null}'
    assert text == jsonify(data, sort_keys=True)



# Generated at 2022-06-12 23:39:57.328232
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 'ascii_only'}) == '{"a": "ascii_only"}'
    assert jsonify({'b': b'using_latin1'}) == '{"b": "using_latin1"}'
    assert jsonify({'c': u'using_utf8'}) == '{"c": "using_utf8"}'
    assert jsonify({'d': u'\u062a\u0648\u0636\u06cc\u062d'}) == '{"d": "\\u062a\\u0648\\u0636\\u06cc\\u062d"}'

# Generated at 2022-06-12 23:40:06.153506
# Unit test for function to_bytes
def test_to_bytes():
    assert isinstance(to_bytes(''), binary_type)
    assert to_bytes('') == b''
    assert isinstance(to_bytes(b''), binary_type)
    assert to_bytes(b'') == b''
    assert isinstance(to_bytes(u''), binary_type)
    assert to_bytes(u'') == b''

    assert isinstance(to_bytes(b'\xff'), binary_type)
    assert to_bytes(b'\xff') == b'\xff'
    assert isinstance(to_bytes(u'\uffff'), binary_type)
    assert to_bytes(u'\uffff') == b'\xff'
    assert isinstance(to_bytes(u'\uffff', encoding='latin-1'), binary_type)

# Generated at 2022-06-12 23:40:18.924644
# Unit test for function to_bytes
def test_to_bytes():
    def _test_to_bytes(text, expected_bytes, encoding, errors, nonstring):
        result = to_bytes(text, encoding=encoding, errors=errors, nonstring=nonstring)
        assert result == expected_bytes
    # Basic text to bytes
    _test_to_bytes('\xe9', b'\xc3\xa9', 'utf-8', 'strict', 'simplerepr')
    # Basic text to bytes that's badly encoded
    _test_to_bytes('\xe9', b'?', 'ascii', 'strict', 'simplerepr')
    # Basic bytes to bytes
    _test_to_bytes(b'\xc3\xa9', b'\xc3\xa9', 'utf-8', 'strict', 'simplerepr')
    # badly encoded bytes to bytes
    _test

# Generated at 2022-06-12 23:40:22.009931
# Unit test for function jsonify
def test_jsonify():
    test_data = {
                 'status': True,
                 'results': [
                             {'name': u'日本語'},
                             {'name': u'日本語'},
                            ],
                }
    encoded_data = jsonify(test_data)
    import json
    assert json.loads(encoded_data) == test_data



# Generated at 2022-06-12 23:40:23.316778
# Unit test for function jsonify
def test_jsonify():
    jsonify({'b': [1, 2, 3], 'a': {'x': 11, 'y': 12}})



# Generated at 2022-06-12 23:40:32.030288
# Unit test for function jsonify
def test_jsonify():
    data = {'a': [1, 2, 3], 'b': {'one': 1, 'two': 2}}
    assert data == json.loads(jsonify(data))
    data = {'a': [1, 2, text_type("příliš žluťoučký kůň úpěl ďábelské ódy")]}
    assert data == json.loads(jsonify(data))


# Exceptions


# Generated at 2022-06-12 23:40:39.298871
# Unit test for function jsonify
def test_jsonify():
    # An example of a dict that can not be converted with json.dumps
    data = {u'Atm\xe9tho\xe2t\xea_18': u'\xa0s\xf3la'}
    # An expected result which is encoded with utf-8 in the first try
    expectation = '{"Atm\xc3\xa9tho\xc3\xa2t\xc3\xaa_18": "\xc2\xa0s\xc3\xb3la"}'
    assert jsonify(data) == expectation


# Generated at 2022-06-12 23:40:50.059314
# Unit test for function jsonify
def test_jsonify():
    import pytest

    def _test(data):
        assert data == json.loads(jsonify(data))

    _test(dict(a='b', b=5, c=['a', u'b', u'\u2297', '\xc3\xa9']))
    _test([u'\u2297', u'\u2297', '\xc3\xa9'])
    _test([u'\u2297', '\xc3\xa9'])
    _test(dict(a='b'))
    _test([u'a'])
    _test(u'a')
    _test([u'a', dict(b=[dict(c=u'd')])])
    _test(dict(c=['\xc3\xa9']))

# Generated at 2022-06-12 23:41:16.833648
# Unit test for function jsonify
def test_jsonify():
    data = {
        'unicode': u'\u2713',
        'bytestring': b'\xe2\x9c\x93',
        'datetime': datetime.datetime(1991, 5, 1, 14, 25, 5),
        'nested': {
            'unicode': u'\u2713',
            'bytestring': b'\xe2\x9c\x93',
            'list': [u'\u2713', b'\xe2\x9c\x93'],
        }
    }

# Generated at 2022-06-12 23:41:28.395668
# Unit test for function jsonify
def test_jsonify():
    data = {
        b'foo': b'\xe2\x98\x83',
        'bar': b'\xe2\x98\x83',
    }
    out = jsonify(data)
    assert isinstance(out, text_type)
    assert isinstance(out, text_type)
    assert json.loads(out) == {u'foo': u'\u2603', u'bar': u'\u2603'}

    data = {
        b'foo': [b'\xe2\x98\x83'],
        'bar': [b'\xe2\x98\x83'],
    }
    out = jsonify(data)
    assert isinstance(out, text_type)

# Generated at 2022-06-12 23:41:32.344401
# Unit test for function jsonify
def test_jsonify():
    import json
    data = {
        b'binary': b'value'
    }
    res = jsonify(data)
    assert json.loads(res) == {
        'binary': 'value'
    }


# Generated at 2022-06-12 23:41:42.311026
# Unit test for function jsonify
def test_jsonify():
    ''' test jsonify '''

    # Use Set, Datetime
    data = {'a': Set(['c', 'b', 'a']), 'b': datetime.datetime(2016, 12, 8, 9, 15, 16, 281925)}
    result = jsonify(data)
    assert result == '{"a": ["c", "b", "a"], "b": "2016-12-08T09:15:16.281925"}'

    # String already encoded
    data = {'a' : b'foo'}
    result = jsonify(data)
    assert result == '{"a": "foo"}'

    # UnicodeDecodeError: 'ascii' codec can't decode byte
    data = {'a' : b'\xc2\xa3'}
    result = jsonify(data)
   

# Generated at 2022-06-12 23:41:48.709668
# Unit test for function jsonify
def test_jsonify():
    data = {
        "a": {
            "b": "c"
        },
        "d": ["e"],
        "f": set(["g"])
    }
    my_json = '{"a": {"b": "c"}, "f": ["g"], "d": ["e"]}'
    assert (my_json == jsonify(data))


# Generated at 2022-06-12 23:41:58.627352
# Unit test for function jsonify
def test_jsonify():
    test_data = {
        u"f\xc3\xb8\xc3\xb8": u"foo bar",
        u"b\xc3\xa5r": u"foo baz",
        u"\xc3\xa5\xc3\xa5": u"n\xc3\xb8g",
        }
    json_data = jsonify(test_data)
    assert isinstance(json_data, str)
    assert json_data == '{"b\xc3\xa5r": "foo baz", "f\xc3\xb8\xc3\xb8": "foo bar", "\xc3\xa5\xc3\xa5": "n\xc3\xb8g"}'



# Generated at 2022-06-12 23:42:09.289123
# Unit test for function to_bytes
def test_to_bytes():
    class TestObject:
        def __repr__(self):
            return repr(u'\u1234')

    assert to_bytes(True) == b'true'
    assert to_bytes('hello') == b'hello'
    assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    assert to_bytes(TestObject()) == b'\xe1\x88\xb4'

    # Non-standard error handlers
    assert to_bytes(u'\u1234', errors='surrogate_or_strict') == b'\xe1\x88\xb4'
    assert to_bytes(u'\u1234', errors='surrogate_or_replace') == b'\xe1\x88\xb4'

# Generated at 2022-06-12 23:42:18.987390
# Unit test for function to_bytes
def test_to_bytes():
    return_string = to_bytes(u'abc')
    assert isinstance(return_string, binary_type)
    return_string = to_bytes(u'abc', errors='strict')
    assert isinstance(return_string, binary_type)
    return_string = to_bytes(u'abc', errors='surrogate_or_strict')
    assert isinstance(return_string, binary_type)
    return_string = to_bytes(u'abc', errors='ignore')
    assert isinstance(return_string, binary_type)
    return_string = to_bytes(u'abc', errors='replace')
    assert isinstance(return_string, binary_type)
    return_string = to_bytes(u'abc', errors='surrogate_or_replace')

# Generated at 2022-06-12 23:42:26.903192
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'hola') == b'hola'
    assert to_bytes(b'hola') == b'hola'
    assert to_bytes(u'h\ufffdo', nonstring='passthru') == u'h\ufffdo'
    assert to_bytes(None) == b''
    assert to_bytes(u'h\ufffdo', errors='ignore') == b'hdo'
    if PY3:
        # Python 3 ignores surrogates when encoding non utf-8
        assert to_bytes(u'h\ufffdo', encoding='ascii', errors='ignore') == b'hdo'

# Generated at 2022-06-12 23:42:37.786632
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(None) == b''
    assert to_bytes(None, nonstring='passthru') is None
    assert to_bytes(None, nonstring='strict') == b''
    assert to_bytes(None, nonstring='empty') == b''
    assert to_bytes(False) == b'False'
    assert to_bytes(False, nonstring='passthru') is False
    assert to_bytes(False, nonstring='strict') == b'False'
    assert to_bytes(False, nonstring='empty') == b'False'
    assert to_bytes(1) == b'1'
    assert to_bytes(1, nonstring='passthru') == 1
    assert to_bytes(1, nonstring='strict') == b'1'

# Generated at 2022-06-12 23:42:49.981958
# Unit test for function to_native
def test_to_native():
    """
    Test function to_native
    """
    from ansible.module_utils._text import to_native
    native_val = to_native("")
    assert type(native_val) is str


# Generated at 2022-06-12 23:42:58.704649
# Unit test for function to_native
def test_to_native():
    string_types = (bytes, str)
    try:
        str('string')
        unicode
    except NameError:
        pass
    else:
        string_types = string_types + (unicode,)

    nonstring_types = (bool, int, float, complex, datetime.datetime,
                       datetime.timedelta, set, frozenset, list, tuple, bytearray,
                       memoryview)
    try:
        long
    except NameError:
        pass
    else:
        nonstring_types = nonstring_types + (long,)

    try:
        from collections import OrderedDict
    except ImportError:
        pass
    else:
        nonstring_types = nonstring_types + (OrderedDict,)

    if PY3:
        nonstring_types = nonstring_types

# Generated at 2022-06-12 23:43:04.016251
# Unit test for function jsonify
def test_jsonify():
    test_data = {
        "list": [
            "foo",
            "bar"
        ],
        "a": 1,
        "b": 2
    }
    new_data = jsonify(test_data)
    assert new_data == '{"a": 1, "b": 2, "list": ["foo", "bar"]}'



# Generated at 2022-06-12 23:43:13.266700
# Unit test for function to_bytes
def test_to_bytes():
    # Test the different options for errors
    utf8_b = to_bytes(u'\u2222\u1111')

    expected_b = b'\xe2\x88\xa2\xe1\x84\x91'
    assert to_bytes(utf8_b, 'latin-1') == utf8_b
    assert to_bytes(utf8_b, 'latin-1', 'strict') == utf8_b
    assert to_bytes(utf8_b, 'latin-1', 'ignore') == b''
    assert to_bytes(utf8_b, 'latin-1', 'replace') == b'???'
    assert to_bytes(utf8_b, 'latin-1', 'xmlcharrefreplace') == b'&#8986;&#4369;'
   

# Generated at 2022-06-12 23:43:21.889460
# Unit test for function jsonify
def test_jsonify():
    def _test_encode(data):
        encoded = jsonify(data)

# Generated at 2022-06-12 23:43:33.075629
# Unit test for function to_bytes
def test_to_bytes():
    # Make sure that we don't traceback when trying to encode objects with
    # surrogates
    class TestObj(object):
        def __repr__(self):
            return u'\u0001'

        def __str__(self):
            return u'\u0001'

    class TestUnicodeSubclass(text_type):
        def __str__(self):
            return u'\u0001'

    class TestUnicodeSubclass2(text_type):
        def __str__(self):
            return u'\u0001'

    class TestUnicodeSubclass3(text_type):
        def __str__(self):
            return u'\u0001'

    class TestUnicodeSubclass4(text_type):
        def __str__(self):
            return u'\u0001'

   

# Generated at 2022-06-12 23:43:41.484824
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils._text import to_bytes

    def _to_bytes_defaults(obj):
        return to_bytes(obj)
    def _to_bytes_defaults_surrogate_then_replace(obj):
        return to_bytes(obj, errors='surrogate_then_replace')

    # Try simple strings that should work
    assert to_bytes('hello') == b'hello'
    assert to_bytes(u'hello') == b'hello'
    assert to_bytes(b'hello') == b'hello'
    assert to_bytes(bytearray(b'hello')) == b'hello'

    # We can't really test this as we don't know if surrogateescape is available
    #assert to_bytes(u'\udcd6') == b'\udcd6'

    # Test

# Generated at 2022-06-12 23:43:51.220701
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_bytes
    import json
    import copy
    import datetime

    data = {to_bytes('foo'): [1, 2, 3], to_bytes('bar'): {to_bytes('baz'): to_bytes('hello')}}
    assert json.loads(jsonify(data)) == {'foo': [1, 2, 3], 'bar': {'baz': 'hello'}}
    assert jsonify(data) == '{"foo": [1, 2, 3], "bar": {"baz": "hello"}}'

    data = {to_bytes('foo'): [1, 2, 3], to_bytes('bar'): {to_bytes('baz'): to_bytes('hello')}}
    data = Set(data.keys())

# Generated at 2022-06-12 23:43:52.760294
# Unit test for function jsonify
def test_jsonify():
    data = {'a': 'b', u'c': u'd'}
    print(jsonify(data))




# Generated at 2022-06-12 23:44:05.729660
# Unit test for function jsonify
def test_jsonify():
    assert u'"\u3042"' == jsonify(u"\u3042")
    assert u'"\u3042"' == jsonify(u"\u3042".encode("utf-8"))
    assert u'"\u3042"' == jsonify(u"\u3042".encode("latin-1"))
    assert u'"\u3042"' == jsonify(u"\u3042".encode("utf-16"))
    assert u'"\u3042"' == jsonify(u"\u3042".encode("utf-16-le"))
    assert u'"\u3042"' == jsonify(u"\u3042".encode("utf-16-be"))
    assert u'"\u3042"' == jsonify(u"\u3042".encode("utf-32"))

# Generated at 2022-06-12 23:44:16.835583
# Unit test for function jsonify
def test_jsonify():
    assert '"a"' == jsonify('a')
    assert '["a"]' == jsonify(['a'])
    assert '{"a": "a"}' == jsonify({'a': 'a'})
    assert '["abc/def"]' == jsonify(['abc/def'])



# Generated at 2022-06-12 23:44:28.185038
# Unit test for function to_native

# Generated at 2022-06-12 23:44:30.145662
# Unit test for function jsonify
def test_jsonify():
    data = {'a': 1, 'b': [1,2,3]}
    assert jsonify(data) == '{"a":1,"b":[1,2,3]}'


# Generated at 2022-06-12 23:44:40.718728
# Unit test for function jsonify
def test_jsonify():
    # Test by comparing a complex data structure to a jsonified,
    # and then de-jsonified, version of the original data structure.
    # The two should always be the same.
    assert jsonify(json.load(open("tests/jsonify_test.json"))) \
        == json.dumps(json.load(open("tests/jsonify_test.json")))
    assert jsonify(json.loads('{}')) == jsonify({})
    assert jsonify(json.loads('[]')) == jsonify([])
    assert jsonify(json.loads('"foo"')) == jsonify("foo")
    assert jsonify(json.loads('1')) == jsonify(1)


# Generated at 2022-06-12 23:44:49.261712
# Unit test for function to_native
def test_to_native():
    '''
    Test to_native()
    '''
    from ansible.module_utils._text import to_native
    def check(s):
        assert(s)

    # Test a normal string
    check(to_native('hello world'))

    # Test a native string
    check(to_native(u'hello world'))

    # Test with non-UTF-8 encoding
    check(to_native('hello world', encoding='ascii'))

    # Test with non-UTF-8 encoding
    check(to_native('hello world', encoding='latin-1'))

    # Test with a surrogate
    check(to_native(u'\udcff'))

    # Test with non-UTF-8 encoding and a surrogate
    # NOTE: This will fail on Python 2 because we don't know how to handle
   

# Generated at 2022-06-12 23:44:59.539298
# Unit test for function jsonify
def test_jsonify():
    result = jsonify({"f": "€"})
    assert json.loads(result).get('f') == u'€'

    assert jsonify({"f": "€"}, ensure_ascii=True) == '{"f": "\\\\u20ac"}'

    assert jsonify({"f": "€"}, ensure_ascii=False) == u'{"f": "€"}'

    assert jsonify({"f": "€"}, ensure_ascii=False) == u'{"f": "€"}'

    assert jsonify({"f": "€"}, ensure_ascii=False, sort_keys=True) == u'{"f": "€"}'


# Generated at 2022-06-12 23:45:08.725076
# Unit test for function to_bytes
def test_to_bytes():
    # Test the easy cases (byte string and unicode)
    try:
        value = unicode('Iñtërnâtiônàlizætiøn', 'utf-8')
    except NameError:
        value = 'Iñtërnâtiônàlizætiøn'

    result = to_bytes(value)
    assert isinstance(result, binary_type)
    assert result == bytes(value, 'utf-8')

    result = to_bytes(result)
    assert isinstance(result, binary_type)
    assert result == bytes(value, 'utf-8')

    # Test non-string (and non-byte-string) values
    result = to_bytes(1)
    assert isinstance(result, binary_type)
    assert result == b'1'

    result = to_

# Generated at 2022-06-12 23:45:16.947553
# Unit test for function jsonify
def test_jsonify():
    # Test with a string
    assert '"foo"' == jsonify('foo')
    # Test with a dict containing strings
    assert '{"foo": "bar"}' == jsonify({'foo': 'bar'})
    # Test with a list of strings
    assert '["foo", "bar"]' == jsonify(['foo', 'bar'])
    # Test with a Set
    assert '["foo", "bar"]' == jsonify(Set(['foo', 'bar']))
    # Test with a datetime
    date = datetime.datetime(2016, 6, 30, 15, 52, 44, 717998)
    assert '"2016-06-30T15:52:44.717998"' == jsonify(date)
    # Test with a non-string

# Generated at 2022-06-12 23:45:22.652365
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native

# Generated at 2022-06-12 23:45:29.270868
# Unit test for function jsonify
def test_jsonify():
    D = {1: 'a', '2': None, '3': [1, 'a'], '4': {'a': 'b'}}
    jsonify(D)
    jsonify({1: 'a', '2': to_bytes('字符串'), '3': [1, 'a']})
    jsonify(D, skipkeys=True)
    jsonify(D, ensure_ascii=True)
    jsonify(D, check_circular=True)
    jsonify(D, allow_nan=False)
    jsonify(D, cls=None)
    jsonify(D, indent=4)
    jsonify(D, separators=(',', ':'))
    jsonify(D, encoding='utf-8', default=_json_encode_fallback)

# Generated at 2022-06-12 23:45:55.822097
# Unit test for function to_bytes
def test_to_bytes():
    # These are all byte strings
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(b'\xff') == b'\xff'
    assert to_bytes(b'\xc3\xbc') == b'\xc3\xbc'

    # These are all text strings
    assert to_bytes('abc') == b'abc'
    assert to_bytes('\xff') == b'\xff'
    assert to_bytes('\xc3\xbc') == b'\xc3\xbc'
    assert to_bytes(u'abc') == b'abc'
    assert to_bytes(u'\u8765') == b'\xe8\xbd\xa5'

# Generated at 2022-06-12 23:45:58.740421
# Unit test for function to_native
def test_to_native():
    obj = u'\\u1234'
    assert obj == to_text(obj)
    assert b'\\u1234' == to_bytes(obj)


# Generated at 2022-06-12 23:46:10.480616
# Unit test for function to_bytes
def test_to_bytes():
    assert b'123' == to_bytes('123', encoding='ascii')

    assert b'123' == to_bytes(b'123', encoding=None)
    assert b'123' == to_bytes(u'123', encoding=None)

    assert b'123' == to_bytes(b'123', encoding='ascii')
    assert b'123' == to_bytes(u'123', encoding='ascii')

    assert u'\ufffd'.encode('utf-8') == to_bytes('\U0001d120', encoding='ascii')
    assert u'\ufffd'.encode('utf-8') == to_bytes(u'\U0001d120', encoding='ascii')

# Generated at 2022-06-12 23:46:14.308085
# Unit test for function to_native
def test_to_native():
    pass


try:
    from collections import UserString

    class _UnicodeType(text_type, UserString):
        pass
except ImportError:
    class _UnicodeType(text_type):
        pass


# Backwards compat
native_ = _UnicodeType



# Generated at 2022-06-12 23:46:23.956082
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1, b=2), sort_keys=True) == '{"a": 1, "b": 2}'
    assert jsonify(['a', 'b']) == '["a", "b"]'
    assert jsonify('abc') == '"abc"'
    assert jsonify({'b': [1, 2], 'a': 0}) == '{"a": 0, "b": [1, 2]}'
    # This requires utf-8 to be the default encoding
    assert jsonify([to_bytes(u'\xe9', encoding='latin-1')]) == '["\\u00e9"]'


# Generated at 2022-06-12 23:46:32.566235
# Unit test for function to_native
def test_to_native():
    assert to_native("test") == "test"
    assert to_native(u"test") == "test"
    assert to_native("test") == b"test"
    assert to_native("test", method='smart') == "test"
    assert to_native("test", method='byte') == b"test"
    assert to_native("test", method='smart') == u"test"
    assert to_native("test", method='byte') == b"test"
    assert to_native(u"test", method='smart') == "test"
    assert to_native(u"test", method='byte') == b"test"
    assert to_native([b"test"], method='smart') == [u"test"]
    assert to_native([u"test"], method='smart') == [u"test"]
    assert to_native

# Generated at 2022-06-12 23:46:37.224496
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1, "b": "füübär", "c": 1, "d": 1}) == '{"a": 1, "b": "f\\u00fc\\u00fcb\\u00e4r", "c": 1, "d": 1}'



# Generated at 2022-06-12 23:46:44.973843
# Unit test for function jsonify
def test_jsonify():
    valid_utf8 = {u"v\xe4lid": "utf-8"}
    try:
        jsonify(valid_utf8)
    except Exception as e:
        raise AssertionError('jsonify() fails with valid utf-8 data %s: %s' % (valid_utf8, e))

    invalid_utf8 = {'invalid': u"v\xe4lid".encode('latin-1')}
    try:
        jsonify(invalid_utf8)
    except UnicodeDecodeError:
        pass
    except Exception as e:
        raise AssertionError('jsonify() fails with invalid utf-8 data %s: %s' % (invalid_utf8, e))



# Generated at 2022-06-12 23:46:56.473149
# Unit test for function jsonify
def test_jsonify():
    assert jsonify("hello world") == '"hello world"'
    assert jsonify("привіт світ") == '"\u043f\u0440\u0438\u0432\u0456\u0442 \u0441\u0432\u0456\u0442"'
    assert jsonify("שלום") == '"\u05e9\u05dc\u05d5\u05dd"'
    assert jsonify(["hello world"]) == '["hello world"]'
    assert jsonify(("hello world",)) == '["hello world"]'
    assert jsonify({"a": "hello"}) == '{"a": "hello"}'

# Generated at 2022-06-12 23:47:06.952586
# Unit test for function to_bytes
def test_to_bytes():
    # pylint: disable=consider-iterating-dictionary
    assert to_bytes(b'12345') == b'12345'
    for nonstring in ('empty', 'simplerepr', 'passthru'):
        assert to_bytes(12345, nonstring=nonstring) == to_bytes(u'12345')
    assert to_bytes(b'12345', nonstring='passthru') == b'12345'
    assert to_bytes(b'12345', nonstring='empty') == b''
    try:
        to_bytes(12345, nonstring='strict')
    except TypeError:
        pass
    else:
        assert False, 'to_bytes should have raised an exception on nonstring=strict'

    # Test that surrogate_or_replace works as expected

# Generated at 2022-06-12 23:47:35.199395
# Unit test for function to_bytes
def test_to_bytes():
    # Test that we can encode text strings
    assert to_bytes('a') == b'a'
    assert to_bytes(u'a') == b'a'
    assert to_bytes('\xe2\x82\xac') == b'\xe2\x82\xac'
    assert to_bytes(u'\xe2\x82\xac') == b'\xe2\x82\xac'

    assert to_bytes(u'\xe2') == b'\xc3\xa2'
    assert to_bytes(u'\uFFFE') == b'\xef\xbf\xbe'

    # Test that we can decode byte strings
    assert to_bytes(b'a') == b'a'

# Generated at 2022-06-12 23:47:43.882127
# Unit test for function to_bytes
def test_to_bytes():
    # Test the function manually
    assert b'hello' == to_bytes('hello')
    assert b'hello' == to_bytes(u'hello')
    assert b'\xc3\xbc' == to_bytes(u'\xfc', encoding='utf-8')
    assert b'\xc3\xbc' == to_bytes(u'\xfc', encoding='latin-1')
    assert b'\xfc' == to_bytes(b'\xfc', encoding='utf-8', nonstring='passthru')
    assert b'\xfc' == to_bytes(b'\xfc', encoding='latin-1', nonstring='passthru')
    assert b'\xc3\xbc' == to_bytes(b'\xfc', encoding='utf-8')

# Generated at 2022-06-12 23:47:46.941002
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_bytes
    assert to_bytes('{"key": "value"}') == jsonify({u'key': u'value'})
    assert to_bytes('{"key": "value"}') == jsonify({'key': 'value'})


# Generated at 2022-06-12 23:47:48.647818
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1, b=2, c=None)) == '{"a": 1, "b": 2, "c": null}'



# Generated at 2022-06-12 23:48:00.127838
# Unit test for function to_bytes
def test_to_bytes():
    def test_encode(obj, encoding, errors=None, nonstring='simplerepr'):
        return to_bytes(obj, encoding, errors, nonstring)

    # to_bytes with a surrogate in the source text when surrogateescape is
    # available.
    surrogate = u'\udc80'
    if HAS_SURROGATEESCAPE:
        assert test_encode(surrogate, 'ascii', 'surrogateescape') == b'\x80'
        assert test_encode(surrogate, 'ascii', 'surrogate_or_strict') == b'\x80'
        assert test_encode(surrogate, 'ascii', 'surrogate_or_replace') == b'\x80'

# Generated at 2022-06-12 23:48:07.524226
# Unit test for function jsonify
def test_jsonify():
    # test for normal text
    str_data = {"key": "value"}
    assert jsonify(str_data) == '{"key": "value"}'

    # test for unicode text
    unicode_data = {"key": u"val\u1234ue"}
    assert jsonify(unicode_data) == '{"key": "val\\u1234ue"}'

    # test for text in a container
    container_data = {"key": ["val\u1234ue_1", u"val\u1234ue_2"]}
    assert jsonify(container_data) == '{"key": ["val\\u1234ue_1", "val\\u1234ue_2"]}'


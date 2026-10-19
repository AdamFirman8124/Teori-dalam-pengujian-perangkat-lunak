

# Generated at 2022-06-12 23:38:28.796492
# Unit test for function to_bytes
def test_to_bytes():
    """ Unit test for function to_bytes"""

# Generated at 2022-06-12 23:38:36.759579
# Unit test for function to_bytes
def test_to_bytes():
    utf8obj = 'the execution of this module is failing'

    check = to_bytes(utf8obj)
    try:
        check = to_bytes(utf8obj, encoding='latin-1')
    except UnicodeEncodeError:
        pass

    utf8obj = '\xe4\xbd\xa0\xe5\xa5\xbd'
    check = to_bytes(utf8obj, errors='surrogateescape')

    utf8obj = b'\xe4\xbd\xa0\xe5\xa5\xbd'
    check = to_bytes(utf8obj)



# Generated at 2022-06-12 23:38:48.856933
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('hello world') == b'hello world'
    assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    assert to_bytes(u'\udc80') == b'\xed\xb2\x80'
    assert to_bytes(u'\udc80'*10) == b'\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80\xed\xb2\x80'

# Generated at 2022-06-12 23:38:53.702787
# Unit test for function jsonify
def test_jsonify():
    data = {'A': u'\xe9', 'B': 2}
    json_data = jsonify(data)
    assert json_data == '{"A": "\\u00e9", "B": 2}'


# Generated at 2022-06-12 23:39:01.911684
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils.basic import to_native
    from ansible.module_utils.common._collections_compat import Mapping

    def make_unicode():
        if PY3:
            return str('\u2713', 'unicode_escape')  # Unicode check mark
        else:
            return text_type(bytearray('\xe2\x9c\x93', encoding='utf-8'), encoding='utf-8')

    # All the valid nonstring values
    valid_nonstring_values = frozenset(('simplerepr', 'empty', 'passthru', 'strict'))

    # Test to ensure that to_native returns unicode on python3
    test_string = "to_native test text"
    assert isinstance(to_native(test_string), text_type)

    #

# Generated at 2022-06-12 23:39:10.979370
# Unit test for function to_native
def test_to_native():
    """
    :returns: `None` on success.
    :raises: Assertion error on failure.
    """
    import sys
    import types
    # Make sure that the to_native() function always returns a text
    # string if you give it a text string.
    assert isinstance(to_native(u'foo'), text_type)

    # Make sure that the to_native() function always returns a byte
    # string if you give it a byte string
    if PY3:
        assert isinstance(to_native(b'foo'), binary_type)
    else:
        assert isinstance(to_native(b'foo'), text_type)

    # Make sure that surrogate_or_strict decodes surrogate escapes to
    # real characters

# Generated at 2022-06-12 23:39:19.656061
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\xe9') == '"\\u00e9"'
    assert jsonify(b'\xe9') == '"\\u00e9"'
    assert jsonify(b'\xe9', ensure_ascii=False) == u'"é"'
    assert jsonify(u'\u20ac') == '"\\u20ac"'
    assert jsonify(b'\xe2\x82\xac') == '"\\u20ac"'
    assert jsonify(b'\xe2\x82\xac', ensure_ascii=False) == u'"€"'
    assert jsonify([u'\xe9']) == '["\\u00e9"]'
    assert jsonify([b'\xe9']) == '["\\u00e9"]'

# Generated at 2022-06-12 23:39:29.608153
# Unit test for function jsonify
def test_jsonify():
    inputs_with_outputs = [
        (u"it's a unicode test", '"it\'s a unicode test"'),
        ({u"a": [1, 2, 3]}, '{"a": [1, 2, 3]}'),
        ({"a": [1, 2, 3]}, '{"a": [1, 2, 3]}'),
        ([1, 2, 3], '[1, 2, 3]'),
        (datetime.datetime(year=2016, month=2, day=19, hour=13, minute=22, second=17), '"2016-02-19T13:22:17"'),
    ]
    for input_data, output_data in inputs_with_outputs:
        assert output_data == jsonify(input_data)


# Generated at 2022-06-12 23:39:33.657076
# Unit test for function jsonify
def test_jsonify():
    data = [
        "a",
        "b",
        "c",
        1,
        2,
        3,
        ["a", "b", "c"],
        {"a": "b", "c": "d", "e": "f"},
        {"a": 1, "c": 2, "e": 3},
        {"a": ["b", "c", {"d": "e"}]},
        {"a": "中文", "c": "2", "e": "3"},
    ]
    ret = jsonify(data)
    assert ret == '["a", "b", "c", 1, 2, 3, ["a", "b", "c"], {"a": "b", "c": "d", "e": "f"}, {"a": 1, "c": 2, "e": 3}, ' \
                 

# Generated at 2022-06-12 23:39:39.332013
# Unit test for function jsonify
def test_jsonify():
    import datetime
    assert jsonify(dict(a=1, b=2, c=[3], d=dict(aa=1, bb=2), e=datetime.datetime(2017, 12, 7, 8, 24, 27))) == '{"a": 1, "c": [3], "b": 2, "e": "2017-12-07T08:24:27", "d": {"aa": 1, "bb": 2}}'



# Generated at 2022-06-12 23:39:54.600645
# Unit test for function jsonify
def test_jsonify():
    data = {u"key": u"value"}
    data_with_list = {u"key": [u"value"]}
    data_with_dict = {u"key": {u"key": u"value"}}
    data_with_set = {u"key": set([u"value"])}
    assert jsonify(data) == '{"key": "value"}'
    assert jsonify(data_with_list) == '{"key": ["value"]}'
    assert jsonify(data_with_dict) == '{"key": {"key": "value"}}'
    assert jsonify(data_with_set) == '{"key": ["value"]}'



# Generated at 2022-06-12 23:40:04.044964
# Unit test for function to_native
def test_to_native():
    class Foo(object):
        def __str__(self):
            return 'str'
        def __repr__(self):
            return 'repr'

    class Bar(object):
        def __str__(self):
            return u'str'
        def __repr__(self):
            return u'repr'

    class Boo(object):
        pass

    assert to_text('foo') == u'foo'
    assert to_text(u'foo') == u'foo'
    assert to_text(to_bytes(u'foo')) == u'foo'
    assert to_text(to_bytes(to_text(u'foo'))) == u'foo'

    assert to_text(Foo()) == 'str'
    assert to_text(Bar()) == u'str'

# Generated at 2022-06-12 23:40:16.891758
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'test', nonstring='strict') == b'test'
    assert to_bytes(b'test', nonstring='strict') == b'test'
    assert to_bytes(1, nonstring='strict') == b'1'


# Generated at 2022-06-12 23:40:26.207825
# Unit test for function jsonify
def test_jsonify():
    import os
    import sys
    import ansible.module_utils.six as six
    if six.PY2:
        EXTRA_STRING = to_bytes("\xF0\x9F\x98\x98")
        EXTRA_STRING_UNICODE_ESCAPE = b'\\ud83d\\ude42'
    else:
        EXTRA_STRING = to_text("\xF0\x9F\x98\x98")
        EXTRA_STRING_UNICODE_ESCAPE = '\\ud83d\\ude42'

    class MockDateTime(object):
        def __init__(self, mock_isoformat):
            self.mock_isoformat = mock_isoformat
        def isoformat(self, *args):
            return self.mock_isoformat


# Generated at 2022-06-12 23:40:38.048317
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('') == b''
    assert to_bytes(u'') == b''
    assert to_bytes(b'') == b''
    assert to_bytes(u'\xe0') == b'\xc3\xa0'

    if PY3:
        assert to_bytes(u'\udcee') == b'\xed\xb3\xae'

    # NEEDSWRITE we might want to call ``to_bytes`` without an error handler
    # when the error handler is not a parameter passed by the caller (ie.
    # default error handler).
    # assert to_bytes(u'\udcee') == b'\xed\xb3\xae'
    # assert to_bytes(u'\udcee', errors='surrogate_then_replace') == b'\xef

# Generated at 2022-06-12 23:40:49.219561
# Unit test for function to_bytes
def test_to_bytes():
    # verify surrogateescape behavior in data that would cause UnicodeEncodeError
    # NOTE: this is a place where unit tests may break on different Python versions across platforms
    # basic surrogateescape behavior
    mystr = to_bytes(u'Iñtërnâtiônàlizætiøn', encoding='ascii', errors='surrogateescape')
    assert mystr == b'I\xedt\xebrn\xe2ti\xf4n\xe0liz\xe6ti\xf8n'
    # surrogateescape behavior on non-ASCII encoding
    mystr = to_bytes(u'Iñtërnâtiônàlizætiøn', encoding='latin-1', errors='surrogateescape')

# Generated at 2022-06-12 23:40:53.552582
# Unit test for function to_bytes
def test_to_bytes():
    # Basic functionality
    assert to_bytes('test') == b'test'
    assert to_bytes(b'test') == b'test'
    assert to_bytes(u'test') == b'test'
    assert to_bytes(u'testé') == b'test\xc3\xa9'

    # nonstring options
    class Foo(object):
        def __str__(self):
            return u'testé'

    assert to_bytes(Foo()) == b'test\xc3\xa9'
    assert to_bytes(Foo(), nonstring='simplerepr') == b'test\xc3\xa9'
    assert to_bytes(Foo(), nonstring='passthru') == Foo()
    assert to_bytes(Foo(), nonstring='empty') == b''

# Generated at 2022-06-12 23:41:03.142316
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo') == b'foo'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes('foo', errors='strict') == b'foo'
    #assert to_bytes(b'foo', errors='strict') == b'foo'
    assert to_bytes(u'foo', errors='strict') == b'foo'

    assert to_bytes('©') == b'\xc2\xa9'
    assert to_bytes('©', errors='strict') == b'\xc2\xa9'
    assert to_bytes(u'©') == b'\xc2\xa9'
    assert to_bytes(u'©', errors='strict') == b'\xc2\xa9'

   

# Generated at 2022-06-12 23:41:12.101837
# Unit test for function to_bytes

# Generated at 2022-06-12 23:41:17.511634
# Unit test for function jsonify
def test_jsonify():
    data = {'a': 'b', 'c': 'd'}
    test_json = '{"a": "b", "c": "d"}'
    assert test_json == jsonify(data)

    #test with unencodable character
    data = {'a': 'b', 'c': u'\u8888'}
    assert test_json == jsonify(data)

    data = {'a': 'b', 'c': b'\x88\x88'}
    assert test_json == jsonify(data)


# Generated at 2022-06-12 23:41:30.760218
# Unit test for function to_native
def test_to_native():
    """
    Test :func:`ansible.module_utils._text.to_native`

    Since this is being done as a unittest, it'll be "unpythonic" to write
    multiple tests in one test case.  But to maintain consistency with the
    other tests, we'll write them all into one test.
    """

    # Test that a string gets returned as is
    string_value = u'foo'
    result = to_native(string_value)
    # If there's a problem, this will raise an AssertionError
    if isinstance(string_value, text_type):
        assert isinstance(result, text_type)
    else:
        assert isinstance(result, binary_type)
    assert string_value is result

    # Test that a byte string gets returned as is
    byte_string_value = b

# Generated at 2022-06-12 23:41:41.109195
# Unit test for function to_native
def test_to_native():
    """
    Test to_native() function.
    """
    assert to_native(b'a', 'ascii') == 'a'
    assert to_native(b'a', 'ascii', nonstring='strict') == 'a'
    assert to_native(u'a', 'ascii') == 'a'
    assert to_native(u'\u2713', 'ascii') == u'\u2713'
    #assert to_native(u'\u2713', 'utf-8') == '\xe2\x9c\x93'  # does not work on all platforms
    assert to_native(u'\u2713', 'utf-8', nonstring='strict') == u'\u2713'

# Generated at 2022-06-12 23:41:53.375605
# Unit test for function to_bytes
def test_to_bytes():
    # Verify that bytes
    assert to_bytes(b'abc', encoding='ascii') == b'abc'
    assert to_bytes(u'abc'.encode(u'ascii'), encoding='ascii') == b'abc'

    # Verify that encoding a unicode string works
    assert to_bytes(u'abc', encoding='ascii') == b'abc'

    # Verify that surrogates don't traceback
    assert to_bytes(u'\udc61\udc6c\udc61', encoding='ascii', errors='surrogate_or_strict') == b'\xed\xb1\xac\xed\xb1\xa1'

# Generated at 2022-06-12 23:42:02.686800
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'abc') == b'abc'
    assert to_bytes(u'a\xac') == b'a\xac'
    assert to_bytes(u'b\xcc') == b'b\xc3\xac'
    assert to_bytes(u'c\U0010ffff') == b'c\xf4\x8f\xbf\xbf'

    # Test the nonstring parameter
    assert to_bytes(1234, nonstring='simplerepr') == b'1234'
    assert to_bytes({1: 2}, nonstring='simplerepr') == b'{1: 2}'
    assert to_bytes(1234, nonstring='passthru') == 1234
    assert to_bytes({1: 2}, nonstring='passthru') == {1: 2}
   

# Generated at 2022-06-12 23:42:12.178344
# Unit test for function jsonify
def test_jsonify():
    d = dict(
        a=1,
        b=2,
        c=3,
        d="unicode string",
        e={"1": "2", "2": "3",
           "unicode key": "unicode value"},
        f=u'\N{CYRILLIC CAPITAL LETTER A}',
        # g={"1": {"2": {"3": "4", "4": "5"}}},
        h=set(['a', 'b', 'c']),
    )
    # Testing for both Python2.x and Python3.x
    for enc in ("utf-8", "latin-1"):
        assert jsonify(d, encoding=enc)
        if PY3:
            # Testing for Ascii characters
            d["i"] = "Ascii"

# Generated at 2022-06-12 23:42:16.496241
# Unit test for function jsonify
def test_jsonify():
    # Test for modern JSON module
    assert jsonify('test') == '"test"'

    # Test for older JSON module
    # Monkey-patch the json module
    old_json = json
    json = type('DummyJson', (object, ), dict(dumps=lambda x, default=None: x))
    assert jsonify('test') == 'test'
    json = old_json


# Generated at 2022-06-12 23:42:23.274706
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    import sys

    assert to_native(1) == "1"
    assert to_native(1.0) == "1.0"
    assert to_native(None) == "None"
    assert to_native(u'\u2018') == u'\u2018'
    assert to_native(True) == "True"
    assert to_native(set()) == "set()"
    assert to_native(set([1, 2, 3])) == "set([1, 2, 3])"
    assert to_native(['a', 'b', 'c']) == '[u\'a\', u\'b\', u\'c\']'

# Generated at 2022-06-12 23:42:29.652827
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"key1": u"value1", "key2": u"value2"}) == '{"key2": "value2", "key1": "value1"}'
    assert jsonify({"key1": u"value1", "key2": [u"value2", u"value3"]}) == '{"key2": ["value2", "value3"], "key1": "value1"}'
    assert jsonify({"key1": u"value1", "key2": [u"value2", u"value3"]}) == '{"key2": ["value2", "value3"], "key1": "value1"}'
    assert jsonify(u"value1") == '"value1"'
    assert jsonify(u"\u00e9") == '"\u00e9"'



# Generated at 2022-06-12 23:42:39.543237
# Unit test for function jsonify
def test_jsonify():
    dict_data = dict(a=1, b=u"中文", c=[u"中文", 1], d={u"中文": 1, "a": u"中文"})
    assert jsonify(dict_data) == json.dumps(dict_data, encoding="utf-8", default=_json_encode_fallback)
    list_data = [1, u"中文", [u"中文", 1], {u"中文": 1, "a": u"中文"}]
    assert jsonify(list_data) == json.dumps(list_data, encoding="utf-8", default=_json_encode_fallback)

    # The default is decoding all strings in the data based on utf-8
    unicode_string = u"中文"
   

# Generated at 2022-06-12 23:42:50.186376
# Unit test for function to_bytes
def test_to_bytes():
    from six import b, text_type, u
    from ansible.module_utils.common.text.converters import to_bytes
    if hasattr(to_bytes, 'test_composed_error_handlers'):
        raise RuntimeError('to_bytes already has tests; refactoring is necessary')

    to_bytes.test_composed_error_handlers = True

    def test_to_bytes_succeeds(obj, encoding, accept_encoding=None):
        result = to_bytes(obj, encoding=encoding, errors='surrogate_or_replace')
        if accept_encoding is None:
            accept_encoding = encoding
        assert isinstance(result, binary_type)
        assert result.decode(accept_encoding, 'surrogateescape') == obj

# Generated at 2022-06-12 23:43:04.999772
# Unit test for function jsonify
def test_jsonify():
    obj = {u'byte_str': b'\xc3\xa9',  # utf-8 encoded
           u'unicode_str': u'\xe9',
           u'unicode_str_list':[u'\xe9', u'\xf1'],
           u'unicode_str_dict': {u'x': u'\xe9', u'y': u'\xf1'}
           }
    obj_expected = to_text(jsonify(obj))
    obj_actual_decoded = json.loads(obj_expected)
    for k, v in iteritems(obj):
        assert obj_actual_decoded[k] == v

# Generated at 2022-06-12 23:43:08.502130
# Unit test for function to_native
def test_to_native():
    '''
    Unit test for function to_native
    '''
    result = to_native(b"foo\xa3", errors='surrogate_or_strict', nonstring='passthru')
    assert result == "foo\ufffd"


# Generated at 2022-06-12 23:43:18.737777
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'abc') == b'abc'
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(b'\x80') == b'\x80'
    assert to_bytes(u'\ucaf1') == b'\xee\x82\xb1'
    assert to_bytes(u'\uFFFD') == b'\xef\xbf\xbd'
    assert to_bytes(u'\uDCAF1') == b'\xed\xb3\xaf\xed\xb2\xb1'
    assert to_bytes(u'\uDCAF1', errors='surrogate_then_replace') == b'\xef\xbf\xbd\xed\xb2\xb1'

# Generated at 2022-06-12 23:43:24.644750
# Unit test for function to_native
def test_to_native():
    class Test(object):
        def __init__(self, val):
            self.val = val

        def __repr__(self):
            return 'Test(%r)' % self.val

    class TestNative(object):
        def __init__(self, val):
            self.val = val

        def __native__(self):
            return self.val

    # byte strings
    assert to_text(to_bytes('abc\xe5\xe4\xf6'), encoding='latin-1') == u'abc\xe5\xe4\xf6'
    assert to_text(to_bytes('abc\xe5\xe4\xf6', encoding='latin-1'), encoding='latin-1', errors='surrogateescape') == u'abc\xe5\xe4\xf6'

    # unicode strings

# Generated at 2022-06-12 23:43:30.008165
# Unit test for function jsonify
def test_jsonify():
    # test for issue #26996
    test_dict = dict(
        test1=dict(
            test2=dict(test3=dict(test4=dict(test5="test6")))
        )
    )
    try:
        jsonify(test_dict)
    except UnicodeDecodeError:
        assert False


# Generated at 2022-06-12 23:43:39.325306
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'fóo'.encode('utf-8'), 'latin-1') == b'f\xf3o'
    assert to_bytes(b'this is a string', 'ascii', 'surrogate_or_strict') == b'this is a string'
    # test surrogate_then_replace
    assert to_bytes(u'fóo') == b'f\xc3\xb3o'
    assert to_bytes(b'f\xc3\x28o') == b'f\xc3\x28o'
    assert to_bytes(u'fóo'.encode('utf-8'), 'ascii', 'surrogate_then_replace') == b'f?o'

# Generated at 2022-06-12 23:43:49.567705
# Unit test for function to_native
def test_to_native():
    """Unit test for function to_native"""
    # Test a basic string to string conversion
    assert to_native(to_bytes(u'foo')) == u'foo'
    assert to_native(to_bytes(u'foo')) == 'foo'

    # Test a list of strings
    assert to_native(to_bytes(u'foo'), nonstring='passthru') == [u'foo']

    # Test that simplerepr works as expected
    assert to_native(datetime.datetime.now(), nonstring='simplerepr') == str(datetime.datetime.now())

    # Test that simplerepr works as expected with a nonascii char
    assert to_native(to_bytes(u'✅', 'latin-1'), nonstring='simplerepr') == u'✅'
    # Test that

# Generated at 2022-06-12 23:43:51.562368
# Unit test for function to_native
def test_to_native():
    assert to_native(b'hi') == b'hi'
    assert to_native(u'hi') == u'hi'


# Generated at 2022-06-12 23:44:03.810031
# Unit test for function jsonify
def test_jsonify():
    assert jsonify("Hello World") == '"Hello World"'
    assert jsonify(b"\xf0\x9f\x92\xa9") == '"\\ud83d\\udca9"'
    assert jsonify("\xf0\x9f\x92\xa9") == '"\\ud83d\\udca9"'
    assert jsonify({"a": "Hello World"}) == '{"a": "Hello World"}'
    assert jsonify({"a": b"\xf0\x9f\x92\xa9"}) == '{"a": "\\ud83d\\udca9"}'
    assert jsonify({"a": "\xf0\x9f\x92\xa9"}) == '{"a": "\\ud83d\\udca9"}'



# Generated at 2022-06-12 23:44:14.245322
# Unit test for function to_native
def test_to_native():
    # datetime, date and time are not JSON serializable,
    # but they can be serialized by jsonutils.dumps().
    now = datetime.datetime.now()
    # dict order unpredictable in Python 3.6 and if we don't use assertDictEqual,
    # then the dicts may be in different order and the test will be unsuccessful
    assert json.loads(to_json({"foo": {"bar": {"baz": [now]}}}, indent=4)) == \
        json.loads('{"foo": {"bar": {"baz": ["%s"]}}}' % now.isoformat())

    # bytes_obj: encodable as utf-8, but also contains bytes that cannot be
    # so we have to encode with surrogate_then_replace
    bytes_obj = b'\xc3\x28'

# Generated at 2022-06-12 23:44:25.954095
# Unit test for function to_native
def test_to_native():
    from .._text import to_native
    assert to_native('unicode stuff') == u'unicode stuff'
    assert to_native(u'unicode stuff') == u'unicode stuff'
    assert to_native(b'bytes stuff') == b'bytes stuff'

# Generated at 2022-06-12 23:44:32.679099
# Unit test for function to_bytes
def test_to_bytes():
    import sys

    # Ensure the surrogateescape codec is registered so that the unit tests don't
    # introduce a failure because of that.
    if hasattr(sys, 'set_inheritable'):
        # Ensure the surrogateescape codec is registered so that the unit tests don't
        # introduce a failure because of that.
        try:
            codecs.lookup_error('surrogateescape')
        except LookupError:
            # Python3 without the backport
            codecs.register_error('surrogateescape',
                                  codecs.lookup_error('replace'))

# Generated at 2022-06-12 23:44:45.133900
# Unit test for function to_native
def test_to_native():
    def test_one_encoding(obj, expected, encoding, errors='strict', nonstring='simplerepr'):
        if isinstance(obj, binary_type):
            input_type = binary_type
        else:
            input_type = text_type
        if isinstance(expected, binary_type):
            expected_type = binary_type
        else:
            expected_type = text_type

        native = to_native(obj, encoding=encoding, errors=errors, nonstring=nonstring)
        if isinstance(native, binary_type):
            output_type = binary_type
        else:
            output_type = text_type
        if encoding is None:
            encoding = 'ascii'


# Generated at 2022-06-12 23:44:57.036443
# Unit test for function to_bytes
def test_to_bytes():
    # Test without surrogate character
    assert to_bytes('hello') == b'hello'
    assert to_bytes('hello', nonstring='empty') == b''
    assert to_bytes('hello', nonstring='passthru') == 'hello'
    assert to_bytes('hello', nonstring='strict') == b'hello'
    assert to_bytes(b'hello') == b'hello'
    assert to_bytes(b'hello', nonstring='empty') == b''
    assert to_bytes(b'hello', nonstring='passthru') == b'hello'
    assert to_bytes(b'hello', nonstring='strict') == b'hello'
    # Test with surrogate character
    assert to_bytes('\udcc3') == b'\xed\xb3\x83'

# Generated at 2022-06-12 23:45:06.891397
# Unit test for function to_bytes
def test_to_bytes():
    SURROGATE_TEST = u'\U00010163hello'
    # if the surrogate error handler fails, just skip the test
    try:
        codecs.lookup_error('surrogateescape')
        HAS_SURROGATEESCAPE = True
    except LookupError:
        HAS_SURROGATEESCAPE = False

    def check(value, encoding, errors, answer):
        result = to_bytes(value, encoding=encoding, errors=errors)

# Generated at 2022-06-12 23:45:15.537213
# Unit test for function jsonify
def test_jsonify():
    data = {
        'a': 'hello',
        'b': u'unicode',
        'c': [1, 2, 3],
        'd': {
            'e': 'world',
            'f': u'ocean'
        },
        'g': set([1, 2, 3]),
        'h': 'sp\xe2ce',
    }
    assert jsonify(data) == '{"a": "hello", "c": [1, 2, 3], "b": "unicode", "d": {"e": "world", "f": "ocean"}, "g": [1, 2, 3], "h": "spance"}'


# Generated at 2022-06-12 23:45:27.449990
# Unit test for function jsonify
def test_jsonify():
    mdict = {u'a': 123, u'b': u'abc', u'c': [u'abc', 123]}
    assert jsonify(mdict) == '{"a": 123, "c": ["abc", 123], "b": "abc"}'
    mdict = {u'a': 123, u'b': u'abc', u'c': Set([u'abc', 123])}
    assert jsonify(mdict) == '{"a": 123, "c": ["abc", 123], "b": "abc"}'
    assert jsonify({u'a': u'\uF8FF'}) == '{"a": "\\udbff\\udfff"}'
    assert jsonify({u'a': to_bytes(u'\uFFFD', errors='replace')}) == '{"a": "?"}'
    assert jsonify

# Generated at 2022-06-12 23:45:36.598128
# Unit test for function to_native
def test_to_native():
    '''
    Unit test for ansible.module_utils._text.to_native
    '''
    # Try to detect the locale
    try:
        locale_encoding = locale.getpreferredencoding()
    except AttributeError:
        locale_encoding = 'ascii'

    # This data was captured from an encrypted ansible-vault file.  It contains
    # a UTF-8 BOM (\xef\xbb\xbf) and a UTF-8 non-ascii character (\xe2\x98\xba)
    # encoded as 3 bytes.  It has bytes that are invalid in several encodings.
    # It was specifically crafted to have all non-ASCII bytes for ease of
    # finding the encoded output in unit tests.  It was then base64-encoded so
    # that it would be

# Generated at 2022-06-12 23:45:43.933503
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_bytes, to_text
    data = {b'key': b'value'}
    assert jsonify(data) == to_text('{"key": "value"}')
    data = {b'key': b'value',
            b'nested': {b'key2': b'value2'}}
    assert jsonify(data) == to_text('{"key": "value", "nested": {"key2": "value2"}}')
    data = {b'key': b'value',
            b'dict': {b'key2': b'value2'},
            b'list': [b'value1', b'value2']}

# Generated at 2022-06-12 23:45:54.092673
# Unit test for function to_bytes
def test_to_bytes():
    """ Test function to_bytes """
    # pylint: disable=protected-access
    import sys
    if sys.version_info[0] > 2:
        assert b'hello' == to_bytes('hello')
        assert b'hello' == to_bytes(u'hello')
        assert b'hello\xe4' == to_bytes(u'hello\xe4')
        assert b'Bella' == to_bytes(u'B\xe9lla')
        assert b'Bella' == to_bytes(u'B\xe9lla', encoding='iso-8859-1')
        assert b'B\xe9lla' == to_bytes(u'B\xe9lla', encoding='utf-8')

# Generated at 2022-06-12 23:46:13.717902
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.common._json_compat import json

    # Simple strings
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes('foo') == b'foo'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(bytearray(b'foo')) == b'foo'

    # Simple nonstring
    #   We have to be careful here.  We don't know what type the class will be
    #   on other Python implementations so we need to make sure that we can
    #   handle any type.
    class Foo(object):
        def __repr__(self):
            return u'ą'  # This code point is latin small letter a with ogone

# Generated at 2022-06-12 23:46:25.268145
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'hello', 'ascii') == b'hello'
    assert to_bytes('hello', 'ascii') == b'hello'
    assert to_bytes(123, 'ascii') == b'123'
    assert to_bytes(b'still hello', 'ascii', 'replace') == b'still hello'
    assert to_bytes('still hello', 'ascii', 'replace') == b'still hello'
    assert to_bytes(123, 'ascii', 'replace') == b'123'
    assert to_bytes(u'\u1234hello', 'ascii', 'replace') == b'\\u1234hello'

# Generated at 2022-06-12 23:46:33.532161
# Unit test for function jsonify
def test_jsonify():
    assert u'["\u043f\u0440\u0438\u0432\u0435\u0442"]' == jsonify([u'\u043f\u0440\u0438\u0432\u0435\u0442'])
    assert u'["\u043f\u0440\u0438\u0432\u0435\u0442"]' == jsonify([b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('utf-8')])
    assert u'{"1": "1"}' == jsonify(dict(one=u'1'))

# Generated at 2022-06-12 23:46:42.898375
# Unit test for function to_native
def test_to_native():
    # These should always be a unicode string
    assert isinstance(to_text(b'foo'), text_type)
    assert isinstance(to_text(u'foo'), text_type)
    assert isinstance(to_text(b'f\xc3\xb6\xc3\xb6'), text_type)
    assert isinstance(to_text(u'f\xf6\xf6'), text_type)

    # Nonstrings should always return unicode strings
    assert to_text(1) == u'1'
    assert to_text(1, nonstring='empty') == u''
    assert to_text(1, nonstring='passthru') == 1
    raises(TypeError, to_text, 1, nonstring='strict')

    # Default errors should always return items without failures
    # If we get unicode,

# Generated at 2022-06-12 23:46:54.861619
# Unit test for function to_native
def test_to_native():
    # Unit test for function to_native
    assert to_native('foo') == 'foo'
    assert to_native(b'foo') == 'foo'
    assert to_native(u'foo') == 'foo'
    assert to_native(u'\u9326') == '\u9326'
    assert to_native(b'\xe9\x8c\x96') == '\xe9\x8c\x96'
    assert to_native(b'\xe9\x8c\x96', encoding='latin-1') == '\xe9\x8c\x96'
    assert to_native(b'\xe9\x8c\x96', errors='surrogateescape') == '\u9326'

# Generated at 2022-06-12 23:47:05.516109
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
        assert to_bytes(u'\u1234', errors='replace') == b'?'
        assert to_bytes(u'\u1234', errors='surrogate_or_replace') == b'?'
        assert to_bytes(u'\u1234', errors='surrogate_or_strict') == b'\xe1\x88\xb4'
    else:
        assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
        assert to_bytes(u'\u1234', errors='replace') == b'?'

# Generated at 2022-06-12 23:47:13.871595
# Unit test for function jsonify
def test_jsonify():
    inputs = dict(
        A='B',
        C=[u'D', 'E'],
        F=dict(G=u'H')
    )
    assert jsonify(inputs) == '{"A": "B", "C": ["D", "E"], "F": {"G": "H"}}', "jsonify() should convert unicode to bytes"
    assert jsonify(inputs, ensure_ascii=False) == '{"A": "B", "C": ["D", "E"], "F": {"G": "H"}}', "jsonify() should return a valid json even with ensure_ascii=False"

# Generated at 2022-06-12 23:47:24.478665
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('\xe9\x99\x8d') == b'\xe9\x99\x8d'
    assert to_bytes(u'\xe9\x99\x8d') == b'\xe9\x99\x8d'
    assert to_bytes(u'\u8349') == b'\xe8\x8a\x89'
    assert to_bytes(b'\xe9\x99\x8d') == b'\xe9\x99\x8d'
    assert to_bytes(b'\xe9\x99\x8d', encoding='utf-8', errors='surrogateescape') == b'\xe9\x99\x8d'

# Generated at 2022-06-12 23:47:34.254177
# Unit test for function jsonify
def test_jsonify():
    import collections
    import datetime
    assert jsonify({'a': 'b'}) == '{"a": "b"}'
    assert jsonify(set([1, 2, 3])) == '[1, 2, 3]'
    assert jsonify(datetime.datetime(2012, 5, 1, 11, 22, 33)) == '"2012-05-01T11:22:33"'
    assert jsonify(collections.OrderedDict([('a', 'b'), ('c', 'd')])) == '{"a": "b", "c": "d"}'
    # Test unicode
    j = jsonify({u'中文': u'你好'})
    assert isinstance(j, text_type)
    assert u'中文' in j
    assert u'你好' in j



# Generated at 2022-06-12 23:47:43.050520
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.common._collections_compat import ordereddict

# Generated at 2022-06-12 23:47:57.406990
# Unit test for function to_bytes
def test_to_bytes():
    # These operates under the assumption that UTF-8 is the default encoding
    from ansible.module_utils.six import PY3
    # The surrogateescape error handler is only valid in Python3
    if PY3:
        try:
            codecs.lookup_error('surrogateescape')
            HAS_SURROGATEESCAPE = True
        except LookupError:
            HAS_SURROGATEESCAPE = False
    else:
        HAS_SURROGATEESCAPE = False

    # Test byte strings in various encodings

# Generated at 2022-06-12 23:48:01.813080
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1, b=2)) == '{"a": 1, "b": 2}'
    assert jsonify(['a', 'b']) == '["a", "b"]'
    assert jsonify(u'\u4e2d\u6587') == '"\\u4e2d\\u6587"'



# Generated at 2022-06-12 23:48:08.301692
# Unit test for function jsonify
def test_jsonify():
    valid_unicode_data = u'{ "key": "value" }'
    invalid_unicode_data = u'{ "key": "value" }'.encode('utf-16')
    try:
        assert jsonify(valid_unicode_data) == valid_unicode_data
    except UnicodeError:
        raise AssertionError("UnicodeError during jsonify valid unicode data test")
    try:
        assert jsonify(invalid_unicode_data) == '{"key": "value"}'
    except UnicodeError:
        raise AssertionError("UnicodeError during jsonify invalid unicode data test")

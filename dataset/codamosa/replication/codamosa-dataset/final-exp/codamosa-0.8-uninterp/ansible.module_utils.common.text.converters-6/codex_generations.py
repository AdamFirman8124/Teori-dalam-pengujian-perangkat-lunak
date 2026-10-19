

# Generated at 2022-06-12 23:38:24.546109
# Unit test for function to_native
def test_to_native():
    # Test that we return a native string - bytes in Python2 and unicode in
    # Python3.
    assert isinstance(to_native(b'bytes'), text_type)
    assert isinstance(to_native(u'unicode'), text_type)

    # Test that we return a native string - bytes in Python2 and unicode in
    # Python3.
    assert isinstance(to_native(u'unicode'), text_type)
    assert isinstance(to_native(b'bytes'), text_type)

    # Test that we return a native string - bytes in Python2 and unicode in
    # Python3.
    assert isinstance(to_native(b'bytes'), text_type)
    assert isinstance(to_native(u'unicode'), text_type)

    # Test that we return a native string - bytes in Python

# Generated at 2022-06-12 23:38:31.497844
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        assert to_bytes('\u1234') == b'\xe1\x88\xb4'
        assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    else:
        assert to_bytes('\u1234') == b'\\u1234'
        assert to_bytes(u'\u1234') == b'\\u1234'
        assert to_bytes('\u1234', errors='surrogateescape') == b'\xed\xa0\xb4'
        assert to_bytes(u'\u1234', errors='surrogateescape') == b'\xed\xa0\xb4'
        assert to_bytes('\u1234', errors='surrogate_or_replace') == b'?'

# Generated at 2022-06-12 23:38:33.262196
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\u03f3') == u'"\u03f3"'



# Generated at 2022-06-12 23:38:41.079529
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({1: ["value", "value"]}) == '{"1": ["value", "value"]}'
    assert jsonify({1: "value", 2: ["value"]}) == '{"1": "value", "2": ["value"]}'
    assert jsonify({1: "value", 2: {"value": "value"}}) == '{"1": "value", "2": {"value": "value"}}'
    assert jsonify({1: u"value", 2: [u"value"]}) == '{"1": "value", "2": ["value"]}'
    assert jsonify([1, "value"]) == '[1, "value"]'
    assert jsonify(Set([1, 2])) == '[1, 2]'

# Generated at 2022-06-12 23:38:49.230087
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({u'a': u'b'}) == '{"a": "b"}'
    assert jsonify({u'a': u'b\u20ac'}) == '{"a": "b\u20ac"}'
    assert jsonify({u'a': u'b\xc3\xa5'}) == '{"a": "b\xc3\xa5"}'
    assert jsonify({u'a': u'b\xe3\x82\xa2'}) == '{"a": "b\xe3\x82\xa2"}'



# Generated at 2022-06-12 23:38:59.978337
# Unit test for function to_bytes
def test_to_bytes():
    assert b'bob' == to_bytes('bob')
    assert b'bob' == to_bytes(b'bob')
    # We need to call to_bytes again because we want to test if the default
    # errors= is 'surrogate_or_replace'
    assert b'bob' == to_bytes(b'bob', errors='surrogate_or_replace')

    # surrogateescape should work normally if we don't have to port
    if HAS_SURROGATEESCAPE:
        value = u'bob\udcff'
        assert value.encode('utf-8', 'surrogateescape') == to_bytes(value, errors='surrogateescape')

        # We need to call to_bytes again because we want to test if the default
        # errors= is 'surrogate_or

# Generated at 2022-06-12 23:39:04.915000
# Unit test for function jsonify

# Generated at 2022-06-12 23:39:15.650805
# Unit test for function to_bytes
def test_to_bytes():
    # We are getting some unicode objects
    output = to_bytes(u'\u0141')
    assert isinstance(output, binary_type)
    assert output == b'\xc5\x81'

    output = to_bytes(u'\u0141', encoding='ascii')
    assert isinstance(output, binary_type)
    assert output == b'L'

    # We are getting some unicode objects with a nonascii character
    output = to_bytes(u'\u0141\u0142')
    assert isinstance(output, binary_type)
    assert output == b'\xc5\x81\xc5\x82'

    # We are getting some unicode objects with a nonascii character

# Generated at 2022-06-12 23:39:26.535374
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert codecs.decode(to_bytes(u'\u1234'), 'unicode_escape') == u'\u1234'
    assert codecs.decode(to_bytes(u'\udc80'), 'unicode_escape') == u'\udc80'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes('foo'.encode('utf-16')) == b'foo'
    assert to_bytes(u'\u1234'.encode('utf-16')) == u'\u1234'.encode('utf-8')
    assert to_bytes(bytearray(b'foo')) == b'foo'
    assert to_

# Generated at 2022-06-12 23:39:29.977686
# Unit test for function jsonify
def test_jsonify():
    data_latin = [{"key1": b'\xe6\x96\xb0\xe5\x8d\xa1'},
                  {"key2": b'\xe7\xb1\xb36'},
                 ]
    data_utf8 = [{"key1": u'新卡'},
                 {"key2": u'类6'},
                ]
    jsonified_data_latin = jsonify(data_latin)
    jsonified_data_utf8 = jsonify(data_utf8)
    assert jsonified_data_latin == jsonified_data_utf8


# Generated at 2022-06-12 23:39:45.740193
# Unit test for function to_native
def test_to_native():
    output = to_native([1, 2, 3])
    assert isinstance(output, text_type)
    assert output == u'[1, 2, 3]'

    output = to_native({'key': 'value'})
    assert isinstance(output, text_type)
    assert output == u'{\'key\': \'value\'}'

    output = to_native('value')
    assert isinstance(output, text_type)
    assert output == u'value'

    if PY3:
        output = to_native(u'\u0259')
        assert isinstance(output, binary_type)
        assert output == b'\xc4\x99'



# Generated at 2022-06-12 23:39:56.236650
# Unit test for function to_native

# Generated at 2022-06-12 23:40:05.350678
# Unit test for function to_native
def test_to_native():
    # Tests for to_bytes
    assert to_bytes(u'hello') == b'hello'
    assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    # Default encoding is utf-8
    assert to_bytes(u'\u1234', encoding='latin-1') == b'\xe1\x88\xb4'
    assert to_bytes(b'hello') == b'hello'

    # Test for surrogateescape error handler

    # This should work because there is no encoding step and we
    # always allow for surrogate escapes in the original string
    # provided that surrogateescape is a valid error handler.
    assert to_bytes(u'\udc80\udc00', errors='surrogateescape') == b'\x80\x00'
    assert to_bytes

# Generated at 2022-06-12 23:40:14.088735
# Unit test for function jsonify
def test_jsonify():
    class Foo:
        def __str__(self):
            return "jsonify"
    assert jsonify("A") == "\"A\""
    assert jsonify(b"A") == "\"A\""
    assert jsonify(set([])) == "[]"
    assert jsonify(set([1, 2, 3])) == "[1, 2, 3]"
    assert jsonify(Foo()) == "\"jsonify\""



# Generated at 2022-06-12 23:40:22.156960
# Unit test for function to_bytes
def test_to_bytes():
    """
    :py:func:`to_bytes`: functional tests for encoding, error handling, and invalid input

    .. versionadded:: 2.3
    """
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.module_utils._text import to_bytes, to_text


# Generated at 2022-06-12 23:40:33.015874
# Unit test for function jsonify
def test_jsonify():
    class Test(object):
        def __repr__(self):
            return to_text(self.__class__)

    assert '"{0}"'.format(to_text(Test())) == jsonify(Test())

    class Test2(object):
        def __str__(self):
            return to_text(self.__class__)

    assert '"{0}"'.format(to_text(Test2())) == jsonify(Test2())

    assert '"{0}"'.format(to_text(Test)) == jsonify(Test)

    assert jsonify(datetime.datetime(1972, 6, 30, 12, 34, 56, 7890)) == '"1972-06-30T12:34:56.007890"'



# Generated at 2022-06-12 23:40:41.758044
# Unit test for function to_bytes
def test_to_bytes():
    import sys
    if PY3:
        assert to_bytes('abc') == b'abc'
        assert to_bytes(b'abc') == b'abc'
    else:
        assert to_bytes('abc') == 'abc'
        assert to_bytes(b'abc') == 'abc'

    assert to_bytes(b'\xe4') == b'\xe4'
    assert to_bytes(b'\xe4', encoding='latin-1') == b'\xe4'
    assert to_bytes(b'\xe4', encoding='latin-1', errors='replace') == b'\xe4'
    assert to_bytes(b'\xe4\xe8', encoding='latin-1', errors='replace') == b'\xe4\xe8'

# Generated at 2022-06-12 23:40:51.451345
# Unit test for function to_native
def test_to_native():
    assert "foo" == to_native("foo")
    assert u"foo" == to_native(u"foo")
    assert "foo" == to_native("foo".encode("utf-8"))

    assert "foo" == to_native("foo", keep_underscores=True)
    assert "f_o_o" == to_native("f_o_o", keep_underscores=True)
    assert "f_o_o" == to_native("f_o_o".encode("utf-8"), keep_underscores=True)

    assert "f_o_o" == to_native("f_o_o".encode("utf-8"), keep_underscores=True)

# Generated at 2022-06-12 23:41:01.578205
# Unit test for function jsonify

# Generated at 2022-06-12 23:41:11.216769
# Unit test for function to_bytes
def test_to_bytes():
    utf16_str='\u0050\u0079\u0074\u0068\u006f\u006e'
    utf8_str = to_bytes(utf16_str, 'utf-8')
    assert isinstance(utf8_str, binary_type)
    utf8_str = to_bytes(utf16_str, 'utf-8')
    assert not isinstance(utf8_str, text_type)
    assert utf8_str == b'Python'

    utf16_str='\u0050\u0079\u0074\u0068\u006f\u006e'
    utf8_str = to_bytes(utf16_str, 'utf-8')
    assert isinstance(utf8_str, binary_type)
    utf8_str = to

# Generated at 2022-06-12 23:41:27.839629
# Unit test for function to_bytes

# Generated at 2022-06-12 23:41:38.286651
# Unit test for function to_native
def test_to_native():
    """
    Test to_native function
    :return:
    """
    ak_list = [
        "str",
        u'unicode\u20ac',
        b'bytes',
    ]
    expected_list = [
        "str",
        u'unicode\u20ac',
        u'bytes',
    ]
    if PY3:
        expected_list = [
            "str",
            u'unicode\u20ac',
            'bytes',
        ]
    for v, e in zip(ak_list, expected_list):
        assert to_native(v) == e
    assert to_native(ak_list) == expected_list



# Generated at 2022-06-12 23:41:41.364351
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import _text
    res = _text.jsonify({'a': 6, 'b': b'abc\xff'})
    assert res == '{"a": 6, "b": "abc\\u00ff"}'


# Generated at 2022-06-12 23:41:42.369940
# Unit test for function to_native
def test_to_native():
    assert to_native(b'foobar') == 'foobar'

# Generated at 2022-06-12 23:41:54.859327
# Unit test for function to_bytes
def test_to_bytes():

    # Test string types
    assert to_bytes(u'hi') == b'hi'
    assert to_bytes(b'hi') == b'hi'

    # Test surrogateescape
    if HAS_SURROGATEESCAPE:
        assert to_bytes(u'\udcc3') == b'\xed\xb3\x83'
        assert to_bytes(u'\udcc3', errors='surrogateescape') == b'\xed\xb3\x83'

        # Test that surrogateescape doesn't get applied when given an invalid
        # encoding
        assert to_bytes(u'\udcc3', encoding='ascii') == b'?'
        assert to_bytes(u'\udcc3', encoding='ascii', errors='surrogateescape') == b'?'

        # Test that surrogateescape doesn

# Generated at 2022-06-12 23:42:03.618343
# Unit test for function jsonify
def test_jsonify():
    # Test all types
    aList = [123, 123.123, 'abc', u'level1', u'level2']
    aList.append(aList)
    aDict = {'key1': aList, 'key2': aList, u'level1': {'level2': 'abc'},
             123: aList, 123.123: 'abc', None: 'abc'}
    aSet = set()
    aSet.add("abc")
    aTuple = (1, aList, aDict, "abc")
    aString = 'abc'
    aUnicode = u'abc'
    aFloat = 123.123
    anInteger = 123
    aLong = 1234567890123456789
    aDatetime = datetime.datetime.now()
    aTrue = True
   

# Generated at 2022-06-12 23:42:13.183762
# Unit test for function to_native
def test_to_native():
    assert to_native(b'\xc3\xb6\xc3\xa4\xc3\xbc', 'utf-8') == u'\xf6\xe4\xfc'
    assert to_native(u'\xf6\xe4\xfc') == u'\xf6\xe4\xfc'
    assert to_native(u'\xc3\xb6\xc3\xa4\xc3\xbc') == u'\xc3\xb6\xc3\xa4\xc3\xbc'
    assert to_native(1234) == u'1234'
    assert to_native([b'\xc3\xb6\xc3\xa4\xc3\xbc', 1234]) == [u'\xf6\xe4\xfc', 1234]

# Generated at 2022-06-12 23:42:20.745014
# Unit test for function to_bytes
def test_to_bytes():
    import sys

    if sys.version_info[0] == 2:
        b = binary_type
        u = text_type
    else:
        b = binary_type
        u = text_type

    assert to_bytes(u('foo'), nonstring='simplerepr') == b('foo')
    assert to_bytes(1, nonstring='simplerepr') == b('1')
    assert to_bytes(u('\u0410\u0411'), encoding='utf-8', errors='strict') == b('\xd0\x90\xd0\x91')
    assert to_bytes(u('\u0410\u0411'), encoding='ascii', errors='strict') == b('\xd0\x90\xd0\x91')

# Generated at 2022-06-12 23:42:27.456743
# Unit test for function jsonify
def test_jsonify():
    def assert_dumps(input_data, output_data):
        assert jsonify(input_data) == output_data

    assert_dumps({u'x': u'y'}, '{"x": "y"}')
    assert_dumps({u'x': b'y'}, '{"x": "y"}')
    assert_dumps({u'x': b'y\x80'}, '{"x": "y\u0080"}')
    assert_dumps({u'x': b'y\x80'.decode('latin-1')}, '{"x": "y\u0080"}')
    assert_dumps({u'x': b'y\x80'.decode('utf-8', 'surrogateescape')}, '{"x": "y\u0080"}')

# Generated at 2022-06-12 23:42:38.189813
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.common._collections_compat import (
        Mapping,
        Sequence,
    )

    def _check_check_bytes(obj, encoding, errors, nonstring):
        if isinstance(obj, binary_type):
            assert isinstance(to_bytes(obj, encoding, errors, nonstring), binary_type)
            return
        if isinstance(obj, text_type):
            assert isinstance(to_bytes(obj, encoding, errors, nonstring), binary_type)
            return
        if nonstring == 'simplerepr':
            try:
                simplerepr = str(obj)
            except UnicodeError:
                simplerepr = repr(obj)
            assert isinstance(to_bytes(obj, encoding, errors, nonstring), binary_type)
            # Make sure that to_bytes returns

# Generated at 2022-06-12 23:42:52.588014
# Unit test for function to_native
def test_to_native():
    data = {
        "ascii": "Foo",
        "with_umlaut": "\xc3\x84\xc3\xb6\xc3\x96",
        "with_control_char": "foo\x12bar"
    }

    # we don't need to test the dict value, we need to test the actual keys
    # the dict values are only there to get all the different encodings into one dict
    data_as_keys = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=True)
    data_as_keys_native = to_native(data_as_keys)
    assert isinstance(data_as_keys_native, str)
    assert data_as_keys_native[0] == '{'
   

# Generated at 2022-06-12 23:43:00.364711
# Unit test for function to_bytes
def test_to_bytes():

    class TestObj(object):
        def __str__(self):
            return u'\u65e5\u672c\u8a9e'

    assert to_bytes(7) == b'7'
    assert to_bytes('foo') == b'foo'
    assert to_bytes(True) == b'True'
    assert to_bytes(u'\u65e5\u672c\u8a9e') == b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'

# Generated at 2022-06-12 23:43:10.950895
# Unit test for function jsonify
def test_jsonify():
    """
    This is a unit test for the following code.
    1. json.dumps(data, encoding=encoding, default=_json_encode_fallback, **kwargs)
    2. json.dumps(new_data, default=_json_encode_fallback, **kwargs)
    3. raise UnicodeError('Invalid unicode encoding encountered')
    """
    import json
    data_json = b'{"status": 200, "content": "ok"}'
    data_dict = {'status': 200, 'content': 'ok'}
    data_unicode_decode_error = {'status': 200, 'content': 'o\xe2\x9c\x8bk'}

# Generated at 2022-06-12 23:43:20.454335
# Unit test for function jsonify
def test_jsonify():
    demo_dict = {u'a': 1, u'b': 2, u'c': 3, u'巴塞罗那': u'Barcelona'}
    demo_set = set([1, 2, 3])
    demo_datetime = datetime.datetime.now()
    json_demo_dict = jsonify(demo_dict)
    json_demo_set = jsonify(demo_set)
    json_demo_datetime = jsonify(demo_datetime)
    assert isinstance(json_demo_dict, str)
    assert isinstance(json_demo_set, str)
    assert isinstance(json_demo_datetime, str)

# Generated at 2022-06-12 23:43:32.734548
# Unit test for function to_native
def test_to_native():
    assert to_native(1) == "1"

# Generated at 2022-06-12 23:43:38.882158
# Unit test for function to_native
def test_to_native():
    native_str = u'foo'
    if PY3:
        assert to_native(native_str) is native_str
        assert to_native(b'foo') == u'foo'
        assert to_native(b'\xc3\x28') == u'\ufffd('
    else:
        assert to_native(native_str) == b'foo'
        assert to_native(b'foo') is native_str
        assert to_native(u'\ubcf4') == b'\xc3\x28'


# Generated at 2022-06-12 23:43:49.206990
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'123', nonstring='passthru') == b'123'
    assert to_bytes(123, nonstring='passthru') == 123

    assert to_bytes(b'123', encoding='ascii', errors='surrogateescape') == b'123'
    assert to_bytes(u'123', encoding='ascii', errors='surrogateescape') == b'123'
    assert to_bytes(1, encoding='ascii') == b'1'
    assert to_bytes(1, encoding='ascii', errors='surrogateescape') == b'1'
    assert to_bytes(1, encoding='ascii', errors='strict') == b'1'
    assert to_bytes(u'\uFFFD', encoding='ascii') == b'?'
    assert to_

# Generated at 2022-06-12 23:43:54.283915
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'\u2019') == b"\xe2\x80\x99"
    assert to_bytes(u'\u0080') == b"\xc2\x80"
    assert to_bytes(u'\u0080', encoding='latin1') == b"\x80"
    assert to_bytes(u'\u4e16') == b"\xe4\xb8\x96"
    assert to_bytes(u'\u4e16', encoding='latin1') == b"\x4e\x16"
    assert to_bytes(u'\u4e16', encoding='latin1', errors='surrogateescape') == b"\x4e\x16"

# Generated at 2022-06-12 23:44:06.594654
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(b'\xe9') == '"\u00e9"'
    assert jsonify(u'\xe9') == '"\u00e9"'
    assert jsonify(u'\u20ac'*500000) == '"%s"' % (u'\u20ac'*500000)
    assert jsonify(u'\u20ac') == '"\u20ac"'
    assert jsonify(u'\u20ac', ensure_ascii=False) == '"\u20ac"'
    assert jsonify(b'\xe9', ensure_ascii=False) == '"\u00e9"'
    assert jsonify(u'\n') == '"\\n"'
    assert jsonify(u'"') == '"\\""'

# Generated at 2022-06-12 23:44:09.841369
# Unit test for function jsonify
def test_jsonify():
    """Test the jsonify function"""
    assert jsonify([1, 2, 3]) == '[1, 2, 3]'
    assert jsonify(dict(a=1, b=2)) == '{"a": 1, "b": 2}'



# Generated at 2022-06-12 23:44:26.474817
# Unit test for function jsonify
def test_jsonify():
    import json
    from ansible.module_utils._text import to_native

    class Obj1(object):
        def __repr__(self):
            return u'Ö'

    class Obj2(object):
        def __str__(self):
            return u'Ö'

    class Obj3(object):
        def __repr__(self):
            return 'Ö'

    class Obj4(object):
        def __str__(self):
            return 'Ö'

    class Obj5(object):
        def __repr__(self):
            return '\xc3\x96'

    class Obj6(object):
        def __str__(self):
            return u'\xc3\x96'


# Generated at 2022-06-12 23:44:27.429600
# Unit test for function to_native
def test_to_native():
    """This is a stupid test function"""
    pass



# Generated at 2022-06-12 23:44:33.904218
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native

    assert to_native(b'b\xe2\x99\xa5\xef\xb8\x8f\xe2\x98\x85\xef\xb8\x8f\xe2\xad\x90') == 'b♥🅅💯'
    assert to_native(u'b\u2665\uFE0F\u263a\uFE0F\u2728') == 'b♥🅅💯'
    assert to_native(b'\xc3\xa9\xc3\xa9') == 'éé'
    # note the unicode character is the same as the e with acute accent
    assert to_native(u'\xe9\xe9') == '\xe9\xe9'


# Generated at 2022-06-12 23:44:39.233317
# Unit test for function to_native
def test_to_native():
    '''
    function to_native test
    >>> assert to_native(unicode, u'yay')
    >>> assert not to_native(unicode, 'yay')
    >>> assert not to_native(bytes, u'yay')
    >>> assert to_native(bytes, 'yay')
    '''
    pass



# Generated at 2022-06-12 23:44:48.608096
# Unit test for function jsonify
def test_jsonify():
    data = dict(a=None, b=1, c=u'\u1049')
    result = jsonify(data)
    assert result == '{"a": null, "c": "\\u1049", "b": 1}'
    result = jsonify(data, sort_keys=True)
    assert result == '{"a": null, "b": 1, "c": "\\u1049"}'
    result = jsonify(data, indent=2)
    assert result == '{\n  "a": null, \n  "c": "\\u1049", \n  "b": 1\n}'
    result = jsonify(data, separators=(',', ':'))
    assert result == '{"a":null,"c":"\\u1049","b":1}'

# Generated at 2022-06-12 23:44:59.168748
# Unit test for function to_native
def test_to_native():
    """
    Unit test for the to_native convenience function
    """
    from ansible.module_utils._text import to_native, to_bytes, to_text
    ustr = u'\u043a\u0438\u0440\u0438\u043b\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442'

# Generated at 2022-06-12 23:45:08.515488
# Unit test for function jsonify
def test_jsonify():
    import json
    import datetime
    from ansible.module_utils.six import PY3

    if PY3:
        unicode_type = str
    else:
        unicode_type = unicode

    # Check that a str object is unchanged
    t = u"This is a test string"
    assert jsonify(t) == unicode_type(t)

    # Check that a unicode object is unchanged
    t = u"This is a test string"
    assert jsonify(t) == unicode_type(t)

    # Check that a non-string that can't be serialized results in an exception
    d = datetime.datetime.now()
    try:
        jsonify(d)
    except TypeError:
        pass
    else:
        assert False, "TypeError should have been raised"

    #

# Generated at 2022-06-12 23:45:10.216635
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(foo=b"bar")) == '{"foo": "bar"}'



# Generated at 2022-06-12 23:45:12.088334
# Unit test for function jsonify
def test_jsonify():
    data = {"test_key": u"test_value"}
    assert jsonify(data) == '{"test_key": "test_value"}'


# Generated at 2022-06-12 23:45:23.188679
# Unit test for function to_bytes
def test_to_bytes():
    # First some basic sanity tests.

    # These should be no-ops
    assert to_bytes(b'asdf') == b'asdf'
    assert to_bytes(b'\xe9') == b'\xe9'
    assert to_bytes(u'\u6c34') == b'\xe6\xb0\xb4'
    assert to_bytes(u'\U0001f40d') == b'\xf0\x9f\x90\x8d'

    assert to_bytes(u'\u6c34', errors='strict') == b'\xe6\xb0\xb4'
    assert to_bytes(u'\u6c34', encoding='GB18030') == b'\xb6\xb1\xbb\xfa'

    # Try some invalid things

# Generated at 2022-06-12 23:45:29.405104
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify({"a": "b"}) == json.dumps({"a": "b"}))



# Generated at 2022-06-12 23:45:39.538542
# Unit test for function jsonify
def test_jsonify():
    test = {}
    assert jsonify(test) == '{}'
    test = {'test': [1234, 5678]}
    assert jsonify(test) == '{"test": [1234, 5678]}'
    test = {'test': {'a': 'A'}}
    assert jsonify(test) == '{"test": {"a": "A"}}'
    test = {'test': {'a': 'A'}}
    assert jsonify(test) == '{"test": {"a": "A"}}'
    test = {'test': {'a': [1, 2, 3, 4, 5]}}
    assert jsonify(test) == '{"test": {"a": [1, 2, 3, 4, 5]}}'

# Generated at 2022-06-12 23:45:45.064751
# Unit test for function jsonify
def test_jsonify():
    ''' this unit test is used to test jsonify function '''
    data = {
        "foo": {
            "bar": "baz"
        }
    }
    assert jsonify(data) == '{"foo": {"bar": "baz"}}'
    assert jsonify(data, sort_keys=True) == '{"foo": {"bar": "baz"}}'
    assert jsonify(data, indent=4) == '{\n    "foo": {\n        "bar": "baz"\n    }\n}'
    assert jsonify(data, sort_keys=True, indent=4) == '{\n    "foo": {\n        "bar": "baz"\n    }\n}'


# Generated at 2022-06-12 23:45:48.689371
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo') == b'foo'
    assert to_bytes('fòô') == b'f\xc3\xb2\xc3\xb4'
    assert to_bytes('fòô', errors='surrogate_or_strict') == b'f\xc3\xb2\xc3\xb4'
    assert to_bytes('fòô', errors='surrogate_or_replace') == b'f\xc3\xb2\xc3\xb4'
    assert to_bytes('fòô', errors='surrogate_then_replace') == b'f\xc3\xb2\xc3\xb4'
    assert to_bytes(b'foo') == b'foo'

# Generated at 2022-06-12 23:45:56.277996
# Unit test for function to_native
def test_to_native():
    """
    Test module_utils.to_native()
    """

    # Test with normal string
    assert to_native("simple string") == "simple string"

    # Test with unicode string
    assert to_native(u"simple unicode string") == u"simple unicode string"

    # Test with byte string
    assert to_native(b"simple byte string") == b"simple byte string"

    # Test with integer
    assert to_native(33) == 33

    # Test with list of strings
    assert to_native(['one', u'two', b'three']) == ['one', u'two', b'three']

    # Test with list of floats
    assert to_native([1.1, 2.2, 3.3]) == [1.1, 2.2, 3.3]


# Generated at 2022-06-12 23:46:08.473621
# Unit test for function to_native
def test_to_native():
    # check on Python 3
    if PY3:
        assert to_native(b'test') == 'test'
        assert to_native(b'\xe5\x85\xa8\xe9\x85\x8d\xe7\xbd\xae') == '全配置'
        assert to_native('全配置') == '全配置'
    # check on Python 2
    else:
        assert to_native(b'test') == u'test'
        assert to_native(b'\xe5\x85\xa8\xe9\x85\x8d\xe7\xbd\xae') == u'全配置'
        assert to_native(u'全配置')

# Generated at 2022-06-12 23:46:10.171344
# Unit test for function jsonify
def test_jsonify():
    jsonify({b'a': b'\xe4'})
    assert jsonify(u'\xe4')



# Generated at 2022-06-12 23:46:17.818389
# Unit test for function to_native
def test_to_native():
    # Test simple string types
    assert to_native(b"foo") == u"foo"
    assert to_native(b"foo", errors='surrogate_or_strict') == u"foo"
    assert to_native(b"foo", errors='surrogate_or_replace') == u"foo"
    assert to_native(u"foo") == u"foo"
    assert to_native(u"foo", errors='surrogate_or_strict') == u"foo"
    assert to_native(u"foo", errors='surrogate_or_replace') == u"foo"

    # Test surrogate errors
    assert to_native(b"\xff", errors='surrogate_or_strict') == u'\ufffd'

# Generated at 2022-06-12 23:46:18.556544
# Unit test for function to_bytes
def test_to_bytes(): pass


# Generated at 2022-06-12 23:46:27.485253
# Unit test for function to_native
def test_to_native():
    tn = to_native
    assert tn(u'foo') == 'foo'
    assert tn(u'foo'.encode('utf-8')) == 'foo'
    assert tn(b'foo') == 'foo'
    assert tn(b'foo'.decode('utf-8')) == 'foo'
    assert tn(datetime.datetime(2018, 7, 10, 10, 55, 4, 614)) == '2018-07-10T10:55:04.000614'
    assert tn("2018-07-10T10:55:04.000614") == '2018-07-10T10:55:04.000614'



# Generated at 2022-06-12 23:46:42.667784
# Unit test for function to_bytes
def test_to_bytes():
    u = u'привет'
    assert to_bytes(u, encoding='utf-8') == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
    assert to_bytes(u, encoding='latin-1') == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# Generated at 2022-06-12 23:46:49.267375
# Unit test for function jsonify
def test_jsonify():
    test_data = [ "A", "B", u'\u20ac', {u'key1': u'\u20ac', 'key2': 'D'}, ['E', u'\u20ac', 'G'] ]
    result = jsonify(test_data)
    true_result = json.dumps(test_data, default=_json_encode_fallback)
    assert result == true_result



# Generated at 2022-06-12 23:47:00.517858
# Unit test for function to_bytes
def test_to_bytes():
    # No change
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'foo', nonstring='strict') == b'foo'
    assert to_bytes(b'foo', nonstring='passthru') == b'foo'
    assert to_bytes(b'foo', encoding='ascii', errors='strict') == b'foo'
    assert to_bytes(b'foo', encoding='ascii', errors='replace') == b'foo'

    # Non-ascii bytes in the string
    assert to_bytes(b'\xff') == b'\xff'
    assert to_bytes(b'\xff', nonstring='strict') == b'\xff'
    assert to_bytes(b'\xff', nonstring='passthru') == b'\xff'
   

# Generated at 2022-06-12 23:47:06.407431
# Unit test for function to_native
def test_to_native():
    # Not much to test...
    assert to_native(u'test') == u'test'
    assert to_native(u'test'.encode('utf-8')) == u'test'
    assert to_native(u'\xe9') == u'\xe9'
    assert to_native('\xe9') == u'\xe9'
    assert to_native('\xe9'.decode('utf-8')) == u'\xe9'

# Generated at 2022-06-12 23:47:14.452481
# Unit test for function jsonify
def test_jsonify():

    # Test a basic string
    assert jsonify("hello") == "\"hello\""

    # Test a unicode string
    assert jsonify(u"hello") == "\"hello\""

    # Make sure that we encode things correctly
    assert jsonify({"a": u"hello"}) == "{\"a\": \"hello\"}"

    # Test that sets are represented as lists
    assert jsonify({"a": set([1, 2, 3])}) == "{\"a\": [1, 2, 3]}"

    # Test that datetimes are converted to ISO8601 format
    assert jsonify({"a": datetime.datetime(2014, 5, 1)}) == '{"a": "2014-05-01T00:00:00"}'

    # Test that if encoding fails we get an error

# Generated at 2022-06-12 23:47:19.090347
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(selfRef=u'\u2605')) == '{"selfRef": "\u2605"}'
    #assert jsonify(dict(selfRef=u'\u2605'), ensure_ascii=False) == \
    #    u'{"selfRef": "\u2605"}'



# Generated at 2022-06-12 23:47:20.417019
# Unit test for function to_bytes
def test_to_bytes():
    # Lazy to add a test for that for now...
    pass



# Generated at 2022-06-12 23:47:31.141131
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six.moves import StringIO

    class TestObj(object):
        def __str__(self):
            return 'str output'

        def __unicode__(self):
            return u'unicode output'

        def __repr__(self):
            return 'repr <output>'

    class TestUnicodeObj(object):
        def __str__(self):
            return u'str output'

        def __unicode__(self):
            return u'unicode output'

        def __repr__(self):
            return u'repr <output>'

    assert(to_bytes(TestObj()) == b'str output')
    assert(to_bytes(TestObj(), nonstring='passthru') is TestObj)


# Generated at 2022-06-12 23:47:33.888510
# Unit test for function jsonify
def test_jsonify():
    data = {"key1": "value1", "key2": "value2"}
    expected_output = '{"key1": "value1", "key2": "value2"}'
    assert jsonify(data) == expected_output



# Generated at 2022-06-12 23:47:42.635302
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo') == b'foo'
    assert isinstance(to_bytes('foo'), binary_type)
    assert to_bytes('\ufeff') == b'\xef\xbb\xbf'
    assert to_bytes('\udc00') == b'\xed\xb0\x80'
    assert to_bytes('\udc00', encoding='ascii') == b'?'
    assert to_bytes('\udc00', encoding='ascii', errors='surrogate_or_strict') == b'?'

    assert to_bytes(b'bar') == b'bar'
    assert isinstance(to_bytes(b'bar'), binary_type)
    assert to_bytes(b'\xef\xbb\xbf') == b'\xef\xbb\xbf'

# Generated at 2022-06-12 23:47:58.272857
# Unit test for function to_native
def test_to_native():


    assert to_native(u'hello') == u'hello'

    assert to_native(to_bytes(u'hello')) == u'hello'

    assert to_native(to_text(u'hello')) == u'hello'

    assert to_native(u'hello', 'ascii') == u'hello'

    assert to_native(to_text(to_bytes(u'hello', 'ascii'), 'ascii')) == u'hello'

    assert to_native(to_bytes(to_text(u'hello', 'ascii'), 'ascii')) == u'hello'

    assert to_native(to_bytes(u'héllö', 'ascii')) == u'héllö'


# Generated at 2022-06-12 23:48:06.830045
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    x = u"\n\xef\xbb\xbf#!/usr/bin/env python\n\n# This is a UTF-8 file\n\xc2\xa1\xc2\xa2\xc2\xa3\xc2\xa4\n\nprint 'hello world'\n"
    print(to_native(x))

    print(to_native('foo'.encode('utf-8')))
    print(to_native(u'foo'))
    print(to_native(u'ØÆ'.encode('utf-8')))
    print(to_native('ØÆ'.encode('latin-1')))
    print(to_native(u'ØÆ'.encode('latin-1')))
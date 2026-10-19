

# Generated at 2022-06-12 23:38:25.713775
# Unit test for function to_native

# Generated at 2022-06-12 23:38:32.269761
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'abc') == b'abc'
    assert to_bytes(u'\u2603') == b'\xe2\x98\x83'
    assert to_bytes(u'\u2603', errors='surrogate_or_strict') == b'\xe2\x98\x83'
    assert to_bytes(u'\u2603', errors='surrogate_or_replace') == b'\xe2\x98\x83'

    # surrogateescape is not present in this python
    assert to_bytes(u'\udce3', errors='surrogate_or_strict') == b'?'
    assert to_bytes(u'\udce3', errors='surrogate_or_replace') == b'?'

# Generated at 2022-06-12 23:38:43.481754
# Unit test for function to_bytes
def test_to_bytes():
    import sys

    # Note: No longer using the 'unicode' name as it has been removed in Python3
    # Test encoding a text string
    test_string = u'test'
    expected = b'test'
    assert to_bytes(test_string) == expected

    # Test returning an already-encoded byte string
    test_string = b'test'
    assert to_bytes(test_string) == expected

    # Test encoding a text string with non-ascii chars
    test_string = u'\u043f\u043e\u0447\u0435\u043c\u0443 \u0436\u0435\u043b\u0430\u0435\u0442\u044c'

# Generated at 2022-06-12 23:38:53.104155
# Unit test for function jsonify
def test_jsonify():
    import unittest
    class TestString(unittest.TestCase):
        def test_jsonify(self):
            test_unicode_str = u"\u6c49\u5b57"
            test_str = "乱堆"
            test_bytes = b"\xe4\xb9\xb1\xe5\xa0\x86"
            test_dict = dict(utf8="\u6c49\u5b57", bytes=test_bytes, str=test_str)
            assert jsonify(test_unicode_str) == u'"\u6c49\u5b57"'
            assert jsonify(test_str) == u'"\u4e71\u5846"'
            assert jsonify(test_bytes) == u'"\u4e71\u5846"'
           

# Generated at 2022-06-12 23:39:01.521659
# Unit test for function to_native
def test_to_native():
    assert to_native(u"hello") == u"hello"
    assert to_native("hello") == u"hello"
    assert to_native("hello") == u"hello"
    assert to_native("hello".encode('utf-8')) == u"hello"
    assert to_native("hello".encode('utf-16')) == u"hello"
    assert to_native("hello".encode('utf-32')) == u"hello"
    assert to_native("héllo".encode('utf-8')) == u"héllo"
    assert to_native("héllo".encode('utf-16')) == u"héllo"
    assert to_native("héllo".encode('utf-32')) == u"héllo"

# Generated at 2022-06-12 23:39:04.007547
# Unit test for function to_native
def test_to_native():
    assert to_native(True) is True
    assert to_native(False) is False
    native_number = 1
    assert to_native(native_number) is native_number
    assert to_native(1) == 1
    assert to_native('a') == 'a'
    assert to_native(u'a') == u'a'


# Generated at 2022-06-12 23:39:15.275166
# Unit test for function jsonify
def test_jsonify():
    assert jsonify("foo") == '"foo"'
    assert jsonify(u"foo") == '"foo"'
    assert jsonify("föö") == '"föö"'
    assert jsonify(u"föö") == '"föö"'
    assert jsonify(["foo",u"föö"]) == '["foo","föö"]'
    assert jsonify((u"foo",u"föö")) == '["foo","föö"]'
    assert jsonify({"foo":None,"föö":3.2}) == '{"föö": 3.2, "foo": null}'
    assert jsonify({"foo":u"föö","bar":u"bär"}) == '{"föö": "foo", "bär": "bar"}'
    assert jsonify

# Generated at 2022-06-12 23:39:22.978517
# Unit test for function jsonify
def test_jsonify():
    hostvars = {
        u'foo': {'a': u'hello'},
        u'bar': {'a': u'world'}
    }
    hostlist = [u'foo', u'bar']
    print(jsonify({'_meta': {'hostvars': container_to_text(hostvars)}, 'ungrouped': container_to_text(hostlist)}))
    print(jsonify(hostvars))
    print(jsonify({'a': '中文'}))



# Generated at 2022-06-12 23:39:32.284485
# Unit test for function to_native
def test_to_native():
    print("Testing the 'ansible.module_utils._text.to_native' function")
    assert to_native('') == ''
    assert to_native('test') == 'test'
    assert to_native(b'test') == 'test'
    assert to_native(b'test', errors='surrogate_or_strict') == 'test'
    assert to_native(u'test') == 'test'
    assert to_native(1) == '1'
    assert to_native(1, nonstring='passthru') == 1
    assert to_native(1, nonstring='strict') == 1
    assert to_native(1, nonstring='empty') == ''
    assert to_native(1, nonstring='simplerepr') == '1'
    # NOTE: If this test fails it most likely means the

# Generated at 2022-06-12 23:39:38.171435
# Unit test for function jsonify

# Generated at 2022-06-12 23:39:50.836164
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'


# Generated at 2022-06-12 23:39:58.842994
# Unit test for function to_native
def test_to_native():
    assert to_native(u'\u2713') == u'\u2713'
    assert to_native(b'\xe2\x9c\x93') == b'\xe2\x9c\x93'
    assert to_native(u'\u2713'.encode('utf-8')) == u'\u2713'
    assert to_native(u'\u2713', nonstring='empty') == u''
    assert to_native(b'\xe2\x9c\x93', nonstring='empty') == b''
    assert to_native(u'\xe2\x9c\x93'.encode('latin1'), encoding='latin1') == \
        u'\xe2\x9c\x93'.encode('latin1').decode('utf-8')

# Generated at 2022-06-12 23:40:03.644753
# Unit test for function to_native
def test_to_native():
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(True) == b'true'
    assert to_bytes(False) == b'false'
    assert to_bytes(5) == b'5'
    assert to_bytes(None) == b'None'



# Generated at 2022-06-12 23:40:09.390683
# Unit test for function to_bytes
def test_to_bytes():

    def assert_bytes_equal(b1, b2):
        if isinstance(b1, text_type):
            b1 = b1.encode('utf-8')
        if isinstance(b2, text_type):
            b2 = b2.encode('utf-8')
        assert b1 == b2

    # test to_bytes with strings
    assert_bytes_equal(to_bytes(u'passwd:x:20:20::/var/empty:/usr/bin/false'), b'passwd:x:20:20::/var/empty:/usr/bin/false')

# Generated at 2022-06-12 23:40:20.239599
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'foo': 'bar'}) == "{\"foo\": \"bar\"}"
    assert jsonify([1,2]) == "[1, 2]"
    assert jsonify(set([1,2])) == "[1, 2]"
    assert jsonify({'foo': set([1,2])}) == "{\"foo\": [1, 2]}"
    assert jsonify({'foo': 'bar', 'dict': {'foo': 'foo'}}) == "{\"dict\": {\"foo\": \"foo\"}, \"foo\": \"bar\"}"
    assert jsonify({'foo': 'bar', 'list': [1, 2]} ) == "{\"foo\": \"bar\", \"list\": [1, 2]}"

# Generated at 2022-06-12 23:40:28.239489
# Unit test for function to_native
def test_to_native():
    def do_test(text, bytes_, encoding, expected):
        if PY3:
            b_func = bytes_
            t_func = text
        else:
            b_func = text
            t_func = bytes_

        # test py2 str(unicode)
        _out = t_func(text(expected), encoding=encoding)
        assert _out == expected

        # test py2 str(str)
        _out = t_func(bytes_(expected), encoding=encoding)
        assert _out == expected

        # test py3 bytes(unicode)
        _out = b_func(text(expected), encoding=encoding)
        if isinstance(expected, text_type):
            assert _out == expected.encode(encoding)
        else:
            assert _out == expected

        # test py3

# Generated at 2022-06-12 23:40:39.433440
# Unit test for function to_bytes
def test_to_bytes():
    # Test normal operation
    result = to_bytes('abc')
    assert result == b'abc'
    result = to_bytes('Café')
    assert result == b'Caf\xc3\xa9'

    # Test non-strings
    result = to_bytes(12)
    assert result == b'12'

    result = to_bytes(12, nonstring='strict')
    assert isinstance(result, TypeError)

    result = to_bytes(b'abc')
    assert result == b'abc'

    result = to_bytes(b'abc', 'latin-1')
    assert result == b'abc'

    result = to_bytes(u'Caf\xe9', 'latin-1')
    assert result == b'Caf\xc3\xa9'


# Generated at 2022-06-12 23:40:50.132122
# Unit test for function to_native
def test_to_native():

    # Test no conversions needed
    assert to_text(u'foo') == u'foo'
    assert to_bytes(b'foo') == b'foo'

    # Test encoding a byte string
    assert to_text(b'foo') == u'foo'
    assert to_text(b'foo\xe9') == u'foo\xe9'

    # Test encoding a non-byte string
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'foo\xe9') == b'foo\xc3\xa9'

    # Test handling encoding errors
    assert to_text(b'foo\xff') == u'foo\ufffd'
    assert to_bytes(u'foo\u1234') == b'foo\xe1\x88\xb4'

    # Test non-string

# Generated at 2022-06-12 23:41:00.546235
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils.six import PY3, b, u

    # Make a native string
    v = to_native("\u00F6ster\xe4\xf6")
    assert isinstance(v, str) and v == "\u00F6ster\xe4\xf6"

    # Make a native string from b'foo'
    v = to_native(b'foo')
    if PY3:
        assert isinstance(v, str)
    else:
        assert isinstance(v, str) and v == "foo"

    # Ensure we don't double decode
    v = to_native(u("\u00F6ster\xe4\xf6"))
    assert isinstance(v, str) and v == "\u00F6ster\xe4\xf6"

    # Ensure we don't double

# Generated at 2022-06-12 23:41:02.555886
# Unit test for function to_native
def test_to_native():
    pass



# Generated at 2022-06-12 23:41:19.120911
# Unit test for function to_native
def test_to_native():
    """
    :func:`to_native` converts objects to the system's native string type
    """
    assert to_native(u'foo') == u'foo'
    assert to_native(u'\u2019') == u'\u2019'
    assert to_native(b'foo') == u'foo'
    assert to_native(b'\xef\xbf\xbd') == u'\ufffd'



# Generated at 2022-06-12 23:41:29.358405
# Unit test for function to_bytes
def test_to_bytes():
    """Test the to_bytes function"""
    # Test byte -> byte
    assert b'blah' == to_bytes(b'blah')
    assert b'' == to_bytes(b'', 'ascii')
    assert b'' == to_bytes(b'', 'ascii')
    assert (u'blah'.encode('utf-16') ==
            to_bytes(u'blah'.encode('utf-16'), 'utf-16'))
    # Test text -> byte
    assert b'blah' == to_bytes(u'blah')
    assert b'blah' == to_bytes(u'blah', 'ascii')
    assert (u'blah'.encode('utf-16') ==
            to_bytes(u'blah', 'utf-16'))

# Generated at 2022-06-12 23:41:40.099501
# Unit test for function to_native
def test_to_native():
    '''
    Test to_native()
    '''
    data = dict(
        null=None,
        str=to_text('hello world'),
        bytes=to_bytes(b'hello world'),
        utf8_u=u'\u00a4',
        utf8_b=to_bytes(u'\u00a4'),
        array=['one', b'two', u'three', 4],
        object={'name': 'Brian'},
    )
    if PY3:
        data['utf8_u_bytes'] = to_bytes(u'\u00a4', errors='surrogate_then_replace')
    else:
        data['utf8_u_bytes'] = to_bytes(u'\u00a4', errors='replace')

    # Create a dict with inf

# Generated at 2022-06-12 23:41:51.824701
# Unit test for function to_native
def test_to_native():
    import pytest
    from ansible.module_utils._text import to_native
    # Convert str to bytes in python2
    if not PY3:
        assert isinstance(to_native('unicode'), bytes)
        assert to_native('unicode') == 'unicode'
        assert isinstance(to_native(u'unicode'), bytes)
        assert to_native(u'unicode') == 'unicode'
        assert isinstance(to_native(b'bytes'), bytes)
        assert to_native(b'bytes') == 'bytes'

    # Convert str(obj) to bytes in python2
    if not PY3:
        assert isinstance(to_native(Dummy()), bytes)
        assert to_native(Dummy()) == "I'm a dummy"

# Generated at 2022-06-12 23:41:57.870184
# Unit test for function to_native
def test_to_native():
    # Non strings should pass through
    assert to_native(None) is None
    assert to_native(1) == 1
    assert to_native(1.1) == 1.1
    assert to_native(set()) == set()
    assert to_native(dict()) == dict()
    assert to_native([]) == []

    if PY3:
        # Python3 native strings are already a text type
        assert to_native(b'foo') == 'foo'
    else:
        # Python2 native strings aren't a text type
        assert to_native(b'foo') == u'foo'

    # Python2 unicode should stay unicode
    assert to_native(u'foo') == u'foo'

    # Python3 byte string should become unicode

# Generated at 2022-06-12 23:42:07.989405
# Unit test for function to_bytes
def test_to_bytes():
    try:
        codecs.lookup_error('surrogateescape')
    except LookupError:
        pass
    else:
        assert to_bytes(u'foo') == b'foo'
        assert to_bytes(b'foo') == b'foo'
        assert to_bytes(u'foo', errors='surrogateescape') == b'foo'
        assert to_bytes(b'foo', errors='surrogateescape') == b'foo'
        try:
            to_bytes(u'foo\ud800bar')
        except UnicodeEncodeError:
            pass
        else:
            raise AssertionError('Should have raised UnicodeEncodeError')
        try:
            to_bytes(u'foo\ud800bar', errors='surrogateescape')
        except UnicodeEncodeError:
            raise AssertionError

# Generated at 2022-06-12 23:42:17.944648
# Unit test for function to_native
def test_to_native():
    assert(to_native(u"Iñtërnâtiônàlizætiøn", 'utf-8')=="Iñtërnâtiônàlizætiøn")
    assert(to_native("Iñtërnâtiônàlizætiøn", 'utf-8')=="Iñtërnâtiônàlizætiøn")
    assert(to_native(u"Iñtërnâtiônàlizætiøn")=="Iñtërnâtiônàlizætiøn" if PY3 else "I\xf1t\xebrn\xe2ti\xf4n\xe0liz\xe6ti\xf8n")

# Generated at 2022-06-12 23:42:19.190496
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(a=1)) == '{"a": 1}'


# Generated at 2022-06-12 23:42:25.938618
# Unit test for function to_bytes
def test_to_bytes():
    # Check simple conversion of latin-1 text string
    assert to_bytes(u'\xe9') == b'\xc3\xa9'

    # Check simple conversion of utf-8 text string
    assert to_bytes(u'\xe9', encoding='utf-8') == b'\xc3\xa9'

    # Check simple conversion of multibyte utf-8 text string
    assert to_bytes(u'\u043a') == b'\xd0\x9a'

    # Check decoding utf-8 with surrogateescape when utf-8 encoding is specified
    assert to_bytes(u'\udcc3\udca9'.encode('utf-8', 'surrogateescape'), encoding='utf-8') == b'\xc3\xa9'

    # Check decoding utf-8 with surrogateescape when

# Generated at 2022-06-12 23:42:32.662574
# Unit test for function jsonify
def test_jsonify():
    data = {b"foo": u"bar"}
    assert jsonify(data) == '{"foo": "bar"}'
    assert jsonify(data, ensure_ascii=True) == '{"foo": "bar"}'
    data = {u"foo": b"bar"}
    assert jsonify(data) == '{"foo": "bar"}'
    assert jsonify(data, ensure_ascii=True) == '{"foo": "bar"}'



# Generated at 2022-06-12 23:42:59.715398
# Unit test for function to_native
def test_to_native():
    assert "u'foo'" == to_native(u'foo')
    assert "'foo'" == to_native('foo')
    assert "42" == to_native(42)
    assert "42.23" == to_native(42.23)
    assert "datetime.datetime(2017, 9, 19, 11, 35, 35, 234000)" == to_native(datetime.datetime(2017, 9, 19, 11, 35, 35, 234000))
    assert "set(['foo', 42])" == to_native(set(['foo', 42]))
    assert "set(['foo', 42])" == to_native(Set(['foo', 42]))
    assert "None" == to_native(None)
    assert "u'foo'" == to_native(u'foo', nonstring='passthru')
   

# Generated at 2022-06-12 23:43:10.607312
# Unit test for function to_bytes
def test_to_bytes():
    # Try passing a byte string
    b = to_bytes('\xc3\xb1')
    assert b == b'\xc3\xb1'

    # Try passing a unicode string
    b = to_bytes(to_text('\xc3\xb1'))
    assert b == b'\xc3\xb1'

    # Try passing a unicode string with encoding
    b = to_bytes(to_text('\xc3\xb1'), encoding='latin-1')
    assert b == b'\xc3\xb1'

    # Try passing a unicode string with encoding
    b = to_bytes(to_text('\xe4\xb8\x9c'), encoding='utf-8')
    assert b == b'\xe4\xb8\x9c'

    # Try passing a unicode string with encoding

# Generated at 2022-06-12 23:43:20.415755
# Unit test for function to_native
def test_to_native():
  obj1 = 'abc'
  to_native(obj1, encoding='utf-8', errors=None, nonstring='simplerepr')
  to_native(obj1, encoding='utf-8', errors=None, nonstring='passthru')
  to_native(obj1, encoding='utf-8', errors=None, nonstring='strict')
  to_native(obj1, encoding='utf-8', errors=None, nonstring='empty')
  obj2 = 12
  to_native(obj2, encoding='utf-8', errors=None, nonstring='simplerepr')
  to_native(obj2, encoding='utf-8', errors=None, nonstring='passthru')
  to_native(obj2, encoding='utf-8', errors=None, nonstring='strict')

# Generated at 2022-06-12 23:43:32.735240
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('test') == b'test'
    assert to_bytes(b'test') == b'test'
    assert to_bytes('test', errors='strict') == b'test'
    assert to_bytes(b'test', errors='strict') == b'test'
    assert to_bytes(u'test' + chr(0xD800)) == b'test'
    assert to_bytes(u'test' + chr(0xD800), errors='strict') == b'test'
    assert to_bytes(u'test' + chr(0xD800), errors='surrogate_then_replace') == b'test?'
    assert to_bytes(u'test' + chr(0xD800), errors='surrogate_then_replace') != b'test'
    assert to_

# Generated at 2022-06-12 23:43:35.491428
# Unit test for function jsonify
def test_jsonify():
    data = dict(key=b'value \xe2\x99\xa5')
    assert b'"value \\u2665"' in jsonify(data).encode("utf-8")


# Generated at 2022-06-12 23:43:43.121606
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native

    assert to_native(b'foo') == u'foo'
    assert to_native(u'foo') == u'foo'
    assert to_native(1) == u'1'
    assert to_native(text_type('foo')) == u'foo'
    assert to_native(binary_type('foo')) == u'foo'
    assert to_native(u"\N{THAI CHARACTER SARA A}") == u"\u0e32"
    #assert to_native(u"\ud840\udc0b") == u"\U00010200"  # this is what we want but can't make it work yet

# Generated at 2022-06-12 23:43:48.237583
# Unit test for function jsonify
def test_jsonify():
    data = {'foo': b'bar'}
    assert jsonify(data).encode('utf-8') == \
        '{"foo": "bar"}'.encode('utf-8')
    data = {'foo': u'\u2713'}
    assert jsonify(data).encode('utf-8') == \
        '{"foo": "\u2713"}'.encode('utf-8')



# Generated at 2022-06-12 23:43:49.207461
# Unit test for function jsonify
def test_jsonify():
    jsonify({})



# Generated at 2022-06-12 23:43:56.542993
# Unit test for function to_bytes
def test_to_bytes():
    # Test bytes passthru
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'foo', nonstring='empty') == b''
    assert to_bytes(b'foo', nonstring='passthru') == b'foo'
    assert to_bytes(b'foo', nonstring='strict') == b'foo'

    # Test text
    assert to_bytes('foo') == b'foo'
    assert to_bytes('foo', nonstring='empty') == b''
    assert to_bytes('foo', nonstring='passthru') == 'foo'
    assert to_bytes('foo', nonstring='strict') == b'foo'

    # Test nonstring
    # Add one of these for every type we expect to see

# Generated at 2022-06-12 23:44:06.124556
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('{"foo": "bar"}') == '{"foo": "bar"}'
    assert jsonify('{"foo": "b\xe1r"}') == '{"foo": "b\\u00e1r"}'  # default encoding is utf-8
    assert jsonify(u"{u'foo': u'b\xe1r'}") == '{"foo": "b\\u00e1r"}'
    assert jsonify(u"{u'foo': u'b\xe1r'}".encode('latin-1')) == '{"foo": "b\\u00e1r"}'



# Generated at 2022-06-12 23:44:33.561055
# Unit test for function to_bytes
def test_to_bytes():
    # Note: We can't just test all unicode characters because there are too many of them on Python 2 and
    # the test runner will complain with a ResourceWarning.
    if PY3:
        assert to_bytes(u'This is a string') == b'This is a string'
        assert to_bytes(u'café') == b'caf\xc3\xa9'
        assert to_bytes(u'\u20ac') == b'\xe2\x82\xac'
    else:
        assert to_bytes(u'This is a string') == u'This is a string'.encode('ascii')
        assert to_bytes(u'café') == u'caf\xe9'.encode('utf-8')

# Generated at 2022-06-12 23:44:45.216763
# Unit test for function to_bytes
def test_to_bytes():
    """
    Make sure that to_bytes returns the expected results
    """
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(u'\u2603') == b'\xe2\x98\x83'
    assert to_bytes(u'\u2603', nonstring='passthru') == u'\u2603'
    assert to_bytes(u'\u2603', nonstring='empty') == b''
    assert to_bytes(u'\u2603', nonstring='strict') == b'\xe2\x98\x83'
    assert to_bytes(u'\u2603', nonstring='simplerepr') == b"u'\\u2603'"

# Generated at 2022-06-12 23:44:57.035736
# Unit test for function to_bytes
def test_to_bytes():
    result = to_bytes('hello world', 'latin-1')
    if PY3:
        assert isinstance(result, binary_type)
    else:
        assert isinstance(result, text_type)
    assert result == b'hello world'

    result = to_bytes('héllö wørld', 'latin-1')
    if PY3:
        assert isinstance(result, binary_type)
    else:
        assert isinstance(result, text_type)
    assert result == b'h\xe9ll\xf6 w\xf8rld'

    result = to_bytes('héllö wørld', 'latin-1', 'surrogate_or_replace')
    if PY3:
        assert isinstance(result, binary_type)

# Generated at 2022-06-12 23:45:06.848574
# Unit test for function to_bytes
def test_to_bytes():
    # Test text string -> bytes
    u = u'\u043f\u0440\u0438\u0432\u0435\u0442 \u0431\u0438\u043b\u0438\u043d'
    encoded = u.encode('utf-8')
    utf8_b = to_bytes(u, errors='strict', nonstring='simplerepr')
    utf8_b_err = to_bytes(u, errors='strict', nonstring='simplerepr')
    assert utf8_b == encoded
    assert utf8_b_err == encoded

    # Test text string with surrogates -> bytes with surrogateescape
    if HAS_SURROGATEESCAPE:
        # Non bmp char for python3
        u = chr(0x10000)
        utf

# Generated at 2022-06-12 23:45:15.535821
# Unit test for function to_native
def test_to_native():
    global result

# Generated at 2022-06-12 23:45:27.448477
# Unit test for function jsonify
def test_jsonify():
    newdata = {b'foo': u'bar', b'bing': [1, 2, 3], b'bang': {u'bing': u'baz'}}
    print(jsonify(newdata))
    assert jsonify(newdata) == '{"foo": "bar", "bing": [1, 2, 3], "bang": {"bing": "baz"}}'
    newdata = {b'foo': u'bar', b'bing': {u'bing': u'baz', b'bang': [1, 2, 3]}}
    assert jsonify(newdata) == '{"foo": "bar", "bing": {"bing": "baz", "bang": [1, 2, 3]}}'

# Generated at 2022-06-12 23:45:37.542411
# Unit test for function to_native
def test_to_native():
    try:
        import pytest
    except ImportError:
        pytest = None

    if pytest is not None:
        pytest.importorskip("_jsonnet")


# Generated at 2022-06-12 23:45:43.215379
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\u1234') == u'"\u1234"'
    assert jsonify('\x80') == u'"\ufffd"'
    assert jsonify(u'\u1234'.encode('latin-1')) == u'"\u1234"'
    assert jsonify(b'\x80'.decode('latin-1')) == u'"\ufffd"'
    assert jsonify(b'\xff') == u'"\ufffd"'
    assert jsonify(Set([1,2,3])) == '[1,2,3]'



# Generated at 2022-06-12 23:45:53.833713
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils._text import to_bytes
    # encode non-unicode text with error handler
    assert to_bytes('\n', errors='surrogate_or_strict') == b'\n'
    assert to_bytes('\n', errors='surrogate_or_replace') == b'\n'
    assert to_bytes('\n', errors='surrogate_then_replace') == b'\n'
    # decode unicode with error handler
    assert to_bytes(u'foo\u2028bar', errors='surrogate_or_strict') == 'foo\xe2\x80\xa8bar'.encode('utf-8')

# Generated at 2022-06-12 23:46:03.820797
# Unit test for function jsonify
def test_jsonify():
    set_dict = {'a': Set([1,2,3])}
    dt_dict = {'b':datetime.datetime(1991, 10, 12, 8, 29)}
    assert jsonify(set_dict) == '{"a": [1, 2, 3]}'
    assert jsonify(dt_dict) == r'{"b": "1991-10-12T08:29:00"}'
    set_dict['c'] = dt_dict['b']
    assert jsonify(set_dict) == r'{"a": [1, 2, 3], "c": "1991-10-12T08:29:00"}'

test_jsonify()


# Generated at 2022-06-12 23:46:42.732497
# Unit test for function to_bytes
def test_to_bytes():
    if PY3:
        # assertEqual isn't guaranteed to be unicode
        assert to_bytes("unicode", errors='surrogateescape') == b"unicode"
        assert to_bytes("unicode", errors='surrogate_or_strict') == b"unicode"
        assert to_bytes("unicode", errors='surrogate_or_replace') == b"unicode"
        assert to_bytes("unicode", errors='surrogate_then_replace') == b"unicode"
        assert to_bytes("unicode".encode('utf-8'), errors='surrogateescape') == b"unicode"
        assert to_bytes("unicode".encode('utf-8'), errors='surrogate_or_strict') == b"unicode"

# Generated at 2022-06-12 23:46:54.606464
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u"abc") == b"abc"
    assert to_bytes(u"Омар Хайям против") == b"\xd0\x9e\xd0\xbc\xd0\xb0\xd1\x80 \xd0\xa5\xd0\xb0\xd0\xb9\xd1\x8f\xd0\xbc \xd0\xbf\xd1\x80\xd0\xbe\xd1\x82\xd0\xb8\xd0\xb2"

# Generated at 2022-06-12 23:47:05.279341
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"k": "v"}) == '{"k": "v"}'
    assert jsonify(Set(["a", "b"])) == '["a", "b"]'
    #the datetime and timedelta object in python 2.6 are not supported by json,
    #we will use isoformat to convert the datetime and timedelta object
    assert jsonify(datetime.datetime.utcnow()) == datetime.datetime.utcnow().isoformat()
    assert jsonify(datetime.timedelta(seconds=1)) == '0:00:01'
    raise_string = "Cannot json serialize %s" % to_native({"k": "v"})
    try:
        jsonify({"k": "v"}, encoding="123")
    except TypeError as e:
        assert str(e)

# Generated at 2022-06-12 23:47:13.685975
# Unit test for function jsonify
def test_jsonify():
    data = {'aaa': 'bbb', 'aaa2': {'ccc': u'a\u00a0b', 'ccc2': 'ddd'}}
    data_json = jsonify(data)
    assert data_json == '{"aaa": "bbb", "aaa2": {"ccc": "a\\u00a0b", "ccc2": "ddd"}}'

# Generated at 2022-06-12 23:47:24.247686
# Unit test for function to_bytes
def test_to_bytes():
    # Logic would be much simpler without the fallback support
    # It should be possible to simplify this by setting up a codec lookup
    # error somewhere and then testing the default codec in that error

    # Test that the function returns a byte string
    assert isinstance(to_bytes('test'), binary_type)

    # Test that a bytes string is returned unchanged
    assert to_bytes(b'test') == b'test'
    assert to_bytes(b'\xff\xf0\x80\x80') == b'\xff\xf0\x80\x80'

    # Test passing through nonstrings
    obj = object()
    assert to_bytes(obj, nonstring='passthru') is obj
    obj2 = object()
    assert to_bytes(obj2, nonstring='passthru') is obj2

    # Test that the default error

# Generated at 2022-06-12 23:47:34.022107
# Unit test for function to_bytes
def test_to_bytes():
    # Need to specify an encoding for these to work
    # Also, need to have both bytes and str present on Py2.
    import os
    import sys

    if os.name == 'java':
        # Jython will always return unicode strings
        # https://bugs.jython.org/issue2357
        # We can't test this function properly there
        return

    assert isinstance(to_bytes('foo'), binary_type)
    assert to_bytes('foo') == b'foo'
    assert isinstance(to_bytes(b'foo'), binary_type)
    assert to_bytes(b'foo') == b'foo'
    assert isinstance(to_bytes(u'\u2713'), binary_type)
    assert to_bytes(u'\u2713') == b'\xe2\x9c\x93'

# Generated at 2022-06-12 23:47:37.429354
# Unit test for function jsonify
def test_jsonify():
    data = {u'a': {u'b': u'c'}}
    # Should not raise exception
    jsonify(data)
    data = {u'a': {u'b': None}}
    # Should not raise exception
    jsonify(data)



# Generated at 2022-06-12 23:47:45.802806
# Unit test for function to_native
def test_to_native():
    """
    Test to_native function
    """
    assert to_native(None) == text_type(None)
    assert to_native(None, errors='surrogate_or_replace') == text_type(None)
    assert to_native(None, errors='surrogate_or_strict') == text_type(None)
    assert to_native(None, errors='surrogate_then_replace') == text_type(None)
    # Intentionally choose latin-1 because there are lots of places where latin-1 is used
    # Ensure that to_native will always return a unicode string, not a str
    assert to_native(b"\xe1", encoding='latin-1') == u"\xe1"

# Generated at 2022-06-12 23:47:51.850255
# Unit test for function to_native
def test_to_native():
    # Tests
    assert to_native(b'hello') == u'hello'
    assert to_native(u'hello') == u'hello'

    class Fake(object):
        def __str__(self):
            return u'fake'

        def __repr__(self):
            return u'fake'

    # With nonstring = 'passthru' - returns the object
    assert to_native(Fake(), nonstring='passthru') == Fake()
    # With nonstring = 'simplerepr' - returns the string value of the object
    assert to_native(Fake(), nonstring='simplerepr') == u'fake'
    # With nonstring = 'strict' - raises TypeError
    import pytest
    with pytest.raises(TypeError):
        to_native(Fake(), nonstring='strict')
   

# Generated at 2022-06-12 23:47:55.922943
# Unit test for function to_native
def test_to_native():
    assert to_native(b'foo') == u'foo'
    assert to_native(u'foo') == u'foo'
    assert to_native(5) == u'5'


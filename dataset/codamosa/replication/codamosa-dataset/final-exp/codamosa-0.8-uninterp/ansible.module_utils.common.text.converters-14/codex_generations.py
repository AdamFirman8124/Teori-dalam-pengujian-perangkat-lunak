

# Generated at 2022-06-12 23:38:24.273699
# Unit test for function to_bytes
def test_to_bytes():
    import os
    import sys
    import subprocess

    # Make sure we're not using surrogateescape on py2
    if sys.version_info[0] == 2:
        assert not HAS_SURROGATEESCAPE

    # Make sure we're using surrogateescape on py3
    if sys.version_info[0] == 3:
        assert HAS_SURROGATEESCAPE


# Generated at 2022-06-12 23:38:31.269103
# Unit test for function to_bytes
def test_to_bytes():
    text_value = to_text("Hello World")

    # Test that bytes are not touched
    bs = b"Hello World"
    assert bs == to_bytes(bs)

    # Test that text values are converted to bytes using utf-8
    assert b"Hello World" == to_bytes(text_value)

    # Test an integer
    assert b"5" == to_bytes(5)

    # Test a simple object
    class Obj(object):
        def __str__(self):
            return text_value

    assert b"Hello World" == to_bytes(Obj())

    # Test with a bad encoding
    assert b"\xf7\xbf\xbf\xbf" == to_bytes(text_value, 'utf-8', 'surrogate_then_replace')

    # Test encoding errors
    bad_

# Generated at 2022-06-12 23:38:37.950447
# Unit test for function jsonify
def test_jsonify():
    if not PY3:
        from ansible.module_utils._text import to_bytes
        data = {'item': to_bytes("I am Ansible")}
        result = jsonify(data)
        assert result == '{"item": "I am Ansible"}'
        assert isinstance(result, basestring)
    else:
        data = {'item': "I am Ansible"}
        result = jsonify(data)
        assert result == '{"item": "I am Ansible"}'
        assert isinstance(result, str)



# Generated at 2022-06-12 23:38:46.234006
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": "b"}) == '{"a": "b"}'
    assert jsonify({"a": 1, "b": 2}) == '{"a": 1, "b": 2}'
    assert jsonify({"a": 1, "b": "2"}) == '{"a": 1, "b": "2"}'
    assert jsonify({"a": 1, "b": u"\xe9"}) == '{"a": 1, "b": "\\\\u00e9"}'



# Generated at 2022-06-12 23:38:54.230644
# Unit test for function jsonify
def test_jsonify():
    data = {u'foo': u'bar',b'test':to_bytes(u'blah', 'latin-1')}
    assert jsonify(data) == '{"foo": "bar", "test": "blah"}'
    try:
        data = {u'foo': u'bar',b'\x80\x82':to_bytes(u'blah', 'latin-1')}
        jsonify(data)
        assert False
    except UnicodeDecodeError:
        pass
    try:
        data = {u'foo': u'bar',u'\U0001F4A9': to_bytes(u'blah', 'latin-1')}
        jsonify(data)
        assert False
    except UnicodeDecodeError:
        pass



# Generated at 2022-06-12 23:38:56.597546
# Unit test for function to_native
def test_to_native():
    """Make sure that strings are converted to native strings

    Simple strings should be left unchanged.
    Unicode strings should be encoded to the default
    """
    pass

# Generated at 2022-06-12 23:39:00.287377
# Unit test for function jsonify
def test_jsonify():
    mydict = {"foo": u"bar", u"baz": "qux"}
    mylist = [u"bar", "qux"]
    myset = set()
    print(mydict)
    print(mylist)
    j = jsonify(mydict)
    print(j)
    print(mydict)
    j = jsonify(mylist)
    print(j)
    myset.add(u"bar")
    myset.add(u"qux")
    j = jsonify(myset)
    print(j)



# Generated at 2022-06-12 23:39:10.667106
# Unit test for function to_native
def test_to_native():
    # Python's native str type is unicode
    assert isinstance(to_text(u"foo"), text_type)
    assert isinstance(to_bytes(u"foo"), binary_type)

    # When given a text string, we return the same string
    assert u"foo" == to_text(u"foo")
    assert b"foo" == to_bytes(u"foo")

    # When given a binary string, we codecs.decode it to unicode()
    assert u"foo" == to_text(b"foo")
    assert b"foo" == to_bytes(b"foo")

    # When given an int, we return the int as a unicode() type
    assert u"123" == to_text(123)
    assert b"123" == to_bytes(123)

    # When given a list, we

# Generated at 2022-06-12 23:39:18.361725
# Unit test for function jsonify
def test_jsonify():
    '''
    Ansible core module jsonify function tests.
    '''
    # new structure to hold results
    results = {}

    # test the function directly
    data = jsonify({'a': 'hello world'})
    results['jsonify_1'] = data == '{"a": "hello world"}'

    # jsonify with utf-8 encoding
    data = jsonify({'a': 'hello\u2018world'})
    results['jsonify_2'] = data == '{"a": "hello\u2018world"}'
    results['jsonify_2_1'] = isinstance(data, unicode)

    return results

# Generated at 2022-06-12 23:39:28.757562
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('\u4e2d\u6587') == b'\xe4\xb8\xad\xe6\x96\x87'
    assert to_bytes('foo') == b'foo'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'foo', nonstring='empty') == b''
    assert to_bytes(b'foo', nonstring='strict') == b'foo'
    assert to_bytes('\uFFFD') == b'?'
    assert to_bytes('\uFFFD', errors='ignore') == b''
    assert to_bytes('\uFFFD', errors='replace') == b'?'
    assert to_bytes('\uFFFD', errors='xmlcharrefreplace') == b'&#65533;'
    assert to_bytes

# Generated at 2022-06-12 23:39:43.770940
# Unit test for function to_bytes
def test_to_bytes():
    import sys

    if PY3:
        unicode_type = str
    else:
        unicode_type = unicode

    def normalize_output(value):
        if isinstance(value, unicode_type):
            value = value.encode('utf-8', 'surrogateescape')
            value = value.decode('utf-8', 'surrogatepass')
            value = value.encode('utf-8')
        return value

    assert b'foo' == to_bytes('foo')
    assert b'' == to_bytes('')
    assert b'foo' == to_bytes('foo', errors='strict')
    assert b'd\xc3\xbcr' == to_bytes(u'd\xfc', encoding='utf-8', nonstring='passthru')

# Generated at 2022-06-12 23:39:48.418460
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils.common._collections_compat import TestDict
    obj = TestDict({'a':'b', 'c':'d'})
    assert obj == to_native(obj), "to_native() must return correct value"


# Generated at 2022-06-12 23:39:57.455031
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native(b'abc\xe4\xb8\x96\xe7\x95\x8c') == u'abc世界'
    assert to_native(u'abc\u4e16\u754c') == u'abc世界'
    assert to_native(u'abc\ud840\udc0b') == u'abc\ud840\udc0b'
    assert to_native(b'abc\xf0\x90\x84\x8b') == u'abc\U00010303'
    assert to_native(1) == 1
    assert to_native(None) is None
    assert to_native(u'☃') == u'☃'



# Generated at 2022-06-12 23:40:06.241274
# Unit test for function to_native
def test_to_native():
    # Test non-string values
    for nonstring in (True, 1, 0, 1.0, 0.0, [1], {'a': 'b'}):
        assert to_text(nonstring, nonstring='simplerepr') == text_type(str(nonstring))

    # Test py3 native strings
    u = u'\u043f\u0440\u0438\u0432\u0435\u0442 \u043c\u0438\u0440'
    assert to_text(u) == u
    assert to_text(u, errors='surrogate_or_strict') == u
    assert to_text(u, errors='surrogate_or_replace') == u
    assert to_text(u, errors='surrogate_then_replace') == u
    assert to_text

# Generated at 2022-06-12 23:40:18.994407
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.common._collections_compat import b

    assert to_bytes('foo') == b('foo')
    assert to_bytes(b('foo')) == b('foo')
    assert to_bytes('foo', nonstring='passthru') == 'foo'
    assert to_bytes('foo', nonstring='empty') == b('')
    assert to_bytes('foo', nonstring='strict') == b('foo')
    try:
        to_bytes(None, nonstring='strict')
    except TypeError:
        pass
    else:
        assert False, 'to_bytes(None, nonstring="strict") should raise TypeError'

    assert to_bytes(None) == b('')
    assert to_bytes(1) == b('1')

# Generated at 2022-06-12 23:40:26.828883
# Unit test for function to_native
def test_to_native():
    values = (
        u'foo',
        text_type(123),
        text_type(123.45),
        to_bytes('ascii'),
        u'ünicode',
    )
    for value in values:
        assert to_native(value) == value
    assert to_native(to_bytes(u'unicode')) == u'unicode'
    assert to_native(to_bytes(u'unicode', encoding='utf-8')) == u'unicode'
    assert to_native(to_bytes(u'unicode', encoding='utf-8', errors='surrogateescape')) == u'unicode'

test_to_native()



# Generated at 2022-06-12 23:40:38.439240
# Unit test for function to_native
def test_to_native():
    # Test with unicode
    assert to_native(u'foo') == u'foo'

    assert to_native(u'foo'.encode('utf-8')) == u'foo'

    # Test with byte strings
    assert to_native('foo'.encode('utf-8')) == u'foo'
    assert to_native('foo'.encode('utf-32')) == u'foo'

    # Test with non-strings
    assert to_native(1) == 1
    assert to_native(1.1) == 1.1
    assert to_native(object) == 'object'
    assert to_native(object()) == '<object object at 0x%x>' % id(object())
    assert to_native(Exception()) == "Exception('',)"

# Generated at 2022-06-12 23:40:49.463889
# Unit test for function to_bytes
def test_to_bytes():
    def b(v):
        try:
            return v.encode('utf8')
        except UnicodeEncodeError:
            return v

    assert to_bytes(u'') == b('None')
    assert to_bytes(u'foo') == b('foo')
    assert to_bytes(b'foo') == b('foo')
    assert to_bytes(True) == b('True')
    assert to_bytes(False) == b('False')
    assert to_bytes(0) == b('0')
    assert to_bytes(datetime.datetime.now()) == b("'datetime.datetime(")

    # check that the nonstring parameter works
    assert to_bytes(123, nonstring='passthru') == 123
    assert to_bytes(123, nonstring='empty') == b('')
    assert to

# Generated at 2022-06-12 23:41:00.161683
# Unit test for function to_bytes
def test_to_bytes():
    # Test with an ascii string
    assert to_bytes('abc') == b'abc'
    assert to_bytes('a\xFF') == b'a\xFF'

    # Test with a byte string
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(b'a\xFF') == b'a\xFF'

    # Test with a nonstring
    assert to_bytes(['a', 'b']) == b'[\'a\', \'b\']'
    assert to_bytes(['a', 'b'], nonstring='passthru') == ['a', 'b']
    assert to_bytes(['a', 'b'], nonstring='empty') == b''
    assert to_bytes(['a', 'b'], nonstring='strict') == TypeError

   

# Generated at 2022-06-12 23:41:10.643848
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'string') == b'string'
    assert to_bytes(u"ようこそ") == b"\xe3\x82\x88\xe3\x81\x86\xe3\x81\x93\xe3\x81\xad"
    assert to_bytes(u"ようこそ", 'utf-16') == b"\xff\xfey\x00\x00o\x00\x00u\x00\x00k\x00\x00o\x00\x00s\x00\x00o\x00\x00"
    assert to_bytes(b"\x80") == b"\x80"

# Generated at 2022-06-12 23:41:55.282480
# Unit test for function jsonify
def test_jsonify():
    my_dict = {"key": "value"}
    assert jsonify(my_dict) == '{"key": "value"}'

    my_list = ["value1", "value2"]
    assert jsonify(my_list) == '["value1", "value2"]'

    my_dict = {"key": "value"}
    assert jsonify(my_dict) == '{"key": "value"}'

    my_set = set(["value1", "value2"])
    assert jsonify(my_set) == '["value1", "value2"]'

    my_datetime = datetime.datetime(2017, 11, 27, 20, 39, 54, 652380)
    assert jsonify(my_datetime) == '"2017-11-27T20:39:54.652380"'



# Generated at 2022-06-12 23:42:03.897286
# Unit test for function to_native
def test_to_native():
    for string in (u'hello', 'hello'):
        for encoding in ('ascii', 'utf-8', 'utf-16', 'utf-32', 'latin-1'):
            try:
                result = to_native(string, encoding=encoding)
            except UnicodeDecodeError:
                # this should never happen because we're passing
                # in a native string which should be implicitly
                # decodable to the passed in encoding
                raise
            except UnicodeEncodeError:
                # this should never happen because we're passing
                # in a native string which should be implicitly
                # encodable to the passed in encoding
                raise
            assert isinstance(result, text_type)
            assert result == string
            # Note: This is a valid test but it's commented out because
            # surrogateescape isn't always available.  If it

# Generated at 2022-06-12 23:42:13.439540
# Unit test for function jsonify

# Generated at 2022-06-12 23:42:15.270629
# Unit test for function to_native
def test_to_native():
    ret = to_native(" " * 1000, errors='surrogate_or_strict')
    assert isinstance(ret, text_type)


# Generated at 2022-06-12 23:42:18.135061
# Unit test for function to_native
def test_to_native():
    assert to_native(u'\u2713') == u'\u2713'
    assert to_native(b'\xe2\x9c\x93') == u'\u2713'


# Generated at 2022-06-12 23:42:26.378786
# Unit test for function to_native
def test_to_native():
    """
    Make sure that a string is converted to native string
    """
    assert to_native('test') == 'test'
    assert to_native(u'test') == 'test'
    assert to_native(u'test\u1234') == 'test\u1234'
    assert to_native(u'test\xab') == 'test\xab'
    assert to_native(b'test') == 'test'
    assert to_native(b'test\xab') == 'test\xab'
    assert to_native(b'test\xc3\x82') == 'test\xc3\x82'
    assert to_native(b'test\xc3\x82', errors='surrogate_or_replace') == 'test\xc3\x82'

# Generated at 2022-06-12 23:42:37.168888
# Unit test for function to_native
def test_to_native():
    '''
    Test that strings get decoded correctly
    '''
    try:
        # Python 3
        to_unicode = to_text
    except NameError:
        # Python 2
        to_unicode = to_bytes

    # Strings that look like bytes
    assert to_unicode(b'\xc2\xa2', errors='strict') == u'\xa2'
    assert to_unicode(b'\xc2\xa2', errors='ignore') == u''
    assert to_unicode(b'\xc2\xa2', errors='replace') == u'?'
    assert to_unicode(b'\xc2\xa2', errors='surrogateescape') == u'\udca2'

# Generated at 2022-06-12 23:42:48.344207
# Unit test for function to_bytes

# Generated at 2022-06-12 23:42:57.584630
# Unit test for function to_native
def test_to_native():
    # to_native should simply return a text_type object
    assert isinstance(u'text', text_type)
    assert to_native(u'text') == u'text'
    assert to_native(u'text'.encode('utf-8')) == u'text'
    assert to_native(u'text'.encode('utf-16')) == u'text'
    assert to_native(u'text'.encode('latin-1')) == u'text'

    if PY3:
        # to_native should decode a bytes object to a text_type object using the
        # utf-8 codec.
        assert isinstance(b'text', bytes)
        assert to_native(b'text') == u'text'

# Generated at 2022-06-12 23:43:08.311614
# Unit test for function to_bytes
def test_to_bytes():
    # Test surrogate_then_replace
    u_danger = text_type('\U0001F4A5', 'unicode_escape')
    b_danger = u_danger.encode('utf-8', 'surrogateescape')
    assert to_bytes(u_danger, encoding='ascii', errors='surrogate_then_replace') == b_danger.decode('utf-8', 'replace').encode('ascii', 'replace')
    # Test surrogate_or_replace
    assert to_bytes(u_danger, encoding='ascii', errors='surrogate_or_replace') == b_danger.decode('utf-8', 'replace').encode('ascii', 'replace')
    assert to_bytes(u_danger, encoding='utf-8', errors='surrogate_or_replace') == b_danger

# Generated at 2022-06-12 23:43:47.005935
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'\u2603') == '"\xe2\x98\x83"'
    assert jsonify(b'\xe2\x98\x83') == '"\xe2\x98\x83"'
    assert jsonify({u'a': u'\u2603', b'b': {u'b': b'\xe2\x98\x83'}}) == '{"a": "\xe2\x98\x83", "b": {"b": "\xe2\x98\x83"}}'



# Generated at 2022-06-12 23:43:55.187438
# Unit test for function to_bytes

# Generated at 2022-06-12 23:44:01.950507
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':'b'}) == '{"a": "b"}'
    assert jsonify({'a':'b'}, ensure_ascii=True) == '{"a": "b"}'
    assert u'{{"a": "b"}}'.encode('utf-8').decode('utf-8') == u'{"a": "b"}'



# Generated at 2022-06-12 23:44:09.278633
# Unit test for function to_bytes
def test_to_bytes():
    """unit tests for to_bytes()"""

    from ansible.module_utils.common._collections_compat import MutableMapping

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            super(MockModule, self).__init__()
            self.params = MutableMapping()
            for arg in args:
                self.params[arg] = True
            self.params.update(kwargs)

    from ansible.module_utils.basic import AnsibleModule

    # If a user specifies nonstring='strict', they expect to get a TypeError if
    # they pass in a nonstring.
    failed = False
    try:
        to_bytes(b'foo', nonstring='strict')
    except TypeError:
        failed = True

# Generated at 2022-06-12 23:44:12.406889
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'world') == b'world'
    assert to_bytes(0) == b'0'



# Generated at 2022-06-12 23:44:20.958925
# Unit test for function jsonify
def test_jsonify():

    # simple test first
    assert b'{"foo": "bar"}' == jsonify({u"foo": u"bar"})

    # now with unicode chars
    ud = {u"foo": u"bar"}
    assert b'{"foo": "bar"}' == jsonify(ud)

    # now with unicode chars in a set
    ud = {u"foo": u"bar", u"baz": Set([u"bam", u"boo"])}
    assert b'{"foo": "bar", "baz": ["bam", "boo"]}' == jsonify(ud)

    # now with a datetime
    ud = {u"foo": u"bar", u"baz": datetime.datetime(2012, 12, 24, 23, 59, 59)}

# Generated at 2022-06-12 23:44:31.593547
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    utf8_str = '\u00e0'
    latin1_str = utf8_str.encode('latin-1')
    utf8_str_as_unicode = utf8_str.decode()
    assert utf8_str == utf8_str_as_unicode == u'\u00e0'
    assert latin1_str == b'\xe0'

    assert to_native(latin1_str) == u'\xe0'
    assert to_native(latin1_str, encoding='latin-1') == u'\xe0'
    assert to_native(utf8_str) == u'\u00e0'

# Generated at 2022-06-12 23:44:43.881556
# Unit test for function to_bytes
def test_to_bytes():
    utf8_encoded = u'\u1234\u5678\u9abc'.encode('utf-8')
    utf8_raw = b'\xe1\x88\xb4\xe5\x99\xb8\xe9\xaa\xbc'
    latin1_encoded = u'\u1234\u5678\u9abc'.encode('latin-1')
    latin1_raw = b'\xe1\x88\xb4\xe5\x99\xb8\xe9\xaa\xbc'
    cp437_encoded = u'\u1234\u5678\u9abc'.encode('cp437')
    cp437_raw = b'\x84\xd6\xdc\xde'

    # We're going to patch out HAS

# Generated at 2022-06-12 23:44:44.456014
# Unit test for function to_bytes
def test_to_bytes():
    pass



# Generated at 2022-06-12 23:44:51.200290
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six import text_type

    # Unicode string
    unicode_string = u'\u043f\u0440\u0438\u0432\u0435\u0442 \u043c\u0438\u0440'
    assert unicode_string == to_text(to_bytes(unicode_string))
    # Bytes, ascii compatible
    byte_string = b'\xf0\x9f\x98\x8d'
    assert byte_string == to_bytes(to_bytes(byte_string))
    # Bytes, non ascii compatible
    byte_string = b'\xff'
    assert byte_string == to_bytes(to_bytes(byte_string, errors='surrogate_or_strict'))
    # Bytes, non as

# Generated at 2022-06-12 23:46:25.139102
# Unit test for function jsonify
def test_jsonify():
    # Simple str will not be touched
    assert jsonify(u'test') == u'test'

    # dict can be converted
    assert jsonify({u'test': u'ing'}) == u'{"test": "ing"}'

    # Test some invalid bytes
    assert jsonify(u'test\ufffd') == u'"test\\ufffd"'
    assert jsonify(u'test\ufffd'.encode("latin-1")) == u'"test\\ufffd"'

    # Test with fallback
    assert jsonify({u'test': Set([u'ing'])}) == u'{"test": ["ing"]}'



# Generated at 2022-06-12 23:46:27.401417
# Unit test for function jsonify
def test_jsonify():
    jsonify({u'foo': u'bar'}, indent=4)
    jsonify(u'foo')
    jsonify(1)



# Generated at 2022-06-12 23:46:34.826172
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('hi') == b'hi'
    assert to_bytes(b'hi') == b'hi'
    assert to_bytes(u'hi') == b'hi'
    assert to_bytes(u'\xe2\x98\x83') == b'\xe2\x98\x83'
    assert to_bytes(u'\xe2\x98\x83'.encode('utf-8')) == b'\xe2\x98\x83'
    assert to_bytes(u'\xe2\x98\x83'.encode('latin-1')) == b'\xe2\x98\x83'

# Generated at 2022-06-12 23:46:43.754072
# Unit test for function to_bytes
def test_to_bytes():
    # Test with default options
    assert to_bytes('a string') == b'a string'
    assert to_bytes(b'byte string') == b'byte string'
    assert to_bytes(u'Unicode string') == b'Unicode string'
    assert to_bytes(u'a text with non-ASCII character: \u0141') == b'a text with non-ASCII character: \xc5\x81'

    # Test with nonstring=strict
    assert to_bytes('a string') == b'a string'
    assert to_bytes(b'byte string') == b'byte string'
    assert to_bytes(u'Unicode string') == b'Unicode string'

# Generated at 2022-06-12 23:46:44.961117
# Unit test for function to_bytes
def test_to_bytes():
    pass
    # TODO



# Generated at 2022-06-12 23:46:49.267446
# Unit test for function jsonify
def test_jsonify():
    try:
        jsonify({'a': to_bytes('h\xe9')})
    except Exception:
        # If the function does not catch the Unicode error and raises it,
        # the test fails.
        raise


# Generated at 2022-06-12 23:47:00.517802
# Unit test for function to_bytes
def test_to_bytes():
    # Test strings
    assert to_bytes(u'string') == b'string'
    assert to_bytes(u'€') == b'\xe2\x82\xac'
    # This character is not in latin-1.  It's a euro sign in windows-1252
    # so it encodes a different way
    assert to_bytes(u'€', 'latin-1') == b'\x80'
    assert to_bytes(u'€', 'latin-1', 'replace') == b'?'
    assert to_bytes(u'string', encoding='ascii') == b'string'
    assert to_bytes(u'\u0394', encoding='ascii', errors='replace') == b'?'
    if HAS_SURROGATEESCAPE:
        assert to_bytes

# Generated at 2022-06-12 23:47:09.961541
# Unit test for function to_bytes
def test_to_bytes():
    # Test that it returns a byte string.  We'll assume the rest of the tests
    # are correct
    assert isinstance(to_bytes(u'foo'), binary_type)

    # Test that None comes through as an empty string
    assert b'' == to_bytes(None)

    # Test that the nonstring parameter works
    assert 123 == to_bytes(123, nonstring='passthru')
    assert b'' == to_bytes(None, nonstring='empty')
    raises(TypeError, to_bytes, None, nonstring='strict')

    # Test that when passed a text string, it returns the utf8 encoded value
    # Note: We could also test that it transforms latin-1 to utf-8 correctly
    # but that's tested in another function (to_text).  The important thing
    # to test here is that the

# Generated at 2022-06-12 23:47:11.021954
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify('abcd') == '"abcd"')



# Generated at 2022-06-12 23:47:20.417683
# Unit test for function jsonify
def test_jsonify():
    # test simple str
    input_data = u"this is a test"
    result = jsonify(input_data)
    assert result == b'"this is a test"'
    assert isinstance(result, binary_type)
    # test utf8 str
    input_data = u"\u7a0b\u5e8f\u4e13\u5bb6\u8bbe\u8ba1\u7684Linux\u8ba1\u7b97\u673a\u914d\u7f6e"
    result = jsonify(input_data)

# Generated at 2022-06-12 23:48:00.542709
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"a": b"abc"}) == '{"a": "abc"}'
    assert jsonify({"a": u"abc"}) == '{"a": "abc"}'



# Generated at 2022-06-12 23:48:08.544318
# Unit test for function to_bytes
def test_to_bytes():
    # We have a bunch of these tests in test_utils so people porting to Python3
    # are likely to find them eventually.  For now just make sure that we're
    # calling the to_bytes with the proper default arguments.
    assert isinstance(to_bytes('foo'), binary_type)
    assert isinstance(to_bytes(b'foo'), binary_type)
    assert isinstance(to_bytes(u'foo'), binary_type)
    assert isinstance(to_bytes('foo', errors='surrogate_then_replace'), binary_type)
    assert to_bytes(u'和製漢語', encoding='latin1') == u'和製漢語'.encode('latin1')


# Generated at 2022-06-12 23:38:27.605107
# Unit test for function to_native

# Generated at 2022-06-12 23:38:37.950249
# Unit test for function to_bytes

# Generated at 2022-06-12 23:38:49.878971
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('a') == '"a"'
    assert jsonify(u'a') == '"a"'
    assert jsonify(b'a') == '"a"'
    assert jsonify(100) == '100'
    assert jsonify([b"a", u'\xc3\x9f', 'foo']) == '["a", "\\u00df", "foo"]'
    assert jsonify(dict(x=100, y='foo')) == '{"x": 100, "y": "foo"}'

    # Test proper handling of unicode with utf-8 and latin1
    assert jsonify({u'\xc3\x9f'.encode('latin-1'): 100}, sort_keys=True) == '{"\\u00df": 100}'

# Generated at 2022-06-12 23:39:00.362756
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('abc') == b'abc'
    assert to_bytes('abc', 'ascii') == b'abc'
    assert to_bytes(b'def') == b'def'
    assert to_bytes(b'ghi', 'ascii') == b'ghi'
    assert to_bytes('jkl', 'ascii', 'surrogate_or_replace') == b'jkl'
    assert to_bytes('mno', 'ascii', 'surrogate_or_strict') == b'mno'
    assert to_bytes(u'%x' % -0x2020, 'utf-8') == b'\xe2\x88\x98'

# Generated at 2022-06-12 23:39:10.742200
# Unit test for function to_native
def test_to_native():
    def _t():
        import sys
        return sys.version_info[0]

    if _t() == 2:
        # Python 2
        assert to_native(None) is None
        assert type(to_native(None)) is type(None)
        assert to_native(u'unicode') == u'unicode'
        assert type(to_native(u'unicode')) is type(u'unicode')
        assert to_native(u'unicode'.encode('utf-8')) == u'unicode'
        assert type(to_native(u'unicode'.encode('utf-8'))) is type(u'unicode')
        assert to_native('str') == 'str'
        assert type(to_native('str')) is type('str')
        assert to_native(b'bytes')

# Generated at 2022-06-12 23:39:19.529641
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(b'mybytes') == b'mybytes'
    assert to_bytes('mybytes') == b'mybytes'
    assert to_bytes(b'mybytes', nonstring='empty') == b''
    assert to_bytes('mybytes', nonstring='empty') == b''
    assert to_bytes(b'mybytes', nonstring='strict') == b'mybytes'
    with pytest.raises(TypeError):
        to_bytes(b'mybytes', nonstring='passthru')
    with pytest.raises(TypeError):
        to_bytes(b'mybytes', nonstring='unknown_value')
    assert to_bytes('\x80') == b'\xc3\x80'

# Generated at 2022-06-12 23:39:29.812289
# Unit test for function jsonify
def test_jsonify():
    data = {u'f\xe4lse': False, u'tur': True, u'n\xf8ll': None}
    for encoding in ("utf-8", "latin-1"):
        try:
            result = jsonify(data, encoding=encoding)
            assert result == '{"n\xf8ll": null, "tur": true, "f\xe4lse": false}'
        # Old systems using old simplejson module does not support encoding keyword.
        except TypeError:
            try:
                new_data = container_to_text(data, encoding=encoding)
            except UnicodeDecodeError:
                continue
            result = jsonify(new_data)
            # It's not always possible to encode all strings as latin1

# Generated at 2022-06-12 23:39:39.173518
# Unit test for function to_bytes
def test_to_bytes():
    if not HAS_SURROGATEESCAPE:
        return

    # Test encoding of a Unicode string
    #   'ascii'
    assert to_bytes(u'Hello', 'ascii') == b'Hello'
    assert to_bytes(u'\u1234', 'ascii', errors='surrogate_or_replace') == b'?'
    assert to_bytes(u'\u1234', 'ascii', errors='surrogate_or_strict') == b'?'
    assert to_bytes(u'\u1234', 'ascii', errors='surrogate_then_replace') == b'\xef\xbf\xbd'
    #   'latin-1'
    assert to_bytes(u'Hello', 'latin-1') == b'Hello'

# Generated at 2022-06-12 23:39:51.726553
# Unit test for function to_native
def test_to_native():
    to_native = to_text

# Generated at 2022-06-12 23:40:03.059037
# Unit test for function to_native
def test_to_native():
    for type_name, obj in iteritems(dict(
            text=u'foo',
            binary=b'bar',
            int=3,
            dict=dict(a=1),
            list=['a', 'b', 'c'],
            tuple=('a', 'b', 'c'),
            set=set(['a', 'b', 'c']),
            frozenset=frozenset(['a', 'b', 'c']),
            datetime=datetime.datetime.now(),
            )):
        if PY3:
            assert isinstance(to_native(obj), text_type), "Type %s should be text" % type_name
        else:
            assert isinstance(to_native(obj), binary_type), "Type %s should be binary" % type_name


# Generated at 2022-06-12 23:40:19.994316
# Unit test for function to_native
def test_to_native():
    assert to_text(True) == u'True'
    assert to_text(False) == u'False'

    assert to_text(1) == u'1'
    assert to_text(0) == u'0'

    assert to_text(None) == u'None'

    assert to_text(u'string') == u'string'
    assert isinstance(to_text(u'string'), text_type)

    if PY3:
        assert to_text(b'string') == u'string'
        assert isinstance(to_text(b'string'), text_type)

        assert to_text(u'string'.encode('utf-16', 'surrogateescape')) == u'string'

# Generated at 2022-06-12 23:40:27.145352
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(1) == '1'
    assert jsonify('a') == '"a"'
    assert jsonify({'a':1}) == '{"a": 1}'
    assert jsonify({'a':to_bytes('\xe9')}) == '{"a": "\\u00e9"}'
    assert jsonify({'a':to_text('\xe9')}) == '{"a": "\\u00e9"}'
    assert jsonify([1,to_bytes('\xe9')]) == '[1, "\\u00e9"]'
    assert jsonify([1,to_text('\xe9')]) == '[1, "\\u00e9"]'


# Generated at 2022-06-12 23:40:38.692574
# Unit test for function to_native
def test_to_native():
    # Run all tests with PY3 True and False
    for PY3 in (True, False):
        assert to_native(b'hello') == 'hello'
        assert to_native(u'\u00e9') == '\u00e9'
        assert to_native(1) == '1'
        assert to_native(1, nonstring='empty') == ''
        assert to_native(b'\xe9') == '\u00e9'

        try:
            to_native(u'\u00e9'.encode('ascii'), errors='strict')
        except UnicodeDecodeError:
            pass
        else:
            assert False, "to_native with strict error should not have passed"


# Generated at 2022-06-12 23:40:49.704989
# Unit test for function to_bytes

# Generated at 2022-06-12 23:40:52.708800
# Unit test for function to_native
def test_to_native():
    assert to_native(b'bytes') == b'bytes'
    assert to_native(u'unicode') == u'unicode'
    assert to_native(123) == 123



# Generated at 2022-06-12 23:41:02.563300
# Unit test for function to_bytes
def test_to_bytes():
    # Ensure that surrogates are preserved
    if PY3:
        # idk why these aren't the same in Python2
        assert b'\xed\xa0\x80\xed\xb0\x80' == to_bytes(u'\ud800\udc00')
    else:
        # There is no surrogateescape error handler in Python2.  Surrogates
        # will be preserved via using the ascii codec but this is slightly
        # different from surrogateescape.
        assert b'\xef\xbf\xbd\xef\xbf\xbd' == to_bytes(u'\ud800\udc00')

    # Bytes strings should just be returned
    assert b'' == to_bytes(b'')
    assert b'foo' == to_bytes(b'foo')

# Generated at 2022-06-12 23:41:03.676293
# Unit test for function jsonify
def test_jsonify():

    assert jsonify({'test': u'test'}, indent=4) == '{\n    "test": "test"\n}'



# Generated at 2022-06-12 23:41:12.539476
# Unit test for function to_native
def test_to_native():
    #to_native - Python3 compatibility wrapper around unicode(string, encoding)
    to_native("", encoding='utf-8')
    #to_native - Python3 compatibility wrapper around unicode(string, encoding)
    to_native("", encoding='utf-8', nonstring='simplerepr')
    #to_native - Python3 compatibility wrapper around unicode(string, encoding)
    to_native("", encoding='utf-8', nonstring='passthru')
    #to_native - Python3 compatibility wrapper around unicode(string, encoding)
    to_native("", encoding='utf-8', nonstring='strict')
    #to_native - Python3 compatibility wrapper around unicode(string, encoding)
    to_native("", encoding='utf-8', nonstring='empty')
    #to_native - Python3 compatibility wrapper around unicode(

# Generated at 2022-06-12 23:41:19.714852
# Unit test for function jsonify
def test_jsonify():
    # Test basic JSON conversion
    assert '"true"' == jsonify(True)
    assert '"Value"' == jsonify("Value")
    assert '"123"' == jsonify(123)
    assert '{"a": "True"}' == jsonify({'a': True})

    # Test datetime
    t = datetime.datetime(2017,1,1,1,1,1)
    assert '"2017-01-01T01:01:01"' == jsonify(t)

    # Test sets
    assert '[1, 2, 3]' == jsonify({1, 2, 3})

    # Test unicode
    assert '"\u2018"' == jsonify(u'\u2018')

    # Test Invalid encoding

# Generated at 2022-06-12 23:41:21.500994
# Unit test for function to_native
def test_to_native():
    assert('foo'==to_native(u'foo'))



# Generated at 2022-06-12 23:41:40.056240
# Unit test for function to_native
def test_to_native():
    # If a byte string is passed in no change should occur
    # This is important to make sure we can handle binary data
    # when it is present
    assert to_native(b'foo') == b'foo'

    # If we're in Python2 and a unicode string is passed in,
    # no change should occur
    assert to_native(u'foo') == u'foo'

    # If we're in Python3 and a text string is passed in,
    # no change should occur
    assert to_native(u'foo') == u'foo'

    # If we're in Python2 and a text string is passed in,
    # it should be decoded to unicode
    assert to_native('foo') == u'foo'

    # If we're in Python3 and a byte string is passed in,
    # it should be decoded to

# Generated at 2022-06-12 23:41:51.771935
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a': 'Hello World'}) == '{"a": "Hello World"}'
    assert jsonify({'a': u'Hello World'}) == '{"a": "Hello World"}'
    assert jsonify({'a': 'Hello World', u'b': u'Hello World'}) == '{"a": "Hello World", "b": "Hello World"}'
    assert jsonify({'a': 'Hello World', u'b': u'Hello World', 'c': '\xc7'}) == '{"a": "Hello World", "b": "Hello World", "c": "\xc7"}'
    assert jsonify({'a': 'Hello World', u'b': u'Hello World', 'c': u'\xc7'}) == '{"a": "Hello World", "b": "Hello World", "c": "\xc7"}'

# Generated at 2022-06-12 23:42:01.386428
# Unit test for function to_bytes
def test_to_bytes():

    # Test all the nonstring settings
    assert to_bytes(1, nonstring='empty') == to_bytes('')
    assert to_bytes(1, nonstring='passthru') == 1
    with pytest.raises(TypeError):
        to_bytes(1, nonstring='strict')
    assert u'1'.encode('utf-8') == to_bytes(1, nonstring='simplerepr')

    # Test with a utf-8 text string
    assert u'spam'.encode('utf-8') == to_bytes(u'spam')
    assert u'spam'.encode('utf-8') == to_bytes(u'spam')
    # Test with a latin-1 text string

# Generated at 2022-06-12 23:42:07.580680
# Unit test for function to_native
def test_to_native():
    assert to_native(u'this is a test') == u'this is a test'
    assert to_native(u'this is a test'.encode('utf-8')) == u'this is a test'
    assert to_native(b'\xe4\xbd\xa0\xe5\xa5\xbd') == '\xe4\xbd\xa0\xe5\xa5\xbd'
    assert to_native(5) == 5



# Generated at 2022-06-12 23:42:12.915563
# Unit test for function jsonify
def test_jsonify():
    assert jsonify([1, 2, 3]) == '[1, 2, 3]'
    assert jsonify({'a': 1, 'b': 2, 'c': 3}) == '{"a": 1, "b": 2, "c": 3}'
    assert jsonify('1') == '"1"'



# Generated at 2022-06-12 23:42:20.541698
# Unit test for function to_bytes
def test_to_bytes():
    # to_bytes works on byte strings
    assert PY3 or type(to_bytes('foo')) is binary_type
    assert to_bytes(b'foo') == b'foo'

    # to_bytes works on text strings
    assert not PY3 or type(to_bytes(u'foo')) is binary_type
    assert to_bytes(u'foo') == b'foo'

    # to_bytes works on non-strings
    assert to_bytes(42) == b'42'
    assert to_bytes([u'42']) == b"[u'42']"
    assert to_bytes(Set([1, 2])) == b"set([1, 2])"
    assert to_bytes(datetime.datetime.now())[:13] == b'2013-06-12 13:'

    # to_bytes can

# Generated at 2022-06-12 23:42:27.287901
# Unit test for function jsonify
def test_jsonify():
    from ansible.utils import jsonify
    from collections import OrderedDict
    from datetime import datetime
    from ansible.module_utils.six import (
        PY3,
        text_type,
        binary_type,
    )
    # ord_dict = OrderedDict([('name', 'Prince'), ('age', 12), ('grade', '1st'), ('gender', 'M')])
    # setting utf8 encoded strings in data
    ord_dict = OrderedDict([('name', 'Pranavi'), ('age', 24), ('grade', '1st'), ('gender', 'F'),
                            ('hobbies', ['Writing','Reading','Coding','Travelling','Watching Tv Shows','Singing'])])
    jsonify_text = jsonify(ord_dict)

# Generated at 2022-06-12 23:42:31.018631
# Unit test for function jsonify
def test_jsonify():
    try:
        jsonify(b'\xe4')
    except UnicodeDecodeError:
        # The order depends on Python version.
        pass
    else:
        assert False



# Generated at 2022-06-12 23:42:37.039518
# Unit test for function to_native
def test_to_native():
    assert to_native(None) is None
    assert to_native(b'foo') == 'foo'
    assert to_native('foo') == 'foo'
    assert to_native(42) == 42
    assert to_native(u'\u043f\u0440\u0438\u0432\u0456\u0442') == u'\u043f\u0440\u0438\u0432\u0456\u0442'



# Generated at 2022-06-12 23:42:40.727596
# Unit test for function jsonify
def test_jsonify():
    '''
    input:
      data: {"s":"\xe3\x80\x80"}
      encoding: utf-8
    output:
      "{\"s\": \"\u3000\"}"
    '''
    data = jsonify({"s":"\xe3\x80\x80"})
    assert data == "{\"s\": \"\u3000\"}"


# Generated at 2022-06-12 23:42:55.338226
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('string') == b'string'
    assert to_bytes(b'bytes') == b'bytes'
    assert to_bytes(1) == b'1'
    assert to_bytes(u'\u2019') == b'\xe2\x80\x99'
    assert to_bytes(u'\u2019', errors='replace') == b'?'
    assert to_bytes(u'\u2019', errors='surrogate_or_replace') == b'\xef\xbf\xbd'
    try:
        to_bytes(u'\u2019', errors='surrogate_or_strict')
    except UnicodeEncodeError:
        pass
    else:
        raise AssertionError('to_bytes() should have raised UnicodeEncodeError')

# Generated at 2022-06-12 23:43:06.537032
# Unit test for function to_native
def test_to_native():

    # Check that to_native is able to return unicode objects
    unicode_text = u'this is a unicode string'
    assert isinstance(to_native(unicode_text), text_type)

    # Check that to_native is able to return byte objects
    byte_text = b'this is a byte string'
    assert isinstance(to_native(byte_text), binary_type)

    # Check that to_native is able to return subclassed str/unicode objects
    class TestArray(str):
        pass
    class TestUnicode(text_type):
        pass
    assert isinstance(to_native(TestArray(byte_text)), TestArray)
    assert isinstance(to_native(TestUnicode(unicode_text)), TestUnicode)

    # Check that to_native is able to return text type

# Generated at 2022-06-12 23:43:17.188458
# Unit test for function to_native
def test_to_native():
    def check_to_native(value, expected_native, encoding='utf-8'):
        if PY3:
            # If we're in Python3 we want to check that not only will
            # to_native return the expected native string but that decoding
            # the native string back to utf-8 gives us the original string
            # We need to do this as we are not enforcing unicode anywhere.
            if isinstance(expected_native, text_type):
                expected_native = expected_native.encode(encoding)
            actual_native = to_native(value, encoding=encoding)
            if expected_native != actual_native:
                print('to_native returned: %s' % repr(actual_native))
                print('expected: %s' % repr(expected_native))
                assert False
            actual_text = to_text

# Generated at 2022-06-12 23:43:20.972307
# Unit test for function to_native
def test_to_native():
    assert to_native(u'\u270d') == u'\u270d'
    assert to_native(b'\xe2\x9c\x8d') == u'\u270d'
    assert to_native('\xe2\x9c\x8d') == u'\u270d'



# Generated at 2022-06-12 23:43:32.825455
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('some text') == b'some text'
    assert to_bytes('some text', nonstring='strict') == b'some text'
    assert to_bytes(b'bytes') == b'bytes'
    assert to_bytes(b'bytes', nonstring='strict') == b'bytes'
    assert to_bytes(u'\u20ac', errors='surrogate_then_replace') == b'?'
    assert to_bytes(u'\u20ac', encoding='latin-1', errors='surrogate_then_replace') == b'\xe2\x82\xac'
    assert to_bytes(u'\u20ac', encoding='latin-1', errors='surrogate_or_replace') == b'?'

# Generated at 2022-06-12 23:43:41.316367
# Unit test for function to_native
def test_to_native():

    assert to_native(to_bytes(u'Hello')) == u'Hello'
    assert to_native(to_bytes(u'Hello', errors='surrogate_or_strict')) == u'Hello'
    assert to_native(to_bytes(u'Hello', errors='surrogate_or_replace')) == u'Hello'
    assert to_native(to_bytes(u'Hello', errors='surrogate_then_replace')) == u'Hello'
    assert to_native(to_bytes(u'Hello', encoding='ascii')) == u'Hello'
    assert to_native(to_bytes(u'Hello', encoding='ascii', errors='surrogate_or_strict')) == u'Hello'

# Generated at 2022-06-12 23:43:51.089597
# Unit test for function jsonify
def test_jsonify():
    from ansible import module_utils
    import datetime
    data = dict(a=1, b=2, c="日本語")
    assert module_utils.jsonify(data) == u'{"a": 1, "c": "\\u65e5\\u672c\\u8a9e", "b": 2}'
    data_2 = dict(a=1, b=2, c=u"日本語".encode("utf-8"))
    assert module_utils.jsonify(data_2) == u'{"a": 1, "c": "\\u65e5\\u672c\\u8a9e", "b": 2}'
    data_3 = dict(a=1, b=2, c=u"日本語".encode("latin-1"))

# Generated at 2022-06-12 23:43:56.151537
# Unit test for function to_native

# Generated at 2022-06-12 23:44:02.994571
# Unit test for function jsonify
def test_jsonify():
    data = {'str_key':'str_val',
            'unicode_key':u'unicode_val',
            'bytes_key':b'bytes_val'}

    assert jsonify(data) == '{"bytes_key": "bytes_val", "str_key": "str_val", "unicode_key": "unicode_val"}'


# Generated at 2022-06-12 23:44:08.143749
# Unit test for function jsonify
def test_jsonify():
    data = dict(listOfDict=[dict(name='joey', color='red'), dict(name='finn', color='blue')])
    data_text = dict(listOfDict=[dict(name=u'joey', color=u'red'), dict(name=u'finn', color=u'blue')])
    data_utf8  = '{"listOfDict": [{"name": "joey", "color": "red"}, {"name": "finn", "color": "blue"}]}'
    data_latin1 = '{"listOfDict": [{"name": "joey", "color": "red"}, {"name": "finn", "color": "blue"}]}'
    assert jsonify(data) == data_utf8
    assert jsonify(data_text) == data_utf8
   

# Generated at 2022-06-12 23:44:21.692734
# Unit test for function to_native
def test_to_native():
    assert to_native(None) == 'None'
    assert to_native(True) == 'True'
    assert to_native(False) == 'False'
    assert to_native(1) == '1'
    assert to_native(1000) == '1000'
    assert to_native(1.1) == '1.1'
    assert to_native(set(('a', 'b'))) == "{'a', 'b'}"
    assert to_native(set(['a', 'b'])) == "{'a', 'b'}"
    assert to_native(set((('a', 'b'), ('x', 'y')))) == "{('a', 'b'), ('x', 'y')}"

# Generated at 2022-06-12 23:44:32.074883
# Unit test for function to_bytes
def test_to_bytes():
    # To_bytes should never return a text string it should always be a byte string
    assert isinstance(to_bytes(u"hi"), binary_type)
    assert isinstance(to_bytes(b"hi"), binary_type)

    # If the original object was a text string is should be able to transform
    # back to the original string
    assert to_text(to_bytes(u"hi"), errors="surrogate_or_strict") == u"hi"
    assert to_text(to_bytes(u"hì"), errors="surrogate_or_strict") == u"hì"

    # If the original object was not a string it should return a byte string
    # representation of the object
    assert to_text(to_bytes(42), errors="surrogate_or_strict") == u"42"



# Generated at 2022-06-12 23:44:44.534370
# Unit test for function to_bytes
def test_to_bytes():
    # Make sure that we raise TypeError for nonstrings if strict is specified
    for nonstring in ('simplerepr', 'passthru', 'empty'):
        try:
            to_bytes(object(), nonstring=nonstring)
        except TypeError:
            assert nonstring == 'strict', 'Nonstring %s failed' % nonstring

    # Test to_bytes of a text string with various error handlers
    assert to_bytes('\u2713', errors='strict') == b'\xe2\x9c\x93'
    assert to_bytes('\u2713', errors='surrogateescape') == b'\xe2\x9c\x93'
    assert to_bytes('\u2713', errors='surrogate_then_replace') == b'\xe2\x9c\x93'
    assert to

# Generated at 2022-06-12 23:44:51.265203
# Unit test for function jsonify
def test_jsonify():
    from nose.tools import assert_true
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import PY2

    if PY2:
        # This does not work with PY3 as you can not serialize bytes
        # in json with PY3
        my_data = {'bytes1': to_bytes("all your base"),
                   'bytes2': to_bytes("are belong to us"),
                   'text': to_text("Leet"),
                   'mixed': to_bytes("\xa1\xa2\xab\xac\xd7\xd8\xdf\xe0"),
                   }
        my_json_data = jsonify(my_data)

# Generated at 2022-06-12 23:45:00.340547
# Unit test for function jsonify
def test_jsonify():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.six as six

    if six.PY3:
        unicode_type = str
    else:
        unicode_type = unicode

    text_value = u"foobar"
    list_value = [u"foobar"]
    dict_value = {u"foobar": u"foobar"}
    basic_obj = basic.AnsibleModule(argument_spec=dict(foobar=dict()))
    set_value = set([u"foobar"])
    datetime_value = datetime.datetime.now()

    for value in [text_value, list_value, dict_value, basic_obj, set_value, datetime_value]:
        assert jsonify(value) is not None

    # Test encodings


# Generated at 2022-06-12 23:45:09.414968
# Unit test for function to_bytes
def test_to_bytes():
    '''
    >>> test_to_bytes()
    '''
    # This probably won't happen as we generally don't use complex encodings
    # but the test is here just in case.
    #
    # Note that we can't use u'\u1234' throughout the test because python2.4
    # can't compile that.  We end up using u'\xe1\x88\xb4' instead of u'ሴ'

# Generated at 2022-06-12 23:45:17.337605
# Unit test for function to_bytes
def test_to_bytes():
    class Unencodable(object):
        def __repr__(self):
            raise UnicodeError()

    for obj in (u'foo',  # unicode string
                to_bytes(u'foo'),  # byte string
                Unencodable(),  # nonstring with simplerepr
                [u'foo'],  # nonstring with simplerepr
                {u'foo': u'bar'},  # nonstring with simplerepr
                Unencodable(),  # nonstring with passthru
                [u'foo'],  # nonstring with passthru
                {u'foo': u'bar'}):  # nonstring with passthru
        test_value = to_bytes(obj)
        assert isinstance(test_value, binary_type)
        assert test_value == b'foo'

    # None is

# Generated at 2022-06-12 23:45:28.476200
# Unit test for function jsonify
def test_jsonify():
    """Test the jsonify function"""

    assert jsonify(dict(a=dict(b=1), l=[1, 2, 3])) == '{"a": {"b": 1}, "l": [1, 2, 3]}'

    assert jsonify(dict(a='a', b='b')) == '{"a": "a", "b": "b"}'

    assert jsonify(dict(a=u'\u00e9')) == '{"a": "\\u00e9"}'

    assert jsonify(dict(a=u'\u00e9'), ensure_ascii=False) == '{"a": "\\u00e9"}'

    assert jsonify(dict(a=u'\u00e9'), ensure_ascii=True) == '{"a": "\\\\u00e9"}'


# Generated at 2022-06-12 23:45:38.592364
# Unit test for function to_native
def test_to_native():

    astr = 'astring'
    aunicode = u'a unicode \u2019 string'
    abyte = astr.encode('utf-8')

    test_cases = dict(
        unicode_to_native=dict(
            text=aunicode,
            expected=aunicode,
        ),
        bytes_to_native=dict(
            text=abyte,
            expected=astr,
        ),
        bytes_to_unicode=dict(
            text=abyte,
            expected=aunicode,
        ),
    )

    def _to_native(case):
        text = case['text']
        try:
            result = to_native(text)
        except UnicodeError:
            result = None
        return result == case['expected']


# Generated at 2022-06-12 23:45:39.968980
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u"t\xe9st") == u'"t\xe9st"'



# Generated at 2022-06-12 23:45:50.415425
# Unit test for function jsonify
def test_jsonify():
    assert '"test"' == jsonify('test')
    assert '"\\u1234"' == jsonify(u'\u1234')
    assert '{"test": "\\u1234"}' == jsonify({'test': u'\u1234'})
    assert jsonify([u'\u1234']) == '["\\u1234"]'



# Generated at 2022-06-12 23:46:00.376707
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('a') == b'a'

    assert to_bytes(u'☃') == b'\xe2\x98\x83'
    assert to_bytes(u'☃', errors='surrogate_or_strict') == b'\xe2\x98\x83'
    assert to_bytes(u'☃', errors='surrogate_or_replace') == b'\xe2\x98\x83'
    assert to_bytes(u'\ud800') == b'\xed\xa0\x80'
    assert to_bytes(u'☃', errors='surrogate_then_replace') == b'\xe2\x98\x83'
    assert to_bytes(u'\ud800', errors='surrogate_then_replace') == b'?'

   

# Generated at 2022-06-12 23:46:09.493421
# Unit test for function to_native
def test_to_native():
    assert to_native('simple') == u'simple'
    assert to_native(b'byte_string') == u'byte_string'
    assert to_native(u'simple') == u'simple'
    assert to_native('\u2019') == u'\u2019'
    assert to_native(b'\xe2\x80\x99') == u'\u2019'
    # assert to_native(b'\xff') == u'\ufffd'
    # assert to_native(u'\u2019'.encode('latin-1')) == u'\ufffd'



# Generated at 2022-06-12 23:46:16.480073
# Unit test for function jsonify
def test_jsonify():
    for json_str in (six.u('{"str": "str", "str2": "str2"}'), six.u('{"str": "str", "str2": "str2"}'), six.u('''{
        "obj": {
            "str": "str",
            "str2": "str2"
        },
        "str": "str",
        "str2": "str2"
    }''')):
        try:
            data = json.loads(json_str)
        except ValueError:
            continue
        if data != json.loads(jsonify(data)):
            raise Exception('Failed to jsonify data and get same result.')



# Generated at 2022-06-12 23:46:27.642093
# Unit test for function to_bytes
def test_to_bytes():
    # All of them return the same thing, this is just to make sure that they
    # all work
    assert to_bytes('1') == b'1'
    assert to_bytes(u'1') == b'1'
    assert to_bytes(u'\u043f\u0440\u0438\u0432\u0435\u0442') == b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# Generated at 2022-06-12 23:46:34.963501
# Unit test for function to_native
def test_to_native():
    """
    Basic unit test for function to_native
    """
    from ansible.module_utils._text import to_native

    class TestClass(unicode):
        pass

    assert to_native(u"foo") == u"foo"
    assert to_native(b"foo") == u"foo"
    assert to_native(TestClass(b"foo")) == u"foo"
    assert isinstance(to_native(TestClass(b"foo")), unicode)
    assert to_native(TestClass(b"foo"), nonstring='passthru') == TestClass(u"foo")
    assert to_native(TestClass(b"foo"), nonstring='empty') == u""
    try:
        to_native(datetime.datetime.now(), nonstring='strict')
    except TypeError:
        pass


# Generated at 2022-06-12 23:46:43.854188
# Unit test for function to_bytes
def test_to_bytes():
    teststring = u'sé'
    assert to_bytes(teststring) == b's\xc3\xa9'
    assert to_bytes(teststring.encode('cp1252')) == b's\xe9'
    # Check that surrogate_then_replace works
    assert to_bytes(u'\udce2\udce4this string is not going to decode', errors='surrogate_then_replace') == b'\xef\xbf\xbd\xef\xbf\xbdthis string is not going to decode'
    assert isinstance(to_bytes(u'\udce2\udce4this string is not going to decode', errors='surrogate_then_replace'), binary_type)

    # Check that surrogate_or_replace works

# Generated at 2022-06-12 23:46:54.032130
# Unit test for function jsonify
def test_jsonify():
    json_str = jsonify({u'a': u'b'})
    assert json_str == '{"a": "b"}'
    json_str = jsonify({u'a': u'b'}, separators=(',', ':'))
    assert json_str == '{"a":"b"}'
    json_str = jsonify({u'a': u'b'}, separators=(',', ':') , sort_keys=True)
    assert json_str == '{"a":"b"}'
    json_str = jsonify({u'a': u'b'}, sort_keys=True)
    assert json_str == '{"a": "b"}'


# Generated at 2022-06-12 23:47:04.688916
# Unit test for function to_bytes
def test_to_bytes():
    # Test with no nonstring value
    result = to_bytes('test')
    assert isinstance(result, binary_type)
    assert result == b'test'

    result = to_bytes('test', nonstring='simplerepr')
    assert isinstance(result, binary_type)
    assert result == b'test'

    result = to_bytes(b'test', nonstring='simplerepr')
    assert isinstance(result, binary_type)
    assert result == b'test'

    result = to_bytes(b'test', nonstring='passthru')
    assert isinstance(result, binary_type)
    assert result == b'test'

    result = to_bytes(b'test', nonstring='empty')
    assert isinstance(result, binary_type)
    assert result == b''


# Generated at 2022-06-12 23:47:09.308351
# Unit test for function jsonify
def test_jsonify():
    data = {u'a':1, u'\u8000':2, b'b':3, u'c':u'\xe9\u20ac'}
    #Ensure to jsonify works as expected
    result = jsonify(data)
    #Ensure to jsonify handles non ascii character
    assert(u'\xe9\u20ac' in result)


# Generated at 2022-06-12 23:47:29.713751
# Unit test for function jsonify
def test_jsonify():
    # Test with valid data
    assert jsonify([{"name": "John Doe"}, {"name": "Jane Doe"}]) == '[{"name": "John Doe"}, {"name": "Jane Doe"}]'

    # Test with invalid encoding
    try:
        jsonify([{"name": u"ÄÖÜ"}])
        assert False, "Exception should have been raised"
    except UnicodeError:
        pass

    # Test with invalid type
    try:
        jsonify([{"name": Set([1, 2, 3])}])
        assert False, "Exception should have been raised"
    except TypeError:
        pass

    # Test with datetime
    assert jsonify([{"name": datetime.datetime(2005, 8, 15, 15, 37, 0)}]) == '[{"name": "2005-08-15T15:37:00"}]'



# Generated at 2022-06-12 23:47:33.007578
# Unit test for function jsonify
def test_jsonify():
    import six
    if six.PY2:
        assert jsonify('"\xe2\x80\x99"') == '"\\u2019"'
    else:
        assert jsonify('"\xe2\x80\x99"') == '"’"'



# Generated at 2022-06-12 23:47:37.629426
# Unit test for function jsonify
def test_jsonify():
    assert '{"a": 1, "b": 2}' == jsonify({u'a': 1, u'b': 2})
    assert '["spam", "eggs"]' == jsonify([u'spam', u'eggs'])
    assert '{"a": ["spam", "eggs"]}' == jsonify({u'a': [u'spam', u'eggs']})


# Generated at 2022-06-12 23:47:39.897380
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(True) == 'true'
    assert jsonify('foo') == '"foo"'
    assert jsonify(1) == '1'



# Generated at 2022-06-12 23:47:47.651041
# Unit test for function to_bytes
def test_to_bytes():
    # These versions should all work in both python2 and 3
    # single byte strings
    assert to_bytes('hello world') == b'hello world'
    assert to_bytes('中国') == b'\xe4\xb8\xad\xe5\x9b\xbd'
    assert to_bytes('中国', encoding='latin1') == b'\xd6\xd0\xb9\xfa'
    assert to_bytes('\udcc3\udca5', encoding='cp950') == b'\xa5E\xa5A'

    # multi-byte strings

# Generated at 2022-06-12 23:47:58.775385
# Unit test for function to_native
def test_to_native():
    if PY3:
        # This is a test of the actual function being tested.  pylint: disable=protected-access
        assert json._native_types_stringify == 'transparent'
        # pylint: enable=protected-access
        # If a text string is passed in we need to first encode that as bytes to
        # test the true behavior of the function
        returns = to_native('test string')
        assert isinstance(returns, str)

        returns = to_native(u'test string')
        assert isinstance(returns, str)

        returns = to_native(u'test string'.encode('utf-8'))
        assert isinstance(returns, str)

        returns = to_native(u'test string'.encode('utf-16'))
        assert isinstance(returns, str)

       

# Generated at 2022-06-12 23:48:07.216531
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'unicode string') == b'unicode string'
    assert to_bytes(u'\u30aa\u30ea\u30b8\u30ca\u30eb') == b'\xe3\x82\xaa\xe3\x83\xaa\xe3\x82\xb8\xe3\x82\xca\xe3\x83\xab'
    assert to_bytes(u'\u30aa\udc30\u30b8\u30ca\u30eb') == b'\xe3\x82\xaa?\xe3\x82\xb8\xe3\x82\xca\xe3\x83\xab'
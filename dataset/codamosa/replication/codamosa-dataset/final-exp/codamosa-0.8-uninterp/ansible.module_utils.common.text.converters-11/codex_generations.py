

# Generated at 2022-06-12 23:38:18.615412
# Unit test for function jsonify
def test_jsonify():
    # Note we expect to get an error on this one, but that means the function
    # correctly handled it and gave back a useful error message.
    assert isinstance(jsonify(dict(a=dict(b='\xd3'))), text_type)



# Generated at 2022-06-12 23:38:26.922503
# Unit test for function to_native
def test_to_native():
    ''' test_to_native module: utils.py '''
    from ansible.module_utils._text import to_native
    s_unicode_in = u"\u9993\u5e2d\u5047\u8a9e"
    s_unicode_out = "\u9993\u5e2d\u5047\u8a9e"
    s_unicode_out_py3 = s_unicode_out
    try:
        s_unicode_out_py3 = s_unicode_out.encode('utf-8').decode('latin-1')
    except UnicodeDecodeError:
        pass
    assert (isinstance(s_unicode_in, text_type))
    assert (isinstance(to_native(s_unicode_in), str))


# Generated at 2022-06-12 23:38:37.186729
# Unit test for function to_native
def test_to_native():
    from ansible.text.converters import to_native
    # to_native function
    assert to_native(u'test', encoding='ascii') == 'test'
    assert to_native(b'test') == 'test'
    assert to_native(34) == '34'
    assert to_native(to_text('34')) == '34'
    assert to_native(to_bytes('34')) == '34'
    # Python3 does not allow non-native strings to be used as dict keys
    #assert to_native(u'test', errors='surrogate_or_replace', nonstring='strict') == 'test'
    #assert to_native(to_text('test', 'ascii', 'surrogate_or_replace'), errors='surrogate_or_replace', nonstring='strict

# Generated at 2022-06-12 23:38:49.319580
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six import StringIO

    # Test when we're given a byte string
    assert to_bytes('text') == b'text'
    # Test when we're given a text string
    assert to_bytes(u'text') == b'text'
    # Test ensuring we decode surrogate pairs
    assert to_bytes(u'\udcc3\udca9') == b'\xed\xb3\x8b\xed\xba\xa9'
    # Test when we're given an object with a special repr
    class Foo(object):
        def __repr__(self):
            return str(self)
        def __str__(self):
            return u'text'
    assert to_bytes(Foo()) == b'text'

    # Test when we're given a text string that is not enc

# Generated at 2022-06-12 23:39:00.017708
# Unit test for function to_native
def test_to_native():
    # FIXME:
    # Doesn't handle bools correctly
    # Doesn't handle sets correctly
    # Doesn't handle datetime.date correctly
    # Doesn't handle datetime.time correctly
    # Doesn't handle datetime.datetime or datetime.timedelta correctly
    # Doesn't handle ints correctly
    # Doesn't handle floats correctly
    # Doesn't handle byte arrays correctly
    # Doesn't handle iterators correctly
    # Doesn't handle generators correctly
    # Doesn't handle complex to native correctly

    # doesn't handle None correctly
    assert to_native(None) is None

    # doesn't handle bools correctly
    assert to_native(False) is False
    assert to_native(True) is True

    # doesn't handle sets correctly
    assert to_native(set()) == set()
    assert to_native({1, 2, 3})

# Generated at 2022-06-12 23:39:10.387945
# Unit test for function to_bytes
def test_to_bytes():
    """Test to_bytes"""
    assert to_bytes(u'abc') == b'abc'
    assert to_bytes(u'\u1234', encoding='ascii') == b'?'
    assert to_bytes(u'\u1234', encoding='ascii', errors='replace') == b'?'
    assert to_bytes(u'\u1234') == b'\xe1\x88\xb4'
    assert to_bytes(u'\u1234', errors='replace') == b'\xe1\x88\xb4'
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(bytearray(b'abc')) == b'abc'
    assert to_bytes(123) == b'123'
    assert to_bytes(123, nonstring='empty')

# Generated at 2022-06-12 23:39:11.729025
# Unit test for function to_native
def test_to_native():
    assert to_native('test', 'utf-8') == u'test'



# Generated at 2022-06-12 23:39:17.112839
# Unit test for function to_native
def test_to_native():
    assert to_native(u'test {}', 'utf-8') == u'test {}'
    assert to_native(u'test {}'.encode('utf-8'), 'utf-8') == u'test {}'
    assert to_native(b'test {}', 'utf-8') == u'test {}'
    assert to_native(b'test {}', 'ascii') == u'test {}'



# Generated at 2022-06-12 23:39:26.535216
# Unit test for function jsonify
def test_jsonify():
    foo = {u'unicode_str': u'foo', 'bytestrings': b'bar'}
    jsonify(foo)
    foo2 = {u'unicode_str': u'한국어'}
    jsonify(foo2)
    foo3 = {u'unicode_str': u'привет'}
    jsonify(foo3)
    foo4 = {u'unicode_str': u'العربية'}
    jsonify(foo4)
    foo5 = {u'unicode_str': u'你好'}
    jsonify(foo5)



# Generated at 2022-06-12 23:39:34.655847
# Unit test for function jsonify
def test_jsonify():
    not_match = 0
    test_data = [
        {'aaa': 'bbb'},
        {u'aaa': 'bbb'},
        {u'aaa': u'bbb'},
        {'aaa': u'bbb'},
        {b'aaa': 'bbb'},
        {'aaa': b'bbb'},
        {b'aaa': b'bbb'},
    ]
    expect_data = [
        '{"aaa": "bbb"}',
        '{"aaa": "bbb"}',
        '{"aaa": "bbb"}',
        '{"aaa": "bbb"}',
        '{"aaa": "bbb"}',
        '{"aaa": "bbb"}',
        '{"aaa": "bbb"}',
    ]

# Generated at 2022-06-12 23:39:52.750417
# Unit test for function jsonify
def test_jsonify():
    data = '{"json":"obj"}'
    if PY3:
        assert jsonify(data) == data
    else:
        assert jsonify(data) == data.encode('utf-8')

    data = {"a": 1, "b": "text", "c": u"unic\u00d8de"}
    if PY3:
        assert jsonify(data) == '{"a": 1, "c": "unic\\u00d8de", "b": "text"}'
    else:
        assert jsonify(data) == '{"a": 1, "c": "unic\\u00d8de", "b": "text"}'.encode('utf-8')

# Generated at 2022-06-12 23:40:03.273413
# Unit test for function to_native
def test_to_native():
    if PY3:
        class Foo():
            def __str__(self):
                return u'☃'

        # Strings can be decoded into unicode
        assert to_native(b'unicode') == u'unicode'
        # byte literals can be decoded into unicode
        assert to_native(b'\xe2\x98\x83') == u'☃'
        assert to_native(br'\xe2\x98\x83') == u'☃'
        # obj.__str__() can be decoded into unicode
        assert to_native(Foo()) == u'☃'
        # Things that are already unicode are returned as unicode
        assert to_native(u'☃') == u'☃'
        # If a native string is passed in the encoding used is

# Generated at 2022-06-12 23:40:15.734879
# Unit test for function to_bytes
def test_to_bytes():
    # Function is tested with ansible.module_utils.basic.AnsibleModule
    from ansible.module_utils import six
    from ansible.module_utils._text import to_bytes

    # unicode
    assert to_bytes(u'ascii', errors='strict') == b'ascii'
    assert to_bytes(u'unicode', encoding='latin-1', errors='strict') == b'unicode'
    assert to_bytes(u'unicode', encoding='latin-1', errors='surrogate_then_replace') == b'unicode'
    if HAS_SURROGATEESCAPE:
        assert to_bytes(u'unicode\udcff', encoding='latin-1', errors='surrogate_then_replace') == b'unicode\ufffd'
        assert to

# Generated at 2022-06-12 23:40:24.571777
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.utils.unicode import to_bytes, to_text
    # A valid utf-8 string
    input_string = u'Iñtërnâtiônàlizætiøn'
    # The utf-8 bytes of the above string
    utf8_bytes = b'I\xc3\xb1t\xc3\xabrn\xc3\xa2ti\xc3\xb4n\xc3\xa0liz\xc3\xa6ti\xc3\xb8n'
    # Bytes that are a utf-16 encoding of the above string

# Generated at 2022-06-12 23:40:36.710425
# Unit test for function to_bytes
def test_to_bytes():
    def check(input, encoding, errors, nonstring, expect_type, expect_value,
              expect_errors=None):
        test_errors = errors if expect_errors is None else expect_errors
        result = to_bytes(input, encoding, test_errors, nonstring)
        assert type(result) is expect_type
        assert result == expect_value
        if expect_errors is not None:
            assert errors == expect_errors

    # Text strings
    if PY3:
        check('abcd\udc41', 'ascii', 'surrogate_then_replace', 'simplerepr',
              binary_type, b'abcd?')
        check('abcd\udc41', 'ascii', 'surrogate_or_replace', 'simplerepr',
              binary_type, b'abcd?')


# Generated at 2022-06-12 23:40:45.093490
# Unit test for function to_bytes
def test_to_bytes():
    '''
    Tests to_bytes function
    '''
    from ansible.utils.unicode import to_bytes
    test_str = 'This is a test string'
    test_bytes = 'This is a test string'
    result = to_bytes(test_str)
    assert(result == test_bytes)
    test_bytes = 'This is a test string'.encode('utf-16')
    result = to_bytes(test_str, encoding='utf-16')
    assert(result == test_bytes)

# Unit test function to_bytes


# Generated at 2022-06-12 23:40:53.007793
# Unit test for function to_bytes
def test_to_bytes():
    print('testing to_bytes with default encoding')
    assert b'foobar' == to_bytes('foobar', 'utf-8')
    assert b'\xe3\x81\x82' == to_bytes(u'\u3042', 'utf-8')
    assert b'\xe3\x81\x82' == to_bytes(u'\u3042', 'utf-8')
    assert b'\xe3\x81\x82' == to_bytes(u'\u3042', 'utf-8')
    assert b'\xc3\xbc' == to_bytes(u'\xc3\xbc', 'utf-8')
    assert b'\xef\xbf\xbd' == to_bytes(u'\ufffd', 'utf-8')

# Generated at 2022-06-12 23:40:54.964406
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(key='value')) == '{"key": "value"}'


# Generated at 2022-06-12 23:41:03.874559
# Unit test for function jsonify
def test_jsonify():
    # Dict
    data = {'a': u'\u6c49'}
    assert jsonify(data) == '{"a": "\u6c49"}'.encode('utf-8')
    # List
    data = [u'\u6c49']
    assert jsonify(data) == '["\u6c49"]'.encode('utf-8')
    # Tuple
    data = (u'\u6c49',)
    assert jsonify(data) == '["\u6c49"]'.encode('utf-8')
    # String
    data = 'abc'
    assert jsonify(data) == '"abc"'
    # int
    data = 123
    assert jsonify(data) == "123"

# TODO: fix this
# A function to transform a data structure to text objects

# Generated at 2022-06-12 23:41:08.640642
# Unit test for function jsonify
def test_jsonify():
    # testing json encode
    data = {u"\u6c49":u"\u6f22"}
    result = jsonify(data)
    assert result == '{"\\u6c49": "\\u6f22"}'

    # testing json encode
    data = {u"\u6c49":u"\u6f22", u"a":"a"}
    result = jsonify(data)
    assert result == '{"\\u6c49": "\\u6f22", "a": "a"}'

    # testing json encode
    data = {u"\u6c49":u"\u6f22", u"a":"a", 0.1: 1.22}
    result = jsonify(data)

# Generated at 2022-06-12 23:41:26.188374
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    import collections

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str'),
            mutable=dict(type='bool', default=False),
        ),
    )

    data = module.params['data']
    mutable = module.params['mutable']

    if mutable:
        data = collections.OrderedDict(sorted(data.items()))

    try:
        result = jsonify(data)
    except Exception as e:
        module.fail_json(msg=to_native(e), exception=traceback.format_exc())

    module.exit_json(msg=data, result=result)



# Generated at 2022-06-12 23:41:37.748377
# Unit test for function to_native
def test_to_native():
    assert to_native(1, encoding='ascii') == u'1'
    assert to_native('a', encoding='ascii') == u'a'
    assert to_native(b'a', encoding='ascii') == u'a'
    assert to_native(u'a', encoding='ascii') == u'a'
    assert to_native(1, nonstring='simplerepr') == '1'
    assert to_native(1, nonstring='passthru') == 1
    assert to_native(1, nonstring='empty') == u''
    assert to_native(1, nonstring='strict') == TypeError
    assert to_native(1, encoding='ascii') == u'1'

# Generated at 2022-06-12 23:41:42.113715
# Unit test for function jsonify
def test_jsonify():
    assert jsonify([u'\u2019']) == '["\u2019"]'
    assert jsonify({u'a': u'\u2019'}) == '{"a": "\u2019"}'
    assert jsonify(u'\u2019') == '"\u2019"'
    assert jsonify("\xe2\x80\x99") == '"\u2019"'



# Generated at 2022-06-12 23:41:54.548435
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import text_type

    assert isinstance(to_native(text_type(u'abc')), text_type)
    assert isinstance(to_native(b'abc'), text_type)
    assert isinstance(to_native({}), text_type)
    assert isinstance(to_native([]), text_type)
    assert isinstance(to_native(set()), text_type)

    assert to_native(text_type(u'abc')) == 'abc'
    assert to_native(b'abc') == 'abc'
    # On Python 2, JSON uses str() to convert
    assert to_native({}) == json.dumps({})
    assert to_native([]) == json.dumps([])
   

# Generated at 2022-06-12 23:42:03.467777
# Unit test for function jsonify
def test_jsonify():
    o = {}
    o['a'] = "ascii"
    o['b'] = u'\u1234'
    o['c'] = to_bytes(o['b'])
    o['d'] = {'a':'ascii','b':u'\u1234','c':o['c']}
    o['e'] = [o['a'], o['b'], o['c']]
    o['f'] = Set(['a','b','c'])
    o['g'] = 'a'
    o['h'] = 2
    json_str = jsonify(o)
    assert isinstance(json_str, text_type)

# Generated at 2022-06-12 23:42:06.904803
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'{"key": "value"}') == '{"key": "value"}'
    assert jsonify(u'{"key": "value"}', sort_keys=True) == '{"key": "value"}'



# Generated at 2022-06-12 23:42:16.842466
# Unit test for function to_native
def test_to_native():
    # Test that it tests for the right type
    try:
        to_native(1)
        assert False
    except TypeError:
        assert True

    # Test that a text string doesn't get converted
    text = u'こんにちは'
    assert isinstance(text, text_type)
    assert to_native(text) is text

    # Test that a bytestring in a good encoding doesn't get converted
    good_encoding = text.encode('utf-8')
    assert isinstance(good_encoding, binary_type)
    assert to_native(good_encoding) is good_encoding

    # Test that an explicit unicode string doesn't get converted
    assert isinstance(u'asdf', text_type)
    assert to_native(u'asdf') is u'asdf'

    #

# Generated at 2022-06-12 23:42:25.342420
# Unit test for function to_bytes
def test_to_bytes():
    import responses

    def assert_is_bytes(obj):
        assert isinstance(obj, binary_type)

    assert_is_bytes(to_bytes('hi'))
    assert_is_bytes(to_bytes('hi'.encode('utf-8')))
    assert_is_bytes(to_bytes('hi'.encode('utf-16'), encoding='utf-16'))
    assert_is_bytes(to_bytes('hi'.encode('utf-8'), encoding='utf-8'))

    assert_is_bytes(to_bytes('\U0001f642'))  # U+1F642 SLIGHTLY SMILING FACE
    assert_is_bytes(to_bytes('\U0001f642'.encode('utf-8')))

# Generated at 2022-06-12 23:42:36.045027
# Unit test for function to_native
def test_to_native():
    def f(obj, expected, exception=None, encoding='utf-8', errors=None, nonstring='simplerepr'):
        if type(expected) is type(exception):
            # They probably forgot to use the right class
            raise TypeError('test_to_native needs obj, expected result, and exception, not %s' % expected)
        if exception is not None:
            from ansible.module_utils.six import reraise
            try:
                result = to_native(obj, encoding=encoding, errors=errors, nonstring=nonstring)
            # This is correct: We're supposed to raise exception
            except exception:
                return
            except Exception as e:
                raise AssertionError('to_native did not throw %s when expected.  Instead it raised %s' % (exception, e))

# Generated at 2022-06-12 23:42:42.809160
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('{"a": ["foo", "bar"]}') == '{"a": ["foo", "bar"]}'
    assert jsonify({b'a': [b'foo', b'bar']}) == '{"a": ["foo", "bar"]}'
    assert jsonify({u'a': [u'foo', u'bar']}) == '{"a": ["foo", "bar"]}'



# Generated at 2022-06-12 23:42:57.772550
# Unit test for function to_native
def test_to_native():
    print("Test to_native")
    print("\tPY3 = %s" % PY3)
    print("\tcodecs.lookup_error('surrogateescape') = %s" % codecs.lookup_error('surrogateescape'))

    # TODO: MAKE SURE TO FIX THIS TESTING SECOND CALL BELOW
    # I THINK THING IS NOT SURE WHAT IMPORTED TO_NATIVE IS
    # SO IT CAN NOT INFER THE TYPE OF TO_NATIVE(OBJECT)
    # 
    # The goal of this function test is to see if function
    # to_native(object) works as expected.
    #
    # to_bytes(object) returns binary string in python 2, str
    # to_bytes(object) returns binary string in python 3, bytes
    # to_text(

# Generated at 2022-06-12 23:43:04.753187
# Unit test for function jsonify
def test_jsonify():
    print(jsonify({"a": 1, "b": 2}))
    print(jsonify({"a": "ssss", "b": 2}))
    print(jsonify({"a": "ssss", "b": "中文"}))
    print(jsonify({"a": 123, "b": 100}))
    print(jsonify({"a": "ssss", "b": "中文"}, ensure_ascii=False))


# Generated at 2022-06-12 23:43:13.569656
# Unit test for function to_bytes
def test_to_bytes():
    # Check that to_bytes always returns a bytes string
    assert isinstance(to_bytes('hi'), binary_type)
    assert isinstance(to_bytes(u'hi'), binary_type)
    assert isinstance(to_bytes('hi', nonstring='simplerepr'), binary_type)
    assert isinstance(to_bytes('hi', nonstring='passthru'), binary_type)
    assert isinstance(to_bytes('hi', nonstring='empty'), binary_type)

    # Check that encoded bytes strings are not decoded
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(b'foo', encoding='utf-8') == b'foo'

    # Check that str strings are encoded
    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b

# Generated at 2022-06-12 23:43:22.135795
# Unit test for function to_bytes
def test_to_bytes():
    """Unit tests for :func:`to_bytes.to_bytes`"""
    assert to_bytes(u'unicode_str') == b'unicode_str'
    assert to_bytes(b'bytes_str') == b'bytes_str'

    assert to_bytes(u'언어') == b'\xec\x96\xb8\xec\x96\xb4'
    assert to_bytes(b'\xec\x96\xb8\xec\x96\xb4') == b'\xec\x96\xb8\xec\x96\xb4'

    assert to_bytes(u'\udce4\udce8\udcec') == b'\xec\x96\xb8\xec\x96\xb4'

# Generated at 2022-06-12 23:43:33.302378
# Unit test for function to_bytes
def test_to_bytes():
    # simple test for the cases that should pass
    assert to_bytes('hello world', nonstring='passthru') == 'hello world'
    assert to_bytes(b'hello world', nonstring='passthru') == b'hello world'
    assert to_bytes(5, nonstring='passthru') == 5
    assert to_bytes(5, nonstring='simplerepr') == b'5'

    # Non-utf8 encoding
    assert to_bytes('hello world', 'latin-1') == b'hello world'
    assert to_bytes(b'hello world', 'latin-1') == b'hello world'
    if PY3:
        assert to_bytes(b'\xff\xfe\xe9\x00', 'latin-1') == b'\x00\xe9'

# Generated at 2022-06-12 23:43:42.989480
# Unit test for function to_native
def test_to_native():
    """
    Test the logic to_native
    """

    from ansible.module_utils._text import to_native

    assert to_native('foo') == 'foo'
    assert to_native(b'foo') == 'foo'
    assert to_native(b'foo'.decode('utf-8')) == 'foo'
    assert to_native(u'\u2713') == u'\u2713'
    assert to_native(u'\u2713'.encode('utf-8')) == u'\u2713'
    assert to_native(b'\xe2\x9c\x93') == u'\u2713'
    assert to_native(b'pl\xc3\xb4t') == u'pl\xf4t'

# Generated at 2022-06-12 23:43:48.508150
# Unit test for function to_native
def test_to_native():
    assert to_native(u'foo') == u'foo'

    if PY3:
        assert to_native('foo') == 'foo'
    else:
        assert to_native('foo') == u'foo'

    assert to_native(b'foo') == u'foo'

    # Test the error handlers
    try:
        to_native(b'\xff')
        raise AssertionError('Exception expected')
    except UnicodeDecodeError:
        pass
    assert to_native(b'\xff', errors='ignore') == u''
    if PY3:
        assert to_native(b'\xff', errors='surrogate_or_strict') == u''
    else:
        assert to_native(b'\xff', errors='surrogate_or_strict') == u'\ufffd'

# Generated at 2022-06-12 23:43:56.184576
# Unit test for function jsonify
def test_jsonify():
    from ansible.module_utils._text import to_text, to_bytes
    import json
    if PY3:
        str_type = str
        unicode_type = str
    else:
        str_type = str
        unicode_type = unicode

    data = { to_text(u'foo', nonstring='passthru'): u'bar', u'baz': [1, 2, 3]}
    assert jsonify(data) == '{"foo": "bar", "baz": [1, 2, 3]}'

    data = { to_bytes('foo', nonstring='passthru'): 'bar', 'baz': [1, 2, 3]}
    assert jsonify(data) == '{"foo": "bar", "baz": [1, 2, 3]}'


# Generated at 2022-06-12 23:44:07.540468
# Unit test for function jsonify
def test_jsonify():
    test_data = dict(foo=dict(bar='unicodeé'), biz=6, baz=[u'unicodeé'])
    test_json = jsonify(test_data)
    assert test_json == """{"foo": {"bar": "unicode\\u00e9"}, "biz": 6, "baz": ["unicode\\u00e9"]}"""


# In python2, dict.items() returns a list of items, and we cannot easily
# convert it to a generator without having to call iteritems().
#
# This function provides a way to create a dictionary generator in Python2.
# This is useful because many dictionaries we work with can be very large, and
# we should not have to consume large amounts of memory just to do things like
# iterate over the keys, or values in a dictionary.

# Generated at 2022-06-12 23:44:08.122949
# Unit test for function to_bytes
def test_to_bytes():
    pass

# Generated at 2022-06-12 23:44:22.004696
# Unit test for function to_native
def test_to_native():
    # pylint: disable=protected-access
    """Unit test for function to_native"""
    native = text_type('')

    # Test with an actual native string
    assert to_native(native) == native

    # Test byte string
    byte_string = binary_type('')
    assert to_native(byte_string) == native

    # Test with a non-string object
    assert to_native(25) == native
    assert to_native(datetime.datetime.now()) == native

    # Test different encoding and errors
    assert to_native(byte_string, encoding='ascii', errors='surrogate_or_strict') == native

    # Test the nonstring args
    # empty
    assert to_native(object(), nonstring='empty') == native
    # passthru

# Generated at 2022-06-12 23:44:32.297572
# Unit test for function to_bytes
def test_to_bytes():
    # Python 2
    if PY3:
        return
    assert to_bytes(u'\u1234') == '\xe1\x88\xb4'
    assert to_bytes(u'\u1234', encoding='latin-1') == '\xe1\x88\xb4'
    assert to_bytes(u'\u1234', encoding='ascii') == '\xe1\x88\xb4'
    assert to_bytes(u'\u1234', encoding='ascii', errors='ignore') == ''
    assert to_bytes(u'\u1234', encoding='ascii', errors='replace') == '?'
    assert to_bytes(u'\u1234', encoding='ascii', errors='surrogateescape') == '\xe1\x88\xb4'
   

# Generated at 2022-06-12 23:44:35.351561
# Unit test for function jsonify
def test_jsonify():
    data = {"test_data": b'\xc3\x14'}
    assert jsonify(data)


# Generated at 2022-06-12 23:44:38.214500
# Unit test for function to_native
def test_to_native():
   assert to_native(b'{"test":1}') == json.loads(to_native(b'{"test":1}'))



# Generated at 2022-06-12 23:44:47.911237
# Unit test for function to_bytes
def test_to_bytes():
    # This can't be a doctest because doctest doesn't allow us to properly test
    # bytes in Python2
    assert to_bytes('hello') == b'hello'
    assert to_bytes(u'hello') == b'hello'
    assert to_bytes(u'héllo') == b'h\xc3\xa9llo'
    assert to_bytes(u'héllo', encoding='latin-1') == b'h\xe9llo'
    assert to_bytes(b'hello') == b'hello'
    # We don't have a way to round trip these in doctest
    assert to_bytes(b'\xff') == b'\xff'
    assert to_bytes(u'\udce4\udcb3\udce5') == b'\xff\xff\xff'

# Generated at 2022-06-12 23:44:58.835794
# Unit test for function to_bytes
def test_to_bytes():
    # Use the greek word for "Is" in the following tests: 'Είναι'
    b_string = 'Είναι'.encode('utf-8')
    u_string = u'Είναι'
    i_string = b_string.decode('utf-8')

    assert isinstance(b_string, binary_type)
    assert not isinstance(b_string, text_type)
    assert isinstance(u_string, text_type)
    assert not isinstance(u_string, binary_type)
    assert isinstance(i_string, text_type)
    assert not isinstance(i_string, binary_type)

    assert to_bytes(b_string) == b_string

# Generated at 2022-06-12 23:45:08.186938
# Unit test for function to_bytes
def test_to_bytes():

    import sys
    import unittest

    class TestToBytes(unittest.TestCase):
        def setUp(self):
            pass
        def tearDown(self):
            pass
        def test_with_unicode_nonascii_input(self):
            test_input = u'f\u0191'
            reference = 'f\xc6\x91'
            test_output = to_bytes(test_input)
            self.assertTrue(isinstance(test_output, binary_type))
            self.assertEqual(test_output, reference)
        def test_with_unicode_surrogate_input(self):
            test_input = u'\udc80'
            reference = b'\xed\xb2\x80'
            test_output = to_bytes(test_input)


# Generated at 2022-06-12 23:45:14.601504
# Unit test for function to_bytes
def test_to_bytes():
    assert(to_bytes('"foo" bar') == b'"foo" bar')
    assert(to_bytes(u'"foo" bar') == b'"foo" bar')
    assert(to_bytes(u'"foo" bar', nonstring='strict') == b'"foo" bar')
    assert(to_bytes(u'"foo" bar', nonstring='empty') == b'')
    assert(to_bytes(b'"foo" bar', nonstring='passthru') == b'"foo" bar')
    assert(to_bytes(b'"foo" bar', nonstring='simplerepr') == b'"foo" bar')



# Generated at 2022-06-12 23:45:19.393593
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('{"a": ["b", "c"]}') == '{"a": ["b", "c"]}'
    assert jsonify(dict(a=1, b='2', c=(3, 4))) == '{"a": 1, "b": "2", "c": [3, 4]}'
    assert jsonify(dict(a=1, b=u'2', c=u'\u20ac')) == '{"a": 1, "b": "2", "c": "\\u20ac"}'



# Generated at 2022-06-12 23:45:25.450276
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(dict(foo='bar')) == b'{"foo": "bar"}'
    assert jsonify({ to_text(k, errors='surrogate_or_strict'): to_text(v, errors='surrogate_or_strict') for k,v in iteritems(dict(foo='bar'))}) == b'{"foo": "bar"}'



# Generated at 2022-06-12 23:45:41.375401
# Unit test for function jsonify
def test_jsonify():
    a = jsonify({"foo":"bar"})
    assert a == '{"foo": "bar"}'
    a = jsonify({"foo":u"bar"})
    assert a == '{"foo": "bar"}'
    a = jsonify({"foo":b"bar"})
    assert a == '{"foo": "bar"}'
    a = jsonify({"foo":1})
    assert a == '{"foo": 1}'
    a = jsonify({"foo":True})
    assert a == '{"foo": true}'
    a = jsonify({"foo":False})
    assert a == '{"foo": false}'
    a = jsonify({"foo":None})
    assert a == '{"foo": null}'
    a = jsonify([{"foo":"bar"}])

# Generated at 2022-06-12 23:45:52.483334
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'A text string') == b'A text string'
    assert to_bytes(b'A byte string') == b'A byte string'
    assert to_bytes(12345) == b'12345'

    # Using simplerepr strategy
    assert to_bytes(12345, nonstring='simplerepr') == b'12345'

    # Empty strings give empty strings
    assert to_bytes('', nonstring='simplerepr') == b''

    # Using empty strategy
    assert to_bytes([1, 2, 3], nonstring='empty') == b''

    # Using strict strategy
    try:
        to_bytes([1, 2, 3], nonstring='strict')
    except TypeError:
        pass
    else:
        assert False, 'Non-string was passed without error'

    # Using pas

# Generated at 2022-06-12 23:45:55.813780
# Unit test for function jsonify
def test_jsonify():
    test_data = "{\"a\": \"2\"}"
    result = jsonify(test_data)
    assert result == test_data
    revert_data = json.loads(result)
    assert revert_data == {"a": "2"}



# Generated at 2022-06-12 23:46:08.032537
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'foo'.encode('utf-16'), encoding='utf-8') == b'foo'
    assert to_bytes(b'foo') == b'foo'

    # nonstring
    assert to_bytes('foo', nonstring='simplerepr') == b'foo'
    assert to_bytes('foo', nonstring='passthru') == 'foo'
    assert to_bytes('foo', nonstring='empty') == b''
    assert to_bytes(b'foo', nonstring='simplerepr') == b'foo'
    assert to_bytes(b'foo', nonstring='passthru') == b'foo'
    assert to_bytes(b'foo', nonstring='empty')

# Generated at 2022-06-12 23:46:14.978434
# Unit test for function to_bytes
def test_to_bytes():
    # Create a source string that is hard to encode
    bs = bytearray(range(0, 256))
    src = bs.decode('latin-1', 'surrogateescape')

    # Run it through to_bytes
    data = to_bytes(src)
    assert not isinstance(data, text_type)
    decoded = data.decode('utf-8')

    # Run it through to_text to make sure it's the same as the original
    # This would fail if to_bytes wasn't using surrogateescape
    assert src == to_text(data, errors='surrogateescape')



# Generated at 2022-06-12 23:46:26.143751
# Unit test for function to_bytes
def test_to_bytes():
    # Test to_bytes with different values and nonstring settings
    assert to_bytes('foo') == b'foo'
    assert to_bytes(b'foo') == b'foo'
    assert to_bytes(u'\u2603') == b'\xe2\x98\x83'
    assert to_bytes('こんにちは') == b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf'
    assert to_bytes(u'\u2603'.encode('utf-8'), errors='surrogate_or_strict') == b'\xe2\x98\x83'


# Generated at 2022-06-12 23:46:29.907860
# Unit test for function to_native
def test_to_native():
    """Should take unicode types and convert to bytestrings"""
    assert isinstance(to_native(u'foo'), bytes)
    assert isinstance(to_native(u'привет'), bytes)
    assert isinstance(to_native(u'⽔'), bytes)



# Generated at 2022-06-12 23:46:36.162301
# Unit test for function to_native
def test_to_native():
    assert to_native({'a': 'a'}) == {'a': 'a'}
    class FakeUnicodeObj(object):
        def __str__(self):
            raise UnicodeError('Cannot convert to str')
        def __repr__(self):
            raise UnicodeError('Cannot convert to repr')

    assert to_native(FakeUnicodeObj()) == u''



# Generated at 2022-06-12 23:46:44.732919
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u'{"foo":"bar"}') == '{"foo":"bar"}'
    assert jsonify(u'{"baz":"whÄts"}') == '{"baz":"whÄts"}'
    assert jsonify({u'foo': u'bar'}) == '{"foo": "bar"}'
    assert jsonify({u'baz': u'whÄts'}) == '{"baz": "whÄts"}'
    assert jsonify(u'\u00a1Hola!') == '"\\u00a1Hola!"'
    assert jsonify({u'foo': [1, 2, 3]}) == '{"foo": [1, 2, 3]}'

# Generated at 2022-06-12 23:46:56.104026
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({}) == '{}'
    assert jsonify({'dict': {'key': 'value'}}) == '{"dict": {"key": "value"}}'
    assert jsonify({'list': ['value1', 'value2']}) == '{"list": ["value1", "value2"]}'
    assert jsonify({'string': u'value'}) == '{"string": "value"}'
    assert jsonify({'set': set(['a', 'b', 'c'])}) == '{"set": ["a", "b", "c"]}'
    assert jsonify({'unicode': u'\u4f60\u597d'}, ensure_ascii=False) == '{"unicode": "\\u4f60\\u597d"}'

# Generated at 2022-06-12 23:47:10.911500
# Unit test for function to_native

# Generated at 2022-06-12 23:47:20.236263
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native

# Generated at 2022-06-12 23:47:30.966326
# Unit test for function to_bytes
def test_to_bytes():
    def b(obj='', encoding='utf-8', errors=None, nonstring='simplerepr'):
        return to_bytes(obj, encoding, errors, nonstring)

    assert b('hello world') == b'hello world'
    assert b(b'hello world') == b'hello world'
    assert b(u'hello world') == b'hello world'

    assert b(u'\u1234') == b'\xe1\x88\xb4'
    assert b(u'\u1234', encoding='latin-1') == b'\x34\x12'
    assert b(u'\u1234', encoding='ascii', errors='surrogate_then_replace') == b'?'
    assert b(None) == b'None'

    # regression for #16824

# Generated at 2022-06-12 23:47:39.476285
# Unit test for function to_native
def test_to_native():
    # pylint: disable=no-member, undefined-variable, invalid-name
    # Test bytes path
    assert(to_native(b'\xe4\xbd\xa0\xe5\xa5\xbd') == u'\u4f60\u597d')
    if PY3:
        # if we are on Python3, ensure that surrogateescape error handler
        # works as described

        # surrogateescape error handler makes bytes which are not valid
        # utf-8 into surrogates which can be decoded back into the original
        # bytes.
        assert(to_native(b'\xff\xfe\xfd') == u'\udcff\udcfd\udcfc')

# Generated at 2022-06-12 23:47:41.416989
# Unit test for function jsonify
def test_jsonify():
    pass
    # print(jsonify({"test": "\xe6\xb5\x8b\xe8\xaf\x95"}))



# Generated at 2022-06-12 23:47:48.648462
# Unit test for function to_native
def test_to_native():

    assert to_native(b'\xe8\x80\x81') == '老'
    assert to_native(b'\xe8\x80\x81', encoding='ascii', nonstring='passthru') == b'\xe8\x80\x81'
    assert to_native('\udcc3\udca9') == '\udcc3\udca9'
    assert to_native('\udcc3\udca9', errors='surrogate_then_replace') == '??'
    assert to_native(b'\xe8\x80\x81', errors='surrogate_or_replace', encoding='ascii') == '�'

# Generated at 2022-06-12 23:47:54.813882
# Unit test for function to_native
def test_to_native():
    assert to_native(u'\u2713') == '\u2713'  # unicode
    assert to_native('\xe2\x9c\x93') == '\u2713'  # utf-8 byte string
    assert to_native('\xe2\x9c\x93') == '\xe2\x9c\x93'  # utf-8 byte string



# Generated at 2022-06-12 23:48:04.651326
# Unit test for function to_bytes
def test_to_bytes():
    # Test encoding to one that doesn't support surrogates
    utf8=to_bytes('\udce4', 'utf-8')
    # Test encoding to one that does support surrogates
    latin1=to_bytes('\udce4', 'latin-1')
    # make sure that surrogate_then_replace works (we only reach this code
    # path when surrogateescape is present)
    assert to_bytes('\udce4', 'latin-1', 'surrogate_then_replace') == latin1
    # Assume latin1 is correct and check that surrogate_then_replace gives us
    # correct characters
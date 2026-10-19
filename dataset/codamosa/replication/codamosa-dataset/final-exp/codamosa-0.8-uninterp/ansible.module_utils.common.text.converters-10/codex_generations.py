

# Generated at 2022-06-12 23:38:23.361082
# Unit test for function to_bytes
def test_to_bytes():
    # quick start
    assert to_bytes('abc') == b'abc'
    # unicode text
    assert to_bytes(u'東京') == b'\xe6\x9d\xb1\xe4\xba\xac'
    # str text
    assert to_bytes('東京') == b'\xe6\x9d\xb1\xe4\xba\xac'
    # unicode surrogate pair
    assert to_bytes(u'\U0001f604') == b'\xf0\x9f\x98\x84'
    # utf8 str surrogate pair
    assert to_bytes("\xf0\x9f\x98\x84") == b'\xf0\x9f\x98\x84'
    # surrogateescape in a str surrogate pair
   

# Generated at 2022-06-12 23:38:29.578953
# Unit test for function to_bytes
def test_to_bytes():

    assert to_bytes('foo') == b'foo'
    assert to_bytes(u'foo') == b'foo'
    assert to_bytes(u'foo\u20ac') == b'foo\xe2\x82\xac'
    assert to_bytes(u'\u20ac') == b'\xe2\x82\xac'

    # Nonstrings:
    assert to_bytes('$') == b'$'
    assert to_bytes(u'$') == b'$'
    assert to_bytes(u'$\u20ac') == b'$\xe2\x82\xac'
    assert to_bytes('$\xe2\x82\xac') == b'$\xe2\x82\xac'
    assert to_bytes(5) == b'5'

# Generated at 2022-06-12 23:38:39.486536
# Unit test for function to_bytes
def test_to_bytes():
    """Test to_bytes function

    Need test cases for:

        - byte strings
        - text strings in ascii, utf-8, and latin-1
        - error handler: strict, replace, ignore, surrogateescape,
                                 surrogate_or_replace, surrogate_or_strict
        - nonstrings: simplerepr, empty, passthru, strict, Invalid input
           - simplerepr and empty should not recurse
        - errors in text and nonstring
    """
    # What error handlers to test against
    error_handlers = (None, 'strict', 'replace', 'ignore', 'surrogate_or_replace',
                      'surrogate_or_strict')

    # Common byte strings

# Generated at 2022-06-12 23:38:50.991451
# Unit test for function to_native
def test_to_native():

    def test_to_native_with_errors(case):
        for errors in (None,
                       'strict',
                       'replace',
                       'surrogate_or_strict',
                       'surrogate_or_replace',
                       'surrogate_then_replace'):
            if PY3 and errors == 'surrogate_or_strict':
                continue

            if PY3 and errors in ('surrogate_or_replace',
                                  'surrogate_then_replace'):
                # On py3 surrogateescape is always the right choice
                assert to_native(case, errors=errors) == to_native(case, errors='surrogateescape')
                assert to_native(case, errors=errors).__class__ is text_type
                continue

            result = to_native(case, errors=errors)


# Generated at 2022-06-12 23:38:56.161632
# Unit test for function jsonify
def test_jsonify():

    example = {
        "string": to_text("value"),
        "unicode": u"\u0430\u0431",
        "dict": {
            to_text("  string"): u"\u0430\u0431",
            "list": ["1", 1, {"string": "value"}]
        }
    }

    jsonify(example)


# Generated at 2022-06-12 23:39:00.638152
# Unit test for function to_native
def test_to_native():
    """Make sure that a native string is the appropriate type on both
    Python 2 and 3.
    """
    if PY3:
        assert to_native(b'foo') == u'foo'
        assert to_native(u'foo') == u'foo'
    else:
        assert to_native(b'foo') == 'foo'
        assert to_native(u'foo') == 'foo'



# Generated at 2022-06-12 23:39:10.849095
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six import u
    assert to_bytes(u('foo'), nonstring='passthru') == u('foo')
    assert to_bytes(u('foo')) == 'foo'
    assert to_bytes(u('fóo')) == 'fóo'
    assert to_bytes(u('fóo'), encoding='latin-1') == u('fóo').encode('latin-1')
    assert (to_bytes(u('fóo'), encoding='latin-1', errors='surrogate_or_strict') ==
            u('fóo').encode('latin-1', 'surrogateescape'))

# Generated at 2022-06-12 23:39:17.703324
# Unit test for function jsonify
def test_jsonify():
    test_data = dict(c1=set([1, 2, 3]), c2=set([4, 5, 6]), c3=datetime.datetime.now())
    json_data = jsonify(test_data)
    assert isinstance(json_data, (str, bytes))
    import json
    deserialized_data = json.loads(json_data)
    assert 'c1' in deserialized_data
    assert 'c2' in deserialized_data
    assert 'c3' in deserialized_data



# Generated at 2022-06-12 23:39:19.607761
# Unit test for function jsonify
def test_jsonify():
    assert(jsonify([1,2,3]) == '[1, 2, 3]')
    assert(jsonify({'k': 'value'}) == '{"k": "value"}')
    assert(jsonify('k') == '"k"')
    assert(jsonify(None) == 'null')



# Generated at 2022-06-12 23:39:26.303334
# Unit test for function to_native
def test_to_native():
    assert to_native(u'foo') == u'foo'
    assert to_native('foo') == u'foo'
    assert to_native(u'\xe9') == u'\xe9'
    assert to_native('\xe9') == u'\xe9'
    assert to_native(b'\xe9', errors='surrogate_or_replace') == u'\ufffd'
    assert to_native(b'\xe9') == u'\xe9'



# Generated at 2022-06-12 23:39:41.187635
# Unit test for function to_bytes

# Generated at 2022-06-12 23:39:52.749414
# Unit test for function jsonify
def test_jsonify():
    ansible_dict = dict(ansible=[u'\u2713', '@', u'\u2713'],
                        ansible_facts=[u'\u2713', '@', u'\u2713'],
                        changed=[u'\u2713', '@', u'\u2713'],
                        skipped=[u'\u2713', '@', u'\u2713'],
                        unreachable=[u'\u2713', '@', u'\u2713'],
                        failed=[u'\u2713', '@', u'\u2713'])
    ansible_json = jsonify(ansible_dict)
    assert '"msg": "\\u2713"' in ansible_json
    assert '"msg": "@"' in ansible_json

# Generated at 2022-06-12 23:40:03.316508
# Unit test for function jsonify
def test_jsonify():
    obj = {"key1":u"value\xe9"}
    result = jsonify(obj, ensure_ascii=False)
    assert isinstance(result, str)
    assert result == '{"key1": "value\\u00e9"}'

#: :py:func:`container_to_bytes`
#:     Recursively encode the contents of a container to bytes.
#:
#:     This function will recursively walk a container and run any strings
#:     it finds through :func:`~ansible.module_utils._text.to_bytes`.  Note
#:     that this will **only** affect strings.  Despite it's name it will
#:     not encode the container itself.
#:
#:     :arg container: The container to encode
#:     :kwarg encoding: The encoding to use for the

# Generated at 2022-06-12 23:40:15.840174
# Unit test for function to_native
def test_to_native():
    for x in (1, 3.14, datetime.datetime(2015, 1, 1, 1, 1, 1), True, False, None):
        assert str(x) == to_native(x), '%r != %r' % (str(x), to_native(x))
    assert '<no value>' == to_native(None)
    assert '1' == to_native(1)
    assert '3.14' == to_native(3.14)
    assert 'True' == to_native(True)
    assert 'False' == to_native(False)
    assert str(datetime.datetime(2015, 1, 1, 1, 1, 1)) == to_native(datetime.datetime(2015, 1, 1, 1, 1, 1))


# Generated at 2022-06-12 23:40:18.481470
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('foo', 'utf-8') == b'foo'
    assert to_bytes('foo', 'utf-8', nonstring='empty') == b''
    assert to_bytes('foo', 'utf-8', nonstring='strict') == b''

# Generated at 2022-06-12 23:40:27.546621
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils.six import b

    # Test empty string
    assert '' == to_bytes('')
    assert '' == to_bytes(b(''))
    assert '' == to_bytes('', nonstring='simplerepr')
    assert '' == to_bytes(b(''), nonstring='simplerepr')

    # Test simple string
    assert '123' == to_bytes('123')
    assert '123' == to_bytes(b('123'))

    # Test simple string with unicode
    assert '123\xe6' == to_bytes(u'123\xe6')
    assert '123\xe6' == to_bytes(u'123\xe6', errors='strict')
    # Test simple string with unicode that's not encodable as ascii

# Generated at 2022-06-12 23:40:38.894392
# Unit test for function to_bytes
def test_to_bytes():
    assert(to_bytes('\u1234') == '\xe1\x88\xb4')
    assert(to_bytes(u'\u1234') == '\xe1\x88\xb4')
    assert(to_bytes(b'\xe1\x88\xb4') == b'\xe1\x88\xb4')
    # Non-ascii text
    assert(to_bytes('\xe1\x88\xb4') == '\xe1\x88\xb4')
    assert(to_bytes('\xe1\x88\xb4', 'ascii') == b'\xe1\x88\xb4')
    # Non-ascii text with surrogate_escape

# Generated at 2022-06-12 23:40:48.109475
# Unit test for function jsonify
def test_jsonify():
    import datetime
    data_dict = {"my_dict": {"my_list": [1, 2, 3], "my_string": "foo"}}
    assert jsonify(data_dict) == b'{"my_dict": {"my_list": [1, 2, 3], "my_string": "foo"}}'
    assert jsonify(Set([1, 2, 3])) == b'[1, 2, 3]'

    fake_dt = datetime.datetime(2017, 1, 1, 0, 0, 0, 100)
    assert jsonify(fake_dt) == b'"2017-01-01T00:00:00.000100"'


# Generated at 2022-06-12 23:40:58.560031
# Unit test for function to_bytes

# Generated at 2022-06-12 23:41:03.468719
# Unit test for function to_native
def test_to_native():
    assert to_native(b'ascii') == 'ascii'
    assert to_native('utf-8') == 'utf-8'

    # This will only work on python3
    assert to_native(u'unicode') == 'unicode'

    # Will throw UnicodeDecodeError exception
    try:
        # noinspection PyStatementEffect
        to_native(b'\xff')
    except UnicodeDecodeError:
        pass


# Generated at 2022-06-12 23:41:15.836668
# Unit test for function jsonify
def test_jsonify():
    for obj in [
            1,
            'test',
            {'test': 'test'},
            [1, 2, 3],
            # Ensure that unencodable characters are correctly handled
            to_bytes(u'\u2620', encoding='utf-8', errors='surrogate_or_strict'),
            to_bytes(u'\udc80', encoding='utf-8', errors='surrogate_or_strict'),
    ]:
        try:
            new_obj = jsonify(obj)
        except UnicodeDecodeError:
            new_obj = obj
            pass
        assert json.loads(new_obj), "jsonify could not serialize %s" % repr(obj)




# Generated at 2022-06-12 23:41:21.855269
# Unit test for function jsonify
def test_jsonify():
    assert jsonify([u'\u4e94', {u'\u4e94': u'\u4e01'}]) == '[u"\u4e94", {"\u4e94": "\u4e01"}]'
    assert jsonify(['五','五']) == '["五", "五"]'



# Generated at 2022-06-12 23:41:30.637322
# Unit test for function to_native
def test_to_native():
    class Foo(object):
        def __repr__(self):
            return 'FOO'

    class Bar(object):
        def __str__(self):
            return 'bar'

    class Baz(object):
        def __str__(self):
            return b'baz'

    class Qux(object):
        def __str__(self):
            return u'\u1234'

    def test(value, expected, encoding='utf-8', errors=None):
        result = to_text(value, encoding, errors)
        assert result == expected and isinstance(result, text_type)
        result = to_bytes(value, encoding, errors)
        assert result == to_bytes(expected, encoding, errors) and isinstance(result, binary_type)
        result = to_native(value, encoding, errors)


# Generated at 2022-06-12 23:41:40.995622
# Unit test for function to_native
def test_to_native():
    """
    make sure that to_native returns bytestrings for py2 and strings for py3
    """
    to_native("foobar")
    to_native(b"foobar")
    to_native("foobar".encode("utf-8"))
    # Now make sure that we're returning bytestrings on py2 and strings on py3
    # On py3, this is always a string
    if PY3:
        assert to_native("foobar") == "foobar"
        assert to_native(b"foobar") == "foobar"
        assert to_native("foobar".encode("utf-8")) == "foobar"
    else:
        # On py2, this is always bytes
        assert to_native("foobar") == b"foobar"

# Generated at 2022-06-12 23:41:53.196874
# Unit test for function to_bytes
def test_to_bytes():
    from ansible.module_utils._text import to_bytes, to_text

    assert to_bytes(u'abc') == b'abc'
    assert to_bytes(b'abc') == b'abc'

    # Nonstring conversion
    assert to_bytes(u'abc', nonstring='empty') == b''
    assert to_bytes(u'abc', nonstring='passthru') == u'abc'
    assert to_bytes(u'abc', nonstring='simplerepr') == b"'abc'"
    assert to_bytes(u'abc', nonstring='strict') is None  # Strict makes it not return anything
    new_obj = object()
    assert to_bytes(new_obj, nonstring='passthru') is new_obj

    # Errors

# Generated at 2022-06-12 23:41:58.715338
# Unit test for function jsonify
def test_jsonify():
    data = {'a':1, 'b':[1,2,3], 'c':{'a':1, 'b':2}}
    data["d"] = Set(data)
    assert jsonify(data) == '{"a": 1, "b": [1, 2, 3], "c": {"a": 1, "b": 2}, "d": [1, 2, 3]}'



# Generated at 2022-06-12 23:42:01.686867
# Unit test for function jsonify
def test_jsonify():
    class Foo(object):
        def toJSON(self):
            return dict(foo='bar')
    assert jsonify(Foo()) == '{"foo": "bar"}'



# Generated at 2022-06-12 23:42:10.332733
# Unit test for function to_native
def test_to_native():
    for inp in (None, True, False, 1, 3.14159, u'Hello', b'World'):
        # If something is already a string, it should just be returned as-is
        assert to_native(inp) == inp
        # If something is not a string, it should be converted via str() as expected
        assert to_native(inp, nonstring='simplerepr') == str(inp)
        assert to_native(inp, nonstring='empty') == ""
        assert to_native(inp, nonstring='passthru') == inp
        assert to_native(inp, nonstring='strict') == str(inp)



# Generated at 2022-06-12 23:42:18.938595
# Unit test for function jsonify
def test_jsonify():
    assert jsonify(u"\u0444\u0438\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c") == '"\u0444\u0438\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c"'

# Generated at 2022-06-12 23:42:26.872788
# Unit test for function to_native
def test_to_native():
    import sys
    if sys.version_info[0] == 3:
        test_str = 'vløyfaføyfaføy'
        if sys.version_info[1] >= 6:
            # In py3.6 python provides a surrogateescape error handler
            # which allows us to test that to_native properly
            # uses surrogateescape when we ask it to.
            # This check will fail on earlier versions
            # (it will raise a UnicodeError when it tries to
            #  decode the value returned by to_native).
            assert to_native(test_str, errors='surrogate_then_replace') == test_str

        # Test the surrogate_or_strict handler
        # This is (currently) equivalent to surrogateescape

# Generated at 2022-06-12 23:42:40.291992
# Unit test for function jsonify
def test_jsonify():
    import datetime, json
    # byte string does not cause
    base_string = to_bytes("foo")
    data = {"base_string": base_string}

    # unicode string
    unicode_string = to_text("foo")
    data["unicode_string"] = unicode_string

    # non string objects
    data["int_obj"] = 1
    data["float_obj"] = 1.5
    data["list_obj"] = ["f", "o", "o"]
    data["dict_obj"] = {"f": to_text("foo")}

    # datetime object
    data["datetime_obj"] = datetime.datetime.utcnow()

    # set object
    data["set_obj"] = set(["f", "o", "o"])

    # bytes in lists or dicts


# Generated at 2022-06-12 23:42:45.163979
# Unit test for function jsonify
def test_jsonify():
    test1 = {'test1': 'test1', 'test2': 'test2'}
    test2 = {'test1': u'test1', 'test2': 'test2'}
    test3 = {'test1': u'test1', 'test2': u'test2'}
    test4 = {'test1': 'test1', 'test2': u'test2'}
    for test in [test1, test2, test3, test4]:
        expected = u'{"test1": "test1", "test2": "test2"}'
        result = jsonify(test)
        assert result == expected, result


# Generated at 2022-06-12 23:42:54.830736
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes('abc') == b'abc', "Trivial check that to_bytes works"

    assert to_bytes('abc', nonstring='empty') == b'', "b'' returned when nonstring is empty"
    def sideeffect():
        sideeffect.call = True
    sideeffect.call = False
    assert to_bytes('abc', nonstring=sideeffect) == b'', "b'' returned when nonstring is empty"
    assert not sideeffect.call, "nonstring parameter was not called when a string was passed"
    assert to_bytes(5, nonstring='empty') == b'', "b'' returned when nonstring is empty and str() raises an exception"
    assert to_bytes(5, nonstring='passthru') == 5, "5 returned when nonstring is passthru"

# Generated at 2022-06-12 23:42:57.659389
# Unit test for function jsonify
def test_jsonify():
    test_data = {'key': 'value', u'unicode_key': u'unicode_value'}
    assert jsonify(test_data) == '{"key": "value", "unicode_key": "unicode_value"}'



# Generated at 2022-06-12 23:43:05.057179
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert to_native(u'\u0080') == b'\xc2\x80'
    assert to_native(u'\u0080', encoding='latin-1') == b'\x80'
    assert to_native(u'\u0080', nonstring='passthru') == u'\u0080'
    assert to_native(u'\u0080', nonstring='simplerepr') == '\u0080'



# Generated at 2022-06-12 23:43:13.702553
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u"ünicode", errors='surrogate_or_replace') == b'\xfcnicode'
    assert to_bytes(u"ünicode", errors='surrogate_then_replace') == b'nicode'
    assert to_bytes(u"ünicode", errors='surrogate_or_strict') == b'\xfcnicode'
    assert to_bytes(u'\udce4\udcec\udce7\udce8', errors='surrogate_or_replace') == b'\xed\xb3\xa4\xed\xb3\xac\xed\xb3\xa7\xed\xb3\xa8'

# Generated at 2022-06-12 23:43:22.215703
# Unit test for function to_native
def test_to_native():
    # TODO: Consider testing exec of to_text and to_bytes
    # TODO: Consider testing with surrogateescape if available
    # TODO: Consider testing with surrogate_then_replace if available
    # TODO: Consider testing with invalid encoding

    # to_native(obj, encoding=None)

    # If no encoding is given, explicitly encode text strings as utf-8
    # bytes.
    assert to_native(u'Hello') == b'Hello'
    # Bytes are passed through unchanged
    assert to_native(b'Hello') == b'Hello'

    # Note: we don't test non-string objects since we just call str(obj)
    # on them and then check for the str type

    # to_native(obj, encoding='text')
    # If we're in text mode then we expect all strings to be text strings
   

# Generated at 2022-06-12 23:43:26.871882
# Unit test for function jsonify
def test_jsonify():
    doc = {u'doc': {u'field': 'val'}}
    assert doc == json.loads(jsonify(doc))
    doc = {u'doc': {u'field': '你好'}}
    assert doc == json.loads(jsonify(doc))



# Generated at 2022-06-12 23:43:36.998258
# Unit test for function to_native
def test_to_native():
    def _test_encoding(obj, encoding='utf-8'):
        assert to_native(obj, encoding) == to_text(obj, encoding, nonstring='passthru')

    # Test bytes don't blow up
    _test_encoding(b"simple bytes")

    # Test that a utf8 unicode string becomes a native string
    _test_encoding("H\u00e9l\u00e8ne")

    # Test that a latin1 unicode string becomes a native string
    _test_encoding("H\xe9l\xe8ne", 'latin-1')


# Generated at 2022-06-12 23:43:48.236922
# Unit test for function to_native

# Generated at 2022-06-12 23:44:08.107550
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    assert isinstance(to_native(u'test'), str)
    assert isinstance(to_native(b'test'), str)
    assert isinstance(to_native(u'test', nonstring='passthru'), unicode)
    assert to_native(u'test', nonstring='passthru') == u'test'
    assert isinstance(to_native(b'test', nonstring='passthru'), bytes)
    assert to_native(b'test', nonstring='passthru') == b'test'
    assert to_native(b'test') == u'test'
    assert to_native(b'123') == u'123'
    assert to_native(u'test') == u'test'

# Generated at 2022-06-12 23:44:18.450500
# Unit test for function to_bytes
def test_to_bytes():
    assert to_bytes(u'\xfcbr\xfcger') == b'\xfcbr\xfcger'
    assert to_bytes('\xfcbr\xfcger') == b'\xfcbr\xfcger'
    assert to_bytes(u'\xfcbr\xfcger', errors='strict') == b'\xc3\xbcbr\xc3\xbcger'
    assert to_bytes(u'\xfcbr\xfcger', errors='replace') == b'?'
    # Surrogateescape isn't available in Python2.  This tests the default behavior
    # of no surrogateescape
    assert to_bytes(u'\xfcbr\xfcger', errors='surrogate_then_replace') == b'?'

# Generated at 2022-06-12 23:44:24.234014
# Unit test for function jsonify
def test_jsonify():
  data = {'k0': text_type('a', 'utf-8')}
  ret_value = jsonify(data)
  assert ret_value == '{"k0": "a"}'
  data = {'k0': text_type('a', 'latin-1')}
  ret_value = jsonify(data)
  assert ret_value == '{"k0": "a"}'



# Generated at 2022-06-12 23:44:30.675912
# Unit test for function to_native
def test_to_native():
    # Add in support for surrogate escape
    import codecs
    codecs.register_error('surrogateescape', codecs.surrogateescape_error)
    # Test various input types
    # bytes
    assert to_native(b'bytes') == b'bytes'
    # text
    assert to_native(u'text') == u'text'
    # nonstring
    assert to_native(42) == '42'

    # b'bytes' with surrogateescape
    assert to_native(b'\xf4\x8f\xbf\xbf') == u'\U0010ffff'
    assert to_native(b'a\xf4\x8f\xbf\xbfz') == u'a\U0010ffffz'

# Generated at 2022-06-12 23:44:36.003603
# Unit test for function to_native
def test_to_native():
    from ansible.module_utils._text import to_native
    unicode_string = to_bytes('ñ')
    assert isinstance(unicode_string, bytes)
    assert to_native(unicode_string) == 'ñ'
    # for the non-UTF-8 case, we use surrogate escapes
    assert to_native(to_bytes(u'\u00e1', encoding='iso8859-1'), errors='surrogate_or_strict') == '\xE1'
    # for the invalid UTF-8 case, we use surrogate escapes
    assert to_native(to_bytes(u'\xFF', encoding='utf-8'), errors='surrogate_or_strict') == '\xFF'
    # the default error handler is 'surrogate_then_replace'

# Generated at 2022-06-12 23:44:39.736530
# Unit test for function jsonify
def test_jsonify():
    b = {b'a': 1, b'b': b'bytes', b'c': b'caf\xc3\xa9'}
    assert jsonify(b, sort_keys=True) == '{"a": 1, "b": "bytes", "c": "caf\\u00e9"}'
    assert jsonify(u'unicode', sort_keys=True) == '"unicode"'
    assert jsonify({"a": [1, 2, 3]}, sort_keys=True) == '{"a": [1, 2, 3]}'


# Backwards compatibility
# Not used in Ansible
# No longer required in python3 as dicts and sets are always ordered.

# Generated at 2022-06-12 23:44:42.645678
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({'a':u'\xe9'}) == '{"a": "\\u00e9"}'



# Generated at 2022-06-12 23:44:50.307444
# Unit test for function jsonify
def test_jsonify():
    import json
    from ansible.module_utils._text import to_native
    from ansible.module_utils._text import to_text
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_unicode
    from ansible.module_utils._text import to_native

    #test for the to_unicode function
    if not PY3:
        assert to_unicode(to_bytes(u'foo')) == u'foo'
    assert to_unicode(u'foo') == u'foo'

    try:
        #test for the to_unicode function
        assert to_unicode(b'foo') == u'foo'
    except UnicodeDecodeError:
        raise AssertionError("Could not apply to_unicode on a binary an get text")

# Generated at 2022-06-12 23:45:00.208526
# Unit test for function to_native
def test_to_native():
    assert to_native(u'foo') == 'foo'
    assert to_native('foo') == 'foo'
    value = b'\xef'
    if PY3:
        assert to_native(value) == '�'
        assert to_native(value, errors='ignore') == ''
    else:
        assert to_native(value) == '\xef'
        assert to_native(value, errors='ignore') == '\xef'


if PY3:
    # In python3 we don't need special encoding
    to_unicode = text_type
    to_bytes = bytes


# Generated at 2022-06-12 23:45:04.114518
# Unit test for function jsonify
def test_jsonify():
    assert jsonify('test') == '"test"'
    assert jsonify(['test']) == '["test"]'
    assert jsonify({'test': [1], 'test2': 'test3'}) == '{"test": [1], "test2": "test3"}'


# Generated at 2022-06-12 23:45:32.413361
# Unit test for function to_bytes
def test_to_bytes():
    # Basic tests to ensure we encode text to utf-8 when passed a unicode
    # string
    import sys
    import os
    print("1")
    assert to_bytes(u'abc') == b'abc'
    print("2")
    assert to_bytes(u'\xe9', 'utf-8') == b'\xc3\xa9'
    print("3")
    # Ensure that we don't transform byte strings
    assert to_bytes(b'abc') == b'abc'
    assert to_bytes(b'\xe9', 'utf-8') == b'\xe9'
    print("4")
    # Ensure that we can pass in a text_type and get the expected result with
    # a non-ascii encoding
    assert to_bytes(u'\xe9', 'latin-1')

# Generated at 2022-06-12 23:45:41.533235
# Unit test for function to_native
def test_to_native():
    utf8_value = '\xe2\x9c\x93'  # This is a UTF-8 tick symbol
    unicode_value = to_text(utf8_value)  # Convert to unicode
    converted_value = to_native(unicode_value)
    assert type(converted_value) is unicode  # We're using six, so this should never fail
    assert converted_value == unicode_value  # The values should be the same
    oneline_value = to_bytes(utf8_value)
    converted_value = to_native(oneline_value)
    assert type(converted_value) is unicode  # We're using six, so this should never fail
    assert converted_value == unicode_value  # The values should be the same
    # If we send it something that is already unicode,

# Generated at 2022-06-12 23:45:52.698567
# Unit test for function to_native
def test_to_native():
    assert isinstance(to_native(True), bool)                # bool
    assert isinstance(to_native(False), bool)               # bool
    assert isinstance(to_native(2147483647), int)           # Max int32
    assert isinstance(to_native(-2147483647), int)          # Min int32
    assert isinstance(to_native(2147483648), long)          # Min int64, will be int on 32-bit arch
    assert isinstance(to_native(1.2), float)                # float
    assert isinstance(to_native("hello world"), basestring) # string
    assert isinstance(to_native([]), list)                  # list
    assert isinstance(to_native({}), dict)                  # dict
    assert isinstance(to_native(set()), set)               

# Generated at 2022-06-12 23:46:04.135944
# Unit test for function jsonify
def test_jsonify():
    data = {
        u'alpha': u'\xce\xb1',
        u'beta': u'\xce\xb2',
        u'gamma': u'\xce\xb3',
    }
    data_ascii = jsonify(data, encoding='ascii')
    assert isinstance(data_ascii, str)
    assert data_ascii == '{"alpha": "\\u03b1", "beta": "\\u03b2", "gamma": "\\u03b3"}'
    # Invalid unicode encoding
    invalid_data = {
        u'alpha': '\xce\xb1',
        u'beta': u'\xce\xb2',
        u'gamma': u'\xce\xb3'
    }

# Generated at 2022-06-12 23:46:11.831511
# Unit test for function to_native
def test_to_native():
    # If 'byte, then UnicodeDecodeError would be raised
    assert isinstance(to_native("foo"), text_type)
    assert isinstance(to_native("foo".encode("ascii")), text_type)
    # If 'bytes, then UnicodeDecodeError would be raised
    assert isinstance(to_native("foo".encode("utf-16")), text_type)
    assert isinstance(to_native("foo".encode("utf-32")), text_type)
# test_to_native()



# Generated at 2022-06-12 23:46:18.517193
# Unit test for function to_bytes
def test_to_bytes():
    # Give a text string
    assert to_bytes(u'hello') == b'hello'
    assert to_bytes(u'hello', nonstring='passthru') == u'hello'
    assert to_bytes(u'hello', nonstring='empty') == b''
    try:
        to_bytes(u'hello', nonstring='strict')
        assert False
    except TypeError:
        pass

    # Give a byte string
    assert to_bytes(b'hello') == b'hello'
    assert to_bytes(b'hello', nonstring='passthru') == b'hello'
    assert to_bytes(b'hello', nonstring='empty') == b''
    try:
        to_bytes(b'hello', nonstring='strict')
        assert False
    except TypeError:
        pass

    # Give

# Generated at 2022-06-12 23:46:28.908983
# Unit test for function jsonify
def test_jsonify():
    dict1 = {'a': u'a', 'b': u'b'}
    dict2 = {u'a': u'a', b'b': u'b'}
    dict3 = {u'a': u'a', 'b': b'b'}
    dict4 = {b'a': u'a', b'b': u'b'}
    dict5 = {b'a': u'a', u'b': b'b'}
    dict6 = {u'a': b'a', u'b': b'b'}
    dict7 = {b'a': b'a', u'b': b'b'}
    dict8 = {u'a': b'a', b'b': b'b'}

# Generated at 2022-06-12 23:46:31.252432
# Unit test for function to_native
def test_to_native():
    '''make sure to_native works as expected'''

    assert to_native(u'foo') == u'foo'
    assert to_native('foo') == u'foo'
    assert to_native(1) == '1'


# Generated at 2022-06-12 23:46:42.220712
# Unit test for function to_native
def test_to_native():
    # Try to make sure that the function is a noop for valid inputs
    for value in [u'', '', b'', to_text(''), to_bytes('')]:
        assert to_native(value) == value

    # Input is something that implements __str__ or __unicode__
    class _TextLike(object):
        def __init__(self, string_value, raise_on_unicode=False):
            self.string_value = string_value
            self.raise_on_unicode = raise_on_unicode

        def __str__(self):
            return self.string_value

        def __unicode__(self):
            if self.raise_on_unicode:
                raise UnicodeError
            else:
                return self.string_value


# Generated at 2022-06-12 23:46:53.695242
# Unit test for function jsonify
def test_jsonify():
    assert jsonify({"key1": "val1", "key2": "val2"}) == '{"key1": "val1", "key2": "val2"}'
    assert jsonify({"key1": u"val1", "key2": u"val2"}) == '{"key1": "val1", "key2": "val2"}'
    assert jsonify({"key1": b"val1", "key2": b"val2"}) == '{"key1": "val1", "key2": "val2"}'
    assert jsonify([b"val1", b"val2"]) == '["val1", "val2"]'
    assert jsonify([u"val1", u"val2"]) == '["val1", "val2"]'

# Generated at 2022-06-12 23:47:45.697698
# Unit test for function to_bytes
def test_to_bytes():
    # to_bytes should be a drop in replacement for the to_bytes function in utils.py in Ansible-2.3
    # We're going to use a forced UTF8 locale to test this.
    # XXX: We don't actually know if this is actually a UTF8 locale
    from ansible.module_utils.six import u
    for u in (u'\x00', u'\u0100', u"\u8fff"):
        if len(u) == 1:
            # Technically we're testing surrogate pairs here but that's good enough
            assert to_bytes(u, 'utf-8', 'surrogateescape') == u.encode('utf-8', 'surrogateescape'), repr(u)

# Generated at 2022-06-12 23:47:49.584782
# Unit test for function jsonify
def test_jsonify():
    data = {u'bytes': u'\x80abc'}
    try:
        json.dumps(data)
    except UnicodeDecodeError:
        pass
    else:
        assert False, 'Expected failure: No decoding should work with the data given'
    result = jsonify(data)
    assert result == '{"bytes": "\\u0080abc"}', 'Expected {"bytes": "\\\\u0080abc"}'



# Generated at 2022-06-12 23:47:58.227352
# Unit test for function jsonify
def test_jsonify():
    # test for ascii
    ascii_string = '{\"name\": \"foo\", \"time\": \"10:00\"}'
    assert (jsonify(eval(ascii_string)) == ascii_string)

    # test for non-ascii
    nonascii_string = '{\"name\": \"bar\", \"time\": \"09:30\"}'
    assert (jsonify(eval(nonascii_string)) == nonascii_string)



# Generated at 2022-06-12 23:48:06.792976
# Unit test for function to_bytes
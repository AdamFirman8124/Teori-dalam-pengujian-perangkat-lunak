

# Generated at 2022-06-13 16:46:46.574886
# Unit test for function wrap_var
def test_wrap_var():

    # Wrap a simple string
    s = '{"foo": "bar"}'
    assert isinstance(wrap_var(s), AnsibleUnsafeText)

    # Wrap a string in a dict
    d = dict(a=s)
    expected = AnsibleUnsafeText('{"foo": "bar"}')
    assert wrap_var(d) == dict(a=expected)

    # Wrap a string in a list
    l = [s]
    assert wrap_var(l) == [expected]

    # Wrap a string in a tuple
    t = (s,)
    assert wrap_var(t) == (expected,)

    # Wrap a string in a set
    t = {s}
    assert wrap_var(t) == {expected}

    # Wrap a dict in a dict
    s = dict(foo=dict(bar=1))


# Generated at 2022-06-13 16:46:57.666719
# Unit test for function wrap_var
def test_wrap_var():
    # Ripped from test_template_module.py
    tests = [
        (
            '{{ with_sequence }}',
            dict(with_sequence=['1', '2', '3']),
            [('1', '2', '3')],
        ),
        (
            '{{ with_list }}',
            dict(with_list=['1', '2', '3']),
            [('1', '2', '3')],
        ),
        (
            '{{ with_set }}',
            dict(with_set=set(['1', '2', '3'])),
            [('1', '2', '3')],
        ),
    ]
    for template, data, expected in tests:
        wrapped_template = wrap_var(template)
        wrapped_data = wrap_var(data)

# Generated at 2022-06-13 16:47:08.196859
# Unit test for function wrap_var
def test_wrap_var():

    # test wrap_var is idempotent
    assert wrap_var(wrap_var(None)) is None
    assert isinstance(wrap_var(wrap_var(dict())), dict)
    assert isinstance(wrap_var(wrap_var(set())), set)
    assert isinstance(wrap_var(wrap_var(tuple())), tuple)
    assert isinstance(wrap_var(wrap_var([])), list)
    assert isinstance(wrap_var(wrap_var(b"unsafe")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(wrap_var(u"unsafe")), AnsibleUnsafeText)

    # test string types are safe
    assert wrap_var(None) is None
    assert wrap_var('') == u''
    assert wrap_var(b'') == b''


# Generated at 2022-06-13 16:47:19.461112
# Unit test for function wrap_var
def test_wrap_var():
    v = {'key1':'value1', 'key2': 'value2', 'key3': {'key4': 'value4'}}
    v = wrap_var(v)
    assert isinstance(v, dict)
    for i in v.values():
        assert isinstance(i, AnsibleUnsafeText)

    v = [3, 4, 5, {'key': 'value'}]
    v = wrap_var(v)
    assert isinstance(v, list)
    for i in v:
        assert isinstance(i, AnsibleUnsafeText)

    v = 'test_string'
    v = wrap_var(v)
    assert isinstance(v, AnsibleUnsafeText)

    v = b'test_bytes'
    v = wrap_var(v)

# Generated at 2022-06-13 16:47:25.757513
# Unit test for function wrap_var

# Generated at 2022-06-13 16:47:35.444607
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import string_types, binary_type, text_type
    from ansible.module_utils._text import to_bytes, to_text
    # simple string
    assert(isinstance(wrap_var('simple string'), AnsibleUnsafeText))
    assert(isinstance(wrap_var(to_bytes('simple string')), AnsibleUnsafeBytes))
    # list of strings
    assert(isinstance(wrap_var(['a', 'b']), tuple))
    assert(isinstance(wrap_var(('a', 'b')), tuple))
    # dict of strings
    assert(isinstance(wrap_var({'key': 'value'}), dict))
    # recursive string types
    assert(isinstance(wrap_var({'key': ['a', 'b']}), dict))

# Generated at 2022-06-13 16:47:41.765985
# Unit test for function wrap_var
def test_wrap_var():
    assert getattr(wrap_var('safe'), '__UNSAFE__', False) is False
    assert getattr(wrap_var(None), '__UNSAFE__', False) is False
    assert type(wrap_var(None)) is type(None)
    assert getattr(wrap_var(b'unsafe'), '__UNSAFE__', False) is True
    assert type(wrap_var(b'unsafe')) is AnsibleUnsafeBytes
    assert getattr(wrap_var(u'unsafe'), '__UNSAFE__', False) is True
    assert type(wrap_var(u'unsafe')) is AnsibleUnsafeText
    assert getattr(wrap_var(NativeJinjaText()), '__UNSAFE__', False) is True
    assert type(wrap_var(NativeJinjaText()))

# Generated at 2022-06-13 16:47:50.081696
# Unit test for function wrap_var
def test_wrap_var():
    # Basic usage
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)

    # Ensure classes of input and output are the same for non-strings
    assert type(wrap_var({u'foo': u'bar'})) == dict
    assert type(wrap_var([u'foo', u'bar'])) == list
    assert type(wrap_var((u'foo', u'bar'))) == tuple
    assert type(wrap_var(set([u'foo', u'bar']))) == set

    # Ensure AnsibleUnsafeBytes is returned for binary data
    assert type(wrap_var(u'foo'.encode('utf-8'))) is AnsibleUnsafeBytes

    # Ensure AnsibleUnsafeString is returned for string data
    assert type(wrap_var(u'foo')) is AnsibleUnsafeText



# Generated at 2022-06-13 16:47:51.698216
# Unit test for function wrap_var
def test_wrap_var():
    import doctest
    result = doctest.testmod(verbose=False)
    assert result.failed == 0, result

# Generated at 2022-06-13 16:47:59.568129
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(123) == 123
    assert wrap_var('abc') == u'abc'
    assert wrap_var(['abc', 'def']) == [u'abc', u'def']
    assert wrap_var(['abc', 123]) == [u'abc', 123]
    assert wrap_var({'a': 123}) == {'a': 123}
    assert wrap_var({'a': '123'}) == {'a': u'123'}


# Generated at 2022-06-13 16:46:47.350402
# Unit test for function wrap_var
def test_wrap_var():
    # TODO:
    # - Add tests for the new wrap_var, which should be able to wrap
    #   any type, but with the added benefit that it will not wrap it if
    #   it is already unsafe.
    test_dict = {1: "1", 2: "2", 3: "3"}
    test_list = ["a", "b", "c"]
    test_set = {"a", "b", "c"}
    test_string = "test_string"

    # Check dictionary
    assert isinstance(wrap_var(test_dict), dict)
    assert isinstance(wrap_var(test_dict)[1], string_types)
    assert isinstance(wrap_var(test_dict)[2], string_types)
    assert isinstance(wrap_var(test_dict)[3], string_types)

    #

# Generated at 2022-06-13 16:46:54.362717
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    string_types_tuple = (str,)

    assert issubclass(str, string_types) is True
    assert issubclass(str, string_types_tuple) is True

    assert issubclass(string_types, string_types_tuple) is False
    assert issubclass(string_types, tuple) is False
    assert issubclass(string_types, str) is True
    assert issubclass(string_types, AnsibleUnsafeBytes) is True
    assert issubclass(string_types, AnsibleUnsafeText) is False

    assert issubclass(string_types_tuple, string_types) is False
    assert issubclass(string_types_tuple, tuple) is True
    assert issubclass(string_types_tuple, str) is True

# Generated at 2022-06-13 16:46:59.831087
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import u, b
    from ansible.module_utils._text import to_text

    assert wrap_var(u('foo')) == AnsibleUnsafeText(u('foo'))
    assert wrap_var(b('foo')) == AnsibleUnsafeBytes(b('foo'))
    assert wrap_var([u('foo'), u('bar')]) == [AnsibleUnsafeText(u('foo')), AnsibleUnsafeText(u('bar'))]
    assert wrap_var(dict(a=u('foo'), b=u('bar'))) == dict(a=AnsibleUnsafeText(u('foo')), b=AnsibleUnsafeText(u('bar')))

# Generated at 2022-06-13 16:47:08.415164
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert isinstance(wrap_var(b"foo"), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("foo"), AnsibleUnsafeText)

    # don't wrap if it is already AnsibleUnsafe class
    assert isinstance(wrap_var(AnsibleUnsafeBytes("foo")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(AnsibleUnsafeText("foo")), AnsibleUnsafeText)

    assert isinstance(wrap_var(NativeJinjaText("foo")), NativeJinjaUnsafeText)

    assert isinstance(wrap_var({}), dict)
    assert isinstance(wrap_var(set()), set)
    assert isinstance(wrap_var(()), tuple)
    assert isinstance(wrap_var([]), list)

# Generated at 2022-06-13 16:47:19.775042
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    # Testing the following conditions
    # should return U
    assert UnsafeProxy(u'd') == u'd'
    assert UnsafeProxy('d') == u'd'
    assert UnsafeProxy(u's') == u's'
    assert UnsafeProxy('s') == u's'
    assert UnsafeProxy(u'd').__class__ == AnsibleUnsafeText
    assert UnsafeProxy('d').__class__ == AnsibleUnsafeText
    assert UnsafeProxy(u's').__class__ == AnsibleUnsafeText
    assert UnsafeProxy('s').__class__ == AnsibleUnsafeText

    # should return U from bytes
    assert UnsafeProxy(b'd').__class__ == AnsibleUnsafeText
    assert UnsafeProxy(b's').__class__ == AnsibleUnsafeText

    # should return U from bytes
    assert Unsafe

# Generated at 2022-06-13 16:47:29.841926
# Unit test for function wrap_var
def test_wrap_var():
    # Test wrap_var against various python objects
    assert type(wrap_var(['a', 'list'])) == list
    assert type(wrap_var(('a', 'tuple'))) == tuple
    assert type(wrap_var({'a': 'dict'})) == dict
    assert type(wrap_var(set(['a', 'set']))) == set
    assert type(wrap_var('a_string')) == AnsibleUnsafeText
    assert type(wrap_var(b'a_byte_string')) == AnsibleUnsafeBytes
    assert type(wrap_var(AnsibleUnsafeText('AnsibleUnsafeText'))) == AnsibleUnsafeText
    assert type(wrap_var(AnsibleUnsafeBytes(b'AnsibleUnsafeBytes'))) == AnsibleUnsafeBytes

    # Test that wrap_

# Generated at 2022-06-13 16:47:38.257561
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    assert isinstance(UnsafeProxy(None), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(''), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(u''), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(b''), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(AnsibleUnsafeText(u'')), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(AnsibleUnsafeBytes(b'')), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(AnsibleUnsafeText(u'a')), AnsibleUnsafe)
    assert isinstance(UnsafeProxy(AnsibleUnsafeBytes(b'a')), AnsibleUnsafe)
    assert isinstance(UnsafeProxy([u'']), AnsibleUnsafe)

# Generated at 2022-06-13 16:47:46.523217
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    assert isinstance(UnsafeProxy(None), type(None))
    assert isinstance(UnsafeProxy(''), type(AnsibleUnsafeText()))

    assert isinstance(UnsafeProxy(b'Unsafe'), type(AnsibleUnsafeBytes()))
    assert isinstance(UnsafeProxy(u'Unsafe'), type(AnsibleUnsafeText()))

    # Check that unsafe stays unsafe.
    assert isinstance(UnsafeProxy(AnsibleUnsafeBytes()), type(AnsibleUnsafeBytes()))
    assert isinstance(UnsafeProxy(AnsibleUnsafeText()), type(AnsibleUnsafeText()))

# Generated at 2022-06-13 16:47:56.288141
# Unit test for function wrap_var
def test_wrap_var():
    import json
    from ansible.module_utils._text import to_native

    objects = [None, False, True, '', '1', 1, 1.0, [], (), {}]
    wrapped_objects = [None, False, True, AnsibleUnsafeText(''), AnsibleUnsafeText('1'), 1, 1.0, [], (), {}]
    safe_dict = {"a": "A", "b": "B"}
    unsafe_dict = {AnsibleUnsafeText("a"): AnsibleUnsafeText("A"), AnsibleUnsafeText("b"): AnsibleUnsafeText("B")}
    objects.append(safe_dict)
    wrapped_objects.append(unsafe_dict)


# Generated at 2022-06-13 16:48:04.735995
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    import ansible.module_utils.urls
    from ansible.module_utils.six.moves.urllib.parse import urlparse as urlparse
    from ansible.module_utils.six.moves.urllib.parse import urljoin as urljoin
    import ansible.module_utils.six.moves.urllib.error
    import ansible.module_utils.six.moves.urllib.request
    from ansible.module_utils.six import PY3

    # The ansible.module_utils.six module has exposed six.moves
    # to the global namespace in PY3.  As we don't want to
    # replace the built-in urlparse, urljoin and
    # URLError modules, we need to use __import__ in order
    # to avoid namespace clashes.
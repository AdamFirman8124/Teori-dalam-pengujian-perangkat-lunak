

# Generated at 2022-06-13 16:46:47.007827
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var("foo") == "foo"
    assert wrap_var(1) == 1
    assert wrap_var(u"foo") == u"foo"
    assert wrap_var({u"foo": u"bar"}) == {u"foo": u"bar"}
    assert wrap_var([u"foo", u"bar"]) == [u"foo", u"bar"]
    assert wrap_var([u"foo", 1]) == [u"foo", 1]
    assert wrap_var([u"foo"]) == [u"foo"]
    assert wrap_var((u"foo", u"bar")) == (u"foo", u"bar")
    assert wrap_var((u"foo", 1)) == (u"foo", 1)
    assert wrap_var((u"foo",)) == (u"foo",)

    assert wrap

# Generated at 2022-06-13 16:46:57.784686
# Unit test for function wrap_var
def test_wrap_var():
    """Unit testing for function wrap_var."""
    assert wrap_var('hello') == 'hello'
    assert wrap_var('hello') == 'hello'
    assert wrap_var(u'hello') == u'hello'

    # dict
    assert wrap_var({"key": "value"}) == {"key": "value"}
    assert wrap_var({"key": 123}) == {"key": 123}

    # list
    assert wrap_var(['a', 'b']) == ['a', 'b']
    assert wrap_var(['a', 123]) == ['a', 123]

    # tuple
    assert wrap_var(('a', 'b')) == ('a', 'b')
    assert wrap_var(('a', 123)) == ('a', 123)

    # set

# Generated at 2022-06-13 16:47:08.199185
# Unit test for function wrap_var
def test_wrap_var():
    # Test non-strings
    assert wrap_var(True) is True
    assert wrap_var(1) == 1
    assert wrap_var({}) == {}
    assert wrap_var([]) == []
    assert wrap_var([1, 2, 3]) == [1, 2, 3]
    assert wrap_var((1, 2, 3)) == (1, 2, 3)
    assert wrap_var({'a': 'b', 'c': 'd', 'e': ['f', 'g']}) == {'a': wrap_var('b'), 'c': wrap_var('d'), 'e': wrap_var(['f', 'g'])}

# Generated at 2022-06-13 16:47:19.522284
# Unit test for function wrap_var
def test_wrap_var():

    # dict
    vdict = dict(a=1, b=2)
    x = wrap_var(vdict)
    assert(isinstance(x, UnsafeProxy))
    assert(isinstance(x, dict))
    assert(x['a'] == 1)
    assert(x['b'] == 2)

    # list
    vlist = [1, 2, 3]
    x = wrap_var(vlist)
    assert(isinstance(x, UnsafeProxy))
    assert(isinstance(x, list))
    assert(x[0] == 1)
    assert(x[1] == 2)
    assert(x[2] == 3)

    # str
    vstr = "abcd"
    x = wrap_var(vstr)
    assert(isinstance(x, UnsafeProxy))

# Generated at 2022-06-13 16:47:25.779296
# Unit test for function wrap_var
def test_wrap_var():
    import copy
    import inspect
    import sys
    import types
    import unittest

    o = object()
    u = None
    s = 'hello'
    b = b'hello'

    #  python 2.6 does not support a literal frozenset, so must create it from a set
    if sys.version_info < (2, 7):
        i = eval("set([o, u, s, b])")
    else:
        i = {o, u, s, b}
    t = (o, u, s, b)
    l = [o, u, s, b]
    d = {'o': o, 'u': u, 's': s, 'b': b}
    f = [o, u, s, b]
    f.append(f)

# Generated at 2022-06-13 16:47:33.528130
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import BytesIO, StringIO

    assert wrap_var(None) is None
    assert wrap_var(AnsibleUnsafeBytes(b'some string')) is AnsibleUnsafeBytes(b'some string')
    assert wrap_var(AnsibleUnsafeText(u'some string')) is AnsibleUnsafeText(u'some string')

    # strings
    assert isinstance(wrap_var(b'some string'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'some string'), AnsibleUnsafeText)

    # sequences

# Generated at 2022-06-13 16:47:37.974247
# Unit test for function wrap_var
def test_wrap_var():

    # test None
    assert wrap_var(None) is None

    # test bool
    assert wrap_var(True)

    # test int
    assert wrap_var(-1) == -1
    assert wrap_var(0) == 0
    assert wrap_var(1) == 1

    # test float
    assert wrap_var(-1.0) == -1.0
    assert wrap_var(0.0) == 0.0
    assert wrap_var(1.0) == 1.0

    # test str
    assert isinstance(wrap_var(''), AnsibleUnsafeText)
    assert wrap_var('test') == 'test'

    # test bytes
    assert isinstance(wrap_var(b''), AnsibleUnsafeBytes)
    assert wrap_var(b'bytes') == b'bytes'

    # test

# Generated at 2022-06-13 16:47:47.899964
# Unit test for function wrap_var
def test_wrap_var():
    import datetime
    import math

    assert wrap_var(None) is None
    assert wrap_var(True) is True
    assert wrap_var(False) is False
    assert wrap_var(1) == 1
    assert wrap_var(0) == 0
    assert wrap_var(-1) == -1
    assert wrap_var(1.1) == 1.1
    assert wrap_var(-1.1) == -1.1
    assert wrap_var(1.0/0.0) == math.inf
    assert wrap_var(-1.0/0.0) == -math.inf
    assert wrap_var(math.acos(2)) == math.acos(2)
    assert wrap_var(b'') == b''
    assert wrap_var(b'foo') == b'foo'

# Generated at 2022-06-13 16:47:57.168282
# Unit test for function wrap_var
def test_wrap_var():
    import types
    assert not isinstance(wrap_var('hello'), AnsibleUnsafe)
    assert isinstance(wrap_var(b'hello'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var('hello'), AnsibleUnsafeText)
    assert isinstance(wrap_var(NativeJinjaText('hello')), NativeJinjaUnsafeText)
    assert isinstance(wrap_var({'hello': 'world'}), dict)
    assert isinstance(wrap_var({'hello': wrap_var('world')}), dict)
    assert isinstance(wrap_var({b'hello': 'world'}), dict)
    assert isinstance(wrap_var({'hello': b'world'}), dict)
    assert isinstance(wrap_var(('hello', b'world')), types.TupleType)

# Generated at 2022-06-13 16:48:07.084348
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import is_sequence
    assert wrap_var(None) is None
    assert wrap_var('abcd') == AnsibleUnsafeText('abcd')
    assert wrap_var(u'abcd') == AnsibleUnsafeText(u'abcd')
    assert isinstance(wrap_var(AnsibleUnsafeText(u'abcd')), AnsibleUnsafeText)
    assert wrap_var(b'abcd') == AnsibleUnsafeBytes(b'abcd')
    assert wrap_var(('a', 'b')) == _wrap_sequence(('a', 'b'))
    assert wrap_var(['a', 'b']) == _wrap_sequence(['a', 'b'])
    assert wrap_var(('a', 'b', dict(c='d')))
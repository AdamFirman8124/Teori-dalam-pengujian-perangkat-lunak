

# Generated at 2022-06-13 16:46:45.816745
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import PY3

    # test with unsafe object
    message = "safe"
    message_unsafe = AnsibleUnsafeText(message)
    wrapped_message = wrap_var(message_unsafe)
    assert wrapped_message == message_unsafe

    # test with None object
    wrapped_message = wrap_var(None)
    assert wrapped_message == None

    # test with string_types(text_type, binary_type) object
    message = "safe"
    if PY3:
        wrapped

# Generated at 2022-06-13 16:46:53.159143
# Unit test for function wrap_var
def test_wrap_var():
    import pytest

    # Test None
    assert wrap_var(None) is None
    # Test existing type
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    class Unsafe(AnsibleUnsafe): pass
    assert isinstance(wrap_var(Unsafe()), Unsafe)
    # Test some string types
    assert wrap_var(b'foo') == b'foo'
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert wrap_var(u'foo') == u'foo'
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert wrap_var(u'\N{SNOWMAN}') == u'\N{SNOWMAN}'

# Generated at 2022-06-13 16:47:00.996293
# Unit test for function wrap_var
def test_wrap_var():
    from nose.plugins.skip import SkipTest
    from ansible.utils.display import Display

    try:
        from ansible.module_utils.six import u
        from ansible.module_utils.six.moves import builtins
    except ImportError:
        raise SkipTest("test_wrap_var: Unable to import ansible modules")

    def customfunction(args):
        return args

    display = Display()
    display.deprecated = lambda x, y, z: None  # we do not care about deprecations here

    # Test regular types
    assert wrap_var(customfunction) == customfunction
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0
    assert wrap_var(True) is True
    assert wrap_var(False) is False

# Generated at 2022-06-13 16:47:04.674611
# Unit test for function wrap_var
def test_wrap_var():
    # Following should not throw any exception
    wrap_var("test")
    wrap_var(123)
    wrap_var({"k1":"test", "k2":"test"})
    wrap_var(["test", "test"])

test_wrap_var()

# Generated at 2022-06-13 16:47:11.197040
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(""), AnsibleUnsafeText)
    assert isinstance(wrap_var(to_bytes("")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("test"), AnsibleUnsafeText)
    assert isinstance(wrap_var(to_bytes("test")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("test".encode("utf-8")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("test".encode("utf-8").decode("utf-8")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("test".encode("utf-8").decode("utf-8")), AnsibleUnsafeText)

# Generated at 2022-06-13 16:47:20.371129
# Unit test for function wrap_var
def test_wrap_var():

    assert wrap_var(u'foo') == AnsibleUnsafeText(u'foo')
    assert wrap_var(b'foo') == AnsibleUnsafeBytes(b'foo')
    assert wrap_var(1) == 1
    assert wrap_var(set([1])) == {1}
    assert wrap_var(list([1])) == [1]
    assert wrap_var(tuple([1])) == (1,)
    assert wrap_var(dict({'foo': 'bar'})) == {'foo': 'bar'}
    assert wrap_var(dict(foo='bar')) == {'foo': 'bar'}
    assert wrap_var(NativeJinjaText(u'foo')) == NativeJinjaUnsafeText(u'foo')

# Generated at 2022-06-13 16:47:28.065620
# Unit test for function wrap_var
def test_wrap_var():
    """Test cases for function wrap_var"""
    # case 1
    input = 'ansible'
    result = wrap_var(input)
    assert isinstance(result, AnsibleUnsafeText)

    # case 2
    input = b'ansible'
    result = wrap_var(input)
    assert isinstance(result, AnsibleUnsafeBytes)

    # case 3
    input = {'a': 'b'}
    result = wrap_var(input)
    assert isinstance(result, dict)
    assert isinstance(result['a'], AnsibleUnsafeText)

# Generated at 2022-06-13 16:47:36.947490
# Unit test for function wrap_var
def test_wrap_var():
    seq1 = (1, 2, 3, 4)
    seq2 = ['hello', 'world']
    seq3 = range(10)
    seq4 = (1.1, 2.2, 3.3, 4.4)

    seq1_wrapped = _wrap_sequence(seq1)
    seq2_wrapped = _wrap_sequence(seq2)
    seq3_wrapped = _wrap_sequence(seq3)
    seq4_wrapped = _wrap_sequence(seq4)

    test_map = {1: '2', 2: '4'}

    string_test = 'hello world'

    assert(type(seq1_wrapped) == tuple)
    assert(type(seq2_wrapped) == list)
    assert(type(seq3_wrapped) == range)

# Generated at 2022-06-13 16:47:47.129801
# Unit test for function wrap_var
def test_wrap_var():
    # Ensure binary_type is wrapped
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)

    # Ensure text_type is wrapped
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)

    # Ensure that a dictionary of binary_types is wrapped
    assert isinstance(wrap_var({b'foo': b'bar'}), Mapping)
    assert isinstance(wrap_var({u'foo': u'bar'}).keys()[0], AnsibleUnsafeText)
    assert isinstance(wrap_var({u'foo': u'bar'}).values()[0], AnsibleUnsafeText)

    # Ensure that a dictionary of text_types is wrapped
    assert isinstance(wrap_var({b'foo': b'bar'}), Mapping)

# Generated at 2022-06-13 16:47:56.728155
# Unit test for function wrap_var
def test_wrap_var():
    assert type(wrap_var('foo')) == AnsibleUnsafeText
    assert type(wrap_var(b'bar')) == AnsibleUnsafeBytes
    assert type(wrap_var(AnsibleUnsafeText('foo'))) == AnsibleUnsafeText
    assert type(wrap_var(AnsibleUnsafeBytes(b'bar'))) == AnsibleUnsafeBytes

    assert type(wrap_var(('foo',))) == tuple
    assert type(wrap_var(['bar'])) == list
    assert type(wrap_var(dict(foo='foo'))) == dict
    assert type(wrap_var({'bar': 'baz'})) == dict
    assert type(wrap_var(set(['a', 'b', 'c']))) == set
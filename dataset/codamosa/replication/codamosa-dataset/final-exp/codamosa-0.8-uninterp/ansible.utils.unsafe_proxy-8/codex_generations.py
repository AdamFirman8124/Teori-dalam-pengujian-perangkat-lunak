

# Generated at 2022-06-13 16:46:47.232586
# Unit test for function wrap_var
def test_wrap_var():
    # Test Mapping
    mapping = {'a': '2', 'b': 3}
    wrapped_mapping = wrap_var(mapping)
    assert isinstance(wrapped_mapping['a'], AnsibleUnsafe)
    assert isinstance(wrapped_mapping['b'], AnsibleUnsafe)

    # Test Sequence
    sequence = [1, 2, 3, 4]
    wrapped_sequence = wrap_var(sequence)
    assert isinstance(wrapped_sequence[0], AnsibleUnsafe)
    assert isinstance(wrapped_sequence[1], AnsibleUnsafe)
    assert isinstance(wrapped_sequence[2], AnsibleUnsafe)
    assert isinstance(wrapped_sequence[3], AnsibleUnsafe)

    # Test Set

# Generated at 2022-06-13 16:46:57.784306
# Unit test for function wrap_var
def test_wrap_var():
    def _test_expect_type(obj_to_wrap, expected_type):
        # Wrap the given object, assert the result is an instance of the
        # expected type, then ensure that double-wrapping the same object
        # yields the same result.
        wrapped = wrap_var(obj_to_wrap)
        assert isinstance(wrapped, expected_type)
        assert wrap_var(wrapped) is wrapped

    _test_expect_type(None, type(None))
    _test_expect_type(True, type(True))
    _test_expect_type(False, type(False))
    _test_expect_type(1234567890, type(1234567890))
    _test_expect_type(3.14159, type(3.14159))
    _test_expect_

# Generated at 2022-06-13 16:47:08.197472
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common._collections_compat import OrderedDict
    import pytest


# Generated at 2022-06-13 16:47:19.521803
# Unit test for function wrap_var
def test_wrap_var():

    output_foo = wrap_var('foo')
    assert isinstance(output_foo, AnsibleUnsafeText)

    output_bar = wrap_var(b'bar')
    assert isinstance(output_bar, AnsibleUnsafeBytes)

    output_dict = wrap_var({1: 'a', b'2': to_bytes('b')})
    value = output_dict['1']
    assert isinstance(value, AnsibleUnsafeText)
    value = output_dict['2']
    assert isinstance(value, AnsibleUnsafeBytes)

    output_list = wrap_var([1, b'2', 3])
    value = output_list[0]
    assert isinstance(value, int)
    value = output_list[1]
    assert isinstance(value, AnsibleUnsafeBytes)
    value = output_

# Generated at 2022-06-13 16:47:25.800807
# Unit test for function wrap_var
def test_wrap_var():
    """ Tests for function wrap_var
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.loader import AnsibleLoader

    class MyPlay(object):
        def __init__(self, context):
            self.context = context

    play_context = PlayContext()
    myplay = MyPlay(play_context)

    # create a string
    mystr = "a"
    s = wrap_var(mystr)
    assert not isinstance(s, PlayContext)
    assert isinstance(s, AnsibleUnsafeText)

    # create a dictionary
    mydict = dict()
    mydict["mykey"] = "myvalue"
    d = wrap_var(mydict)
    assert not isinstance(d["mykey"], PlayContext)
    assert isinstance

# Generated at 2022-06-13 16:47:33.551143
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(AnsibleUnsafeText('unsafe text')) == AnsibleUnsafeText('unsafe text')
    assert wrap_var('unsafe text') == AnsibleUnsafeText(u'unsafe text')
    assert wrap_var(b'unsafe bytes') == AnsibleUnsafeBytes(b'unsafe bytes')
    assert wrap_var(1) == 1
    assert wrap_var(['unsafe text', AnsibleUnsafeText('unsafe text')]) == ['unsafe text', AnsibleUnsafeText('unsafe text')]
    assert wrap_var(('unsafe text', AnsibleUnsafeText('unsafe text'))) == ('unsafe text', AnsibleUnsafeText('unsafe text'))

# Generated at 2022-06-13 16:47:45.055927
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(dict(a=1, b=2)) == dict(a=1, b=2)
    assert wrap_var(dict(a=1, b=dict(c=3))) == dict(a=1, b=dict(c=3))
    assert wrap_var(dict(a=1, b=[2, 3, 4])) == dict(a=1, b=[2, 3, 4])
    assert wrap_var(dict(a=1, b=set([2, 3, 4]))) == dict(a=1, b=set([2, 3, 4]))
    assert wrap_var(tuple([2, 3, 4])) == tuple([2, 3, 4])
    assert wrap_var(set([2, 3, 4])) == set([2, 3, 4])
    assert wrap_var

# Generated at 2022-06-13 16:47:54.658798
# Unit test for function wrap_var
def test_wrap_var():
    v1 = {b'a': b'b', b'c': b'e'}
    assert( isinstance(v1, dict) )
    assert( not isinstance(v1, AnsibleUnsafe) )
    v2 = wrap_var(v1)
    assert( isinstance(v1, dict) )
    assert( isinstance(v2, dict) )
    assert( not isinstance(v2, AnsibleUnsafe) )
    # check contents
    for k in v1.keys():
        assert( isinstance(k, AnsibleUnsafeBytes) )
        assert( isinstance(v1[k], AnsibleUnsafeBytes) )
        assert( isinstance(v2[k], AnsibleUnsafeBytes) )

# Generated at 2022-06-13 16:48:03.654161
# Unit test for function wrap_var
def test_wrap_var():
    import pytest

    def test_none():
        assert wrap_var(None) is None

    def test_str():
        assert wrap_var("jenkins") is "jenkins"

    def test_int():
        assert wrap_var(42) == 42

    def test_unicode():
        assert wrap_var(u"bob") is "bob"

    def test_list():
        assert wrap_var([1, 2]) == [1, 2]

    def test_dict():
        assert wrap_var({"a": 1}) == {"a": 1}

    def test_dict_recurse():
        assert wrap_var({"a": ["b"]}) == {"a": ["b"]}


# Generated at 2022-06-13 16:48:09.410838
# Unit test for function wrap_var
def test_wrap_var():

    from ansible.module_utils.common.collections import _is_unsafe
    from ansible.module_utils.common.collections import _is_unsafe_bytes
    from ansible.module_utils.common.collections import _is_unsafe_text

    assert _is_unsafe_bytes(wrap_var(b"test"))
    assert _is_unsafe_text(wrap_var(u"test"))
    assert _is_unsafe_bytes(wrap_var(b"test".decode().encode()))
    assert _is_unsafe_text(wrap_var(u"test".encode().decode()))
    assert not _is_unsafe(wrap_var('test'))
    assert not _is_unsafe(wrap_var(u"test"))

# Generated at 2022-06-13 16:48:17.147551
# Unit test for function wrap_var
def test_wrap_var():

    import json
    import pytest

    assert wrap_var(None) is None
    assert isinstance(wrap_var('str'), AnsibleUnsafeText)

    # Test that we can wrap a class
    class A:
        def __init__(self, val):
            self.val = val

        def __eq__(self, other):
            return (
                isinstance(other, type(self)) and
                self.val == other.val
            )

    assert wrap_var(A(1)) == A(1)

    # Test that wraps with AnsibleUnsafe for dicts, lists, tuples, and sets
    assert isinstance(wrap_var({}), dict)
    assert isinstance(wrap_var([1, 2, 3]), list)

# Generated at 2022-06-13 16:48:21.501139
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var({'foo': b'bar'}), AnsibleUnsafe)
    assert isinstance(wrap_var({'foo': u'bar'}), AnsibleUnsafe)
    assert isinstance(wrap_var({'foo': None}), AnsibleUnsafe)
    assert isinstance(wrap_var({u'foo': None}), AnsibleUnsafe)
    assert isinstance(wrap_var({b'foo': None}), AnsibleUnsafe)
    assert isinstance(wrap_var([b'foo']), AnsibleUnsafe)
    assert isinstance(wrap_var([u'foo']), AnsibleUnsafe)
    assert isinstance(wrap_var([None]), AnsibleUnsafe)
    assert isinstance(wrap_var((b'foo',)), AnsibleUnsafe)

# Generated at 2022-06-13 16:48:32.168457
# Unit test for function wrap_var
def test_wrap_var():
    assert not isinstance(wrap_var('foo'), string_types), "wrap_var did not wrap string"
    assert not isinstance(wrap_var(u'foo'), string_types), "wrap_var did not wrap unicode string"
    assert not isinstance(wrap_var({'foo': 'bar'}), Mapping), "wrap_var did not wrap dict"
    assert not isinstance(wrap_var(['foo']), list), "wrap_var did not wrap list"
    assert not isinstance(wrap_var((1, 2)), tuple), "wrap_var did not wrap tuple"
    assert isinstance(wrap_var(u'foo'), text_type), "wrap_var wrapped string to wrong type"
    assert isinstance(wrap_var(b'foo'), binary_type), "wrap_var wrapped bytes to wrong type"

# Generated at 2022-06-13 16:48:42.493498
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(None), type(None))

    assert isinstance(wrap_var(""), type(""))
    assert isinstance(wrap_var(""), AnsibleUnsafeText)
    assert isinstance(wrap_var(""), text_type)

    assert isinstance(wrap_var(b""), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(b""), binary_type)

    assert isinstance(wrap_var(""), AnsibleUnsafeText)

    assert isinstance(wrap_var({}), type({}))
    assert isinstance(wrap_var({}), Mapping)

    assert isinstance(wrap_var([]), type([]))
    assert isinstance(wrap_var([]), list)

    assert isinstance(wrap_var(()), type(()))

# Generated at 2022-06-13 16:48:53.020152
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.module_utils.common.collections as col
    import types

    class Foo:
        pass

    # Test basic functionality
    assert wrap_var(None) is None
    assert wrap_var(5) == 5
    assert isinstance(wrap_var(5), int)
    assert wrap_var(True) is True
    assert isinstance(wrap_var(True), bool)
    assert wrap_var(b"foo") == b'foo'
    assert isinstance(wrap_var(b"foo"), AnsibleUnsafeBytes)
    assert wrap_var(u"foo") == u'foo'
    assert isinstance(wrap_var(u"foo"), AnsibleUnsafeText)

    # Test sequences
    assert wrap_var(()) == ()
    assert isinstance(wrap_var(()), tuple)
    assert wrap

# Generated at 2022-06-13 16:49:00.880184
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var('a'), AnsibleUnsafeText)
    assert isinstance(wrap_var(1), int)
    assert isinstance(wrap_var(1.0), float)
    assert isinstance(wrap_var(b'a'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var([1, 2, 3]), list)
    assert isinstance(wrap_var((1, 2, 3)), tuple)
    assert isinstance(wrap_var({'a': 1}), dict)
    assert isinstance(wrap_var(range(1, 10)), range)
    assert isinstance(wrap_var(set([1, 2, 3])), set)
    assert isinstance(wrap_var(AnsibleUnsafeBytes(b'a')), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:49:09.228574
# Unit test for function wrap_var
def test_wrap_var():
    # Make sure wrap_var returns a unicode string
    assert isinstance(wrap_var("test_string"), text_type)

    # Make sure wrap_var returns a dict
    assert isinstance(wrap_var({"test": "dict"}), dict)

    # Make sure wrap_var returns a list
    assert isinstance(wrap_var(["test", "list"]), list)

    # Make sure wrap_var returns a tuple
    assert isinstance(wrap_var(("test", "tuple")), tuple)

# Generated at 2022-06-13 16:49:18.470611
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var(42) == 42
    assert isinstance(wrap_var(42.0), float)
    assert wrap_var(True) is True
    assert isinstance(wrap_var(b'data'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'data'), AnsibleUnsafeText)
    assert isinstance(wrap_var(NativeJinjaText(u'data')), NativeJinjaUnsafeText)
    test_dict = dict(
        foo=7,
        bar=u'test',
        baz=dict(
            fizz=u'test2',
            buzz=u'test3',
        ),
    )
    assert wrap_var(test_dict)['bar'] == u'test'

# Generated at 2022-06-13 16:49:25.010285
# Unit test for function wrap_var
def test_wrap_var():
    '''Wrap some basic vars with AnsibleUnsafe wrapper'''
    import copy
    import ansible.module_utils
    import ansible.module_utils.common.collections

    # define a dict to use for testing
    base_dict = dict(one='1', two=dict(three=3), four=['a', 'b'])

    # define a new dict based on base_dict but wrap the vars
    # use copy.deepcopy to ensure dicts are truly new
    wrapped_dict = copy.deepcopy(base_dict)

    wrapped_dict['one'] = wrap_var(wrapped_dict['one'])
    wrapped_dict['two'] = wrap_var(wrapped_dict['two'])
    wrapped_dict['four'] = wrap_var(wrapped_dict['four'])

    # define a test

# Generated at 2022-06-13 16:49:33.573447
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import is_sequence

    assert wrap_var(None) is None
    assert wrap_var('foo') == AnsibleUnsafeText(u'foo')
    assert wrap_var(b'foo') == AnsibleUnsafeBytes(b'foo')
    assert wrap_var(u'foo') == AnsibleUnsafeText(u'foo')
    assert wrap_var(AnsibleUnsafeText(u'foo')) == AnsibleUnsafeText(u'foo')
    assert wrap_var(AnsibleUnsafeBytes(b'foo')) == AnsibleUnsafeBytes(b'foo')

    assert is_sequence(wrap_var((1, 2)))


# Generated at 2022-06-13 16:46:46.606637
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    Display().deprecated(
        'UnsafeProxy is being deprecated. Use wrap_var or AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
        version='2.13', collection_name='ansible.builtin'
    )
    # Test wrapping an empty list
    assert wrap_var([]) == []
    # Test wrapping a list of unsafe text
    assert wrap_var([b"val1", b"val2"]) == [AnsibleUnsafeText("val1"), AnsibleUnsafeText("val2")]
    # Test wrapping a list of unsafe text and a list of unsafe text

# Generated at 2022-06-13 16:46:57.702511
# Unit test for function wrap_var
def test_wrap_var():
    import unittest
    class WrapVarUnitTests(unittest.TestCase):
        def test_wrap_var_safe_dict(self):
            data = {'a': 'a', 'b': {'b': 'b'}, 'c': [{'c': 'c'}, ['d', 'e'], 'f', {'g': {'h': 'i'}}]}
            self.assertEqual(wrap_var(data), data)

        def test_wrap_var_unsafe_dict(self):
            data = {'a': 'a', 'b': {'b': b'b'}, 'c': [{'c': 'c'}, ['d', 'e'], 'f', {'g': {'h': b'i'}}]}

# Generated at 2022-06-13 16:47:08.175512
# Unit test for function wrap_var
def test_wrap_var():
    import pytest
    from ansible.utils.unsafe_proxy import UnsafeText, UnsafeBytes, UnsafeProxy

    assert UnsafeProxy('safe') == 'safe'

    assert isinstance(UnsafeProxy(b'unsafe'), UnsafeBytes)
    assert UnsafeProxy(b'unsafe') == b'unsafe'

    assert isinstance(UnsafeProxy(u'unsafe'), UnsafeText)
    assert UnsafeProxy(u'unsafe') == u'unsafe'

    assert UnsafeProxy(['safe', b'safe', u'safe']) == ['safe', b'safe', u'safe']
    assert UnsafeProxy([b'unsafe', u'unsafe']) == [b'unsafe', u'unsafe']

# Generated at 2022-06-13 16:47:13.544425
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.utils.unsafe_proxy

    x = {u'a': 'string', u'b': [1, 2, 3], u'c': {1: 'one', 2: 'two'}, u'd': set(range(4))}
    x_u = ansible.utils.unsafe_proxy.wrap_var(x)

    assert isinstance(x_u, dict)
    assert isinstance(x_u[u'a'], ansible.utils.unsafe_proxy.AnsibleUnsafeText)
    assert isinstance(x_u[u'b'], list)
    assert isinstance(x_u[u'c'], dict)
    assert isinstance(x_u[u'd'], set)

# Generated at 2022-06-13 16:47:22.178851
# Unit test for function wrap_var
def test_wrap_var():
    # Check a dict
    d = {u'a': u'b', u'c': u'd', u'e': u'f'}
    dd = wrap_var(d)
    assert isinstance(dd, dict)
    assert isinstance(dd[u'a'], AnsibleUnsafeText)
    assert isinstance(dd[u'a'], text_type)

    # Check list
    l = [u'a', u'b', u'c', u'd']
    ll = wrap_var(l)
    assert isinstance(ll, list)
    assert isinstance(ll[0], AnsibleUnsafeText)
    assert isinstance(ll[0], text_type)

    # Check bytes
    b = to_bytes('abc123')
    bb = wrap_var(b)

# Generated at 2022-06-13 16:47:31.250175
# Unit test for function wrap_var
def test_wrap_var():

    class MyList(object):
        def __init__(self, l):
            self.l = l

        def __iter__(self):
            return iter(self.l)

        def __len__(self):
            return len(self.l)

    class mystr(str):
        pass

    assert isinstance(wrap_var(1), AnsibleUnsafe)

    assert isinstance(wrap_var('string'), AnsibleUnsafe)
    assert isinstance(wrap_var(mystr('string')), AnsibleUnsafe)

    assert isinstance(wrap_var(['string']), AnsibleUnsafe)
    assert isinstance(wrap_var(MyList(['string'])), AnsibleUnsafe)

    assert isinstance(wrap_var({'string': 'string'}), AnsibleUnsafe)

# Generated at 2022-06-13 16:47:35.939882
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var("string") == "string"
    assert wrap_var(None) is None

    assert wrap_var(dict(a='string', b=2)) == dict(a='string', b=2)
    assert wrap_var(dict(a='string', b=dict(c='string', d=2))) == dict(a='string', b=dict(c='string', d=2))
    assert wrap_var(dict(a='string', b=set([2, 'string']))) == dict(a='string', b=set([2, 'string']))
    assert wrap_var(dict(a='string', b=set([2, dict(c=2)]))) == dict(a='string', b=set([2, dict(c=2)]))

# Generated at 2022-06-13 16:47:42.093538
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var('test') == AnsibleUnsafeText('test')
    assert wrap_var(b'bytes') == AnsibleUnsafeBytes(b'bytes')
    assert wrap_var(b'bytes'.decode('utf-8')) == AnsibleUnsafeText('bytes')
    assert wrap_var(['a', 'b', 'c']) == _wrap_sequence(['a', 'b', 'c'])
    assert wrap_var({'a': 'b'}) == _wrap_dict({'a': 'b'})
    assert wrap_var(['a', 'b', ['c', 'd'], {'e': 'f'}]) == _wrap_sequence(['a', 'b', ['c', 'd'], {'e': 'f'}])

# Generated at 2022-06-13 16:47:50.171719
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(u'foo') == u'foo'
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert wrap_var(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert isinstance(wrap_var(['a', 'b', 'c'])[0], AnsibleUnsafeText)
    assert wrap_var(['a', 'b', {'c': 'd'}]) == ['a', 'b', {'c': 'd'}]
    assert isinstance(wrap_var(['a', 'b', {'c': 'd'}])[2]['c'], AnsibleUnsafeText)

# Generated at 2022-06-13 16:47:53.371781
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import namedtuple

    def validate_unsafe(x):
        assert isinstance(x, AnsibleUnsafe)
        assert isinstanc

# Generated at 2022-06-13 16:48:03.687092
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import text_type, binary_type

    assert wrap_var(text_type(u'hello')) == text_type(u'hello')
    assert isinstance(wrap_var(text_type(u'hello')), text_type)
    assert isinstance(wrap_var(text_type(u'hello')), AnsibleUnsafeText)

    bval = binary_type(b'\x80\x81\x82\x83')
    assert wrap_var(bval) == bval
    assert isinstance(wrap_var(bval), AnsibleUnsafeBytes)

    yaml_str = text_type(u'[{a: b}, c, d]')
    yaml_bytes = binary_type(b'[{a: b}, c, d]')

    parsed_

# Generated at 2022-06-13 16:48:09.030553
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var("abc") == "abc"
    assert wrap_var("abc") != b"abc"
    assert wrap_var("abc") != u"abc"
    assert wrap_var("abc") != AnsibleUnsafeText("abc")
    assert wrap_var("abc") != AnsibleUnsafeBytes("abc")
    assert wrap_var(b"abc") == b"abc"
    assert wrap_var(b"abc") != "abc"
    assert wrap_var(b"abc") != u"abc"
    assert wrap_var(b"abc") != AnsibleUnsafeText("abc")
    assert wrap_var(b"abc") != AnsibleUnsafeBytes("abc")
    assert wrap_var(u"abc") == u"abc"
    assert wrap_var(u"abc") != "abc"
    assert wrap_

# Generated at 2022-06-13 16:48:16.209034
# Unit test for function wrap_var
def test_wrap_var():
    class A(object):
        pass
    a = A()
    assert wrap_var(a) is a
    assert wrap_var(None) is None
    assert wrap_var(True) is True
    assert wrap_var(False) is False
    assert wrap_var(1) == 1
    assert wrap_var({}) == {}
    assert wrap_var([]) == []
    assert wrap_var(()) == ()
    assert wrap_var(set()) == set()
    assert wrap_var('foo') == 'foo'
    assert wrap_var(b'foo') == b'foo'
    assert wrap_var(u'foo') == u'foo'
    assert wrap_var({'foo': 'bar'}) == {'foo': 'bar'}

# Generated at 2022-06-13 16:48:26.491571
# Unit test for function wrap_var
def test_wrap_var():
    import json
    import os
    import sys
    import tempfile
    from ansible.module_utils.six import PY3, StringIO
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils.six import text_type

    # Tests for wrap_var on string types
    assert isinstance(wrap_var('foo'), text_type)
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(AnsibleUnsafeText(u'foo')), AnsibleUnsafeText)
    assert isinstance(wrap_var(AnsibleUnsafeBytes(b'foo')), AnsibleUnsafeBytes)

    # Tests for wrap_var on

# Generated at 2022-06-13 16:48:35.314045
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.utils.unsafe_proxy
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var(None), type(None))

    # Checks for native types
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var(True), type(True))
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var(0), type(0))
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var(0.0), type(0.0))

    # Checks for sequences
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var((0, 1)), tuple)
    assert isinstance(ansible.utils.unsafe_proxy.wrap_var([0, 1]), list)

# Generated at 2022-06-13 16:48:45.933588
# Unit test for function wrap_var
def test_wrap_var():
    class FakeClass:
        pass
    fake_class = FakeClass()
    fake_class.__UNSAFE__ = True

    # Test None
    assert wrap_var(None) is None

    # Test wrapped variable
    assert isinstance(wrap_var(fake_class), FakeClass)

    # Test mapping
    assert isinstance(wrap_var({'1': '2'}), dict)
    assert isinstance(wrap_var({'1': '2'})['1'], AnsibleUnsafeText)

    # Test sequence
    assert isinstance(wrap_var(['1', '2']), list)
    assert isinstance(wrap_var(('1', '2'))[0], AnsibleUnsafeText)

    # Test set
    assert isinstance(wrap_var({'1'}), set)

# Generated at 2022-06-13 16:48:56.149717
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence

    assert wrap_var("test") == "test"
    assert isinstance(wrap_var("test"), AnsibleUnsafeText)

    assert wrap_var(b"test") == b"test"
    assert isinstance(wrap_var(b"test"), AnsibleUnsafeBytes)

    assert wrap_var({1: "test"}) == {1: "test"}
    assert isinstance(wrap_var({1: "test"}), MutableMapping)
    assert isinstance(wrap_var({1: "test"})[1], AnsibleUnsafeText)

    assert wrap_var(("test", "test2")) == ("test", "test2")

# Generated at 2022-06-13 16:49:05.589908
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'bar'), AnsibleUnsafeText)
    assert isinstance(wrap_var(1), AnsibleUnsafe)
    assert isinstance(wrap_var(1.1), AnsibleUnsafe)
    assert isinstance(wrap_var(b'a'), AnsibleUnsafe)
    assert isinstance(wrap_var(u'a'), AnsibleUnsafe)

    assert wrap_var(b'foo') == wrap_var(b'foo')
    assert wrap_var(u'foo') == wrap_var(u'foo')
    assert wrap_var(1) == wrap_var(1)

# Generated at 2022-06-13 16:49:13.465888
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils._text import to_bytes, to_text

    # string test
    assert isinstance(wrap_var('test'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'test'), AnsibleUnsafeText)
    assert isinstance(wrap_var(to_bytes('test')), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(to_text('test')), AnsibleUnsafeText)

    # sequence test
    assert wrap_var([1, 2, 3]) == [1, 2, 3]
    assert [isinstance(e, AnsibleUnsafeText) for e in wrap_var([u'1', u'2', u'3'])] == [True, True, True]

# Generated at 2022-06-13 16:49:21.741495
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(['foo']), list)
    assert isinstance(wrap_var(('foo', 'bar')), tuple)
    assert isinstance(wrap_var({'foo': 'bar'}), dict)
    assert isinstance(wrap_var({'foo', 'bar'}), set)
    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var('foo'.encode('utf-8')), AnsibleUnsafeBytes)
    assert isinstance(wrap_var('foo'.join('abcd')), AnsibleUnsafeText)


# Generated at 2022-06-13 16:49:31.575038
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var(False) is False
    assert wrap_var(True) is True
    assert wrap_var(0) == 0
    assert wrap_var(1) == 1
    assert wrap_var(0.0) == 0.0
    assert wrap_var(1.0) == 1.0

    assert wrap_var('') == AnsibleUnsafeText('')
    assert wrap_var('test') == AnsibleUnsafeText('test')
    assert wrap_var(b'') == AnsibleUnsafeBytes(b'')
    assert wrap_var(b'test') == AnsibleUnsafeBytes(b'test')

    assert wrap_var({}) == {}

# Generated at 2022-06-13 16:49:39.262890
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils import six

    # Test primitive and builtin types:
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0
    assert wrap_var(True) is True
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0
    assert wrap_var(True) is True

    # Test that we do not convert existing ansible unsafe objects
    assert AnsibleUnsafeBytes is type(wrap_var(AnsibleUnsafeBytes(b'foo')))
    assert AnsibleUnsafeText is type(wrap_var(AnsibleUnsafeText('foo')))
    assert NativeJinjaUnsafeText is type(wrap_var(NativeJinjaUnsafeText('foo')))

    # Test str type
    assert Ansible

# Generated at 2022-06-13 16:49:50.585298
# Unit test for function wrap_var
def test_wrap_var():
    import os
    import tempfile
    import shutil
    import sys
    # Save the current stdout so that we can restore it later
    stdout_save = sys.stdout

    # In case the current working directory has a space in it, we need to
    # create a temporary directory that can be used for testing this function.
    # If a space is not present, we'll just use the current working directory
    if " " in os.getcwd():
        test_dir = tempfile.mkdtemp()
    else:
        test_dir = os.getcwd()

    # Change the current working directory to the temporary directory
    os.chdir(test_dir)

    # Create a temporary file and write some data to it
    fd, temp_file = tempfile.mkstemp()

# Generated at 2022-06-13 16:50:02.288750
# Unit test for function wrap_var
def test_wrap_var():
    import jinja2

    import sys
    if sys.version_info.major > 2:
        BINARY_TYPE = bytes
        TEXT_TYPE = str
    else:
        BINARY_TYPE = str
        TEXT_TYPE = unicode

    def to_text(value):
        return TEXT_TYPE(value, errors="surrogate_or_strict")


# Generated at 2022-06-13 16:50:08.958021
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.loader import AnsibleLoader

    play_context = PlayContext()
    unsafe_loader = AnsibleLoader(play_context, file_name='<string>')
    unsafe_loader.set_unsafe()

    # Safe examples
    assert wrap_var("str") == "str"
    assert wrap_var(1) == 1
    assert wrap_var(2.0) == 2.0
    assert wrap_var(["list", "of", 1]) == ["list", "of", 1]
    assert wrap_var(["list", "of", 1, ["list", "of", 1]]) == ["list", "of", 1, ["list", "of", 1]]
    assert wrap_var(("tuple", "of", 1))

# Generated at 2022-06-13 16:50:16.986452
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import u, PY2
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.common._collections_compat import Mapping, Sequence, Set

    # Don't do any wrapping on None or strings
    assert wrap_var(None) is None
    assert isinstance(wrap_var(u('foo')), text_type)
    assert isinstance(wrap_var(b'foo'), binary_type)

    # Wrap all the types subclassing Mapping
    mapping_types = (dict, builtins.set) if PY2 else (dict, set)
    for m in mapping_types:
        assert isinstance(wrap_var(m()), Mapping)

    # Wrap all the types subclassing Set
    set_types = (frozenset,)

# Generated at 2022-06-13 16:50:27.996495
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) is None
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0
    assert wrap_var(True) == True
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var({'a': 'b'}), dict)
    for k in wrap_var({'a': 'b'}):
        assert isinstance(k, AnsibleUnsafeText)

# Generated at 2022-06-13 16:50:39.076153
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var

    a = wrap_var('test')
    assert isinstance(a, AnsibleUnsafeText), 'Failed to wrap string with AnsibleUnsafeText'
    assert not isinstance(a, UnsafeProxy), 'Created an UnsafeProxy which is deprecated'

    b = wrap_var(('test', 'test'))
    assert isinstance(b, tuple), 'Failed to create tuple on sequence'

    c = wrap_var(['test', 'test'])
    assert isinstance(c, list), 'Failed to create list on sequence'

    d = wrap_var({'dict_value': 'test'})
    assert isinstance(d, dict), 'Failed to create dict'

# Generated at 2022-06-13 16:50:45.205246
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import is_sequence

    assert type(wrap_var(b"ansible")) is AnsibleUnsafeBytes
    assert type(wrap_var("ansible")) is AnsibleUnsafeText
    assert type(wrap_var({"foo": "bar"})) is dict
    assert type(wrap_var(["foo", "bar", "baz"])) is list
    assert type(wrap_var(("foo", "bar", "baz"))) is tuple
    assert type(wrap_var(set(["foo", "bar", "baz"]))) is set
    assert type(wrap_var(NativeJinjaText("{{ foo }}"))) is NativeJinjaUnsafeText
    assert type(wrap_var(None)) is type(None)
    assert wrap_var("") is ""
    assert wrap

# Generated at 2022-06-13 16:50:53.975175
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    display = Display()
    failed = False


# Generated at 2022-06-13 16:46:47.008847
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) == None
    assert wrap_var(True) == True
    assert wrap_var(1) == 1
    assert wrap_var(1.0) == 1.0
    assert wrap_var(1.0+2.0j) == 1.0+2.0j

    assert isinstance(wrap_var(to_unsafe_text('')), AnsibleUnsafeText)
    assert isinstance(wrap_var(to_unsafe_bytes(b'')), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u''), AnsibleUnsafeText)
    assert isinstance(wrap_var(b''), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(b'0'), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:46:57.784044
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var(None) == None
    assert wrap_var(1) == 1
    assert wrap_var(1.1) == 1.1
    assert wrap_var(True) == True
    assert wrap_var(False) == False
    assert isinstance(wrap_var(to_bytes('Byte string')), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(to_text('Unicode string')), AnsibleUnsafeText)
    assert type(wrap_var(['1', '2'])) is list
    assert tuple(wrap_var(('1', '2'))) == (to_unsafe_text('1'), to_unsafe_text('2'))
    assert type(wrap_var(('1', '2'))) is tuple
    assert set(wrap_var(('1', '2'))) == set

# Generated at 2022-06-13 16:47:08.201319
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2, PY3

    u = AnsibleUnsafeText(to_text('foo', errors='surrogate_or_strict'))
    u2 = wrap_var(u)
    assert u2 is u

    assert wrap_var(None) is None

    # Wrap a unicode, should return an AnsibleUnsafeText
    val = wrap_var(u'foo')
    assert isinstance(val, AnsibleUnsafeText)
    assert val == u'foo'

    # Wrap a str, should return an AnsibleUnsafeBytes
    val = wrap_var('foo')
    assert isinstance(val, AnsibleUnsafeBytes)
    assert val == b'foo'

    # Wrap a byte string, should return an AnsibleUnsafeBytes

# Generated at 2022-06-13 16:47:13.569293
# Unit test for function wrap_var
def test_wrap_var():
    import sys
    import os
    import doctest
    import ansible.constants as C

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))))

    from units.mock.loader import DictDataLoader

    from ansible.parsing.plugin_docs import read_docstring
    from ansible.utils.display import Display
    display = Display()

    # read module docs, get docstring
    my_doc, my_plainexamples, my_returndocs = read_docstring(wrap_var, verbose=False, ignore_errors=True)

# Generated at 2022-06-13 16:47:22.211334
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY2

    import json
    import locale
    import sys

    def test_encoding(wrapper, value, expected, msg):
        wrapped = wrapper(value)
        assert wrapped == expected, '%s: %r != %r' % (msg, wrapped, expected)
        assert type(wrapped) is type(expected), '%s: types %r != %r' % (msg, type(wrapped), type(expected))

    # list of (bytes, unicode) pairs for each possible encoding
    encodings = []
    for encoding in locale.getdefaultlocale()[1], locale.getpreferredencoding():
        try:
            encodings.append((encoding, encoding.replace('cp', 'CP')))
        except (TypeError, AttributeError):
            pass

   

# Generated at 2022-06-13 16:47:31.849503
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.collections import ImmutableList
    from ansible.module_utils.common.collections import ImmutableSequence
    from ansible.module_utils.common.collections import ImmutableSet

    d1 = dict(a=1, b=2, c=3)
    l1 = [1, 2, 3]
    t1 = (1, 2, 3)
    s1 = set(l1)
    di1 = ImmutableDict(a=1, b=2, c=3)
    li1 = ImmutableList([1, 2, 3])
    ti1 = ImmutableSequence((1, 2, 3))
    si1 = ImmutableSet([1, 2, 3])

    do = wrap

# Generated at 2022-06-13 16:47:36.498940
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(None), type(None))
    assert isinstance(wrap_var(123), type(123))
    assert isinstance(wrap_var(123.45), type(123.45))
    assert isinstance(wrap_var([]), list)
    assert isinstance(wrap_var(()), tuple)
    assert isinstance(wrap_var({}), dict)
    assert isinstance(wrap_var(set([])), set)
    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'bar'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'{{foo}}'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'{{foo}}'), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:47:46.838588
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import PY3

    # Check that the module variables are what we expect them to be
    assert isinstance(AnsibleUnsafe, AnsibleUnsafe)
    assert isinstance(AnsibleUnsafeBytes, AnsibleUnsafeBytes)
    assert isinstance(AnsibleUnsafeText, AnsibleUnsafeText)
    assert isinstance(NativeJinjaUnsafeText, NativeJinjaUnsafeText)

    # Make sure we don't accidentally wrap things that are already wrapped
    assert AnsibleUnsafe == wrap_var(AnsibleUnsafe)
    assert AnsibleUnsafeBytes == wrap_var(AnsibleUnsafeBytes)
    assert AnsibleUnsafeText == wrap_var(AnsibleUnsafeText)


# Generated at 2022-06-13 16:47:56.514392
# Unit test for function wrap_var
def test_wrap_var():
    import ansible.module_utils.six as six
    from ansible.module_utils.six.moves import builtins

    assert wrap_var(None) is None
    assert isinstance(wrap_var('foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(u'foo'), AnsibleUnsafeText)
    assert isinstance(wrap_var(six.binary_type()), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(list()), list)
    assert isinstance(wrap_var([]), list)
    assert isinstance(wrap_var((1, 2, 3)), tuple)
    assert isinstance(wrap_var(builtins.range(10)), list)
    assert isinstance(wrap_var(dict(key=1)), dict)

# Generated at 2022-06-13 16:48:02.195673
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var([1, 2, 3]) == [1, 2, 3]
    assert wrap_var(u"foo") == u"foo"
    assert wrap_var(u"foo") == u"foo"
    assert wrap_var(u"foo") == u"foo"
    assert wrap_var(u"foo") == u"foo"
    assert wrap_var(u"foo") == u"foo"
    assert wrap_var(u"foo") == u"foo"

# Generated at 2022-06-13 16:48:09.072324
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common.collections import is_sequence, is_hashable
    import types
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleNative

    # Check that an empty dict gets wrapped correctly
    assert(isinstance(wrap_var(dict()), dict))

    # Check that a dict gets wrapped correctly
    assert(isinstance(wrap_var(dict(foo="bar")), dict))

    # Check that a dict with unsafe value gets wrapped correctly
    fixed_dict = dict(foo="bar")

# Generated at 2022-06-13 16:48:14.004532
# Unit test for function wrap_var
def test_wrap_var():
    import copy
    test_dict = {'a': 'hello', 'b': '{{ foo }}'}
    test_list = ['a', 'b', '{{ foo }}']
    test_tuple = ('a', 'b', '{{ foo }}')
    test_set = {'a', 'b', '{{ foo }}'}

    # Deep copy -> Test if wrap_var is functional
    test_dict_copy = copy.deepcopy(test_dict)
    test_list_copy = copy.deepcopy(test_list)
    test_tuple_copy = copy.deepcopy(test_tuple)
    test_set_copy = copy.deepcopy(test_set)

    assert wrap_var(test_dict) == test_dict_copy
    assert wrap_var(test_list) == test_list_copy

# Generated at 2022-06-13 16:48:25.234563
# Unit test for function wrap_var
def test_wrap_var():
    class A():  # pylint: disable=too-few-public-methods
        pass

    a = A()
    assert isinstance(wrap_var(a), A)
    assert isinstance(wrap_var(isinstance), type)
    # By default, test is run with -bb, so bytes_or_text is not available
    # from ansible.module_utils.common._collections_compat import bytes_or_text
    # assert isinstance(wrap_var(bytes_or_text), type)

    assert isinstance(wrap_var(True), bool)
    assert isinstance(wrap_var(1), int)
    assert isinstance(wrap_var(1.0), float)
    assert isinstance(wrap_var((1, 2)), tuple)


# Generated at 2022-06-13 16:48:34.631587
# Unit test for function wrap_var
def test_wrap_var():
    # Test wrap_var
    assert(isinstance(wrap_var('my-string'), AnsibleUnsafeText))
    assert(isinstance(wrap_var(b'my-byte-string'), AnsibleUnsafeBytes))
    assert(isinstance(wrap_var(AnsibleUnsafeText('foo')), AnsibleUnsafeText))
    assert(isinstance(wrap_var(u'unicode-string'), AnsibleUnsafeText))

    assert(isinstance(wrap_var(['foo', 'bar']), list))
    assert(isinstance(wrap_var(('foo', 'bar')), tuple))
    assert(isinstance(wrap_var({'foo': 'bar'}), dict))
    assert(isinstance(wrap_var(set(['foo', 'bar'])), set))
    # Wrap embedded lists, tuples, dicts

# Generated at 2022-06-13 16:48:41.580889
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(b'abc'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(u'abc'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'abc'.decode('utf-8')), AnsibleUnsafeText)
    assert isinstance(wrap_var({'hello': b'world'}), dict)
    assert isinstance(wrap_var({'hello': b'world'}['hello']), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:48:49.302149
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import binary_type, text_type
    from ansible.module_utils.common.collections import is_sequence

    # Test Sequence
    s = 'foo'
    assert isinstance(wrap_var(s), AnsibleUnsafeText)
    assert wrap_var(s) == s
    assert type(wrap_var(s)) is AnsibleUnsafeText

    s = [1, 2, 3, 4]
    assert isinstance(wrap_var(s), list)
    assert wrap_var(s) == s
    assert type(wrap_var(s)) is list

    s = [1, 2, 3, [4, 5, 6]]
    assert isinstance(wrap_var(s), list)
    assert wrap_var(s) == s
    assert type(wrap_var(s))

# Generated at 2022-06-13 16:48:58.476403
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.common.collections import is_sequence

    safe_types = [
        '',
        u'',
        text_type(''),
        AnsibleUnsafeText(''),
        binary_type(''),
        AnsibleUnsafeBytes(''),
    ]

    unsafe_types = [
        AnsibleUnsafeText(''),
        AnsibleUnsafeBytes(''),
    ]

    # Test safe types
    for st in safe_types:
        ret = wrap_var(st)
        assert type(ret) in unsafe_types

    # Test unsafe types
    for ut in unsafe_types:
        ret = wrap_var(ut)
        assert type(ret) in unsafe_types

    # Test sequence

# Generated at 2022-06-13 16:49:05.089484
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import PY3

    assert wrap_var("test") == b"test"
    assert wrap_var(None) is None

    assert isinstance(wrap_var(b"test"), AnsibleUnsafeBytes)
    assert isinstance(wrap_var("test"), AnsibleUnsafeText)
    assert isinstance(wrap_var(u"test"), AnsibleUnsafeText)

    if PY3:
        assert isinstance(wrap_var("test"), AnsibleUnsafeText)
    else:
        assert isinstance(wrap_var("test"), unicode)


# Generated at 2022-06-13 16:49:06.684108
# Unit test for function wrap_var
def test_wrap_var():
    assert(type(wrap_var(None)) is type(None))
    assert(isinstance(wrap_var(u'plain old string'), text_type))

# Generated at 2022-06-13 16:49:14.361974
# Unit test for function wrap_var
def test_wrap_var():
    assert wrap_var('safe bytes') == AnsibleUnsafeText(u'safe bytes')
    assert wrap_var('safe unicode') == AnsibleUnsafeText(u'safe unicode')
    assert wrap_var('safe {{ foo }}') == AnsibleUnsafeText(u'safe {{ foo }}')

    # Ensure that we don't wrap AnsibleUnsafeBytes
    assert wrap_var(AnsibleUnsafeBytes(b'safe')) == AnsibleUnsafeBytes(b'safe')

    # Ensure that we don't wrap AnsibleUnsafeText
    assert wrap_var(AnsibleUnsafeText(u'safe')) == AnsibleUnsafeText(u'safe')

    # Ensure that we escape unsafe bytes regardless of input
    assert wrap_var(b'safe {{ foo }}') == AnsibleUnsafeBytes(b'safe {{ foo }}')

# Generated at 2022-06-13 16:49:23.181247
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var
    assert wrap_var(b'abc') == b'abc'
    assert wrap_var(b'abc') == u'abc'
    assert wrap_var(u'abc') == b'abc'
    assert wrap_var(u'abc') == u'abc'

    assert wrap_var(AnsibleUnsafeBytes(b'abc')) == b'abc'
    assert wrap_var(AnsibleUnsafeText(u'abc')) == u'abc'

    assert wrap_var(b'abc').__UNSAFE__ is True
    assert wrap_var(u'abc').__UNSAFE__ is True
    assert wrap_var(AnsibleUnsafeBytes(b'abc')).__UNSAFE__ is True

# Generated at 2022-06-13 16:49:33.164994
# Unit test for function wrap_var
def test_wrap_var():
    old_str = "This is a string"
    new_str = wrap_var(old_str)
    assert isinstance(new_str, AnsibleUnsafeText)
    assert new_str == old_str

    old_str = "string with 'quotes'"
    new_str = wrap_var(old_str)
    assert isinstance(new_str, AnsibleUnsafeText)
    assert new_str == old_str

    old_str = "string with \"double quotes\""
    new_str = wrap_var(old_str)
    assert isinstance(new_str, AnsibleUnsafeText)
    assert new_str == old_str

    old_dict = {"a": 1, "b": 2, "c": 3}
    new_dict = wrap_var(old_dict)

# Generated at 2022-06-13 16:49:41.434342
# Unit test for function wrap_var
def test_wrap_var():
    import jinja2
    from ansible.module_utils.common._collections_compat import Mapping, Set
    from ansible.module_utils.six import string_types

    def is_sequence(v):
        """Helper function to determine if a variable is a sequence
        """
        return (Mapping.__instancecheck__(v) or Set.__instancecheck__(v)) and not isinstance(v, string_types)

    assert is_sequence([])  # pylint: disable=no-member
    assert is_sequence({})  # pylint: disable=no-member

    # List
    l_list = ['a', 'b', 'c']
    type_list = type(l_list)
    assert l_list == wrap_var(l_list)

# Generated at 2022-06-13 16:49:51.956192
# Unit test for function wrap_var
def test_wrap_var():
    obj = {"a": {"b": "c"}}

    # Test wrapping a dictionary object
    assert isinstance(wrap_var(obj), dict)

    # Test wrapping a dictionary object in unsafe proxy
    assert isinstance(wrap_var(obj), dict)

    # Test wrapping a list object
    assert isinstance(wrap_var(["a", "b", "c"]), list)

    # Test wrapping a list object in unsafe proxy
    assert isinstance(wrap_var(["a", "b", "c"]), list)

    # Test wrapping a tuple object
    assert isinstance(wrap_var(("a", "b", "c")), tuple)

    # Test wrapping a tuple object in unsafe proxy
    assert isinstance(wrap_var(("a", "b", "c")), tuple)

    # Test wrapping a set object
    assert isinstance

# Generated at 2022-06-13 16:50:03.432686
# Unit test for function wrap_var
def test_wrap_var():
    '''
    This function checks if "wrap_var" can be safely called on multiple types.
    '''
    import collections
    import datetime
    import os
    import stat
    import sys
    import time
    import types

    TEXT_TYPES = (str, wxr.Dialog, wxr.TextCtrl, wxr.StaticText)

    # Numbers
    assert wrap_var(10) == 10
    assert wrap_var(-2.5) == -2.5
    assert wrap_var(3+4j) == 3+4j
    assert wrap_var(0xFF) == 255

    # Strings
    assert wrap_var('simple string') == 'simple string'
    assert isinstance(wrap_var('simple string'), AnsibleUnsafeText)

# Generated at 2022-06-13 16:50:09.565380
# Unit test for function wrap_var
def test_wrap_var():
    from io import StringIO
    from sys import stdout
    import unittest

    class TestWrapVar(unittest.TestCase):
        def setUp(self):
            self.old_stdout, stdout = stdout, StringIO()
            self.addCleanup(setattr, stdout, 'getvalue', stdout.getvalue)
            self.addCleanup(setattr, stdout, 'close', lambda: None)

        def test_list(self):
            x = ["mylist", 123]
            wrapped_list = wrap_var(x)
            self.assertIsInstance(wrapped_list, list)
            self.assertIsInstance(wrapped_list[1], AnsibleUnsafeBytes)
            self.assertIsInstance(wrapped_list[0], AnsibleUnsafeText)


# Generated at 2022-06-13 16:50:17.281705
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var("test_text"), AnsibleUnsafeText)
    assert wrap_var("test_text") == to_unsafe_text("test_text")

    assert isinstance(wrap_var(b"test_bytes"), AnsibleUnsafeBytes)
    assert wrap_var(b"test_bytes") == to_unsafe_bytes(b"test_bytes")

    unsafe_text = to_unsafe_text("test_unsafe_text")
    assert isinstance(wrap_var(unsafe_text), AnsibleUnsafeText)
    assert wrap_var(unsafe_text) == unsafe_text

    unsafe_bytes = to_unsafe_bytes(b"test_unsafe_bytes")
    assert isinstance(wrap_var(unsafe_bytes), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:50:28.195996
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils import six
    if six.PY3:
        from collections.abc import Mapping, Set, Sequence
    else:
        from collections import Mapping, Set, Sequence

    class Foo(object):
        pass

    assert wrap_var(1) == 1
    assert wrap_var('foo') == 'foo'
    assert wrap_var(u'foo') == u'foo'
    assert wrap_var(('foo', 'bar')) == ('foo', 'bar')
    assert wrap_var(['foo', 'bar']) == ['foo', 'bar']
    assert wrap_var({'foo': 'bar'}) == {'foo': 'bar'}
    assert wrap_var(Foo()) == Foo()

    assert isinstance(wrap_var(b'foo'), AnsibleUnsafeBytes)

# Generated at 2022-06-13 16:50:39.074788
# Unit test for function wrap_var
def test_wrap_var():
    ''' Should raise an UnsafeProxyError if unsafe content is found in data '''
    import string
    import sys
    import unittest
    from ansible.errors import AnsibleUnsafeTextError

    from ansible.module_utils.common._collections_compat import Mapping, Set

    if sys.version_info[0] > 2:
        unicode = str

    class TestUnsafeProxy(unittest.TestCase):
        def test_unsafe_proxy(self):
            self.assertTrue(isinstance(wrap_var('test'), unicode),
                            "wrap_var returned the wrong type")
            self.assertTrue(isinstance(wrap_var(b'test'), bytes),
                            "wrap_var returned the wrong type")

# Generated at 2022-06-13 16:50:47.315876
# Unit test for function wrap_var
def test_wrap_var():
    # Testing safe vars
    assert wrap_var('test') == 'test'
    assert wrap_var(None) is None
    assert wrap_var(False) is False
    assert wrap_var(True) is True
    assert wrap_var(5) == 5
    # Sequence
    assert wrap_var(['test', True, 5.0]) == ['test', True, 5.0]
    assert wrap_var(('test', True, 5.0)) == ('test', True, 5.0)
    assert wrap_var(set(['test', True, 5.0])) == set(['test', True, 5.0])
    # Mapping
    assert wrap_var({'test': True, 'foo': 5.0}) == {'test': True, 'foo': 5.0}
    # Testing unsafe vars

# Generated at 2022-06-13 16:50:56.738712
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.display import Display
    from ansible.module_utils.common.text.converters import to_text
    Display().deprecated('This module is being deprecated', version='2.13')
    # Test wrap_var
    s = b"16\n"
    assert isinstance(s, binary_type)
    assert isinstance(s, string_types)
    assert not isinstance(s, AnsibleUnsafeBytes)
    assert not isinstance(s, AnsibleUnsafeText)
    assert wrap_var(s) == b'16\n'
    assert isinstance(wrap_var(s), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(s), binary_type)
    assert isinstance(wrap_var(s), string_types)

    s = "16\n"

# Generated at 2022-06-13 16:51:05.029503
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.unsafe_proxy import wrap_var, to_unsafe_bytes, to_unsafe_text

    assert isinstance(wrap_var(1), (int, type(None)))
    assert isinstance(wrap_var('1'), (int, str, type(None)))
    assert isinstance(wrap_var('foo'), (str, type(None)))
    assert isinstance(wrap_var(b'1'), (int, str, type(None)))
    assert isinstance(wrap_var(b'foo'), (str, type(None)))
    assert isinstance(wrap_var([1, 2, 3]), (list, type(None)))
    assert isinstance(wrap_var(b'bar'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var('bar'), AnsibleUnsafeText)

# Generated at 2022-06-13 16:51:14.067279
# Unit test for function wrap_var
def test_wrap_var():

    # Test dict
    v1 = {'a': 'b', 'c': 'd'}
    assert wrap_var(v1) == v1, 'Dict(str) test failed'
    v2 = {'a': 1, 'c': 2}
    assert wrap_var(v2) == v2, 'Dict(int) test failed'
    v3 = {'a': [1, 2, '3'], 'c': 1}
    assert wrap_var(v3) == v3, 'Dict(list, int) test failed'
    v4 = {'a': {'1': '1', '2': 2}, 'c': 1}
    assert wrap_var(v4) == v4, 'Dict(dict, int) test failed'

# Generated at 2022-06-13 16:51:23.386970
# Unit test for function wrap_var
def test_wrap_var():
    # test string type input
    string = 'this is a string'
    assert isinstance(wrap_var(string), text_type)
    assert isinstance(wrap_var(string), AnsibleUnsafeText)

    # test string type input
    b_string = b'aaabbbccc'
    assert isinstance(wrap_var(b_string), binary_type)
    assert isinstance(wrap_var(b_string), AnsibleUnsafeBytes)

    # test tuple type input
    tuple_input = (1, 2, 3, 4, 5)
    assert isinstance(wrap_var(tuple_input), tuple)
    for i in wrap_var(tuple_input):
        assert isinstance(i, int)

    # test list type input
    list_input = [1, 2, 3, 4, 5]


# Generated at 2022-06-13 16:51:34.185447
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.six import text_type

    # Test for None
    assert wrap_var(None) is None

    # Test for string
    assert wrap_var("bobby") == AnsibleUnsafeText("bobby")
    assert type(wrap_var("bobby")) is AnsibleUnsafeText
    assert wrap_var("bobby") == AnsibleUnsafeText("bobby")
    assert wrap_var(u"bobby") == AnsibleUnsafeText(u"bobby")
    assert wrap_var(u"bobby") == AnsibleUnsafeText(u"bobby")

    # Test for tuple

# Generated at 2022-06-13 16:51:41.463585
# Unit test for function wrap_var
def test_wrap_var():
    import datetime

    import pytz


# Generated at 2022-06-13 16:51:49.788633
# Unit test for function wrap_var
def test_wrap_var():
    from ansible.utils.path import unfrackpath

    assert isinstance(wrap_var(1), int)
    assert isinstance(wrap_var("abc"), AnsibleUnsafeText)
    assert isinstance(wrap_var(unfrackpath("/usr/bin/")), AnsibleUnsafeText)
    assert isinstance(wrap_var(['a', 1]), list)
    assert isinstance(wrap_var(('a', 1)), tuple)
    assert isinstance(wrap_var({'a': 1}), dict)
    assert isinstance(wrap_var(set(['a', 1])), set)

    assert isinstance(wrap_var(AnsibleUnsafeBytes("abc")), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(AnsibleUnsafeText("abc")), AnsibleUnsafeText)


# Generated at 2022-06-13 16:51:59.735539
# Unit test for function wrap_var
def test_wrap_var():
    assert isinstance(wrap_var(None), type(None))
    assert wrap_var({'foo': 1}) == {'foo': 1}
    assert wrap_var(['foo', 'bar']) == ['foo', 'bar']
    assert wrap_var(('foo', 'bar')) == ('foo', 'bar')

    assert isinstance(wrap_var(NativeJinjaText('haha')), NativeJinjaUnsafeText)
    assert isinstance(wrap_var('haha'), AnsibleUnsafeText)
    assert isinstance(wrap_var(b'haha'), AnsibleUnsafeBytes)
    assert isinstance(wrap_var(AnsibleUnsafeText('haha')), AnsibleUnsafeText)

# Generated at 2022-06-13 16:52:07.718362
# Unit test for function wrap_var
def test_wrap_var():
    # List
    a = [1, 2, 3, '4']
    b = wrap_var(a)
    assert isinstance(b[0], int)
    assert isinstance(b[1], int)
    assert isinstance(b[2], int)
    assert isinstance(b[3], AnsibleUnsafeText)
    # Tuple
    a = (1, 2, 3, '4')
    b = wrap_var(a)
    assert isinstance(b[0], int)
    assert isinstance(b[1], int)
    assert isinstance(b[2], int)
    assert isinstance(b[3], AnsibleUnsafeText)
    # Dict
    a = {'1': 1, '2': '2'}
    b = wrap_var(a)

# Generated at 2022-06-13 16:52:16.305146
# Unit test for function wrap_var
def test_wrap_var():
    orig_obj = {'a': [1, 2, 3, {'1': 'one', '2': 'two', '3': 'three'}], 'b': 'b'}
    wrapped_obj = wrap_var(orig_obj)
    # Assert the original obj is untouched
    assert orig_obj['a'][3]['2'] == 'two'
    # Assert the wrapped obj is correctly wrapped
    assert isinstance(wrapped_obj['a'], list)
    assert isinstance(wrapped_obj, Mapping)
    assert isinstance(wrapped_obj['a'][3], Mapping)
    assert isinstance(wrapped_obj['a'][3]['2'], AnsibleUnsafeText)


# Generated at 2022-06-22 12:01:15.162855
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test correct behavior on valid literal values
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([1, 2, 3.0]) == 123.0
    assert ansible_native_concat([['a', 'b', 'c']]) == ['a', 'b', 'c']
    assert ansible_native_concat(['[', 'a', ']']) == ['a']
    assert ansible_native_concat(['{"a": "b"}']) == {'a': 'b'}
    assert ansible_native_concat(['True']) is True
    assert ansible_native

# Generated at 2022-06-22 12:01:27.596910
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native

    def _test_ansible_native_concat(tested_result, expected_result):
        assert tested_result == expected_result
        assert isinstance(tested_result, type(expected_result))

    _test_ansible_native_concat(ansible_native_concat([1]), 1)
    _test_ansible_native_concat(ansible_native_concat(['foo']), 'foo')
    _test_ansible_native_concat(ansible_native_concat(['foo', 'bar']), 'foobar')
    _test_ansible_native_concat(ansible_native_concat(['foo', 1]), 'foo1')


# Generated at 2022-06-22 12:01:39.014625
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2

    env = jinja2.Environment()
    env.filters['ansible_native_concat'] = ansible_native_concat
    env.filters['to_json'] = container_to_text


# Generated at 2022-06-22 12:01:51.632924
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['']) == ''
    assert ansible_native_concat(['Lorem']) == 'Lorem'
    assert ansible_native_concat(['Lorem', 'Ipsum']) == 'LoremIpsum'
    assert ansible_native_concat(['Lorem ', 'Ipsum']) == 'Lorem Ipsum'
    assert ansible_native_concat([False]) == False
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'

# Generated at 2022-06-22 12:02:03.636011
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['f', 'oo']) == 'foo'
    assert ansible_native_concat(['foo', 'b', 'a', 'r']) == 'foobar'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat([1, 2]) == '12'

# Generated at 2022-06-22 12:02:14.689510
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _check_merge(input_val, expected_val):
        result = ansible_native_concat([input_val, input_val])
        assert result == expected_val

    # valid python literals
    _check_merge(True, True)
    _check_merge(False, False)
    _check_merge(None, None)
    _check_merge(0, 0)
    _check_merge(1, 1)
    _check_merge(0.0, 0.0)
    _check_merge(1.0, 1.0)
    _check_merge([], [])
    _check_merge([1, 2], [1, 2])
    _check_merge({}, {})

# Generated at 2022-06-22 12:02:24.255624
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([container_to_text('a')]) == 'a'
    assert ansible_native_concat([container_to_text('a'), container_to_text('b')]) == 'ab'
    assert ansible_native_concat([container_to_text(42)]) == 42
    assert ansible_native_concat([container_to_text('42')]) == 42

    assert ansible_native_concat(iter([42])) == 42
    assert ansible_native_concat(iter([42, 43])) == '4243'



# Generated at 2022-06-22 12:02:36.115735
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper


# Generated at 2022-06-22 12:02:47.754419
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([])) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(iter([2])) == 2
    # A generator is passed to the function body and then converted to
    # a chain for processing.
    g = (i for i in range(10))
    assert ansible_native_concat(g) == 0
    assert ansible_native_concat([5, u'67']) == u'567'
    assert ansible_native_concat(iter([5, u'67'])) == u'567'
    g = (x for x in [6, 7])
    assert ansible_native_concat(g) == u'67'


# Generated at 2022-06-22 12:03:00.218847
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert isinstance(ansible_native_concat([1, 1]), int)
    assert isinstance(ansible_native_concat(["1", "1"]), text_type)
    assert isinstance(ansible_native_concat([1, "1"]), text_type)
    assert ansible_native_concat(["1", 1]) == "11"
    assert ansible_native_concat([True, 1]) is True
    assert ansible_native_concat([None, "1"]) is None
    assert ansible_native_concat([None, 1]) is None
    assert ansible_native_concat([1, None]) is 1
    assert ansible_native_concat([None, None]) is None
    assert ansible_native_concat(["123"]) == 123
    assert ansible_native

# Generated at 2022-06-22 12:03:13.810896
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # strings
    assert u'foo' == ansible_native_concat([u'foo'])
    assert u'foo' == ansible_native_concat([u'foo', u''])
    assert u'foobar' == ansible_native_concat([u'foo', u'bar'])
    assert u'foo bar' == ansible_native_concat([u'foo', u' ', u'bar'])

    # numbers
    assert 0 == ansible_native_concat([0])
    assert 1 == ansible_native_concat([1])
    assert 3.5 == ansible_native_concat([1.5, 2])

    # booleans
    assert True == ansible_native_concat([True])
    assert False == ansible_native_concat([False])

    # None
   

# Generated at 2022-06-22 12:03:21.006766
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([1, 'a']) == 1

    # Python 2.6 - 2.7
    # https://bugs.python.org/issue28155
    assert ansible_native_concat([1e1000, 'a']) == 1e+1000

    # Invalid float literal
    # https://github.com/pallets/jinja/issues/1200
    assert ansible_native_concat([u'1.2.3']) == u'1.2.3'

    # Too many indices for array
    # https://github.com/pallets/jinja/issues/1201

# Generated at 2022-06-22 12:03:32.038668
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class _MockContext(object):
        def __init__(self, value):
            self.value = value

        def resolve(self):
            return self.value

    assert ansible_native_concat([_MockContext('a')]) == 'a'
    assert ansible_native_concat([_MockContext('a'), _MockContext('b')]) == 'ab'
    assert ansible_native_concat([_MockContext('a'), _MockContext('b'), _MockContext('c')]) == 'abc'
    assert ansible_native_concat([_MockContext('a'), _MockContext('\u2603')]) == 'a\u2603'

# Generated at 2022-06-22 12:03:42.102741
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def test_format(expected, *args):
        assert expected == ansible_native_concat(map(text_type, args))

    test_format(None)
    test_format("")
    test_format("", "")
    test_format("1")
    test_format("1", "1")
    test_format("1", "1", "")
    test_format("str")
    test_format("str", "str")
    test_format("str", "s", "tr")
    test_format(1, 1)
    test_format(1, "1")
    test_format(1, 1, "")
    test_format(1, 1, "", "", "")
    test_format(1, "1", 1)
    test_format(1, "", 1, "")
   

# Generated at 2022-06-22 12:03:51.335717
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['{{ foo }}', '{{ bar }}']) == '{{ foo }}{{ bar }}'
    assert ansible_native_concat(['{{ foo }}', 'bar']) == '{{ foo }}bar'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([u'1', u'2', u'3']) == '123'
    assert ansible_native_concat([1, 2, 3], ',') == '1,2,3'

# Generated at 2022-06-22 12:04:00.379461
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import (
        list_to_bytes,
        list_to_native,
        list_to_text,
        to_bool,
        to_bytes,
        to_native,
        to_text,
    )

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'bar', 2]) == u'foobar2'
    assert ansible_native_concat([u'foo', 2, u'bar']) == u'foo2bar'

# Generated at 2022-06-22 12:04:11.058752
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([2, 3]) == "2, 3"
    assert ansible_native_concat(['a', 'b', 'c', 'd']) == 'abcd'
    assert ansible_native_concat('abc') == 'abc'
    assert ansible_native_concat([None, "abc"]) == 'abc'

# Generated at 2022-06-22 12:04:22.849315
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1.1]) == 1.1
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([{'foo': 'bar'}]) == {'foo': 'bar'}
    assert ansible_native_concat([{'foo': ['bar']}]) == {'foo': ['bar']}
    assert ansible_native_concat([['foo', 'bar']]) == ['foo', 'bar']

# Generated at 2022-06-22 12:04:33.468929
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:04:45.179154
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    f = ansible_native_concat
    assert f([]) == None
    assert f([1]) == 1
    assert f([1, 2]) == u'12'
    assert f([1, 2, 3, 4]) == u'1234'
    assert f([1, 2, 3, 4, 5]) == u'12345'
    assert f(i for i in [1, 2]) == u'12'
    assert f(i for i in [1, 2, 3, 4]) == u'1234'
    assert f(i for i in [1, 2, 3, 4, 5]) == u'12345'
    assert f(i for i in [1, 2]) == u'12'

# Generated at 2022-06-22 12:05:00.010349
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    res = ansible_native_concat([b'foo '])
    assert res == b'foo '
    res = ansible_native_concat([u'foo '])
    assert res == u'foo '
    res = ansible_native_concat([u'foo ', u'bar'])
    assert res == u'foo bar'
    res = ansible_native_concat([u'foo ', 1])
    assert res == u'foo 1'
    res = ansible_native_concat([u'foo ', 1, u' bar', u' baz', 2])
    assert res == u'foo 1 bar baz2'
    res = ansible_native_concat([u'[1, 2]', ' ', u'"bar"', ' ', u"(1, 2)"])

# Generated at 2022-06-22 12:05:09.916086
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test with no args
    assert ansible_native_concat([]) is None

    # test with a single int
    assert ansible_native_concat([1]) == 1

    # test with a single str
    assert ansible_native_concat(['abc']) == 'abc'

    # test with a single unsupported type
    assert ansible_native_concat([None]) is None

    # test with a single strict undefined
    assert ansible_native_concat([StrictUndefined()]) == u''

    # test with a single unicode
    assert ansible_native_concat([u'abc']) == u'abc'

    # test with a single boolean
    assert ansible_native_concat([True]) is True

    # test with a single float
    assert ansible_native_concat([1.1])

# Generated at 2022-06-22 12:05:22.980906
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import nodes
    from jinja2.compiler import concat
    from jinja2.runtime import Undefined

    undefined = Undefined('foo', name='foo')
    assert ansible_native_concat([undefined]) == undefined

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([undefined, undefined]) == undefined

    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([undefined, 'a']) == undefined

    assert ansible_

# Generated at 2022-06-22 12:05:34.793606
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, ",", 2]) == '1,2'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, ",", 2, ",", 3]) == '1,2,3'
    assert ansible_native_concat([1, ",", 2, ",", 3, 4, 5]) == '1,2,345'
    assert ansible_native_concat([1, 2, 3, 4, 5]) == '12345'

# Generated at 2022-06-22 12:05:43.732485
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert None is ansible_native_concat([])
    assert "Hello world!" is ansible_native_concat(["Hello world!"])
    assert "1" is ansible_native_concat([1])
    assert 5 is ansible_native_concat([5])
    assert None is ansible_native_concat([[None, None]])
    assert "['Hello', 'world!']" is ansible_native_concat([['Hello', 'world!']])
    assert 5 is ansible_native_concat([[1, 4]])
    assert "[1, 4]" is ansible_native_concat([[1, '4']])
    assert "Hello world!" is ansible_native_concat(["Hello ", "world!"])
    assert "['Hello', 'world!']" is ansible_native_concat

# Generated at 2022-06-22 12:05:54.626522
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 3
    assert ansible_native_concat([1, 2, 3]) == 6
    assert ansible_native_concat([1, 2, 3]) == 6
    assert ansible_native_concat(['one', 'two']) == 'onetwo'
    assert ansible_native_concat(['one', 'two', 'three']) == 'onetwothree'
    assert ansible_native_concat(is_sequence(None)) is None
    assert ansible_native_concat(is_sequence(None)) is None
    assert ansible_native_concat(is_sequence(None)) is None
    assert ansible_native_concat(['one', True]) == 'oneTrue'

# Generated at 2022-06-22 12:06:02.849772
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['alan', ' turing']) == 'alan turing'
    assert ansible_native_concat(['The number is ', '42', '.']) == 'The number is 42.'
    assert ansible_native_concat([1, '2']) == 1
    assert ansible_native_concat([-8, '2']) == -8
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['bob', ' ', 'jones']) == 'bob jones'
    assert ansible_native_concat(['bob', '\t', 'jones']) == 'bob\tjones'

# Generated at 2022-06-22 12:06:10.553517
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([None]) == None
    assert ansible_native_concat([container_to_text('foo')]) == 'foo'
    assert ansible_native_concat([container_to_text('foo'), container_to_text('bar')]) == 'foobar'
    assert ansible_native_concat([container_to_text('foo'), container_to_text('bar')]) == 'foobar'
    assert ansible_native_concat([container_to_text('{{"foo"}}')]) == 'foo'
    assert ansible_native_concat([container_to_text('{{"foo"}}'), container_to_text('bar')]) == 'foobar'

# Generated at 2022-06-22 12:06:21.325486
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test strings
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["a"]) == "a"
    assert ansible_native_concat(["a", "b"]) == "ab"
    assert ansible_native_concat(["a", "b", "c"]) == "abc"

    assert ansible_native_concat(["a", " b"]) == "a b"
    assert ansible_native_concat(["a", "  b"]) == "a  b"
    assert ansible_native_concat(["a", "   b"]) == "a   b"
    assert ansible_native_concat(["a", "    b"]) == "a    b"


# Generated at 2022-06-22 12:06:33.230044
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def check(x, y):
        assert x == y

    d = {'a': 'b', 'c': 'd'}

    check(ansible_native_concat(d.values()),
          'bd')
    check(ansible_native_concat(d),
          "abcd")

    b = {'b': 'b'}
    check(ansible_native_concat((d, b)),
          "abcd{'b': 'b'}")

    check(ansible_native_concat([d, b]),
          "{'a': 'b', 'c': 'd'}{'b': 'b'}")

    check(ansible_native_concat((d, b, 'c')),
          "abcd{'b': 'b'}c")

# Generated at 2022-06-22 12:06:46.552624
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["hello", "world"]) == 'helloworld'
    assert ansible_native_concat([1, "hello", 2, "world", 3]) == '123helloworld'
    assert ansible_native_concat([1, ["hello"], "world"]) == ['hello', 'world']
    assert ansible_native_concat([[1, 2, 'hello'], "world"]) == [[1, 2, 'hello'], 'world']
    assert ansible_native_concat([[1, 2, "hello"], ["world"]]) == [1, 2, 'hello', ['world']]
    assert ansible_native_concat([1, "hello", 2.0, "world", 3]) == ['hello', 2.0, 'world']

# Generated at 2022-06-22 12:06:58.471510
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test with list of numbers
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]

    # Test with list of strings
    assert ansible_native_concat(['a', 'b', 'c']) == ['a', 'b', 'c']

    # Test with list of numbers and strings
    assert ansible_native_concat(['a', 3, 'c']) == 'a3c'

    # Test with numbers
    assert ansible_native_concat([3]) == 3

    # Test with strings
    assert ansible_native_concat(['a']) == 'a'

    # Test with dict
    assert ansible_native_concat({'a': 1, 'b': 3}) == {'a': 1, 'b': 3}

    # Test with boolean


# Generated at 2022-06-22 12:07:10.341225
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test function with empty list
    data = []
    assert ansible_native_concat(data) is None

    # Concat list with int, str, bool
    data = [1, 'hello', True]
    assert ansible_native_concat(data) == '1helloTrue'

    # Test with various combinations of ansible.module_utils.six.text_type,
    # string, and bytes
    data = [u'\u0001', u'hello', b'world']
    assert ansible_native_concat(data) == '\x01helloworld'

    data = [u'\u0001', u'hello', 'world']
    assert ansible_native_concat(data) == '\x01helloworld'

    data = [u'\u0001', 'hello', b'world']
   

# Generated at 2022-06-22 12:07:20.616571
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # some function to test AST parseable things
    def get_string(string):
        return string

    def get_string_with_interpolation(node):
        return f'{node} {node}'

    def get_number(number):
        return number

    # the tests
    assert ansible_native_concat(iter([])) is None

    assert ansible_native_concat(iter(['1'])) == '1'

    assert ansible_native_concat(iter(['1', '2', '3'])) == '123'

    assert ansible_native_concat(iter([1, 2, 3])) == '123'

    assert ansible_native_concat(iter([1, '2', '3'])) == '123'


# Generated at 2022-06-22 12:07:31.822872
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Example nodes
    node1 = ast.Constant(1)
    node2 = ast.Constant("abc")
    node3 = ast.Constant("def")
    node4 = ast.Constant("1")
    node5 = ast.Constant("")
    node6 = ast.Constant("")
    node7 = ast.Constant("0")
    node8 = ast.Constant("0")
    node9 = ast.Constant("0.0")
    node10 = ast.Constant("0.0")
    node11 = ast.Constant("0.0e0")
    node12 = ast.Constant("0.0e0")
    node13 = ast.Constant("1.")
    node14 = ast.Constant("1.")
    node15 = ast.Constant("1.0")
    node

# Generated at 2022-06-22 12:07:42.969853
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat(['1', 2, 3]) == '123'
    assert ansible_native_concat([1, '2', 3]) == '123'

    assert ansible_native_concat([3]) == 3
    assert ansible_native_concat(['3']) == '3'
    assert ansible_native_concat([3, '3']) == '33'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False


# Generated at 2022-06-22 12:07:52.145495
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    result = ansible_native_concat(['test'])
    assert result == 'test'

    result = ansible_native_concat(['test', 'string'])
    assert result == 'teststring'

    result = ansible_native_concat([1, 2, 3])
    assert result == [1, 2, 3]

    result = ansible_native_concat(['test', 'string', 1, 2, 3])
    assert result == 'teststring1, 2, 3'

    result = ansible_native_concat(['test', 'string', 1, 2, 3, True])
    assert result == 'teststring1, 2, 3, True'



# Generated at 2022-06-22 12:08:04.658165
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['A', 'B']) == 'AB'
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1.1, 2.2, 3.3]) == 1.1 + 2.2 + 3.3
    assert ansible_native_concat([1, 2.2, 3.3]) == '123.3'
    assert ansible_native_concat([1.1, 2, 3.3]) == '123.3'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat([1, '2', '3']) == '123'

# Generated at 2022-06-22 12:08:14.562153
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:08:26.233504
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_text
    from jinja2 import Environment
    env = Environment(extensions=['jinja2.ext.do'])


# Generated at 2022-06-22 12:08:43.273978
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Unit test for function ansible_native_concat"""

# Generated at 2022-06-22 12:08:55.242738
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat(x for x in []) is None
    assert ansible_native_concat(x for x in [1]) == 1
    assert ansible_native_concat(x for x in [1, 2, 3]) == u'123'
    assert ansible_native_concat([1, 2, '3']) == 123
    assert ansible_native_concat(['1', 2, 3]) == 123
    assert ansible_native_concat([1, '2', '3']) == 123

# Generated at 2022-06-22 12:09:07.256907
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([object()]) == object()
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([u'te', u'st']) == u'test'
    assert ansible_native_concat(
        chain([u'te'], [u'st'])
    ) == u'test'
    assert ansible_native_concat([None, u'test']) == u'test'
    assert ansible_native_concat([u'12', u'34']) == 1234
    assert ansible_native_concat([u'test', u'12', u'34']) == 'test1234'

# Generated at 2022-06-22 12:09:18.524962
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _fail(nodes, msg=None):
        try:
            ansible_native_concat(nodes)
            raise AssertionError("expected failure: %s" % msg)
        except:
            pass

    _fail([], "empty data")
    _fail(['', None, ''], "empty string")
    _fail([1], "literal int")
    _fail([1, 2, 3], "literal ints")
    _fail([1, '', 2, ''])
    _fail(['', 1, ''], "int")
    _fail(['1', None, '2', None])
    _fail(['a', 'b', 'c', 'd'], "literal str")

    assert ansible_native_concat([1, 2, None, 3, None]) == 123
    assert ans

# Generated at 2022-06-22 12:09:59.020317
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:10.717954
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2
    env = jinja2.Environment(
        undefined=StrictUndefined,
        extensions=['jinja2.ext.do'],
    )

    env.filters['native'] = ansible_native_concat

    def _render(expr_str, data, expected=None, **kwargs):
        actual = env.from_string("{{ %s | native }}" % expr_str).render(data, **kwargs)
        assert actual == expected, text_type("Failed to handle {{ %s | native }}: Expected '%s', got '%s'"
                                             % (expr_str, expected, actual))

    _render("[1, 2, 3] + [4, 5, 6]", dict(), '123456')

# Generated at 2022-06-22 12:10:21.536866
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test function ansible_native_concat

    ansible-native-concat is a Jinja2 filter to create python native value
    from variable.

    The following test cases validate the variable's conversion to python
    native value and the exceptions are handled.

    The following are the test cases
    1. variable is None
    2. variable is string
    3. variable is integer
    4. variable is dictionary
    5. variable is list
    6. variable is tuple
    7. variable is None
    8. variable is AnsibleVaultEncryptedUnicode
    9. variable is NativeJinjaText
    10. variable is AnsibleVaultEncryptedUnicode
    11. variable is AnsibleVaultEncryptedUnicode and invalid literal
    """

# Generated at 2022-06-22 12:10:32.988209
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([]) is None

    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat([True, 'foo', None]) == 'TruefooNone'

    assert ansible_native_concat([1, '2', 3]) == '123'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat(['1', 2, 3.0]) == '123.0'

# Generated at 2022-06-22 12:10:41.685192
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat(['foo']) == 'foo'

    assert ansible_native_concat(['foo', 'bar']) == 'foobar'

    assert ansible_native_concat(['1', '2', '3']) == 123

    assert ansible_native_concat(['foo ', 'bar']) == 'foo bar'

    assert ansible_native_concat(['foo ', 'bar', ' baz']) == 'foo bar baz'

    assert ansible_native_concat(['foo ', 'bar', '\n', 'baz']) == 'foo bar\nbaz'


# Generated at 2022-06-22 12:10:53.372827
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test with a single node
    node_0 = ['node_0']
    assert ansible_native_concat(node_0) == 'node_0'

    # Test with a single undefined node
    node_1 = [StrictUndefined]
    assert ansible_native_concat(node_1) is StrictUndefined

    # Test with a single AnsibleVaultEncryptedUnicode node
    node_2 = [AnsibleVaultEncryptedUnicode('encrypted_data')]
    assert ansible_native_concat(node_2) == 'encrypted_data'

    # Test with a single NativeJinjaText node
    node_3 = [NativeJinjaText('native_text')]
    assert ansible_native_concat(node_3) == 'native_text'

    # Test with 2

# Generated at 2022-06-22 12:11:08.255922
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test for function ansible_native_concat:
        assert that the function properly returns a single value if the list
        of compiled nodes has length one and that the function properly
        concatenates the string values if the list has length greater than
        one and that the function returns the parsed value if the result
        can be parsed with ast.literal_eval and that the function returns
        the string if it cannot be parsed with ast.literal_eval.
    """
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 10, 'b']) == 'a10b'
    assert ansible_native_concat([10, 'a', 'b']) == 10
    assert ansible_native_con
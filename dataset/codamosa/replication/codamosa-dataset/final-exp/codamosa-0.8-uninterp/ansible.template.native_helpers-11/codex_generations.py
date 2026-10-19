

# Generated at 2022-06-22 12:01:14.198824
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat([1, 2, 3, 4]) == '1234'
    assert ansible_native_concat(['12', '34']) == 1234
    assert ansible_native_concat(['12', '3,4']) == '123,4'
    assert ansible_native_concat([1, None, 3]) == 1
    assert ansible_native_concat([1, None, 3, 4]) == '1None34'
    assert ansible_native_concat(['12', '34', {}]) == '1234{}'
    assert ansible_native_concat(['12', '34', []]) == '1234[]'

# Generated at 2022-06-22 12:01:26.503522
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat([' '.join(['a', 'b'])]) == 'a b'

    assert ansible_native_concat(['a', 'b']) == 'ab'

    assert ansible_native_concat((i for i in ['a', 'b', 'c'])) == 'abc'

    assert ansible_native_concat(('a', 'b')) == 'ab'

    assert ansible_native_concat(['+', '2', '2']) == '+2 2'
    assert ansible_native_concat(['+', '2', '2']) == '+2 2'

    assert ansible_native_concat(['a', '2']) == 'a2'
    assert ansible_native_

# Generated at 2022-06-22 12:01:36.865340
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # value can be parsed with 'ast.literal_eval' so we return the parsed value
    # 'ast.literal_eval' is able to parse int, float, list, tuple, dict, bool, None
    assert ansible_native_concat([True, False]) == [True, False]
    assert ansible_native_concat([1, 2]) == (1, 2)
    assert ansible_native_concat([1, '2']) == [1, '2']
    assert ansible_native_concat([1, [2, 3]]) == [1, [2, 3]]
    assert ansible_native_concat([1, (2, 3)]) == (1, (2, 3))

# Generated at 2022-06-22 12:01:50.075735
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', u' ', u'b']) == 'a b'
    assert ansible_native_concat([u' ', 'a', u' ', u'b']) == ' a b'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', u' ', u'b', 'c']) == 'a bc'
    assert ansible_native_concat(['a', u' ', u'b', 'c', 'd']) == 'a bcd'

    assert ansible_native_concat(['a']) == 'a'

# Generated at 2022-06-22 12:02:02.474494
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["FOO"]) == 'FOO'
    assert ansible_native_concat(["123", "456"]) == '123456'
    assert ansible_native_concat(["123", 456]) == '123456'
    assert ansible_native_concat([123, 456]) == 123456
    assert ansible_native_concat([123, "456"]) == 123456
    assert ansible_native_concat([123, "456.7"]) == 123
    assert ansible_native_concat([123, "456.7"]) == 123
    assert ansible_native_concat(["123.0", "456.0"]) == 123.0

# Generated at 2022-06-22 12:02:13.726707
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, '2', True, False, None]) == [1, '2', True, False, None]
    assert ansible_native_concat(['1', '2', '\n']) == '12'
    assert ansible_native_concat(['1', '2', '\n', 'a=1']) == '12\na=1'

    assert ansible_native_concat(['1', '2', '\n', 'a=1', '\n']) == '12\na=1'

    assert isinstance(ansible_native_concat(['1', '2', '\n', 'a=1', '\n']), text_type)

# Generated at 2022-06-22 12:02:25.385661
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == [1, 2]
    assert ansible_native_concat(['1', '2']) == [1, 2]
    assert ansible_native_concat([1, '2']) == u'12'
    assert ansible_native_concat([['1', '2']]) == u'12'
    assert ansible_native_concat([['1', '2'], ['3', '4']]) == u'1234'
    assert ansible_native_concat(['1', '2', ['3', '4']]) == u'124'
    assert ansible_native_concat(['1', '2', '3', ['4', '5']]) == u'1234'



# Generated at 2022-06-22 12:02:33.281568
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 1, 'b']) == 'a1b'
    assert ansible_native_concat(['a', True, 'b']) == 'aTrueb'
    assert ansible_native_concat(['a', False, 'b']) == 'aFalseb'
    assert ansible_native_concat(['a', {'a': 'b'}, 'b']) == "a{'a': b}b"
    assert ansible_native_concat(['a', ['b'], 'b']) == "a['b']b"

# Generated at 2022-06-22 12:02:42.093801
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'abc']) == u'abc'
    assert ansible_native_concat([u'abc', u'def']) == u'abcdef'
    assert ansible_native_concat([u' ']) == u' '
    assert ansible_native_concat([u' ', u'  ']) == u'    '
    assert not ansible_native_concat([])
    assert ansible_native_concat([u'abc', u'123']) == u'abc123'



# Generated at 2022-06-22 12:02:53.915586
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # Test that if a list of references to variables with undefined values
    # is passed and all of the references are undefined, that an exception
    # is raised.
    try:
        ansible_native_concat([StrictUndefined(), StrictUndefined()])
        assert False
    except Exception:
        pass

    assert ansible_native_concat(None) is None

    assert ansible_native_concat([]) is None

    test_obj = object()
    assert ansible_native_concat([test_obj]) is test_obj

    assert ansible_native_concat(('some', 'string')) == 'some string'

    assert ansible_native_concat((1, 2, 3)) == 123

    assert ansible_native_concat(('[1, 2, 3]')) == [1, 2, 3]

# Generated at 2022-06-22 12:03:07.791464
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat([1, '2', '3']) == 123
    assert ansible_native_concat([1, '2', '3']) == '123'
    assert ansible_native_concat(['1', 2, 3]) == 123
    assert ansible_native_concat(['1', 2, 3]) == '123'
    assert ansible_native_concat(['1', 2, 3]) == 123
    assert ans

# Generated at 2022-06-22 12:03:17.786138
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test the correctness of the ansible_native_concat function."""
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class NativeJinjaExpression(NativeJinjaText):
        def __call__(self, *args, **kwargs):
            return self


# Generated at 2022-06-22 12:03:29.017086
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    # This test case uses a single value of type NativeJinjaText and
    # three literal_evalable strings at the end.
    # This structure and order of values was added to handle a specific
    # problem in the inventory code:
    # https://github.com/ansible/ansible/issues/70831
    # https://github.com/pallets/jinja/issues/1200
    # https://github.com/ansible/ansible/issues/70831#issuecomment-664190894

# Generated at 2022-06-22 12:03:40.103515
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.utils import context_objects as co
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # TODO: eval is using literal_eval for everything but booleans, nums and None
    # so maybe that should be fixed instead. This is a test to cover that case
    assert ansible_native_concat(['false', 'true']) == 'falsetrue'

    # with_items
    assert container_to_text(ansible_native_concat(['foo', 'bar'])) == 'foobar'
    # string with with_items
    assert container_to_text(ansible_native_concat(['foo', 'bar'])) == 'foobar'

    # pipe operator - strings don't get evaled

# Generated at 2022-06-22 12:03:49.184807
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.six import PY2


# Generated at 2022-06-22 12:04:01.039578
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader

    loader = AnsibleLoader(None, None)
    dumper = AnsibleDumper(indent=2, width=80)

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(loader.construct_yaml_null()) is None

    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([3.14]) == 3.14
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat

# Generated at 2022-06-22 12:04:11.549068
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_int, to_yaml

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([['a', 2]]) == ['a', 2]
    assert ansible_native_concat([['a', 2], 'b']) == ['a', 2, 'b']
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['a', 2]) == 'a2'

# Generated at 2022-06-22 12:04:23.321736
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.common.text.converters import to_text

    im_class = type(ansible_native_concat)
    # test ansible_native_concat with single item iterable
    assert ansible_native_concat((1,)) == 1
    # test ansible_native_concat with two item iterable
    assert ansible_native_concat((1, 2)) == '12'
    # test ansible_native_concat with three item iterable
    assert ansible_native_concat((1, None, 2)) == '1None2'
    # test ansible_native_concat with string in iterable
    assert ansible_native_concat(('y',)) == 'y'
    # test ansible_

# Generated at 2022-06-22 12:04:33.904812
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ansible_native_concat([u'a', u'b', u'c', u'd']) == u'abcd'
    assert ansible_native_concat([None, None]) is None
    assert ansible_native_concat([1, None, None]) == 1
    assert ansible_native_concat(['a']) == u'a'

    assert ansible_native_concat([u'1']) == 1
    assert ans

# Generated at 2022-06-22 12:04:45.634735
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([])) is None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(iter([1])) == 1

    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(iter([1, 2])) == '12'

    assert ansible_native_concat([1, 2.2]) == '1.22'
    assert ansible_native_concat(iter([1, 2.2])) == '1.22'

    assert ansible_native_concat([False, True]) == 'FalseTrue'
    assert ansible_native_concat(iter([False, True])) == 'FalseTrue'


# Generated at 2022-06-22 12:04:58.822113
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = [
        u'1', u'2', u'3', u'4', u'5',
    ]

    assert ansible_native_concat(nodes) == u'12345'
    assert ansible_native_concat(nodes[0:1]) == u'1'
    assert ansible_native_concat(nodes[0:1]) == 1
    assert ansible_native_concat(nodes[0:2]) == u'12'
    assert ansible_native_concat(nodes[0:2]) == 12

    assert ansible_native_concat([u'False']) == u'False'
    assert ansible_native_concat([u'False']) is False

# Generated at 2022-06-22 12:05:09.192497
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:05:22.323278
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # pylint: disable=import-error
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.module_utils.common.text.converters import to_bytes, to_native

    assert ansible_native_concat(iter([])) is None
    assert ansible_native_concat(iter(['a'])) == 'a'
    assert ansible_native_concat(iter(['a', 'b'])) == 'ab'
    assert ansible_native_concat(iter(['1', 1, 1.0])) == '111.0'

    assert ansible_native_concat(iter(['1', 1, 1.0])).__class__.__name__ == 'str'

# Generated at 2022-06-22 12:05:34.238843
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['abc', 'def', 'ghi']) == 'abcdefghi'
    assert ansible_native_concat(['abc', 'def', 'ghi', 3, 4, 5]) == 'abcdefghi345'
    assert ansible_native_concat(['abc', 'def', 'ghi', 3, 4, 5, 'jkl', 'mno', 'pqr']) == 'abcdefghi345jklmnopqr'
    assert ansible_native_concat(['abc', 'def', 'ghi', 3, 4, 5, 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']) == 'abcdefghi345jklmnopqrstuvwxyz'
    assert ansible_native_concat

# Generated at 2022-06-22 12:05:44.942467
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([]) is None

    # int
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1, '2', 3]) == 123
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['1', ' 2', '3']) == u'1 2 3'
    # list
    assert ansible_native_concat([[1, 2]]) == [1, 2]
    assert ansible_native_concat(['[1,', ' 2]', '3']) == '1, 2'


# Generated at 2022-06-22 12:05:54.754927
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_text

    class jinja2_test(object):
        def __init__(self, value):
            self.value = value
        # Required for container_to_text
        def __getattr__(self, name):
            if name == '__dict__':
                return self.value
            raise AttributeError


# Generated at 2022-06-22 12:06:02.850883
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Jinja converts bare strings (e.g. 'foo') to a string object
    # and not a plain string.
    # TODO we need to unify this behavior with the rest of Ansible
    class String(str):
        pass

    test_strings = (
        String('foo'), str('foo'),
        String('foo'), b'foo'
    )

    expected_strings = (
        'foo', 'foo',
        'foo', 'foo'
    )

    for test_string, expected_string in zip(test_strings, expected_strings):
        assert ansible_native_concat([test_string]) == expected_string

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([{}]) == {}
   

# Generated at 2022-06-22 12:06:10.555243
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest
    import jinja2

    env = jinja2.Environment()
    env.filters['ansible_native_concat'] = ansible_native_concat

# Generated at 2022-06-22 12:06:21.324396
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    data = [1, 2, 3]
    assert ansible_native_concat(data) == data

    data = {'a': 1, 'b': 2, 'c': 3}
    assert ansible_native_concat(data) == data

    def _gen():
        yield 1
        yield 2
        yield 3
    assert ansible_native_concat(_gen()) == data

    data = [1, 2, 3]
    assert ansible_native_concat(v for v in data) == data

    data = {'a': 1, 'b': 2, 'c': 3}
    assert ansible_native_concat(v for v in data.items()) == data

    data = [1, 2, 3]
    assert ansible_native_concat(container_to_text(v) for v in data)

# Generated at 2022-06-22 12:06:33.229929
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['test']) == 'test'
    assert ansible_native_concat([None, 'b']) is None
    assert isinstance(ansible_native_concat(['123', '456']), int)
    assert ansible_native_concat(['123', '456']) == 123456
    assert ansible_native_concat([123, 456]) == 123456
    assert ansible_native_concat(['abc', 'def', '']) == 'abcdef'
    assert ansible_native_concat([123, None]) is None
    assert ansible_native_concat([None, 456]) is None
    assert ansible_native_concat([123]) == 123

# Generated at 2022-06-22 12:06:46.544248
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["foo", "bar"]) == "foobar"
    assert ansible_native_concat([1, "bar"]) == 1
    assert ansible_native_concat([1.0, "bar"]) == 1.0
    assert ansible_native_concat(["[1, 2]", "bar"]) == "[1, 2]"

ansible_native_concat.__doc__ = (
    """Calls jinja2 ``native_concat()`` and parses the result with ``ast.literal_eval()``.
    """
    + ansible_native_concat.__doc__
)



# Generated at 2022-06-22 12:06:58.469463
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # The ast.literal_eval(s) is equivalent to:
    # eval(compile(s, filename='', mode='eval'), {})

    # string
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['a', 'b', 'c', 'd', 'e', 'f']) == 'abcdef'
    assert ansible_native_concat(['a ', 'b', ' c', ' d ', 'e', ' f ']) == 'a b c d e f '  # noqa

    # list
    assert ansible_native_concat(['[1]']) == [1]

# Generated at 2022-06-22 12:07:10.280215
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import text_to_native_list
    from ansible.parsing.vault import VaultLib

    input_list = '''
    - a
    - b
    - c
    '''

    output = ansible_native_concat(text_to_native_list(input_list))
    if not isinstance(output, list):
        raise AssertionError("'%s' is not a list" % output)
    if output != ['a', 'b', 'c']:
        raise AssertionError("'%s' is invalid" % output)

    output = ansible_native_concat(text_to_native_list(input_list + "- d"))

# Generated at 2022-06-22 12:07:20.578410
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Verify that literal_eval is working as expected
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 1, 'b', True, False, 'c']) == 'a1bTrueFalsec'

    # Verify that literal_eval is not called when there is a single node
    assert ansible_native_concat([{'a': 1}]) == {'a': 1}

    # Verify that literal_eval is not called when there is an error

# Generated at 2022-06-22 12:07:31.763986
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # literal_eval is expected to do all the type conversion here
    # so we are only testing if it is called on the right string
    # or not

    class TestingException(Exception):
        pass

    def _test_literal_eval(s):
        if isinstance(s, text_type):
            if s == u'a':
                raise TestingException()
            else:
                return s
        else:
            raise AssertionError(u'Expected a unicode string!')

    literal_eval_call_count = 0
    literal_eval_set_value = {}

    def _literal_eval(s):
        nonlocal literal_eval_call_count
        literal_eval_call_count += 1

        if isinstance(literal_eval_set_value, dict):
            value = literal_eval_set_value

# Generated at 2022-06-22 12:07:42.926622
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, u' + ', 2]) == 3
    assert ansible_native_concat([u'a', u' + ', u'b']) == u'a + b'
    assert ansible_native_concat([u'x', u' + ', u'y', u' + ', u'z']) == u'x + y + z'
    assert ansible_native_concat([u'1', u' + ', u'2']) == 3
    assert ansible_native_concat([u'1 + 2']) == u'1 + 2'
    assert ansible_native_concat([u'1+2']) == u'1+2'
    assert ansible_native_concat([u'1 + 2 + 3']) == u'1 + 2 + 3'
   

# Generated at 2022-06-22 12:07:54.189596
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _assert_native_concat(expected, *args):
        assert expected == ansible_native_concat(args)

    _assert_native_concat(42, '42')
    _assert_native_concat(42, '  42')
    _assert_native_concat('42', 'foo', '42')
    _assert_native_concat('42foo', '42', 'foo')
    _assert_native_concat(
        [1, 2, 3],
        '  [',
        1,
        ', ',
        2,
        ', ',
        3,
        ']',
    )

# Generated at 2022-06-22 12:08:06.887248
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(container_to_text([u'foo', u'bar'])) == u'foobar'
    assert ansible_native_concat(container_to_text([u'foo', 42, u'bar'])) == u'foo42bar'
    assert ansible_native_concat(container_to_text(u'foo')) == u'foo'
    assert ansible_native_concat(42) == 42
    assert ansible_native_concat(['foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', 42, 'bar']) == u'foo42bar'

# Generated at 2022-06-22 12:08:16.734833
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import ansible.parsing.yaml.constructor
    from ansible.module_utils.common.text.converters import to_text, to_bytes

    assert ansible_native_concat([]) == None
    assert ansible_native_concat(iter([])) == None
    assert ansible_native_concat([NativeJinjaText('|')]) == '|'

    # string values
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', '1']) == 'a1'
    assert ansible_native_concat(['a', '1', '2']) == 'a12'
    assert ansible_native_concat

# Generated at 2022-06-22 12:08:28.763904
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 1

    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 1]) == 'a1'

    assert ansible_native_concat(['a', [1]]) == 'a1'
    assert ansible_native_concat([[1], 'a']) == 1
    assert ansible_native_concat([[1], [2]]) == 1

    assert ansible_native_concat([123, u'4']) == 123
    assert ansible_native_concat([u'1', 23]) == u'1'

    assert ansible_native_concat([u'\\', u'1']) == u'\\'
    assert ansible_native_concat

# Generated at 2022-06-22 12:08:39.305704
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    fail = StrictUndefined()
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert container_to_text(ansible_native_concat(['hello', 'world'])) == 'helloworld'
    assert ansible_native_concat(['123', '456']) == 123456
    assert ansible_native_concat(["'abc'"]) == 'abc'
    assert container_to_text(ansible_native_concat(['"my string"', fail])) == '"my string"'
    assert ansible_native_concat([fail]) == fail
    assert ansible_native_concat([fail, fail]) == fail

# Generated at 2022-06-22 12:08:49.285049
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert None is ansible_native_concat([])
    assert True is ansible_native_concat([True])
    assert 42 is ansible_native_concat([42])
    assert 42.42 is ansible_native_concat([42.42])
    assert 'foo' is ansible_native_concat(['foo'])
    assert 'bar' is ansible_native_concat(['foo', 'bar'])
    assert 42 is ansible_native_concat([42, 'bar'])
    assert 42.0 is ansible_native_concat([42, '42'])
    assert '42' is ansible_native_concat([42, 'bar'], '42')
    assert 42.0 is ansible_native_concat([42, 'bar'], '42', 42)
    assert '42'

# Generated at 2022-06-22 12:09:01.030086
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', 2]) == '12'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat([1, 2, '3']) == '123'

# Generated at 2022-06-22 12:09:11.837823
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # assert that we can concat two strings
    assert ansible_native_concat(['a', 'b']) == 'ab'
    # assert that we can concat two strings
    assert ansible_native_concat(['b', 'c']) == 'bc'
    # assert that we can concat a string and a number
    assert ansible_native_concat(['a', 2]) == 'a2'
    # assert that we can concat a number and a string
    assert ansible_native_concat([1, 'a']) == '1a'
    # assert that we can concat two lists
    assert ansible_native_concat(['a, b', 'a, b']) == ['a, b', 'a, b']
    # assert that we can concat a list and a string
    assert ansible

# Generated at 2022-06-22 12:09:23.358622
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['\n']) == '\n'
    assert ansible_native_concat(['\n', '\n']) == '\n\n'

    # Test multiline string
    assert ansible_native_concat(['foo', '\n', 'bar']) == 'foo\nbar'
    assert ansible_native_concat(['foo', 'bar']) == "foobar"
    assert ansible_native_concat(['1,2,3']) == '1,2,3'
    assert ansible_native_concat([container_to_text(['a', 'b'])]) == 'a,b'

# Generated at 2022-06-22 12:09:34.767941
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = ["a", "b", "c", "d", "e"]
    res = ansible_native_concat(nodes)
    assert res == "abcde"

    nodes = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]
    res = ansible_native_concat(nodes)
    assert res == "a1b2c3d4e5"

    nodes = ["a", 1, "b", 2.0, "c", 3, "d", 4, "e", 5]
    res = ansible_native_concat(nodes)
    assert res == "a1b2.0c3d4e5"


# Generated at 2022-06-22 12:09:44.597090
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    class MockNode:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

    class TestCase:
        def __init__(self, case_name, input, expected_output):
            self.case_name = case_name
            self.input = input
            self.expected_output = expected_output


# Generated at 2022-06-22 12:09:53.680933
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test 1: 'a' + 'b' = 'ab'
    nodes = [u'a', u'b']
    result = ansible_native_concat(nodes)
    assert result == u'ab'

    # Test 2: str + int = str(int)
    nodes = [u'a', 5]
    result = ansible_native_concat(nodes)
    assert result == u'5'

    # Test 3: int + str = str(int)
    nodes = [4, u'a']
    result = ansible_native_concat(nodes)
    assert result == u'4'

    # Test 4: 4 == 4
    nodes = [4]
    result = ansible_native_concat(nodes)
    assert result == 4

    # Test 5: ' ' + 'a

# Generated at 2022-06-22 12:10:04.740346
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # 'test' is not a valid python literal, so return as string
    assert 'test' == ansible_native_concat([u'test'])

    assert True == ansible_native_concat([u'True'])
    assert 42 == ansible_native_concat([u'42'])
    assert u'/tmp' == ansible_native_concat([u"'/", u'tmp'])
    assert [u'a', u'b', u'c'] == ansible_native_concat([u"['a',", u" 'b', ", u"'c']"])
    assert [u'a', u'b', u'c'] == ansible_native_concat([u"['", u'a', u"', '", u'b', u"', '", u'c', u"']"])

# Generated at 2022-06-22 12:10:15.286059
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import os
    import sys
    import subprocess
    import json

    # Save the current path
    cwd = os.getcwd()

    # Change to the directory where the playbook is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Execute the unittest Playbook
    result = subprocess.run(
        [
            sys.executable,
            'test_module.py',
            '-c',
            'local',
            '-i',
            './hosts',
            '-M',
            '../../lib',
            'test_native_concat.yaml',
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


# Generated at 2022-06-22 12:10:34.704321
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([
        u'First line\nSecond line\n'
    ]) == u'First line\nSecond line\n'

    assert ansible_native_concat([
        u'First line\n',
        u'Second line\n'
    ]) == u'First line\nSecond line\n'

    assert ansible_native_concat([
        u'{\n',
        u'    "a": "b"\n',
        u'}\n'
    ]) == {u'a': u'b'}


# Generated at 2022-06-22 12:10:42.654766
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:47.348978
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['test_string']) == 'test_string'
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, u'2', 3]) == [1, u'2', 3]
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['10', '20', '30']) == [10, 20, 30]
    assert ansible_native_concat(['test_string', 'second_string']) == 'test_stringsecond_string'
    assert ansible_native_concat(['10', '20', '30']) == [10, 20, 30]
    assert ansible

# Generated at 2022-06-22 12:10:55.904360
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u' foo', u'bar']) == u' foobar'
    assert ansible_native_concat([u'true']) is True
    assert ansible_native_concat([u'true', u'bar']) == u'truebar'
    assert ansible_native_concat([u'false']) is False



# Generated at 2022-06-22 12:11:06.134024
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test a single node
    assert ansible_native_concat(['a']) == 'a'
    # Test that literal values are returned unchanged
    assert ansible_native_concat(['a', True, {1:2, 3:4}, [1, 2]]) == ['a', True, {1:2, 3:4}, [1, 2]]
    # Test that literal values with whitespaces are returned unchanged
    assert ansible_native_concat(['a ', True, {1:2, 3:4}, [1, 2]]) == ['a ', True, {1:2, 3:4}, [1, 2]]
    # Test that literal values containing strings are returned unchanged
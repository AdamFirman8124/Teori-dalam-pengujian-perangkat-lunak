

# Generated at 2022-06-22 12:01:10.221135
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["test"]) == "test"
    assert ansible_native_concat(["test", "test1"]) == "testtest1"
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([1, "2", 3]) == "123"
    assert ansible_native_concat([1, [2], 3]) == "123"

# Generated at 2022-06-22 12:01:17.965822
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['some str']) is 'some str'
    assert ansible_native_concat([123]) is 123
    assert ansible_native_concat([1, '2', 3]) == '123'
    assert ansible_native_concat([1, '2', 3]) == 123
    assert ansible_native_concat(['a', 'b', '\"c\"']) == 'abc'
    assert ansible_native_concat(['a', 'b', '\"c\"']) == 'abc'
    assert ansible_native_concat(['a', 'b', '\"c\"']) == 'abc'
    assert ansible_

# Generated at 2022-06-22 12:01:30.601398
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat([u'1']) == u'1'
    assert ansible_native_concat(['a','b','c']) == 'abc'
    assert ansible_native_concat(['a','b',u'c']) == u'abc'
    assert ansible_native_concat(['1.0']) == '1.0'
    assert ansible_native_concat(['1.0', '2.0']) == '1.0 2.0'
    assert ansible_native_concat(['a', 1]) == 'a1'

# Generated at 2022-06-22 12:01:41.385769
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([1, 'b', 2]) == '1b2'
    assert ansible_native_concat(['{"a": [1]}']) == {'a': [1]}
    assert ansible_native_concat(['{"a": [1]}', 'b']) == '{"a": [1]}b'

    assert ansible_native_concat('a') == 'a'
    assert ansible_native_concat('ab') == 'ab'
    assert ansible_native_concat(('a', 'b')) == 'ab'
    assert ansible_native_concat('{"a": [1]}')

# Generated at 2022-06-22 12:01:53.165846
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat('a') == 'a'
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([['a']]) == 'a'
    assert ansible_native_concat('') == ''
    assert ansible_native_concat([]) == ''
    assert ansible_native_concat([[]]) == ''
    assert ansible_native_concat(1) == 1
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([[1]]) == 1
    assert ansible_native_concat([['a', 'b', 'c']]) == 'abc'

# Generated at 2022-06-22 12:02:05.582016
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Node:
        def __init__(self, v):
            self.v = v

    assert ansible_native_concat([Node('a')]) == 'a'
    assert ansible_native_concat([Node('a'), Node('b')]) == 'ab'

    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'

    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['None']) == 'None'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat(['True']) == 'True'
    assert ansible_native_concat([False]) is False
    assert ansible_native_con

# Generated at 2022-06-22 12:02:15.579719
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.six import PY3

    nodes = [True, 1, 10, 10.0, '', 'a', 'abc', u'abc', [1, 2, 3], (1, 2, 3), {'a': 1}, {'a': [1, 2, 3]}, Ellipsis, None]
    if PY3:
        nodes.append(bytes([0x61, 0x62, 0x63]))

    for node in nodes:
        assert ansible_native_concat([node]) == node

    assert ansible_native_concat([True, False]) is None
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, 'hello']) == 1

# Generated at 2022-06-22 12:02:27.240062
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['']) == ''
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['']) == ''
    assert ansible_native_concat(['', '', '']) == ''
    assert ansible_native_concat(['a ', 'b c']) == "a b c"
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['1', '2']) == '12'

# Generated at 2022-06-22 12:02:38.604863
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class TestNode(object):
        def __init__(self, value):
            self.value = value


# Generated at 2022-06-22 12:02:48.186929
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo ', 'bar']) == 'foo bar'
    assert ansible_native_concat(['foo' 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 1]) == 'foo1'
    assert ansible_native_concat([1, 2, 3]) == '123'

# Generated at 2022-06-22 12:03:03.277614
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.basic import jsonify
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # str -> str
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([b'foo']) == u'foo'
    assert ansible_native_concat([AnsibleUnsafeText(u'foo')]) == u'foo'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([1.0, 2.0]) == u'1.02.0'

# Generated at 2022-06-22 12:03:10.764781
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from jinja2 import Environment

    env = Environment(trim_blocks=True, lstrip_blocks=True, undefined=StrictUndefined)
    env.globals['native_concat'] = ansible_native_concat
    env.finalize = lambda: env.globals.update(dict(native_concat=ansible_native_concat))
    env.ansible_vault_password = 'test'


# Generated at 2022-06-22 12:03:21.629851
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test for issue https://github.com/ansible/ansible/issues/70831
    # ast.literal_eval should not be called for non-string values
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([42, 43]) == '4243'

    # ast.literal_eval should be called for string values
    assert ansible_native_concat([container_to_text(42)]) == 42
    assert ansible_native_concat([container_to_text(42), container_to_text(43)]) == '4243'

    # ast.literal_eval should be called for AnsibleVaultEncryptedUnicode values
    assert ansible_native_concat([AnsibleVaultEncryptedUnicode('42')]) == 42
    assert ansible

# Generated at 2022-06-22 12:03:33.070791
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # These tests are based off the tests in the upstream python_native module.

    # Test for concatenation
    assert ansible_native_concat([1, u'a', u'b']) == u'1ab'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([]) is None

    # Test for literal_eval
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u'True']) is True
    assert ansible_native_concat([u'False']) is False
    assert ansible_native_concat([u'None']) is None
    assert ansible_native_concat([u'1.0']) == 1.0

# Generated at 2022-06-22 12:03:42.563480
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    L = [
        to_text(x)
        for x
        in [
            1, 3, 3, 7,
            u' 1', u' 3', u' 3', u' 7',
            u'+ 1', u'+ 3', u'+ 3', u'+ 7',
            u'+1', u'+3', u'+3', u'+7',
            u'1', u'3', u'3', u'7',
        ]
    ]


# Generated at 2022-06-22 12:03:51.957169
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from collections import OrderedDict
    from ansible.module_utils.common import json

    def _test(input_, expected):
        actual = ansible_native_concat(input_)
        assert actual == expected, 'for input {0!r} expected {1!r} but got {2!r}'.format(input_, expected, actual)

    _test(['string'], 'string')
    _test(['string', 'string'], 'stringstring')
    _test(['string', {'dict': 'dict'}, 'string'], 'string{0}string'.format(container_to_text(dict(dict='dict'), format=None)))
    _test(['string', 'string'], 'stringstring')

# Generated at 2022-06-22 12:04:03.372431
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    test_cases = [
        ((), None),
        (('',), ''),
        (('a',), 'a'),
        (('a',), u'a'),
        ((u'a',), 'a'),
        ((u'a',), u'a'),
        ((u'a', 'b'), 'ab'),
        ((u'a', 'b'), u'ab'),
        (('a', u'b'), 'ab'),
        (('a', u'b'), u'ab'),
        ((u'a', u'b'), 'ab'),
        ((u'a', u'b'), u'ab'),
    ]

    for nodes, result in test_cases:
        assert ansible_native_concat(nodes) == result
        assert ansible_native_concat(iter(nodes)) == result

# Generated at 2022-06-22 12:04:12.473888
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2

    env = jinja2.Environment(
        finalize=ansible_native_concat,
        undefined_to_none=True,
    )

    template = env.from_string('{{ (1, 2, 3) | map("int") | list }}')
    assert template.render() == [1, 2, 3]

    template = env.from_string('{{ "x" * 3 }}')
    assert template.render() == "xxx"

    template = env.from_string('{{ "x" "y" "z" }}')
    assert template.render() == "xyz"

    template = env.from_string('{{ "x" | int }}')
    assert template.render() == 0

    template = env.from_string('{{ ("x", "y", "z") | join }}')

# Generated at 2022-06-22 12:04:24.271349
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Literal evaluation test
    assert ansible_native_concat([1, '+', '1']) == 2
    assert ansible_native_concat(['1', '+', '1']) == '1+1'
    assert ansible_native_concat(['a', '+', '1']) == 'a+1'
    assert ansible_native_concat(['a', '+', 'b']) == 'a+b'
    assert ansible_native_concat(['\'a\'']) == "'a'"
    assert ansible_native_concat(['"a"']) == '"a"'

    # Beginning with Python 3.10 ast.literal_eval removes leading
    # spaces/tabs from the given string.
    # For backwards compatibility we need to parse the string ourselves.
    assert ansible

# Generated at 2022-06-22 12:04:34.692812
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment, DictLoader
    e = Environment(loader=DictLoader(dict()))
    # Check single node
    node = e.native_concatenate(e.compile_expression('{{ [10, 20] }}'))
    assert node == [10, 20]
    # Check multiple nodes
    node = e.native_concatenate(e.compile_expression('{{ [10, 20] }}{{ " " }}{{ "string" }}'))
    assert node == '10 20string'
    # Check multiple nodes with variables
    node = e.native_concatenate(e.compile_expression('{{ [10, 20] }}{{ " " }}{{ "string" }}{{ " " }}{{ 40 }}'))
    assert node == '10 20string 40'
    #

# Generated at 2022-06-22 12:04:47.426259
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'test']) == u'test'
    assert ansible_native_concat([3]) == 3
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([u'test', u'1', u'test']) == u'test1test'
    # not supported by ast.literal_eval
    assert ansible_native_concat([u'0o1234']) == u'0o1234'
    # not supported by ast.literal_eval
    assert ansible_native_concat([u'0x1234']) == u'0x1234'
    # not

# Generated at 2022-06-22 12:04:50.072520
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = [None, 'foo', 'bar']
    nodes_expected = 'foobar'
    nodes_actual = ansible_native_concat(nodes)
    assert nodes_expected == nodes_actual



# Generated at 2022-06-22 12:05:00.122460
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    test = ansible_native_concat
    assert test(['foo', 'bar']) == 'foobar'
    assert test([None, 'bar']) == 'bar'
    assert test(['foo', None]) == 'foo'
    assert test([None, None]) is None
    # ensure literal_eval is working
    assert test(['{"foo": "bar"}']) == {'foo': 'bar'}
    assert test(['[1, 2, 3]']) == [1, 2, 3]
    assert test(['1']) == 1
    assert test(['[1']) == '[1'
    assert test(['-1']) == -1
    assert test(['-1.0']) == -1.0
    assert test(['-1.0e10']) == -1.0e10
   

# Generated at 2022-06-22 12:05:09.972761
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([1, 2, 3, 4]) == u'1234'

    assert ansible_native_concat(['1']) == u'1'
    assert ansible_native_concat(['1', '2']) == u'12'
    assert ansible_native_concat(['1', '2', '3']) == u'123'
    assert ansible_native_concat(['1', '2', '3', '4']) == u'1234'


# Generated at 2022-06-22 12:05:22.982932
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.playbook.play_context import PlayContext

    from jinja2 import Environment, DictLoader

    env = Environment(loader=DictLoader({'template': '{{ var1 }}'}), trim_blocks=True)
    env.filters['native'] = ansible_native_concat

    jinja_text = NativeJinjaText(env.from_string('{{ [var1]|native }}'))

    # e(): expr() test lambda that handles double-nesting of expr() in compiled code
    # jinja2.nodes.Expr => ast.Name => ast.expr
    e = lambda obj: isinstance(obj, (ast.Name, ast.Call))

    # actual(): converts compiled code objects to their actual values
    # e(): expr() test lambda
    # text_type(): convert to text_

# Generated at 2022-06-22 12:05:34.793585
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar', 42]) == 'foobar42'
    assert ansible_native_concat(['foo', 'bar', 'baz', 42]) == 'foobarbaz42'
    assert ansible_native_concat(['foo', 42, {'bar': 'baz'}]) == 'foo42{bar: baz}'
    assert ansible_native_concat(['foo', '42', 'bar', 42]) == 'foo42bar42'
    assert ansible_native_concat(['foo', 42, 'bar', '42']) == 'foo42bar42'

# Generated at 2022-06-22 12:05:41.363457
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """
    >>> test_ansible_native_concat()
    """
    import doctest
    ctx = {}

    function_name = "ansible_native_concat"
    globals_dict = {function_name: ansible_native_concat}

    doctest.run_docstring_examples(
        ansible_native_concat,
        ctx,
        optionflags=(doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.REPORT_NDIFF),
        globals=globals_dict,
        name=function_name,
    )



# Generated at 2022-06-22 12:05:51.887821
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    yaml = AnsibleConstructor(typ='safe')

    assert ansible_native_concat(()) is None

    # scalar
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat([yaml.construct_yaml_int('1'), yaml.construct_yaml_int('2')]) == '12'
    assert ansible_native_concat([u'1', u'2']) == '12'

# Generated at 2022-06-22 12:06:01.600818
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([None, None]) is None
    assert ansible_native_concat([]).strip() == u''
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', None]) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', u'b', 1]) == u'ab1'
    assert ansible_native_concat([u'a', u'b', 1, u'2']) == u'ab12'

# Generated at 2022-06-22 12:06:06.300582
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert isinstance(ansible_native_concat(['a']), string_types)
    assert isinstance(ansible_native_concat(['1']), int)
    assert isinstance(ansible_native_concat(['a', 'b']), string_types)
    assert isinstance(ansible_native_concat(['1', '2']), string_types)

# Generated at 2022-06-22 12:06:21.958629
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:06:33.869593
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat('abc') == 'abc'
    assert ansible_native_concat([1.1, 2.2, 3.3]) == '1.12.23.3'
    assert ansible_native_concat(['a', 1]) == 'a1'
    assert ansible_native_concat([1, 'a']) == '1a'
    assert ansible_native_concat(['a', 1, 'b']) == 'a1b'
    test_dict = {'foo': 'bar'}

# Generated at 2022-06-22 12:06:45.251791
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['True']) is True
    assert ansible_native_concat(['True', 'False']) == 'TrueFalse'
    assert ansible_native_concat(['[1, 2]']) == [1, 2]
    assert ansible_native_concat(['[1, 2]', '[3, 4]']) == '[1, 2][3, 4]'
    assert ansible_native_concat(['{1:2}']) == {1:2}

# Generated at 2022-06-22 12:06:52.927040
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:07:03.671308
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    native = ansible_native_concat

    assert native([]) is None
    assert native(['']) == ''
    assert native(['hello']) == 'hello'
    assert native(['hello', 'world']) == 'helloworld'
    assert native(['hello ', 'world']) == 'hello world'
    assert native(['hello\n', 'world']) == 'hello\nworld'
    assert native(['True', False]) == 'TrueFalse'
    assert native(['True', 'False']) == 'TrueFalse'
    assert native(['True', '', 'False']) == 'TrueFalse'
    assert native(['', 'True', '', 'False']) == 'TrueFalse'
    assert native(['\n', 'True', '\n', 'False']) == '\nTrue\nFalse'
   

# Generated at 2022-06-22 12:07:14.151035
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'1', u'2', u'3']) == '123'
    assert ansible_native_concat([u'1', u'2']) == '12'
    assert ansible_native_concat([u'1']) == '1'
    assert ansible_native_concat(()) == ''
    assert ansible_native_concat([u'1', u'+', u'2', u'*', u'3']) == '1+2*3'
    assert ansible_native_concat([u'2+2']) == 4
    assert ansible_native_concat([u'[1, 2, 3]']) == [1, 2, 3]
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native

# Generated at 2022-06-22 12:07:23.430494
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([ast.Str(s=1)]) == 1
    assert ansible_native_concat([ast.NameConstant(value='1')]) == '1'
    assert ansible_native_concat([ast.NameConstant(value=None)]) == None
    assert ansible_native_concat([ast.Num(n=1)]) == 1
    assert ansible_native_concat([ast.Num(n=1), ast.Num(n=2)]) == '12'
    assert ansible_native_concat([ast.Num(n=2), ast.Num(n=1)]) == '21'
    assert ansible_native_concat([ast.NameConstant(value='1'), ast.Num(n=1)]) == '11'
    assert ansible_native_

# Generated at 2022-06-22 12:07:30.348405
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # pylint: disable=missing-docstring
    assert ansible_native_concat(u'foo') is None
    assert ansible_native_concat(u'') is None
    assert ansible_native_concat([u'']) is None

    assert ansible_native_concat([u'foo']) == 'foo'
    assert ansible_native_concat([u'foo', u'bar']) == 'foobar'

    assert ansible_native_concat([u'foo', u'bar', 0, u'baz']) == 'foobar0baz'
    assert ansible_native_concat([u'foo', {u'bar': u'baz'}, u'qux']) == 'foobazqux'


# Generated at 2022-06-22 12:07:39.635362
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _test(result, nodes):
        assert ansible_native_concat(nodes) == result

    _test(None, [])
    _test('abc', ['abc'])
    _test(False, ['False'])
    _test(True, ['True'])
    _test(0, ['0'])
    _test(1, ['1'])
    _test(1.1, ['1.1'])
    _test(1j, ['1j'])
    _test(['a'], ['[', "'", 'a', "'", ']'])
    _test({'a': True}, ['{', "'", 'a', "'", ':', 'True', '}'])

# Generated at 2022-06-22 12:07:50.771792
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.common.text.converters import to_native
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping

    # The _test_data constructs a structure that would result in different
    # behavior between ansible 2.9 and 2.10. In particular, when a string
    # is concatenated with a sequence/mapping or vice versa before being
    # evaluated with literal_eval, the result is different between 2.9 and 2.10.
    # For example:
    # in 2.9 the following behaves as:
    #   to_native(['test'] + {'key:' 'value'}) == '[test]{

# Generated at 2022-06-22 12:08:10.402898
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', '2', '3']) == '123'

    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 1, 'b', 'c']) == 'a1bc'
    assert ansible_native_concat(['a', 1, 'b', 1.0, 'c']) == 'a1b1.0c'

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'

# Generated at 2022-06-22 12:08:18.897034
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test function ansible_native_concat."""
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1, 2, 3, 4]) == '1234'
    assert ansible_native_concat(['1', 2, 3, 4]) == '1234'
    assert ansible_native_concat([1, 2, 3, 4]) == '1234'
    assert ansible_native_concat([1.1, 2.2, 3.3, 4.4]) == '1.12.23.34.4'
    assert ansible_native_concat([1, 2, 3, 4]) == '1234'

# Generated at 2022-06-22 12:08:31.262075
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _test_concat(expected, *nodes):
        actual = ansible_native_concat(iter(nodes))
        assert expected == actual

    _test_concat(
        u'a',
        u'a',
    )

    _test_concat(
        u'a',
        u'a',
        None,
    )

    _test_concat(
        u'ab',
        u'a',
        u'b',
    )

    _test_concat(
        u'abcd',
        u'a',
        u'b',
        u'c',
        u'd',
    )

    _test_concat(
        u'ab',
        None,
        u'a',
        u'b',
    )


# Generated at 2022-06-22 12:08:37.488131
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([{}]) == {}
    assert ansible_native_concat([[]]) == []
    assert ansible_native_concat([[1, 2, 3]]) == [1, 2, 3]
    assert ansible_native_concat([u'']) == u''
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([1, '2', 3]) == u'123'

# Generated at 2022-06-22 12:08:45.439477
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment, meta

    env = Environment(extensions=['jinja2.ext.do'])

    # setup fake jinja nodes
    class StringValue:
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s

    nodes = []

    nodes.append(StringValue('foo'))
    nodes.append(StringValue('bar'))
    assert ansible_native_concat(nodes) == 'foobar'

    nodes.append(StringValue('/xyz'))
    assert ansible_native_concat(nodes) == 'foobar/xyz'

    nodes.append(StringValue('ansible_foo'))

# Generated at 2022-06-22 12:08:52.643532
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # pylint: disable=unused-variable,too-many-locals,too-many-branches,too-many-statements,too-many-nested-blocks
    # pylint: disable=arguments-differ,unpacking-non-sequence
    from jinja2.sandbox import ImmutableSandboxedEnvironment
    from jinja2 import UndefinedError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText
    from ansible.module_utils._text import to_text

    dummy_string = to_text(u'foo')

    # NOTE: if you change this code, you must add the corresponding test condition to the list below.
    #       We're unable to auto-include the new test

# Generated at 2022-06-22 12:09:01.189933
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Foo():
        def __len__(self):
            return 1
        def __getitem__(self, index):
            return 'foo'
    foo = Foo()
    result = ansible_native_concat([foo, 'bar'])
    assert result == 'foobar', result
    result = ansible_native_concat(['foo', foo])
    assert result == 'foobar', result
    result = ansible_native_concat([foo, foo])
    assert result == 'foofoo', result
    result = ansible_native_concat([foo, 12345])
    assert result == 'foo12345', result
    result = ansible_native_concat(['foo', 12345])
    assert result == 'foo12345', result
    result = ansible_native_concat([12345, foo])
   

# Generated at 2022-06-22 12:09:11.971687
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([1, 2]) == 3
    assert ansible_native_concat(['a', 1, 'b', 1, 'c', 2]) == 'a1b1c2'
    assert ansible_native_concat(['a', 1, 'b', 1, 2, 'c']) == 'a1b12c'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'

# Generated at 2022-06-22 12:09:23.530448
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # empty list
    assert ansible_native_concat([]) is None

    # simple join
    assert ansible_native_concat(['one', 'two']) == u'onetwo'

    # parseable as dictionary
    assert ansible_native_concat(['{', '"foo":', '"bar",', '"baz":', '42', '}']) == {u'foo': u'bar', u'baz': 42}

    # parseable as list
    assert ansible_native_concat(['[', 'True', ',', 'False', ',', '42', ']']) == [True, False, 42]

    # parseable as boolean
    assert ansible_native_concat(['True']) is True

    # unparseable

# Generated at 2022-06-22 12:09:35.067941
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Concatenation of two objects that can be parsed with ast.literal_eval
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([1.2, 3]) == 4.2
    assert ansible_native_concat(["a", "b"]) == "ab"
    assert ansible_native_concat(["a", u"b"]) == "ab"
    assert ansible_native_concat(["1", "2"]) == "12"
    assert ansible_native_concat([u"1", "2"]) == "12"
    assert ansible_native_concat(["1", u"2"]) == "12"
    assert ansible_native_concat([u"1", u"2"]) == "12"
    assert ans

# Generated at 2022-06-22 12:09:57.946810
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Using a generic function
    def test_case(result, *args):
        assert result == ansible_native_concat(args)

    test_case(1, 1)
    test_case(1, [1])

    test_case('abc', ['a', 'b', 'c'])
    test_case('a1b2c3', ['a', 1, 'b', 2, 'c', 3])
    test_case(['a1b2c3'], ['a', 1, 'b', 2, 'c', 3])
    test_case(False, False)
    test_case(False, [False])
    test_case(True, True)
    test_case(True, [True])
    test_case(False, [1])
    test_case(1, 1)

# Generated at 2022-06-22 12:10:09.959820
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', None]) == u'a'
    assert ansible_native_concat([True, None]) == True
    assert ansible_native_concat([None]) == None
    assert ansible_native_concat([]) == None

    assert ansible_native_concat([1, 2]) == 3
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([u'a', True, 1]) == u'aTrue1'

# Generated at 2022-06-22 12:10:21.439133
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2.environment import Environment

    lit_str = NativeJinjaText(u'string text')
    lit_num = NativeJinjaText(u'42')
    lit_bool = NativeJinjaText(u'False')
    lit_list = NativeJinjaText(u'[1, 2]')
    lit_dict = NativeJinjaText(u'{a: b}')
    lit_unparseable_list = NativeJinjaText(u'["a", b]')
    lit_unparseable_dict = NativeJinjaText(u'{"a": b}')
    lit_types = NativeJinjaText(u'int, float, str')

# Generated at 2022-06-22 12:10:32.938819
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test function for https://github.com/ansible/ansible/issues/52646
    # Created as separate function because of the decorator in decorators.py
    # prevents running this test from the main test suite.
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-22 12:10:41.685352
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([None, 2, 3]) is None
    assert ansible_native_concat([1, 2, 3, 4, 5]) == 12345
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a', 'bc']) == u'abc'
    assert ansible_native_concat(['a', [1, 2], 3]) == u'a[1, 2]3'
    assert ansible_native_concat(['a', {'b': 1}, 3]) == u'a{u\'b\': 1}3'

# Generated at 2022-06-22 12:10:53.372744
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["True"])
    assert ansible_native_concat(["true"]) is not True
    assert ansible_native_concat(["false"]) is not False
    assert ansible_native_concat(["False"]) is False
    assert ansible_native_concat(["1"]) == 1
    assert ansible_native_concat(["1.0"]) == 1.0
    assert ansible_native_concat(["1.1"]) == 1.1
    assert ansible_native_concat(["1e1"]) == 10.0
    assert ansible_native_concat(["1,0"]) == 1.0

# Generated at 2022-06-22 12:11:05.806741
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # This test is a bit ugly, but it is necessary to test the native python
    # type implementation, because it is invoked via the Jinja environment.
    # So, the best way to test it is to create the Jinja environment and
    # compile the j2 template and run the resulting AST against the function.
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.jinja2.environment import Environment

    vault_pass = 'secret'
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
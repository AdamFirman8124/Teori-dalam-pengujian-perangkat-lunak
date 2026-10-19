

# Generated at 2022-06-22 12:01:14.197454
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    class A:
        def __add__(self, other):
            return str(self) + str(other)

        def __str__(self):
            return "str(A)"

        def __repr__(self):
            return "repr(A)"

    class B:
        def __init__(self, string):
            self.string = string

        def __str__(self):
            return self.string

        def __repr__(self):
            return self.string

    # Test the generator directly
    def get_generator(*values):
        def gen():
            for i in values:
                yield i
        return gen()

    # Test with a single node
    assert ansible_native_concat([A()]) == "str(A)"

    # Test with multiple nodes
    assert ansible_native_con

# Generated at 2022-06-22 12:01:26.507211
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat(["hello", "world"]) == "helloworld"
    assert ansible_native_concat([ast.literal_eval("['hello', 'world']")]) == ["hello", "world"]
    assert ansible_native_concat([ast.literal_eval("{'hello': 'world'}")]) == {'hello': 'world'}
    assert ansible_native_concat([ast.literal_eval("('hello', 'world')")]) == ('hello', 'world')
    assert ansible_native_concat([ast.literal_eval("'hello world'")]) == 'hello world'
    assert ansible_native_concat([ast.literal_eval("1")]) == 1
   

# Generated at 2022-06-22 12:01:36.864932
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['hello', 2, 3, 'foo']) == 'hello23foo'
    assert ansible_native_concat(['hello', 2, 3, 'foo']) != 'hello2foo'
    assert ansible_native_concat(('hello', 2)) == 'hello2'
    assert ansible_native_concat(('hello', True)) == 'hellotrue'
    assert ansible_native_concat(('hello', False)) == 'hellofalse'
    assert ansible_native_concat(('hello', 2, 'foo')) == 'hello2foo'
    assert ansible_native_concat('hello') == 'hello'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['false']) == 'false'
   

# Generated at 2022-06-22 12:01:50.075566
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 'a']) == '1a'
    assert ansible_native_concat(['1', 'a']) == '1a'
    assert ansible_native_concat([u'1', u'a']) == u'1a'
    assert ansible_native_concat([u'1', 'a']) == u'1a'
    assert ansible_native_concat(['1', u'a']) == u'1a'
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat([u'1']) == u'1'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([u'1a']) == u'1a'


# Generated at 2022-06-22 12:02:02.474529
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import container_to_text
    assert container_to_text(ansible_native_concat(['123', None, 123])) == '123'
    assert container_to_text(ansible_native_concat(['123', None, 123, '456'])) == '123456'
    assert container_to_text(ansible_native_concat(['123', None, 123, '456', '789', None, '456'])) == '123456789456'
    assert container_to_text(ansible_native_concat(['123', None, 123, '456', None, '456', '789', None, '456'])) == '12345678'

# Generated at 2022-06-22 12:02:13.726814
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test tuple
    assert ansible_native_concat([1, 2, 3] + [4, 5, 6]) == (1, 2, 3, 4, 5, 6)

    # test list
    assert ansible_native_concat(['a', 'b', 'c'] + ['d', 'e', 'f']) == ['a', 'b', 'c', 'd', 'e', 'f']

    # test unquoted string
    assert ansible_native_concat([text_type("unquoted_string")]) == text_type("unquoted_string")

    # test scalar returned but only if 1 node
    assert ansible_native_concat([3]) == 3

    # test numbers
    assert ansible_native_concat([3] + [7]) == 10

    # test floats
    assert ans

# Generated at 2022-06-22 12:02:25.833994
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # empty list
    assert ansible_native_concat([]) is None

    # int
    assert ansible_native_concat([1]) == 1

    # string
    assert ansible_native_concat([u'foo']) == u'foo'

    # list
    assert ansible_native_concat([u'[1, 2, 3]']) == [1, 2, 3]

    # dict
    assert ansible_native_concat([u'{"a": 1}']) == {"a": 1}

    # generator
    assert ansible_native_concat((x for x in [u'foo', u'bar'])) == u'foobar'

    # multiple values
    assert ansible_native_concat([1, 2]) == u'12'

    # multiple values
    assert ansible_native_con

# Generated at 2022-06-22 12:02:37.524525
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Check for empty list
    assert ansible_native_concat([]) == None

    # Check for list with one element
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['one']) == 'one'
    assert ansible_native_concat(['one', 'two']) == 'onetwo'
    assert ansible_native_concat(['one']) == 'one'
    assert ansible_native_concat(['one', 'two']) == 'onetwo'

    # Check for list that can be parsed with ast.literal_eval
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat(['"one"', '"two"', '"three"']) == 'one two three'

# Generated at 2022-06-22 12:02:47.783092
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # https://github.com/pallets/jinja/blob/master/src/jinja2/tests/test_nativetypes.py
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["foo"]) == 'foo'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(1) == 1
    assert ansible_native_concat([u'\u1234']) == u'\u1234'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    asser

# Generated at 2022-06-22 12:02:56.247283
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Limit the size of the internal stack to make sure recursive
    # references are properly handled (7 is an arbitrary choice).
    from ansible.parsing.yaml import objects

    objects.FIXER_CONTAINER_RECURSION_LIMIT = 7
    objects.DEFAULT_VAULT_ID_MATCH = '^VaultPassword'

    # import into context so it can be called directly
    from ansible.module_utils.common.text.extended_json import _ansible_native_concat
    from ansible.module_utils.compat import ipaddress
    from ansible.module_utils.parsing.convert_bool import boolean

# Generated at 2022-06-22 12:03:10.350383
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['1', '2', '3'], '4') == 1234
    assert ansible_native_concat(['1', '2', '3'], 4) == 1234
    assert ansible_native_concat(['1', '2', '3'], 4.3) == '1234.3'
    assert ansible_native_concat(['1', '2', '3'], [4, 5, 6]) == '123456'

# Generated at 2022-06-22 12:03:21.267730
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test ansible_native_concat function."""

# Generated at 2022-06-22 12:03:32.249593
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["a", "b", "c"]) == "abc"
    assert ansible_native_concat(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]) == "abcdefghijklmnopqrstuvwxyz"
    assert ansible_native_concat([{'a': 'b'}, {'c': 'd'}]) == [{'a': 'b'}, {'c': 'd'}]

# Generated at 2022-06-22 12:03:42.237074
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([]) is None

    assert ansible_native_concat(['a', '1']) == 'a1'
    assert ansible_native_concat(['a', '1.0']) == 'a1.0'
    assert ansible_native_concat(['a', '1.0', 'b']) == 'a1.0b'
    assert ansible_native_concat(['a', 1, 'b', 2.0]) == 'a1b2.0'

    assert ansible_native_concat(['a', '1', 'b', '2']) == 'a1b2'


# Generated at 2022-06-22 12:03:51.540779
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.yaml import objects

    sandbox = {'undefined': objects.AnsibleUnsafeText('{{ foo }}')}


# Generated at 2022-06-22 12:04:02.979585
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.basic import AnsibleModule
    import base64
    import json
    import zlib

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='raw'),
        ),
        supports_check_mode=False,
    )

    def assert_concat_result(args, expected):
        data = module.params['data']

        if isinstance(data, (list, tuple)):
            data = ' '.join(data)

        if isinstance(data, string_types):
            data = data.encode('utf-8')

        module.params.update(data=data)

        with module.ansible_return_values(**args) as results:
            module.exit_json(**results)


# Generated at 2022-06-22 12:04:12.023529
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Unit test for function ansible_native_concat"""
    from nose.tools import assert_equal

    # test concat of string
    assert_equal(ansible_native_concat([1, "foo", 2, "bar", 3]), "1foobar3")

    # test concat of string and list with literal_eval
    assert_equal(ansible_native_concat([[], "foo", "bar"]), ["foo", "bar"])

    # test concat of list with literal_eval
    assert_equal(ansible_native_concat([[], 1, 2, 3]), [1, 2, 3])

    # test concat of list, tuple with literal_eval
    assert_equal(ansible_native_concat([[], '1,2,3']), [1, 2, 3])

    # test conc

# Generated at 2022-06-22 12:04:21.069941
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    test_inputs = [
        (["abc", "de"], "abcde"),
        ([123, "abc", 456], "123abc456"),
        (["abc", "456"], "abc456"),
        ([123, "456"], "123456"),
        (["123", "456"], "123456"),
        (["123", "456.789"], "123456.789"),
        (["123.456", "0"], "123.4560"),
        (["123.456", "0.789"], "123.4560.789"),
    ]
    for test_input, expected in test_inputs:
        actual = ansible_native_concat(test_input)
        assert actual == expected


# Generated at 2022-06-22 12:04:31.077036
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    original = [
        'foo',
        'bar',
        True,
        False,
        None,
        2,
        2.0,
        [1, 2, 3],
        {'a': 1, 'b': 2},
        '',
        ' ',
        [u'\u2022', 'foo'],
        ['1', '2'],
        [-3, -2, -1],
    ]

# Generated at 2022-06-22 12:04:35.984983
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest
    from ansible.module_utils.six import PY3

    from jinja2.nodes import Name, Dict, List, Tuple
    from jinja2.runtime import Context
    from jinja2.sandbox import SandboxedEnvironment

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    env = SandboxedEnvironment()
    env.globals.update({
        'ansible_native_concat': ansible_native_concat
    })

    ctx = Context({
        'v1': AnsibleUnsafeText('1'),
        'v2': AnsibleUnsafeText('2'),
    })


# Generated at 2022-06-22 12:04:50.111789
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Does not yield a single value
    assert ansible_native_concat([]) is None
    assert ansible_native_concat((n for n in [1, 2, 3])) is None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([u'abc']) == u'abc'
    assert ansible_native_concat([b'abc']) == b'abc'
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u'1.1']) == 1.1
    assert ansible_native_concat([u'1+1']) == u'1+1'

# Generated at 2022-06-22 12:04:57.975305
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text import compress_frozenset

    # Create a native type for a string
    native_string = container_to_text(u'ansible')
    assert isinstance(native_string, NativeJinjaText)
    assert isinstance(native_string.data, text_type)

    # Create a native type for a list
    native_list = container_to_text(u'["ansible", "ansible2"]')
    assert isinstance(native_list, NativeJinjaText)

# Generated at 2022-06-22 12:05:08.722281
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = [ast.Constant(1, kind=None), ast.Constant(2, kind=None)]
    assert ansible_native_concat(nodes) == 1
    nodes = [ast.Constant(1, kind=None)]
    assert ansible_native_concat(nodes) == 1
    nodes = [ast.Constant(1, kind=None), ast.Constant(u'"2"', kind=None)]
    assert ansible_native_concat(nodes) == u"12"
    nodes = [ast.Constant(1, kind=None), ast.Constant(u'"2"', kind=None), ast.Constant(3, kind=None)]
    assert ansible_native_concat(nodes) == u"123"

# Generated at 2022-06-22 12:05:21.875302
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:05:31.050741
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([2, 3]) == '23'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 2, 'c']) == 'a2c'


# https://github.com/pallets/jinja/blob/master/src/jinja2/filters.py

# Generated at 2022-06-22 12:05:42.505220
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment


# Generated at 2022-06-22 12:05:52.770872
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, 2, '3']) == '123'
    assert ansible_native_concat([1, 2, 'a']) == '1a'
    assert ansible_native_concat(['a', 2]) == 'a2'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 'b',  u'\xf3']) == u'ab\xf3'
    assert ansible_native_concat(['a', 2, True]) == 'a2True'

# Generated at 2022-06-22 12:06:01.723162
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    try:
        # python 3.8+
        from ast import Constant, Str, Tuple
    except ImportError:
        return

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['string']) == u'string'
    assert ansible_native_concat([Constant(5)]) == 5
    assert ansible_native_concat([u'5']) == 5
    assert ansible_native_concat([Constant(5), u'+']) == u'5+'
    assert ansible_native_concat([Constant(5), u'+', Constant(5)]) == 10
    assert ansible_native_concat([Constant((1, 2))]) == (1, 2)

# Generated at 2022-06-22 12:06:09.300599
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.template.safe_eval import safe_eval
    from ansible.template.templar import Templar

    def _ansible_native_concat_caller(nodes):
        return ansible_native_concat(nodes)

    templar = Templar(loader=None, shared_loader_obj=None, variables={})

    # Test the special native jinja marker
    data = NativeJinjaText(text_type('{{ foo }}'))
    assert data is _ansible_native_concat_caller([data])

    # Test the special ansible vault marker
    data = AnsibleVaultEncryptedUnicode('test')

# Generated at 2022-06-22 12:06:19.941599
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(["foo"]) == "foo"
    assert ansible_native_concat([1, "foo"]) == "1foo"
    assert ansible_native_concat([1, "foo", 2]) == "1foo2"
    assert ansible_native_concat([1, "foo", 2, 3]) == "1foo23"
    assert ansible_native_concat([1, "foo", 2, 3, 4]) == "1foo234"
    assert ansible_native_concat([1, "foo", 2, 3, 4, 5]) == "1foo2345"

    assert ansible_native_concat([u"foo"]) == u"foo"

# Generated at 2022-06-22 12:06:35.329752
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    data = [
        'hello',
        {
            'a': 1,
            'b': '2',
            'c': 3.0,
            'd': True,
            'e': False,
            'f': None,
            'g': [1, 2],
            'h': ['a', 'b'],
            'i': {'x': 1, 'y': 2},
            'j': (1, 2),
            'k': {'a': 'hello'},
            'l': ['a', 1],
            'm': '1'
        },
        {'a': 'hello'},
        [1, 2]
    ]


# Generated at 2022-06-22 12:06:46.301418
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.text.converters import to_native

    def run_test(input, expected_output):
        assert input is not None
        assert expected_output is not None

        # convert input to bytes because this is what ansible-native-concat accepts
        out = ansible_native_concat(to_bytes(input))

        # convert the output back to text so that it can be properly compared
        out = to_native(out)

        # convert both input and output to text so that we can display them properly as part of assert error message
        input = to_native(input)
        expected_output = to_native(expected_output)


# Generated at 2022-06-22 12:06:58.418344
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([u"\n"]) == u"\n"
    assert ansible_native_concat([u"\n", u"\n"]) == u"\n\n"
    assert ansible_native_concat([u"a", u"b", u"c"]) == u"abc"
    assert ansible_native_concat([123, 456]) == u"123456"
    assert ansible_native_concat([u"123", u"456"]) == 789
    assert ansible_native_concat([u"123.45", u"6"]) == 123.456
    assert ansible_native_concat([u"123.", u"456"]) == 123.456
    assert ansible_native_con

# Generated at 2022-06-22 12:07:10.281414
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Check undefined value
    assertStrictUndefined = "UndefinedError: 'strict' is undefined"
    try:
        ansible_native_concat([StrictUndefined])
    except Exception as e:
        assert str(e) == assertStrictUndefined

    # Check whether single string input returned as-is
    assert ansible_native_concat(['one']) == 'one'

    # Check whether single non-string input returned as-is
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1.1]) == 1.1
    assert ansible_native_concat([(1, 1)]) == (1, 1)
    assert ansible_native_concat([[1, 1]]) == [1, 1]
    assert ansible_native_concat

# Generated at 2022-06-22 12:07:20.578222
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test function for ansible_native_concat.
    """
    gen_data = (i for i in [1, 'str'])

    # test literal_eval succeeds
    literal_eval_nodes = [None, 1, 1.1, 'foo']
    literal_eval_nodes += ['"foo"', "'foo'"]
    literal_eval_nodes += ['{}', '[]', '()']
    literal_eval_nodes += ['{1:1}', '[1,2]', '(1,2)']
    literal_eval_nodes += [gen_data, [gen_data, 'str'], [1, gen_data]]


# Generated at 2022-06-22 12:07:29.179663
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([1, 'foo']) == '1foo'
    assert ansible_native_concat(['1', 2]) == '1'
    assert ansible_native_concat([2, 'foo']) == 2
    assert ansible_native_concat(['foo', '1', 'bar']) == 'foo1bar'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat([1, 2]) == 3
    assert ansible_native_concat(['foo', 1, 2]) == 'foo1'
    assert ansible_native_concat(['foo', 1])

# Generated at 2022-06-22 12:07:35.797637
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    tests = [
        ((), None),
        (("a",), "a"),
        (("a", "b"), u"ab"),
        ((u"\u2424",), u"\u2424"),
    ]
    for test_args, expected_value in tests:
        got_value = ansible_native_concat(test_args)
        assert got_value == expected_value



# Generated at 2022-06-22 12:07:45.450190
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def is_literal_eval(value):
        try:
            ast.literal_eval(value)
            return True
        except (ValueError, SyntaxError, MemoryError):
            return False

    # Testing correctly formatted complex strings
    assert ansible_native_concat(['["test", "test2"]']) == ['test', 'test2']
    assert ansible_native_concat(['{"key": "value"}']) == {'key': 'value'}
    assert ansible_native_concat(['("test", "test2")']) == ('test', 'test2')
    assert ansible_native_concat(['("test", "test2",)']) == ('test', 'test2',)

# Generated at 2022-06-22 12:07:56.476813
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([1, 2, 3, 4, 5]) == 12345
    assert ansible_native_concat(['a', 1, 'b']) == 'a1b'
    assert ansible_native_concat(['a', 1, 'b', 2, 'c']) == 'a1b2c'
    assert ansible_native_concat(['a', 1, 'b', 2, 'c', 3, 'd']) == 'a1b2c3d'
    assert ans

# Generated at 2022-06-22 12:08:09.219333
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _assert_literal_eval(out):
        assert isinstance(out, text_type)

        # TODO send unvaulted data to literal_eval?
        if isinstance(out, AnsibleVaultEncryptedUnicode):
            return out.data

        try:
            literal_eval_out = ast.literal_eval(
                # In Python 3.10+ ast.literal_eval removes leading spaces/tabs
                # from the given string. For backwards compatibility we need to
                # parse the string ourselves without removing leading spaces/tabs.
                ast.parse(out, mode='eval')
            )
        except (ValueError, SyntaxError, MemoryError):
            return out

        assert literal_eval_out == out

    _assert_literal_eval(ansible_native_concat([None]))
   

# Generated at 2022-06-22 12:08:23.521337
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Tests with strings
    assert ansible_native_concat([u'cat', u'chicken']) == u'catchicken'
    # The '| string' filter is needed in cases when a variable
    # is passed to a filter, such as:
    # {{ 2 | random | default(1) }}
    assert ansible_native_concat([u'cat', u'chicken | string']) == u'catchicken'
    assert ansible_native_concat([u'cat', u'/chicken']) == u'cat/chicken'
    assert ansible_native_concat([u'cat/', u'chicken']) == u'cat/chicken'
    # Tests with arrays
    assert ansible_native_concat([u'[1,', u'2, 3]']) == [1, 2, 3]

# Generated at 2022-06-22 12:08:29.782127
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat(['1', 2, 3]) == [1, 2, 3]
    assert ansible_native_concat(['[1, ', 2, 3, ']']) == [1, 2, 3]


from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.common.text.converters import to_bytes
from ansible.module_utils.common.text.converters import to_unicode
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common.text.converters import to_list
from ansible.module_utils.common.text.converters import to_bool


# Generated at 2022-06-22 12:08:41.534655
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat(u'foo') == u'foo'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([u'foo', 'bar']) == u'foobar'
    assert ansible_native_concat([1, [2]]) == u'12'
    assert ansible_native_concat([u'foo', [u'bar']]) == u'foobar'
    assert ansible_native_concat([u'foo', [u'bar', 3]]) == u'foobar3'
    assert ansible

# Generated at 2022-06-22 12:08:50.258919
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # When there is only one node, its value is returned
    assert ansible_native_concat(['1']) == '1'

    # When there are multiple nodes, they are stringly concatenated
    assert ansible_native_concat(['1', '2']) == '12'

    # When the result of the concatenation is a dict, its dict value is returned
    assert ansible_native_concat(['{', '"a": 1', '}']) == {'a': 1}

    # When the result of the concatenation is a list, its list value is returned
    assert ansible_native_concat(['[', '1, ', '2', ']']) == [1, 2]

    # When the result of the concatenation is a set, its set value is returned
    assert ansible_native_

# Generated at 2022-06-22 12:09:01.081963
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(["a"]) == "a"
    assert ansible_native_concat(["1", "2"]) == "12"
    assert ansible_native_concat(["0x100", "256"]) == "0100256"
    assert ansible_native_concat(["0x100", "0x256"]) == 0x100256
    assert ansible_native_concat(["[1, 2]", [3]]) == "[1, 2][3]"
    assert ansible_native_concat(["[1, 2]", NativeJinjaText('{"foo": "bar"}')]) == '{"foo": "bar"}'



# Generated at 2022-06-22 12:09:11.892072
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest

    assert ansible_native_concat(None) is None

    assert ansible_native_concat([]) is None

    assert ansible_native_concat([1, 2]) == '1, 2'

    assert ansible_native_concat([1, 2, 3]) == '1, 2, 3'

    assert ansible_native_concat(["1", "2", "3"]) == '"1", "2", "3"'

    assert ansible_native_concat(["1", 2, "3"]) == '"1", 2, "3"'

    assert ansible_native_concat(["1", "2", 3]) == '"1", "2", 3'

    def return_input(i):
        yield i


# Generated at 2022-06-22 12:09:23.415894
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class thing(object):
        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            return self.name == getattr(other, 'name', object())

        def __repr__(self):
            return '<Thing: %r>' % self.name

    class MockNode(object):
        def __init__(self, value):
            self.value = value

    class MockUndefined(object):
        def __str__(self):
            raise Exception()

        def __nonzero__(self):
            raise ValueError()

        __bool__ = __nonzero__


# Generated at 2022-06-22 12:09:34.847294
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) is 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat(chain([1], [2])) == u'12'
    assert ansible_native_concat([1, 2, u'3']) == u'123'
    assert ansible_native_concat([1, u'2', u'3']) == u'123'
    assert ansible_native_concat(chain([1], [u'2'], [u'3'])) == u'123'
    assert ansible_native_concat([u'1', u'2', u'3']) == u'123'

# Generated at 2022-06-22 12:09:44.669382
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2

    env = jinja2.Environment(
        undefined=StrictUndefined,
        extensions=['jinja2.ext.do'],
        keep_trailing_newline=True,
    )

    env.filters['native_concat'] = ansible_native_concat

    def test(template, expected, **kwargs):
        assert env.from_string(
            '{{ %s }}' % template
        ).render(**kwargs) == expected + '\n'

    test('"a" | native_concat', "'a'")
    test('"a" | string | native_concat', "'a'")
    test('123 | native_concat', '123')
    test('true | native_concat', 'True')

# Generated at 2022-06-22 12:09:53.758849
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    from jinja2.nodes import List, Const
    from ansible.module_utils.common.collections import is_sequence

    def mock_eval(node):
        if isinstance(node, List):
            out = []
            for item in node.items:
                out.append(mock_eval(item))
            return out
        elif isinstance(node, Const):
            return node.value
    assert 'foo' == mock_eval(ast.parse('foo', mode='eval'))
    assert b'foo' == mock_eval(ast.parse('b"foo"', mode='eval'))
    assert ast.parse("[1, 2, 3]", mode='eval') == ast.parse("[1, 2, 3]", mode='eval')

# Generated at 2022-06-22 12:10:12.055118
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    strict_undefined = StrictUndefined()
    assert ansible_native_concat([]) is None

    # Test catch of strict undefined and correct exception raising
    iter1 = [strict_undefined, 1]
    iter2 = [strict_undefined, 2]
    try:
        ansible_native_concat(iter1)
        assert False, 'strict undefined should have raised an exception'
    except UndefinedError:
        pass

    # Test single value evaluation
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'

    # Test string concatenation
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'

# Generated at 2022-06-22 12:10:23.129480
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([])) is None

    # native type
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(iter([1])) == 1

    # native type
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat(iter([1, 2])) == 1

    # native type
    assert ansible_native_concat([u'123']) == u'123'
    assert ansible_native_concat(iter([u'123'])) == u'123'

    # native type
    assert ansible_native_concat([u'123', u'456']) == u'123'
    assert ansible_native_concat

# Generated at 2022-06-22 12:10:33.923363
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Markup

    assert ansible_native_concat([1, 2]) == [1, 2]
    assert ansible_native_concat([1.0, 2.0]) == [1.0, 2.0]
    assert ansible_native_concat([]) is None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1.0]) == 1.0
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([None]) is None

    assert ansible_native_concat([1, 2]) == [1, 2]

# Generated at 2022-06-22 12:10:42.260954
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Useful if running tests on python 2.6, which doesn't have the
    # ast.literal_eval function.
    try:
        ast.literal_eval('1')
    except AttributeError:
        import sys
        def dumb_ast_literal_eval(node_or_string):
            return node_or_string
        ast.literal_eval = dumb_ast_literal_eval

# Generated at 2022-06-22 12:10:53.979746
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test with a single node
    assert ansible_native_concat([True]) is True

    # Test with multiple nodes
    assert ansible_native_concat([True, 'bar']) == 'Truebar'

    # Test with empty node
    assert ansible_native_concat([]) is None

    # Test with literal string
    assert ansible_native_concat([True, 'bar', 'baz']) == 'Truebarbaz'

    # Test with literal string
    assert ansible_native_concat([True, AnsibleVaultEncryptedUnicode("foo")]) == 'TrueVARIABLE_STRING:foo'

    # Test with native jinja text
    native_jnj_txt = NativeJinjaText("foo")

# Generated at 2022-06-22 12:11:05.906048
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo', 1, 'bar', 2, 'baz', 3, 0]) == 'foo1bar2baz30'
    assert ansible_native_concat(['foo', 1, 'bar', 2, 'baz', 3, 0]) == 'foo1bar2baz30'
    assert ansible_native_concat([u'foo', 1, u'bar', 2, u'baz', 3, 0]) == u'foo1bar2baz30'
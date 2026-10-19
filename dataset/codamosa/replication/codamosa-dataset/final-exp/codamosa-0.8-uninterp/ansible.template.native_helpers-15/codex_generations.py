

# Generated at 2022-06-22 12:01:15.730772
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert ansible_native_concat([]) == None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([u'foo']) == u'foo'

    assert ansible_native_concat([0, 1, 2]) == u'012'
    assert ansible_native_concat([True, False]) == u'TrueFalse'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([{}, {'foo': 'bar'}]) == u'{}{foo=bar}'
    assert ansible_native_concat([0, 1, 2]) == u'012'
    assert ansible_native_concat([True, False]) == u'TrueFalse'
    assert ansible_

# Generated at 2022-06-22 12:01:28.259397
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """
    Test cases for ansible_native_concat()
    """
    testcases = [
        # Test single node
        (('some_string', ), 'some_string'),
        # Test multiple nodes
        (('some_string', '_extra'), 'some_string_extra'),
        # Test multiple nodes with a list
        (('some_string', '_extra', [1, 2, 3]), 'some_string_extra[1, 2, 3]'),
        # Test multiple nodes with a dict
        (('some_string', '_extra', {'key': 'value'}), 'some_string_extra{key: value}'),
    ]

    for t in testcases:
        args, expected = t
        actual = ansible_native_concat(args)

# Generated at 2022-06-22 12:01:39.595310
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1, 2, 3, 4]) == '1 2 3 4'
    assert ansible_native_concat([1, 2, '3', 4]) == '1 2 3 4'
    assert ansible_native_concat([1, 2, '3', '4']) == '1 2 3 4'
    assert ansible_native_concat([1, 2, '3', '4.5']) == '1 2 3 4.5'
    assert ansible_native_concat([1, 2, '3', '4.5']) == '1 2 3 4.5'

# Generated at 2022-06-22 12:01:52.048684
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([1, '2', 3]) == 1
    assert ansible_native_concat([1, '2', 3]) == 1
    assert ansible_native_concat([1, '2', 3]) == 1
    assert ansible_native_concat([1, '2', 3]) == 1
    assert ansible_native_concat(['1', '2', 3]) == '1'
    assert ansible_native_concat(['1', '2', 3]) == '1'
    assert ansible_native_concat(['1', '2', 3]) == '1'

# Generated at 2022-06-22 12:02:04.181833
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from jinja2.compiler import CodeGenerator
    from jinja2.nodes import Const
    from jinja2.parser import Parser
    from jinja2.runtime import Context

    def _test_expr(expr, value_type, value=None, context=None):
        ast = Parser(expr).parse()
        cg = CodeGenerator()
        ast.accept(cg)
        codeobj = compile(cg.code, '<string>', 'exec')
        value_func = types.FunctionType(codeobj, {})

        if context is None:
            context = Context()

        got = value_func(context)
        if value is not None:
            assert got == value


# Generated at 2022-06-22 12:02:14.873799
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class UndefinedObject:
        def __str__(self):
            raise StrictUndefined("Sorry, this is not defined.")

        def __unicode__(self):
            raise StrictUndefined("Sorry, this is not defined.")

        def __mod__(self, v):
            raise StrictUndefined("Sorry, this is not defined.")

        def __call__(self):
            raise StrictUndefined("Sorry, this is not defined.")

        def __getitem__(self, item):
            raise StrictUndefined("Sorry, this is not defined.")

        def __getattr__(self, name):
            raise StrictUndefined("Sorry, this is not defined.")

        def __nonzero__(self):
            raise StrictUndefined("Sorry, this is not defined.")

        def __bool__(self):
            raise StrictUnd

# Generated at 2022-06-22 12:02:26.617482
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test the function in ansible_native_concat
    # 1. Test for list
    # 2. Test for dictionary
    # 3. Test for string
    # 4. Test for integer
    # 5. Test for boolean
    # 6. Test for set
    # 7. Test for tuple
    # 8. Test for frozen set

    test_list = [1, 2, 3, 4]
    test_dictionary = {"key1": 1, "key2": 2}
    test_string = "This is a string"
    test_integer = 5
    test_boolean = True
    test_set = {1, 2, 3, 4}
    test_tuple = 1, 2, 3, 4
    test_frozen_set = frozenset([1, 2, 3, 4])

    # Test for list
    assert ans

# Generated at 2022-06-22 12:02:38.192517
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([None]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(['a', u'\u2022', 'c']) == u'a•c'
    assert ansible_native_concat(['a', u'\u2022', 'c']) == [u'a', u'\u2022', u'c']
   

# Generated at 2022-06-22 12:02:48.023540
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(["test"]) == "test"
    assert ansible_native_concat([1, 2]) == "12"
    assert ansible_native_concat([1, None, 2]) == "12"
    assert ansible_native_concat([None, None]) == ""
    assert ansible_native_concat([1, "2"]) == "12"
    assert ansible_native_concat(["1", 2]) == "12"
    assert ansible_native_concat(["1", "2"]) == "12"
    assert ansible_native_concat([b"1", b"2"]) == "12"
    assert ansible_native_

# Generated at 2022-06-22 12:03:00.436108
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None

    # when passed a single item, return it
    assert ansible_native_concat([1]) == 1

    # when passed multiple items, concatenate them and try to
    # parse them using ast.literal_eval
    assert ansible_native_concat([1, 2, 3, 4]) == 10
    assert ansible_native_concat(["1", "2", "3", "4"]) == "1234"
    assert ansible_native_concat([1, "1", "2", "3", "4"]) == "11234"

    # should parse/evaluate valid python expressions
    assert ansible_native_concat(['[1, 2, 3]']) == [1, 2, 3]

# Generated at 2022-06-22 12:03:14.053869
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import ansible.constants as C

    from ansible.module_utils.common.collections import to_native_types as to_native

    C.DEFAULT_HASH_BEHAVIOUR = 'replace'

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([None]) is None

    assert ansible_native_concat([1, 2]) == '1 2'
    assert ansible_native_concat([None, 1, None]) == 'None 1 None'
    assert ansible_native_concat([None, 1, None, (), None]) == 'None 1 None () None'

    assert ansible_native_concat([u'hello']) == u'hello'

# Generated at 2022-06-22 12:03:21.149065
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    from ansible.module_utils.common.text.converters import to_native

    assert to_native(ansible_native_concat([])) is None
    assert to_native(ansible_native_concat([5])) == 5
    assert to_native(ansible_native_concat(['foo'])) == 'foo'

    assert to_native(ansible_native_concat([5, 3])) == '53'
    assert to_native(ansible_native_concat(['foo', 'bar'])) == 'foobar'

    assert to_native(ansible_native_concat([5, 'bar'])) == '5bar'
    assert to_native(ansible_native_concat(['foo', 3])) == 'foo3'


# Generated at 2022-06-22 12:03:32.178611
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([42, 1337]) == u'421337'
    assert ansible_native_concat([u'42', u'1337']) == u'421337'
    assert ansible_native_concat([u'42', 1337]) == u'421337'

    # literal_eval
    assert ansible_native_concat([u'42']) == 42
    assert ansible_native_concat([u'42', u'1337']) == 421337
    assert ansible_native_concat([u'42', u'1337']) == 421337
    assert ansible_native_concat([u'42', u'1337'])

# Generated at 2022-06-22 12:03:42.211739
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Test basic string concatenation
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat([u'foo', u'bar']) == 'foobar'
    assert ansible_native_concat([AnsibleUnicode('foo'), AnsibleUnicode('bar')]) == 'foobar'

    # Test text data type
    lst = [AnsibleUnicode('foo'), NativeJinjaText(AnsibleUnicode('bar'))]
    assert ansible_native_concat(lst) == 'foobar'

    # Test integer concatenation
    assert ansible_native_concat([1, 2]) == 3
    assert ansible_

# Generated at 2022-06-22 12:03:51.451605
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class test_strictundefined(object):
        def __str__(self):
            raise RuntimeError

        def __repr__(self):
            raise RuntimeError

    # Test single item, non-string
    data = ansible_native_concat([5])
    assert data == 5

    # Test multiple items, non-string
    data = ansible_native_concat([5, 3])
    assert data == u'53'

    # Test single item, string
    data = ansible_native_concat(['foo'])
    assert data == 'foo'

    # Test multiple items, string
    data = ansible_native_concat(['foo', ' bar'])
    assert data == u'foo bar'

    # Test single item, dict

# Generated at 2022-06-22 12:03:56.836283
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u"test"]) == "test"
    assert ansible_native_concat([u"test", u"test"]) == "testtest"
    assert ansible_native_concat([123, u"test"]) == 123
    assert ansible_native_concat([u"123", u"test"]) == 123



# Generated at 2022-06-22 12:04:07.296698
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_text
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', u'b', 'c']) == 'abc'
    assert ansible_native_concat([1, 2, 3, 4]) == 10
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat(['1', '2, 3', '4']) == '1, 234'
    assert ansible_native_concat(['1', '2.5', '3']) == '1.5'

# Generated at 2022-06-22 12:04:16.091576
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert(ansible_native_concat([u'foo', ' ', 'bar']) == u'foo bar')
    assert(ansible_native_concat([u'\u20ac', ' ', 'bar']) == u'€ bar')
    assert(ansible_native_concat([]) is None)
    assert(ansible_native_concat((x for x in [])) is None)
    assert(ansible_native_concat(u'foo') == u'foo')
    assert(ansible_native_concat(u'\u20ac') == u'\u20ac')



# Generated at 2022-06-22 12:04:27.530256
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test function, formally known as concat_native."""
    # Variables
    UTF8_STRING = u'\"123ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\"'

# Generated at 2022-06-22 12:04:36.132961
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat('') is None
    assert ansible_native_concat('a') == 'a'
    assert ansible_native_concat('a', 'b') == 'ab'
    assert ansible_native_concat(1, 2, 3) == '123'

    assert ansible_native_concat(1) == 1
    assert ansible_native_concat(1, 2) == [1, 2]
    assert ansible_native_concat(1, 2, 3) == [1, 2, 3]
    assert ansible_native_concat('a', 'b', 'c') == ['a', 'b', 'c']

    assert ansible_native_concat('a', 1) == 'a1'

# Generated at 2022-06-22 12:04:53.692851
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'bar', u'baz']) == u'foobarbaz'
    assert ansible_native_concat([u'foo', u'bar', u'baz', u'qux']) == u'foobarbazqux'

    assert ansible_native_concat([u'foo']) == u'foo'

    assert ansible_native_concat([u'True']) is True
    assert ansible_native_concat([u'False']) is False
    assert ansible_native_concat([u'None']) is None
    assert ansible_native_concat([u'1234']) == 1234
    assert ansible_

# Generated at 2022-06-22 12:05:07.292116
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment, DictLoader, nodes
    env = Environment(loader=DictLoader(dict()))
    env.filters['ansible_native_concat'] = ansible_native_concat
    env.runtime.__ansible_native_concat = ansible_native_concat


# Generated at 2022-06-22 12:05:20.628946
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["abc", "def"]) == "abcdef"
    assert ansible_native_concat(["abc", "{# foo #}", "def"]) == "abc{# foo #}def"
    assert ansible_native_concat(["{% raw %}abc", "def{% endraw %}"]) == "{% raw %}abcdef{% endraw %}"
    assert ansible_native_concat(["abc", "2", "1"]) == "abc21"
    assert ansible_native_concat(["abc", "2", "+", "1"]) == "abc2+1"
    assert ansible_native_concat(["abc", ["a", "b", "c"]]) == "abcabc"

# Generated at 2022-06-22 12:05:32.961606
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test for boolean
    node1 = ast.NameConstant(True)
    node2 = ast.NameConstant(False)
    assert ansible_native_concat([node1]) == True
    assert ansible_native_concat([node2]) == False
    # test for int
    node3 = ast.Constant(123)
    assert ansible_native_concat([node3]) == 123
    # test for long
    node4 = ast.Constant(123456789123456789)
    assert ansible_native_concat([node4]) == 123456789123456789
    # test for float
    node5 = ast.Constant(1.0)
    assert ansible_native_concat([node5]) == 1.0
    # test for list

# Generated at 2022-06-22 12:05:44.022737
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def _generator(items):
        for i in items:
            yield i

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([1, 2]) == 12

# Generated at 2022-06-22 12:05:53.968828
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['1', '2']) == '12'

    orig = [1, '2', ['3'], AnsibleVaultEncryptedUnicode('1234'), {'a': 'b'}]
    assert ansible_native_concat(iter(orig)) == orig

    assert ansible_native_concat([u'1', u'2']) == u'12'
    assert ansible_native_concat([u'\u00f1']) == u'\u00f1'

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, '2']) == '12'
   

# Generated at 2022-06-22 12:06:02.311939
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """The function ansible_native_concat is tested for a wide range of
    values.
    """


# Generated at 2022-06-22 12:06:11.718010
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # Test simple strings
    assert ansible_native_concat(['a', 'b']) == 'ab'

    # Test simple literals
    assert ansible_native_concat(['1', '2']) == 12
    assert ansible_native_concat([1, 2]) == 3

    # Test native types
    assert ansible_native_concat(['{', '}']) == {}
    assert ansible_native_concat(['[', ']']) == []
    assert ansible_native_concat(['(', ')']) == ()

    # Test combinations of literals and non-literals
    assert ansible_native_concat(['1', 2]) == 12
    assert ansible_native_concat(['{', '}', 'abc']) == '{}abc'
    assert ansible_

# Generated at 2022-06-22 12:06:22.468018
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def assert_equal(nodes, expected):
        assert ansible_native_concat(nodes) == expected

    # Recursively call assert_equal with multiple items in the `nodes` list
    # and compare the result with the given `expected` value.
    # Note: The first item in `nodes` is used as the first argument to
    # assert_equal. If `nodes` is a single item, there is no recursive call.
    nodes = 'value'
    expected = 'value'
    assert_equal(nodes, expected)

    nodes = ['value']
    expected = 'value'
    assert_equal(nodes, expected)

    nodes = [1]
    expected = 1
    assert_equal(nodes, expected)

    nodes = []
    expected = None
    assert_equal(nodes, expected)

# Generated at 2022-06-22 12:06:34.435033
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat([1, 2, '3']) == '123'
    assert ansible_native_concat([1, 2, '3', []]) == '123[]'
    assert ansible_native_concat([1, 2, '3', {}]) == '123{}'
    assert ansible_native_concat([1, 2, '3', {}, '4']) == '123{}4'

# Generated at 2022-06-22 12:06:47.460776
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == 12
    assert ansible_native_concat([1, 'b']) == "'1b'"
    assert ansible_native_concat(['a', 2]) == "'a2'"
    assert ansible_native_concat('abc') == 'abc'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, 'b', 3]) == "'1b3'"
    assert ansible_native_

# Generated at 2022-06-22 12:06:59.196773
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:07:11.012510
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.six import PY3

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaVariable

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([])) is None

    if PY3:
        assert ansible_native_concat([None]) is None
        assert ansible_native_concat(iter([None])) is None
    else:
        assert ansible_native_concat([None]) == ''
        assert ansible_native_concat(iter([None])) == ''

    assert ansible_native_concat([NativeJinjaVariable('var1')]) == 'var1'
    assert ansible_native_con

# Generated at 2022-06-22 12:07:16.840592
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import types
    import ansible.parsing.yaml.objects

    # test defaults
    assert ansible_native_concat(None) is None
    assert ansible_native_concat([]) is None

    # test string concatenation
    assert ansible_native_concat(["a", "b"]) == "ab"
    assert ansible_native_concat(["a", "b", "c", "d"]) == "abcd"

    # test string escaping
    assert ansible_native_concat(["a'b", "c'd", "e'f", "g'h"]) == "a'bc'de'fg'h"
    assert ansible_native_concat(["a", "b", "c", "'single_quote'"]) == "abcsingle_quote"
    assert ansible

# Generated at 2022-06-22 12:07:28.181169
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, 2, 3, 4]) == '1234'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat(['1', 2, '3', '4']) == '1234'
    assert ansible_native_concat([1, '2', 3, '4']) == '1234'
    assert ansible_native_concat(['1', '2', '3', '4']) == '1234'
    assert ansible_

# Generated at 2022-06-22 12:07:40.133843
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([0]) == 0
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat([None]) is None

    assert ansible_native_concat([0, 1]) == '01'
    assert ansible_native_concat([0, 1, 2]) == '012'
    assert ansible_native_concat([0, 'foo', 1]) == '0foo1'

    # dict
    assert ansible_native_concat([{'foo': 'bar'}]) == {'foo': 'bar'}

    # list
    assert ansible

# Generated at 2022-06-22 12:07:51.475487
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_str

    # in most cases the list is short
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'Hello']) == u'Hello'
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat([u'Hello', u'World']) == u'HelloWorld'
    assert ansible_native_concat([u'Hello', 42, u'World']) == u'HelloWorld'
    assert ansible_native_concat([u'Hello', 42, u'World', True]) == u'HelloWorld'
    assert ansible_native_concat([u'Hello', 42, u'World', True, False]) == u'HelloWorld'
    assert ansible

# Generated at 2022-06-22 12:08:04.033390
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'foo', u'', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'bar', u'']) == u'foobar'
    assert ansible_native_concat([u'', u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo', u'', u'bar', u'']) == u'foobar'

# Generated at 2022-06-22 12:08:14.050578
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test normal concat
    nodes = ['a', 'b', 'c']
    assert ''.join(nodes) == ansible_native_concat(nodes)

    # test literal_eval on int
    nodes = ['1']
    assert 1 == ansible_native_concat(nodes)

    # test literal_eval on string
    nodes = ['"a', 'b"']
    assert 'ab' == ansible_native_concat(nodes)

    # test literal_eval on string with spaces
    nodes = ['"a ', ' b"']
    assert 'a b' == ansible_native_concat(nodes)

    # test literal_eval on string with leading spaces
    nodes = ['"  a ', ' b"']
    assert '  a b' == ansible_native_concat(nodes)

# Generated at 2022-06-22 12:08:22.326431
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # ensure passed values are native
    assert ansible_native_concat(['item']) == 'item'
    assert ansible_native_concat(['item', 'next_item']) == 'itemnext_item'
    assert ansible_native_concat(['item', 'next_item', 'next_next_item']) == 'itemnext_itemnext_next_item'

    # ensure passed lists are converted to strings
    assert ansible_native_concat(['item', ['next_item']]) == "['next_item']"
    assert ansible_native_concat(['item', ['next_item'], 'next_next_item']) == "['next_item']next_next_item"

    # ensure passed dictionaries are converted to strings

# Generated at 2022-06-22 12:08:42.398944
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test that ansible_native_concat function works as expected."""
    # data

# Generated at 2022-06-22 12:08:54.315967
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test that container objects can be converted to strings
    assert ansible_native_concat([6, 'test']) == u'6test'
    assert ansible_native_concat(['6', ['test']]) == u'6test'

    # Test that literal_eval is performed
    assert ansible_native_concat([6, 'test']) == u'6test'

    # Test that StrictUndefined raises an exception
    try:
        ansible_native_concat([6, StrictUndefined()])
        assert False
    except UndefinedError:
        assert True

    # Test that the type is correct
    assert ansible_native_concat(['test']) == u'test'
    assert type(ansible_native_concat(['test'])) == string_types

    # Test that native jin

# Generated at 2022-06-22 12:09:06.250837
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Undefined(StrictUndefined):
        """An undefined, which can be added to any object to force
        undefined behavior in native types.
        """

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([1.5, 2, 3]) == u'1.52'
    assert ansible_native_concat([1.5, 2, 3]) == u'1.52'
    assert ansible_native_concat(['a', 'b']) == u'ab'

    # short-circuit literal_eval for non-string values
    assert ansible_native_concat([u'1'])

# Generated at 2022-06-22 12:09:17.366809
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', ' ', 'c']) == 'a c'
    assert ansible_native_concat(['a', '"', 'c']) == 'a"c'
    assert ansible_native_concat(['a', '\n', 'c']) == 'a\nc'
    assert ansible_native_concat(['a', '\n', 'c\n', 'def']) == 'a\nc\ndef'
    assert ansible_native_concat(['a', ' ', True, ' ', False]) == 'a True False'

# Generated at 2022-06-22 12:09:28.816584
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    ast_literal_eval = ast.literal_eval

    def ast_literal_eval_exception(value):
        try:
            ast_literal_eval(value)
        except (ValueError, SyntaxError, MemoryError):
            return True
        return False

    # Check if ast.literal_eval supports the "is" keyword
    if ast_literal_eval_exception("is"):
        # ast.literal_eval does not support the "is" keyword,
        # so we need to replace ast.literal_eval for the unit test below
        def ast_literal_eval(value):
            if value == "is":
                return True
            return ast_literal_eval_exception(value)

    # types.GeneratorType is base class for generator objects.
    # Since generator objects are not iter

# Generated at 2022-06-22 12:09:38.988260
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["a", "b ", " c\n\\\n\n", "d\ne", "f\n", "g"]) == u'ab c\n\\\n\n\nd\nef\ng'
    assert ansible_native_concat(["a", "b ", " c\n\\\n\n", "d\ne", "f\n", "g"]) == u'ab c\n\\\n\n\nd\nef\ng'
    assert ansible_native_concat(["a", "b ", " c\n\\\n\n", "d\ne", "f\n", "g"]) == u'ab c\n\\\n\n\nd\nef\ng'

# Generated at 2022-06-22 12:09:47.717908
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test function ansible_native_concat."""
    from ansible.template import Templar

    ref = {
        'str': 'this is a string',
        'lst': [1, 2, 3],
        'tpl': '{% if tst %}true{% else %}false{% endif %}',
        'dict': {'a': 'b'},
        'flt': 1.5,
        'bin': b'\xff',
        'none': None,
    }
    templar = Templar(None)

    for key, value in ref.items():
        # Test valid input
        assert ansible_native_concat([value]) == value, 'input: %s' % value

# Generated at 2022-06-22 12:09:57.947338
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        {'yaml': '''
  - 42
  - name:
    - foo
    - 42
  - name:
    - foo
    - 42
  - 42
        ''',
         'json': '''
            {"foo": ["bar", [24, 42, "baz"]]}
        '''},
        check_invalid_arguments=False,
    )
    result = module.from_json(module.params['json'])
    assert result == {'foo': ['bar', [24, 42, 'baz']]}
    # check that whitespace does not get removed from json
    result = module.from_json(''' {"foo": ["bar", [24, 42, "baz"]]} ''')


# Generated at 2022-06-22 12:10:09.915721
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # https://github.com/pallets/jinja/blob/master/tests/test_nativetypes.py
    assert ansible_native_concat(iter([])) is None
    assert ansible_native_concat(iter([42])) == 42
    assert ansible_native_concat(iter([42, 1337])) == '421337'
    assert ansible_native_concat(iter([42, 1337, 3.14])) == '4213373.14'
    assert ansible_native_concat(iter([42, 1337, 3.14, u'π'])) == '421337' + container_to_text(3.14) + u'π'

# Generated at 2022-06-22 12:10:21.439735
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def check(expected, items):
        assert expected == ansible_native_concat(items)

    items = [u'foo', u'bar', u'baz', u'qux']

    for item in items:
        check(item, (item,))
        for other in items:
            if item is other:
                continue
            check(u''.join((item, other)), (item, other))

    def join(items):
        return u''.join(map(container_to_text, items))

    check(u'foobarbazqux', items)

    check(u'foobarbazqux', (u'foo', u'', u'bar', u'baz', u'qux'))

# Generated at 2022-06-22 12:10:36.774610
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    import sys

    class MockNode(object):
        hidden_attr = None

    class MockCompiler(object):
        def __init__(self, name, params, body):
            self.func = lambda: name

        def __call__(self, *args, **kwargs):
            return MockNode()

    class TestStrictUndefined(StrictUndefined):
        def __init__(self, name, locals, fail_on_undefined=True, undefined_to_none=False):
            self.name = name
            self.locals = locals

        def __repr__(self):
            return 'Undefined(%r)' % self.name

    class MockEnvironment(object):
        """Mock jinja environment for concat tests.

        Takes a dict of functions that can be mocked out for simpler testing.
        """
       

# Generated at 2022-06-22 12:10:47.399284
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(iter(['1', '1'])) == '11'
    assert ansible_native_concat(iter(['1', '1.0'])) == 11
    assert ansible_native_concat(iter(['1', 'a'])) == '1a'
    assert ansible_native_concat(iter(['1', None])) is None
    assert ansible_native_concat(iter(['1', ['1']])) == ['1', '1']
    assert ansible_native_concat(iter(['1', {'a': 'b'}])) == {'a': 'b'}
    assert not isinstance(ansible_native_concat(iter([u'\xdf'])), text_type)

# Generated at 2022-06-22 12:10:58.604866
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2
    # This test depends on jinja2.native_concat because it evaluates the compiled nodes.
    env = jinja2.Environment(extensions=[], undefined=jinja2.StrictUndefined)

    undefined = env.undefined
    assert ansible_native_concat([undefined]) is undefined

    assert ansible_native_concat([undefined, 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', undefined, 'c']) == 'a%s' % undefined
    assert ansible_native_concat(['a', 'b', undefined]) == '%sbc' % undefined
    assert ansible_native_concat([undefined, undefined, undefined]) == undefined


# Generated at 2022-06-22 12:11:07.163628
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([123]) == 123
    assert ansible_native_concat(['1.23']) == 1.23
    assert ansible_native_concat(['de']) == 'de'
    assert ansible_native_concat(['de']) == 'de'
    assert ansible_native_concat([[12, 34]]) == [12, 34]
    assert ansible_native_concat([['123', '456']]) == '123456'
    assert ansible_native_concat(['123', '456']) == '123456'
    assert ansible_native_concat([['123', '456'], '78']) == '12345678'
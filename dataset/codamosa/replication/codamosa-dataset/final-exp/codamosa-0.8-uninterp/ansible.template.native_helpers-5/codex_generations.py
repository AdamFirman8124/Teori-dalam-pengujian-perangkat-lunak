

# Generated at 2022-06-22 12:01:14.116391
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([2]) == 2
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([{}]) == {}
    assert ansible_native_concat([{1: 2}]) == {1: 2}
    assert ansible_native_concat([[]]) == []
    assert ansible_native_concat([[1]]) == [1]
    assert ansible_native_concat([1, 2]) == 3
    assert ansible_native_concat(["foo", 2]) == "foo2"
    assert ansible_native_concat(["foo", "bar", 2]) == "foobar2"
    assert ans

# Generated at 2022-06-22 12:01:26.443991
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template.safe_eval import ansible_template

    t = ansible_template("{{ foo | concat('a', 42, 42.5, [1, 2, 3], {a: b}) }}")
    assert t({'foo': 'abc', 'b': 42}) == 'abc42a424242.5[1, 2, 3]{u\'a\': 42}'

    t = ansible_template("{{ foo | concat(42) }}")
    assert t({'foo': 'abc'}) == 42

    t = ansible_template("{{ foo | concat(42.5) }}")
    assert t({'foo': 'abc'}) == 42.5

    t = ansible_template("{{ foo | concat([1, 2, 3]) }}")

# Generated at 2022-06-22 12:01:38.078117
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert isinstance(ansible_native_concat(['str', None]), string_types)
    assert ansible_native_concat(['str', None]) == 'str'

    assert isinstance(ansible_native_concat(['str', 'none']), string_types)
    assert ansible_native_concat(['str', 'none']) == 'strNone'

    assert isinstance(ansible_native_concat(['str', 'none', 1]), string_types)
    assert ansible_native_concat(['str', 'none', 1]) == 'strNone1'

    assert isinstance(ansible_native_concat(['str1', 'str2']), string_types)
    assert ansible_native_concat(['str1', 'str2']) == 'str1str2'


# Generated at 2022-06-22 12:01:50.859219
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    from ansible.template import generate_ansible_template_vars
    from operator import getitem
    source = generate_ansible_template_vars()

    def _get_function(name, source):
        return getitem(source, name)

    def _call_function(name, source, args):
        return _get_function(name, source)(*args)

    # Basic tests
    func = _get_function('ansible_native_concat', source)
    assert func() is None  # Empty list
    assert func(1) == 1
    assert func(1, 2) == '12'
    assert func(u'a', 1, 2) == u'a12'
    assert func(1, 2, u'a') == '12a'

    assert func(1, u'2', 3) == '123'

# Generated at 2022-06-22 12:02:03.065359
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat([1, 2, 3]) == '1'
    assert ansible_native_concat([u'1', u'2']) == '1'
    assert ansible_native_concat([u'1', u'2', u'3']) == '123'
    assert ansible_native_concat([u'1', u'2', u'3']) == '123'
    assert ansible_native_concat([u'{', u'"test_str":', u'"foo",', u'"test_int":', u'42', u'}']) == \
        '{"test_str": "foo", "test_int": 42}'

# Generated at 2022-06-22 12:02:14.198815
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template.safe_eval import ansible_native_concat as nc

    assert nc(None) is None
    assert nc([]) is None
    assert nc([1]) == 1
    assert nc([1, 2, 3]) == '123'
    assert nc([1, 'foo', 3]) == [1, 'foo', 3]
    assert nc([1, 2, 3, 'foo']) == '123foo'
    assert nc([1, 'foo', 3, 'bar']) == [1, 'foo', 3, 'bar']
    assert nc(['foo', 'bar']) == 'foobar'
    assert nc(['foo', 'bar', 'baz']) == 'foobarbaz'

# Generated at 2022-06-22 12:02:22.615404
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert True is ansible_native_concat([])
    assert False is ansible_native_concat([False])
    assert True is ansible_native_concat([True])
    assert 'True' is ansible_native_concat([True, ' '])
    assert 'abc' is ansible_native_concat(['a', 'b', 'c'])
    assert '1' is ansible_native_concat([1])
    assert 'ab' is ansible_native_concat([u'a', u'b'])
    assert u'ab' is ansible_native_concat([u'a', u'b'])
    assert 1 == ansible_native_concat(['1'])
    assert 1 == ansible_native_concat(['1 '])
    assert ['a'] == ansible_native

# Generated at 2022-06-22 12:02:30.146895
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['"foo"', '"bar"']) == 'foobar'
    assert ansible_native_concat([u'foo', 'bar']) == u'foobar'

    assert ansible_native_concat([u'foo', 1]) == u'foo1'
    assert ansible_native_concat([u'foo', '1']) == u'foo1'
    assert ansible_native_concat([u'foo', u'1']) == u'foo1'

    assert ansible_native_concat([u'foo', None]) == u'fooNone'
    assert ansible_native_concat([u'foo', 'None']) == u'fooNone'
    assert ans

# Generated at 2022-06-22 12:02:40.356740
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test function ansible_native_concat and related functions
    """

    # Test normal case
    assert ansible_native_concat(["a", "b", "c"]) == "abc"

    # Test case where one node is evaluated
    assert ansible_native_concat([0, 1, 2]) == 0

    # Test case where literal_eval parse fails
    assert ansible_native_concat(["a", "b", ":"]) == "abc:"

    # Test case where literal_eval parse succeeds
    assert ansible_native_concat(["[", "a", ",", "b", "]"]) == ["a", "b"]

    # Test case where literal_eval raises an exception

# Generated at 2022-06-22 12:02:52.212742
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b', '4', '5', '"']) == 'ab45"'
    assert ansible_native_concat(['a', 'b', '"', '\n', 'c', '"']) == 'ab"\nc"'
    assert ansible_native_concat(['a', 'b', '"', '\n', 'c', '"', '\n', 'd', "'", '"']) == 'ab"\nc"\nd\'\''
    assert ansible_native_concat(['a', 'b', '"', '\n', 'c', '"', '\n', 'd', "'", '"', '\n', 'e', "'", "'", "'"]) == 'ab"\nc"\nd\'\'\ne\'\'\''
    assert ansible

# Generated at 2022-06-22 12:03:07.226606
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None

    assert ansible_native_concat(["True"]) == "True"
    assert ansible_native_concat(["1"]) == "1"
    assert ansible_native_concat(["1.0"]) == "1.0"
    assert ansible_native_concat(["'single'"]) == "'single'"
    assert ansible_native_concat(['"double"']).strip("'") == '"double"'
    assert ansible_native_concat(['1,2,3']) == '1,2,3'
    assert ansible_native_concat(['1.0,2.0,3.0']) == '1.0,2.0,3.0'

# Generated at 2022-06-22 12:03:17.751475
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template.safe_eval import ansible_native_concat as ansible_native_concat_eval

# Generated at 2022-06-22 12:03:29.017712
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'a']) == 'a'
    assert ansible_native_concat([u'a', u'b']) == 'ab'
    assert ansible_native_concat([u'a', u'b', u'c']) == 'abc'
    assert ansible_native_concat([u'a', 1, u'b', None, u'c']) == 'a1bNonec'
    assert ansible_native_concat([u'a', u'b', u'c']) == 'abc'
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 1]) == '11'


# Generated at 2022-06-22 12:03:40.102105
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest

    # Define some variables
    test_vars = {
        'an_empty_str': '',
        'an_empty_unicode': '',
        'some_str': 'this is a string',
        'some_unicode': u'\u00f6\u00e4\u00fc',
        'a_list': ['this', 'is', 'a', 'list'],
        'a_dict': {'this': 'is', 'a': 'dict'},
        'an_int': 42,
        'a_float': 3.141592,
        'a_bool': True
    }

    # Define some tests

# Generated at 2022-06-22 12:03:51.279863
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # with literal_eval
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([1, 2, 3, 4]) == 10
    assert ansible_native_concat([1.4, 2.6]) == 4.0
    assert ansible_native_concat([True, False]) == True
    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([u'foo'])) == u'foo'
    assert ansible_native_concat(iter([u'foo', u'bar'])) == u'foobar'
    # no literal

# Generated at 2022-06-22 12:04:02.742822
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["a"])  == "a"
    assert ansible_native_concat(["a", "b"]) == "ab"
    assert ansible_native_concat(["True"])  == "True"
    assert ansible_native_concat(["1", "a"]) == "1a"
    assert ansible_native_concat(["1", "2", "a"]) == "12a"
    assert ansible_native_concat(["True"]) is True
    assert ansible_native_concat(["False"]) is False
    assert ansible_native_concat(["True"]) == "True"

# Generated at 2022-06-22 12:04:11.851165
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.template.template import Template
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    loader.set_vault_secrets(['test_secret'])

# Generated at 2022-06-22 12:04:20.977196
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:04:30.997159
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['test']) == 'test'
    assert ansible_native_concat(['test', 'test2']) == 'testtest2'
    assert ansible_native_concat(['test', 1]) == 'test1'
    assert ansible_native_concat([1, 'test']) == '1test'
    assert ansible_native_concat(['true']) == 'true'
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1.0']) == 1.0
    assert ansible_native_concat(['[1,2,3]']) == [1, 2, 3]

# Generated at 2022-06-22 12:04:35.945604
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    raw = 'a b'
    jinja_text = NativeJinjaText(raw, keep_trailing_newline=False)
    ansible_text = AnsibleVaultEncryptedUnicode(raw, keep_trailing_newline=False)
    assert raw == ansible_native_concat([raw])
    assert jinja_text == ansible_native_concat([jinja_text])
    assert ansible_text == ansible_native_concat([ansible_text])
    assert raw == ansible_native_concat([ansible_text, raw])
    assert jinja_text == ansible_native_concat([ansible_text, jinja_text])
    assert ansible_text == ansible_native_concat([ansible_text, ansible_text])

# Generated at 2022-06-22 12:04:51.023872
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Unevaluatable(object):
        def __unicode__(self):
            return u'<Unevaluatable>'
    example = {'a': ['b', Unevaluatable()]}

    res = ansible_native_concat([example])
    assert example == res, \
        'ansible_native_concat returned %s instead of %s' % (res, example)

    res = ansible_native_concat([u'{"a": ', example, u'}'])
    assert example == res, \
        'ansible_native_concat returned %s instead of %s' % (res, example)

    res = ansible_native_concat([u'{"a": [', u'b', u', ', example, u'}'])

# Generated at 2022-06-22 12:04:59.055510
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar', 1]) == 'foobar1'
    assert ansible_native_concat([1, 'foo', 'bar']) == '1foobar'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(["'foo'"]) == "'foo'"
    assert ansible_native_concat(['foo', '"bar"']) == 'foo"bar"'



# Generated at 2022-06-22 12:05:09.362090
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # AnsibleVaultEncryptedUnicode
    data1 = AnsibleVaultEncryptedUnicode('test')
    output1 = ansible_native_concat(data1)
    assert output1 == 'test'

    # NativeJinjaText
    data2 = NativeJinjaText('test')
    output2 = ansible_native_concat(data2)
    assert output2 == 'test'

    # boolean types
    data3 = False
    output3 = ansible_native_concat(data3)
    assert output3 == False

    # dict type
    data4 = dict(a = 1, b = 2)
    output4 = ansible_native_concat(data4)
    assert output4 == dict(a = 1, b = 2)

    # list type

# Generated at 2022-06-22 12:05:22.486200
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2.runtime import Context
    from jinja2.nodes import List, Const, Name

    def join_list(node_list):
        return ansible_native_concat([v.as_const(Context()) for v in node_list])

    assert u'1 2' == join_list([List([Const(1), Const(2)])])
    assert u'1text2' == join_list([Const(u'1'), List([Const(u'text')]), Const(2)])
    assert u'1text2' == join_list([Const(u'1'), Const(u'text'), Const(2)])
    assert u'1Hello2' == join_list([Const(u'1'), Const(u'Hello'), Const(2)])

# Generated at 2022-06-22 12:05:34.389299
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.dumper import ansible_representer
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # a string
    assert ansible_native_concat("a") == "a"
    assert ansible_native_concat(u'a') == u'a'

    # a native python type
    assert ansible_native_concat(1) == 1
    assert ansible_native_concat(1.1) == 1.1
    assert ansible_native_concat(True) is True
    assert ansible_native_concat(False) is False
    assert ansible_native_concat(None) is None
    assert ansible_native_con

# Generated at 2022-06-22 12:05:45.095728
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([])) is None
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat(iter([u'a'])) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat(iter([u'a', u'b'])) == u'ab'
    assert ansible_native_concat([u'a', u'b', u'c', u'd']) == u'abcd'
    assert ansible_native_concat(iter([u'a', u'b', u'c', u'd'])) == u'abcd'
    assert ansible

# Generated at 2022-06-22 12:05:51.736171
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['test']) == 'test'
    assert ansible_native_concat(['{"test"}']) == {"test"}
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, [2, 3]]) == '1[2, 3]'
    assert ansible_native_concat([1, (2, 3)]) == '1(2, 3)'

# Generated at 2022-06-22 12:06:01.603097
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test for concat for two value with native type
    a = ansible_native_concat(['foo', 10])
    assert a == 'foo10'

    # Test for concat for two value with native type but one value is jinja2 text object
    from jinja2.utils import Markup
    b = ansible_native_concat([Markup('foo'), 10])
    assert b == 'foo10'

    # Test for concat for one value with native type
    c = ansible_native_concat([10])
    assert c == 10

    # Test for concat for three value with native type
    d = ansible_native_concat(['1', 2, 3])
    assert d == 123

    # Test for concat is jinja2 text object
    from jinja2.utils import Markup


# Generated at 2022-06-22 12:06:09.088890
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # ValueError: need more than 0 values to unpack
    # SyntaxError: invalid syntax
    # MemoryError: out of memory
    for error in (ValueError, SyntaxError, MemoryError):
        try:
            assert ansible_native_concat([]) is None
        except error:
            assert False, '{} should not be raised on an empty list'.format(error)

        try:
            assert ansible_native_concat([error]) is error
        except error:
            assert False, '{} should not be raised on a single item'.format(error)

        try:
            assert ansible_native_concat([error, error]) is error
        except error:
            assert False, '{} should not be raised on two different items'.format(error)


# Generated at 2022-06-22 12:06:19.749651
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # TODO: placeholder; not really unit tests, just demonstrate how the
    # function works

    from jinja2 import Environment, Template
    env = Environment(extensions=['jinja2.ext.do'])
    env.filters.update({
        'ansible_native_concat': ansible_native_concat,
    })
    env.globals.update({
        'to_text': to_text
    })


# Generated at 2022-06-22 12:06:37.522102
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:06:47.782475
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    result = ansible_native_concat(['value'])
    assert isinstance(result, text_type)
    assert result == 'value'

    result = ansible_native_concat(['value', 'value'])
    assert isinstance(result, text_type)
    assert result == 'valuevalue'

    result = ansible_native_concat([10])
    assert isinstance(result, int)
    assert result == 10

    result = ansible_native_concat([10, 10])
    assert isinstance(result, text_type)
    assert result == '1010'


# Generated at 2022-06-22 12:06:59.526725
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from collections import namedtuple
    from ansible.module_utils.common.text.converters import to_text

    class Undefined(object):
        def __call__(self, *args, **kwargs):
            raise RuntimeError('dummy exception')
    undefined = Undefined()

    # string is passed as is (no change)
    assert u'a string' == ansible_native_concat((u'a string',))

    # dict is passed as is (no change)
    assert {u'a': 1} == ansible_native_concat(({u'a': 1},))

    # list is passed as is (no change)
    assert [u'a string'] == ansible_native_concat(([u'a string'],))

    # undefined is passed as is (no change)
    assert undefined == ans

# Generated at 2022-06-22 12:07:11.278559
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # This test is to ensure we are getting the correct output for
    # ansible_native_concat.

    # Test for AnsibleVaultEncryptedUnicode
    out = ansible_native_concat([AnsibleVaultEncryptedUnicode(b'foo')])
    assert out == b'foo'

    # Test for NativeJinjaText
    # The test case 'i.e {{ foo }}' is to ensure that we are always
    # returning back string when the output is NativeJinjaText.
    # This test case covers https://github.com/pallets/jinja/issues/1200
    # https://github.com/ansible/ansible/issues/70831#issuecomment-664190894
    out = ansible_native_concat([NativeJinjaText('{{ foo }}')])

# Generated at 2022-06-22 12:07:18.044102
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # data:
    # - [1, 2, 3]
    # - [4, 5, 6]
    # - [7, 8, 9]
    nodes = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert ansible_native_concat(nodes) == nodes

    # data: "{% set _v=False %}{{ _v|int }}"
    nodes = [False]
    assert ansible_native_concat(nodes) == 0

    # data: "{% set _v=True %}{{ _v|int }}"
    nodes = [True]
    assert ansible_native_concat(nodes) == 1

    # data: "{% set _v=7 %}{{ _v|int }}"
   

# Generated at 2022-06-22 12:07:28.934152
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2.nodes import Call, List
    from jinja2.nodes import Name, Const

    const = Const(1)
    const2 = Const(2)
    const3 = Const(AnsibleVaultEncryptedUnicode(b'foo'))
    const4 = Const(AnsibleVaultEncryptedUnicode(b'bar'))
    list_ = List([const, const2, const3])
    name = Name('ansible_native_concat', 'load')
    func = Call(name, [list_], [], None, None)
    assert ansible_native_concat(func.generate()) == [1, 2, const3]

    const5 = Const(5)
    list_ = List([const5, const4])

# Generated at 2022-06-22 12:07:40.779829
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'

    assert len(ansible_native_concat(['foo', 'bar', []])) == 2
    assert len(ansible_native_concat(['foo', 'bar', ['foo', 'bar']])) == 4

    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['0b1101', '0b1', '0b1']) == 0b11011

    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_

# Generated at 2022-06-22 12:07:51.627712
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template import Templar


# Generated at 2022-06-22 12:08:04.240404
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat([1, 2.0]) == '12.0'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(range(5)) == '01234'
    assert ansible_native_concat([1, [2, 3]]) == '[2, 3]'
    assert ansible_native_concat(['1', '2']) == '12'

# Generated at 2022-06-22 12:08:14.157407
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([123]) == 123
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([123, 456]) == 123456
    assert ansible_native_concat([123, 456, 789]) == 123456789
    assert ansible_native_concat(["a", "b", "c"]) == 'abc'
    assert ansible_native_concat(['"a"', "\'b\'", "c"]) == '"a"\'b\'c'
    assert ansible_native_concat(["a", "b", "c", 123, 456]) == 'abc123456'

# Generated at 2022-06-22 12:08:39.373627
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None

    # As in the name literal_eval, we only evaluate literals
    assert ansible_native_concat(['null']) == 'null'

    assert ansible_native_concat(['null', 'true']) == 'nulltrue'
    assert ansible_native_concat(['null', 'null']) == 'nullnull'

    # ast.literal_eval raises a value error when we give a string as input
    # ansible_native_concat uses ast.literal_eval before returning the value
    assert ansible_native_concat(['null']) == 'null'

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(1) == 1


# Generated at 2022-06-22 12:08:49.284469
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([to_text('foo')]) == 'foo'
    assert ansible_native_concat([to_text('foo'), to_text('bar')]) == 'foobar'
    assert ansible_native_concat([to_text('The {answer} is {what}')]) == 'The {answer} is {what}'
    assert ansible_native_concat([to_text(42)]) == 42
    assert ansible_native_concat([to_text(42), to_text(1)]) == '421'
    assert ansible_native_concat([to_text(True)]) is True
    assert ansible_native_concat([to_text(True), to_text(False)]) == 'TrueFalse'

   

# Generated at 2022-06-22 12:08:56.627698
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    input = [u'a', u'b', u'c']
    expected = u'abc'
    assert ansible_native_concat(input) == expected

    input = [u'a', 100]
    expected = u'a100'
    assert ansible_native_concat(input) == expected

    input = [u'a', 100, u'b']
    expected = u'a100b'
    assert ansible_native_concat(input) == expected

    input = [u'a', 100, 2.5]
    expected = u'a1002.5'
    assert ansible_native_concat(input) == expected


# Generated at 2022-06-22 12:09:08.334535
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['one']) == 'one'
    assert ansible_native_concat(['one', 'two']) == 'onetwo'
    assert ansible_native_concat(['1', '2']) == 3
    assert ansible_native_concat(['foo ', 'bar', ' baz']) == 'foo bar baz'
    assert ansible_native_concat(['foo ', 'bar', '', ' baz']) == 'foo bar baz'
    assert ansible_native_concat(['a', ' ', 'b']) == 'a b'
    assert ansible_native_concat(['a', ' ', 'b', '{']) == 'a b{'
    assert ansible_native_concat

# Generated at 2022-06-22 12:09:18.755743
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Obj(object):
        def __add__(self, other):
            return other

    # Test with single values
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(iter([1])) == 1
    assert isinstance(ansible_native_concat(iter(["1"])), unicode)
    assert ansible_native_concat(iter(["1"])) == u"1"
    assert ansible_native_concat(iter(["1"])) == "1"
    assert isinstance(ansible_native_concat(iter([u"1"])), unicode)
    assert ansible_native_concat(iter([u"1"])) == u"1"
    assert ansible_native_concat(iter([u"1"])) == "1"

# Generated at 2022-06-22 12:09:58.824192
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:10.677924
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Check that
    # 1. NativeJinjaText is handled properly
    # 2. ansible_vault strings are handled properly
    # 3. any non-string values get returned as is
    # 4. otherwise, the result of `ast.literal_eval` is used
    nodes = [
        42,
        # Pallets/Jinja2#1200
        NativeJinjaText(container_to_text([u'foo', 42])),
        container_to_text([u'foo', 42]),
        AnsibleVaultEncryptedUnicode(u'{"key": 42}'),
    ]
    assert ansible_native_concat(nodes) == [42, NativeJinjaText(u'42'), [u'foo', 42], u'{"key": 42}']


# Generated at 2022-06-22 12:10:21.535777
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    _fail_on_undefined("foo")  # no exception is raised
    _fail_on_undefined(["foo", "bar"])  # no exception is raised
    _fail_on_undefined({'foo': 'bar'})  # no exception is raised

    # Test for https://github.com/ansible/ansible/issues/70831
    out = ansible_native_concat(["{{ foo }}"])
    assert isinstance(out, NativeJinjaText)
    assert out.value == u"{{ foo }}"

    # Test if literal_eval is not called for non-string types
    out = ansible_native_concat([None])
    assert out is None
    out = ansible_native_concat(["foo", "bar"])
    assert out == u"foobar"
    out = ans

# Generated at 2022-06-22 12:10:33.083720
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # Test that an undefined variable is properly raised (deferred)
    from jinja2.runtime import StrictUndefined
    strict_undefined = StrictUndefined('foo')
    try:
        ansible_native_concat([strict_undefined])
        assert False
    except UndefinedError:
        assert True

    # Test that literal_eval works with a single item
    assert ansible_native_concat([NativeJinjaText(123)]) is 123
    assert ansible_native_concat([NativeJinjaText('[1, 2, 3]')]) == [1, 2, 3]
    assert ansible_native_concat([NativeJinjaText('(1, 2, 3)')]) == (1, 2, 3)

# Generated at 2022-06-22 12:10:41.715706
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat(['42']) == 42
    assert ansible_native_concat(['42', '3.14', '.158']) == 4232.14158

# Generated at 2022-06-22 12:11:06.185980
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def assert_result(expected, *nodes):
        assert expected == ansible_native_concat(nodes)

    # Return None if nodes list is empty
    assert_result(None)

    # Return node value if list has only 1 node
    assert_result('foo', 'foo')
    assert_result(42, 42)

    # Return concatenation of strings if list has more than 1 node
    assert_result('foobar', 'foo', 'bar')

    # Return string created from sequence of nodes if they are not strings
    assert_result('[42 123]', [42, 123])

    # Return string if it can't be parsed with literal_eval
    assert_result('[42 123', '[42 123')

    # Return result of literal_eval parsing
    assert_result([42, 123], '[42 123]')

    # Return
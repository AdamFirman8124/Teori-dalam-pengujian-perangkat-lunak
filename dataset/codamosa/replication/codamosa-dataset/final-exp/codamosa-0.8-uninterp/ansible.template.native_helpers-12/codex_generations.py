

# Generated at 2022-06-22 12:01:14.028826
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native, to_bytes
    # Single node
    assert to_text(ansible_native_concat([1])) == "1"
    # Single node with spaces
    assert to_text(ansible_native_concat([u' '])) == " "
    # Single node with spaces, tabs and new lines
    assert to_text(ansible_native_concat([u'\n\t   '])) == "\n\t   "
    # Single node with spaces and tabs, followed by a string.
    assert to_text(ansible_native_concat([u'\n\t  ', 'hello'])) == "\n\t  hello"
    # Single node with spaces and tabs, followed by a string and a number.
    assert to_text

# Generated at 2022-06-22 12:01:26.274776
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment, meta, StrictUndefined, TemplateSyntaxError

    env = Environment(undefined=StrictUndefined, extensions=['jinja2.ext.do'])

    def test_eval_ast(template, expected, strict=True, trim_blocks=True, lstrip_blocks=True):
        t = Template(template, undefined=env.undefined, extensions=env.extensions)
        p = t.parse()
        assert len(p.find_undeclared_variables()) == 0
        if expected is TemplateSyntaxError:
            with pytest.raises(expected):
                ansible_native_concat(t.iter_expressions(t.parse()))
        else:
            ans_ev = ansible_native_concat(t.iter_expressions(t.parse()))


# Generated at 2022-06-22 12:01:37.864561
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # Test StrictUndefined handling
    assert ansible_native_concat([StrictUndefined('data')]) == 'data'
    assert ansible_native_concat([StrictUndefined('foo'), StrictUndefined('bar')]) == 'foobar'
    assert ansible_native_concat([StrictUndefined('foo'), StrictUndefined('bar')]) == 'foobar'
    assert ansible_native_concat([StrictUndefined('foo'), StrictUndefined('bar'), StrictUndefined('baz')]) == 'foobarbaz'

    # Test concatenation of strings
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'

    # Test

# Generated at 2022-06-22 12:01:50.665003
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # Call the function with a single argument
    assert ansible_native_concat([1]) == 1

    # Call the function with two arguments
    assert ansible_native_concat([1, 2]) == u'12'

    # Call the function with two arguments and one of them is a text
    assert ansible_native_concat([1, u'a']) == u'1a'

    # Call the function with a list of arguments
    assert ansible_native_concat([1, 2, 3]) == u'123'

    # Call the function with a list of arguments and a single argument
    assert ansible_native_concat(list(range(4))) == u'0123'

    # Call the function with a list of arguments and one of them is a text

# Generated at 2022-06-22 12:02:02.937254
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['', 'bar']) == 'bar'
    assert ansible_native_concat(['foo', '']) == 'foo'
    assert ansible_native_concat(['', '', '']) == ''
    assert ansible_native_concat(['123', '456']) == '123456'
    assert ansible_native_concat(['123', '456']) == '123456'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(['1', '2', '']) == '12'

# Generated at 2022-06-22 12:02:14.107112
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import pytest
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.text.converters import jsonify
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.template import Templar

    loader = AnsibleLoader(None, None)
    templar = Templar(loader=loader)


# Generated at 2022-06-22 12:02:26.160835
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat('1') == '1'
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat([1, 2, 3, 4]) == '1234'
    assert ansible_native_concat([[1, '2'], '3', [4, ['5', [6]]]]) == '123456'
    assert ansible_native_concat([1, [2, [3, 4]], '5']) == '12345'
    assert ansible_native_concat([1, 2]) == '12'

# Generated at 2022-06-22 12:02:34.042245
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # This is a test string with spaces and tabs
    s = "  abc\t"
    assert ansible_native_concat(s) == s
    assert ansible_native_concat([s]) == s
    assert ansible_native_concat([s, s]) == s * 2
    assert ansible_native_concat([s, s, s]) == s * 3

    assert ansible_native_concat([True]) == True
    assert ansible_native_concat([True, False]) == 'TrueFalse'
    assert ansible_native_concat([False, True]) == 'FalseTrue'

    assert ansible_native_concat([1, 2, 3]) == 6
    assert ansible_native_concat(["1", "2", "3"]) == "123"
    assert ansible_native_

# Generated at 2022-06-22 12:02:45.955416
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment
    import jinja2
    env = Environment()
    env.concat = ansible_native_concat

# Generated at 2022-06-22 12:02:58.078522
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(('a', 'b', 42)) == 'ab42'
    assert ansible_native_concat(str(i) for i in range(10)) == '0123456789'
    assert ansible_native_concat(str(i) for i in range(10)) == '0123456789'
    assert ansible_native_concat([42]) == 42
    assert ansible_native_concat(['1', 2, 3, 4]) == '1234'
    assert ansible_native_concat([text_type('a'), text_type('b')]) == text_type('ab')
    assert ansible_native_concat([b'a', b'b'])

# Generated at 2022-06-22 12:03:10.058645
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([b'foo']) == b'foo'
    assert ansible_native_concat([b'foo', b'bar']) == b'foobar'
    assert ansible_native_concat([u'foo']) == u'foo'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([container_to_text(u'foo')]) == u'foo'
    assert ansible_native_concat([container_to_text(u'foo'), container_to_text(u'bar')]) == u'foobar'
    assert ansible_native_concat([3]) == 3
    assert ansible_native_concat([3, 4]) == 34
    assert ansible_native_con

# Generated at 2022-06-22 12:03:20.954774
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import PY3

    assert ansible_native_concat(['string']) == 'string'
    assert ansible_native_concat(['string', ' other string']) == 'string other string'
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1' * int(1e8)]) == '1' * int(1e8)
    assert ansible_native_concat(['1', '2' * int(1e8)]) == '12' * int(1e8)

# Generated at 2022-06-22 12:03:31.989891
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.loader import AnsibleLoader

    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ansible_native_concat([1, 2, 3]) == 123

    assert ansible_native_concat([u'a', 1]) == u'a1'
    assert ansible_native_concat([1, u'a']) == u'1a'

    # list
    items = [u'a', u'b', u'c']

# Generated at 2022-06-22 12:03:42.068628
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert ansible_native_concat([]) is None

    assert ansible_native_concat([
        container_to_text([1, 2, 3]),
        container_to_text([4, 5, 6]),
        container_to_text([7, 8, 9]),
    ]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ansible_native_concat([
        container_to_text('{{ a }}, {{ b }}'),
        container_to_text('{{ c }}, {{ d }}'),
        container_to_text('{{ e }}, {{ f }}'),
    ]) == '{{ a }}, {{ b }}{{ c }}, {{ d }}{{ e }}, {{ f }}'


# Generated at 2022-06-22 12:03:51.298080
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(iter([])) is None

    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(iter([1])) == 1

    assert ansible_native_concat([123, 456]) == 123456
    assert ansible_native_concat(iter([123, 456])) == 123456

    assert ansible_native_concat([[]]) == []
    assert ansible_native_concat(iter([[]])) == []

    assert ansible_native_concat([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]

# Generated at 2022-06-22 12:04:00.346728
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Single value
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['foo']) == 'foo'

    # Multiple values
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['foo', 'bar', 'baz']) == 'foobarbaz'

    # Evaluable
    assert ansible_native_concat([1, ' + ', 2]) == 3
    assert ansible_native_concat(['foo', ' . ', 'bar']) == 'foo . bar'

    # Special string
    special_string = NativeJinjaText('foo')
    assert ansible_native_concat([special_string]) == 'foo'

    # String not evaluable
    # https://github.com/

# Generated at 2022-06-22 12:04:10.637993
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat([1, '2', '3']) == 1
    assert ansible_native_concat(['123', None, '4']) == '123None4'
    assert ansible_native_concat(['[1, 2 ,3]']) == [1, 2, 3]
    assert ansible_native_concat(['{"foo": 42, "bar": 50}']) == {"foo": 42, "bar": 50}
    assert ansible_native_concat(['"value" is 42 foo"bar']) == '"value" is 42 foo"bar'

# Generated at 2022-06-22 12:04:18.988777
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat((1, 2)) == 1
    assert ansible_native_concat(('a', 'b')) == 'ab'

    assert ansible_native_concat(('1', 2)) == 3
    assert ansible_native_concat(('1', '2')) == '12'

    assert ansible_native_concat(('a', 2)) == 'a2'
    assert ansible_native_concat(('a', '2')) == 'a2'

    assert ansible_native_concat(('1', '2', '3')) == '123'
    assert ansible_native_concat(('a', 'b', 'c')) == 'abc'



# Generated at 2022-06-22 12:04:29.402359
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1,2,3,4]) == '1234'
    assert ansible_native_concat(['a', 'bc', 'def']) == 'abcdef'
    assert ansible_native_concat(['a', [1, 2], 'def']) == 'a[1, 2]def'
    assert ansible_native_concat([{'a': {'b': 'c'}}, '1', '2']) == "{'a': {'b': 'c'}}12"
    assert ansible_native_concat('foo') == 'foo'
    assert ansible_native_concat(1) == 1
    assert ansible_native_concat([[1, 2], 3, [4, 5]]) == '[1, 2]34[4, 5]'

# Generated at 2022-06-22 12:04:36.917868
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    def native_concat(nodes):
        """Simplified version of ansible_native_concat without exception
        handling.
        """
        return ansible_native_concat((n.value for n in nodes))

    assert native_concat([]) is None
    assert native_concat([1]) == 1
    assert native_concat([1, 2]) == '12'
    assert native_concat(['1', '2']) == '12'
    assert native_concat([1, '2']) == '12'
    assert native_concat([1, True]) == '1true'
    assert native_concat([1, None]) == '1None'
    assert native_concat([True, 1]) == 'True1'
    assert native_concat([None, True]) == 'NoneTrue'
   
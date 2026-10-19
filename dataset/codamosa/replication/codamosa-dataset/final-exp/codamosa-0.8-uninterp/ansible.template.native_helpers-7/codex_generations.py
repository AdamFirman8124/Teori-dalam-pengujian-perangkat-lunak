

# Generated at 2022-06-22 12:01:14.114297
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['foo', 'bar']) == u'foobar'
    assert ansible_native_concat(['foo', 'bar', 1]) == u'foobar1'

    # literal_eval
    assert ansible_native_concat(['{', 'foo', ':', 'bar', '}']) == {'foo': 'bar'}
    assert ansible_native_concat(['[', '1', ',', '2', ']']) == [1, 2]
    assert ansible_native_concat(['1']) == 1

    # legacy behavior
    assert ansible_native_concat(['[', 'foo', ',', 'bar']) == u'[foo,bar'
    assert ansible_native_concat(['{', 'foo', ':', 'bar'])

# Generated at 2022-06-22 12:01:19.930845
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat(('1', 2)) == '12'
    assert ansibl

# Generated at 2022-06-22 12:01:32.377097
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.template.vars import AnsibleUnsafeText
    from ansible.template.vars import AnsibleUnsafeBytes
    from ansible.template.vars import AnsibleUnsafeNativeTypes
    from jinja2.nativetypes import string_concat

    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["foo"]) == "foo"

    assert ansible_native_concat([AnsibleUnsafeText("foo")]) == "foo"
    assert ansible_native_concat([AnsibleUnsafeBytes("foo")]) == "foo"
    assert ansible_native_concat([AnsibleUnsafeNativeTypes("foo")]) == "foo"

    assert ansible_native_concat([1, 2, 3]) == "123"
    assert ansible_

# Generated at 2022-06-22 12:01:42.242913
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def assert_type(value, expected):
        assert isinstance(value, expected), (
            '{!r} (type={}) is not instance of the expected type: {}'.format(
                value, type(value), expected))

    text = ansible_native_concat([to_text(1), to_text(2)])
    assert_type(text, text_type)
    assert text == '12'

    text = ansible_native_concat([[1], [2]])
    assert_type(text, list)
    assert text == [1, 2]

    text = ansible_native_concat([(1,), (2,)])
    assert_type(text, tuple)
    assert text == (1, 2)


# Generated at 2022-06-22 12:01:54.141813
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.cli.arguments import get_valid_file
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    filters = loader.load(get_valid_file('/dev/null'), True)

    # test_simple
    assert ansible_native_concat([b'a']) == 'a'
    assert ansible_native_concat([b'a', b'b']) == 'ab'
    assert ansible_native_concat([b'a', b'b', b'c']) == 'abc'
    # test_parse_string
    assert ansible_native_concat([b'True']) is True
    assert ansible_native_concat([b'False']) is False

# Generated at 2022-06-22 12:02:06.283732
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['hello', ' ', 'world']) == 'hello world'
    assert ansible_native_concat(['1', '+', '1', '=', '2']) == '1+1=2'
    assert ansible_native_concat([1, '+', 2, '=', 3]) == '1+2=3'
    assert ansible_native_concat([[1], '+', 2, '=', 3]) == '1+2=3'
    assert ansible_native_concat([1, '+', [2], '=', 3]) == '1+2=3'
    assert ansible_native_concat([1, '+', 2, '=', [3]]) == '1+2=3'

# Generated at 2022-06-22 12:02:16.081272
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == 1
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat([True, False]) is True
    assert ansible_native_concat([1, 'b', True]) == '1bTrue'
    assert ansible_native_concat([1, 'b', True, StrictUndefined()]) is StrictUndefined()
    assert ansible_native_concat(container_to_text([1, 'b', True, StrictUndefined()])) is StrictUndefined()
    assert ansible_native_concat(['a', [1, 'b', True, StrictUndefined()]]) == 'a[1, \'b\', True, True]'
    assert ansible_native_concat

# Generated at 2022-06-22 12:02:27.695157
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class FakedNode(object):
        def __init__(self, value):
            self.value = value

        def __iter__(self):
            return iter([self])

        def __repr__(self):
            return 'FakedNode(%r)' % self.value

        def __str__(self):
            return self.value

        def __eq__(self, other):
            if isinstance(other, FakedNode):
                return self.value == other.value
            return self.value == other

        def __ne__(self, other):
            return not self.__eq__(other)

        def __add__(self, other):
            if isinstance(other, FakedNode):
                return FakedNode(self.value + other.value)
            return FakedNode(self.value + other)

       

# Generated at 2022-06-22 12:02:39.012617
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u' 1']) == ' 1'
    assert ansible_native_concat([u'1\t']) == '1\t'
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u'a']) == 'a'

    assert ansible_native_concat([u'1\n']) == '1\n'
    assert ansible_native_concat([u'1']) == 1


# Generated at 2022-06-22 12:02:50.436323
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # A single string
    assert ansible_native_concat(['a']) == 'a'
    # A single non-string
    assert ansible_native_concat([None]) is None
    # Two strings
    assert ansible_native_concat(['a', 'b']) == 'ab'
    # Concat of a boolean and an int
    assert ansible_native_concat([True, 42]) == 'True42'
    # A string that should evaulate to a dict literal
    assert ansible_native_concat([("{'a': 'A', 'b': 'B', 'c': 'C'}")]) == {'a': 'A', 'b': 'B', 'c': 'C'}
    # A string that should evaulate to a list literal

# Generated at 2022-06-22 12:03:04.302370
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment, DictLoader
    from jinja2.exceptions import UndefinedError

    env = Environment(undefined=StrictUndefined, loader=DictLoader({}))
    env.filters.update({'ansible_native_concat': ansible_native_concat})

    # variables are evaluated lazily so we cannot use dicts or lists,
    # they will be evaluated by "| ansible_native_concat" and we won't
    # get UndefinedError. Thus use a generator instead.
    def generate_dict():
        while True:
            yield {'key': 'value'}

    def generate_list():
        while True:
            yield [1, 2, 3]

    def generate_undefined():
        while True:
            yield undefined

    # Test that a dictionary is evaluated laz

# Generated at 2022-06-22 12:03:16.182137
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    nodes = ['A', 123, 1.23, True, False, None]
    result = ansible_native_concat(nodes)
    assert result == 'A123123TrueFalseNone'

    nodes = chain(['A', 123], [1.23, True], [False, None])
    result = ansible_native_concat(nodes)
    assert result == 'A1231.23TrueFalseNone'

    nodes = [[1, 2, 3], ['a', 'b', 'c']]
    result = ansible_native_concat(nodes)
    assert result == [[1, 2, 3], ['a', 'b', 'c']]

    nodes = ['A', 123, '[linux, windows]', 1.23, True, False, None]
    result = ansible_native_concat(nodes)
   

# Generated at 2022-06-22 12:03:25.710258
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import sys

    if sys.version_info >= (3, 8):
        # this test is a work-around for JINJA2-1221
        assert ansible_native_concat([None, "foo"]) == "foo"
    else:
        # this test is a work-around for JINJA2-1221
        assert ansible_native_concat([None, "foo"]) == None

    assert ansible_native_concat([3, "foo"]) == 3
    assert ansible_native_concat([3, True, "False"]) == '3TrueFalse'
    assert ansible_native_concat([3, True, ["foo", "bar"]]) == '3Truefoo bar'
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([None]) == None

# Generated at 2022-06-22 12:03:35.934999
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    data = [
        (None, None),
        ('string', 'string'),
        ('null', None),
        ('false', False),
        ('true', True),
        ('123', 123),
        ('123.4', 123.4),
        ('"str"', 'str'),
        ('["a", "b"]', ['a', 'b']),
    ]
    for s, expected in data:
        actual = ansible_native_concat([s])
        assert type(expected) == type(actual), "'%s' is '%s', expected '%s'" % (s, type(actual), type(expected))
        assert expected == actual, "'%s' is '%s', expected '%s'" % (s, actual, expected)



# Generated at 2022-06-22 12:03:47.388328
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['ab', 'cd']) == u'abcd'
    assert ansible_native_concat(['ab', 1]) == u'ab1'
    assert ansible_native_concat([1, 'cd']) == u'1cd'
    assert ansible_native_concat([1, 2, 3]) == u'123'
    assert ansible_native_concat([1, 'ab', 2]) == u'1ab2'
    assert ansible_native_concat([u'ab', u'cd']) == u'abcd'
    assert ansible_native_concat(u'abcd') == u'abcd'
    assert ansible_native_concat(u'ab1') == u'ab1'

# Generated at 2022-06-22 12:03:59.254711
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['', 'b', 'c']) == 'bc'
    assert ansible_native_concat(['f', 'o', 'o', '', 'b', 'a', 'r']) == 'foobar'
    assert ansible_native_concat(['a', '', '', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 5]) == 'a5'
    assert ansible_native_concat([5, 'a']) == '5a'
    assert ansible_native_concat([5]) == 5
    assert ansible

# Generated at 2022-06-22 12:04:09.471969
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['1.0', '2.0', '3.0']) == 1.0
    assert ansible_native_concat(['1.0', 'foo', '1']) == u'1.0foo1'
    assert ansible_native_concat(['1.0', 'foo', '1', 'bar', '2']) == u'1.0foo1bar2'

# Generated at 2022-06-22 12:04:21.606989
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2

    env = jinja2.Environment()
    env.filters['to_text'] = to_text

    env.tests['literal'] = lambda value: not isinstance(value, StrictUndefined)


# Generated at 2022-06-22 12:04:32.393427
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # values which should not be evaluated
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['a', 3]) == 'a3'
    assert ansible_native_concat([3, 4]) == '34'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 3, 'c']) == 'a3c'
    assert ansible_native_concat([3, 'b', 'c']) == '3bc'
    assert ansible_native_concat(['a', 3, 5]) == 'a35'

# Generated at 2022-06-22 12:04:43.980501
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 6
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 2, 3, 'b']) == 'a23b'
    assert ansible_native_concat(['a', 'b', 'c', 1, 2, 3]) == 'abc123'
    assert ansible_native_concat([1, 'b', 'c', 2, 3, 'd']) == '1bc23d'
    assert ansible_native_concat(['a', None, 'b']) == u'anoneb'
    assert ansible_native_concat([None, 'b', 'c', None]) == u'NonebcNone'
    assert ansible_native_

# Generated at 2022-06-22 12:04:57.481630
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:05:08.586480
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # We have to import this function from the top level module.
    # It's not possible to import it from the inner scope because
    # `ast.literal_eval` does not import the same way on Python 2.
    # See: `library/pwd.py`.
    #
    # TODO remove this import when dropping Python2 support.
    from ansible.module_utils.common.text.converters import to_native

    AA = NativeJinjaText('foo')
    BB = NativeJinjaText('bar')
    CC = NativeJinjaText('baz')
    DD = NativeJinjaText('42')
    EE = NativeJinjaText('42.0')
    FF = NativeJinjaText('True')
    GG = NativeJinjaText('"foo"')
    HH = NativeJinjaText

# Generated at 2022-06-22 12:05:21.775924
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([1, [2, 3], 4]) == '1234'
    assert ansible_native_concat([1, [2, [3]], 4]) == '1234'
    assert ansible_native_concat(["1", "2", 3]) == '123'
    assert ansible_native_concat([1, {'a': 'b'}, 3]) == '1b3'
    assert ansible_native_concat([1, "2", 3]) == '123'
    assert ansible_native_concat(["1", "2", {"a": "b"}]) == '1b2'
    assert ansible_native_concat([1, 2, 3]) == '123'
   

# Generated at 2022-06-22 12:05:33.852509
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat((u'foo', u'bar')) == u'foobar'
    assert ansible_native_concat(['foo', 'bar']) == u'foobar'
    assert ansible_native_concat(['foo', 'bar']) == u'foobar'
    assert ansible_native_concat([['foo'], 'bar']) == [u'foo', u'bar']
    assert ansible_native_concat([['foo', 'bar']]) == [u'foo', u'bar']

# Generated at 2022-06-22 12:05:44.540276
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # pass
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat([1, 'a', 2, 'b', 3, 'c']) == [1, 'a', 2, 'b', 3, 'c']
    assert ansible_native_concat([1, {'a': 1}, 2, {'b': 2}, 3, {'c': 3}]) == [1, {'a': 1}, 2, {'b': 2}, 3, {'c': 3}]

# Generated at 2022-06-22 12:05:55.673667
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common.text.converters import to_list

    # Valid Python literal
    result = ansible_native_concat(['1', '2', '3'])
    assert result == [1, 2, 3]
    if PY3:
        assert isinstance(result, list)

    # Not a valid Python literal
    result = ansible_native_concat(['1', '2', '3', '4'])
    assert result == '1234'
    assert isinstance(result, text_type)

    result = ansible_native_concat(['True', 'False'])
    assert result == 'TrueFalse'
    assert isinstance(result, text_type)


# Generated at 2022-06-22 12:06:03.528690
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat(['1']) == '1'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', 2]) == '12'
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat([1, 2.0]) == '12.0'
    assert ansible_native_concat(['1', 2.0]) == '12.0'

# Generated at 2022-06-22 12:06:11.240288
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    try:
        from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    except ImportError:
        from ansible.parsing.unsafe_proxy import AnsibleUnsafeText

    assert container_to_text(ansible_native_concat([u'foo'])) == u'foo'

    assert ansible_native_concat([AnsibleUnsafeText("foo"),
                                  AnsibleUnsafeText("bar")]) == u'foobar'

    assert ansible_native_concat([AnsibleUnsafeText("foo "),
                                  AnsibleUnsafeText("bar")]) == u'foo bar'

    assert ansible_native_concat([AnsibleUnsafeText("foo "),
                                  AnsibleUnsafeText(" bar")]) == u'foo  bar'

    assert container_to_text

# Generated at 2022-06-22 12:06:21.993703
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # https://github.com/pallets/jinja/blob/master/tests/test_concat.py
    from ansible.module_utils.common.text.converters import to_bytes

    # an actual jinja2 environment object isn't needed for these tests
    def _render(value):
        return ansible_native_concat((value,))

    assert _render(None) is None
    assert _render('foo') == 'foo'
    assert _render('f') == 'f'
    assert _render(b'foo') == b'foo'
    assert _render('f') == 'f'
    assert _render(42) == 42
    assert _render(42.5) == 42.5
    assert _render(True) is True
    assert _render(False) is False

# Generated at 2022-06-22 12:06:33.918473
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 3]) == 123
    assert ansible_native_concat([]) == None

    assert ansible_native_concat(['abc', 123]) == 'abc123'
    assert ansible_native_concat(['abc', 123, 1.01]) == 'abc1231.01'
    assert ansible_native_concat(['abc', 123, 1.01, False]) == 'abc1231.01False'
    assert ansible_native_concat(['abc', 123, 1.01, False, None]) == 'abc1231.01FalseNone'

# Generated at 2022-06-22 12:06:49.110812
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:07:01.030634
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class _Undefined(StrictUndefined):
        def __str__(self):
            raise ValueError('undefined')

    undefined = _Undefined()

    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat([1, undefined]) == 1
    assert ansible_native_concat([1, 2, undefined]) == 1
    assert ansible_native_concat([undefined, 2]) == 2
    assert ansible_native_concat(list(range(50000))) == container_to_text(range(50000))
    assert ansible_native_concat(list(range(50000)), undefined) == container_to_text(range(50000))

# Generated at 2022-06-22 12:07:12.378171
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    _fail_on_undefined = _fail_on_undefined
    ansible_native_concat = ansible_native_concat
    eval_literal = ast.literal_eval

    # Tests if fail_on_undefined will properly raise Jinja2's
    # StrictUndefined exception when it's in the data structure.
    def test_strict_undefined_exception_in_data():
        message = 'test raises strict undefined exception'
        foobar = StrictUndefined(message)
        try:
            _fail_on_undefined(foobar)
        except StrictUndefined as e:
            assert e.message == message
        else:
            raise Exception('Should have raised a StrictUndefined exception')

    test_strict_undefined_exception_in_data()

    # Tests if fail_

# Generated at 2022-06-22 12:07:21.625835
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat([u'\U0001F4A9', u'\U0001F4A9']) == u'\U0001F4A9\U0001F4A9'
    assert ansible_native_concat([[1, 2, 3], [1, 2, 3]]) == '123123'
    assert ansible_native_concat({'a': 'b'}) == 'b'
    assert ansible_native_concat(['a', 1, {'a': 'b'}, [1, 2, 3]]) == 'a1b123'

# Generated at 2022-06-22 12:07:29.689636
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat("") is None
    assert ansible_native_concat("abc") == "abc"
    assert ansible_native_concat("1") == 1
    assert ansible_native_concat("1.0") == 1.0
    assert ansible_native_concat("1+1") == "1+1"
    assert ansible_native_concat("1", "2") == "12"
    assert ansible_native_concat("1", "2", "3") == "123"
    assert ansible_native_concat(1, 2, 3) == "123"
    assert ansible_native_concat(1, 2, 3) == "123"
    assert ansible_native_concat(True, False, True) == "TrueFalseTrue"
    assert ansible_

# Generated at 2022-06-22 12:07:41.299723
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', 'b', 42]) == 'ab42'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['1', '2', 'three']) == '12three'
    assert ansible_native_concat([1, 2, 3]) == 6
    assert ansible_native_concat(['yes', 'no']) == 'yesno'
    assert ansible_native_concat(['yes', 'no']) == 'yesno'
    assert ansible_native_concat(['yes', [1, 2, 3]]) == 'yes[1, 2, 3]'
    assert ansible

# Generated at 2022-06-22 12:07:51.936539
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ansible_native_concat(u'abc') == u'abc'
    assert ansible_native_concat(1) == 1
    assert ansible_native_concat([1, u'b', u'c']) == u'1bc'
    assert ansible_native_concat([u'a', 1, u'c']) == u'a1c'
    assert ansible_native_concat([u'a', u'b', 1]) == u'ab1'
    assert ansible_native_concat(['a', 1, u'c']) == u

# Generated at 2022-06-22 12:08:04.463681
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'test']) == u'test'
    assert ansible_native_concat([u'foo', u'bar']) == u'foobar'
    assert ansible_native_concat([u'test', u'bar', 1]) == u'testbar1'
    assert ansible_native_concat([u'foo', 1, u'bar']) == u'foo1bar'
    assert ansible_native_concat([u'foo', 1, None, 3.14]) == u'foo1None3.14'
    assert ansible_native_concat(u'test') == u'test'
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([False]) is False
    assert ansible_native_concat([None])

# Generated at 2022-06-22 12:08:14.409490
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([u'1']) == 1
    assert ansible_native_concat([u'1', u'2']) == 12
    assert ansible_native_concat([u'1', u'2', u'3']) == u'123'
    assert ansible_native_concat([u'1', u'2', u'3.0']) == u'123.0'
    assert ansible_native_concat([u'1', u'2', u'3.0', u'4']) == u'123.04'

    assert ansible_native_concat(m for m in [u'1', u'2', u'3.0']) == u'123.0'

# Generated at 2022-06-22 12:08:26.075259
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def parse(nodes):
        parsed = ansible_native_concat(nodes)
        if isinstance(parsed, string_types):
            return parsed
        else:
            return container_to_text(parsed, prefer_unicode=True)

    assert parse([]) is None
    assert parse([u'a']) == u'a'
    assert parse((u'a', u'b')) == u'ab'
    assert parse([u'a', u'b', u'c']) == u'abc'
    assert parse([u'a', u'b', u'c', u'd', u'e', u'f']) == u'abcdef'
    assert parse([u'a' * 8]) == u'a' * 8

# Generated at 2022-06-22 12:08:45.503041
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:08:57.179978
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([{'foo': 'bar'}]) == {'foo': 'bar'}
    assert ansible_native_concat([[1, 2, 3]]) == [1, 2, 3]
    assert ansible_native_concat(['bar']) == 'bar'
    assert ansible_native_concat(['42']) == 42
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat(['false']) is False
    assert ansible_native_concat(['baz', 'foo', 'bar']) == 'bazfoobar'
    assert ansible_native_concat(['concat', ' ', 'strings']) == 'concat strings'



# Generated at 2022-06-22 12:09:08.832427
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test it with a dictionary as input.
    expected = {
        "a": {
    	    "b": {
    	        "c": "d"
    	    }
        },
        "e": {
            "f": {
                "g": "h"
            }
        }
    }
    actual = ansible_native_concat([
        {
            "a": {
                "b": {
                    "c": "d"
                }
            },
            "e": {
                "f": {
                    "g": "h"
                }
            }
        }
    ])
    assert actual == expected

    # Test it with a list as input.

# Generated at 2022-06-22 12:09:19.414580
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(()) is None
    assert ansible_native_concat((1,)) == 1
    assert ansible_native_concat(('true',)) is True
    assert ansible_native_concat(('3',)) == 3
    assert ansible_native_concat(('3', '.')) == '3.'
    assert ansible_native_concat((0, '1', '2')) == '012'
    assert ansible_native_concat((None, '1')) == '1'
    assert ansible_native_concat((None, None)) is None
    assert ansible_native_concat(('a', None)) == 'a'
    assert ansible_native_concat(('"',)) == '"'
    assert ansible_native_concat((u'"',))

# Generated at 2022-06-22 12:09:58.982379
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:10.716640
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    ast.literal_eval(None)  # Quiet flake8 unused import
    assert ansible_native_concat('') == ''
    assert ansible_native_concat('1') == 1
    assert ansible_native_concat(' 1 ') == 1
    assert ansible_native_concat('1 2') == '1 2'
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(i for i in ['1', '2', '3']) == '123'
    assert ansible_native_concat(['1', [], '2', '3'])

# Generated at 2022-06-22 12:10:21.535003
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None


# Generated at 2022-06-22 12:10:33.035161
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == u'12'
    assert ansible_native_concat(['1', 2]) == u'12'
    assert ansible_native_concat(['1', 2.0]) == u'12.0'
    assert ansible_native_concat([1, '2']) == u'12'
    assert ansible_native_concat([1, u'2']) == u'12'
    assert ansible_native_concat([u'1', '2']) == u'12'
    assert ansible_native_concat([u'1', u'2']) == u'12'

# Generated at 2022-06-22 12:10:41.717396
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['1', '2', '3']) == '123'
    assert ansible_native_concat(['1', '2', '3', '4', '5', '6']) == '123456'
    assert ansible_native_concat(u'abc') == u'abc'
    assert ansible_native_concat(u'abc', u'def') == u'abcdef'
    assert ansible_native_concat(u'abc', u'def', u'ghi') == u'abcdefghi'
    assert ansible_native_concat(u'abc', u'def', u'ghi', u'jkl') == u'abcdefghijkl'

# Generated at 2022-06-22 12:10:53.373375
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['abc', 'def']) == 'abcdef'
    assert ansible_native_concat(['abc', 'def123']) == 'abcdef123'
    assert ansible_native_concat(['123', 'def']) == '123def'
    assert ansible_native_concat([123, 'def']) == '123def'
    assert ansible_native_concat([123, 456]) == '123456'
    assert ansible_native_concat([1.23, 456]) == '1.23456'
    assert ansible_native_concat([None, 456]) == 'None456'
    assert ansible_native_concat(['None', 456]) == 'None456'
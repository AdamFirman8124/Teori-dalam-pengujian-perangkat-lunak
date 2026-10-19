

# Generated at 2022-06-22 12:01:13.728704
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', '1']) == 'a1'
    assert ansible_native_concat(['a', 1]) == 'a1'
    assert ansible_native_concat(['a', True]) == 'aTrue'
    assert ansible_native_concat([True, 'b']) is True
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([]) is None

# Generated at 2022-06-22 12:01:25.987239
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat((u'foo', u'bar')) == u'foobar'
    assert ansible_native_concat((u'foo', u'bar', u'qux')) == u'foobarqux'
    assert ansible_native_concat((u'foo', u'', u'bar')) == u'foobar'
    assert ansible_native_concat((u'', u'foo', u'bar')) == u'foobar'
    assert ansible_native_concat((u'foo', u'bar', u'')) == u'foobar'
    assert ansible_native_concat((u'', u'foo', u'bar', u'')) == u'foobar'
    assert ansible_native_concat((u'foo', u'12.34')) == u

# Generated at 2022-06-22 12:01:37.656600
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['str']) == 'str'
    assert ansible_native_concat(['str', 'ing']) == 'string'
    assert ansible_native_concat([123, 'string']) == 123

    v = AnsibleVaultEncryptedUnicode('foo')
    assert ansible_native_concat([v]) == 'foo'

    # when there are undefined variables
    u = StrictUndefined('undefined')
    assert ansible_native_concat([u, 'string']) == 'string'
    assert ansible_native_concat(['string', u]) == 'string'

    # test ansible_native_concat with a generator, eg. from itertools.chain
    assert ansible_native_con

# Generated at 2022-06-22 12:01:50.362586
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat(['']) == ''
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['1']) == 1
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', '2']) == '12'
    assert ansible_native_concat(['1', u'2']) == '12'
    assert ansible_native_concat([1, 2]) == '12'

# Generated at 2022-06-22 12:02:02.629401
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, 'a', 2]) == '1a2'
    assert ansible_native_concat(['a', 1, 2]) == 'a12'
    assert ansible_native_concat([1, 'a', 'b', 2]) == '1ab2'
    assert ansible_native_concat(['a', 1, 'b', 2]) == 'a1b2'
    assert ansible_native_concat([1, 'a', 2, 'b']) == '1a2b'

# Generated at 2022-06-22 12:02:13.856641
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([NativeJinjaText(u'foo')]) == u'foo'
    assert ansible_native_concat([u'{{', NativeJinjaText(u'foo'), u'}}']) == u'{{foo}}'
    assert ansible_native_concat([u'{{', NativeJinjaText(u'foo'), u' | string }}']) == u'foo'
    assert ansible_native_concat([u'{{', NativeJinjaText(u'foo'), u'}}']) == u'{{foo}}'

    assert ansible_native_concat([NativeJinjaText(u'foo'), NativeJinjaText(u'bar')]) == u'foobar'

# Generated at 2022-06-22 12:02:26.159185
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert (ansible_native_concat(['a', 'b']) ==
            'a' + ansible_native_concat(['b']))

    assert ansible_native_concat({'b': 1, 'a': 2}) == {'b': 1, 'a': 2}

    assert ansible_native_concat(['b', 1, 'a', 2]) == ['b', 1, 'a', 2]

    assert ansible_native_concat([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]

    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat([1]) == 1
    assert isinstance(ansible_native_concat({'a': 1}), dict)

# Generated at 2022-06-22 12:02:34.041159
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Literal eval examples
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1.5, 2.5, 3.5]) == [1.5, 2.5, 3.5]
    assert ansible_native_concat([1, 2.5, 3.5]) == [1, 2.5, 3.5]
    assert ansible_native_concat(['foo', 'bar', 'baz']) == ['foo', 'bar', 'baz']
    assert ansible_native_concat(['foo', '1', '2', 3.5]) == ['foo', '1', '2', 3.5]

# Generated at 2022-06-22 12:02:45.955683
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(["foo"]) == "foo"
    assert ansible_native_concat(["foo", "bar"]) == "foobar"
    assert ansible_native_concat(["foo", " bar "]) == "foo bar "
    assert ansible_native_concat(["foo", "123 ", "baz", "456", "xyz"]) == "foo123 baz456xyz"
    assert ansible_native_concat([[]]) == "[]"
    assert ansible_native_concat([["foo"]]) == "['foo']"
    assert ansible_native_concat(["foo", ["bar", "baz"]]) == "foo['bar', 'baz']"

# Generated at 2022-06-22 12:02:54.598513
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == 'ab'
    assert ansible_native_concat(['5']) == 5
    assert ansible_native_concat(['5', '5']) == 55
    assert isinstance(ansible_native_concat([u'a']), text_type)
    assert isinstance(ansible_native_concat(['a', ' ']), text_type)
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'

    assert ansible_native_concat([5]) == 5

# Generated at 2022-06-22 12:02:59.847909
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test for string concatenation
    assert (ansible_native_concat(['abc', 'def']) == 'abcdef')
    # Test for variable + string concatenation
    assert (ansible_native_concat([container_to_text('abc'), 'def']) == 'abcdef')
    # Test for variable list + string concatenation
    assert (ansible_native_concat([container_to_text(['abc', 'def']), 'ghi']) == 'abcdefghi')
    # Test for list creation
    assert (ansible_native_concat([['abc', 'def'], ['ghi', 'jkl']]) == ['abc', 'def', 'ghi', 'jkl'])
    # Test for dict creation

# Generated at 2022-06-22 12:03:10.542624
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native

    class _StrictUndefined(StrictUndefined):
        def __str__(self):
            raise StrictUndefined('undefined value')

    class Test(object):
        def __str__(self):
            return 'a'

    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['a']) == u'a'
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([to_native('a')]) == u'a'
    assert ansible_native_concat([Test()]) == u'a'
    assert ansible_native_concat(['a', 'b']) == u'ab'
   

# Generated at 2022-06-22 12:03:21.313123
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['abc']) == 'abc'
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2, 'c']) == '1, 2, c'
    assert ansible_native_concat([1, 2, 'c']) == '1, 2, c'
    assert ansible_native_concat([1, 2, '"quoted"']) == '1, 2, "quoted"'
    assert ansible_native_concat([1, 2, 'c']) == '1, 2, c'
    assert ansible_native_concat([1, 2, 'c']) == '1, 2, c'

# Generated at 2022-06-22 12:03:32.566495
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Base case
    assert ansible_native_concat(list(zip(range(5)))) == 0
    assert ansible_native_concat(list(zip(range(1)))) == 0
    assert ansible_native_concat([]) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([False]) is False

    # Test "nodes" which is not an iterable
    with pytest.raises(TypeError):
        ansible_native_concat(None)

    # Non-string result
    assert ansible_native_concat([2, 3, 4]) == 5
    assert ansible_native_concat([1, None]) is None
    assert ansible_native_concat([None, 1]) is None

# Generated at 2022-06-22 12:03:42.365558
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['a', ['b', 'c'], 'd']) == 'abcd'
    assert ansible_native_concat([None, 'b', ['c', 'd']]) == 'bcd'
    assert ansible_native_concat([None, None]) is None

    assert ansible_native_concat(['1', '2', '3', '4']) == '1234'
    assert ansible_native_concat(['12', '34']) == '1234'
    assert ansible_native_concat(['1', 2, 3, '4']) == '1234'

# Generated at 2022-06-22 12:03:51.744288
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test to check the list of compiled nodes."""
    nodes = []
    ret = ansible_native_concat(nodes)
    assert None == ret

    nodes = ["this is a string"]
    ret = ansible_native_concat(nodes)
    assert "this is a string" == ret

    # ast.literal_eval is equivalent to int
    nodes = ["1234567890"]
    ret = ansible_native_concat(nodes)
    assert 1234567890 == ret

    # ast.literal_eval is equivalent to float
    nodes = ["12.3456789"]
    ret = ansible_native_concat(nodes)
    assert 12.3456789 == ret

    # ast.literal_eval is equivalent to bool
    nodes = ["true"]
    ret = ansible_native_

# Generated at 2022-06-22 12:04:03.204844
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText

    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, '2']) == '12'
    assert ansible_native_concat(map(lambda x: x, [1, '2'])) == '12'
    assert ansible_native_concat(map(lambda x: x, (1, '2'))) == '12'
    assert ansible_native_concat([1, ' 2', '3.4']) == '123.4'


# Generated at 2022-06-22 12:04:12.305644
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Test 1
    node = [1]
    ret = ansible_native_concat(node)
    assert ret == 1

    # Test 2
    node = [1, 2]
    ret = ansible_native_concat(node)
    assert ret == 12

    # Test 3
    node = [1, 2]
    ret = ansible_native_concat(node)
    assert ret == 12

    # Test 4
    node = [1, 2, 3]
    ret = ansible_native_concat(node)
    assert ret == 123

    # Test 5
    node = [1, 2, 3, 4]
    ret = ansible_native_concat(node)
    assert ret == 1234

    # Test 6
    node = [1, 2, 3, 4, 5]
    ret = ans

# Generated at 2022-06-22 12:04:21.257512
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Ensure compatibility with Python 3.7+'s ast.literal_eval
    # (which disallows leading whitespace)
    assert ansible_native_concat([' ']) == ' '
    assert ansible_native_concat([' ' * 8]) == ' ' * 8

    assert ansible_native_concat([]) is None

    assert ansible_native_concat([u'\u2026']) == u'\u2026'

    assert ansible_native_concat([' ']) == ' '
    assert ansible_native_concat(['']) == ''
    assert ansible_native_concat([' ' * 8]) == ' ' * 8
    assert ansible_native_concat([u'123']) == 123


# Generated at 2022-06-22 12:04:28.589391
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    class Test(object):
        def __str__(self):
            return "CONCAT"

    class Test2(object):
        def __unicode__(self):
            return "CONCAT"

    value = ansible_native_concat([1, 2, 3, 4, 5])
    assert isinstance(value, int)
    assert value == 12345

    value2 = ansible_native_concat([Test(), Test2(), 'CONCAT'])
    assert isinstance(value2, string_types)
    assert value2 == "CONCATCONCATCONCAT"

# Generated at 2022-06-22 12:04:44.128294
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """This function tests Python's ast.literal_eval on a set of string
    values from Ansible to validate that it does not cause exceptions to be
    raised.
    """
    import sys
    import os
    import tempfile

    if sys.version_info[:2] < (3, 5):
        print("This test requires Python 3.5 or greater.")
        return True

    # Make sure the test file is removed during the teardown
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_native_types')
    test_file_path = os.path.join(tmpdir, 'test_file')

# Generated at 2022-06-22 12:04:51.275326
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_text
    native = ansible_native_concat(['x', 'y', 1, 3.14, True, False, (1j,), [1], {'x': 1}, to_text('foo')])
    expected = container_to_text([
        'x', 'y', 1, 3.14, True, False, (1j,), [1], {'x': 1}, to_text('foo'),
    ])
    assert native == expected

# Generated at 2022-06-22 12:05:00.651816
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # the following strings are used to check that literal_eval is called
    # and decoding is done.
    # ['a', 'b', 'c']
    encoded_list = b"[u'a', u'b', u'c']"
    # {'a': 'b'}
    encoded_dict = b'{u\'a\': u\'b\'}'

    # make sure we are not getting exceptions from ansible_native_concat
    assert [None] == [ansible_native_concat(None)]
    # ['a', 'b', 'c']
    assert ansible_native_concat([encoded_list]) == [u'a', u'b', u'c']
    # ['a', 'b', 'c']

# Generated at 2022-06-22 12:05:04.946020
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat(['a']) == 'a'
    assert ansible_native_concat(['a', 'b']) == u'ab'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['A ', 'B']) == u'A B'
    assert ansible_native_concat([' A ', 'B']) == u' A B'
    assert ansible_native_concat([' A ', 'B ']) == u' A B '

# Generated at 2022-06-22 12:05:18.728934
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    undefined = StrictUndefined()
    native_jinja_text = NativeJinjaText()
    ansible_vault_encrypted_unicode = AnsibleVaultEncryptedUnicode(b'\x00\x01\x02')
    ansible_vault_encrypted_unicode_2 = AnsibleVaultEncryptedUnicode(b'\x03\x04\x05')

    assert ansible_native_concat([undefined]) == str(undefined)
    assert ansible_native_concat([native_jinja_text]) == str(native_jinja_text)
    assert ansible_native_concat([ansible_vault_encrypted_unicode]) == str(ansible_vault_encrypted_unicode)
    assert ansible_native_concat([1]) == 1
    assert ansible

# Generated at 2022-06-22 12:05:31.658796
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Test ansible_native_concat function"""

    # Test on literal values
    assert ansible_native_concat(['hello']) == 'hello'
    assert ansible_native_concat(['true']) is True
    assert ansible_native_concat(['false']) is False
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([0]) == 0

    # Test None
    assert ansible_native_concat([]) is None

    # Test concatenation of multiple literals
    assert ansible_native_concat(['hello ', 'world']) == 'hello world'
    assert ansible_native_concat(['hello ', 1, ' ', 'world']) == 'hello 1 world'

# Generated at 2022-06-22 12:05:42.666175
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # test empty list
    assert ansible_native_concat([]) is None

    # test a single value
    assert ansible_native_concat([42]) == 42

    # test concat values
    assert ansible_native_concat([42, u'fish']) == u'42fish'
    assert ansible_native_concat([u'fish', 42]) == u'fish42'
    assert ansible_native_concat([u'fish', True, u'wars']) == u'fishTruewars'
    assert ansible_native_concat([True, 42]) == u'True42'
    assert ansible_native_concat([42, False]) == u'42False'
    assert ansible_native_concat([u'fish', [42]]) == u'fish[42]'

    # test conc

# Generated at 2022-06-22 12:05:52.944563
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, u'+', 1]) == 2
    assert ansible_native_concat([1, u'+', u'1']) == 2
    assert ansible_native_concat([1, u'+', u'1.0']) == 2.0
    assert ansible_native_concat([u'True']) is True
    assert ansible_native_concat([u'False']) is False
    assert ansible_native_concat([u'data']) == u'data'
    assert ansible_native_concat([u'data', u'+', u'data']) == u'datadata'
    assert ansible_native_concat([u'[', u'data', u']']) == [u'data']

# Generated at 2022-06-22 12:06:00.068732
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(["a", 1, b"b"]) == "a1b"
    assert ansible_native_concat([[1, 2], 3]) == [1, 2, 3]
    assert ansible_native_concat(["a", 1, b"b"], keep_together=True) == "a1b"
    assert ansible_native_concat([[1, 2], 3], keep_together=True) == "12.3"
    assert ansible_native_concat([1, 2, 3], keep_together=True) == "123"



# Generated at 2022-06-22 12:06:10.335302
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([u'a']) == u'a'
    assert ansible_native_concat([u'a', u'b']) == u'ab'
    assert ansible_native_concat([u'a', u'b', u'c']) == u'abc'
    assert ansible_native_concat([u'a', 1]) == u'a1'
    assert ansible_native_concat([u'a', 1, u'b']) == u'a1b'
    assert ansible_native_concat([u'a', {'b': 1}]) == u"a{'b': 1}"

# Generated at 2022-06-22 12:06:24.375509
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.module_utils.common.text.converters import to_native
    import ansible.module_utils.common.text.converters as conv
    # test strings
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['42', 'foo', 'bar']) == '42foobar'
    assert ansible_native_concat(['42', '0o11', '0b10101']) == '42012'

    # test lists
    assert ansible_native_concat([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]

# Generated at 2022-06-22 12:06:36.510172
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    def check(values, expected, vaulted=False):
        nodes = [NativeJinjaText(unicode(v)) for v in values]
        if vaulted:
            # This mimics the actual Vault class
            nodes = [AnsibleVaultEncryptedUnicode(unicode(n), unicode(n)) for n in nodes]
        concated = ansible_native_concat(nodes)
        if is_sequence(expected):
            assert is_sequence(concated)
            assert all(a == b for a, b in zip_longest(concated, expected))
        else:
            assert concated == expected

    check(['foo', 'bar'], u'foobar')
    check(['foo', '', 'bar'], u'foobar')

    check([1, 2], [1, 2])

# Generated at 2022-06-22 12:06:46.802307
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Type: text
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([True]) is True
    assert ansible_native_concat([10]) == 10
    assert ansible_native_concat([u'foo bar']) == u'foo bar'
    assert ansible_native_concat([u'foo\tbar']) == u'foo\tbar'
    assert ansible_native_concat([u'\r']) == u'\r'

    # Type: int
    assert ansible_native_concat([u'10']) == 10

    # Type: float
    assert ansible_native_concat([u'1.0E+5']) == 100000.0

    # Type: complex

# Generated at 2022-06-22 12:06:58.519260
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    # Create an instance of the class to be able to call its methods
    test = globals()['test_ansible_native_concat']

    assert isinstance(ansible_native_concat([
        u'abc 123',
        u'def 456',
    ]), string_types)
    assert ansible_native_concat([
        u'abc 123',
        u'def 456',
    ]) == u'abc 123def 456'
    assert ansible_native_concat([
        u'abc 123',
        u'def 456',
    ]) == u'abc 123def 456'
    assert ansible_native_concat([
        u'abc 123',
        u'def 456',
    ]) == u'abc 123def 456'


# Generated at 2022-06-22 12:07:09.331995
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(['Hello', '', 'World']) == 'HelloWorld'
    assert ansible_native_concat(['1', '2', '3']) == 123
    assert ansible_native_concat(['"', '>', '|']) == '">|'
    assert ansible_native_concat([True, ' ', 'World']) == ' True World'
    assert ansible_native_concat([True, '', True]) == True
    assert ansible_native_concat([{'aaa': 'vvv'}, ' ', 'World']) == " {'aaa': 'vvv'} World"
    assert ansible_native_concat([[1, 2, 3], ' ', 'World']) == " [1, 2, 3] World"
    assert ansible_native_con

# Generated at 2022-06-22 12:07:19.813172
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2 import Environment
    env = Environment(extensions=['jinja2.ext.do'])
    env.globals['ansible_native_concat'] = ansible_native_concat

    tmpl = env.from_string(u"{{ [1, 2, '3'] }}")
    assert tmpl.render() == u'[1, 2, \'3\']'

    tmpl = env.from_string(u"{{ ansible_native_concat([1, 2, '3']) }}")
    assert tmpl.render() == u'[1, 2, \'3\']'

    tmpl = env.from_string(u"{{ ansible_native_concat([1, 2, '3']).0 }}")

# Generated at 2022-06-22 12:07:31.018438
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import unittest.mock as mock

    class MockNode:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

    class MockNodeGenerator:
        def __init__(self, values):
            self._values = iter(values)

        def __iter__(self):
            return self

        def __next__(self):
            return MockNode(next(self._values))

    with mock.patch('ansible.module_utils.common.text.converters.container_to_text') as ct:
        ct.side_effect = lambda x: str(x) + '+'

        # Test empty list
        assert ansible_native_concat([]) is None

        # Test single element list
        assert ansible

# Generated at 2022-06-22 12:07:39.775960
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    def _assert_native(value, expected):
        # literal_eval removes leading spaces/tabs from the string in Python
        # 3.10+ while it is not removed in Python 3.8 and 3.9.
       assert ansible_native_concat([value]) == expected

    _assert_native('1', 1)
    _assert_native([1, 2, 3], [1, 2, 3])
    _assert_native({'foo': 'bar'}, {'foo': 'bar'})
    _assert_native(True, True)
    _assert_native('1 2 3', [1, 2, 3])

# Generated at 2022-06-22 12:07:50.965602
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, 2, 3, 4, 5, 6, 7, 8]) == 12345678

# Generated at 2022-06-22 12:08:03.476493
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['']) is None
    assert ansible_native_concat([None]) is None
    assert ansible_native_concat([' ']) is None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '12'
    assert ansible_native_concat([1, 2, 3]) == '123'
    assert ansible_native_concat(['1', 2, 3]) == '123'
    assert ansible_native_concat([None, 'a', None, 'b', None, 'c', None]) == 'abc'
    assert ansible_native_concat([None, '1', None, 2, None, 3, None]) == '123'


# Generated at 2022-06-22 12:08:22.764625
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2, 3]) == 1
    assert ansible_native_concat([NativeJinjaText('a'), 'b', NativeJinjaText('c')]) == 'abc'
    assert ansible_native_concat([NativeJinjaText('a'), NativeJinjaText('b')]) == 'ab'
    assert ansible_native_concat(['a', 'b', 'c']) == 'abc'
    assert ansible_native_concat(['1', 1]) == '11'
    assert ansible_native_concat(['1', 2]) == '12'
    assert ansible_native_concat(['1', 2, '3']) == '123'
    assert ansible_native_concat([1, '2', 3]) == '123'

# Generated at 2022-06-22 12:08:34.682008
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    """Unit test for function ansible_native_concat"""

    assert ansible_native_concat([container_to_text(1)]) == 1
    assert ansible_native_concat([container_to_text([1, 2, 3])]) == [1, 2, 3]
    assert ansible_native_concat([container_to_text(1), container_to_text(1)]) == "11"

    # mimic literal_eval
    assert ansible_native_concat([container_to_text("1")]) == 1
    assert ansible_native_concat([container_to_text("[1, 2, 3]")]) == [1, 2, 3]

    # mimic literal_eval, but fail
    assert ansible_native_concat([container_to_text("1 1")]) == "1 1"

# Generated at 2022-06-22 12:08:44.483447
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # test with strings
    assert ansible_native_concat([]) == None

    assert ansible_native_concat(['test']) == 'test'

    assert ansible_native_concat(['1', '2', '3', '4', '5']) == '12345'
    assert ansible_native_concat(['1', '2', '3', '4', '5']).__class__ == str

    assert ansible_native_concat(['1', '2', '3', '4', '5']) == '12345'
    assert ansible_native_concat(['1', '2', '3', '4', '5']).__class__ == str

    # test with StrictUndefined

# Generated at 2022-06-22 12:08:56.475542
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from jinja2.nativetypes import NativeUndefined
    from jinja2.runtime import Undefined

    assert ansible_native_concat([]) is None

    assert ansible_native_concat(iter([NativeJinjaText('foo')])) == 'foo'
    assert ansible_native_concat(iter([NativeJinjaText('foo'), NativeJinjaText('bar')])) == 'foobar'

    assert ansible_native_concat([u'foo']) == 'foo'

    assert ansible_native_concat(iter([u'foo', u'bar'])) == 'foobar'
    assert isinstance(ansible_native_concat(iter([u'foo', u'b'])), string_types)

    assert ansible_native_concat([u'42']) == 42
   

# Generated at 2022-06-22 12:09:08.187008
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    import jinja2

    env = jinja2.Environment(undefined=StrictUndefined)

    ctx = {'whatevers': [5, 6, 7]}

    def compile_raw(value):
        c = env.compile_expression(value, undefined_to_none=False)
        v = c._eval(ctx)
        assert isinstance(v, StrictUndefined)

        # Make sure v is accessible and the exception is raised.
        str(v)

    # See: https://github.com/pallets/jinja/issues/1200
    assert ansible_native_concat([[1, 2, 3]]) == [1, 2, 3]

    assert ansible_native_concat([b'a']) == u'a'

# Generated at 2022-06-22 12:09:18.644938
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([1, 2]) == [1, 2]
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, 2, 3]) == [1, 2, 3]
    assert ansible_native_concat([1, '2', 3]) == [1, '2', 3]
    assert ansible_native_concat([1, 2, 'literal']) == [1, 2, 'literal']
    assert ansible_native_concat(('a', 2, 'literal')) == ('a', 2, 'literal')
    assert ansible_native_concat(('foo', 'bar')) == 'foobar'

# Generated at 2022-06-22 12:09:39.118783
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:09:47.806627
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.native_jinja import NativeJinjaText

    # Success test cases
    # 1) Simple test cases
    assert ansible_native_concat([]) == None
    assert ansible_native_concat([1]) == 1
    assert ansible_native_concat([1, 2]) == '[1, 2]'
    assert ansible_native_concat(['1', '2']) == '[1, 2]'
    assert ansible_native_concat(['1', 2]) == '[1, 2]'
    assert ansible_native_concat(['1', '2', '3']) == '[1, 2, 3]'

# Generated at 2022-06-22 12:09:57.946601
# Unit test for function ansible_native_concat
def test_ansible_native_concat():

    # test for concatenating strings
    assert ("hello" == ansible_native_concat([
        ast.Constant("hello"),
    ]))

    assert ("hello world" == ansible_native_concat([
        ast.Constant("hello"),
        ast.Constant(" world"),
    ]))

    assert ("hello 'world' 123" == ansible_native_concat([
        ast.Constant("hello"),
        ast.Constant(" 'world'"),
        ast.Constant(" 123"),
    ]))

    # test for concatenating integers
    assert (42 == ansible_native_concat([
        ast.Constant(42),
    ]))

    assert (42 == ansible_native_concat([
        ast.Constant(40),
        ast.Constant(2),
    ]))



# Generated at 2022-06-22 12:10:09.962424
# Unit test for function ansible_native_concat

# Generated at 2022-06-22 12:10:41.652022
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat(iter(['1', 2, 3])) == '123'
    assert ansible_native_concat(chain(iter(['1', 2, 3]), [4])) == '1234'
    assert isinstance(ansible_native_concat(iter([1, 2, 3])), int)
    assert ansible_native_concat(iter([1, 2, 3])) == 123

    # literal_eval
    assert ansible_native_concat(iter(['[1, 2, 3]', 2, 3])) == [1, 2, 3]
    assert ansible_native_concat(iter(['[1, 2, 3]', '(1, 2)', '{1: 2}', 4])) == [1, 2, 3]
    # literal_eval can't parse


# Generated at 2022-06-22 12:10:53.372968
# Unit test for function ansible_native_concat
def test_ansible_native_concat():
    assert ansible_native_concat([]) is None
    assert ansible_native_concat(['foo']) == 'foo'
    assert ansible_native_concat(['foo', 'bar']) == 'foobar'
    assert ansible_native_concat(['foo', 1]) == 'foo1'
    assert ansible_native_concat(['foo', 1, 'bar']) == 'foo1bar'
    # Cannot be parsed with ast.literal_eval
    assert ansible_native_concat(['[', 1, 2, ']']) == '[1, 2]'
    assert ansible_native_concat(['{', 1, 2, '}']) == '{1, 2}'
    # Can be parsed with ast.literal_eval

# Generated at 2022-06-22 12:11:05.806966
# Unit test for function ansible_native_concat


# Generated at 2022-06-22 11:40:42.868959
# Unit test for function get_hash
def test_get_hash():
    assert get_hash("", 'md5') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert get_hash("a") == '86f7e437faa5a7fce15d1ddcb9eaeaea377667b8'
    assert get_hash("a", 'sha1') == '86f7e437faa5a7fce15d1ddcb9eaeaea377667b8'
    assert get_hash("a", 'sha256') == 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'

# Generated at 2022-06-22 11:40:51.777040
# Unit test for function subelements

# Generated at 2022-06-22 11:41:02.975146
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import Jinja2Environment
    from ansible.template import generate_ansible_module_args

    # for each tuple in testdata, check that value[0] is equivalent to
    # to value[1] after being through do_groupby

# Generated at 2022-06-22 11:41:16.706821
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(pattern='^a(.*)c$', value='abc', replacement='A\\1C') == 'AbC'
    assert regex_replace(pattern='^a(.*)c$', value='abbc', replacement='A\\1C') == 'Abbc'
    assert regex_replace(pattern='^a(.*)c$', value='abbc', replacement='A\\1C', ignorecase=True) == 'ABC'
    assert regex_replace(pattern='^a(.*)c$', value='abbc', replacement='\\1', ignorecase=True) == 'bb'
    assert regex_replace(pattern='^a(.*)c$', value='ac', replacement='\\1') == 'ac'

# Generated at 2022-06-22 11:41:21.752352
# Unit test for function comment
def test_comment():
    print(comment("My text"))
    print(comment("My text", style='erlang'))
    print(comment("My text", style='c'))
    print(comment("My text", style='cblock'))
    print(comment("My text", style='xml'))
    print(comment("My text", style='c', newline='\n\r'))
    print(comment("My text", style='c', prefix='-- '))
    print(comment("My text", style='c', prefix='-- ', postfix=''))
    print(comment("My text", style='c', prefix='', postfix=' --'))
    print(comment("My text", style='c', decoration='== '))
    print(comment("My text", style='c', decoration='== ', prefix='-- '))

# Generated at 2022-06-22 11:41:29.606753
# Unit test for function regex_escape
def test_regex_escape():
    for case in [
        ['[foo]', '[foo]'],
        ['', ''],
        ['abcd', 'abcd'],
        ['"', '\\"'],
        ['/home/user.foo', '/home/user\\.foo'],
        ['$variable', '\\$variable'],
        [
            {
                'foo': 'bar',
                'qux': 'quux'
            },
            {
                'qux': 'quux',
                'foo': 'bar'
            }
        ]
    ]:
        assert regex_escape(case[0]) == case[1]


# Generated at 2022-06-22 11:41:39.513613
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    from jinja2.nodes import List, Compare, Name, Const
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleSequence
    templar = Templar(None)
    loop_context = {
        'groups': AnsibleSequence([
            {'environment': 'dev', 'servers': ['foo', 'bar', 'baz']},
            {'environment': 'prod', 'servers': ['qux', 'quux', 'corge']},
            {'environment': 'prod', 'servers': ['garply', 'waldo', 'fred', 'plugh', 'xyzzy', 'thud']},
        ]),
    }


# Generated at 2022-06-22 11:41:50.761920
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('Hello world', 'world') == 'world'
    assert regex_search('Hello world', 'world', '\\g<1>') == ['world', 'world']
    assert regex_search('Hello world', r'w(o)(r)ld', r'\g<2>\g<1>\g<3>') == ['orw', 'orw']
    assert regex_search('Hello 1', r'(\d)', r'\g<1>', ignorecase=True) == ['1']
    assert regex_search('Hello world', 'world', '\\0') == ['world', 'world']
    assert regex_search('Hello world', r'(\w+)', r'\g<1>') == ['Hello', 'world']

# Generated at 2022-06-22 11:41:55.283895
# Unit test for function mandatory
def test_mandatory():
    from ansible.template import Jinja2Template
    jinja_env = Jinja2Template().environment
    jinja_env.filters['mandatory'] = mandatory
    assert jinja_env.from_string("{{ data | mandatory }}").render(data="42") == "42"
    try:
        jinja_env.from_string("{{ data | mandatory }}").render(data=None)
    except AnsibleFilterTypeError:
        pass
    else:
        assert False



# Generated at 2022-06-22 11:42:07.396832
# Unit test for function comment
def test_comment():
    """
    Test cases for the comment filter.
    """
    # Multiple lines
    assert comment('Test string.') == '# Test string.'
    assert comment('Test string.\nFoo') == '# Test string.\n# Foo'
    assert comment(
        'Test string.\nFoo\nBar\n') == '# Test string.\n# Foo\n# Bar\n'
    # Predefined style 'plain'
    assert comment('Test string.', 'plain') == '# Test string.'
    assert comment('Test string.\nFoo', 'plain') == '# Test string.\n# Foo'
    assert comment(
        'Test string.\nFoo\nBar\n', 'plain') == '# Test string.\n# Foo\n# Bar\n'
    # Predefined style 'c

# Generated at 2022-06-22 11:42:16.645547
# Unit test for function get_hash
def test_get_hash():
    def test_hash(hash_type):
        assert get_hash('my data', hash_type) == getattr(hashlib, hash_type)('my data'.encode()).hexdigest()
    for hash_type in ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'):
        test_hash(hash_type)



# Generated at 2022-06-22 11:42:21.007778
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'foo[bar]baz') == 'foo\\[bar\\]baz'
    assert regex_escape(r'foo[bar]baz', re_type='posix_basic') == 'foo[.]bar[.]baz'



# Generated at 2022-06-22 11:42:30.165783
# Unit test for function mandatory
def test_mandatory():
    assert '1' == mandatory('1')
    assert '1' == mandatory(1)
    assert 1 == mandatory(1, msg="mandatory error test")
    try:
        mandatory(Undefined(name='foo'))
    except AnsibleFilterError as e:
        assert 'foo' in str(e)
        assert "Mandatory variable 'foo' not defined." in str(e)
    try:
        mandatory(Undefined())
    except AnsibleFilterError as e:
        assert "Mandatory variable not defined." in str(e)



# Generated at 2022-06-22 11:42:41.894084
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    env = Environment()
    for x in [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]:
        assert do_groupby(env, x, 'a') == _do_groupby(env, x, 'a')

    assert do_groupby(env, [], 'a') == []
    assert do_groupby(env, [{'a': 1}], 'a') == [(1, [{'a': 1}])]

# Generated at 2022-06-22 11:42:47.396971
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/*.conf*') == ['/etc/mke2fs.conf', '/etc/lvm/lvm.conf', '/etc/yum.conf', '/etc/sysconfig/rhn/up2date', '/etc/init.d/functions', '/etc/ld.so.conf.d/libc.conf']


# Generated at 2022-06-22 11:42:51.753690
# Unit test for function ternary
def test_ternary():
    assert ternary(True, 1, 2) == 1
    assert ternary(False, 1, 2) == 2
    assert ternary(None, 1, 2, 3) == 3
    assert ternary("foo", 1, 2) == 1
    assert ternary("", 1, 2) == 2
    assert ternary("", 1, 2, 3) == 3


# Generated at 2022-06-22 11:42:56.470435
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml([1, {'a': 'b'}], default_flow_style=False) == """- 1
- a: b
"""



# Generated at 2022-06-22 11:43:01.879065
# Unit test for function mandatory
def test_mandatory():
    env = {}

    try:
        mandatory(env['should_be_defined'])
        assert False, "Failed to raise error on missing variable"
    except AnsibleFilterError as e:
        pass

    try:
        assert mandatory(env.get('should_be_defined'), 'forced message') == "forced message", "Failed to return custom message"
    except AnsibleFilterError as e:
        pass



# Generated at 2022-06-22 11:43:12.176795
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import DictEnvironment, StrictUndefined

    # only use DictEnvironment for test, do not use in production
    environment = DictEnvironment(undefined=StrictUndefined)
    value = [dict(key=1, value='foo'), dict(key=2, value='bar'), dict(key=1, value='baz')]
    attribute = 'key'
    result = do_groupby(environment, value, attribute)
    expected = [(1, [('key', 1), ('value', 'foo')]), (2, [('key', 2), ('value', 'bar')]), (1, [('key', 1), ('value', 'baz')])]
    assert result == expected, result



# Generated at 2022-06-22 11:43:16.854738
# Unit test for function comment
def test_comment():
    assert comment('thetext') == '# thetext'
    assert comment('thetext', 'plain') == '# thetext'
    assert comment('thetext', 'erlang') == '% thetext'
    assert comment('thetext', 'c') == '// thetext'
    assert comment('thetext', 'cblock') == '''/*
 * thetext */'''
    assert comment('thetext', 'xml') == '''<!--
 - thetext-->'''
    assert comment('thetext', 'xml', decoration='## ') == '''<!--
## thetext-->'''
    assert comment('thetext', decoration='@@ ') == '#@ @thetext'
    assert comment('thetext', decoration='') == '#thetext'

# Generated at 2022-06-22 11:43:26.393548
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo') == 'foo'
    assert regex_escape('foo/bar') == 'foo/bar'
    assert regex_escape('foo/bar\n') == 'foo/bar\\n'
    assert regex_escape('foo/bar\n', re_type='posix_basic') == 'foo/bar\\n'



# Generated at 2022-06-22 11:43:37.565731
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1, "1 is not None") == 1
    assert mandatory(0, "0 is not None") == 0
    assert mandatory(None) == None
    assert mandatory({"name": "Test", "age": 100}, "This is not a null value") == {"name": "Test", "age": 100}
    assert mandatory(()) == ()
    assert mandatory([1,2,3]) == [1,2,3]
    assert mandatory(set([1,2,3])) == set([1,2,3])
    assert not mandatory(set([]))
    assert not mandatory([])
    assert not mandatory(())
    assert not mandatory({})
    assert not mandatory(None, "None is a null value")
    assert not mandatory(None)



# Generated at 2022-06-22 11:43:44.930135
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo\nbar', r'\n', '\\1') == '\n'
    assert regex_search('foo\nbar', r'\n', '\\g<1>') == '\n'
    assert regex_search('foo\nbar', r'^(\w+)', '\\g<1>') == 'foo'
    assert regex_search('foo\nbar', r'^(\w+)', '\\1', '\\g<1>') == ['foo', 'foo']
    assert regex_search('foo\nbar', r'^(\w+)', '\\g<1>', '\\1') == ['foo', 'foo']

# Generated at 2022-06-22 11:43:46.120653
# Unit test for function mandatory
def test_mandatory():
    assert mandatory != None



# Generated at 2022-06-22 11:43:51.056981
# Unit test for function do_groupby
def test_do_groupby():
    env = Environment()
    env.filters['groupby'] = do_groupby
    # jinja 2.9.0
    v = [AttrDict({'a': 1, 'b': 3}), AttrDict({'a': 1, 'b': 4}), AttrDict({'a': 2, 'b': 6})]

    # idempotency check
    gb = env.from_string('{{ value | groupby( "a" ) | list }}').render(value=v)
    assert gb == env.from_string('{{ value | groupby( "a" ) | list }}').render(value=gb)

    # conversion of namedtuple to tuple
    gb = env.from_string('{{ value | groupby( "a" ) | list }}').render(value=v)

# Generated at 2022-06-22 11:44:03.002788
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foobar', 'foo') == 'foo'
    assert regex_search('foobar', 'foo', '\\g<1>') == ['foo', 'bar']
    assert regex_search('foobar', 'foo', '\\0') == ['foo', 'foo']
    assert regex_search('foo123bar', 'foo(?P<num>\d+)', '\\g<num>') == ['123']
    assert regex_search('foo123bar', 'foo(?P<num>\d+)', '\\g<num>', '\\g<num>') == ['123', '123']
    assert regex_search('foo123bar', 'foo(?P<num>\d+)', '\\1') == ['123']

# Generated at 2022-06-22 11:44:12.412668
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('', '^.+$', r'\g<0>', True, True) == ''
    assert regex_replace('foo', '', '', True, True) == 'foo'
    assert regex_replace('foo', '^.+$', r'\g<0>', True, True) == 'foo'
    assert regex_replace('foo', '^(?P<one>.+)(?P<two>.+)$', r'\g<two> \g<one>', True, True) == 'foo foo'



# Generated at 2022-06-22 11:44:17.908481
# Unit test for function mandatory
def test_mandatory():
    assert mandatory() == None
    try:
        mandatory(AnsibleUndefined)
        assert False, 'should throw an exception'
    except AnsibleFilterError:
        pass
    return True



# Generated at 2022-06-22 11:44:19.489014
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'\w+') == '\\\\w\\+'



# Generated at 2022-06-22 11:44:27.395487
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('aabbbbccc', pattern='b+', replacement='d') == 'aadccc'
    assert regex_replace('aabbbbccc', pattern='b+', replacement='d', ignorecase=True) == 'aadccc'
    assert regex_replace('aabbbbccc', pattern='B+', replacement='d') == 'aabbbbccc'
    assert regex_replace('aabbbbccc', pattern='B+', replacement='d', ignorecase=True) == 'aadccc'


# Generated at 2022-06-22 11:44:43.222841
# Unit test for function mandatory
def test_mandatory():
    # Test variables
    undefined = 'JINJA_UNDEFINED'
    variable = 'variable'
    null_variable = None
    undef_var_msg = 'The variable is undefined'
    undef_var_msg_fail = 'The variable is not undefined'

    # Test class for unit test
    class TestClass(object):
        pass

    # Test function for unit test
    def test_func():
        pass

    from ansible.template import Templar
    t = Templar(
        loader=None,
        variables={
        }
    )

    # Test variable types
    assert mandatory(t.template(undefined, fail_on_undefined=True)) == undefined
    assert mandatory(variable) == variable
    assert mandatory(null_variable, 'Null variable') == null_variable
    assert mandatory(TestClass) == TestClass

# Generated at 2022-06-22 11:44:45.632563
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'k0': 'v0'}) == 'k0: v0\n'



# Generated at 2022-06-22 11:44:47.815919
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'a': 'b'}) == '{a: b}\n'


# Generated at 2022-06-22 11:44:57.925875
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo', '^(\\d+)') == None
    assert regex_search('1024', '^(\\d+)') == '1024'
    assert regex_search('1024', '^(\\d+)', '\\1') == ['1024', '1024']
    assert regex_search('foo,1024', '^(\\w+),(\\d+)', '\\2', '\\g<1>') == ['1024', 'foo']
    assert regex_search('foo,1024', '^(?P<alpha>\\w+),(?P<beta>\\d+)', '\\g<alpha>', '\\g<beta>') == ['foo', '1024']
    return True


# Generated at 2022-06-22 11:45:08.392603
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    assert mandatory("a") == "a"
    assert mandatory("a", "msg") == "a"
    assert mandatory(Undefined("a")) == a  # nosec
    assert mandatory(Undefined("a"), "msg") == a  # nosec
    assert mandatory(Undefined("a", name="b")) == b  # nosec
    assert mandatory(Undefined("a", name="b"), "msg") == b  # nosec
    with pytest.raises(AnsibleFilterError) as exception:
        mandatory(Undefined("a"), "msg")
    assert "msg" in to_text(exception.value)
    with pytest.raises(AnsibleFilterError) as exception:
        mandatory(Undefined("a"))
    assert "Mandatory variable" in to_text

# Generated at 2022-06-22 11:45:16.587973
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    a = {"key": {"subkey": "value"},
         "list": ["item", 2, {"subitem": "value"}],
         "dup": ["item", "item", "value", 2, 2]}
    result = to_nice_yaml(a, default_flow_style=False)
    assert result == '''list:
    - item
    - 2
    - subitem: value
dup:
    - item
    - item
    - value
    - 2
    - 2
key:
    subkey: value
'''



# Generated at 2022-06-22 11:45:29.888066
# Unit test for function mandatory
def test_mandatory():
    from jinja2 import Environment

    env = Environment()
    assert env.from_string('{{ bar }}').render(bar='bar') == 'bar'
    assert env.from_string('{{ bar | mandatory }}').render(bar='bar') == 'bar'
    try:
        assert env.from_string('{{ bar | mandatory }}').render() == ''
        assert False
    except AnsibleFilterError as e:
        assert str(e) == "Mandatory variable 'bar' not defined."

    assert env.from_string('{{ bar | mandatory("foo") }}').render(bar='bar') == 'bar'
    try:
        assert env.from_string('{{ bar | mandatory("foo") }}').render() == ''
        assert False
    except AnsibleFilterError as e:
        assert str(e) == "foo"



# Generated at 2022-06-22 11:45:33.666427
# Unit test for function mandatory
def test_mandatory():
    ''' mandatory should raise an error when called with param set to AnsibleUndefined
    '''
    failed = False
    try:
        mandatory(AnsibleUndefined, "Failed Test")
    except AnsibleFilterError:
        failed = True

    assert(failed)
# Test module


# Generated at 2022-06-22 11:45:39.783611
# Unit test for function do_groupby
def test_do_groupby():
    from distutils.version import LooseVersion

    import jinja2

    # We only need to monkeypatch this for jinja2 <2.9.5
    if LooseVersion(jinja2.__version__) < LooseVersion('2.9.5'):
        jinja2.filters.FILTERS['groupby'] = do_groupby



# Generated at 2022-06-22 11:45:49.373460
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo', '^.{3}$') == 'foo'
    assert regex_search('foo', '^.{3}$', '\\g<0>') == 'foo'
    assert regex_search('foo', '^.{3}$', '\\0') == 'foo'
    assert regex_search('foo', '^.{3}$', '\\1') is None
    assert regex_search('foo', '^.{3}$', '\\g<1>') is None
    assert regex_search('foo', 'foo') == 'foo'
    assert regex_search('foo', 'foo', '\\g<0>') == 'foo'
    assert regex_search('foo', 'foo', '\\0') == 'foo'

# Generated at 2022-06-22 11:46:04.155426
# Unit test for function regex_search
def test_regex_search():
    regex_search("miXedCAse", "[a-z]+", "\\g<0>", ignorecase=True) == ['miXedCAse']
    regex_search("test_test", "t\\g<0>", "\\g<0>") == ['test_test']
    regex_search("test_test", "t(e)\\1", "\\1") == ['e']
    regex_search("test_test", "t(e)", "\\1") == ['e']
    regex_search("test_test", "t(e)\\g<0>", "\\1") == ['e']
    regex_search("test_test", "t(e)\\g<0>", "\\g<0>") == ['test']

# Generated at 2022-06-22 11:46:12.328877
# Unit test for function mandatory
def test_mandatory():
    from jinja2.exceptions import UndefinedError
    from jinja2 import DictEnvironment
    env = DictEnvironment()
    env.filters['mandatory'] = mandatory
    template = env.from_string("{{var | mandatory(msg='test message')}}")
    assert template.render(var='value') == 'value'
    try:
        template.render()
    except UndefinedError as e:
        assert isinstance(e, AnsibleFilterError)
        assert "Mandatory variable not defined" in str(e)
    # test msg parameter
    template = env.from_string("{{var | mandatory(msg='test message')}}")
    try:
        template.render()
    except UndefinedError as e:
        assert isinstance(e, AnsibleFilterError)

# Generated at 2022-06-22 11:46:16.101436
# Unit test for function combine
def test_combine():
    assert {'bar': [1, 2, 3, 4]} == combine([{'foo': 'nowhere'}, {'bar': [1, 2]}, {'bar': [3, 4]}, {}], list_merge='append')



# Generated at 2022-06-22 11:46:20.233686
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(2) == 2
    assert mandatory(None) is None
    assert mandatory([1, 2, 3]) == [1, 2, 3]
    assert mandatory(object()) == object()
    assert mandatory(dict(a=1, b=2, c=3)) == dict(a=1, b=2, c=3)



# Generated at 2022-06-22 11:46:30.016152
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'a': 'b', 'c': 'd'}) == "---\na: b\nc: d\n"
    assert to_yaml([1, 2, 3]) == "---\n- 1\n- 2\n- 3\n"
    assert to_yaml([1, 2, 3], default_flow_style=True) == "--- [1, 2, 3]\n"
    assert to_yaml({'a': [1, 2, 3], 'b': 'c'}, default_flow_style=True) == "---\na: [1, 2, 3]\nb: c\n"

# Generated at 2022-06-22 11:46:33.001141
# Unit test for function mandatory
def test_mandatory():
    assert mandatory({'a': '1', 'b': '2'}, msg="") == {u'a': u'1', u'b': u'2'}


# Generated at 2022-06-22 11:46:37.383389
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foobar', r'foo') == 'foo'
    assert regex_search('foo\nbar', r'foo', '\\g<1>', ignorecase=True, multiline=True) == ['foo', '\n']


# Generated at 2022-06-22 11:46:48.845109
# Unit test for function regex_search
def test_regex_search():
    '''Test function regex_search'''
    value = 'hello, a.'
    regex = r'a.'
    assert regex_search(value, regex) == 'a.'
    assert regex_search(value, regex, '\\g<0>') == 'a.'
    assert regex_search(value, regex, '\\g<0>') == regex_search(value, regex, '\\1')
    assert regex_search(value, regex, '\\g<0>', '\\g<0>') == [u'a.', u'a.']
    value = 'Hello World!'
    assert regex_search(value, r'(\w+) (\w+)!' , '\\g<2>', '\\g<1>') == ['World', 'Hello']



# Generated at 2022-06-22 11:46:51.861460
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml(['foo', 'bar']) == "---\n- foo\n- bar\n"



# Generated at 2022-06-22 11:47:00.902852
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Undefined
    from jinja2 import StrictUndefined
    from jinja2 import Environment
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import AnsibleJ2Vars
    from ansible.parsing.vault import VaultLib
    import sys


# Generated at 2022-06-22 11:47:35.303102
# Unit test for function regex_search
def test_regex_search():
    text = "Example string"
    # Asserts without arguments
    assert regex_search(text, r'string') == u'string'
    assert regex_search(text, r's\dng') is None
    # Asserts with arguments
    assert regex_search(text, r's\dng', '\\g<0>') == u's\x02ng'
    assert regex_search(text, r'[a-z]+', '\\g<0>') == u'example'
    assert regex_search(text, r'[a-z]+', '\\g<1>') == u'tring'
    assert regex_search(text, r'[a-z]+', '\\g<0>', '\\g<1>') == [u'example', u'tring']

# Generated at 2022-06-22 11:47:46.537649
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('', 'python') == ''
    assert regex_escape('[f]oo.bar\\baz', 'python') == '\\[f\\]oo\\.bar\\\\baz'
    assert regex_escape('[f]oo.bar\\baz', 'posix_basic') == '\\[f\\]oo\\.bar\\\\baz'
    assert regex_escape('[f]oo.bar\\baz', 'posix_extended') == '\\[f\\]oo\\.bar\\\\baz'
    assert regex_escape('[f]oo.bar\\baz', 'nonsense') == '\\[f\\]oo\\.bar\\\\baz'
# /Unit test for function regex_escape



# Generated at 2022-06-22 11:47:53.207710
# Unit test for function strftime
def test_strftime():
    assert strftime("%Y", strftime("%s", "2032-02-07")) == '2032'
    assert strftime("%Y-%m-%d", strftime("%s", "2032-02-07")) == '2032-02-07'
    assert strftime("%Y-%m-%d", "2032-02-07") == '2032-02-07'


# Generated at 2022-06-22 11:47:58.018667
# Unit test for function strftime
def test_strftime():
    now = datetime.datetime.now()
    epoch = time.mktime(now.timetuple())
    assert strftime("%Y/%m/%d %H:%M:%S", epoch) == now.strftime("%Y/%m/%d %H:%M:%S")



# Generated at 2022-06-22 11:48:04.767914
# Unit test for function mandatory
def test_mandatory():
    # success case
    assert mandatory('test') == 'test'
    # failure case
    try:
        mandatory('test', msg="Mandatory message test")
        assert False
    except AnsibleFilterError as e:
        assert e.message == "Mandatory message test"

    try:
        mandatory({}, msg="Mandatory message test")
        assert False
    except AnsibleFilterError as e:
        assert e.message == "Mandatory message test"



# Generated at 2022-06-22 11:48:13.120929
# Unit test for function mandatory
def test_mandatory():
    # Test case 1
    assert mandatory(True) == True
    # Test case 2
    assert mandatory(True, msg='test') == True
    # Test case 3
    try:
        mandatory(False, msg='test')
    except Exception as e:
        assert isinstance(e, AnsibleFilterError)
        assert str(e) == "Mandatory variable 'undefined' not defined."
    # Test case 4
    try:
        mandatory(False)
    except Exception as e:
        assert isinstance(e, AnsibleFilterError)
        assert str(e) == "Mandatory variable 'undefined' not defined."



# Generated at 2022-06-22 11:48:20.902763
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    env = Environment()
    env.filters['mandatory'] = mandatory

    # Test that a message is raised if a variable is not set
    template = env.from_string(
        '{{ not_set | mandatory }}'
    )
    try:
        template.render()
    except AnsibleFilterError:
        pass
    else:
        assert False, 'Should have raised an error'

    # Test that we can specify an error message
    template = env.from_string(
        '{{ not_set | mandatory(msg="oops") }}'
    )
    try:
        template.render()
    except AnsibleFilterError as e:
        assert str(e) == 'oops'
    else:
        assert False, 'Should have raised an error'

    # Test that we can

# Generated at 2022-06-22 11:48:27.895493
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    try:
        mandatory(Undefined(name='foo'))
        assert False, "Should have raised an exception"
    except AnsibleFilterError:
        pass

    assert mandatory(None, "my msg") is None
    assert mandatory(42) == 42


# Generated at 2022-06-22 11:48:39.473019
# Unit test for function do_groupby
def test_do_groupby():
    # jinja2.Undefined is a function in jinja2 which allows us to
    # use undefined variables without causing issues.
    from jinja2.runtime import Undefined
    from ansible.utils import apply_filter_func

    # Since we're testing a filter, we need to call apply_filter_func in order to get
    # an environment, which is what the do_groupby function uses.
    d = apply_filter_func(
        'do_groupby',
        [
            {'a': '1', 'b': '1'},
            {'a': '2', 'b': '2'},
            {'a': '1', 'b': '3'},
            {'a': '2', 'b': '4'}
        ],
        'a',
    )

# Generated at 2022-06-22 11:48:46.281086
# Unit test for function mandatory
def test_mandatory():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'mandatory_var': 'hello'}
    inventory = InventoryManager(loader=None, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    templar = Templar(loader=None, variables=variable_manager)
    assert templar.template('{{ mandatory_var }}') == 'hello'
    assert templar.template('{{ mandatory_var | mandatory() }}') == 'hello'


# Generated at 2022-06-22 11:49:00.234252
# Unit test for function mandatory
def test_mandatory():
    'Test mandatory filter'
    assert mandatory(object()) == object()
    assert mandatory(None) == None
    assert mandatory(1) == 1
    assert mandatory(0) == 0
    assert mandatory(AnsibleUndefined) == AnsibleUndefined
    assert mandatory(AnsibleUndefined, '%s is mandatory') == AnsibleUndefined
    assert mandatory(AnsibleUndefined._text, '%s is mandatory') == AnsibleUndefined._text
    try:
        mandatory(AnsibleUndefined, '%s is mandatory')
    except AnsibleFilterError as e:
        assert str(e) == 'Mandatory variable is mandatory.'


# Generated at 2022-06-22 11:49:12.849158
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template.safe_eval import SafeEval

    environment = AnsibleEnvironment(loader=DictLoader({}))
    from jinja2.filters import FILTERS

    # set up a test where jinja2 returns a namedtuple, but ansible.template.safe_eval does not
    do_groupby = FILTERS['groupby']
    safe_eval = SafeEval(environment, loader=DictLoader({}))

    data = [{'location': '1', 'name': 'B'}, {'location': '1', 'name': 'A'}, {'location': '2', 'name': 'C'}]
    attribute = 'location'

    # do jinja2's groupby
    jinja2_groupby = do_groupby(environment, data, attribute)

# Generated at 2022-06-22 11:49:20.719287
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(None, msg='No None allowed')
    # Without msg param
    try:
        mandatory(None)
    except AnsibleFilterError:
        pass
    else:
        assert False, 'Expected an exception to be raised'
    # test that a variable name is passed as part of the message
    try:
        mandatory(AnsibleUndefined('foo'))
    except AnsibleFilterError as e:
        assert 'foo' in to_native(e)
    else:
        assert False, 'Expected an exception to be raised'



# Generated at 2022-06-22 11:49:32.275359
# Unit test for function do_groupby
def test_do_groupby():
    class Tmp(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
    tmp = [Tmp(1, 'A'), Tmp(1, 'B'), Tmp(2, 'C'), Tmp(2, 'D'), Tmp(1, 'E')]
    env = Environment()
    result = do_groupby(env, tmp, 'a')
    assert isinstance(result, list)
    for r in result:
        assert isinstance(r, tuple)
        assert isinstance(r[0], int)
        assert isinstance(r[1], list)
        for entry in r[1]:
            assert isinstance(entry, Tmp)
            assert isinstance(entry.a, int)
            assert isinstance(entry.b, str)
   

# Generated at 2022-06-22 11:49:42.764700
# Unit test for function regex_search
def test_regex_search():
    obj = {
        "replace_me": "replace me",
        "dont_replace_me": "dont replace me"
    }
    assert regex_search(obj, "replace") == "replace"
    assert regex_search(obj, "replace", '\g<0>') == "replace"
    assert regex_search(obj, "place", '\g<0>') == "place"
    assert regex_search(obj, "place", '\g<0>', ignorecase=True) == "place"
    assert regex_search(obj, "replace", '\\g<0>') == "replace"
    assert regex_search(obj, "[ae]", '\g<0>') == "a"

# Generated at 2022-06-22 11:49:51.632799
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('', 'ansible') is None
    assert regex_search('ansible', 'ansible') == 'ansible'
    assert regex_search('ansible', 'ansible', '\\0') == ['ansible']
    assert regex_search('ansible ansible.com', 'ansible', '\\0', '\\1') == ['ansible', 'ansible.com']
    assert regex_search('ansible ansible.com', 'ansible', '\\g<0>', '\\g<1>') == ['ansible', 'ansible.com']



# Generated at 2022-06-22 11:49:59.650831
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    try:
        mandatory(Undefined())
        raise AssertionError("Failed to raise exception for mandatory()")
    except AnsibleFilterError:
        pass
    try:
        mandatory(Undefined(name='foo'), "Custom Message")
        raise AssertionError("Failed to raise exception for mandatory()")
    except AnsibleFilterError as e:
        assert e.__str__() == 'Custom Message'



# Generated at 2022-06-22 11:50:05.316589
# Unit test for function mandatory
def test_mandatory():
    def test(a):
        try:
            mandatory(a)
        except AnsibleFilterError:
            return False
        return True

    class Undefined():
        pass
    u = Undefined()
    u._undefined_name = "foo"
    assert test("b")
    assert not test(None)
    assert not test(u)
    assert not test(u)


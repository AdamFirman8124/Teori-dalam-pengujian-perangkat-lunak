

# Generated at 2022-06-22 11:40:42.257339
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/*d') == ['/etc/fstab', '/etc/mtab']
    assert fileglob('/etc/fstab') == ['/etc/fstab']
    assert fileglob('/etc/dtab') == []



# Generated at 2022-06-22 11:40:49.968704
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/ansible/hosts') == ['/etc/ansible/hosts']
    assert fileglob('/etc/ansible/h?sts') == ['/etc/ansible/hosts']
    assert fileglob('/etc/ansible/h[!o]sts') == []
    assert fileglob('/etc/ansible/h*/') == []
    assert fileglob('/etc/ansible/h*') == []
    assert fileglob('/no_such_file') == []
    assert fileglob('/etc/passwd') == []



# Generated at 2022-06-22 11:40:57.393250
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/host*') == ['/etc/hostname', '/etc/hosts']
    # no match
    assert fileglob('/etc/*/hosts') == []
    # no match
    assert fileglob('/some/bad/path') == []
    # a directory
    assert fileglob('/etc/') == []



# Generated at 2022-06-22 11:41:09.579168
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('aaaa', 'a+', '\\g<0>') == 'aaaa'
    assert regex_search('aaaa', 'a+', '\\g<1>') == 'a'
    assert regex_search('aaaa', 'a+', '\\g<2>') == 'a'
    assert regex_search('aaaa', 'a+', '\\1') == 'a'
    assert regex_search('aaaa', 'a+', '\\2') == 'a'
    assert regex_search('aaaa', 'a+', '\\3') == 'a'
    assert regex_search('aaaa', 'a+', '\\4') == 'a'
    assert regex_search('ああああ', 'あ+', '\\g<0>') == 'ああああ'



# Generated at 2022-06-22 11:41:21.385186
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import Templar

    templar = Templar(loader=None)
    testlist = [{'a': 1, 'b': 2}, {'a': 1, 'b': 3}, {'a': 2, 'b': 4}]

    # assert that the output is the same as jinja2's built-in `groupby`
    assert _do_groupby(templar, testlist, 'a') == do_groupby(templar, testlist, 'a')

    # This is the only real purpose of the `do_groupby` override.
    # assert that the output is equal to a list of _regular_ tuples

# Generated at 2022-06-22 11:41:26.070419
# Unit test for function comment
def test_comment():
    failures = 0

    # This test vector defines the expected results

# Generated at 2022-06-22 11:41:30.873096
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1, msg='msg') == 1
    with pytest.raises(AnsibleFilterError, match="Mandatory variable 'variable' not defined."):
        mandatory(AnsibleUndefined(name='variable'))


# Generated at 2022-06-22 11:41:40.184259
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('', '', '') == ''
    assert regex_replace('abcd', '', '') == 'abcd'
    assert regex_replace('', '', 'E') == ''
    assert regex_replace('abcd', '', 'E') == 'abcd'
    assert regex_replace('', 'a', '') == ''
    assert regex_replace('abcd', 'a', '') == 'bcd'
    assert regex_replace('', 'a', 'E') == ''
    assert regex_replace('abcd', 'a', 'E') == 'Ebcd'
    assert regex_replace('', 'A', 'E') == ''
    assert regex_replace('abcd', 'A', 'E') == 'abcd'
    assert regex_replace('', 'A', 'E', ignorecase=True) == ''


# Generated at 2022-06-22 11:41:51.305089
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("abcde", r"\w{3}", "\g<0>") == ['abc']
    assert regex_search("abcde", r"\w{3}", "\g<1>") == ['abc']
    assert regex_search("abcde", r"\w{3}", "\g<2>") == ['abc']
    assert regex_search("abcde", r"\w{3}", "\g<1>", "\g<0>") == ['abc', 'abc']
    assert regex_search("abcde", r"\w{3}", "\g<2>", "\g<1>") == ['abc', 'abc']

# Generated at 2022-06-22 11:42:00.206443
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml(['a', 'b', 'c']) == ("- a\n- b\n- c\n", True)
    value = {'a': '1',
             'b': '2',
             'c': '3',
             }
    expected = '{a: \'1\', b: \'2\', c: \'3\'}\n...\n'
    assert to_yaml(value) == (expected, True)

    value = 'a, b, c'
    expected = '"a, b, c"\n'
    assert to_yaml(value) == (expected, True)


# Generated at 2022-06-22 11:42:18.244862
# Unit test for function to_bool
def test_to_bool():
    assert to_bool(True)
    assert to_bool('1')
    assert to_bool('on')
    assert to_bool('true')
    assert to_bool('yes')
    # Following values should return False
    assert not to_bool('')
    assert not to_bool(False)
    assert not to_bool('False')
    assert not to_bool('0')
    assert not to_bool('off')
    assert not to_bool('no')
    assert not to_bool('none')
    assert not to_bool('false')



# Generated at 2022-06-22 11:42:29.389886
# Unit test for function get_hash

# Generated at 2022-06-22 11:42:35.612597
# Unit test for function to_yaml
def test_to_yaml():
    to_yaml_input = dict(a='alpha', b='beta', c=['charlie', 'cat'])
    output = to_yaml(to_yaml_input, default_flow_style=False)
    assert output == '''\
a: alpha
b: beta
c:
- charlie
- cat
'''

# Generated at 2022-06-22 11:42:49.408647
# Unit test for function extract
def test_extract():
    class MyDict(dict):
        def __getitem__(self, key):
            # force a KeyError if it's missing
            return dict.__getitem__(self, key)

    assert extract(MyDict(a={'b':2}), 'b', MyDict(a={'b':1}), 'a') == 2
    assert extract('b', MyDict(a={'b':1}), 'a') == 1
    assert extract('b', MyDict(a={'b':1}), 'a', 'a') == 1
    assert extract('b', MyDict(a={'b':1}), 'a', morekeys=['a']) == 1
    assert extract('b', MyDict(a={'b':1}), 'a', morekeys=['b', 'b']) == 1


# Generated at 2022-06-22 11:42:53.761624
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('1', r'1') == '1'
    assert regex_search('12', r'1') == '1'
    assert regex_search('123', r'1') == '1'
    assert regex_search('1234', r'1') == '1'
    assert regex_search('12345', r'1') == '1'
    assert regex_search('123456', r'1') == '1'
    assert regex_search('1234567', r'1') == '1'
    assert regex_search('12345678', r'1') == '1'
    assert regex_search('123456789', r'1') == '1'
    assert regex_search('1234567890', r'1') == '1'
    assert regex_search('foo', r'foo') == 'foo'

# Generated at 2022-06-22 11:42:58.152757
# Unit test for function comment
def test_comment():
    assert comment(
        text='',
        style='plain') == '# '

    assert comment(
        text='',
        style='erlang') == '% '

    assert comment(
        text='',
        style='c') == '// '

    assert comment(
        text='',
        style='cblock') == '/* *  */'

    assert comment(
        text='',
        style='xml') == '<!-- - -->'

    assert comment(
        text='',
        decoration=';; ') == ';; '

    assert comment(
        text='\n',
        decoration=';; ') == ';; \n;; '

    assert comment(
        text='example text',
        decoration=';; ') == ';; example text'


# Generated at 2022-06-22 11:43:01.631226
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml([{"a": 1,"b": 2,"c": [1,2,3,4,5,6]}]) == u'[{a: 1, b: 2, c: [1, 2, 3, 4, 5, 6]}]\n'



# Generated at 2022-06-22 11:43:12.743491
# Unit test for function extract
def test_extract():
    assert extract('a', {'a': 123}) == 123
    assert extract('a', {'a': {'b': 'c'}}) == {'b': 'c'}
    assert extract('a', {'a': {'b': {'c': 'd'}}}) == {'b': {'c': 'd'}}
    assert extract('a', {'a': {'b': {'c': 'd'}}}, 'b') == {'c': 'd'}
    assert extract('a', {'a': {'b': {'c': 'd'}}}, 'c') == 'd'
    assert extract('a', {'a': {'b': {'c': 'd'}}}, ['b', 'c']) == 'd'



# Generated at 2022-06-22 11:43:16.977653
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('hello', r'\w+', 'hi') == 'hi'
    assert regex_replace('hello', 'l', 'xx', ignorecase=True) == 'hexxo'
    assert regex_replace('hello', 'l', 'xx') == 'hexxo'



# Generated at 2022-06-22 11:43:27.854183
# Unit test for function flatten
def test_flatten():
    assert flatten(['foo', ['bar', ['baz']]]) == ['foo', 'bar', 'baz']
    assert flatten(['foo', ['bar', ['baz']]], levels=1) == ['foo', 'bar', ['baz']]
    assert flatten(['foo', ['bar', ['baz']]], levels=2) == ['foo', 'bar', 'baz']
    assert flatten(['foo', ['bar', ['baz']]], levels=3) == ['foo', 'bar', 'baz']
    assert flatten(['foo', ['bar', ['baz']]], levels=4) == ['foo', 'bar', 'baz']
    # When using levels, if None is specified we should not go beyond the first level

# Generated at 2022-06-22 11:43:42.113846
# Unit test for function regex_search
def test_regex_search():
    value = "The quick brown fox jumped over the lazy dog"

    assert regex_search(value, r"brown (\w+)", '\\g<1>') == 'fox'
    assert regex_search(value, r"brown (\w+)", '\\1') == 'fox'

    assert regex_search(value, r"brown (\w+)", '\\g<1>', '\\2') == ['fox', None]
    assert regex_search(value, r"brown (\w+) fox (\w+)", '\\g<1>', '\\2') == ['quick', 'jumped']
    assert regex_search(value, r"brown (\w+) fox (\w+)", '\\g<1>', '\\g<2>') == ['quick', 'jumped']


# Generated at 2022-06-22 11:43:53.367094
# Unit test for function regex_escape
def test_regex_escape():
    """
    Test escaping a string according to various regex types
    """
    test_string = r'Test [string] \.^$*+?{,}|()'
    test_python_escaped = r'Test\ \[string\]\ \\\.\^\$\*\+\?\{\,\}\|\(\)\Z'
    assert regex_escape(test_string) == test_python_escaped
    test_posix_basic_escaped = r'Test\ \[string\]\ \\\.\^\$\*\\\+\?\{\,\}\|\(\)\Z'
    assert regex_escape(test_string, re_type='posix_basic') == test_posix_basic_escaped



# Generated at 2022-06-22 11:44:02.769370
# Unit test for function regex_escape
def test_regex_escape():
    assert to_text(regex_escape('test')) == 'test'
    assert to_text(regex_escape('a.b^c$d*e+f?g|h\\i')) == 'a\\.b\\^c\\$d\\*e\\+f\\?g\\|h\\\\i'
    assert to_text(regex_escape('a.b^c$d*e+f?g|h\\i', re_type='posix_basic')) == 'a\\.b\\^c\\$d\\*e\\+f\\?g\\|h\\\\i'



# Generated at 2022-06-22 11:44:12.227749
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('this is a test') == 'this\\ is\\ a\\ test'
    assert regex_escape('this is a test', re_type='python') == 'this\\ is\\ a\\ test'
    assert regex_escape('this is a test', re_type='posix_basic') == 'this\\ is\\ a\\ test'
    # these are the only exceptions for posix_basic
    assert regex_escape('a^b.d$f', re_type='posix_basic') == 'a\\^b\\.d\\$f'



# Generated at 2022-06-22 11:44:19.494443
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    env = Environment()
    t = [{'name':'a', 'value': 1}, {'name':'a', 'value': 2}, {'name':'b', 'value': 2}]
    result = do_groupby(env, t, 'name')
    assert (list(result[0]) == ('a', [{'name':'a', 'value': 1}, {'name':'a', 'value': 2}]))
    assert (list(result[1]) == ('b', [{'name':'b', 'value': 2}]))
    assert (len(result) == 2)

# Generated at 2022-06-22 11:44:30.298371
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.plugins.filter.core import FilterModule
    from ansible.inventory.manager import InventoryManager
    # Fake inventory
    inventory = InventoryManager(loader=None, sources='')
    variable_manager = VariableManager(loader=None, inventory=inventory)
    templar = Templar(variable_manager=variable_manager)
    fake_filter = FilterModule(None)
    get_do_groupby = lambda x,y: fake_filter._templar.run_filters(
        fake_filter._get_do_groupby(fake_filter._environment, x, y),
        fake_filter._environment
    )

    # Test a real life example.
    # 1) Create the base object

# Generated at 2022-06-22 11:44:36.716808
# Unit test for function regex_escape
def test_regex_escape():
    # Test a few strings
    assert regex_escape('a.*b') == 'a\\.\\*b'
    assert regex_escape('a.b', re_type='posix_basic') == 'a\\.b'
    # Test unicode
    assert regex_escape(u'a\u00B1b') == 'a\\u00B1b'



# Generated at 2022-06-22 11:44:48.791787
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("Your name is Bob", "[a-z]+[\s]+([a-z]+)") == 'Bob'
    assert regex_search("Your name is Bob and your surname is Johnson", "[a-z]+[\s]+([a-z]+)", "\\g<1> Johnson") == ['Bob','Johnson']
    assert regex_search("Your name is Bob and your surname is Johnson", "[a-z]+[\s]+([a-z]+)", "\\2") == 2
    try:
        regex_search("Your name is Bob and your surname is Johnson", "[a-z]+[\s]+([a-z]+)", "\n")
    except AnsibleFilterError as e:
        assert "Unknown argument" in to_native(e)

# Generated at 2022-06-22 11:45:00.674372
# Unit test for function extract
def test_extract():
    # Setup input data
    inp = dict(
        dict_1={'key_1': 'value_1'},
        dict_2={'key_2': 'value_2'},
        dict_3={'key_3': 'value_3'})

    # Setup test data
    rtn_1 = dict(
        dict_1={'key_1': 'value_1'},
        dict_2={'key_2': 'value_2'})

    rtn_2 = dict(
        dict_1={'key_1': 'value_1'},
        dict_2={'key_2': 'value_2'},
        dict_3={'key_3': 'value_3'})

    rtn_3 = 'value_2'


# Generated at 2022-06-22 11:45:11.888134
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    from copy import copy
    from jinja2.runtime import Undefined
    env = jinja2.Environment()
    result = do_groupby(env, [{'foo': 1, 'bar': 2}, {'foo': 2, 'bar': 2}], 'foo')
    assert len(result) == 2
    assert result[0][0] == 1
    assert result[0][1] == [{'foo': 1, 'bar': 2}]
    assert result[1][0] == 2
    assert result[1][1] == [{'foo': 2, 'bar': 2}]
    env = jinja2.Environment()
    result = do_groupby(env, [{'foo': 1}], 'foo')
    assert len(result) == 1

# Generated at 2022-06-22 11:45:19.728830
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    a = {'a':[1,2,3,{'b':7}], 'c':{'d':[4,5,6]}}
    assert to_nice_yaml(a) == """a:
- 1
- 2
- 3
- b: 7
c:
  d:
  - 4
  - 5
  - 6
"""


# Generated at 2022-06-22 11:45:31.443977
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment

    env = Environment()
    env.filters['groupby'] = do_groupby

    class TestClass(object):
        def __init__(self, test1, test2):
            self.test1 = test1
            self.test2 = test2

    test_objs = [TestClass(1, 2), TestClass(2, 3)]
    result = env.from_string('{{ [test_objs]|groupby(attribute="test1") }}').render(test_objs=test_objs)
    assert result == "[(1, [TestClass(test1=1, test2=2)]), (2, [TestClass(test1=2, test2=3)])]"



# Generated at 2022-06-22 11:45:43.924342
# Unit test for function do_groupby
def test_do_groupby():
    value = [{'h': {'a':1, 'b':'x'}}, {'h': {'a':2, 'b':'y'}}, {'h': {'a':1, 'b':'z'}}, {'h': {'a':2, 'b':'x'}}]
    result = do_groupby(None, value, 'h.a')
    assert len(result) == 2, 'Result length should match total number of items in original list, grouped by attribute h.a'
    assert result[0][1][0]['h'] == {'a': 1, 'b': 'x'}, 'First item in second tuple should be the first item in the original list, as grouped'

# Generated at 2022-06-22 11:45:52.469672
# Unit test for function strftime
def test_strftime():
    assert strftime('%Y-%m-%d', '1375285593') == '2013-07-31'
    assert strftime('%Y-%m-%d', time.time()) == time.strftime('%Y-%m-%d')
    try:
        strftime('%x', 'not float')
        assert False, 'strftime accepted invalid float'
    except AnsibleFilterError as e:
        assert to_text(e) == 'Invalid value for epoch value (not float)'


# Generated at 2022-06-22 11:46:05.017074
# Unit test for function comment
def test_comment():
    expected = """
# -------------------------
# | This is a comment
# | that spans multiple
# | lines.
# -------------------------\n"""
    assert (comment('This is a comment  that spans multiple  lines.', style='plain')) == expected

    expected = """
<!--
  This is an XML style comment
  that spans multiple lines.
-->\n"""
    assert (comment('This is an XML style comment  that spans multiple lines.', style='xml')) == expected

    expected = """
// This is a C style comment
// that spans multiple lines.\n"""
    assert (comment('This is a C style comment  that spans multiple lines.', style='c')) == expected

    expected = """
/* This is a C block style comment
 * that spans multiple lines. */
"""

# Generated at 2022-06-22 11:46:12.640099
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('test1', '(test)', '\\g<1>') == 'test'
    assert regex_search('test1', '(te)', '\\0') == 'te'
    assert regex_search('test1', '(te)', '\\1') == 'st'
    assert regex_search('test1', '(te)', '\\g<1>') == 'st'
    assert regex_search('test1', '(te)(st)(1)', '\\3') == '1'
    assert regex_search('test1', '(te)(st)(1)', '\\g<3>') == '1'
    assert regex_search('test1', '(te)(st)(1)', '\\2', '\\1') == ['st', 'te']

# Generated at 2022-06-22 11:46:22.601647
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    test_string = '''
    test:
        name: foo
        state: absent
    '''
    assert len(to_nice_yaml(test_string, indent=6)) == len(to_nice_yaml(test_string, indent=4))
    assert len(to_nice_yaml(test_string, indent=2)) != len(to_nice_yaml(test_string, indent=4))
    assert len(to_nice_yaml(test_string, indent=2)) == len(to_nice_yaml(test_string, indent=0))
    assert to_nice_yaml(test_string, indent=4) == to_nice_yaml(test_string)

# Generated at 2022-06-22 11:46:26.755802
# Unit test for function regex_escape

# Generated at 2022-06-22 11:46:38.384299
# Unit test for function to_yaml
def test_to_yaml():
    input_ = "{'a': 'b', 'c': 'd'}"
    output = "a: b\nc: d\n"
    assert to_yaml(input_) == output
    input_ = "{'a': 'b', 'c': 'd', 'e': None}"
    output = "a: b\nc: d\ne: null\n"
    assert to_yaml(input_) == output
    input_ = "{'a': 'b', 'c': 'd', 'e': {'f': 'g'}}"
    output = "a: b\nc: d\ne:\n  f: g\n"
    assert to_yaml(input_) == output
    input_ = "{'a': 'b', 'c': 'd', 'e': {'f': ['g']}}"
   

# Generated at 2022-06-22 11:46:49.591306
# Unit test for function regex_search
def test_regex_search():
    regex = '^(?:::f{4,6}:)?(?P<ip>[\da-fA-F]{1,4}(?:::?[\da-fA-F]{1,4}){0,5})$'
    value = '2001:0db8:3c4d:0015:0000:0000:1a2f:1a2b'

    assert regex_search(value, regex, '\\g<ip>') == '2001:0db8:3c4d:0015:0000:0000:1a2f:1a2b'
    assert regex_search(value, regex, '\\1') == '::f:0015::1a2f:1a2b'

# Generated at 2022-06-22 11:47:01.733578
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(u'foo:bar:baz', u'(foo):(bar):(baz)') == 'foo:bar:baz'
    assert regex_search(u'foo:bar:baz', u'(foo):(bar):(baz)', u'\\g<1>') == 'foo'
    assert regex_search(u'foo:bar:baz', u'(foo):(bar):(baz)', u'\\g<2>') == 'bar'
    assert regex_search(u'foo:bar:baz', u'(foo):(bar):(baz)', u'\\g<3>') == 'baz'

# Generated at 2022-06-22 11:47:11.233946
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(value="key0: value\n key1: value\n key2: value", regex="^\s*([^ ]*)") == "key0:"
    assert regex_search(value="key0: value\n key1: value\n key2: value", regex="^\s*([^ ]*)", ignorecase=True) == "key0:"
    assert regex_search(value="key0: value\n key1: value\n key2: value", regex="^\s*([^ ]*)", multiline=True) == "key0:"
    assert regex_search(value="key0: value\n key1: value\n key2: value", regex="^\s*([^0-9]*)", multiline=True) == "key:"

# Generated at 2022-06-22 11:47:24.336646
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('Hello World', 'Hello') == 'Hello'
    assert regex_search('Hello World', 'World') == 'World'
    assert regex_search('Hello World', 'o', '\\g<1>') == 'o'
    assert regex_search('Hello World', 'o', '\\g<0>') == 'o'
    assert regex_search('Hello World', 'o', '\\g<01>') == 'o'
    assert regex_search('Hello World', 'o', '\\1') == 'o'
    assert regex_search('Hello World', 'o', '\\0') == 'o'
    assert regex_search('Hello World', 'o', '\\01') == 'o'
    assert regex_search('Hello World', 'l') == 'l'

# Generated at 2022-06-22 11:47:36.183912
# Unit test for function regex_search

# Generated at 2022-06-22 11:47:48.770819
# Unit test for function regex_search
def test_regex_search():
    # Test cases
    src = [
        # return the match
        "ab",
        # return subpattern matches
        "\\g<1>\\g<2>\\g<1>",
        # return backreferences
        "\\1\\2",
        # return subpattern matches and backreferences
        "\\g<1>\\2",
        # return a combination of both
        "\\1\\g<2>\\3\\g<1>",
        # positional arguments raise error
        "\\1g<1>",
        # invalid backreferences raise error
        "\\4",
        # non-existing backreferences return empty string
        "\\g<3>",
        "\\g<4>",
    ]

# Generated at 2022-06-22 11:47:59.200952
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(r'c', r'[ab]') == 'c'
    assert regex_search(r'c', r'[ab]', '\\1') == 'c'
    assert regex_search(r'a', r'a', '\\g<0>') == 'a'
    assert regex_search(r'a', r'a', '\\g<0>', '\\g<0>') == ['a', 'a']
    assert regex_search(r'a', r'a', '\\g<0>', '\\1') == ['a', 'a']
    assert regex_search(r'a', r'a', '\\1', '\\g<0>') == ['a', 'a']

# Generated at 2022-06-22 11:48:08.173344
# Unit test for function randomize_list
def test_randomize_list():
    import random

    r = random.Random()
    r.seed(1)
    expected = r.sample(range(10), 10)
    assert randomize_list(range(10), seed=1) == expected

    r.seed(2)
    expected = r.sample(range(10), 10)
    assert randomize_list(range(10), seed=2) == expected

    actual = randomize_list(range(10), seed=3)
    assert randomize_list(range(10), seed=3) == actual



# Generated at 2022-06-22 11:48:18.840502
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('test', 'es') == 'es'
    assert regex_search('test', 'es', '\\1') == ['es']
    assert regex_search('test', 'es', '\\g<0>') == 'es'
    assert regex_search('tes', 'tes(t)', '\\g<1>') == ['t']
    assert regex_search('tes', 'tes(t)', '\\1', '\\g<1>') == ['t', 't']
    assert regex_search('test', '(?P<word>es)', '\\g<word>') == 'es'
    assert regex_search('test', '(?P<word>es)', '\\g<word>', '\\g<1>') == ['es', 'es']

# Generated at 2022-06-22 11:48:31.750320
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # Run unit test
    print("Ansible FilterModule implemented in C")
    print("---------------------------------------")

    import doctest
    suite = doctest.DocTestSuite()
    suite.testmod()

    from ansible.template import Template
    import sys
    import os
    import json

    if len(sys.argv) > 1:
        print("\n-----------------------")
        print("Running unit tests")

        print("\n##### Jinja2 tests #####")
        t = Template("testdata/filters.j2")
        print("%s" % t.render({}))

        print("\n##### Filter tests #####")
        t2 = Template("testdata/filters2.j2")
        print("%s" % t2.render({}))

        print("\n##### Templates #####")

# Generated at 2022-06-22 11:48:45.128289
# Unit test for function do_groupby
def test_do_groupby():
    import ansible.template
    template_vars = ansible.template.VarsModule()
    env = ansible.template.AnsibleEnvironment(loader=None, variables=template_vars)
    env.filters['groupby'] = do_groupby

    from ansible.template.safe_eval import safe_eval
    dict1 = dict(ansible=dict(version='2.2.0.0'),
                 ceph=dict(version='1.2.3'))
    _dict1 = safe_eval(repr(dict1))
    assert dict1 == _dict1

    dict2 = dict(ansible=dict(version='2.3.4.0'),
                 ceph=dict(version='2.2.3'))
    _dict2 = safe_eval(repr(dict2))
    assert dict2

# Generated at 2022-06-22 11:48:58.224032
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape("apple") == "apple"

    # list of BRE special chars:
    # https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions
    assert regex_escape("[apple]", re_type="posix_basic") == r"\[apple\]"

    # list of ERE special chars:
    # https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Extended_Regular_Expressions
    # assert regex_escape("(apple)", re_type="posix_extended") == r"\(apple\)"


# Generated at 2022-06-22 11:49:11.114448
# Unit test for function do_groupby
def test_do_groupby():
    l = [1,2,3,4,5,6,7,8,9]
    grouped = do_groupby(l, attr='even')
    assert len(grouped) == 2
    assert grouped[0][0] is True
    assert grouped[1][0] is False
    assert len(grouped[0][1]) == 4
    assert len(grouped[1][1]) == 5
    assert grouped[0][1] == [2,4,6,8]
    assert grouped[1][1] == [1,3,5,7,9]
    #
    l = "string with lots of characters".split()
    grouped = do_groupby(l, attr='len')
    assert len(grouped) == 6
    assert len(grouped[0][1]) == 1

# Generated at 2022-06-22 11:49:19.223325
# Unit test for function regex_search
def test_regex_search():
    test_input = '''
    testA:
      - 'abc'
      - 'abc'
    testB:
      - 'abc'
      - 'abc'
    '''

    regex = 'testA:\s*-\s*(\S+)'
    results = regex_search(test_input, regex, r'\g<1>', r'\g<1>')
    assert results == ['abc', 'abc']
    results = regex_search(test_input, regex, r'\1')
    assert results == ['abc', 'abc']



# Generated at 2022-06-22 11:49:27.204009
# Unit test for function randomize_list
def test_randomize_list():
    # Test using 3 separate seeds
    r = Random(123)
    list1 = ['a', 'b', 'c', 'd', 'e']
    r.shuffle(list1)
    assert randomize_list(['a', 'b', 'c', 'd', 'e'], seed=123) == list1
    r = Random(456)
    list2 = ['a', 'b', 'c', 'd', 'e']
    r.shuffle(list2)
    assert randomize_list(['a', 'b', 'c', 'd', 'e'], seed=456) == list2
    r = Random(789)
    list3 = ['a', 'b', 'c', 'd', 'e']
    r.shuffle(list3)

# Generated at 2022-06-22 11:49:28.666625
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    # TODO: Implement test
    assert True

# Generated at 2022-06-22 11:49:41.850188
# Unit test for function strftime
def test_strftime():
    assert strftime('%Y-%m-%d') == time.strftime('%Y-%m-%d')
    assert strftime('%y-%m-%d') == time.strftime('%y-%m-%d')
    assert strftime('%H-%M',second=1542161288) == '18-09'
    assert strftime('%H-00') == time.strftime('%H-00')
    assert strftime('%Y-%m-%d',second=int(time.time())) == time.strftime('%Y-%m-%d')

# Generated at 2022-06-22 11:49:49.506673
# Unit test for function extract
def test_extract():
    class Object(object):
        value = 'some_value'

    d = dict(k1=Object(),
             k2=dict(k3={'k4': 'test_value'},
                    k5=[{'test': 'another_value'}]))

    assert extract('k1', d) == Object()
    assert extract('value', extract('k1', d)) == 'some_value'
    assert extract('k4', extract('k2', d), 'k3') == 'test_value'
    assert extract('value', extract('k2', d), 'k3', 'k4') == 'test_value'
    assert extract('value', extract('k2', d), 'k3', 'k4') == 'test_value'

# Generated at 2022-06-22 11:50:01.124528
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('bar', r'[a-z]+', '\\0') == 'bar'
    assert regex_search('foo bar baz', r'bar\s*(baz)', '\\g<1>') == 'baz'
    assert regex_search('foo bar baz', r'bar\s*(baz)', '\\g<0>') == 'bar baz'
    assert regex_search('foo bar baz', r'bar\s*(baz)', '\\g<1>', '\\g<0>') == ['baz', 'bar baz']
    assert regex_search('foo bar baz', r'bar\s*(baz)', '\\1') == 'baz'

# Generated at 2022-06-22 11:50:08.575485
# Unit test for function do_groupby
def test_do_groupby():
    """tests whether the do_groupby function work and behaves
    like the original groupby jinja2 filter.
    """
    env = jinja2.Environment()
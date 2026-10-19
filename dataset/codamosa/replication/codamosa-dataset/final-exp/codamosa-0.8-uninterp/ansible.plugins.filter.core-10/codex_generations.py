

# Generated at 2022-06-22 11:40:44.001823
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('aabbcc', 'ab', '\\1', '\\g<1>') == ['a', 'a']
    assert regex_search('aabbcc', 'ab', '\\1', '\\2') == ['a', None]
    assert regex_search('aabbcc', 'ab', '\\1', '\\g<2>') == ['a', None]
    assert regex_search('aabbcc', 'ab', '\\2', '\\g<2>') == [None, None]
    assert regex_search('aabbcc', 'ab', '\\2') == [None]
    assert regex_search(u'aabbcc', u'ab', u'\\1', u'\\g<1>') == [u'a', u'a']

# Generated at 2022-06-22 11:40:51.219369
# Unit test for function ternary
def test_ternary():
    assert ternary(1, 2, 3) == 2
    assert ternary(0, 2, 3) == 3
    assert ternary(None, 2, 3) == 3
    assert ternary(0, 2, None) == None
    assert ternary(None, 2, None) == 2
    assert ternary(1, None, 3) == None
    assert ternary(1, 2, None, 3) == 2
    assert ternary(0, 2, None, 3) == 3
    assert ternary(None, 2, None, 3) == 3



# Generated at 2022-06-22 11:41:02.841725
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo', r'^\w+') == 'foo'
    assert regex_search('foo', r'^\w+', '\\1', '\\g<1>') == ['1', '1']
    assert regex_search('foo', r'^\w+', '\\1', '\\g<1>', '\\2') == ['1', '1', None]
    assert regex_search('foo', r'^\w+', '\\1', '\\g<foo>') == 'ansible.errors.AnsibleFilterError: Unknown argument'
    assert regex_search('foo', r'^\w+', '\\g<foo>') == 'ansible.errors.AnsibleFilterError: Unknown argument'

# Generated at 2022-06-22 11:41:16.664157
# Unit test for function regex_search
def test_regex_search():
    regex_input_1 = "Find patt\\g<1>rn in me\\g<1>"
    regex_input_2 = "Find patt\\1rn in me\\2"
    regex_input_3 = "Find pattern in me"
    regex_input_4 = "Find pattern in me"
    regex_input_5 = "Ansible"
    regex_input_6 = "Ansible"

    # Let's make sure the test will fail if we get an exception
    test_1 = False
    test_2 = False
    test_3 = False
    test_4 = False
    test_5 = False
    test_6 = False


# Generated at 2022-06-22 11:41:28.883700
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(value="this is 123 a test", regex=" (\d+)(\S+) (a) ") == ['123', 'a']
    assert regex_search(value="this is 123 a test", regex=" (\d+)(\S+) (a) ", ignorecase=True) == ['123', 'a']
    assert regex_search(value="this is a test, foo", regex=" (\d+)(\S+) (a) ", multiline=True) == ['123', 'a']
    assert regex_search(value="this is a test, foo", regex=" (\d+)(\S+) (a) ", multiline=True, ignorecase=True) == ['123', 'a']
    assert regex_search(value="this is a test", regex=" (\d+)(\S+) (a) ") is None

# Generated at 2022-06-22 11:41:39.000662
# Unit test for function subelements
def test_subelements():
    subelements(obj=[{'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}], subelements='groups')
    subelements(obj=[{'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}], subelements=['groups'])
    subelements(obj=[{'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}], subelements=['groups'])
    subelements(obj=[{'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}], subelements=['groups'])

# Generated at 2022-06-22 11:41:50.723024
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import Jinja2Environment
    from collections import namedtuple

    FakeGroup = namedtuple('FakeGroup', ['item', 'grouper'])

    def test_do_groupby_namedtuple():
        jenv = Jinja2Environment()
        input_items = [
            FakeGroup('server_1', 1),
            FakeGroup('server_2', 1),
            FakeGroup('server_3', 2),
            FakeGroup('server_4', 2),
            FakeGroup('server_5', 3),
        ]
        grouped = do_groupby(jenv, input_items, 'grouper')
        assert len(grouped) == 3
        assert tuple(grouped[0]) == (1, [('server_1', 1), ('server_2', 1)])

# Generated at 2022-06-22 11:41:52.360896
# Unit test for function mandatory
def test_mandatory():
    assert mandatory([1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-22 11:41:56.191718
# Unit test for function strftime
def test_strftime():
    ret = strftime('%Y')
    assert ret == '1970'
    ret = strftime('%Y', 2)
    assert ret == '1970'
    ret = strftime('%Y', 5.6)
    assert ret == '1970'



# Generated at 2022-06-22 11:42:07.613004
# Unit test for function to_yaml
def test_to_yaml():
    def assert_to_yaml_equal(actual, expected, **kw):
        assert to_yaml(actual, **dict(kw, default_flow_style=False)) == expected, "to_yaml(%r, %r) != %r" % (actual, kw, expected)

    assert_to_yaml_equal(
        [{'test1': {'test2': 'test3', 'test4': 'test5'}}],
        '[{test1: {test2: test3, test4: test5}}]',
    )

# Generated at 2022-06-22 11:42:18.998602
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'name': 'joe', 'uid': 1000, 'groups': ['wheel', 'dev']}) == 'name: joe\nuid: 1000\ngroups:\n- wheel\n- dev\n'


# the JINJA2ENV.filters dictionary does not seem to be updating correctly,
# so we define our own
_FILTERS = dict()


# Generated at 2022-06-22 11:42:31.066192
# Unit test for function comment
def test_comment():
    # Default test. Ensures no exception is thrown
    assert comment('some text')
    # Custom params test
    assert comment('some text', beginning='BEGIN', prefix='PREFIX', decoration='*', postfix='POSTFIX', end='END')
    # Multiline param test
    assert comment('some multiline\ntext', prefix='PREFIX')
    assert comment(text='some multiline\ntext', decoration='*')
    # Predefined params test
    assert comment(text='some text', style='erlang')
    assert comment(text='some text', style='c')
    assert comment(text='some text', style='cblock')
    assert comment(text='some text', style='xml')
    # Param overrides test

# Generated at 2022-06-22 11:42:37.637713
# Unit test for function mandatory
def test_mandatory():
    # Failure 1
    try:
        mandatory(None)
        assert False == True
    except AnsibleFilterError:
        pass
    # Failure 2
    try:
        mandatory(None, "msg")
        assert False == True
    except AnsibleFilterError:
        pass
    # Success 1
    assert mandatory(1)
    # Success 2
    assert mandatory(None, None)
    return True



# Generated at 2022-06-22 11:42:49.314914
# Unit test for function regex_replace
def test_regex_replace():
    ''' regex_replace should return a string '''
    assert isinstance(regex_replace(), string_types)
    ''' regex_replace should replace text from a string '''
    assert regex_replace('ansible', pattern='n[^ ]+e', replacement=' is ') == 'a is ble'
    ''' regex_replace should replace the first match from a string '''
    assert regex_replace('ansible', pattern='n[^ ]+e', replacement=' is ', count=1) == 'a is ble'
    ''' regex_replace should replace the second match from a string '''
    assert regex_replace('ansible ansible', pattern='n[^ ]+e', replacement=' is ', count=1) == 'ansible is ible'



# Generated at 2022-06-22 11:42:51.486044
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    for x in [{'foo': 'bar'}, 'foo', [1,2,3]]:
        assert yaml_load(to_nice_yaml(x)) == x
        assert yaml_load(to_nice_yaml(x, indent=2)) == x
        assert yaml_load(to_nice_yaml(x, indent=100)) == x



# Generated at 2022-06-22 11:42:55.973439
# Unit test for function comment
def test_comment():
    assert comment('', newline='\n') == ''

    assert comment('', style='plain') == ''
    assert comment('', style='plain', beginning='') == ''
    assert comment('', style='plain', beginning='BEGIN') == 'BEGIN\n'
    assert comment('', style='plain', beginning='BEGIN', newline='\n', end='END') == 'BEGIN\nEND\n'

    assert comment(
        '', style='plain', beginning='', prefix='', postfix='', end='') == ''
    assert comment(
        '', style='plain', beginning='', prefix='', postfix='', end='') == ''
    assert comment(
        '', style='plain', beginning='BEGIN', prefix='', postfix='', end='END') == 'BEGIN\nEND\n'
    assert comment

# Generated at 2022-06-22 11:43:01.544646
# Unit test for function fileglob
def test_fileglob():
    assert fileglob("/bin/bash") == ['/bin/bash']
    assert fileglob("/bin/b*") == ['/bin/bash']
    assert fileglob("/bin/___") == []
    assert fileglob("/bin/b???") == []
    assert fileglob("/root/a.txt") == []
    assert fileglob("/root/.gitignore") == []



# Generated at 2022-06-22 11:43:13.007057
# Unit test for function to_yaml
def test_to_yaml():
  print(to_yaml({'a': True, 'b': 3, 'c': 'foo'}))
  print(to_yaml([1, 'two', {'3': None}]))
  print(to_yaml((1, 'two', {'3': None})))
  print(to_yaml(42))
  print(to_yaml('foo'))
  print(to_yaml({'k1': {'k2': {'k3': 'v'}}}, default_flow_style=False))
  print(to_yaml({'k1': {'k2': {'k3': 'v'}}}, default_flow_style=True))

# Generated at 2022-06-22 11:43:14.848566
# Unit test for function regex_findall
def test_regex_findall():
    assert regex_findall('hello world', '\w+') == ['hello', 'world']



# Generated at 2022-06-22 11:43:15.464385
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(42) == 42



# Generated at 2022-06-22 11:43:25.617758
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'foo': 'bar'}) == to_nice_yaml({'foo': 'bar'}, 4) == to_nice_yaml({'foo': 'bar'}, indent=4)
    assert to_nice_yaml({'foo': 'bar'}, 2) == to_nice_yaml({'foo': 'bar'}, indent=2)



# Generated at 2022-06-22 11:43:30.315222
# Unit test for function randomize_list
def test_randomize_list():
    assert sorted(randomize_list([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert sorted(randomize_list([1, 2, 3, 4, 5], seed=100)) == [1, 2, 3, 4, 5]



# Generated at 2022-06-22 11:43:38.293966
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2.environment import Environment

    environment = Environment()
    test = [{'foo': 'bar', 'baz': [1, 2]}]

    assert do_groupby(environment, test, 'foo') == [('bar', [{'foo': 'bar', 'baz': [1, 2]}])]
    assert do_groupby(environment, test, 'baz') == [(1, [{'foo': 'bar', 'baz': [1, 2]}])]



# Generated at 2022-06-22 11:43:42.938423
# Unit test for function randomize_list
def test_randomize_list():
    l = [1,2,3,4,5]
    assert l == randomize_list(l, seed=0)
    try:
        randomize_list('this is not a list')
    except Exception:
        pass
    else:
        # Should raise an exception
        assert False



# Generated at 2022-06-22 11:43:47.621762
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template.safe_eval import AnsibleUndefined
    from jinja2 import DictRuntimeError
    from jinja2 import Undefined
    from ansible.template import Jinja2Environment, AnsibleContext
    from collections import namedtuple

    # "Regular" jinja2 usage
    env = Jinja2Environment()
    value = [1, 2, 3, 4, 5, 6]
    attribute = 'mod(2)'
    res = do_groupby(env, value, attribute)

    assert res == [(False, [1, 3, 5]), (True, [2, 4, 6])]

    # Groupby with ansible.template.safe_eval.safe_eval
    # (first answer in https://stackoverflow.com/questions/32092336/group-by-in-jinja2)

# Generated at 2022-06-22 11:43:55.939790
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    try:
        mandatory(Undefined)
    except AnsibleFilterError as e:
        assert str(e) == 'Mandatory variable not defined.'
    try:
        mandatory(Undefined(name='foo'))
    except AnsibleFilterError as e:
        assert str(e) == "Mandatory variable 'foo' not defined."
    try:
        mandatory(Undefined(name='foo'), msg='bar')
    except AnsibleFilterError as e:
        assert str(e) == 'bar'
    print("Successfully passed tests for 'mandatory' filter")



# Generated at 2022-06-22 11:44:05.563309
# Unit test for function regex_findall
def test_regex_findall():
    assert regex_findall("unit", r"unit") == ["unit"]
    assert regex_findall("unit unit", r"unit") == ["unit", "unit"]
    assert regex_findall("unit unit unit", r"unit") == ["unit", "unit", "unit"]
    assert regex_findall("unit unit unit", r"unit", ignorecase=True) == ["unit", "unit", "unit"]
    assert regex_findall("unit unit unit", r"unit", ignorecase=False) == ["unit", "unit", "unit"]
    assert regex_findall("Unit Unit Unit", r"unit", ignorecase=True) == ["Unit", "Unit", "Unit"]
    assert regex_findall("Unit Unit Unit", r"unit", ignorecase=False) == []

# Generated at 2022-06-22 11:44:16.650808
# Unit test for function do_groupby
def test_do_groupby():
    """Ensure that do_groupby returns a list of tuples, even with
    jinja>2.9.0,<2.9.5
    """
    from jinja2.environment import Environment
    from jinja2.runtime import Context
    from copy import copy
    from ansible.template.safe_eval import safe_eval

    class DummyNamedtuple(tuple):
        _fields = 500

        def __repr__(self):
            return "DummyNamedtuple(%s)" % (', '.join(self))

    # the namedtuple would cause a TypeError in safe_eval, but the
    # tuple is evaluated properly
    safe_eval(str(DummyNamedtuple((1, 2, 3, 4, 5))))

    # set up a jinja2 Environment and Context to call

# Generated at 2022-06-22 11:44:18.375801
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('foo', 'oo', 'uu') == 'fuu'



# Generated at 2022-06-22 11:44:27.630903
# Unit test for function strftime
def test_strftime():
    assert strftime('%Y/%m/%d/%H') == time.strftime('%Y/%m/%d/%H', time.localtime(None))
    assert strftime('%Y/%m/%d/%H', 1464661862.35261) == "2016/06/02/10"
    assert strftime('%Y/%m/%d/%H', '1464661862.35261') == "2016/06/02/10"
    assert strftime('%Y/%m/%d/%H', 'invalid') == "2016/06/02/13"



# Generated at 2022-06-22 11:44:48.371721
# Unit test for function comment
def test_comment():
    assert comment('text') == '# text'
    assert comment('text\n') == '# text\n'
    assert comment('text\n', newline='\r') == '# text\r'
    assert comment('text\n', newline='\r\n') == '# text\r\n'
    assert comment('text\n', newline='\r\n', prefix='>>> ', prefix_count=0) == 'text\r\n'
    assert comment('text\n', newline='\r\n', prefix='>>> ', prefix_count=1) == '>>> text\r\n'
    assert comment('text\n', newline='\r\n', prefix='>>> ', prefix_count=2) == '>>> \r\n>>> text\r\n'

# Generated at 2022-06-22 11:44:49.873301
# Unit test for function extract
def test_extract():
    assert extract({}, 'b', {'a': {'b': 'c'}}) == 'c'
    assert extract({}, 'b', {'a': {'b': 'c'}}, 'a') == 'c'



# Generated at 2022-06-22 11:44:56.873679
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo bar baz', r'b.*', '\\g<0>') == 'bar'
    assert regex_search('foo bar baz', r'b.*', '\\g<1>', ignorecase=True) == 'ar'
    assert regex_search('foo bar baz', r'b.*', *['\\g<0>', '\\1'], ignorecase=True) == ['bar', 'ar']



# Generated at 2022-06-22 11:45:05.459420
# Unit test for function randomize_list
def test_randomize_list():
    a = ['e', 'a', 'p', 'q', 'i', 'm', 'u', 'c', 'o', 'x']
    b = randomize_list(a, seed='seed_1')
    for x in b:
        if x not in a:
            raise AssertionError('Randomized list contains unexpected element: {0}'.format(x))
    a.sort()
    b.sort()
    for x in range(len(a)):
        if a[x] != b[x]:
            raise AssertionError('Randomized list not as expected.')
    a.sort()
    b = randomize_list(a)
    for x in b:
        if x not in a:
            raise AssertionError('Randomized list contains unexpected element: {0}'.format(x))

# Generated at 2022-06-22 11:45:08.820283
# Unit test for function regex_replace
def test_regex_replace():
    test_value = regex_replace(value='Example String to replace', pattern='Example Pattern', replacement='Replaced Pattern')
    result_value = "Replaced Pattern String to replace"
    assert test_value == result_value



# Generated at 2022-06-22 11:45:18.140721
# Unit test for function regex_search
def test_regex_search():
    ''' Test regex_search filter '''
    assert regex_search("foobar", "oo", "\\g<1>") == 'oo'
    assert regex_search("foobar", "oo", "\\g<1>", "\\g<1>") == ['oo', 'oo']
    assert regex_search("foobar", "o(o)", "\\g<1>", "\\1") == ['o', 'o']
    assert regex_search("foobar", "o(o)", "\\1", "\\g<1>") == ['o', 'o']
    assert regex_search("foobar", "z", "\\1") == None



# Generated at 2022-06-22 11:45:21.134696
# Unit test for function extract
def test_extract():
    c = {'a': {'b': {'c': 'd'}}}
    assert extract('c', c) == 'd'
    assert extract('c', c, 'a') == 'd'
    assert extract('b', c, 'a') == {'c': 'd'}
    assert extract(['a', 'b'], c) == {'c': 'd'}
    assert extract(['c', 'd'], c) == None
    assert extract('c', c, 'a', 'b') == 'd'


# Generated at 2022-06-22 11:45:23.556309
# Unit test for function mandatory
def test_mandatory():
    from . import env_var
    env_var.set('x', 1)
    assert mandatory(env_var.get('y')) is None


# Generated at 2022-06-22 11:45:28.359950
# Unit test for function get_hash
def test_get_hash():
    assert get_hash(to_bytes('hello world'), 'sha1') == get_hash('hello world', 'sha1')
    assert get_hash(1234, 'md5') == get_hash('1234', 'md5')



# Generated at 2022-06-22 11:45:37.954507
# Unit test for function mandatory

# Generated at 2022-06-22 11:45:44.846993
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]



# Generated at 2022-06-22 11:45:51.530960
# Unit test for function regex_search
def test_regex_search():
    s = '''This is a line of text
    this is another line of text
    '''
    line = regex_search(s, '.*line')
    assert type(line) is unicode
    assert line == u'This is a line of text'
    lines = regex_search(s, '.*line', '\\g<1>\\g<2>')
    assert type(line) is unicode
    assert len(lines) == 2
    assert lines[0] == u' of '
    assert lines[1] == u'text'



# Generated at 2022-06-22 11:45:54.282074
# Unit test for function extract
def test_extract():
    container = {'a': {'b': {'c': 'd'}}}
    assert extract('c', container) == 'd'
    assert extract('c', container, 'a') == 'd'
    assert extract('c', container, ['a', 'b']) == 'd'
    assert extract(['c'], container, ['a', 'b']) == 'd'
    assert extract(['c', 'd'], container, ['a']) == 'd'



# Generated at 2022-06-22 11:45:56.741494
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'a': 'b'}, indent=1) == to_nice_yaml({'a': 'b'})


# Generated at 2022-06-22 11:46:09.383204
# Unit test for function fileglob
def test_fileglob():
    import tempfile
    (fd, file1) = tempfile.mkstemp()
    os.write(fd, b"test1")
    os.close(fd)
    (fd, file2) = tempfile.mkstemp()
    os.write(fd, b"test2")
    os.close(fd)
    (fd, file3) = tempfile.mkstemp()
    os.write(fd, b"test3")
    os.close(fd)
    (fd, file4) = tempfile.mkstemp(text=True)
    os.write(fd, b"test4")
    os.close(fd)
    assert fileglob(file1) == [file1]
    assert fileglob([file1]) == [file1]

# Generated at 2022-06-22 11:46:16.437739
# Unit test for function flatten
def test_flatten():
    assert flatten(['foo', 'bar', ['baz', ['qux']]]) == ['foo', 'bar', 'baz', 'qux']
    assert flatten(['foo', 'bar', ['baz', ['qux']]], levels=1) == ['foo', 'bar', 'baz', ['qux']]
    assert flatten(['foo', 'bar', [None], ['baz', ['qux']]], skip_nulls=False) == ['foo', 'bar', None, 'baz', 'qux']



# Generated at 2022-06-22 11:46:24.168048
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    from ansible import constants as C
    yaml.indent(mapping=4, sequence=6, offset=3)
    assert to_nice_yaml({"key": "value"}) == "{key: value}"
    assert to_nice_yaml({"key": "value"}, indent=2) == "{\n  key: - value\n}"
    C.DEFAULT_YAML_INDENT = 2
    assert to_nice_yaml({"key": "value"}) == "{\n  key: - value\n}"
    C.DEFAULT_YAML_INDENT = 4



# Generated at 2022-06-22 11:46:37.279161
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('hello world', 'l(o)', r'\1') == 'heo world'
    assert regex_replace('hello world', '(?P<greeting>hel+o)', r'\g<greeting> there') == 'hello there world'
    assert regex_replace('hello world', 'z', r'\g<0>') == 'hello world'
    assert regex_replace('hello world', 'l', r'\L') == 'heLLo world'
    assert regex_replace('hello world', 'l', r'\u') == 'heu+00ao world'
    assert regex_replace('hello world', 'l', r'\U') == 'heU+000Ao world'
    assert regex_replace('hello world', 'l', r'\Q') == 'heQlo world'
   

# Generated at 2022-06-22 11:46:49.195369
# Unit test for function comment
def test_comment():
    assert comment('text', 'plain', newline='\n') == \
        '# text'
    assert comment('text', 'erlang', newline='\n') == \
        '% text'
    assert comment('text', 'c', newline='\n') == \
        '// text'
    assert comment('text', 'cblock', newline='\n') == \
        '/*\n * text\n */'
    assert comment('text', newline='\n') == \
        '# text'

    assert comment('text', 'plain', newline='\r\n') == \
        '# text\r\n'
    assert comment('text', 'erlang', newline='\r\n') == \
        '% text\r\n'

# Generated at 2022-06-22 11:46:59.513165
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(value="foobar", pattern="a", replacement="y") == "foybory"
    assert regex_replace(value="foobar", pattern="a", replacement="y", ignorecase=True) == "foybory"
    assert regex_replace(value="A", pattern="a", replacement="y", ignorecase=True) == "y"
    assert regex_replace(value="A", pattern="a", replacement="y", ignorecase=False) == "A"
    assert regex_replace(value="foo\nbar\nzot", pattern="a", replacement="y", multiline=True) == "foy\nbory\nzot"
    assert regex_replace(value="foo\nbar\nzot", pattern="a", replacement="y", multiline=False) == "foo\nbar\nzot"
   

# Generated at 2022-06-22 11:47:08.980495
# Unit test for function strftime
def test_strftime():
    assert strftime("%Y-%m-%d %H:%M:%S", "1506276994") == "2017-09-25 14:36:34"
    assert strftime("%Y-%m-%d %H:%M:%S", "1506276994.1234567890") == "2017-09-25 14:36:34"



# Generated at 2022-06-22 11:47:22.149928
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    from jinja2.exceptions import UndefinedError

    # Ensure we get an error for undefined
    try:
        mandatory(Undefined)
    except AnsibleFilterError as e:
        assert "Mandatory variable '' not defined." in to_native(e)

    # Ensure we get an error for undefined
    try:
        mandatory(Undefined(name='foo'))
    except AnsibleFilterError as e:
        assert "Mandatory variable 'foo' not defined." in to_native(e)

    # Ensure we get a custom message
    try:
        mandatory(Undefined(name='foo'), "This should never happen.")
    except AnsibleFilterError as e:
        assert "This should never happen." in to_native(e)

    # Ensure we get no error for defined

# Generated at 2022-06-22 11:47:32.872823
# Unit test for function fileglob
def test_fileglob():
    # setup file list to use
    files = ['./test_filter_plugins/file1.tmp', './test_filter_plugins/file2.tmp']
    if sys.version_info >= (3, 6):
        import pathlib
        for path in files:
            pathlib.Path(path).touch()
    else:
        import tempfile
        for i in range(0, len(files)):
            # create a temporary file
            file = tempfile.TemporaryFile()
            # we close it because we just wanted to create the file
            file.close()
            # Rename the temporary file to the desired name
            os.rename(file.name, files[i])

    # test fileglob

# Generated at 2022-06-22 11:47:45.702977
# Unit test for function extract
def test_extract():
    from jinja2 import Environment

    environment = Environment()
    assert extract(environment, 'k1', {'k1': 'v1'}) == 'v1'
    assert extract(environment, 'k1', {'k1': 'v1', 'k2': 'v2'}) == 'v1'
    assert extract(environment, 'k1', {'k1': {'k2': 'v2'}}) == {'k2': 'v2'}
    assert extract(environment, 'k2', {'k1': {'k2': 'v2'}}) == 'v2'
    assert extract(environment, 'k1', {'k1': {'k2': 'v2'}}, 'k2') == 'v2'

# Generated at 2022-06-22 11:47:49.324636
# Unit test for function strftime
def test_strftime():
    second = 1429784380
    assert strftime('%Y-%m-%d %H:%M:%S', second) == '2015-04-27 14:03:00'



# Generated at 2022-06-22 11:47:56.418716
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list([1,2,3]) != [1,2,3]
    assert randomize_list([1,2,3], seed=None) != [1,2,3]
    assert randomize_list([1,2,3], seed='foobar') != [1,2,3]
    assert randomize_list([1,2,3], seed='foobar') == randomize_list([1,2,3], seed='foobar')



# Generated at 2022-06-22 11:47:59.839523
# Unit test for function fileglob
def test_fileglob():
    assert len(fileglob("*.py")) > 1



# Generated at 2022-06-22 11:48:12.268431
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import Jinja2Environment, AnsibleJ2Template, DictLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import generate_ansible_template_vars, ansible_native_convert_data

    class FakeVarsModule(object):
        def __init__(self, data, basedir, env):
            self.basedir = basedir
            self.data = data
            self.env = env

    class FakeHost(object):
        def __init__(self, vars_copy):
            self.vars = vars_copy

    # FakeArgs creates the basic context that ansible runs in,
    # and is sufficient for this test to run.

# Generated at 2022-06-22 11:48:20.452774
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    undef = Undefined()
    undef._undefined_name = None
    assert mandatory(1) == 1
    try:
        mandatory(undef)
    except AnsibleFilterError as e:
        assert to_native(e) == 'Mandatory variable \'\' not defined.'
        pass

    assert mandatory(1, msg="this is a custom warning") == 1
    try:
        mandatory(undef, msg="this is a custom warning")
    except AnsibleFilterError as e:
        assert to_native(e) == 'this is a custom warning'
        pass
    else:
        assert False, "AnsibleFilterError should be raised"

    undef._undefined_name = "customvar"

# Generated at 2022-06-22 11:48:29.710258
# Unit test for function regex_replace
def test_regex_replace():
    '''Test the regex_replace filter'''
    from ansible.errors import AnsibleFilterError
    from ansible.template import Templar
    from ansible.vars import VariableManager


# Generated at 2022-06-22 11:48:36.028504
# Unit test for function extract
def test_extract():
    environment = Environment()
    test_dict = {'a': {'b': {'c': 'd'}}}
    assert extract(environment, 'c', test_dict, 'b') == 'd'
    assert extract(environment, 'c', test_dict, ['b']) == 'd'



# Generated at 2022-06-22 11:48:38.467970
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    x = Undefined('x')
    assert mandatory(x) is None
# --



# Generated at 2022-06-22 11:48:41.039338
# Unit test for function fileglob
def test_fileglob():
    files = fileglob('/etc/*')
    for file in files:
        assert os.path.isfile(file)



# Generated at 2022-06-22 11:48:50.221884
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml(dict(a=5, b=6)) == "a: 5\nb: 6\n"
    assert to_yaml([1,[2,3]]) == "- 1\n- - 2\n  - 3\n"
    assert to_yaml(dict(a=5, b=6), default_flow_style=True) == "{a: 5, b: 6}\n"
    assert to_yaml([1,[2,3]], default_flow_style=True) == "[1, [2, 3]]\n"


# Generated at 2022-06-22 11:49:01.791136
# Unit test for function mandatory
def test_mandatory():
    # Tests for unconditionally failing conditions
    assert isinstance(mandatory(None), None.__class__)
    assert isinstance(mandatory([3, 2, 1]), list)
    assert isinstance(mandatory(3), int)
    assert isinstance(mandatory('test string'), str)
    assert isinstance(mandatory(True), bool)
    assert isinstance(mandatory(dict()), dict)
    assert isinstance(mandatory((2, 2)), tuple)

    # Tests for conditionally failing conditions
    try:
        mandatory(AnsibleUndefined)
    except AnsibleFilterError as e:
        assert str(e) == 'Mandatory variable not defined.'
    else:
        assert False


# Generated at 2022-06-22 11:49:11.104236
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    class AnsibleUndefined_exception(AnsibleUndefined):
        def __repr__(self):
            return "AnsibleUndefined"

    assert mandatory(1) == 1
    assert mandatory(AnsibleUndefined_exception()) == 'AnsibleUndefined'
    try:
        assert mandatory(AnsibleUndefined_exception(), "test") == "test"
        assert False
    except AnsibleFilterError as e:
        assert e.message == "test"



# Generated at 2022-06-22 11:49:19.608968
# Unit test for function extract
def test_extract():
    env = DummyEnvironment()
    assert extract(env, 'a', {'a': {'b': 'c'}}, []) == {'b': 'c'}
    assert extract(env, 'a', {'a': {'b': 'c'}}, 'b') == 'c'
    assert extract(env, 'a', {'a': {'b': 'c'}}, ['a', 'b']) == 'c'
    assert extract(env, 'a', {'a': {'b': 'c'}}, morekeys=['a', 'b']) == 'c'



# Generated at 2022-06-22 11:49:22.919282
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/bin/ls') == ['/bin/ls']
    assert fileglob('/bin/ls*') == ['/bin/ls']
    assert fileglob('/bin/??') == ['/bin/ls']



# Generated at 2022-06-22 11:49:34.343981
# Unit test for function randomize_list
def test_randomize_list():
    mylist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
    seed = 30

    # Seed is a value of type int.
    new_random_list = randomize_list(mylist, seed)

# Generated at 2022-06-22 11:49:45.026518
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.module_utils._text import to_text
    from ansible.template import Templar
    from ansible.template.vars import AnsibleJ2Vars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Compile the jinja expression
    from jinja2 import Environment
    from ansible.plugins.filter.core import FilterModule
    core_filters = FilterModule().filters()
    env = Environment(extensions=core_filters.keys())
    env.filters.update(core_filters)
    t = env.from_string("{{ mylist | groupby('name') | list }}")

    # Setup the jinja2 environment
    vars_loader = Data

# Generated at 2022-06-22 11:50:00.117964
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('abcdefg', r'a(.{2})c', '--\\1--') == '--bde--fg'
    assert regex_replace('abcdefg', r'x(.{2})z', '--\\1--') == 'abcdefg'
    assert regex_replace('hello', r'x(.{2})z', '--\\1--') == 'hello'
    assert regex_replace('hello', r'x(.{2})z', '--\\1--', ignorecase=True) == 'hello'
    assert regex_replace('hello', r'(?i)x(.{2})z', '--\\1--') == 'hello'

# Generated at 2022-06-22 11:50:08.392826
# Unit test for function mandatory
def test_mandatory():
    def callback(v):
        return '_' + v + '_'
    env = {
        'variable': 'Foo',
        'undefined': AnsibleUndefined,
        'mandatory': mandatory,
        'callback': callback,
        'jsonstring': json.dumps({'answer': 42}),
    }
    assert mandatory('Foo') == 'Foo'
    assert mandatory(42) == 42
    assert mandatory(42.0) == 42.0
    assert mandatory(True)
    assert not mandatory(False)
    assert mandatory(False) == False
    assert mandatory(None) == None
    assert mandatory(env['undefined']) == env['undefined']
    # Test that the mandatory filter can take a callable as its first argument
    assert mandatory(callback, 'bla') == '_bla_'

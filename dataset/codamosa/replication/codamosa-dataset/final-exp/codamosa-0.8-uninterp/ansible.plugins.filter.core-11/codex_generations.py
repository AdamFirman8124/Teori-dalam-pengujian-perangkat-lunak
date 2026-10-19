

# Generated at 2022-06-22 11:40:43.844553
# Unit test for function fileglob
def test_fileglob():
    assert fileglob("") == []
    assert fileglob("/dev/null") == ["/dev/null"]
    assert fileglob("somefile") == []
    assert fileglob("somefile") == []
    assert fileglob("*.pyc") == []
    assert fileglob("*.sh") == []


# Generated at 2022-06-22 11:40:51.803098
# Unit test for function fileglob
def test_fileglob():
    from ansible import constants as C
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    path1 = os.path.join(C.DEFAULT_TEST_DIR, 'test1.txt')
    if not os.path.exists(path1):
        raise AnsibleFilterError(u'Could not find test file %s' % path1)
    path2 = os.path.join(C.DEFAULT_TEST_DIR, 'test2.txt')
    if not os.path.exists(path2):
        raise AnsibleFilterError(u'Could not find test file %s' % path2)
    pathname = os.path.join(C.DEFAULT_TEST_DIR, 'test*.txt')
    testfiles = fileglob(pathname)

# Generated at 2022-06-22 11:41:02.973097
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    assert mandatory(1) == 1
    if sys.version_info >= (3, 0):
        assert mandatory(None) is None
    else:
        assert mandatory(None) == "None"
    assert mandatory('') == ''
    assert mandatory(0) == 0
    assert mandatory(0.0) == 0.0

    assert mandatory([0, 1]) == [0, 1]
    assert mandatory({'a': 'b'}) == {'a': 'b'}

    try:
        mandatory(Undefined)
    except Exception as e:
        assert isinstance(e, AnsibleFilterError)

    try:
        mandatory(Undefined(name='foo'))
    except Exception as e:
        assert isinstance(e, AnsibleFilterError)

# Generated at 2022-06-22 11:41:09.466403
# Unit test for function fileglob
def test_fileglob():
    pathname = ".gitignore"
    assert fileglob(pathname) == ['.gitignore']
    pathname = "../*.py"
    assert fileglob(pathname) == []
    pathname = "../lib/ansible/*.py"
    assert fileglob(pathname) != []



# Generated at 2022-06-22 11:41:20.692427
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    Undefined().__nonzero__ = lambda _: False
    Undefined().__bool__ = lambda _: False

    a = None
    b = ""
    c = "c"
    d = 0
    e = 1
    f = []
    g = [1]
    h = {}
    i = {'a': 'a'}
    j = Undefined(name='j')
    k = Undefined(name='k')

    # Test the inversion of truth
    assert mandatory(a) is None
    assert mandatory(b) is None
    assert mandatory(c) == 'c'
    assert mandatory(d) is None
    assert mandatory(e) == 1
    assert mandatory(f) is None
    assert mandatory(g) == [1]
    assert mandatory(h)

# Generated at 2022-06-22 11:41:25.642981
# Unit test for function comment
def test_comment():
    assert (comment('Test', style='plain') == '# Test')
    assert (comment('Test', style='cblock') == '/*\n * Test\n */')
    assert (comment('Test', style='c', prefix='// ') == '// Test')
    assert (comment('Test', style='erlang') == '% Test')
    assert (comment('Test', style='xml') == '<!--\n - Test\n-->')
    assert (comment('Test\nTest', style='plain', decoration='# ') == '# Test\n# Test')
    assert (comment('Test\nTest', style='plain', decoration='# ', newline='\n') == '# Test\n# Test')

# Generated at 2022-06-22 11:41:37.636626
# Unit test for function do_groupby

# Generated at 2022-06-22 11:41:43.477127
# Unit test for function fileglob
def test_fileglob():
  assert fileglob('test/ansible/roles/test/templates/{action}/{{foo,bar}}') == ['test/ansible/roles/test/templates/{action}/{{foo,bar}}']


# Generated at 2022-06-22 11:41:53.173696
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('^$') == '\\^\\$'
    assert regex_escape('^$', re_type='posix_basic') == '\\^\\$'  # Legacy behavior
    assert regex_escape('\\a', re_type='posix_basic') == '\\a'
    assert regex_escape('\\|') == '\\\\\\|'

    # Related code: ansible/plugins/filter/regex.py
    assert regex_escape('foo') == 'foo'
    assert regex_escape('foo.*') == 'foo\\.\\*'
    assert regex_escape('foo.*', re_type='posix_basic') == 'foo\\.\\*'
    assert regex_escape('foo.\\') == 'foo\\.\\\\'
    assert regex_escape('foo.\\', re_type='posix_basic')

# Generated at 2022-06-22 11:42:02.945122
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/resolv.conf') == ['/etc/resolv.conf']
    assert fileglob('/etc/resolv.conf*') == ['/etc/resolv.conf']
    assert fileglob('/etc/resolv.conf*a') == []
    assert fileglob('/etc/resolv.conf*a*') == ['/etc/resolv.conff.bak']
    assert fileglob('/etc/resolv.conf*a*b') == []
    assert fileglob('/etc/resolv.conf*a*b*') == []



# Generated at 2022-06-22 11:42:17.413436
# Unit test for function comment
def test_comment():
    fail_msg = "Test failed for comment(style=%r)"
    assert comment(
        "Test text", style="erlang") == (
            "% Test text"
        ), fail_msg % "erlang"
    assert comment(
        "Test text", style="c") == (
            "// Test text"
        ), fail_msg % "c"
    assert comment(
        "Test text", style="cblock") == (
            "/*\n"
            " * Test text\n"
            " */"
        ), fail_msg % "cblock"
    assert comment(
        "Test text", style="xml") == (
            "<!--\n"
            " - Test text\n"
            "-->"
        ), fail_msg % "xml"

# Generated at 2022-06-22 11:42:28.739326
# Unit test for function combine
def test_combine():
    def from_yaml(data):
        if isinstance(data, string_types):
            return yaml.safe_load(to_text(data))
        return data

    def recursive_check(a):
        if isinstance(a, dict):
            for key, value in iteritems(a):
                if isinstance(value, string_types):
                    raise AnsibleUndefined('%s is not defined.' % value)
                recursive_check(value)
        elif isinstance(a, list):
            for value in a:
                recursive_check(value)

    def kw(**kwargs):
        return kwargs


# Generated at 2022-06-22 11:42:35.049252
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml([1,2,3]) == '- 1\n- 2\n- 3\n'
    assert to_yaml([{'name': 'Bob'}, {'name': 'Alice'}]) == '- name: Bob\n- name: Alice\n'
    assert to_yaml({"one": 1, "two": [{"three": [1, 2, 3]}]}, default_flow_style=False) == 'one: 1\ntwo:\n- three:\n  - 1\n  - 2\n  - 3\n'


# Generated at 2022-06-22 11:42:40.469049
# Unit test for function regex_search
def test_regex_search():
    # Test when no group
    my_str = "one,two,three"
    regex = r"^(\S+),(\S+),(\S+)$"
    regex_out = regex_search(my_str, regex, '\\g<2>', '\\g<3>')
    assert regex_out[0] == 'two'
    assert regex_out[1] == 'three'
    # Test with backreference
    regex_out = regex_search(my_str, regex, '\\2', '\\3')
    assert regex_out[0] == 'two'
    assert regex_out[1] == 'three'
    # Test with multiple keywords
    my_str = "one,Two,Three"

# Generated at 2022-06-22 11:42:51.328753
# Unit test for function flatten
def test_flatten():

    from ansible_collections.rubrikinc.cdm.plugins.module_utils.helpers import flatten

    assert flatten([[1, 2, 3], 4, [5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, 2, 3], 4, [5, 6]], levels=2) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, 2, [3, 4]], 5, [6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, 2, [3, 4]], 5, [6]], levels=2) == [1, 2, 3, 4, 5, 6]

# Generated at 2022-06-22 11:43:00.169608
# Unit test for function mandatory
def test_mandatory():
    # mandatory() without msg
    assert mandatory('foo') == 'foo'
    assert mandatory(None, msg='foo') == 'foo'
    try:
        mandatory(None)
        assert 1 == 0, "mandatory() failed to raise exeption when variable is None."
    except AnsibleFilterError as e:
        assert to_text(e) == "Mandatory variable not defined."

    # mandatory() with msg
    assert mandatory('foo', msg="foo") == 'foo'
    assert mandatory(None, msg="foo") == 'foo'
    try:
        mandatory(None, msg='foo')
        assert 1 == 0, "mandatory() failed to raise exeption when variable is None."
    except AnsibleFilterError as e:
        assert to_text(e) == "foo"



# Generated at 2022-06-22 11:43:12.831616
# Unit test for function to_bool
def test_to_bool():
    ''' to_bool should return a bool or raise a TypeError '''
    true_values = [True, 'True', 'true', 1, '1', 'ON', 'On', 'on', 'YES',
                   'Yes', 'yes', 'y', 'Y']
    false_values = [False, 'False', 'false', 0, '0', 'OFF', 'Off', 'off', 'NO',
                    'No', 'no', 'n', 'N']
    for v in true_values:
        assert to_bool(v) is True
    for v in false_values:
        assert to_bool(v) is False
    bad_values = [2, 'a', 'foo', list(), dict()]

# Generated at 2022-06-22 11:43:19.459412
# Unit test for function randomize_list
def test_randomize_list():
    ''' Test randomize_list() '''
    test_env = {'vars': {'test_seed': 42}}
    assert randomize_list(['a', 'b', 'c']) == ['a', 'c', 'b']
    assert randomize_list(['a', 'b', 'c'], seed=test_env['vars']['test_seed']) == ['c', 'a', 'b']



# Generated at 2022-06-22 11:43:26.198541
# Unit test for function randomize_list
def test_randomize_list():
    mylist = [1,2,3,4,5]
    assert randomize_list(mylist) != mylist
    assert randomize_list(mylist) != randomize_list(mylist)
    assert randomize_list(mylist, seed=1) == randomize_list(mylist, seed=1)
    assert randomize_list(mylist, seed=1) != randomize_list(mylist, seed=2)



# Generated at 2022-06-22 11:43:38.166697
# Unit test for function extract
def test_extract():
    if extract(({'a': {'k': 'v'}}, 'a', 'k')) != 'v':
        raise AssertionError('extract must work with 2 parameters')
    if extract(({'a': None}, 'a', 'k')) is not None:
        raise AssertionError('extract must be able to return None')
    if extract(({'a': {'k': 'v'}}, 'a', 'k', 'more')) is not None:
        raise AssertionError('extract must not recurse to 3 depth (since key "more" was not found)')

# Generated at 2022-06-22 11:43:44.749950
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('yay') == 'yay'
    try:
        mandatory(None)
    except Exception:
        pass
    else:
        assert False, "should have raised an exception"

    # This does not seem to actually be the case
    #try:
    #    mandatory(undefined)
    #except Exception, e:
    #    assert "Mandatory variable 'myvar' not defined." in str(e)
    #else:
    #    assert False, "should have raised an exception"



# Generated at 2022-06-22 11:43:57.441589
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('hello', 'h') == 'h'
    assert regex_search('hello', '^h') == 'h'
    assert regex_search('hello', 'h$') == 'h'
    assert regex_search('hello', 'l') == 'l'
    assert regex_search('hello', 'l$') == 'l'
    assert regex_search('hello', '^l') == 'l'
    assert regex_search('hello', 'el') == 'el'
    assert regex_search('hello', 'x') is None
    assert regex_search('hello', 'hello') == 'hello'
    assert regex_search('hello', '^hello$') == 'hello'
    assert regex_search('foo\nbar', '^bar') == 'bar'

# Generated at 2022-06-22 11:44:02.958194
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list([1, 2.0, u'3']) == [1, u'3', 2.0]  # possible
    assert randomize_list([1, 2.0, u'3'], 'foo') == [u'3', 2.0, 1]  # deterministic
    assert randomize_list(123) == 123
    assert randomize_list(None) == None



# Generated at 2022-06-22 11:44:15.102031
# Unit test for function do_groupby
def test_do_groupby():
    # Define groupby array:
    class A(object):
        def __init__(self, name, number):
            self.name = name
            self.number = number
    class B(object):
        def __init__(self, name, number):
            self.name = name
            self.number = number
    aset = [A(name,number) for name,number in [
        ('base','1'),
        ('base','2'),
        ('custom','1'),
        ('custom','2'),
        ('custom','3'),
        ('custom','4')]]
    bset = [B(name,number) for name,number in [
        ('base','1'),
        ('base','2'),
        ('custom','1'),
        ('custom','2'),
        ('custom','3'),
        ('custom','4')]]


# Generated at 2022-06-22 11:44:20.401493
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    d = {'a':1, 'b':{'c':'d', 'e':'f'}}
    nice_yaml = to_nice_yaml(d)
    assert nice_yaml == "a: 1\nb:\n    c: d\n    e: f\n"


# Generated at 2022-06-22 11:44:31.829647
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(value='Hello world', pattern='(\w+)', replacement=r'\1\1') == 'Hello worldHello world'
    assert regex_replace(u'Stark\nSnow', pattern='.*\n', replacement=r'\1\1', multiline=True) == 'StarkStark'
    assert regex_replace(u'Stark\nSnow', pattern='.*\n', replacement=r'\1\1') == 'Snow'
    assert regex_replace(u'Stark\nSnow', pattern='(.*)(\n)(.*)', replacement=r'\2\2', multiline=True) == '\n\nSnow'

# Generated at 2022-06-22 11:44:43.825855
# Unit test for function mandatory
def test_mandatory():
    # pylint: disable=undefined-variable,unused-variable
    from jinja2.runtime import Undefined
    from jinja2 import Environment
    from ansible.compat.tests import unittest

    tests = unittest.TestCase('__init__')
    env = Environment()

    def do_test(test_name, j2_vars, expected_exception=AnsibleFilterError, fixture_msg=None, fixture_name=None):
        ''' DRY function for tests that are parameterized '''
        msg = fixture_msg
        if fixture_name is not None:
            msg = "Mandatory variable '%s' not defined." % fixture_name

        def do_assert(exc):
            ''' DRY function to assert exceptions '''

# Generated at 2022-06-22 11:44:47.221715
# Unit test for function mandatory
def test_mandatory():
    try:
        mandatory('', 'my message')
    except AnsibleFilterError as err:
        assert 'my message' in to_native(err)
    else:
        assert 0 == 1

    try:
        mandatory(None)
    except AnsibleFilterError as err:
        assert 'Mandatory' in to_native(err)
    else:
        assert 0 == 1

    assert mandatory('foo') == 'foo'



# Generated at 2022-06-22 11:44:56.049898
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("foobar", r"foo") == "foo"
    assert regex_search("foobar", r"bar") == "bar"
    assert regex_search("foobar", r"^foo", ignorecase=True) == "foo"
    assert regex_search("foobar", r"^bar", ignorecase=True) == "bar"
    assert regex_search("foobar", r"^foo", ignorecase=False) == "foo"
    assert regex_search("foobar", r"^bar", ignorecase=False) == "bar"
    assert regex_search("foo\nbar", r"^foo", multiline=True) == "foo"
    assert regex_search("foo\nbar", r"^bar", multiline=True) == "bar"

# Generated at 2022-06-22 11:45:00.675199
# Unit test for function strftime
def test_strftime():
    assert strftime('%Y-%m-%d %H:%M:%S') == time.strftime('%Y-%m-%d %H:%M:%S')
    assert strftime('%Y-%m-%d', second=0) == '1970-01-01'



# Generated at 2022-06-22 11:45:10.654052
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('123', '\\d') == '1'
    assert regex_search('123', '\\d', '\\g<1>') == ['1', '1']
    assert regex_search('123', '\\d', '\\1') == ['1', '1']



# Generated at 2022-06-22 11:45:23.062754
# Unit test for function mandatory
def test_mandatory():
    # The following test is intended to fail, in order to demonstrate
    # the correct functionality of the mandatory filter
    ansible_return = {"failed": False, "tests": []}
    test_cases = [
        {'args': {'a': 1, 'msg': 'This message should not be returned'}, 'expected': 1},
    ]
    for testcase in test_cases:
        a = testcase['args']['a']
        msg = testcase['args'].get('msg', None)
        expected = testcase['expected']

# Generated at 2022-06-22 11:45:34.283566
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    from .loader import AnsibleLoader

    # jinja2>=2.9.0,<2.9.5 is affected by the issue where
    # namedtuples are returned, and their repr prevents ansible from
    # parsing the data.
    #
    # The following test actually catches the issue in the jinja2
    # function, and the tests for do_groupby() verify that the
    # adaptation in the function works.
    #
    # We use a jinja2 template, because the same template is used in
    # ansible.template.safe_eval, and we want to ensure this check is
    # as close to the test in ansible.template.safe_eval, as possible.
    #
    # A sample of the namedtuple that is returned by jinja2>=2.9

# Generated at 2022-06-22 11:45:46.535785
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("foobar", "o+bar") == "oobar"
    assert regex_search("foobar", "f+bar") == None
    assert regex_search("foobar", "o+bar", "\\g<1>") == ["oo"]
    assert regex_search("foobar", "o+bar", "\\g<0>") == ["oobar"]
    assert regex_search("foobar", "o+bar", "\\2", "\\1") == [None, "oo"]
    assert regex_search("foobar", "o+bar", "\\1", "\\2") == ["oo", None]
    assert regex_search("foobar", "(o+)bar", "\\1", "\\2") == ["oo", None]

# Generated at 2022-06-22 11:45:57.231291
# Unit test for function rand
def test_rand():
    env = {'vars': {}}
    assert rand(env, 10) in range(10)
    res1 = rand(env, 10, 2, 2)
    res2 = rand(env, 10, 2, 2)
    res3 = rand(env, 10, 2, 2, seed=0)
    assert res1 in range(2, 10, 2)
    assert res2 in range(2, 10, 2)
    assert res3 in range(2, 10, 2)
    assert res1 == res3
    assert res2 == res3
    assert rand(env, [1,2,3,4,5]) in [1,2,3,4,5]


# Generated at 2022-06-22 11:46:04.004573
# Unit test for function mandatory
def test_mandatory():
    try:
        assert isinstance(mandatory('{"foo":"bar", "baz": "bart"}'), dict)
        assert isinstance(mandatory(dict(foo='bar', baz='bart')), dict)
        assert isinstance(mandatory('foo'), type('foo'))

    except AnsibleFilterError as e:
        assert not e


# Generated at 2022-06-22 11:46:16.775295
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('unicøde') == 'e9c8b38e26fcdf2acb403d5fbb66b8f06b1c561d'
    assert get_hash('unicøde', hashtype='md5') == 'd4eca8b4f4b2d6c0588665a9f6da8b36'
    assert get_hash('unicøde', hashtype='sha224') == 'f10462f0d0c7db9d96faa2956b0c74c730146fefcb19e59fdfce1ad77'

# Generated at 2022-06-22 11:46:22.731504
# Unit test for function extract
def test_extract():
    """Extracting keys from a dictionary"""
    assert extract('a', {'a': 1, 'b': 2}) == 1
    assert extract('a', {'b': {'a': 1}, 'c': 2}) == 1
    assert extract('a', {'a': 1, 'b': 2}, 'b', 'c', 'd') == 2
    assert extract('a', {'a': 1, 'b': 2}, ['b', 'c', 'd']) == 2



# Generated at 2022-06-22 11:46:31.224696
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo') == 'foo'
    assert regex_escape('foo.') == 'foo\\.'
    assert regex_escape('(foo') == '\\(foo'
    assert regex_escape('[foo') == '\\[foo'
    assert regex_escape(']foo') == '\\]foo'
    assert regex_escape('{foo') == '\\{foo'
    assert regex_escape('}foo') == '\\}foo'
    assert regex_escape('?foo') == '\\?foo'
    assert regex_escape('*foo') == '\\*foo'
    assert regex_escape('+foo') == '\\+foo'
    assert regex_escape('^foo') == '\\^foo'
    assert regex_escape('$foo') == '\\$foo'

# Generated at 2022-06-22 11:46:35.843343
# Unit test for function extract
def test_extract():
    environment = Dict({})
    container = {'a': {'b': 1, 'c': ['a','b','c','d','e']}}
    result = extract(environment, 'b', container)
    assert result == 1
    result = extract(environment, 'c', container, '1')
    assert result == 'b'



# Generated at 2022-06-22 11:46:44.888477
# Unit test for function regex_search
def test_regex_search():
    # Test the case where the capture group is a number
    assert 'ABC' == regex_search('abcabcABCabc', 'A(.*?)A', '\\2')
    # Test the case where the capture group is a string
    assert 'ABC' == regex_search('abcabcABCabc', '(?P<group>A.*?A)', '\\g<group>')



# Generated at 2022-06-22 11:46:56.396183
# Unit test for function mandatory
def test_mandatory():
    from jinja2 import Environment
    env = Environment()
    env.filters['mandatory'] = mandatory

    assert env.from_string('{{ missing | mandatory }}').render() == ''
    assert env.from_string('{{ missing | mandatory("error message") }}').render() == ''

    try:
        env.from_string('{{ missing | mandatory }}').render()
    except AnsibleFilterError as e:
        assert to_native(e) == "Mandatory variable 'missing' not defined."
    else:
        assert False

    try:
        env.from_string('{{ missing | mandatory("error message") }}').render()
    except AnsibleFilterError as e:
        assert to_native(e) == "error message"
    else:
        assert False



# Generated at 2022-06-22 11:47:03.581266
# Unit test for function to_bool
def test_to_bool():
    assert to_bool('yes') == True
    assert to_bool('1') == True
    assert to_bool('on') == True
    assert to_bool('true') == True
    assert to_bool('True') == True
    assert to_bool('false') == False
    assert to_bool('False') == False
    assert to_bool('no') == False
    assert to_bool('0') == False
    assert to_bool('off') == False
    assert to_bool('off') == False
    assert to_bool('foo') == False
    assert to_bool(1) == True
    assert to_bool(0) == False
    assert to_bool(True) == True
    assert to_bool(False) == False



# Generated at 2022-06-22 11:47:12.098023
# Unit test for function mandatory
def test_mandatory():
    from ansible.template import Templar
    templar = Templar()
    assert templar.template("{{ var|mandatory }}", dict(var='foo'), fail_on_undefined=True) == 'foo'
    try:
        templar.template("{{ var|mandatory }}", dict(), fail_on_undefined=True)
        assert False, "mandatory filter did not fail on undefined variable"
    except AnsibleError as e:
        assert 'variable \'var\' is undefined' in str(e), str(e)

# Generated at 2022-06-22 11:47:18.992476
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import DictLoader
    from jinja2.sandbox import SandboxedEnvironment

    env = SandboxedEnvironment(loader=DictLoader({"tmpl": "{{ [1,2] | groupby(attribute='real') | list }}"}))
    result = env.get_template('tmpl').render()
    expected = '[(1, [1, 2])]'
    assert result == expected



# Generated at 2022-06-22 11:47:25.019886
# Unit test for function strftime
def test_strftime():
    assert strftime('%Y-%m-%dT%H:%M:%SZ', 1279470347.0) == '2010-06-29T20:49:07Z'
    assert strftime('%Y-%m-%dT%H:%M:%SZ') > '2000-06-29T20:49:07Z'



# Generated at 2022-06-22 11:47:29.076169
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('hello') == 'hello'
    assert mandatory('') == ''
    assert mandatory('hello', msg="some message") == 'hello'
    assert mandatory('') == ''



# Generated at 2022-06-22 11:47:38.253774
# Unit test for function to_bool
def test_to_bool():
    assert to_bool('true')==True
    assert to_bool('True')==True
    assert to_bool('TRUE')==True
    assert to_bool(1)==True
    assert to_bool('t')==False
    assert to_bool('false')==False
    assert to_bool('False')==False
    assert to_bool('FALSE')==False
    assert to_bool('bad')==False
    assert to_bool(0)==False
    assert to_bool('')==False
    assert to_bool([])==False
    assert to_bool(None)==None
    assert to_bool('yes')==True
    assert to_bool('no')==False
    assert to_bool('off')==False
    assert to_bool('on')==True
    assert to_bool(True)==True


# Generated at 2022-06-22 11:47:51.478424
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined, StrictUndefined

    assert mandatory(None) is None
    assert mandatory(1) == 1
    assert mandatory(0) == 0
    assert mandatory("one") == "one"
    assert mandatory("") == ""
    assert mandatory([1, 2, 3]) == [1, 2, 3]

    assert mandatory(Undefined(name="foo"))
    assert mandatory(StrictUndefined(name="foo"))

    try:
        mandatory(Undefined())
        # Should never get here
        assert False
    except:
        pass

    try:
        mandatory(Undefined(name="foo"), "Bad foo")
        # Should never get here
        assert False
    except:
        pass


# Generated at 2022-06-22 11:48:00.911689
# Unit test for function comment
def test_comment():
    assert comment('') == '# \n'
    assert comment('test', 'plain') == '# test\n'
    assert comment('', 'cblock') == '/**/\n'
    assert comment('test', 'cblock') == '/**\n * test\n */\n'
    assert comment('test', 'cblock', 'decoration', '@') == '/**\n * @test\n */\n'
    assert comment('test', 'cblock', 'prefix', '@') == '/**\n * test\n * @\n */\n'
    assert comment('test', 'cblock', 'postfix', '@') == '/**\n * test\n * @\n */\n'

# Generated at 2022-06-22 11:48:16.247811
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo', re_type='python') == 'foo'
    assert regex_escape(r'foo*python*.\d', re_type='python') == r'foo\*python\*\.\\d'

    assert regex_escape('foo', re_type='posix_basic') == 'foo'
    assert regex_escape(r'foo*python*.\d', re_type='posix_basic') == r'foo\*python\*\.\\\d'
    assert regex_escape(r'foo*python*.\d', re_type='posix_basic') == r'foo\*python\*\.\\\d'

    # TODO: Implement posix_extended
    # assert regex_escape('foo', re_type='posix_extended') == 'foo'
    # assert regex_escape(r'

# Generated at 2022-06-22 11:48:19.336821
# Unit test for function to_yaml
def test_to_yaml():
    results = []
    results.append(to_yaml({"a":1,"b":2}))
    return results

# Generated at 2022-06-22 11:48:24.107081
# Unit test for function flatten
def test_flatten():
    assert flatten([[1, 2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, 2, 3], [4, [5, 6]]], 1) == [1, 2, 3, 4, [5, 6]]
    assert flatten([[1, 2, 3], [4, [5, 6]]], 2) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, 2, 3], [4, [5, 6]]], 3) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, 2, 3], [4, [5, 6]]], 0) == [[1, 2, 3], [4, [5, 6]]]

# Generated at 2022-06-22 11:48:33.300746
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1) == 1
    assert mandatory(1, msg="a") == 1
    try:
        mandatory(AnsibleUndefined)
    except AnsibleFilterError as e:
        assert to_native(e) == "Mandatory variable 'None' not defined."
    try:
        mandatory(AnsibleUndefined, msg="undef")
    except AnsibleFilterError as e:
        assert to_native(e) == "undef"
    try:
        mandatory(AnsibleUndefined, msg="{{ somevar }}")
    except AnsibleFilterError as e:
        assert to_native(e) == "{{ somevar }}"



# Generated at 2022-06-22 11:48:42.564579
# Unit test for function mandatory
def test_mandatory():
    from ansible.compat.tests.mock import patch

    mock_undefined = patch('ansible.template.AnsibleUndefined')
    mock_undefined.start()

    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(AnsibleUndefined, "Test")
    assert 'Test' in str(excinfo.value)

    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(AnsibleUndefined)
    assert 'Mandatory variable \'\' not defined.' in str(excinfo.value)

    mock_undefined.stop()



# Generated at 2022-06-22 11:48:47.110527
# Unit test for function strftime
def test_strftime():
    string_format = "%c"
    second = 1449183094
    result = strftime(string_format, second)
    assert result == "Tue Dec  1 17:18:14 2015"
    second = -1449183094
    try:
        strftime(string_format, second)
    except Exception:
        pass



# Generated at 2022-06-22 11:48:59.221187
# Unit test for function comment
def test_comment():
    assert comment('test') == '# test'
    assert comment('test', 'c') == '// test'
    assert comment('test', 'plain', decoration='## ') == '## test'
    assert comment('test', 'erlang', decoration='%% ') == '% test'
    assert comment('test', 'cblock') == '/*\n * test\n */'
    assert comment('test', 'xml') == '<!--\n - test\n-->'
    assert comment('test\nline2', 'xml') == '<!--\n - test\n - line2\n-->'
    assert comment('test\nline3', 'cblock') == '/*\n * test\n * line3\n */'



# Generated at 2022-06-22 11:49:05.431396
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    # Test with a list
    assert subelements(obj, 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]



# Generated at 2022-06-22 11:49:17.715617
# Unit test for function mandatory
def test_mandatory():
    def test_arguments(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                reraise(AnsibleFilterError, AnsibleFilterError('Unable to determine error message for test. Exception was: {}'.format(to_native(e))), sys.exc_info()[2])
        return new_func

    @test_arguments
    def test(msg=None, operation='basic test', args=None):
        if not isinstance(args, list) and not isinstance(args, tuple):
            raise ValueError('Test does not have the correct arguments. Expected list or tuple, but got %s.' % type(args))

        from jinja2.runtime import Undefined
        if msg:
            expected_msg = msg
       

# Generated at 2022-06-22 11:49:24.908880
# Unit test for function do_groupby
def test_do_groupby():
    assert do_groupby(list(map(GroupableMock, ['a', 'a', 'b'])), GroupableMock.group_key) == \
           [('a', [GroupableMock('a'), GroupableMock('a')]), ('b', [GroupableMock('b')])]
    assert do_groupby(list(map(GroupableMock, ['a', 'a', 'b'])), 'nonexistent') == []

# Generated at 2022-06-22 11:49:39.608898
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    a = Undefined('yes')
    try:
        mandatory(a)
        assert 0, "Should have thrown an exception"
    except AnsibleFilterError:
        pass
    try:
        mandatory(a, 'oops')
        assert 0, "Should have thrown an exception"
    except AnsibleFilterError as e:
        assert str(e) == "oops"

    # test that non-undefined, undefined and missing variables can be accessed
    a = 1
    assert mandatory(a, 'oops') == 1
    a = Undefined()
    assert mandatory(a, 'oops') is a
    del a

# Generated at 2022-06-22 11:49:47.514257
# Unit test for function do_groupby
def test_do_groupby():
    data = [{"a":1, "b":0},
            {"a":1, "b":1},
            {"a":2, "b":2},
            {"a":1, "b":3},
            {"a":3, "b":4}]
    grouped_data = [((1, 0),),
                    ((1, 1),),
                    ((1, 3),),
                    ((2, 2),),
                    ((3, 4),)]
    ntuple_data = _do_groupby({}, data, 'a')
    tuple_data = [tuple(t) for t in ntuple_data]
    assert tuple_data == grouped_data


# Generated at 2022-06-22 11:49:53.506692
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({"key": "value"}) == u'key: value\n'
    assert to_nice_yaml(["item1", "item2"]) == u'- item1\n- item2\n'
    assert to_nice_yaml(["item1", ["item2", "item3"]]) == u'- item1\n-\n  - item2\n  - item3\n'
    assert to_nice_yaml(["item1", {"key": "value"}]) == u'- item1\n-\n    key: value\n'



# Generated at 2022-06-22 11:50:03.845597
# Unit test for function extract
def test_extract():
    from jinja2 import Environment
    environment = Environment()
    assert extract(environment, 'key1', {'key1': {'key2': 42}}) == {'key2': 42}

    class Container(object):
        def __init__(self, parent=None, name=None):
            self._parent = parent
            self._name = name

        def __getattr__(self, name):
            if self._name == 'key3':
                return None
            return Container(self, name)

        def get_value(self):
            return self._parent._parent.__dict__[self._parent._name].get(self._name)

    assert extract(environment, 'key1', Container(), 'key2') == 42



# Generated at 2022-06-22 11:50:07.484818
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({"k1": "v1", "k2": "v2"}) == """{
    k1: v1
    k2: v2
}
"""


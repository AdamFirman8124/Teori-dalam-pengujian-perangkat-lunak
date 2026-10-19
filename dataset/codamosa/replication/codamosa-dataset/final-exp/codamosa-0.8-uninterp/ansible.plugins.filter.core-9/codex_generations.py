

# Generated at 2022-06-22 11:40:46.669553
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('fizzbuzz', r'fizz', 'abc') == 'abcbuzz'
    assert regex_replace('fizzbuzz', r'fizz', 'abc', ignorecase=True) == 'abcbuzz'
    assert regex_replace('fizzbuzz', r'fizz', r'buzz', ignorecase=True) == 'buzzbuzz'
    assert regex_replace('fizzbuzz', r'fizz', r'buzz', ignorecase=True, multiline=True) == 'buzzbuzz'
    assert regex_replace('1st line\n2nd line\n3rd line', r'(\d+)', r'\g<1>rd', ignorecase=True, multiline=True) == '1rd line\n2rd line\n3rd line'



# Generated at 2022-06-22 11:40:53.282141
# Unit test for function regex_search
def test_regex_search():
    def _test_regex_search(value, pattern, expected, ignorecase=False, multiline=False):
        result = regex_search(value, pattern, ignorecase=ignorecase, multiline=multiline)
        if result != expected:
            raise AssertionError("results do not match:\nexpected=%s\nreceived=%s\n" % (expected, result))
    _test_regex_search('', '', '')
    _test_regex_search('', '.', None)
    _test_regex_search('a', '.', 'a')
    _test_regex_search('a', 'b', None)
    _test_regex_search('a', '[a-z]', 'a')

# Generated at 2022-06-22 11:40:58.437022
# Unit test for function to_yaml
def test_to_yaml():
    a = {'YAML': 'text', 'is': 'neat'}
    assert(to_yaml(a, default_flow_style=False) == """{YAML: text, is: neat}
""")
    assert("to_yaml" in globals())


# Generated at 2022-06-22 11:41:07.299464
# Unit test for function comment
def test_comment():
    from ansible.module_utils._text import to_bytes
    import ansible.module_utils.basic
    # ansible.module_utils.basic.AnsibleModule

    def assertSameOutput(text, expected):
        actual = comment(text)
        assert expected == actual, \
            "FAIL for case:\n\tinput:    %s\n\texpected: %s\n\tactual:   %s" % (
                text, expected, actual)

    # Tests with defaults
    assertSameOutput(
        'text', '# text')
    assertSameOutput(
        'first line\nsecond line', '# first line\n# second line')
    assertSameOutput(
        'first line\n\nsecond line', '# first line\n# \n# second line')

    # Tests with custom decorators


# Generated at 2022-06-22 11:41:14.240532
# Unit test for function strftime
def test_strftime():
    string_format = '%Y-%m-%d %H:%M:%S'
    second = time.time()
    assert strftime(string_format) == time.strftime(string_format, time.localtime(second))
    second = 1438630152.0
    assert strftime(string_format, second) == time.strftime(string_format, time.localtime(second))



# Generated at 2022-06-22 11:41:23.377828
# Unit test for function to_bool
def test_to_bool():
    assert to_bool('1') == True
    assert to_bool(1) == True
    assert to_bool('YES') == True
    assert to_bool('True') == True
    assert to_bool(True) == True
    assert to_bool('00001') == True
    assert to_bool('true ') == True
    assert to_bool('') == False
    assert to_bool('0') == False
    assert to_bool(0) == False
    assert to_bool('False') == False
    assert to_bool('false') == False
    assert to_bool(False) == False
    assert to_bool(' ') == False
    assert to_bool('foo') == False


# Generated at 2022-06-22 11:41:35.674014
# Unit test for function rand
def test_rand():
    env = {}
    assert rand(env, 2) in [0, 1]
    assert rand(env, 2, seed='f') in [0, 1]
    env = {'vars': {'seed': 1}}
    assert rand(env, 2) in [0, 1]
    assert rand(env, 2, seed='f') in [0, 1]
    assert rand(env, 2, seed=1) in [0, 1]
    assert rand(env, [1, 2, 2]) in [1, 2]
    assert rand(env, [1, 2, 2], seed='f') in [1, 2]
    assert rand(env, [1, 2, 2], seed=1) in [1, 2]
    assert rand(env, 0, 2) in [0, 1]

# Generated at 2022-06-22 11:41:48.569539
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('hello world', '(?<=hello )\w+') == 'world'
    assert regex_search('hello world', '(?<=hello )(\w+)', '\\g<1>') == ['world', 'world']
    assert regex_search('hello world', '(?<=hello )(\w+)', '\\g<1>', '\\g<1>') == ['world', 'world', 'world']
    assert regex_search('hello world', 'x') == None
    assert regex_search('hello world', '\d') == None
    assert regex_search('2', '\d') == '2'
    assert regex_search('2', '\d', '\\1') == ['2']
    assert regex_search('2', 'w?(\d)', '\\g<1>') == ['2']
   

# Generated at 2022-06-22 11:41:55.737345
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('abc') == 'abc'
    assert regex_escape('a+b') == 'a\\+b'
    assert regex_escape('?[]') == '\\?\\[\\]'

    assert regex_escape('abc', re_type='posix_basic') == 'abc'
    assert regex_escape('a+b', re_type='posix_basic') == 'a+b'
    assert regex_escape('?[]', re_type='posix_basic') == '\\?\\[\\]'



# Generated at 2022-06-22 11:42:07.578258
# Unit test for function combine
def test_combine():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cStringIO as StringIO
    if PY3:
        from io import StringIO
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    # Monkeypatch `combine()` into builtins so it can be used in tests
    builtins.__dict__['combine'] = combine

    # Test that imports work as expected
    # Test that the right Python version is in use
    assert isinstance(StringIO(), (StringIO, StringIO))

    # Test that the function is valid and produces the expected output
    assert combine({}) == combine({}, {}) == combine({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}
   

# Generated at 2022-06-22 11:42:25.949282
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(r'Hello', r'[a-z]+') == 'Hello'
    assert regex_search(r'Hello world', r'[a-z]', '\\g<0>') == ['Hello', 'world']
    assert regex_search(r'Hello world', r'[a-z]+', '\\g<0>') == ['Hello', 'world']
    assert regex_search(r'Hello world', r'[a-z]+', '\\g<0>', '\\1', '\\2') == ['Hello', 'world', 'H', None]
    assert regex_search(r'Hello world', r'([a-z]+) ([a-z]+)', '\\1', '\\g<2>') == ['Hello', 'world']

# Generated at 2022-06-22 11:42:38.205009
# Unit test for function regex_search
def test_regex_search():
    '''Test regex_search filter'''
    assert regex_search('hello world', r'hello (\S+)', '\\1') == 'world'
    assert regex_search('hello world', r'hello (\S+)', '\\g<1>') == 'world'
    assert regex_search('hello world', r'hello (\S+)', '\\g<1>', '\\1') == ['world', 'world']
    assert regex_search('hello world', r'hello (\S+)', '\\g<1>', '\\2') == ['world', None]
    assert regex_search('hello world', r'hello (\S+)', '\\g<2>') == [None]
    assert regex_search('hello world', r'hello (\S+)', '\\2') == [None]

# Generated at 2022-06-22 11:42:44.399122
# Unit test for function get_hash
def test_get_hash():
    assert get_hash(b'foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    assert get_hash(b'foo', hashtype='md5') == 'acbd18db4cc2f85cedef654fccc4a4d8'


# Generated at 2022-06-22 11:42:55.459053
# Unit test for function subelements

# Generated at 2022-06-22 11:43:06.609746
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    # define a fake jinja context for testing mandatory()
    class FakeJinjaContext(dict):
        def __init__(self, d):
            self.dicts = [d]

        def resolve(self, k):
            for d in self.dicts:
                if k in d:
                    return d[k]
            return Undefined(k)

        def undef(self, k):
            return isinstance(self[k], Undefined)

    # test undefined scenario
    c = FakeJinjaContext({})
    assert mandatory(c.resolve('test'), 'undefined test')

    # test defined scenario
    c = FakeJinjaContext({'test': 'value'})
    assert mandatory(c.resolve('test'), 'defined test')



# Generated at 2022-06-22 11:43:18.175826
# Unit test for function fileglob
def test_fileglob():
    # Create test directory and some files
    test_dir = os.path.join(os.path.dirname(__file__), 'fileglob_test_dir')
    try:
        os.mkdir(test_dir)
    except OSError:
        # Directory already exists
        pass
    try:
        os.chdir(test_dir)
    except Exception:
        raise AnsibleError('Could not change to test directory.')
    open('a', 'w').close()
    open('1', 'w').close()
    open('a1', 'w').close()
    assert(fileglob('a*') == [os.path.join(test_dir, g) for g in ['a', 'a1']])

# Generated at 2022-06-22 11:43:30.210034
# Unit test for function get_hash
def test_get_hash():
    sample = b"Sample text"
    sample_sha1 = get_hash(sample)
    assert sample_sha1 == "c9a1e7e94c8b65a86b9738e5f7e68d5ad373f590"

    sample_sha256 = get_hash(sample, 'sha256')
    assert sample_sha256 == "3db891a7b919cacd7fdc6e8a980b00eaa5f7d5b5c5d02f51713c9e9a4b4db0b4"

    sample_md5 = get_hash(sample, 'md5')
    assert sample_md5 == "f87c2450f1f6cae0e7f41cf8d64c7ffb"


#
# New in Ansible 2.

# Generated at 2022-06-22 11:43:33.931731
# Unit test for function fileglob
def test_fileglob():
    assert ['/etc/ansible/hosts'] == fileglob('/etc/ansible/hosts')
    assert [] == fileglob('/etc/ansible/hosts-does-not-exist')



# Generated at 2022-06-22 11:43:43.259295
# Unit test for function combine
def test_combine():
    test_dict1 = {'foo': {'bar': 'baz'},
                  'qix': [1, 2, 3],
                  'alpha': 'beta',
                  'testing': 'ansible'}
    test_dict2 = {'foo': {'bar': 'quz'},
                  'qix': [9, 8, 7, 6],
                  'alpha': 'gamma'}
    # test recursive merge
    r_out = combine(test_dict1, test_dict2, recursive=True)
    assert r_out == {'foo': {'bar': 'quz'},
                     'qix': [9, 8, 7, 6],
                     'alpha': 'gamma',
                     'testing': 'ansible'}
    # test list merge

# Generated at 2022-06-22 11:43:46.684941
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml(dict(a=5,b=6)) == '''\
{a: 5,
b: 6}\
'''



# Generated at 2022-06-22 11:43:59.782931
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from jinja2 import DictLoader
    from jinja2.runtime import StrictUndefined
    from jinja2.exceptions import UndefinedError

    env = Environment(loader=DictLoader(dict(
        a='{{ a | do_groupby("stooges")|list }}',
    )))
    env.filters['do_groupby'] = do_groupby

    # Verify dict is unchanged with do_groupby if the value is not a list.
    env.from_string('{{ foo | do_groupby("stooges") }}') \
        .render(dict(foo='bar', stooges=['moe', 'curly', 'larry'])) == 'bar'

    # Verify do_groupby raises an error if

# Generated at 2022-06-22 11:44:03.096858
# Unit test for function get_hash
def test_get_hash():
    assert(get_hash('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33')



# Generated at 2022-06-22 11:44:15.217929
# Unit test for function mandatory
def test_mandatory():
    def test_fail(msg, func):
        try:
            func()
        except AnsibleFilterError as e:
            if msg not in to_text(e):
                raise AssertionError('Expected error message "%s" to contain "%s"' % (to_text(e), msg))
        else:
            raise AssertionError('Expected error message "%s"' % msg)

    test_fail('"undef" not defined', lambda: mandatory(undef))

    def test_unsafe_string(var):
        test_fail('"var" not defined', lambda: mandatory(var))

    test_unsafe_string('__main__.undef')
    test_unsafe_string('variable_undefined_in_task')


# Generated at 2022-06-22 11:44:24.939571
# Unit test for function do_groupby
def test_do_groupby():
    """
    Unit test for the do_groupby filter.
    """
    from ansible.template import JinjaEnvironment
    from ansible.template.vars import AnsibleJ2Vars
    from jinja2.sandbox import SandboxedEnvironment

    env = JinjaEnvironment(
        loader=DictLoader({}),
        undefined=StrictUndefined,
        extensions=['jinja2.ext.do'],
        variable_start_string="{{",
        variable_end_string="}}",
        loader=None,
        trim_blocks=True
    )
    env.filters.update({
        'groupby': do_groupby,
    })


# Generated at 2022-06-22 11:44:33.319959
# Unit test for function extract
def test_extract():
    filter_plugin = _FilterModule({})
    extract = FilterModule(filter_plugin)
    inventory = {
        'group1': {
            'hosts': ['host1'],
            'vars': {
                'name1': 'value1',
            },
        },
        'group2': {
            'hosts': ['host2'],
            'vars': {
                'name1': 'value2',
            },
        }
    }

    assert extract.extract('group2', inventory, 'vars', 'name1') == 'value2'
    assert extract.extract('group2', inventory, 'vars.name1') == 'value2'
    assert extract.extract('group1', inventory, 'vars.name1') == 'value1'



# Generated at 2022-06-22 11:44:41.786121
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(None) is None
    assert mandatory(False) is False
    assert mandatory(0) == 0
    assert mandatory('') == ''
    assert mandatory('foo') == 'foo'
    assert mandatory(3.14159) == 3.14159
    assert mandatory(dict()) == dict()
    assert mandatory(dict(one=1, two=2)) == dict(one=1, two=2)
    assert mandatory(['foo', 'bar']) == ['foo', 'bar']
    assert mandatory((1, 2, 3)) == (1, 2, 3)



# Generated at 2022-06-22 11:44:53.205873
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo.bar','fo[^.]+\.(.+)','\\g<1>') == 'bar'
    assert regex_search('foo.bar','fo[^.]+\.(.+)','\\1') == 'bar'
    assert regex_search('foo/bar','fo[^/]+(/.+)','\\1') == '/bar'
    assert regex_search('foo.bar','fo[^.]+\.(.+)','\\1', ignorecase=True) == 'bar'
    assert regex_search('FOO.BAR','fo[^.]+\.(.+)','\\2', ignorecase=True) == 'BAR'
    assert regex_search('foo.bar','foo(.+)','\\g<1>', multiline=True) == 'bar'

# Generated at 2022-06-22 11:45:03.661173
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({"a": 123, "b": "test", "c": ["a","b"]}) == '''{a: 123, b: test, c: [a, b]}
'''
    assert to_yaml({"a": 123, "b": "test", "c": ["a","b"]}, default_flow_style=True) == '''{a: 123, b: test, c: [a, b]}
'''
    assert to_yaml(["a","b","c"]) == '''- a
- b
- c
'''
    assert to_yaml(["a","b","c"], default_flow_style=True) == '''[a, b, c]
'''
# End unit test for function to_yaml



# Generated at 2022-06-22 11:45:11.781478
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'foo': 'bar'}) == '{foo: bar}\n'
    assert to_yaml({'foo': 'bar'}, default_flow_style=False) == '{foo: bar}\n'
    assert to_yaml({'foo': 'bar'}, default_flow_style=True) == '{foo: bar}\n'
    assert to_yaml({'foo': 'bar'}, default_flow_style=None) == '{foo: bar}\n'



# Generated at 2022-06-22 11:45:17.429586
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    a = dict(
        a=1,
        b=dict(
            c='c',
            d='d',
            f=5
        )
    )
    nice_yaml = to_nice_yaml(a)
    assert nice_yaml == """\
a: 1
b:
    c: c
    d: d
    f: 5
"""



# Generated at 2022-06-22 11:45:29.689633
# Unit test for function mandatory
def test_mandatory():
    data = 1
    output = mandatory(data)
    assert output == 1



# Generated at 2022-06-22 11:45:39.080589
# Unit test for function mandatory
def test_mandatory():
    # import _mock_t
    # _mock_t.patch('ansible.moduleutils._text.to_native')
    # _mock_t.patch('ansible.moduleutils.six.text_type')
    # _mock_t.patch('ansible.utils.display.Display.display')

    from jinja2.runtime import Undefined

    assert mandatory(42) == 42
    assert mandatory(None) == None
    assert mandatory([1, 2]) == [1, 2]
    assert mandatory({'a': 'b'}) == {'a': 'b'}
    assert mandatory('') == ''
    assert mandatory(u'foo') == u'foo'


# Generated at 2022-06-22 11:45:49.199561
# Unit test for function mandatory
def test_mandatory():
    from nose.tools import assert_raises, assert_equal
    from jinja2.runtime import Undefined

    assert_equal(mandatory(42, "msg"), 42)
    with assert_raises(AnsibleFilterError):
        mandatory(Undefined(42, 'a'))
    with assert_raises(AnsibleFilterError):
        mandatory(Undefined(42, None, 'a'))
    with assert_raises(AnsibleFilterError) as cm:
        mandatory(Undefined(42, 'a'),"msg")
    assert_equal(str(cm.exception), "msg")
    with assert_raises(AnsibleFilterError) as cm:
        mandatory(Undefined(42, None, 'a'),"msg")
    assert_equal(str(cm.exception), "msg")

# Generated at 2022-06-22 11:46:00.548308
# Unit test for function mandatory
def test_mandatory():

    from jinja2 import StrictUndefined
    env = Environment(undefined=StrictUndefined)

    assert mandatory(42, env) == 42
    assert mandatory(None, env) == None
    assert mandatory("foo", env) == "foo"
    assert mandatory({}, env) == {}
    assert mandatory(False, env) == False

    # No exception if no message is provided
    try:
        mandatory(Undefined(env), env)
        assert False
    except AnsibleFilterError as e:
        assert to_native(e) == "Mandatory variable  not defined."

    # Exception if message is provided
    try:
        mandatory(Undefined(env), env, msg="Some message")
        assert False
    except AnsibleFilterError as e:
        assert to_native(e) == "Some message"

    # Exception if

# Generated at 2022-06-22 11:46:02.428975
# Unit test for function to_yaml
def test_to_yaml():
    """Test function return a non-empty string"""
    assert len(to_yaml({})) > 0

# Generated at 2022-06-22 11:46:13.750355
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment

    env = Environment()
    filt = lambda *args: list(args)
    env.filters['groupby'] = do_groupby

    do_groupby_result = env.from_string("{% set groups = [{'name': 'John'}, {'name': 'Jane'}, {'name': 'Joe'}] | groupby('name') -%}")._dump()
    default_groupby_result = env.from_string("{% set groups = [{'name': 'John'}, {'name': 'Jane'}, {'name': 'Joe'}] | groupby('name') -%}")._dump()
    assert do_groupby_result == default_groupby_result



# Generated at 2022-06-22 11:46:23.869894
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("hello", r"hello") == "hello"
    assert regex_search("hello world", r"hello world") == "hello world"
    assert regex_search("hello world", r"hello") == "hello"
    assert regex_search("hello", r"(h|H)ello") == "hello"
    assert regex_search("Yes,My name is Bob", r"(?P<name>\w+)", "\\g<name>") == "Bob"
    assert regex_search("Yes,My name is Bob", r"(?P<name>\w+)", "\\1") == "Bob"
    assert regex_search("Yes,My name is Bob", r"(?P<name>\w+)", "\\g<name>", "\\1") == ["Bob", "Bob"]

# Generated at 2022-06-22 11:46:28.661925
# Unit test for function fileglob
def test_fileglob():
    testfile = 'fileglob_testfile.txt'
    f = open(os.path.join(os.getcwd(), testfile), 'w')
    f.close()
    globbed_files = fileglob('fileglob_test*')
    assert(to_native(testfile) in globbed_files)
    os.remove(testfile)



# Generated at 2022-06-22 11:46:34.429674
# Unit test for function to_yaml
def test_to_yaml():
    a = dict(a='b')
    s = to_yaml(a)
    assert s == '{a: b}\n'
    s = to_yaml(a, default_flow_style=False)
    assert s == 'a: b\n'
    assert to_yaml(a, default_flow_style=None) != to_yaml(a, default_flow_style=False)


# Generated at 2022-06-22 11:46:37.948990
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    value = {"data":"value"}
    expected = u"---\ndata: value\n"
    assert to_nice_yaml(value) == expected



# Generated at 2022-06-22 11:46:53.482717
# Unit test for function randomize_list
def test_randomize_list():
    r1 = randomize_list([0,1,2,3,4])
    r2 = randomize_list([0,1,2,3,4], seed=1)
    assert r1 != [0,1,2,3,4]
    assert r2 == [0,1,2,3,4]


# Generated at 2022-06-22 11:47:01.898331
# Unit test for function to_yaml
def test_to_yaml():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    _test = dict(
        a=1,
        b=dict(
            c=[
                1,
                23,
                u'{{foo}}',
                AnsibleUnsafeText(u'{{foo}}'),
                2,
                u'{{bar}}',
                AnsibleUnsafeText(u'{{bar}}'),
            ],
            d='foo',
        ),
    )

# Generated at 2022-06-22 11:47:11.304856
# Unit test for function comment

# Generated at 2022-06-22 11:47:19.670045
# Unit test for function regex_search

# Generated at 2022-06-22 11:47:21.421062
# Unit test for function strftime
def test_strftime():
    assert '2017' == strftime('%Y')



# Generated at 2022-06-22 11:47:25.693921
# Unit test for function flatten
def test_flatten():
    # Test defaults
    assert(flatten([0, 1, [2, [3, 4]]]) == [0, 1, 2, 3, 4])
    # Test levels=1 and levels=2
    assert(flatten([0, 1, [2, [3, 4]]], 1) == [0, 1, 2, [3, 4]])
    assert(flatten([0, 1, [2, [3, 4]]], 2) == [0, 1, 2, 3, 4])
    # Test levels=0
    assert(flatten([0, 1, [2, [3, 4]]], 0) == [0, 1, [2, [3, 4]]])
    # Test levels=None

# Generated at 2022-06-22 11:47:36.875698
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    from jinja2 import meta
    from jinja2.runtime import Undefined
    from itertools import groupby
    import jinja2
    from collections import namedtuple

    env = Environment()
    env.filters['groupby'] = do_groupby
    ast = env.parse('{% set _foo = [{"a":1,"b":"c"},{"a":2,"b":"c"},{"a":2,"b":"d"}] %}'
                    '{% for key, items in _foo | groupby("a") | dictsort %}'
                    '{{ key }}:'
                    '{% for i in items %}'
                    '{{ i.b }}, '
                    '{% endfor %}<br />'
                    '{% endfor %}')
    assert isinstance

# Generated at 2022-06-22 11:47:42.372234
# Unit test for function extract
def test_extract():

    # Initialise test variables
    item = 0
    container = [1, 2, 3]
    morekeys = None

    # Set expected results
    expected = 1

    # Run the test
    actual = extract(item, container, morekeys)

    # Assert expected == actual
    assert actual == expected



# Generated at 2022-06-22 11:47:54.709676
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('123456', r'\d+', '\\g<0>') == '123456'
    assert regex_search('123456', r'\d+', '\\0') == '123456'
    assert regex_search('123456', r'\d+', '\\g<0>', '\\1') == ['123456', '2']
    assert regex_search('123456', r'\d+', '\\g<0>', '\\g<1>') == ['123456', '2']
    assert regex_search('a1b2c3', r'\w(\d)', '\\g<1>') == '1'
    assert regex_search('a1b2c3', r'\w(\d)', '\\1') == '1'

# Generated at 2022-06-22 11:47:57.090702
# Unit test for function mandatory
def test_mandatory():
    try:
        mandatory(None)
    except AnsibleFilterError:
        pass
    assert mandatory(1) == 1


# Generated at 2022-06-22 11:48:14.998007
# Unit test for function mandatory
def test_mandatory():
    # This test case has to be improved
    # Currently, we need to know that mandatory calls Undefined's constructor to
    # create its 'undefined' singleton, which is Undefined, and the Undefined
    # class is expected to be the Jinja2 Undefined class.
    from jinja2.runtime import Undefined
    assert Undefined is jinja2.Undefined, "Sorry, this test case needs to be updated"

    # We need to simulate a missing variable, which requires a template
    # context.
    env = jinja2.Environment()
    tpl = env.from_string('{{ missing }}')
    assert isinstance(tpl.new_context()['missing'], Undefined)

    # Now that we have an exception to catch, let's test mandatory
    assert mandatory(42) == 42

# Generated at 2022-06-22 11:48:24.690584
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/bin/ls') == ['/bin/ls']
    assert fileglob('/bin') == []
    assert fileglob('/b?n') == ['/bin']
    assert fileglob('/b*ls') == ['/bin/ls']
    assert fileglob('/bin/ls /bin/bash') == ['/bin/ls', '/bin/bash']
    assert fileglob('/foo/') == []
    assert fileglob('/foo') == []
    assert fileglob('/foo/bar') == []
    assert fileglob('/foo/bar/baz') == []



# Generated at 2022-06-22 11:48:34.928951
# Unit test for function get_hash
def test_get_hash():
    assert get_hash("") == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    assert get_hash("The quick brown fox jumps over the lazy dog") == "2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"
    assert get_hash("The quick brown fox jumps over the lazy dog", hashtype="sha256") == "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"
    try:
        get_hash("The quick brown fox jumps over the lazy dog", hashtype="fake")
    except AnsibleFilterError:
        pass

# Generated at 2022-06-22 11:48:42.831127
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'foo': 1, 'bar': {'a': 'b'}}) == \
"""foo: 1
bar:
  a: b
"""
    assert to_yaml({'foo': 1, 'bar': {'a': 'b'}}, default_flow_style=True) == '{"foo": 1, "bar": {"a": "b"}}'
    assert to_yaml({'foo': 1, 'bar': {'a': 'b'}, 'c': 'string'}) == \
"""foo: 1
bar:
  a: b
c: string
"""



# Generated at 2022-06-22 11:48:48.297729
# Unit test for function flatten
def test_flatten():
    assert flatten(["foo", "bar"]) == ["foo", "bar"]
    assert flatten(["foo", ["bar", "baz"]]) == ["foo", "bar", "baz"]
    assert flatten(["foo", ["bar", ["baz"]]]) == ["foo", "bar", "baz"]
    assert flatten(["foo", ["bar", ["baz"]]], skip_nulls=False) == ["foo", "bar", ["baz"]]
    assert flatten(["foo", ["bar", ['null']]]) == ["foo", "bar"]
    assert flatten(["foo", ["bar", ['null']]], skip_nulls=False) == ["foo", "bar", 'null']

# Generated at 2022-06-22 11:48:53.606486
# Unit test for function fileglob
def test_fileglob():
    pathname = os.path.join(os.getcwd(), "fileglob.py")
    assert pathname in fileglob(pathname)
    assert not fileglob(os.path.join(os.getcwd()[:-1], '*/fileglob.py'))


# Generated at 2022-06-22 11:48:57.494006
# Unit test for function get_hash
def test_get_hash():
    '''test the sha256 hash'''
    msg = 'Hello World'
    hashtype='sha256'
    h = hashlib.new(hashtype)
    h.update(to_bytes(msg, errors='strict'))
    assert get_hash(msg, hashtype) == h.hexdigest()



# Generated at 2022-06-22 11:49:08.652906
# Unit test for function mandatory
def test_mandatory():
    class VariableUndefined(object):
        _undefined_name = None

    u = VariableUndefined()
    try:
        mandatory(u)
        assert False
    except AnsibleFilterError as e:
        assert "Mandatory variable ''" in to_text(e)
        assert "not defined" in to_text(e)
    try:
        mandatory(u, "Mandatory variable '%s' not defined and/or something extra")
        assert False
    except AnsibleFilterError as e:
        assert "Mandatory variable ''" not in to_text(e)
        assert "not defined" in to_text(e)
        assert "something extra" in to_text(e)

# Generated at 2022-06-22 11:49:21.150254
# Unit test for function flatten
def test_flatten():
    # The "levels" parameter is no longer optional, as it was in older
    # versions of Ansible. However, in order to maintain backwards
    # compatibility with older playbooks which use any older versions
    # of Ansible, we need to continue to support the flatten filter
    # being called with only one parameter, in which case we assume
    # that it's the "levels" parameter and not "mylist". This means
    # that we can't simply use the "@environmentfilter" decorator
    # without a custom call_filter() function
    environment = jinja2.Environment()
    filter_ = environment.filters['flatten']

    assert filter_(None) == []
    assert filter_([]) == []
    assert filter_([1]) == [1]
    assert filter_([1, 2, 3]) == [1, 2, 3]
   

# Generated at 2022-06-22 11:49:30.682923
# Unit test for function flatten
def test_flatten():
    # 1-D
    assert flatten([1,2,3]) == [1,2,3]
    assert flatten([1,2,[3]]) == [1,2,3]

    # 2-D
    assert flatten([1,[2,3]]) == [1,2,3]

    # 2-D w/levels
    assert flatten([[1,2],[3,4]], levels=1) == [[1,2], [3,4]]
    assert flatten([[1,2],[3,4]], levels=2) == [1,2,3,4]
    assert flatten([[1,2],[3,4]], levels=3) == [1,2,3,4]

    # 3-D (default leveling means 3-D)

# Generated at 2022-06-22 11:49:40.252152
# Unit test for function mandatory
def test_mandatory():
    a = mandatory('foo bar')
    assert a == 'foo bar'



# Generated at 2022-06-22 11:49:48.838048
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("Hello World!", r"He(\w+)") == "llo"
    assert regex_search("Hello World!", r"He(\w+)", '\\1') == "llo"
    assert regex_search("Hello World!", r"He(\w+)", '\\g<1>') == "llo"
    assert regex_search("Hello World!", r"He(\w+)", '\\2', '\\g<1>') == ['llo', 'llo']
    assert regex_search("Hello World!", r"He(\w+)", '\\g<2>', '\\g<1>') == [None, 'llo']
    assert regex_search("Hello World!", r"He(\w+)", '\\g<2>') is None
    assert regex_search("Hello World!", r"He(\w+)", '\\2') is None

    assert regex

# Generated at 2022-06-22 11:49:52.729954
# Unit test for function get_hash
def test_get_hash():
    assert get_hash("value") == "b21a9e5fadb35a373718298a9e9ff1f03d1dd2c8"
    assert get_hash("", hashtype="md5") == "d41d8cd98f00b204e9800998ecf8427e"


# Generated at 2022-06-22 11:50:02.897909
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    # Check for undefined variable
    try:
        mandatory(Undefined(name='my_undefined_variable'))
        assert False
    except AnsibleFilterError as e:
        assert 'Mandatory variable' in to_native(e)

    # Check for undefined variable with custom message
    msg = 'My custom message'
    try:
        mandatory(Undefined(name='my_undefined_variable'), msg)
        assert False
    except AnsibleFilterError as e:
        assert to_native(e).endswith(msg)

    # Check for defined variable
    assert mandatory('my_defined_variable') == 'my_defined_variable'


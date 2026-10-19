

# Generated at 2022-06-22 11:40:49.176345
# Unit test for function regex_search
def test_regex_search():
    value = '''echidna:
track: seven
humuhumunukunukuapuaa:
track: eight'''

    assert regex_search(value, "track:\s(?P<track>\w+)", "\\g<track>") == ['seven']
    assert regex_search(value, "track:\s(\w+)", "\\1") == ['seven']
    assert regex_search(value, "track:\s(\w+)", "\\1", "\\1") == ['seven', 'seven']
    assert regex_search(value, "humuhumunukunukuapuaa:\s*\n.*track:\s(\w+)", "\\1", ignorecase=True) == ['eight']

# Generated at 2022-06-22 11:40:58.908745
# Unit test for function fileglob
def test_fileglob():
    f = fileglob
    assert f('/bin/ls') == ['/bin/ls']
    assert f('/bin/ls /bin/dd') == []
    assert f('/bin/*')
    assert f('/bin/l[asdf]') == []
    assert f('/bin/l?') == ['/bin/ld', '/bin/ls']
    assert f('/bin/ls *') == []
    assert f('/bin/ls /usr/bin/sort') == ['/bin/ls', '/usr/bin/sort']



# Generated at 2022-06-22 11:41:07.534611
# Unit test for function do_groupby
def test_do_groupby():
    assert [tuple(t) for t in _do_groupby(None, [{"a": 1, "b": 2, "c": 3}, {"a": 2, "b": 4, "c": 6}, {"a": 1, "b": 3, "c": 9}, {"a": 2, "b": 6, "c": 12}], "a")] == [(1, [{'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 3, 'c': 9}]), (2, [{'a': 2, 'b': 4, 'c': 6}, {'a': 2, 'b': 6, 'c': 12}])]

# Generated at 2022-06-22 11:41:09.638656
# Unit test for function comment
def test_comment():
    # Test all possible comment types
    for t in comment_styles.keys():
        c = comment("Test comment", t)
        print("Comment %s: %s" % (t, c))



# Generated at 2022-06-22 11:41:21.425174
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template.safe_eval import safe_eval
    # Basic smoke test
    assert 'foo' == safe_eval("['foo', 'bar'].groupby('1.') | map(attribute='0') | list | first")

    # Verify issue with jinja2>=2.9.0,<2.9.5
    assert 'foo' == safe_eval(
            "[{'1': 'foo'}, {'1': 'bar'}].groupby('1') | map(attribute='0') | list | first")
    assert False == safe_eval(
            "[{'1': 'foo'}, {'1': 'bar'}].groupby('1') | map(attribute='0') | list | first | isdefined")

    # Verify fix with jinja2>=2.9.0,<2.9

# Generated at 2022-06-22 11:41:31.415363
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abcdefghijklmnop', 'fgh') == 'fgh'
    assert regex_search('abcdefghijklmnop', 'fgh', '\\g<0>') == ['fgh', 'fgh']
    assert regex_search('abcdefghijklmnop', 'fgh', '\\g<0>', '\\g<0>') == ['fgh', 'fgh', 'fgh']
    assert regex_search('abcdefghijklmnop', 'fgh', '\\2') == ['h']
    assert regex_search('abcdefghijklmnop', 'fgh', '\\2', '\\g<0>') == ['h', 'fgh']
    assert regex_search('abcdefghijklmnop', 'fgh', '\\9') == None
    assert regex_

# Generated at 2022-06-22 11:41:33.326709
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('foo') == 'foo'
    raises(AnsibleFilterError, test_mandatory, 'bar')
    raises(AnsibleFilterError, test_mandatory, 'bar', msg='Error message.')
    raises(AnsibleFilterError, test_mandatory, None, msg='Error message.')



# Generated at 2022-06-22 11:41:41.085804
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('1a2b3c', '\d+', '\\g<1>') == '1'
    assert regex_search('1a2b3c', '\d+', '\\1') == '1'
    assert regex_search('1a2b3c', '\d+', '\\g<1>', '\\g<1>') == ['1', '1']
    assert regex_search('1a2b3c', '\d+', '\\1', '\\1') == ['1', '1']
    assert regex_search('1a2b3c', '\d+', '\\g<1>', '\\2') == ['1', '2']

# Generated at 2022-06-22 11:41:51.739054
# Unit test for function regex_search
def test_regex_search():
    '''
    Test an exact match with regex_search
    '''
    # Test match with string
    value = 'This string will be searched'
    pattern = 'will'
    result = regex_search(value, pattern, '\\1')
    assert result == 'will'

    # Test match with string and ignorecase
    value = 'This string will be searched'
    pattern = 'Will'
    result = regex_search(value, pattern, '\\1', ignorecase=True)
    assert result == 'Will'

    # Test match with string, ignorecase and multiline
    value = '''This string will be searched
    And I am sure that it is working'''
    pattern = 'Will'
    result = regex_search(value, pattern, '\\1', ignorecase=True, multiline=True)

# Generated at 2022-06-22 11:41:58.552878
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'.\*+$?()|[]{}^$') == r'\.\\\*\+\$\?\(\)\|\[\]\{\}\^\$'
    assert regex_escape(r'.\*+$?()|[]{}^$', re_type='posix_basic') == r'\.\\.\*\+\$\?\(\)\|\[\]\{\}\^\$'


# Generated at 2022-06-22 11:42:10.104425
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]

    results = subelements(obj, 'groups')
    assert len(results) == 1
    assert results[0][0] == obj[0]
    assert results[0][1] == 'wheel'

    results = subelements(obj, 'authorized')
    assert len(results) == 1
    assert results[0][0] == obj[0]
    assert results[0][1] == '/tmp/alice/onekey.pub'

    with pytest.raises(AnsibleFilterTypeError):
        subelements(obj, 'name')

    assert len(subelements(obj, 'sshkeys')) == 0

# Generated at 2022-06-22 11:42:19.426633
# Unit test for function regex_escape
def test_regex_escape():
    test_cases = (
        ('$', 'python', r'\$'),
        ('$', 'posix_basic', r'\$'),
        ('.', 'python', r'\.'),
        ('.', 'posix_basic', r'\.'),
    )
    for (string, re_type, expected) in test_cases:
        actual = regex_escape(string, re_type)
        assert actual == expected, \
            "regex_escape('%s', '%s') expected '%s', got '%s'" % (string, re_type, expected, actual)
    # test errors
    try:
        regex_escape('', 'foobar')
        assert False, "regex_escape with bad re_type name failed to raise exception"
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:42:25.138569
# Unit test for function randomize_list
def test_randomize_list():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    mylist = ['one', 'two', 'three', 'four']
    mylist = randomize_list(mylist, seed=0)

    assert len(mylist) == 4
    assert mylist[0] == 'two'
    assert isinstance(mylist[0], AnsibleUnsafeText)



# Generated at 2022-06-22 11:42:30.622745
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('foo') == 'foo'
    try:
        assert mandatory(AnsibleUndefined)
        raise AssertionError
    except AnsibleFilterError as e:
        assert "Mandatory variable 'None' not defined." in str(e)
    assert mandatory(AnsibleUndefined, "custom message") == "custom message"



# Generated at 2022-06-22 11:42:40.892600
# Unit test for function mandatory
def test_mandatory():
    ''' unit test for mandatory filter '''
    assert mandatory('foo') == 'foo'
    assert mandatory('foo', 42) == 'foo'

    from jinja2.runtime import Undefined
    undef = Undefined(name='bar')
    assert mandatory(undef) == undef

    try:
        mandatory(undef, 'the bar has no value')
        assert False, 'filter must fail with an exception'
    except AnsibleFilterError as e:
        assert 'the bar has no value' in str(e)

    try:
        mandatory(undef)
        assert False, 'filter must fail with an exception'
    except AnsibleFilterError as e:
        assert 'undefined' in str(e)


# Generated at 2022-06-22 11:42:51.550152
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import DictLoader
    from jinja2 import Environment
    from collections import namedtuple

    # set up the environment
    loader = DictLoader({'test.j2': '{% for group in things | groupby("greeting") %}{{ group.greeting }} {{ group.items | map(attribute="name") | list }}{% endfor %}'})
    environment = Environment(loader=loader)

    # create a namedtuple to simulate the _GroupTuple in jinja2._make_dicts
    _GroupTuple = namedtuple('_GroupTuple', [
        'greeting',
        'list',
        'items'
    ])

    # input data that will be used as the "things" parameter

# Generated at 2022-06-22 11:42:58.251287
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    a = 3
    assert mandatory(a) == 3, "Mandatory value fails to return"

    class TestUndefined(Undefined):
        def __init__(self, *args, **kwargs):
            self._undefined_name = 'test_var'
            self._fail_msg = 'Test fail message'

        def __bool__(self):
            return False

    b = TestUndefined()
    try:
        mandatory(b)
    except AnsibleFilterError as e:
        assert 'test_var' in e.message

    try:
        mandatory(b, msg='test_message')
    except AnsibleFilterError as e:
        assert 'test_message' in e.message



# Generated at 2022-06-22 11:43:05.658623
# Unit test for function to_bool
def test_to_bool():
    assert to_bool({}) is False
    assert to_bool('') is False
    assert to_bool('foo') is False
    assert to_bool('false') is False
    assert to_bool('0') is False
    assert to_bool(0) is False
    assert to_bool('1') is True
    assert to_bool(1) is True
    assert to_bool(True) is True



# Generated at 2022-06-22 11:43:16.927099
# Unit test for function regex_search
def test_regex_search():
    value = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    arcu ante, tincidunt id auctor gravida, volutpat vitae nunc.
    In at fermentum lectus, vitae tempor leo. Aliquam id dui
    ullamcorper, scelerisque risus in, posuere leo. Nullam
    luctus arcu a dui imperdiet, a vehicula lorem tristique.
    Vivamus nec enim eu nisl vehicula pharetra eget vel augue.
    '''
    result = regex_search(value, r'Lorem\sipsum[\s\S]+?tristique\.')

# Generated at 2022-06-22 11:43:21.132383
# Unit test for function randomize_list
def test_randomize_list():
    mylist = [1, 2, 3, 4, 5]
    seed = 5
    resultset = [4, 3, 1, 2, 5]
    randomized_list = randomize_list(mylist, seed)
    assert list(randomized_list) == resultset


# Generated at 2022-06-22 11:43:36.869940
# Unit test for function strftime
def test_strftime():
    assert strftime('%Y-%m-%d %H:%M:%S') == time.strftime('%Y-%m-%d %H:%M:%S')
    assert strftime('%Y-%m-%d %H:%M:%S', 1486236322) == '2017-02-07 16:18:42'
    try:
        strftime('%Y-%m-%d %H:%M:%S', '2017-04-10 09:57:20')
    except Exception as e:
        assert type(e) == AnsibleFilterError
        assert e.message == 'Invalid value for epoch value (2017-04-10 09:57:20)'
        assert e.orig_exc is None
    else:
        assert False, 'AnsibleFilterError was not raised' 

# Generated at 2022-06-22 11:43:48.787205
# Unit test for function comment
def test_comment():
    # Test usage of predefined comment types
    testcases = {
        'erlang': '% comment',
        'c': '// comment',
        'cblock': '/**\n * comment\n */\n',
        'xml': '<!-- - comment -->\n',
        'plain': '# comment'
    }
    for type, expected in testcases.items():
        actual = comment('comment', style=type)
        assert actual == expected, '%s != %s' % (actual, expected)

    # Test overriding of predefined comment types
    actual = comment('comment', style='cblock', newline='!', beginning='(', prefix='<', postfix='>', end=')')
    expected = '(!\n<comment!\n>!)'

# Generated at 2022-06-22 11:43:58.786667
# Unit test for function regex_replace
def test_regex_replace():
    ''' regex_replace unit test'''
    # Test with str
    input_str = """
    a: b
    c: d
    foo: bar
    baz: qux
    """
    pattern_str = """
    ^(?P<key>\w+):\s(?P<value>\w+)
    """
    replacement_str = """
    \'{\g<key>}\':\'{\g<value>}\'
    """
    regex_replace_str = regex_replace(input_str, pattern_str, replacement_str, ignorecase=False, multiline=True)

# Generated at 2022-06-22 11:44:11.867559
# Unit test for function do_groupby
def test_do_groupby():
    import pytest
    from jinja2 import Environment

    env = Environment()
    env.filters['groupby'] = do_groupby

    # Test: groupby works as expected with a simple example

# Generated at 2022-06-22 11:44:20.369602
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    def test_groupby(env, source, result, args=[]):
        tmpl = env.from_string(source)
        assert tmpl.render(args=args) == result
    env = Environment()
    env.globals['groupby'] = do_groupby

# Generated at 2022-06-22 11:44:30.837044
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list(['foo', 'bar', 'baz']) != ['foo', 'bar', 'baz']
    assert len(randomize_list(['foo', 'bar', 'baz'])) == 3
    assert randomize_list(['foo', 'bar', 'baz'], seed=42) == ['baz', 'bar', 'foo']
    assert randomize_list(('foo', 'bar', 'baz'), seed=42) == ['baz', 'bar', 'foo']
    assert randomize_list(set(['foo', 'bar', 'baz']), seed=42) == ['baz', 'bar', 'foo']
    assert randomize_list('abc', seed=42) == ['c', 'b', 'a']
    assert randomize_list(42) == 42 # non-iterable is returned unchanged

# Generated at 2022-06-22 11:44:41.307563
# Unit test for function comment
def test_comment():
    assert comment('test') == '# test'
    assert comment('test', prefix='+-') == '+-\n# test'
    assert comment('test\ntest', prefix='+-') == '+-\n# test\n# test'
    assert comment('test\ntest', decoration='+-') == '+-test\n+-test'
    assert comment('test\ntest', prefix='+-', decoration='+-') == '+-\n+-# test\n+-# test'
    assert comment('test\ntest', prefix='\n') == '\n\n# test\n# test'
    assert comment('test', style='c') == '// test'
    assert comment('test', style='cblock') == '/*\n * test\n */'

# Generated at 2022-06-22 11:44:43.063506
# Unit test for function fileglob
def test_fileglob():
    if not fileglob('/bin/ls'):
        return False
    return True



# Generated at 2022-06-22 11:44:53.060942
# Unit test for function mandatory
def test_mandatory():
    if mandatory(None) is not None:
        raise AssertionError('None is not None')
    if mandatory(42) != 42:
        raise AssertionError('42 is not 42')
    if mandatory(AnsibleUndefined) is not None:
        raise AssertionError('AnsibleUndefined is not None')

    from jinja2.runtime import Undefined

    try:
        mandatory(Undefined())
    except AnsibleFilterError as e:
        if 'Mandatory' not in to_text(e):
            raise AssertionError('Not the error we expected')
    else:
        raise AssertionError('We expected an AnsibleFilterError')



# Generated at 2022-06-22 11:44:55.263078
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    assert mandatory(Undefined()) == AnsibleFilterError



# Generated at 2022-06-22 11:45:09.138819
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('hello', 'll', 'LL') == 'heLLo'
    assert regex_replace('hello world', 'll', 'LL') == 'heLLo world'
    assert regex_replace('hello world', 'll', 'LL', ignorecase=True) == 'heLLo worLD'
    assert regex_replace('Hello World', 'll', 'LL', ignorecase=False) == 'Hello World'
    assert regex_replace('Hello World', 'll', 'LL', ignorecase=True) == 'HeLLo WorLD'
    assert regex_replace('Hello World\nHello World', 'll', 'LL', ignorecase=True, multiline=False) == 'HeLLo WorLD\nHello World'

# Generated at 2022-06-22 11:45:18.677405
# Unit test for function extract
def test_extract():
    env = Environment()

    # retrieve an item of a list
    assert extract(env, 0, [1, 2, 3]) == 1

    # retrieve a key of a dict
    assert extract(env, 'key1', {'key1': 'value1'}) == 'value1'

    # retrieve several keys of a dict
    assert extract(env, 'key1', {'key1': 'value1', 'key2': 'value2, value3'}, 'key2') == 'value2, value3'

    # retrieve a deeply nested key of a dict
    assert extract(env, 'key1', {'key1': {'key2': {'key3': 'value1'}}}) == {'key2': {'key3': 'value1'}}

    # retrieve several deeply nested keys of a dict

# Generated at 2022-06-22 11:45:21.875865
# Unit test for function fileglob
def test_fileglob():
    assert fileglob(pathname='README*') == [u'README.md']



# Generated at 2022-06-22 11:45:33.349990
# Unit test for function regex_escape
def test_regex_escape():
    assert 'foo' == regex_escape('foo')
    assert 'foo\\.' == regex_escape('foo.')
    assert 'foo\\\\bar' == regex_escape('foo\\bar')
    assert 'foo\\*bar' == regex_escape('foo*bar')
    assert 'foo\\+bar' == regex_escape('foo+bar')
    assert 'foo\\^bar' == regex_escape('foo^bar')
    assert 'foo\\$bar' == regex_escape('foo$bar')
    assert 'foo\\|bar' == regex_escape('foo|bar')
    assert 'foo\\(bar' == regex_escape('foo(bar')
    assert 'foo\\)bar' == regex_escape('foo)bar')
    assert 'foo\\[bar' == regex_escape('foo[bar')
    assert 'foo\\]bar' == regex

# Generated at 2022-06-22 11:45:45.917628
# Unit test for function combine
def test_combine():

    def assert_equal(first, second):
        if first == second:
            return True
        else:
            from ansible.utils.unsafe_proxy import AnsibleUnsafeText
            if isinstance(first, AnsibleUnsafeText):
                first = to_text(first)
            if isinstance(second, AnsibleUnsafeText):
                second = to_text(second)
            raise AssertionError('%r != %r' % (first, second))


# Generated at 2022-06-22 11:45:55.649218
# Unit test for function mandatory
def test_mandatory():
    if mandatory('bar') != 'bar':
        raise AssertionError('Expected bar')

    if mandatory(AnsibleUndefined) is not None:
        raise AssertionError('Expected this not None')

    try:
        mandatory(AnsibleUndefined, msg='Nope')
    except Exception as e:
        if not isinstance(e, AnsibleFilterError) or 'Nope' not in to_native(e):
            raise AssertionError('Expected exception with message "Nope"')
        return

    raise AssertionError('Mandatory exception did not raise')



# Generated at 2022-06-22 11:46:02.697934
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('^$*+?|{[()') == r'\^\$\*\+\?\|\{\[\(\)'
    assert regex_escape('^$*+?|{[()', re_type='posix_basic') == r'\^\$\*\+\?\|\{\[\(\)'



# Generated at 2022-06-22 11:46:14.682448
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list([1, 2, 3, 4, 5], seed='test_randomize_list') == [3, 5, 4, 1, 2], \
        'randomize_list failed to produce expected output with given test seed'
    '''
    assert randomize_list([1, 2, 3, 4, 5], seed='test_randomize_list') == [5, 2, 1, 4, 3], \
        'randomize_list failed to produce expected output with given test seed'
    assert randomize_list([1, 2, 3, 4, 5], seed='test_randomize_list') == [3, 5, 4, 1, 2], \
        'randomize_list failed to produce expected output with given test seed'
    '''
    assert randomize_list(range(9), seed='test_randomize_list')

# Generated at 2022-06-22 11:46:26.567973
# Unit test for function mandatory
def test_mandatory():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from jinja2.runtime import Undefined

    # test a real undefined
    try:
        mandatory(Undefined)
        assert False, "mandatory did not error on missing variable"
    except AnsibleFilterError:
        pass

    # test an undefined with a name
    try:
        mandatory(Undefined(name='foo'))
        assert False, "mandatory did not error on missing variable"
    except AnsibleFilterError:
        pass

    # test a defined variable
    assert mandatory('foo') == 'foo'

    # test a variable wrapped in an UnsafeProxy
    assert mandatory(UnsafeProxy('foo', is_safe=False)) == 'foo'

    # test a variable wrapped in an UnsafeProxy

# Generated at 2022-06-22 11:46:38.297385
# Unit test for function mandatory
def test_mandatory():
    # Test that mandatory() fails when undefined variable is provided
    try:
        mandatory(AnsibleUndefined)
        assert False, 'Mandatory function did not fail'
    except AnsibleFilterError:
        assert True, 'Mandatory function failed as expected'

    # Test that mandatory() fails with provided error message
    try:
        mandatory(AnsibleUndefined, msg='A message')
        assert False, 'Mandatory function did not fail'
    except AnsibleFilterError as e:
        assert str(e) == 'A message', 'Mandatory function failed with provided error message'

    # Test that mandatory() does not fail when AnsibleUndefined is not provided
    try:
        mandatory(True)
        assert True, 'Mandatory function did not fail'
    except AnsibleFilterError:
        assert False, 'Mandatory function failed'



# Generated at 2022-06-22 11:46:54.524391
# Unit test for function combine
def test_combine():
    # No args should be valid, but return an empty dict
    assert combine() == {}
    # One arg should return itself even if it is an empty dict
    assert combine(dict()) == {}
    # Two args should return a merged dict
    assert combine(dict(a=1), dict(b=42)) == dict(a=1, b=42)
    # Start with one dict and merge the other dicts : the dicts after should have precedence
    assert combine(dict(a=1, b=dict(c=3, d=4)), dict(a=42, b=dict(d=43))) == dict(a=42, b=dict(c=3, d=43))
    # Start with one dict and merge the other dicts : the dicts after should have precedence.
    # The merge should be recursive

# Generated at 2022-06-22 11:46:58.449664
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
  assert to_nice_yaml([1, 2, 3]) == "- 1\n- 2\n- 3\n"
  assert to_nice_yaml({'k1':'v1', 'k2':'v2'}) == "k1: v1\nk2: v2\n"


# Generated at 2022-06-22 11:47:01.268566
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/passwd') == ['/etc/passwd']



# Generated at 2022-06-22 11:47:10.041288
# Unit test for function do_groupby
def test_do_groupby():
    jenv = jinja2.Environment()
    test_filter = do_groupby
    # test groupby
    test_dict = [{'a': 1, 'x': 'y'}, {'a': 2, 'x': 'z'}, {'a': 1, 'x': 'x'}]
    res = test_filter(jenv, test_dict, 'a')
    assert res[0][0]['a'] == 1
    assert res[0][1]['a'] == 1
    assert len(res) == 2
    assert res[1][0]['a'] == 2


# Generated at 2022-06-22 11:47:18.089896
# Unit test for function to_yaml
def test_to_yaml():
    '''Function to_yaml returns correct yaml'''
    string = '\n'.join(['---',
                        '# comment',
                        'a: 1',
                        'd:',
                        '  e: 2',
                        '  f:',
                        '    g: 3'])
    assert to_yaml({'a': 1, 'd': {'e': 2, 'f': {'g': 3}}}, default_flow_style=False) == string



# Generated at 2022-06-22 11:47:28.678719
# Unit test for function fileglob
def test_fileglob():
    m = Mock()
    m.glob = mock_glob = Mock()
    mock_glob.return_value = ['/path/to/file1', '/path/to/file2']
    m.isfile = mock_isfile = Mock()
    mock_isfile.return_value = True
    pathname = '/path/to/*'
    assert fileglob(pathname) == ['/path/to/file1', '/path/to/file2']
    mock_glob.assert_called_once_with(pathname)
    mock_isfile.assert_any_call('/path/to/file1')
    mock_isfile.assert_any_call('/path/to/file2')



# Generated at 2022-06-22 11:47:38.078141
# Unit test for function fileglob
def test_fileglob():
    def _fileglob(pathname):
        try:
            ret = fileglob(pathname)
            return ret
        except Exception as e:
            raise AnsibleFilterError("fileglob(%s) => %s" % (pathname, to_native(e)), orig_exc=e)
    assert _fileglob("/dev/*") == ['/dev/zero', '/dev/null', '/dev/sda', '/dev/sda1', '/dev/sda2', '/dev/sda3']
    assert _fileglob("/dev/*[!e]") == ['/dev/sda', '/dev/sda1', '/dev/sda2', '/dev/sda3']

# Generated at 2022-06-22 11:47:42.496672
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(True) == True
    assert mandatory(False) == False
    try:
        assert mandatory(None)
    except AnsibleFilterError:
        pass
    else:
        raise AssertionError("Failed assert")



# Generated at 2022-06-22 11:47:53.049647
# Unit test for function flatten
def test_flatten():
    list_compare = [1, 2, 3, 4, 5, 6, 7]
    assert flatten([[[[[[[[[[1]]]]]]]]], [[2], 3], [[4], 5], [[6], [[[[[7]]]]]]]) == list_compare
    assert flatten([[[[[[[[[[1]]]]]]]]], [[2], 3], [[4], 5], [[6], [[[[[7]]]]]]], levels=1) == list_compare
    assert flatten([[[[[[[[[[1]]]]]]]]], [[2], 3], [[4], 5], [[6], [[[[[7]]]]]]], levels=2) == list_compare

# Generated at 2022-06-22 11:47:57.311367
# Unit test for function combine
def test_combine():
    assert combine([{'a': 1}]) == {'a': 1}
    assert combine([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]) == {'a': 1, 'b': 3, 'c': 4}
    assert combine([{'a': {'b': 1}}, {'a': {'c': 2}}]) == {'a': {'b': 1, 'c': 2}}
    assert combine([{'a': 1, 'b': 2}, {'a': {'b': 3}}]) == {'a': {'b': 3}, 'b': 2}

    # complex data

# Generated at 2022-06-22 11:48:07.800084
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    assert 'ok' == mandatory('ok')
    assert raises(AnsibleFilterError, test_mandatory, Undefined(name='foo'))
    assert raises(AnsibleFilterError, test_mandatory, Undefined())
    assert raises(AnsibleFilterError, test_mandatory, Undefined(name='bar'), msg="Something is missing: %s")



# Generated at 2022-06-22 11:48:16.961008
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list([1, 2, 3, 4, 5]) != [1, 2, 3, 4, 5]
    assert randomize_list([1, 2, 3, 4, 5]) != randomize_list([1, 2, 3, 4, 5])
    assert randomize_list([1, 2, 3, 4, 5], seed=2) == randomize_list([1, 2, 3, 4, 5], seed=2)
    assert randomize_list([1, 2, 3, 4, 5], seed=2) != randomize_list([1, 2, 3, 4, 5], seed=3)



# Generated at 2022-06-22 11:48:27.396991
# Unit test for function comment
def test_comment():
    # Comment with Erlang comment style
    expected_erlang_comment = '''%   This is a comment
% - with multiple lines
'''
    assert comment(
        'This is a comment\nwith multiple lines', 'erlang') == expected_erlang_comment

    # Comment with XML comment style
    expected_xml_comment = '''<!-- This is a comment -->
<!-- This is a comment -->
'''
    assert comment(
        'This is a comment\nThis is a comment', 'xml') == expected_xml_comment

    # Comment with XML comment style, multiple prefix lines
    expected_xml_comment = '''<!-- This is a comment
 * with multiple lines -->
'''
    assert comment(
        'This is a comment\nwith multiple lines', 'xml', prefix_count=2) == expected_xml_comment

   

# Generated at 2022-06-22 11:48:35.876617
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2

    # Get the real do_groupby function
    do_groupby = jinja2.filters.FILTERS['groupby']

    # apply it directly to a list of dictionaries
    results = do_groupby([
        {'foo': 'bar', 'group': 23, 'baz': 42},
        {'foo': 'spam', 'group': 42, 'baz': 23},
        {'foo': 'ham', 'group': 42, 'baz': 23},
        {'foo': 'eggs', 'group': 42, 'baz': 42},
    ], 'group')

    # we expect both dictionaries in the returned tuple
    for (k, v) in results:
        for d in v:
            assert isinstance(d, dict)

    # now try our special do_groupby

# Generated at 2022-06-22 11:48:48.279967
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    def compare_structures(original, filtered):
        assert len(original) == len(filtered)
        for item in original:
            assert item in filtered
    base_data = ["value1", "value2", "value3"]
    data_for_testing = dict(
        list_of_items=base_data,
        list_of_dicts=[dict(key1=val) for val in base_data],
        deep_dict_of_dicts=dict(
            list_of_dicts=[dict(key1=val) for val in base_data],
            list_of_items=base_data,
            another_dict=dict(
                list_of_dicts=[dict(key1=val) for val in base_data],
                list_of_items=base_data
            )
        )
    )

# Generated at 2022-06-22 11:48:56.928778
# Unit test for function regex_escape
def test_regex_escape():
    assert(regex_escape(r'[a-z]', re_type='python') == r'\[a\-z\]')
    assert(regex_escape(r'[a-z]', re_type='posix_basic') == r'\[a\-z\]')
    try:
        regex_escape(r'[a-z]', re_type='posix_extended')
        assert(False)
    except AnsibleFilterError:
        pass
    try:
        regex_escape(r'[a-z]', re_type='unknown')
        assert(False)
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:49:04.754421
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'a': 'b'}) == '{a: b}\n'
    assert to_nice_yaml({'a': 'b', 'c': 'd'}) == ('{a: b,\n'
                                                  'c: d}\n')
    assert to_nice_yaml({'a': 'b', 'c': {'d': 'e'}}) == ('{a: b,\n'
                                                         'c: {d: e}}\n')



# Generated at 2022-06-22 11:49:13.505812
# Unit test for function get_hash
def test_get_hash():
    import uuid
    hash_id = str(uuid.uuid4())
    assert get_hash('test', hashtype='md5') == get_hash(to_bytes('test'), hashtype='md5')
    assert get_hash(hash_id) == get_hash(to_bytes(hash_id))
    assert isinstance(get_hash(hash_id), str)
    # invalid hash algorithm will result in an exception
    with pytest.raises(AnsibleFilterError):
        get_hash(hash_id, hashtype='sha1x')


# Generated at 2022-06-22 11:49:24.064740
# Unit test for function combine
def test_combine():

    d = {'foo': 42, 'bar': 43, 'baz': {'key0': 'value0'}}
    assert combine(d, recursive=False) == d

    d2 = {'foo': 42, 'bar': 43, 'baz': {'key0': 'value1'}}
    assert combine(d, d2, recursive=False) == d2

    d2 = {'baz': {'key0': 'value1'}, 'qux': 42}
    d3 = {'baz': {'key1': 'value2'}}
    d4 = {'baz': {'key0': 'value3', 'key1': 'value4'}}
    assert combine(d, d2, d3, recursive=True) == d4


# Generated at 2022-06-22 11:49:36.303820
# Unit test for function to_yaml
def test_to_yaml():
    # This is the same data structure used by test_to_json
    data = {
        'foo': 'bar',
        'baz': [1, 2, 3, 4, 5],
        'boolean': True,
        'null': None,
        'dict': {
            'foo': 'bar',
            'baz': [1, 2, 3, 4, 5],
            'boolean': True,
            'null': None,
        }
    }

    yaml_data = to_yaml(data)


# Generated at 2022-06-22 11:49:48.838876
# Unit test for function extract
def test_extract():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    data = {'a': 'b'}
    manager = VariableManager()
    manager.set_inventory(Inventory(
        loader=None,
        variable_manager=manager,
        host_list=[
            'localhost',
        ]))
    if not hasattr(Play(), '_variable_manager'):
        # Ansible-2.1
        manager.set_globals({'inventory_hostname': 'localhost'})
    else:
        # Ansible-2.2
        manager.set_host_variable('localhost', 'inventory_hostname', 'localhost')
    environment = manager.get_vars(host=None, include_hostvars=True)


# Generated at 2022-06-22 11:50:00.117880
# Unit test for function extract
def test_extract():
    assert extract('a', {'a': 'b'}) == 'b'
    assert extract('a', {'a': 'b', 'c': 'd'}) == 'b'
    assert extract('a', {'c': 'd'}) is None
    assert extract('a', {'a': {'b': 'c'}}) == {'b': 'c'}
    assert extract('a', {'a': {'b': 'c'}}, 'b') == 'c'
    assert extract('a', {'a': {'b': {'c': 'd'}}}, 'b', 'c') == 'd'
    assert extract('a', {'c': {'d': {'e': 'f'}}}, 'b', 'c') == {'e': 'f'}

# Generated at 2022-06-22 11:50:07.723271
# Unit test for function regex_search
def test_regex_search():
    value = 'The quick brown fox jumps over the lazy dog'
    regex = 'The quick (?P<foxcolor>brown) fox jumps over the lazy dog'
    expected = ['brown']
    assert regex_search(value, regex, '\\g<foxcolor>', ignorecase=True, multiline=True) == expected
    assert regex_search(value, regex, '\\g<foxcolor>', ignorecase=True) == expected
    assert regex_search(value, regex, '\\g<foxcolor>') == expected


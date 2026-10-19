

# Generated at 2022-06-22 11:40:38.268802
# Unit test for function regex_search
def test_regex_search():
    ''' re.search: return the list of matches or a backref '''
    # multi line
    value = '''
        foo = 'bar'
        bar = 'baz'
        '''
    regex = r'^bar\s*=\s*(\'baz\')'
    assert ['baz'] == regex_search(value, regex, '\\g<1>', multiline=True)
    # single line
    value = "foo = 'bar'"
    regex = r"^foo\s*=\s*(\'bar\')"
    assert ['bar'] == regex_search(value, regex, '\\g<1>')
    # no match
    assert None is regex_search(value, regex, '\\g<2>')
    # group not found

# Generated at 2022-06-22 11:40:48.340618
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo.bar') == 'foo\\.bar'
    assert regex_escape('foo*bar') == 'foo\\*bar'
    assert regex_escape('foo\\bar') == 'foo\\\\bar'
    assert regex_escape('foo^bar') == 'foo\\^bar'
    assert regex_escape('foo$bar') == 'foo\\$bar'
    assert regex_escape(r'foo\bar') == r'foo\\bar'
    assert regex_escape('foo[]bar') == 'foo\\[\\]bar'
    assert regex_escape('foo?bar') == 'foo\\?bar'



# Generated at 2022-06-22 11:40:57.692028
# Unit test for function regex_replace
def test_regex_replace():
    # Test with no flags
    assert regex_replace(value='hello', pattern='l', replacement='x') == 'hexxo'

    # Test with ignorecase flag
    assert regex_replace(value='hello', pattern='L', replacement='x', ignorecase=True) == 'hexlo'

    # Test with ignorecase and multiline flags
    assert regex_replace(value='hello\nhello', pattern='L', replacement='x', ignorecase=True, multiline=True) == 'hexxo\nhexxo'


# Generated at 2022-06-22 11:41:06.833730
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'a': 'b'}, default_flow_style=True) == '{a: b}\n'
    assert to_yaml({'a': 'b'}, default_flow_style=False) == (
        'a: b\n'
    )
    # test with what we can't dump
    if sys.version_info[:2] >= (2, 7):
        from collections import OrderedDict
        assert to_yaml({'a': OrderedDict([('b', 'c')])}, default_flow_style=False) == (
            "a:\n"
            "  b: c\n"
        )

# Generated at 2022-06-22 11:41:18.141618
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]
    obj = {'a': {'b': [{'c': ['c1', 'c2']}]}}
    assert subelements(obj, 'a.b.c') == [({'b': [{'c': ['c1', 'c2']}]}, 'c1'), ({'b': [{'c': ['c1', 'c2']}]}, 'c2')]



# Generated at 2022-06-22 11:41:23.412764
# Unit test for function do_groupby
def test_do_groupby():
    # Test the Jinja2 groupby filter
    # This is slightly modified from the actual jinja2
    # test, but allows it to run unmodified.
    import jinja2
    from jinja2 import Environment, meta
    from jinja2.runtime import Undefined

    class Object(object):
        def __init__(self, name):
            self.name = name

    items = [Object(name) for name in 'abracadabra']
    env = Environment(trim_blocks=True)

# Generated at 2022-06-22 11:41:35.716871
# Unit test for function regex_escape
def test_regex_escape():
    ''', regex_escape, regex_escape_compare)'''
    regex_escape_compare = dict(
        escape_slash='\\\\',
        escape_bracket='\\[',
        escape_dot='\\.',
        escape_dollar='\\$',
        escape_carrot='\\^',
        escape_plus='\\+',
        escape_curly='\\{',
        escape_paren='\\(',
        escape_star='\\*',
        escape_pipe='\\|',
        escape_question='\\?',
        escape_backslash='\\\\',
        escape_all=r'\/\[\.\$\^\+\{\(\*\|\?\\\\',
        escape_none='''abcdefghijklmnopqrstuvwxyz''',
    )


# Generated at 2022-06-22 11:41:48.681627
# Unit test for function flatten
def test_flatten():
    assert [] == flatten([])
    assert [[1, 2, 3]] == flatten([[1, 2, 3]])
    assert [1, 2, 3] == flatten([1, 2, 3])
    assert [1, 2, 3] == flatten([[1], [2], [3]])
    assert ['a', 'b', 'c'] == flatten(['a', ['b'], 'c'])
    assert [1, 2, 3, 'a', 'b', 'c'] == flatten([1, [2], [[3]], 'a', [['b']], 'c'])
    assert [1, 2, 3, 'a', 'b', 'c'] == flatten([1, [2], [[3]], 'a', [['b']], 'c'], levels=10)

# Generated at 2022-06-22 11:41:59.679858
# Unit test for function combine
def test_combine():
    # Test if combine is really recursive
    d1 = {
        'a': {
            'b': 1,
            'c': 2,
            'd': 3
        }
    }
    d2 = {
        'a': {
            'b': 4,
            'd': 5
        }
    }
    d3 = {
        'a': {
            'b': 6,
            'c': 7,
            'd': 8,
            'e': 9
        },
        'b': 10
    }
    d = combine(d1, d2, d3)
    assert d.get('a').get('b') == 6
    assert d.get('a').get('c') == 7
    assert d.get('a').get('d') == 8

# Generated at 2022-06-22 11:42:05.499730
# Unit test for function flatten
def test_flatten():
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[1, 2, 3]]) == [1, 2, 3]
    assert flatten([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1], 2, 3]) == [1, 2, 3]
    assert flatten([[[1], 2], 3]) == [1, 2, 3]
    assert flatten([[[1], [2]], 3]) == [1, 2, 3]
    assert flatten([['one', ['two']], 'three']) == ['one', 'two', 'three']
    assert flatten([['one', ['two']]], levels=1) == ['one', ['two']]
    assert flatten

# Generated at 2022-06-22 11:42:28.496253
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1, 'foo') == 1
    assert mandatory(AnsibleUndefined(), 'foo') == 'foo'
    assert mandatory(None, 'foo') == 'foo'
    assert mandatory([], 'foo') == 'foo'
    assert mandatory('', 'foo') == 'foo'
    assert mandatory(0, 'foo') == 'foo'
    assert mandatory(False, 'foo') == 'foo'



# Generated at 2022-06-22 11:42:40.893902
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('', 'md5') == 'd41d8cd98f00b204e9800998ecf8427e'
    assert get_hash('', 'sha1') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    assert get_hash('', 'sha256') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

# Generated at 2022-06-22 11:42:51.597969
# Unit test for function mandatory
def test_mandatory():
    '''Test mandatory function'''
    from jinja2.runtime import Undefined

    def check_mandatory(template):
        '''Check mandatory filter using AnsibleError raised'''
        try:
            template.render()
        except AnsibleError:
            return True
        return False

    env = Environment()
    env.filters['mandatory'] = mandatory

    template = env.from_string('{{ undefined_variable | mandatory }}')
    assert check_mandatory(template)

    # Test with undefined object
    template = env.from_string('{{ undefined | mandatory }}')
    assert check_mandatory(template)

    # Test with defined object
    template = env.from_string('{{ defined | mandatory }}')
    assert not check_mandatory(template)

    # Test with msg

# Generated at 2022-06-22 11:43:00.637975
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/usr/local/lib') == [], "Failed fileglob with directories"
    assert fileglob('/usr/local/lib/*.py') == [], "Failed fileglob with non matching files"
    assert os.path.isfile(fileglob('/bin/*')[0]), "Failed fileglob with matching files"
    assert fileglob('/bin/thisisnotarealcommand') == [], "Failed fileglob with non existent files"



# Generated at 2022-06-22 11:43:12.878253
# Unit test for function extract

# Generated at 2022-06-22 11:43:17.889559
# Unit test for function strftime
def test_strftime():
    # make the epoc time happen now
    now = int(time.time())
    assert now == int(time.mktime(time.localtime(now)))
    assert now == int(time.mktime(time.gmtime(now)))
    assert strftime('%Y', now) == time.strftime('%Y', time.localtime(now))



# Generated at 2022-06-22 11:43:28.673178
# Unit test for function rand
def test_rand():
    try:
        rand([], 'test')
        raise Exception('Expected failure when end is a string')
    except AnsibleFilterError:
        pass

    try:
        rand([], 1, 'test')
        raise Exception('Expected failure when start is a string')
    except AnsibleFilterError:
        pass

    try:
        rand([], 1, step='test')
        raise Exception('Expected failure when step is a string')
    except AnsibleFilterError:
        pass

    try:
        rand([], 1, None, 'test')
        raise Exception('Expected failure when step is a string')
    except AnsibleFilterError:
        pass

    assert rand([], 1) == rand([], 1)
    assert rand([], 1, seed=42) == rand([], 1, seed=42)


# Generated at 2022-06-22 11:43:34.936285
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    undef = Undefined(name='foo')
    assert mandatory(undef) == undef
    assert mandatory('foo') == 'foo'
    try:
        mandatory(undef, msg="test")
        raise Exception("Should have thrown an exception")
    except AnsibleFilterError as e:
        assert "test" in str(e)


# Generated at 2022-06-22 11:43:46.685150
# Unit test for function fileglob
def test_fileglob():
    import tempfile
    import os
    dir1 = tempfile.mkdtemp(prefix='test_filter_plugins')
    fh1, fn1 = tempfile.mkstemp(dir=dir1, prefix='test', suffix='.txt')
    fh2, fn2 = tempfile.mkstemp(dir=dir1, prefix='test', suffix='.txt')
    subdir = tempfile.mkdtemp(dir=dir1, prefix='test')
    fh3, fn3 = tempfile.mkstemp(dir=subdir, prefix='test', suffix='.txt')
    os.close(fh1)
    os.close(fh2)
    os.close(fh3)

# Generated at 2022-06-22 11:43:52.273712
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    a = {'a': 'b'}
    try:
        assert isinstance(to_nice_yaml(a), text_type)
        assert "a: b" in to_nice_yaml(a) 
    except Exception as e:
        raise AnsibleFilterError("to_nice_yaml - %s" % to_native(e), orig_exc=e)


# Generated at 2022-06-22 11:44:05.980004
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo.bar') == 'foo\\.bar'
    assert regex_escape('foo-bar') == 'foo-bar'
    assert regex_escape('foo?bar') == 'foo\\?bar'
    assert regex_escape('foo.bar', re_type='posix_basic') == 'foo\\.bar'
    assert regex_escape('foo-bar', re_type='posix_basic') == 'foo-bar'
    assert regex_escape('foo?bar', re_type='posix_basic') == 'foo\\?bar'



# Generated at 2022-06-22 11:44:13.870916
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('I like puppies', hashtype='sha1') == '7d17cae2864f9e18c2b6d7d6f1f6ac77034e0544'
    assert get_hash('foo', hashtype='md5') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    with pytest.raises(AnsibleFilterError):
        get_hash('foo', hashtype='fake')



# Generated at 2022-06-22 11:44:26.681907
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abcd', 'ab') == 'ab'
    assert regex_search('abcd', 'ab', '\\g<1>') == 'ab'
    assert regex_search('abcd', 'ab', '\\g<1>c') == ['ab', 'c']
    assert regex_search('abcd', 'ab', '\\g<a>') == 'ab'
    assert regex_search('abcd', 'ab', '\\g<a>', ignorecase=True) == 'ab'
    assert regex_search('abcd', 'ab', '\\g<a>', multiline=True) == 'ab'
    assert regex_search('abcd', 'ab', '\\g<a>', ignorecase=True, multiline=True) == 'ab'

# Generated at 2022-06-22 11:44:35.289389
# Unit test for function regex_escape
def test_regex_escape():
    assert not regex_escape(r'')
    assert regex_escape(r'a') == r'a'
    assert regex_escape(r'A') == r'A'
    assert regex_escape(r'ab') == r'ab'
    assert regex_escape(r'Ab') == r'Ab'
    assert regex_escape(r'aB') == r'aB'
    assert regex_escape(r'AB') == r'AB'
    assert regex_escape(r'$') == r'\$'
    assert regex_escape(r'.') == r'\.'
    assert regex_escape(r'*') == r'\*'
    assert regex_escape(r'^') == r'\^'
    assert regex_escape(r'a^b') == r'a\^b'



# Generated at 2022-06-22 11:44:47.335695
# Unit test for function regex_search
def test_regex_search():
    # Parameter default test
    assert regex_search('Thomas', r'Thomas') == 'Thomas'

    # Default and explicit ignorecase=False should behave the same
    assert regex_search('Thomas', r'^thomas$', ignorecase=False) is None
    assert regex_search('Thomas', r'^thomas$') is None

    # Explicit ignorecase=True should match
    assert regex_search('Thomas', r'^thomas$', ignorecase=True) == 'Thomas'

    # Default and explicit multiline=False should behave the same
    assert regex_search('Thomas\nBerger\n', r'berger', multiline=False) is None
    assert regex_search('Thomas\nBerger\n', r'berger') is None

    # Explicit multiline=True should match

# Generated at 2022-06-22 11:44:56.088412
# Unit test for function flatten
def test_flatten():
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, [2, 3, 4], 5]) == [1, 2, 3, 4, 5]
    assert flatten([1, [2, 3, 4], 5], levels=1) == [1, 2, 3, 4, 5]
    assert flatten([1, [2, 3, 4], 5], levels=2) == [1, 2, 3, 4, 5]
    assert flatten([1, [2, 3, 4], 5], levels=3) == [1, 2, 3, 4, 5]

# Generated at 2022-06-22 11:45:07.361137
# Unit test for function do_groupby
def test_do_groupby():
    """
    Unit test for function do_groupby
    """
    # get the do_groupby function that is used in the filter plugin
    do_groupby = globals()['do_groupby']
    # rename this function, so it can be called in the unit test
    _do_groupby = do_groupby
    del do_groupby
    # create an environment that we can pass to the groupby function
    # this needs to be a subclass of Environment, so that the _do_groupby
    # function is able to extract the getitem function
    class DummyEnvironmentForTest(_do_groupby.environmentfilter.environment):
        def __init__(self, **kwargs):
            super(DummyEnvironmentForTest, self).__init__(**kwargs)

# Generated at 2022-06-22 11:45:18.932774
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template.vars import AnsibleJ2Vars
    import jinja2
    mydict = [{'age': 25, 'name': 'foo'},
              {'age': 18, 'name': 'bar'},
              {'age': 25, 'name': 'baz'},
              {'age': 25, 'name': 'qux'}]
    env = jinja2.Environment()
    env.filters['groupby'] = do_groupby
    env.globals = AnsibleJ2Vars({'mydict': mydict})

# Generated at 2022-06-22 11:45:22.040199
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('./library/*.py') == ['library/filter_plugins/core.py']



# Generated at 2022-06-22 11:45:28.560944
# Unit test for function flatten
def test_flatten():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    lists = [[1, dict(test="test"), 3], [4, AnsibleUnsafeText('this is encrypted'), 6]]
    lists_flatten = flatten(lists)

    assert 1 in lists_flatten
    assert 'test' in lists_flatten
    assert 3 in lists_flatten
    assert 4 in lists_flatten
    assert 6 in lists_flatten
    assert lists_flatten[1] == AnsibleUnsafeText('this is encrypted')



# Generated at 2022-06-22 11:45:45.133038
# Unit test for function combine
def test_combine():
    assert combine() == {}
    assert combine({}) == {}
    assert combine({1: 1}) == {1: 1}
    assert combine({1: 1}, {}) == {1: 1}
    assert combine({1: 1}, {1: 2}) == {1: 2}
    assert combine({1: 1}, {2: 2}) == {1: 1, 2: 2}
    assert combine({1: 1}, {1: 2}, {2: 3}) == {1: 2, 2: 3}
    assert combine({1: 1}, {1: 2}, {1: 3}) == {1: 3}
    assert combine({1: {2: 2}}, {1: {3: 3}}) == {1: {2: 2, 3: 3}}

# Generated at 2022-06-22 11:45:55.115313
# Unit test for function comment
def test_comment():
    assert comment('') == '#  '
    assert comment(
        '',
        style='erlang') == '%  '
    assert comment(
        '',
        style='c') == '//  '
    assert comment(
        '',
        style='cblock') == '/*\n *  */'
    assert comment(
        '',
        style='xml') == '<!--\n -  -->'
    assert comment(
        '',
        style='xml',
        decoration='=') == '<!--\n =  -->'
    assert comment(
        '',
        style='cblock',
        decoration='=') == '/*\n =  */'
    assert comment(
        '',
        decoration='=') == '# =  '

# Generated at 2022-06-22 11:46:01.436422
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/bin/ls') == ['/bin/ls']
    assert fileglob('/bin/c*') == ['/bin/cat', '/bin/chgrp', '/bin/chmod', '/bin/chown', '/bin/cp', '/bin/cpio', '/bin/cut']



# Generated at 2022-06-22 11:46:08.624501
# Unit test for function regex_search
def test_regex_search():
    assert(regex_search('a', 'a')) == 'a'
    assert(regex_search('ab', 'a')) == 'a'
    assert(regex_search('ab', 'a', '\\g<1>b'))[0] == 'a'
    assert(regex_search('ab', 'a', '\\1b'))[0] == 'a'



# Generated at 2022-06-22 11:46:20.878686
# Unit test for function do_groupby
def test_do_groupby():
    env = Environment()
    assert do_groupby(env, [], '0') == []
    assert do_groupby(env, [{'x': 1}, {'x': 2}, {'x': 1}], 'x') == [(1, [{'x': 1}, {'x': 1}]), (2, [{'x': 2}])]
    assert do_groupby(env, [{'x': 1}, {'x': 2}, {'x': 1}], 'y') == []
    # Test that objects that are not dicts/lists are coerced into
    # being lists containing the object
    assert do_groupby(env, [(1, 2), (2, 3), (1, 3)], '0') == [(1, [(1, 2), (1, 3)]), (2, [(2, 3)])]


# Generated at 2022-06-22 11:46:33.714524
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    # test formatting a list
    data = [1,2,3]
    out = to_nice_yaml(data)
    assert(out == '- 1\n- 2\n- 3')
    # test formatting a dict
    data = {'a':1, 'b':2, 'c':3}
    out = to_nice_yaml(data)
    assert(out == 'a: 1\nb: 2\nc: 3')
    # test formatting a complex object
    data = {'a':1, 'b':[1,2,3], 'c':{'d':1,'e':2}, 'f':['a','b','c']}
    out = to_nice_yaml(data)

# Generated at 2022-06-22 11:46:44.831398
# Unit test for function extract
def test_extract():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()


# Generated at 2022-06-22 11:46:56.744550
# Unit test for function extract
def test_extract():
    env = DummyEnvironment()
    ret = extract(env, 'v1', {'k1': {'v1': 1, 'v2': 2}})
    assert ret == 1
    ret = extract(env, 'v2', {'k1': {'v1': 1, 'v2': 2}}, 'k1')
    assert ret == 2
    ret = extract(env, 'v2', [{'k1': {'v1': 1, 'v2': 2}}], 0)
    assert ret == 2
    ret = extract(env, 'v2', [{'k1': {'v1': 1, 'v2': 2}}, {'k2': 3}], 0)
    assert ret == 2

# Generated at 2022-06-22 11:46:58.049350
# Unit test for function subelements
def test_subelements():
    import doctest
    results = doctest.testmod(subelements)
    if not results.failed:
        return True
    else:
        raise AnsibleFilterError('subelements filter unit test failed')



# Generated at 2022-06-22 11:47:05.104349
# Unit test for function extract
def test_extract():
    # First, make sure that the normal use case works
    result = extract('mykey', {"mykey": [1, 2, 3]})
    assert result == [1, 2, 3]

    # Now, make sure that the fall through to the list works as expected
    result = extract('nothere', "Hello World", "orhere")
    assert result == "Hello World"

    # Now make sure that it works if we provide more keys
    result = extract('firstkey', {"firstkey": {"secondkey": "hello"}}, "secondkey")
    assert result == "hello"

    # Now make sure that it works if we provide more keys as a list
    result = extract('firstkey', {"firstkey": {"secondkey": "hello"}}, ["secondkey"])
    assert result == "hello"

    # Make sure that if we don't match anything,

# Generated at 2022-06-22 11:47:22.091407
# Unit test for function extract
def test_extract():
    "filter.extract works as expected"
    env = DummyEnvironment()


# Generated at 2022-06-22 11:47:34.601362
# Unit test for function comment
def test_comment():
    '''Unit test for function comment'''
    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp(prefix='tmp-ansible-test-filter-comment')
    fn = os.path.join(tmpdir, 'test')

# Generated at 2022-06-22 11:47:41.179212
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'a*b') == r'a\*b'
    assert regex_escape(r'1+2') == r'1\+2'
    assert regex_escape('a') == 'a'
    assert regex_escape(r'a*b', re_type='posix_basic') == r'a\*b'



# Generated at 2022-06-22 11:47:49.871497
# Unit test for function to_bool
def test_to_bool():
    """
    Test cases to test bool conversion
    """
    # Test boolean values
    assert to_bool(True)
    assert not to_bool(False)

    # Test string and number values
    assert to_bool('1')
    assert to_bool('true')
    assert to_bool('yes')
    assert to_bool('on')
    assert to_bool(1)

    # Test other values
    assert not to_bool('false')
    assert not to_bool('off')
    assert not to_bool(0)
    assert not to_bool(None)



# Generated at 2022-06-22 11:47:52.218823
# Unit test for function strftime
def test_strftime():
    assert(strftime('%a') == time.strftime('%a'))



# Generated at 2022-06-22 11:47:57.050117
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'class': 'Giraffe', 'name': 'George'}) == u'{name: George, class: Giraffe}\n'
    assert to_nice_yaml({'class': 'Giraffe', 'name': 'George'}, indent=2) == u'{name: George,\n  class: Giraffe}\n'



# Generated at 2022-06-22 11:48:03.860922
# Unit test for function do_groupby
def test_do_groupby():
    # To test this function, it needs to be a part of the filters.
    # That is a larger change than I want to make right now, however it is easy
    # to implement as a separate function.
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Environment
    from jinja2.runtime import Context
    from jinja2.runtime import StrictUndefined
    from jinja2.exceptions import UndefinedError
    from jinja2.exceptions import TemplateRuntimeError
    from jinja2.filters import do_groupby

    # The do_groupby function in jinja2 can accept a list, any iterable, or a mapping,
    # which we want to test.
    test_

# Generated at 2022-06-22 11:48:14.700802
# Unit test for function combine
def test_combine():
    """
    This is not a unit test per-se, but a way to alleviate development burden by
    running arbitrary code in an environment where the filters described in this
    module are available.

    test_combine_list() is designed so that it can be copied into a playbook
    and the output observed.
    """
    import json
    from ansible.plugins.filter.core import combine

    def test_combine_list(list_merge='replace', recursive=True):
        """
        Example of how combine() works with lists.
        """
        lists = [
            [],
            [1, 2, 3],
            ['a', 'b', 'c'],
            [None, None, None],
            [{}, {'a': 'b'}],
        ]

# Generated at 2022-06-22 11:48:21.561167
# Unit test for function do_groupby
def test_do_groupby():
    test_list = [{"a": 1, "b": "x"}, {"a": 2, "b": "y"}, {"a": 1, "b": "z"}]
    expected_list = [(1, [{"a": 1, "b": "x"}, {"a": 1, "b": "z"}]), (2, [{"a": 2, "b": "y"}])]

    class FakeEnvironment(object):
        def __init__(self):
            self.name = "ansible-{0}".format(uuid4())
        def getitem(self, obj, key):
            return obj[key]

    fake_env = FakeEnvironment()
    ret = do_groupby(fake_env, test_list, "a")
    assert expected_list == ret


# Generated at 2022-06-22 11:48:32.045654
# Unit test for function extract
def test_extract():
    # pylint: disable=undefined-variable
    assert extract('a', {'a': 1}) == 1
    assert extract('a', {'a': {'b': 2}}) == {'b': 2}
    assert extract('b', {'a': {'b': 2}}, 'a') == 2
    assert extract('b', {'a': {'b': 2}}, ['a']) == 2
    assert extract('b', {'a': {'b': 2}}, ['a', 'b']) == 2
    assert extract('a', ['a', 'b']) == 'a'



# Generated at 2022-06-22 11:48:49.339279
# Unit test for function combine
def test_combine():
    assert_equals(combine({}, {}), {})
    assert_equals(combine({'a': 1}, {}), {'a': 1})
    assert_equals(combine({'a': 1}, {'a': 2}), {'a': 2})
    assert_equals(combine({'a': 1}, {'a': {'b': 2}}), {'a': {'b': 2}})
    assert_equals(combine({'a': {'b': 2}}, {'a': 1}), {'a': 1})
    assert_equals(combine(({'a': {'b': 2}}, {'a': 1}),  recursive=True), {'a': {'b': 2}})

# Generated at 2022-06-22 11:48:51.485342
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({1:2}) == '{1: 2}'


# Generated at 2022-06-22 11:49:01.832313
# Unit test for function to_yaml
def test_to_yaml():
    # example data structure
    a = { 'one': 1, 'two': [2, 3, 4], 'three': { 'four': 4, 'five': [ None, 5, 'six' ] } }
    # expected result
    b = """\
---
one: 1
three:
  five:
  - ~
  - 5
  - six
  four: 4
two:
- 2
- 3
- 4
"""
    # actual result
    c = to_yaml(a)
    # compare results
    if b != c:
        raise Exception('to_yaml failed: expected "%s", got "%s"' % (b, c))

# ---- Jinja2 filters ----


# Generated at 2022-06-22 11:49:14.435672
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('bar: foo, baz: foo', 'baz: (\S+)') == "foo"
    assert regex_search('bar: foo, baz: foo', 'baz: (\S+)', '\\1') == "foo"
    assert regex_search('bar: foo, baz: foo', 'baz: (\S+)', '\\g<1>') == "foo"
    assert regex_search('bar: foo, baz: foo', 'baz: (\S+)', '\\1', '\\g<1>') == ["foo", "foo"]
    assert regex_search('bar: span(foo), baz: span(foo)', 'baz: span\(\S+\)', '\\g<1>') == "span(foo)"

# Generated at 2022-06-22 11:49:20.351035
# Unit test for function regex_search
def test_regex_search():
    match = regex_search('foobar', r'foo', '\\g<1>')
    assert match == 'foo'

    match = regex_search('foobar', r'foo(bar)', '\\g<1>')
    assert match == 'bar'

    match = regex_search('foobar', r'foo(bar)', '\\1')
    assert match == 'bar'


# Generated at 2022-06-22 11:49:32.164904
# Unit test for function comment
def test_comment():
    # Test: predefined comment style 'c'
    assert(comment("""\
Compilation of a C program
Including some C block
""",
                   style='c') == """\
// Compilation of a C program
// Including some C block
""")

    # Test: predefined comment style 'cblock'
    assert(comment("""\
Compilation of a C program
Including some C block
""",
                   style='cblock') == """\
/*
 * Compilation of a C program
 * Including some C block
 */
""")

    # Test: predefined comment style 'erlang'
    assert(comment("""\
Compilation of an Erlang program
Including some Erlang block
""",
                   style='erlang') == """\
% Compilation of an Erlang program
% Including some Erlang block
""")

   

# Generated at 2022-06-22 11:49:36.011422
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    expected = """
- a: 1
- b: 4
- c: 8
"""
    assert to_nice_yaml([{'a': 1}, {'b': 4}, {'c': 8}]) == expected



# Generated at 2022-06-22 11:49:47.127127
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('test string', hashtype='md5') == '2daa99b3c3b4a4b4f4c1fdfd4a4a7d75'
    assert get_hash('test string', hashtype='sha1') == '58c7cb17d3d3a8f0a6eef0317e154cf1f2d1fc61'
    assert get_hash('test string', hashtype='sha224') == '03ef36e9b27d2121e8f8c201eefd6b25c6badbf38cd8ad04f0b1e964'

# Generated at 2022-06-22 11:49:50.874105
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml([1, 2]) == u'---\n- 1\n- 2\n'
    assert to_yaml({"x": "y"}) == u'---\nx: y\n'



# Generated at 2022-06-22 11:50:01.762226
# Unit test for function regex_search
def test_regex_search():
    rst = regex_search('black box', r'\w+\s+\w+')
    assert rst == 'black box'
    rst = regex_search('black box', r'\w+\s+\w+', '\\g<1>')
    assert rst == 'black'
    rst = regex_search('black box', r'\w+\s+\w+', '\\g<2>')
    assert rst == 'box'
    rst = regex_search('black box', r'\w+\s+\w+', '\\1')
    assert rst == 'black'
    rst = regex_search('black box', r'\w+\s+\w+', '\\2')
    assert rst == 'box'
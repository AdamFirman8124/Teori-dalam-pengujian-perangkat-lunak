

# Generated at 2022-06-22 11:40:36.283816
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('Hello', r'^\w+') == 'Hello'
    assert regex_search('Hello', r'^\w+', '\\g<0>') == 'Hello'
    assert regex_search('Hello', r'^\w+', '\\g<0>', '\\g<0>') == ['Hello', 'Hello']
    assert regex_search('Hello', r'^\w+', '\\0') == 'Hello'
    assert regex_search('Hello', r'^\w+', '\\0', '\\0') == ['Hello', 'Hello']
    assert regex_search('Hello', r'^\w+', '\\1') == None
    assert regex_search('Hello', r'^\w+(\s\w+)?', '\\g<0>') == 'Hello'
    assert regex_search

# Generated at 2022-06-22 11:40:43.079773
# Unit test for function extract
def test_extract():
    assert extract('a', {'a': 'b'}) == 'b', "test_extract #1 failed"
    assert extract('a', {'a': {'b': 'c'}}, 'b') == 'c', "test_extract #2 failed"
    assert extract('a', {'a': {'b': 'c'}}, ['b']) == 'c', "test_extract #3 failed"



# Generated at 2022-06-22 11:40:51.538025
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'a.b[c]d.^e$f*g\\h|i') == r'a\.b\[c\]d\.\^e\$f\*g\\h\|i'
    assert regex_escape('a.b[c]d.^e$f*g\\h|i', re_type='posix_basic') == r'a\.b\[c\]d\.\^e\$f\*g\h\i'
    assert regex_escape(r'a.b[c]d.^e$f*g\\h|i', re_type='posix_extended') == r'a\.b\[c\]d\.\^e\$f\*g\\h\|i'



# Generated at 2022-06-22 11:40:54.654329
# Unit test for function subelements
def test_subelements():
    from ansible.module_utils import six
    from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
    import doctest
    import sys

    failed, tests = doctest.testmod(sys.modules[__name__])
    sys.stdout.write("%d tests failed\n" % failed)
    if failed <= 0:
        sys.exit(0)
    else:
        sys.exit(1)



# Generated at 2022-06-22 11:40:58.961808
# Unit test for function fileglob
def test_fileglob():
    '''
    Return test name as string if function fileglob works else return False
    '''
    name = sys._getframe().f_code.co_name
    if not fileglob('test_fileglob*'):
        return False
    return name



# Generated at 2022-06-22 11:41:08.302540
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(None) == None
    assert mandatory(1) == 1

    try:
        mandatory(AnsibleUndefined)
        assert False
    except AnsibleFilterError as e:
        assert "Mandatory variable '<unknown>' not defined." in to_native(e)

    try:
        mandatory(AnsibleUndefined, "foo")
        assert False
    except AnsibleFilterError as e:
        assert "foo" in to_native(e)



# Generated at 2022-06-22 11:41:19.721530
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('/path/to/something', r'[a-z]+/\.+', '\\g<0>') == 'to/.'
    assert regex_search('/path/to/something', r'[a-z]+/\.+', '\\0') == 'to/.'
    assert regex_search('/path/to/something', r'[a-z]+/\.+', '\\1') == ''
    assert regex_search('/path/to/something', r'[a-z]+/(\.+)', '\\1') == '.'
    assert regex_search('/path/to/something', r'[a-z]+/(\.+)', '\\2') == ''
    assert regex_search('/path/to/something', r'[a-z]+/(\.)', '\\g<1>') == '.'

# Generated at 2022-06-22 11:41:28.456346
# Unit test for function regex_search
def test_regex_search():
    '''Unit test for function regex_search'''
    assert regex_search("12345", "(\d+)(\d+)", "\\1") == "12"
    assert regex_search("12345", "(\d+)(\d+)", "\\2") == "34"
    assert regex_search("12345", "(?P<one>\d+)(?P<two>\d+)", "\\g<one>", "\\g<two>") == ['12', '34']
    assert regex_search("12345", "(?P<one>\d+)(?P<two>\d+)", "\\1", "\\2") == ['12', '34']



# Generated at 2022-06-22 11:41:39.094330
# Unit test for function regex_search
def test_regex_search():
    assert None == regex_search('foo', 'not found')
    assert 'it matches' == regex_search('it matches', '^it.*es$')
    assert 'bar' == regex_search('123 bar 456', r'bar')
    assert 'bar' == regex_search('123 bar 456', r'\g<0>')
    assert '123' == regex_search('123 bar 456', r'^(.*) ')

# Generated at 2022-06-22 11:41:50.722906
# Unit test for function strftime
def test_strftime():
    secs = 1546343600.0
    assert strftime("%Y-%m-%d %H:%M:%S") == "2019-01-01 12:00:00"
    assert strftime("%Y-%m-%d %H:%M:%S", secs) == "2019-01-01 12:00:00"
    assert strftime("%Y-%m-%d", secs) == "2019-01-01"
    assert strftime("%F %H:%M:%S") == "2019-01-01 12:00:00"
    assert strftime("%F %H:%M:%S", secs) == "2019-01-01 12:00:00"
    assert strftime("%F", secs) == "2019-01-01"



# Generated at 2022-06-22 11:42:11.573777
# Unit test for function mandatory
def test_mandatory():
    from jinja2.exceptions import UndefinedError
    from jinja2.runtime import Undefined

    undefined = Undefined(hint=None, obj=None, name=None)

    try:
        mandatory(undefined)
    except AnsibleFilterError:
        pass
    except Exception as e:
        raise
    else:
        raise AssertionError('Exception not raised')

    try:
        mandatory(undefined, msg="A message")
    except AnsibleFilterError as e:
        pass
    except Exception as e:
        raise
    else:
        raise AssertionError('Exception not raised')

    try:
        mandatory("abc")
    except AnsibleFilterError as e:
        raise
    except Exception as e:
        raise


# Generated at 2022-06-22 11:42:23.044441
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import Template

    class TestValue:

        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    env = TemplateEnvironment()
    env.filters['groupby'] = do_groupby

    data = []
    data.append(TestValue('a', '1', 2, 3))
    data.append(TestValue('b', '4', 5, 6))
    data.append(TestValue('a', '7', 8, 9))
    data.append(TestValue('a', 'x', 'y', 'z'))
    data.append(TestValue('b', '12', 13, 14))


# Generated at 2022-06-22 11:42:28.111502
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list(['a', 'b', 'c']) == ['b', 'a', 'c']
    assert randomize_list([1, 2, 3], seed='foobar') == [2, 1, 3]



# Generated at 2022-06-22 11:42:37.133330
# Unit test for function randomize_list
def test_randomize_list():
    # test on list
    assert sorted(randomize_list([1,2,3,4], seed=42)) == sorted([4,3,1,2])
    # test on set
    assert sorted(randomize_list({1,2,3}, seed=42)) == sorted([2,1,3])
    # test that it works on other iterable types
    myiter = (x for x in [1,2,3])
    assert sorted(randomize_list(myiter, seed=42)) == sorted([2,1,3])



# Generated at 2022-06-22 11:42:49.919216
# Unit test for function regex_search
def test_regex_search():
    assert(regex_search('abc-def-ghi', 'xyz') is None)
    assert(regex_search('abc-def-ghi', 'a') == 'a')
    assert(regex_search('abc-def-ghi', '-') == '-')
    assert(regex_search('abc-def-ghi', '^a') == 'a')
    assert(regex_search('abc-def-ghi', '^abc') == 'abc')
    assert(regex_search('abc-def-ghi', 'h') == 'h')
    assert(regex_search('abc-def-ghi', '^h') is None)
    assert(regex_search('abc-def-ghi', 'i$') == 'i')

# Generated at 2022-06-22 11:42:53.440731
# Unit test for function extract
def test_extract():
    e = Environment()
    d = {'a': {'b': {'c': 1, 'd': {'e': 2}}}}
    assert extract(e, 'c', d) == 1
    assert extract(e, 'e', d, 'a', 'b', 'd') == 2
    assert 'a' in d
    assert 'e' not in d
    return True



# Generated at 2022-06-22 11:42:58.009504
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('sample') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'



# Generated at 2022-06-22 11:43:10.761639
# Unit test for function subelements
def test_subelements():
    foo = [
        {
            "name": "alice",
            "groups": [
                "wheel",
                "staff"
            ],
            "authorized": [
                "/tmp/alice/onekey.pub",
                "/home/alice/.ssh/id_rsa.pub"
            ]
        },
        {
            "name": "joe",
            "groups": [
                "staff",
                "dev"
            ],
            "authorized": [
                "/home/joe/.ssh/id_rsa.pub"
            ]
        }
    ]


# Generated at 2022-06-22 11:43:12.933180
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/*/*') == glob.glob('/etc/*/*')



# Generated at 2022-06-22 11:43:17.807291
# Unit test for function comment
def test_comment():
    assert comment('', 'plain') == '# '
    assert comment('foo') == '# foo'
    assert comment('foo', style='c') == '// foo'
    assert comment(
        'foo',
        decoration='* ') == '* foo'
    assert comment(
        'foo',
        decoration='* ',
        beginning='# BEGIN',
        end='# END') == '# BEGIN\n* foo\n# END'
    assert comment(
        'foo',
        decoration='* ',
        prefix='# ',
        end='# END') == '* foo\n# # END'
    assert comment(
        'foo',
        decoration='* ',
        prefix='# ',
        prefix_count=2,
        end='# END') == '* foo\n# # # END'

# Generated at 2022-06-22 11:43:30.591221
# Unit test for function rand
def test_rand():
    assert rand(None, 1) == 0
    assert rand(None, 0) == 0
    assert rand(None, [0]) == 0
    assert rand(None, [0, 1]) in (0, 1)
    assert rand(None, [0, 1], 0) in (0, 1)
    assert rand(None, [0, 1, 2], 1, 2) in (1, 3)
    assert rand(None, [0, 1, 2], seed=0) in (0, 1, 2)
    assert rand(None, [0, 1, 2], seed=1) == 1



# Generated at 2022-06-22 11:43:41.583112
# Unit test for function combine
def test_combine():
    from ansible.module_utils.common.collections import ImmutableDict
    from operator import or_

    def _test_combine_for_recursive_list_merge(recursive, list_merge):
        assert combine({'a': 1, 'b': 3},
                       {'b': 2, 'c': 3}) == {'a': 1, 'b': 2, 'c': 3}
        assert combine({'a': 1, 'b': 2},
                       {'a': 2, 'c': 3}) == {'a': 2, 'b': 2, 'c': 3}

# Generated at 2022-06-22 11:43:44.067259
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('ok') == 'ok'
    try:
        assert mandatory(None)
        assert False
    except AssertionError:
        pass
    try:
        assert mandatory(None, "msg")
        assert False
    except AssertionError:
        pass



# Generated at 2022-06-22 11:43:56.305287
# Unit test for function mandatory

# Generated at 2022-06-22 11:44:05.720559
# Unit test for function regex_findall
def test_regex_findall():
    def t(str, regex, ignorecase=False, multiline=False, expected=[]):
        value = regex_findall(str, regex, ignorecase, multiline)
        assert expected == value, "%s should have matched %s but matched %s instead" % (str, expected, value)
    t("a1b2c3d4e5f6", "([a-z][0-9])", True, True, ['a1'])
    t("a1b2c3d4e5f6", "([a-z][0-9])", True, False, ['a1'])
    t("a1b2c3d4e5f6", "([a-z][0-9])", False, True, [])

# Generated at 2022-06-22 11:44:16.721694
# Unit test for function regex_findall
def test_regex_findall():
    assert regex_findall("abcdefabcdefabcdef", "abc") == ["abc", "abc", "abc"]
    assert regex_findall("ABCDEFabcdefabcdef", "abc", ignorecase=True) == ["ABC", "abc", "abc"]
    assert regex_findall("ABCDEFabcdefabcdef", "abc", ignorecase=False) == ["abc"]
    assert regex_findall("ABCDEFabcdefabcdef", "abc", ignorecase=True, multiline=True) == ["ABC", "abc", "abc", "def", "abc", "abc", "def"]
    assert regex_findall("ABCDEFabcdefabcdef", "abc", ignorecase=False, multiline=True) == ["abc", "def", "abc", "abc", "def"]

# Generated at 2022-06-22 11:44:20.050445
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    a = dict(name="John", age=42,
              children=["Jane", "Jill", "Jack"])
    b = to_nice_yaml(a)
    print(b)

# test_to_nice_yaml()


# Generated at 2022-06-22 11:44:30.605126
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(value="abcdefg", pattern="def", replacement="DEF") == "abcDEFg"
    assert regex_replace(value="abcdefg", pattern="def", replacement="DEF", ignorecase=True) == "abcDEFg"
    assert regex_replace(value="abcdefg", pattern="def", replacement="DEF", ignorecase=False) == "abcDEFg"
    assert regex_replace(value="abcdefg", pattern="def", replacement="DEF", ignorecase=True, multiline=True) == "abcDEFg"
    assert regex_replace(value="abcdefg", pattern="def", replacement="DEF", ignorecase=False, multiline=True) == "abcDEFg"

# Generated at 2022-06-22 11:44:33.375568
# Unit test for function to_yaml
def test_to_yaml():
    var = {'a': 'b'}
    assert 'a: b' in to_yaml(var)



# Generated at 2022-06-22 11:44:45.337078
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo', r'foo') == 'foo'
    assert regex_search('foo', r'bar') is None
    assert regex_search('foo', r'f(o)o') == 'oo'
    assert regex_search('foo', r'f(o)o', '\\1') == ['o']
    assert regex_search('foo', r'f(o)o', '\\g<1>') == ['o']
    assert regex_search('abc123def456ghi', r'\d+', '\\g<0>') == ['123', '456']
    assert regex_search('abc123def456ghi', r'\d+', '\\g<0>', ignorecase=True) == ['123', '456']

# Generated at 2022-06-22 11:44:57.599479
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(None) is None
    assert mandatory('value') == 'value'
    try:
        mandatory(None, 'test')
        assert False
    except AnsibleFilterError:
        assert True
    try:
        mandatory(None, None)
        assert False
    except AnsibleFilterError:
        assert True



# Generated at 2022-06-22 11:45:08.104976
# Unit test for function do_groupby
def test_do_groupby():

    # For grouping by a list of items
    a = [{'name': 'bob', 'group': ['admins', 'dev']},
         {'name': 'john', 'group': 'dev'},
         {'name': 'susan', 'group': 'ops'}]
    b = do_groupby(a, 'group')
    expected = [('admins', [{'group': ['admins', 'dev'], 'name': 'bob'}]),
                ('dev', [{'group': 'dev', 'name': 'john'},
                         {'group': ['admins', 'dev'], 'name': 'bob'}]),
                ('ops', [{'group': 'ops', 'name': 'susan'}])]
    assert b == expected

    # For grouping by a list of items and then by

# Generated at 2022-06-22 11:45:19.606015
# Unit test for function mandatory
def test_mandatory():

    def f_assertion_error(var, msg=None, assertion_msg=None):
        try:
            mandatory(var, msg)
            assert False
        except AssertionError:
            assert True
        except AnsibleFilterError:
            if assertion_msg:
                assert False, assertion_msg
            else:
                assert True

    def f_assert_equal(a, b):
        try:
            res = mandatory(a)
            assert False
        except AssertionError:
            assert True
        except AnsibleFilterError as e:
            assert False, 'Unexpected AnsibleFilterError: "%s"' % to_native(e)
        else:
            assert res == b

    from jinja2.runtime import Undefined
    assert isinstance(Undefined(), AnsibleUndefined)


# Generated at 2022-06-22 11:45:23.451903
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'a': 'slkdjf', 'b': 'sdfsdf'}) == '''\
a: slkdjf
b: sdfsdf
'''


# Generated at 2022-06-22 11:45:30.024388
# Unit test for function regex_search
def test_regex_search():
    from ansible.module_utils.common.collections import ImmutableDict
    data = {
        "value": "blah",
        "regex": r"\b(\w+)",
        "args": ["\\g<1>"],
        "kw": ImmutableDict(ignorecase=True),
    }
    assert regex_search(**data) == "blah"



# Generated at 2022-06-22 11:45:40.069566
# Unit test for function do_groupby
def test_do_groupby():
    # we need a jinja2 environment
    from jinja2 import Environment
    from ansible.template import Templar

    env = Environment()

    # we need a jinja2 template first
    template = env.from_string("{{ [{'id': 1, 'foo': 'one'}, {'id': 2, 'foo': 'two'}, {'id': 2, 'foo': '3'}] | groupby(attribute='id') | list }}")

    # now we have the template, and we can compile it
    template_compiled = template.compile()

    # now we need a vars dictionary on which to render the template
    vars = {}

    # create a templar to parse the result
    templar = Templar(loader=None, variables=vars)

    # and finally we render, using the templ

# Generated at 2022-06-22 11:45:47.627608
# Unit test for function randomize_list
def test_randomize_list():
    if randomize_list(['1','2','3']) != ['1','2','3']:
        return False
    elif randomize_list(['1','2','3'],seed='foo') == ['1','2','3']:
        return False
    else:
        return True

#@environmentfilter
#def randomize_list(environment, mylist, seed=None):
#    try:
#        r = Random(seed)
#    except TypeError:
#        r = SystemRandom()
#    mylist = list(mylist)
#    r.shuffle(mylist)
#    return mylist



# Generated at 2022-06-22 11:45:59.494758
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("abcd efg", "^[a-z]*\s[a-z]*$") == "abcd efg"
    assert regex_search("abcd efg", "^[a-z]*\s[a-z]*$", '\g<0>') == "abcd efg"
    assert regex_search("abcd efg", "^[a-z]*\s[a-z]*$", '\g<1>') == None
    assert regex_search("abcd efg", "^([a-z]*)\s([a-z]*)$", '\g<1>') == "abcd"

# Generated at 2022-06-22 11:46:07.444865
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(42) == 42
    assert mandatory(42, msg='my custom message') == 42
    assert mandatory(2, msg='my custom message') == 2
    try:
        mandatory(AnsibleUndefined())
    except AnsibleError as e:
        assert "Mandatory variable 'foo' not defined." in to_native(e)
    try:
        mandatory(AnsibleUndefined(), msg='my custom message')
    except AnsibleError as e:
        assert "my custom message" in to_native(e)



# Generated at 2022-06-22 11:46:19.933812
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import JinjaEnvironment
    jenv = JinjaEnvironment(extensions=['jinja2.ext.do'])
    jenv.filters.update({'groupby': do_groupby})

    func_args = [([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}], 'a'),]
    expected_results = [
        [(1, [{'a': 1, 'b': 2}]), (3, [{'a': 3, 'b': 4}]), (5, [{'a': 5, 'b': 6}])]
    ]


# Generated at 2022-06-22 11:46:30.910451
# Unit test for function randomize_list
def test_randomize_list():
    mylist = ['a', 'b', 'c', 'd', 'e']
    mylist_copy = mylist[:]

    new_list = randomize_list(mylist)
    # Check that the list has effectively been reordered
    assert new_list != mylist

    new_list = randomize_list(mylist, seed=42)
    assert new_list == mylist_copy



# Generated at 2022-06-22 11:46:39.252491
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'a': [1, 2, 3], 'b': True}) == '{a: [1, 2, 3], b: true}\n'
    assert to_yaml({'a': [1, 2, 3], 'b': True}, default_flow_style=False) == 'a:\n- 1\n- 2\n- 3\nb: true\n'
    assert to_yaml({'a': '123', 'b': True}, default_flow_style=False) == 'a: "123"\nb: true\n'


# Generated at 2022-06-22 11:46:43.778703
# Unit test for function do_groupby
def test_do_groupby():
    # the jinja2 `do_groupby` function is only used in a Filter environment.
    # here we create a fake class that has a name attribute, so it's
    # more closely simulates what would happen in a real filter env
    class FakeEnv(object):
        def __init__(self, name):
            self.name = name

        def getattr(self, value, attribute):
            return getattr(value, attribute)

    # make a fake env
    fake_env = FakeEnv('do_groupby')

# Generated at 2022-06-22 11:46:54.523435
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('1234567890', r'\d+') == '1234567890'
    assert regex_search('1234567890', r'\g<1>', r'\\g<1>') == ['1234567890', '1234567890']
    assert regex_search('1234567890', r'\g<1>', r'\\1') == ['1234567890', '1234567890']
    assert regex_search('10 and 20 are not 30', r'(\d)+ and (\d)+', r'\\2 \\1', ignorecase=True) == ['20 10']
    assert regex_search(' 10 and 20 are not 30', r'(\d)+ and (\d)+', r'\\2 \\1', ignorecase=True) == ['20 10']

# Generated at 2022-06-22 11:47:03.665322
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Template
    from collections import namedtuple
    from ansible.template import templar

    tpl = Template('{% set my_group = [{ "foo": 1, "bar": "A" }, { "foo": 2, "bar": "B" }, { "foo": 1, "bar": "C" }] | groupby("foo") %}'
                   '{% for group in my_group %}'
                   '{{ group.0.foo }}:'
                   '{% for item in group %} {{ item.bar }}{% endfor %},'
                   '{% endfor %}')

    tm = templar.Templar(loader=None)
    tm._available_variables = dict()
    res = tm.template(tpl)
    assert '1: A C,'

# Generated at 2022-06-22 11:47:12.097664
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('hello world', r'hello') == 'hello'
    assert regex_search('hello world', r'hello', '\\g<0>') == ['hello', 'hello']
    assert regex_search('hello world', r'hello', '\\0', '\\g<0>') == ['hello', 'hello', 'hello']
    assert regex_search('hello world', r'hello', '\\1') == []
    assert regex_search('hello world', r'hello', '\\g<1>') == []
    assert regex_search('hello world', r'hello', '\\g<nonmatch>') == []
    assert regex_search('hello world', r'hello', '\\g<nonmatch>', '\\g<0>') == ['hello']

# Generated at 2022-06-22 11:47:20.175015
# Unit test for function regex_search
def test_regex_search():
    with pytest.raises(AnsibleFilterError):
        regex_search("word1 word2", r"(word1) (word2)", "\\g<1>")
    with pytest.raises(AnsibleFilterError):
        regex_search("word1 word2", r"(word1) (word2)", "\\1")
    with pytest.raises(AnsibleFilterError):
        regex_search("word1 word2", r"(word1) (word2)", "dog")
    assert regex_search("word1 word2", r"(word1) (word2)", "\\2") == "word2"
    assert regex_search("word1 word2", r"(word1) (word2)", "\\1") == "word1"

# Generated at 2022-06-22 11:47:29.893414
# Unit test for function regex_search
def test_regex_search():
    data = dict(
        url='https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=test',
        url_no_port='http://api.test.com/',
        ipv4='192.168.1.1',
        ipv6='fe80::8a0:2122:fff:eeee:891b%7',
        ipv6_no_address='fe80::8a0:2122:fff:eeee:%7',
        fqdn='www.google.com',
    )

# Generated at 2022-06-22 11:47:42.045743
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('bar', 'oo') == None
    assert regex_search('bar', 'oo', multiline=True) == None
    assert regex_search('foo', 'oo') == 'oo'
    assert regex_search('b1a,r2a', '\d+') == '1'
    assert regex_search('b1a', '\d+') == '1'
    assert regex_search('b1a,r2a', '\d+', '\d') == ['1', '2']
    assert regex_search('b1a,r2a', '\d+', '\d', ignorecase=True) == ['1', '2']
    assert regex_search('b1a,r2a', '\d+', '\d', multiline=True) == ['1', '2']
   

# Generated at 2022-06-22 11:47:52.773271
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(42) == 42
    assert mandatory(None) == None

    try:
        mandatory(None, 'custom message')
    except AnsibleFilterError as e:
        assert 'custom message' in str(e)

    from jinja2.runtime import Undefined
    try:
        mandatory(Undefined)
    except AnsibleFilterError as e:
        assert 'Mandatory variable not defined' in str(e)

    undefined_var = Undefined(name='my_var')
    try:
        mandatory(undefined_var)
    except AnsibleFilterError as e:
        assert 'Mandatory variable \'my_var\' not defined.' in str(e)



# Generated at 2022-06-22 11:48:12.732832
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert [({"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}, 'wheel')] == subelements(obj, 'groups')
    assert [({"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}, '/tmp/alice/onekey.pub')] == subelements(obj, 'authorized')
    assert [({"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}, 'alice')] == subelements(obj, 'name')



# Generated at 2022-06-22 11:48:24.254132
# Unit test for function subelements
def test_subelements():
    '''subelements unit tests'''

    # test that the subelements function returns the correct output
    def test_subelements_values(obj, subelements, expected_result):
        '''subelements unit tests'''
        result = subelements(obj, subelements)

        if not isinstance(result, list):
            raise AssertionError("subelements returned a non-list type: %r" % result)

        if len(result) != len(expected_result):
            raise AssertionError("subelements returned a list of incorrect length: expected %d, got %d" % (len(expected_result), len(result)))


# Generated at 2022-06-22 11:48:31.834930
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    import pytest

    with pytest.raises(AnsibleFilterError):
        mandatory(Undefined())

    with pytest.raises(AnsibleFilterError):
        mandatory(None)

    with pytest.raises(AnsibleFilterError):
        mandatory("")

    with pytest.raises(AnsibleFilterError):
        mandatory("", msg='foo')

    assert mandatory("foo") == "foo"



# Generated at 2022-06-22 11:48:45.128459
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.plugins.filter.core import FilterModule
    import jinja2
    template_path = ':memory:'
    dataloader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=dataloader)
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-22 11:48:56.353179
# Unit test for function comment
def test_comment():
    import pprint

    pp = pprint.PrettyPrinter(indent=2)

    pp.pprint(comment(
        "text",
        beginning=os.linesep,
        decoration="--",
        end=""))
    pp.pprint(comment(
        "text",
        beginning="<!--",
        decoration="--",
        end="-->"))
    pp.pprint(comment(
        "text",
        beginning="<!--",
        decoration="--",
        end="-->"))
    pp.pprint(comment(
        "text",
        decoration="..",
        end=""))
    pp.pprint(comment(
        "text",
        beginning="#",
        decoration="",
        end=""))

# Generated at 2022-06-22 11:49:01.790935
# Unit test for function randomize_list
def test_randomize_list():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert (randomize_list(x) != x)
    y = randomize_list(x)
    assert (randomize_list(x, seed=1) == y)
    assert (y != randomize_list(x, seed=2))


# Generated at 2022-06-22 11:49:03.441356
# Unit test for function subelements
def test_subelements():
    import doctest
    doctest.testmod()



# Generated at 2022-06-22 11:49:09.712865
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]



# Generated at 2022-06-22 11:49:21.710181
# Unit test for function extract
def test_extract():
    import jinja2
    env = jinja2.Environment()
    env.globals['extract'] = extract
    container = [1, 2, 3, 4, 5]
    template = '''{{extract(0, container)}}'''
    rendered = env.from_string(template).render(container=container)
    assert rendered == '1'
    template = '''{{extract(0, container, morekeys=[1, 1, 1])}}'''
    rendered = env.from_string(template).render(container=container, morekeys=[1])
    assert rendered == '2'
    container = {'a': ['the', 'quick', 'brown', 'fox']}
    template = '''{{extract(0, container, 'a')}}'''
    rendered = env.from_string(template).render

# Generated at 2022-06-22 11:49:33.258372
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2

    env = jinja2.Environment()
    tmpl = env.from_string('''
    {% set test = ['a1', 'b1', 'b2', 'c1', 'c2', 'c3'] %}
    {% set groups = test|groupby('1')|list %}
    {{ groups }}
    ''')
    assert tmpl.render(to_native=to_text) == "[('a', ['a1']), ('b', ['b1', 'b2']), ('c', ['c1', 'c2', 'c3'])]"

    # if jinja2 is the system version, ensure that the issue we are fixing does not happen
    #   see https://github.com/ansible/ansible/issues/20098
    jinja2_

# Generated at 2022-06-22 11:50:03.492529
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abc123def456', r'\d+', '\\g<0>') == '123'
    assert regex_search('abc123def456', r'\d+', '\\2') == '123'
    assert regex_search('abc123def456', r'(?P<num_3>\d{3})(?P<num_6>\d{3})', '\\g<num_3>') == '123'
    assert regex_search('abc123def456', r'(?P<num_3>\d{3})(?P<num_6>\d{3})', '\\g<num_3>', '\\g<num_6>') == ['123', '456']

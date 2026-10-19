

# Generated at 2022-06-22 11:40:37.191191
# Unit test for function extract
def test_extract():
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    hosts = ["localhost"]
    play_context = PlayContext(vault_password='secret')
    vault_secrets = VaultLib([])
    variable_manager = VariableManager(loader=None, inventory=InventoryManager(hosts=hosts))

    # Case 1:
    # Access a value in a list
    # keys: [3]
    test_data = {'a': ['b', 'c', 'd', 'e']}
    extract_value = extract(test_data, 3, environment=variable_manager, play_context=play_context, vault_secrets=vault_secrets)

# Generated at 2022-06-22 11:40:46.447622
# Unit test for function regex_search
def test_regex_search():
    value = 'Item1 Item2 Item3 Item4 Item5 Item6 Item7'
    # expected results
    results1 = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6', 'Item7']
    results2 = ['Item2', 'Item3', 'Item4', 'Item5', 'Item6', 'Item7']
    results3 = ['Item2', 'Item4', 'Item6']
    results4 = ['Item1', 'Item3', 'Item5', 'Item7']
    results5 = ['Item2']
    results6 = ['Item1', 'Item3', 'Item5', 'Item7']
    results7 = ['Item2', 'Item4', 'Item6', 'Item8']
    # run tests

# Generated at 2022-06-22 11:40:53.157656
# Unit test for function regex_replace
def test_regex_replace():
    ''' Validate that a regex is replaced correctly in the given value.
        Assuming a string of 'banana' is passed to regex_replace with the pattern an and the replacement xyz
        the final output should be bxzanax.
    '''
    # Test single occurence
    final_string = regex_replace(value='banana', pattern='an', replacement='xyz')
    assert final_string == 'bxzanax'

    # Test multiple occurence
    final_string = regex_replace(value='banana', pattern='a', replacement='xyz')
    assert final_string == 'bxyznxyz'

    # Test regex special character
    final_string = regex_replace(value='banana', pattern='^b', replacement='xyz')
    assert final_string == 'xyzanana'



# Generated at 2022-06-22 11:40:59.183767
# Unit test for function regex_escape
def test_regex_escape():
    # Python test cases
    assert regex_escape('^$*[]') == r'\^\$\*\[\]'
    # POSIX BRE test cases
    assert regex_escape('^$*[]', re_type='posix_basic') == r'\^\$\*\[\]'
    # TODO: add POSIX ERE test cases



# Generated at 2022-06-22 11:41:13.547945
# Unit test for function flatten
def test_flatten():
    ''' Ansible jinja2 filter unit test
        -------------------------------
        This unit test uses the pytest unit test framework.
        To run it use:
           - py.test -v

        Test that the 'flatten' filter flattens the given list
        with the following syntax:
        - mylist | flatten [levels]
        - mylist | flatten 2
        - mylist | flatten 1
        - mylist | flatten 0
    '''
    # Test that the 'flatten' filter flattens lists as expected
    assert flatten(mylist=["Hello", "world", {"a": 1, "b": 2, "c": 3}]) == ["Hello", "world", 1, 2, 3]

# Generated at 2022-06-22 11:41:24.242758
# Unit test for function regex_search
def test_regex_search():
  assert None != regex_search("foobar2baz", "bar")
  assert None != regex_search("foobar2baz", "bar2")
  assert None == regex_search("foobar2baz", "foo", "\\g<1>")
  assert ["bar"] == regex_search("foobar2baz", "foo(bar)", "\\g<1>")
  assert ["bar2baz"] == regex_search("foobar2baz", "(bar2baz)")
  assert ["bar", "baz"] == regex_search("foobar2baz", "(bar)|(baz)")
  assert ["bar2baz"] == regex_search("foobar2baz", "(?P<word>bar2baz)")

# Generated at 2022-06-22 11:41:31.387091
# Unit test for function flatten
def test_flatten():
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, ['foo', 'bar'], 3]) == [1, 'foo', 'bar', 3]
    assert flatten([1, ['foo', ['baz', 'qux', 'quux'], 3]]) == [1, 'foo', 'baz', 'qux', 'quux', 3]
    assert flatten([1, ['foo', ['baz', 'qux', 'quux'], 3], 4], levels=1) == [1, 'foo', ['baz', 'qux', 'quux'], 3, 4]

# Generated at 2022-06-22 11:41:39.910316
# Unit test for function ternary
def test_ternary():
    assert ternary(1, 'a', 'b') == 'a'
    assert ternary(0, 'a', 'b') == 'b'
    assert ternary(None, 'a', 'b') == 'b'
    assert ternary(None, 'a', 'b', 'c') == 'c'
    assert ternary('', 'a', 'b') == 'b'
    assert ternary('foo', 'a', 'b') == 'a'
    assert ternary(False, 'a', 'b') == 'b'
    assert ternary(['foo'], 'a', 'b') == 'a'
    assert ternary(dict(), 'a', 'b') == 'a'



# Generated at 2022-06-22 11:41:50.595538
# Unit test for function flatten
def test_flatten():
    assert flatten([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert flatten([1, 2, [3, 4, 5], [6, 7], 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert flatten([1, 2, [3, 4, 5], 6, [7], [8, 9, 10]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert flatten([1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# Generated at 2022-06-22 11:42:00.692073
# Unit test for function comment
def test_comment():
    # Tests for plain style
    assert comment("foo", style='plain') == "# foo"
    assert comment("foo", style='plain', decoration='+ ') == "+ foo"
    assert comment("foo", style='plain', decoration='+ ', newline='\n') == "+ foo"
    assert comment("foo\nbar\nbaz", style='plain') == "# foo\n# bar\n# baz"
    assert comment("foo\n\nbar\nbaz",
                   style='plain') == "# foo\n# \n# bar\n# baz"
    assert comment("foo\n\nbar\nbaz",
                   style='plain', prefix_count=2) == "#\n# foo\n# \n# bar\n# baz"

# Generated at 2022-06-22 11:42:08.710710
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(None) is None
    assert mandatory("some") == "some"
    assert mandatory("some", "Some message") == "some"



# Generated at 2022-06-22 11:42:18.512325
# Unit test for function mandatory
def test_mandatory():
    # Test mandatory variable
    assert mandatory(1, 2) == 1
    # Test undefined variable
    try:
        mandatory(AnsibleUndefined(name='foo'))
    except AnsibleFilterError as err:
        assert str(err) == "Mandatory variable 'foo' not defined."
    else:
        raise Exception('Expecting exception')
    # Test undefined variable with customized error message
    try:
        mandatory(AnsibleUndefined(name='foo'), msg='bar')
    except AnsibleFilterError as err:
        assert str(err) == "bar"
    else:
        raise Exception('Expecting exception')
    # Test undefined variable with empty name (not possible through jinja2)

# Generated at 2022-06-22 11:42:28.659036
# Unit test for function mandatory
def test_mandatory():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import ansible.constants as C

    vars = VariableManager()
    env = dict()
    templar = Templar(loader=None, variables=vars, shared_loader_obj=None)
    assert templar.template('{{ foo | mandatory }}', from_any_context=True, preserve_trailing_newlines=True,
                            convert_bare=C.DEFAULT_BOOLEAN_CONVERSION_ERRORS,
                            fail_on_undefined=C.DEFAULT_UNDEFINED_VAR_BEHAVIOR) == 'FAILED! >>> Mandatory variable not defined.'



# Generated at 2022-06-22 11:42:41.084577
# Unit test for function fileglob
def test_fileglob():
    files_present = ['one.txt', 'two.txt', 'three.txt']
    files_absent = ['notme.txt', 'notmeeither.txt']

    for fp in files_present:
        open(fp, 'w').close()

    basedir = os.getcwd()
    assert fileglob('*.txt') == sorted(['%s/%s' % (basedir, fp) for fp in files_present])
    if not os.path.exists(os.path.join(basedir, '*.txt')):
        assert fileglob('*.txt') == sorted(['%s/%s' % (basedir, fp) for fp in files_present])


# Generated at 2022-06-22 11:42:51.663195
# Unit test for function regex_replace
def test_regex_replace():
    cases = [
        ('abc', '^(?P<val1>a)(?P<val2>b)(?P<val3>c)', 'val1=\\g<val1> val2=\\g<val2> val3=\\g<val3>', 'val1=a val2=b val3=c'),
        ('abc', '^(a)(b)(c)', 'val1=\\1 val2=\\2 val3=\\3', 'val1=a val2=b val3=c'),
        # multiline replacement
        ('abc\nabc', '^(a)(b)(c)', 'val1=\\1\nval2=\\2\nval3=\\3', 'val1=a\nval2=b\nval3=c'),
    ]

# Generated at 2022-06-22 11:42:58.791331
# Unit test for function mandatory
def test_mandatory():
    from __main__ import env
    env = {'mandatory_variable': 'value',
           'mandatory_variable_undef': 'value',
           'nested': {
              'mandatory_variable_undef': 'value',
           }}

    assert mandatory(env['mandatory_variable']) == 'value'
    assert mandatory(env['nested']['mandatory_variable_undef']) == 'value'

    try:
        mandatory(env['mandatory_variable_undef'])
    except AnsibleFilterError as e:
        assert e.message == "Mandatory variable 'mandatory_variable_undef' not defined."

    assert mandatory(env['nested']['mandatory_variable_undef']) == 'value'

# Generated at 2022-06-22 11:43:04.016600
# Unit test for function mandatory
def test_mandatory():
    assert(mandatory(1) == 1)
    assert(mandatory('abc') == 'abc')
    assert(mandatory({'a':1}) == {'a':1})
    try:
        ret = mandatory(None)
        raise AssertionError("should not get here")
    except AnsibleFilterError:
        pass
    try:
        ret = mandatory(AnsibleUndefined("foo"))
        raise AssertionError("should not get here")
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:43:16.071010
# Unit test for function subelements

# Generated at 2022-06-22 11:43:18.658739
# Unit test for function regex_search
def test_regex_search():
    value = 'spam eggs'
    regex = '\w+(?=\s[eggs])'
    assert regex_search(value, regex) == 'spam'


# Generated at 2022-06-22 11:43:27.202632
# Unit test for function mandatory
def test_mandatory():
    from ansible.template import Jinja2TemplateModule
    tm = Jinja2TemplateModule(None, None, None)
    assert tm._apply_filter(u'mandatory', Jinja2TemplateModule.UNDEFINED, ()) is Jinja2TemplateModule.UNDEFINED
    try:
        tm._apply_filter(u'mandatory', Jinja2TemplateModule.UNDEFINED, (u'foo',))
    except AnsibleError:
        assert True
    else:
        assert False  # pragma: no cover



# Generated at 2022-06-22 11:43:38.335931
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1) == 1
    assert mandatory(0) == 0
    assert mandatory([]) == []
    assert mandatory("") == ""
    assert mandatory(False) is False
    try:
        mandatory()
    except AnsibleFilterError:
        pass
    else:
        fail("Expected an exception")
    try:
        mandatory(None)
    except AnsibleFilterError:
        pass
    else:
        fail("Expected an exception")



# Generated at 2022-06-22 11:43:50.425013
# Unit test for function extract
def test_extract():
    env = Environment()


# Generated at 2022-06-22 11:43:59.704164
# Unit test for function do_groupby
def test_do_groupby():
    # jinja2 is not a requirement, so restrict this test to when
    # ansible-base is installed
    from ansible.module_utils._text import to_bytes
    try:
        import jinja2
    except ImportError:
        return
    from jinja2.template import Template
    template = Template("{{ {1: {'a': 0}, 2: {'a': 1}, 3: {'a': 1}}|groupby('a')|list }}")
    env = jinja2.Environment()
    assert template.render(env) == template.render(env)
    # we can no longer do this test here, as jinja2.GroupTuple is defined in
    # jinja2/runtime.py and jinja2/runtime.py is not bundled with ansible
    # if LooseVersion(

# Generated at 2022-06-22 11:44:04.353507
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    data = [{"foo1": "bar1"}, {"foo2": "bar2"}]
    result = to_nice_yaml(data)
    expected = '''- foo1: bar1
- foo2: bar2
'''
    assert result == expected



# Generated at 2022-06-22 11:44:10.557732
# Unit test for function do_groupby
def test_do_groupby():
    # It is a generator, so we need to consume it for the actual test
    # We could use next(iterator) but we want to keep compatibility with python2 as well
    list(do_groupby([{'test': 1}, {'test': 2}], 'test'))



# Generated at 2022-06-22 11:44:17.752257
# Unit test for function randomize_list
def test_randomize_list():
    mylist = [1, 2, 3, 4, 5, 6]
    # The randomization should be deterministic
    # with a seed, so the result should always
    # be the same
    expected = [6, 3, 1, 5, 4, 2]
    assert randomize_list(mylist, seed=1) == expected



# Generated at 2022-06-22 11:44:28.900786
# Unit test for function comment
def test_comment():
    def compare(expected, returned):
        try:
            assert expected == returned
        except Exception as e:
            raise e

    # No params, no decoration
    # =========================
    expected = '''This is a line.
This is another line
'''
    returned = comment(expected)
    compare(expected, returned)

    # No params, with decoration
    # ==========================
    expected = '''# This is a line.
# This is another line
'''
    returned = comment(expected, decoration='# ')
    compare(expected, returned)

    # Multiline, no decoration
    # ========================
    expected = '''Multiline
    text
    '''
    returned = comment(expected, beginning='Multiline', prefix='    ')
    compare(expected, returned)

    # Multiline, with

# Generated at 2022-06-22 11:44:33.196442
# Unit test for function to_bool
def test_to_bool():
    assert(to_bool(True) is True)
    assert(to_bool(False) is False)
    assert(to_bool('true') is True)
    assert(to_bool('false') is False)
    assert(to_bool('foo') is False)
    assert(to_bool(1) is True)
    assert(to_bool(0) is False)
    assert(to_bool([]) is False)



# Generated at 2022-06-22 11:44:44.347170
# Unit test for function to_bool
def test_to_bool():
    assert to_bool('true') is True
    assert to_bool('True') is True
    assert to_bool('TRUE') is True
    assert to_bool('yes') is True
    assert to_bool('Yes') is True
    assert to_bool('YES') is True
    assert to_bool('y') is True
    assert to_bool('Y') is True
    assert to_bool('1') is True
    assert to_bool('on') is True
    assert to_bool('On') is True
    assert to_bool('ON') is True
    assert to_bool(True) is True
    assert to_bool('false') is False
    assert to_bool('False') is False
    assert to_bool('FALSE') is False
    assert to_bool('no') is False
    assert to_bool('No') is False

# Generated at 2022-06-22 11:44:50.327368
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('hello', r'l|L', 'XX') == 'heXXo'
    assert regex_replace('hello', r'l|L', 'XX', ignorecase=True) == 'heXXo'
    assert regex_replace('Hello', r'l|L', 'YY', ignorecase=True) == 'HeYYo'



# Generated at 2022-06-22 11:45:12.180257
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("hello",r'\w') == "h"
    assert regex_search("hello",r'\w') == "h"
    assert regex_search("hello",r'\w',ignorecase=True) == "h"
    assert regex_search("hello",r'((\w)\w)',ignorecase=True) == "hello"
    assert regex_search("hello",r'((\w)\w)',ignorecase=True,multiline=True) == "hello"

# Generated at 2022-06-22 11:45:17.738765
# Unit test for function mandatory
def test_mandatory():
    assert mandatory("foo") == "foo"
    try:
        mandatory(AnsibleUndefined("Foo", 'myvar'))
        assert False
    except AnsibleFilterError:
        pass
    try:
        mandatory(AnsibleUndefined("Foo", 'myvar'), msg="foobar")
        assert False
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:45:30.995235
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment, StrictUndefined
    from collections import namedtuple
    a = namedtuple('a', 'foo bar')
    b = namedtuple('b', 'foo bar')
    environment = Environment(undefined=StrictUndefined)
    value = [a(1, 2), a(1, 3), b(2, 4), b(2, 5), a(1, 6)]
    result = do_groupby(environment, value, 'foo')
    assert result == [
        (1, [tuple(a(1, 2)), tuple(a(1, 3)), tuple(a(1, 6))]),
        (2, [tuple(b(2, 4)), tuple(b(2, 5))]),
    ]



# Generated at 2022-06-22 11:45:33.484334
# Unit test for function fileglob
def test_fileglob():
    assert fileglob("test/test*.yml") == [ 'test/test1.yml', 'test/test2.yml' ]



# Generated at 2022-06-22 11:45:46.020464
# Unit test for function regex_replace
def test_regex_replace():
    '''Test regex_replace'''
    # Simple substitution
    assert 'one two three four' == regex_replace('one#two#three four', pattern='#', replacement=' ')
    assert 'one 1 two 3' == regex_replace('one 1 two 3', pattern='[0-9]+', replacement='#')
    # Ignore case
    assert 'ONE TWO' == regex_replace('one two', pattern='[oO][Nn][Ee]', replacement='ONE', ignorecase=True)
    assert 'ONE two' == regex_replace('one two', pattern='[oO][Nn][Ee]', replacement='ONE', ignorecase=False)
    # Multi-line
    assert 'one\ntwo' == regex_replace('one\ntwo', pattern='2', replacement='2\n', multiline=True)

# Generated at 2022-06-22 11:45:58.360702
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import JinjaEnvironment
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import UndefinedError, Undefined

    env = JinjaEnvironment(undefined=StrictUndefined)
    env.filters['groupby'] = do_groupby

    # test grouping of list of dicts

    data = dict(a=[
        dict(a=1, b=1, c=1),
        dict(a=1, b=2, c=2),
        dict(a=2, b=1, c=2),
    ])

    # test dict with string key
    tpl = '{{ a | groupby("a") | list }}'
    r = env.from_string(tpl).render(data)

    # check type and value
    assert isinstance(r, SafeText)


# Generated at 2022-06-22 11:46:05.161212
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    ret = subelements(obj, 'groups')
    assert ret == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]



# Generated at 2022-06-22 11:46:11.090511
# Unit test for function do_groupby
def test_do_groupby():
    # Tests in this file are only run on Python 2
    # The tests in the groupby_spec.py are run on Python 2&3
    assert do_groupby([{'name': 'Terry', 'age': 43}, {'name': 'Bob', 'age': 42}, {'name': 'Terry', 'age': 42}], 'name') == [('Bob', [{'name': 'Bob', 'age': 42}]), ('Terry', [{'name': 'Terry', 'age': 43}, {'name': 'Terry', 'age': 42}])]



# Generated at 2022-06-22 11:46:16.603581
# Unit test for function to_yaml
def test_to_yaml():
    test_dict = {'1': {'2': 3, '4': ['5', '6']}}
    result = to_yaml(test_dict)
    assert result == u"{1: {2: 3, 4: [5, 6]}}\n", "Expected {1: {2: 3, 4: [5, 6]}}\n and got %s" % result


# Generated at 2022-06-22 11:46:22.917670
# Unit test for function fileglob
def test_fileglob():
    # searching for nonexistent files should return an empty list
    assert fileglob('') == []
    assert fileglob('i-dont-exist') == []
    assert fileglob('i-dont-exist-*') == []
    assert fileglob('test/test/*') == []
    assert fileglob('test/test/test') == []



# Generated at 2022-06-22 11:46:38.427827
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import Jinja2Environment

    env = Jinja2Environment(undefined=AnsibleUndefined)
    mylist = [{'a': 1, 'b': 1, 'c': 1}, {'a': 2, 'b': 2, 'c': 2}, {'a': 1, 'b': 1, 'c': 2}, {'a': 1, 'b': 2, 'c': 1}]
    expected_result = [(1, [{'b': 1, 'c': 1, 'a': 1}, {'b': 1, 'c': 2, 'a': 1}]), (2, [{'b': 2, 'c': 2, 'a': 2}, {'b': 2, 'c': 1, 'a': 1}])]


# Generated at 2022-06-22 11:46:49.638410
# Unit test for function do_groupby
def test_do_groupby():
    assert do_groupby([], 'a') == []
    assert do_groupby({}, 'a') == []
    assert do_groupby({'a': 1}, 'a') == []
    assert do_groupby([{'a': 'b'}], 'a') == []
    assert do_groupby([{'a': 'b'}], 'b') == [('b', [{'a': 'b'}])]
    assert do_groupby([{'a': 'b'}, {'a': 'b'}], 'a') == [('b', [{'a': 'b'}, {'a': 'b'}])]

# Generated at 2022-06-22 11:47:00.038876
# Unit test for function comment
def test_comment():
    assert comment('test') == '# test'
    assert comment('test', decoration='## ') == '## test'
    assert comment('test', decoration='', prefix='//') == '// test'
    assert comment('test', decoration='', postfix='//') == 'test //'
    assert comment('test\nmulti\nline') == '# test\n# multi\n# line'
    assert comment('test\nmulti\nline', postfix='') == '# test\n# multi\n# line'
    assert comment('test\nmulti\nline', decoration='##', postfix='') == '## test\n## multi\n## line'
    assert comment('test\nmulti\nline', decoration='## ', postfix='') == '## test\n## multi\n## line'

# Generated at 2022-06-22 11:47:02.742045
# Unit test for function fileglob
def test_fileglob():
    pathname = "./testpath/*"
    assert fileglob(pathname) == ['./testpath/file3.txt']



# Generated at 2022-06-22 11:47:11.414004
# Unit test for function subelements
def test_subelements():
    import pytest
    obj = {'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}
    expected = [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]
    assert list(subelements(obj, 'groups')) == expected
    assert list(subelements(obj, ['groups'])) == expected
    with pytest.raises(AnsibleFilterTypeError):
        list(subelements(obj, 1))
    with pytest.raises(AnsibleFilterError):
        list(subelements(obj, 'not_a_key'))

# Generated at 2022-06-22 11:47:18.109898
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo bar', 'a') is None
    assert regex_search('foo bar', 'f') == 'f'
    assert regex_search('foo bar', 'f', '\\g<0>') == 'f'
    assert regex_search('foo bar', 'f', '\\1') == 'f'
    assert regex_search('foo bar', 'o', '\\g<0>', '\\g<0>') == ['o', 'o']
    assert regex_search('foo bar', 'o', '\\2', '\\1') == ['oo', 'o']



# Generated at 2022-06-22 11:47:29.440126
# Unit test for function do_groupby
def test_do_groupby():
    # test with namedtuple
    result = _do_groupby(DummyEnvironment(), [{'value': 1}, {'value': 1}, {'value': 2}, {'value': 3}, {'value': 3}], 'value')
    assert len(result) == 3
    assert (1, [{'value': 1}, {'value': 1}]) in result
    assert (2, [{'value': 2}]) in result
    assert (3, [{'value': 3}, {'value': 3}]) in result
    # test with tuple
    result = _do_groupby(DummyEnvironment(), [{'value': (1, 1)}, {'value': (1, 1)}, {'value': (2, 1)}, {'value': (3, 1)}, {'value': (3, 1)}], 'value')

# Generated at 2022-06-22 11:47:41.882084
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    # Test for defined variables
    assert(mandatory(1, 'test1') == 1)
    assert(mandatory(True, 'test2') is True)
    assert(mandatory('f', 'test3') == 'f')

    # Test for undefined variables
    try:
        mandatory(dict(a='b')['b'])
    except AnsibleFilterError as e:
        assert(to_text(e) == "Mandatory variable 'a' not defined.")
    else:
        assert(False)
    try:
        mandatory(dict(a=1)['b'])
    except AnsibleFilterError as e:
        assert(to_text(e) == "Mandatory variable 'b' not defined.")
    else:
        assert(False)

# Generated at 2022-06-22 11:47:50.188920
# Unit test for function mandatory
def test_mandatory():
    x = temporary_loader()
    assert jinja2.Environment(loader=x).from_string('{{ mandatory() }}').render() == ''
    assert jinja2.Environment(loader=x).from_string('{{ mandatory(1) }}').render() == '1'
    assert jinja2.Environment(loader=x).from_string('{{ mandatory(b=1) }}').render().startswith('Mandatory variable')
    assert jinja2.Environment(loader=x).from_string('{{ mandatory(msg="1") }}').render() == 'Mandatory variable not defined. (1)'



# Generated at 2022-06-22 11:47:57.340678
# Unit test for function fileglob
def test_fileglob():
    pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testkit", "files", "fileglob.d", "*.ini")
    assert 2 == len(fileglob(pathname))
    pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testkit", "files", "fileglob.d", "*.foo")
    assert 0 == len(fileglob(pathname))


# Generated at 2022-06-22 11:48:09.976006
# Unit test for function do_groupby
def test_do_groupby():
    env = jinja2.Environment()
    filter_ = env.filters['do_groupby']
    value = [{'key': 'K1', 'value': 1}, {'key': 'K1', 'value': 2}, {'key': 'K2', 'value': 3}]
    assert filter_(value, 'key') == [('K1', [{'key': 'K1', 'value': 1}, {'key': 'K1', 'value': 2}]), ('K2', [{'key': 'K2', 'value': 3}])]



# Generated at 2022-06-22 11:48:19.675034
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/tmp/ansible_fileglob_test_file*') == []
    open('/tmp/ansible_fileglob_test_file1', 'a').close()
    open('/tmp/ansible_fileglob_test_file2', 'a').close()
    assert set(fileglob('/tmp/ansible_fileglob_test_file*')) in [
        set(['/tmp/ansible_fileglob_test_file1', '/tmp/ansible_fileglob_test_file2']),
        set(['/tmp/ansible_fileglob_test_file2', '/tmp/ansible_fileglob_test_file1']),
    ]
    os.remove('/tmp/ansible_fileglob_test_file1')
    os.remove

# Generated at 2022-06-22 11:48:32.626846
# Unit test for function do_groupby
def test_do_groupby():
    class List(list):
        def __getitem__(self, key):
            if not isinstance(key, integer_types):
                raise TypeError(
                    "List indices must be integers, not %s" % str(type(key))
                )
            return super(List, self).__getitem__(key)
    class Dict(dict):
        def __getitem__(self, key):
            if key not in self:
                raise KeyError('dict key %s not found' % key)
            return super(Dict, self).__getitem__(key)
    class Environment(object):
        def __init__(self, dict_cls):
            self.dict_cls = dict_cls

# Generated at 2022-06-22 11:48:35.495335
# Unit test for function fileglob
def test_fileglob():
    pathname = 'playbooks/*.yml'
    assert isinstance(fileglob(pathname), list)



# Generated at 2022-06-22 11:48:40.047262
# Unit test for function fileglob
def test_fileglob():
    assert ['foo.txt'] == fileglob('foo.txt')
    assert ['foo.txt'] == fileglob('./foo.txt')
    assert ['foo.txt'] == fileglob('*.txt')
    assert ['foo.txt', 'bar.txt'] == fileglob('*.txt')



# Generated at 2022-06-22 11:48:45.835204
# Unit test for function mandatory
def test_mandatory():
    f = partial(mandatory, msg="Foo")
    assert f(10) == 10
    assert f(0) == 0
    assert f("Example") == "Example"
    assert f("") == ""
    assert f({}) == {}
    assert f({'a': 1}) == {'a': 1}
    assert f(['a']) == ['a']

    try:
        assert f()
    except AnsibleFilterError:
        pass
    else:
        assert False  # Should have raised an exception
    try:
        assert f(None)
    except AnsibleFilterError:
        pass
    else:
        assert False  # Should have raised an exception



# Generated at 2022-06-22 11:48:54.077914
# Unit test for function extract
def test_extract():
    literal = [
        { "one" : 'foo' },
        { "two" : 'bar' },
        { "three" : 'baz' }
    ]

    assert 'foo' == extract('one', literal), "extract(\"one\", literal) should return 'foo'"
    assert 'bar' == extract(['two'], literal), "extract(['two'], literal) should return 'bar'"
    assert 'baz' == extract('three', literal, 'second'), "extract('three', literal, 'second') should return 'baz'"



# Generated at 2022-06-22 11:49:06.396531
# Unit test for function comment

# Generated at 2022-06-22 11:49:09.456900
# Unit test for function regex_replace
def test_regex_replace():
    result = regex_replace("aaaaaaaaaa", "a", "b")
    assert result == "bbbbbbbbbb"


# Generated at 2022-06-22 11:49:17.551255
# Unit test for function regex_search
def test_regex_search():
    filter_regex_search = regex_search
    # Default is search for the first match
    assert filter_regex_search('one two three', 'two') == 'two'

    # \\3 matches the third match
    assert filter_regex_search('one two three', '\w+', '\\3') == ['three']

    # \\g<1> matches group 1
    assert filter_regex_search('one two three', '(\w+) (\w+) (\w+)', '\\g<1>') == ['one']


# Generated at 2022-06-22 11:49:32.560905
# Unit test for function randomize_list
def test_randomize_list():
    test_list = [1, 2, 3, 4]
    # Test for seed value
    mylist = randomize_list(test_list, "seed")
    assert mylist == [2, 4, 3, 1]
    # Test for no seed value
    mylist = randomize_list(test_list)
    assert mylist != [2, 4, 3, 1]
    # Test for invalid seed value
    mylist = randomize_list(test_list, [])
    assert mylist == []
    mylist = randomize_list(test_list, {})
    assert mylist == {}
    mylist = randomize_list(test_list, 0)
    assert mylist == [1, 2, 3, 4]
    # Test for invalid list
    mylist = randomize_list(0)
    assert mylist

# Generated at 2022-06-22 11:49:41.666167
# Unit test for function subelements
def test_subelements():
    base_obj = [
        {
            'name': 'alice',
            'groups': ['wheel'],
            'authorized': [
                '/tmp/alice/onekey.pub',
                '/tmp/alice/twokey.pub'
            ]
        }
    ]
    assert subelements(base_obj, 'groups') == [
        (base_obj[0], 'wheel')
    ]
    assert subelements(base_obj, 'authorized') == [
        (base_obj[0], '/tmp/alice/onekey.pub'),
        (base_obj[0], '/tmp/alice/twokey.pub')
    ]



# Generated at 2022-06-22 11:49:44.564673
# Unit test for function regex_search
def test_regex_search():
    # We expect a TypeError here because we passed a string instead of a regex
    try:
        regex_search('abc', 'abc')
    except TypeError:
        pass
    assert regex_search('abc', r'abc') == 'abc'



# Generated at 2022-06-22 11:49:55.714849
# Unit test for function comment

# Generated at 2022-06-22 11:50:00.973980
# Unit test for function regex_search
def test_regex_search():
    value = "https://jira.domain.com/browse/JIRA-123"
    assert regex_search(value, r'(?<=https?://[^/]+/browse/)[^/]+.*$') == 'JIRA-123'

# End of unit test for function regex_search



# Generated at 2022-06-22 11:50:13.739321
# Unit test for function get_hash
def test_get_hash():
    # the value is not unicode because it contains literal u, but the default encoding is utf-8
    assert get_hash(u'unicode string') == u'8e0b72fea479744b7e15e08a8ddc0ec2b3f9b3ee'
    assert get_hash(u'unicode string', u'sha256') == u'2a0d80a7f1dd39e18f4a4a68a4e7d2de970aefca9c75f4397b8f0b46394c0e51'
    assert get_hash(u'unicode string', u'ripemd160') == u'c5a3aac6f2c6f8d8d13b6f4900ab9dcb55dda0b7'
    assert get
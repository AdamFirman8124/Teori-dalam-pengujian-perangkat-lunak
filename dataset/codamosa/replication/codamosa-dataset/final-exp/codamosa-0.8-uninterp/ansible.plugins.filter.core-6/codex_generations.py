

# Generated at 2022-06-22 11:40:46.540696
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('hello, world', 'hello', '\\g<0>') == 'hello'
    assert regex_search('hello, world', 'l+', '\\g<0>') == 'll'
    assert regex_search('hello, world', 'hello', '\\1') == 'hello'
    assert regex_search('hello, world', 'l+', '\\1') == 'll'
    assert regex_search('hello, world', 'l+', '\\1', '\\2')[0] == 'll'
    assert regex_search('hello, world', 'l+', '\\1', '\\2')[1] == 'l'
    assert regex_search('hello, world', 'l+', '\\2', '\\1')[0] == 'l'

# Generated at 2022-06-22 11:40:53.207587
# Unit test for function subelements
def test_subelements():
    test_elements = [
        {
            "name": "alice",
            "groups": ["wheel", "dev"],
            "authorized": ["/tmp/alice/onekey.pub"]
        },
        {
            "name": "bob",
            "authorized": ["/tmp/bob/onekey.pub"]
        }
    ]

    test1 = subelements(test_elements, 'groups')
    assert isinstance(test1, list)
    assert len(test1) == 4
    assert ('wheel',) in [t[1] for t in test1]
    assert ('dev',) in [t[1] for t in test1]

    test2 = subelements(test_elements, 'not.a.real.key')
    assert len(test2) == 0


# Generated at 2022-06-22 11:41:00.815131
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo.bar*baz?') == 'foo\\.bar\\*baz\\?'
    assert regex_escape('foo.bar*baz?', re_type='posix_basic') == 'foo\\.bar\\*baz\\?'
    with pytest.raises(AnsibleFilterError) as excinfo:
        regex_escape('foo.bar*baz?', re_type='fake')
    assert 'Invalid regex type (fake)' in str(excinfo.value)



# Generated at 2022-06-22 11:41:08.576779
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'foo': 'bar'}) == "---\nfoo: bar\n"
    assert to_nice_yaml({'foo': 'bar'}, indent=2) == "---\n  foo: bar\n"
    assert to_nice_yaml({'foo': 'bar'}, indent=2, width=15) == "---\n  foo: bar\n"



# Generated at 2022-06-22 11:41:20.072324
# Unit test for function subelements
def test_subelements():
    import pytest
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]
    assert subelements(obj, 'groups', skip_missing=True) == []
    assert subelements(obj[0], 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]
    assert subelements(obj[0], 'groups', skip_missing=True) == []

# Generated at 2022-06-22 11:41:21.910250
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(None) == None
    assert mandatory(False) == False
    assert mandatory(True) == True


# Generated at 2022-06-22 11:41:35.403774
# Unit test for function combine
def test_combine():
    '''Unit test for function combine'''
    filter_ = FilterModule()
    filter_loader = filter_.filters()

    dict_template = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': {'e_a': 0, 'e_b': 0, 'e_c': 0}, 'f': [0, 1, 2], 'g': 0}
    dict_r1 = {'a': 1, 'b': 1, 'c': 1}
    dict_r2 = {'c': 2, 'd': 2}
    dict_r3 = {'d': 3, 'e': {'e_a': 3, 'e_b': 3, 'e_c': 3}, 'g': 3}

# Generated at 2022-06-22 11:41:48.273089
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("test string", "test (?P<str>string)") == "test string"
    assert regex_search("test string", r"test (?P<str>string)", r'\g<str>') == 'string'
    assert regex_search("test string", r"test (?P<str>string)", r'\g<str>', '\\1') == ['string', 'string']
    assert regex_search("test string", r"test (?P<str>string)", '\\1') == 'string'
    assert regex_search("test 123 string", r"test (?P<num>\d+) string", '\\g<num>') == '123'

# Generated at 2022-06-22 11:41:56.825189
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    # Check different kind of input
    assert to_nice_yaml(1) == "1\n"
    assert to_nice_yaml(dict(a=1,b=2)) == "a: 1\nb: 2\n"
    assert to_nice_yaml(["a",1,2]) == "- a\n- 1\n- 2\n"
    assert to_nice_yaml([u"a",1,2]) == "- a\n- 1\n- 2\n"
    assert to_nice_yaml(u"a") == "a\n"


# Generated at 2022-06-22 11:42:07.090254
# Unit test for function mandatory
def test_mandatory():
    from ansible.template import Jinja2Template
    from jinja2.runtime import Undefined

    foo_val = 'bar'
    msg = 'Custom message'
    j2_env = Jinja2Template('.').environment
    j2_env.filters['mandatory'] = mandatory
    j2_undefined = Undefined(j2_env)
    assert mandatory(foo_val) == foo_val
    try:
        mandatory(j2_undefined)
    except AnsibleFilterError as e:
        assert to_text(e) == "Mandatory variable not defined."

    try:
        mandatory(j2_undefined, msg)
    except AnsibleFilterError as e:
        assert to_text(e) == msg



# Generated at 2022-06-22 11:42:16.881273
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1) == 1
    assert mandatory(None) == None
    #assert False



# Generated at 2022-06-22 11:42:21.682837
# Unit test for function regex_search
def test_regex_search():
    '''Test function regex_search'''
    assert regex_search('foo', 'o') == 'o'
    assert regex_search('foo', 'o', '\\1') == ['o', 'o']
    assert regex_search('foo', 'o', '\\g<1>') == ['o']



# Generated at 2022-06-22 11:42:31.346362
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(value='abc 123', pattern='(\d+)', replacement='456') == 'abc 456'
    assert regex_replace(value='abc 123', pattern='(\d+)', replacement='456', multiline=True) == 'abc 456'
    assert regex_replace(value='abc 123', pattern='(\d+)', replacement='456', ignorecase=True) == 'abc 456'
    assert regex_replace(value='ABC 123', pattern='(\d+)', replacement='456') == 'ABC 123'
    assert regex_replace(value='ABC 123', pattern='(\d+)', replacement='456', ignorecase=True) == 'ABC 456'


# Generated at 2022-06-22 11:42:37.637631
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abcd\nefgh', r'cd\\nefg\\n', '\\g<1>', '\\1') == ['cd\n', '1']
    assert regex_search('abcd\nefgh', r'cd\\nefg\\n', '\\g<1>', '\\2') == ['cd\n', None]



# Generated at 2022-06-22 11:42:40.223783
# Unit test for function ternary
def test_ternary():
    return ternary(None, 'bad', 'good') != 'good'


# Generated at 2022-06-22 11:42:46.804674
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abc123', r'\d+') == '123'
    assert regex_search('abc123', r'\d+', '\\g<0>') == ['123', '123']
    assert regex_search('abc123', r'\d+', '\\0') == '123'
    assert regex_search('abc123', r'\d+', '\\1') == ''



# Generated at 2022-06-22 11:42:55.548137
# Unit test for function mandatory
def test_mandatory():
    # fact should not fail
    a = AnsibleUndefined('foo')
    assert mandatory(a) is a

    # fact should fail with provided msg
    a = AnsibleUndefined('bar')
    with pytest.raises(AnsibleFilterError) as exc:
        mandatory(a, "BAR is not defined!")
    assert str(exc.value) == "BAR is not defined!"

    # fact should fail with default msg
    a = AnsibleUndefined('foo')
    with pytest.raises(AnsibleFilterError) as exc:
        mandatory(a)
    assert str(exc.value) == "Mandatory variable 'foo' not defined."



# Generated at 2022-06-22 11:43:06.803919
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo', '^f') == 'f'
    assert regex_search('foo', 'o', ignorecase=True) == 'o'
    assert regex_search('foo', 'o', multiline=True) == 'o'
    assert regex_search('foo', 'o', ignorecase=True, multiline=True) == 'o'
    assert regex_search('foobar', '^foo(.*)$', '\\g<1>') == ['bar']
    assert regex_search('foobar', '^foo(.*)$', '\\g<1>', '\\g<1>') == ['bar', 'bar']
    assert regex_search('foobar', '^foo(.*)$', '\\g<1>', '\\1') == ['bar', 'bar']

# Generated at 2022-06-22 11:43:09.972248
# Unit test for function fileglob
def test_fileglob():
    ret = fileglob("/var/log/messages*")
    assert ret == ['/var/log/messages']



# Generated at 2022-06-22 11:43:11.302234
# Unit test for function mandatory
def test_mandatory():
    raise AssertionError("mandatory filter test should not be called")


# Generated at 2022-06-22 11:43:29.889169
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    import collections
    test_dict = {'foo': 'bar', 'fie': 'baz'}
    test_ntuple = collections.namedtuple('test_ntuple', test_dict.keys())
    test_ntuple_inst = test_ntuple(**test_dict)
    test_data = [test_ntuple_inst, test_ntuple_inst]

    env = jinja2.Environment()
    env.filters['groupby'] = do_groupby

    template = env.from_string("""
        {% for key,val in data|groupby('foo') %}
            {{ key }}
        {% endfor %}
    """)

    assert template.render(data=test_data) == 'bar'



# Generated at 2022-06-22 11:43:40.777477
# Unit test for function do_groupby
def test_do_groupby():
    # for testing we will use a jinja2 template sandbox
    from jinja2.sandbox import SandboxedEnvironment
    from ansible.template.safe_eval import ansible_safe_eval
    env = SandboxedEnvironment()
    # create a mock structure to be processed by the groupby
    mock_struct = [{'price': 1, 'name': 'A'}, {'price': 2, 'name': 'B'},
                   {'price': 1, 'name': 'C'}, {'price': 2, 'name': 'D'}]
    # first, test what happens when we don't override the groupby function
    # jinja2>=2.9.0,<2.9.5 will return a namedtuple

# Generated at 2022-06-22 11:43:43.103075
# Unit test for function ternary
def test_ternary():
    assert ternary(True, 1, 2) == 1
    assert ternary(False, 1, 2) == 2
    assert ternary(None, 1, 2, 3) == 3



# Generated at 2022-06-22 11:43:48.901901
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('this_file_does_not_exist') == []
    assert fileglob('this_file_*_not_exist') == []
    assert fileglob('test/utils/filter_plugins/test_fileglob.py') == ['test/utils/filter_plugins/test_fileglob.py']



# Generated at 2022-06-22 11:43:58.860530
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment

    items = [
        {'name': 'alice', 'gender': 'female'},
        {'name': 'bob', 'gender': 'male'},
        {'name': 'carol', 'gender': 'female'},
        {'name': 'dave', 'gender': 'male'},
        {'name': 'eve', 'gender': 'female'},
    ]
    # We need to initialize a template environment so that the `groupby`
    # filter works correctly
    env = Environment()
    # Ensure that our new jinja2 filter works correctly.

# Generated at 2022-06-22 11:44:06.711450
# Unit test for function regex_search
def test_regex_search():
    test_str = '''
    label: master
    host: 192.168.1.10
    port: 8080
    '''

    regex = r"label: (\w+)"
    search_result = regex_search(test_str, regex)
    assert search_result == 'master'

    regex = r"label: (\w+)"
    groups_result = regex_search(test_str, regex, '\\g<1>')
    assert groups_result == 'master'

    regex = r"label: (\w+)"
    group_digits_result = regex_search(test_str, regex, '\\1')
    assert group_digits_result == 'master'

    regex = r"label: (\w+)"

# Generated at 2022-06-22 11:44:07.892780
# Unit test for function fileglob
def test_fileglob():
    ''' test_fileglob: values returns list of matched files'''
    assert fileglob('*') == glob.glob('*')



# Generated at 2022-06-22 11:44:15.511863
# Unit test for function do_groupby
def test_do_groupby():
    env = Environment()
    env.loader = DictLoader({'template': '{{ lookup('
                             '"sequence", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], '
                             'true) | groupby("even") }}'})
    template = env.get_template('template')
    result = template.render()
    assert result == "[('true', [2, 4, 6, 8, 10]), ('false', [1, 3, 5, 7, 9])]", \
        "groupby does not work correctly"



# Generated at 2022-06-22 11:44:21.174166
# Unit test for function ternary
def test_ternary():
    assert ternary(True, "this is true", "this is false") == "this is true"
    assert ternary(False, "this is true", "this is false") == "this is false"
    assert ternary(None, "this is true", "this is false", "this is None") == "this is None"


# Generated at 2022-06-22 11:44:31.357306
# Unit test for function regex_replace
def test_regex_replace():

    # Basic use case
    assert(regex_replace(value='', replacement='bar') == '')
    assert(regex_replace(value='foo', replacement='bar') == 'bar')

    # Multiline default
    assert(regex_replace(value='foo', replacement='bar', pattern='foo') == 'bar')
    assert(regex_replace(value='foo\nfoo', replacement='bar', pattern='foo') == 'bar\nbar')

    # Singleline default
    assert(regex_replace(value='foo', replacement='bar', pattern='foo', multiline=False) == 'bar')
    assert(regex_replace(value='foo\nfoo', replacement='bar', pattern='foo', multiline=False) == 'bar\nfoo')

    # Matches

# Generated at 2022-06-22 11:44:39.750437
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'test': {'test_test': 'test'}}) == '{\n    test: {\n        test_test: test\n    }\n}'


# Generated at 2022-06-22 11:44:47.860274
# Unit test for function mandatory
def test_mandatory():
    ''' mandatory should raise an exception if it receives an Undefined.
    '''
    from jinja2.runtime import Undefined

    def _test_result(a):
        return mandatory(a)

    def _test_exception(a, e=AnsibleFilterError):
        try:
            _test_result(a)
        except e:
            return True
        return False

    assert _test_exception(Undefined())
    assert _test_exception(Undefined(name='Foo'))
    assert _test_exception(1)



# Generated at 2022-06-22 11:44:53.736344
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(pattern='a', replacement='b', value='aaa') == 'bbb'
    assert regex_replace(pattern='a', replacement='b', value='aaa', ignorecase=True) == 'bbb'
    assert regex_replace(pattern='A', replacement='b', value='aaa') == 'aaa'
    assert regex_replace(pattern='A', replacement='b', value='aaa', ignorecase=True) == 'bbb'



# Generated at 2022-06-22 11:45:00.674751
# Unit test for function randomize_list
def test_randomize_list():
    mylist = ['foo', 'bar', 'baz', 'qux', 'quux']
    assert mylist.sort() == None
    assert mylist == ['bar', 'baz', 'foo', 'quux', 'qux']
    assert randomize_list(mylist).sort() == None
    assert randomize_list(mylist, seed="password").sort() == None
    assert randomize_list(mylist, seed=12345).sort() == None



# Generated at 2022-06-22 11:45:11.889001
# Unit test for function regex_replace
def test_regex_replace():
    # Normal use
    assert regex_replace('123', '(2)', 'X') == '1X3'

    # Ensure the repl string is interpreted correctly
    assert regex_replace('123', '(2)', r'\g<1>X') == '12X3'

    # Test the ignorecase flag
    assert regex_replace('ABC', '[A-Z]', 'X', ignorecase=True) == 'XXX'

    # Test the multiline flag
    assert regex_replace('1\n2', '\n', 'X', multiline=True) == '1X2'

    # Test the errors option to ensure it propagates

# Generated at 2022-06-22 11:45:18.376280
# Unit test for function fileglob
def test_fileglob():
    assert fileglob("/tmp/xyzzy") == []
    assert fileglob("/etc/*-release") == ["/etc/os-release", "/etc/lsb-release"]
    assert fileglob("/dev") == []
    assert fileglob("/dev/tty[0-9]*") == ["/dev/tty12"]
    assert fileglob("/dev/tty??") == ["/dev/tty12"]



# Generated at 2022-06-22 11:45:20.117238
# Unit test for function strftime
def test_strftime():
    assert strftime('%H:%M', 1386393472) == '09:01'



# Generated at 2022-06-22 11:45:30.313797
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(u'Foo123', u'123', u'456') == u'Foo456'
    assert regex_replace(u'Foo123', u'123', u'456', True, False) == u'Foo456'
    assert regex_replace(u'Foo123', u'123', u'456', True, True) == u'Foo456'
    assert regex_replace(u'Foo123', u'123', u'456', False, True) == u'Foo123'
    assert regex_replace(u'Foo123', u'123', u'456', False, False) == u'Foo456'



# Generated at 2022-06-22 11:45:40.707743
# Unit test for function regex_search
def test_regex_search():
    value = "http://www.cisco.com"
    expect = "http"

    result = regex_search(value, r'http')

    assert result == expect

    value = "http://www.cisco.com"
    expect = "www.cisco.com"

    result = regex_search(value, r'http://\g<core>')

    assert result == expect

    value = "(http)://www.cisco.com"
    expect = "http"

    result = regex_search(value, r'\g<1>')

    assert result == expect

    value = "(http)://www.cisco.com"
    expect = "http"

    result = regex_search(value, r'\(http\)\g<1>')

    assert result == expect


# Generated at 2022-06-22 11:45:50.462043
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import template
    from ansible.plugins.filter import core
    import collections


# Generated at 2022-06-22 11:46:03.790218
# Unit test for function to_yaml
def test_to_yaml():
    data = {'red': [1, 100, 200], 'green': [1, 150, 200], 'blue': [1, 50, 100]}
    output = '[{"blue": [1, 50, 100], "green": [1, 150, 200], "red": [1, 100, 200]}]'
    yaml_data = to_yaml(data)
    json_data = json.dumps(json.loads(output), indent=4)
    assert yaml_data == json_data


# Generated at 2022-06-22 11:46:12.088015
# Unit test for function mandatory
def test_mandatory():
    for arg in [[], ['foo'], ['foo', 'bar']]:
        try:
            from jinja2.runtime import Undefined
            from ansible.template import Templar
            t = Templar(loader=None, variables={})
            t._fail_lookup = True
            mandatory(Undefined(*arg))
        except AnsibleFilterError as e:
            assert "Mandatory variable" in to_native(e)
        else:
            assert False, "Expected AnsibleFilterError"
test_mandatory()



# Generated at 2022-06-22 11:46:23.972583
# Unit test for function regex_search
def test_regex_search():
    import unittest
    class TestAnsibleModule(unittest.TestCase):
        def test_regex_search(self):
            value = 'hostname'
            regex = 'hostname'
            self.assertEqual(regex_search(value, regex), 'hostname')

            regex = '(hostname)'
            self.assertEqual(regex_search(value, regex, '\\g<1>'), 'hostname')

            regex = '^(.+)name$'
            self.assertEqual(regex_search(value, regex, '\\1'), 'host')

            regex = '(host).+(name)'
            self.assertEqual(regex_search(value, regex, '\\1', '\\2'), ['host', 'name'])

    unittest.main()



# Generated at 2022-06-22 11:46:37.146167
# Unit test for function mandatory
def test_mandatory():
    ''' just to make sure the code above is functionally identical to the code removed '''
    try:
        mandatory('foo')
        raise AnsibleError() # should not get here
    except AnsibleFilterError:
        pass
    try:
        mandatory('foo', msg='blah')
        raise AnsibleError() # should not get here
    except AnsibleFilterError as e:
        assert(to_text(e) == 'blah')
    try:
        mandatory(AnsibleUndefined)
        raise AnsibleError() # should not get here
    except AnsibleFilterError as e:
        assert(to_text(e) == "Mandatory variable not defined.")


# Generated at 2022-06-22 11:46:45.197957
# Unit test for function extract
def test_extract():
    from jinja2 import StrictUndefined
    env = Environment(undefined=StrictUndefined)
    assert extract(env, 'x', {'x': 0}) == 0
    assert extract(env, 'x', {'x': 0, 'y': 1}) == 0
    assert extract(env, 'x', {'x': {'y': 0}}) == {'y': 0}
    assert extract(env, 'x', {'x': {'y': {'z': 0}}}) == {'y': {'z': 0}}
    assert extract(env, 'x', {'x': {'y': {'z': 0}}}, 'y') == {'z': 0}
    assert extract(env, 'x', {'x': {'y': {'z': 0}}}, 'y', 'z') == 0


# Generated at 2022-06-22 11:46:56.952126
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment

    env = Environment()
    env.filters['groupby'] = do_groupby
    template = env.from_string("{{ [{'a': 1, 'b': 'x'},{'a': 2, 'b': 'y'},{'a': 3, 'b': 'z'}] | groupby('b') }}")
    # do this to get the precise repr of the namedtuple, as the unit tests
    # on Precise64 return a different repr than most others
    def _namedtuple(typename, field_names, **kwargs):
        return tuple.__new__(namedtuple(typename, field_names)(**kwargs))
    template.globals['namedtuple'] = _namedtuple
    result = template.render({})

# Generated at 2022-06-22 11:47:01.922809
# Unit test for function regex_search
def test_regex_search():
    value = "https://www.ansible.com/ansible-mulit-cloud"
    regex = r'http.*com.*/(\w+)'
    assert regex_search(value, regex, '\\1') == 'ansible-mulit-cloud'



# Generated at 2022-06-22 11:47:13.981163
# Unit test for function regex_search
def test_regex_search():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.tests.unit.compat import unittest

    class TestRegexSearch(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.regex_search = basic._get_exported_symbols()['ansible.module_utils.basic.regex_search']

        def test_match_group_and_backref(self):
            # First match group + backref test
            regex = r'^(\d+)(\w)=(\d+)(\w)$'
            value = '123x=456y'

# Generated at 2022-06-22 11:47:26.325160
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'') == r''
    assert regex_escape(r'*') == r'\*'
    assert regex_escape(r'*', re_type='posix_basic') == r'\*'
    assert regex_escape(r'>') == r'\>'
    assert regex_escape(r'>', re_type='posix_basic') == r'\>'
    assert regex_escape(r'<') == r'\<'
    assert regex_escape(r'<', re_type='posix_basic') == r'\<'
    assert regex_escape(r'+') == r'\+'
    assert regex_escape(r'+', re_type='posix_basic') == r'\+'
    assert regex_escape(r'?') == r'\?'

# Generated at 2022-06-22 11:47:36.945110
# Unit test for function regex_search
def test_regex_search():

    assert "nginx" == regex_search("foo nginx bar", r"nginx")
    assert ["nginx"] == regex_search("foo nginx bar", r"nginx", '\\g<0>')
    assert ("nginx", "1") == regex_search("foo nginx bar > 1", r"(nginx).*>(\d+)", '\\g<1>', '\\2')
    assert "nginx" == regex_search("foo nginx bar 1", r".*(nginx)", '\\1')

    # regex_search patterns that would fail in regex_findall
    assert "nginx" == regex_search("foo nginx bar", r"n\S+")
    assert ["nginx"] == regex_search("foo nginx bar", r"n\S+", '\\g<0>')

# Generated at 2022-06-22 11:47:44.821561
# Unit test for function extract
def test_extract():
    env = DummyEnvironment([], None)
    result = extract(env, 'f', {'a': {'b': {'c': {'d': 'e', 'f': {'g': 'h'}}}}})
    assert result == {'g': 'h'}



# Generated at 2022-06-22 11:47:49.664431
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list([1, 2, 3, 4, 5, 6], seed=0) == [4, 1, 5, 2, 6, 3]
    assert randomize_list([1, 2, 3, 4, 5, 6], seed=26) == [4, 3, 6, 5, 2, 1]



# Generated at 2022-06-22 11:47:58.901730
# Unit test for function do_groupby
def test_do_groupby():
    jinja_env = Environment()
    jinja_env.filters['groupby'] = do_groupby

    tf = tempfile.NamedTemporaryFile()
    tf.write(b"foo\nbar\nfoo\nbar\n")
    tf.flush()

    template = Template('{% set foo = ["%s"] | map("extract", "0") | list | groupby("length") | list %}'
                        '{% if foo is defined %}'
                        'foo is defined'
                        '{% endif %}',
                        jinja_env)
    res = template.render(foo=tf.name)
    assert res == "foo is defined"



# Generated at 2022-06-22 11:48:02.967217
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({'just': 'some', 'sample': 'data'}, default_flow_style=False) == '''\
just: some
sample: data
'''



# Generated at 2022-06-22 11:48:13.831334
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(value='foo', regex='.') == 'f'
    assert regex_search(value='foo', regex='.', ignorecase=True) == 'f'
    assert regex_search(value='foo', regex='.', multiline=True) == 'f'
    assert regex_search(value='foo', regex='.', multiline=True, ignorecase=True) == 'f'
    assert regex_search(value='foo', regex='.', ignorecase=True, multiline=True) == 'f'

# Generated at 2022-06-22 11:48:18.931235
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('ansible', r'ans(.*)') == 'ible'
    assert regex_search('ansible', r'ans(.*)', '\\g<1>') == 'ible'
    assert regex_search('ansible', r'ans(.*)', '\\1') == 'ible'
    assert regex_search('ansible', r'ans(.*)', '\\g<1>', '\\1') == ['ible', 'ible']



# Generated at 2022-06-22 11:48:31.835545
# Unit test for function get_hash
def test_get_hash():
    assert(get_hash('get_hash') == 'dae110a7e935fdc8bb105be6c751f6fea710f81a')
    assert(get_hash('get_hash', 'sha224') == 'a33cbf0b6ae7b4f4c838ee69d4c809188723ff6e9b6f0e4c4a4f4d4')
    assert(get_hash('get_hash', 'md5') == 'bc6e6f16b8a077ef5fbc8d59d0bad9ea')

# Generated at 2022-06-22 11:48:37.845577
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('hello') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    assert get_hash('hi', 'md5') == '49f68a5c8493ec2c0bf489821c21fc3b'



# Generated at 2022-06-22 11:48:41.647248
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('test*string') == 'test\\*string'
    assert regex_escape('test[string') == 'test\\[string'
    assert regex_escape('test.string') == 'test\\.string'
    assert regex_escape('test^string') == 'test\\^string'
    assert regex_escape('test$string') == 'test\\$string'
    assert regex_escape('test\\string') == 'test\\\\string'
    assert regex_escape('(test)string') == '\\(test\\)string'
    assert regex_escape('test?string') == 'test\\?string'
    assert regex_escape('test|string') == 'test\\|string'
    assert regex_escape('test*string', re_type='posix_basic') == 'test\\*string'

# Generated at 2022-06-22 11:48:53.456304
# Unit test for function comment
def test_comment():
    class TestCase(object):
        def assertEqual(self, a, b):
            if a != b:
                raise AssertionError('%s != %s' % (repr(a), repr(b)))
    t = TestCase()

    t.assertEqual(
        comment(text='This is a text to comment', decoration=';'),
        '; This is a text to comment')

    t.assertEqual(
        comment('This is a text to comment', decoration=';'),
        '; This is a text to comment')

    t.assertEqual(
        comment(
            text='This is a text to comment',
            style='cblock',
            decoration=' -',
            beginning='/*'
        ),
        '/*\n * - This is a text to comment\n */')

    t.assertEqual

# Generated at 2022-06-22 11:49:04.721066
# Unit test for function mandatory
def test_mandatory():
    from ansible.template import Templar
    current = dict(a=42, b=43)

    t = Templar(loader=None, variables=current)
    assert 42 == t.template('{{ a }}')
    assert '' == t.template('{{ c }}')
    with pytest.raises(AnsibleFilterError) as e:
        t.template('{{ c|mandatory }}')
    assert 'Mandatory variable \'c\' not defined.' == e.value.__str__()



# Generated at 2022-06-22 11:49:10.891947
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml(dict(a="b")) == to_text("{a: b}\n")
    assert to_yaml(list(range(10))) == to_text("- 0\n- 1\n- 2\n- 3\n- 4\n- 5\n- 6\n- 7\n- 8\n- 9\n")



# Generated at 2022-06-22 11:49:22.600342
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from jinja2 import DictLoader
    from jinja2.environment import Environment

    simple_template = """
        {% set data = {
          'a': [1, 2, 3],
          'b': [4, 5, 6],
        } %}
        {{ data | do_groupby("key") }}
    """
    env = Environment(loader=DictLoader({'test_do_groupby.j2': simple_template}))
    template = env.get_template('test_do_groupby.j2')
    result = template.render()

    assert result == '{u\'a\': [1, 2, 3], u\'b\': [4, 5, 6]}'


# Generated at 2022-06-22 11:49:34.048792
# Unit test for function randomize_list
def test_randomize_list():
    assert ''.join(randomize_list('foo')) == 'foo'
    assert ''.join(randomize_list('foo', 'bar')) == 'ba'
    assert ''.join(randomize_list('foo', 'bar', 'baz')) == 'baz'
    assert ''.join(randomize_list('foo', 'bar', 'baz', 'qux')) == 'bx'
    assert ''.join(randomize_list('foo', 'bar', 'baz', 'qux', 'foobar')) == 'bxof'

# Generated at 2022-06-22 11:49:40.700522
# Unit test for function get_hash
def test_get_hash():
    data = {1: 2}
    hashtype = 'sha256'
    h = get_hash(data, hashtype)
    assert h == '3b424f8fa2c06a6abf734ddc7f818a1a1fa73f37c099c8b8d08e192c7cbf73ae'


# Generated at 2022-06-22 11:49:46.767592
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    string = to_nice_yaml({'a': 1, 'b': 2, 'c': 3})
    assert u'\n'.join([u'a: 1', u'b: 2', u'c: 3']) == string, 'to_nice_yaml failed on dictionary'

    string = to_nice_yaml([{'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}])
    assert u'\n'.join([u'-', u'    a: 1', u'    b: 2', u'    c: 3', u'-', u'    a: 1', u'    b: 2', u'    c: 3']) == string, 'to_nice_yaml failed on list of dictionaries'


# Generated at 2022-06-22 11:49:50.979013
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("1:2:3:4","2","\\2") == "2"
    assert regex_search("abcabcabcabcabc","abcabcabcabcabc","\\g<key1>","key1") == "abcabcabcabcabc"



# Generated at 2022-06-22 11:50:01.914727
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Template
    from collections import namedtuple
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vars import merge_hash

    # We want to use the actual `do_groupby` from jinja2
    do_groupby = Template("{{ [{'a':'b', 'c':'d'}, {'a':'e', 'c':'f'}] | groupby('a') }}").module.do_groupby

    # We want to use the actual `do_groupby` from jinja2

# Generated at 2022-06-22 11:50:04.936948
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo.bar') == 'foo\\.bar'
    assert regex_escape('foo.bar', re_type='posix_basic') == 'foo\\.bar'
    assert regex_escape('foo.bar', re_type='posix_extended') == 'foo\\.bar'

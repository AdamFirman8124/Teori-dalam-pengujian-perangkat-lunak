

# Generated at 2022-06-22 11:40:39.721859
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/no/such/file') == []
    assert fileglob('*') == fileglob('*.py')
    assert all(fileglob('./*.py'))



# Generated at 2022-06-22 11:40:50.247298
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    from ansible.vars.unsafe_proxy import UnsafeProxy

    # Test with a variable defined
    class TestObj(object):
        pass

    test_obj = TestObj()
    test_obj.a = 10
    test_obj.var = 5
    test_obj2 = TestObj()
    test_obj2.var = UnsafeProxy(test_obj, 'var')
    test_obj.undefined_obj = test_obj2
    atr = partial(mandatory, msg="Error message")
    assert atr(test_obj.a) == 10
    # Test with the special case of a `list`
    # The `list` class does not have an `__getattr__` method, so we try to
    # access an attribute that does not exist to make sure that

# Generated at 2022-06-22 11:41:02.659300
# Unit test for function comment
def test_comment():
    import re


# Generated at 2022-06-22 11:41:10.138596
# Unit test for function comment
def test_comment():
    def test_case(comment_string,
                  text='',
                  style='cblock',
                  beginning='',
                  prefix='///',
                  prefix_count=1,
                  decoration=' * ',
                  postfix='///',
                  postfix_count=1,
                  end='',
                  newline='\n'):
        # "Run" the test
        _comment = comment(
            text=text,
            style=style,
            beginning=beginning,
            prefix=prefix,
            prefix_count=prefix_count,
            decoration=decoration,
            postfix=postfix,
            postfix_count=postfix_count,
            end=end,
            newline=newline)
        # Check the result

# Generated at 2022-06-22 11:41:21.463251
# Unit test for function do_groupby
def test_do_groupby():
    # The regular jinja2 groupby works fine with this dataset
    jinja2_groupby([{'foo': 'a', 'bar': 47}, {'foo': 'a', 'bar': 42}], 'foo')

    # However, when we try to convert that to a safe dict, we get an error
    # about AttributeError: 'tuple' object has no attribute 'bar'
    # We can avoid this error, by using the safe_groupby function
    from ansible.template.safe_eval import safe_dict
    safe_dict({'result': jinja2_groupby([{'foo': 'a', 'bar': 47}, {'foo': 'a', 'bar': 42}], 'foo')})

# Generated at 2022-06-22 11:41:31.458300
# Unit test for function subelements
def test_subelements():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-22 11:41:34.625071
# Unit test for function mandatory
def test_mandatory():
    assert mandatory("Hello, World") == "Hello, World"

    try:
        mandatory("Hello, World", "This is a custom error")
    except AnsibleFilterError as e:
        assert e.message == "This is a custom error"
    except:
        raise AssertionError("AnsibleFilterError exception not raised")

    try:
        mandatory("This is a custom error")
    except AnsibleFilterError as e:
        assert e.message == "Mandatory variable not defined."
    except:
        raise AssertionError("AnsibleFilterError exception not raised")



# Generated at 2022-06-22 11:41:44.015478
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abc', r'abc') == 'abc'
    assert regex_search('abc', r'a(bc)') == ['bc']
    assert regex_search('abc', r'a(bc)', '\\g<1>') == ['bc']
    assert regex_search('abc', r'a(b)c', '\\g<1>') == ['b']
    assert regex_search('abc', r'a(b)c', '\\1') == ['b']



# Generated at 2022-06-22 11:41:53.518336
# Unit test for function randomize_list
def test_randomize_list():
    mylist = ['apple', 'banana', 'cherry', 'durian', 'eggplant']
    the_same_list = ['apple', 'banana', 'cherry', 'durian', 'eggplant']
    seed_123 = 123
    seed_321 = 321

    # Test for unorder and empty list
    list_unorder = ['banana', 'eggplant', 'apple', 'cherry', 'durian']
    list_empty = []
    randomize_list(list_unorder)
    randomize_list(list_empty)
    assert mylist == list_unorder
    assert list_empty == list_empty

    # Test for the same seed
    list_unorder_seed_123 = randomize_list(mylist, seed_123)

# Generated at 2022-06-22 11:41:56.063152
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    fm = FilterModule()
    print(fm.filters())

# Generated at 2022-06-22 11:42:11.827459
# Unit test for function do_groupby
def test_do_groupby():
    environment = DummyEnvironment()
    do_groupby(environment, [{'name': 'a', 'value': 1},
                             {'name': 'b', 'value': 2},
                             {'name': 'a', 'value': 3}], 'name') == \
        [('a', [{'name': 'a', 'value': 1}, {'name': 'a', 'value': 3}]),
         ('b', [{'name': 'b', 'value': 2}])]



# Generated at 2022-06-22 11:42:18.063252
# Unit test for function comment
def test_comment():
    assert comment(
        'Comment text',
        style='plain') == '# Comment text'
    assert comment(
        'Comment text\nSecond line',
        style='plain') == '# Comment text\n# Second line'
    assert comment(
        'Comment text\nSecond line',
        style='xml',
        decoration=' < ') == '<!-- < Comment text\n < Second line -->'



# Generated at 2022-06-22 11:42:26.484426
# Unit test for function fileglob
def test_fileglob():
    files = ["test1.txt", "test2.txt", "test1.tmp", "test2.tmp"]

    for f in files:
        open(f, 'a').close()

    assert fileglob("test1.*") == ["test1.txt"]
    assert fileglob("test*.txt") == ["test1.txt", "test2.txt"]
    assert fileglob("test*.tmp") == ["test1.tmp", "test2.tmp"]
    assert fileglob("test*.jpg") == []

    for f in files:
        os.remove(f)



# Generated at 2022-06-22 11:42:29.876510
# Unit test for function get_hash
def test_get_hash():
    assert get_hash("Ansible") == "ce7a1fdb1e9c7bdb0fbaef94d0c46aebb50c091b"



# Generated at 2022-06-22 11:42:41.775795
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import DictLoader, Environment
    from operator import attrgetter, itemgetter
    from itertools import groupby

    env = Environment(loader=DictLoader({'tmpl': '''
            {%- for group in values|groupby('f1') -%}
              [{{ group.grouper }}]
              {%- for item in group.list -%}
                {{ item.f0 }}|{{ item.f1 }}
              {%- endfor -%}
            {%- endfor -%}
        '''}))

    values = [MyTestClass(0, 0), MyTestClass(1, 0), MyTestClass(2, 1)]
    tmpl = env.get_template('tmpl')

    # Check default result

# Generated at 2022-06-22 11:42:45.976003
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape('foo') == r'foo'
    assert regex_escape('foo.*') == r'foo\..*'
    assert regex_escape('foo.*', re_type='posix_basic') == r'foo[.]\*'



# Generated at 2022-06-22 11:42:56.238245
# Unit test for function comment
def test_comment():
    assert comment('text') == '# text'
    assert comment('text', style='xml') == '<!-- text -->'
    assert comment('text', style='cblock') == '/* text */'
    assert comment('text', decoration=' ') == '# text'
    assert comment('text', decoration=' ' *
                   2, style='erlang') == '%  text'
    assert comment('text', prefix='% ') == '% text'
    assert comment('text', decoration=' ', prefix='% ') == '% text'
    assert comment('text', decoration=' ',
                   prefix='% ', postfix='%') == '% text %'
    assert comment('text', newline='\r\n') == '# text'
    assert comment('text', postfix_count=2) == '# text\n#'
    assert comment

# Generated at 2022-06-22 11:43:04.774835
# Unit test for function strftime
def test_strftime():
    assert strftime("%Y-%m-%d %H:%M:%S", "1392376368.12345") == "2014-02-18 15:59:28"
    assert strftime("%Y-%m-%d %H:%M:%S", "1392376368") == "2014-02-18 15:59:28"
    assert strftime("%Y-%m-%d %H:%M:%S", "1392376368.000") == "2014-02-18 15:59:28"
    assert strftime("%Y-%m-%d %H:%M:%S", 1392376368.12345) == "2014-02-18 15:59:28"

# Generated at 2022-06-22 11:43:09.138396
# Unit test for function mandatory
def test_mandatory():
    assert mandatory("hello", "msg") == "hello"

    try:
        mandatory("hello")
    except AnsibleFilterError:
        pass
    else:
        assert False, "succeed when variable is not defined"



# Generated at 2022-06-22 11:43:20.965101
# Unit test for function fileglob
def test_fileglob():
    fn_fileglob = sys.modules[__name__].fileglob
    pathname = '{{ test_dir }}/files/file*'

# Generated at 2022-06-22 11:43:36.972492
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('username', 'name') == 'name'
    assert regex_search('username', 'name', '\\g<0>') == 'name'
    assert regex_search('username', 'name', '\\g<0>', '\\g<0>') == ['name', 'name']
    assert regex_search('username', 'name', '\\0', '\\0') == ['name', 'name']
    assert regex_search('username', 'name', '\\g<0>', '\\1') == ['name', 'name']
    assert regex_search('username', 'name', '\\0', '\\1') == ['name', 'name']
    assert regex_search('username', 'name', '\\g<1>') == None
    assert regex_search('username', 'name', '\\1') == None
    assert regex_

# Generated at 2022-06-22 11:43:40.546894
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    assert mandatory(None, msg='error msg') == None
    assert mandatory('b') == 'b'
    assert mandatory(Undefined('foo'), msg='error msg') == 'error msg'



# Generated at 2022-06-22 11:43:44.347409
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/*') == ['/etc/ansible', '/etc/hosts']
    assert fileglob('/bin/*') == ['/bin/ls', '/bin/ps']



# Generated at 2022-06-22 11:43:56.462135
# Unit test for function subelements
def test_subelements():
    from collections import Mapping

    obj = [
        {"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]},
        {"name": "bob", "groups": ["dev", "test"], "authorized": ["/tmp/bob/onekey.pub", "/tmp/bob/otherkey.pub"]},
    ]
    result = [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]
    assert subelements(obj, 'groups') == result, 'subelements did not return the correct result'

    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]

# Generated at 2022-06-22 11:44:05.796348
# Unit test for function regex_search
def test_regex_search():
    ''' Unit test for function regex_search '''
    data = '''
---
- name: Host 1
  ip: 192.168.1.1
  l4_proto: TPC
- name: Host 2
  ip: 192.168.1.2
  l4_proto: TCP
- name: Host 3
  ip: 192.168.1.3
  l4_proto: UDP
- name: Host 4
  ip: 192.168.1.4
  l4_proto: ICMP
  '''

    for host in yaml.load(data):
        assert regex_search(host['l4_proto'], '(?P<proto>TCP|UDP|ICMP)', '\\g<proto>') == host['l4_proto']

# Generated at 2022-06-22 11:44:16.772022
# Unit test for function do_groupby
def test_do_groupby():

    # Create a list of named tuples we'll use as a template
    nt_tpl = namedtuple('TestTuple', 'a b')

    # Create a list of named tuples we'll use as a template
    nt_tpl1 = namedtuple('TestTuple1', 'c d')

    # Create a list of named tuples we'll use as a template
    nt_tpl2 = namedtuple('TestTuple2', 'd e')


# Generated at 2022-06-22 11:44:24.771603
# Unit test for function mandatory
def test_mandatory():
    data = {'var': 10}

    assert(mandatory(data['var']) == 10)
    assert(mandatory(data['var'], "Custom message") == 10)
    try:
        assert(mandatory(data['Var']) == 10)
    except Exception as e:
        assert(isinstance(e, AnsibleFilterError))

    try:
        assert(mandatory(data['Var'], "Custom message") == 10)
    except Exception as e:
        assert(isinstance(e, AnsibleFilterError))


# Generated at 2022-06-22 11:44:33.442170
# Unit test for function comment
def test_comment():
    assert(comment("") == '# \n')
    assert(comment("", newline='x') == '# x')
    assert(comment("", decoration='; ') == '; \n')
    assert(comment("", decoration='', newline='x') == '#x')
    assert(comment("", decoration='') == '#\n')
    assert(comment("", beginning='/*', end='*/') == '/*\n# \n*/')
    assert(comment("", beginning='/*', end='*/', decoration='*') == '/*\n* \n*/')
    assert(comment("", beginning='/*', end='*/', decoration='* ') == '/*\n* \n*/')
    assert(comment("", beginning='/*', end='*/', decoration='') == '/*\n#\n*/')
   

# Generated at 2022-06-22 11:44:45.542155
# Unit test for function subelements
def test_subelements():
    # Test using a single dict
    element = {"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}
    result = subelements(element, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')], result

    # Test using a list of dicts
    elements = [
        {"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]},
        {"name": "bob", "groups": ["root", "users"], "authorized": ["/tmp/bob/onekey.pub", "/tmp/bob/twokey.pub"]}
        ]

# Generated at 2022-06-22 11:44:57.655109
# Unit test for function comment
def test_comment():
    # Simple one-line test
    assert comment('one line test') == '# one line test'
    # Two lines test
    assert (comment('two\nlines test') == '# two\n# lines test')
    assert (comment('two\nlines test', decoration='### ') ==
            '### two\n### lines test')
    # Change the decorator
    assert comment('one line', decoration='-- ') == '-- one line'
    # Add a newline
    assert (comment('last line', prefix='', postfix='\n') ==
            'one line\n# \n')
    # Default decorator
    assert comment('one line', style='plain') == '# one line'
    # C-style comment
    assert comment('one line', style='c') == '// one line'
    # XML-style comment

# Generated at 2022-06-22 11:45:13.003484
# Unit test for function mandatory
def test_mandatory():
    legal_vars = [
        True,
        False,
        [],
        [1, 2, 3],
        {},
        {'1': '2'},
        0,
        42,
        '',
        '42',
        None,
        object,
    ]
    for var in legal_vars:
        assert mandatory(var) == var
    try:
        mandatory(Undefined)
    except AnsibleFilterError:
        pass
    else:
        assert False



# Generated at 2022-06-22 11:45:19.874408
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    env = jinja2.Environment()
    env.filters['groupby'] = do_groupby
    assert env.from_string(
        '{{ [{ "a": 1, "b": 2 }, { "a": 1, "b": 3}, { "a": 2, "b": 3}] | groupby("a") | list }}'
    ).render() == "[('1', [('1', {'a': 1, 'b': 2}), ('2', {'a': 1, 'b': 3})]), ('2', [('3', {'a': 2, 'b': 3})])]"

# ===========================================
#  Main jinja2 filters
# ===========================================

# Generated at 2022-06-22 11:45:22.685768
# Unit test for function strftime
def test_strftime():
    assert strftime('%Y-%m-%d', second='1442831580') == '2015-09-22'



# Generated at 2022-06-22 11:45:31.989219
# Unit test for function randomize_list
def test_randomize_list():
    '''
    randomize_list: Check that randomize_list() gives a random order of list elements
    '''
    mylist = ['a', 'b', 'c', 'd']
    random_lists = []
    for i in range(0, 1000):
        tmp = randomize_list(mylist, seed=i)
        if tmp not in random_lists:
            random_lists.append(tmp)
    if len(random_lists) < 50:
        raise Exception("randomize_list() does not randomize lists effectively")
test_randomize_list.unittest = ['.randomize_list']



# Generated at 2022-06-22 11:45:44.465781
# Unit test for function regex_search
def test_regex_search():
    string = '<a href="http://ansible.com"> link</a>'
    regex_1 = (r'<a.*href=[\'"](.*?)[\'"].*>.*<\/a>')

    assert regex_search(string, regex_1, '\\g<1>') == 'http://ansible.com'

    regex_2 = (r'<a.*href="(?P<url>.*?)".*>(?P<text>.*)<\/a>')
    assert regex_search(string, regex_2, '\\g<url>', '\\g<text>') == ['http://ansible.com', 'link']

    regex_3 = (r'<a.*href="(?P<url>.*?)".*>(?P<text>.*)<\/a>')
    assert regex_search

# Generated at 2022-06-22 11:45:57.126870
# Unit test for function regex_search
def test_regex_search():
    value = 'test2test'
    regex = r'\d(\w+)'
    multiline = False
    ignorecase = False
    assert regex_search(value, regex, multiline, ignorecase) == '2test'
    assert regex_search(value, regex, '\\g<1>', multiline, ignorecase) == '2test'
    assert regex_search(value, regex, '\\g<1>', '\\g<0>', multiline, ignorecase) == ['2test', '2test']
    assert regex_search(value, regex, '\\1', multiline, ignorecase) == '2test'
    assert regex_search(value, regex, '\\1', '\\0', multiline, ignorecase) == ['2test', '2test']

# Generated at 2022-06-22 11:46:08.473786
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('ab', r'^.*$', '\\g<0>', False, False) == 'ab'
    assert regex_search('ab', r'^(.*)$', '\\g<1>', False, False) == 'a'
    assert regex_search('ab', r'^(.*)$', '\\1', False, False) == 'a'
    assert regex_search('ab', r'^(.*)$', '\\g<1>', '\\1', False, False) == ['a', 'a']
    assert regex_search('ab', r'^(.*)$', '\\g<1>', '\\2', False, False) == ['a']



# Generated at 2022-06-22 11:46:19.938076
# Unit test for function do_groupby
def test_do_groupby():
    items = [
        {'name': 'foo', 'group': 'A'},
        {'name': 'bar', 'group': 'B'},
        {'name': 'baz', 'group': 'B'},
        {'name': 'qux', 'group': 'A'},
    ]
    env = jinja2.Environment()
    assert [(('A', [{'group': 'A', 'name': 'foo'}, {'group': 'A', 'name': 'qux'}]),), (
        ('B', [{'group': 'B', 'name': 'bar'}, {'group': 'B', 'name': 'baz'}]),)] == do_groupby(env, items, 'group')



# Generated at 2022-06-22 11:46:22.283419
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    x = mandatory(Undefined('test'))
    assert x == 'test'



# Generated at 2022-06-22 11:46:27.561931
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'\a') == r'\\a'
    assert regex_escape(r'abc.[]$*') == r'abc\.[]\$\*'
    assert regex_escape(r'abc.[]$*', re_type='posix_basic') == r'abc\.\[\]\$\*'
    raise AnsibleFilterError('Failed to complete unit test')



# Generated at 2022-06-22 11:46:39.935544
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('abc123abc', r'123') == '123'
    assert regex_search('abc123abc', r'123', r'\\g<1>') == ['123', '3']
    assert regex_search('abcdabcdabcd', r'a(b)(c)(d)', r'\\g<1>', r'\\2') == ['a', 'b']
    assert regex_search('abcdabcdabcd', r'a(b)(c)(d)', r'\\g<3>', r'\\3') == ['d', 'd']



# Generated at 2022-06-22 11:46:45.287480
# Unit test for function regex_search
def test_regex_search():
    #assert type(regex_search('abc', '')) is re.Match
    assert regex_search('abc', r'a(.)c') == 'b'
    assert regex_search('abc', r'a(.)c', r'\\1') == ['b']
    assert regex_search('abc', r'a(.)c', r'\\g<1>') == ['b']
    assert regex_search('abc', r'a(.)c', r'\\1', r'\\g<1>') == ['b', 'b']



# Generated at 2022-06-22 11:46:50.812891
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('hello world', 'world', 'universe') == 'hello universe'
    assert regex_replace('fooBAR', 'BAR', 'bar', ignorecase=True) == 'foobar'
    assert regex_replace(r'foo\nbar', '\n', '\\n', multiline=True) == 'foo\\nbar'



# Generated at 2022-06-22 11:47:00.610308
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("test<>", r"<(.*?)>") == '>'
    assert regex_search("test<>", r"<(.*?)>", "\\g<1>") == '<'
    assert regex_search("test<>", r"<(.*?)>", "\\1") == '>'
    assert regex_search("test<>", r"<(.*?)>", "\\g<1>", "\\1") == ['<', '>']
    assert regex_search("test<>", r"(<.*?>)") == '<>'
    assert regex_search("test<>", r"(<.*?>)", "\\1") == '<>'
    assert regex_search("test<>", r"(<).*?(>)") == ['<', '>']
    assert regex_search

# Generated at 2022-06-22 11:47:12.643792
# Unit test for function mandatory
def test_mandatory():
    # Test various cases
    a = None
    assert mandatory("foo:{{ bar }}", "my message") == "foo:{{ bar }}"
    assert mandatory("foo:{{ bar }}") == "foo:{{ bar }}"
    try:
        mandatory("foo:{{ baz }}")
        assert False
    except AnsibleFilterError:
        pass
    try:
        mandatory("foo:{{ baz }}", "my message")
        assert False
    except AnsibleFilterError as e:
        assert to_native(e) == "my message"
    try:
        # The template does not have a variable named 'bar'
        assert mandatory("foo:{{ bar }}", "my message") == "foo:{{ bar }}"
        assert False
    except AnsibleFilterError as e:
        assert to_native(e) == "my message"


# Generated at 2022-06-22 11:47:25.274152
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Template
    from ansible.template import generate_ansible_template_vars, Jinja2Environment

    env = Jinja2Environment()

    # test jinja >= 2.9.0, <= 2.9.4
    template_from = generate_ansible_template_vars(env, from_version='2.9.0')
    template_to = generate_ansible_template_vars(env, to_version='2.9.4')
    template = Template("{% set foo = [{'a':'1', 'b':'2'}, {'a':'3', 'b':'2'}] %}"
                        "{% set foo = foo | groupby('b') %}"
                        "{{ foo | to_json | from_json }}")

# Generated at 2022-06-22 11:47:36.727214
# Unit test for function do_groupby
def test_do_groupby():
    """
    This unit test ensures that the do_groupby function will correctly
    convert a namedtuple to a regular tuple.

    It should work across all versions of jinja2.
    """
    # pylint: disable=protected-access
    # Ensure that we aren't using the real `do_groupby`
    if jinja2._do_groupby is _do_groupby:
        jinja2._do_groupby = None

    from jinja2.runtime import Undefined
    from jinja2.filters import do_groupby

    # Mock out the jinja2 `do_groupby` function.
    # We don't want to use the real do_groupby here, as it won't give
    # us the namedtuple that we want to test with.

# Generated at 2022-06-22 11:47:49.293834
# Unit test for function mandatory
def test_mandatory():
    from ansible.module_utils._text import to_text
    try:
        assert mandatory(to_text("hello")) == to_text("hello")
        assert mandatory(to_text("hello"), msg="error") == to_text("hello")

        # Should fail with msg
        assert mandatory(AnsibleUndefined(), msg="error") == "error"

        # Should fail without msg
        assert mandatory(AnsibleUndefined()) == "Mandatory variable not defined."

        # Should fail with a custom undefined name
        assert mandatory(AnsibleUndefined("myvar")) == "Mandatory variable 'myvar' not defined."
    except AnsibleFilterError as e:
        raise AssertionError("%s failed: %s" % (to_text(e.caller), to_text(e.msg)))
# End unit tests for function mandatory



# Generated at 2022-06-22 11:47:55.646338
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('some_value') == 'some_value'
    try:
        mandatory()
        assert False
    except AnsibleFilterError as e:
        assert to_text(e) == "Mandatory variable not defined."
    try:
        mandatory(None, 'some_msg')
        assert False
    except AnsibleFilterError as e:
        assert to_text(e) == 'some_msg'



# Generated at 2022-06-22 11:48:07.156544
# Unit test for function mandatory
def test_mandatory():
    env = {}

    if sys.version_info < (2, 7):
        import ansible.utils.unsafe_proxy

        @ansible.utils.unsafe_proxy.safe_eval(globals=globals(), locals=env)
        def assert_equals(left, right):
            assert left == right

        assert_equals(mandatory(env['mandatory'], "msg"), "foo")
        try:
            assert_equals(mandatory(env['mandatory']), "foo")
            # Should not get here
            assert False
        except AnsibleFilterError:
            pass

# Generated at 2022-06-22 11:48:22.984684
# Unit test for function subelements
def test_subelements():
    test_data = [
        {'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']},
        {'name': 'bob', 'groups': ['wheel', 'users'], 'authorized': ['/tmp/bob/acme.pub', '/tmp/bob/evil.pub']},
    ]


# Generated at 2022-06-22 11:48:28.074078
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    simple_list = [u"item1", u"item2", u"item3"]
    assert to_nice_yaml(simple_list) == (
        '- item1\n'
        '- item2\n'
        '- item3\n'
    )


# Generated at 2022-06-22 11:48:39.736548
# Unit test for function regex_replace
def test_regex_replace():
    # Tests for regex_replace
    string_1 = 'test'
    string_2 = 'Test'
    string_3 = 'test test'
    string_4 = 'test Test'
    string_5 = 'Test test'
    string_6 = 'Test Test'
    string_7 = 'TEST'
    string_8 = 'TEST TEST'

    pattern_1 = 'test'
    pattern_2 = 'TEST'
    pattern_3 = 'TESTA'
    pattern_4 = 'test test'

    replacement_1 = 'replacement'
    replacement_2 = 'RePlAcEmEnT'

    assert regex_replace(string_1, pattern_1, replacement_1) == replacement_1
    assert regex_replace(string_1, pattern_1, replacement_2) == replacement_2

# Generated at 2022-06-22 11:48:44.736342
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'a': '1'}) == '''\
a: 1
'''
    assert to_nice_yaml({'a': '1', 'b': '2'}, indent=2) == '''\
  a: 1
  b: 2
'''
    assert to_nice_yaml({'a': '1', 'b': {'c': '2'}}, indent=2) == '''\
  a: 1
  b:
    c: 2
'''



# Generated at 2022-06-22 11:48:56.745526
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import DictLoader
    from jinja2.environment import Environment
    from ansible.template.safe_eval import unsafe_eval
    env = Environment(loader=DictLoader({'tmpl': u"""{{{
        {% set users = [
            {'name': 'Bob', 'group': 'admin'},
            {'name': 'David', 'group': 'member'},
            {'name': 'Chris', 'group': 'admin'}
        ] %}
        {% set users_grouped = users | groupby('group') %}
        {{ users_grouped | map(attribute='list') | list }}
        }}}"""}))
    result_template = env.get_template('tmpl')
    result = result_template.render()
    elastic_result = unsafe_eval(result)

   

# Generated at 2022-06-22 11:49:06.052269
# Unit test for function extract
def test_extract():
    env = DummyEnvironment()
    result = extract(env, 'key1', {'key1': 'value'})
    assert result == 'value'

    result = extract(env, 'key1', {'key1': 'value'}, 'key2')
    assert result == None

    result = extract(env, 'key1', {'key1': 'value'}, ['key2', 'key3'])
    assert result == None

    result = extract(env, 'key1', {'key1': 'value'}, ['key2', 'key3'], 'key4')
    assert result == None



# Generated at 2022-06-22 11:49:12.415625
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = subelements(obj, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]


# Generated at 2022-06-22 11:49:23.304425
# Unit test for function to_nice_yaml

# Generated at 2022-06-22 11:49:28.533973
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('foobar', '(b.r)', '\\1') == 'foo\\1'
    assert regex_replace('foobar', '(foo)(bar)', '\\2\\1') == 'barfoo'
    assert regex_replace('foobar', '(foo)(bar)', '\\2\\1', multiline=True) == 'barfoo'



# Generated at 2022-06-22 11:49:41.726778
# Unit test for function regex_search
def test_regex_search(): 
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.plugins.filter import regex_search
    value = "hello world's"
    regex = r'(\w+) (\w+)\w*'
    assert wrap_var(regex_search(value, regex, '\\1', '\\g<2>')) == wrap_var(yaml_load('''
- hello
- world
'''))
    assert wrap_var(regex_search(value, regex, '\\1')) == wrap_var(yaml_load('''
- hello
'''))

# Generated at 2022-06-22 11:49:56.777535
# Unit test for function comment
def test_comment():
    assert comment('text') == '# text'
    assert comment(
        'text', 'plain', decoration='// ') == '// text'
    assert comment(
        'text', 'erlang', decoration='%% ') == '% text'
    assert comment('text', 'c') == '// text'
    assert comment('text', 'cblock') == '/*\n * text\n */'
    assert comment(
        'text', 'xml', decoration='@ ', newline='\r\n') == '<!--\r\n - text\r\n-->'
    assert comment(
        'text\nwith\nnewlines',
        'cblock',
        prefix='% ') == '/*\n * % text\n * % with\n * % newlines\n */'

# Generated at 2022-06-22 11:50:08.548493
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.compat.tests.mock import patch, MagicMock

    # pylint: disable=redefined-outer-name
    environment = MagicMock()

    with patch.object(environment, 'getattribute') as getattribute_mock:
        getattribute_mock.return_value = "groupname"

        with patch('ansible.parsing.yaml.objects.groupby') as groupby_mock:
            groupby_mock.return_value = [
                ("groupname", [{"itema": "vala"}]),
                ("groupname", [{"itemb": "valb"}])
            ]

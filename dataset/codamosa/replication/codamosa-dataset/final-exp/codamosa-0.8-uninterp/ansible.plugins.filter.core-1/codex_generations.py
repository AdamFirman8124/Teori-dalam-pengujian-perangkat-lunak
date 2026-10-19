

# Generated at 2022-06-22 11:40:49.766370
# Unit test for function extract
def test_extract():
    env = {}
    #test standard dict
    d = dict(testing=dict(one=1, two=2))
    assert extract('one', d, env) == 1
    assert extract('two', d, env) == 2
    #test nested dict
    assert extract(['testing', 'one'], d, env) == 1
    assert extract(['testing', 'two'], d, env) == 2
    #test lists
    l = [1, 2, 3]
    assert extract(0, l, env) == 1
    assert extract(1, l, env) == 2
    assert extract(2, l, env) == 3
    #test morekeys
    d2 = dict(a=dict(b=dict(c=dict(d=1))))
    assert extract('a', d2, env, ['b', 'c'])

# Generated at 2022-06-22 11:41:02.328700
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r'\ # $ ^ . [ ] + ( ) ? * { } |') == r'\\ \# \$ \^ \. \[ \] \+ \( \) \? \* \{ \} \|'
    assert regex_escape('foo/bar', 'posix_basic') == 'foo/bar'
    assert regex_escape('foo/bar', 'posix_extended') == r'foo/bar'
    assert regex_escape('foo/bar', 'posix_extended') == r'foo/bar'
    assert regex_escape('foo[bar', 'posix_basic') == r'foo\[bar'
    assert regex_escape('foo[bar', 'posix_extended') == r'foo\[bar'

# Generated at 2022-06-22 11:41:09.798897
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1) == 1
    try:
        assert mandatory(None)
    except AnsibleFilterError as e:
        assert to_native(e) == 'Mandatory variable  not defined.'

    try:
        assert mandatory(None, msg='Custom msg')
    except AnsibleFilterError as e:
        assert to_native(e) == 'Custom msg'



# Generated at 2022-06-22 11:41:21.076564
# Unit test for function flatten
def test_flatten():
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, 2, [3, 4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([1, 2, [3, 4, [5]]]) == [1, 2, 3, 4, [5]]
    assert flatten([1, 2, [3, 4, [5]]], levels=2) == [1, 2, 3, 4, 5]
    assert flatten([1, 2, [3, 4, [5]]], levels=1) == [1, 2, 3, 4, [5]]
    assert flatten([1, 2, [3, 4, [5]]], levels=0) == [1, 2, [3, 4, [5]]]

# Generated at 2022-06-22 11:41:23.784101
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/passwd') == ['/etc/passwd']
    assert fileglob('/etc/r*wd') == ['/etc/r*wd']



# Generated at 2022-06-22 11:41:33.334929
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    if mandatory(Undefined()):
        raise Exception("test_mandatory failed (1)")

    try:
        mandatory(Undefined(name="foo"))
    except:
        pass
    else:
        raise Exception("test_mandatory failed (2)")

    try:
        mandatory(Undefined(name="foo"), msg="some custom message")
    except Exception as e:
        if "some custom message" not in str(e):
            raise Exception("test_mandatory failed (%s)" % e)
    else:
        raise Exception("test_mandatory failed (3)")

# -----------------------------------------------------------------------------
# jinja2 Filters for transforming variables
# Reference: http://jinja.pocoo.org/docs/dev/templates/#list-of-builtin-filters




# Generated at 2022-06-22 11:41:35.744706
# Unit test for function fileglob
def test_fileglob():
    pathname = "/etc/profile.d/gcc.csh"
    return [g for g in glob.glob(pathname) if os.path.isfile(g)]



# Generated at 2022-06-22 11:41:48.682753
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(value="test", pattern="test", replacement="some") == "some"
    assert regex_replace(value="test", pattern="[a-z]{4}", replacement="some") == "some"
    assert regex_replace(value="test", pattern="[a-z]{3}", replacement="some") != "some"
    assert regex_replace(value="Test", pattern="[a-z]{4}", replacement="some") != "some"
    assert regex_replace(value="Test", pattern="[a-z]{4}", replacement="some", ignorecase=True) == "some"
    assert regex_replace(value="Test", pattern="[A-Z]{4}", replacement="some", ignorecase=True) == "some"

# Generated at 2022-06-22 11:41:56.183615
# Unit test for function flatten

# Generated at 2022-06-22 11:42:07.316261
# Unit test for function regex_replace

# Generated at 2022-06-22 11:42:15.612440
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(10) == 10
    assert mandatory("foo", msg="Hello") == "foo"
    try:
        mandatory()
        assert False
    except AnsibleFilterError as e:
        assert to_text(e) == "Mandatory variable  not defined."



# Generated at 2022-06-22 11:42:27.139013
# Unit test for function comment
def test_comment():
    import sys
    import textwrap

    # Test all supported comment styles
    for style in ['plain', 'erlang', 'c', 'cblock', 'xml']:
        assert comment(
            textwrap.dedent('''\
                Test comment string
                Second line of the string
            '''),
            style,
            decoration='-- ',
            prefix_count=0,
            postfix_count=2) == textwrap.dedent('''\
                -- Test comment string
                -- Second line of the string

                --
            '''), \
            '''Failed comment() test for a "%s" style with all parameters specified''' % style

# Generated at 2022-06-22 11:42:33.259007
# Unit test for function fileglob
def test_fileglob():
    assert ['/etc/ansible/hosts'] == fileglob('/etc/ansible/hosts')
    assert [] == fileglob('/etc/ansible/nohostshere')
    assert [] == fileglob('/etc/ansible/nohostshere*')
    assert ['/etc/ansible/hosts', '/etc/ansible/hosts.new'] == fileglob('/etc/ansible/hosts*')



# Generated at 2022-06-22 11:42:38.214660
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(42) == 42
    assert mandatory(None) is None
    assert mandatory([42]) == [42]
    assert mandatory({'a': 42}) == {'a': 42}
    assert mandatory(AnsibleUndefined) == ''
    try:
        mandatory(AnsibleUndefined, 'mandatory() failed')
    except AnsibleFilterError as e:
        assert e.message == 'mandatory() failed'
    try:
        mandatory(AnsibleUndefined)
    except AnsibleFilterError as e:
        assert e.message == "Mandatory variable '' not defined."



# Generated at 2022-06-22 11:42:41.283391
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list([0, 1, 2]) == [0, 1, 2]
    assert randomize_list([0, 1, 2], seed=0) == [1, 2, 0]



# Generated at 2022-06-22 11:42:46.883868
# Unit test for function do_groupby
def test_do_groupby():
    """simple test case to ensure that do_groupby runs as expected to ensure it behaves
    the same as the jinja2 groupby functionality.  Ensures that it can group on
    simple attributes, and recursive attributes.
    """
    from jinja2 import Environment, meta, Template
    import jinja2

    # We need to load the ansible filters so that jinja2 will recognize them when
    # parsing for template variables
    import ansible.plugins.filter.core
    import ansible.plugins.filter.json
    import ansible.plugins.filter.mathstuff
    import ansible.plugins.filter.network
    import ansible.plugins.filter.strings
    import ansible.plugins.filter.template
    import ansible.plugins.filter.urls
    import ansible.plugins.filter.uuid
    import ansible.plugins

# Generated at 2022-06-22 11:42:51.652024
# Unit test for function strftime
def test_strftime():
    assert strftime("%Y-%m-%d %H:%M", 1475581741) == '2016-10-03 21:29'
    assert strftime("%Y-%m-%d %H:%M") == strftime("%Y-%m-%d %H:%M", time.time())


# Generated at 2022-06-22 11:42:58.750281
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    from jinja2.runtime import Context

    env = jinja2.Environment(extensions=[])
    # Ensure that the environment has the filter
    assert 'groupby' in env.filters
    assert env.filters['groupby'] == filters.do_groupby

    value = [
        {'name': 'a', 'group': 'x'},
        {'name': 'b', 'group': 'y'},
        {'name': 'c', 'group': 'x'},
    ]

    # Test regular working case
    template = "{%- for group in list|groupby('group') -%}{{ group.grouper }}: {{ group.list|map(attribute='name')|list }} {%- endfor -%}"
    t = env.from_string(template)

# Generated at 2022-06-22 11:43:01.169660
# Unit test for function get_hash
def test_get_hash():
    assert len(get_hash('')) == 40
    assert len(get_hash('')) == 40
    assert len(get_hash('mary had a little lamb')) == 40


# Generated at 2022-06-22 11:43:07.065942
# Unit test for function mandatory
def test_mandatory():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    a = AnsibleUnicode('\xe2\x82\xac')  # utf-8 encoded Euro sign
    try:
        mandatory(a)
    except AnsibleFilterError:
        pass



# Generated at 2022-06-22 11:43:23.260641
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    from ansible.module_utils.six import text_type
    from ansible.modules.extras.cloud.amazon import ec2_tag
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    dataloader.set_vault_password('secret')

# Generated at 2022-06-22 11:43:26.275602
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(True) is True
    assert mandatory(None) is None
    assert mandatory(False) is False
    assert mandatory(0) == 0
    assert mandatory(['test']) == ['test']



# Generated at 2022-06-22 11:43:34.357241
# Unit test for function regex_replace
def test_regex_replace():
    # No options
    assert regex_replace('abc123', '123', '456') == 'abc456'
    # Ignorecase
    assert regex_replace('abc123', '123', '456', ignorecase=True) == 'abc456'
    assert regex_replace('abc123', '123', '456', ignorecase=True) == 'abc456'
    assert regex_replace('abc123', 'ABC', '456', ignorecase=True) == '456123'
    # Multiline
    assert regex_replace('abc\n123', '^abc', '456', multiline=True) == '456\n123'
    assert regex_replace('abc\n123', '^123', '456', multiline=True) == 'abc\n456'



# Generated at 2022-06-22 11:43:43.409502
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Template
    from jinja2 import Environment
    from jinja2 import StrictUndefined

    items = [{'a': 1, 'b': 2}, {'a': 1, 'b': 3}, {'a': 2, 'b': 4}]

    env = Environment()
    env.filters['groupby'] = do_groupby
    template = Template(
        "{%- set grouped = items | groupby('a') -%}"
        "{{ grouped | map(attribute='list') | list }}")

    # Before this was fixed, this would raise an exception of:
    #   "TypeError: No encoder found for type '<class 'jinja2.runtime.Undefined'>'".
    # This is because the safe_eval function in ansible.template.safe_eval.safe_eval
    #

# Generated at 2022-06-22 11:43:55.309492
# Unit test for function mandatory
def test_mandatory():
    data = {'var1': 'var1 is alive'}

    # Test that if variable is mandatory, it returns the same variable
    assert mandatory(data['var1']) == 'var1 is alive'

    # Test that if variable is not mandatory, it raises an error
    data['var2'] = None

    try:
        mandatory(data['var2'])
    except Exception as e:
        assert isinstance(e, AnsibleFilterError)
        assert 'Mandatory variable not defined' in e.message

    try:
        mandatory(data['var1'], msg="Variable 'var1' is required")
    except Exception as e:
        assert isinstance(e, AnsibleFilterError)
        assert e.message == 'Variable \'var1\' is required'



# Generated at 2022-06-22 11:43:58.484824
# Unit test for function fileglob
def test_fileglob():
  assert fileglob('/tmp/nofile') == []
  assert len(fileglob('/etc/passwd')) == 1



# Generated at 2022-06-22 11:44:11.464336
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import jinja2
    env = jinja2.Environment()

    class Collection(list):
        attr = None

    test_list = Collection([
        {'key': 'abc', 'value': 1},
        {'key': 'def', 'value': 2},
        {'key': 'ghi', 'value': 1},
        {'key': 'jkl', 'value': 2},
        {'key': 'mno', 'value': 3},
    ])

    result = _do_groupby(env, test_list, 'value')
    assert len(result) == 3
    assert type(result[0]) == tuple
    assert type(result[1]) == tuple
    assert type(result[2]) == tuple

# Generated at 2022-06-22 11:44:19.006649
# Unit test for function regex_search
def test_regex_search():
    assert None == regex_search('', 'foo')
    assert 'bar' == regex_search('foo', 'o+')
    assert 'bar' == regex_search('foo', 'o+', '\\g<0>')
    assert 'bar' == regex_search('foo', 'o+', '\\0')
    assert ['bar'] == regex_search('foo', 'o+', '\\g<0>', 'foobar')
    assert ['bar', 'bar'] == regex_search('foo', 'o+', '\\g<0>', '\\1')
    assert ['o'] == regex_search('foo', 'o+', '\\1')


# Generated at 2022-06-22 11:44:29.840926
# Unit test for function extract
def test_extract():

    test_data = dict(
        dict_1=dict(key_1='value_1', list_1=['item_1', 'item_2']),
        key_2='value_2',
        list_2=['item_1', dict(key_3='value_3')],
        key_4='value_4',
        key_5=['item_1', dict(key_6=['item_1', dict(key_7='value_7')])])

# Generated at 2022-06-22 11:44:42.038036
# Unit test for function do_groupby
def test_do_groupby():
    # Test jinja2 <2.9.0
    # In python3 namedtuples use `ClassName=` in repr, in py2 they just use
    # `...`. The latter is safe to eval and the former is not.
    # Test that this is not overloaded and that tuples are returned
    _jinja2_orig_groupby = environmentfilter(jinja2._jinja2.Filters.do_groupby)

# Generated at 2022-06-22 11:44:58.456230
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(r'hello world', r'hello (\w+)', '\\g<1>') == ['world']
    assert regex_search(r'hello world', r'hello (\w+)', '\\1') == ['world']
    assert regex_search(r'hello world', r'world hello') is None
    assert regex_search(r'hello world', r'hello (\w+)', '\\1', '\\2') == ['world', None]
    assert regex_search(r'hello world', r'hello (\w+)', '\\g<1>', '\\g<2>') == ['world', None]
    assert regex_search(r'hello world', r'hello (\w+)', '\\2', '\\g<1>') == [None, 'world']

# Generated at 2022-06-22 11:45:08.356671
# Unit test for function mandatory
def test_mandatory():
    try:
        assert mandatory(1) == 1
        assert mandatory('') == ''
        assert mandatory(None) is None
        assert mandatory(False) is False
    except Exception as e:
        assert False, "mandatory filter returned unexpected result: %s" % to_native(e)

    try:
        from jinja2.runtime import Undefined
        u = Undefined("foo")
        assert mandatory(u, 'some message') == 1
    except Exception as e:
        assert 'some message' in to_native(e)

    try:
        from jinja2.runtime import Undefined
        u = Undefined()
        assert mandatory(u) == 1
    except Exception as e:
        assert 'Mandatory variable not defined' in to_native(e)



# Generated at 2022-06-22 11:45:15.656555
# Unit test for function mandatory
def test_mandatory():
    assert mandatory('foo') == 'foo'
    assert mandatory(None) == None
    assert mandatory(False) == False
    try:
        mandatory(list())
    except AnsibleFilterError as e:
        ex = e
    assert str(ex) == "Mandatory variable not defined."
    try:
        mandatory(list(), msg='Testing')
    except AnsibleFilterError as e:
        ex = e
    assert str(ex) == "Testing"



# Generated at 2022-06-22 11:45:18.696896
# Unit test for function randomize_list
def test_randomize_list():
    assert randomize_list([1, 2, 3, 4]) != [1, 2, 3, 4]
    assert randomize_list([1, 2, 3, 4], seed=1) == [1, 3, 4, 2]



# Generated at 2022-06-22 11:45:31.899227
# Unit test for function regex_search
def test_regex_search():
    # Tests with named groups
    assert regex_search("spam and eggs", r"(?P<spam>(.*)) and (?P<eggs>(.*))") == ['spam and eggs', 'spam', 'eggs']
    assert regex_search("spam and eggs", r"(?P<spam>(.*)) and (?P<eggs>(.*))", '\\g<spam>') == ['spam and eggs', 'spam']
    assert regex_search("spam and eggs", r"(?P<spam>(.*)) and (?P<eggs>(.*))", '\\g<eggs>') == ['spam and eggs', 'eggs']

# Generated at 2022-06-22 11:45:44.412885
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("I want to  see what is  behind", r"[^\s]+", "\\2", "\\g<word>") == ["is", "what"]
    assert regex_search("I want to  see what is  behind", r"[^\s]+", "\\2", "\\g<word>", ignorecase=True) == ["is", "what"]
    assert regex_search("I want to  see what is  behind", r"[^\s]+", "\\2", "\\g<word>", ignorecase=False) == ["is", "what"]
    assert regex_search("I want to  see what is  behind", r"[^\s]+", "\\2", "\\g<word>", multiline=True) == ["is", "what"]

# Generated at 2022-06-22 11:45:54.356434
# Unit test for function mandatory
def test_mandatory():
    '''Test mandatory'''
    try:
        mandatory(None)
    except AnsibleFilterError as e:
        assert "Mandatory variable 'None' not defined." in to_text(e)
    try:
        mandatory(undefined)
    except AnsibleFilterError as e:
        assert "Mandatory variable not defined." in to_text(e)
    try:
        mandatory(undefined, "Custom error")
    except AnsibleFilterError as e:
        assert "Custom error" in to_text(e)
    assert mandatory(42) == 42
    assert mandatory('Hello World!') == 'Hello World!'


# Generated at 2022-06-22 11:46:00.734323
# Unit test for function fileglob
def test_fileglob():
    ret = fileglob("/bin/[b-c]*")
    assert isinstance(ret, list)
    # This test is fragile.
    # TODO: sort the return values to avoid issues from filesystem order
    assert ret == ['/bin/bash', '/bin/cat', '/bin/chgrp']



# Generated at 2022-06-22 11:46:10.652423
# Unit test for function regex_search
def test_regex_search():
    def result(args, kwargs, want):
        got = regex_search(*args, **kwargs)
        assert got == want, 'regex_search({}, {}) == {} != {}'.format(args, kwargs, got, want)

    # Test for single value
    result(['\\g<1>', '((foo)(bar))', 'foobar'], {}, 'foo')
    result(['\\g<2>', '((foo)(bar))', 'foobar'], {}, 'bar')
    result(['\\g<3>', '((foo)(bar))', 'foobar'], {}, None)
    result(['\\2', '((foo)(bar))', 'foobar'], {}, 'bar')
    result(['\\3', '((foo)(bar))', 'foobar'], {}, None)


# Generated at 2022-06-22 11:46:12.138543
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/tmp/') == '/tmp/'



# Generated at 2022-06-22 11:46:27.688130
# Unit test for function regex_search
def test_regex_search():
    value = 'myvarname'
    assert regex_search(value,'myvarname') == 'myvarname'
    assert regex_search(value,'myvar') == 'myvar'
    assert regex_search(value,'var') == 'var'
    assert regex_search(value,'name') == 'name'
    assert regex_search(value,'x') == None
    assert regex_search(value,'\\g<var>') == 'myvarname'
    assert regex_search(value,'\\g<var>\\g<name>') == ['myvar', 'name']
    assert regex_search(value,'myvar\\g<name>') == ['myvarname']
    assert regex_search(value,'\\g<var>name') == ['myvarname']

# Generated at 2022-06-22 11:46:38.913559
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('foo', 'f.+') == 'foo'
    assert regex_search('foobar', 'f.+', '\\1') == ['foo']
    assert regex_search('bar', 'f.+') is None
    assert regex_search('foobar', 'f.+', '\\2') is None
    assert regex_search('foobar', 'f.+', '\\g<1>') == ['foo']
    assert regex_search('foobar', 'f.+', '\\g<2>') is None
    assert regex_search('foo', 'f(.)(.)', '\\1', '\\2') == ['o', 'o']
    assert regex_search('foo', 'f(.)(.)', '\\g<1>', '\\g<2>') == ['o', 'o']
    assert regex

# Generated at 2022-06-22 11:46:50.080861
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    # Successfully parse dictionary as nice yaml
    d = {'data': {'key': 'value'}}
    result = to_nice_yaml(d)
    assert(result == 'data:\n    key: value\n')
    # Successfully parse map of dictionary
    d = {'data': {'key': 'value'}, 'data2': {'key2': 'value2'}}
    result = to_nice_yaml(d)
    assert(result == 'data:\n    key: value\ndata2:\n    key2: value2\n')
    # Successfully parse list as nice yaml
    d = ['a','b','c','d']
    result = to_nice_yaml(d)
    assert(result == '- a\n- b\n- c\n- d\n')


# Generated at 2022-06-22 11:46:59.080625
# Unit test for function mandatory
def test_mandatory():
    try:
        mandatory(None, msg='Hello')
        raise Exception('mandatory did not raise exception')
    except AnsibleFilterError as e:
        assert 'Hello' in e.message, e.message

    try:
        mandatory(AnsibleUndefined, msg='Hello')
        raise Exception('mandatory did not raise exception')
    except AnsibleFilterError as e:
        assert 'Hello' in e.message, e.message

    result = mandatory(12345, msg='Hello')
    assert result == 12345, result

    result = mandatory(AnsibleUndefined, msg='Hello')
    assert result == AnsibleUndefined, result



# Generated at 2022-06-22 11:47:08.869635
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    env = jinja2.Environment()
    do_groupby = lambda x, y: do_groupby(env, x, y)
    assert do_groupby(['a', 'b', 'c'], 'upper') == [('a', 'A'), ('b', 'B'), ('c', 'C')]
    assert do_groupby([{'id': 1, 'a': 'b'}, {'id': 2, 'c': 'd'}], 'id') == [(1, {'id': 1, 'a': 'b'}), (2, {'id': 2, 'c': 'd'})]



# Generated at 2022-06-22 11:47:22.026460
# Unit test for function regex_search
def test_regex_search():
    string = 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
    assert regex_search(string, r"(a)", ignorecase=False) == 'a'
    assert regex_search(string, r"(a)", ignorecase=True) == 'a'
    assert regex_search(string, r"([a-z]+)", ignorecase=False) == 'abc'
    assert regex_search(string, r"([a-z]+)", ignorecase=True) == 'abc'
    assert regex_search(string, r"([a-z]+)", ignorecase=True, multiline=True) == 'abc'
    assert regex_search(string, r"([a-z]+)", ignorecase=True, multiline=False) == 'abc'

# Generated at 2022-06-22 11:47:32.776354
# Unit test for function strftime
def test_strftime():
    # Get the current time
    now = time.time()
    # Use time module to get timezone
    timezone = time.strftime('%Z', time.localtime(now))
    # Convert timezone to acceptable format
    timezone = timezone.replace('+', '-plus-').replace('-', '-minus-')
    # Assert strftime returns the same time as time.strftime
    if strftime('%Y-%m-%d %H:%M:%S %z', now) != time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(now)):
        raise AssertionError('strftime should return the same date as time.strftime')
    # Assert strftime returns the same timezone as time.strftime

# Generated at 2022-06-22 11:47:45.591845
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined
    from ansible.module_utils.six import PY3

    # Test a defined variable
    assert mandatory('test') == 'test'
    assert mandatory(True) is True
    assert mandatory(1) == 1
    assert mandatory(['test', 'test2']) == ['test', 'test2']

    # Test an undefined variable
    try:
        mandatory(Undefined())
    except AnsibleFilterError:
        pass
    else:
        assert False, "Expected an AnsibleFilterError"

    # Test an undefined variable with a custom error message
    try:
        mandatory(Undefined(), msg="Custom error message")
    except AnsibleFilterError:
        pass
    else:
        assert False, "Expected an AnsibleFilterError"

    # Test an undefined variable with a variable name

# Generated at 2022-06-22 11:47:47.152544
# Unit test for function mandatory
def test_mandatory():
    variable = 'test'
    assert mandatory(variable) == variable



# Generated at 2022-06-22 11:47:58.070756
# Unit test for function do_groupby
def test_do_groupby():
    """ Unit test to ensure that do_groupby returns a list of tuples,
    as opposed to namedtuples which could cause an issue with
    `ansible.template.safe_eval.safe_eval`
    """
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inv)
    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-22 11:48:10.150775
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(1) == 1

# Generated at 2022-06-22 11:48:19.706073
# Unit test for function to_yaml

# Generated at 2022-06-22 11:48:32.705612
# Unit test for function comment
def test_comment():
    assert comment('test') == '# test'
    assert comment('test', style='erlang') == '% test'
    assert comment('test', style='c') == '// test'
    assert comment('test', style='cblock') == '/*\n * test\n */'
    assert comment('test', style='xml') == '<!--\n - test\n-->'
    assert comment('test', style='xml', decoration='-- ') == '<!--\n-- test\n-->'
    assert comment('test', beginning='/*\n *') == '/*\n *\n * test'
    assert comment('test', end='*/') == '# test\n*/'
    assert comment('test', end='*/', decoration='# ') == '# test\n*/'

# Generated at 2022-06-22 11:48:45.403094
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('zzz', 'z+', '\\g<0>') == ['zzz']
    assert regex_search('zzz', 'z+', '\\g<0>', '\\1') == ['zzz', 'z']
    assert regex_search('zzz', 'z+', '\\g<0>', '\\42') == ['zzz', None]
    assert regex_search('zzz', 'z+', '\\g<0>', '\\g<42>') == ['zzz', None]
    assert regex_search('zzz', 'z+', '\\g<0>', '\\g<0>') == ['zzz', 'zzz']
    assert regex_search('zzz', 'z+(?P<letter>z)', '\\g<letter>') == ['z']
    assert regex_

# Generated at 2022-06-22 11:48:56.461671
# Unit test for function regex_search
def test_regex_search():
    fail = False
    fail |= regex_search('abc123', r'(?P<group1>\d{3})(?P<group2>\d{3})') != '123'
    fail |= regex_search('abc123', r'(?P<group1>\d{3})(?P<group2>\d{3})', '\\g<group2>') != '123'
    fail |= regex_search('abc123', r'(?P<group1>\d{3})(?P<group2>\d{3})', '\\2') != '123'

# Generated at 2022-06-22 11:49:09.125023
# Unit test for function comment
def test_comment():
    assert comment('test') == '# test\n'
    assert comment('test', 'xml') == '<!-- - test -->\n'
    assert comment('test', 'cblock') == '/*\n * test\n */\n'
    assert comment('test', newline='\r\n') == '# test\r\n'
    assert comment('test', 'xml', newline='\r\n') == '<!--\r\n - test\r\n-->\r\n'
    assert comment('test', 'cblock', newline='\r\n') == '/*\r\n * test\r\n */\r\n'
    assert comment('test', decoration='; ') == '; test\n'

# Generated at 2022-06-22 11:49:15.508951
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Template
    from jinja2.runtime import Context
    t = Template(
        '{{ lookup("pipe", "/bin/echo -n test") | groupby("test", "test") }}'
    )
    assert [("test", ["test"])] == t.root_render_func(Context())

# Generated at 2022-06-22 11:49:26.907182
# Unit test for function mandatory
def test_mandatory():
    from jinja2.exceptions import UndefinedError

    # When
    #   given a variable that is not defined
    try:
        mandatory(None)
        assert False, 'Should raise'
    except AnsibleFilterError as e:
        # Then
        #   it should raise an exception that contains the variable name
        assert 'not defined' in to_native(e)

        # When
        #   given a variable that is defined
        assert mandatory('value') == 'value'

    # When
    #   given a variable that is undefined

# Generated at 2022-06-22 11:49:38.027150
# Unit test for function mandatory
def test_mandatory():

    # test input as str
    try:
        mandatory("test_string")
    except AnsibleFilterError:
        assert False

    # test input as int
    try:
        mandatory(1)
    except AnsibleFilterError:
        assert False

    # test input as float
    try:
        mandatory(1.1)
    except AnsibleFilterError:
        assert False

    # test input as bool
    try:
        mandatory(True)
    except AnsibleFilterError:
        assert False

    # test input as list
    try:
        mandatory([])
    except AnsibleFilterError:
        assert False

    # test input as dict
    try:
        mandatory({})
    except AnsibleFilterError:
        assert False

    # test input as AnsibleUndefined

# Generated at 2022-06-22 11:49:47.643023
# Unit test for function mandatory
def test_mandatory():
    # Test if string is returned
    assert mandatory('one') == 'one'
    # Test if dict is returned.
    assert mandatory({'one': 1, 'two': 2}) == {'one': 1, 'two': 2}

    # Test if error is raised when non existing var is referenced.
    try:
        mandatory(mandatory_fake_var)
    except AnsibleFilterError as e:
        assert "Mandatory variable 'mandatory_fake_var' not defined." in str(e)

    # Test if error is raised when var is undefined
    try:
        mandatory(undefined_var)
    except AnsibleFilterError as e:
        assert "not defined" in str(e)

    # Test if error is raised when var is None

# Generated at 2022-06-22 11:49:56.384692
# Unit test for function flatten
def test_flatten():
    assert flatten([[["foo", "bar"], "baz"], "qux", ["corge"]], skip_nulls=False) == ["foo", "bar", "baz", "qux", "corge"]
    assert flatten([[["foo", "bar"], "baz"], "qux", ["corge"]], skip_nulls=True) == ["foo", "bar", "baz", "qux", "corge"]
    assert flatten([[[["foo", "bar"], "baz"], "qux"], "corge"], skip_nulls=False) == ["foo", "bar", "baz", "qux", "corge"]

# Generated at 2022-06-22 11:50:08.210274
# Unit test for function do_groupby
def test_do_groupby():
    """Test for jinja2-formatting of namedtuples in ansible
    see: https://github.com/ansible/ansible/issues/20098
    """
    from . import env

    env = env({
        'list_of_groups': [
            dict(group_name='group1', name='host1', hostname='host1.example.com'),
            dict(group_name='group1', name='host2', hostname='host2.example.com'),
            dict(group_name='group2', name='host3', hostname='host3.example.com'),
        ],
    })
    # The jinja2 version that creates the issue returns an
    # unevaluatable repr of the namedtuple.
    # We need to cast it to tuple, to be able to iterate the values
    # and
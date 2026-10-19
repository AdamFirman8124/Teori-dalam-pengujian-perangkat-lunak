

# Generated at 2022-06-22 11:40:47.830207
# Unit test for function get_hash
def test_get_hash():
    assert get_hash('test') == hashlib.sha1('test'.encode()).hexdigest()
    assert get_hash('test', hashtype='md5') == hashlib.md5('test'.encode()).hexdigest()



# Generated at 2022-06-22 11:41:00.365416
# Unit test for function regex_search
def test_regex_search():
    """
    - name: get the filename from a path
      debug: var=item
      with_items: "{{ \"/path/to/filename\" | regex_search('(?<=/)[^/]+$') }}"
    - name: get the filename from a path and the parent directory's name
      debug: var=item
      with_items: "{{ \"/path/to/filename\" | regex_search('(?<=/)[^/]+$', '\\g<1>') }}"
    - name: get the filename from a path, which contains umlauts (äöü), and the parent directory's name
      debug: var=item
      with_items: "{{ \"/path/tö/filename\" | regex_search('(?<=/)[^/]+$', '\\g<1>') }}"
    """
    pass

# Generated at 2022-06-22 11:41:08.391993
# Unit test for function do_groupby
def test_do_groupby():
    # The unit test is here because I'm not sure of the best way to expose the
    # groupby filter unit test to Ansible's test harness.
    #
    # This unit test is designed to run the same test as
    # ansible/test/unit/filter/test_groupby.py, but use the patched
    # `do_groupby` filter.
    import jinja2
    # We only need this filter to test `do_groupby`
    filters = jinja2.Environment().filters


# Generated at 2022-06-22 11:41:15.212300
# Unit test for function mandatory
def test_mandatory():
    data = dict()
    data['foo'] = None
    try:
        result = mandatory(data['foo'])
    except AnsibleFilterError as e:
        result = "failed"
    assert result == "failed"

    data = dict()
    data['bar'] = "bar is defined"
    result = mandatory(data['bar'])
    assert result == "bar is defined"



# Generated at 2022-06-22 11:41:20.724009
# Unit test for function do_groupby
def test_do_groupby():
    environment = Environment()
    data = dict(key1=1, key2=2)
    out = do_groupby(environment, data, 'key1')
    assert len(out) == 1
    assert out[0][0] == 1
    assert out[0][1] == 2



# Generated at 2022-06-22 11:41:30.455028
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('test') == []
    assert fileglob('/test') == []

    assert fileglob('nonexistant') == []
    assert fileglob('/nonexistant') == []

    file_name = 'testfile'
    with open(file_name, 'w+') as f:
        f.close()
    assert fileglob(file_name) == [file_name]

    dir_name = 'testdir'
    os.mkdir(dir_name)
    assert fileglob(dir_name) == []

    try:
        os.remove(file_name)
        os.rmdir(dir_name)
    except:
        # on Windows, cleanup may fail if Git Bash is still running
        pass



# Generated at 2022-06-22 11:41:31.586688
# Unit test for function subelements
def test_subelements():
    import doctest
    doctest.testmod(subelements)



# Generated at 2022-06-22 11:41:34.507163
# Unit test for function fileglob
def test_fileglob():
    list_file = fileglob("/etc/hosts")
    assert list_file == ['/etc/hosts']
    list_file = fileglob("/etc/*")
    assert isinstance(list_file, list)
    assert '/etc/fstab' in list_file



# Generated at 2022-06-22 11:41:37.881473
# Unit test for function mandatory
def test_mandatory():
    try:
        assert mandatory("foo") == "foo"
        assert mandatory("foo", "msg") == "foo"
        assert False, "Mandatory did not raise an exception"
    except Exception as e:
        assert e.msg == "Mandatory variable not defined."



# Generated at 2022-06-22 11:41:50.638955
# Unit test for function do_groupby
def test_do_groupby():
    from ._compat import OrderedDict
    hostvars = {
        'foo': {
            'nic_properties': [('mac_address', '00:11:22:33:44:55'), ('fqdn', 'foo.example.org')]
        },
        'bar': {
            'nic_properties': [('mac_address', '66:77:88:99:00:aa'), ('fqdn', 'bar.example.org')]
        }
    }
    jinjaenv = ansible.plugins.loader.jinja2_env
    jinjaenv.globals['hostvars'] = hostvars
    jinjaenv.filters['mandatory'] = mandatory
    jinjaenv.filters['do_groupby'] = do_groupby

# Generated at 2022-06-22 11:42:06.057362
# Unit test for function subelements
def test_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'groups') == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    assert subelements(obj, 'groups', skip_missing=True) == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

# Generated at 2022-06-22 11:42:12.772503
# Unit test for function regex_escape
def test_regex_escape():
    string = r'Hello, world! How do we $escape everything? Yes, \too.'
    _type = 'posix_basic'
    output = r'Hello\, world\! How do we \$escape everything\? Yes\, \\too\.'
    assert regex_escape(string, _type) == output
    string = r'Hello, world! How do we $escape everything? Yes, \too.'
    _type = 'python'
    output = r'Hello\,\ world\!\ How\ do\ we\ \$escape\ everything\?\ Yes\,\ \\too\.'
    assert regex_escape(string, _type) == output
    string = r'Hello, world! How do we $escape everything? Yes, \too.'
    _type = 'posix_extended'

# Generated at 2022-06-22 11:42:16.599275
# Unit test for function rand
def test_rand():
    for i in xrange(100):
        assert rand(end=100, seed=42) == rand(end=100, seed=42)



# Generated at 2022-06-22 11:42:27.963280
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2.runtime import Context
    from jinja2.environment import Environment
    from jinja2.loaders import DictLoader
    from jinja2 import TemplateNotFound

    # Setup the environment and context
    env = Environment(loader=DictLoader({
        'template': '{{ items | groupby(attribute) }}'
    }), undefined=StrictUndefined)

    ctx = Context({
        'items': [
            {'name': 'a', 'attribute': 'color'},
            {'name': 'b', 'attribute': 'shape'},
            {'name': 'c', 'attribute': 'color'},
            {'name': 'd', 'attribute': 'color'}
        ],
        'attribute': 'attribute'
    })

    # Render the template
    result = env.get_template

# Generated at 2022-06-22 11:42:40.350937
# Unit test for function do_groupby
def test_do_groupby():
    import jinja2
    env = jinja2.Environment()
    data = [{'name': 'Alice', 'role': 'admin'},
            {'name': 'Bob', 'role': 'user'},
            {'name': 'Carol', 'role': 'admin'}]
    res = [('admin', [{'name': 'Alice', 'role': 'admin'},
                      {'name': 'Carol', 'role': 'admin'}]),
           ('user', [{'name': 'Bob', 'role': 'user'}])]
    data.append(res)
    assert do_groupby(env, data[:3], 'role') == res


# functions that are used in the filters module
# (and can be overridden by plugins)

# For backwards compatibility

# Generated at 2022-06-22 11:42:51.180278
# Unit test for function comment
def test_comment():
    # Test with defaults
    assert comment("This is a test") == "# This is a test\n"

    # Test with simple prefix
    assert comment("This is a test", decoration=">>> ") == "# >>> This is a test\n"

    # Test with multiple prefixes
    assert comment("This is a test", decoration=">>> ", prefix_count=3) == "# >>> This is a test\n# >>> \n# >>> \n"

    # Test with simple prefix and postfix
    assert comment("This is a test", decoration=">>> ", postfix="<<< ", postfix_count=1) == "# >>> This is a test\n# <<< \n"

    # Test with simple prefix and multiple postfixes

# Generated at 2022-06-22 11:43:00.366672
# Unit test for function regex_search
def test_regex_search():
    text = '''\
    <link rel="stylesheet" href="https://static.jianshukeji.com/highcharts/6.0.6/css/highcharts.css" />
    <script src="https://static.jianshukeji.com/highcharts/6.0.6/js/highcharts.js"></script>
    <script src="https://code.highcharts.com.cn/highcharts/highcharts-zh_CN.js"></script>
    '''
    pattern = r'src=(?P<quote>["\'])(?P<src_url>.*?)\k<quote>'
    result = regex_search(text, pattern)

# Generated at 2022-06-22 11:43:09.589128
# Unit test for function mandatory
def test_mandatory():
    assert mandatory(True) is True
    assert mandatory(False) is False
    assert mandatory('foobar') == 'foobar'
    assert mandatory(10) == 10
    assert mandatory(0) == 0

    try:
        mandatory(None)
        assert False
    except AnsibleFilterError:
        assert True

    try:
        mandatory('')
        assert False
    except AnsibleFilterError:
        assert True

    try:
        mandatory('', msg='foobar')
        assert False
    except AnsibleFilterError:
        assert True



# Generated at 2022-06-22 11:43:14.661359
# Unit test for function mandatory
def test_mandatory():
    # Undefined:
    assert mandatory(AnsibleUndefined()) == AnsibleUndefined()
    assert mandatory(AnsibleUndefined(name='foo')) == AnsibleUndefined()
    assert mandatory(AnsibleUndefined(name='bar'), msg='baz') == AnsibleUndefined()
    # Defined:
    assert mandatory('foo') == 'foo'



# Generated at 2022-06-22 11:43:25.648297
# Unit test for function mandatory
def test_mandatory():
    # test that scope variables work
    assert mandatory(dict(a=1)) == 1
    assert mandatory(dict(a=dict(b=2)), msg="test_mandatory") == 2

    # test that jinja2.Undefined works
    assert mandatory(Undefined("foo")) == Undefined("foo")
    # test that jinja2.Undefineds with undefined_name works
    assert mandatory(Undefined("foo")) == Undefined("foo")
    assert mandatory(Undefined("foo")) == Undefined("foo")
    assert mandatory(Undefined("foo")) == Undefined("foo")

    # test that jinja2.Undefined with error messages works
    msg = "test_mandatory_error_message"

# Generated at 2022-06-22 11:43:40.777947
# Unit test for function regex_search
def test_regex_search():
    # backrefs
    value = 'backref_foo'
    regex = '(?P<b>\w+)_(?P<a>\w+)'
    assert regex_search(value, regex, '\\2\\g<a>') == 'foo_foo'

    # support ignorecase/multiline
    assert regex_search('fOo','(?P<g>foo)', ignorecase=True) == 'fOo'
    assert regex_search('fOo\nfoo','(?P<g>foo)', multiline=True) == 'foo'

    # support multiple backrefs
    assert regex_search('fOo','(?P<g>foo)', '\\g<g>\\g<g>') == ['fOofOo']



# Generated at 2022-06-22 11:43:43.583682
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'out': {'stdout_lines': ['msg', 'msg2']}}) == """{
    "out": {
        "stdout_lines": [
            "msg",
            "msg2"
        ]
    }
}"""


# Generated at 2022-06-22 11:43:54.153710
# Unit test for function to_yaml
def test_to_yaml():
    value = {
        'some_binary_value': b'\xe2\x9c\x93',  # b'\xe2\x9c\x93' == u'\u2713' == checkmark
        'some_unicode_value': u'\xf0\x9f\x8c\xa6',  # u'\xf0\x9f\x8c\xa6' == smiley-planet
    }
    expected = '''{some_binary_value: !!binary |-
  4pyT
some_unicode_value: \xf0\x9f\x8c\xa6}'''
    result = to_yaml(value)
    assert result == expected


# Generated at 2022-06-22 11:44:03.913582
# Unit test for function regex_search
def test_regex_search():
    print("Unit test for function regex_search(value, regex, args, kwargs)")
    str = '''This is some text
with multiple lines
of text
it also has a 0 which we don't want
'''
    # Note: Result is list, not string
    result = [x for x in regex_search(str, r'^\S+', '\\g<0>', ignorecase=False, multiline=True)]
    print("Result: %s" % result)
    if result == ['This']:
        print("Unit test for function regex_search PASS")
    else:
        print("Unit test for function regex_search FAIL")
    print()



# Generated at 2022-06-22 11:44:15.729163
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('<html><head><title>Test</title></head></html>', '(TITLE)', '\\g<1>') == 'TITLE'
    assert regex_search('<html><head><title>Test</title></head></html>', '(TITLE)', '\\g<1>', ignorecase=True) == 'TITLE'
    assert regex_search('<html><head><title>Test</title></head></html>', '(?i)(TITLE)', '\\g<1>') == 'TITLE'
    assert regex_search('<html><head><title>Test</title></head></html>', '(TITLE)', '\\1') == 'TITLE'

# Generated at 2022-06-22 11:44:27.818756
# Unit test for function subelements
def test_subelements():
    # Test a dict object
    obj = {
        "name": "alice",
        "groups": ["wheel"],
        "authorized": ["/tmp/alice/onekey.pub"],
    }
    result = subelements(obj, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

    # Test a list with dict objects
    obj = [{"name": "bob", "groups": ["users"], "authorized": ["/tmp/alice/onekey.pub"]},
           {"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = subelements(obj, 'groups')

# Generated at 2022-06-22 11:44:30.786048
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml([1,2,3], output=None) == '''- 1
- 2
- 3
'''



# Generated at 2022-06-22 11:44:42.908350
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace(r'foo', r'f(o)', r'a\1b') == "aob"
    assert regex_replace(r'foo', r'f(o)', r'a\1b', ignorecase=True) == "aob"
    assert regex_replace(r'FOO', r'f(o)', r'a\1b', ignorecase=True) == "aob"
    assert regex_replace(r'FOO', r'f(o)', r'a\1b', ignorecase=False) == "FOO"
    assert regex_replace(r'FOO', r'f(o)', r'a\1b', ignorecase=1) == "aob"

# Generated at 2022-06-22 11:44:47.221116
# Unit test for function regex_search
def test_regex_search():
    text = 'this is a test string'
    match = regex_search(text, r'^\w+')
    assert match == 'this'
    match = regex_search(text, r'^\w+', '\\g<0>')
    assert match == 'this'
    match = regex_search(text, r'(\w+) is a (.+) string', '\\g<1>', '\\g<2>')
    assert match == ['this', 'test']



# Generated at 2022-06-22 11:44:56.049328
# Unit test for function regex_search
def test_regex_search():
    t = '''
    # IPADDR3: 192.168.1.1/255.255.255.0 :192.168.1.254
    '''

    # Test with no index
    assert regex_search(t, r'\bIPADDR3\s*:\s*([\d.]+)') == '192.168.1.1'

    # Test with index
    assert regex_search(t, r'\bIPADDR3\s*:\s*([\d.]+)', '\\1') == ['192.168.1.1']
    assert regex_search(t, r'\bIPADDR3\s*:\s*([\d.]+)', '\\1', '\\g<mask>') == ['192.168.1.1', '255.255.255.0']
    assert regex_

# Generated at 2022-06-22 11:45:18.781684
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("Hello, my name is John Doe", r'John(?P<lastname>\w+)', '\\g<lastname>') == ['Doe']
    assert regex_search("Hello, my name is John Doe", r'John(?P<lastname>\w+)', '\\g<lastname>', '\\1') == ['Doe', 'Doe']
    assert regex_search("Hello, my name is John Doe", r'John(?P<lastname>\w+)', '\\1', '\\g<lastname>') == ['Doe', 'Doe']
    assert regex_search("Hello, my name is John Doe", r'John(?P<lastname>\w+)', '\\1', '\\2') == ['Doe', '']


# Generated at 2022-06-22 11:45:32.040962
# Unit test for function comment
def test_comment():
    expected = (
        "# This is a plain text comment\n"
        "# This line is also a comment\n"
        "# You can have as many lines as you like\n"
        "# All lines will have the same prefix\n"
        "# It is a good practice to have a blank line at the end\n"
        "\n"
    )
    text = (
        "This is a plain text comment\n"
        "This line is also a comment\n"
        "You can have as many lines as you like\n"
        "All lines will have the same prefix\n"
        "It is a good practice to have a blank line at the end\n"
        "\n"
    )
    assert expected == comment(text)


# Generated at 2022-06-22 11:45:44.465323
# Unit test for function regex_search
def test_regex_search():
    string = "string!@#$%^&*()_+"
    key_regex = r'[a-zA-Z0-9!@#$%^&*()_+]+'
    assert regex_search(string, key_regex) == string

    regex = r'[a-zA-Z0-9]*'
    assert regex_search(string, regex, '\\g<1>') == 'string'

    regex = r'(?P<group1>[a-zA-Z0-9]*).*(?P<group2>[!@#$%^&*()_+]+)'
    assert regex_search(string, regex, '\\g<group1>', '\\g<group2>') == ['string', '!@#$%^&*()_+']


# Generated at 2022-06-22 11:45:46.565395
# Unit test for function comment
def test_comment():
    # Print to stdout
    #print comment("Ceci est un test", style='c')
    pass



# Generated at 2022-06-22 11:45:52.933436
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace("sed is fun", pattern="sed", replacement="awk") == "awk is fun"
    assert regex_replace("sed is fun", pattern="SED", replacement="awk", ignorecase=True) == "awk is fun"
    assert regex_replace("this is\nmultiline\ninput", pattern="^(.*)", replacement="last line: \\1", multiline=True) == "last line: this is\nlast line: multiline\nlast line: input"



# Generated at 2022-06-22 11:46:05.647324
# Unit test for function comment
def test_comment():
    # Start with the plain
    assert comment("The cake is a lie") == '# The cake is a lie'
    assert comment("The cake is a lie", style='plain') == '# The cake is a lie'
    assert comment("The cake is a lie", decoration='// ') == '// The cake is a lie'
    assert comment("The cake is a lie", decoration='### ') == '### The cake is a lie'
    assert comment("The cake is a lie", decoration='=== ') == '=== The cake is a lie'
    # Erlang
    assert comment("The cake is a lie", style='erlang') == '% The cake is a lie'
    assert comment("The cake is a lie", style='erlang', decoration=';;;') == ';;; The cake is a lie'
    # C-like

# Generated at 2022-06-22 11:46:12.873177
# Unit test for function regex_search
def test_regex_search():
    value = "test ab cd"
    assert regex_search(value, "ab") == 'ab'
    value = "test ab cd ab"
    assert regex_search(value, "ab") == 'ab'
    value = "test ab cd"
    assert regex_search(value, r'ab\s+cd') == 'ab cd'
    assert regex_search(value, r'ab\s+cd', '\\g<0>') == ['ab cd']
    assert regex_search(value, r'(ab)\s+(cd)', '\\g<2>') == ['ab', 'cd']
    assert regex_search(value, r'(ab)\s+(cd)', '\\2') == ['ab', 'cd']

# Generated at 2022-06-22 11:46:23.035684
# Unit test for function regex_search
def test_regex_search():
    str = "resource r1 { type: 'mytype' }"
    assert regex_search(str, '(resource \S+)|(type:\s*(?:\'|\")(.+)(?:\'|\"))') == "resource r1"
    str = "resource r1 { type: 'mytype' }"
    assert regex_search(str, '(resource \S+)|(type:\s*(?:\'|\")(.+)(?:\'|\"))', ignorecase=True) == "resource r1"
    str = "resource r1 { type: 'mytype' }"
    assert regex_search(str, '(resource \S+)|(type:\s*(?:\'|\")(.+)(?:\'|\"))', '\\g<1>') == "r1"

# Generated at 2022-06-22 11:46:30.590023
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    environment = Environment()
    assert do_groupby(environment, [{'name': 'foo'}, {'name': 'bar'}, {'name': 'foo'}],
                      attribute=('name')) == [('foo', [{'name': 'foo'}, {'name': 'foo'}]),
                                              ('bar', [{'name': 'bar'}])]


# Ansible common filters

# Generated at 2022-06-22 11:46:37.241108
# Unit test for function do_groupby
def test_do_groupby():
    assert do_groupby([
        {'name': 'a', 'uid': 1000},
        {'name': 'a', 'uid': 1001},
        {'name': 'b', 'uid': 1002}
    ], 'name') == [
        ('a', [{'name': 'a', 'uid': 1000}, {'name': 'a', 'uid': 1001}]),
        ('b', [{'name': 'b', 'uid': 1002}])
    ]



# Generated at 2022-06-22 11:46:57.388786
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('hello world', '....o.*') == 'hello world'
    assert regex_search('hello world', '....o.*', '\\g<0>') == 'hello world'
    assert regex_search('hello world', '....o.*', '\\2') is None
    assert regex_search('hello world', '(... ).*', '\\g<1>') == 'wor'
    assert regex_search('hello world', '(... ).*', '\\g<0>', '\\g<1>') == ['hello world', 'wor']
    assert regex_search('hello world', '(... ).*', '\\g<0>', '\\1') == ['hello world', 'wor']
    assert regex_search('hello world', 'h(... ).*', '\\g<1>') == 'ell'
    assert regex

# Generated at 2022-06-22 11:47:04.712622
# Unit test for function rand
def test_rand():
    env = ansible.utils.unsafe_proxy.AnsibleUnsafeText('test_env')
    # test random from list
    data = list(range(0, 6))
    for i in range(0, 10):
        assert rand(env, data) in data
    # test random from integer range
    for i in range(0, 10):
        assert rand(env, 10) in range(0, 10)
        assert rand(env, 10, seed='anything') in range(0, 10)
        assert rand(env, 10, 1) in range(1, 10)
        assert rand(env, 10, 1, seed='anything') in range(1, 10)
        assert rand(env, 10, 1, 3) in range(1, 10, 3)
        assert rand(env, 10, 1, 3, seed='anything')

# Generated at 2022-06-22 11:47:15.182458
# Unit test for function do_groupby
def test_do_groupby():
    data = [{'name': 'Alice', 'last_name': 'Chen'},
            {'name': 'Bob', 'last_name': 'Dole'},
            {'name': 'Alice', 'last_name': 'Anderson'},
            {'name': 'Cathy', 'last_name': 'Chen'}]
    grouped = do_groupby(data, 'name')

    expected = [('Alice', [('Alice', 'Chen'), ('Alice', 'Anderson')]),
                ('Bob', [('Bob', 'Dole')]),
                ('Cathy', [('Cathy', 'Chen')])]
    assert expected == grouped



# Generated at 2022-06-22 11:47:18.822493
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    '''
    ensure NoID is not used when converting to yaml
    '''
    assert to_nice_yaml({'id': '123'}) == to_yaml({'id': '123'})



# Generated at 2022-06-22 11:47:28.435451
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('abc123', r'[0-9]+', r'\g<0>-suffix', False, False) == 'abc123-suffix'
    assert regex_replace('abc123', r'[0-9]+', r'\g<0>-suffix', False, True) == 'abc123-suffix'
    assert regex_replace('abc123', r'[0-9]+', r'\g<0>-suffix', True, False) == 'abc123-suffix'
    assert regex_replace('abc123', r'[0-9]+', r'\g<0>-suffix', True, True) == 'abc123-suffix'



# Generated at 2022-06-22 11:47:30.198665
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({'foo': 123}) == '''{foo: 123}'''



# Generated at 2022-06-22 11:47:42.427809
# Unit test for function randomize_list
def test_randomize_list():
    ''' randomize_list() should return a list with the same elements as the original list.
        It should return the list in a different order from the original list.
        It should return the same list if the original list's contents are changed.
    '''
    seed = 'abc'
    item_list = ['a', 'b', 'c', 'd', 'e']
    assert randomize_list(item_list, seed) == ['c', 'b', 'a', 'e', 'd']
    assert randomize_list(item_list, seed) == ['c', 'b', 'a', 'e', 'd']
    item_list.append('f')
    assert randomize_list(item_list, seed) == ['c', 'b', 'a', 'e', 'd', 'f']



# Generated at 2022-06-22 11:47:51.904919
# Unit test for function get_hash
def test_get_hash():
    assert get_hash(b'foo', hashtype='md5') == 'acbd18db4cc2f85cedef654fccc4a4d8'
    assert get_hash(b'foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'
    assert get_hash(b'foo', hashtype='sha256') == '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae'



# Generated at 2022-06-22 11:48:00.435458
# Unit test for function mandatory
def test_mandatory():
    try:
        mandatory(123)
    except AnsibleFilterError:
        assert False, "unexpected error"
    try:
        mandatory()
    except AnsibleFilterError:
        assert True, "expected error: mandatory()"
    try:
        mandatory(None)
    except AnsibleFilterError:
        assert False, "unexpected error: mandatory(None)"
    try:
        mandatory(None, "fake error")
    except AnsibleFilterError:
        assert True, "expected error: mandatory(None, 'fake error')"
    try:
        mandatory(123, "fake error")
    except AnsibleFilterError:
        assert False, "unexpected error: mandatory(123, 'fake error')"



# Generated at 2022-06-22 11:48:12.781664
# Unit test for function subelements
def test_subelements():
    obj1 = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    obj2 = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]},
            {"name": "bob", "groups": ["admin", "wheel", "users"], "authorized": ["/tmp/bob/.ssh/id_rsa.pub"]}]

# Generated at 2022-06-22 11:48:34.689462
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    test_list = [
        {'a': [1, 2, 3, [4, 5], 7]},
        {'b': 'test', 'c': None, 'd': {'e': 'f'}},
        ['test1', 2, 3, {'four': 'test'}],
    ]

    # This is what each of the above items should look like when formatted
    test_list_formatted = [
        """a:
- 1
- 2
- 3
-
- - 4
  - 5
- 7
""",
        """b: test
c: null
d:
  e: f
""",
        """- test1
- 2
- 3
- four: test
""",
    ]


# Generated at 2022-06-22 11:48:41.477107
# Unit test for function strftime
def test_strftime():
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    class TestStringMethods(unittest.TestCase):
        def test_format_time(self):
            self.assertEqual(strftime('%Y-%m-%d %H:%M:%S', '1443193208'), '2015-09-24 15:33:28')

    return unittest.main()



# Generated at 2022-06-22 11:48:53.261068
# Unit test for function comment
def test_comment():
    import random
    import string
    import sys
    # Get number of arguments
    argc = len(sys.argv)
    # Set default test parameters
    options = {
        'style': 'plain',
        'decoration': '# ',
        'newline': '\n',
        'beginning': '',
        'prefix': '',
        'prefix_count': 1,
        'decoration': '',
        'postfix': '',
        'postfix_count': 1,
        'end': ''
    }
    n_tests = 10
    if argc > 1:
        if sys.argv[1] == '-n':
            if argc > 2:
                n_tests = int(sys.argv[2])
    # Set random default text

# Generated at 2022-06-22 11:49:00.018214
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml([1, 2, 3]) == "---\n- 1\n- 2\n- 3\n"
    assert to_yaml({'k1': 'v1', 'k2': 'v2'}) == "---\nk1: v1\nk2: v2\n"
    assert to_yaml("some string") == "--- some string\n"

# Generated at 2022-06-22 11:49:02.945843
# Unit test for function get_hash
def test_get_hash():
  assert get_hash('my data', 'sha1') == 'c79737b1aba079efc9d8a8c20fde6f1671a4dca6'



# Generated at 2022-06-22 11:49:06.122875
# Unit test for function strftime
def test_strftime():
    strftime('%Y-%m-%d', '1504444255.0') == '2017-09-04'

# Generated at 2022-06-22 11:49:16.753282
# Unit test for function mandatory
def test_mandatory():
    from jinja2 import Undefined
    from ansible.parsing.yaml.objects import AnsibleUnicode
    assert mandatory(Undefined) is Undefined
    assert mandatory(AnsibleUnicode(u'foo')) == u'foo'
    assert mandatory(AnsibleUnicode('')) == u''
    assert mandatory(2) == 2
    try:
        mandatory(Undefined, 'XYZ')
    except AnsibleFilterError as e:
        assert e.message == 'XYZ'
    try:
        mandatory(Undefined)
    except AnsibleFilterError as e:
        assert e.message == "Mandatory variable not defined."





# Generated at 2022-06-22 11:49:27.735997
# Unit test for function to_yaml
def test_to_yaml():
    def _check(input, expected):
        actual = to_yaml(input)
        assert expected == actual, '''
# input:
{0}
# expected:
{1}
# actual:
{2}
'''.format(input, expected, actual)

    _check({"a": "b"}, '{a: b}\n')
    _check({"a": "b", "c": "d"}, '{a: b, c: d}\n')
    _check(["a", "b"], '- a\n- b\n')
    _check(["a", {"b": "c"}], '- a\n- {b: c}\n')
    _check(["a", "b\nc"], "- a\n- 'b\nc'\n")

# Generated at 2022-06-22 11:49:30.633800
# Unit test for function get_hash
def test_get_hash():
  assert get_hash('test') == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'


# Generated at 2022-06-22 11:49:41.180876
# Unit test for function rand
def test_rand():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class TestModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            raise AnsibleError(kwargs['msg'])

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])

# Generated at 2022-06-22 11:50:03.915128
# Unit test for function do_groupby
def test_do_groupby():
    from ansible.template import Environment
    env = Environment()
    fn = env.tests['do_groupby']
    class MyObject(object):
        def __init__(self, abc):
            self.abc = abc
    assert fn([MyObject('def'), MyObject('def'), MyObject('ghi')], attribute='abc') == [('def', [('abc', 'def')]), ('ghi', [('abc', 'ghi')])]
    assert fn([MyObject('def'), MyObject('ghi'), MyObject('ghi')], attribute='abc') == [('def', [('abc', 'def')]), ('ghi', [('abc', 'ghi'), ('abc', 'ghi')])]

# Generated at 2022-06-22 11:50:16.479668
# Unit test for function regex_search
def test_regex_search():
    ''' Test function regex_search '''

    # Test with bad parameter values
    try:
        regex_search('a', 'b', 'fail')
    except AnsibleFilterError:
        pass
    else:
        raise AssertionError('Expected AnsibleFilterError')

    # Test with missing match
    assert not regex_search('a', 'b')

    # Test with single match
    assert regex_search('abc', 'abc') == 'abc'

    # Test with single match and single group
    assert regex_search('abcd', '(ab)(cd)', '\\g<1>') == 'ab'

    # Test with single match and multiple groups
    assert regex_search('abcd', '(ab)(cd)', '\\g<1>', '\\g<2>') == ['ab', 'cd']

    # Test with single
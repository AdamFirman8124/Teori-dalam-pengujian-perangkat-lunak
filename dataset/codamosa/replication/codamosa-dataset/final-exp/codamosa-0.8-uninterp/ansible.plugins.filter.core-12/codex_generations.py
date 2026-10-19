

# Generated at 2022-06-22 11:40:40.929496
# Unit test for function fileglob
def test_fileglob():
    ''' fileglob should return a list of files for glob '''
    listfiles = fileglob('./test/files/*')
    assert './test/files/file1' in listfiles



# Generated at 2022-06-22 11:40:49.646987
# Unit test for function extract
def test_extract():
    """ Unit tests for extract()
    :return:
    """
    # import pdb; pdb.set_trace()
    d = {
        "key1": "value1",
        "key2": {
            "key3": "value2",
            "key4": {
                "key5": "value3",
                "key6": "value4"
            },
            "keyA": {
                "keyB": "value5",
                "keyC": [
                    {"keyD": "value6"},
                    {"keyE": "value7"}
                ]
            }
        }
    }

    result = extract('key1', d)
    assert result == 'value1'

    result = extract('key2.key3', d)
    assert result == 'value2'


# Generated at 2022-06-22 11:41:02.244596
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml({"a": 1, "b": 2}) == "a: 1\nb: 2\n", 'failed to transform dict to yaml'
    assert to_yaml({"a": 1, "b": 2}, default_flow_style=False) == "a: 1\nb: 2\n", 'failed to transform dict to yaml'
    assert to_yaml({"mylist": [1,2,3]}) == "mylist:\n- 1\n- 2\n- 3\n", 'failed to transform list to yaml'
    assert to_yaml({"mylist": [1,2,3]}, default_flow_style=False) == "mylist:\n- 1\n- 2\n- 3\n", 'failed to transform list to yaml'



# Generated at 2022-06-22 11:41:12.698741
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    assert mandatory(1) == 1
    assert mandatory(0) == 0
    assert mandatory(Undefined('foo')) == 1

    try:
        assert mandatory(Undefined('foo'), msg="bad stuff there") == 1
    except AnsibleFilterError as e:
        assert "bad stuff there" == to_text(e)

    try:
        assert mandatory(Undefined('foo')) == 1
    except AnsibleFilterError as e:
        assert "Mandatory variable 'foo' not defined." == to_text(e)



# Generated at 2022-06-22 11:41:21.009934
# Unit test for function mandatory
def test_mandatory():
    from jinja2.environment import Environment
    env = Environment()
    env.filters['mandatory'] = mandatory
    env.globals['zoo'] = "zoo"
    assert env.from_string('{{ zoo | mandatory }}').render() == 'zoo'
    assert env.from_string('{{ non_existant_var | mandatory }}').render() == ''
    try:
        env.from_string('{{ zoo | mandatory("not defined") }}').render()
    except AnsibleFilterError:
        pass
    else:
        raise AssertionError('Exception expected')



# Generated at 2022-06-22 11:41:22.250701
# Unit test for function extract
def test_extract():
    assert extract(None, None, {'a': {'b': {'c': None}}}, ['b', 'c']) is None



# Generated at 2022-06-22 11:41:35.449734
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('python python python', 'py') == 'py'
    assert regex_search('python python python', 'py', '\\g<1>') == 'py'
    assert regex_search('python python python', 'py', '\\1') == ['py']
    assert regex_search('python python python', 'py', '\\1', '\\g<1>') == ['py', 'py']
    assert regex_search('python python python', 'py', '\\g<1>', '\\1') == ['py', 'py']
    assert regex_search('python python python', 'py', '\\g<1>', '\\2') == ['py', None]
    assert regex_search('python python python', 'py', '\\1', '\\2') == ['py', None]

# Generated at 2022-06-22 11:41:45.689837
# Unit test for function extract
def test_extract():
    assert extract('bar', {'foo': {'bar': 'baz'}}, None) == 'baz'
    assert extract('bar', ['baz'], None) == None
    assert extract('bar', ['baz'], 'foo') == 'foo'
    assert extract('bar', 'foo', None) == None
    assert extract('bar', 'foo', 'bar') == 'bar'
    assert extract('bar', 'foo', 'foo') == None
    assert extract('bar', '', 'foo') == None
    assert extract('bar', '', 'foo', 'bar') == None



# Generated at 2022-06-22 11:41:55.424573
# Unit test for function fileglob
def test_fileglob():
    assert fileglob('/etc/*conf') == ['/etc/host.conf', '/etc/hosts', '/etc/hosts.allow', '/etc/hosts.deny', '/etc/mime.types', '/etc/nsswitch.conf', '/etc/protocols', '/etc/services']
    assert fileglob('/etc/h*') == ['/etc/host.conf', '/etc/hosts', '/etc/hosts.allow', '/etc/hosts.deny']
    assert fileglob('/etc/nosuchfileglob*') == []


# Generated at 2022-06-22 11:42:06.799390
# Unit test for function do_groupby
def test_do_groupby():

    class MockEnvironment(jinja2.Environment):
        def getitem(self, obj, argument):
            return obj[argument]

        def is_undefined(self, obj):
            return False

        def getattr(self, obj, argument):
            return getattr(obj, argument)

    # List of tuples
    data = [('foo', 1), ('bar', 2), ('baz', 3)]

    # Create a jinja env
    env = MockEnvironment()

    # Run the do_groupby function
    results = do_groupby(env, data, attribute=0)

    for result in results:
        assert isinstance(result, tuple)
        assert isinstance(result[0], str)
        assert isinstance(result[1], list)


# Generated at 2022-06-22 11:42:17.304763
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('nonsense', '^(n[o|e]n)sense$') == 'nonsense'
    assert regex_search('nonsense', '^(n[o|e]n)se(ns)e$', '\\2') == 'ns'
    assert regex_search('nonsense', '^(?P<LEADING>(n[o|e]n))se(ns)e$', '\\g<LEADING>') == 'nonsense'



# Generated at 2022-06-22 11:42:20.760814
# Unit test for function get_hash
def test_get_hash():
    data = 'test string'
    hashtype = 'sha1'
    assert get_hash(data, hashtype) == hashlib.sha1(data.encode('utf-8')).hexdigest()



# Generated at 2022-06-22 11:42:23.777980
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml([{'a': 1, 'b': 2}]) == '''- a: 1
  b: 2
'''



# Generated at 2022-06-22 11:42:34.430145
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('123', '\d+') == '123'
    assert regex_search('123', '\d+', '\\1') == ['123', '123']
    assert regex_search('123', '\d+', '\\g<0>') == ['123', '123']
    assert regex_search('123', '\d+', '\\g<1>') == ['123', '123']
    assert regex_search('123', '\d+', '\\g<a>') == ['123']
    assert regex_search('123', '\d+', '\\g<a>', '\\1') == ['123', '123']
    assert regex_search('abc', 'a(.+?)c') == 'abc'

# Generated at 2022-06-22 11:42:37.167553
# Unit test for function to_yaml
def test_to_yaml():
    # Can't use isinstance for comparing classes in different modules
    class DummyException(Exception):
        pass

    val = DummyException
    try:
        to_yaml(val)
    except AnsibleFilterError as e:
        assert isinstance(e.exception, DummyException)



# Generated at 2022-06-22 11:42:45.924206
# Unit test for function fileglob
def test_fileglob():
    expected = [
        '__init__.pyc',
        '__pycache__',
        'docs',
        'filter_plugins',
        'lib',
        'logger.pyc',
        'plugin_docs',
        'plugins',
        'README.md',
        'utils',
    ]
    result = fileglob('*')
    assert result == expected, "Expected %s, got %s" % (expected, result)



# Generated at 2022-06-22 11:42:56.195544
# Unit test for function mandatory
def test_mandatory():
    from jinja2.environment import Environment

    env = Environment()
    env.filters['mandatory'] = mandatory

    template = env.from_string(u"{{ undefined | mandatory }}")
    try:
        template.render()
    except AnsibleFilterError as e:
        if "Mandatory variable 'undefined' not defined" not in to_text(e):
            raise AssertionError("Unexpected template error thrown %s" % to_text(e))
        else:
            pass
    else:
        raise AssertionError("No template error was thrown")

    template = env.from_string(u"{{ undefined | mandatory('error message') }}")
    try:
        template.render()
    except AnsibleFilterError as e:
        if "error message" not in to_text(e):
            raise Assertion

# Generated at 2022-06-22 11:43:04.750369
# Unit test for function regex_search
def test_regex_search():
    assert regex_search(value='My name is John Doe', regex=r'John\sDoe') == 'John Doe'
    assert regex_search(value='The number is 123', regex=r'\d+') == '123'
    assert regex_search(value='The number is 123', regex=r'\d+', ignorecase=True) == '123'
    assert regex_search(value='The number is 123', regex=r'\d+', ignorecase=True, multiline=True) == '123'
    assert regex_search(value='My name is John Doe', regex=r'John\sDoe', groups=['\\g<1>']) == 'John Doe'
    assert regex_search(value='The number is 123', regex=r'(\d+)', groups=['\\1']) == '123'

# Generated at 2022-06-22 11:43:16.769285
# Unit test for function mandatory
def test_mandatory():
    from jinja2.exceptions import UndefinedError
    from ansible.errors import AnsibleFilterError

    try:
        mandatory(None)
    except AnsibleFilterError as e:
        assert 'Mandatory variable' in e.message
    try:
        mandatory([])
    except AnsibleFilterError as e:
        assert 'Mandatory variable' in e.message
    try:
        mandatory('')
    except AnsibleFilterError as e:
        assert 'Mandatory variable' in e.message
    try:
        mandatory(undefined)
    except UndefinedError:
        pass
    try:
        mandatory(undefined, 'hello')
    except AnsibleFilterError as e:
        assert 'hello' in e.message
    assert mandatory('hello') == 'hello'

# Generated at 2022-06-22 11:43:21.829229
# Unit test for function combine
def test_combine():
    # simple dicts
    assert combine({'foo': 'bar'}) == {'foo': 'bar'}
    assert combine({'foo': 'bar'}, {'biz': 'baz'}) == {'foo': 'bar', 'biz': 'baz'}
    assert combine({'foo': 'bar'}, {'foo': 'notbar'}) == {'foo': 'notbar'}
    assert combine({'foo': 'bar'}, {'foo': 'notbar', 'biz': 'baz'}) == {'foo': 'notbar', 'biz': 'baz'}
    assert combine({'foo': 'bar'}, {'biz': 'baz'}, {'foo': 'notbar'}) == {'foo': 'notbar', 'biz': 'baz'}

    # nested dicts

# Generated at 2022-06-22 11:43:35.094713
# Unit test for function regex_escape
def test_regex_escape():
    # Test input and expected output
    test_input = r'abc$def.001'
    test_output = 'abc\\$def\\.001'

    assert regex_escape(test_input) == test_output



# Generated at 2022-06-22 11:43:46.921234
# Unit test for function comment
def test_comment():
    assert comment("text", style='plain') == '# text'
    assert comment("text", style='plain', decoration='// ') == '// text'
    assert comment("text", style='c') == '// text'
    assert comment("text", style='erlang') == '% text'
    assert comment("hello", style='plain', beginning='---', end='---') == '---\n# hello\n---'
    assert comment("hello", style='erlang', beginning='---', end='---') == '---\n% hello\n---'
    assert comment("hello", style='plain', prefix='###', postfix='###', prefix_count=2) == '# ###\n# ###\n# hello'

# Generated at 2022-06-22 11:43:59.487725
# Unit test for function comment
def test_comment():
    assert (comment('foo\nbar') == '# foo\n# bar')
    assert (comment('foo\nbar', newline='\r\n') == '# foo\r\n# bar')
    assert (comment('foo\nbar', decoration='// ') == '// foo\n// bar')
    assert (comment('foo\nbar', decoration='// ',
                    prefix='',
                    prefix_count=0) == '// foo\n// bar')
    assert (comment('foo\nbar', decoration='// ',
                    prefix='\n',
                    prefix_count=0) == '\n// foo\n// bar')
    assert (comment('foo\nbar', decoration='// ',
                    prefix='\n',
                    prefix_count=1) == '\n// foo\n// bar')

# Generated at 2022-06-22 11:44:00.520749
# Unit test for function mandatory
def test_mandatory():
    assert mandatory("foo") == "foo"



# Generated at 2022-06-22 11:44:12.132745
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('asdf', '\w{4}') == 'asdf'
    assert regex_search('asdf', '\w{4}', '\\2') == 's'
    assert regex_search('asdf', '\w{4}', '\\g<0>', '\\g<1>', '\\g<2>') == ['asdf', 'a', 's']
    assert regex_search('asdf', '\w{4}', '\\2', '\\g<2>') == ['s', 's']
    assert regex_search('asdf', '\w{4}', '\\1', '\\g<2>') == None



# Generated at 2022-06-22 11:44:19.274896
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace('123123abc123', '123', 'ZZZ') == 'ZZZZZZabcZZZ'
    assert regex_replace('one1two2three3', r'(\d)', r'Z\1Y') == 'oneZ1YtwoZ2YthreeZ3Y'



# Generated at 2022-06-22 11:44:25.245832
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml(dict(a=5, b="foo")) == "a: 5\nb: 'foo'\n"
    assert to_yaml(dict(a=5, b="foo"), default_flow_style=False) == "a: 5\nb: foo\n"
    assert to_yaml([1, 2, "foo"]) == "- 1\n- 2\n- foo\n"



# Generated at 2022-06-22 11:44:31.727217
# Unit test for function mandatory
def test_mandatory():
    # test msg override
    try:
        mandatory(None, 'Bag of shells')
        assert False, 'failed to enforce msg'
    except AnsibleFilterError as e:
        assert 'Bag' in e.message

    # test standard msg
    try:
        mandatory(None)
        assert False, 'failed to enforce msg'
    except AnsibleFilterError as e:
        assert 'Mandatory' in e.message

    # validate no exception raised on full value
    assert mandatory('Happy little trees') == 'Happy little trees'



# Generated at 2022-06-22 11:44:43.746746
# Unit test for function mandatory
def test_mandatory():
    assert mandatory("a") == "a"
    assert mandatory("a", "msg") == "a"

    from jinja2.runtime import Undefined
    from ansible.template import Jinja2Template
    from ansible.template.safe_eval import AnsibleUndefined

    try:
        mandatory(Jinja2Template("{{ undefined | mandatory }}").apply())
    except AnsibleFilterError as err:
        assert to_text(err) == "Mandatory variable not defined."

    try:
        mandatory(Jinja2Template("{{ undefined | mandatory(msg='custom msg') }}").apply())
    except AnsibleFilterError as err:
        assert to_text(err) == "custom msg"


# Generated at 2022-06-22 11:44:49.373127
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert to_nice_yaml({"a": "b"}) == "---\na: b\n"  # default indent=4 works
    assert to_nice_yaml({"a": "b"}, indent=2) == "---\n  a: b\n"  # indent=2 works



# Generated at 2022-06-22 11:45:15.987746
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment
    from jinja2.runtime import StrictUndefined
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    env = Environment(undefined=StrictUndefined)
    env.filters['groupby'] = do_groupby

    # Test conversion of groupby output with jinja2 <2.9.0
    e = lambda s: to_native(env.from_string(s).render().decode('utf-8'))
    s = '{{ [{ "foo": "1", "bar": "a" }, { "foo": "2", "bar": "b"}] | groupby("foo") | list | to_json }}'

# Generated at 2022-06-22 11:45:23.454792
# Unit test for function regex_search
def test_regex_search():
    string = "ansible"
    regex_pattern = "^ansible"
    result = regex_search(string, regex_pattern, '\\g<0>')
    assert result == string
    pattern_group_name = "ansi"
    regex_pattern = "(?P<%s>ansible)" % pattern_group_name
    result = regex_search(string, regex_pattern, "\\g<%s>" % pattern_group_name)
    assert result == string
# End of unit test



# Generated at 2022-06-22 11:45:34.495134
# Unit test for function to_yaml
def test_to_yaml():
    assert to_yaml(dict(a=5, b=6)) == '{a: 5, b: 6}\n'
    assert to_yaml(dict(a=5, b=6), default_flow_style=True) == '{a: 5, b: 6}\n'
    assert to_yaml(dict(a=5, b=6), default_flow_style=False) == 'a: 5\nb: 6\n'
    assert to_yaml(dict(a=5, b=[1, 2, 3])) == '{a: 5, b: [1, 2, 3]}\n'
    assert to_yaml(dict(a=5, b=[1, 2, 3]), default_flow_style=True) == '{a: 5, b: [1, 2, 3]}\n'


# Generated at 2022-06-22 11:45:36.947014
# Unit test for function regex_replace
def test_regex_replace():
    assert regex_replace("abcdef", "cd", "zz") == "abzzef"



# Generated at 2022-06-22 11:45:47.008444
# Unit test for function comment
def test_comment():
    assert comment('hello, world!', style='plain') == '# hello, world!'
    assert comment('hello, world!', style='erlang') == '% hello, world!'
    assert comment('hello, world!', style='c') == '// hello, world!'
    assert comment('hello, world!', style='cblock') == \
        """/*
 * hello, world!
 */"""
    assert comment('hello, world!', style='xml') == '<!-- - hello, world!-->'
    assert comment('hello, world!', style='c', prefix='/* ', postfix=' */') == \
        """/*
 * hello, world!
 */"""
    assert comment('hello, world!', style='cblock', decoration='- ', prefix='/*', postfix='*/') == \
        """/*
- hello, world!
*/"""

# Generated at 2022-06-22 11:45:59.053245
# Unit test for function regex_search
def test_regex_search():
    samples = dict(
        basic="A quick brown fox",
        ignorecase="A quick Brown fox",
        multiline="A quick\n Brown fox"
    )
    def _run(clue, value, regex, *groups):
        matches = ['basic', 'ignorecase', 'multiline']
        if clue.startswith('no'):
            matches.remove(clue[2:])
        assert regex_search(value[clue], regex, *groups) == value[clue]
        for sample in [s for s in value if s not in matches]:
            assert regex_search(value[sample], regex, *groups) == None
    _run('basic', samples, r'(?P<animal>\w+)\sbrown', '\\g<animal>')

# Generated at 2022-06-22 11:46:10.062105
# Unit test for function regex_search
def test_regex_search():
    assert regex_search("hello world", "hello (world)" ) == "world"
    assert regex_search("hello world", "hello (world)", "\\1") == ["world"]
    assert regex_search("hello world", "hello (world)", "\\g<1>") == ["world"]
    assert regex_search("hello world", "hello (world)", "\\g<1>", "\\1") == ["world", "world"]
    assert regex_search("hello world", "hello (world)", "\\2") == []
    assert regex_search("hello world", "hello (world)", "\\g<2>") == []
    assert regex_search("hello world", "hello world", "\\g<1>") == []
    assert regex_search("hello world", "hello (world)", "\\1", "\\2") == ["world"]

# Generated at 2022-06-22 11:46:21.745159
# Unit test for function regex_escape
def test_regex_escape():
    assert regex_escape(r"foo\+bar[1]") == r"foo\+bar\[1\]"
    assert regex_escape(r"foo\+bar[1]", re_type='posix_basic') == r"foo\\+bar\\[1\\]"
    assert regex_escape(r"foo\+bar[1]", re_type='posix_extended') == r"foo\+bar\[1\]"

    test_string = u"谢谢"
    assert regex_escape(test_string) == test_string
    assert regex_escape(test_string, re_type='posix_basic') == test_string
    assert regex_escape(test_string, re_type='posix_extended') == test_string



# Generated at 2022-06-22 11:46:34.429675
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('test', '^test$') == 'test'
    assert regex_search('test', '^test$', '\\g<0>') == 'test'
    assert regex_search('test', '^test$', '\\0') == 'test'
    assert regex_search('test', '(t)', '\\g<1>') == 't'
    assert regex_search('test', '(t)', '\\1') == 't'
    assert regex_search('test', '^.*$', '\\g<0>', '\\g<0>') == ['test', 'test']
    assert regex_search('test', '^(.*)$', '\\g<0>', '\\g<1>') == ['test', 'test']

# Generated at 2022-06-22 11:46:43.070919
# Unit test for function strftime
def test_strftime():
    assert strftime("%Y-%m-%d %H:%M:%S") == time.strftime("%Y-%m-%d %H:%M:%S")
    assert strftime("%Y-%m-%d %H:%M:%S", time.time()) == time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    assert strftime("%Y-%m-%d %H:%M:%S", time.time() + 60) == time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 60))

# Generated at 2022-06-22 11:46:59.173176
# Unit test for function get_hash
def test_get_hash():
    assert get_hash("data", "md5") == "1bc29b36f623ba82aaf6724fd3b16718"
    assert get_hash("data", "sha1") == "7ddf1b41e2c0869bba0fdb6747c3a440a3ea9a9c"
    assert get_hash("data", "sha256") == "73feffa4b7f6bb68e44cf984c85f6e88cbadf4b6031b7f318daa3234c6d3fad9"



# Generated at 2022-06-22 11:47:06.930077
# Unit test for function mandatory
def test_mandatory():
    try:
        mandatory('foo')
    except AnsibleFilterError as e:
        raise AssertionError("Unexpected error raised: %s" % to_native(e))
    try:
        mandatory(None)
    except AnsibleFilterError as e:
        assert 'not defined' in to_native(e)
    try:
        mandatory(None, "test")
    except AnsibleFilterError as e:
        assert to_native(e) == "test"



# Generated at 2022-06-22 11:47:20.051231
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('ansible', 'an\w{3}') == 'ansi'
    assert regex_search('ansible', '^an\w{3}') == 'ansi'
    assert regex_search('ansible', '^an\w{3}', ignorecase=True) == 'ansi'
    assert regex_search('ansible', '^an\w{3}', multiline=True) == 'ansi'
    assert regex_search('ansible', '^an\w{3}', ignorecase=True, multiline=True) == 'ansi'
    assert regex_search('ansible', '^an\w{3}', '\\g<1>') == 'an'

# Generated at 2022-06-22 11:47:25.724767
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Template
    tmpl = Template('{% set foo = [{ "a": 1, "b": 2 }, { "a": 3, "b": 4 }] %}{{ foo | groupby(attribute="a") | map(attribute="grouper") | list }}')
    assert tmpl.render() == "[(1,), (3,)]"



# Generated at 2022-06-22 11:47:36.877932
# Unit test for function regex_search
def test_regex_search():
    assert regex_search('matches', '.*t[^ ]*s') == 'matches'
    assert regex_search('matches', '.*t[^ ]*s', '\\g<0>') == ['matches']
    assert regex_search('matches', '.*t([^ ]*)s', '\\g<1>') == ['matche']
    assert regex_search('matches', '.*t([^ ]*)s', '\\1') == ['matche']
    assert regex_search('matches', '.*t([^ ]*)s', '\\g<1>', '\\1') == ['matche', 'matche']
    assert regex_search('matches', '.*t([^ ]*)s', '\\1', '\\g<1>') == ['matche', 'matche']

# Generated at 2022-06-22 11:47:49.453121
# Unit test for function do_groupby
def test_do_groupby():
    class Test1(object):
        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

        def __repr__(self):
            return 'Test1(var1=%r, var2=%r)' % (self.var1, self.var2)
    env = Environment()
    values = [Test1(1, 2), Test1(1, 3), Test1(2, 4), Test1(2, 5), Test1(3, 6)]

# Generated at 2022-06-22 11:47:53.770338
# Unit test for function comment

# Generated at 2022-06-22 11:47:58.725500
# Unit test for function strftime
def test_strftime():
    assert strftime('%H:%M', '3600.0') == "01:00"
    assert strftime('%H:%M:%S', 3600) == "01:00:00"
    assert strftime('%Y-%m-%d', 3600.0) == "1970-01-01"



# Generated at 2022-06-22 11:48:06.522358
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    assert '' == to_nice_yaml('')
    assert 'a: b' == to_nice_yaml({'a':'b'})
    assert """a:
  b:
    c: d
    e: f""" == to_nice_yaml({'a': { 'b': {'c':'d','e':'f'}}})
    assert ("""[ { "a": "b" },
  { "c": "d" },
  { "e": "f" } ]""") == to_nice_yaml([{'a':'b'},{'c':'d'},{'e':'f'}])



# Generated at 2022-06-22 11:48:12.629983
# Unit test for function randomize_list
def test_randomize_list():
    r = Random()
    r.seed(123)
    input_list = [1, 2, 3]
    shuffled_list = randomize_list(input_list, seed=123)
    assert(shuffled_list)
    assert(shuffled_list[0] == 3)
    assert(shuffled_list[1] == 1)
    assert(shuffled_list[2] == 2)



# Generated at 2022-06-22 11:48:26.075161
# Unit test for function regex_search
def test_regex_search():
    res = regex_search("foo-bar", "foo-(?P<last>.*)", "\\g<last>")
    assert res == "bar"



# Generated at 2022-06-22 11:48:33.154653
# Unit test for function regex_replace
def test_regex_replace():
    assert ('FOO' == regex_replace('bar', r'^b', 'FOO'))
    assert ('FOO' == regex_replace('baz', r'(?i)^b', 'FOO'))
    assert ('FOO' == regex_replace(u'b\xe1r', r'(?i)^b', 'FOO'))
    assert ('FOO bar' == regex_replace('bar bar', r'(?mi)^(.*)', 'FOO \\1'))



# Generated at 2022-06-22 11:48:45.684927
# Unit test for function combine
def test_combine():
    '''Test that combine function behaves as expected'''
    # recursive option testing
    d1 = dict(a=dict(b=True))
    d2 = dict(a=dict(c=True))
    d3 = dict(a=dict(d=True))
    d4 = dict(a=dict(b=False, e=True))

    assert combine(d1, d2, d3) == dict(a=dict(b=True, c=True, d=True))
    assert combine(d1, d2, d3, recursive=True) == dict(a=dict(b=True, c=True, d=True))
    assert combine(d1, d2, d3, recursive=False) == dict(a=dict(b=True))

# Generated at 2022-06-22 11:48:50.680062
# Unit test for function mandatory
def test_mandatory():
    try:
        a = None
        mandatory(a)
    except AnsibleFilterError as e:
        assert(e.message == "Mandatory variable 'None' not defined.")

    a = "hello"
    b = mandatory(a)
    assert(a == b)
    assert(b == "hello")


# Generated at 2022-06-22 11:48:57.102935
# Unit test for function randomize_list
def test_randomize_list():
    test_list = [1, 2, 3, 4, 5, 6]
    test_list_rz = randomize_list(test_list, seed=42)
    assert test_list_rz != test_list
    test_list_rz_1 = randomize_list(test_list, seed=42)
    assert test_list_rz == test_list_rz_1


# Generated at 2022-06-22 11:49:09.562274
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2 import Environment

    env = Environment()
    env.filters['do_groupby'] = do_groupby
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    from ansible.template import Templar

    t = Templar(loader=loader, variables={})

    # test with a string
    data = [
        ('foo', 'a'),
        ('bar', 'b'),
        ('foo', 'c'),
    ]
    try:
        env.from_string('''{% set grouped = data | do_groupby('0') %}''').render(data=data)
    except Exception as e:
        assert False, 'do_groupby failed with string: %s' % to_native(e)

    # test with a number

# Generated at 2022-06-22 11:49:21.617659
# Unit test for function mandatory
def test_mandatory():
    test_list = [
        {
            'input': None,
            'expected': True,
            'description': 'Passing None',
        },
        {
            'input': '',
            'expected': True,
            'description': 'Passing empty string',
        },
        {
            'input': {'key': 'value'},
            'expected': True,
            'description': 'Passing dict',
        },
        {
            'input': [],
            'expected': True,
            'description': 'Passing empty list',
        },
        {
            'input': (),
            'expected': True,
            'description': 'Passing empty tuple',
        },
    ]


# Generated at 2022-06-22 11:49:24.657269
# Unit test for function to_nice_yaml
def test_to_nice_yaml():
    test_yaml = {
        'a': 'b',
        'c': 'd'
    }
    to_nice_yaml_result = to_nice_yaml(test_yaml)
    assert to_nice_yaml_result == 'a: b\nc: d\n'



# Generated at 2022-06-22 11:49:34.001772
# Unit test for function mandatory
def test_mandatory():
    from jinja2.runtime import Undefined

    assert mandatory(1) == 1
    try:
        mandatory(Undefined())
        assert False
    except AnsibleFilterError as e:
        assert 'Mandatory variable not defined' in to_native(e)

    try:
        mandatory(Undefined(), msg="custom error")
        assert False
    except AnsibleFilterError as e:
        assert 'custom error' in to_native(e)

    try:
        mandatory(Undefined(name='foo'))
        assert False
    except AnsibleFilterError as e:
        assert "'foo' " in to_native(e)



# Generated at 2022-06-22 11:49:45.342447
# Unit test for function do_groupby
def test_do_groupby():
    from jinja2.runtime import Undefined
    environment = jinja2.Environment()
    environment.filters['groupby'] = do_groupby
    tmpl = environment.from_string("{{ hosts | groupby('osfamily') | dictsort }}")
    result = tmpl.render(hosts=Undefined(name='hosts', message=u"hosts is undefined"))
    assert result == {}
    result = tmpl.render(hosts=[])
    assert result == {}
    result = tmpl.render(
        hosts=[
            {'name': 'foo', 'osfamily': 'RedHat'},
            {'name': 'bar', 'osfamily': 'Debian'}
        ]
    )

# Generated at 2022-06-22 11:50:04.288976
# Unit test for function regex_search
def test_regex_search():
    """
    Test regex_search filter
    """
    # Test single group
    value = regex_search('one two three', '\w*\s\w*', '\\g<0>')
    assert value == 'one two'
    # Test multiple group
    value = regex_search('one two three', '\w*\s\w*', '\\g<0>', '\\g<1>')
    assert value == ['one two', 'one']
    # Test single backref
    value = regex_search('one two three', '\w*\s\w*', '\\1')
    assert value == 'two'
    # Test multiple backref
    value = regex_search('one two three', '\w*\s\w*', '\\1', '\\2')
    assert value == ['two', 'three']
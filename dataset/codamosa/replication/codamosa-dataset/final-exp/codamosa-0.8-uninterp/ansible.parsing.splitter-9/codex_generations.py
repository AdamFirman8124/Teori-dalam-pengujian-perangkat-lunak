

# Generated at 2022-06-13 07:07:42.650804
# Unit test for function split_args
def test_split_args():
    tests = dict()
    tests['test_split_args_1'] = dict(
        input='a=b c="foo bar"',
        expected=['a=b', 'c="foo bar"'],
        )
    tests['test_split_args_2'] = dict(
        input='a=b\nc=d',
        expected=['a=b', 'c=d'],
        )
    tests['test_split_args_3'] = dict(
        input='a=b c=d',
        expected=['a=b', 'c=d'],
        )
    tests['test_split_args_4'] = dict(
        input="'a=b' c=d",
        expected=["'a=b'", 'c=d'],
        )

# Generated at 2022-06-13 07:07:54.492548
# Unit test for function split_args

# Generated at 2022-06-13 07:08:05.288227
# Unit test for function split_args
def test_split_args():
    s = "shell sh -c 'foo bar'"
    assert split_args(s) == ["shell", "sh", "-c", "'foo bar'"]

    s = "sh -x 'foo bar'"
    assert split_args(s) == ["sh", "-x", "'foo bar'"]

    s = """
foo bar bam
"""
    assert split_args(s) == ["foo", "bar", "bam"]

    s = """foo "bar bam" baz"""
    assert split_args(s) == ["foo", '"bar bam"', "baz"]

    s = """foo "bar bam" baz"""
    assert split_args(s) == ["foo", '"bar bam"', "baz"]

    s = """foo "bar bam" baz"""

# Generated at 2022-06-13 07:08:16.454887
# Unit test for function parse_kv
def test_parse_kv():
    res = parse_kv("foo=bar bar=baz baz=bat")
    assert res[u'foo'] == 'bar'
    assert res[u'bar'] == 'baz'
    assert res[u'baz'] == 'bat'

    assert u'_raw_params' not in res

    res = parse_kv("foo=bar bar=baz baz=bat test")
    assert res[u'foo'] == 'bar'
    assert res[u'bar'] == 'baz'
    assert res[u'baz'] == 'bat'

    assert res[u'_raw_params'] == 'test'

    res = parse_kv("foo=bar bar=baz baz=bat test \"test one\"")
    assert res[u'foo'] == 'bar'

# Generated at 2022-06-13 07:08:26.626905
# Unit test for function split_args
def test_split_args():
    print("Testing split_args")


# Generated at 2022-06-13 07:08:37.733675
# Unit test for function split_args
def test_split_args():
    # simple test
    args = u"{{foo}} {{bar}}"
    result = split_args(args)
    assert result == [u'{{foo}}', u'{{bar}}']

    args = u"{{foo}} {{bar}} -a {{hello}}=1"
    result = split_args(args)
    assert result == [u'{{foo}}', u'{{bar}}', u'-a', u'{{hello}}=1']

    args = u"{{foo}} {{bar}} -a=1"
    result = split_args(args)
    assert result == [u'{{foo}}', u'{{bar}}', u'-a=1']

    args = u"{{foo}} {{bar}} -a=1 {{hello}}"
    result = split_args(args)

# Generated at 2022-06-13 07:08:48.275723
# Unit test for function split_args
def test_split_args():
    from nose.tools import assert_equal
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.errors import AnsibleParserError

    display = Display()
    loader = DataLoader()

    # Test newline split

# Generated at 2022-06-13 07:08:59.854376
# Unit test for function split_args
def test_split_args():
    import textwrap


# Generated at 2022-06-13 07:09:10.002135
# Unit test for function split_args

# Generated at 2022-06-13 07:09:18.704896
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"'a=b' c='d e' f='g'") == {
        u'a': u'b',
        u'c': u'd e',
        u'f': u'g',
        u'_raw_params': u"'a=b' c='d e' f='g'"
    }
    assert parse_kv(u"'a=b' c='d e' f='g'", check_raw=True) == {
        u'a': u'b',
        u'c': u'd e',
        u'f': u'g'
    }

# Generated at 2022-06-13 07:09:38.267632
# Unit test for function parse_kv
def test_parse_kv():
    original = "--foo=bar --bar -baz=bat"
    parsed = parse_kv(original)
    expected = {u'foo': u'bar', u'bar': True, u'baz': u'bat'}
    assert parsed == expected
    # quoted values
    original = "--foo='bar' --bar -baz='bat'"
    parsed = parse_kv(original)
    expected = {u'foo': u'bar', u'bar': True, u'baz': u'bat'}
    assert parsed == expected
    # patch #19700: mixing quoted and unquoted values
    original = "--foo='bar' --bar -baz=bat"
    parsed = parse_kv(original)

# Generated at 2022-06-13 07:09:49.515939
# Unit test for function split_args
def test_split_args():
    '''
    run with: nosetests -v
    '''

    print("test_split_args")

    def get_expected_output(stripped_string, quoted_index):
        '''
        Convenience function to extract the expected output
        '''
        if len(quoted_index) == 1:
            return [stripped_string[:quoted_index[0]], stripped_string[quoted_index[0]:]]
        else:
            return [stripped_string[:quoted_index[0]], stripped_string[quoted_index[0]:quoted_index[1]]]


# Generated at 2022-06-13 07:09:58.440902
# Unit test for function split_args
def test_split_args():

    # Example args with valid jinja2 blocks, no counts should be non-zero after split()
    args = "{% block1 %} -a {{ foo }} -b 'bar' {{ baz }} {% foo.bar('foo') %} {% endblock1 %} {% if 1 in [1, 2, 3] %} {% endif %}"
    (print_depth, block_depth, comment_depth, inside_quotes) = split_args(args)
    assert print_depth == 0
    assert block_depth == 0
    assert comment_depth == 0
    assert inside_quotes is False

    # One unbalanced block should result in error

# Generated at 2022-06-13 07:10:08.232808
# Unit test for function parse_kv

# Generated at 2022-06-13 07:10:20.680307
# Unit test for function split_args
def test_split_args():

    # test the normal cases
    assert split_args('a=b c=d') == ['a=b', 'c=d']
    assert split_args('a=b \'c=d\'') == ['a=b', '\'c=d\'']
    assert split_args('a=b "c=d"') == ['a=b', '"c=d"']
    assert split_args('a=b "c=d" e=f') == ['a=b', '"c=d"', 'e=f']
    assert split_args('a=b "c=d" e="f g"') == ['a=b', '"c=d"', 'e="f g"']

# Generated at 2022-06-13 07:10:32.795362
# Unit test for function parse_kv
def test_parse_kv():
    print(parse_kv('a=1 b=2'))
    print(parse_kv('a=1 b=2 b=3'))
    print(parse_kv('a==1 b=2'))
    print(parse_kv('a=1 b=2 c=3'))
    print(parse_kv('a=1 b=2 c=3 '))
    print(parse_kv('a=1 "b=2 c"=3 d="e f g" h=4'))
    print(parse_kv('a=1 "b=2 c"="e f g"'))
    print(parse_kv('a=1 =2'))
    print(parse_kv('a=1 =2 '))
    print(parse_kv('a=1 ==2 '))
    print

# Generated at 2022-06-13 07:10:41.845553
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    assert parse_kv("key=value") == {u'key': 'value'}
    assert parse_kv("key = value") == {u'key': 'value'}
    assert parse_kv("key = \"value\"") == {u'key': 'value'}
    assert parse_kv("key = 'value'") == {u'key': 'value'}
    assert parse_kv("key = 'val ue'") == {u'key': 'val ue'}
    assert parse_kv("key = 'val ue") == {u'key': "val ue"}
    assert parse_kv("key = \"val ue") == {u'key': "val ue"}

# Generated at 2022-06-13 07:10:46.918949
# Unit test for function parse_kv
def test_parse_kv():
    # No args
    assert len(parse_kv(None)) == 0

    # Trivial args
    assert parse_kv('foo=bar') == {'foo': 'bar'}

    # Quoted args
    assert parse_kv('foo="bar baz"') == {'foo': 'bar baz'}

    # Quoted args with escaped quotes
    assert parse_kv(r'foo="bar \"baz\""') == {'foo': 'bar "baz"'}

    # Test parsing of escaped values
    assert parse_kv(r"foo='bar \'baz\''") == {'foo': 'bar \'baz\''}

    # Test parsing of bare args

# Generated at 2022-06-13 07:10:55.639816
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=foo') == {'a':'foo'}
    assert parse_kv('  a  =  foo  ') == {'a': 'foo'}
    assert parse_kv('  a  =  foo  b=bar') == {'a': 'foo', 'b': 'bar'}
    assert parse_kv('foo') == {}
    # Make sure that a=b=c doesn't parse as we expect
    assert parse_kv('a=b=c') == {'a': 'b=c'}
    assert parse_kv('a b c d') == {'_raw_params': 'a b c d'}
    # Make sure that param=val doesn't parse as we expect

# Generated at 2022-06-13 07:10:59.164984
# Unit test for function split_args
def test_split_args():
    test_str = """{{ foo }} {% bar %} {# baz #} 'foo bar' \"qux quux\"\\
    foobar"""
    test_list = ['{{', 'foo', '}}', '{%', 'bar', '%}', '{#', 'baz', '#}',
                 '\'foo bar\'', '"qux quux"', 'foobar']
    assert split_args(test_str) == test_list

# Generated at 2022-06-13 07:11:18.386651
# Unit test for function split_args
def test_split_args():
    arg_str = "  hello   world   "
    vargs = split_args(arg_str)
    assert vargs == ['hello', 'world'], "Failed to split arguments on spaces"

    arg_str = " {{ foo_bar }}"
    vargs = split_args(arg_str)
    assert vargs == ['{{ foo_bar }}'], "Failed to split arguments on jinja2 syntax"

    arg_str = "  {{ foo_bar }} bar "
    vargs = split_args(arg_str)
    assert vargs == ['{{ foo_bar }}', 'bar'], "Failed to split arguments on jinja2 syntax"

    arg_str = "  {{ foo_bar }} bar {{ baz }} "
    vargs = split_args(arg_str)

# Generated at 2022-06-13 07:11:24.630131
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(None) == {}
    assert parse_kv('') == {}
    assert parse_kv('a=b') == {'a': 'b'}
    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}
    assert parse_kv('a="b c=d"') == {'a': 'b c=d'}
    assert parse_kv('a="b c=d" e=f') == {'a': 'b c=d', 'e': 'f'}
    assert parse_kv('a=b e="f g"') == {'a': 'b', 'e': 'f g'}

# Generated at 2022-06-13 07:11:38.857335
# Unit test for function parse_kv
def test_parse_kv():
    # Test 1
    input_cmd = "why=foo arg1 arg2 arg3"
    expected_output = {"why": "foo", "_raw_params": "arg1 arg2 arg3"}
    assert parse_kv(input_cmd) == expected_output

    # Test 2
    input_cmd = "arg1 arg2 arg3"
    expected_output = {"_raw_params": "arg1 arg2 arg3"}
    assert parse_kv(input_cmd) == expected_output

    # Test 3
    input_cmd = "arg1=val1 arg2=val2 arg3=val3 why=foo"
    expected_output = {"arg1": "val1", "arg2": "val2", "arg3": "val3", "why": "foo"}
    assert parse_kv(input_cmd) == expected_

# Generated at 2022-06-13 07:11:49.321020
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('a=1') == {'a': '1'}
    assert parse_kv('a=1 b=2') == {'a': '1', 'b': '2'}
    assert parse_kv('a = 1 b = 2') == {'a': '1', 'b': '2'}
    # free form params
    assert parse_kv('a=1 b=2 c') == {'a': '1', 'b': '2', '_raw_params': 'c'}
    assert parse_kv('a=1 b=2 "c"') == {'a': '1', 'b': '2', '_raw_params': 'c'}

# Generated at 2022-06-13 07:12:00.499667
# Unit test for function split_args
def test_split_args():
    '''
    Basic test cases for split_args.
    '''

    # Basic split on newlines test
    assert split_args("echo 'Hello'\n echo 'World'") == ["echo 'Hello'", "echo 'World'"]

    # Simple single-level split on space inside a quoted section
    assert split_args("foo.sh 'a b'") == ["foo.sh 'a b'"]

    # Simple multi-level split on spaces inside a quoted section
    assert split_args("foo.sh 'a b' b=c d=e 'f g' h=i") == ["foo.sh 'a b'", "b=c", "d=e", "'f g'", "h=i"]

    # Split on space inside a quoted section, followed by a jinja2 block

# Generated at 2022-06-13 07:12:08.133985
# Unit test for function parse_kv
def test_parse_kv():
    # Test for characters not in k=v
    data = split_args('a b c')
    assert data[0] == 'a'

    # Test for characters in k=v
    data = split_args('a=b c=d')
    assert data[0] == 'a=b'

    # Test for empty string
    data = split_args('')
    assert data == []

    # Test for empty string with spaces
    data = split_args('   ')
    assert data == []

    # Test for single quotes in list
    data = split_args('a="b c"')
    assert data == ['a="b c"']

    # Test for single quoted string
    data = split_args("a='b c'")
    assert data == ["a='b c'"]

    # Test for double quoted string
   

# Generated at 2022-06-13 07:12:17.994436
# Unit test for function split_args
def test_split_args():
    options = []
    options.append([u'creates=/var/lock/file.lock', ['creates=/var/lock/file.lock']])
    options.append([u'creates="/var/lock/file.lock"', ['creates="/var/lock/file.lock"']])
    options.append([u'creates=/var/lock/file.lock removes=/var/lock/file.lock', ['creates=/var/lock/file.lock', 'removes=/var/lock/file.lock']])
    options.append([u'creates=/var/lock/file.lock removes="/var/lock/file.lock"', ['creates=/var/lock/file.lock', 'removes="/var/lock/file.lock"']])

# Generated at 2022-06-13 07:12:31.374947
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("cmd") == {'_raw_params': 'cmd'}
    assert parse_kv("cmd1 cmd2") == {'_raw_params': 'cmd1 cmd2'}
    assert parse_kv("cmd with spaces") == {'_raw_params': 'cmd with spaces'}
    assert parse_kv("cmd=\"with spaces\"") == {'_raw_params': 'cmd=with spaces'}
    assert parse_kv("cmd='with spaces'") == {'_raw_params': 'cmd=with spaces'}
    assert parse_kv("cmd=with\\ spaces") == {'_raw_params': 'cmd=with spaces'}
    assert parse_kv("cmd=with spaces") == {'cmd': 'with spaces'}

# Generated at 2022-06-13 07:12:36.248300
# Unit test for function parse_kv
def test_parse_kv():
    '''
    Test for function parse_kv
    '''
    assert parse_kv('a="1" b="2"') == {'a': '1', 'b': '2'}



# Generated at 2022-06-13 07:12:48.875822
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:16.555390
# Unit test for function parse_kv
def test_parse_kv():
    def check(inp, expected):
        res = parse_kv(inp)
        assert res == expected, "'%s' != '%s'" % (res, expected)

    check('foo=bar', {'foo': 'bar'})
    check('foo   =   bar', {'foo': 'bar'})
    check(' foo = bar ', {'foo': 'bar'})
    check('foo=  bar', {'foo': 'bar'})
    check('foo =bar', {'foo': 'bar'})
    check('foo = bar', {'foo': 'bar'})
    check('foo = bar=baz=bop', {'foo': 'bar=baz=bop'})
    check('foo=bar=baz', {'foo': 'bar=baz'})

# Generated at 2022-06-13 07:13:25.071966
# Unit test for function parse_kv

# Generated at 2022-06-13 07:13:34.302305
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.module_utils.quoting import no_quotes
    options = parse_kv("foo=bar baz='hello world'")
    assert options == dict(foo='bar', baz='hello world')
    assert isinstance(options['foo'], str)
    assert isinstance(options['baz'], str)
    options = parse_kv("foo=bar=baz")
    assert options == dict(foo='bar=baz')
    options = parse_kv("foo='bar \\\'baz'")
    assert options == dict(foo='bar \'baz')
    no_quotes(options)
    assert isinstance(options, dict)
    assert isinstance(options['foo'], str)



# Generated at 2022-06-13 07:13:41.033180
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv(u"creates=/tmp/foo executable=/bin/false") == dict(creates='/tmp/foo', executable='/bin/false')
    assert parse_kv(u'c="foo bar" d="wow \'boo\'"') == dict(c='foo bar', d='wow \'boo\'')
    assert parse_kv(u'a="wow" b=\'boo\'') == dict(a='wow', b='boo')
    assert parse_kv(u'a="wow") b=\'boo\'') == dict(a='wow)"', b='boo')
    assert parse_kv(u'a="wow\" b=\'boo\'') == dict(a='wow\'"', b='boo')

# Generated at 2022-06-13 07:13:50.591312
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:04.987790
# Unit test for function parse_kv
def test_parse_kv():
    from ansible.utils import listify_lookup_plugin_terms
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()

# Generated at 2022-06-13 07:14:12.520206
# Unit test for function parse_kv

# Generated at 2022-06-13 07:14:20.346751
# Unit test for function parse_kv
def test_parse_kv():
    def parse_args_and_check(args, expected, **kwargs):
        options = parse_kv(args, **kwargs)
        assert not bool(set(expected.keys()) ^ set(options.keys()))
        for k, v in options.items():
            assert expected[k] == v

    # Single quoted string, with an escaped quote
    parse_args_and_check("'Hello World' hello='world'", {
        'hello': 'world',
        '_raw_params': "'Hello World'"
    })

    # Double quoted strings and escaped double quotes
    parse_args_and_check('"Hello World" hello="world"', {
        'hello': 'world',
        '_raw_params': '"Hello World"'
    })

    # Mix of quoted strings and no string
    parse_args_and_

# Generated at 2022-06-13 07:14:24.547571
# Unit test for function parse_kv
def test_parse_kv():
    options = parse_kv('ansible_python_interpreter=/usr/bin/python create=True home=/path/to/home')
    assert options[u'ansible_python_interpreter'] == '/usr/bin/python'
    assert options[u'create'] == 'True'
    assert options[u'home'] == '/path/to/home'

    options = parse_kv('ansible_python_interpreter=/usr/bin/python create=True home=/path/to/home',True)
    assert options[u'create'] == 'True'
    assert options[u'home'] == '/path/to/home'
    assert options[u'_raw_params'] == 'ansible_python_interpreter=/usr/bin/python'


# Generated at 2022-06-13 07:14:30.108609
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=1 b=2 c=3") == {u'c': u'3', u'a': u'1', u'b': u'2'}
    assert parse_kv("a=1 b=2 c=3", True) == {u'c': u'3', u'a': u'1', u'b': u'2'}
    assert parse_kv("a=1 b=2 c=3", check_raw=True) == {u'c': u'3', u'a': u'1', u'b': u'2', u'_raw_params': u'a=1 b=2 c=3'}


# Generated at 2022-06-13 07:14:50.212701
# Unit test for function parse_kv
def test_parse_kv():
    kv_string = ""
    assert parse_kv(kv_string) == {}

    kv_string = "a=b"
    assert parse_kv(kv_string) == {'a':'b'}

    kv_string = "a=b c=d"
    assert parse_kv(kv_string) == {'a':'b', 'c':'d'}

    kv_string = "a=b c=d e"
    assert parse_kv(kv_string) == {'a':'b', 'c':'d', '_raw_params':u'e'}

    kv_string = "a=b c=d e creates=f"

# Generated at 2022-06-13 07:14:58.827873
# Unit test for function parse_kv
def test_parse_kv():
    '''
     Unit test for function parse_kv
    '''
    options = parse_kv('creates=/test/test/test removes=test2 chdir=/test/test')
    assert(options['creates'] == '/test/test/test')
    assert(options['removes'] == 'test2')
    assert(options['chdir'] == '/test/test')
    assert(options['_raw_params'] == None)

    options = parse_kv('test1=test2 test3=test4')
    assert(options['_raw_params'] == 'test1=test2 test3=test4')
    assert('test1' not in options)
    assert('test3' not in options)

    options = parse_kv('test1=test2 test3=test4', True)

# Generated at 2022-06-13 07:15:08.399184
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("a=b c='d e' f=''") == dict(a='b', c='d e', f='')
    assert parse_kv("a=b c='d e' f=''", True) == dict(a='b', c='d e', f='', _raw_params="a=b c='d e' f=''")
    assert parse_kv("a='c=d' c='a=b'") == dict(a='c=d', c='a=b')


# Generated at 2022-06-13 07:15:17.624516
# Unit test for function split_args

# Generated at 2022-06-13 07:15:25.091765
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}

    assert parse_kv('a=b c=d') == {'a': 'b', 'c': 'd'}

    assert parse_kv('a=b "c d"') == {'a': 'b', '_raw_params': '"c d"'}

    assert parse_kv('a=b "c d"', check_raw=False) == {'a': 'b', 'c d': ''}

#
# Helper class for parsing the arguments to an ansible module
#

# Generated at 2022-06-13 07:15:32.539198
# Unit test for function parse_kv
def test_parse_kv():
    print("testing parse_kv()")
    cases = dict()
    cases[''] = dict()

    # basic test
    cases['f1=v1 f2=v2'] = dict(f1='v1', f2='v2')
    cases['f1=v1 "f2=v2 f3=v3"'] = dict(f1='v1', f2='v2 f3=v3')
    cases['"f1=v1 f2=v2" f3=v3'] = dict(f1='v1 f2=v2', f3='v3')

    # testing quotes
    cases["f1='v1' f2='v2'"] = dict(f1='v1', f2='v2')
    cases["f1='v1' \"f2=v2\""]

# Generated at 2022-06-13 07:15:41.410205
# Unit test for function split_args
def test_split_args():
    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c=foo\\ bar') == ['a=b', 'c=foo bar']
    assert split_args('a=b c=foo\\\nbar') == ['a=b', 'c=foobar']
    assert split_args('a=b c=\\"foo bar\\"') == ['a=b', 'c="foo bar"']
    assert split_args('a=b c={{foo}}') == ['a=b', 'c={{foo}}']
    assert split_args('a=b c={{ foo }}') == ['a=b', 'c={{ foo }}']

# Generated at 2022-06-13 07:15:50.954598
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv("foo=bar") == {u'foo': u'bar'}
    assert parse_kv("foo=bar baz=bar") == {u'foo': u'bar', u'baz': u'bar'}
    assert parse_kv("foo='ba r'") == {u'foo': u'ba r'}
    assert parse_kv("foo='ba r' baz=bar") == {u'foo': u'ba r', u'baz': u'bar'}
    assert parse_kv("foo=\"ba r\"") == {u'foo': u'ba r'}
    assert parse_kv("foo=\"ba r\" baz=bar") == {u'foo': u'ba r', u'baz': u'bar'}

# Generated at 2022-06-13 07:16:04.679919
# Unit test for function parse_kv

# Generated at 2022-06-13 07:16:13.858131
# Unit test for function split_args
def test_split_args():
    # Test case 1:
    params = split_args(u'ansible -m ping -i myhosts jdoe@sample.server.org,mrsmith@another.server.org')
    assert params == ['ansible', '-m', 'ping', '-i', 'myhosts', 'jdoe@sample.server.org,mrsmith@another.server.org'], 'Test case 1 failed'

    # Test case 2:
    params = split_args(u'ansible -m ping -i myhosts jdoe@sample.server.org,mrsmith@another.server.org -vvvv -u johnd')

# Generated at 2022-06-13 07:16:30.490721
# Unit test for function split_args
def test_split_args():
    #test case 1
    args = ''' foo bar 
    baz'''
    expected = ['foo', 'bar', 'baz']
    result = split_args(args)
    assert result == expected
    #test case 2
    args = ''' foo 
    bar baz'''
    expected = ['foo', 'bar', 'baz']
    result = split_args(args)
    assert result == expected
    #test case 3
    args = ''' "{# foo bar #}" baz '''
    expected = ['{#', 'foo bar #}', 'baz']
    result = split_args(args)
    assert result == expected
    #test case 4
    args = '''foo \\\n bar'''
    expected = ['foo', 'bar']
    result = split_args(args)

# Generated at 2022-06-13 07:16:36.135529
# Unit test for function split_args
def test_split_args():
    '''
    Test cases for split_args from
     https://raw.githubusercontent.com/ansible/ansible/devel/test/units/parsing/test_split_args.py
    '''

    # test quoting
    assert split_args(u'"foo bar"') == [u'"foo bar"']
    assert split_args(u"'bar foo'") == [u"'bar foo'"]

    # test no quoting
    assert split_args(u'a b c d e') == [u'a', u'b', u'c', u'd', u'e']
    assert split_args(u'a=b c=d e=f') == [u'a=b', u'c=d', u'e=f']

    # test jinja2 blocks

# Generated at 2022-06-13 07:16:49.823590
# Unit test for function parse_kv

# Generated at 2022-06-13 07:16:57.634070
# Unit test for function parse_kv
def test_parse_kv():
    assert parse_kv('') == {}
    assert parse_kv('foo=bar') == {u'foo': u'bar'}
    assert parse_kv('foo=bar val1 val2') == {u'foo': u'bar', u'_raw_params': u'val1 val2'}
    assert parse_kv('foo=bar val1 val2', check_raw=True) == {u'foo': u'bar', u'val1': u'val2'}
    assert parse_kv('foo=bar val1 val2 name=joe') == {u'foo': u'bar', u'_raw_params': u'val1 val2 name=joe'}
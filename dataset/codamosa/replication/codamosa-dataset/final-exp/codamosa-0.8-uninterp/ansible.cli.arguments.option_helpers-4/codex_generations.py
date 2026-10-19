

# Generated at 2022-06-12 20:12:27.149444
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/home/ansible/ansible_path') == '/home/ansible/ansible_path'
    assert sorted(unfrack_path(pathsep=True)('/home/ansible/ansible_path/lib:/home/ansible/ansible_path/modules')) == ['/home/ansible/ansible_path/lib', '/home/ansible/ansible_path/modules']
    assert sorted(unfrack_path(pathsep=True)('/home/ansible/ansible_path/lib:$ANSIBLE_LIB:/home/ansible/ansible_path/modules')) == ['/home/ansible/ansible_path/lib', '/home/ansible/ansible_path/modules']



# Generated at 2022-06-12 20:12:37.963695
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():

    test_case = "test_PrependListAction___call__"
    print(test_case)
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action=PrependListAction, type=int)
    args = parser.parse_args('--foo 1 2 3'.split())
    assert args.foo == [1, 2, 3], \
        "parser.parse_args('--foo 1 2 3'.split()).foo = {},  Expected = {}".format(args.foo, [1, 2, 3])

    args = parser.parse_args('--foo'.split())
    assert args.foo is None, \
        "parser.parse_args('--foo'.split()).foo = {},  Expected = {}".format(args.foo, None)


# Generated at 2022-06-12 20:12:46.792370
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    options = parser.parse_args(['-t', 'log'])
    assert options.tree == 'log'
    options = parser.parse_args(['-t', '~/logs'])
    assert options.tree == os.path.abspath(os.path.expanduser('~/logs'))
    options = parser.parse_args([])
    assert options.tree == None


# Generated at 2022-06-12 20:12:54.112004
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_cases = (
        ('@/path', '@' + os.path.abspath('/path')),
        ('@@/path', '@@' + os.path.abspath('/path')),
        ('@@@path', '@@@path'),
        ('/path', '/path'),
    )

    for case in test_cases:
        result = maybe_unfrack_path('@')(case[0])
        assert result == case[1], "Result should be %s instead of %s" % (case[1], result)



# Generated at 2022-06-12 20:13:03.293418
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(prog='ansible-runner', add_help=False)
    add_connect_options(parser)
    assert '--private-key' in [x.option_strings for x in parser._actions][3]
    assert '-u' in [x.option_strings for x in parser._actions][4]
    assert '-c' in [x.option_strings for x in parser._actions][5]
    assert '-T' in [x.option_strings for x in parser._actions][6]
    assert '--ssh-common-args' in [x.option_strings for x in parser._actions][7]
    assert '--sftp-extra-args' in [x.option_strings for x in parser._actions][8]

# Generated at 2022-06-12 20:13:09.131494
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser(description="Test the add_check_options function", conflict_handler="resolve")
    add_check_options(parser)
    argv = ["-C", "--syntax-check", "-D"]
    options = parser.parse_args(argv)
    assert options.check == True
    assert options.diff == True
    assert options.syntax == True
    argv = ["--syntax-check", "-D", "-C"]
    options = parser.parse_args(argv)
    assert options.check == True
    assert options.diff == True
    assert options.syntax == True



# Generated at 2022-06-12 20:13:11.667029
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = AnsibleArgumentParser(None, None, None, None)
    add_runas_options(parser)
    return parser



# Generated at 2022-06-12 20:13:20.807399
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    """Unit test function for function add_runas_prompt_options"""
    parser = argparse.ArgumentParser()
    add_runas_prompt_options(parser)
    args = parser.parse_args(['-K', '--become-password-file=test'])
    assert args.become_ask_pass
    assert args.become_password_file == 'test'
    args = parser.parse_args(['--become-password-file=test'])
    assert args.become_password_file == 'test'



# Generated at 2022-06-12 20:13:25.258417
# Unit test for function add_async_options
def test_add_async_options():
    parser = create_base_parser('/usr/bin/ansible')
    add_async_options(parser)
    parser.print_help()
    args = parser.parse_args(['-B', '300', '-P', '10'])
    assert args.seconds == 300
    assert args.poll_interval == 10


# Generated at 2022-06-12 20:13:37.764304
# Unit test for function unfrack_path
def test_unfrack_path():
    # os.path.expanduser function will expand environment variables by default.
    # So we have to use the os.path.expandvars function explicitly to test this function.
    os.environ['ANSIBLE_CONFIG'] = './ansible.cfg'
    os.environ['ANSIBLE_LIBRARY'] = 'library'

# Generated at 2022-06-12 20:14:12.153390
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(beacon='@')(value='@/tmp/ansible1') == '@/tmp/ansible1'
    assert maybe_unfrack_path(beacon='@')(value='@/tmp/../ansible') == '@/ansible'
    assert maybe_unfrack_path(beacon='@')(value='/etc/passwd') == '/etc/passwd'
    assert maybe_unfrack_path(beacon='@')(value='@../ansible') == '@../ansible'
    assert maybe_unfrack_path(beacon='@')(value='@/tmp/../../ansible/') == '@/ansible/'


# Generated at 2022-06-12 20:14:19.005111
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace:
        pass
    namespace = Namespace
    ensure_value(namespace, 'a', 3)
    assert namespace.a == 3
    ensure_value(namespace, 'b', [])
    assert namespace.b == []
    namespace.a = 5
    ensure_value(namespace, 'a', 3)
    assert namespace.a == 5


#
# Option parsers
#

# Generated at 2022-06-12 20:14:24.741266
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace(object):
        pass
    my_ns = Namespace()
    assert ensure_value(my_ns, 'foo', []) is not None
    assert ensure_value(my_ns, 'foo', []) is not None
    my_ns.foo = None
    assert ensure_value(my_ns, 'foo', []) is not None
    assert ensure_value(my_ns, 'foo', []) is not None
    assert getattr(my_ns, 'foo') is None

# Generated at 2022-06-12 20:14:30.489302
# Unit test for function ensure_value
def test_ensure_value():
    class FakeNamespace:
        def __init__(self):
            pass
    assert ensure_value(FakeNamespace(), 'foo', 'bar') == 'bar'
    ns = FakeNamespace()
    setattr(ns, 'foo', 'baz')
    assert ensure_value(ns, 'foo', 'bar') == 'baz'


#
# Base class for AnsibleOptions
#

# Generated at 2022-06-12 20:14:32.517286
# Unit test for function version
def test_version():
    file = os.path.splitext(os.path.basename(__file__))[0]
    assert version(file).startswith(file)

# Generated at 2022-06-12 20:14:39.617496
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # beacon is different than first character, value should be unchanged
    assert maybe_unfrack_path('/')('.') == '.'
    assert maybe_unfrack_path('/')('./path/to/file') == './path/to/file'
    # beacon is first character, value should be unfracked
    assert maybe_unfrack_path('.')('./path/to/file') == './path/to/file'
    assert maybe_unfrack_path('.')('~/path/to/file') == '~/path/to/file'



# Generated at 2022-06-12 20:14:45.930875
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    cmdline = "--vault-password-file foo --vault-password-file bar --vault-id vault id1 --vault-id vault id2"
    try:
        parser.parse_args(cmdline.split())
    except SystemExit:
        assert False



# Generated at 2022-06-12 20:14:46.921560
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    pass


# Generated at 2022-06-12 20:14:50.141874
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@BAR') == '@' + unfrackpath('BAR')
    assert maybe_unfrack_path('@')('FOO') == 'FOO'


# Generated at 2022-06-12 20:14:53.246713
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = MockOptParser()
    add_vault_options(parser)
    assert_equal(parser.add_argument.call_count, 2)

# Generated at 2022-06-12 20:15:04.275707
# Unit test for function unfrack_path
def test_unfrack_path():
    '''test unfrack_path'''
    if not os.path.exists('testfile'):
        with open('testfile', 'w') as test_file:
            test_file.write('testfile')

    try:
        assert unfrack_path()('testfile') == os.path.join(os.getcwd(), 'testfile')
        assert unfrack_path(os.pathsep)('testfile') == [os.path.join(os.getcwd(), 'testfile')]
    finally:
        os.remove('testfile')


#
# OptionGroups
#

# Generated at 2022-06-12 20:15:05.137876
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    pass



# Generated at 2022-06-12 20:15:12.130545
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('foo') == 'foo'
    assert unfrack_path()('foo/bar') == 'foo/bar'
    assert unfrack_path()('foo/bar/') == 'foo/bar/'
    assert unfrack_path()('bar') == 'bar'
    assert unfrack_path(pathsep=True)('foo/bar:bar') == ['foo/bar', 'bar']
    assert unfrack_path(pathsep=True)('foo/bar:') == ['foo/bar', '']
    assert unfrack_path(pathsep=True)('foo/bar:/') == ['foo/bar', '']
    assert unfrack_path(pathsep=True)('foo/bar:bar:') == ['foo/bar', 'bar', '']

# Generated at 2022-06-12 20:15:16.770020
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)

    args = parser.parse_args(['-t', 'tag1', '-t', 'tag2'])
    assert args.tags == ['tag1', 'tag2']
    assert args.skip_tags == C.TAGS_SKIP

    args = parser.parse_args(['--skip-tags', 'tag1', '--skip-tags', 'tag2'])
    assert args.tags == C.TAGS_RUN
    assert args.skip_tags == ['tag1', 'tag2']

# Generated at 2022-06-12 20:15:20.905867
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser(prog="test", formatter_class=SortingHelpFormatter)
    add_subset_options(parser)
    result = parser.parse_args(
        ['--tags=a', '--tags=b', '--tags=c', '--skip-tags=c', '--skip-tags=d', '--skip-tags=e']
    )
    assert result.tags == ['a', 'b', 'c']
    assert result.skip_tags == ['c', 'd', 'e']



# Generated at 2022-06-12 20:15:26.190675
# Unit test for function add_subset_options
def test_add_subset_options():
    """Unit test for function add_subset_options"""
    parser = Mock()
    add_subset_options(parser)
    parser.add_argument.assert_has_calls([call('-t', '--tags', dest='tags', default=C.TAGS_RUN, action='append', help="only run plays and tasks tagged with these values"), call('--skip-tags', dest='skip_tags', default=C.TAGS_SKIP, action='append', help="only run plays and tasks whose tags do not match these values")])

# Generated at 2022-06-12 20:15:34.067142
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action=PrependListAction)
    parser.add_argument('bar', default=[], nargs='?')
    parser.parse_args(['--foo', '1', '--foo', '2', '3'], namespace=argparse.Namespace())
    assert getattr(parser, 'foo') == ['1', '2']
    assert getattr(parser, 'bar') == ['3']



# Generated at 2022-06-12 20:15:43.941341
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/path/to/new/project/') == '@/path/to/new/project/'
    assert maybe_unfrack_path('@')('@ansible/project/') == '@/etc/ansible/ansible/project/'
    assert maybe_unfrack_path('@')('@/etc/ansible/ansible/project/') == '@/etc/ansible/ansible/project/'
    assert maybe_unfrack_path('@')('@@@ansible/project/') == '@@@/etc/ansible/ansible/project/'

# Generated at 2022-06-12 20:15:53.680033
# Unit test for function unfrack_path
def test_unfrack_path():
    # These tests assume the following values:
    # - datadir = '/etc/ansible'
    # - local datadir = '/usr/share/ansible'
    # - local rolespath = '/etc/ansible/roles:/usr/share/ansible/roles:/usr/local/ansible/roles'

    # Test for Nones
    assert unfrack_path()(None) is None
    # Test for an empty string
    assert unfrack_path()('') == ''

    # Test for a bare path
    assert unfrack_path()('/usr/bin/foo') == '/usr/bin/foo'
    # Test for a bare relative path
    assert unfrack_path()('foo') == 'foo'
    # Test for a '~' path

# Generated at 2022-06-12 20:16:01.155352
# Unit test for function unfrack_path
def test_unfrack_path():

    assert unfrack_path(pathsep=True)('a') == ['a']
    assert unfrack_path(pathsep=True)('a,b') == ['a', 'b']
    assert unfrack_path(pathsep=True)('a,b,') == ['a', 'b']

    assert unfrack_path(pathsep=False)('a') == 'a'
    assert unfrack_path(pathsep=False)('-') == '-'
    assert unfrack_path(pathsep=False)('a,b') == 'a,b'


# Generated at 2022-06-12 20:16:17.283068
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@@')('@@/tmp') == '@@' + unfrackpath('/tmp')
    assert maybe_unfrack_path('@@')('@@' + unfrackpath('/tmp')) == '@@' + unfrackpath('/tmp')
    assert maybe_unfrack_path('@@')('foo@@/tmp') == 'foo@@/tmp'
    assert maybe_unfrack_path('@@')('@@') == '@@'
    assert maybe_unfrack_path('@@')('@@foo') == '@@foo'
    assert maybe_unfrack_path('@@')('') == ''


# Generated at 2022-06-12 20:16:19.496678
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    fun = maybe_unfrack_path('@')
    r = fun('@/foo')
    assert r == '@/foo'


#
# Main parsing
#

# Generated at 2022-06-12 20:16:23.074895
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument("-a")
    parser.add_argument("-b")
    parser.add_argument("-c")
    parser.print_help()


# Generated at 2022-06-12 20:16:25.712708
# Unit test for function version
def test_version():
    test_version.result = version('VERSION TEST')
version.__test__ = False


#
# Common OptionGroups for cli.py and others
#

# Generated at 2022-06-12 20:16:31.893328
# Unit test for function version
def test_version():
    sys.argv[0] = '/home/user/ansible/bin/ansible'
    version()
    C.CONFIG_FILE = '/etc/ansible/ansible.cfg'
    version()
    ansible.__path__ = ['/tmp/ansible/lib/ansible']
    C.COLLECTIONS_PATHS = ['/tmp/ansible/collections']
    version()
    sys.argv[0] = '/ansible/bin/ansible'
    version()
    del sys.argv[0]
    version()

# Generated at 2022-06-12 20:16:38.470641
# Unit test for function version
def test_version():
    class DummyContainer(object):
        def __init__(self, value):
            self.value = value

        def __getattr__(self, key):
            if key == 'prog':
                return self.value
            raise AttributeError

    assert version(prog='prog') == version(DummyContainer('prog'))
    assert version() == version(DummyContainer(None))
    assert version() == version(prog=None)

# Generated at 2022-06-12 20:16:48.527893
# Unit test for function version

# Generated at 2022-06-12 20:16:55.972921
# Unit test for function unfrack_path
def test_unfrack_path():
    p = ['$HOME/a', '$HOME/b']
    path = unfrack_path()
    assert path('$HOME/a' + os.pathsep + '$HOME/b') == [unfrackpath(x) for x in p if x]
    assert path('') == [unfrackpath(x) for x in p if x]
    assert path('$HOME/a' + os.pathsep + '$HOME/b') != [x for x in p if x]

b_pathsep_defaults = ['$HOME/.ansible/tmp', '/tmp']
p_pathsep_defaults = [unfrackpath(x) for x in b_pathsep_defaults if x]


# Generated at 2022-06-12 20:17:04.202377
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(':')(':foobar') == ':foobar'
    assert maybe_unfrack_path(':')(':/foo/bar') == ':/foo/bar'
    assert maybe_unfrack_path('::')('::foobar') == '::foobar'
    assert maybe_unfrack_path('::')('::/foo/bar') == '::/foo/bar'
    try:
        assert maybe_unfrack_path('')('foobar') == '/foobar'
    except AssertionError:
        pass
    else:
        raise AssertionError('maybe_unfrack_path should have failed due to invalid startswith')



# Generated at 2022-06-12 20:17:10.716421
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter, add_help=False)
    parser.add_argument('--bar', help='bar help')
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--baz', help='baz help')
    output = parser.format_help()
    assert '--bar' in output
    assert '--foo' in output
    assert '--baz' in output
    assert output.index("--foo") < output.index("--bar")
    assert output.index("--bar") < output.index("--baz")


# Generated at 2022-06-12 20:17:52.207981
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    value1 = "./test_maybe_unfrack_path"
    maybe_unfrack_path_actual = maybe_unfrack_path("./")(value1)
    maybe_unfrack_path_expected = "./" + unfrackpath(value1[1:])

    assert(maybe_unfrack_path_actual == maybe_unfrack_path_expected)
    assert(maybe_unfrack_path_actual == "./test_maybe_unfrack_path")  # unfrack_path returns a path which is already expanded



# Generated at 2022-06-12 20:17:58.094788
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common import tmp_path
    import os
    import os.path
    import sys

    m_up = maybe_unfrack_path(to_bytes('b', encoding=sys.getdefaultencoding()))
    # Test that nothing happens if we don't match a beacon
    assert m_up(to_bytes("nope")) == to_bytes("nope")
    # Write data to a file and test that the file is actually written to and that
    # the path is returned
    tf = tmp_path()

# Generated at 2022-06-12 20:18:06.674958
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@PATH')('@PATH/foo/bar') == '@PATH' + unfrackpath('/foo/bar')
    assert maybe_unfrack_path('@PATH')('/foo/bar') == '/foo/bar'
    assert maybe_unfrack_path('@PATH')('@PATH') == '@PATH' + unfrackpath('')
    assert maybe_unfrack_path('@PATH')('@PATH/') == '@PATH' + unfrackpath('')
    assert maybe_unfrack_path('@PATH')('@PATH///') == '@PATH' + unfrackpath('/')



# Generated at 2022-06-12 20:18:11.195153
# Unit test for function unfrack_path
def test_unfrack_path():
    path = "/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin"
    target = unfrack_path(True)
    assert target(path) == ['/usr/local/bin', '/usr/bin', '/usr/local/sbin', '/usr/sbin']

    path = "/usr/local/bin"
    target = unfrack_path()
    assert target(path) == '/usr/local/bin'

    path = "-"
    target = unfrack_path()
    assert target(path) == '-'



# Generated at 2022-06-12 20:18:16.410770
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)("") == ""
    assert unfrack_path(pathsep=False)("$HOME") == os.path.expanduser("~")
    assert unfrack_path(pathsep=False)("/foo/bar") == "/foo/bar"
    assert unfrack_path(pathsep=False)("/foo/bar") == "/foo/bar"
    assert unfrack_path(pathsep=True)("/foo/bar:/tmp") == ["/foo/bar", "/tmp"]
    assert unfrack_path(pathsep=True)("/foo/bar") == ["/foo/bar"]



# Generated at 2022-06-12 20:18:23.157096
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """
    This is a utility function that will un-fudge things.
    >>> maybe_unfrack_path('myprefix:')

    :param value:
    :return:
    """
    assert maybe_unfrack_path('myprefix:')

    assert maybe_unfrack_path('myprefix:')('myvalue') == 'myvalue'
    assert maybe_unfrack_path('myprefix:')('myprefix:myvalue') == 'myprefix:myvalue'
    assert maybe_unfrack_path('myprefix:')('myprefix:/foo/bar') == 'myprefix:/foo/bar'



# Generated at 2022-06-12 20:18:33.054652
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('--d', action='store')
    parser.add_argument('--e', action='store')
    parser.add_argument('--b', action='store')
    parser.add_argument('--c', action='store')
    parser.add_argument('--a', action='store')
    help_text = parser.format_help()
    assert len(help_text) > 0
    help_text_lines = help_text.split('\n')
    assert help_text_lines[4] == '  -a A, --a A'
    assert help_text_lines[5] == '  -b B, --b B'
    assert help_text_lines[6] == '  -c C, --c C'
    assert help_text_lines

# Generated at 2022-06-12 20:18:36.637213
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('-')('-foo') == '-foo'
    assert maybe_unfrack_path('-@')('-@foo') == '-@' + unfrackpath('foo')
    assert maybe_unfrack_path('-@')('@foo') == '@foo'



# Generated at 2022-06-12 20:18:41.262471
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('path/to/file') == 'path/to/file'
    assert unfrack_path()('./path/to/file') == './path/to/file'
    assert unfrack_path()('~/path/to/file') == os.path.expanduser('~/path/to/file')
    assert unfrack_path()('~foo/path/to/file') == '~foo/path/to/file'
    assert unfrack_path()('$HOME/path/to/file') == os.path.expandvars('$HOME/path/to/file')
    assert unfrack_path(pathsep=True)('/path/to/file:/another/path') == ['/path/to/file', '/another/path']



# Generated at 2022-06-12 20:18:41.840685
# Unit test for function version
def test_version():
    assert version() != __version__

# Generated at 2022-06-12 20:19:34.780103
# Unit test for function unfrack_path
def test_unfrack_path():
    value = os.path.join('~', 'ansible')
    assert os.path.join('/', 'home', 'bob', 'ansible') == unfrack_path(value)
    value = os.path.join('~', 'ansible1') + os.pathsep + os.path.join('~', 'ansible2')
    assert [os.path.join('/', 'home', 'bob', 'ansible1'), os.path.join('/', 'home', 'bob', 'ansible2')] == unfrack_path(value)



# Generated at 2022-06-12 20:19:37.404434
# Unit test for function unfrack_path
def test_unfrack_path():
    unfrack_path(pathsep=True)('~/test1:~/test2') == unfrackpath('~/test1') + ':' + unfrackpath('~/test2')


# Generated at 2022-06-12 20:19:43.934881
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    namespace = argparse.Namespace()
    setattr(namespace, 'dest', ['a', 'b', 'c'])
    action = PrependListAction('', 'dest', nargs=2)
    action.__call__(None, namespace, ['1', '2'])
    assert getattr(namespace, 'dest') == ['1', '2', 'a', 'b', 'c']



# Generated at 2022-06-12 20:19:47.285145
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/tmp') == '@' + unfrackpath('/tmp')
    assert maybe_unfrack_path('@')('/tmp') == '/tmp'
    assert maybe_unfrack_path('@')('@@/tmp') == '@@/tmp'


# Generated at 2022-06-12 20:19:48.301037
# Unit test for function unfrack_path
def test_unfrack_path():
    return unfrack_path(pathsep=False)



# Generated at 2022-06-12 20:19:57.027424
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    """
    This function unit tests some important aspects of constructor of class
    SortingHelpFormatter. This is to ensure that our customized class
    SortingHelpFormatter is working as expected.
    """
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-b', action='store_true', help='Last in the list')
    parser.add_argument('-a', action='store_true', help='First in the list')
    parser.add_argument('-c', action='store_true', help='Middle in the list')

    expected = ['-a', '-b', '-c']
    actual = parser._optionals._group_actions[0].option_strings
    print(actual)
    assert expected == actual



# Generated at 2022-06-12 20:20:05.184361
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """
    Match:

    - '-c test.yml' from '-c test.yml'
    - '-c ./test.yml' from '-c ./test.yml'
    - '-c test.yml' from '-c ./test.yml'
    - '-c ./test.yml' from '-c ~/test.yml'
    - '-c ./test.yml' from '-c /tmp/test.yml'
    """
    example_args = ['-c test.yml', '-c ./test.yml', '-c ./test.yml', '-c ~/test.yml', '-c /tmp/test.yml']

# Generated at 2022-06-12 20:20:07.882871
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument("-a", help="a")
    parser.add_argument("--ab", help="ab")
    parser.add_argument("--aa", help="aa")
    parsed = parser.parse_args([])



# Generated at 2022-06-12 20:20:14.412664
# Unit test for function unfrack_path
def test_unfrack_path():
    if sys.platform.startswith('win'):
        lib_fragged_path = 'C:/ansible/module_utils\\module_utils'
        lib_unfragged_path = 'c:/ansible/module_utils/module_utils'
        lib_path_sep_frag = 'C:/ansible/;module_utils\\module_utils'
        lib_path_sep_unfrag = ['c:/ansible/', 'c:/ansible/module_utils/module_utils']
        lib_path_sep_unfrag_win_ansible = ['c:\\ansible\\', 'c:\\ansible\\module_utils\\module_utils']

        assert unfrack_path()(lib_fragged_path) == lib_unfragged_path

# Generated at 2022-06-12 20:20:19.857592
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/usr/share') == '/usr/share'
    assert unfrack_path()('./my/relative/path') == os.path.abspath('./my/relative/path')
    assert unfrack_path(pathsep=True)('/usr/share:/opt/lib') == ['/usr/share', '/opt/lib']



# Generated at 2022-06-12 20:21:22.553200
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo-bar', action='store_true')
    parser.add_argument('--bar-baz', action='store_true')
    parser.add_argument('--baz-quux', action='store_true')
    # These option_strings will produce the following ordering:
    # --baz-quux
    # --bar-baz
    # --foo-bar
    # This is because the short options '-b' and '-f' are sorted after '-q' alphabetically.

# Generated at 2022-06-12 20:21:24.023793
# Unit test for function version
def test_version():
    assert version("program name") == "program name [core %s]" % __version__



# Generated at 2022-06-12 20:21:33.221005
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    examples = [
        ('@foo', '@/data/ansible/foo'),
        ('@@foo', '@@foo'),
        ('@foo/bar', '@/data/ansible/foo/bar'),
        ('@@foo/bar', '@@foo/bar'),
        ('foo/@bar', 'foo/@bar'),
        ('foo/@@bar', 'foo/@@bar'),
        ('foo/bar', 'foo/bar'),
    ]
    for example, expected in examples:
        actual = maybe_unfrack_path('@')(example)
        if actual != expected:
            raise Exception("Failed to unfrack '%s': expected '%s', got '%s'" % (example, expected, actual))
test_maybe_unfrack_path()

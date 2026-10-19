

# Generated at 2022-06-12 20:12:16.701124
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)

    # Test params
    args = parser.parse_args([
        '-o',
        '-t', 'tree_path'
    ])
    assert args.one_line == True
    assert args.tree == 'tree_path'



# Generated at 2022-06-12 20:12:18.615978
# Unit test for function add_runas_options
def test_add_runas_options():
    # Note: this function has no unit tests, because it contains code that produces output
    #       (e.g. writing to stderr).
    pass



# Generated at 2022-06-12 20:12:29.371710
# Unit test for function unfrack_path
def test_unfrack_path():
    testpaths = [
        ('', ''),
        # Keep - for backwards compatibility
        ('-', '-'),
        ('~/some/path', os.path.expanduser('~/some/path')),
        (os.path.expanduser('~/some/path'), os.path.expanduser('~/some/path')),
        ('/some/other/path', '/some/other/path'),
        ('$HOME/more/stuff', os.path.expandvars('$HOME/more/stuff')),
        ('$ANSIBLE_CONFIG/../library', os.path.expandvars('$ANSIBLE_CONFIG/../library')),
        ('/some/other/path:/one/more/path', ['/some/other/path', '/one/more/path'])
    ]


# Generated at 2022-06-12 20:12:31.729180
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = SortingHelpFormatter()
    assert parser

# AnsibleModule has its own OptionParser, which is passed to modules (as AM)

# Generated at 2022-06-12 20:12:38.654495
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = argparse.ArgumentParser()
    add_fork_options(parser)
    options = parser.parse_args([])
    assert options.forks == C.DEFAULT_FORKS, "Default for for the forks "# options should be 5
    args = ['-f', '10']
    options = parser.parse_args(args)
    assert options.forks == 10, "Options for for the forks should be 10"



# Generated at 2022-06-12 20:12:50.015380
# Unit test for function add_tasknoplay_options
def test_add_tasknoplay_options():
    parser = argparse.ArgumentParser()
    add_tasknoplay_options(parser)
    # Test default value
    options = parser.parse_args([])
    assert options.task_timeout == C.TASK_TIMEOUT
    # Test default None
    options = parser.parse_args(['--task-timeout', 'None'])
    assert options.task_timeout is None
    # Test integer
    options = parser.parse_args(['--task-timeout', '30'])
    assert options.task_timeout == 30
    # Test negative integer
    with pytest.raises(SystemExit):
        parser.parse_args(['--task-timeout', '-1'])
    # Test 0

# Generated at 2022-06-12 20:12:57.068193
# Unit test for function add_subset_options
def test_add_subset_options():
    # create an argumentparser for unit testing
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    # call function add_subset_options
    add_subset_options(parser)
    # create an empty args list
    args = []
    # feed in empty args to the parser
    # and capture the output of parser
    output = parser.parse_args(args)
    # check if the function is working properly
    # by checking the output
    assert output.tags == C.TAGS_RUN
    assert output.skip_tags == C.TAGS_SKIP


# Generated at 2022-06-12 20:13:06.302993
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = CLI.base_parser()
    add_runas_options(parser)
    # Only check if the options are added to the parser.
    # Check the arguments are correct in the unit test of the
    # _parse_options function in the action plugin.
    assert parser.get_option('--become') == '-b'
    assert parser.get_option('--become-method') == '--become-method'
    assert parser.get_option('--become-user') == '--become-user'
    assert parser.get_option('--ask-become-pass') == '--ask-become-pass'
    assert parser.get_option('--become-ask-pass') == '--become-ask-pass'

# Generated at 2022-06-12 20:13:11.791363
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
     assert maybe_unfrack_path('~')('~/abc') == '~/./abc'
     assert maybe_unfrack_path('~')('a~/abc') == 'a~/abc'


# Generated at 2022-06-12 20:13:13.731403
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    options, args = parser.parse_known_args()
    assert options
    assert not args



# Generated at 2022-06-12 20:13:25.724327
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    result=add_inventory_options(parser)
    assert result
    args = parser.parse_args('-i test.file'.split())
    assert args.inventory == ['test.file']


# Generated at 2022-06-12 20:13:34.994338
# Unit test for function add_runas_options
def test_add_runas_options():
    from ansible.cli.arguments import AnsibleCliArgumentParser

    # Create the parser object
    parser = AnsibleCliArgumentParser(prog="test_add_runas_options", description="Test parser for Ansible runas options")
    parser = add_runas_options(parser)

    # Test the parser
    options = parser.parse_args(["--ask-become-pass"])

    # Check to make sure the options were processed correctly
    assert options.ask_become_pass == True
# --finish


# Generated at 2022-06-12 20:13:42.777285
# Unit test for function ensure_value
def test_ensure_value():
    class Args():
        def __init__(self):
            self.a = None
            self.b = 1
            self.c = None
            self.d = None
            self.e = [1, 2, 3]

    args = Args()
    assert args.a is None
    assert args.b == 1
    assert args.c is None
    assert args.d is None
    assert args.e == [1, 2, 3]

    ensure_value(args, 'a', 1)
    ensure_value(args, 'b', 10)
    ensure_value(args, 'c', [1, 2, 3])
    ensure_value(args, 'd', ['a'])
    ensure_value(args, 'e', ['a', 'b'])

    assert args.a == 1
    assert args.b

# Generated at 2022-06-12 20:13:52.478836
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import unittest.mock as mock
    # Stub object
    stub_parser = mock.Mock()
    stub_parser.prog = 'test_prog'
    stub_values = None
    stub_option_string = None
    # Create instance to test
    ansible_version = AnsibleVersion()
    # Call method __call__
    ansible_version(stub_parser, None, stub_values, stub_option_string)
    # Check expected calls
    stub_parser.exit.assert_called_once()

# Generated at 2022-06-12 20:13:57.677793
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    from ansible.utils.path import Path
    assert maybe_unfrack_path('@libexecdir@')('@libexecdir@/foo') == '@libexecdir@/foo'
    if Path('/etc/ansible/library').exists():
        assert maybe_unfrack_path('@libexecdir@')('@libexecdir@/foo') == '/etc/ansible/library/foo'


# Generated at 2022-06-12 20:14:04.144876
# Unit test for function unfrack_path
def test_unfrack_path():
    # pylint: disable=unused-argument
    def test(a, **kwargs):
        return a
    assert unfrack_path()(test) == test
    assert unfrack_path(pathsep=True)('a:b:c', test='test') == ['a', 'b', 'c']
    assert unfrack_path()('/dev/null') == '/dev/null'



# Generated at 2022-06-12 20:14:05.350565
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    assert AnsibleVersion().__call__(None, None, None, None)



# Generated at 2022-06-12 20:14:13.539511
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action=PrependListAction, const=[3,3,3])
    parser.add_argument('--bar', action=PrependListAction, const=[4,4,4])
    parser.add_argument('--baz', action=PrependListAction, nargs=3, default=[5,5,5])
    args = parser.parse_args(['--baz', '1', '2', '3', '--bar', '--foo'])
    assert args.foo == [3,3,3]
    assert args.bar == [4,4,4]
    assert args.baz == [1,2,3]
    args = parser.parse_args([])
    assert args.foo == []
    assert args.bar == []
   

# Generated at 2022-06-12 20:14:23.816210
# Unit test for function add_runas_options
def test_add_runas_options():
    # create a parser
    parser = argparse.ArgumentParser()

    # add the options to the parser
    add_runas_options(parser)

    # parse the arguments
    args = parser.parse_args(['--become-method', 'pbrun'])

    # verify the options are set properly
    assert args.become
    assert args.become_method == 'pbrun'
    assert args.become_user is None

    # parse another set of arguments
    args = parser.parse_args(['--become-user', 'test'])

    # verify the options are set properly
    assert args.become
    assert args.become_method == 'sudo'
    assert args.become_user == 'test'


# Generated at 2022-06-12 20:14:28.006090
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    n = maybe_unfrack_path('@')
    assert n('@foo') == '@/path/to/foo'
    assert n('nochange') == 'nochange'

#
# Core Option Parser functionality
#

# Generated at 2022-06-12 20:14:51.796321
# Unit test for function unfrack_path
def test_unfrack_path():
    # if pathsep is True, path is split on os.pathsep, resulting in a list
    assert unfrack_path(pathsep=True)('foo/:/tmp') == ['foo/', '/tmp']
    assert unfrack_path(pathsep=True)('foo/') == ['foo/']
    # if value == '-', unfrackpath does not change value
    assert unfrack_path()('-') == '-'
    # default pathsep is False, resulting in a string
    assert unfrack_path()('/etc/ansible/foo') == '/etc/ansible/foo'



# Generated at 2022-06-12 20:15:01.803762
# Unit test for function unfrack_path
def test_unfrack_path():
    """Test function unfrack_path"""
    # The function relies on os.path.expanduser and os.path.expandvars
    # but we don't want to set environment variables to control the result
    # This test uses a fixed path for an environment variable and user home
    # directory, but that should be enough to confirm the function works

# Generated at 2022-06-12 20:15:03.885264
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser(
        prog='test_actions',
        formatter_class=SortingHelpFormatter,
        description='actions',
    )
    add_subset_options(parser)
    print(parser.parse_args(['-t','TAG1','--skip-tags','TAG2']))

# Generated at 2022-06-12 20:15:10.238787
# Unit test for function ensure_value
def test_ensure_value():
    class DummyNamespace(object):
        pass

    namespace = DummyNamespace()
    assert ensure_value(namespace, 'test', 'value') == 'value'
    assert getattr(namespace, 'test') == 'value'
    assert ensure_value(namespace, 'test', 'should not get here') == 'value'
    assert getattr(namespace, 'test') == 'value'
    delattr(namespace, 'test')
    assert ensure_value(namespace, 'test', 'value') == 'value'
    assert getattr(namespace, 'test') == 'value'



# Generated at 2022-06-12 20:15:19.969258
# Unit test for function version
def test_version():
    fake_sys = type('', (), {'argv': ['-c', 'fake_argv.cfg']})()
    fake_sys.modules = {
        'ansible': type('ansible_module', (), {'__file__': '/path/to/ansible/__init__.py', '__path__': ['/path/to/ansible']}),
        'jinja2': type('jinja2_module', (), {'__version__': '2.10'})
    }


# Generated at 2022-06-12 20:15:29.093923
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/tmp') == '/tmp'
    assert unfrack_path(True)('/a/b:/c/d') == ['/a/b', '/c/d']
    assert unfrack_path()('.') == '.'
    assert unfrack_path()('/a/b') == '/a/b'
    assert unfrack_path()('~/a/b') == '~/a/b'
    assert unfrack_path()('../a/b') == '../a/b'
    assert unfrack_path()('../a/b') == '../a/b'
    assert unfrack_path()('-') == '-'
    assert unfrack_path()('./a/b') == './a/b'


# Generated at 2022-06-12 20:15:41.171228
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/does/not/exist') == ''
    assert unfrack_path()('./does/not/exist') == os.path.join(os.getcwd(), 'does', 'not', 'exist')
    assert unfrack_path()('/does/not/exist%s/' % os.pathsep) == ''
    assert unfrack_path()('/does/not/exist:/does/not/exist') == '/does/not/exist'

    for value in ('/does/not/exist', './does/not/exist'):
        assert unfrack_path(pathsep=True)(value) == [unfrack_path()(value)]

# Generated at 2022-06-12 20:15:51.135962
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument("--verbose", action='count')
    parser.add_argument("--quiet", "-q", action='count')
    args = parser.parse_args("".split())
    args = parser.parse_args("--verbose".split())
    args = parser.parse_args("-qqq".split())
    args = parser.parse_args("-qqq --verbose".split())
    args = parser.parse_args("-q --verbose".split())
    args = parser.parse_args("-q --verbose --verbose".split())
    args = parser.parse_args("-q -v".split())



# Generated at 2022-06-12 20:16:02.136184
# Unit test for function add_subset_options
def test_add_subset_options():
    """ Unit test that validates --tags and --skip-tags take multiple values """
    argv = []
    argv_copy = []
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    options = parser.parse_args(argv)
    assert isinstance(options.tags, list)
    assert isinstance(options.skip_tags, list)
    for i in range(3):
        argv.insert(0, '--tags')
        argv.insert(0, 't' + str(i))
        argv_copy.insert(0, 't' + str(i))
        for j in range(3):
            argv.insert(0, '--skip-tags')
            argv.insert(0, 's' + str(j))

# Generated at 2022-06-12 20:16:12.109858
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    """Check that AnsibleVersion.__call__ returns expected value"""

    import io
    import sys
    typ, val, tb = None, None, None
    out = io.StringIO()
    sys.stdout = out
    typ, val, tb = sys.exc_info()

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--version',
            action=AnsibleVersion,
            nargs=0
        )
        args = parser.parse_args(['--version'])
    except SystemExit:
        pass
    sys.exc_info()
    if typ is not None:
        raise(typ, val, tb)

    sys.stdout = sys.__stdout__
    value = out.getvalue()
    out.close()
    assert value

# Generated at 2022-06-12 20:16:25.591399
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # os.pathsep is not defined for windows
    if 'win' not in sys.platform:
        test_path = u'/tmp/../tmp/foo'
        beacon = os.pathsep
        clean_path = unfrackpath(test_path)
        assert maybe_unfrack_path(beacon)(beacon + test_path) == beacon + clean_path
        assert maybe_unfrack_path(beacon)(test_path) == test_path
    else:
        #TODO: implement test
        pass
test_maybe_unfrack_path()


#
# Argparse options
#

# Generated at 2022-06-12 20:16:26.529465
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():   
    pass
        

# Generated at 2022-06-12 20:16:31.275373
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    real_stdout = sys.stdout
    try:
        sys.stdout = mystdout = StringIO()
        args = ['-V']
        cli = CommandLine(args)
        cli.parse()
        cli.run()
        assert mystdout.getvalue() == '2.3.0.0\n'
    finally:
        sys.stdout = real_stdout

# Generated at 2022-06-12 20:16:41.935031
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    dummy_map = dict(
        getopt='/tmp',
        templar='/tmp',
        variables='/tmp'
    )
    # beacon in value
    assert maybe_unfrack_path('/')('/abc') == '/abc'
    assert maybe_unfrack_path('/')('/abc') != '/abc', 'Double-fracked paths are not unfracked'
    assert maybe_unfrack_path('/')('/abc') == '/tmp/abc'
    assert maybe_unfrack_path('/')('//abc') == '//tmp/abc'
    # no beacon in value
    assert maybe_unfrack_path('/')('abc') == 'abc'
    # with default
    assert maybe_unfrack_path('/')('abc', defaults=dummy_map)

# Generated at 2022-06-12 20:16:49.510109
# Unit test for function ensure_value
def test_ensure_value():
    class Options:
        def __init__(self, _=None):
            pass

        def __setattr__(self, name, value):
            self.__dict__[name] = value

    for args in [
        ({'namespace': Options(default_opts=None), 'name': 'default_opts', 'value': {}},
            {'result': {}, 'namespace': {'default_opts': {}}}),
        ({'namespace': Options(default_opts={'foo': 'bar'}), 'name': 'default_opts', 'value': {}},
            {'result': {'foo': 'bar'}, 'namespace': {'default_opts': {'foo': 'bar'}}}),
    ]:
        result = ensure_value(**args[0])

# Generated at 2022-06-12 20:16:56.189091
# Unit test for function version
def test_version():
    import ansible.utils.version as av
    assert(av.version("/bin/ansible-playbook") == "ansible-playbook [core {0}]\n  config file = /etc/ansible/ansible.cfg\n  configured module search path = {1}\n  ansible python module location = {2}\n  executable location = /bin/ansible-playbook\n  python version = {3}\n  jinja version = {4}\n  libyaml = True".format(__version__, C.DEFAULT_MODULE_PATH, ':'.join(ansible.__path__), ''.join(sys.version.splitlines()), j2_version))

# Generated at 2022-06-12 20:17:02.440733
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace():
        pass
    namespace = Namespace()
    setattr(namespace, "attr", None)
    ensure_value(namespace, "attr", 1)
    assert getattr(namespace, "attr", None) == 1
    ensure_value(namespace, "attr", 2)
    assert getattr(namespace, "attr", None) == 1
    ensure_value(namespace, "another_attr", 2)
    assert getattr(namespace, "another_attr", None) == 2



# Generated at 2022-06-12 20:17:09.638335
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bar', action=PrependListAction)
    args = parser.parse_args(['--bar', 'a', '--bar', 'B'])
    print(args)
    assert args.bar == ['a', 'B']

    parser = argparse.ArgumentParser()
    parser.add_argument('--bar', action=PrependListAction, nargs=2)
    args = parser.parse_args(['--bar', 'a', 'b', '--bar', 'C', 'D'])
    print(args)
    assert args.bar == ['a', 'b', 'C', 'D']


# Generated at 2022-06-12 20:17:14.467152
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    class TestArgumentParser(argparse.ArgumentParser):
        def format_help(self):
            # SortingHelpFormatter sorts options, the first in 'ch'
            # the second in 'chr', the third in 'char'
            self.add_argument('-ch', action='store_true', default=False)
            self.add_argument('-char', action='store_true', default=False)
            self.add_argument('-chr', action='store_true', default=False)
            return super(TestArgumentParser, self).format_help()
    t = TestArgumentParser(formatter_class=SortingHelpFormatter)
    help = t.format_help()
    assert 'store_true' in help
    assert '-ch' in help
    assert '-chr' in help

# Generated at 2022-06-12 20:17:23.329943
# Unit test for function version

# Generated at 2022-06-12 20:17:38.151417
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    maybe_unfrack_path_obj = maybe_unfrack_path("@")
    assert maybe_unfrack_path_obj("@git") == "@git"
    assert maybe_unfrack_path_obj("@/orig/path") == "@/ansible/path"



# Generated at 2022-06-12 20:17:40.000155
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    constructor = SortingHelpFormatter
    h = constructor(prog='PROG')
    assert isinstance(h.add_arguments, object)



# Generated at 2022-06-12 20:17:44.289135
# Unit test for function unfrack_path
def test_unfrack_path():
    # os.pathsep is different in Unix and Windows.
    parameter = '-/usr/bin:/usr/local/bin:/usr/bin:/usr/local/bin'
    expected_result = ['-', '/usr/bin', '/usr/local/bin', '/usr/bin', '/usr/local/bin']
    result = unfrack_path(pathsep=True)(parameter)
    assert result == expected_result



# Generated at 2022-06-12 20:17:49.781648
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    result = maybe_unfrack_path('a beacon value')('a beacon value/something/else')
    assert result == 'a beacon value%s/something/else' % os.pathsep
    result = maybe_unfrack_path('a beacon value')('/something/else')
    assert result == '/something/else'
test_maybe_unfrack_path()



# Generated at 2022-06-12 20:17:51.920708
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    object = AnsibleVersion(None, None, None, None)
    object = object.__call__(None, None, None)
    assert object == None



# Generated at 2022-06-12 20:17:55.106250
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    p = argparse.ArgumentParser(prog='__main__')
    p.add_argument('-v', '--version', action=AnsibleVersion, nargs=0)
    opts = p.parse_args(["--version"])
    assert opts.version == None


# Generated at 2022-06-12 20:18:04.822087
# Unit test for function unfrack_path
def test_unfrack_path():
    # unfrack_path should leave "-" alone
    try:
        if unfrack_path()('-') != '-':
            raise Exception("unfrack_path() doesn't work")
    except:
        raise Exception("unfrack_path() doesn't work")
    # unfrack_path should turn a path into an absolute path
    try:
        if unfrack_path()('./somefile') == './somefile':
            raise Exception("unfrack_path() doesn't work")
    except:
        raise Exception("unfrack_path() doesn't work")
    # unfrack_path should turn a path in a list into an absolute path

# Generated at 2022-06-12 20:18:08.788962
# Unit test for function unfrack_path
def test_unfrack_path():
    assert './foo' == unfrack_path(pathsep=False)('./foo')
    assert ['./foo', '/bar'] == unfrack_path(pathsep=True)('foo:bar')
    assert '-' == unfrack_path(pathsep=False)('-')
    assert ['-', '.'] == unfrack_path(pathsep=True)('-:.')


#
# OptionGroups
#

# Generated at 2022-06-12 20:18:11.860380
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    a = AnsibleVersion(option_strings=['--version'])
    a.__call__(argparse.ArgumentParser(), argparse.Namespace(), None)



# Generated at 2022-06-12 20:18:16.691909
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Ansible internal venv must be present or unfrack_path function will fail
    raw_path = '/tmp/foo'
    rc = maybe_unfrack_path('$')('$' + raw_path)
    assert rc == ('$' + unfrackpath(raw_path))
    assert maybe_unfrack_path('$')(raw_path) == raw_path
    assert maybe_unfrack_path('@')('@' + raw_path) == ('@' + unfrackpath(raw_path))
    assert maybe_unfrack_path('@')(raw_path) == raw_path


# Generated at 2022-06-12 20:18:37.337898
# Unit test for function unfrack_path
def test_unfrack_path():
    import tempfile
    cwd = os.getcwd()
    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    # Change the current working directory to common_base_dir
    os.chdir(tmpdir)
    # Create a temporary file
    testfile = tempfile.mkstemp()[1]
    # Test unfrack_path function
    assert unfrack_path()(testfile) == unfrackpath(testfile)
    assert unfrack_path(pathsep=True)(os.path.join(tmpdir,testfile)) == [unfrackpath(testfile)]
    # Remove the temporary file
    os.remove(testfile)
    # Go back to previous directory
    os.chdir(cwd)
    # Remove the temporary directory
    os.rmdir(tmpdir)




# Generated at 2022-06-12 20:18:42.491187
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():

    class Parser(argparse.ArgumentParser):
        def error(self, message):
            pass

    module = AnsibleModule()

    # _AppendAction object
    module.params = {'AppendAction_': []}
    parser = Parser()
    parser.add_argument('-t', action=PrependListAction)
    parser.parse_args('-t a -t b -t c'.split(), namespace=module.params)
    assert(module.params['AppendAction_'] == ['c', 'b', 'a'])
    module.params = {'AppendAction_': [1, 2, 3]}
    parser.parse_args('-t a -t b -t c'.split(), namespace=module.params)

# Generated at 2022-06-12 20:18:43.533396
# Unit test for function version
def test_version():
    assert version()
    assert version("ansible-test")

# Generated at 2022-06-12 20:18:48.511468
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(description='description', formatter_class=SortingHelpFormatter)
    parser.add_argument('--foo')
    parser.add_argument('-b', '--bar')
    parser.add_argument('-f', '--foo')
    parser.add_argument('-z', '--zzz')
    parser.add_argument('-a', '--aaa')
    parser.print_help()



# Generated at 2022-06-12 20:18:48.972215
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    pass

# Generated at 2022-06-12 20:18:55.962915
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    # Call method __call__ of class PrependListAction
    ansible_version_parser = argparse.ArgumentParser()
    ansible_version_parser.add_argument('-a', '--abc', dest='abc', action='store_true', help='abc')
    ansible_version_parser.add_argument('-b', '--bcd', dest='bcd', type=int, help='bcd')
    argv = ['-a', '--bcd', '5']
    options = ansible_version_parser.parse_args(argv)
    assert options.abc == True
    assert options.bcd == 5



# Generated at 2022-06-12 20:19:03.927235
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/') == '/'
    # If a value starts with a '~', it should return the expanded path
    assert unfrack_path()('~/ansible') == os.path.expanduser('~/ansible')
    # If a value is found in the path specified by ANSIBLE_CONFIG, return the expanded path of that value
    assert unfrack_path()('DEFAULT') == os.path.expanduser(os.path.join('~', '.ansible.cfg'))
    assert unfrack_path()('DEFAULT') == os.path.expanduser(os.path.join('~', '.ansible.cfg'))
    # If a value equals the empty string, return value
    assert unfrack_path()('') == ''
    # If a value is not a path and is not in the

# Generated at 2022-06-12 20:19:07.304671
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    import argparse
    class Namespace:
        pass
    namespace = Namespace()
    namespace.a = None
    parser = argparse.ArgumentParser()
    a = PrependListAction(option_strings=['--a'], dest='a')
    a(parser, namespace, ['1', '2'], option_string='--a')
    assert namespace.a == ['1', '2']
    a(parser, namespace, ['3'], option_string='--a')
    assert namespace.a == ['3', '1', '2']
    a(parser, namespace, [], option_string='--a')
    assert namespace.a == ['3', '1', '2']

# Generated at 2022-06-12 20:19:13.026287
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # pylint: disable=unused-variable,too-few-public-methods
    class TestArgParser(argparse.ArgumentParser):
        def exit(self, status=0, msg=None):
            pass

    argparser = TestArgParser()
    argparser.prog = 'Test Ansible Version'
    # pylint: enable=unused-variable,too-few-public-methods

    action = AnsibleVersion(option_strings=['--version'])
    try:
        action(argparser, None, None)
    except SystemExit as e:
        assert e.code == 0

# Generated at 2022-06-12 20:19:20.876337
# Unit test for function unfrack_path
def test_unfrack_path():
    current_path = os.path.dirname(os.path.abspath(__file__))
    def test_path(path, expected_path):
        assert unfrack_path()(path) == expected_path

    # test a real relative path
    test_path(current_path, current_path)

    # test a home path
    test_path('~/.ansible/foo', '~/.ansible/foo')

    # test a windows path
    test_path(r'%ProgramData%\Ansible\foo', r'%ProgramData%\Ansible\foo')

#

# Generated at 2022-06-12 20:20:03.757300
# Unit test for function unfrack_path
def test_unfrack_path():
    import pytest
    assert unfrack_path()('./a') == './a'
    assert unfrack_path(True)('./a:./b') == ['./a', './b']



# Generated at 2022-06-12 20:20:06.515943
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("./foo") == os.path.join(os.getcwd(), "foo")
    assert unfrack_path()("/foo") == "/foo"
    assert unfrack_path()("~/foo") == os.path.expanduser("~/foo")



# Generated at 2022-06-12 20:20:14.156998
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    class ArgparseFakeParser(object):
        _actions = []

        def add_action(self, action):
            self._actions.append(action)
            return action

        def parse_known_args(self, argv, namespace):
            return argv, []

        def exit(self, status=0, message=None):
            pass

    parser = ArgparseFakeParser()
    PrependListAction(option_strings=['--opt'], dest='opt')(
        parser,
        None,
        ['foo', 'bar']
    )

    assert parser._actions[0].__call__(
        parser,
        None,
        ['foo', 'bar'],
        option_string=None
    ) == ['foo', 'bar']

# Generated at 2022-06-12 20:20:14.658699
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    pass


# Generated at 2022-06-12 20:20:20.104105
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    opts = argparse.Namespace()
    opts.foo = []
    p = PrependListAction('-f', 'foo', nargs=1)
    p(None, opts, ['bar'])
    assert opts.foo == ['bar']
    p(None, opts, ['baz'])
    assert opts.foo == ['baz', 'bar']


# Generated at 2022-06-12 20:20:21.700518
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action=AnsibleVersion)

# Generated at 2022-06-12 20:20:29.745372
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    JSONParser = argparse.ArgumentParser()
    JSONParser.add_argument('-j', '--json', action='store_true')
    YAMLParser = argparse.ArgumentParser()
    YAMLParser.add_argument('-y', '--yaml', action='store_true')
    # the following will fail if add_arguments of SortingHelpFormatter sorts args in the parser
    assert operator.eq(str(JSONParser.format_help()), str(YAMLParser.format_help()))


# Generated at 2022-06-12 20:20:32.813445
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", nargs=0, dest="version", action=AnsibleVersion, help="return ansible version")
    assert parser.parse_args(['--version']).version == to_native(version(sys.argv[0])), '--version should return ansible version'


# Generated at 2022-06-12 20:20:37.726496
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    class Action(PrependListAction):
        pass

    action = Action('--append', dest='append', nargs='+')
    parser = argparse.ArgumentParser()
    parser.add_argument('--append', action='append', nargs='+')
    namespace = argparse.Namespace()

    action(parser, namespace, 'default')
    assert all(['default' == x for x in namespace.append])

    action(parser, namespace, 'append_value')
    assert all(['append_value' == x for x in namespace.append])

    action(parser, namespace, 'append_value')
    assert all(['append_value' == x for x in namespace.append])



# Generated at 2022-06-12 20:20:42.390393
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("/a:/b") == "/a:/b"
    assert unfrack_path(pathsep=True)("/a:/b") == ["/a", "/b"]
    assert unfrack_path(pathsep=True)("/a::/b") == ["/a", "", "/b"]
    assert unfrack_path(pathsep=True)("/a:") == ["/a"]
    assert unfrack_path(pathsep=True)(":/b") == ["", "/b"]
    assert unfrack_path()("-") == "-"
    assert unfrack_path()("~/ansible") == "/a/user/home/ansible"


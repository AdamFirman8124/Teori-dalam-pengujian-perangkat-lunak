

# Generated at 2022-06-12 20:12:09.679159
# Unit test for function add_runas_options
def test_add_runas_options():
    assert callable(add_runas_options)



# Generated at 2022-06-12 20:12:18.555191
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser(description='test', prog='test', conflict_handler='resolve')
    add_check_options(parser)
    args = parser.parse_args([])
    assert args.check == False
    assert args.syntax == False
    assert args.diff == None
    args = parser.parse_args(["--syntax-check"])
    assert args.check == False
    assert args.syntax == True
    assert args.diff == None
    args = parser.parse_args(["--check"])
    assert args.check == True
    assert args.syntax == False
    assert args.diff == C.DIFF_ALWAYS
    args = parser.parse_args(["--diff"])
    assert args.check == False
    assert args.syntax == False

# Generated at 2022-06-12 20:12:21.472079
# Unit test for function add_runas_options
def test_add_runas_options():
    from ansible.cli.arguments import option_helpers
    parser = option_helpers.create_base_parser('test')
    add_runas_options(parser)
    args = parser.parse_args(['-b', '--become-method', 'su'])
    assert args.become
    assert args.become_method == 'su'



# Generated at 2022-06-12 20:12:24.878624
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    opts=parser.parse_args(['--vault-password-file', '/foo'])
    assert opts.vault_password_files == ['/foo']

# Generated at 2022-06-12 20:12:29.652145
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser()
    add_async_options(parser)
    options = parser.parse_args(['-P', '5', '-B', '10'])
    assert options.poll_interval == 5
    assert options.seconds == 10



# Generated at 2022-06-12 20:12:34.808714
# Unit test for function add_subset_options
def test_add_subset_options():
    my_args = ['ansible-playbook', 'playbook.yml', '-t', 'tag1', '-t', 'tag2', '--skip-tags', 'tag3', '--skip-tags', 'tag4']
    parser = add_subset_options(create_base_parser(my_args[0], my_args[1], my_args[2]))
    options = parser.parse_args(my_args)
    assert options.tags == ['tag1', 'tag2']
    assert options.skip_tags == ['tag3', 'tag4']


# Generated at 2022-06-12 20:12:43.232732
# Unit test for function add_connect_options
def test_add_connect_options():
    from ansible.utils import plugins
    parser = argparse.ArgumentParser(prog='mycode', formatter_class=SortingHelpFormatter, description='create base parser')
    add_connect_options(parser)
    cmd_line_args = parser.parse_args(['--private-key', 'mykey', '-k', '--connection-password-file', 'password_file',
                                       '--connection', 'ssh', '-u', 'peter', '-T', '100', '--ssh-common-args', 'cargs',
                                       '--sftp-extra-args', 'sextraargs', '--scp-extra-args', 'scextraargs',
                                       '--ssh-extra-args', 'sshextraargs'])
    # Connection Options
    assert cmd_line_args.private

# Generated at 2022-06-12 20:12:49.036948
# Unit test for function unfrack_path
def test_unfrack_path():
    import tempfile
    if sys.version_info >= (3, 6):
        with tempfile.TemporaryDirectory() as tempdir:
            abspath = os.path.join(tempdir, 'ansible.cfg')
            os.makedirs(os.path.dirname(abspath), exist_ok=True)
            with open(abspath, 'w+') as f:
                f.write('[defaults]\nroles_path = {0}'.format(tempdir))
            parser = ConfigCLI(['-c', abspath])
            args = parser.parse_cli_args(['--roles-path', 'roles'])
            assert args.roles_path[0] == os.path.join(tempdir, "roles")
    else:
        from pytest import skip

# Generated at 2022-06-12 20:12:56.270022
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = create_base_parser("ansible")
    add_subset_options(parser)
    args = parser.parse_args(["-t", "a", "--skip-tags", "b", "-t", "c", "--skip-tags", "d"])
    assert 'tags' in args
    assert 'skip_tags' in args
    assert args.tags == ['a', 'c']
    assert args.skip_tags == ['b', 'd']

# To test the function itself, we should add:
# test_add_subset_options()
# to the end of this program



# Generated at 2022-06-12 20:13:01.993734
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser(
        prog='ansible-test',
        formatter_class=SortingHelpFormatter,
        epilog=None,
        description=None,
        conflict_handler='resolve',
    )
    add_async_options(parser)
    opts = parser.parse_args(['-P', '30', '-B', '60'])
    assert opts.poll_interval == 30
    assert opts.seconds == 60



# Generated at 2022-06-12 20:13:19.867910
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    args = parser.parse_args([])
    assert args.tree == None
    assert args.one_line == False

    args = parser.parse_args(["--one-line"])
    assert args.tree == None
    assert args.one_line == True


# Generated at 2022-06-12 20:13:21.260856
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)



# Generated at 2022-06-12 20:13:28.025508
# Unit test for function add_inventory_options
def test_add_inventory_options():
    test_parser = argparse.ArgumentParser()
    add_inventory_options(test_parser)
    test_commands = [[['-i'], {'inventory': ['hosts']}], [['-i path1 -i path2'], {'inventory': ['path1', 'path2']}]]
    for test_command, test_opts in test_commands:
        with pytest.raises(SystemExit) as pytest_context:
            test_parser.parse_args(test_command)
        for key, value in test_opts.items():
            assert getattr(pytest_context.value.args[0], key) == value


# Generated at 2022-06-12 20:13:34.368647
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(description='ansible-playbook program')
    add_connect_options(parser)
    subparsers = parser.add_subparsers(dest='subcommand')

    args = parser.parse_args([])
    assert not 'ask_pass' in args
    assert not 'private_key_file' in args
    assert not 'remote_user' in args



# Generated at 2022-06-12 20:13:38.581886
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser(prog='test')
    list_hosts_help = 'outputs a list of matching hosts; does not execute anything else'
    inventory_help = 'specify inventory host path or comma separated host list. --inventory-file is deprecated'
    limit_help = 'further limit selected hosts to an additional pattern'
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'file', '--list-hosts', '-l', 'subset'])
    assert args.inventory == ['file']
    assert args.listhosts == True
    assert args.subset == 'subset'
    args = parser.parse_args([])
    assert args.inventory == None
    assert args.listhosts == False
    assert args.subset == C.DEFAULT_SU

# Generated at 2022-06-12 20:13:42.414754
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    values = ['v1', 'v2']
    nspace = {}
    action = PrependListAction('option_strings', 'dest', default=[])
    action(parser=None, namespace=nspace, values=values, option_string=None)
    expected = {'dest': ['v1', 'v2']}
    assert nspace == expected



# Generated at 2022-06-12 20:13:48.599308
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import sys
    import re

    class printer(object):
        def __init__(self, text):
            self.text = text
        def __call__(self, msg, file=sys.stdout):
            self.text.append(msg)

    class exit(object):
        def __init__(self, code):
            self.code = code
        def __call__(self, code):
            pass

    class argparse_object(object):
        def __init__(self, prog):
            self.prog = prog
            self.print_call = False
            self.exit_call = False
            self.print_output = []
            self.exit_code = None
        def print_help(self, file=sys.stdout):
            self.print_call = True

# Generated at 2022-06-12 20:13:57.713199
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(prog='test')
    add_connect_options(parser)
    opts, remainder = parser.parse_known_args(['-k', '--conn-pass-file', 'ansible.passwd'])
    assert opts.ask_pass is True
    assert opts.connection_password_file == 'ansible.passwd'
    opts, remainder = parser.parse_known_args(['--conn-pass-file', 'ansible.passwd'])
    assert opts.ask_pass is False
    assert opts.connection_password_file == 'ansible.passwd'
    opts, remainder = parser.parse_known_args(['-k'])
    assert opts.ask_pass is True

# Generated at 2022-06-12 20:14:00.723287
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = argparse.ArgumentParser()
    add_fork_options(parser)
    opts = parser.parse_args("")
    assert opts.forks == C.DEFAULT_FORKS



# Generated at 2022-06-12 20:14:07.710982
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/home/user/import') == '@' + unfrackpath('/home/user/import')
    assert maybe_unfrack_path('@')('@foo/bar') == '@foo/bar'
    assert maybe_unfrack_path('@')('@foo/bar/') == '@foo/bar/'
    assert maybe_unfrack_path('@')('@@/home/user/import') == '@@' + unfrackpath('/home/user/import')
    assert maybe_unfrack_path('/')('@/home/user/import') == '@' + unfrackpath('/home/user/import')
    assert maybe_unfrack_path('/')('@/home/user/import') == '@'

# Generated at 2022-06-12 20:14:22.424714
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$/test') == '$/test'
    assert maybe_unfrack_path('$')('$') == '$'

#
# Command line option validators
#



# Generated at 2022-06-12 20:14:26.298852
# Unit test for function add_meta_options
def test_add_meta_options():

    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    result= vars(parser.parse_args(['--force-handlers','--flush-cache']))
    assert result['force_handlers'] == True
    assert result['flush_cache'] == True
#
# Function for ansible-test to add options for commands which require a test subcommand
#

# Generated at 2022-06-12 20:14:35.897562
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    import types
    parser = Mock()
    args = ['-v', '-v']
    ns = argparse.Namespace(v=None)

    action = PrependListAction(option_strings=['-v', '--verbose'], dest='v', nargs=None, const=None, default=None, type=None, help=None, metavar=None)
    action.__call__(parser, ns, args, option_string=None)
    assert ns == argparse.Namespace(v=['-v', '-v'])

    action = PrependListAction(option_strings=['-v', '--verbose'], dest='v', nargs=None, const=None, default=None, type=None, help=None, metavar=None)

# Generated at 2022-06-12 20:14:40.318945
# Unit test for function unfrack_path
def test_unfrack_path():
    import tempfile
    import mock
    path = tempfile.gettempdir()
    path = os.path.normcase(os.path.normpath(path))
    with mock.patch.object(C, 'DEFAULT_MODULE_PATH', path):
        assert unfrack_path()(path) == path
        assert unfrack_path(True)(path) == [path]



# Generated at 2022-06-12 20:14:47.565292
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test the maybe_unfrack_path function
    assert maybe_unfrack_path('@')('@/path') == '@' + unfrackpath('/path')
    assert maybe_unfrack_path('$')('$/path') == '$' + unfrackpath('/path')
    assert maybe_unfrack_path('@')('@@/path') == '@@/path'


#
# Option/OptionGroup-related utils
#

# Generated at 2022-06-12 20:14:51.483720
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    prepend_list_action = PrependListAction('namespace', 'dest', [])
    parser = ''
    namespace = ''
    values = ''
    option_string = ''
    prepend_list_action.__call__(parser, namespace, values, option_string)


#
# Common basic parser
#

# Generated at 2022-06-12 20:14:59.299445
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    path_sep = os.pathsep
    os.pathsep = ':'
    with open('/tmp/test_maybe_unfrack_path.txt', 'w') as f:
        f.write('This is a simple test file')
    assert maybe_unfrack_path('@')('@/tmp/test_maybe_unfrack_path.txt') == '@/tmp/test_maybe_unfrack_path.txt'
    os.remove('/tmp/test_maybe_unfrack_path.txt')
    os.pathsep = path_sep


# Generated at 2022-06-12 20:15:03.314247
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace(object):
        pass
    n = Namespace()
    ensure_value(n, 'test', [])
    assert n.test == [], "Failure on initial call of ensure_value"
    ensure_value(n, 'test', 1)
    assert n.test == [], "Failure on second call of ensure_value"


#
# Functions
#

# Generated at 2022-06-12 20:15:05.260560
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    print('FIXME: test AnsibleVersion.__call__')



# Generated at 2022-06-12 20:15:12.208984
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('-%s' % os.path.sep)('-/path/to/nowhere')
    assert maybe_unfrack_path('-%s' % os.path.sep)('-%s/' % os.path.sep)
    assert maybe_unfrack_path('-%s' % os.path.sep)('b') == 'b'
    assert maybe_unfrack_path('-%s' % os.path.sep)('-') == '-'
    #assert maybe_unfrack_path('-%s' % os.path.sep)('-/') == '-/'
    #assert maybe_unfrack_path('-%s' % os.path.sep)('-@') == '-@'
#
# Option Parsers
#


# Generated at 2022-06-12 20:15:20.927947
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("foo") == "foo"
    assert unfrack_path()("foo:bar") == "foo:bar"
    assert unfrack_path(pathsep=True)("foo:bar") == ["foo", "bar"]



# Generated at 2022-06-12 20:15:23.615592
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('~')('~/test') == '~/test'
    assert maybe_unfrack_path('~')('./test') == './test'

#
# OptionParsers
#

# Generated at 2022-06-12 20:15:29.861351
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(False)('r') == unfrackpath('r')
    assert unfrack_path(False)('.') == unfrackpath('.')
    assert unfrack_path(False)('~/x') == unfrackpath('~/x')
    assert unfrack_path(True)('~/x') == [unfrackpath('~/x')]
    assert unfrack_path(True)('~/x:~/y') == [unfrackpath('~/x'), unfrackpath('~/y')]
    assert unfrack_path(True)('~/x::~/y') == [unfrackpath('~/x'), unfrackpath('~/y')]

# Generated at 2022-06-12 20:15:40.414052
# Unit test for function unfrack_path
def test_unfrack_path():
    print("Testing unfrack_path():")
    print(to_native(unfrack_path()('one/two/three')))
    print(to_native(unfrack_path()('/one/two/three')))
    print(to_native(unfrack_path(pathsep=True)('/one/two/three:/four/five/six')))
    print(to_native(unfrack_path()('one/two/three')))
    print(to_native(unfrack_path()('~/one/two/three')))
    print(to_native(unfrack_path()('one/two/three')))
    print("unfrack_path() looks good.")


# Generated at 2022-06-12 20:15:47.134279
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    class Namespace:
        def __init__(self, a=None, b=None):
            self.a = a
            self.b = b
    # We need to set an option to '-x' so that the argument for this option will be treated as a plain
    # string and not as a file name
    args = ['-x', 'b', '-x', 'c', 'a']
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', action=PrependListAction, dest='a')
    namespace = parser.parse_args(args, namespace=Namespace('a'))
    assert namespace.a == ['b', 'c', 'a']

# Generated at 2022-06-12 20:15:51.863370
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    my_json_path = maybe_unfrack_path('@')('@/path/to/my/file.json')
    assert my_json_path == '@' + unfrackpath('/path/to/my/file.json')
    empty_path = maybe_unfrack_path('@')('')
    assert empty_path == ''



# Generated at 2022-06-12 20:15:56.310112
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/tmp/foo') == '/tmp/foo'
    assert unfrack_path(True)('/tmp/foo') == ['/tmp/foo']
    assert unfrack_path()('/tmp/foo') == '/tmp/foo'
    assert unfrack_path(True)('/tmp/foo:/tmp/bar') == ['/tmp/foo', '/tmp/bar']



# Generated at 2022-06-12 20:16:03.203943
# Unit test for function unfrack_path
def test_unfrack_path():
    """This function uses the pytest framework to execute the unit tests of unfrack_path function.
    This function is in the util module.
    """
    assert unfrack_path()("/dev/null") == "/dev/null"
    assert unfrack_path("")("/dev/null") == ["/dev/null"]
    assert unfrack_path("")("/dev/null:/dev/null") == ["/dev/null", "/dev/null"]
    assert unfrack_path(True)("/dev/null:/dev/null") == ["/dev/null", "/dev/null"]
    assert unfrack_path("")("/dev/null:/dev/null:/dev/null") == ["/dev/null", "/dev/null", "/dev/null"]

# Generated at 2022-06-12 20:16:08.624379
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
  parser = argparse.ArgumentParser()
  parser.add_argument('--file', action=PrependListAction, nargs='*')
  args = parser.parse_args('--file foo bar'.split())
  assert args.file == ['foo', 'bar']
  args = parser.parse_args(''.split())
  assert args.file == []



# Generated at 2022-06-12 20:16:16.562479
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    import StringIO
    import argparse

    class MyParser(argparse.ArgumentParser):
        def format_help(self):
            # capture help from stdout
            old = sys.stdout
            sys.stdout = StringIO.StringIO()
            super(MyParser, self).format_help()
            text = sys.stdout.getvalue()
            sys.stdout = old
            return text

    description_text = "sorting help formatter description"
    epilog_text = "sorting help formatter epilog"

    p = MyParser(description=description_text, epilog=epilog_text,
                 formatter_class=SortingHelpFormatter)

    # add several positional arguments
    p.add_argument('bar')
    p.add_argument('baz', nargs='?')


# Generated at 2022-06-12 20:16:31.655214
# Unit test for function unfrack_path
def test_unfrack_path():
    # Test for function unfrack_path
    assert(unfrack_path()('~/test') == '/home/username/test')
    assert(unfrack_path()('~username/test') == '/home/username/test')



# Generated at 2022-06-12 20:16:42.157424
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('a') == unfrackpath('a')
    assert unfrack_path()('/a') == unfrackpath('/a')
    assert unfrack_path()('a/b') == unfrackpath('a/b')
    assert unfrack_path()('/a/b') == unfrackpath('/a/b')
    assert unfrack_path()('-') == '-'

    assert unfrack_path(pathsep=True)('a') == [unfrackpath('a')]
    assert unfrack_path(pathsep=True)('/a') == [unfrackpath('/a')]
    assert unfrack_path(pathsep=True)('a/b') == [unfrackpath('a/b')]

# Generated at 2022-06-12 20:16:43.385136
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    return None



# Generated at 2022-06-12 20:16:46.372764
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    class Options:
        prog = 'prog'
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action=AnsibleVersion, help='Show the version and exit')
    print(parser.parse_args(['-v'], namespace=Options))



# Generated at 2022-06-12 20:16:51.619082
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    cwd = os.getcwd()
    os.chdir("/tmp")
    print("cwd: %s" %os.getcwd())
    test_paths = ["~/ansible/tmp", "/tmp/ansible/tmp", "$HOME/ansible/tmp"]
    for path in test_paths:
        print("Testing path: %s" %path)
        print("Expect: %s" %os.path.expandvars(os.path.expanduser(path)))
        print("Result: %s" %maybe_unfrack_path("/")(path))
    os.chdir(cwd)


# Generated at 2022-06-12 20:16:55.181032
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action=PrependListAction, nargs='+')
    args = parser.parse_args(['--foo', '1', '2', '--foo', '3', '4'])
    assert args.foo == [3, 4, 1, 2]



# Generated at 2022-06-12 20:17:04.326361
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)(None) == None
    assert unfrack_path(pathsep=True)(None) == None

    # TODO: add tests to cover unfrackpath's behavior
    assert unfrack_path(pathsep=False)("/foo/bar") == "/foo/bar"
    assert unfrack_path(pathsep=True)("/foo/bar") == ["/foo/bar"]
    assert unfrack_path(pathsep=True)("/foo/bar:/bar/foo:/baz/bar") == ["/foo/bar", "/bar/foo", "/baz/bar"]

    assert unfrack_path(pathsep=False)("-") == "-"
    assert unfrack_path(pathsep=True)("-") == "-"


# Generated at 2022-06-12 20:17:05.944325
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    setattr(namespace, self.dest, items)



# Generated at 2022-06-12 20:17:09.673665
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from ansible import __version__
    parser = argparse.ArgumentParser()
    namespace = parser.parse_args(args=[])
    assert(namespace.ansible_version is None)
    ansible_version = AnsibleVersion()
    ansible_version(parser, namespace, False, None)
    assert(namespace.ansible_version == __version__)



# Generated at 2022-06-12 20:17:11.085639
# Unit test for function unfrack_path
def test_unfrack_path():
    """Return simple result for test of unfrack_path function"""
    return unfrack_path()(__file__)

#
# Top level OptionParser
#



# Generated at 2022-06-12 20:17:46.043745
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    version = AnsibleVersion()
    # Mock sys.argv
    sys.argv = ['ansible-2.4.0']
    sys.argv[0] = unfrackpath(sys.argv[0])
    parser = argparse.ArgumentParser()
    namespace = parser.parse_args()
    option_string = '--version'
    version(parser, namespace, None, option_string)
    assert sys.stdout.getvalue() == 'ansible 2.4.0\n'
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    # Catch SystemExit exception
    parser.exit = lambda status=0, message=None: None
    version(parser, namespace, None, option_string)



# Generated at 2022-06-12 20:17:50.886741
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("#")("#/foo/bar/") == "#" + unfrackpath("/foo/bar/")
    assert maybe_unfrack_path("#")("#/foo/") == "#" + unfrackpath("/foo/")
    assert maybe_unfrack_path("#")("#/") == "#" + unfrackpath("/")

# Generated at 2022-06-12 20:17:53.965190
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """Test function maybe_unfrack_path"""
    actual = maybe_unfrack_path(beacon='@')('@/tmp/test')
    expected = '@' + os.path.abspath('/tmp/test')
    assert actual == expected



# Generated at 2022-06-12 20:18:04.464856
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    import pytest
    from ansible.utils.parser import PrependListAction

    class Namespace(object):
        pass
    namespace = Namespace()
    namespace.my_list = []
    action = PrependListAction('-s', dest='my_list', nargs=1,
                               const=None, default=None, type=str,
                               choices=None, required=False, help=None,
                               metavar=None)
    action(parser=None, namespace=namespace, values=['s'])
    assert namespace.my_list == ['s']
    action(parser=None, namespace=namespace, values=['t'])
    assert namespace.my_list == ['t', 's']
    action(parser=None, namespace=namespace, values=['u', 'v'])

# Generated at 2022-06-12 20:18:08.091174
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/etc/ansible') == '/etc/ansible'
    assert unfrack_path()('$HOME/ansible') == os.path.expanduser('~/ansible')
    assert unfrack_path()('/etc/ansible') == '/etc/ansible'
    assert unfrack_path(pathsep=True)('/etc/ansible:/etc') == ['/etc/ansible', '/etc']


# Generated at 2022-06-12 20:18:15.505418
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument = mock.MagicMock()
    parser.exit = mock.MagicMock()
    parser.prog = 'ansible'
    action = AnsibleVersion(option_strings='--version')
    action(parser, None, None, None)
    assert parser.add_argument.called
    assert parser.exit.called


#
# General purpose functions
#

# Generated at 2022-06-12 20:18:23.979680
# Unit test for function unfrack_path
def test_unfrack_path():
    os.environ['ANSIBLE_CONFIG'] = "/home/me/.ansible.cfg"
    os.environ['ANSIBLE_DATA_DIR'] = "/home/me/.ansible"
    os.environ['ANSIBLE_LIBRARY'] = "/home/me/.ansible/lib"
    os.environ['ANSIBLE_ROLES_PATH'] = "/home/me/.ansible/roles"
    os.environ['ANSIBLE_PRIVATE_ROLES_PATH'] = "/home/me/.ansible/private_roles:/etc/ansible/private_roles"

    assert unfrack_path()('~/tmp') == '/home/me/tmp'
    assert unfrack_path()('hidden/tmp') == os.path.expanduser('~/hidden/tmp')
    assert unfrack_path

# Generated at 2022-06-12 20:18:30.870588
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test strings
    test_str = [
        '!foo/bar',
        './foo/bar',
    ]
    # Test dict
    test_dict = [
        {'foo': '!foo/bar'},
        {'foo': './foo/bar'},
    ]

    for s in test_str:
        print(maybe_unfrack_path('!')(s))

    for d in test_dict:
        print(maybe_unfrack_path('!')(d))



# Generated at 2022-06-12 20:18:37.696143
# Unit test for function unfrack_path
def test_unfrack_path():
    # the actual path doesn't matter, just that it is a single string
    assert(unfrack_path()('/path/test')) == '/path/test'
    assert(unfrack_path(True)('/path/test:/path/test2') == ['/path/test', '/path/test2'])
    assert(unfrack_path(True)('/path/test') == ['/path/test'])
    assert(unfrack_path(True)('/path/test:') == ['/path/test', ''])
    assert(unfrack_path(True)('') == [])
    assert(unfrack_path(True)(':') == ['', ''])

# Generated at 2022-06-12 20:18:46.238237
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
	from ansible.parsing.dataloader import DataLoader
	from ansible.vars.manager import VariableManager
	from ansible.inventory.manager import InventoryManager
	from ansible.playbook.play import Play
	from ansible.executor.task_queue_manager import TaskQueueManager
	from ansible.plugins.callback import CallbackBase
	from ansible.executor.playbook_executor import PlaybookExecutor
	from ansible.utils.ssh_functions import check_for_controlpersist
	from ansible.errors import AnsibleParserError
	from ansible.config.manager import ConfigManager
	import os
	import yaml
	import json
	

# Generated at 2022-06-12 20:20:00.778888
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument("--foo", action="store_false", help="foo help")
    parser.add_argument("--bar", action="store_true", help="bar help")
    parser.add_argument("--baz", action="store", help="baz help")
    parser.add_argument("--qux", action="store_const", const=42, help="qux help")
    parser.add_argument("--norf", action="store_false", help="norf help")
    parser.print_help()


# Generated at 2022-06-12 20:20:03.606739
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser=argparse.ArgumentParser(prog='ansible')
    fake_version='foo'
    setattr(parser, 'prog',fake_version)
    AnsibleVersion()(parser, None, None, None)



# Generated at 2022-06-12 20:20:09.400924
# Unit test for function unfrack_path
def test_unfrack_path():
    test_vals = [
        ('/path/to/file', '/path/to/file'),
        ('../test/test/test/test', '../test/test/test/test'),
        ('~', '~'),
        ('~/test/test/test', '~/test/test/test'),
        ('~/test/../test', '~/test/../test'),
        ('file', 'file'),
        ('/home/user/test.yml', '/home/user/test.yml'),
        ('/path/to/../test/test/test.yml', '/path/to/../test/test/test.yml'),
        ('test', 'test'),
        ('test/test/test/test.yml', 'test/test/test/test.yml'),
    ]

# Generated at 2022-06-12 20:20:12.381743
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    sys.argv[1:] = ["--version"]
    assert version() == "ansible-playbook {0}".format(__version__)
    sys.argv[1:] = ["-v"]
    assert version() == "ansible-playbook {0}".format(__version__)



# Generated at 2022-06-12 20:20:21.474589
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', action=PrependListAction)
    args = parser.parse_args(['-f', 'file1', 'file2'])
    assert args.filename == ['file2', 'file1']
    with pytest.raises(ValueError):
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', action=PrependListAction, nargs=0)
    with pytest.raises(ValueError):
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', action=PrependListAction, const=1, nargs=2)
#
# Functions to find ansible and its subdirectories
#

# Generated at 2022-06-12 20:20:29.350959
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    a = PrependListAction(option_strings=['--list'], dest='list', nargs=1, const=None, default='default', type=None, choices=None, required=False, help=None, metavar=None)
    b = argparse.Namespace()
    setattr(b, a.dest, [])
    a(parser="", namespace=b, values=['value'], option_string=None)
    assert(getattr(b, a.dest) == ['value'])



# Generated at 2022-06-12 20:20:33.312389
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--ansible-version', dest='ansible_version', action=AnsibleVersion, default=argparse.SUPPRESS, help="Show program's Ansible version number and exit.")
    args = parser.parse_args(['--ansible-version'])
    assert args.ansible_version == to_native(version(parser.prog))



# Generated at 2022-06-12 20:20:35.175171
# Unit test for function version
def test_version():
    v = version()
    assert len(v.split("\n")) == 13

# Generated at 2022-06-12 20:20:37.497670
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    teststr = '~/test'
    resultstr = maybe_unfrack_path('~')(teststr)
    expectedstr = os.path.expanduser(teststr)
    assert resultstr == expectedstr


# Generated at 2022-06-12 20:20:38.988073
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    assert True

#
# Option Parser Initialization
#
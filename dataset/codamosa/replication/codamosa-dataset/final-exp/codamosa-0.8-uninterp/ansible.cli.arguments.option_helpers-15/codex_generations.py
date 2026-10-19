

# Generated at 2022-06-12 20:12:10.452735
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser(
        prog="test",
        formatter_class=SortingHelpFormatter,
        conflict_handler='resolve',
    )
    add_check_options(parser)
    args = parser.parse_args('-C -D'.split())
    assert args.check is True
    assert args.diff is True
    args = parser.parse_args('--syntax-check'.split())
    assert args.syntax is True


# Generated at 2022-06-12 20:12:14.475275
# Unit test for function unfrack_path
def test_unfrack_path():
    passed = True
    cwd = os.getcwd()
    try:
        os.chdir(os.path.expanduser('~'))
        if "~" not in unfrack_path()("~/.ansible/tmp"):
            passed = False
    finally:
        os.chdir(cwd)

    return passed


# Generated at 2022-06-12 20:12:18.675283
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    opts = parser.parse_args(['-t', 'foo', '-t', 'bar', '--skip-tags', 'foo'])
    assert opts.tags == ['foo', 'bar']
    assert opts.skip_tags == ['foo']



# Generated at 2022-06-12 20:12:28.009680
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    args_prefix = parser.parse_args('')
    assert args_prefix.one_line is None
    assert args_prefix.tree is None
    args_one_line = parser.parse_args('--one-line')
    assert args_one_line.one_line is True
    assert args_one_line.tree is None
    args_tree = parser.parse_args('--tree /root/tmp')
    assert args_tree.one_line is None
    assert args_tree.tree == '/root/tmp'


# Generated at 2022-06-12 20:12:32.701211
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/tmp') == '/tmp'
    assert unfrack_path(True)('/tmp:') == ['/tmp']
    assert unfrack_path(True)('/tmp:/foo') == ['/tmp', '/foo']



# Generated at 2022-06-12 20:12:41.691020
# Unit test for function add_connect_options
def test_add_connect_options():
    from ansible.utils import context_objects as co

    args = ['-u', 'dude', '--private-key', 'a', '--connection', 'local', '--connection-password-file', 'b',
            '--ssh-common-args', 'c', '--sftp-extra-args', 'd', '--scp-extra-args', 'e', '--ssh-extra-args', 'f',
            '--timeout', '1000']

    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    parsed = parser.parse_args(args=args)

    assert parsed.remote_user == 'dude'
    assert parsed.private_key_file == unfrackpath('a')
    assert parsed.connection == 'local'

# Generated at 2022-06-12 20:12:43.985373
# Unit test for function add_meta_options
def test_add_meta_options():
    parser=argparse.ArgumentParser(description='test')
    add_meta_options(parser)
    assert len(parser._actions)==2


# Generated at 2022-06-12 20:12:49.271891
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser(prog='ansible-playbook')
    add_vault_options(parser)
    args = parser.parse_args(['--vault-id', 'ident1@prompt',
                              '--vault-id', 'ident2',
                              '--ask-vault-password',
                              '--vault-password-file', 'file1',
                              '--vault-password-file', 'file2'])
    assert args.vault_ids == ['ident1@prompt', 'ident2']
    assert args.ask_vault_pass
    assert args.vault_password_files == ['file1', 'file2']


#
# Functions to build subcommand parsers
#


# Generated at 2022-06-12 20:12:52.161283
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser(prog='ansible')
    add_output_options(parser)
    return parser



# Generated at 2022-06-12 20:13:02.031078
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/')("/ansible/roles/role") == "/ansible/roles/role"
    assert maybe_unfrack_path('/')("/ansible/roles/role/") == "/ansible/roles/role/"
    assert maybe_unfrack_path('/')("~/ansible/roles/role") == "~/ansible/roles/role"
    assert maybe_unfrack_path('~/')("~/ansible/roles/role") == "/home/user/ansible/roles/role"
    assert maybe_unfrack_path('~/')("~user/ansible/roles/role") == "~user/ansible/roles/role"



# Generated at 2022-06-12 20:13:19.926932
# Unit test for function add_runtask_options
def test_add_runtask_options():
    parser = argparse.ArgumentParser(prog = 'TESTING', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40, width=100))
    add_runtask_options(parser)
    options = parser.parse_args(args=['-e', '"foo=bar"', '-e', '@extra_variables_file.yaml'])
    assert options.extra_vars == ['"foo=bar"', '@extra_variables_file.yaml']



# Generated at 2022-06-12 20:13:22.736554
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = argparse.ArgumentParser(prog="ansible")
    add_runas_options(parser)
    argv = ["-b",
            "--become-method", "test",
            "--become-user", "test"
            ]
    options = parser.parse_args(argv)
    assert options.become
    assert options.become_method == "test"
    assert options.become_user == "test"



# Generated at 2022-06-12 20:13:25.063738
# Unit test for function add_async_options
def test_add_async_options():
    parser=argparse.ArgumentParser()
    add_async_options(parser)
    parser.parse_args(['-B', '1'])

# Generated at 2022-06-12 20:13:33.064013
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_paths = (
        ('file', 'file'),
        ('@file', '@/etc/ansible/file'),
        ('@@file', '@@file'),
        ('@/file', '@/file'),
    )

    for (path, expected) in test_paths:
        assert maybe_unfrack_path('@')(path) == expected



# Generated at 2022-06-12 20:13:40.773810
# Unit test for function add_runas_options
def test_add_runas_options():

    class test_args:
        pass

    # Test add_runas_options with all possible options
    my_args1 = test_args()
    my_args1.become = True
    my_args1.become_method = "su"
    my_args1.become_user = "root"
    my_args1.become_ask_pass = True
    my_args1.become_pass = "password"

    assert my_args1.become == True
    assert my_args1.become_method == "su"
    assert my_args1.become_user == "root"
    assert my_args1.become_ask_pass == True
    assert my_args1.become_pass == "password"

    # Test add_runas_options with some options
    my_args

# Generated at 2022-06-12 20:13:48.017260
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    parser = argparse.ArgumentParser()
    runas_group = parser.add_argument_group("Privilege Escalation Options")
    add_runas_prompt_options(parser, runas_group)
    options = parser.parse_args(shlex.split('-K'))
    assert True is options.become_ask_pass
    options = parser.parse_args(shlex.split('--become-pass-file=somefile'))
    assert 'somefile' == options.become_password_file



# Generated at 2022-06-12 20:13:52.172759
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = SortingHelpFormatter()
    parser.add_argument('--foo')
    parser.add_argument('--bar')
    assert parser.format_help() == 'usage: prog [--bar BAR] [--foo FOO]\n\noptional arguments:\n  --bar BAR\n  --foo FOO\n'


# Generated at 2022-06-12 20:13:57.148788
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser()
    add_async_options(parser)
    arr = ['-P', '20', '-B', '30']
    nsp = parser.parse_args(arr)
    assert nsp.poll_interval == 20, "error with parsing options for poll_interval"
    assert nsp.seconds == 30, "error with parsing options for background"



# Generated at 2022-06-12 20:14:03.973343
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    class Parser(object):
        def __init__(self, prog_name):
            self.prog = prog_name
        def exit(self):
            pass

    class ParseArgs(object):
        ansible_version_action = AnsibleVersion(None, None, None, None)
        def __init__(self):
            self.parser = Parser(None)
        def run(self):
            self.ansible_version_action(self.parser, None, None, None)

    t = ParseArgs()
    t.run()
# Unit test case for ArgumentParser.exit()

# Generated at 2022-06-12 20:14:08.772298
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion, nargs=0, help='Show Ansible version number and exit')
    parser.parse_args('--version'.split())
    parser.execute()
    parser.parse_args('--version -v'.split())
    parser.execute()

# Generated at 2022-06-12 20:14:24.557078
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/etc') == '/etc'
    assert unfrack_path()('/etc:.') == '/etc'
    assert unfrack_path(pathsep=True)('/etc') == ['/etc']
    assert unfrack_path(pathsep=True)('/etc:.') == ['/etc', '.']
    assert unfrack_path()('~/path') == os.path.expanduser('~/path')
    assert unfrack_path()('~/path:.') == os.path.expanduser('~/path')
    assert unfrack_path(pathsep=True)('~/path:.') == [os.path.expanduser('~/path'), '.']

# Generated at 2022-06-12 20:14:31.597193
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    """Verify that the constructor of ``PrependListAction`` does not raise an exception."""
    # pylint: disable=unused-variable
    action = PrependListAction(
        option_strings=['-f', '--foo'],
        dest='foo',
        nargs=None,
        const=None,
        default='abc',
        type="unicode",
        choices=None,
        required=False,
        help=None,
        metavar='BAR'
    )



# Generated at 2022-06-12 20:14:34.279059
# Unit test for function version
def test_version():
    assert isinstance(version(), str)
    assert isinstance(version(''), str)
    assert isinstance(version('ansible-test'), str)


#
# Options Definitions
#

# Generated at 2022-06-12 20:14:39.080412
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('--help')
    parser.add_argument('-a')
    parser.add_argument('-b')
    parser.add_argument('--zzz')
    parser.add_argument('--long')
    try:
        parser.parse_args()
    except SystemExit as e:
        assert e.code == 0



# Generated at 2022-06-12 20:14:45.109560
# Unit test for function unfrack_path
def test_unfrack_path():
    for path in "./path", '~/path', '/path', 'c:\\path':
        assert unfrack_path()(path) == os.path.expanduser(path)
        assert unfrack_path(pathsep=True)(path + os.pathsep + path) == [os.path.expanduser(path), os.path.expanduser(path)]


# Generated at 2022-06-12 20:14:49.542696
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = argparse.ArgumentParser(description='add_fork_options test')
    add_fork_options(parser)
    options = parser.parse_args([])
    assert isinstance(options.forks, int)
    assert options.forks == C.DEFAULT_FORKS



# Generated at 2022-06-12 20:14:54.438552
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    options = parser.parse_args(['-i', 'a.b.com,c.d.com', '-l', 'some_pattern'])
    assert options.inventory == ['a.b.com,c.d.com']
    assert options.subset == 'some_pattern'
    assert not options.listhosts



# Generated at 2022-06-12 20:14:58.852277
# Unit test for function ensure_value
def test_ensure_value():
    namespace = argparse.Namespace(foo=None)
    ensure_value(namespace, 'foo', 3)
    assert namespace.foo == 3
    namespace = argparse.Namespace(bar=None)
    ensure_value(namespace, 'bar', [3, 2, 1])
    assert namespace.bar == [3, 2, 1]


#
# Option Parser factories
#

# Generated at 2022-06-12 20:15:07.174537
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    p = argparse.ArgumentParser()
    p.add_argument('--foo', dest='foo', action=PrependListAction, nargs='*', metavar='LIST')
    p.add_argument('--bar', dest='bar', action='append', nargs='*', metavar='LIST')
    p.add_argument('-b', dest='b', action='store_true')
    p.add_argument('-c', dest='c', action='store_false')
    p.add_argument('-d', dest='d', action='store', nargs='?')
    p.add_argument('-e', dest='e', action='store_const', const='x')
    p.add_argument('-f', dest='f', action='append_const', const='x')

# Generated at 2022-06-12 20:15:19.116393
# Unit test for function unfrack_path
def test_unfrack_path():
    """A unit test for function unfrack_path"""

# Generated at 2022-06-12 20:15:36.627535
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from ansible.cli import CLI
    from unittest import mock
    import pkg_resources
    m = mock.mock_open()
    with mock.patch('builtins.open', m, create=True):
        mock_get_dist = mock.MagicMock(spec_set=pkg_resources.get_distribution, project_name="", version="")
        pkg_resources.get_distribution.return_value = mock_get_dist
        cli = CLI(None, None)
        cli.parser = mock.MagicMock()
        av = AnsibleVersion("a", "b", "c", "d", "e")
        av.__call__(cli.parser, None, None, None)
        cli.parser.exit.assert_called_once()

# Generated at 2022-06-12 20:15:45.888540
# Unit test for function unfrack_path
def test_unfrack_path():
    option, envvar = C.DEFAULT_LOCAL_TMP, 'ANSIBLE_REMOTE_TEMP'
    default = '/tmp'

    # Test with pathsep
    assert unfrack_path(pathsep=True)('{0}:/tmp/foo'.format(option)) == [option, '/tmp/foo']
    os.environ[envvar] = '/tmp/bar'
    assert unfrack_path(pathsep=True)('$ANSIBLE_REMOTE_TEMP:/tmp/foo') == ['/tmp/bar', '/tmp/foo']
    del os.environ[envvar]

    # Test without pathsep
    assert unfrack_path()(option) == option
    assert unfrack_path()('$ANSIBLE_REMOTE_TEMP') == default

# Generated at 2022-06-12 20:15:47.500655
# Unit test for function version
def test_version():
    # Check for valid output
    assert(version("prog"))
    assert(version("prog") == version("prog"))

# Generated at 2022-06-12 20:15:51.862675
# Unit test for function add_check_options
def test_add_check_options():
    class args:
        pass

    parser = argparse.ArgumentParser()
    add_check_options(parser)
    a = args
    parser.parse_args(['--check', '--syntax-check', '--diff'], namespace=a)
    assert a.check
    assert a.syntax
    assert a.diff



# Generated at 2022-06-12 20:15:58.980568
# Unit test for function add_check_options
def test_add_check_options():
    parser=argparse.ArgumentParser()
    add_check_options(parser)
    test_parser=parser.parse_args(['--check',"-D"])
    if test_parser.check!=True:
        raise AssertionError
    if test_parser.syntax!=False:
        raise AssertionError
    if test_parser.diff!=True:
        raise AssertionError



# Generated at 2022-06-12 20:16:02.373290
# Unit test for function add_check_options
def test_add_check_options():
    p = argparse.ArgumentParser()
    add_check_options(p)
    args = p.parse_args(['--diff', '--syntax-check', '--check'])
    assert args.diff == True
    assert args.syntax == True
    assert args.check == True
    test_check_options = test_add_check_options()


# Generated at 2022-06-12 20:16:12.301834
# Unit test for function version
def test_version():
    # include a bunch of special chars in the test, to make sure they don't break formatting, etc
    ansible.__version__ = '\n2.0.0.0-alpha3\\/'
    C.CONFIG_FILE = './ansible.cfg'
    C.DEFAULT_MODULE_PATH = '/usr/share/ansible/modules'
    ansible.__path__ = ['/usr/lib/python2.7/dist-packages/ansible']
    C.COLLECTIONS_PATHS = ['/usr/share/ansible/collections']
    sys.argv = ['/usr/bin/ansible-playbook', 'playbook.yml']
    sys.version = 'Python 2.7.17 (default, Nov  7 2019, 10:07:09)\n[GCC 7.4.0]'

# Generated at 2022-06-12 20:16:16.638003
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    options = parser.parse_args(["-C", "--syntax-check", "-D", "--diff"])
    assert options.check == True
    assert options.syntax == True
    assert options.diff == True


# Generated at 2022-06-12 20:16:20.139317
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion)
    args = parser.parse_args(['--version'])
    if args.version is not None:
        sys.exit(1)


# Generated at 2022-06-12 20:16:23.811294
# Unit test for function add_basedir_options
def test_add_basedir_options():
    obj = argparse.ArgumentParser()
    add_basedir_options(obj)
    assert obj.parse_args(['--playbook-dir', 'test_add_basedir_options']).basedir == 'test_add_basedir_options'



# Generated at 2022-06-12 20:16:30.012986
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    print(version('ansible-console'))



# Generated at 2022-06-12 20:16:41.545873
# Unit test for function unfrack_path
def test_unfrack_path():
    def test(func, arg, result):
        res = func(arg)
        if res != result:
            raise AssertionError("Result for arg '%s': '%s' != '%s'" % (arg, res, result))

    test(unfrack_path(), '-', '-')
    test(unfrack_path(), '~/relative/path', '~/relative/path')
    test(unfrack_path(), '/absolute/path', '/absolute/path')
    test(unfrack_path(), '$HOME/relative/path', '$HOME/relative/path')
    test(unfrack_path(), '$HOME/relative/$HOME', '$HOME/relative/$HOME')
    test(unfrack_path(), '$HOME/relative/~', '$HOME/relative/~')

# Generated at 2022-06-12 20:16:51.434233
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
        parser = argparse.ArgumentParser()
        args = parser.parse_args([])
        os.environ["ANSIBLE_VERSION_CHECK"] = "False"
        os.environ["ANSIBLE_VERSION_SKIP"] = "False"
        os.environ["ANSIBLE_TRANSPORT"] = "smart"
        os.environ["ANSIBLE_SCP_IF_SSH"] = "ssh"
        os.environ["ANSIBLE_SFTP_BATCH_MODE"] = "False"
        os.environ["ANSIBLE_SUDO_FLAGS"] = "False"
        os.environ["ANSIBLE_SSH_RETRIES"] = "False"
        os.environ["ANSIBLE_SSH_PIPELINING"] = "False"
        os.environ["ANSIBLE_NOCOWS"]

# Generated at 2022-06-12 20:16:58.404932
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    '''Ensures that the `PrependListAction` class is instantiatable and exposes the same
    interface as `argparse._AppendAction`'''
    try:
        import argparse
    except ImportError:
        return

    test_option_strings = ['-t', '--test']
    test_dest = 'test'
    test_nargs = None
    test_const = None
    test_default = None
    test_type = None
    test_choices = None
    test_required = False
    test_help = None
    test_metavar = None

    # Ensure that the class is instantiatable

# Generated at 2022-06-12 20:17:02.103079
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser(prog='test_AnsibleVersion___call__')
    parser.add_argument('--version', action=AnsibleVersion)
    args = parser.parse_args(['--version'])
    assert True



# Generated at 2022-06-12 20:17:07.102099
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('foo') == 'foo'
    assert unfrack_path()('.') == '.'
    assert unfrack_path(pathsep=True)('foo:bar') == ['foo', 'bar']
    assert unfrack_path(pathsep=True)('foo:bar:') == ['foo', 'bar']
    assert unfrack_path(pathsep=True)('') == []



# Generated at 2022-06-12 20:17:11.095269
# Unit test for function version
def test_version():
    """
    :return:
    """
    from ansible.utils.display import Display
    from ansible.plugins.loader import fragment_loader

    raw = "tests/unit/utils/argparsing/ansible_v.txt"
    exp = fragment_loader.get_fragment('cli.version', 'exp', raw)
    with Display(width=80, verbosity=6):
        res = version()
    assert res == exp
# ==========================================================
# main
#

# Generated at 2022-06-12 20:17:15.561665
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/usr/local/bin:/usr/bin:/bin') == ['/usr/local/bin', '/usr/bin', '/bin']
    assert unfrack_path(pathsep=False)('/usr/local/bin') == '/usr/local/bin'
    assert unfrack_path(pathsep=False)('-') == '-'



# Generated at 2022-06-12 20:17:20.937595
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/dev/null') == '/dev/null'
    assert unfrack_path()('relative/path') == 'relative/path'
    assert unfrack_path()('~/home/path') == os.path.expanduser('~/home/path')


#
# Special purpose Options
#

# Generated at 2022-06-12 20:17:27.825115
# Unit test for function unfrack_path
def test_unfrack_path():
    assert 'directory/import.yml' == unfrack_path(pathsep=False)('directory/import.yml')
    assert 'directory/import.yml' == unfrack_path(pathsep=False)('../directory/import.yml')
    assert 'directory/import.yml' == unfrack_path(pathsep=False)('/absolute/directory/import.yml')
    assert 'directory/import.yml' == unfrack_path(pathsep=False)('~/directory/import.yml')
    assert 'directory/import.yml' == unfrack_path(pathsep=False)('~/directory/import.yml')
    assert 'directory/import.yml' == unfrack_path(pathsep=False)('../~/directory/import.yml')

# Generated at 2022-06-12 20:17:47.980807
# Unit test for function ensure_value
def test_ensure_value():
    class mockNamespace(object):
        """an empty class meant to act like ArgumentParser.Namespace"""
        pass

    ns = mockNamespace()
    ensure_value(ns, "foo", [])
    assert getattr(ns, "foo", None) == []
    ensure_value(ns, "foo", [])
    assert getattr(ns, "foo", None) == []
    ensure_value(ns, "bar", "hello")
    assert getattr(ns, "bar", None) == "hello"


# Generated at 2022-06-12 20:17:48.962192
# Unit test for function version
def test_version():
    assert isinstance(version(), str)



# Generated at 2022-06-12 20:17:56.535620
# Unit test for function unfrack_path
def test_unfrack_path():
    a = unfrack_path()
    if os.name == 'nt':
        assert a(r'C:\a\b') == os.path.normpath(r'C:\a\b')
        assert a(r'C:\\a\\b') == os.path.normpath(r'C:\a\b')
        assert a(r'~\a\b') == os.path.normpath(r'~\a\b')
        assert a(r'~\\a\\b') == os.path.normpath(r'~\a\b')
        assert a(r'c:\Program Files\Git\a\b') == os.path.normpath(r'c:\Program Files\Git\a\b')

# Generated at 2022-06-12 20:18:00.487459
# Unit test for function unfrack_path
def test_unfrack_path():
    f = unfrack_path()
    assert f('foobar') == unfrackpath('foobar')
    f = unfrack_path(pathsep=True)
    assert f('foo:bar') == [unfrackpath('foo'), unfrackpath('bar')]


# Generated at 2022-06-12 20:18:07.963121
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    script='ansible-config'
    test_parser = argparse.ArgumentParser()
    test_parser.add_argument('--version', action=AnsibleVersion)
    test_args = ['--version']

# Generated at 2022-06-12 20:18:19.274842
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--foo')
    parser.add_argument('-b')
    parser.add_argument('-a')
    parser.add_argument('-c')
    parser.add_argument('-a', dest='a2')
    parser.add_argument('-c', dest='c2')
    parser.add_argument('-d', help='d help')
    parser.add_argument('-b', dest='b2')
    parser.add_argument('--bar')
    parser.add_argument('-e', dest='e2')
    parser.add_argument('-f', dest='f2')
    parser.print_help()


# Generated at 2022-06-12 20:18:23.283565
# Unit test for function ensure_value
def test_ensure_value():
    argparse.ArgumentParser.ensure_value = ensure_value
    p = argparse.ArgumentParser()
    p.add_argument('--foo', '-f', dest='foo', action='ensure_value', ensure_value=1)
    ns = p.parse_args([])
    assert ns.foo, "Failed to insert default value into Namespace"



# Generated at 2022-06-12 20:18:33.122384
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)("/etc/ansible"
        ) == "/etc/ansible"
    assert unfrack_path(pathsep=False)("~/.ansible"
        ) == "~/.ansible"
    assert unfrack_path(pathsep=False)("~/ansible/playbooks"
        ) == "~/ansible/playbooks"
    assert unfrack_path(pathsep=False)("/home/someuser/ansible/playbooks"
        ) == "/home/someuser/ansible/playbooks"
    assert unfrack_path(pathsep=False)("/etc/ansible/plays"
        ) == "/etc/ansible/plays"

# Generated at 2022-06-12 20:18:37.487131
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace(object):
        def __init__(self):
            self.foo = None

    ns = Namespace()
    result = ensure_value(ns, 'foo', 42)
    assert result == 42, result
    assert ns.foo == 42, ns.foo

    ns.foo = 1
    result = ensure_value(ns, 'foo', 2)
    assert result == 1, result
    assert ns.foo == 1, ns.foo



# Generated at 2022-06-12 20:18:45.816072
# Unit test for function ensure_value
def test_ensure_value():
    test_class = type('Test', (object,), {})()
    ensure_value(test_class, 'testattr', 5)
    assert test_class.testattr == 5
    ensure_value(test_class, 'testattr', 7)
    assert test_class.testattr == 5
    assert ensure_value(test_class, 'testattr2', []) == []
    assert test_class.testattr2 == []
    assert ensure_value(test_class, 'testattr2', [1, 2, 2]) == []
    assert test_class.testattr2 == []
    ensure_value(test_class, 'testattr2', None)
    assert test_class.testattr2 is None

#
# Options that are used for all programs in ansible
#


# Generated at 2022-06-12 20:19:25.830355
# Unit test for function version
def test_version():
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 3

# Generated at 2022-06-12 20:19:29.343255
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = to_native(version())
    assert "ansible" in ansible_version
    assert "python" in ansible_version
    assert __version__ in ansible_version



# Generated at 2022-06-12 20:19:33.758798
# Unit test for function unfrack_path
def test_unfrack_path():
    import tempfile
    from ansible.utils.path import makedirs_safe
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.six.moves import configparser
    for pathsep in (False, True):
        unfrack_path_func = unfrack_path(pathsep)
        localpath = tempfile.mkdtemp()
        distpath = tempfile.mkdtemp()
        config = configparser.SafeConfigParser()
        config.add_section('defaults')
        config.set('defaults', 'ansible_managed', '#')
        config.set('defaults', 'roles_path', os.path.join(localpath, 'roles'))
        config.set('defaults', 'library', os.path.join(localpath, 'library'))


# Generated at 2022-06-12 20:19:39.000423
# Unit test for function version
def test_version():
    """ test_version """
    assert version('/foo') == "-/- [core ]\n  config file = /foo\n  configured module search path = Default w/o overrides\n  ansible python module location = /foo\n  ansible collection location = /foo\n  executable location = /foo\n  python version = \n  jinja version = \n  libyaml = None\n"


# Generated at 2022-06-12 20:19:40.769611
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = to_native(version("ansible-vault"))
    print(ansible_version)



# Generated at 2022-06-12 20:19:48.983689
# Unit test for function unfrack_path
def test_unfrack_path():
    # test against other than absolute path
    assert unfrack_path()('../to/home/ansible.cfg') == unfrackpath('../to/home/ansible.cfg')
    assert unfrack_path()('~/ansible.cfg') == unfrackpath('~/ansible.cfg')
    assert unfrack_path()('/path/to/ansible/ansible.cfg') == unfrackpath('/path/to/ansible/ansible.cfg')
    # test against absolute path (should return unchanged)
    assert unfrack_path()('/../to/home/ansible.cfg') == '/../to/home/ansible.cfg'
    assert unfrack_path()('/home/user/ansible.cfg') == '/home/user/ansible.cfg'

# Generated at 2022-06-12 20:19:58.063628
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    import argparse, tempfile
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-f', action='store')
    parser.add_argument('-b', action='store')
    parser.add_argument('-c', action='store')
    tf = tempfile.TemporaryFile()
    parser.print_help(file=tf)
    tf.seek(0)
    lines = tf.readlines()
    if len(lines) != 5 or '-b' not in lines[1] or '-c' not in lines[2] or '-f' not in lines[3]:
        raise ValueError("unexpected help format, lines=%s" % lines)

# The superclass of the following option parser classes
# This class is not used directly.

# Generated at 2022-06-12 20:20:00.418961
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion)
    args = parser.parse_args()



# Generated at 2022-06-12 20:20:04.677321
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=True)("one:two:three:four:five") == ['one', 'two', 'three', 'four', 'five']
    assert unfrack_path(pathsep=False)("one:two:three:four:five") == 'one:two:three:four:five'
    assert unfrack_path(pathsep=False)("-") == '-'



# Generated at 2022-06-12 20:20:13.339428
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('/nonexist/file') == '/nonexist/file'
    assert unfrack_path(pathsep=False)('~/nonexist/file') == os.path.expanduser('~/nonexist/file')
    assert unfrack_path(pathsep=False)('~/nonexist/file') != '~/nonexist/file'
    assert unfrack_path(pathsep=True)('/nonexist/file') == ['/nonexist/file']
    assert unfrack_path(pathsep=True)('/nonexist/file' + os.pathsep) == ['/nonexist/file']

# Generated at 2022-06-12 20:20:57.225223
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('c', help='c help')
    parser.add_argument('d', help='d help')
    parser.add_argument('x', help='x help')
    parser.add_argument('a', help='a help')
    parser.add_argument('b', help='b help')
    args = parser.parse_args([])
    help = parser.format_help()

    assert help.index('c help') < help.index('d help')
    assert help.index('d help') < help.index('x help')
    assert help.index('x help') < help.index('a help')
    assert help.index('a help') < help.index('b help')


#
# Main
#

# Generated at 2022-06-12 20:21:04.074615
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("/dev/null") == "/dev/null"
    assert unfrack_path(pathsep=True)("/dev/null:/tmp") == ["/dev/null", "/tmp"]
    assert unfrack_path()("~/blah") == os.path.expanduser("~/blah")
    assert unfrack_path(pathsep=True)("~/blah:/tmp") == [os.path.expanduser("~/blah"), "/tmp"]


# Generated at 2022-06-12 20:21:04.762660
# Unit test for function version
def test_version():
    assert 'ansible --version' in version()

# Generated at 2022-06-12 20:21:05.838959
# Unit test for function version
def test_version():
    assert version().startswith('2.0')



# Generated at 2022-06-12 20:21:08.948333
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path('/foo:/bar') == ['/foo', '/bar']
    assert unfrack_path('/foo') == '/foo'
    assert unfrack_path('-') == '-'



# Generated at 2022-06-12 20:21:17.376625
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from ansible.cli import CLI
    from ansible.cli.arguments import option_helpers as opt_help

    args = ["version"]

# Generated at 2022-06-12 20:21:23.531634
# Unit test for function unfrack_path
def test_unfrack_path():
    '''Test function unfrack_path'''
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 1

    # test %(basedir)s
    curdir = os.path.dirname(os.path.realpath(__file__))
    basedir = os.path.realpath(os.path.join(curdir, '../../'))
    assert unfrack_path(pathsep=False)('%(basedir)s') == basedir

    # test %(cwd)s
    cwd = os.getcwd()
    assert unfrack_path(pathsep=False)('%(cwd)s') == cwd

    # test %(home)s
    if os.environ.get('HOME') is not None:
        home = os.path

# Generated at 2022-06-12 20:21:31.555827
# Unit test for function unfrack_path
def test_unfrack_path():

    # Check single path
    path = '/usr/share/ansible/my_plugins'
    expected_path = ['/usr/share/ansible/my_plugins']
    assert unfrack_path()(path) == expected_path

    # Check multiple paths
    path = '/usr/share/ansible/my_plugins:/usr/share/ansible/lib:/usr/share/ansible/plugins'
    expected_path = ['/usr/share/ansible/my_plugins', '/usr/share/ansible/lib', '/usr/share/ansible/plugins']
    assert unfrack_path(pathsep=True)(path) == expected_path


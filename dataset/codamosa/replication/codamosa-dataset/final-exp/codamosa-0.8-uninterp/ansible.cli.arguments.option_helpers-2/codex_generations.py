

# Generated at 2022-06-12 20:12:07.113550
# Unit test for function unfrack_path
def test_unfrack_path():
    os.environ['ANSIBLE_CONFIG'] = 'sample'
    os.environ['ANSIBLE_CONFIG_DIR'] = 'sample_2'
    os.environ['ANSIBLE_CONFIG_FILE'] = '/usr/local/etc/ansible/sample.cfg'
    os.environ['ANSIBLE_CONFIG_MODULE_PATH'] = '/usr/share/modules'
    os.environ['ANSIBLE_LIBRARY'] = 'sample_3'
    os.environ['ANSIBLE_LOG_PATH'] = 'sample_4'
    os.environ['ANSIBLE_NOCOWS'] = '1'
    os.environ['ANSIBLE_NOCOLOR'] = '1'
    os.environ['ANSIBLE_STDOUT_CALLBACK'] = 'default'

# Generated at 2022-06-12 20:12:15.829830
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    options,args = parser.parse_known_args()
    assert options.connection == C.DEFAULT_TRANSPORT
    assert options.ssh_common_args == None
    assert options.sftp_extra_args == None
    assert options.scp_extra_args == None
    assert options.ssh_extra_args == None
    assert options.connection_password_file == C.CONNECTION_PASSWORD_FILE
    assert options.timeout == C.DEFAULT_TIMEOUT
    assert options.ask_pass == C.DEFAULT_ASK_PASS
    assert options.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert options.remote_user == C.DEFAULT_REMOTE_USER


# Generated at 2022-06-12 20:12:22.231971
# Unit test for function add_inventory_options
def test_add_inventory_options():
    """Tests for the add_inventory_options function."""
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    add_inventory_options(parser)
    result = parser.parse_args(['--list-hosts','-i', 'inventory'])
    assert result.listhosts == True
    assert result.inventory == 'inventory'


# Generated at 2022-06-12 20:12:27.736359
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser(prog='ansible', formatter_class=SortingHelpFormatter)
    add_vault_options(parser)
    args = parser.parse_args(['--vault-id', 'testid', '--vault-password-file', 'vaultfile'])
    assert args.vault_ids == ['testid']
    assert args.vault_password_files == ['vaultfile']



# Generated at 2022-06-12 20:12:33.525558
# Unit test for function unfrack_path
def test_unfrack_path():
    # TODO: Make this a pytest test
    # Currently this passes
    result = unfrack_path(pathsep=False)('~/test')
    assert result[0] == '/'
    assert len(result) == 3
    assert result[1] == 'home'
    assert result[2] == 'test'



# Generated at 2022-06-12 20:12:36.992963
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    options = parser.parse_args(args=[])
    assert getattr(options, "one_line", None) == None


# Generated at 2022-06-12 20:12:41.651090
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    transition(parser, ['--vault-password-file', '@/tmp/vault_password_file_path'])
    assert C.DEFAULT_ASK_VAULT_PASS == False
    assert C.VAULT_PASSWORD_FILES == ['/tmp/vault_password_file_path']


# Generated at 2022-06-12 20:12:42.976667
# Unit test for function add_async_options
def test_add_async_options():
    assert add_async_options(argparse.ArgumentParser())



# Generated at 2022-06-12 20:12:49.846588
# Unit test for function add_runas_options
def test_add_runas_options():
    # created option parser
    parser = create_base_parser('unit test')
    add_runas_options(parser)
    add_runas_prompt_options(parser)
    # parse command line
    args = parser.parse_args(['-b', '-K', '-k'])
    # check options
    assert args.become is True, 'bad value for option parser'
    assert args.ask_become_pass is True, 'bad value for option parser'
    assert args.ask_pass is True, 'bad value for option parser'


# Generated at 2022-06-12 20:12:54.149188
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()

    add_vault_options(parser)

    results = parser.parse_args(['--ask-vault-pass', '--vault-id', 'foo'])
    assert results.ask_vault_pass and results.vault_ids == ['foo']



# Generated at 2022-06-12 20:13:12.611686
# Unit test for function add_tasknoplay_options
def test_add_tasknoplay_options():
    parser = argparse.ArgumentParser()
    add_tasknoplay_options(parser)
    options = parser.parse_args(['--task-timeout', '1000'])
    assert options.task_timeout == 1000, 'add_tasknoplay_options function failed to add task timeout option'



# Generated at 2022-06-12 20:13:16.860654
# Unit test for function add_inventory_options
def test_add_inventory_options():
    arg = argparse.Namespace()
    arg.inventory = []

    add_inventory_options(arg)

    assert arg.inventory is not None
    assert arg.listhosts is not None
    assert arg.subset is not None




# Generated at 2022-06-12 20:13:19.957907
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    point = argparse.ArgumentParser(prog='ansible');
    point.add_argument('-v', '--version', nargs=0, action=AnsibleVersion)
    option = point.parse_args([])
    assert option.version == None


# Generated at 2022-06-12 20:13:22.219863
# Unit test for function unfrack_path
def test_unfrack_path():
    assert ["/etc/ansible/hosts"] == unfrack_path()("/etc/ansible/hosts")
    assert ["/etc/ansible/hosts", "/path/to/some/place"] == unfrack_path(True)("/etc/ansible/hosts:/path/to/some/place")
    assert ["-"] == unfrack_path()("-")



# Generated at 2022-06-12 20:13:25.619691
# Unit test for function ensure_value
def test_ensure_value():
    class A:
        pass
    a = A()
    assert a.foo is None

    ensure_value(a, 'foo', None)
    assert a.foo is None

    ensure_value(a, 'foo', 1)
    assert a.foo == 1



# Generated at 2022-06-12 20:13:37.801422
# Unit test for function add_subset_options
def test_add_subset_options():
    mock_parser = Mock(spec=argparse.ArgumentParser)
    add_subset_options(mock_parser)
    assert mock_parser.add_argument.call_count == 2
    call_0 = mock_parser.add_argument.call_args_list[0]
    call_1 = mock_parser.add_argument.call_args_list[1]
    assert call_0 == ((('-t', '--tags'),
                       {'action': 'append',
                       'default': 'all',
                       'dest': 'tags',
                       'help': 'only run plays and tasks tagged with these values'}),)

# Generated at 2022-06-12 20:13:43.152602
# Unit test for function add_tasknoplay_options
def test_add_tasknoplay_options():
    parser = argparse.ArgumentParser()
    add_tasknoplay_options(parser)
    args = parser.parse_args(["--task-timeout", "123"])
    assert args.task_timeout == 123
    assert parser.parse_args(["--task-timeout", "-1"]) == None
    assert parser.parse_args(["--task-timeout", "0"]) == None
    assert parser.parse_args(["--task-timeout", "a"]), None



# Generated at 2022-06-12 20:13:46.933141
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    parser.add_argument('-j', '--json', action='store_true', help='set the stdout output to JSON')
    add_verbosity_options(parser)
    options = parser.parse_args([])
    assert None == options.json



# Generated at 2022-06-12 20:13:56.974219
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('ansible.cfg') == os.path.abspath('ansible.cfg')
    assert unfrack_path(pathsep=False)('~/ansible.cfg') == os.path.expanduser('~/ansible.cfg')
    assert unfrack_path(pathsep=False)('-') == '-'
    assert unfrack_path(pathsep=True)('ansible.cfg') == [os.path.abspath('ansible.cfg')]
    assert unfrack_path(pathsep=True)('~/ansible.cfg') == [os.path.expanduser('~/ansible.cfg')]

# Generated at 2022-06-12 20:13:59.104468
# Unit test for function add_module_options
def test_add_module_options():
    p=add_module_options()
    p.add_module_options()

# Generated at 2022-06-12 20:14:08.115830
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    p = maybe_unfrack_path("@")

    assert p("@@HOME@/tmp") == "@${HOME}/tmp"



# Generated at 2022-06-12 20:14:11.145480
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    ret = '~/.ansible/tmp'
    assert maybe_unfrack_path('~')('~/.ansible/tmp') == ret
    ret = '/some/path'
    assert maybe_unfrack_path('~')('/some/path') == ret



# Generated at 2022-06-12 20:14:22.008386
# Unit test for function ensure_value
def test_ensure_value():
    fake = argparse.Namespace()

    assert (None, None) == (getattr(fake, 'test', None), fake.test)
    ensure_value(fake, 'test', 'test_value')
    assert ('test_value', 'test_value') == (getattr(fake, 'test', None), fake.test)
    ensure_value(fake, 'test', 'ignored_value')
    assert ('test_value', 'test_value') == (getattr(fake, 'test', None), fake.test)
    ensure_value(fake, 'test_value', 'another_value')
    assert ('test_value', 'test_value') == (getattr(fake, 'test', None), fake.test)



# Generated at 2022-06-12 20:14:26.604074
# Unit test for function add_runtask_options
def test_add_runtask_options():
    parser1 = create_base_parser("testadd_runtask_options", usage="test1")
    add_runtask_options(parser1)
    #args = parser.parse_args(["test1", "-e", "'a=1'", "-e", "'b=2'"])
    args1 = parser1.parse_args(["test1", "-e", "extra_vars.yaml", "-e", "'a=1'", "-e", "'b=2'"])
    #assert args.extra_vars == ["a=1", "b=2"], "extra_vars value is wrong"
    assert args1.extra_vars == ["extra_vars.yaml", "a=1", "b=2"], "extra_vars value is wrong"


# Generated at 2022-06-12 20:14:36.114708
# Unit test for function unfrack_path
def test_unfrack_path():
    opt = unfrack_path()
    tests = dict(
        file=opt('/etc/ansible/ansible.cfg'),
        file_no_pathsep=opt('/etc/ansible/ansible.cfg', pathsep=True),
        file_with_pathsep=opt('/etc/ansible/ansible.cfg:/etc/ansible/hosts', pathsep=True),
        stdin=opt('-'),
    )
    assert tests['file'] == '/etc/ansible/ansible.cfg'
    assert tests['file_no_pathsep'] == '/etc/ansible/ansible.cfg'
    assert tests['file_with_pathsep'] == ['/etc/ansible/ansible.cfg', '/etc/ansible/hosts']
    assert tests['stdin'] == '-'

# Generated at 2022-06-12 20:14:40.141913
# Unit test for function add_subset_options
def test_add_subset_options():
    from ansible.cli.arguments import ListType
    parser = create_base_parser(prog="test")
    add_subset_options(parser)
    result = list(parser._actions[3].default)
    assert result == C.TAGS_RUN, "expected action.default of ['all'] but got %s" % result
    assert isinstance(parser._actions[3].default, ListType)
    if not result == ["all"]:
        raise Exception("unexpected default value for action.default; got %s" % result)
    assert result[0] == "all", "expected action.default of ['all'] but got %s" % result



# Generated at 2022-06-12 20:14:44.212252
# Unit test for function version
def test_version():
    assert version()


__all__ = ['UnrecognizedArgument', 'SortingHelpFormatter',
           'version', 'unfrack_path', 'maybe_unfrack_path']

# Generated at 2022-06-12 20:14:54.861958
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b')
    parser.add_argument('-a')
    parser.add_argument('-d')
    parser.add_argument('-c')
    expected = '''usage: [--version] [--help] [-v] [-b B] [-a A] [-d D] [-c C]

optional arguments:
  -h, --help            show this help message and exit
  -b B
  -a A
  -d D
  -c C
  --version             show program's version number and exit
  -v, --verbose         verbose mode (-vvv for more)'''

    hp = SortingHelpFormatter()
    hp.add_argument = lambda x: None
    parser._print_message = lambda message, file: None
    parser

# Generated at 2022-06-12 20:14:59.824062
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@test_host') == '@' + unfrackpath('test_host')
    assert maybe_unfrack_path('@')('test_host') == 'test_host'
    assert maybe_unfrack_path('~')('~test_host') == '~' + unfrackpath('test_host')
    assert maybe_unfrack_path('~')('test_host') == 'test_host'



# Generated at 2022-06-12 20:15:00.554462
# Unit test for function add_runtask_options
def test_add_runtask_options():
    add_runtask_options(argparse.ArgumentParser())


# Generated at 2022-06-12 20:15:19.299761
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import tempfile
    inf, outf = tempfile.TemporaryFile(), tempfile.TemporaryFile()
    parser = argparse.ArgumentParser(add_help=False, prog='prog')
    # parser.print_help = lambda f: f.write(b'usage: prog [-h] {--version}\n')
    parser.add_argument('--version', action=AnsibleVersion)
    parser.output_stream = outf
    parser.parse_args(['--version'], namespace=argparse.Namespace())
    outf.seek(0)
    assert outf.read() == b'prog version: %s.  Ansible version: %s' % (__version__, ansible.__version__)
    outf.close()
    inf.close()



# Generated at 2022-06-12 20:15:24.776268
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # given
    test_opts = [
        argparse.Option([]),
        argparse.Option(['-a']),
        argparse.Option(['-b', '--bb'])
    ]

    # when
    actual_opts = SortingHelpFormatter().add_arguments(test_opts)

    # then
    assert actual_opts == ['[]', ['-a'], ['-b', '--bb']]



# Generated at 2022-06-12 20:15:29.267393
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/tmp/foo') == unfrackpath('/tmp/foo')
    assert unfrack_path(pathsep=True)('/tmp/foo:/tmp/bar') == [unfrackpath('/tmp/foo'), unfrackpath('/tmp/bar')]



# Generated at 2022-06-12 20:15:32.131754
# Unit test for function add_module_options
def test_add_module_options():
    assert add_module_options.__name__ == 'add_module_options'



# Generated at 2022-06-12 20:15:37.913733
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    version_string = version()
    version_string_split = version_string.split('.')

    main_version = int(version_string_split[0])
    sub_version = int(version_string_split[1])
    revision_version = int(version_string_split[2])

    assert tuple([main_version, sub_version, revision_version]) == tuple(ansible.__version__)


# Generated at 2022-06-12 20:15:46.712374
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("/etc/ansible") == "/etc/ansible"
    assert unfrack_path()("/etc/ansible/ansible.cfg") == "/etc/ansible/ansible.cfg"
    # N.B. This isn't the best test ever -- it will fail if the user
    # somehow doesn't have an ansible.cfg in their first two locations,
    # but at least it's a start:
    assert unfrack_path()("ansible.cfg") in [unfrackpath(x) for x in ('ansible.cfg', '/etc/ansible/ansible.cfg')]
    assert unfrack_path(pathsep=True)("/etc/ansible/ansible.cfg:/tmp") == ['/etc/ansible/ansible.cfg', '/tmp']


# Generated at 2022-06-12 20:15:51.434456
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    argv = ['cmd', 'vers']
    parser = create_base_parser(argv)
    parser.exit = lambda: None
    parser.prog = argv[0]
    action = AnsibleVersion(option_strings=['--version'], dest='vers', nargs=0)
    action(parser, None, None, '--version')



# Generated at 2022-06-12 20:15:56.228491
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import ansible.module_utils.ansible_release
    ansible_release = ansible.module_utils.ansible_release
    ansible_release.__version__ = '2.5.1'
    a = AnsibleVersion()
    p = argparse.ArgumentParser()
    p.prog = 'EXAMPLE'
    n = argparse.Namespace()
    a(p, n, None)

# Generated at 2022-06-12 20:16:01.641105
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import io
    import contextlib
    from ansible.module_utils.common.yaml import yaml_load
    sys.argv = ['im_a_module_utility']
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        parser = argparse.ArgumentParser()
        action = AnsibleVersion()
        namespace = argparse.Namespace()
        action(parser, namespace, None, None)
    output = yaml_load(output.getvalue())
    assert output['ansible_version'] == __version__



# Generated at 2022-06-12 20:16:11.593812
# Unit test for function unfrack_path
def test_unfrack_path():
    #  We can't do live testing here, since the system-wide config file may not be
    #  in either of the default locations, so we'll fake it.
    unfrack_path.faked_paths = {
        'foo': 'bar',
        'biff': 'baz',
    }

    #  Test a single path
    values = [
        'foo',
        os.path.join('foo', 'bar'),
        os.path.join('biff', 'bar'),
        os.path.join('baz', 'bar'),
    ]
    expected = [
        'bar',
        os.path.join('bar', 'bar'),
        os.path.join('baz', 'bar'),
        os.path.join('baz', 'bar'),
    ]

# Generated at 2022-06-12 20:16:32.163082
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('') == ''
    assert unfrack_path(pathsep=False)('.') == './'
    assert unfrack_path(pathsep=False)('foo') == './foo'
    assert unfrack_path(pathsep=False)('~/bar') == '~/bar'

    assert unfrack_path(pathsep=True)('') == []
    assert unfrack_path(pathsep=True)('.') == ['./']
    assert unfrack_path(pathsep=True)('foo') == ['./foo']
    assert unfrack_path(pathsep=True)('~/bar') == ['~/bar']
    assert unfrack_path(pathsep=True)('.' + os.pathsep + 'bar')

# Generated at 2022-06-12 20:16:37.117836
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    value = '/path/to/myfile'
    beacon = '@'
    unfrack_value = maybe_unfrack_path(beacon)(beacon+value)
    assert unfrack_value == beacon+os.path.expanduser(value)


# Generated at 2022-06-12 20:16:46.889550
# Unit test for function unfrack_path
def test_unfrack_path():
    """Unit test for function unfrack_path"""
    def _test_path(path):
        assert not os.path.isabs(path), path
        assert not path.startswith('~'), path
        assert path.startswith('/'), path

    _test_path(unfrack_path()('~foo'))
    _test_path(unfrack_path()('/foo'))
    _test_path(unfrack_path()('foo/bar'))
    _test_path(unfrack_path()('.'))
    _test_path(unfrack_path()('./foo'))
    _test_path(unfrack_path()('./foo/../bar'))


# Generated at 2022-06-12 20:16:54.881483
# Unit test for function unfrack_path
def test_unfrack_path():
    p = unfrack_path()
    assert '~' not in p('~/foo')
    m = ''.join([os.pathsep, os.pathsep])
    assert len(p(m * 100).split(os.pathsep)) == 102
    assert p('/') == '/'
    assert p('') == ''
    s = os.pathsep
    assert p('/foo%s~%s~/bar%s/baz' % ((s,) * 3)) == '/foo%s%s/bar%s/baz' % ((s,) * 3)
    assert p('-' + s + '-') == '-/' + s + '-'
    assert p('-') == '-'


# Generated at 2022-06-12 20:16:57.116902
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from argparse import Namespace
    from ansible.cli.playbook import PlaybookCLI

    args = Namespace()
    setattr(args, 'version', None)

    playbook_cli = PlaybookCLI(args)
    playbook_cli.parse()



# Generated at 2022-06-12 20:17:00.447607
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-b')
    parser.add_argument('-a')
    parser.parse_args(['-h'])



# Generated at 2022-06-12 20:17:06.865942
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    prog = "ansible"
    prog_version = "2.2.0"
    object_ = AnsibleVersion(["-v"], dest=None, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None)
    object_.__call__(prog=prog, parser=None, namespace=None, values=None, option_string=None)
    assert ansible_version == prog_version

# Generated at 2022-06-12 20:17:13.451288
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    from subprocess import check_output
    from os.path import join
    from tempfile import TemporaryDirectory

    def _realpath(path):
        if path == '-':
            return path
        return check_output(["realpath", "-s", path]).decode("utf-8").strip()

    with TemporaryDirectory() as d:
        assert _realpath(maybe_unfrack_path('-e')('-')) == '-'
        assert _realpath(maybe_unfrack_path('library')('library')) == 'library'
        assert _realpath(maybe_unfrack_path('roles')('roles')) == 'roles'
        in_dir = join(d, 'in.yml')
        out_dir = join(d, 'out')

# Generated at 2022-06-12 20:17:21.997360
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # a relative path
    path = '../foo'
    beacon = '@'
    assert maybe_unfrack_path(beacon)(beacon + path) == beacon + os.path.abspath(path)
    # an absolute path
    beacon = '@'
    path = '/foo'
    assert maybe_unfrack_path(beacon)(beacon + path) == beacon + path
    # a path using HOME
    beacon = '~'
    path = '~/foo'
    assert maybe_unfrack_path(beacon)(beacon + path) == beacon + os.path.expanduser(path)



# Generated at 2022-06-12 20:17:28.363615
# Unit test for function version
def test_version():
    path = os.path.join(os.getcwd(), 'versionfixture', 'ansible')
    ansible.__path__ = [path]
    basedir = os.path.join(os.path.dirname(__file__), 'versionfixture')
    repo_path = os.path.join(basedir, '.git')
    with open(os.path.join(basedir, 'ansible', '__init__.py'), 'w') as f:
        f.write("__version__ = '2.5.7'\n")
    with open(os.path.join(repo_path, "HEAD"), 'w') as f:
        f.write("ref: refs/heads/stable-2.4\n")

# Generated at 2022-06-12 20:17:53.221584
# Unit test for function unfrack_path
def test_unfrack_path():
    if os.environ.get('CURL_CA_BUNDLE', None):
        del os.environ['CURL_CA_BUNDLE']
    if os.environ.get('CURL_CA_PATH', None):
        del os.environ['CURL_CA_PATH']
    test_paths = [
        ("/etc:/usr/local/etc", True),
        ("/etc:/usr/local/etc"),
        (u"/etc:/usr/local/etc"),
    ]
    for path in test_paths:
        assert unfrack_path()(path) == unfrack_path(True)(path[0])



# Generated at 2022-06-12 20:17:59.154142
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('./')('./test.yml') == './test.yml'
    assert maybe_unfrack_path('/')('/test.yml') == '/test.yml'
    assert maybe_unfrack_path('./')('test.yml') == 'test.yml'



# Generated at 2022-06-12 20:18:05.980136
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-e', '--end', help="the end")
    parser.add_argument('-f', '--force', help="the force")
    parser.add_argument('-s', '--start', help="the start")
    hlp = parser.format_help()
    assert hlp.index('--end') < hlp.index('--force') < hlp.index('--start')



# Generated at 2022-06-12 20:18:12.171148
# Unit test for function version
def test_version():

    # Mock C.CONFIG_FILE and C.DEFAULT_MODULE_PATH
    from ansible.utils import context_objects as co

    orig_cfg_file = co.global_context.cf
    orig_def_module_path = co.global_context.dmp
    orig_sys_path = sys.argv
    orig_v = sys.version

    co.global_context.cf = 'config_file'
    co.global_context.dmp = 'module_search_path'
    sys.argv = ['executable', 'arg1', 'arg2']
    sys.version = 'python' + ''.join(sys.version.splitlines())

    # Test module_path and program_name are correctly output


# Generated at 2022-06-12 20:18:14.238941
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('some_path') == unfrackpath('some_path')
    assert unfrack_path(pathsep=True)('some_path:some_path2') == [unfrackpath('some_path'), unfrackpath('some_path2')]


# Generated at 2022-06-12 20:18:18.125262
# Unit test for function unfrack_path
def test_unfrack_path():
    x = '/Users/admin/ansible/lib/ansible/module_utils/facts'
    y = '-/Users/admin/ansible/lib/ansible/module_utils/facts'
    y2 = '/Users/admin/ansible/lib/ansible/module_utils/facts-/Users/admin/ansible/lib/ansible/module_utils/facts'
    results = unfrack_path(pathsep=False)(y)
    expected = '-/Users/admin/ansible/lib/ansible/module_utils/facts'
    assert results == expected, 'unfracked path not formatted correctly. should be %s, got %s' % (expected, results)
    results = unfrack_path(pathsep=False)(x)

# Generated at 2022-06-12 20:18:25.609362
# Unit test for function unfrack_path
def test_unfrack_path():
    """Test with and without the pathsep flag to unfrack_path"""
    path = ':/usr/local/bin:/etc:'
    ex_path = ['/usr/local/bin', '/etc']
    ansible_path = os.path.dirname(__file__) + '/../../'
    ansible_lib_path = ansible_path + 'lib/'

    assert unfrack_path()(path) == ansible_lib_path + path[1:]
    assert unfrack_path(pathsep=True)(path) == [ansible_lib_path + path[1:]]
    assert unfrack_path(pathsep=True)(ansible_path) == [unfrackpath(ansible_path)]
    for item in unfrack_path(pathsep=True)(path):
        assert item in ex_path

# Generated at 2022-06-12 20:18:30.432026
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from ansible.utils.display import Display
    import sys
    sys.stderr = sys.stdout
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion)
    options = parser.parse_args(['--version'])
    # We don't test the version itself
    assert True



# Generated at 2022-06-12 20:18:32.166815
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    assert isinstance(argparse.ArgumentParser(formatter_class=SortingHelpFormatter)(), SortingHelpFormatter)


# Generated at 2022-06-12 20:18:32.835161
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    assert AnsibleVersion.__call__()



# Generated at 2022-06-12 20:19:21.619401
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    unfrackpaths = [unfrack_path()(x) for x in ('/a/./b/../c', '~/d/./e/../f')]
    beacon = '!!!'
    maybe_unfrack_paths = [maybe_unfrack_path(beacon)(x) for x in ('/a/./b/../c', '~/d/./e/../f')]
    assert unfrackpaths == maybe_unfrack_paths
    maybe_unfrack_paths = [maybe_unfrack_path(beacon)(beacon+x) for x in ('/a/./b/../c', '~/d/./e/../f')]
    assert unfrackpaths == maybe_unfrack_paths



# Generated at 2022-06-12 20:19:31.447885
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Load the test yml file
    data = os.path.join(os.path.dirname(__file__), 'test_maybe_unfrack_path.yml')
    with open(data) as f:
        test_cases = yaml_load(f, Loader=yaml.SafeLoader)
    # if python version is 2.7, import unittest2.
    if sys.version_info[:2] < (3, 0):
        import unittest2 as unittest
    else:
        import unittest
    # Run unit test
    for case in test_cases:
        args = case.get('args', {})
        kwargs = case.get('kwargs', {})
        results = case.get('result', {})

# Generated at 2022-06-12 20:19:41.363867
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()(b'/tmp') == unfrackpath(b'/tmp')
    assert unfrack_path()(b'/tmp') == unfrack_path()(u'/tmp')
    assert unfrack_path(pathsep=True)(b'/tmp:/var/tmp') == [unfrackpath(b'/tmp'), unfrackpath(b'/var/tmp')]
    assert unfrack_path(pathsep=True)(b'/tmp:/var/tmp') == unfrack_path(pathsep=True)(u'/tmp:/var/tmp')
    assert unfrack_path(pathsep=True)(b'-') == '-'
    assert unfrack_path(pathsep=True)(b'-') == unfrack_path(pathsep=True)(u'-')


# Generated at 2022-06-12 20:19:46.907153
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@~/test') == '@%s' % os.path.expanduser('~/test')
    assert maybe_unfrack_path('@')('@/test') == '@%s' % os.path.abspath('/test')
    assert maybe_unfrack_path('@')('/@test') == '/@test'

#
# OptionParsers
#

# Generated at 2022-06-12 20:19:48.561926
# Unit test for function unfrack_path
def test_unfrack_path():
    """Unfrack path should return - when given - as input."""
    assert unfrack_path()('-') == '-'



# Generated at 2022-06-12 20:19:50.440144
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('modules:library:/usr/share/ansible/plugins/modules') == '/usr/share/ansible/plugins/modules'


# Generated at 2022-06-12 20:19:56.949605
# Unit test for function unfrack_path
def test_unfrack_path():
  assert unfrack_path()('/abc/def') == unfrackpath('/abc/def')
  assert unfrack_path()('${HOME}/abc/def') == os.path.join(os.environ['HOME'], 'abc/def')
  assert unfrack_path(True)('${HOME}/abc/def:/foo/bar') == [os.path.join(os.environ['HOME'], 'abc/def'), '/foo/bar']
  assert unfrack_path()('-') == '-'



# Generated at 2022-06-12 20:20:03.714120
# Unit test for function unfrack_path
def test_unfrack_path():
    tpath=unfrack_path()
    assert tpath('/a/b/c') == '/a/b/c'
    assert tpath('~/b/c') == '/a/b/c'
    assert tpath('$HOME/b/c') == '/a/b/c'
    assert tpath('${HOME}/b/c') == '/a/b/c'
    assert tpath('~/b/c') == '/a/b/c'
    assert tpath('~/b/c') == '/a/b/c'
    assert tpath('~/b/c') == '/a/b/c'


# Generated at 2022-06-12 20:20:09.730151
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # Reset
    try:
        del(sys.argv[1:])
    except AttributeError:
        # Python 3
        sys.argv = sys.argv[0:1]
    # Execute
    my_args = sys.argv[0:]
    my_args.append('--version')
    with open('/tmp/ansible_version', 'w') as f:
        try:
            old_stdout = sys.stdout
            sys.stdout = f
            my_parser = argparse.ArgumentParser()
            my_parser.add_argument('--version', action=AnsibleVersion)
            my_parser.parse_args(args=my_args)
        finally:
            sys.stdout = old_stdout
    # Make assertions

# Generated at 2022-06-12 20:20:12.961034
# Unit test for function unfrack_path
def test_unfrack_path():
    # Check for unfrack_path() with multiple paths
    assert unfrack_path(True)('~/playbooks:~/test:~/test2') == ['~/playbooks', '~/test', '~/test2']
    # Check unfrack_path() with a single path
    assert unfrack_path()('~/playbooks') == '~/playbooks'


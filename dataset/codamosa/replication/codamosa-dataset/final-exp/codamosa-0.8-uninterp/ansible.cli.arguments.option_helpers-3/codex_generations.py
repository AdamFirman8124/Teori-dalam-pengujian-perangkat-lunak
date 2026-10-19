

# Generated at 2022-06-12 20:11:57.818037
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    parser = argparse.ArgumentParser(prog='ansible-test')
    add_runas_prompt_options(parser)
    options = parser.parse_args(['-K'])
    assert options.become_ask_pass is True
    options = parser.parse_args(['--become-password-file', '~/test'])
    assert options.become_password_file == '~/test'



# Generated at 2022-06-12 20:12:02.855466
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    (args, extra) = parser.parse_known_args()
    assert args.check == False
    assert args.syntax == False
    assert args.diff == C.DIFF_ALWAYS


# Generated at 2022-06-12 20:12:11.469556
# Unit test for function add_inventory_options
def test_add_inventory_options():
    '''
    Unit test for function add_inventory_options
    '''
    parser = argparse.ArgumentParser(description="Test add_inventory_options")
    add_inventory_options(parser)
    parser.parse_args(["-i", "/path/to/hostsfile"])
    parser.parse_args(["--inventory", "/path/to/hostsfile"])
    parser.parse_args(["--inventory", "/path/to/hostsfile", "-i", "/path/to/listfile"])
    try:
        parser.parse_args(["--inventory", "/path/without/file"])
    except SystemExit:
        pass
    else:
        raise



# Generated at 2022-06-12 20:12:15.165785
# Unit test for function add_runtask_options
def test_add_runtask_options():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    add_runtask_options(parser)
    args = parser.parse_args([])
    assert args.extra_vars is not None


# Generated at 2022-06-12 20:12:23.483816
# Unit test for function add_basedir_options
def test_add_basedir_options():
    args = 'cli/ansible --playbook-dir ./test'
    class FakeParser(object):
        def __init__(self):
            self.values = {}
        def set_defaults(self,**kwargs):
            for k,v in kwargs.items():
                self.values[k] = v
    parser = FakeParser()
    add_basedir_options(parser)
    sys.argv = args.split()
    nargs = vars(parser.parse_args())
    assert parser.values.get('basedir') == ['./test']
    assert nargs['playbook_dir'] == ['./test']

# test for unfrack_path

# Generated at 2022-06-12 20:12:27.560638
# Unit test for function add_async_options
def test_add_async_options():
    prog = "ANSIBLE"
    usage = "usage: %(prog)s [options]"
    desc = "description"
    epilog = "epilog"

    parser = create_base_parser(prog, usage, desc, epilog)
    add_async_options(parser)


# Generated at 2022-06-12 20:12:37.029352
# Unit test for function add_module_options
def test_add_module_options():
    import unittest
    from unittest.mock import patch

    class TestModuleOption(unittest.TestCase):
        def test_add_module_options(self):
            parser = argparse.ArgumentParser()
            add_module_options(parser)
            with patch('ansible.config.get_configuration_definition') as config_mock:
                config_mock.return_value = {'default': ''}
                args = parser.parse_args(['-M', '/path/to/module'])
                self.assertEqual(args, argparse.Namespace(module_path=['/path/to/module', '']))

    unittest.main()



# Generated at 2022-06-12 20:12:48.713712
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = argparse.ArgumentParser(description='Runas test')
    add_runas_options(parser)
    options = parser.parse_args([])
    assert options.become is False
    assert options.become_method == 'sudo'
    assert options.become_user is None
    assert options.ask_pass is False
    assert options.become_ask_pass is False
    assert options.ask_become_pass is False
    options = parser.parse_args(['-b'])
    assert options.become is True
    assert options.become_ask_pass is False
    assert options.ask_become_pass is False
    options = parser.parse_args(['--become-user', 'foobar'])
    assert options.become is True

# Generated at 2022-06-12 20:12:52.243687
# Unit test for function add_basedir_options
def test_add_basedir_options():
    parser = create_base_parser('ansible-console')
    add_basedir_options(parser)
    options = parser.parse_args(['--playbook-dir', '/basedir'])
    assert options.basedir == '/basedir'

# Generated at 2022-06-12 20:12:57.055926
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    # Test setup and configuration
    parser = argparse.ArgumentParser()
    result = add_runas_prompt_options(parser)
    expressions = [
        ("-K", "--ask-become-pass"),
        ("--become-password-file", "--become-pass-file")
    ]
    for expression in expressions:
        try:
            assert result.get_option(expression[0])
            assert result.get_option(expression[1])
        except AttributeError:
            raise AssertionError("Option %s should exist " % expression[0])



# Generated at 2022-06-12 20:13:11.965421
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    add_connect_options(parser)
    parser.parse_known_args(['--private-key=test'])



# Generated at 2022-06-12 20:13:19.950672
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    arguments = parser.parse_args(['--vault-id', 'test-id', '--ask-vault-password', '--vault-password-file', 'test-file'])
    assert arguments.vault_ids == ['test-id']
    assert arguments.ask_vault_pass is True
    assert arguments.vault_password_files == ['test-file']



# Generated at 2022-06-12 20:13:21.703945
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from ansible.utils.display import Display
    display = Display()
    a = AnsibleVersion(None, None, 'prog', None, display)
    a(None, None, None)



# Generated at 2022-06-12 20:13:26.387065
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/')('/etc/my.cnf') == '/etc/my.cnf'
    assert maybe_unfrack_path('@')('@/etc/my.cnf') == '@/etc/my.cnf'
    assert maybe_unfrack_path('@')('@/etc/my.cnf') == '@/etc/my.cnf'
    assert maybe_unfrack_path('@')('@./my.cnf') == '@./my.cnf'



# Generated at 2022-06-12 20:13:31.570699
# Unit test for function add_tasknoplay_options
def test_add_tasknoplay_options():
    parser = argparse.ArgumentParser()
    add_tasknoplay_options(parser)
    results = parser.parse_known_args(['--task-timeout', '2'])
    assert results[0].task_timeout == 2


# Generated at 2022-06-12 20:13:39.429684
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    home_path = os.environ["HOME"]
    pwd_path = os.getcwd()
    user_beacon = '~'
    pwd_beacon = '@'
    assert(maybe_unfrack_path(user_beacon)("~/foo") == f"~{home_path}/foo")
    assert(maybe_unfrack_path(user_beacon)("foo") == "foo")
    assert(maybe_unfrack_path(pwd_beacon)("@/foo") == f"@{pwd_path}/foo")
    assert(maybe_unfrack_path(pwd_beacon)("foo") == "foo")



# Generated at 2022-06-12 20:13:40.423106
# Unit test for function version
def test_version():
    assert isinstance(version(), str)

# Generated at 2022-06-12 20:13:43.153917
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    cmdline = ['--flush-cache']
    args = parser.parse_args(cmdline)
    assert args.flush_cache == True


# Generated at 2022-06-12 20:13:52.672929
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("C:")("C:\\test") == "C:\\test"
    assert maybe_unfrack_path("C:")("C:/test") == "C:\\test"
    assert maybe_unfrack_path("C:")("C://test") == "C:/test"
    assert maybe_unfrack_path("C:/")("C://test") == "C:/test"
    assert maybe_unfrack_path("C:")("C:\\\\test") == "C:\\test"
    assert maybe_unfrack_path("C:")("C:\\/test") == "C:/test"
    assert maybe_unfrack_path("C:")("C:/test") == "C:\\test"

# Generated at 2022-06-12 20:13:59.353766
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    parser.print_help()
    result = parser.parse_args([])

    assert result.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert result.remote_user == C.DEFAULT_REMOTE_USER
    assert result.connection == C.DEFAULT_TRANSPORT
    assert result.timeout == C.DEFAULT_TIMEOUT
    assert result.ask_pass == C.DEFAULT_ASK_PASS
    assert result.connection_password_file == C.CONNECTION_PASSWORD_FILE



# Generated at 2022-06-12 20:14:12.730151
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    test_usage = " %(prog)s [-h] [-v] [-f] [--debug] [--connection=CONNECTION]\n"
    test_description = "test"
    argparse_obj = argparse.ArgumentParser(usage=test_usage, description=test_description, formatter_class=SortingHelpFormatter)
    argparse_obj = argparse_obj.add_argument("-v", "--verbose", action='store_true', default=False, dest='verbose', help="verbose mode (-vvv for more)")
    argparse_obj = argparse_obj.add_argument("-f", "--force", action='store_true', dest='force', help="ignore errors")

# Generated at 2022-06-12 20:14:19.423745
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_value = "~/test/path"
    assert maybe_unfrack_path("~")(test_value) == os.path.expanduser("~") + test_value[1:]
    test_value2 = "/test/path"
    assert maybe_unfrack_path("/")(test_value2) == test_value2
# End unit test for function maybe_unfrack_path.



# Generated at 2022-06-12 20:14:23.071852
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test positive case, when value starts with beacon
    assert "@@file" == maybe_unfrack_path("@")("@file")
    # Test negative case, when value doesn't start with beacon
    assert "file" == maybe_unfrack_path("@")("file")



# Generated at 2022-06-12 20:14:23.627024
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
  pass



# Generated at 2022-06-12 20:14:34.036035
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Two actions in subparsers
    parser_foo = subparsers.add_parser('foo')
    parser_foo.add_argument('-b')
    parser_foo.add_argument('-a')
    parser_bar = subparsers.add_parser('bar')
    parser_bar.add_argument('-a')
    parser_bar.add_argument('-b')

    # SortingHelpFormatter instance
    parser.formatter_class = SortingHelpFormatter

    # Get help message
    string_io = sys.stdout
    try:
        from cStringIO import StringIO  # python 2.x
    except ImportError:
        from io import StringIO        # python 3.x

# Generated at 2022-06-12 20:14:41.950494
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    path = 'some/random/path'
    unfracked_path = unfrackpath(path)
    assert maybe_unfrack_path(beacon='/path/')('/path/{}'.format(path)) == '/path/{}'.format(unfracked_path)
    assert maybe_unfrack_path(beacon='/path/')('some/random/path') == 'some/random/path'
    assert maybe_unfrack_path(beacon=None)('some/random/path') == 'some/random/path'
    assert maybe_unfrack_path(beacon='')('some/random/path') == 'some/random/path'



# Generated at 2022-06-12 20:14:42.581878
# Unit test for function version
def test_version():
    version()

# Generated at 2022-06-12 20:14:53.158184
# Unit test for function maybe_unfrack_path

# Generated at 2022-06-12 20:14:56.492278
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('~')('~/myfile.yaml') == os.path.join(os.path.expanduser('~'), 'myfile.yaml')
    assert maybe_unfrack_path('/')('/myfile.yaml') == '/myfile.yaml'



# Generated at 2022-06-12 20:14:58.676483
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = to_native(ansible.__version__)
    assert ansible_version == '2.11.0'



# Generated at 2022-06-12 20:15:05.345621
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
  pass
  



# Generated at 2022-06-12 20:15:10.196505
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import ansible.cli.argparser as argparser
    parser = argparser.create()
    args = parser.parse_args(['--version'])
    assert hasattr(args, 'func'), "There is no attribute 'func' under args"
    args.func(args)



# Generated at 2022-06-12 20:15:19.410204
# Unit test for function unfrack_path
def test_unfrack_path():
    # Assume this module is installed next to -with-plugins package
    ansible_plugins = os.path.join(os.path.dirname(__file__), '..')
    assert unfrack_path()(ansible_plugins) == ansible_plugins
    assert unfrack_path(pathsep=True)(ansible_plugins) == [ansible_plugins]
    assert unfrack_path(pathsep=True)('ansible_plugins') == ['ansible_plugins']
    assert unfrack_path(pathsep=True)('/tmp/ansible_plugins1%s/tmp/ansible_plugins2' % os.pathsep) == ['/tmp/ansible_plugins1', '/tmp/ansible_plugins2']



# Generated at 2022-06-12 20:15:21.856413
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    av = AnsibleVersion(option_strings=['--version'])
    namespace = argparse.Namespace()
    av(None, namespace, None, option_string=None)


# Generated at 2022-06-12 20:15:26.124113
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    av = AnsibleVersion(option_strings=['--version'])
    parser = argparse.ArgumentParser()
    with open('test', 'w') as f:
        f.write('test')
    parser.print_help = lambda _: print('version')
    parser.exit = lambda: exit(0)
    av(parser=parser, namespace=None, values=None, option_string='--version')
    os.remove('test')



# Generated at 2022-06-12 20:15:37.820537
# Unit test for function unfrack_path
def test_unfrack_path():
    from ansible.module_utils.common.yaml import _ordered_dict
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar

    class AnsibleVarsFake(object):
        def __init__(self, variables):
            self.variables = variables

        def get_vars(self, play=None, host=None, task=None, include_hostvars=True, include_delegate_to=True):
            return self.variables

    class FakeTemplar(Templar):
        def __init__(self, loader, variables=None, **kwargs):
            self._loader = loader
            if variables is None:
                variables = dict()
            self._available_variables = variables

        def set_available_variables(self, variables):
            self._available_

# Generated at 2022-06-12 20:15:45.427969
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    class MockParser(object):
        def __init__(self, exit_code):
            self.exit_code = exit_code

        def exit(self):
            sys.exit(self.exit_code)

    mock_namespace = object()

    action = AnsibleVersion(["--version"], dest="version", help="version")
    action.__call__(MockParser(0), mock_namespace, [], "--version")

    action = AnsibleVersion(["-v"], dest="version", help="version")
    action.__call__(MockParser(0), mock_namespace, [], "-v")

# Generated at 2022-06-12 20:15:54.353753
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    formatter = SortingHelpFormatter(sorted_arguments=True, add_help=False)
    # Using an example from the argparse module documentation
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    parser.add_argument('--verbose', '-v', action='count', help='increase verbosity')
    parser.add_argument('--version', action='version', version="what version?", help='show program version')
    group = parser.add_mutually_exclusive_

# Generated at 2022-06-12 20:16:02.069955
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # construct parser
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    # add arguments
    parser.add_argument("-a", "--all", action="store_true", help="set all")
    parser.add_argument("-f", "--foo", nargs=1, help="foo help")
    parser.add_argument("-b", help="b help")
    # generate help by SortingHelpFormatter
    help_str= parser.format_help()
    # get expected help
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(cur_dir, "test_class_option_parser.txt"), "r")
    expected_help_str = f.read()
    f.close

# Generated at 2022-06-12 20:16:10.727392
# Unit test for function unfrack_path
def test_unfrack_path():
    def check(path, expected):
        result = unfrack_path()(path)
        assert result == expected, "unfrack_path('%s') = '%s' but expected '%s'" % (path, result, expected)

    check("/usr/bin/", "/usr/bin/")
    check("/usr/bin", "/usr/bin/")
    check("../lib/", "../lib/")
    check("test", "test")
    check("~/bin", os.path.expanduser("~/bin"))
    check("~", os.path.expanduser("~"))


#
# Utility functions to expand Options
#

# Generated at 2022-06-12 20:16:22.982851
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(beacon='@')(value='@@foo/bar') == '@@foo/bar'
    assert maybe_unfrack_path(beacon='@')(value='@foo/bar') == '@/Users/myuser/.ansible/foo/bar'
    assert maybe_unfrack_path(beacon='@')(value='/tmp/foo/bar') == '/tmp/foo/bar'
    assert maybe_unfrack_path(beacon='@')(value='/tmp/@foo/bar') == '/tmp/@foo/bar'


# Generated at 2022-06-12 20:16:28.231468
# Unit test for function unfrack_path
def test_unfrack_path():
    if os.sep == '/':
        assert unfrackpath("~/test") == os.environ['HOME'] + "/test"
        assert unfrackpath("~/test", True) == os.environ['HOME'] + "/test"
    assert unfrackpath("test") == "test"
    assert unfrackpath("test", True) == "test"


# Generated at 2022-06-12 20:16:39.334854
# Unit test for function unfrack_path
def test_unfrack_path():
    #pylint: disable=redefined-outer-name
    from ansible.utils.path import PATH_TRANSLATIONS
    from ansible.utils.display import Display
    display = Display()

    def unfrack_func(pathsep):
        def inner(value):
            if pathsep:
                return [unfrackpath(x) for x in value.split(os.pathsep) if x]
            else:
                return unfrackpath(value)
        return inner

    # TODO(galstrom21): modify the test to be independent from PATH_TRANSLATIONS
    #                   to make it more unit-test like
    for pathsep in (True, False):
        for env_name, (path_id, subdir) in PATH_TRANSLATIONS.items():
            env_val = os.environ

# Generated at 2022-06-12 20:16:48.439553
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():

    unfrack_paths = [
        'defaults/main.yml',
        'roles/example/defaults/main.yml',
        'roles/example/meta/main.yml',
        'roles/example/tasks/main.yml',
        'roles/example/vars/main.yml',
        'host_vars/example.com',
        'host_vars/www',
    ]

    for unfrack_path in unfrack_paths:
        unfracked_path = maybe_unfrack_path('@')(unfrack_path)
        assert unfracked_path == ('@' + unfrack_path)
#
# Options
#



# Generated at 2022-06-12 20:16:50.532462
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('beacon_value')('beacon_value/value') == 'beacon_value/value'



# Generated at 2022-06-12 20:16:54.209234
# Unit test for function ensure_value
def test_ensure_value():
    class Foo(object):
        pass
    namespace = Foo()
    ensure_value(namespace, 'bar', 'baz')
    assert namespace.bar == 'baz'
    namespace.bar = None
    ensure_value(namespace, 'bar', 'baz')
    assert namespace.bar == 'baz'



# Generated at 2022-06-12 20:16:58.749203
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    result = maybe_unfrack_path('$')('$/foo/bar')
    assert result == '$' + unfrackpath('/foo/bar')
    result = maybe_unfrack_path('$')('/foo/bar')
    assert result == '/foo/bar'
    result = maybe_unfrack_path('$')('$/foo/bar')
    assert result == '$' + unfrackpath('/foo/bar')
    result = maybe_unfrack_path('$')('/foo/bar')
    assert result == '/foo/bar'



# Generated at 2022-06-12 20:17:05.567112
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    print("test_AnsibleVersion___call__")
    formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(
        prog = "N/A (unit test)",
        formatter_class=formatter,
        add_help=False
    )
    parser.add_argument("--version", dest="version", action=AnsibleVersion)
    args = parser.parse_args(["--version"])
    print("args: %s" % args)
    assert args.version is None



# Generated at 2022-06-12 20:17:10.951569
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    maybe_unfrack = maybe_unfrack_path('_')
    test = '/ansible/playbooks'
    expected = '_/ansible/playbooks'
    assert expected == maybe_unfrack(test)

    test = '_/ansible/playbooks'
    expected = '_/ansible/playbooks'
    assert expected == maybe_unfrack(test)

    test = '_R:\\ansible\\playbooks'
    expected = '_R:\\ansible\\playbooks'
    assert expected == maybe_unfrack(test)


# Generated at 2022-06-12 20:17:18.433605
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # This unit test is not run by nose test collection because this is a class
    # whose sole purpose is to exit the program.
    from ansible.release import __version__
    parser = argparse.ArgumentParser()
    namespace = argparse.Namespace()
    option_string = None
    action = AnsibleVersion(option_strings=['--version'])
    action(parser, namespace, values=None, option_string=option_string)
    assert ansible_version == __version__
    assert True  # This is to indicate that we reached the end of the function.

# Generated at 2022-06-12 20:17:34.306365
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/test') == '@/test'
    assert maybe_unfrack_path('@')('@test') == '@test'
    assert maybe_unfrack_path('@')('/test') == '/test'



# Generated at 2022-06-12 20:17:40.576583
# Unit test for function ensure_value
def test_ensure_value():
    class fake_namespace(object):
        def __init__(self):
            self._test_attr = None
    namespace = fake_namespace()
    ensure_value(namespace, '_test_attr', [])
    assert namespace._test_attr == []
    ensure_value(namespace, '_test_attr', [1])
    assert namespace._test_attr == []
    ensure_value(namespace, '_test_attr', None)
    assert namespace._test_attr == []



# Generated at 2022-06-12 20:17:45.606720
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace:
        pass
    namespace = Namespace()
    ensure_value(namespace, 'foo', 'bar1')
    assert namespace.foo == 'bar1'
    ensure_value(namespace, 'foo', 'bar2')
    assert namespace.foo == 'bar1'



# Generated at 2022-06-12 20:17:49.064478
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    value = maybe_unfrack_path('+')('+foo')
    assert value == '+' + os.path.join(C.DEFAULT_LOCAL_TMP, 'ansible_foo')
    assert maybe_unfrack_path('+')('bar') == 'bar'


#
# OptionGroups
#

# Generated at 2022-06-12 20:17:56.399236
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    from ansible.module_utils.common.yaml import AnsibleMapping
    @unfrackpath
    def _get_parser():
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('--foobar', action='append')
        parser.add_argument('--baz', action=PrependListAction)
        return parser

    args = ['--foobar="foo"', '--foobar="bar"', '--baz="baz"', '--baz="baz2"']
    parser = _get_parser()
    args = parser.parse_args(args)

    assert args.foobar == ['foo', 'bar']
    assert args.baz == ['baz', 'baz2']



# Generated at 2022-06-12 20:18:05.706353
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # Save original parser
    original_parser = copy.deepcopy(SortingHelpFormatter.parser)

    # Create new parser
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    # String of the first test_help_formatting object
    s1 = ("-c, --foo, --bar, --baz, --qu, --qux, --quux, --corge, --grault, --garply, --waldo, --fred, --plugh, "
          "--xyzzy, --thud")
    # Out of order args to test initial functionality
    parser.add_argument("-c")
    parser.add_argument("--corge")
    parser.add_argument("--qux")
    parser.add_argument("--garply")

# Generated at 2022-06-12 20:18:09.773884
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    from ansible.config import load_config_file
    from ansible.cli.arguments import option_helpers as opt_help

    data = {
        'ANSIBLE_CONFIG' : "~/ansible.cfg",
        'ANSIBLE_ROLES_PATH' : "~/ansible_roles",
        'ANSIBLE_LIBRARY' : "~/ansible_library",
        'ANSIBLE_ACTION_PLUGINS' : "~/ansible_action_plugins",
    }

    test_config = load_config_file(ConfigCLI(None))
    for key, value in data.items():
        test_config[key] = value

    home = "/home/%s" % os.environ['USER']
    for key, value in data.items():
        assert opt_help.maybe_un

# Generated at 2022-06-12 20:18:12.304375
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # deprecated: AnsibleVersion() is tested in module_utils/common/test_argparsing.py
    pass



# Generated at 2022-06-12 20:18:15.081436
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    unfrack_value = maybe_unfrack_path("@")("@/usr/share/ansible/plugins/actions/test")
    assert unfrack_value == "@/" + unfrackpath("/usr/share/ansible/plugins/actions/test")


# Generated at 2022-06-12 20:18:17.008885
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace(object):
        pass
    ns = Namespace()
    assert getattr(ns, 'foo', None) is None
    result = ensure_value(ns, 'foo', 'bar')
    assert result == 'bar'
    assert getattr(ns, 'foo', None) == 'bar'



# Generated at 2022-06-12 20:18:32.944793
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/')('/tmp/test') == '/tmp/test'
    assert maybe_unfrack_path('/')('@tmp/test') == '/tmp/test'



# Generated at 2022-06-12 20:18:38.443773
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    argv = [sys.argv[0], '--version']
    with mock.patch.object(sys, 'argv', argv):
        with mock.patch.object(argparse.ArgumentParser, 'exit') as mock_exit:
            with mock.patch.object(ansible.cli.CLI, 'version') as mock_version:
                ansible.cli.cli.AnsibleVersion()
                mock_exit.assert_called_once_with(0)
                mock_version.assert_called_once_with(getattr(mock_version.ansible_version, 'prog'))



# Generated at 2022-06-12 20:18:46.733462
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('-') == '-'

    test_paths = [
        ('/some/path', '/some/path'),
        ('some/path', os.path.join(os.getcwd(), 'some/path'))
    ]
    for path, expected_path in test_paths:
        assert unfrack_path()(path) == expected_path


# Generated at 2022-06-12 20:18:47.375487
# Unit test for function version
def test_version():
    assert version()
    assert version('ansible')

# Generated at 2022-06-12 20:18:56.060210
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    path_s = '/home/foo/bar'
    path_d = '~/foo/bar'
    path_r = '@DEFAULT@/foo/bar'

    def check(exp, test, msg=None):
        if exp != test:
            if msg is None:
                msg = 'expected %s, got %s' % (exp, test)
            raise AssertionError(msg)

    exp = '/home/foo/bar'
    test = maybe_unfrack_path('/')(path_d)
    check(exp, test, 'home relative path not properly expanded')

    exp = '@DEFAULT@/foo/bar'
    test = maybe_unfrack_path('@DEFAULT@/')(path_d)
    check(exp, test, 'config path not properly ignored')


# Generated at 2022-06-12 20:19:02.308416
# Unit test for function version
def test_version():
    assert 'ansible-molecule [core' in version('ansible-molecule')
    assert __version__ in version('ansible-molecule')
    assert '.git' in version('ansible-molecule')
    assert 'config file' in version('ansible-molecule')
    assert 'python version' in version('ansible-molecule')
    assert 'jinja version' in version('ansible-molecule')
    assert 'libyaml' in version('ansible-molecule')

#
# Base Parser from which all others descend
#

# Generated at 2022-06-12 20:19:08.428666
# Unit test for function version
def test_version():
    assert version('prog') == 'prog [core 2.9.9]\n  config file = /etc/ansible/ansible.cfg\n  configured module search path = Default w/o overrides\n  ansible python module location = /home/user1/ansible/lib/ansible\n  ansible collection location = /home/user1/.ansible/collections\n  executable location = /home/user1/ansible/bin/ansible\n  python version = 3.7.3 (default, Apr  3 2019, 05:39:12)\n [GCC 8.3.0]\n  jinja version = 2.10.1\n  libyaml = 1.2.2\n'

# Generated at 2022-06-12 20:19:13.658631
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-b')
    parser.add_argument('-c')
    parser.add_argument('-d')

    test_result = ['  -c ACTION', '  -d ACTION', '  -a ACTION', '  -b ACTION']
    result = []
    for line in SortingHelpFormatter().format_help(parser).split('\n'):
        if line.strip().startswith('-'):
            result.append(line.strip())
    assert result == test_result



# Generated at 2022-06-12 20:19:15.938202
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("/tmp")("/tmp/ansible/") == "/tmp/ansible/"
    assert maybe_unfrack_path("/tmp")("/ansible/") == "/ansible/"
    assert maybe_unfrack_path("/tmp")("ansible") == "ansible"



# Generated at 2022-06-12 20:19:20.613111
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    class Parser:
        def __init__(self, prog):
            self.prog = prog

        def exit(self):
            pass
    parser = Parser('')
    av = AnsibleVersion()
    av(parser, None, None, None)



# Generated at 2022-06-12 20:20:32.564001
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/etc/ansible') == unfrackpath('/etc/ansible')



# Generated at 2022-06-12 20:20:35.669409
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('/usr/lib/python3/dist-packages/ansible') == '/usr/lib/python3/dist-packages/ansible'
    assert unfrack_path(pathsep=True)('path/to/ansible,path/to/library') == ['/path/to/ansible', '/path/to/library']

# Generated at 2022-06-12 20:20:41.404729
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(":")(":/home/user") == ":/home/user"
    assert maybe_unfrack_path(":")(":~/file") == ":~/file"
    assert maybe_unfrack_path(":")(":~user2/file") == ":~user2/file"
    assert maybe_unfrack_path(":")("/home/user") == "/home/user"
    assert maybe_unfrack_path(":")("~/file") == "~/file"
    assert maybe_unfrack_path(":")("~user2/file") == "~user2/file"


# Generated at 2022-06-12 20:20:50.965376
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # test with pre_defined actions
    test_SortingHelpFormatter_parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    test_SortingHelpFormatter_parser.add_argument('foo')
    test_SortingHelpFormatter_parser.add_argument('-s', '--spam', action='store_true')
    test_SortingHelpFormatter_parser.add_argument('-a', '--aardvark', action='store_true')
    test_SortingHelpFormatter_parser.add_argument('-n', '--nuts', action='store_true')
    test_SortingHelpFormatter_parser.parse_args([])
    test_SortingHelpFormatter_result = test_SortingHelpFormatter_parser.format_help()
    test_SortingHelpFormatter

# Generated at 2022-06-12 20:20:57.340057
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # print out the result of a test, return the result (True/False)
    def do_test(value, expected):
        actual = maybe_unfrack_path('!')  # the '!' character is somewhat random
        result = actual(value) == expected
        print(('%s -> %s: %s' % (value, expected, result)).encode('utf-8'))
        return result

    # run the tests

# Generated at 2022-06-12 20:21:02.633665
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true', default=False)
    parser.add_argument('-b', '--bar', action='store_false', default=True)
    parser.add_argument('--baz', action='store_false', default=True)
    parser.add_argument('-a', '--apple', action='store_true', default=False)

    parser.epilog = 'output:\n  -b --bar\n  --baz\n  -a --apple\n  --foo'
    parser.print_help()
    print("---")

    parser.formatter_class = SortingHelpFormatter
    parser.print_help()
    print("---")

    formatter = SortingHelpFormatter(parser.prog)
   

# Generated at 2022-06-12 20:21:05.596270
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(description='test',
                                     formatter_class=SortingHelpFormatter)
    parser.add_argument('--zoo')
    parser.add_argument('--boo')
    parser.add_argument('--foo')
    parser.print_help()


# Generated at 2022-06-12 20:21:13.969994
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    from ansible.module_utils.six.moves.urllib.parse import urlparse
    my_url = "https://www.somewhere.org/my_collection/my_module"
    beacon = '~'
    value = '~/my/path'
    assert (maybe_unfrack_path(beacon)(value) == value)
    assert (maybe_unfrack_path(beacon)(my_url) == my_url)
    my_url = "https://www.somewhere.org/~/my_collection/my_module"
    assert (maybe_unfrack_path(beacon)(my_url) == "https://www.somewhere.org/" + unfrackpath('~/my_collection/my_module'))


# Generated at 2022-06-12 20:21:20.930209
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    base = __file__
    # the first value is the possibly prefixed path and the second
    # the beacon which is used to prefix the path
    paths = [
        # absolute
        ("/x/y/z", "@"),
        ("~/x/y/z", "@"),
        ("@/x/y/z", "@"),
        # relative
        ("x/y/z", "@"),
        ("./x/y/z", "@"),
        ("../x/y/z", "@"),
        # special
        ("-", "@")
    ]
    for path, beacon in paths:
        assert maybe_unfrack_path(beacon)(path) == path



# Generated at 2022-06-12 20:21:26.880886
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    f = maybe_unfrack_path('@')
    assert f('@/home/user/foo/bar') == '@' + os.path.abspath('/home/user/foo/bar')
    assert f('@/tmp/foo') == '@' + os.path.abspath('/tmp/foo')
    assert f('/tmp/foo') == '/tmp/foo'
    assert f('/tmp/foo/') == '/tmp/foo/'


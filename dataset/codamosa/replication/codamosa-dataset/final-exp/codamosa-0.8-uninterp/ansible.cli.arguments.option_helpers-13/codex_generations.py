

# Generated at 2022-06-12 20:12:42.651759
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    # Test 1: add_runas_prompt_options(parser)
    parser = argparse.ArgumentParser(description='ansible')
    add_runas_prompt_options(parser)
    argv = ['--become-password-file', '/home/xavierc/ansible/ansible_password',
    '--become-method', 'su', '--become-user', 'root']
    args = parser.parse_args(argv)
    assert args.become_method == 'su'
    assert args.become_user == 'root'

    # Test 2: add_runas_prompt_options(parser, runas_group)
    runas_group = parser.add_argument_group("Privilege Escalation Options", "control how and which user you become as on target hosts")
    add_

# Generated at 2022-06-12 20:12:46.016585
# Unit test for function add_vault_options
def test_add_vault_options():
      parser = argparse.ArgumentParser()
      add_vault_options(parser)
      opt = parser.parse_args(['--vault-id', 'secret', '--vault-id', 'another', '--ask-vault-password'])
      assert opt.vault_ids == ['secret', 'another']
      assert opt.ask_vault_pass
test_add_vault_options()

# Generated at 2022-06-12 20:12:47.546634
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    assert_true('-i' in parser._option_string_actions)



# Generated at 2022-06-12 20:12:56.500677
# Unit test for function add_runas_options
def test_add_runas_options():
  parser = argparse.ArgumentParser()
  add_runas_options(parser)


# Generated at 2022-06-12 20:13:00.775604
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    options = parser.parse_args()

    assert options.inventory is None
    assert not options.listhosts
    assert options.subset == C.DEFAULT_SUBSET
#
# Functions to parse optparse/argparse options
#


# Generated at 2022-06-12 20:13:06.100289
# Unit test for function add_runas_options
def test_add_runas_options():

    parser = argparse.ArgumentParser()
    add_runas_options(parser)

    options = parser.parse_args([])
    assert not options.become
    assert isinstance(options.become_method, str)
    assert isinstance(options.become_user, six.string_types)

    options = parser.parse_args(['--become', '--become-method', 'foo', '--become-user', 'bar'])
    assert options.become
    assert options.become_method == 'foo'
    assert options.become_user == 'bar'



# Generated at 2022-06-12 20:13:11.709083
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser(prog="test", usage="test", formatter_class=SortingHelpFormatter)
    add_meta_options(parser)
    parser.parse_args(["--help"])



# Generated at 2022-06-12 20:13:15.714659
# Unit test for function add_subset_options
def test_add_subset_options():
    """ ansible.utils.add_subset_options:
    Test whether module add_subset_options from utils.py successfully works. """
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    options = parser.parse_args(["-t", "test1", "-t", "test2", "--skip-tags", "skip1"])
    assert (options.tags == ["test1", "test2"]) and (options.skip_tags == ["skip1"])



# Generated at 2022-06-12 20:13:23.363524
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args("-i foo".split())
    assert args.inventory == ['foo']

    args = parser.parse_args("--inventory-file foo".split())
    assert args.inventory == ['foo']

    args = parser.parse_args("--inventory-file foo --list-hosts".split())
    assert args.listhosts == True

    args = parser.parse_args("--inventory-file foo --limit bar".split())
    assert args.subset == 'bar'


# Generated at 2022-06-12 20:13:27.343285
# Unit test for function add_inventory_options
def test_add_inventory_options():
    from unittest.mock import Mock
    parser_mock = Mock()
    add_inventory_options(parser_mock)
    assert parser_mock.add_argument.assert_called_with('-i', '--inventory', '--inventory-file', dest='inventory', action="append",
                                                 help="specify inventory host path or comma separated host list. --inventory-file is deprecated")


# Generated at 2022-06-12 20:13:44.764319
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('foo') == unfrackpath('foo')
    assert unfrack_path(pathsep=True)('foo') == [unfrackpath('foo')]
    assert unfrack_path(pathsep=False)('foo:' + ('bar' * 100)) == unfrackpath('foo:bar' * 100)
    assert unfrack_path(pathsep=True)('foo:' + ('bar' * 100)) == [unfrackpath('foo'), unfrackpath('bar' * 100)]
    assert unfrack_path(pathsep=True)('foo:bar:baz') == [unfrackpath('foo'), unfrackpath('bar'), unfrackpath('baz')]

# Generated at 2022-06-12 20:13:50.354088
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser()
    add_async_options(parser)
    arg = ['ansible-playbook', '-B', '-P']
    ns = parser.parse_args(arg)
    assert(ns.seconds == 0)
    assert(ns.poll_interval == C.DEFAULT_POLL_INTERVAL)



# Generated at 2022-06-12 20:13:51.330209
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    check_me = maybe_unfrack_path('@')
    assert check_me('@test/test') == '@test/test'



# Generated at 2022-06-12 20:13:59.298461
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser()
    add_async_options(parser)
    args = parser.parse_args(['-B', '5'])
    assert args.poll_interval == 5
    assert args.seconds == 5
    args = parser.parse_args(['-BP', '5'])
    assert args.poll_interval == C.DEFAULT_POLL_INTERVAL
    assert args.seconds == 5
    args = parser.parse_args(['-P', '5'])
    assert args.poll_interval == 5
    assert args.seconds == 0
    args = parser.parse_args([])
    assert args.poll_interval == C.DEFAULT_POLL_INTERVAL
    assert args.seconds == 0



# Generated at 2022-06-12 20:14:00.766009
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    start_path = "~/ansible"
    assert maybe_unfrack_path("~")(start_path) == "~" + os.path.expanduser("~/ansible")



# Generated at 2022-06-12 20:14:07.864104
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = create_base_parser(description="description", epilog="epilog")
    add_meta_options(parser)
    args = parser.parse_known_args([])
    assert args[0].force_handlers == C.DEFAULT_FORCE_HANDLERS
    args = parser.parse_known_args(["--force-handlers"])
    assert args[0].force_handlers == True


# Generated at 2022-06-12 20:14:14.791401
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from ansible.module_utils.common.tree import TreeData
    from ansible.module_utils.six import PY3

    def stdout():
        return sys.stdout

    def output_version(parser):
        parser.exit()

    class FakeNamespace:
        def __init__(self):
            self.verbosity = 0

    class FakeOptionString:
        def __init__(self):
            self.option_string = None

    class FakeArgParse:
        def exit(self):
            return

        def error(self, msg):
            return

    fake_namespace = FakeNamespace()
    fake_option_string = FakeOptionString()
    fake_argparse = FakeArgParse()
    tree_instance = TreeData()

# Generated at 2022-06-12 20:14:24.962186
# Unit test for function unfrack_path
def test_unfrack_path():
    # Testing unfrack_path
    assert unfrack_path()('/foo/bar') == unfrackpath('/foo/bar')
    assert unfrack_path()('bar') == unfrackpath('bar')
    assert unfrack_path()('bar') == unfrackpath('bar')
    assert unfrack_path()('-') == '-'
    # Testing unfrack_path with paths separated by the system's path separator
    assert unfrack_path('pathsep')('/foo/bar:bar') == [unfrackpath('/foo/bar'), unfrackpath('bar')]
    # Testing unfrack_path with a list as input

# Generated at 2022-06-12 20:14:29.389915
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser(prog='test_argument')
    add_async_options(parser)
    options_list = ['-P', '--poll', '-B', '--background']
    for option in options_list:
        assert option in parser._actions[0].option_strings


# Generated at 2022-06-12 20:14:36.201661
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(beacon="~")('~/foo') == '~/foo'
    assert maybe_unfrack_path(beacon="~")('~foo') == '~foo'
    assert maybe_unfrack_path(beacon="~")('~/bar/') == '~/bar/'
    assert maybe_unfrack_path(beacon="~")('/foo/~/bar') == '/foo/~/bar'
    assert maybe_unfrack_path(beacon="~")('foo') == 'foo'



# Generated at 2022-06-12 20:14:51.540503
# Unit test for function unfrack_path
def test_unfrack_path():
    """
    This function should be removed once the unit tests are implemented in
    the test framework.
    """

    # testing unfrackpath function
    assert os.path.isabs(unfrackpath('/some/absolute/path/to/file')) == True
    assert os.path.isabs(unfrackpath('some/absolute/path/to/file')) == True
    assert os.path.isabs(unfrackpath('$HOME/some/relative/path/to/file')) == False
    assert os.path.isabs(unfrackpath('~/some/relative/path/to/file')) == False
    assert os.path.isabs(unfrackpath('~/some/path/to/file')) == False

# Generated at 2022-06-12 20:14:55.993106
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    args = parser.parse_args(["-t", "test"])
    assert args.tree == "test"
    assert args.one_line == True


# Generated at 2022-06-12 20:14:58.366821
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
     AnsibleVersion(option_strings=['--version'])(
         parser=None,
         namespace=Namespace(),
         values=None,
         option_string=None
     )

# Generated at 2022-06-12 20:15:05.545471
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    opts, _ = parser.parse_known_args(['--tree','/tmp/'])
    assert opts.tree == '/tmp/'
    opts, _ = parser.parse_known_args(['-t','/tmp/'])
    assert opts.tree == '/tmp/'
    opts, _ = parser.parse_known_args(['--tree'])
    assert opts.tree == None
    opts, _ = parser.parse_known_args(['-t'])
    assert opts.tree == None
    opts, _ = parser.parse_known_args(['--tree=/tmp/'])
    assert opts.tree == '/tmp/'
    opts, _ = parser.parse_known_args

# Generated at 2022-06-12 20:15:11.350219
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/foo/bar') == '@' + os.path.abspath(os.path.expanduser('~/foo/bar'))
    assert maybe_unfrack_path('@')('~/foo/bar') == '~/foo/bar'
# End unit test.



# Generated at 2022-06-12 20:15:20.753230
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    argparse_stdout_old = argparse.ArgumentParser(formatter_class=argparse.HelpFormatter)
    argparse_stdout_new = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    args = ["--help"]

# Generated at 2022-06-12 20:15:24.991681
# Unit test for function unfrack_path
def test_unfrack_path():
    # Return absolute path if the input path is relative path
    assert os.path.isabs(unfrack_path()('./test.yml'))
    # Return the input path if the input path is absolute path
    assert unfrack_path()('./test.yml') == unfrack_path()(os.path.abspath('./test.yml'))



# Generated at 2022-06-12 20:15:36.989646
# Unit test for function unfrack_path
def test_unfrack_path():
    # Test 1: Check that the unfrack_path function will return the correct path for a file,
    # given all possible types of paths
    # Test 1.1: Check that a simple path is returned with no changes
    assert unfrack_path('/foo/bar') == '/foo/bar'
    # Test 1.2: Check that a path using ~/ is returned as an expanded path
    assert unfrack_path('~/foo/bar') == os.path.expanduser('~/foo/bar')
    # Test 1.3: Check that a path using ~username is returned as an expanded path
    assert unfrack_path('~username/foo/bar') == os.path.expanduser('~username/foo/bar')
    # Test 1.4: Check that a path using environment variables is returned as an expanded path
    env_user = os.get

# Generated at 2022-06-12 20:15:46.130863
# Unit test for function version
def test_version():
    import ansible

    test_result = version()
    test_result = test_result.replace(ansible.__file__, '[ANSIBLE_INSTALL_DIR]')
    test_result = test_result.replace(sys.argv[0], '[ANSIBLE_EXE_LOCATION]')


# Generated at 2022-06-12 20:15:52.193601
# Unit test for function unfrack_path
def test_unfrack_path():
    print("TESTING unfrack_path")
    test_cases = [("/etc/ansible/hosts", "/etc/ansible/hosts"),
                  ("/etc/ansible/hosts:/etc/zshrc", ['/etc/ansible/hosts', '/etc/zshrc'])]
    for test_case in test_cases:
        assert unfrack_path(pathsep=True)(test_case[0]) == test_case[1]
        print("SUCCESS")



# Generated at 2022-06-12 20:16:04.103939
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    unfrack_test = "~/.ansible/tmp/this/is/a/test"
    test_1 = "/~/.ansible/tmp/this/is/a/test"
    test_2 = "~/.ansible/.this/is/a/test"
    test_3 = "~/ansible/tmp/this/is/a/test"
    test_4 = "~/.ansible/tmp/this/is/a/te~t"
    unfrack = maybe_unfrack_path("/")
    assert unfrack(test_1) == "/" + unfrack_test
    assert unfrack(test_2) == test_2
    assert unfrack(test_3) == test_3
    assert unfrack(test_4) == test_4

# Generated at 2022-06-12 20:16:12.626938
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_path = '/foo/bar'
    test_path_out = maybe_unfrack_path('@')('@%s' % test_path)
    assert(('@' + unfrackpath(test_path)) == test_path_out)
    # Calling with a bogus path should return the path unaltered
    test_path_bogus = '/foo/bogus'
    test_path_bogus_out = maybe_unfrack_path('@')(test_path_bogus)
    assert(test_path_bogus == test_path_bogus_out)


#
# Subcommands
#

# Generated at 2022-06-12 20:16:21.913429
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/foo') == '/foo'
    assert unfrack_path()('bar') == 'bar'
    assert unfrack_path()('./bar') == './bar'
    assert unfrack_path()('dir/bar') == 'dir/bar'
    assert unfrack_path()(os.path.join(os.getcwd(),'dir/bar')) == os.path.join(os.getcwd(),'dir/bar')
    assert unfrack_path()('~/bar') == os.path.expanduser('~/bar')
    assert unfrack_path()('~/bar') != '~/bar'
    assert unfrack_path()('/foo/bar') == unfrackpath('/foo/bar')
    assert unfrack_path()('/foo/bar/') == unfrack

# Generated at 2022-06-12 20:16:27.345210
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    f = maybe_unfrack_path("@")
    result = f("@test/path")
    assert result == "@test/path"
    result = f("./test/path")
    assert result == "@test/path"
    result = f("@~/test/path")
    assert result == "@~/test/path"
    result = f("~/test/path")
    assert result == "@~/test/path"



# Generated at 2022-06-12 20:16:29.868674
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('!')('!bar') == '!%s' % unfrackpath('bar')
    assert maybe_unfrack_path('*')('*bar') == '*%s' % unfrackpath('bar')
    assert maybe_unfrack_path('-')('-bar') == '-%s' % unfrackpath('bar')



# Generated at 2022-06-12 20:16:37.278495
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    sys.argv = sys.argv[:1] + ['--version']
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion, nargs=0)
    parser.add_argument('--foo', action='store_true')

    # call
    args = parser.parse_args()
    assert args.foo is False



# Generated at 2022-06-12 20:16:44.476997
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    "ansible-doc --version produces a non-empty string"
    # FIXME: this test exceeds the normal maximum length for a line (79)
    # FIXME: this test should be in tests/units/doc_fragments instead of tests/units/doc_module
    # FIXME: this test is not really a unit test because it works with stdout
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', nargs=0, action=AnsibleVersion)
    args = parser.parse_args(['--version'])
    ansible_version = to_native(version('ansible-doc'))
    assert len(ansible_version) > 0


# Generated at 2022-06-12 20:16:52.235854
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    sys.path.insert(0, '..')
    from ansible.cli import CLI
    import ansible.__main__ as main
    my_cli = CLI(['ansible', '--version'])
    my_main = main.AnsibleProgram(my_cli.parser, runas_opts=my_cli.runas_opts)
    my_main.parse()
    assert hasattr(my_main, 'run')
    my_main.run()
    assert main.VERSION == __version__
    sys.path.remove('..')


# Generated at 2022-06-12 20:16:57.426721
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("@")("@/") == "@/"
    assert maybe_unfrack_path("@")("@/a") == "@/a"
    assert maybe_unfrack_path("@")("@/a/") == "@/a/"
    assert maybe_unfrack_path("@")("@a") == "@a"
    assert maybe_unfrack_path("@")("/a") == "/a"
    assert maybe_unfrack_path("@")("a") == "a"
test_maybe_unfrack_path()



# Generated at 2022-06-12 20:17:03.406040
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('foo') == unfrackpath('foo')
    assert unfrack_path(pathsep=True)('a:b:c') == [unfrackpath('a'), unfrackpath('b'), unfrackpath('c')]
    assert unfrack_path()('-') == '-'
    assert unfrack_path(pathsep=True)('-') == ['-']

# for invoking methods on types without knowing what the subclass is called

# Generated at 2022-06-12 20:17:17.049074
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    from jinja2 import __version__ as j2_version
    from ansible.module_utils.common.yaml import HAS_LIBYAML, yaml_load
    from ansible.release import __version__
    from ansible.utils.path import unfrackpath

    # Setup option parser
    parser = SortingHelpFormatter()
    parser.prog = 'test'

    # Setup argument list
    arglist = [
        '-f', '--foo',
        '-b', '--bar',
        '-x', '--baz',
    ]

    # Setup help string
    helpstr = 'help'

    # Test Action (1)
    actions = [argparse.Action(s, help=helpstr) for s in arglist]

    # Check help string
    got = parser.format_help().strip

# Generated at 2022-06-12 20:17:23.048830
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/path/to/file') == '@' + unfrackpath('/path/to/file')
    assert maybe_unfrack_path('@')('@@/path/to/file') == '@@/path/to/file'
    assert maybe_unfrack_path('@')('@@') == '@@'
    assert maybe_unfrack_path('@')('@') == '@'



# Generated at 2022-06-12 20:17:23.908314
# Unit test for function version
def test_version():
    assert isinstance(version(), str)

# Generated at 2022-06-12 20:17:33.601623
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action="store_true", help="first")
    parser.add_argument('-b', action="store_true", help="second")
    parser.add_argument('-c', action="store_true", help='third')
    parser.add_argument('-d', action="store_true", help='fourth')
    formatter = SortingHelpFormatter()
    for action in parser._actions:
        margin = len(formatter._format_action_invocation(action))
        text = formatter._expand_help(action)
        lines = formatter._split_lines(text, 80)
        for line in lines:
            print(formatter._pad_text(line, margin))



# Generated at 2022-06-12 20:17:42.757939
# Unit test for function unfrack_path
def test_unfrack_path():
    assert '~/test' == unfrack_path()('~/test')
    assert '~/test2' == unfrack_path()('~/test2')
    assert '/tmp/test' == unfrack_path()('/tmp/test')
    assert '/tmp/test' == unfrack_path()('/tmp/test')
    assert '~/test' == unfrack_path(True)('~/test')
    assert '/tmp/test' == unfrack_path(True)('/tmp/test')
    assert '~/test' == unfrack_path(True)('~/test:/tmp/test')
    assert '/tmp/test' == unfrack_path(True)('/tmp/test:~/test')

# Generated at 2022-06-12 20:17:49.816715
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    p = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    p.add_argument('--foo', help='foo')
    p.add_argument('--bar', help='bar')

    # --help with short options is sorted '--bar', '--foo'
    with open(os.devnull, 'w') as f:
        sys.stderr = f
        p.print_help()



# Generated at 2022-06-12 20:17:50.898864
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('foo') == unfrackpath('foo')


# Generated at 2022-06-12 20:17:57.458780
# Unit test for function ensure_value
def test_ensure_value():
    import unittest
    import argparse
    class TestEnsureValue(unittest.TestCase):
        def setUp(self):
            self.parser = argparse.ArgumentParser(description='Test ensure value')
            self.set_arg = self.parser.add_argument("--set", type=list, default=None)
            self.not_set_arg = self.parser.add_argument("--not-set", type=list, default=None)
            self.not_set_empty_list = self.parser.add_argument("--not-set-empty-list", type=list, default=[])

        def test_init_ensure_list(self):
            args = self.parser.parse_args("--set foo --set bar".split())

# Generated at 2022-06-12 20:18:04.137720
# Unit test for function ensure_value
def test_ensure_value():
    class FakeNamespace(object):
        def __init__(self):
            self.env = None
            self.roles_path = None
    fake_namespace = FakeNamespace()
    fake_list = []
    ensure_value(fake_namespace, 'env', fake_list)
    ensure_value(fake_namespace, 'env', fake_list)
    ensure_value(fake_namespace, 'roles_path', fake_list)
    assert fake_namespace.env is fake_list
    assert fake_namespace.roles_path is not fake_list



# Generated at 2022-06-12 20:18:10.746873
# Unit test for function ensure_value
def test_ensure_value():
    class FakeNamespace(object):
        def __init__(self):
            self.name = None
            self.other_name = None
            self.attr = None
        def __repr__(self):
            return "FakeNamespace({0},{1},{2})".format(self.name, self.other_name, self.attr)

    fake = FakeNamespace()
    ensure_value(fake, 'name', 'test')
    ensure_value(fake, 'other_name', 'test2')
    ensure_value(fake, 'other_name', 'test3')
    ensure_value(fake, 'attr', 'test4')
    assert fake.name == 'test'
    assert fake.other_name == 'test2'
    ensure_value(fake, 'name', 'test2')

# Generated at 2022-06-12 20:18:23.085153
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    """
    Test AnsibleVersion() __call__ method by setting a value to
    option_string and namespace attributes and test that the __call__
    method returns the value of the attributes.
    """
    option_string = '10.11.6'
    namespace = '10.11.6'
    assert AnsibleVersion.__call__(self, option_string, namespace) == namespace



# Generated at 2022-06-12 20:18:26.933167
# Unit test for function version
def test_version():
    with open("test_version.txt", "r") as ver_test:
        version_test = version().splitlines()
        assert version_test == ver_test.read().splitlines()


# Generated at 2022-06-12 20:18:35.058614
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test the results of calling maybe_unfrack_path() in various situations.
    # If any of these tests fail, then something has changed
    # in the expected results of this function.
    AT = '@'
    HOME = '~/'
    DOT = './'
    assert(maybe_unfrack_path(AT)(AT) == AT)
    assert(maybe_unfrack_path(AT)('@/foo') == AT + HOME + 'foo')
    assert(maybe_unfrack_path(AT)('@~/foo') == AT + HOME + 'foo')
    assert(maybe_unfrack_path(DOT)('~/foo') == HOME + 'foo')
    assert(maybe_unfrack_path(DOT)('./foo') == DOT + 'foo')

# Generated at 2022-06-12 20:18:36.271200
# Unit test for function version
def test_version():
    assert version().startswith(__version__)

# Generated at 2022-06-12 20:18:38.416811
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(False)("/usr/bin/python")
    p = unfrack_path(False)('/usr/bin/python /usr/local/bin/python')
    assert len(p) == 2
# end


# Generated at 2022-06-12 20:18:40.619668
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser(prog='ansible-playbook', prog_name='ansible-playbook')
    namespace = parser.parse_args([])
    values = []
    option_string = None
    action = AnsibleVersion()
    action(parser, namespace, values, option_string)



# Generated at 2022-06-12 20:18:43.487108
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    res = maybe_unfrack_path('@DEFAULT')
    assert res('@DEFAULT/new') == '@DEFAULT/new'
    assert res('@DEFAULT/new/new') == '@DEFAULT/new/new'



# Generated at 2022-06-12 20:18:48.511324
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # Create a test Action object e as an object of class AnsibleVersion
    e = AnsibleVersion('--version')
    # Create a test parser object p
    p = argparse.ArgumentParser('ansible --version')
    # Use the object p to call method __call__ of class AnsibleVersion in e and
    # the test method do nothing, but print out the returned value.
    print(e.__call__(p, None, None, None))



# Generated at 2022-06-12 20:18:50.701803
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("@")("@/foo/bar") == "@@/foo/bar"
    assert maybe_unfrack_path("@")("@@/foo/bar") == "@@/foo/bar"

#
# Options Parsers
#

# Generated at 2022-06-12 20:18:58.373564
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    value = "/etc/ansible/roles:/etc/ansible/roles.bak"
    expected = "/etc/ansible/roles:/etc/ansible/roles.bak"
    assert maybe_unfrack_path(":")(value) == expected
    value = "/etc/ansible/roles:/etc/ansible/roles.bak"
    expected = "~/.ansible/roles:/etc/ansible/roles"
    assert maybe_unfrack_path(":")("~/.ansible/roles:/etc/ansible/roles") == expected


# Generated at 2022-06-12 20:19:13.121694
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/foo/bar') == '/foo/bar'
    assert unfrack_path(pathsep=True)('/foo/bar:/baz') == ['/foo/bar', '/baz']



# Generated at 2022-06-12 20:19:18.645736
# Unit test for function unfrack_path
def test_unfrack_path():
    path_list = ['roles/routing/library', 'roles/routing/library/', './roles/routing/library/']
    expected = 'roles/routing/library'
    for role_path in path_list:
        assert unfrack_path(False)(role_path) == expected
    assert unfrack_path(False)('roles/routing/library/') == expected
test_unfrack_path()



# Generated at 2022-06-12 20:19:29.381660
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/a/path/to/something') == '@/a/path/to/something'
    assert maybe_unfrack_path('@')('@a/path/to/something') == '@/a/path/to/something'
    assert maybe_unfrack_path('@')('@@a/path/to/something') == '@/a/path/to/something'
    assert maybe_unfrack_path('@')('@b/path/to/something') == '@b/path/to/something'
    assert maybe_unfrack_path('@')('/a/path/to/something') == '/a/path/to/something'
    assert maybe_unfrack_path('@')('/a/path/to/something')

# Generated at 2022-06-12 20:19:33.863780
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    try:
        if not os.environ['ANSIBLE_CONFIG']:
            os.environ['ANSIBLE_CONFIG'] = "~/.ansible.cfg"
    except KeyError:
        os.environ['ANSIBLE_CONFIG'] = "~/.ansible.cfg"
    assert maybe_unfrack_path(constants.CONFIG_LOCATION_FILE_BEACON)(constants.CONFIG_LOCATION_FILE_BEACON + constants.CONFIG_LOCATION) == os.environ['ANSIBLE_CONFIG']


# Generated at 2022-06-12 20:19:44.309973
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = version('ansible')

# Generated at 2022-06-12 20:19:50.509479
# Unit test for function unfrack_path
def test_unfrack_path():
    # Ensures expected output for unfrack_path, return the same thing for all paths.
    cwd_path = os.getcwd()
    expected_path = unfrackpath(cwd_path)
    unfrack_fn = unfrack_path()
    assert isinstance(unfrack_fn, Callable)
    assert unfrack_fn(cwd_path) == expected_path


#
# Generic Options
#
# Generic opts are opts which are added to multiple parsers.
#
# Note: opts must be in alphabetical order here and in `get_base_opts`.

# Generated at 2022-06-12 20:19:57.027041
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    parser = argparse.ArgumentParser(description='prepends items instead of appending them')
    parser.add_argument('--foo', action=PrependListAction)
    args = parser.parse_args(['--foo', 'abc'])
    assert args.foo == ['abc'], args.foo
    args = parser.parse_args(['--foo', 'abc', '--foo', 'def'])
    assert args.foo == ['def', 'abc'], args.foo

#
# Common options handling
#

# Generated at 2022-06-12 20:20:05.183798
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    fixture = ('#', '/etc/ansible/roles:/usr/share/ansible/roles')
    expected = ('#', '/etc/ansible/roles:/usr/share/ansible/roles')
    actual = maybe_unfrack_path('#')(fixture[1])
    assert actual == expected

    fixture = ('~', '/etc/ansible/roles:/usr/share/ansible/roles')
    expected = ('~', '/etc/ansible/roles:/usr/share/ansible/roles')
    actual = maybe_unfrack_path('#')(fixture[1])
    assert actual == expected

    fixture = ('~', '#/etc/ansible/roles:/usr/share/ansible/roles')

# Generated at 2022-06-12 20:20:10.573398
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # create a list of 'argparse.Action' objects.
    class Action(object):
        def __init__(self, option_strings):
            self.option_strings = option_strings
    actions = [
        # first one, non-option
        Action([]),
        # next, options that share the same prefix string
        Action(['-f', '--foo']),
        Action(['-f']),
        # a positional argument
        Action([None]),
        # finally, options not sharing the same prefix
        Action(['-b', '--bar']),
        Action(['--bar']),
        Action(['-x']),
    ]

    formatter = SortingHelpFormatter()
    formatter.add_arguments(actions)
    assert formatter._action_max_length == 7



# Generated at 2022-06-12 20:20:21.141452
# Unit test for function unfrack_path

# Generated at 2022-06-12 20:20:51.581877
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test that (~) is is replaced with the user's home dir
    assert maybe_unfrack_path('~')('~/.ansible/tmp') == os.path.expanduser('~/.ansible/tmp'), \
        "Test that ~ is replaced with the user's home directory."


#
# Global command line Options
#

# Generated at 2022-06-12 20:20:54.869077
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # Arrange
    parser = argparse.ArgumentParser()
    namespace = argparse.Namespace()
    option_string = None
    values = None

    # Act
    test_ansible_version = AnsibleVersion(parser, namespace, values, option_string)

    # Assert
    assert ansible.__version__ == test_ansible_version


# Generated at 2022-06-12 20:21:03.798404
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():

    f = maybe_unfrack_path('@')
    assert f('@@foo') == '@@foo'
    assert f('@/foo') == '@/foo'
    assert f('@//foo') == '@//foo'
    assert f('@/foo/bar') == '@/foo/bar'
    assert f('@/foo/./bar') == '@/foo/bar'
    assert f('@/foo/../bar') == '@/bar'
    assert f('@foo/bar') == '@foo/bar'



# Generated at 2022-06-12 20:21:08.135303
# Unit test for function version
def test_version():
    assert version('ansible-config') == 'ansible-config [core 2.9.10]  config file = /etc/ansible/ansible.cfg\n  configured module search path = Default w/o overrides\n  ansible python module location = /usr/lib/python2.7/site-packages/ansible\n  ansible collection location = /usr/share/ansible/collections:/usr/share/ansible/collections\n  executable location = /usr/bin/ansible-config\n  python version = 2.7.5 (default, Mar  2 2014, 22:49:27)\n[GCC 4.8.2 20140120 (Red Hat 4.8.2-13)]\n  jinja version = 2.8\n  libyaml = False'

# Generated at 2022-06-12 20:21:11.848949
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', dest='version', default=False, action=AnsibleVersion, nargs=0)
    options = parser.parse_args(["--version"])
    if options.version != False:
        options.version()



# Generated at 2022-06-12 20:21:20.102936
# Unit test for method __call__ of class AnsibleVersion

# Generated at 2022-06-12 20:21:29.351999
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # init function under test and some variables
    maybe_unfrack_path_to_test = maybe_unfrack_path('beacon')
    real_path = '/usr/share/ansible/'
    unfrack_path = '@/usr/share/ansible/'
    # test if the function handles correctly a real path or @path
    assert maybe_unfrack_path_to_test(unfrack_path) == '@' + real_path
    assert maybe_unfrack_path_to_test(real_path) == real_path
    assert maybe_unfrack_path_to_test('') == ''
    #test if the function handles correctly wrong input

# Generated at 2022-06-12 20:21:36.327068
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("b")("b@/abc") == "b@/abc"
    assert maybe_unfrack_path("b")("b@/def") == "b@/def"
    if os.path.sep == "/":
        assert maybe_unfrack_path("b")("~/abc") == "~/abc"
        assert maybe_unfrack_path("b")("~/def") == "~/def"
        assert maybe_unfrack_path("b")("/abc") == "/abc"
        assert maybe_unfrack_path("b")("/def") == "/def"
    else:
        assert maybe_unfrack_path("b")("b@~/abc") == "b@/abc"
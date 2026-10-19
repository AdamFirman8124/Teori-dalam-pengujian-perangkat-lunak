

# Generated at 2022-06-12 20:12:03.403433
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    parser.parse_args(['--vault-id', 'foo'])
    parser.parse_args(['--vault-password-file', 'bar'])
    # TODO: test handling of multiple --vault-id and --vault-password-file arguments


#
# Functions to create an option parser for each ansible-* script
#


# Generated at 2022-06-12 20:12:12.892910
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    required_action = PrependListAction(option_strings='--option', dest='dest',
                                        nargs=0, const='default', required=True,
                                        help='test option')
    assert required_action.option_strings == ['--option']
    assert required_action.dest == 'dest'
    assert required_action.nargs == 0
    assert required_action.const == 'default'
    assert required_action.required
    assert required_action.help == 'test option'
    assert required_action.default is None

    optional_action = PrependListAction(option_strings='--option', dest='dest',
                                        nargs=1, const=None, required=False, type='str',
                                        default='default', help='test option')
    assert optional_action.option_strings == ['--option']
    assert optional

# Generated at 2022-06-12 20:12:20.873806
# Unit test for function unfrack_path
def test_unfrack_path():
    from ansible.constants import ANSIBALLZ_LIB_PATH

    # Check for pathsep:
    result_pathsep = unfrack_path(pathsep=True)(ANSIBALLZ_LIB_PATH)
    assert result_pathsep == [ANSIBALLZ_LIB_PATH]

    # Check for pathsep:
    result_path = unfrack_path()(ANSIBALLZ_LIB_PATH)
    assert result_path == ANSIBALLZ_LIB_PATH

    # Check for pathsep:
    result_path_stdin = unfrack_path()(C.DEFAULT_STDIN_PATH)
    assert result_path_stdin == C.DEFAULT_STDIN_PATH



# Generated at 2022-06-12 20:12:25.284801
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser(prog='ansible', conflict_handler='resolve')
    add_check_options(parser)
    opts, args = parser.parse_known_args()
    assert opts.check is False
    assert opts.syntax is False
    assert opts.diff is True


# Generated at 2022-06-12 20:12:33.712546
# Unit test for function add_runtask_options
def test_add_runtask_options():
    test_parser = argparse.ArgumentParser()
    add_runtask_options(test_parser)
    test_cmdline = "--extra-vars=key1=val1 --extra-vars=@/path/to/file.yaml --extra-vars=@/path/to/file2.yaml key2=val2"
    actual_results = test_parser.parse_args(test_cmdline.split())
    expected_results = argparse.Namespace(extra_vars=[
                                          "key1=val1",
                                          "/path/to/file.yaml",
                                          "/path/to/file2.yaml",
                                          "key2=val2",
                                          ])
    assert actual_results == expected_results


# Generated at 2022-06-12 20:12:40.906115
# Unit test for function add_module_options
def test_add_module_options():
    parser = argparse.ArgumentParser()
    add_module_options(parser)
    parser.parse_args(['-M', '/usr/share/ansible/plugins/modules:/usr/local/share/ansible/plugins/modules:/usr/share/ansible/plugins/module_utils:/usr/local/share/ansible/plugins/module_utils'])

# Generated at 2022-06-12 20:12:51.561973
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import sys
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.cli.arguments import OptionsParser
    from ansible.utils.plugin_docs import get_docstring

    if sys.version_info[0] == 2:

        class AnsibleVersion():
            def __call__(self, parser, namespace, values, option_string=None):
                ansible_version = to_native(version(getattr(parser, 'prog')))
                return ansible_version
    else:

        class AnsibleVersion():
            def __call__(self, parser, namespace, values, option_string=None):
                ansible_version = to_native(version(getattr(parser, 'prog')))
                return ansible_version

    action = AnsibleVersion()
    parser = OptionsParser

# Generated at 2022-06-12 20:12:57.047104
# Unit test for function add_tasknoplay_options
def test_add_tasknoplay_options():
    parser = argparse.ArgumentParser()
    add_tasknoplay_options(parser)
    args = parser.parse_args(['--task-timeout', '1'])
    assert len(vars(args)) == 1



# Generated at 2022-06-12 20:13:05.070176
# Unit test for function add_runtask_options
def test_add_runtask_options():
    """
    TEST: Add options for commands that run a task
    """
    parser=argparse.ArgumentParser()
    add_runtask_options(parser)
    args=parser.parse_args(["-e", "'host=abc'"])
    assert args.extra_vars == ["'host=abc'"]
    args=parser.parse_args(["-e", "host=abc"])
    assert args.extra_vars == ["host=abc"]
    args=parser.parse_args(["-e", "host=abc", "-e", "host=def"])
    assert args.extra_vars == ["host=abc", "host=def"]


# Generated at 2022-06-12 20:13:08.764601
# Unit test for function add_meta_options
def test_add_meta_options():
    """
    # Testing add_meta_options function
    #
    """
    parser = argparse.ArgumentParser(description="add_meta_options")
    add_meta_options(parser)
    options = test_args(parser, ['--force-handlers', '--flush-cache'])
    assert options.force_handlers == True
    assert options.flush_cache == True

# Generated at 2022-06-12 20:13:36.762088
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace(object):
        pass
    namespace = Namespace()
    # func ensure_value should set empty list to 'dest' when namespace.dest is None
    ensure_value(namespace, dest, [])
    assert namespace.dest == []
    # func ensure_value should set empty list to 'abc' when a.abc is None
    ensure_value(namespace, 'abc', [])
    assert namespace.abc == []
    # func ensure_value should not set empty list to 'dest' when namespace.dest is not None
    namespace.dest = 'test'
    ensure_value(namespace, dest, [])
    assert namespace.dest == 'test'



# Generated at 2022-06-12 20:13:41.229411
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    from ansible.module_utils.facts.virtual.net_tools import maybe_unfrack_path

    assert maybe_unfrack_path("-")("-/a/b") == '-/a/b'
    assert maybe_unfrack_path("-")("-\\a\\b") == '-/a/b'



# Generated at 2022-06-12 20:13:44.428612
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = argparse.ArgumentParser()
    add_fork_options(parser)
    parsed_arguments = parser.parse_args([])
    assert parsed_arguments.forks == '5'


# Generated at 2022-06-12 20:13:46.172171
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    parser.parse_args(['-u', 'me'])



# Generated at 2022-06-12 20:13:54.572033
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    from ansible.utils.display import Display
    display = Display()
    test = PrependListAction(['--test'], 'test_field')
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-t', action=test)

    parsed = parser.parse_args(['-t', '10', '-t', '20'])
    display.display(to_native(parsed.test_field))
    assert parsed.test_field == ['20', '10']


# Generated at 2022-06-12 20:14:04.843210
# Unit test for function add_connect_options
def test_add_connect_options():
    from ansible.utils.display import Display
    from ansible.module_utils.common._collections_compat import Mapping
    mock_parser = Mapping()
    mock_parser.add_argument_group = Mapping()
    mock_parser.add_argument_group.mock_add_argument_group = Mapping()
    mock_parser.add_argument = Mapping()
    mock_parser.add_mutually_exclusive_group = Mapping()
    mock_parser.add_mutually_exclusive_group.add_argument = Mapping()
    mock_parser.add_mutually_exclusive_group.add_argument.return_value = None
    mock_display = Display()
    add_connect_options(mock_parser)
    assert 'localhost' in mock_parser.options

# Generated at 2022-06-12 20:14:11.250525
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace:
        class A:
            pass
    ns = Namespace()
    assert ensure_value(ns, 'a', Namespace.A) is Namespace.A
    assert ensure_value(ns, 'a', Namespace.A) is ns.a
    assert ns.a is not None
    ns.a = None
    assert ns.a is None
    assert ensure_value(ns, 'a', Namespace.A) is ns.a
    assert ns.a is not None
# End unit tests for function ensure_value



# Generated at 2022-06-12 20:14:20.662303
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = Mock()
    add_inventory_options(parser)
    parser.add_argument.assert_any_call('-i', '--inventory', '--inventory-file', dest='inventory', action="append",
                        help="specify inventory host path or comma separated host list. --inventory-file is deprecated")
    parser.add_argument.assert_any_call('--list-hosts', dest='listhosts', action='store_true',
                        help='outputs a list of matching hosts; does not execute anything else')
test_add_inventory_options()


# Generated at 2022-06-12 20:14:24.090758
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/a') == '@' + unfrackpath('/a')
    assert maybe_unfrack_path('@')('@a') == '@a'
    pytest.raises(ValueError, maybe_unfrack_path('@'), 'a')



# Generated at 2022-06-12 20:14:32.081649
# Unit test for function add_inventory_options
def test_add_inventory_options():
    """Unit test for function: test_add_inventory_options"""
    parser = argparse.ArgumentParser(epilog='', description='',
                        formatter_class=SortingHelpFormatter)
    add_inventory_options(parser)

    # Test for both short and long options for inventory
    short_options = "-i inventory_path"
    long_options = "--inventory-file inventory_path"
    for options in (short_options, long_options):
        args = parser.parse_args(options.split())
        assert args.inventory == ['inventory_path']



# Generated at 2022-06-12 20:14:38.859009
# Unit test for function unfrack_path
def test_unfrack_path():
    result = unfrack_path()('/tmp/path')
    assert 'tmp/path' == result

# Generated at 2022-06-12 20:14:41.621821
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser()
    add_async_options(parser)
    options = parser.parse_args('-B 1000 -P 30'.split())
    assert options.poll_interval == 30
    assert options.seconds == 1000



# Generated at 2022-06-12 20:14:42.794016
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    return parser
# Unit test: _test_add_inventory_options()

# Generated at 2022-06-12 20:14:45.281115
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.parse_args()


#
# Helpers
#

# Generated at 2022-06-12 20:14:48.519260
# Unit test for function add_async_options
def test_add_async_options():
    # Test output
    parser = argparse.ArgumentParser(prog='test_add_async_options')
    add_async_options(parser)
    parser.print_help()


# Generated at 2022-06-12 20:14:58.671439
# Unit test for function unfrack_path
def test_unfrack_path():
    def check_unfrack(test_cases):
        for input_path, expected_path in test_cases.items():
            assert unfrack_path()(input_path) == expected_path

    def check_unfrack_pathsep(test_cases):
        for input_path, expected_path in test_cases.items():
            path_list = input_path.split(os.pathsep)
            result_list = [unfrackpath(x) for x in path_list]
            assert unfrack_path(pathsep=True)(input_path) == result_list


# Generated at 2022-06-12 20:15:01.642879
# Unit test for function add_async_options
def test_add_async_options():
    parser = _set_up_parser_for_tests()
    add_async_options(parser)
    _assert_dicts_equal(parser.parse_args(['-P', '1', '-B', '0'])
                        , dict(poll_interval='1', seconds='0'))


# Generated at 2022-06-12 20:15:03.784460
# Unit test for function add_subset_options
def test_add_subset_options():
    """Unit test for function add_subset_options"""
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    args = parser.parse_args()
    assert args.tags == C.TAGS_RUN
    assert args.skip_tags == C.TAGS_SKIP




# Generated at 2022-06-12 20:15:11.746991
# Unit test for function add_inventory_options
def test_add_inventory_options():
    arr = []
    parser = create_base_parser(prog='prog', usage="usage", desc='desc', epilog='epilog')
    add_inventory_options(parser)
    parse_args_return = parser.parse_args(arr)
    assert parse_args_return.inventory == None
    assert parse_args_return.listhosts == False
    assert parse_args_return.subset == 'all'
    arr = ['--inventory=inventory_path', '--list-hosts', '-l', 'subset']
    parse_args_return = parser.parse_args(arr)
    assert parse_args_return.inventory == [u'inventory_path']
    assert parse_args_return.listhosts == True
    assert parse_args_return.subset == 'subset'


# Generated at 2022-06-12 20:15:17.989549
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    args = parser.parse_args(['-t', 'a', '-t', 'b'])
    assert args.tags == ['a', 'b']
    args = parser.parse_args(['--skip-tags', 'c', '--skip-tags', 'd'])
    assert args.skip_tags == ['c', 'd']



# Generated at 2022-06-12 20:15:30.367473
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-b')
    parser.add_argument('-a')
    parser.add_argument('-c')
    parser.add_argument('-d')
    assert parser.format_help() == """usage: [-h] [-b B] [-a A] [-c C] [-d D]

optional arguments:
  -h, --help  show this help message and exit
  -b B
  -a A
  -c C
  -d D
"""

#
# Utils
#

# Generated at 2022-06-12 20:15:41.826245
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('~/.ansible/test')('~/.ansible/test/test') == '~/.ansible/test/test'
    assert maybe_unfrack_path('~/.ansible/test')('~/.ansible/test/test') == '~/.ansible/test/test'
    assert maybe_unfrack_path('~/.ansible/test')('~/.ansible/test') == '~/.ansible/test'
    assert maybe_unfrack_path('~/.ansible/test')('~/.ansible/test/') == '~/.ansible/test/'
    assert maybe_unfrack_path('~/.ansible/test')('~/.ansible/test/test/') == '~/.ansible/test/test/'
    assert maybe_

# Generated at 2022-06-12 20:15:42.824125
# Unit test for function version
def test_version():
    assert version()



# Generated at 2022-06-12 20:15:52.881575
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # create a parser that will be used in the tests
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    subparsers = parser.add_subparsers(dest='subcommand')
    # create a subparser
    subcommand = subparsers.add_parser('playbook')
    subcommand.add_argument('-K', '--ask-su-pass', dest='su_pass', default=None, action='store',
                            help="Prompt the user for a privilege escalation password")
    subcommand.add_argument('-b', '--become', dest='become', action='store_true',
                            help="run operations with become (does not imply password prompting)")

# Generated at 2022-06-12 20:16:00.787179
# Unit test for function maybe_unfrack_path

# Generated at 2022-06-12 20:16:11.090137
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/etc/ansible/roles:/etc/ansible/roles_additional') == ['/etc/ansible/roles', '/etc/ansible/roles_additional']
    assert unfrack_path()('/etc/ansible/roles/') == ['/etc/ansible/roles']
    assert unfrack_path()('/etc/ansible/roles') == '/etc/ansible/roles'
    assert unfrack_path()('/etc/ansible/roles/') == '/etc/ansible/roles'
    assert unfrack_path()('-') == '-'
    assert unfrack_path()('.') == './'
    assert unfrack_path()('/') == '/'
    assert unfrack_path()('relative') == 'relative'

# Generated at 2022-06-12 20:16:16.213660
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    option_string = ['-x', '--xoption']
    parser = SortingHelpFormatter(prog='foo',
                                  usage=argparse.SUPPRESS,
                                  option_string=option_string)
    return parser

HAS_OPENSSL = True
try:
    import OpenSSL
except ImportError:
    HAS_OPENSSL = False

try:
    import __main__
    HAS_MAIN = True
except ImportError:
    HAS_MAIN = False

#
# Utility functions
#


# Generated at 2022-06-12 20:16:22.983612
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    class Action:
        def __init__(self, option_strings):
            self.option_strings = option_strings
    fmt = SortingHelpFormatter()
    actions = [Action(['-b']), Action(['-a']), Action(['--foo'])]
    fmt.add_arguments(actions)
    assert '[-a]' in fmt._get_help_string(actions[1])
    assert '[-b]' in fmt._get_help_string(actions[0])
    assert '[--foo]' in fmt._get_help_string(actions[2])



# Generated at 2022-06-12 20:16:23.996166
# Unit test for function version
def test_version():
    assert version()


# Generated at 2022-06-12 20:16:32.582290
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    def check(args, expected):
        parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
        parser.add_argument(args[0], '-a', action='store_true')
        for arg in args[1:]:
            parser.add_argument(arg, '-b', action='store_true')

        output = parser.format_help()
        assert output == expected

    check(['--foo', '--bar', '--baz'], '''\
usage: [-h] [-a] [-b] ...

optional arguments:
  -h, --help  show this help message and exit
  -a
  -b          --bar
              --baz
              --foo\
''')

# Generated at 2022-06-12 20:16:41.280264
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-c', action="store")
    parser.add_argument('-a', action="store")
    parser.add_argument('-b', action="store")
    parser.print_help()

#
# Shared OptionParsers
#

# Generated at 2022-06-12 20:16:51.160770
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/foo/bar') == '@' + unfrackpath('/foo/bar')
    assert maybe_unfrack_path('@')('/foo/bar') == '/foo/bar'
    assert maybe_unfrack_path('@')('@~/foo/bar') == '@' + unfrackpath('~/foo/bar')
    assert maybe_unfrack_path('@')('@@/foo/bar') == '@@/foo/bar'
    assert maybe_unfrack_path('@@')('@@/foo/bar') == '@@' + unfrackpath('/foo/bar')
    assert maybe_unfrack_path('@@')('/foo/bar') == '/foo/bar'

# Generated at 2022-06-12 20:16:52.348307
# Unit test for function version
def test_version():
    assert version('foo') == 'foo [core %s]' % __version__



# Generated at 2022-06-12 20:16:57.948901
# Unit test for function version
def test_version():
    test_text = version('prog')
    assert __ver__ in test_text
    assert 'config file = %s' % C.CONFIG_FILE in test_text
    assert 'configured module search path = %s' % 'Default w/o overrides' in test_text
    assert 'executable location = %s' % sys.argv[0] in test_text
    assert 'python version = %s' % ''.join(sys.version.splitlines()) in test_text
    assert 'jinja version = %s' % j2_version in test_text
    assert 'libyaml = %s' % HAS_LIBYAML in test_text

# Generated at 2022-06-12 20:17:03.744598
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace:
        name = None
    n = Namespace()
    test_value = 'foo'
    assert ensure_value(n, 'name', test_value) == test_value
    test_value2 = 'bar'
    assert ensure_value(n, 'name', test_value2) == test_value
    n.name = test_value2
    assert ensure_value(n, 'name', test_value) == test_value2


# Generated at 2022-06-12 20:17:06.176687
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    parser = argparse.ArgumentParser()
    parser.add_argument('--val', action=PrependListAction, type=int, nargs='+')
    ns = parser.parse_args(['--val', '1', '2', '3', '--val', '4', '5'])

# Generated at 2022-06-12 20:17:11.861001
# Unit test for constructor of class PrependListAction
def test_PrependListAction():

    class Args(object):
        pass

    args     = Args()
    dest     = "foo"
    option_strings = ['--foo', '-f']
    const    = "const"
    default  = "default"
    nargs    = "OPTIONAL"
    type     = "int"
    choices  = "choices"
    required = False
    help     = "help"
    metavar  = "metavar"

    action = PrependListAction(option_strings=option_strings, dest=dest, nargs=nargs, const=const, default=default, type=type,
                 choices=choices, required=required, help=help, metavar=metavar)

    assert action.option_strings ==  ['--foo', '-f']
    assert action.dest == "foo"

# Generated at 2022-06-12 20:17:20.525540
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    x = maybe_unfrack_path('@')
    assert '@/xyz' == x('@./xyz')
    assert '@xyz' == x('@xyz')
    assert '@xyz/' == x('@xyz/')
    assert '@xyz//' == x('@xyz//')
    assert '@xyz' == x('@xyz')
    assert '@@xyz' == x('@@xyz')
    assert '@xyz' == x('@xyz')
    assert '@xyz' == x('@xyz')
    assert '@xyz' == x('@xyz')



# Generated at 2022-06-12 20:17:27.588919
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    action = parser.add_argument("-a", "--aaa", help="arg 1")
    action = parser.add_argument("-c", "--ccc", help="arg 2")
    action = parser.add_argument("-b", "--bbb", help="arg 3")

    expected_help_output = """\
usage: <BLANKLINE>
       [-h] [-a AAA] [-b BBB] [-c CCC]

optional arguments:
  -h, --help  show this help message and exit
  -a AAA      arg 1
  -b BBB      arg 3
  -c CCC      arg 2
""".replace("<BLANKLINE>", " "*8)

    assert parser.format_help() == expected_

# Generated at 2022-06-12 20:17:36.669326
# Unit test for function ensure_value
def test_ensure_value():
    class namespace():
        a = None
        b = 1

    assert(ensure_value(namespace, 'a', 'test') == 'test')
    assert(ensure_value(namespace, 'b', 'test') == 1)

#
# Basic command line option handling for commands.
#

# common options for all commands
common_parser = argparse.ArgumentParser(add_help=False)
common_group = common_parser.add_argument_group('Common Options')
common_group.add_argument('--version', default=False, action='version', version=version(progname='ansible'),
                          help='show program\'s version number and exit')



# Generated at 2022-06-12 20:17:50.145236
# Unit test for function unfrack_path

# Generated at 2022-06-12 20:17:57.114404
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_path = '/home/test/path'
    test_path2 = '/home/test/path2'
    test_beacon = '@'
    unfracked_path = maybe_unfrack_path(test_beacon)(test_beacon + test_path)
    unfracked_path2 = maybe_unfrack_path(test_beacon)(test_path2)

    if unfracked_path == test_path:
        print('test_maybe_unfrack_path passed\n')
    else:
        print('Unfracked path: %s\n' % unfracked_path)
        print('test_maybe_unfrack_path failed\n')

    if unfracked_path2 == test_path2:
        print('test_maybe_unfrack_path passed\n')


# Generated at 2022-06-12 20:18:02.908031
# Unit test for function unfrack_path
def test_unfrack_path():
    assert 'ansible' in unfrack_path()('$HOME/ansible')
    assert 'ansible' in unfrack_path(True)('$HOME/ansible:$HOME/yaml')
    assert 'ansible' in unfrack_path(True)('$HOME/ansible:$HOME/yaml')
    assert unfrack_path()('-') == '-'


# Generated at 2022-06-12 20:18:09.838614
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    class FakeAction(argparse.Action):
        def __init__(self, *args, **kwargs):
            self.option_strings = kwargs.pop('option_strings', [])
            super(FakeAction, self).__init__(*args, **kwargs)

    class FakeParser(argparse.ArgumentParser):
        def format_help(self):
            return 'format_help'

    p = FakeParser()
    p.add_argument('-d', action=FakeAction, option_strings=['-d'])
    p.add_argument('-b', action=FakeAction, option_strings=['-b'])
    p.add_argument('-c', action=FakeAction, option_strings=['-c'])

# Generated at 2022-06-12 20:18:18.801191
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-c')

    class FakeActions:
        def __init__(self, option_strings):
            self.option_strings = option_strings

    actions = [FakeActions(['-a']), FakeActions(['-c']), FakeActions(['-b'])]
    formatter = SortingHelpFormatter(parser)
    formatter.add_arguments(actions)
    help = parser.format_help()
    assert help.index('-a') < help.index('-b') < help.index('-c')



# Generated at 2022-06-12 20:18:24.717954
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-b", "--book", help="book name")
    arg_parse.add_argument("-a", "--author", help="author name")

    output = sys.stdout
    opt_parser = SortingHelpFormatter(prog='PROG', add_help=False)
    opt_parse = arg_parse.parse_args(['-h'])
    opt_parse.print_help(output)
    try:
        assert '-a' < '-b'
    except AssertionError:
        print("ERROR: The output of help is not in a alphabetical order")


#
# CLI flags that are meant to be invoked on the CLI, generally after a module or playbook is specified
#

# Generated at 2022-06-12 20:18:33.797034
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    # Create a list of actions to verify that they are sorted properly by option string.
    def create_arg(cli_option, dest_attr, sort_args_order):
        rval = argparse.Action(option_strings=cli_option, dest=dest_attr)
        rval.sort_args_order = sort_args_order
        return rval
    actions = [
        create_arg(['-h'], 'help', 0),
        create_arg(['-f'], 'f', 1),
        create_arg(['--foo'], 'foo', 2),
        create_arg(['-b'], 'b', 3),
        create_arg(['--bar'], 'bar', 4),
        create_arg(['-c'], 'c', 5),
    ]

    # Use the formatter to sort the list

# Generated at 2022-06-12 20:18:40.426179
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert(maybe_unfrack_path('@')('@/abc') == '@' + unfrackpath('/abc'))
    assert(maybe_unfrack_path('@')('@/a/b/c') == '@' + unfrackpath('/a/b/c'))
    assert(maybe_unfrack_path('@')('@@/a/b/c') == '@@/a/b/c')
    assert(maybe_unfrack_path('@')('@@@/a/b/c') == '@@@/a/b/c')
    assert(maybe_unfrack_path('@')('@') == '@')
    assert(maybe_unfrack_path('@')('a@b') == 'a@b')



# Generated at 2022-06-12 20:18:47.019878
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-x')
    parser.add_argument('-a')
    parser.add_argument('-b')
    parser.add_argument('-c')
    parser.add_argument('-z')
    help_text_lines = parser.format_help().split('\n')
    assert help_text_lines[3] == '-a'
    assert help_text_lines[4] == '-b'
    assert help_text_lines[5] == '-c'
    assert help_text_lines[6] == '-x'
    assert help_text_lines[7] == '-z'



# Generated at 2022-06-12 20:18:51.178778
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/')('/foo') == '/foo'
    assert maybe_unfrack_path('/')('~/foo') == '~/foo'
    assert maybe_unfrack_path('~/')('~/foo') == '~/foo'
    assert maybe_unfrack_path('~/')('~/foo/bar') == '~/foo/bar'
    assert maybe_unfrack_path('~/')('~foo/bar') == '~foo/bar'



# Generated at 2022-06-12 20:19:27.995246
# Unit test for function version
def test_version():
    assert version() == version('')
    assert version().splitlines()[0] == __version__

# Generated at 2022-06-12 20:19:33.641704
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(beacon=b"XXX")(value=b"XXX/foo/bar") == b"XXX/foo/bar"
    assert maybe_unfrack_path(beacon=b"XXX")(value=b"XXX/../../foo/bar") == b"XXX/foo/bar"
    assert maybe_unfrack_path(beacon=b"XXX")(value=b"XXX/foo/bar/../../spam") == b"XXX/spam"
    assert maybe_unfrack_path(beacon=b"XXX")(value=b"/foo/bar") == b"/foo/bar"



# Generated at 2022-06-12 20:19:36.637706
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--z')
    parser.add_argument('--a')
    parser.parse_args(''.split())
# End unit test


# Generated at 2022-06-12 20:19:46.770200
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    class TestSortingHelpFormatter(SortingHelpFormatter):
        def __init__(self, *args, **kwargs):
            SortingHelpFormatter.__init__(self, *args, **kwargs)
            return

        def add_arguments(self, actions):
            super(TestSortingHelpFormatter, self).add_arguments(actions)
            return
    tf = TestSortingHelpFormatter(prog='test_sort_help')
    p = argparse.ArgumentParser(formatter_class=TestSortingHelpFormatter)
    p.add_argument('-z', action="store_true")
    p.add_argument('-a', action="store_true")
    p.add_argument('-f', action="store_true")

# Generated at 2022-06-12 20:19:55.682116
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    print('Testing SortingHelpFormatter.add_arguments()...', end='')
    option_strings = ['--one', '--two', '--three']
    options = []
    for i, s in enumerate(option_strings):
        opt = argparse.Option(s, dest=s[2:])
        opt._option_string_actions[s].help = str(i)
        options.append(opt)
    hf = SortingHelpFormatter()
    hf.add_arguments(options)
    s = hf.format_option_strings(options[1]._option_string_actions[option_strings[1]])
    if s != '--three     1':
        print(s)
        sys.exit(1)

# Generated at 2022-06-12 20:20:04.029258
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(
        description="Unit test for the constructor of class SortingHelpFormatter",
        formatter_class=SortingHelpFormatter)

    parser.add_argument("-c", "--compile", action="store_true",
                        help="compile answers.yaml to a data structure, "
                             "with or without default values, with or without comments.")
    parser.add_argument("--without-defaults", action="store_true",
                        help="compile answers.yaml to a data structure, "
                             "without default values, with or without comments.")
    parser.add_argument("--without-comments", action="store_true",
                        help="compile answers.yaml to a data structure, "
                             "with or without default values, without comments.")

# Generated at 2022-06-12 20:20:07.803677
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("/usr/bin") == "/usr/bin"
    # ansible/config.ini sets ANSIBLE_LIBRARY="/usr/share/ansible:~/.ansible/plugins/modules"
    assert unfrack_path(pathsep=True)("/usr/share/ansible:~/.ansible/plugins/modules") == ['/usr/share/ansible', '/home/group1/.ansible/plugins/modules']


# Generated at 2022-06-12 20:20:12.324382
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(description='foo', formatter_class=SortingHelpFormatter)
    parser.add_argument('b', action='store_true')
    parser.add_argument('a', action='store_true')
    parser.add_argument('c', action='store_true')
    parser.print_help()

#
# CLI specific options
#

# modified from http://stackoverflow.com/a/8521644/1396217

# Generated at 2022-06-12 20:20:21.976074
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    def check_order(actions):
        formatter = SortingHelpFormatter()
        formatter.add_arguments(actions)
        output = formatter.format_help()
        output_lines = output.split("\n")
        pos = output_lines.index("optional arguments:")
        option_strings = []
        for line in output_lines[pos + 1:]:
            if not line:
                break
            option = line.split("  ")[0].strip()
            option_strings.append(option)
        if option_strings == ['-f', '-h', '-k', '-m', '-T']:
            return

# Generated at 2022-06-12 20:20:29.123919
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    unfrack_path = maybe_unfrack_path('@')
    assert unfrack_path('@/tmp/ansible_test') == '@' + unfrackpath('/tmp/ansible_test')
    assert unfrack_path('@tmp/ansible_test') == '@tmp/ansible_test'
    assert unfrack_path('/tmp/ansible_test') == '/tmp/ansible_test'

#
# Command line argument management
#

# Generated at 2022-06-12 20:21:19.813295
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_strings = {
        '/foo': False,
        '@/foo': True,
        '@@/foo': False,
        '@@@/foo': False,
        '@@@@/foo': False,
    }
    for test_str in test_strings:
        result = maybe_unfrack_path('@')(test_str)
        assert (test_strings[test_str] == result.startswith('@'))



# Generated at 2022-06-12 20:21:28.901776
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/')('/my/preferred/path/to/file') == '/my/preferred/path/to/file'
    assert maybe_unfrack_path('~')('~/my/preferred/path/to/file') == '~/my/preferred/path/to/file'
    assert maybe_unfrack_path('~')('~/my/preferred/path/to/file') != '~my/preferred/path/to/file'
    assert maybe_unfrack_path('~')('~my/preferred/path/to/file') == '~/my/preferred/path/to/file'

# Generated at 2022-06-12 20:21:35.627882
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_strings = ['@test/tmp', '@/test/tmp', '@@test/tmp', '@@/test/tmp', '@nope', '@nope/tmp', 'test', '@test/tmp/test', '@@test/tmp/test']

    def output():
        print(' test_string @prefix ansible_path')

    output()

    for i in test_strings:
        print(' ' + i.ljust(20) + str(maybe_unfrack_path('@')(i)))

    output()

    for i in test_strings:
        print(' ' + i.ljust(20) + str(maybe_unfrack_path('@@')(i)))

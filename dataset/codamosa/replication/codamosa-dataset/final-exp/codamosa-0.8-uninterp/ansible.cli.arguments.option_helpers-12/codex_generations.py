

# Generated at 2022-06-12 20:12:17.874163
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(
        formatter_class=SortingHelpFormatter
    )
    add_connect_options(parser)

    options = parser.parse_args(['--private-key', 'pri_key.pem'])
    assert options.private_key_file == unfrackpath('pri_key.pem')

    options = parser.parse_args(['-u', 'me', '-c', 'ssh',
                                 '-T', '2',
                                 '--ssh-common-args', '-C',
                                 '--sftp-extra-args', '-f', '-l',
                                 '--scp-extra-args', '-l',
                                 '--ssh-extra-args', '-R'])
    assert options.remote_user == 'me'

# Generated at 2022-06-12 20:12:19.623833
# Unit test for function add_check_options
def test_add_check_options():
    assert add_check_options is not None


# Generated at 2022-06-12 20:12:23.783139
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    result = parser.parse_args(['-t', '/some/path'])
    assert result.tree == '/some/path'



# Generated at 2022-06-12 20:12:27.908170
# Unit test for function add_vault_options
def test_add_vault_options():
    #Test to check if add_vault_options() is adding an option to parser
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    assert parser._action_groups[-1]._group_actions[1].dest=='ask_vault_pass'


# Generated at 2022-06-12 20:12:35.222770
# Unit test for function add_vault_options
def test_add_vault_options():

    parser_new = argparse.ArgumentParser()
    add_vault_options(parser_new)

    argv = ['--vault-id', 'passwd', '--ask-vault-password', '--vault-password-file', 'passfile']
    args = parser_new.parse_args(argv)

    assert args.vault_ids
    assert args.ask_vault_pass
    assert args.vault_password_files


# Generated at 2022-06-12 20:12:46.480742
# Unit test for function add_runas_options
def test_add_runas_options():

    arg_parser = argparse.ArgumentParser(prog='ansible-inventory')
    add_runas_options(arg_parser)

    # Test parsing of arguments
    args = arg_parser.parse_args(['--become', '--become-method', 'sudo', '--become-user', 'root', '--become-ask-pass', '--ask-pass', '--ask-su-pass'])
    assert args.become == True
    assert args.become_method == 'sudo'
    assert args.become_user == 'root'
    assert args.become_ask_pass == True
    assert args.ask_pass == True
    assert args.ask_su_pass == True



# Generated at 2022-06-12 20:12:56.976044
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    import io
    from mock import patch
    from units.compat.mock import MagicMock, PropertyMock
    from ansible.module_utils.common.arguments import SortingHelpFormatter
    from ansible.cli import CLI
    from ansible.cli.arguments import add_runas_prompt_options

    class Options(object):
        class connection(object):
            class local(object):
                executable = 'python'

    options = Options()

    parser = CLI.base_parser(cli_args=['--become-password-file=/test'])
    parser.formatter_class = SortingHelpFormatter
    add_runas_prompt_options(parser)

    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        parser.parse

# Generated at 2022-06-12 20:13:03.695584
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    ans_cmd_line_str = """Test command line
-t
--tip
-v
--validate
-C
--check
--list-hosts
-k
--ask-pass
-K
--ask-become-pass
--ask-become-pass-prompt
--become-password-file
--become-pass-file
--become-method
--become-user
-b
--become
"""
    ans_runas_pass_group_str = """Become Options
-K
--ask-become-pass
--become-password-file
--become-pass-file
"""
    ans_runas_group_str = """Become Options
--become-method
--become-user
-b
--become
"""


# Generated at 2022-06-12 20:13:05.487391
# Unit test for function add_tasknoplay_options
def test_add_tasknoplay_options():
    """Test function add_tasknoplay_options"""
    result = add_tasknoplay_options(argparse.ArgumentParser())
    # FIXME: any assertion here?
    print(type(result))



# Generated at 2022-06-12 20:13:07.896755
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    namespace = argparse.Namespace()
    PrependListAction([], "dest")(parser=None, namespace=namespace, values=["values"], option_string="option_string")
    assert namespace.dest == ["values"]



# Generated at 2022-06-12 20:13:29.006592
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('') == None
    assert unfrack_path()('.') == os.path.abspath('.')
    assert unfrack_path()('~') == os.path.expanduser('~')
    assert unfrack_path()('./.') == os.path.abspath('./.')
    assert unfrack_path()('~/.') == os.path.abspath(os.path.expanduser('~/.'))
    assert unfrack_path()('././.') == os.path.abspath('././.')
    assert unfrack_path()('~/../.') == os.path.abspath(os.path.expanduser('~/../.'))


# Generated at 2022-06-12 20:13:33.743283
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = create_base_parser("test_add_meta_options")
    add_meta_options(parser)
    args = parser.parse_args("--force-handlers --flush-cache".split(" "))
    assert args.force_handlers == True
    assert args.flush_cache == True


# Generated at 2022-06-12 20:13:36.550458
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    options = parser.parse_args(['--flush-cache'])
    assert options.flush_cache



# Generated at 2022-06-12 20:13:41.994952
# Unit test for function ensure_value
def test_ensure_value():
    class FakeNamespace(object):
        pass

    ns = FakeNamespace()
    test_value = 'test value'
    ensure_value(ns, 'test_value', test_value)
    assert ns.test_value == test_value

    test_value2 = 'test value2'
    ensure_value(ns, 'test_value', test_value2)
    assert ns.test_value == test_value2



# Generated at 2022-06-12 20:13:52.353178
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():

    def get_parser():
        # -------------------------------------------
        # create parser with some options/arguments
        # -------------------------------------------
        parser = argparse.ArgumentParser()
        parser.add_argument('--foo', action=PrependListAction)
        parser.add_argument('--bar', action=PrependListAction)
        parser.add_argument('--baz', action=PrependListAction)
        parser.add_argument('--fob', action=PrependListAction)
        parser.add_argument('--fuz', action=PrependListAction)
        return parser
    # -------------------------------------------
    # test PrependListAction
    # -------------------------------------------
    parser = get_parser()
    # use the same argument more than once

# Generated at 2022-06-12 20:13:59.294605
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)

    args = parser.parse_args([])
    assert args.flush_cache == False
    assert args.force_handlers == C.DEFAULT_FORCE_HANDLERS

    args = parser.parse_args(['--flush-cache'])
    assert args.flush_cache == True

    args = parser.parse_args(['--force-handlers'])
    assert args.force_handlers == True



# Generated at 2022-06-12 20:14:04.914921
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)

    args = parser.parse_args(['-i', 'invent1,invent2', '-l', 'lim1'])
    assert args.inventory == ['invent1,invent2']
    assert args.listhosts is False
    assert args.subset == 'lim1'



# Generated at 2022-06-12 20:14:08.157323
# Unit test for function version
def test_version():
    assert 'ansible-doc' in version('ansible-doc')
    assert 'config file =' in version('ansible-doc')
    assert 'ansible python module location =' in version('ansible-doc')

# Generated at 2022-06-12 20:14:14.596212
# Unit test for function add_connect_options
def test_add_connect_options():
    parser=argparse.ArgumentParser()
    add_connect_options(parser)
    assert parser.parse_args(['--private-key','./mykey.key','--ssh-common-args','C:\Windows\System32\cmd.exe'])
    assert parser.parse_args(['--user','administrator','--ssh-extra-args','-v'])
    assert parser.parse_args(['-k','--connection','local','--connection-password-file','mypass.txt','-c','paramiko','--sftp-extra-args','-f'])
    assert parser.parse_args(['--timeout','-9'])
    assert parser.parse_args(['--scp-extra-args','-l'])



# Generated at 2022-06-12 20:14:24.277447
# Unit test for function add_module_options
def test_add_module_options():
    ''' add_module_options will add -M, --module-path and default value is None.
    '''
    module_path = ''
    ddefault = dict(DEFAULT_MODULE_PATH=module_path)
    cc = C.Config()
    cc.DEFAULT_MODULE_PATH = None
    cc.update_config_from_definitions(ddefault)
    parser = argparse.ArgumentParser()
    add_module_options(parser)
    parser.parse_args(['-M', '/test/foo:/test/bar'])
    args = parser.parse_args(['-M', '/test/foo:/test/bar'])
    assert args.module_path == '/test/foo:/test/bar'

# Generated at 2022-06-12 20:14:33.156245
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('roles/role1') == unfrackpath('roles/role1')
    assert unfrack_path()('roles/role1:roles/role2') == unfrackpath('roles/role1')
    assert unfrack_path(True)('roles/role1:roles/role2') == [unfrackpath('roles/role1'), unfrackpath('roles/role2')]


# Generated at 2022-06-12 20:14:39.817536
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert '%%HOME%%/.ansible' == maybe_unfrack_path('%%')('%%HOME%%/.ansible')
    assert '~/.ansible' == maybe_unfrack_path('%')('~/.ansible')
    assert '~/.ansible' == maybe_unfrack_path('%%')('~/.ansible')
    assert '~/.ansible' == maybe_unfrack_path('%')('~/.ansible')
    assert '~/.ansible' == maybe_unfrack_path('%')('~/.ansible')



# Generated at 2022-06-12 20:14:46.768101
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-c', action="store", dest="c")
    parser.add_argument('-b', action="store", dest="b")
    parser.add_argument('-a', action="store", dest="a")
    assert parser.format_help().startswith('usage:')



# Generated at 2022-06-12 20:14:51.073487
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--foo')
    parser.add_argument('--bar')
    parser.add_argument('--baz')
    #
    # just make sure nothing crashes here
    #
    parser.format_help()



# Generated at 2022-06-12 20:14:54.992520
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser(
        prog='test_AnsibleVersion.py'
    )
    parser.add_argument('--version', action=AnsibleVersion)
    args = parser.parse_args()



# Generated at 2022-06-12 20:15:00.511768
# Unit test for function version
def test_version():
    assert 'ansible-config' in version('ansible-config')
    assert 'ansible-console' in version('ansible-console')
    assert __version__ in version()
    assert 'python version = ' in version()
    assert 'config file = ' in version()
    assert 'configured module search path = ' in version()
    assert 'ansible collection location = ' in version()
    assert 'executable location = ' in version()
    assert 'jinja2 version = ' in version()
    assert 'libyaml = ' in version()



# Generated at 2022-06-12 20:15:05.302597
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser(prog='ansible-test')
    add_async_options(parser)

    args = ['-P', '42', '-B', '666']
    result = parser.parse_args(args)
    assert result.poll_interval == 42
    assert result.seconds == 666

# end of unit test for function add_async_options


# Generated at 2022-06-12 20:15:12.234642
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = 'Ansible {0}\n'.format(__version__)
    action = AnsibleVersion('version', None, None, None)
    parser = argparse.ArgumentParser(prog='ansible-config')
    out = to_native(ansible_version)
    try:
        from unittest.mock import patch
        with patch('ansible.config.cli.AnsibleVersion.print', return_value=None) as mock_print:
            action(parser, None, None)
            mock_print.assert_called_with(out)
    except ImportError:
        import mock
        with mock.patch('ansible.config.cli.AnsibleVersion.print', return_value=None) as mock_print:
            action(parser, None, None)
            mock_print.assert_called

# Generated at 2022-06-12 20:15:18.454748
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    p1 = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    p1.add_argument('--bar')
    p1.add_argument('--foo', default=3)
    p1.add_argument('-q', '-v', action='store_true')
    p1.add_argument('-b', action='store_false')
    p1.add_argument('--frob', '-f', nargs=2)
    p1.add_argument('--foo-bar', action='store_true')
    p1.add_argument('--foo-bing')
    p1.add_argument('name', nargs='?')
    p1.add_argument('--foo-bar-bing')

    p1.add_argument('-a', help='a')

# Generated at 2022-06-12 20:15:22.594249
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--foo')
    parser.add_argument('--bar')
    parser.add_argument('--baz')
    parser.print_help()



# Generated at 2022-06-12 20:15:31.509338
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    os.environ['HOME'] = '/home/test'
    assert maybe_unfrack_path('~')('~/test') == '/home/test/test'
    assert maybe_unfrack_path('~')('~') == '/home/test'
    assert maybe_unfrack_path('~')('~test') == '~test'
    assert maybe_unfrack_path('~')('/home/test') == '/home/test'
    del os.environ['HOME']

# Generated at 2022-06-12 20:15:37.308023
# Unit test for function ensure_value
def test_ensure_value():
    class Namespace(object):
        pass
    namespace = Namespace()
    assert ensure_value(namespace, 'x', 'valx') == ['valx']
    assert ensure_value(namespace, 'x', ['valy']) == ['valx', 'valy']
    assert namespace.x == ['valx', 'valy']
# End unit test for function ensure_value



# Generated at 2022-06-12 20:15:40.760991
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('*')('*x') == '*' + unfrackpath('x')
    assert maybe_unfrack_path('*')('*') == '*.'



# Generated at 2022-06-12 20:15:44.666510
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    mock_parser = MagicMock()
    mock_parser.prog = 'prog'
    AnsibleVersion()(mock_parser, None, None, 'option_string')



# Generated at 2022-06-12 20:15:47.819555
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/tmp/1') == '@/tmp/1'
    assert maybe_unfrack_path('@')('@tmp/1') == '@tmp/1'



# Generated at 2022-06-12 20:15:51.478491
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.prog = 'ansible-config'
    args = parser.parse_args()
    ansible_version = to_native(version(parser.prog))
    assert args == ansible_version



# Generated at 2022-06-12 20:15:59.002132
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    unfrackbeacon = '@'
    frackbeacon = '!'
    test_string = '/path/to/something'
    assert (maybe_unfrack_path(unfrackbeacon)(unfrackbeacon + test_string) == unfrackbeacon + os.path.abspath(test_string))
    assert (maybe_unfrack_path(unfrackbeacon)(frackbeacon + test_string) == frackbeacon + test_string)
    assert (maybe_unfrack_path(unfrackbeacon)(test_string) == test_string)
    assert (maybe_unfrack_path(os.path.pathsep)(test_string) == os.path.abspath(test_string))



# Generated at 2022-06-12 20:16:03.180113
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # test no prepend
    assert maybe_unfrack_path('@')('~/.test') == '~/.test'
    # test with prepend
    assert maybe_unfrack_path('@')('@/test') == '@' + os.path.expanduser('~/test')
    # test with prepend and tilde
    assert maybe_unfrack_path('@')('@~/test') == '@' + os.path.expanduser('~/test')



# Generated at 2022-06-12 20:16:09.841927
# Unit test for function version
def test_version():
    result = version('ansible')
    assert result.startswith('ansible')
    assert result.find("config file = None") != -1
    assert result.find("configured module search path = /usr/share/ansible:/usr/share/ansible/roles") != -1
    assert result.find("python version = ") != -1
    assert result.find("jinja version = ") != -1

#
# Create and configure OptionParser
#

# Generated at 2022-06-12 20:16:15.217334
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():

    assert maybe_unfrack_path('@')('@/tmp/test') == '@' + os.path.abspath('/tmp/test')
    assert maybe_unfrack_path('@')('/tmp/test') == '/tmp/test'

    assert maybe_unfrack_path('@@')('@@/tmp/test') == '@@' + os.path.abspath('/tmp/test')
    assert maybe_unfrack_path('@')('@@/tmp/test') is '@@/tmp/test'



# Generated at 2022-06-12 20:16:26.782528
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    assert parser.prog == 'ansible-console'
    ns = argparse.Namespace()
    ansible_version = "ansible %s" % __version__
    action = AnsibleVersion('-v', '--version', action='store_true', help=ansible_version)
    action(parser, ns, None)
    # TODO: Fix this, as right now it throws an UnboundLocalError
    # assert ns.ansible_version == __version__



# Generated at 2022-06-12 20:16:36.810377
# Unit test for function unfrack_path
def test_unfrack_path():
    assert ['/tmp/library1', '/tmp/library2'] == unfrack_path(pathsep=True)('/tmp/library1:/tmp/library2')
    assert ['/tmp/library1', '/tmp/library2'] == unfrack_path(pathsep=True)('/tmp/library1:/tmp/library2:')
    assert ['/tmp/library1', '/tmp/library2'] == unfrack_path(pathsep=True)('/tmp/library1: :/tmp/library2')
    assert ['/tmp/library1', '/tmp/library2'] == unfrack_path(pathsep=True)('/tmp/library1 : :/tmp/library2')

# Generated at 2022-06-12 20:16:41.896766
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/fake/path') == '@' + unfrackpath('/fake/path')
    assert maybe_unfrack_path('@')('@@/fake/path') == '@@/fake/path'
    assert maybe_unfrack_path('@')('/fake/path') == '/fake/path'

#
# Base command line option parsers
#

# Generated at 2022-06-12 20:16:49.413815
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$HOME/test') == '$HOME/test'
    assert maybe_unfrack_path('$')('$ANSIBLE_CONFIG') == '$ANSIBLE_CONFIG'
    assert maybe_unfrack_path('~')('~~/test') == '~/test'
    assert maybe_unfrack_path('~')('~/test') == '~/test'
    assert maybe_unfrack_path('~')('~foo/test') == '~foo/test'



# Generated at 2022-06-12 20:16:55.095320
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():

    # Create a parser for testing
    verString = '%(prog)s 2.7.10'
    parser = argparse.ArgumentParser(prog='ansible-console')
    parser.add_argument('--version',
                        dest='version',
                        action=AnsibleVersion,
                        nargs=0,
                        help='show program\'s version number and exit')
   
    # Perform the parser.  Add the version argument
    parser.parse_args(['--version'])

#
# Common Code
#


# Generated at 2022-06-12 20:16:58.377208
# Unit test for function version
def test_version():
    p = argparse.ArgumentParser()
    p.add_argument("--version", type=version(), action=AnsibleVersion, nargs=0)
    p.add_argument("--foo")
    args = p.parse_args('--version'.split())
    print("ARGS: %s" % args)
    assert args.foo is None


#
# The main AnsibleOptionParser
#

# Generated at 2022-06-12 20:17:07.792306
# Unit test for function version
def test_version():
    # The first assert is redundant, but it is here to make it explicit what the test is testing.
    assert ansible.__version__ == __version__
    # Since the function depends on sys.argv, we provide the test with a value.

# Generated at 2022-06-12 20:17:14.108925
# Unit test for constructor of class PrependListAction
def test_PrependListAction():

    arg_strings = ['-t', '-v']
    nargs = argparse.REMAINDER
    destination = 'prepend_list'
    const = None
    default = None
    type_ = None
    choices = None
    required = False
    help = 'help'
    metavar = 'METAVAR'

    # Verify constructor with all parameters
    action = PrependListAction(arg_strings, destination, nargs, const, default, type_, choices, required, help, metavar)

    # Verify that paramter values were saved
    assert action.option_strings == arg_strings
    assert action.dest == destination
    assert action.nargs == nargs
    assert action.const == const
    assert action.default == default
    assert action.type == type_
    assert action.choices == choices

# Generated at 2022-06-12 20:17:23.907474
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():

    # Automatically determine the best path separator
    # for the platform
    path_separator = os.pathsep

    # The list of paths to test
    control_paths = ['.', './', '..', '../', './a', '../a', './a/b', '../a/b']

    # The beacon is the first character of this string
    # used to determine whether a path is relative or not
    beacon = '.'

    # Call the function to unfrack the path and
    # store the result in a new list
    result_paths = list(map(maybe_unfrack_path(beacon), control_paths))

    # Create an assert list to determine whether the test failed
    assert result_paths == control_paths


# Generated at 2022-06-12 20:17:30.753623
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # result should be same as input if not starting with beacon
    assert '/etc/my.conf' == maybe_unfrack_path(beacon='/')('/etc/my.conf')
    # result should be <beacon> + unfrackpath(/etc/my.conf) if starting with beacon
    assert '/' + unfrackpath('/etc/my.conf') == maybe_unfrack_path(beacon='/')('//etc/my.conf')



# Generated at 2022-06-12 20:17:40.500898
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action=PrependListAction)
    args = parser.parse_args([])
    print(args)


#
# Option values
#

# Generated at 2022-06-12 20:17:47.495798
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version_string = 'ansible 2.8.0\n  config file = %s\n  configured module search path = %s\n  ansible python module location = %s\n  executable location = %s\n  python version = %s\n'
    ansible_version_string = ansible_version_string % (C.DEFAULT_CONFIG_FILE, str(C.DEFAULT_MODULE_PATH), os.path.dirname(ansible.__file__), os.path.realpath(unfrackpath(os.path.expanduser(sys.argv[0]))), str(sys.version_info))

    parser = argparse.ArgumentParser()
    parser.add_argument('version', action=AnsibleVersion)
    parser.prog = 'test_prog'

# Generated at 2022-06-12 20:17:50.322832
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    version_action = AnsibleVersion(option_strings=('--version',), dest='version')
    assert version_action.__call__(None, None, None, option_string=None) is None


# Generated at 2022-06-12 20:17:59.195555
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    my_action = AnsibleVersion(option_strings='--version',
                               dest='version',
                               default=argparse.SUPPRESS,
                               nargs=0,
                               help='show program\'s version number and exit')
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument = lambda *args, **kwargs: None
    my_parser.exit = lambda x: None
    my_parser.prog = 'my_parser'
    my_namespace = argparse.Namespace()
    my_action.__call__(my_parser, my_namespace, None)



# Generated at 2022-06-12 20:18:08.364500
# Unit test for function version

# Generated at 2022-06-12 20:18:19.684761
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    test_parser = argparse.ArgumentParser()
    test_parser.add_argument('-d', '--daemon', action='store_true')
    test_parser.add_argument('-i', '--init', action='store_true')
    test_parser.add_argument('-w', '--work', action='store_true')
    test_parser.add_argument('-1', '--1st')
    test_parser.add_argument('-2', '--2nd')
    test_parser.add_argument('-3', '--3rd')
    test_parser.add_argument('-4', '--4th')
    test_parser.add_argument('-5', '--5th')
    test_parser.add_argument('-6', '--6th')
    test_parser.add_argument

# Generated at 2022-06-12 20:18:27.267704
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    class MyParser(argparse.ArgumentParser):
        def error(self, message):
            pass

    # pylint: disable=unused-variable
    my_parser = MyParser()

    # nargs == 0
    try:
        PrependListAction(option_strings=['--foo'], dest='my_list', nargs=0)
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError'

    # const is not None, nargs != argparse.OPTIONAL
    try:
        PrependListAction(option_strings=['--foo'], dest='my_list', nargs=1, const='bar')
    except ValueError:
        pass
    else:
        assert False, 'expected ValueError'


#
# Argparse
#

# Generated at 2022-06-12 20:18:28.503767
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('.') == os.path.realpath('.')

# Generated at 2022-06-12 20:18:30.750289
# Unit test for function version
def test_version():
    ansible_version = version(prog='ansible-playbook')
    assert "ansible-playbook [core 2.8.0]" in ansible_version

# Generated at 2022-06-12 20:18:35.331862
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    class ArgumentParser(argparse.ArgumentParser):
        def __init__(self, formatter_class=SortingHelpFormatter, **kwargs):
            super(ArgumentParser, self).__init__(formatter_class=formatter_class, **kwargs)
    parser = ArgumentParser()
    parser.add_argument('--bbb')
    parser.add_argument('--aaa')
    parser.format_help()

#
# Help and version functions
#

# Generated at 2022-06-12 20:18:49.003155
# Unit test for function version
def test_version():
    assert version() is not None
    assert version('test_prog') is not None



# Generated at 2022-06-12 20:18:58.303874
# Unit test for function version
def test_version():
    assert(__version__ in version())
    assert("  config file = %s" % C.CONFIG_FILE in version())
    if C.DEFAULT_MODULE_PATH is None:
        cpath = "Default w/o overrides"
    else:
        cpath = C.DEFAULT_MODULE_PATH
    assert("  configured module search path = %s" % cpath in version())
    assert("  ansible python module location = %s" % ':'.join(ansible.__path__) in version())
    assert("  ansible collection location = %s" % ':'.join(C.COLLECTIONS_PATHS) in version())
    assert("  executable location = %s" % sys.argv[0] in version())

# Generated at 2022-06-12 20:19:02.093228
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    _ansible_version = __version__
    __version__ = "2.4.4"
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--version", action=AnsibleVersion)
    args = arg_parser.parse_args(["--version"])
    __version__ = _ansible_version



# Generated at 2022-06-12 20:19:05.766914
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('-z')
    parser.add_argument('-a')
    help = parser.format_help()
    assert to_native(help) == '''usage: [-h] [-z Z] [-a A]

optional arguments:
  -h, --help   show this help message and exit
  -z Z         -z Z
  -a A         -a A
'''


# Generated at 2022-06-12 20:19:10.179259
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # Test for ansible-playbook
    main(args=[], prog="ansible-playbook")
    # Test for ansible-doc
    main(args=[], prog="ansible-doc")
    # Test for ansible-pull
    main(args=[], prog="ansible-pull")
    # Test for ansible-vault
    main(args=[], prog="ansible-vault")


# Generated at 2022-06-12 20:19:12.857543
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser(prog="ansible-console", formatter_class=SortingHelpFormatter)
    ns, args = parser.parse_known_args(args=['--version'])
    assert not args
    assert (getattr(parser, 'prog') != '')



# Generated at 2022-06-12 20:19:16.762665
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument("-b")
    parser.add_argument("-a")
    parser.add_argument("-d")
    parser.add_argument("-c")
    help_output = parser.format_help()
    assert help_output.index('-a') < help_output.index('-b')
    assert help_output.index('-b') < help_output.index('-c')
    assert help_output.index('-c') < help_output.index('-d')
    assert 'usage:' in help_output



# Generated at 2022-06-12 20:19:20.311132
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = version('')
    assert "version" in ansible_version
    assert value[:3] == '2.5'


# Generated at 2022-06-12 20:19:25.830935
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = AnsibleVersion(option_strings=('--version'))
    parser = argparse.ArgumentParser(description='Test ansible version',
                                     prog='ansible-test')
    namespace = argparse.Namespace()
    parser.exit = lambda status=0, message=None: None
    ansible_version(parser, namespace, '1.2.3.4', option_string='--version')



# Generated at 2022-06-12 20:19:33.284855
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():

    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument("-a", help="a")
    parser.add_argument("-b", help="b")
    parser.add_argument("-c", help="c")
    parser.add_argument("-1", help="1")

    help_text = parser.format_help()

    assert help_text.index("-1") < help_text.index("-a")
    assert help_text.index("-a") < help_text.index("-b")
    assert help_text.index("-b") < help_text.index("-c")

#
# Public functions
#

# Generated at 2022-06-12 20:20:11.638277
# Unit test for function version

# Generated at 2022-06-12 20:20:21.889402
# Unit test for function version
def test_version():
    # first test without git info
    gitinfo = _gitinfo
    _gitinfo = lambda: None

# Generated at 2022-06-12 20:20:30.868335
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(prog='ansible', formatter_class=SortingHelpFormatter)
    parser.add_argument('-f', '--foo')
    parser.add_argument('-b', '--bar')
    parser.add_argument('-z', '--baz')

    assert parser.format_help() == '''usage: ansible [-h] [-f FOO] [-b BAR] [-z BAZ]

optional arguments:
  -h, --help     show this help message and exit
  -f FOO         -f FOO
  -b BAR         -b BAR
  -z BAZ         -z BAZ
'''


# Generated at 2022-06-12 20:20:37.031419
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    """
    Assert that SortingHelpFormatter sorts options alphabetically.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-z')
    formatter = SortingHelpFormatter(prog=parser.prog)
    formatter.add_argument(parser._get_option_tuple('-z'))
    formatter.add_argument(parser._get_option_tuple('-a'))
    assert formatter.current_indent == 0
    assert formatter.level == 0
    assert formatter._indent_increment == 2
    assert formatter._long_break_initial == 12
    assert formatter._long_break_subsequent == 2
    assert formatter.max_help_position == 24
    assert formatter.max_help

# Generated at 2022-06-12 20:20:38.989280
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = to_native(version(getattr(parser, 'prog')))
    assert ansible_version


# Generated at 2022-06-12 20:20:42.583024
# Unit test for function unfrack_path
def test_unfrack_path():
    if sys.platform == 'win32':
        assert unfrack_path(True)('C:\\test\\test')==['C:\\test\\test']
        assert unfrack_path()('C:\\test\\test')=='C:\\test\\test'
    else:
        assert unfrack_path(True)('/tmp/test:/tmp/test2')==['/tmp/test', '/tmp/test2']
        assert unfrack_path()('/tmp/test')=='/tmp/test'



# Generated at 2022-06-12 20:20:51.582111
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-c', '--color', help='color code')
    parser.add_argument('-a', '--alpha', help='alpha type')
    parser.add_argument('-b', '--beta', help='beta')
    output = parser.format_help()
    assert to_native(output).startswith(u"usage:")
    assert u"  -a, --alpha" in to_native(output)
    assert u"  -b, --beta" in to_native(output)
    assert u"  -c, --color" in to_native(output)



# Generated at 2022-06-12 20:20:54.620476
# Unit test for function version
def test_version():
    actual = version()
    test_gitinfo = _git_repo_info(os.path.join(__file__, os.pardir, os.pardir))
    if not test_gitinfo:
        assert actual == __version__
    else:
        assert 'last updated' in actual
# end


#
# Option Parsers
#

# Generated at 2022-06-12 20:20:56.211065
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    ansible_version = '2.8.0 ()'
    text = to_native(version('ansible-playbook'))
    assert ansible_version == text


# Generated at 2022-06-12 20:20:59.081010
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bar", action="store_true")
    parser.add_argument("-a", "--awesome", action="store_true")
    shf = SortingHelpFormatter()
    assert shf.add_arguments([parser._actions[1], parser._actions[0]]) is None


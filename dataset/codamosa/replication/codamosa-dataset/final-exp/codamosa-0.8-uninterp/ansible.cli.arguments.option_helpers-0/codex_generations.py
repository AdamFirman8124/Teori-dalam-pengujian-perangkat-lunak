

# Generated at 2022-06-12 20:12:09.456473
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # ansible_version == "ansible 2.8.0"
    ansible_version = version("ansible")
    # expected == "ansible 2.8.0\n"
    expected = str("ansible %s\n" % ansible_version)
    with patch('sys.stdout', new=StringIO()) as fakeOutput:
        namespace = argparse.Namespace()
        parser = argparse.ArgumentParser()
        AnsibleVersion("AnsibleVersion")(parser, namespace, None)
        output = fakeOutput.getvalue().strip()
        assert output == expected



# Generated at 2022-06-12 20:12:17.442172
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    opts = parser.parse_args(['-t', 'tag1', '-t', 'tag2'])
    assert opts.tags == ['tag1', 'tag2']
    opts = parser.parse_args(['--tags', 'tag3', '--tags', 'tag4'])
    assert opts.tags == ['tag3', 'tag4']
    opts = parser.parse_args(['--skip-tags', 'tag5', '--skip-tags', 'tag6'])
    assert opts.skip_tags == ['tag5', 'tag6']



# Generated at 2022-06-12 20:12:18.951164
# Unit test for function add_runas_options
def test_add_runas_options():
    fake_parser = MyParser()
    add_runas_options(fake_parser)
    fake_parser.print_help()


# Generated at 2022-06-12 20:12:23.519165
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    options = parser.parse_args(args=['-to', '/tmp/mydir'])
    assert options.one_line is True
    assert options.tree == '/tmp/mydir'


# Generated at 2022-06-12 20:12:34.687504
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser(
        formatter_class=SortingHelpFormatter,
        prog="ansible-config",
        description="Ansible config tool",
        epilog="More verbose output is available using the '-vvv' option",
        usage="ansible-config [options] <path,> {action} [setting=value] [setting=[value1,value2]]",
    )

    add_vault_options(parser)

# Generated at 2022-06-12 20:12:42.725925
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = argparse.ArgumentParser(description='Ansible Runner')
    add_runas_options(parser)
    results = parser.parse_args(['-b', '-u', 'root', '--become-method', 'su', '--become-user', 'admin'])
    assert results.become
    assert results.become_method == 'su'
    assert results.become_user == 'admin'



# Generated at 2022-06-12 20:12:46.905764
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    options = parser.parse_args(['--force-handlers', '--flush-cache'])
    assert options.force_handlers == True
    assert options.flush_cache == True



# Generated at 2022-06-12 20:12:50.039761
# Unit test for function add_vault_options
def test_add_vault_options():

    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    add_vault_options(parser)
    cargs = ('--vault-password-file', '/tmp/somepasswordfile')
    args = parser.parse_args(cargs)
    assert args.vault_password_files[0] == '/tmp/somepasswordfile'


#
# Functions to extract options from an OptionParser
#


# Generated at 2022-06-12 20:12:53.408695
# Unit test for function add_runtask_options
def test_add_runtask_options():
  parser = argparse.ArgumentParser()
  add_runtask_options(parser)
  options = parser.parse_args()
  assert options.extra_vars is not None


# Generated at 2022-06-12 20:12:57.462157
# Unit test for function add_tasknoplay_options
def test_add_tasknoplay_options():
    parser = argparse.ArgumentParser()
    add_tasknoplay_options(parser)
    args = parser.parse_args(['--task-timeout', '120'])
    assert args.task_timeout == 120



# Generated at 2022-06-12 20:13:13.669438
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    add_connect_options(parser)
    pargs = parser.parse_args(['-c', 'local', '-k', '--connection-password-file', '../test/test_pass_file'])
    assert pargs.connection == 'local'
    assert pargs.ask_pass == True
    assert pargs.connection_password_file == '../test/test_pass_file'



# Generated at 2022-06-12 20:13:16.818440
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = argparse.ArgumentParser()
    add_fork_options(parser)
    args = parser.parse_args(['--forks', '2'])
    assert args.forks == 2


# Generated at 2022-06-12 20:13:19.865614
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("f")("f") == "f"
    assert maybe_unfrack_path("f")("f/") == "f/"
    assert maybe_unfrack_path("f")("fx") == "f" + unfrackpath("x")



# Generated at 2022-06-12 20:13:26.760748
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(
        formatter_class=SortingHelpFormatter,
        description='test parser',
        conflict_handler='resolve',
    )
    add_connect_options(parser)
    args = parser.parse_args(['-u', 'testuser', '-c', 'local', '--ask-pass', '-T', '20', '-k',
                              '--ssh-extra-args', '-R',
                              '--ssh-common-args', 'ProxyCommand'])
    assert args.remote_user == 'testuser'
    assert args.connection == 'local'
    assert args.ask_pass
    assert args.timeout == 20
    assert args.ssh_extra_args == '-R'
    assert args.ssh_common_args == 'ProxyCommand'


# Generated at 2022-06-12 20:13:30.413565
# Unit test for function unfrack_path
def test_unfrack_path():
    test_path = '/users/home/'
    assert unfrack_path()(test_path) == test_path


# Generated at 2022-06-12 20:13:32.019263
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    mup = maybe_unfrack_path(beacon="@")
    assert mup("@/usr/local/bin") == "@/usr/local/bin"
    assert mup("@@/usr/local/bin") == "@@/usr/local/bin"



# Generated at 2022-06-12 20:13:34.594327
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert (maybe_unfrack_path('@')('@/z/x/c')) == '@' + unfrackpath('/z/x/c')
    assert (maybe_unfrack_path('@')('@./z/x/c')) == '@' + unfrackpath('./z/x/c')
    assert (maybe_unfrack_path('@')('./z/x/c')) == './z/x/c'



# Generated at 2022-06-12 20:13:39.722876
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    class AnyClass:
        def __init__(self, option_strings):
            self.option_strings = option_strings

    actions = [AnyClass(['-a', '--arg2']), AnyClass(['-b', '--arg1'])]
    with copy.copy(sys.stdout):
        sys.stdout = open(os.devnull, 'w')
        my_formatter = SortingHelpFormatter()
        my_formatter.add_arguments(actions)  # should not raise



# Generated at 2022-06-12 20:13:41.434791
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'localhost,'])
    assert args.inventory == ['localhost,']


# Generated at 2022-06-12 20:13:51.942852
# Unit test for function unfrack_path
def test_unfrack_path():
    '''
    Test unfrack_path() function.
    '''
    # To test this function, set the CWD GIVEN_CWD,
    # and the environment variable C.DEFAULT_MODULE_PATH GIVEN_PATHS.
    # Both GIVEN_CWD and GIVEN_PATHS SHOULD be in ':' separated format.
    # Run the test, if both are set.
    GIVEN_CWD = os.environ.get('ANSIBLE_TEST_CWD', None)
    GIVEN_PATHS = os.environ.get('ANSIBLE_TEST_DEFAULT_MODULE_PATH', None)


# Generated at 2022-06-12 20:14:16.616135
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    '''assertion tests for maybe_unfrack_path'''
    assert maybe_unfrack_path(beacon='@')(value='@/foo') == '@/foo'
    assert maybe_unfrack_path(beacon='@@')(value='@@/foo') == '@@/foo'
    assert maybe_unfrack_path(beacon='@')(value='@/kinji/abc') == '@/kinji/abc'
    assert maybe_unfrack_path(beacon='@@')(value='@@/kinji/abc') == '@@/kinji/abc'



# Generated at 2022-06-12 20:14:25.636407
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    parser = argparse.ArgumentParser(description='parser')
    action1 = parser.add_argument('--arg1')
    action2 = parser.add_argument('arg2')
    action3 = parser.add_argument('arg3')
    action4 = parser.add_argument('arg4')

    help_parser = SortingHelpFormatter('description')
    help_parser.add_arguments(parser._actions)

    for index, action in enumerate(help_parser._actions):
        if index == 0:
            assert action == action2
        elif index == 1:
            assert action == action3
        elif index == 2:
            assert action == action4
        elif index == 3:
            assert action == action1



# Generated at 2022-06-12 20:14:33.813775
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=True)('/etc/ansible') == ['/etc/ansible']
    assert unfrack_path(pathsep=True)('/etc/ansible:/etc/ansible') == ['/etc/ansible', '/etc/ansible']
    assert unfrack_path(pathsep=True)('/etc/ansible:/etc/ansible:/etc/ansible') == ['/etc/ansible', '/etc/ansible', '/etc/ansible']
    assert unfrack_path(pathsep=False)('/etc/ansible') == '/etc/ansible'
    assert unfrack_path(pathsep=False)('-') == '-'


# Generated at 2022-06-12 20:14:37.574087
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("/my/path") == unfrackpath("/my/path")
    assert unfrack_path(pathsep=True)("/my/path:/your/path") == [unfrackpath("/my/path"), unfrackpath("/your/path")]


# Generated at 2022-06-12 20:14:45.674067
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    class Action:
        def __init__(self, help, option_strings):
            self.help = help
            self.option_strings = option_strings
        def __str__(self):
            return self.option_strings[0]
    actions = [Action('A help', ['-a']),
               Action('B help', ['-b']),
               Action('C help', ['--cc']),
               Action('D help', ['--dd']),
               Action('E help', ['-e', '--ee'])]
    shf = SortingHelpFormatter()
    # Make sure the method returns None for class compatibility
    assert shf.add_arguments(actions) is None
    # Copy class private attribute _add_item so we can call this
    # method with no argument on the private attribute.
    _add_item = sh

# Generated at 2022-06-12 20:14:52.811135
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # verify that the inner function works
    inner = maybe_unfrack_path('_')
    assert inner('_~/foo') == '_' + unfrackpath('~/foo')
    assert inner('_/foo') == '_' + unfrackpath('/foo')
    # test function returns function
    outer = maybe_unfrack_path('_')
    assert outer('_/foo') == '_' + unfrackpath('/foo')
    assert outer('__/foo') == '__/foo'



# Generated at 2022-06-12 20:15:02.201146
# Unit test for function unfrack_path
def test_unfrack_path():
    import os
    import tempfile
    import unittest
    from ansible.utils.path import unfrackpath

    class TestUnfrackPath(unittest.TestCase):

        def test_unfrack_path(self):
            """Test the unfrack_path() function"""
            curdir = os.path.abspath(os.path.dirname('.'))
            j2file = tempfile.NamedTemporaryFile()
            ldir = j2file.name

            # Test simple path
            self.assertEqual(unfrackpath(curdir), curdir)

            # Test relative path
            self.assertEqual(unfrackpath("playbooks/"), os.path.abspath("playbooks"))

            # Test homedirectory path expansion

# Generated at 2022-06-12 20:15:03.831175
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # test to determine if maybe_unfrack_path works
    assert maybe_unfrack_path(maybe_unfrack_path('@test_beacon:'))



# Generated at 2022-06-12 20:15:07.920590
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    options = parser.parse_args(['--vault-id', 'vaultid1234', '--vault-id', 'vaultid4321',
                                 '--ask-vault-password', '--vault-password-file', 'passwdfile'])
    assert options.vault_ids == ['vaultid1234', 'vaultid4321']
    assert options.ask_vault_pass is True
    assert options.vault_password_files == ['passwdfile']



# Generated at 2022-06-12 20:15:17.730931
# Unit test for function add_vault_options
def test_add_vault_options():
    my_parser = argparse.ArgumentParser()
    add_vault_options(my_parser)
    # Now verify if some simple options were set properly
    # TODO: add more advanced testing, i.e. check if optional arguments were added correctly and if they work as expected
    assert my_parser.description == 'None'
    assert my_parser.prog == 'ansible'
    assert my_parser._option_string_actions['--ask-vault-password']
    assert my_parser._option_string_actions['--vault-password-file']
    assert my_parser._mutually_exclusive_groups[0]


# Generated at 2022-06-12 20:15:35.342792
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter, description="Test description")
    parser.add_argument('-o', '--output', type=str, help='Output filename')
    parser.add_argument('-n', '--name', type=str, help='Name of template')
    parser.add_argument('-t', '--template', type=str, help='Template filename')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

# Generated at 2022-06-12 20:15:44.869896
# Unit test for function unfrack_path

# Generated at 2022-06-12 20:15:50.162648
# Unit test for function version
def test_version():
    assert version('Ansible') == 'Ansible [core 2.9.10]\n  config file = (not set)\n  configured module search path = Default w/o overrides\n  ansible python module location = (not set)\n  ansible collection location = (not set)\n  executable location = (not set)\n  python version = (not set)\n  jinja version = (not set)\n  libyaml = (not set)'

# Generated at 2022-06-12 20:15:53.705190
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)

    parser.add_argument('-a')
    parser.add_argument('-c')
    parser.add_argument('-b')

    assert '[-a] [-b] [-c]' == parser.format_usage()


# Generated at 2022-06-12 20:16:01.666563
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/')('/tmp/foo') == '/tmp/foo'
    assert maybe_unfrack_path('/')('~/foo') == '~/foo'
    assert maybe_unfrack_path('~/')('~/foo') == '~/tmp/foo'
    assert maybe_unfrack_path('~/')('/tmp/foo') == '/tmp/foo'
    assert maybe_unfrack_path('')('~/foo') == '~/foo'
    assert maybe_unfrack_path('')('/tmp/foo') == '/tmp/foo'



# Generated at 2022-06-12 20:16:08.367492
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/home/username/path/to/something') == '/home/username/path/to/something'
    assert unfrack_path()('-') == '-'
    assert unfrack_path(pathsep=True)('/home/username/path/to/something:/home/username/another/path:/home/other_username/path') == ['/home/username/path/to/something', '/home/username/another/path', '/home/other_username/path']


# Generated at 2022-06-12 20:16:17.612758
# Unit test for function unfrack_path
def test_unfrack_path():
    # Make sure the path separator is correct for the OS
    sep = os.pathsep
    # Execute the unfrack_path function with True (for path separator) and store in a variable
    test_unfrack_path_function = unfrack_path(True)
    # Define the test string
    test_string = sep.join(['string1' + sep, 'string2' + sep, 'string3'])
    # Run the test string through the unfrack_path function
    result = test_unfrack_path_function(test_string)
    # Assert that the resulting list is not empty
    assert result
    # Assert that the resultant list is of length 3
    assert len(result) == 3
    # Assert the the list returned is equal to the expected list

# Generated at 2022-06-12 20:16:22.015305
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    p = '/does/not/exist'
    assert maybe_unfrack_path('@')('@%s' % p) == '@%s' % unfrackpath(p)
    assert maybe_unfrack_path('@')('@%s' % os.path.abspath(p)) == '@%s' % unfrackpath(p)
    assert maybe_unfrack_path('@')('%s' % p) == p
    assert maybe_unfrack_path('@')('%s' % os.path.abspath(p)) == os.path.abspath(p)
# end of unit test for function maybe_unfrack_path



# Generated at 2022-06-12 20:16:25.755554
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@@')('@@/some/path') == '@@' + unfrackpath('/some/path')
    assert maybe_unfrack_path('@@')('@/some/path') == '@/some/path'


# Generated at 2022-06-12 20:16:28.224319
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    result = maybe_unfrack_path("@")("@/test/path")
    assert result == "@/test/path"


# Generated at 2022-06-12 20:16:43.046969
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/tmp/ansible_test') == '@/tmp/ansible_test'
    assert maybe_unfrack_path('@')('@') == '@'
    assert maybe_unfrack_path('@')('/tmp/ansible_test') == '/tmp/ansible_test'



# Generated at 2022-06-12 20:16:48.751108
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/new_path') == '@' + os.path.abspath('/new_path')
    assert maybe_unfrack_path('@')('old_path') == 'old_path'
    assert maybe_unfrack_path('@')('@/old_path') == '@/old_path'
    assert maybe_unfrack_path('@')('@@/old_path') == '@@/old_path'
    assert maybe_unfrack_path('@')('@@@/old_path') == '@@@/old_path'



# Generated at 2022-06-12 20:16:51.778803
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/tmp/foo') == '@' + unfrackpath('/tmp/foo')
    assert maybe_unfrack_path('@')('/tmp/foo') == '/tmp/foo'



# Generated at 2022-06-12 20:16:55.874950
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/foo') == '/foo'
    assert unfrack_path(pathsep=True)('/foo') == ['/foo']
    assert unfrack_path(pathsep=True)('/foo:/bar') == ['/foo', '/bar']
    assert unfrack_path()('-') == '-'
    assert unfrack_path(pathsep=True)('-') == ['-']


# Generated at 2022-06-12 20:16:57.366417
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/tmp/foo') == unfrack_path()('/tmp/foo/') == '/tmp/foo'



# Generated at 2022-06-12 20:17:07.103000
# Unit test for function unfrack_path
def test_unfrack_path():
    # Test with pathsep=True
    assert unfrack_path(pathsep=True)('/foo/bar:/baz') == ['/foo/bar', '/baz']
    assert unfrack_path(pathsep=True)(None) == []
    assert unfrack_path(pathsep=True)('') == []
    assert unfrack_path(pathsep=True)('/foo/bar::/baz') == ['/foo/bar', '', '/baz']
    assert unfrack_path(pathsep=True)(':') == ['']
    assert unfrack_path(pathsep=True)('::') == ['', '']
    assert unfrack_path(pathsep=True)(':::') == ['', '', '']

    # Test with pathsep=False

# Generated at 2022-06-12 20:17:13.635442
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_paths = [
        '/galaxy/roles/test.role', '/usr/my_roles/test.role', '/usr/share/ansible', './my_roles/test.role',
        '~/.ansible/roles/test.role', '../test.role', '0', 'test.role', './test.role', 'roles/test.role'
    ]
    prepend = '@'

# Generated at 2022-06-12 20:17:23.720927
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(beacon=os.path.sep)("/usr/bin/env") == "/usr/bin/env"
    assert maybe_unfrack_path(beacon=os.path.sep)("/home/someuser/.ansible/tmp/ansible-tmp-1522737651.84-248001088339055/.ansible/tmp/ansible-tmp-1522737651.85-13649704978670/user_debug") == "/home/someuser/.ansible/tmp/ansible-tmp-1522737651.84-248001088339055/.ansible/tmp/ansible-tmp-1522737651.85-13649704978670/user_debug"

# Generated at 2022-06-12 20:17:26.919249
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    path = '/Users/ansible/foo'
    new_path = '/Users/ansible/foo'
    assert maybe_unfrack_path('/')(path) == new_path



# Generated at 2022-06-12 20:17:33.713404
# Unit test for function version
def test_version():
    version_string = version("ansible-vault")

    # check if ansible_vault string is present in version_string
    assert("ansible-vault" in version_string)
    # check if libyaml flag is present in version_string
    assert("  libyaml =" in version_string)
    # check if ansible core version is present in version_string
    assert("[core {}".format(__version__) in version_string)

#
# Option Parsers of all commands
#
# Test command parser


# Generated at 2022-06-12 20:18:00.241434
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():

    maybe_unfrack_path_ = maybe_unfrack_path('@')

    assert maybe_unfrack_path_('@/test/test') == '@' + unfrackpath('/test/test')
    assert maybe_unfrack_path_('/test/test') == '/test/test'



# Generated at 2022-06-12 20:18:04.854203
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$/path') == '$/path'
    assert maybe_unfrack_path('$')('$/path') == '$/path'
    assert maybe_unfrack_path('$')('$/path') == '$/path'
    assert maybe_unfrack_path('/')('./path') == './path'



# Generated at 2022-06-12 20:18:09.317847
# Unit test for function unfrack_path
def test_unfrack_path():
    assert None == unfrack_path()(None)
    assert '~/ansible' == unfrack_path()('~/ansible')
    assert 'ANSIBLE_LIBRARY' == unfrack_path()('ANSIBLE_LIBRARY')
    assert '~/ansible:ANSIBLE_LIBRARY' == unfrack_path(pathsep=True)('~/ansible:ANSIBLE_LIBRARY')
    assert 'ANSIBLE_LIBRARY:~/ansible' == unfrack_path(pathsep=True)('ANSIBLE_LIBRARY:~/ansible')



# Generated at 2022-06-12 20:18:17.640086
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--foo')
    parser.add_argument('--baz')
    parser.add_argument('--bar')
    assert parser.format_help() == '''\
usage: [-h] [--bar BAR] [--baz BAZ] [--foo FOO]

optional arguments:
  -h, --help  show this help message and exit
  --bar BAR  
  --baz BAZ  
  --foo FOO
'''



# Generated at 2022-06-12 20:18:22.695099
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(
        formatter_class=SortingHelpFormatter)
    parser.add_argument("-f", action="store",
                        help="test 'f' option")
    parser.add_argument("-g", action="store",
                        help="test 'g' option")
    parser.add_argument("-a", action="store",
                        help="test 'a' option")
    parser.parse_args([])



# Generated at 2022-06-12 20:18:32.808468
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    from io import StringIO

    class TestOptionParser(argparse.ArgumentParser):
        def __init__(self, *args, **kwargs):
            super(TestOptionParser, self).__init__(*args, **kwargs)
            for i in "abcd":
                self.add_argument("-" + i, "--" + i * 2)

    stream = StringIO()
    parser = TestOptionParser(formatter_class=SortingHelpFormatter, add_help=False)
    parser.print_help(stream=stream)

    help_output = stream.getvalue()
    stream.close()

    # Expect the help output to be sorted according to the --xxx
    expected_output = """\
-a, --aa
-b, --bb
-c, --cc
-d, --dd
"""

    assert help

# Generated at 2022-06-12 20:18:39.181813
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    testcases = {
        '/foo/bar': ['/foo/bar', '/foo/bar'],
        '~/foo/bar': ['~/foo/bar', '~/foo/bar'],
        '$FOO/bar': ['$FOO/bar', '/baz/bar'],
        '$FOO': ['$FOO', '/baz'],
    }

    tests = {k: maybe_unfrack_path('$')(v) for k, v in testcases.items()}

    for test, actual in tests.items():
        assert actual == test, 'Failed on input: %s. Expected: %s. Actual: %s.' % (testcases[test], test, actual)


# Generated at 2022-06-12 20:18:44.957186
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@foo') == '@' + unfrackpath('foo')
    assert maybe_unfrack_path('@')('foo') == 'foo'
    assert maybe_unfrack_path('/')('/foo') == '/' + unfrackpath('foo')
    assert maybe_unfrack_path('/')('foo') == 'foo'
    assert maybe_unfrack_path('/')('foo') == 'foo'



# Generated at 2022-06-12 20:18:48.644551
# Unit test for function version
def test_version():
    """
    This function tests the version function.
    """
    failure = True
    val = version()
    # Check that the output string is in the format <version> () last updated <date> (GMT <offset>). For the test to pass,
    # the string 'last updated' must be present.
    if val.find('last updated') >= 0:
        failure = False
    return failure


# Generated at 2022-06-12 20:18:49.100921
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    pass



# Generated at 2022-06-12 20:19:29.030608
# Unit test for function unfrack_path
def test_unfrack_path():
    from ansible.utils.path import unfrackpath
    from ansible.parsing.plugin_option_callback import unfrack_path
    # Check if current work is using Windows paths
    if os.name == 'nt':
        # Test normal path
        result = unfrack_path(value='ansible')
        assert result == 'ansible'

        # Test path with drive letter
        result = unfrack_path(value='C:/Path/To/Ansible')
        assert result == 'C:/Path/To/Ansible'

        # Test path with drive letter and slash
        result = unfrack_path(value='C:\\Path\\To\\Ansible')
        assert result == 'C:/Path/To/Ansible'

        # Test path with drive letter and multiple slashes

# Generated at 2022-06-12 20:19:35.117316
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # convenience function: create argument parser
    def init_parser(*args, **kwargs):
        parser = argparse.ArgumentParser(*args, **kwargs)
        parser.add_argument('-b', action='help')
        parser.add_argument('-a', action='help')
        return parser

    # no formatting options, default help should be in upper case
    parser = init_parser()
    assert '-A' in parser.format_help()
    assert '-B' in parser.format_help()

    # formatter with preset help order
    formatter = SortingHelpFormatter(help_order=('a', 'b'))
    parser = init_parser(formatter_class=formatter)
    assert '-A' not in parser.format_help()
    assert '-B' not in parser.format_help()

# Generated at 2022-06-12 20:19:41.432136
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("@")("@tests") == '@' + unfrackpath("tests")
    assert maybe_unfrack_path("@")("@") == '@'
    assert maybe_unfrack_path("@")("something") == 'something'

# Function unfrack_path should be deprecated
# Function maybe_unfrack_path should be used in its place
unfrack_path = maybe_unfrack_path("@")



# Generated at 2022-06-12 20:19:49.246193
# Unit test for function unfrack_path
def test_unfrack_path():
    path = 'foo/bar'
    opt = unfrackpath(path)
    assert opt == os.path.abspath(os.path.expanduser(path))
    path = '~/foo/bar'
    opt = unfrackpath(path)
    assert opt == os.path.abspath(os.path.expanduser(path))
    path = '~/foo/bar,foo/bar'
    opt = unfrack_path(pathsep=True)(path)
    assert opt == [os.path.abspath(os.path.expanduser('~/foo/bar')), os.path.abspath(os.path.expanduser('foo/bar'))]
    path = '~/foo/bar,foo/bar'

# Generated at 2022-06-12 20:19:55.937723
# Unit test for function unfrack_path
def test_unfrack_path():
    local_path = os.path.expanduser("~/ansible")
    unfrack_local_path = unfrack_path()(local_path)
    assert unfrack_local_path == local_path
    assert unfrack_path(pathsep=True)(os.pathsep.join([local_path, 'no_exist_path'])) == [local_path]
    assert unfrack_path(pathsep=True)(local_path) == [local_path]
    assert unfrack_path()('-') == '-'



# Generated at 2022-06-12 20:20:04.272568
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Set home to /tmp
    if 'HOME' in os.environ:
        del os.environ['HOME']
    os.environ['HOME'] = '/tmp'

    on_posix = 'posix' in sys.builtin_module_names

    # Test single path
    # Test with home
    assert '~/test_file' == maybe_unfrack_path('~')('~/test_file')
    # Test with absolute path
    assert '/tmp/test_file' == maybe_unfrack_path('~')('/tmp/test_file')

    # Test list of paths
    test_list = ['~/test_file', '/tmp/file1', '/tmp/file2']
    # Test with home
    assert ['~/test_file', '/tmp/file1', '/tmp/file2']

# Generated at 2022-06-12 20:20:05.494683
# Unit test for function version
def test_version():
    assert version()
    assert version('ansible')

#
# Options Common to Multiple Ansible Tools
#



# Generated at 2022-06-12 20:20:13.970076
# Unit test for function unfrack_path
def test_unfrack_path():
    print(unfrack_path()("./path1"))
    print(unfrack_path()("/path1"))
    print(unfrack_path()("path1"))
    print(unfrack_path()("./path1/test_file.yml"))
    print(unfrack_path()("/path1/test_file.yml"))
    print(unfrack_path()("path1/test_file.yml"))
    print(unfrack_path()("./path1/../sub-path/../sub-sub-path/test_file.yml"))
    print(unfrack_path()("/path1/sub-path/sub-sub-path/test_file.yml"))

# Generated at 2022-06-12 20:20:19.744555
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    """
    Test if object of class 'PrependListAction' is created
    and if created object is of 'PrependListAction'
    """
    assert (type(PrependListAction(["-a", "--append"], "dest", nargs=0, const=False, default=None, type=None,
                 choices=None, required=False, help=None, metavar=None)) == PrependListAction)



# Generated at 2022-06-12 20:20:23.757072
# Unit test for function unfrack_path
def test_unfrack_path():
    def ufp(val): return unfrack_path(pathsep=False)(val)
    def ufps(val): return unfrack_path(pathsep=True)(val)
    assert ufp('/tmp') == '/tmp'
    assert ufps('/tmp') == ['/tmp']
    assert ufps('/tmp:/tmp') == ['/tmp', '/tmp']
    assert ufps('/tmp:') == ['/tmp', '']
    assert ufps('/tmp:/tmp/abc') == ['/tmp', '/tmp/abc']



# Generated at 2022-06-12 20:21:32.611142
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test if value is fracked and starts with beacon
    assert maybe_unfrack_path('@')('@./foo/bar') == '@./foo/bar'
    # Test if value is fracked and does not start with beacon
    assert maybe_unfrack_path('@')('~/foo/bar') == '~/foo/bar'
    # Test if value is not fracked and starts with beacon
    assert maybe_unfrack_path('@')('@/foo/bar') == '@/foo/bar'
    # Test if value is not fracked and does not not start with beacon
    assert maybe_unfrack_path('@')('/foo/bar') == '/foo/bar'


#
# Misc. helpers
#
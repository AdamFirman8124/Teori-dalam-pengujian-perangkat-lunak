

# Generated at 2022-06-12 20:12:08.925874
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    beacon = '@/'
    path = '@/foo/bar'

    assert maybe_unfrack_path(beacon)(path) == path
    assert maybe_unfrack_path(beacon)('@/') == '@/'
    assert maybe_unfrack_path(beacon)('@/ ') == '@/'
    assert maybe_unfrack_path(beacon)('@/foo/bar') == path
    assert maybe_unfrack_path(beacon)('@/foo/bar/') == path
    assert maybe_unfrack_path(beacon)('bar') == 'bar'
    assert maybe_unfrack_path(beacon)('/bar') == '/bar'
    assert maybe_unfrack_path(beacon)('@/bar') == path
    assert maybe_un

# Generated at 2022-06-12 20:12:14.886023
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    parser = argparse.ArgumentParser()
    add_runas_prompt_options(parser)
    parser.parse_args('-K --become-pass-file sample_password_file'.split())
    # test exception
    with pytest.raises(SystemExit):
        parser.parse_args('-K -K --become-pass-file sample_password_file'.split())



# Generated at 2022-06-12 20:12:18.142689
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(
        prog='test_add_connect_options',
        formatter_class=SortingHelpFormatter,
        description='test_add_connect_options',
    )
    add_connect_options(parser)
    parser.print_help()
    return parser



# Generated at 2022-06-12 20:12:29.072638
# Unit test for function version
def test_version():
    """Unit test for version"""
    import ansible.constants as C
    C.DEFAULT_MODULE_PATH = None
    C.COLLECTIONS_PATHS = ['/opt/ansible/collections']

# Generated at 2022-06-12 20:12:38.984578
# Unit test for function maybe_unfrack_path

# Generated at 2022-06-12 20:12:47.892919
# Unit test for function add_meta_options
def test_add_meta_options():
    opts = ['-F']

    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args(opts)
    assert args.force_handlers == True

    opts = ['-F', '--flush-cache']
    args = parser.parse_args(opts)
    assert args.force_handlers == True
    assert args.flush_cache == True

    opts = ['--flush-cache']
    args = parser.parse_args(opts)
    assert args.flush_cache == True



# Generated at 2022-06-12 20:12:56.813835
# Unit test for function add_connect_options
def test_add_connect_options():
    from ansible.cli.arguments import option_helpers as coh

    parser = argparse.ArgumentParser()
    coh.add_connect_options(parser)
    options = parser.parse_args([])

    assert options.timeout == C.DEFAULT_TIMEOUT
    assert options.remote_user == C.DEFAULT_REMOTE_USER
    assert options.connection == C.DEFAULT_TRANSPORT
    assert options.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert options.ask_pass == C.DEFAULT_ASK_PASS
    assert options.ssh_common_args is None
    assert options.sftp_extra_args is None
    assert options.scp_extra_args is None
    assert options.ssh_extra_args is None



# Generated at 2022-06-12 20:13:04.280628
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = argparse.ArgumentParser()
    add_runas_options(parser)
    assert parser.parse_args(["-b"]).become == True
    assert parser.parse_args(["--become"]).become == True
    assert parser.parse_args(["--become-method", "sudo"]).become_method == "sudo"
    assert parser.parse_args(["--become-user", "root"]).become_user == "root"
    assert parser.parse_args(["--ask-become-pass"]).become_ask_pass == True



# Generated at 2022-06-12 20:13:08.929683
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser()
    add_async_options(parser)
    assert parser.parse_args([]).poll_interval == C.DEFAULT_POLL_INTERVAL
    assert parser.parse_args([]).seconds == 0
    assert parser.parse_args(['-P', '1000']).poll_interval == 1000
    assert parser.parse_args(['-P', '1000']).seconds == 0
    assert parser.parse_args(['-B', '1000']).poll_interval == C.DEFAULT_POLL_INTERVAL
    assert parser.parse_args(['-B', '1000']).seconds == 1000



# Generated at 2022-06-12 20:13:20.695300
# Unit test for function add_vault_options
def test_add_vault_options():
    result = []
    _mock_stdout = StringIO()
    with mock.patch('sys.stdout', _mock_stdout):
        parser = argparse.ArgumentParser()
        add_vault_options(parser)
        for arg in vault_opts_to_test:
            parser.parse_args(arg.split())
            result.append(re.sub(r"\s+", " ", _mock_stdout.getvalue().rstrip()))
            _mock_stdout.truncate(0)
            _mock_stdout.seek(0)
        assert result == vault_opts_to_test_output


#
# Functions to generate output
#


# Generated at 2022-06-12 20:13:36.377128
# Unit test for function version
def test_version():
    assert "ansible-doc [core 2.0.0.0]" in version(prog="ansible-doc")
    assert "/usr/bin" in version()

# Generated at 2022-06-12 20:13:44.108541
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    mup = maybe_unfrack_path('&')
    assert mup('&path/to/file') == '&' + unfrackpath('path/to/file')
    assert mup('&path/to/file2') == '&' + unfrackpath('path/to/file2')
    assert mup('&/path/to/file') == '&' + unfrackpath('/path/to/file')
    assert mup('&../path/to/file') == '&' + unfrackpath('../path/to/file')
    assert mup('&../path/to/file2') == '&../path/to/file2'
test_maybe_unfrack_path()



# Generated at 2022-06-12 20:13:51.899807
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert(maybe_unfrack_path("@")("@somedir") == "@somedir")
    assert(maybe_unfrack_path("@")("@/somedir") == "@/somedir")
    assert(maybe_unfrack_path("@")("@../somedir") == "@../somedir")
    assert(maybe_unfrack_path("@")("@../../somedir") == "@../../somedir")
    assert(maybe_unfrack_path("@")("@@../somedir") == "@@../somedir")



# Generated at 2022-06-12 20:13:55.417122
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/var/lib') == '/var/lib'
    assert unfrack_path(pathsep=True)('/var/lib:/var/tmp') == ['/var/lib', '/var/tmp']



# Generated at 2022-06-12 20:14:02.137919
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser(prog="Test", description="A test suite for argparse",

                                     epilog="validate argparse output for -o and -t",

                                     formatter_class=SortingHelpFormatter)

    add_output_options(parser)

    opts = parser.parse_args()

    assert not opts.one_line, "Invalid Output "

    assert opts.tree == None, "Invalid Output"



# Generated at 2022-06-12 20:14:06.152251
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$/test') == '$/test'
    assert maybe_unfrack_path('$')('$test') == '$test'
    assert maybe_unfrack_path('$')('%test') == '%test'


# Generated at 2022-06-12 20:14:10.970196
# Unit test for function unfrack_path
def test_unfrack_path():
    with open("/tmp/test_abs_path.txt","w") as f:
        f.write("test")

    assert unfrack_path(False)("/tmp/test_abs_path.txt") == "/tmp/test_abs_path.txt"
    assert unfrack_path(True)("/tmp/test_abs_path.txt") == ["/tmp/test_abs_path.txt"]



# Generated at 2022-06-12 20:14:23.019787
# Unit test for function unfrack_path
def test_unfrack_path():
    def do_test(path, expected):
        print("Testing [%s] => [%s]" % (path, expected))
        assert unfrack_path(True)(path) == expected

    do_test('~/file', [os.path.expanduser('~/file')])
    do_test('/tmp/hosts', ['/tmp/hosts'])
    do_test('~/hosts:/tmp/hosts', [os.path.expanduser('~/hosts'), '/tmp/hosts'])
    do_test('  ~/hosts   :   /tmp/hosts   ', [os.path.expanduser('~/hosts'), '/tmp/hosts'])

# Generated at 2022-06-12 20:14:29.453348
# Unit test for function unfrack_path
def test_unfrack_path():
    data = ['#1','~2','#$','~','','/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/','~/']

# Generated at 2022-06-12 20:14:34.041894
# Unit test for function add_output_options
def test_add_output_options():
    parser = create_base_parser()
    add_output_options(parser)
    args = parser.parse_args(['-o'])
    assert args.one_line is True
    args = parser.parse_args(['--one-line'])
    assert args.one_line is True
    args = parser.parse_args(['-t'])
    assert args.tree is None
    args = parser.parse_args(['--tree', '/tmp/something'])
    assert args.tree == '/tmp/something'
    args = parser.parse_args(['-t', '/tmp/something'])
    assert args.tree == '/tmp/something'



# Generated at 2022-06-12 20:14:46.965850
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion)
    args = parser.parse_args(['--version'])



# Generated at 2022-06-12 20:14:53.376188
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("/tmp") == "/tmp"
    assert unfrack_path()("/tmp:{{playbook_dir}}") == "/tmp:{{playbook_dir}}"
    assert unfrack_path(True)("/tmp") == ['/tmp']
    assert unfrack_path(True)("/tmp:{{inventory_dir}}") == ['/tmp', '{{inventory_dir}}']
    assert unfrack_path()("-") == "-"


# Generated at 2022-06-12 20:15:02.559298
# Unit test for function version
def test_version():
    expected_output = [
        '{0} [core {1}]  config file = {2}  configured module search path = {3}  ansible python module location = {4}  ansible collection location = {5}  executable location = {6}  python version = {7}  jinja2 version = {8}  libyaml = {9}'.format(
            sys.argv[0], __version__, C.CONFIG_FILE, C.DEFAULT_MODULE_PATH, ':'.join(ansible.__path__), ':'.join(C.COLLECTIONS_PATHS), sys.argv[0], ''.join(sys.version.splitlines()), j2_version, HAS_LIBYAML),
        '',
    ]
    assert version().splitlines() == expected_output

# Generated at 2022-06-12 20:15:03.713948
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    print('')
    AnsibleVersion(['-v'])



# Generated at 2022-06-12 20:15:07.174066
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion)
    args = parser.parse_args(['--version'])
    assert args == args_AnsibleVersion



# Generated at 2022-06-12 20:15:18.205656
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrackpath("foo") == "foo"
    assert unfrackpath("~/foo") == os.path.expanduser("~/foo")
    assert unfrackpath("~/foo") != "~/foo"
    assert unfrackpath("/some/path/to/my_roles") == "/some/path/to/my_roles"
    assert unfrackpath("/some/path/to/my_roles") == os.path.realpath("/some/path/to/my_roles")
    assert unfrackpath("roles/foo") == "roles/foo"
    assert unfrackpath("foo:bar:tar") == "foo:bar:tar"



# Generated at 2022-06-12 20:15:20.588746
# Unit test for function version
def test_version():
    assert version()



# Generated at 2022-06-12 20:15:30.719422
# Unit test for function version
def test_version():
    class argv(object):
        def __init__(self, arg):
            self.argv = arg

        def __enter__(self):
            self.orig = sys.argv
            sys.argv = self.argv

        def __exit__(self, type, value, traceback):
            sys.argv = self.orig

    test_prog = 'ansible-test'
    test_version = "2.7.0_1"
    test_git_info = "git branch commit_hash"
    with argv([test_prog]):
        assert test_version in version()
    with argv([test_prog, '--version']):
        assert "config file = " in version()

# Generated at 2022-06-12 20:15:39.178364
# Unit test for function add_module_options
def test_add_module_options():
    parser = argparse.ArgumentParser()
    add_module_options(parser)
    
    with patch.dict(C.config.DEFAULTS, {'DEFAULT_MODULE_PATH': '/usr/local/lib/libmodule.so'}):
        result = parser.parse_args('-M /usr/local/lib/libmodule.so'.split())
        assert result.module_path == [os.path.normpath('/usr/local/lib/libmodule.so')]
# Test if function add_module_options contains hard coded paths

# Generated at 2022-06-12 20:15:39.873065
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    pass


# Generated at 2022-06-12 20:15:50.833433
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("path") == unfrackpath("path")
    assert unfrack_path(True)("path1" + os.pathsep + "path2") == [unfrackpath("path1"), unfrackpath("path2")]
    assert unfrack_path()("-") == "-"


# Generated at 2022-06-12 20:15:55.644462
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@@test/path') == '@test/path'
    assert maybe_unfrack_path('@')('@/test/path') == '@/test/path'
    assert maybe_unfrack_path('@')('@~/test/path') == '@~/test/path'

#
# Helper functions to load Options from non-cmdline sources
#

# Generated at 2022-06-12 20:16:02.810396
# Unit test for function version
def test_version():
    """Unit test for version"""
    current_dir = os.path.dirname(os.path.dirname(unfrackpath(__file__)))
    installed_dir = os.path.dirname(current_dir)
    repo_dir = os.path.dirname(installed_dir)
    sys.path.append(installed_dir)

    ansible_module_path_backup = C.DEFAULT_MODULE_PATH
    C.DEFAULT_MODULE_PATH = None
    C.COLLECTIONS_PATHS = [os.path.join(current_dir, 'collection_root')]
    sys.argv[0] = 'ansible-playbook'

    old_version_output = version()[14:]
    # Ensure that the output of version is the same as before
    assert version()[14:] == old

# Generated at 2022-06-12 20:16:06.309750
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # Setup
    parser = argparse.ArgumentParser()

    # Exercise
    ansible_version = AnsibleVersion()
    ansible_version(parser, None, None, None)

    # Verify
    # FIXME: Implement
    pass



# Generated at 2022-06-12 20:16:15.182953
# Unit test for function maybe_unfrack_path

# Generated at 2022-06-12 20:16:24.430250
# Unit test for function version
def test_version():
    from ansible.module_utils.common.version import Version
    from ansible import context
    import ansible
    from ansible import collection
    import os
    import sys

    config = context._init_global_context(cli_opts=dict(version=True))
    #reset the config, to avoid breakages
    ansible.constants.DEFAULT_MODULE_PATH = config._original_module_path
    ansible.constants.COLLECTIONS_PATHS = config._original_collections_paths
    ansible.constants.DEFAULT_PRIVATE_ROLE_PATH = config._original_role_path

    #add paths to the system path
    sys.path.append(ansible.constants.DEFAULT_MODULE_PATH)

# Generated at 2022-06-12 20:16:28.193567
# Unit test for function add_output_options
def test_add_output_options():
    parser=argparse.ArgumentParser()
    add_output_options(parser)
    parser.parse_args(["-o"])
    parser.parse_args(["-t", "/tmp/test_add_output_options/"])
    parser.parse_args([])
    with pytest.raises(SystemExit):
        parser.parse_args(["-o", "-t", "/tmp/test_add_output_options/"])
    with pytest.raises(SystemExit):
        parser.parse_args(["-t", "/tmp/test_add_output_options/", "-o"])



# Generated at 2022-06-12 20:16:30.296470
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    args = parser.parse_args()
    assert args.tags == C.TAGS_RUN
    assert args.skip_tags == C.TAGS_SKIP



# Generated at 2022-06-12 20:16:36.887016
# Unit test for function add_check_options
def test_add_check_options():
    parser = create_base_parser('test', desc='')
    add_check_options(parser)
    options = parser.parse_args(['-C', '-D', '--syntax-check'])
    assert options.check is True
    assert options.syntax is True
    assert options.diff is True



# Generated at 2022-06-12 20:16:41.366689
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')("@/usr/local") == "@" + unfrackpath('/usr/local')
    assert maybe_unfrack_path('@')("@nonexistent") == "@nonexistent"
    assert maybe_unfrack_path('@')("/usr/local") == "/usr/local"



# Generated at 2022-06-12 20:16:52.554863
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('frob')('frob/bar') == 'frob' + unfrackpath('/bar')
    assert maybe_unfrack_path('frob')('bar') == 'bar'


#
# Special options
#
# Options that one or more modules or plugins might be interested in.
# They are used in the CLI parser, but that's it.
#
# Looking to create a special option?
# 1. Add a new constant below,
# 2. Add a line to the option_list tuple with a comma at the end,
# 3. Add the option to the OptionParser.
#
# Special options are passed on a per-task basis in order for module parameters to have access
# to the raw cli argument values as well as the ParsedArgs object.
#
# If a special option's value is set

# Generated at 2022-06-12 20:16:56.823156
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_data = [
        # [ in_str,   out_str ]
        [ '@test',   '@test' ],
        [ 'test',    'test' ],
        [ '@/tmp',   '@' + unfrackpath('/tmp') ],
        [ '/tmp',    '/tmp' ],
    ]
    for data in test_data:
        assert maybe_unfrack_path('@')(data[0]) == data[1]



# Generated at 2022-06-12 20:16:57.368093
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    pass



# Generated at 2022-06-12 20:17:07.117150
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    test_parser = argparse.ArgumentParser()
    test_parser._action_groups.append(argparse.ActionContainer(description='description'))
    test_parser._action_groups[-1].add_argument('-c', '--ccc', action='store_true')
    test_parser._action_groups[-1].add_argument('-a', '--aaa', action='store_true')
    test_parser._action_groups[-1].add_argument('-b', '--bbb', action='store_true')

    test_parser.usage = argparse.SUPPRESS
    test_parser.formatter_class = SortingHelpFormatter
    test_parser.print_help()


# Generated at 2022-06-12 20:17:10.486643
# Unit test for function unfrack_path
def test_unfrack_path():
    # Path separator
    assert unfrack_path(True)('/path/to/file1:/path/to/file2') == ['/path/to/file1', '/path/to/file2']
    # Simple path
    assert unfrack_path()('/path/to/file') == '/path/to/file'
    # Special flag
    assert unfrack_path()('-') == '-'


# Generated at 2022-06-12 20:17:17.161405
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@test') == '@test'
    assert maybe_unfrack_path('@')('@%s' % os.sep) == '@%s' % os.sep
    assert maybe_unfrack_path('@')('@%s%s' % (os.sep, os.sep)) == '@%s%s' % (os.sep, os.sep)



# Generated at 2022-06-12 20:17:18.302986
# Unit test for function version
def test_version():
    assert(__version__ in version())

# Generated at 2022-06-12 20:17:23.088298
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_path = '/etc/ansible'
    beacon = '@'
    encoded_path = '@' + test_path
    assert maybe_unfrack_path(beacon)(encoded_path) == ('@' + unfrackpath(test_path))
    assert maybe_unfrack_path(beacon)(test_path) == test_path


# Generated at 2022-06-12 20:17:33.308330
# Unit test for function unfrack_path
def test_unfrack_path():
    # test simple path
    assert '/foo/bar' == unfrack_path()("/foo/bar")
    # test relative path
    assert 'foo/bar' == unfrack_path()("foo/bar")
    # test path list
    assert ['/foo/bar', '/baz/qux'] == unfrack_path(pathsep=True)("/foo/bar:/baz/qux")
    assert ['/foo/bar', '/baz/qux'] == unfrack_path(pathsep=True)("/foo/bar, /baz/qux")
    assert ['/foo/bar', '/baz/qux'] == unfrack_path(pathsep=True)("/foo/bar,/baz/qux")
    # test path to stdin

# Generated at 2022-06-12 20:17:38.074826
# Unit test for function unfrack_path
def test_unfrack_path():
    tester = unfrack_path()
    assert tester('/a/b/c') == unfrackpath('/a/b/c')
    assert tester('/a:/b:/c') == [unfrackpath('/a'), unfrackpath('/b'), unfrackpath('/c')]
    assert tester('-') == '-'



# Generated at 2022-06-12 20:17:54.978418
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    testcases = ['~/ansible_test', 'ANSIBLE_TEST_DIR~/.ansible_test', 'a~/ansible_test']
    expected_outputs = ['~/ansible_test', 'ANSIBLE_TEST_DIR~/.ansible_test', 'a~/ansible_test']

    for i in range(len(testcases)):
        output = maybe_unfrack_path('~')(testcases[i])
        assert output == expected_outputs[i]



# Generated at 2022-06-12 20:17:57.660829
# Unit test for function unfrack_path
def test_unfrack_path():
    opt_value = './my_value'
    assert unfrack_path()(opt_value) == './my_value'


# Generated at 2022-06-12 20:18:06.244873
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # this is a "hidden" option (starts with '_') and shouldn't be in the results
    test_parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter, add_help=False)
    test_parser.add_argument('_basic_action', action='store', help='basic action')

    test_parser.add_argument('--foo',
                             default='xyz',
                             action='store',
                             help='with default')

    test_parser.add_argument('--bar',
                             dest='bar',
                             type=int,
                             default=5,
                             action='store',
                             help='with type')


# Generated at 2022-06-12 20:18:07.676201
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    sys.argv = ['ansible', '--version']
    ARGS = ANSIBLE_PARSER.parse_args()
    assert ARGS.version == False
    assert ARGS.version == False


# Generated at 2022-06-12 20:18:15.066821
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_string = '~/www/html'
    test_string_with_beacon = '/~/www/html'
    result = maybe_unfrack_path('/')(test_string_with_beacon)
    assert result == '/' + unfrackpath(test_string)
    result = maybe_unfrack_path('/')(test_string)
    assert result == test_string



# Generated at 2022-06-12 20:18:16.842680
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    
    print(maybe_unfrack_path('$')('$adfaskljkl'))



# Generated at 2022-06-12 20:18:21.897407
# Unit test for function unfrack_path
def test_unfrack_path():
    assert 'test/path' == unfrack_path()('test/path')
    assert 'test/path' == unfrack_path()('./test/path')
    assert os.path.join(os.getcwd(), 'test/path') == unfrack_path()('./test/path')
    assert ['test/path', '/abs/path'] == unfrack_path(pathsep=True)('test/path:/abs/path')



# Generated at 2022-06-12 20:18:27.524256
# Unit test for function unfrack_path
def test_unfrack_path():
    # Make sure _unfrack_path() returns a string when passed a string.
    # unfrack_path(pathsep=True) returns a list of strings, so pathsep
    # must be False in this test
    assert isinstance(unfrack_path(pathsep=False)('roles'), str)



# Generated at 2022-06-12 20:18:28.803438
# Unit test for function version
def test_version():
    assert version().startswith(__version__)



# Generated at 2022-06-12 20:18:31.876222
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
  parser = argparse.ArgumentParser()
  parser.add_argument('--version', action=AnsibleVersion, nargs=0)
  dummy='''
    This is a dummy script for test function __call__ of class AnsibleVersion.
  '''
  args = parser.parse_args()


# Generated at 2022-06-12 20:19:49.866399
# Unit test for function unfrack_path
def test_unfrack_path():
    test_in = [
        "/etc/ansible/ansible.cfg",
        os.path.expanduser("~/.ansible.cfg"),
        "./ansible.cfg",
        "ansible.cfg",
        "~/ansible.cfg",
        "/etc/../etc/ansible/ansible.cfg",
        "__file__",
        "ansible.cfg:roles/role1/vars/main.yml:roles/role2/tasks/main.yml"
        "ansible.cfg:roles/role1/vars/main.yml,roles/role2/tasks/main.yml"
    ]

# Generated at 2022-06-12 20:19:57.313041
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # Setup Test - Create objects
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-x')
    parser.add_argument('-y')
    parser.add_argument('-w')
    # Perform Test - Capture output of help function
    original_out = sys.stdout  # 2.6 fails to capture stdout without this
    try:
        sys.stdout = to = open(os.devnull, 'w')
        parser.print_help()
    finally:
        sys.stdout = original_out
        to.close()



# Generated at 2022-06-12 20:20:01.216852
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    call_maybe_unfrack_path = maybe_unfrack_path('@')
    assert call_maybe_unfrack_path('@/tmp/test') == '@/tmp/test'
    assert call_maybe_unfrack_path('@test/tmp/test') == '@test/tmp/test'



# Generated at 2022-06-12 20:20:08.035862
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    try:
        # Specify a full path
        path = os.path.join(os.environ['VIRTUAL_ENV'], "some_repo")
        assert path == maybe_unfrack_path('@')('@' + path)
        assert path == maybe_unfrack_path('@')(path)
    except KeyError:
        assert True
    # Specify a relative path
    assert './some_repo' == maybe_unfrack_path('@')('./some_repo')
    # Specify a relative path for the beacon (doesn't work)
    assert './some_repo' == maybe_unfrack_path('./')('./some_repo')

# Generated at 2022-06-12 20:20:14.475713
# Unit test for function unfrack_path
def test_unfrack_path():
    """Unit test for function unfrack_path"""
    # pylint: disable=missing-docstring
    abs_path = '/abs/path'
    rel_path = 'rel/path'
    current_dir_path = '.'
    relative_path_list = ['rel/path1', 'rel/path2']
    correct_list_of_paths = [os.path.join(os.getcwd(), path) for path in relative_path_list]
    import tempfile
    tempdir = tempfile.gettempdir()
    tempdir_path = os.path.join(tempdir, 'path')
    tempfile_path = os.path.join(tempdir, 'file')
    if not os.path.exists(tempfile_path):
        with open(tempfile_path, 'w'):
            pass

# Generated at 2022-06-12 20:20:22.085701
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('') is None
    assert unfrack_path(pathsep=True)('') == []
    assert unfrack_path(pathsep=True)('.') == ['./']
    assert unfrack_path(pathsep=True)('./') == ['./']
    assert unfrack_path(pathsep=True)('.:/usr/lib/python2.6/site-packages') == ['./', '/usr/lib/python2.6/site-packages']
    assert unfrack_path()('.') == './'
    assert unfrack_path()('./') == './'



# Generated at 2022-06-12 20:20:31.950732
# Unit test for function unfrack_path
def test_unfrack_path():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    for prefix in (None, 'ANSIBLE_', 'ANSIBLE_CONFIG', 'ANSIBLE_ROLES_PATH', 'ANSIBLE_LIBRARY', 'ANSIBLE_CALLBACK_PLUGINS', 'ANSIBLE_ACTION_PLUGINS', 'ANSIBLE_CACHE_PLUGIN', 'ANSIBLE_FILTER_PLUGINS', 'ANSIBLE_LOOKUP_PLUGINS', 'ANSIBLE_STDOUT_CALLBACK'):
        env_var = prefix + '_TEST' if prefix else 'TEST'
        test_str = 'one,two'
        test_path = '/one:/two'
        os.environ[env_var] = test_path

# Generated at 2022-06-12 20:20:36.692264
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    "Tests the function maybe_unfrack_path"
    unfracked_path = "/a/b/c"

    assert maybe_unfrack_path("/")(unfracked_path) == unfracked_path
    assert maybe_unfrack_path("/")("@" + unfracked_path) == "@" + unfracked_path

    assert maybe_unfrack_path("@")(unfracked_path) == unfracked_path
    assert maybe_unfrack_path("@")("@" + unfracked_path) == "@" + unfracked_path



# Generated at 2022-06-12 20:20:41.806270
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('XYZ')('XYZ' + os.path.sep + 'a' + os.path.sep + 'b') == 'XYZ' + os.path.sep + 'a' + os.path.sep + 'b'
    assert maybe_unfrack_path('XYZ')('XYZ' + os.path.sep + 'a' + os.path.sep + 'b' + os.path.sep) == 'XYZ' + os.path.sep + 'a' + os.path.sep + 'b'



# Generated at 2022-06-12 20:20:44.956394
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('/foo/bar') == '/foo/bar'
    assert unfrack_path(pathsep=True)('/foo/bar:/baz') == ['/foo/bar', '/baz']


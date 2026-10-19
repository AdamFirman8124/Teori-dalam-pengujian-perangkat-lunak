

# Generated at 2022-06-12 20:12:33.242508
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    args = parser.parse_args(['-C', '-D'])
    assert args.check == True
    assert args.diff == True
    assert args.syntax == False

# Generated at 2022-06-12 20:12:38.142067
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    class Args():
        prog = 'ansible-doc'
        ansible_version = None
    _args = Args()
    _action = AnsibleVersion(option_strings=['--version'], dest='ansible_version')
    _action.__call__(_parser, _args, values=None)
    assert _args.ansible_version == to_native(version(_args.prog))



# Generated at 2022-06-12 20:12:43.056541
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    parser = argparse.ArgumentParser()
    runas_group = parser.add_argument_group("Privilege Escalation Options", "control how and which user you become as on target hosts")
    add_runas_prompt_options(parser, runas_group)
    ns = parser.parse_args()
    assert ns.become_ask_pass is False
    assert ns.become_password_file is None



# Generated at 2022-06-12 20:12:47.194586
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser(prog='ansible')
    add_output_options(parser)
    with pytest.raises(SystemExit):
        parser.parse_args(['--one-line', '-t', 'test'])


# Generated at 2022-06-12 20:12:56.992059
# Unit test for method add_arguments of class SortingHelpFormatter
def test_SortingHelpFormatter_add_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", action="store_true")
    parser.add_argument("-b", action="store_true")
    parser.add_argument("-c", action="store_true")
    assert parser.format_help() == 'usage: [-h] [-a] [-b] [-c]\n\noptional arguments:\n  -h, --help  show this help message and exit\n  -a\n  -b\n  -c\n'
    parser = argparse.ArgumentParser()
    parser.formatter_class = SortingHelpFormatter
    parser.add_argument("-a", action="store_true")
    parser.add_argument("-b", action="store_true")

# Generated at 2022-06-12 20:13:06.193216
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    from ansible.utils.display import Display
    display = Display()
    from ansible.cli.arguments import optparse_helpers
    optparse_helpers._ = lambda s: s
    parser = argparse.ArgumentParser(description='No description for this program.')
    parser.add_argument('--has-old-value', action=PrependListAction, type=str, default=['old-value'], help='description of --has-old-value')
    parser.add_argument('--no-old-value', action=PrependListAction, type=str, default=[], help='description of --no-old-value')
    parser.parse_args(['--has-old-value', 'new', '--has-old-value', 'newer', '--no-old-value', 'new'])

# Generated at 2022-06-12 20:13:08.661615
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser(
        prog='test',
        formatter_class=SortingHelpFormatter,
        conflict_handler='resolve',
    )
    add_async_options(parser)
    args = parser.parse_args(['-P', '5', '-B', '30'])
    assert args.poll_interval == 5
    assert args.seconds == 30

# Generated at 2022-06-12 20:13:14.991348
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    p1 = maybe_unfrack_path('@libexecdir')
    p2 = maybe_unfrack_path('@rundir')
    assert p1('@libexecdir') == '@libexecdir'
    assert p1('@libexecdir@') == '@libexecdir@'
    assert p2('@rundir@') == '@rundir@'
    assert p1('@libexecdir/test') == '@libexecdir/test'
    assert p2('@rundir/test') == '@rundir/test'


# Generated at 2022-06-12 20:13:25.145478
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():

    parser = argparse.ArgumentParser(prog='Test',
                                     formatter_class=SortingHelpFormatter,
                                     conflict_handler='resolve',
                                     )

    add_runas_prompt_options(parser)
    argv = []

    args = parser.parse_args(argv)
    assert args.become_ask_pass == C.DEFAULT_BECOME_ASK_PASS
    assert args.become_password_file == C.BECOME_PASSWORD_FILE

    argv = ['--ask-become-pass']
    args = parser.parse_args(argv)
    assert args.become_ask_pass is True
    assert args.become_password_file == C.BECOME_PASSWORD_FILE


# Generated at 2022-06-12 20:13:32.258990
# Unit test for function add_output_options
def test_add_output_options():
    test_parser = argparse.ArgumentParser()
    add_output_options(test_parser)
    options = test_parser.parse_args(['-o', '-t', '/tmp/test'])
    assert options.one_line is True
    assert options.tree == '/tmp/test'

# Generated at 2022-06-12 20:14:42.261455
# Unit test for function unfrack_path
def test_unfrack_path():
    assert(unfrack_path()('~/foo') == unfrackpath('~/foo'))
    assert(unfrack_path(True)('~/foo' + os.pathsep + '~/bar') == [unfrackpath('~/foo'), unfrackpath('~/bar')])


# Generated at 2022-06-12 20:14:47.858800
# Unit test for function add_vault_options
def test_add_vault_options():

    parser = argparse.ArgumentParser(prog='test_add_vault')

    add_vault_options(parser)
    print(dir(parser))
    print(dir(parser.parse_args))

    sys.exit(0)
    #args = parser.parse_args()
    #print(args)
if __name__ == '__main__':
    test_add_vault_options()

# Generated at 2022-06-12 20:14:58.148034
# Unit test for function unfrack_path
def test_unfrack_path():
    class Options(object):
        pass
    options = Options()
    options.ROLES_PATH = '/etc/foo'
    options.DEFAULT_ROLES_PATH = '/etc/bar'
    options.collections_paths = ['/var/lib/ansible/', '/etc/ansible/collections']

    unfrack_path_callback = unfrack_path()
    env_wrapper = lambda x: x

    assert unfrack_path_callback(options.ROLES_PATH) == '/etc/foo'
    assert unfrack_path_callback('-') == '-'

    assert unfrack_path_callback(options.DEFAULT_ROLES_PATH) == '/etc/bar'
    assert unfrack_path_callback('-') == '-'

    assert unfrack_path_callback('$ROLES_PATH')

# Generated at 2022-06-12 20:15:06.447213
# Unit test for function unfrack_path
def test_unfrack_path():
    try:
        path = os.path.join('home', 'user', 'my_dir')
        os.environ['HOME'] = path
        assert unfrackpath(os.path.join('~', 'my_dir')) == path
        assert unfrackpath(os.path.join('~/my_dir')) == path
        assert unfrackpath(os.path.join('~', 'user', 'my_dir')) == path
        assert unfrackpath(os.path.join('~user/my_dir')) == path
        assert unfrackpath(os.path.join('$HOME/my_dir')) == path
        assert unfrackpath(os.path.join('${HOME}/my_dir')) == path
    finally:
        del os.environ['HOME']


# Generated at 2022-06-12 20:15:18.700095
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/tmp') == '/tmp'
    assert unfrack_path(pathsep=True)('/tmp/baz:/tmp/foo') == ['/tmp/baz', '/tmp/foo']
    assert unfrack_path(pathsep=True)('/tmp/baz:/tmp/foo:') == ['/tmp/baz', '/tmp/foo']
    assert unfrack_path(pathsep=True)('/tmp/baz:/tmp/foo:/') == ['/tmp/baz', '/tmp/foo']
    assert unfrack_path(pathsep=True)('/tmp/baz:/tmp/foo::') == ['/tmp/baz', '/tmp/foo']

# Generated at 2022-06-12 20:15:29.268376
# Unit test for function unfrack_path
def test_unfrack_path():
    if sys.version_info[0] < 3 and sys.platform == 'darwin':
        # with Python 2 on Darwin, os.getcwd() gives a path which has been
        # converted from unicode to str.  That's not a problem by itself,
        # but unfrackpath calls `curdir = os.getcwd()` and then converts
        # curdir back to unicode, which fails under py2.
        # Rather than try to fix that case, just skip this test in that environment.
        # The converting back to unicode is still technically the correct thing to do.
        return
    # use the expected current directory as the path
    # this will work on every platform and Python version
    # The unfrackpath function should recognize this as the current directory.
    current = os.getcwd()

# Generated at 2022-06-12 20:15:33.919956
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=True)('/bogus/one:/bogus/two') == ['/bogus/one', '/bogus/two']



# Generated at 2022-06-12 20:15:37.057010
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    args = parser.parse_args(['-T', '11', '-k', '--connection', 'ssh'])
    assert args.timeout == '11'
    assert args.ask_pass == True
    assert args.connection == 'ssh'

# Generated at 2022-06-12 20:15:45.664627
# Unit test for function unfrack_path
def test_unfrack_path():
    """Unit test for function unfrack_path"""
    assert unfrack_path()('/a/b/c') == '/a/b/c'
    assert unfrack_path()('/a/../b/c/d/../e') == '/b/c/e'
    assert unfrack_path()('/a/b/c/') == '/a/b/c/'
    assert unfrack_path()('/a/./b/c/.') == '/a/b/c'
    assert unfrack_path()('/a/b/c/../../d/..') == '/a'
    assert unfrack_path()('../a/b') == '../a/b'
    assert unfrack_path()('/') == '/'



# Generated at 2022-06-12 20:15:54.551294
# Unit test for function unfrack_path
def test_unfrack_path():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.display import Display
    if HAS_LIBYAML:
        yaml_loader = yaml_load
    else:
        yaml_loader = None
    display = Display()

    input_format = ['~/.vault_pass.txt', '~/group_vars/all', '~/inventory']
    output_format = [os.path.expanduser('~/.vault_pass.txt'),
                     os.path.expanduser('~/group_vars/all'),
                     os.path.expanduser('~/inventory')]

    test_vault_pass_path = os.path.expanduser('~/.vault_pass.txt')

# Generated at 2022-06-12 20:16:10.931672
# Unit test for function unfrack_path
def test_unfrack_path():
    """Check unfrack_path function with multiple cases"""
    if os.path.sep == '/':
        cases = [
            # [ input, expected output]
            ["/tmp", "/tmp"],
            ["/tmp///", "/tmp///"],
            ["/tmp/" + os.path.sep + "//", "/tmp///"],
            ["/tmp/../tmp/../tmp/../" + os.path.sep + "//", "/"],
            ["/tmp/./" + os.path.sep + "//", "/tmp///"],
            ["./././/", "/./."],
        ]

# Generated at 2022-06-12 20:16:17.787823
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # if beacon is not present, return the same value
    assert maybe_unfrack_path('test')('test2') == 'test2'
    # if beacon is present, unfrack the path
    assert maybe_unfrack_path('test')('test/path/to/file') == 'test/path/to/file'
    assert maybe_unfrack_path('test')('test/path/to/dir/') == 'test/path/to/dir/'
    assert maybe_unfrack_path('test')('test/path/to/dir/file') == 'test/path/to/dir/file'
    # if beacon is present, but value is '-'
    assert maybe_unfrack_path('test')('test-') == 'test-'



# Generated at 2022-06-12 20:16:18.597782
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    assert None is not None



# Generated at 2022-06-12 20:16:24.431425
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('foo') == 'foo'
    assert unfrack_path(pathsep=False)('~/foo') == os.path.expanduser('~/foo')
    assert unfrack_path(pathsep=True)('foo:~/bar:baz') == ['foo', os.path.expanduser('~/bar'), 'baz']


# Generated at 2022-06-12 20:16:32.769449
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    """
    # From https://github.com/ansible/ansible/blob/stable-2.9/lib/ansible/utils/module_docs_fragments.py
    """
    from ansible.utils.module_docs_fragments import PrependListAction
    # prepend to empty list
    parser = argparse.ArgumentParser(add_help=False)
    res = parser.parse_args([], namespace=argparse.Namespace(argv=[]))
    assert not hasattr(res, 'argv')  # Remember, this namespace must be clean!
    action = PrependListAction('-a', 'argv')
    res = parser.parse_args(['-a', '1'], namespace=res)
    assert res.argv == ['1']

    # Append to list that already exists
   

# Generated at 2022-06-12 20:16:37.312801
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()(__file__) == unfrackpath(__file__)
    assert unfrack_path(pathsep=True)('.' + os.pathsep + __file__) == [unfrackpath('.'), unfrackpath(__file__)]


# Generated at 2022-06-12 20:16:39.803917
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('foo/../bar') == 'bar'
    assert unfrack_path(True)('foo/../bar:baz/../spam') == ['bar', 'spam']


# Generated at 2022-06-12 20:16:48.028285
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('/foo') == '/foo'
    assert maybe_unfrack_path('@')('@/foo') == '@/foo'
    assert maybe_unfrack_path('@')('@/foo/') == '@/foo'
    assert maybe_unfrack_path('@')('@/foo/../bar') == '@/bar'
    assert maybe_unfrack_path('@')('@/foo/../bar/../../baz') == '@/baz'
    assert maybe_unfrack_path('@')('@../foo') == '@../foo'


# Generated at 2022-06-12 20:16:56.219982
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    with_beacon = maybe_unfrack_path('@')
    assert with_beacon('Testing') == 'Testing'
    assert with_beacon('@/testing') == '@/testing'
    assert with_beacon('@@/testing') == '@@/testing'
    assert with_beacon('@@@/testing') == '@@/testing'
    assert with_beacon('@@//testing') == '@@/testing'
    assert with_beacon('@@/.//testing') == '@@/testing'
    assert with_beacon('@@/././testing') == '@@/testing'
    assert with_beacon('@@/././testing/../') == '@@/testing'
    assert with_beacon('@@/././testing/.././') == '@@/testing'

    with_beacon = maybe_unfr

# Generated at 2022-06-12 20:17:05.984431
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('/tmp') == '/tmp'
    assert unfrack_path(pathsep=False)('~/tmp') == os.path.expanduser('~/tmp')
    assert unfrack_path(pathsep=False)('~/tmp/') == os.path.expanduser('~/tmp/')
    assert unfrack_path(pathsep=False)('~user/tmp') == '~user/tmp'
    assert unfrack_path(pathsep=False)('$HOME/tmp') == os.environ['HOME'] + '/tmp'
    assert unfrack_path(pathsep=True)('/tmp:/tmp2') == ['/tmp', '/tmp2']

# Generated at 2022-06-12 20:17:15.357757
# Unit test for function unfrack_path
def test_unfrack_path():
    path = './a/b/c'
    # Test single path
    assert unfrack_path()(path) == path
    # Test multiple paths split by os.pathsep
    for sep in (':', '::', ','):
        if sep == os.pathsep:
            expected = path
        else:
            expected = ['./a/b/c']
        assert unfrack_path(pathsep=True)(path + sep + path) == expected



# Generated at 2022-06-12 20:17:25.050666
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('ansible') == 'ansible'
    assert unfrack_path()('') == ''
    assert unfrack_path()('/') == '/'
    assert unfrack_path()('/var/lib') == '/var/lib'
    assert unfrack_path()('/tmp/data') == '/tmp/data'
    assert unfrack_path()('/tmp/data/') == '/tmp/data'

    assert unfrack_path(pathsep=True)('ansible') == ['ansible']
    assert unfrack_path(pathsep=True)('') == []
    assert unfrack_path(pathsep=True)('ansible') == ['ansible']
    assert unfrack_path(pathsep=True)('/') == ['/']

# Generated at 2022-06-12 20:17:32.533082
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = get_parser()
    argholder = {
        'filter_plugin': []
    }
    parser.parse_args('-f foo'.split(), argholder)
    assert argholder['filter_plugin'] == ['foo']
    parser.parse_args('-f foo -f bar'.split(), argholder)
    assert argholder['filter_plugin'] == ['foo', 'bar']
    parser.parse_args('-f foo -f bar -f baz'.split(), argholder)
    assert argholder['filter_plugin'] == ['foo', 'bar', 'baz']



# Generated at 2022-06-12 20:17:36.832409
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    parser.add_argument('--bar')
    class_SortingHelpFormatter_obj = SortingHelpFormatter()
    class_SortingHelpFormatter_obj.add_argument(parser)


# Generated at 2022-06-12 20:17:48.653854
# Unit test for function unfrack_path
def test_unfrack_path():
    """
    Test if paths normalized correctly in various environment variables
    """
    result_dict = {
        'AN': ['Z:\\one', 'Z:\\two'],
        'NA': ['Z:\\three', 'Z:\\four'],
        'NF': ['Z:\\five', 'Z:\\six']
    }
    for env_var in result_dict:
        original_env = os.environ.get(env_var, None)
        if original_env is not None:
            del os.environ[env_var]
        os.environ[env_var] = os.pathsep.join(result_dict[env_var])
        assert unfrack_path()(env_var) == result_dict[env_var][0]

# Generated at 2022-06-12 20:17:55.410525
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action=PrependListAction, default=[1, 2, 3])
    parser.add_argument('--bar', nargs=2)
    assert parser.parse_args(['--foo', '4', '5', '--bar', '6', '7']).foo == [4, 5, 1, 2, 3]
    assert parser.parse_args(['--bar', '6', '7']).foo == [1, 2, 3]
    assert parser.parse_args(['--bar', '6', '7']).bar == ['6', '7']


#
# General purpose methods
#

# Generated at 2022-06-12 20:18:04.718433
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('/etc/ansible/file.yml') == '/etc/ansible/file.yml'
    assert unfrack_path(pathsep=False)('file.yml') == os.path.abspath('file.yml')
    assert unfrack_path(pathsep=True)('/etc/ansible/file.yml') == ['/etc/ansible/file.yml']
    assert unfrack_path(pathsep=True)('/etc/ansible/file.yml:/etc/ansible/file.yml:file.yml') == ['/etc/ansible/file.yml', '/etc/ansible/file.yml', os.path.abspath('file.yml')]



# Generated at 2022-06-12 20:18:09.268479
# Unit test for function unfrack_path
def test_unfrack_path():
    def test(path, expected):
        actual = unfrack_path()(path)
        assert actual == expected, "%s != %s" % (actual, expected)

    test('roles/something', os.path.abspath('roles/something'))
    test('$HOME/roles/something', os.path.expanduser('roles/something'))
    test('~/roles/something', os.path.expanduser('~/roles/something'))
    test('../something', os.path.abspath('../something'))
    test('/something', '/something')
    test('/role/../something', os.path.abspath('/something'))
    test('/something/else/..', os.path.abspath('/something'))

# Generated at 2022-06-12 20:18:20.245093
# Unit test for function unfrack_path
def test_unfrack_path():

    class Args:
        inventory = ''
        module_path = ''
        roles_path = ''
        vault_password_file = ''
        # environment variables
        ANSIBLE_VAULT_PASSWORD_FILE = ''
        ANSIBLE_INVENTORY = ''
        ANSIBLE_ROLES_PATH = ''
        ANSIBLE_CONFIG = ''

    # create args object
    args = Args()

    # test unfrack_path
    path = '/path/to/file'
    assert(unfrack_path()(path) == path)  # expected unchanged.


# Generated at 2022-06-12 20:18:25.521773
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a_option', action=PrependListAction, nargs='*')
    namespace = parser.parse_args(['--a_option', '1', '2', '--a_option', '3'])
    assert namespace.a_option == ['3', '1', '2']



# Generated at 2022-06-12 20:18:45.787250
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    import pytest
    option_strings = ("--option-strings",)
    dest = ("--dest",)
    with pytest.raises(ValueError) as excinfo:
        parser = PrependListAction(option_strings, dest, nargs=0)
    msg = "nargs for append actions must be > 0; if arg strings are not supplying the value to append, the append const action may be more appropriate"
    assert str(excinfo.value) == msg
    with pytest.raises(ValueError) as excinfo:
        parser = PrependListAction(option_strings, dest, nargs=1, const="abc")
    msg = "nargs must be <operator.attrgetter object at 0x7f72f1e410c8> to supply const"
    assert str(excinfo.value) == msg
    parser = Prep

# Generated at 2022-06-12 20:18:54.026137
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    test_actions = ['-o', '--option', '--longoption', '-f', '--format', '-e', '--engine']
    argparse_version = pkg_resources.get_distribution('argparse').version
    if argparse_version.startswith('1'):
        expected_output = ("option: -o, --option\n"
                           "longoption: --longoption\n"
                           "format: -f, --format\n"
                           "engine: -e, --engine\n")

# Generated at 2022-06-12 20:18:57.797648
# Unit test for function unfrack_path
def test_unfrack_path():
    os_unfrack_path_out = unfrack_path()('/usr/local/bin:/usr/bin:/opt/bin')

    assert os_unfrack_path_out == ['/usr/local/bin', '/usr/bin', '/opt/bin']



# Generated at 2022-06-12 20:19:01.279734
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("~/test") == os.path.expanduser("~/test")
    # unfrack_path("~/test:~/test2") doesn't work with : since it is a os.pathsep
    assert unfrack_path("~/test:~/test2")("~/test:~/test2") == os.path.expanduser("~/test")

# Generated at 2022-06-12 20:19:05.734066
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """Verify that the maybe_unfrack_path function works as expected"""
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    cwd = os.getcwd()
    tempdir = '/tmp/ansible-test-vault'
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)

    os.chdir(tempdir)

    load = DataLoader()

    context = PlayContext()

    context.vault_password_files = [os.path.join(cwd, 'test/unit/vault/test.vault.pw')]
    context.vault_ids = ['test']
    context.update_vault_secrets(None)


# Generated at 2022-06-12 20:19:08.666187
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/path/to/file') == '@' + unfrackpath('/path/to/file')
    assert maybe_unfrack_path('@')('/path/to/file') == '/path/to/file'



# Generated at 2022-06-12 20:19:14.992517
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    class FakeParser(object):
        def error(self, *args, **kwargs):
            pass
    class FakeNamespace(object):
        pass
    parser = FakeParser()
    namespace = FakeNamespace()
    namespace.foo = None
    prependListAction = PrependListAction(
        option_strings=['--foobar'],
        dest='foo',
        nargs='*',
        const=None,
        default=None,
        type=None,
        choices=None,
        required=True,
        help=None,
        metavar=None
    )
    assert namespace.foo == None
    prependListAction.__call__(parser, namespace, ['bar', 'baz'], option_string='--foobar')
    assert namespace.foo == ['bar', 'baz']
    prependList

# Generated at 2022-06-12 20:19:21.889152
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/usr/lib/python3.6/site-packages/ansible/config/') == \
        '/usr/lib/python3.6/site-packages/ansible/config'
    assert unfrack_path(pathsep=True)('/usr/lib/python3.6/site-packages/ansible/config:/foo/bar') == \
        ['/usr/lib/python3.6/site-packages/ansible/config', '/foo/bar']



# Generated at 2022-06-12 20:19:31.954495
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    from ansible.cli import CLI
    test_key = 'test_key'
    test_value_1 = 'test_value_1'
    test_value_2 = 'test_value_2'

    # create a CLI object with the append arg
    cli = CLI([])
    cli.parser.add_argument(
        '-a', '--append',
        dest=test_key,
        action=PrependListAction,
        help='append to list'
    )

    # run the argument through the parser
    cli.parse(['--append', test_value_1, '--append', test_value_2])

    # extract and return the value from the namespace
    namespace = cli.parser.parse_args([]).__dict__
    return namespace[test_key]



# Generated at 2022-06-12 20:19:39.532727
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert '@test' == maybe_unfrack_path('@')('@test')
    assert unfrackpath('test') == maybe_unfrack_path('@')('test')
    assert '@@test' == maybe_unfrack_path('@')('@@test')
    assert unfrackpath('@test') == maybe_unfrack_path('@')('@test')
    assert 'test' == maybe_unfrack_path('@')('test')
    assert 'test/' == maybe_unfrack_path('@')('test/')



# Generated at 2022-06-12 20:20:21.004037
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    candidates = [
        ('a', 'a'),
        ('#a', '#a'),
        ('#/a', '#' + unfrackpath('/a')),
        ('./#a', './#a'),
        ('./#/a', './#' + unfrackpath('/a')),
        ('./#/a/./#/b', './#' + unfrackpath('/a') + '/./#' + unfrackpath('/b'))
    ]
    test_unfrack_path = maybe_unfrack_path('#')
    for value, expected in candidates:
        assert test_unfrack_path(value) == expected
test_maybe_unfrack_path()


# Generated at 2022-06-12 20:20:30.441988
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    pass

    # from ansible.cli.argparse import PrependListAction
    action = PrependListAction(option_strings=None, dest='my_arg', nargs=None, const=None, default=None, type=None,
                               choices=None, required=False, help=None, metavar=None)

    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--my-arg', action=action)
    args = parser.parse_args(['--my-arg', '[1, 2]', '--my-arg', '[3, 4]'])
    assert args.my_arg == [[3, 4], [1, 2]]

# Generated at 2022-06-12 20:20:35.839630
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$FOO') == '$/some/path/FOO'
    assert maybe_unfrack_path('$')('$') == '$'
    assert maybe_unfrack_path('$')('FOO') == 'FOO'
    assert maybe_unfrack_path('@')('@FOO') == '@/some/path/FOO'
    assert maybe_unfrack_path('@')('@') == '@'
    assert maybe_unfrack_path('@')('FOO') == 'FOO'

#
# Generic Options validators
#

# Generated at 2022-06-12 20:20:41.756428
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()(os.path.expanduser('~/')) == os.path.expanduser('~/')
    assert unfrack_path()(os.path.expanduser('~//')) == os.path.expanduser('~/')
    assert unfrack_path()(os.path.expanduser('~// ')) == os.path.expanduser('~/')
    assert unfrack_path()(os.path.expanduser(' ~/')) == os.path.expanduser('~/')
    assert unfrack_path()(os.path.expanduser(' ~/ ')) == os.path.expanduser('~/')
#
# Generic Options
#

# Generated at 2022-06-12 20:20:45.498893
# Unit test for function unfrack_path
def test_unfrack_path():
    """Tests for function unfrack_path"""
    # UNIX-style paths
    config = 'file:' + os.environ["HOME"] + os.sep + ".ansible" + os.sep + "ansible.cfg"
    assert unfrack_path(False)(config) == config, "Failed to convert an absolute UNIX-style path."
    # Windows-style paths
    if os.name == "nt":
        config = 'file:' + os.sep + os.environ["USERPROFILE"] + os.sep + "ansible.cfg"
        assert unfrack_path(False)(config) == config, "Failed to convert an absolute Windows-style path."
    # Path separators

# Generated at 2022-06-12 20:20:49.769194
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    parser.add_argument('--append', dest='foo', action=PrependListAction)
    args = parser.parse_args('--append a --append b'.split())
    assert args.foo == ['a', 'b'], args.foo



# Generated at 2022-06-12 20:20:56.775803
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    import os
    import os.path
    import sys
    import ansible.constants as C
    import pytest

    C._ANSIBLE_ARGS = C._UNPARSED_ARGS

    @pytest.fixture
    def parser(request):
        # For test_PrependListAction___call__1()
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-b', '--bindir',
            dest='rootpath',
            action='store',
            help="Search for ansible binaries in the directory (or list of directories separated by ':' in *nix).",
            default=None
        )

# Generated at 2022-06-12 20:21:02.186051
# Unit test for function unfrack_path
def test_unfrack_path():
    for input_, expected in (
            ('/etc/ansible', '/etc/ansible'),
            ('http://example.com/ansible/roles', 'http://example.com/ansible/roles'),
            ('/tmp/foo:bar/test', ['/tmp/foo', 'bar/test']),
            ('/tmp/foo::/bar/test', ['/tmp/foo', '/bar/test']),
            ('/tmp/foo::/bar/test:/tests/test', ['/tmp/foo', '/bar/test', '/tests/test'])
    ):
        result = unfrack_path(pathsep=':')(input_)
        if result != expected:
            raise AssertionError('unfrack_path(%r) -> %r, expected %r' % (input_, result, expected))
#

# Generated at 2022-06-12 20:21:07.595938
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    import pytest
    test_cases = [
        {'input': 'foo', 'beacon': '@', 'expected': 'foo'},
        {'input': '@foo', 'beacon': '@', 'expected': '@foo'},
        {'input': '@@foo', 'beacon': '@@', 'expected': '@@foo'},
        {'input': '@foo', 'beacon': '@@', 'expected': '@foo'}
    ]
    for test_case in test_cases:
        got = maybe_unfrack_path(test_case['beacon'])(test_case['input'])
        assert got == test_case['expected']



# Generated at 2022-06-12 20:21:16.577481
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--append-const', dest='x', action=PrependListAction, const='const', nargs='?')
    parser.add_argument('--append', dest='x', action=PrependListAction)
    parser.add_argument('y', nargs='*')
    parser.add_argument('z', nargs='?')
    assert parser.parse_args(['zzz', '--append', 'aaa', 'bbb', '--append-const', 'ccc', 'ddd']).x == ['ccc', 'aaa', 'bbb']
    assert parser.parse_args(['--append-const', 'xxx', 'yyy']).x == ['xxx']
    assert parser.parse_args(['--append-const']).x == ['const']


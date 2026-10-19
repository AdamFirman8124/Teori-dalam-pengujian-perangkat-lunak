

# Generated at 2022-06-12 20:12:15.759977
# Unit test for function add_inventory_options
def test_add_inventory_options():
    inventory = os.path.join(os.path.dirname(__file__), "..", "..", "playbooks", "inventory")
    assert os.path.exists(inventory)
    base_parser = create_base_parser('ansible-config', usage="usage: %%prog [options]")
    add_inventory_options(base_parser)
    args_parser = base_parser.parse_args(['-i', inventory, '--list-hosts', '-l', 'bad*.com'])
    assert args_parser.listhosts is True
    assert args_parser.inventory == [os.path.normpath(inventory)]
    assert args_parser.subset == 'bad*.com'



# Generated at 2022-06-12 20:12:20.323630
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    options = parser.parse_args('-C --syntax-check -D'.split())
    assert options.check == True
    assert options.syntax == True
    assert options.diff == True

# End test_add_check_options


# Generated at 2022-06-12 20:12:25.734060
# Unit test for function add_check_options
def test_add_check_options():
    from ansible.config.manager import ConfigManager
    from ansible.utils.vars import combine_vars
    config_manager = ConfigManager(os.path.join(os.path.dirname(__file__), 'test_config.yml'))
    config_manager.options = combine_vars(get_config(parser, options, output=False), '/dev/null')
    # parser will be a fake parser, the result of parser.parse_args() will be the same as options
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion, nargs=0)
    options = parser.parse_args()
    # test no options
    add_check_options(parser)
    options = parser.parse_args()
    assert options.check == False

# Generated at 2022-06-12 20:12:32.548682
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = create_base_parser(prog="test_add_inventory_options_parser")
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'hosts,host2', '--list-hosts', '-l', 'host'])
    assert args.inventory == ['hosts,host2']
    assert args.listhosts
    assert args.subset == 'host'

# Generated at 2022-06-12 20:12:36.065109
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser()
    add_output_options(parser)
    args = parser.parse_args(['-o', '-t', 'test'])
    assert args.one_line is True
    assert args.tree == 'test'

# Generated at 2022-06-12 20:12:40.621359
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/tmp') == '/tmp'
    assert unfrack_path(pathsep=True)('/tmp:~/') == ['/tmp', '~/']



# Generated at 2022-06-12 20:12:46.686409
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser(prog='mock')
    add_inventory_options(parser)
    args = parser.parse_args(['-i', '/etc/ansible/hosts', '-i', '":"'.join(['/etc/ansible/hosts', ','.join(['localhost', '127.0.0.1'])]), '--list-hosts', '-l', 'all'])
    assert args.inventory == ['/etc/ansible/hosts', ':'.join(['/etc/ansible/hosts', ','.join(['localhost', '127.0.0.1'])])]
    assert args.listhosts == True
    assert args.subset == 'all'



# Generated at 2022-06-12 20:12:53.039838
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('$ANSIBLE_CONFIG') == unfrackpath('$ANSIBLE_CONFIG')
    assert unfrack_path()('/dev/null') == unfrackpath('/dev/null')
    assert unfrack_path(pathsep=True)('$ANSIBLE_CONFIG:/dev/null') == [unfrackpath('$ANSIBLE_CONFIG'), unfrackpath('/dev/null')]



# Generated at 2022-06-12 20:12:58.565498
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    module = AnsibleModule(
        argument_spec = dict(
            become=dict(required=True, type='bool'),
            become_method=dict(required=True, type='str'),
            become_user=dict(required=True, type='str'),
            become_ask_pass=dict(required=True, type='bool'),
            become_password_file=dict(required=True, type='str')
        )
    )

    parser = argparse.ArgumentParser()
    add_runas_prompt_options(parser)
    args = parser.parse_args([])


# Generated at 2022-06-12 20:13:04.039842
# Unit test for function add_meta_options
def test_add_meta_options():
    '''
    valitaion of function add_meta_options
    '''
    from ansible.cli import CLI
    parser = argparse.ArgumentParser(prog='ansible', formatter_class=SortingHelpFormatter)
    CLI.add_parser_options(parser)
    options = parser.parse_args(['--flush-cache'])
    add_meta_options(parser)
    assert options.flush_cache is True


# Generated at 2022-06-12 20:13:23.803588
# Unit test for function add_meta_options
def test_add_meta_options():
  parser = argparse.ArgumentParser()
  add_meta_options(parser)
  return parser



# Generated at 2022-06-12 20:13:29.015486
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    #  parser.parse_args(['--private-key', '--key-file', 'abc'])
    #parsed_args, remaining_args = parser.parse_known_args(['--private-key', '--key-file', 'abc', '--syntax-check'])
    #print(parsed_args)
    return parser

import argcomplete
if __name__ == '__main__':
    parser = test_add_connect_options()
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    print(args)

# Generated at 2022-06-12 20:13:36.928437
# Unit test for function unfrack_path
def test_unfrack_path():
    if os.path.sep == '/':
        assert unfrack_path()('/') == '/'
        assert unfrack_path()('/tmp/') == '/tmp'
        assert unfrack_path(True)('/tmp/:/tmp') == ['/tmp', '/tmp']
    else:
        assert unfrack_path()('C:\\') == 'C:\\'
        assert unfrack_path()('C:\\tmp\\') == 'C:\\tmp'
        assert unfrack_path(True)('C:\\tmp\\;C:\\tmp') == ['C:\\tmp', 'C:\\tmp']


# Generated at 2022-06-12 20:13:45.335083
# Unit test for function add_connect_options
def test_add_connect_options():
    class options:
        private_key_file = None
        remote_user = None
        connection = None
        timeout = None
        ssh_common_args = None
        sftp_extra_args = None
        ssh_extra_args = None
        scp_extra_args = None
        ask_pass = None
        connection_password_file = None

    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    parser.parse_args(namespace=options)
    assert options.private_key_file == '~/.ssh/id_rsa'
    assert options.remote_user == 'root'
    assert options.connection == 'smart'
    assert options.timeout == 10
    assert options.ssh_common_args == None
    assert options.sftp_extra_args == None

# Generated at 2022-06-12 20:13:49.181025
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = create_base_parser('')
    add_fork_options(parser)
    args = parser.parse_args(['-f', '0'])
    assert args.forks == 0



# Generated at 2022-06-12 20:13:51.263398
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    add_connect_options(parser)
    options = parser.parse_args(['--private-key', 'test_key'])
    assert options.private_key_file == 'test_key'

# Generated at 2022-06-12 20:13:59.488808
# Unit test for function add_connect_options
def test_add_connect_options():
    from ansible.config.manager import ConfigManager
    from ansible.cli.arguments import add_connect_options
    from ansible.cli import CLI
    loader = ConfigManager(['ansible.cfg'])
    password = 'password'
    # redefined -u ansible remote_user
    config_args = dict(remote_user='ansible')
    cli_args = dict(remote_user='ansible_cli')

    class BaseCLI(CLI):
        def get_optparser(self):
            parser = CLI.get_optparser(self)
            add_connect_options(parser)
            return parser

    cli = BaseCLI(None, loader, config_args, cli_args)
    options = cli.parse()

    # Check redefined remote_user

# Generated at 2022-06-12 20:14:06.848286
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)

    cli_args = ["-t", "tag1", "--tags", "tag2", "--skip-tags", "tag3", "--skip-tags=tag4"]
    expected_args = {"tags": ["tag1", "tag2"],
                     "skip_tags": ["tag3", "tag4"]}
    parsed_args = parser.parse_args(cli_args)

    # Make sure sets of values have the same members, but ignore the order.
    assert set(vars(parsed_args)["tags"]) == set(expected_args["tags"])
    assert set(vars(parsed_args)["skip_tags"]) == set(expected_args["skip_tags"])



# Generated at 2022-06-12 20:14:10.385856
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = create_base_parser("/ansible-playbook")
    add_meta_options(parser)
    args = parser.parse_args("--flush-cache".split())
    assert args.flush_cache is True
# END Unit test for function add_meta_options


# Generated at 2022-06-12 20:14:16.871794
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser(prog='mock')
    add_subset_options(parser)
    p = parser.parse_args(['-t', 'a', '--skip-tags', 'b', '--tags', 'c'])
    assert p.tags == ['a', 'c']
    assert p.skip_tags == ['b']



# Generated at 2022-06-12 20:14:26.996873
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/tmp/foo') == '@/tmp/foo'
    assert maybe_unfrack_path('@')('@tmp/foo') == '@/tmp/foo'
    assert maybe_unfrack_path('@')('/tmp/foo') == '/tmp/foo'



# Generated at 2022-06-12 20:14:31.817340
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('~')('~test') == '~/test'
    assert maybe_unfrack_path('~')('/test') == '/test'
    assert maybe_unfrack_path('@')('@test') == '@test'
    assert maybe_unfrack_path('@')('/test') == '/test'


# Generated at 2022-06-12 20:14:34.946545
# Unit test for function version
def test_version():
    # basic test for signature and return value
    assert(version() is not None)

    # Test for git info
    try:
        assert(_gitinfo() == "[branch@commit] last updated ")
    except AssertionError:
        pass



# Generated at 2022-06-12 20:14:37.828349
# Unit test for function version
def test_version():
    assert version() is not None



# Generated at 2022-06-12 20:14:40.508742
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # FIXME: This does not actually unit test anything.
    assert maybe_unfrack_path('@')('@/pathsep/path') == '@/pathsep/path'



# Generated at 2022-06-12 20:14:51.347787
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    a = parser.add_argument("--z")
    b = parser.add_argument("--g")
    c = parser.add_argument("--f")
    d = parser.add_argument("--d")
    e = parser.add_argument("--c")
    f = parser.add_argument("--a")
    parser.epilog = '''
    a
    b
    c
    d
    e
    f
    '''
    parser.formatter_class = SortingHelpFormatter
    output = parser.format_help()
    # Note: Windows paths don't sort correctly.  Skip the epilog test on any platform with backslashes in the path
    # Note: the '+' in the regex below matches any number of spaces, including zero.

# Generated at 2022-06-12 20:14:57.388631
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/home/foo') == unfrackpath('/home/foo')
    assert sorted(unfrack_path(True)('/home/foo:/usr/bar:/tmp')[0:3]) == sorted([unfrackpath('/home/foo'), unfrackpath('/usr/bar'), unfrackpath('/tmp')])
    assert unfrack_path()('-') == '-'


# Generated at 2022-06-12 20:15:01.612091
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter, add_help=False)
    parser.add_argument("-c", action="store", dest="c", help="c")
    parser.add_argument("-a", action="store", dest="a", help="a")
    parser.add_argument("-b", action="store", dest="b", help="b")
    parser.print_help()



# Generated at 2022-06-12 20:15:04.977259
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("@")("@/weird/path") == "@/weird/path"
    assert maybe_unfrack_path("@")("~/weird/path") == '~/weird/path'


# Generated at 2022-06-12 20:15:11.562497
# Unit test for function ensure_value
def test_ensure_value():
    # Test with name in namespace
    namespace = argparse.Namespace()
    setattr(namespace, 'foo', 'bar')
    assert ensure_value(namespace, 'foo', 'baz') == 'bar'
    assert getattr(namespace, 'foo') == 'bar'

    # Test with name not in namespace
    namespace = argparse.Namespace()
    assert ensure_value(namespace, 'foo', 'baz') == 'baz'
    assert getattr(namespace, 'foo') == 'baz'

    # Test with default (None)
    namespace = argparse.Namespace()
    assert ensure_value(namespace, 'foo', None) is None
    assert getattr(namespace, 'foo') is None



# Generated at 2022-06-12 20:15:26.652943
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@@')('@@foo/bar') == '@@/etc/ansible/foo/bar'
    assert maybe_unfrack_path('@@')('foo/bar') == 'foo/bar'
    assert maybe_unfrack_path('@')('@@foo/bar') == '@@foo/bar'
    assert maybe_unfrack_path('@')('@foo/bar') == '@/etc/ansible/foo/bar'
    assert maybe_unfrack_path('@')('foo/bar') == 'foo/bar'


# Generated at 2022-06-12 20:15:38.584449
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(description='Sort options alphabetically',
                                     formatter_class=SortingHelpFormatter)
    parser.add_argument('--goo', dest='goo', type=int, help='goo')
    parser.add_argument('--bar', dest='bar', type=float, help='bar')
    parser.add_argument('--hello', dest='hello', help='hello')
    help = parser.format_help()

    # the help output should be sorted alphabetically
    assert '--bar  bar\n' in help
    assert '--goo  goo\n' in help
    assert '--hello  hello\n' in help

    # now check for stdout/stderr order
    help_lines = help.split('\n')
    assert help_lines.index('usage: ') < help_

# Generated at 2022-06-12 20:15:44.727915
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()(u"~/foo") == u"{}/foo".format(os.path.expanduser('~'))
    assert unfrack_path()(u"${USER}/foo") == u"{}/foo".format(os.getenv('USER'))
    assert unfrack_path()(u"$HOME/foo") == u"{}/foo".format(os.getenv('HOME'))
    assert unfrack_path()(u"~/foo") != u"foo"



# Generated at 2022-06-12 20:15:52.920557
# Unit test for function version
def test_version():
    assert version() == '2.10.2 \n  config file = /etc/ansible/ansible.cfg \n  configured module search path = Default w/o overrides \n  ansible python module location = /usr/lib/python3.6/site-packages/ansible \n  ansible collection location = /usr/share/ansible/collections \n  executable location = /usr/bin/ansible-config \n  python version = 3.6.8 (default, Oct  7 2019, 12:59:55) [GCC 8.3.1 20190507 (Red Hat 8.3.1-4)] \n  jinja version = 2.10 \n  libyaml = False'


# Generated at 2022-06-12 20:15:59.655938
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('../../test' ) == unfrackpath('../../test')
    assert unfrack_path(pathsep=True)('../../test' ) == [unfrackpath('../../test')]
    assert unfrack_path(pathsep=True)('../../test:../../test2' ) == [unfrackpath('../../test'), unfrackpath('../../test2')]



# Generated at 2022-06-12 20:16:10.604353
# Unit test for function unfrack_path
def test_unfrack_path():
    for pathsep in [False, True]:
        path = unfrack_path(pathsep=pathsep)
        assert not path('/')
        assert path('~/foo') == 'foo'
        assert path('$HOME/bar') == 'bar'
        assert path('~root/baz') == '~root/baz'
        assert path('${USERNAME}/foobar') == 'foobar'
        if pathsep:
            assert path('/tmp:/usr/tmp') == ['/tmp', '/usr/tmp']
            assert path('~/foo:${HOME}/bar') == ['foo', 'bar']
            assert path('~root/baz:~root/foobaz:~baduser:/tmp') == \
                                            ['~root/baz', '~root/foobaz', '/tmp']

# Generated at 2022-06-12 20:16:13.927476
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/xyz') == '/xyz'
    assert unfrack_path()('./xyz') == os.path.abspath('./xyz')
    assert unfrack_path()('~/xyz') == os.path.expanduser('~/xyz')



# Generated at 2022-06-12 20:16:23.347468
# Unit test for function unfrack_path
def test_unfrack_path():
    curdir = os.getcwd()
    # Test that the os.pathsep is analyzed.
    os.chdir('/tmp')
    assert unfrack_path(pathsep=False)('~/ansible/') == '%s/ansible/' % os.path.expanduser('~')
    assert unfrack_path(pathsep=True)('~/ansible/:/tmp') == ['%s/ansible/' % os.path.expanduser('~'), '/tmp']

    # Test that the dirname is used for relative paths.
    os.chdir(curdir)
    assert unfrack_path(pathsep=False)('../') == '%s/..' % curdir

# Generated at 2022-06-12 20:16:28.223622
# Unit test for function version
def test_version():
    assert str is not bytes
    data = version(prog="ansible-playbook")
    assert "ansible-playbook [core" in data
    assert __version__ in data
    assert os.path.abspath(sys.argv[0]) in data
    assert sys.version in data
    assert "jinja version = 2." in data


# Generated at 2022-06-12 20:16:36.436134
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    # create arguments in different orders to make sure they are sorted later
    parser.add_argument('-a')
    parser.add_argument('--c')
    parser.add_argument('-b')

    output = parser.format_help().split('\n')
    assert '-a' in output[2]
    assert '-b' in output[3]
    assert '--c' in output[4]



# Generated at 2022-06-12 20:16:54.288157
# Unit test for function unfrack_path
def test_unfrack_path():
    original = '~/a/b:~/b/c'
    expected = [os.path.expanduser('~/a/b'), os.path.expanduser('~/b/c')]
    assert sorted(expected) == sorted(unfrack_path(pathsep=True)(original))

    original = '~/a/b'
    expected = os.path.expanduser(original)
    assert expected == unfrack_path(pathsep=False)(original)



# Generated at 2022-06-12 20:16:57.812910
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=False)('spam') == unfrackpath('spam')
    assert unfrack_path(pathsep=False)('-') == '-'
    assert unfrack_path(pathsep=True)('spam' + os.pathsep + 'eggs') == [unfrackpath('spam'), unfrackpath('eggs')]
    assert unfrack_path(pathsep=True)('-') == ['-', '-']


# Generated at 2022-06-12 20:17:03.740036
# Unit test for function version
def test_version():
    '''Test version() function'''
    import ansible.utils.version

    v = ansible.utils.version.version()

    assert 'ansible-config' in v
    assert __version__ in v
    assert 'configured module search path' in v
    assert 'jinja version' in v
    assert 'python version' in v
    assert 'executable location' in v
    assert 'ansible python module location' in v
    assert 'libyaml = ' in v

# Generated at 2022-06-12 20:17:09.841123
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # When the string startswith the beacon, the tail should be unfracked
    assert(maybe_unfrack_path('/foo')('/foo/bar/baz') == '/foo/bar/baz')
    # When the string does not startswith the beacon, return it unchanged
    assert(maybe_unfrack_path('/foo')('/bar/baz') == '/bar/baz')
    # When the string is only the beacon, return it unchanged
    assert(maybe_unfrack_path('/foo')('/foo') == '/foo')


# Generated at 2022-06-12 20:17:15.332923
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('#')('#~/foo') == '#~/foo'
    assert maybe_unfrack_path('#')('#~/foo/bar/baz') == '#~/foo/bar/baz'
    assert maybe_unfrack_path('#')('#foo/bar/baz') == '#foo/bar/baz'
    assert maybe_unfrack_path('#')('foo/bar/baz') == 'foo/bar/baz'
    assert maybe_unfrack_path('#')('foo') == 'foo'
    assert maybe_unfrack_path('#')('#/foo') == '#/foo'
    assert maybe_unfrack_path('#')('~/foo') == '~/foo'


# Generated at 2022-06-12 20:17:23.980530
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('~')('~/foo/bar') == '~/foo/bar'
    assert maybe_unfrack_path('~')('~foo/bar') == '~/foo/bar'
    assert maybe_unfrack_path('~')('~/foo~/bar') == '~/foo/bar'
    assert maybe_unfrack_path('~')('/foo') == '/foo'
    assert maybe_unfrack_path('/')('~/foo/bar') == '~/foo/bar'
    assert maybe_unfrack_path('/')('/foo') == '/foo'



# Generated at 2022-06-12 20:17:29.236059
# Unit test for function unfrack_path
def test_unfrack_path():
    if os.path.sep == '/':
        assert unfrack_path()('~/foo/bar') == os.path.expanduser('~/foo/bar')
        assert unfrack_path(True)('/foo/bar:/baz/qux') == ['/foo/bar', '/baz/qux']



# Generated at 2022-06-12 20:17:32.353726
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@BASEDIR/foo') == '@' + unfrackpath('BASEDIR/foo')
    assert maybe_unfrack_path('@')('/foo') == '/foo'



# Generated at 2022-06-12 20:17:41.485711
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("$")("$/tmp/foo") == "$/tmp/foo"
    assert maybe_unfrack_path("$")("$x/tmp/foo") == "$x/tmp/foo"
    assert maybe_unfrack_path("$")("$x$x/tmp/foo") == "$x$x/tmp/foo"
    assert maybe_unfrack_path("$")("$$/tmp/foo") == "$$/tmp/foo"
    assert maybe_unfrack_path("$")("$$$/tmp/foo") == "$$$/tmp/foo"
    assert maybe_unfrack_path("$")("$$$x/tmp/foo") == "$$$x/tmp/foo"

# Generated at 2022-06-12 20:17:48.790029
# Unit test for function unfrack_path
def test_unfrack_path():
    cur = os.path.dirname(os.path.abspath(__file__))
    cur_local = cur.replace(os.path.sep, '/')
    tests = [
        # Value, PathSep, Expected output
        (cur, False, cur),
        (cur, True, [cur]),
        (cur_local, False, cur),
        (cur_local, True, [cur]),
    ]

    for value, pathsep, expected in tests:
        # Test function is callable and has the correct return type
        nps = unfrack_path(pathsep=pathsep)
        ret = nps(value)
        assert isinstance(ret, type(expected)), "Return type does not match expected type"
        assert ret == expected
# end of test_unfrack_path



# Generated at 2022-06-12 20:18:22.826166
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('*')('*~/somepath') == '*~/somepath'
    assert maybe_unfrack_path('@')('@/somepath') == '@/somepath'
    assert maybe_unfrack_path('*')('*/somepath') == '*' + unfrackpath('/somepath')
    assert maybe_unfrack_path('@')('@./somepath') == '@' + unfrackpath('./somepath')
    assert maybe_unfrack_path('*')('~/somepath') == unfrackpath('~/somepath')
    assert maybe_unfrack_path('@')('./somepath') == unfrackpath('./somepath')



# Generated at 2022-06-12 20:18:26.748081
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert 'yup' == maybe_unfrack_path('yup')('yup')
    assert 'yup-path' == maybe_unfrack_path('yup')('yup-path')



# Generated at 2022-06-12 20:18:34.930924
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("foo") == unfrackpath("foo")
    assert unfrack_path()("foo:bar") == unfrackpath("foo:bar")
    assert unfrack_path(pathsep=True)("foo") == [unfrackpath("foo")]
    assert unfrack_path(pathsep=True)("foo:bar") == [unfrackpath("foo"), unfrackpath("bar")]
    # Ensure path separator is normalized to ':'
    assert unfrack_path(pathsep=True)("foo:bar:baz") == [unfrackpath("foo"), unfrackpath("bar"), unfrackpath("baz")]

# Generated at 2022-06-12 20:18:39.077859
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_values = (
        # test_name, value, beacon, expected_return
        ("No path",
         '/usr/bin/python', '~', '/usr/bin/python'),
        ("Simple path",
         '~/foo', '~', '~/foo'),
        ("Path in a path",
         '/etc/ansible/~/foo', '~', '/etc/ansible/~/foo'),
        ("cwd path",
         './', '~', './'),
        ("cwd path",
         '~/.', '~', '~/.'),
        )

    for test_name, value, beacon, expected_return in test_values:
        return_value = maybe_unfrack_path(beacon)(value)

# Generated at 2022-06-12 20:18:43.770025
# Unit test for function unfrack_path
def test_unfrack_path():
    """Check that unfrack_path returns the same value for values that expand to the same path"""
    fp = unfrack_path()
    assert 'test.yml' == fp('test.yml')
    assert 'test.yml' == fp('$HOME/test.yml')
    assert 'test.yml' == fp('$HOME//test.yml')
    assert '/tmp/test.yml' == fp('/tmp//test.yml')
    assert '/tmp/test.yml' == fp('/tmp//test.yml')
    assert '/tmp/test.yml' == fp('/tmp/../tmp//test.yml')
    assert 'test.yml' == fp(os.path.expanduser("~/test.yml"))

    # Example:  /home

# Generated at 2022-06-12 20:18:50.459465
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("a/b/c") == unfrackpath("a/b/c")
    assert unfrack_path()("a/b/c") == os.path.normpath("a/b/c")
    assert unfrack_path(True)("a/b/c:d/e/f") == [unfrackpath("a/b/c"), unfrackpath("d/e/f")]
    assert unfrack_path(True)("a/b/c:d/e/f") == [os.path.normpath("a/b/c"), os.path.normpath("d/e/f")]
    assert unfrack_path()("-") == "-"



# Generated at 2022-06-12 20:18:52.334405
# Unit test for function version
def test_version():
    assert 'ansible-config' in version('ansible-config')

#
# Create an OptionsParser for a specific program
#

# Generated at 2022-06-12 20:18:58.337503
# Unit test for function unfrack_path
def test_unfrack_path():
    # Test vars
    good_path = '~/foo/bar'
    bad_path = '~bad'
    # Call function
    unfrack_correct = unfrack_path(good_path)
    unfrack_false = unfrack_path(bad_path)
    # Test if output is correct
    assert unfrack_correct == os.path.expanduser(good_path)
    assert unfrack_false == bad_path


# Generated at 2022-06-12 20:19:05.238465
# Unit test for function maybe_unfrack_path

# Generated at 2022-06-12 20:19:12.606876
# Unit test for function version

# Generated at 2022-06-12 20:20:32.597216
# Unit test for function version
def test_version():
    assert version('foo') == 'foo [core 2.10.0]\n  config file = /etc/ansible/ansible.cfg\n  configured module search path = Default w/o overrides\n  ansible python module location = /home/automaton/development/ansible/lib/ansible\n  ansible collection location = \n  executable location = /usr/local/bin/ansible\n  python version = 3.7.1 (default, Oct  6 2019, 21:20:22)\n  jinja version = 2.10\n  libyaml = True'



# Generated at 2022-06-12 20:20:41.085548
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bar')
    parser.add_argument('--foo')
    # instance of class SortingHelpFormatter
    formatter = SortingHelpFormatter()
    #  verify add_arguments of the class SortingHelpFormatter is called
    # with sorted actions
    with mock.patch.object(SortingHelpFormatter, 'add_arguments') as mocked:
        formatter._add_item = mock.Mock()
        formatter._add_container = mock.Mock()
        formatter._current_indent = mock.Mock()
        formatter._format_usage = mock.Mock()
        help_message = formatter.format_help(parser)
        # sort actions in option_strings key

# Generated at 2022-06-12 20:20:45.162755
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    curdir = os.path.dirname(os.path.realpath(__file__))
    beacon = '@'
    target = os.path.join(curdir, 'test_maybe_unfrack_path.txt')
    expected = beacon + target
    actual = maybe_unfrack_path(beacon)(beacon + target)
    assert(expected == actual)


# Generated at 2022-06-12 20:20:48.767277
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_path = "~/.ansible/roles"
    result    = maybe_unfrack_path("~")(test_path)
    assert result == "~"+os.path.expanduser("~/.ansible/roles")


# Generated at 2022-06-12 20:20:54.808535
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    path = "/tmp/ansible/frdo"
    fracked_path = "~/tmp/ansible/frdo"
    fracked_path_expected = "~/tmp/ansible/frdo"
    not_fracked_path_expected = path
    fracked_path_actual = maybe_unfrack_path("~")(fracked_path)
    not_fracked_path_actual = maybe_unfrack_path("~")(path)
    assert fracked_path_actual == fracked_path_expected
    assert not_fracked_path_actual == not_fracked_path_expected



# Generated at 2022-06-12 20:20:59.748097
# Unit test for function unfrack_path
def test_unfrack_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', type=unfrack_path(), default='bar')
    parser.add_argument('--baz', type=unfrack_path(True), default='bar')
    args = parser.parse_args(['--foo', 'test/test', '--baz', 'test1/test1:test2/test2', '--bar', 'test3/test3'])
    assert args.foo == 'test/test'
    assert args.baz == ['test1/test1', 'test2/test2']
    assert args.bar == 'test3/test3'



# Generated at 2022-06-12 20:21:04.615662
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('|')('$HOME/foo') == '$HOME/foo'
    assert maybe_unfrack_path('|')('|$HOME/foo') == '|/home/ansible/foo'

#
# Convenience functions to add Options to an OptionParser
#

# Generated at 2022-06-12 20:21:08.317971
# Unit test for function unfrack_path
def test_unfrack_path():
    unfrack_path_list = unfrack_path(pathsep=True)
    assert unfrack_path_list("/tmp/a:/tmp/b:/tmp/a/file.yml") == ['/tmp/a', '/tmp/b', '/tmp/a/file.yml']


# Generated at 2022-06-12 20:21:15.194851
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/path/to/existing/file') == unfrackpath('/path/to/existing/file')
    assert unfrack_path()('/path/to/../existing/file') == unfrackpath('/path/to/../existing/file')
    assert unfrack_path(pathsep=True)('/path/to/existing/file:/path/to/../existing/file:/path/to:') == [unfrackpath('/path/to/existing/file'), unfrackpath('/path/to/../existing/file'), unfrackpath('/path/to')]

#
# Common OptionGroups and Options
#

# Generated at 2022-06-12 20:21:22.220050
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_beacon = '@'
    test_value_startswith_beacon = '@/tmp/my.yml'
    test_value_not_startswith_beacon = '/tmp/my.yml'

    # test_value_startswith_beacon
    result = maybe_unfrack_path(test_beacon)(test_value_startswith_beacon)
    assert '@' + unfrackpath('/tmp/my.yml') == result

    # test_value_not_startswith_beacon
    result = maybe_unfrack_path(test_beacon)(test_value_not_startswith_beacon)
    assert test_value_not_startswith_beacon == result


#
# Options
#
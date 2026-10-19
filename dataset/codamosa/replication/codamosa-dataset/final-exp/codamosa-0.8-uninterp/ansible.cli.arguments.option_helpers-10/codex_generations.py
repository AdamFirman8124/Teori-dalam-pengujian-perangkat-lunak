

# Generated at 2022-06-12 20:12:19.917514
# Unit test for function add_subset_options
def test_add_subset_options():
  # Mocking argument parser
  class ArgumentParser:
    def __init__(self):
      self.metavar = {}
      self.epilog = {}
      self.usage = {}
      self.description = {}
      self.argument_default = {}
      self.formatter_class = {}
      self.help = {}
      self.name = {}
      self.type = {}
      self.dest = {}
      self.default = {}
      self.action = {}
      self.argument_groups = []
  
  parser = ArgumentParser()

  # Unit test for function add_subset_options
  add_subset_options(parser)

  # Checking argument_groups
  assert parser.argument_groups == ['(-t --tags)', '--skip-tags']

# Generated at 2022-06-12 20:12:21.675244
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('.') == os.path.abspath('.')



# Generated at 2022-06-12 20:12:32.425129
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$a') == '$a'
    assert maybe_unfrack_path('$')('${a}') == '${a}'
    assert maybe_unfrack_path('$')('$a/b') == '$a/b'
    assert maybe_unfrack_path('$')('$a/b/c') == '$a/b/c'
    assert maybe_unfrack_path('$')('a') == 'a'
    assert maybe_unfrack_path('$')('/a') == '/a'
    assert maybe_unfrack_path('$')('a/b') == 'a/b'

# Generated at 2022-06-12 20:12:37.399667
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('path') == unfrackpath('path')
    assert unfrack_path(True)('path') == [unfrackpath('path')]
    assert unfrack_path(True)('path' + os.pathsep + 'path2') == [unfrackpath('path'), unfrackpath('path2')]
    assert unfrack_path()('-') == '-'


# Generated at 2022-06-12 20:12:39.407533
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = Mock()
    add_vault_options(parser)
    assert parser.add_argument.call_count == 2


# Generated at 2022-06-12 20:12:39.955316
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    pass



# Generated at 2022-06-12 20:12:40.903609
# Unit test for function add_meta_options
def test_add_meta_options():
  parser = Mock()

# Generated at 2022-06-12 20:12:42.431085
# Unit test for function version
def test_version():
    version('test_prog')

# Generated at 2022-06-12 20:12:43.644225
# Unit test for function add_module_options
def test_add_module_options():
    parser = argparse.ArgumentParser()
    add_module_options(parser)

# Generated at 2022-06-12 20:12:49.502286
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)
    args = parser.parse_args(['-T', '60', '-k', '-u', 'root',
                              '--connection-password-file', 'autotest'])
    assert args.timeout == 60
    assert args.ask_pass is True
    assert args.remote_user == 'root'
    assert args.connection_password_file == 'autotest'

# Generated at 2022-06-12 20:13:10.175558
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = argparse.ArgumentParser()
    add_runas_options(parser)
    parser.print_help()
    sys.exit(0)



# Generated at 2022-06-12 20:13:12.801226
# Unit test for function add_runas_options
def test_add_runas_options():
    def _assert_runas_options(option_list):
        for option in option_list:
            assert option
    parser = argparse.ArgumentParser()
    add_runas_options(parser)
    options = vars(parser.parse_args())
    _assert_runas_options(options.items())



# Generated at 2022-06-12 20:13:18.108342
# Unit test for function add_vault_options
def test_add_vault_options():
    # Just test if there is any exception raise by this function
    # set up
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    # do test
    args = parser.parse_args()

# ==============================================================
# unit test for class SortingHelpFormatter

# Generated at 2022-06-12 20:13:24.279799
# Unit test for function add_runas_prompt_options
def test_add_runas_prompt_options():
    parser = argparse.ArgumentParser()
    add_runas_prompt_options(parser)
    args = parser.parse_args(["--ask-become-pass"])
    assert args.become_ask_pass is True
    args = parser.parse_args(["--become-password-file", "test"])
    assert os.path.abspath(args.become_password_file) == os.path.abspath("test")



# Generated at 2022-06-12 20:13:29.588672
# Unit test for function add_check_options
def test_add_check_options():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.collection_loader import AnsibleCollectionConfig
    config_data = ImmutableDict(
        DEFAULT_VERBOSITY=4,
        DIFF_ALWAYS=True,
        PLAYBOOK_DIR='/test',
        config_version=1,
    )
    ansible_config = AnsibleCollectionConfig(config_data=config_data)
    config_options = {'verbosity': 4, 'diff': True}
    args = argparse.Namespace
    test_parser = add_check_options(args)
    assert test_parser.check == False
    assert test_parser.syntax == False
    assert test_parser.diff == True

# Generated at 2022-06-12 20:13:36.332669
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    # Test if the arguments are prepended to the list
    PLAction = PrependListAction(['-P', '--PL'], 'PL')
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--PL', action=PLAction)
    namespace = parser.parse_args(['-P', 'PL_arg1', '-P', 'PL_arg2'])
    assert namespace.PL == ['PL_arg2', 'PL_arg1']

# Generated at 2022-06-12 20:13:44.863623
# Unit test for function unfrack_path
def test_unfrack_path():
    os.environ['ANSIBLE_CONFIG'] = '/ansible/config'
    os.environ['ANSIBLE_CONFIG_FILE'] = '/ansible/config/file'
    os.environ['ANSIBLE_CONFIG_DIR'] = '/ansible/config/dir'
    testpath = '~/ansible/test'
    pathsep = ':~/ansible:~/ansible/test'
    expected = '/ansible/test/pathsep'

    # Check the first (unfrack_path) function
    assert unfrack_path()(testpath) == os.path.expanduser(testpath)
    # Check the second (unfrack_path_pathsep) function
    assert unfrack_path(pathsep=True)(expected) == [unfrackpath(expected)]

    # Check

# Generated at 2022-06-12 20:13:49.775034
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    cmdline = ['-i', 'myinventory', '-m', 'mymodule']
    parser = create_base_parser(cmdline)
    pargs = parser.parse_args(cmdline)
    assert pargs.inventory == 'myinventory'
    assert pargs.module_name == 'mymodule'



# Generated at 2022-06-12 20:13:55.033822
# Unit test for function add_check_options
def test_add_check_options():

    parser = argparse.ArgumentParser()
    add_check_options(parser)

    with pytest.raises(SystemExit):
        parser.parse_args(['--check'])
    with pytest.raises(SystemExit):
        parser.parse_args(['--syntax-check'])
    with pytest.raises(SystemExit):
        parser.parse_args(['--diff'])

# Generated at 2022-06-12 20:14:02.062819
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = create_base_parser('./ansible', 'test --vault-password-file vault-pass-file')
    add_vault_options(parser)
    args = parser.parse_args('./ansible --vault-password-file vault-pass-file')
    print(vars(args))
    assert vars(args)["vault_password_files"] == 'vault-pass-file'



# Generated at 2022-06-12 20:14:15.963021
# Unit test for function version
def test_version():
    assert version(prog='ansible')
    assert version()



# Generated at 2022-06-12 20:14:20.923716
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    options, _ = parser.parse_known_args(['--force-handlers', '--flush-cache'])
    assert options.force_handlers is True
    assert options.flush_cache is True



# Generated at 2022-06-12 20:14:25.924272
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = Mock()
    add_meta_options(parser)
    parser.add_argument.assert_has_calls([
        call('--flush-cache', dest='flush_cache', action='store_true', help='clear the fact cache for every host in inventory'),
        call('--force-handlers', default=C.DEFAULT_FORCE_HANDLERS, dest='force_handlers', action='store_true', help='run handlers even if a task fails')
    ])



# Generated at 2022-06-12 20:14:27.773876
# Unit test for function version
def test_version():
    assert len(version().splitlines()) == 8
    assert len(version('something').splitlines()) == 9

# Generated at 2022-06-12 20:14:37.103509
# Unit test for function version
def test_version():
    as_ret = version('test-prog')

# Generated at 2022-06-12 20:14:45.264618
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    import argparse
    from ansible import context
    from ansible.cli.helpers import AnsibleOptionsParser
    from ansible.cli.helpers import ensure_value
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_native

    #
    # Our test cases
    #
    def verify(option_strings, dest, nargs, expected, const=None, default=None, type=None,
               choices=None, required=False, help=None, metavar=None):
        parser = argparse.ArgumentParser()
        # argparse._AppendAction is private, so we can not use it in place of PrependListAction.
        # Since PrependListAction is a near clone of argparse._AppendAction, we can test it like so:
        parser.add

# Generated at 2022-06-12 20:14:53.658467
# Unit test for function unfrack_path
def test_unfrack_path():
    import ansible
    expected = [unfrackpath('foo'), unfrackpath('bar')]
    assert unfrack_path(pathsep=True)('foo:bar') == expected
    assert unfrack_path(pathsep=True)('foo:') == expected
    assert unfrack_path(pathsep=True)(':bar') == expected

    assert unfrack_path(pathsep=False)('foo') == unfrackpath('foo')
    assert unfrack_path(pathsep=False)('-') == '-'

#
# Optparse-style Option Parsing
#



# Generated at 2022-06-12 20:14:57.524935
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args(["--force-handlers", "--flush-cache"])
    assert args.force_handlers == True
    assert args.flush_cache == True


# Generated at 2022-06-12 20:15:05.760556
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    from argparse import Namespace
    args = Namespace()
    args.list = []
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action=PrependListAction, default=[])
    parser.parse_args(['--list', 'item1'], namespace=args)
    assert args.list == ['item1']
    parser.parse_args(['--list', 'item2'], namespace=args)
    assert args.list == ['item2', 'item1']
    parser.parse_args(['--list', 'item3', 'item4'], namespace=args)
    assert args.list == ['item3', 'item4', 'item2', 'item1']
    parser.parse_args(['--list', 'item5', 'item6', 'item7'], namespace=args)


# Generated at 2022-06-12 20:15:07.057307
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    result = parser.parse_args(args=['--force-handlers'])
    assert result.force_handlers



# Generated at 2022-06-12 20:15:21.285691
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    a = argparse.HelpFormatter()
    a_actions = a._get_action_name('one')
    assert a_actions == 'one'

    b = SortingHelpFormatter()
    b_actions = b._get_action_name('one')
    assert b_actions == 'one'

#
# Utility functions
#

# Generated at 2022-06-12 20:15:28.279460
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    # Ensure that given new options, the __call__ method prepends the value to the defaults
    # given in the parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', nargs='+', action=PrependListAction)
    parser.add_argument('bar', nargs='+', default='default')
    args = parser.parse_args('-a x y z foo'.split())
    assert args.bar == ['x', 'y', 'z', 'foo']

    # Ensure that when no options are given, the __call__ method prepends the default
    # value
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', nargs='+', action=PrependListAction)
    parser.add_argument('bar', nargs='+', default='default')

# Generated at 2022-06-12 20:15:30.987769
# Unit test for function version
def test_version():
    # Parameter prog is for coverage test.
    assert len(version(prog='Test Coverage')) > 10

#
# Option Parsers
#

# Generated at 2022-06-12 20:15:42.419154
# Unit test for function unfrack_path
def test_unfrack_path():
    """Return a list with unfrackpath corrected value(s)

    :return: list with a single value or the original value
    """
    if 'HOME' in os.environ:
        home = os.environ['HOME']
    else:
        home = '/tmp'

    # Test abspath, expandvars and expanduser with path separator
    result = unfrack_path(pathsep=True)("/tmp:/usr/bin:$HOME/:~")
    assert result == ['/tmp', '/usr/bin', home, home]

    # Test abspath and expandvars, no path separator
    result = unfrack_path(pathsep=False)("/tmp:$HOME")
    assert result == '/tmp'

    # Test only absolute path

# Generated at 2022-06-12 20:15:50.467365
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    action = parser.add_argument('-a', dest='a', action=PrependListAction)
    namespace = argparse.Namespace()
    action(parser, namespace, 'bar', '-a')
    assert namespace.a == ['bar']
    action(parser, namespace, 'baz', '-a')
    assert namespace.a == ['baz', 'bar']
    action(parser, namespace, ['foo', 'qux'], '-a')
    assert namespace.a == ['foo', 'qux', 'baz', 'bar']



# Generated at 2022-06-12 20:15:53.040298
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    import ansible.utils.args as args

    args.get_parser(['--module-search', 'a', '--module-search', 'b'])

#
# OptionParsers
#

# Generated at 2022-06-12 20:15:58.050897
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    namespace = argparse.Namespace()
    action = PrependListAction(option_strings=['--foo'], dest='foo')
    action.__call__(None, namespace, ['bar'], '-f')
    # TODO: add asserts to test result of __call__


# Generated at 2022-06-12 20:16:04.061338
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    # create a parser for testing
    test_parser = argparse.ArgumentParser()
    test_parser.add_argument('-n', action=PrependListAction, required=False, type=int)
    # get an argument namespace
    test_ns = test_parser.parse_args(['-n', '1', '-n', '2'])
    assert test_ns.n == [2, 1], "Unexpected value for argument 'n': {}".format(test_ns.n)
    test_ns = test_parser.parse_args(['-n1', '-n', '2'])
    assert test_ns.n == [2, 1], "Unexpected value for argument 'n': {}".format(test_ns.n)
    test_ns = test_parser.parse_args([])

# Generated at 2022-06-12 20:16:09.622698
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_beacon = '~'
    test_data = [
        ('~/some/path', '~/some/path'),
        ('/some/path', '/some/path')
    ]

    for pre_value, post_value in test_data:
        assert post_value == maybe_unfrack_path(test_beacon)(pre_value)



# Generated at 2022-06-12 20:16:13.405542
# Unit test for function ensure_value
def test_ensure_value():
    class my_namespace:
        pass
    n = my_namespace()
    assert ensure_value(n, "test", [1, 2, 3]) == [1, 2, 3]
    # test if it doesn't overwrite
    assert ensure_value(n, "test", [4, 5]) == [1, 2, 3]



# Generated at 2022-06-12 20:16:25.713694
# Unit test for function ensure_value
def test_ensure_value():
    class fake_namespace(object):
        def __init__(self):
            self.foo = None
            self.bar = None
    fake_ns = fake_namespace()
    assert fake_ns.foo is None
    assert fake_ns.bar is None
    ensure_value(fake_ns, "foo", "qux")
    ensure_value(fake_ns, "bar", "quux")
    assert fake_ns.foo == "qux"
    assert fake_ns.bar == "quux"



# Generated at 2022-06-12 20:16:32.219722
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, 'test_maybe_unfrack_path')

    with open(test_file, 'w') as f:
        f.write('1')

    assert maybe_unfrack_path('@')('@' + test_file) == '@' + unfrackpath(test_file)
    assert maybe_unfrack_path('@')(test_file) == test_file

    os.remove(test_file)



# Generated at 2022-06-12 20:16:39.438666
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/mnt/test')('/mnt/test/tmp/myfile') == '/mnt/test/tmp/myfile'
    assert maybe_unfrack_path('/mnt/test')('/mnt/test/tmp/myfile') == '/mnt/test/tmp/myfile'
    assert maybe_unfrack_path('/mnt/test')('~/tmp/myfile') == '~/tmp/myfile'



# Generated at 2022-06-12 20:16:49.604617
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    def _assert(expected, actual):
        if not expected == actual:
            raise Exception("%s != %s" % (expected, actual))
    unf = maybe_unfrack_path('$')
    _assert('$foo', unf('$foo'))
    _assert('$BAR', unf('$BAR'))
    _assert('$foo/bar', unf('$foo/bar'))
    _assert('$foo/BAR', unf('$foo/BAR'))
    _assert('$foo/bar/baz', unf('$foo/bar/baz'))
    _assert('$/BAR', unf('$/BAR'))
    _assert('$/', unf('$/'))
    _assert('$/foo', unf('$/foo'))



# Generated at 2022-06-12 20:16:57.222146
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    chdirs = [ '~', '/tmp', '', 'foo/bar', '~/foo/bar', '/tmp/foo/bar' ]  # noqa
    lchdirs = [ (x, maybe_unfrack_path('@@')(x)) for x in chdirs ]  # noqa
    dlchdirs = dict(lchdirs)  # noqa
    dlchdirs_keys = dlchdirs.keys()  # noqa
    assert dlchdirs_keys == chdirs, 'keys are same'
    for chdir in chdirs:
        assert dlchdirs[chdir] == '@@' + chdir, 'values are same'

# Generated at 2022-06-12 20:17:07.103988
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/test/data') == '@' + unfrackpath('/test/data')
    assert maybe_unfrack_path('@')('@data') == '@data'
    assert maybe_unfrack_path('@')('@!data') == '@!data'
    assert maybe_unfrack_path('@')('@data1:@data2') == '@data1:@data2'
    assert maybe_unfrack_path('@')('@!data1:@!data2') == '@!data1:@!data2'
    assert maybe_unfrack_path('@')('@/data1:@/data2') == '@' + unfrackpath('/data1') + ':' + '@' + unf

# Generated at 2022-06-12 20:17:11.609135
# Unit test for function version
def test_version():
    '''
    Test version function
    '''
    result = version('ansible-playbook')
    assert 'ansible-playbook [core 2.8.0] (stable-2.8 7251ee5d61)' in result
    assert 'ansible collection location = ' in result
    assert 'python version = 3.6.7 (default, Oct 25 2018, 09:21:04) ' in result
    result = version()
    assert '2.8.0' in result
    assert 'configured module search path = ' in result
    assert 'ansible python module location = ' in result
    assert 'executable location = ' in result
    assert 'python version = ' in result
    assert 'jinja version = ' in result
    assert 'libyaml = ' in result

# Generated at 2022-06-12 20:17:16.123231
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    value = '@test'
    unfracked_value = maybe_unfrack_path('@')(value)
    assert unfracked_value.startswith('@')

    value = '$test'
    unfracked_value = maybe_unfrack_path('$')(value)
    assert not unfracked_value.startswith('@')



# Generated at 2022-06-12 20:17:18.267983
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    tests = [('@/foo/bar', '@' + unfrackpath('/foo/bar')),
             ('@@/foo/bar', '@@/foo/bar')]
    for test in tests:
        assert maybe_unfrack_path('@')(test[0]) == test[1]


#
# Option Groups
#

# Generated at 2022-06-12 20:17:22.039062
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/path/to/file') == '@' + unfrackpath('/path/to/file')
    assert maybe_unfrack_path('@')('/path/to/file') == '/path/to/file'


# Generated at 2022-06-12 20:17:48.360287
# Unit test for function version
def test_version():
    """ verify that version output is as expected """
    base = 'ansible-doc [core %s]' % __version__
    assert version() == "%s\n  config file = %s\n  configured module search path = %s\n  ansible python module location = %s\n  ansible collection location = %s\n  executable location = %s\n  python version = %s\n  jinja version = %s\n  libyaml = %s" % (base, C.CONFIG_FILE, C.DEFAULT_MODULE_PATH, ':'.join(ansible.__path__), ':'.join(C.COLLECTIONS_PATHS), sys.argv[0], ''.join(sys.version.splitlines()), j2_version, HAS_LIBYAML)

# Generated at 2022-06-12 20:17:56.081528
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("/var/lib/awx/projects") == "/var/lib/awx/projects"
    assert unfrack_path()("/var/lib/awx/projects:/var/lib/awx/jobs:/var/lib/awx/licenses") == "/var/lib/awx/projects:/var/lib/awx/jobs:/var/lib/awx/licenses"
    assert unfrack_path(pathsep=True)("/var/lib/awx/projects:/var/lib/awx/jobs:/var/lib/awx/licenses") == ["/var/lib/awx/projects", "/var/lib/awx/jobs", "/var/lib/awx/licenses"]
    assert unfrack_path()("~/.awx/jobs") == "~/.awx/jobs"

# Generated at 2022-06-12 20:18:05.506196
# Unit test for function unfrack_path
def test_unfrack_path():
    assert '/a/b' == unfrack_path()('/a/b')
    assert 'a/b' == unfrack_path()('a/b')
    assert '/a/b' == unfrack_path()('../a/b')
    assert ['/a/b', '/c/d'] == unfrack_path(pathsep=True)('/a/b:/c/d')
    assert ['/a/b', '/c/d'] == unfrack_path(pathsep=True)('../a/b:/c/d')
    assert ['a/b', '/c/d'] == unfrack_path(pathsep=True)('a/b:/c/d')
    assert '-' == unfrack_path()('-')
    assert ['-'] == unfrack_path(pathsep=True)('-')




# Generated at 2022-06-12 20:18:06.352533
# Unit test for function version
def test_version():
    assert "core" in version("ansible-playbook")



# Generated at 2022-06-12 20:18:09.824726
# Unit test for function ensure_value
def test_ensure_value():
    class mock_class(object): pass
    n = mock_class()
    n.test = None
    r = ensure_value(n, 'test', 'new test')
    assert r == n.test == 'new test'
    n.foo = 'bar'
    assert ensure_value(n, 'foo', 'new bar') == n.foo == 'bar'
del ensure_value  # not used outside of this function


#
# Generic OptionParsers
#

# Generated at 2022-06-12 20:18:20.561317
# Unit test for function unfrack_path
def test_unfrack_path():
    # unfrack_path()
    assert 'foo' == unfrack_path()('foo')
    assert 'foo/bar/baz' == unfrack_path()('foo/bar/baz')
    assert '~' == unfrack_path()('~')
    assert os.path.expanduser('~') == unfrack_path()('~')
    assert '~/foo' == unfrack_path()('~/foo')
    assert os.path.expanduser('~/foo') == unfrack_path()('~/foo')
    assert os.path.expanduser('~/foo') == unfrack_path()('$HOME/foo')

    # unfrack_path(pathsep=True)
    assert ['foo'] == unfrack_path(pathsep=True)('foo')

# Generated at 2022-06-12 20:18:28.126261
# Unit test for function unfrack_path
def test_unfrack_path():
    from ansible.config.manager import ConfigManager
    config_manager = ConfigManager()
    config = config_manager.get_config_data()
    pathval = '-/some/path'
    assert unfrack_path(pathsep=False)(pathval) == config['DEFAULT_ROLES_PATH']
    pathval = '-/some/path:/other/path'
    assert unfrack_path(pathsep=True)(pathval) == [config['DEFAULT_ROLES_PATH'], '/other/path']


# Generated at 2022-06-12 20:18:33.526321
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # pylint: disable=anomalous-backslash-in-string
    assert maybe_unfrack_path('@')('@foo/bar') == '@/etc/ansible/foo/bar'
    assert maybe_unfrack_path('@')('foo/bar') == 'foo/bar'
    assert maybe_unfrack_path('@')('@foo/bar/baz') == '@/etc/ansible/foo/bar/baz'



# Generated at 2022-06-12 20:18:37.397059
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('-') == '-'
    assert unfrack_path()('/foo') == '/foo'
    assert unfrack_path()('/foo/bar') == '/foo/bar'
    assert unfrack_path(pathsep=True)('/foo' + os.pathsep + '/bar') == ['/foo', '/bar']



# Generated at 2022-06-12 20:18:45.757261
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--foo', dest='foo')
    parser.add_argument('--bar', dest='bar')
    # SortingHelpFormatter sorts arguments by option_strings, which is
    # ['--foo'] in the case of foo and ['--bar'] in the case of bar, so
    # --bar is displayed before --foo.
    assert parser.format_help().splitlines() == [
        'usage: None [-h] [--bar BAR] [--foo FOO]',
        '',
        'optional arguments:',
        '  -h, --help   show this help message and exit',
        '  --bar BAR',
        '  --foo FOO',
    ]


# Generated at 2022-06-12 20:19:23.945335
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/usr/share/ansible/plugins') == '/usr/share/ansible/plugins'
    assert unfrack_path()('/usr/share/ansible/plugins:/usr/lib64/python2.7/site-packages/ansible/plugins') == ['/usr/share/ansible/plugins', '/usr/lib64/python2.7/site-packages/ansible/plugins']



# Generated at 2022-06-12 20:19:28.367030
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test for path beginning with @~
    assert maybe_unfrack_path('@~')('@~/username') == '@~/home/username'
    assert maybe_unfrack_path('@~')('@/mypath') == '@/mypath'



# Generated at 2022-06-12 20:19:31.379901
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_values = [
        ("@foo", "@foo"),
        ("@bar", "@" + unfrackpath("bar"))
    ]
    for value, expected in test_values:
        assert maybe_unfrack_path("@")(value) == expected


# Generated at 2022-06-12 20:19:34.467859
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/etc/ansible/ansible.cfg') == '@' + unfrackpath('/etc/ansible/ansible.cfg')



# Generated at 2022-06-12 20:19:38.017533
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter,
                                     add_help=False)
    # pylint: disable=unused-variable
    (options, args) = parser.parse_known_args(['--help'])

#
# Shared
#

# Generated at 2022-06-12 20:19:40.159949
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@tmp') == '@/tmp'



# Generated at 2022-06-12 20:19:44.912683
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():

    #
    # Create a SortingHelpFormatter
    #
    parser = argparse.ArgumentParser()
    parser.add_argument("-a")
    parser.add_argument("-b")
    parser.add_argument("-c")

    SortingHelpFormatter(parser)



# Generated at 2022-06-12 20:19:50.010040
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("@")("@/foo") == "@%s/foo" % unfrackpath(".")
    assert maybe_unfrack_path("@")("foo") == "foo"
    assert maybe_unfrack_path("&")("&/foo") == "&%s/foo" % unfrackpath(".")
    assert maybe_unfrack_path("&")("foo") == "foo"
    assert maybe_unfrack_path("@")("@@/foo") == "@@/foo"
    assert maybe_unfrack_path("@")("&&/foo") == "&&/foo"


# Generated at 2022-06-12 20:19:55.937268
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    tmp = unfrackpath('~')
    value = maybe_unfrack_path('~')('~/foo/bar')
    assert value == tmp + '/foo/bar'
    value = maybe_unfrack_path('~')('~foo/bar')
    assert value == '~foo/bar'
    value = maybe_unfrack_path('~')('/foo/bar')
    assert value == '/foo/bar'



# Generated at 2022-06-12 20:19:59.089355
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()("") == ""
    assert unfrack_path()(".") == os.getcwd()
    assert unfrack_path()("~") == os.path.expanduser("~")


# TODO: fix this to explicitly test the pathsep parameter
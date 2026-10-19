

# Generated at 2022-06-12 20:12:15.228541
# Unit test for constructor of class PrependListAction
def test_PrependListAction():
    """This function checks if all the arguments of the class
        PrependListAction is passed on to the superclass constructor.
    """
    super_getattribute = super(PrependListAction, PrependListAction).__init__
    # Note that we are checking for the existence of the arguments,
    # but not for there type or value, as this might change in the future.
    def _check_arguments(test_case, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(super_getattribute.__call__, key):
                msg = "Attribute {attr} is not present in the class."
                msg = msg.format(attr=key)
                test_case.fail(msg)

# Generated at 2022-06-12 20:12:18.481975
# Unit test for function add_output_options
def test_add_output_options():
    parser=argparse.ArgumentParser()
    add_output_options(parser)
    options,args=parser.parse_known_args()
    assert(options.one_line==False)
    assert(options.tree==None)

# Generated at 2022-06-12 20:12:23.140879
# Unit test for function unfrack_path
def test_unfrack_path():
    test_directory = '~/test_directory'
    real_path = os.path.expanduser(test_directory)
    assert real_path == unfrack_path()(test_directory)
    test_path = '$HOME/test_directory'
    assert real_path == unfrack_path()(test_path)


# Generated at 2022-06-12 20:12:30.813445
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    args = parser.parse_args(args=['--check'])
    assert args.check
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    args = parser.parse_args(args=['--syntax-check'])
    assert args.syntax
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    args = parser.parse_args(args=['--diff'])
    assert args.diff



# Generated at 2022-06-12 20:12:40.324568
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(prog='ansible-doc')
    add_connect_options(parser)
    sys.argv = ['ansible-doc', '-k', '-v', '-u', 'johndoe', '-c', 'smart',
                '--connection-password-file', 'changeme', '--private-key', '~/.ssh/id_rsa']
    options = parser.parse_args()
    assert options.private_key_file == os.path.expanduser('~/.ssh/id_rsa')
    assert options.remote_user == 'johndoe'
    assert options.connection == 'smart'
    assert options.connection_password_file == 'changeme'
    assert options.verbosity == 1
    assert options.ask_pass == True


# Generated at 2022-06-12 20:12:43.755927
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    add_fork_options(parser)
    opts = parser.parse_args(['--forks', '4'])
    assert opts.forks == 4
    opts = parser.parse_args(['--forks', '0'])
    assert opts.forks == 0
# Test case for Base arg parse.

# Generated at 2022-06-12 20:12:47.712913
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter, description="optional app description",
                                     epilog="optional app epilog")
    opts = add_connect_options(parser)
    opts.print_help()



# Generated at 2022-06-12 20:12:51.823721
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser(prog='test_add_vault_options')
    add_vault_options(parser)
    options = parser.parse_args(['--vault-id', 'testid', '--ask-vault-password',
            '--vault-password-file', 'testfile'])
    assert isinstance(options, argparse.Namespace)
    assert options.vault_ids == ['testid']
    assert options.ask_vault_pass is True
    assert options.vault_password_files == ['testfile']

# Unit tests for the main() function in the module.

# Generated at 2022-06-12 20:12:54.864428
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser(prog='add_meta_options')
    add_meta_options(parser)
    args = parser.parse_args(['--force-handlers', '--flush-cache'])
    assert args.force_handlers == True
    assert args.flush_cache == True


# Generated at 2022-06-12 20:13:01.600157
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser=argparse.ArgumentParser()
    parser.add_argument('--foo', action=PrependListAction, default=['bar'])
    args = parser.parse_args([])
    assert args.foo == ['bar']
    args = parser.parse_args(['--foo', 'baz'])
    assert args.foo == ['baz', 'bar']
    args = parser.parse_args(['--foo', 'baz', '--foo', 'qux'])
    assert args.foo == ['qux', 'baz', 'bar']


# Generated at 2022-06-12 20:13:12.757687
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """
    Test case for 'maybe_unfrack_path' function
    """
    assert maybe_unfrack_path('@')('@/some/relative/path') == '@%s/some/relative/path' % unfrackpath('')
    assert maybe_unfrack_path('@')('some/other/path') == 'some/other/path'
    assert maybe_unfrack_path('-')('some/other/path') == 'some/other/path'
    assert maybe_unfrack_path('-')('-') == '-'
    assert maybe_unfrack_path('@')('@') == '@'



# Generated at 2022-06-12 20:13:16.597414
# Unit test for function add_fork_options
def test_add_fork_options():
    parser = argparse.ArgumentParser()
    add_fork_options(parser)
    args = parser.parse_args(['-f', '20'])
    assert args.forks == 20


# Generated at 2022-06-12 20:13:24.300978
# Unit test for function unfrack_path
def test_unfrack_path():
    # By default, split the string into a list of items.
    assert unfrack_path(False)('foo:bar') == ['foo', 'bar']
    # An empty string returns an empty list
    assert unfrack_path(False)('') == []
    # A dash is not a valid directory
    assert unfrack_path(False)('-') == '-'
    # A single pathname is converted into a list
    assert unfrack_path(False)('foo') == ['foo']
    # Split the string into a list of items
    assert unfrack_path(True)('foo:bar') == ['foo', 'bar']
    # An empty string returns an empty list
    assert unfrack_path(True)('') == []
    # A dash is not a valid directory
    assert unfrack_path(True)('-') == '-'
    #

# Generated at 2022-06-12 20:13:28.669350
# Unit test for function unfrack_path
def test_unfrack_path():
    candidate = unfrack_path()
    assert candidate('/tmp/fake_path') == '/tmp/fake_path'
    assert candidate('../fake_path') == '../fake_path'

    candidate = unfrack_path(pathsep=True)
    assert candidate('/tmp/fake_path:/tmp/another_fake_path') == ['/tmp/fake_path', '/tmp/another_fake_path']
    assert candidate('../fake_path:/tmp/fake_path') == ['../fake_path', '/tmp/fake_path']


# Generated at 2022-06-12 20:13:35.353338
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """
    >>> test_maybe_unfrack_path()
    """
    path1 = '~/ansible'
    path2 = '~/ansible/ansible.cfg'

    assert(maybe_unfrack_path(path1)(path1) == path1)
    assert(maybe_unfrack_path(path1)(path2) == os.path.join(path1, 'ansible.cfg'))

#
# Options for the CLI
#

# Generated at 2022-06-12 20:13:38.857314
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/path/to/file') == '/path/to/file'
    assert unfrack_path(pathsep=True)('/path/to/dir1:/path/to/dir2') == ['/path/to/dir1', '/path/to/dir2']


#
# Custom Option parsers
#

# Generated at 2022-06-12 20:13:46.216265
# Unit test for function version

# Generated at 2022-06-12 20:13:51.899238
# Unit test for function unfrack_path
def test_unfrack_path():

    check = unfrack_path()
    assert check('-') == '-'
    assert check('/usr/bin') == '/usr/bin'

    check = unfrack_path(pathsep=True)
    assert check('-') == ['-']
    assert check('/usr/bin:/usr/local/bin') == ['/usr/bin', '/usr/local/bin']



# Generated at 2022-06-12 20:13:59.220080
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion, nargs=0, help=version_help)
    add_runas_options(parser)
    arguments = parser.parse_args()
    check_arguments = set(arguments.__dict__.keys()) == {'verbosity', 'version', 'become', 'become_method', 'become_user', 'ask_pass', 'ask_become_pass', 'ask_become_pass_prompt'}
    assert check_arguments

# Generated at 2022-06-12 20:14:01.473519
# Unit test for function version
def test_version():
    """ test version output """
    from ansible.utils.parse_version import parse_version
    # if version info is updated, please test for it
    assert parse_version(version()) >= parse_version(__version__)

# Generated at 2022-06-12 20:14:10.384335
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
   assert maybe_unfrack_path('@')('@/a/b/c') == '@' + unfrackpath('/a/b/c')
   assert maybe_unfrack_path('@')('@@/a/b/c') == '@@/a/b/c'


# Generated at 2022-06-12 20:14:17.778147
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    t = maybe_unfrack_path('@')
    assert t('@/some/regular/file/path') == '@' + unfrackpath('/some/regular/file/path')
    assert t('@@/some/regular/file/path') == '@@/some/regular/file/path'
    assert t('@@@/some/regular/file/path') == '@@@/some/regular/file/path'



# Generated at 2022-06-12 20:14:22.209534
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    options = parser.parse_args(['-i', 'hostfile.ini', '--list-hosts', '-l', 'webservers', '--list-hosts'])
    assert options.inventory == 'hostfile.ini'
    assert options.listhosts
    assert options.subset == 'webservers'


# Generated at 2022-06-12 20:14:26.847881
# Unit test for function add_inventory_options
def test_add_inventory_options():
    import argparse
    test_arg = ['--inventory', './inventory', '-l', '127.0.0.1', '--list-hosts']
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(test_arg)
    assert args.inventory == ['./inventory']
    assert args.subset == '127.0.0.1'
    assert args.listhosts == True



# Generated at 2022-06-12 20:14:32.388175
# Unit test for function add_inventory_options
def test_add_inventory_options():
    """
    Test function add_inventory_options
    """
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    options = parser.parse_args(['-i', 'inventory', '--list-hosts', '-l', 'localhost'])
    assert options.inventory[0] == 'inventory'
    assert options.listhosts is True
    assert options.subset == 'localhost'



# Generated at 2022-06-12 20:14:39.080338
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser(prog='test_arg_parsing', formatter_class=SortingHelpFormatter)
    add_inventory_options(parser)
    args = parser.parse_args(['-i', 'dev', '--list-hosts'])
    assert args.inventory == ['dev']
    assert args.listhosts == True
    args = parser.parse_args(['-i', 'dev', '-l', 'env-dev'])
    assert args.inventory == ['dev']
    assert args.subset == 'env-dev'


# Generated at 2022-06-12 20:14:47.380034
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    namespace = argparse.Namespace()
    values = ['namespace', 'values']
    option_string = 'option_string'

    prepend_list_action = PrependListAction(option_strings='option_strings',
                                            dest='dest', default=['default'],
                                            help='help')
    prepend_list_action(parser='parser', namespace=namespace, values=values,
                            option_string=option_string)
    assert namespace.dest == ['namespace', 'values', 'default']


# Generated at 2022-06-12 20:14:55.910333
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    # set help formatter
    parser.formatter_class = SortingHelpFormatter
    parser.add_argument("-b", help="b help")
    parser.add_argument("-a", help="a help")
    help_string = parser.format_help()
    assert(help_string == 'usage: None [-h] [-b B] [-a A]\n\noptional arguments:\n  -h, --help  show this help message and exit\n  -b B        b help\n  -a A        a help\n')



# Generated at 2022-06-12 20:14:56.763498
# Unit test for function version
def test_version():
    assert version() is not None



# Generated at 2022-06-12 20:14:57.892002
# Unit test for function add_subset_options
def test_add_subset_options():
    pass



# Generated at 2022-06-12 20:15:17.934808
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    args = parser.parse_args()
    assert args.tags == ['all'], "default tag 'all' was not set"
    assert args.skip_tags == [], "skip tags was not set to empty list"
    args = parser.parse_args(['-t', 'foo'])
    assert args.tags == ['foo'], "single tag was not set"
    args = parser.parse_args(['--tags', 'foo', '--tags', 'bar'])
    assert args.tags == ['foo', 'bar'], "multiple tags were not set"



# Generated at 2022-06-12 20:15:22.429124
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser(prog='playbook')
    add_subset_options(parser)
    parser.parse_args(['-t', 'tag1', '-t', 'tag2'])
    parser.parse_args(['--skip-tags', 'skip1', '--skip-tags', 'skip2'])
    with pytest.raises(SystemExit):
        parser.parse_args(['--tags', 'tag1', '--tags', 'tag2', '-t', 'tag3'])


# Generated at 2022-06-12 20:15:25.247345
# Unit test for function version
def test_version():
    """Test the version function works as expected"""
    # No gitinfo when running from an egg
    if getattr(sys, 'frozen', False):
        assert version() is not None
    else:
        assert version().endswith(' (detached HEAD) last updated')

# Generated at 2022-06-12 20:15:37.082120
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/usr/bin') == '/usr/bin'
    assert unfrack_path()('my_plugin.py') == 'my_plugin.py'
    assert unfrack_path()('/path/to/ansible/plugins/my_plugin.py') == '/path/to/ansible/plugins/my_plugin.py'
    assert unfrack_path()('/path/to/ansible/plugins/my_plugin.py') == C.DEFAULT_MODULE_PATH[-1] + '/my_plugin.py'
    assert unfrack_path()('my_plugin.py') == C.DEFAULT_MODULE_PATH[-1] + '/my_plugin.py'

# Generated at 2022-06-12 20:15:42.338854
# Unit test for function ensure_value
def test_ensure_value():
    namespace = argparse.Namespace()
    ensure_value(namespace, 'foo', [])
    assert getattr(namespace, 'foo') == []
    ensure_value(namespace, 'foo', [1,2,3])
    assert getattr(namespace, 'foo') == [1,2,3]


#
# Parser functions
#

# Generated at 2022-06-12 20:15:47.997685
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = OptionParser()
    add_subset_options(parser)
    options, args = parser.parse_known_args(['-t', 'foo', '--tags', 'bar', '--skip-tags', 'foo', '--skip-tags', 'bar'])
    assert options.tags == ['foo', 'bar']
    assert options.skip_tags == ['foo', 'bar']



# Generated at 2022-06-12 20:15:55.946492
# Unit test for function add_subset_options
def test_add_subset_options():
    parser = argparse.ArgumentParser()
    add_subset_options(parser)
    options = parser.parse_args()
    assert options.tags == ['all']
    assert options.skip_tags == []
    options = parser.parse_args(['--tags', 'tag1', '--skip-tags', 'tag2'])
    assert options.tags == ['tag1']
    assert options.skip_tags == ['tag2']
    options = parser.parse_args(['--tags', 'tag1,tag2', '--skip-tags', 'tag3,tag4'])
    assert options.tags == ['tag1', 'tag2']
    assert options.skip_tags == ['tag3', 'tag4']



# Generated at 2022-06-12 20:16:02.975112
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    tests = [
        # Test values, beacon, expected output
        ['/some/path/here', '@DEFAULT', '/some/path/here'],
        ['@HOME/some/path/here', '@HOME', '@HOME/some/path/here'],
        ['@HOME/some/path/here', '@DEFAULT', '@HOME/some/path/here'],
        ['@DEFAULT/some/path/here', '@DEFAULT', '@DEFAULT/some/path/here'],
        ['@DEFAULT/some/path/here', '@HOME', '@DEFAULT/some/path/here'],
    ]

    for test in tests:
        value, beacon, expected = test
        result = maybe_unfrack_path(beacon)(value)
        assert result == expected


# Generated at 2022-06-12 20:16:06.933878
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test string with no beacon
    no_beacon = 'test'
    assert maybe_unfrack_path(None)(no_beacon) == no_beacon
    no_beacon = 'test'
    assert maybe_unfrack_path(False)(no_beacon) == no_beacon
    no_beacon = ''
    assert maybe_unfrack_path('')(no_beacon) == no_beacon
    no_beacon = '/test'
    assert maybe_unfrack_path(None)(no_beacon) == no_beacon
    no_beacon = '/test'
    assert maybe_unfrack_path(False)(no_beacon) == no_beacon
    no_beacon = '/test'

# Generated at 2022-06-12 20:16:15.642716
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/var/lib')('/var/lib/foo') == '/var/lib/foo'
    assert maybe_unfrack_path('/var/lib')('/var/lib/foo/../bar') == '/var/lib/bar'
    assert maybe_unfrack_path('/var/lib')('/foo/bar') == '/foo/bar'



# Generated at 2022-06-12 20:16:28.989273
# Unit test for function unfrack_path
def test_unfrack_path():
    # Test unfrack_path when pathsep is False
    result = unfrack_path(pathsep=False)('../ansible')
    assert result == os.getcwd() + '/../ansible'

    # Test unfrack_path when pathsep is True
    result = unfrack_path(pathsep=True)('../ansible')
    assert result == [os.getcwd() + '/../ansible']

    # Test unfrack_path when value is -
    result = unfrack_path(pathsep=False)('-')
    assert result == '-'



# Generated at 2022-06-12 20:16:31.697382
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('/foo/bar') == unfrackpath('/foo/bar')

# Generated at 2022-06-12 20:16:34.970746
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    res = parser.parse_args(['-v'])
    assert res.v == True
    assert res.version == True


# Generated at 2022-06-12 20:16:42.207141
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    # Create an instance of class PrependListAction for testing
    prepend_list_action = PrependListAction(option_strings=[], dest=None, nargs=None, const=None, default=None, type=None,
                                            choices=None, required=False, help=None, metavar=None)
    # Create a namespace object to be used as the namespace object of method __call__ of class PrependListAction
    namespace = argparse.Namespace(prepend_list_action)
    # Create a list of values to be used as the values of method __call__ of class PrependListAction
    values = ['a', 'b']
    # Execute method __call__ of class PrependListAction
    prepend_list_action.__call__(parser=None, namespace=namespace, values=values, option_string=None)

# Generated at 2022-06-12 20:16:44.219901
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
  parser = SortingHelpFormatter()
  assert isinstance(parser, SortingHelpFormatter)


# Generated at 2022-06-12 20:16:50.794332
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from io import StringIO
    from unittest import mock

    option_string = None
    test_args = ['--version']
    with mock.patch('ansible.cli.CLI.parse') as mock_parse:
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            with mock.patch('sys.stderr', new=StringIO()) as fake_err:
                real_version = version('').split('\n')[0] # because version outputs many lines
                test_version = AnsibleVersion(self=None, option_strings=None)(
                    parser=None, namespace=None, values=None, option_string=None)
                print(test_version)
                mock_parse.assert_called_once_with(test_args)



# Generated at 2022-06-12 20:16:57.011382
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test + prefix
    assert maybe_unfrack_path('+')('+/var/lib') == '+/var/lib'
    assert maybe_unfrack_path('+')('+/var/lib/../lib') == '+/var/lib'
    assert maybe_unfrack_path('+')('+/tmp/..') == '+/tmp/..'
    # Test - prefix
    assert maybe_unfrack_path('-')('-/var/lib') == '-/var/lib'
    assert maybe_unfrack_path('-')('-/var/lib/../lib') == '-/var/lib'
    assert maybe_unfrack_path('-')('-/tmp/..') == '-/tmp/..'
    # Test both + and - prefix
    assert maybe_

# Generated at 2022-06-12 20:17:06.547044
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter, add_help=False)
    parser.add_argument("-h", "--help", action='help')
    parser.add_argument("-a", action="store_true")
    parser.add_argument("-z", action="store_true")
    options, args = parser.parse_known_args(args=[])
    assert options.a == False
    assert options.z == False
    assert parser.format_help() == """usage: argparse.py [-h] [-a] [-z]

optional arguments:
  -h, --help  show this help message and exit
  -a
  -z
"""


#
# Wrapper for OptionParser for AnsibleCli
#

# Generated at 2022-06-12 20:17:12.847957
# Unit test for function unfrack_path
def test_unfrack_path():
    if sys.platform == 'win32':
        expected = ['C:\\Python35', 'C:\\Windows']
        assert ['C:/Python35', 'C:/Windows'] == unfrack_path()(os.pathsep.join(expected))
        assert 'C:/Windows' == unfrack_path(True)(os.pathsep.join(expected))
    else:
        expected = ['/etc/ansible', '/usr', '/usr/share/ansible']
        assert ['/etc/ansible', '/usr', '/usr/share/ansible'] == unfrack_path()(os.pathsep.join(expected))
        assert '/etc/ansible' == unfrack_path(True)(os.pathsep.join(expected))



# Generated at 2022-06-12 20:17:23.207214
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    arguments = ' -vvvv -vvvvv -v'
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='append', dest='verbosity',
                        default=[], help="Increase verbosity")
    parser.add_argument('-v', '--verbose', action=PrependListAction, dest='verbosity',
                        default=[], help="Increase verbosity")
    args = parser.parse_args(arguments.split())
    assert args.verbosity == [5, 4, 3, 3, 2]
    arguments = ' -vvvv -vvvvv -v'
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='append', dest='verbosity',
                        default=[], help="Increase verbosity")
    args

# Generated at 2022-06-12 20:17:45.206969
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=True)('foo:bar:baz') == [u'foo', 'bar', 'baz']
    assert unfrack_path()('foo:bar:baz') == u'foo:bar:baz'
    assert unfrack_path()('-') == '-'


# Generated at 2022-06-12 20:17:52.862715
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_vectors = [
        ['abc', 'abc'],
        ['/abc', '/abc'],
        ['@abc', '@abc'],
        ['~/abc', '~/abc'],
        ['/@abc', '/@abc'],
        ['/~/abc', '/~/abc'],
        ['/~/abc', '/~/abc'],
        ['/@~/abc', '/@~/abc'],
        ['@~/abc', '@~/abc'],
    ]
    for v in test_vectors:
        assert maybe_unfrack_path('@')(v[0]) == v[1]
        assert maybe_unfrack_path('~')(v[0]) == v[1]



# Generated at 2022-06-12 20:18:03.293732
# Unit test for function unfrack_path
def test_unfrack_path():
    assert [] == unfrack_path(True)('')
    assert ['foo'] == unfrack_path(True)('foo')
    assert ['foo'] == unfrack_path(True)('foo')
    assert ['foo'] == unfrack_path(True)('foo:')
    assert ['foo'] == unfrack_path(True)(':foo')
    assert [] == unfrack_path(True)(':')
    assert [] == unfrack_path(True)('')
    assert ['foo', 'bar'] == unfrack_path(True)('foo:bar')
    assert ['bar', 'foo'] == unfrack_path(True)('bar:foo')
    assert ['foo', 'bar', 'baz'] == unfrack_path(True)('foo:bar:baz')
    assert ['bar', 'baz', 'foo'] == unfrack

# Generated at 2022-06-12 20:18:04.506885
# Unit test for function unfrack_path
def test_unfrack_path():
    test_path = os.path.abspath('/tmp')
    returned_path = unfrack_path()(test_path)
    assert len(test_path) == len(returned_path)



# Generated at 2022-06-12 20:18:07.268806
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--option', dest='option', action=PrependListAction)

    ns = parser.parse_args(['--option', 'foo', '--option', 'bar'])

    assert(['foo', 'bar'] == ns.option)



# Generated at 2022-06-12 20:18:15.266120
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--c')
    parser.add_argument('--a')
    parser.add_argument('--b')
    assert parser.format_help() == """usage: [--a A] [--b B] [--c C]

optional arguments:
  --a A
  --b B
  --c C
"""


# Generated at 2022-06-12 20:18:19.945722
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('.') == os.getcwd()
    assert unfrack_path()('~/.ansible/tmp') == os.path.expanduser('~/.ansible/tmp')
    assert unfrack_path(True)('~/.ansible/tmp:/tmp') == [os.path.expanduser('~/.ansible/tmp'), '/tmp']



# Generated at 2022-06-12 20:18:22.392182
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$/test') == '$/test'
    assert maybe_unfrack_path('$')('$test') == '$/test'



# Generated at 2022-06-12 20:18:25.660577
# Unit test for function version
def test_version():
    result = version('python version')
    assert 'python version' in result
    result = version()
    assert 'python version' not in result

#
# Custom actions for Options
#

# Generated at 2022-06-12 20:18:32.733489
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    ns = argparse.Namespace()
    const = ['const', 'const2']
    action = PrependListAction('--test', 'dest', const=const)
    action(None, ns, None)
    assert ns.dest == const, ns.dest
    action = PrependListAction('--test', 'dest')
    action(None, ns, [1, 2])
    assert ns.dest == [1, 2], ns.dest
    action(None, ns, [3, 4])
    assert ns.dest == [1, 2, 3, 4], ns.dest


#
# Generic Helpers
#

# Generated at 2022-06-12 20:19:00.261037
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    frack = '~/../'
    assert maybe_unfrack_path("/")(frack) == frack
    assert maybe_unfrack_path("/")("/{}".format(frack)) == "/{}".format(unfrackpath(frack))



# Generated at 2022-06-12 20:19:06.903403
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(pathsep=True)('~/foo:~/bar') == [os.path.expanduser('~/foo'), os.path.expanduser('~/bar')]
    assert unfrack_path(pathsep=True)('~/foo:/bar') == [os.path.expanduser('~/foo'), '/bar']
    assert unfrack_path(pathsep=True)('/-') == ['-', '']
    assert unfrack_path(pathsep=True)('/-:~/bar') == ['-', os.path.expanduser('~/bar')]
    assert unfrack_path(pathsep=True)('/path/to/playbook') == ['/path/to/playbook']

# Generated at 2022-06-12 20:19:13.110250
# Unit test for function unfrack_path
def test_unfrack_path():
    try:
        from nose.tools import assert_equal, assert_list_equal
    except ImportError:
        return # skip these tests if assert_equal or assert_list_equal can't be imported

    t = unfrack_path()
    assert_equal(t('/tmp/fred'), '/tmp/fred')
    assert_equal(t('frob'), unfrackpath('frob'))

    # pathsep=True
    p = unfrack_path(True)
    assert_list_equal(p('/tmp/fred:/tmp'), [unfrackpath('/tmp/fred'), unfrackpath('/tmp')])

#
# Memoization (container) class.
#

# Generated at 2022-06-12 20:19:23.160330
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
   assert maybe_unfrack_path('~')('~/tmp/hello') == '~/tmp/hello'
   assert maybe_unfrack_path('~')('~user1/tmp/hello') == '~user1/tmp/hello'
   assert maybe_unfrack_path('@')('@/tmp/hello') == '@/tmp/hello'
   assert maybe_unfrack_path('@')('@user1/tmp/hello') == '@user1/tmp/hello'
   assert maybe_unfrack_path('~')('~/tmp/hello') == '~/tmp/hello'
   assert maybe_unfrack_path('~')('~user1/tmp/hello') == '~user1/tmp/hello'


# Generated at 2022-06-12 20:19:28.140708
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/test/path') == '@/test/path'
    assert maybe_unfrack_path('@')('@test/path') == '@test/path'
    assert maybe_unfrack_path('@')('test/path') == 'test/path'



# Generated at 2022-06-12 20:19:31.208281
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():

    ret = maybe_unfrack_path(beacon="@")("@/some/path")
    assert (ret == "@" + unfrackpath("/some/path"))
    assert maybe_unfrack_path(beacon="@")("@") == "@"



# Generated at 2022-06-12 20:19:41.488440
# Unit test for function unfrack_path
def test_unfrack_path():
    try:
        import __builtin__ as builtins
    except ImportError:
        # Python 3+
        import builtins
    real_open = builtins.open

    expected_path = '/my/file'
    #os.environ['ANSIBLE_ROLES_PATH'] = '/my/path'

    def my_open(filename, *args, **kwargs):
        if filename == expected_path:
            return real_open(filename, *args, **kwargs)
        raise Exception("Unexpected file open: %s" % filename)

    def test_unfrackpath_success(pathsep):
        builtins.open = my_open
        assert unfrack_path(pathsep)(expected_path) == expected_path
        builtins.open = real_open

    # Test the pathsep version, and the

# Generated at 2022-06-12 20:19:46.973172
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    dest = 'dest'
    values = ['first', 'second']
    option_string = '--dest'
    parser.add_argument(*option_string.split(), action=PrependListAction, dest=dest, nargs=2)
    parser.parse_args([option_string] + values)
    assert parser.parse_args([option_string] + values).dest == values


#
# Utility methods
#

# Generated at 2022-06-12 20:19:55.828259
# Unit test for function unfrack_path
def test_unfrack_path():
    tf = '/tmp/foo'
    assert unfrack_path(pathsep=False)('~/foo') == os.path.expanduser('~/foo')
    assert unfrack_path(pathsep=False)('/foo') == '/foo'
    assert unfrack_path(pathsep=False)('$HOME/foo') == os.path.expanduser('~/foo')
    assert unfrack_path(pathsep=False)('$HOME/foo/bar') == os.path.expanduser('~/foo/bar')
    assert unfrack_path(pathsep=False)('${HOME}/foo') == os.path.expanduser('~/foo')

# Generated at 2022-06-12 20:20:00.334104
# Unit test for function unfrack_path
def test_unfrack_path():
    expanded = '~/.ansible/tmp/ansible-tmp-127.0.0.1.8022-1607990579.67-146669964979275/'
    this_dir = os.path.dirname(os.path.realpath(__file__))
    assert unfrack_path()(expanded) == expanded
    assert unfrack_path()('-') == '-'


# Generated at 2022-06-12 20:21:05.268883
# Unit test for function unfrack_path
def test_unfrack_path():
    '''unit test for function unfrack_path'''
    assert unfrack_path(False)('/dev/null') == unfrackpath('/dev/null')


#
# Base Parser class, with some common options.
#

# Generated at 2022-06-12 20:21:09.560785
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/etc/ansible/ansible.cfg') == '@/etc/ansible/ansible.cfg'
    assert maybe_unfrack_path('@')('@./test/testdir/testfile') == '@./test/testdir/testfile'


# Generated at 2022-06-12 20:21:18.276378
# Unit test for function unfrack_path
def test_unfrack_path():
    test_path_true = []
    test_path_true.append(unfrack_path(pathsep=True)('~/ansible'))
    test_path_true.append(unfrack_path(pathsep=True)('.'))
    test_path_true.append(unfrack_path(pathsep=True)('./'))
    test_path_true.append(unfrack_path(pathsep=True)('../'))
    test_path_true.append(unfrack_path(pathsep=True)('~/ansible;'))
    test_path_true.append(unfrack_path(pathsep=True)('~/ansible:~/'))

# Generated at 2022-06-12 20:21:26.585996
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    from ansible.utils.shlex import shlex_split
    from ansible.config.manager import ConfigManager
    parser = ConfigManager.create_parser(usage='', description='')
    parser.add_argument('--foo', action=PrependListAction, default=[])
    parser.add_argument('bar_baz', type='path')
    parser.add_argument('-b', action=PrependListAction)
    ns = parser.parse_args(['bar', '-b', 'a', '-b', 'b'])
    assert ns.foo == []
    assert ns.bar_baz == 'bar'
    assert ns.b == ['a', 'b']
    ns = parser.parse_args(['bar', '--foo', 'a', '--foo', 'b'])

# Generated at 2022-06-12 20:21:29.350035
# Unit test for method __call__ of class PrependListAction
def test_PrependListAction___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action=PrependListAction, default=[])
    args = parser.parse_args('--test foo'.split())
    assert args.test == ['foo']



# Generated at 2022-06-12 20:21:36.145743
# Unit test for function unfrack_path
def test_unfrack_path():
    # test invalid path such as -1, 0 and True
    invalid_paths = [-1, 0, True]
    for invalid_path in invalid_paths:
        try:
            unfrack_path(True)(invalid_path)
        except SystemExit as e:
            assert e.code == 1
        else:
            assert False

    # test path that exists
    exists_path = sys.argv[0]
    assert unfrack_path(True)(exists_path) == [os.path.abspath(sys.argv[0])]

    # test path that doesn't exists
    not_exists_path = '/not_exists_path'
    assert unfrack_path(True)(not_exists_path) == [not_exists_path]

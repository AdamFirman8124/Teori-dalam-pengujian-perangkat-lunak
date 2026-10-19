

# Generated at 2022-06-12 20:12:08.651178
# Unit test for function add_inventory_options
def test_add_inventory_options():
    parser = argparse.ArgumentParser()
    add_inventory_options(parser)
    args = parser.parse_args(args=[
        '-i', 'foo',
        '-i', 'bar',
        '-i', 'baz',
        '-i', 'bam,'
        '-l', 'blip'
    ])
    assert args.inventory == ['foo', 'bar', 'baz', 'bam,']
    assert args.subset == 'blip'



# Generated at 2022-06-12 20:12:11.963769
# Unit test for function add_basedir_options
def test_add_basedir_options():
    args = ['--playbook-dir', 'test']
    parser = argparse.ArgumentParser()
    add_basedir_options(parser)
    parsed_obj = parser.parse_args(args)
    assert parsed_obj.basedir == 'test'


# Generated at 2022-06-12 20:12:19.505720
# Unit test for function unfrack_path
def test_unfrack_path():
    paths = [
        '/tmp/etc',
        '~/foo/bar',
        '~root/bazqux',
        './quux',
    ]
    expected = [
        '/tmp/etc',
        os.path.expanduser('~/foo/bar'),
        os.path.expanduser('~root/bazqux'),
        os.getcwd() + '/quux',
    ]
    assert expected == list(map(unfrack_path(None), paths)), "Got wrong path back"
    assert expected == list(map(unfrack_path(False), paths)), "Got wrong path back"


# Generated at 2022-06-12 20:12:25.074975
# Unit test for function add_runas_options
def test_add_runas_options():
    parser = argparse.ArgumentParser()
    add_runas_options(parser)
    opts = parser.parse_args([])
    # verify defaults
    assert opts.become is False
    assert opts.become_method == C.DEFAULT_BECOME_METHOD
    assert opts.become_user == C.DEFAULT_BECOME_USER
    assert opts.ask_become_pass is False
    assert opts.ask_become_pass is False
    assert opts.become_ask_pass_override is False
    # verify options
    opts = parser.parse_args(['-b', '--become-method', 'sudo', '--become-user', 'admin'])
    assert opts.become is True

# Generated at 2022-06-12 20:12:26.882303
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser()
    add_connect_options(parser)


# Generated at 2022-06-12 20:12:30.307777
# Unit test for function add_meta_options
def test_add_meta_options():
    parser = argparse.ArgumentParser()
    add_meta_options(parser)
    options = parser.parse_args(['--force-handlers','--flush-cache'])
    assert options.force_handlers
    assert options.flush_cache


# Generated at 2022-06-12 20:12:39.953432
# Unit test for function add_connect_options
def test_add_connect_options():
    parser = argparse.ArgumentParser(prog='parser')
    add_connect_options(parser)
    args = parser.parse_args(['--private-key', '~/.ssh/id_rsa', '-u', 'ansiballz', '-c', 'ssh', '-T', '120', '--ssh-common-args', '-o ProxyCommand="ssh -i proxy jumphost.example.com -W %h:%p"',
                              '--sftp-extra-args', '-v', '--scp-extra-args', '-l 2922', '--ssh-extra-args', '-R', '-k', '--connection-password-file', '~/conn.pass'])
    assert args.private_key_file == '~/.ssh/id_rsa'

# Generated at 2022-06-12 20:12:41.268722
# Unit test for function version
def test_version():
    assert version()



# Generated at 2022-06-12 20:12:51.600064
# Unit test for function add_module_options
def test_add_module_options():
    test_parser = argparse.ArgumentParser(prog="test")
    # test default values
    add_module_options(test_parser)
    test_parser.add_argument('--otherargs', action='store_true')
    test_command = ['--otherargs', '-M', '/path1:/path2', '-M', '/path3']
    args = test_parser.parse_args(test_command)
    assert args.module_path == ['/path3', '/path1', '/path2']
    test_command = ['--otherargs', '-M', '/path1', '-M', '/path2']
    args = test_parser.parse_args(test_command)
    assert args.module_path == ['/path2', '/path1']



# Generated at 2022-06-12 20:12:57.104956
# Unit test for function add_async_options
def test_add_async_options():
    parser = argparse.ArgumentParser()
    add_async_options(parser)
    args = parser.parse_args(['-P', '30', '-B', '5'])
    assert args.poll_interval == 30
    assert args.seconds == 5



# Generated at 2022-06-12 20:13:13.378147
# Unit test for function add_output_options
def test_add_output_options():
    parser_test=argparse.ArgumentParser(prog='test')
    add_output_options(parser_test)
    options_test=parser_test.parse_args(['-o','-t','dir'])
    assert options_test.one_line==True
    assert options_test.tree=='dir'


# Generated at 2022-06-12 20:13:24.156795
# Unit test for function unfrack_path
def test_unfrack_path():
    assert ['a', 'b', 'c'] == unfrack_path(pathsep=True)('a:b:c')
    assert ['a', 'b', 'c'] == unfrack_path(pathsep=True)('a::b::c')
    assert [] == unfrack_path(pathsep=True)('')
    assert ['a'] == unfrack_path(pathsep=True)('a')
    assert ['a'] == unfrack_path(pathsep=True)(':a')
    assert ['a'] == unfrack_path(pathsep=True)('a:')
    assert ['-', 'a'] == unfrack_path(pathsep=True)('-:a')
    assert ['a', '-'] == unfrack_path(pathsep=True)('a:-')

# Generated at 2022-06-12 20:13:33.216756
# Unit test for function add_check_options
def test_add_check_options():
    args = """ansible-doc -m ping -l""".split()
    parser = argparse.ArgumentParser()
    add_check_options(parser)
    ns = parser.parse_args(args)
    assert repr(ns) == "Namespace(check=False, diff=False, syntax=False)"
    assert ns.check == False
    assert ns.diff == False
    assert ns.syntax == False


# Generated at 2022-06-12 20:13:39.034703
# Unit test for function add_check_options
def test_add_check_options():
    parser = argparse.ArgumentParser(
        prog="test",
        formatter_class=SortingHelpFormatter,
        conflict_handler='resolve',
    )
    add_check_options(parser)
    options = parser.parse_args(["-C"])
    assert options.check == True
    options = parser.parse_args(["--syntax-check"])
    assert options.syntax == True
    options = parser.parse_args(["--diff"])
    assert options.diff == True


# Generated at 2022-06-12 20:13:44.000507
# Unit test for function add_check_options
def test_add_check_options():
  parser = argparse.ArgumentParser(prog=os.path.basename(__file__))
  add_check_options(parser)
  args = parser.parse_args(['-C'])
  assert args.check==True
  args = parser.parse_args(['--syntax-check'])
  assert args.syntax==True
  args = parser.parse_args(['-D'])
  assert args.diff==True


# Generated at 2022-06-12 20:13:46.484774
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    import argparse
    a = SortingHelpFormatter()
    current_actions = sorted(a._actions, key=operator.attrgetter('option_strings'))
    b = argparse.HelpFormatter()
    b.add_arguments(current_actions)



# Generated at 2022-06-12 20:13:53.889730
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser(prog='test_ansible-config')
    add_vault_options(parser)
    testdata = {
        '--vault-id': [u'@/p@th', 'blah'],
        '--vault-password-file': [u'/path/to/vault_password.txt', '/path/to/vault_password.txt'],
    }

# Generated at 2022-06-12 20:13:55.380041
# Unit test for function add_vault_options
def test_add_vault_options():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)



# Generated at 2022-06-12 20:14:01.250517
# Unit test for function add_output_options
def test_add_output_options():
    parser = argparse.ArgumentParser(prog='test', conflict_handler='resolve')
    add_output_options(parser)
    options = parser.parse_args(['--one-line', '--tree', '/tmp/'])
    assert options.one_line is True
    assert options.tree == '/tmp/'



# Generated at 2022-06-12 20:14:03.932994
# Unit test for function add_subset_options
def test_add_subset_options():
    args = ['-t', 'no_such_tag']
    with pytest.raises(SystemExit):
        parser = argparse.ArgumentParser()
        add_subset_options(parser)
        parser.parse_args(args)



# Generated at 2022-06-12 20:14:17.446662
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_value = '/foo/bar'
    test_beacon = '@'
    expect_return_value = '@/foo/bar'
    assert expect_return_value == maybe_unfrack_path(test_beacon)(test_value)

    test_value = 'TEST/foo/bar'
    assert maybe_unfrack_path(test_beacon)(test_value) == 'TEST/foo/bar'



# Generated at 2022-06-12 20:14:21.316343
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('$')('$foo') == '$' + unfrackpath('foo')
    assert maybe_unfrack_path('$')('$$foo') == '$' + unfrackpath('$foo')



# Generated at 2022-06-12 20:14:23.275354
# Unit test for function version
def test_version():
    dummy_path = "/some/path/to/ansible-executable"
    assert version() == version(None)
    assert version(dummy_path) == version(dummy_path)

# Generated at 2022-06-12 20:14:24.815692
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    value = '$foo/bar'
    print(maybe_unfrack_path('$')(value))


# Generated at 2022-06-12 20:14:33.073123
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    from io import StringIO

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion)

    # when version is not set
    namespace = parser.parse_args([])
    assert namespace.version is None

    # when version is set
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    try:
        namespace = parser.parse_args(['--version'])
        assert ansible.release.__version__ in mystdout.getvalue()
    finally:
        sys.stdout = old_stdout


#
# Version
#

# Generated at 2022-06-12 20:14:34.724859
# Unit test for function version
def test_version():
    assert version()


#
# Utility functions for dealing with extra args and the filesystem
#

# Generated at 2022-06-12 20:14:41.415935
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('-d','--d')
    parser.add_argument('-b','--b')
    parser.add_argument('-c','--c')

    opts = parser.parse_args([])
    string_list = str(opts).split(' ')
    assert string_list[0].endswith('-b --b')
    assert string_list[1].endswith('-c --c')
    assert string_list[2].endswith('-d --d')



# Generated at 2022-06-12 20:14:45.021723
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    class FakeParser:
        prog = 'FAKE_PROG'
    obj = AnsibleVersion(option_strings=[])
    obj(parser=FakeParser(), namespace=None, values=None, option_string=None)



# Generated at 2022-06-12 20:14:49.044309
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--ansible-version", action=AnsibleVersion, help="Show Ansible version number and exit")
    parser.parse_args(["--ansible-version"])



# Generated at 2022-06-12 20:14:59.123122
# Unit test for function version
def test_version():
    t_result = ['2.0.0.0']
    t_result.append('  config file = /etc/ansible/ansible.cfg')
    t_result.append('  configured module search path = Default w/o overrides')
    t_result.append('  ansible python module location = /usr/lib/python2.6/site-packages/ansible')
    t_result.append('  ansible collection location = :/usr/share/ansible/collections')
    t_result.append('  executable location = /bin/ansible')
    t_result.append('  python version = 2.6.6 (r266:84292, Nov  3 2013, 16:26:21) [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)]')
    t_result.append

# Generated at 2022-06-12 20:15:06.800303
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=AnsibleVersion)
    parser.parse_args(['--version'])



# Generated at 2022-06-12 20:15:18.966226
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(formatter_class=SortingHelpFormatter)
    parser.add_argument('--zebra', action='store_true')
    parser.add_argument('--apple', action='store_true')
    parser.add_argument('--banana', action='store_true')
    parser.add_argument('--cherry', action='store_true')
    parser.parse_args(args=[])
    res = parser.format_help()
    lines = res.splitlines()
    lines = [l.strip() for l in lines]
    assert lines[2].startswith('--apple')
    assert lines[3].startswith('--banana')
    assert lines[4].startswith('--cherry')
    assert lines[5].startswith('--zebra')


# Generated at 2022-06-12 20:15:29.356722
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_values = [
        ('yes', 'yes'),
        ('@yes', '@yes'),
        ('@/somedir/somewhere', '@' + unfrackpath('/somedir/somewhere')),
        ('@./somedir/somewhere', '@' + unfrackpath('./somedir/somewhere')),
        ('@@/somedir/somewhere', '@@' + unfrackpath('/somedir/somewhere')),
        ('@/somedir/somewhere', '@' + unfrackpath('/somedir/somewhere')),
        ('@/somedir/somewhere', '@' + unfrackpath('/somedir/somewhere')),
    ]

    for given, expected in test_values:
        assert maybe_

# Generated at 2022-06-12 20:15:40.712413
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Test that the path is returned unchanged if it does not start with a ^
    for path in ('home/root', '/', '', '.', 'foo.txt'):
        assert maybe_unfrack_path('^')(path) == path
    # Test that a ^ followed by a path returns the unfracked path
    paths = [('^/a/b/c.txt', '/some/path/a/b/c.txt'),
             ('^../../a/b/c.txt', '../../a/b/c.txt')]
    for (path, expected_path) in paths:
        assert maybe_unfrack_path('^')(path) == expected_path
test_maybe_unfrack_path()


# Generated at 2022-06-12 20:15:45.503486
# Unit test for function version
def test_version():
    """ test version() output different between ansible and ansible-test """
    assert version("ansible") != version("ansible-test")
    assert version("ansible") == version("ansible")
    assert version() != version("ansible")



# Generated at 2022-06-12 20:15:53.821637
# Unit test for function version
def test_version():
    assert "core 2.4" in version("ansible-playbook")
    assert "core 2.4" in version(prog=None)

# FIXME: suboptimal way to check if we have yaml and yaml.CSafeLoader
# -- in ideal world we would do `from yaml import CLoader as Loader` and
#    then check if Loader is defined
has_real_yaml = True
try:
    from yaml import CSafeLoader as Loader
    # this is ugly workaround for https://bugs.python.org/issue29434
    CSafeLoader = Loader
except ImportError:
    # FIXME: this raises an exception if python-yaml is not installed
    has_real_yaml = False


# Generated at 2022-06-12 20:15:56.543169
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    path_in_executable_directory = maybe_unfrack_path(
        beacon=maybe_unfrack_path.__code__.co_filename)(maybe_unfrack_path.__code__.co_filename)
    assert maybe_unfrack_path.__code__.co_filename == path_in_executable_directory

#
# Options parsers
#

# Generated at 2022-06-12 20:15:58.858609
# Unit test for function version
def test_version():
    result = version('prog')
    # check if the first line has a random number
    assert set(result.split('\n')[0].split()) == set(str(__version__).split())
    # check if the executable location contains the right name
    assert sys.argv[0] in result



# Generated at 2022-06-12 20:16:03.605363
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action=AnsibleVersion, default=argparse.SUPPRESS,
                            help=_('display version information'))
    exit_func = getattr(parser, 'exit', None)
    exit_mock = MagicMock(side_effect=Exception('exit called.'))
    if exit_func is not None:
        parser.exit = exit_mock
    try:
        parser.parse_args(['-v'])
    except Exception as e:
        assert str(e) == 'exit called.'


# Generated at 2022-06-12 20:16:09.887679
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("/")("/hey/there") == "/hey/there"
    assert maybe_unfrack_path("@")("@hey/there") == "@hey/there"
    assert maybe_unfrack_path("@")("@~/hey/there") == "~/hey/there"
    assert maybe_unfrack_path("@")("@/hey/there") == "/hey/there"



# Generated at 2022-06-12 20:16:31.308016
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    av = AnsibleVersion(option_strings=['-v'], dest='version')
    expected_results = [
        'ansible 2.5.0',
        'ansible-connection 2.5.0',
        'ansible-console 2.5.0',
        'ansible-doc 2.5.0',
        'ansible-galaxy 2.5.0',
        'ansible-pull 2.5.0',
    ]

    for test_input in expected_results:
        parsers = argparse.ArgumentParser(prog=test_input.split()[0])
        parsed_results = av.__call__(parsers, None, None, None)
        assert str(expected_results[0]) in test_input



# Generated at 2022-06-12 20:16:35.830472
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@foobar') == '@' + unfrackpath('foobar')
    assert maybe_unfrack_path('@')('@@foobar') == '@@foobar'


# Generated at 2022-06-12 20:16:44.477115
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", help="option b")
    parser.add_argument("-a", help="option a")
    parser.add_argument("-e", help="option e")
    parser.add_argument("-d", help="option d")
    parser.add_argument("-c", help="option c")
    parser.add_argument("-g", help="option g")
    parser.add_argument("-f", help="option f")
    args = parser.parse_args("-e d -f g".split())

    # OptionParser does not order the arguments
    parser.print_help()
    help_str = parser.format_help()
    assert help_str.index("-b") < help_str.index("-a")
    assert help_str

# Generated at 2022-06-12 20:16:50.976079
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_paths = [
        ("--path", "/etc/ansible"),
        ("-p", "/etc/ansible"),
        ("-k", "-k"),
        ("--ask-vault-pass", "-k"),
    ]
    test_const_paths = [
        ("-k", "-k"),
        ("--ask-vault-pass", "-k"),
    ]
    for path in test_paths:
        path_value = maybe_unfrack_path(path[0])(path[0])
        assert path_value == path[1], "%s:%s" % (path_value, path[1])
    for path in test_const_paths:
        path_value = maybe_unfrack_path(path[0])(path[0])

# Generated at 2022-06-12 20:16:54.703173
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(beacon="_")("_/test") == "_" + unfrackpath("/test")
    assert maybe_unfrack_path(beacon="_")("/test") == "/test"
# Unit test end

# This won't be needed when we move to Python 3, which will recognize
# None as a special value for the 'type' argument to the argparse
# add_argument function.

# Generated at 2022-06-12 20:16:59.688275
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """
    All values starting with '$' are appended an extra '/' if value does not end with '/'.
    :return:
    """

    # values which not start with '$'
    beacon = '$'
    valid_values = ['$', '$hello', '$hello/$hello', '$hello/$hello/$hello',
                    '$hello/$hello/$hello/hello', '$hello/$hello/$hello/hello/$hello']

    for value in valid_values:
        valid_value = maybe_unfrack_path(beacon)(value)
        assert valid_value == value

    # values which start with '$'
    invalid_values = ['$hello', '$hello/hello', '$hello/hello/hello', '$hello/hello/hello/hello', '$hello/hello/hello/hello/hello']
    valid_

# Generated at 2022-06-12 20:17:04.325857
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    '''
    value1 = '$HOME/test'
    value2 = '@test'
    value1 = maybe_unfrack_path(value1)
    value2 = maybe_unfrack_path(value2)
    assert value1 == '$HOME/test'
    assert value2 == '@/home/ansible/test'
    '''



# Generated at 2022-06-12 20:17:08.886204
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    test_arg_option_string = "--version"
    parser = argparse.ArgumentParser()
    ansible_version = to_native(version(parser.prog))
    parser.add_argument(test_arg_option_string, action=AnsibleVersion)
    argv = [test_arg_option_string]
    args = parser.parse_args(argv)



# Generated at 2022-06-12 20:17:12.616853
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    class FakeParser(object):
        def __init__(self, prog):
            self.prog = prog
        def exit(self):
            self.exit_called = True
    parser = FakeParser('parser_prog')
    obj = AnsibleVersion()
    ansible.release.__version__ = 'ansible_version'
    obj(parser, None, None, None)
    assert parser.exit_called == True




# Generated at 2022-06-12 20:17:17.285018
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('+')('foo') == 'foo'
    assert maybe_unfrack_path('+')('+bar') == '+' + unfrackpath('bar')
    assert maybe_unfrack_path('+')('++bar') == '++bar'


# Generated at 2022-06-12 20:17:33.491220
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    import unittest
    class TestAnsibleVersion___call__(unittest.TestCase):
        def setUp(self):
            self.example = 'ansible'
        def test_ansible_version(self):
            self.assertEqual(AnsibleVersion().__call__(self.example, None, None, None), None)
    unittest.main()



# Generated at 2022-06-12 20:17:36.914176
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    claz = AnsibleVersion(option_strings=['--version'])
    parser = argparse.ArgumentParser()
    claz(parser, None, None, option_string=None)



# Generated at 2022-06-12 20:17:41.910752
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path(False)('/foo') == '/foo'
    if os.path.sep == '/':
        assert unfrack_path(False)('foo') == 'foo'
    else:
        assert unfrack_path(False)('foo') == '/foo'
        assert unfrack_path(True)('/bar:/baz') == ['/bar', '/baz']
        assert unfrack_path(True)('bar:baz') == ['bar', 'baz']



# Generated at 2022-06-12 20:17:45.924450
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    for path in ('/foo/bar', './foo/bar', '~/foo/bar',
                 '@/foo/bar', '@@/foo/bar', '/foo/bar/@'):
        assert maybe_unfrack_path('@')('@%s' % path[1:]) == path
        assert maybe_unfrack_path('@@')('@@%s' % path[1:]) == path



# Generated at 2022-06-12 20:17:50.820000
# Unit test for function version
def test_version():
    ansible_version = version('ansible-playbook')
    assert ansible_version.startswith('ansible-playbook [core 2.9.7]')
    assert ansible_version.splitlines()[3] == '  config file = /etc/ansible/ansible.cfg'
    assert ansible_version.splitlines()[4].startswith('  configured module search path = C:\\Program Files\\Python3.4\\Lib\\site-packages\\ansible\\modules')
    assert ansible_version.splitlines()[5].startswith('  ansible python module location = C:\\Program Files\\Python3.4\\Lib\\site-packages\\ansible')

# Generated at 2022-06-12 20:17:55.011408
# Unit test for function unfrack_path
def test_unfrack_path():
    assert (unfrack_path()('/foo') == '/foo')
    assert (unfrack_path()('bar') == 'bar')
    assert (unfrack_path()('~/baz') == '~/baz')
    assert (unfrack_path(True)('/foo:/foo1:/foo2') == ['/foo', '/foo1', '/foo2'])



# Generated at 2022-06-12 20:17:56.722322
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    test_obj = AnsibleVersion('test', 'test', 'test')
    parser = argparse.ArgumentParser(prog='test')
    with open(os.devnull, 'w') as devnull:
        with redirect_stdout(devnull):
            test_obj.__call__(parser, 'test', 'test')


#
# Utility module
#

# Generated at 2022-06-12 20:18:03.255316
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path("@")("@test") == "@test"
    assert maybe_unfrack_path("@")("test") == "test"
    assert maybe_unfrack_path("@")("@@test") == "@test"
    assert maybe_unfrack_path("@")("@test") == "@test"
    assert maybe_unfrack_path("@")("@test") == "@test"
    assert maybe_unfrack_path("@")("@test") == "@test"



# Generated at 2022-06-12 20:18:06.045916
# Unit test for method __call__ of class AnsibleVersion
def test_AnsibleVersion___call__():
    # No error if execution is normal.
    action = AnsibleVersion(option_strings=['-v'])
    parser = argparse.ArgumentParser('test')
    action.__call__(parser, None, None, '-v')
    assert True



# Generated at 2022-06-12 20:18:10.757252
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    """Unit test for function maybe_unfrack_path.

    Test passes if code coverage is 100%.
    """
    # coverage: 100%
    assert maybe_unfrack_path('@libexecdir@')('@libexecdir@/ansible') == '@libexecdir@/ansible'
    assert maybe_unfrack_path('@libexecdir@')('@libexecdir@pickle_file') == '@libexecdir@pickle_file'
    assert maybe_unfrack_path('@libexecdir@')('@libexecdir@') == '@libexecdir@'
    assert maybe_unfrack_path('@libexecdir@')('..') == '..'



# Generated at 2022-06-12 20:18:27.155813
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(':')(':tmp') == ':tmp'
    assert maybe_unfrack_path(':')(':/tmp') == ':/tmp'
    assert maybe_unfrack_path(';')(';/tmp') == ';/tmp'
    assert maybe_unfrack_path('|')('|/tmp') == '|/tmp'
    assert maybe_unfrack_path('|')('|tmp') == '|tmp'


# Generated at 2022-06-12 20:18:32.372361
# Unit test for function version
def test_version():
    from ansible.module_utils.common.version import __version__
    # Test when no git information is available
    _gitinfo = _git_repo_info
    _git_repo_info = lambda x: ''
    # Test the normal path
    assert version()
    # Test when called with the module name
    assert version(prog='ansible-playbook')
    # Restore _git_repo_info function
    _git_repo_info = _gitinfo



# Generated at 2022-06-12 20:18:36.016539
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('beacon')('beacon/tmp') == 'beacon/tmp'
    assert maybe_unfrack_path('beacon')('beacon/tmp/another') == 'beacon/tmp/another'
    assert maybe_unfrack_path('beacon')('beacon/tmp/another/path') == 'beacon/tmp/another/path'



# Generated at 2022-06-12 20:18:40.987754
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('+')('+/home/user') == '+/home/user'
    assert maybe_unfrack_path('+')('+/home/user/') == '+/home/user'
    assert maybe_unfrack_path('+')('+~/user') == '+/home/user'
    assert maybe_unfrack_path('+')('+$HOME/user') == '+/home/user'
    # assert maybe_unfrack_path('+')('+./home/user') == '+/./home/user'
    assert maybe_unfrack_path('+')('+./home/user') == '+/home/user'


# Generated at 2022-06-12 20:18:48.238985
# Unit test for function version
def test_version():
    assert version('ansible-playbook').split('\n')[0].startswith('ansible-playbook [core 2.')
    assert version('ansible-playbook').split('\n')[1].startswith('  config file = ')
    assert version('ansible-playbook').split('\n')[2].startswith('  configured module search path = ')
    assert version('ansible-playbook').split('\n')[3].startswith('  ansible python module location = ')
    assert version('ansible-playbook').split('\n')[4].startswith('  executable location = ')
    assert version('ansible-playbook').split('\n')[5].startswith('  python version = ')

# Generated at 2022-06-12 20:18:57.508993
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    parser = argparse.ArgumentParser(description='short sample app', formatter_class=SortingHelpFormatter)
    parser.add_argument("-f", action="store", help="store -f")
    parser.add_argument("-g", action="store", help="store -g")
    parser.add_argument("-b", action="store", help="store -b")
    output = parser.format_help()
    print("output: {}".format(output))
    assert "-b" in output
    assert "-f" in output
    assert "-g" in output
    assert output.index("-b") < output.index("-f")
    assert output.index("-b") < output.index("-g")
    assert output.index("-f") < output.index("-g")


# Generated at 2022-06-12 20:18:59.914978
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    '''Tests maybe_unfrack_path returns the input value when no beacon is present'''
    assert maybe_unfrack_path('beacon')('fake/path') == 'fake/path'


# Generated at 2022-06-12 20:19:03.014705
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    # Input starts with beacon
    assert maybe_unfrack_path('@')('@/foo/bar') == '@' + os.path.abspath('/foo/bar')
    # Input does not start with beacon
    assert maybe_unfrack_path('@')('/foo/bar') == '/foo/bar'



# Generated at 2022-06-12 20:19:06.218447
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    #test no change
    assert maybe_unfrack_path('@tmpdir')('@tmpdir/test.txt') == '@tmpdir/test.txt'

    #test change
    assert maybe_unfrack_path('@tmpdir')('@tmpdir/test/../test2/../test.txt') == '@tmpdir/test.txt'


# Generated at 2022-06-12 20:19:08.348118
# Unit test for function version
def test_version():
    result = version()
    assert isinstance(result, str)
    assert 'config file =' in result

#
# Common OptionGroups for parsers
#

# Generated at 2022-06-12 20:19:30.237026
# Unit test for function version
def test_version():
    assert version(prog='test version') == """test version [core {}]  config file = {}  configured module search path = Default w/o overrides  ansible python module location = {}  ansible collection location = {}  executable location = {}  python version = {}  jinja version = {}  libyaml = {}""".format(__version__, C.CONFIG_FILE, ':'.join(ansible.__path__), ':'.join(C.COLLECTIONS_PATHS), sys.argv[0], ''.join(sys.version.splitlines()), j2_version, HAS_LIBYAML)

# Generated at 2022-06-12 20:19:34.810048
# Unit test for function unfrack_path
def test_unfrack_path():
    unfrackpath = unfrack_path()
    assert unfrackpath("/some/path") == unfrackpath("///some/path")
    assert unfrackpath("/some/path") == unfrackpath("/some//path")
    assert unfrackpath("/some/path") == unfrackpath("/some/path/")
    assert unfrack_path(pathsep=True)("/some/path/with:/multiple/path/delimited/by/colon:/and/trailing/colon:") == ['/some/path/with', '/multiple/path/delimited/by/colon', '/and/trailing/colon']



# Generated at 2022-06-12 20:19:36.748709
# Unit test for function version
def test_version():
    assert version()  # Make sure it doesn't explode without arguments
    assert "not found" not in version()  # Make sure it doesn't print garbage



# Generated at 2022-06-12 20:19:46.875031
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    option_parser = argparse.ArgumentParser()
    option_parser.add_argument('-a', action='store_true')
    option_parser.add_argument('-b', action='store_true')
    shf = SortingHelpFormatter()
    # Just instantiating an OptionParser and passing it to the
    # SortingHelpFormatter should not fail, so let's just call format_help()
    # and see if that works.  We do not care about the result.
    shf.format_help(option_parser)
    # Now we add a positional argument.  This should be listed before the
    # optional arguments, so it can be found in the 2nd argument list.
    option_parser.add_argument('positional_argument')
    # Just like above, we don't care about the result of the actual call.
    #

# Generated at 2022-06-12 20:19:52.367489
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@/etc/ansible/hosts') == '@/etc/ansible/hosts'
    assert maybe_unfrack_path('@')('@~/local/path') == '@~/local/path'
    assert maybe_unfrack_path('')('@~/local/path') == '@~/local/path'
    assert maybe_unfrack_path('@')('@foo@bar') == '@foo@bar'



# Generated at 2022-06-12 20:19:56.326265
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('@')('@test_data/test_vars') == '@test_data/test_vars'
    assert maybe_unfrack_path('@')('test_vars') == 'test_vars'



# Generated at 2022-06-12 20:19:57.456487
# Unit test for function version
def test_version():
    assert 'ansible-config' in version('ansible-config')


# Generated at 2022-06-12 20:20:01.374934
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    data = {
        '~/.ansible/tmp': '~/.ansible/tmp',
        '@~/.ansible/tmp': '@/home/jdoe/.ansible/tmp',
    }
    for key, val in data.items():
        assert maybe_unfrack_path('@')(key) == val


# Generated at 2022-06-12 20:20:04.132690
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path()('foo/bar') == 'foo/bar'
    assert unfrack_path(pathsep=True)('foo/bar:baz/qux') == ['foo/bar', 'baz/qux']



# Generated at 2022-06-12 20:20:10.175483
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert '~/.ansible_config' == maybe_unfrack_path('~')('~/.ansible_config')
    assert '~/foo' == maybe_unfrack_path('~')('~/foo')
    assert '~' == maybe_unfrack_path('~')('~')
    assert './~foo' == maybe_unfrack_path('~')('./~foo')



# Generated at 2022-06-12 20:20:42.390358
# Unit test for function unfrack_path
def test_unfrack_path():

    with open(os.devnull, 'w') as null:
        sout = sys.stdout
        serr = sys.stderr
        sys.stdout = null
        sys.stderr = null

        try:
            # just to make sure this doesn't crash
            unfrack_path(pathsep=True)('foo:bar:baz')
            # check that it works for this pattern
            assert unfrack_path(pathsep=True)('bar:baz:') == ['bar', 'baz']
        finally:
            sys.stdout = sout
            sys.stderr = serr



# Generated at 2022-06-12 20:20:45.029459
# Unit test for constructor of class SortingHelpFormatter
def test_SortingHelpFormatter():
    # Basic test for the constructor.
    # (See http://stackoverflow.com/a/24813609 for rationale)
    assert SortingHelpFormatter()


# Generated at 2022-06-12 20:20:50.895316
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path('/')('./') == './'
    assert maybe_unfrack_path('/')('/foo/bar') == '/foo/bar'
    assert maybe_unfrack_path('/')('~/foo/bar') == '~/foo/bar'
    assert maybe_unfrack_path('/')('z~/foo/bar') == 'z~/foo/bar'



# Generated at 2022-06-12 20:20:53.695277
# Unit test for function version
def test_version():
    test_string = "ansible-playbook [core {0}]".format(__version__)

    assert version()[0:len(test_string)] == test_string
    assert version(prog='ansible-playbook')[0:len(test_string)] == test_string



# Generated at 2022-06-12 20:20:57.224876
# Unit test for function unfrack_path
def test_unfrack_path():
    assert unfrack_path('a$PATHs$PATH/b') == 'a/s/b'
    assert unfrack_path('$PATH/a') == '/a'
    assert unfrack_path('a$PATH/') == 'a/'
    # This returns None as it's not a valid path and the
    # unfrackpath check will fail and return None
    assert unfrack_path('$PATH') == None

# Generated at 2022-06-12 20:21:01.807341
# Unit test for function unfrack_path
def test_unfrack_path():
    # Test standard form
    assert unfrack_path()('lib/ansible/modules') == unfrackpath('lib/ansible/modules')
    # Test empty string
    assert unfrack_path()('') == ''
    # Test dash
    assert unfrack_path()('-') == '-'
    # Test path separator
    assert unfrack_path(pathsep=True)('lib/ansible/modules:/etc/ansible/modules') == [unfrackpath('lib/ansible/modules'), unfrackpath('/etc/ansible/modules')]
    # Test dash when using path separator
    assert unfrack_path(pathsep=True)('-') == '-'


# Generated at 2022-06-12 20:21:07.063208
# Unit test for function unfrack_path
def test_unfrack_path():
    from ansible.config.manager import ConfigManager
    from ansible.parsing.dataloader import DataLoader
    options = ConfigManager(loader = DataLoader())._read_config_file()
    assert unfrack_path(pathsep=True)(options['roles_path']) == ['/usr/share/ansible/roles', '/etc/ansible/roles']
    assert unfrack_path(pathsep=False)(options['roles_path']) == '/usr/share/ansible/roles'

#
# Base and shared options
#

# Generated at 2022-06-12 20:21:15.296093
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    def maybe_unfrack_path2(value):
        maybe_unfrack_path_ = maybe_unfrack_path('@')
        return maybe_unfrack_path_(value)
    assert maybe_unfrack_path2('@testdata/') == '@testdata/'
    assert maybe_unfrack_path2('@testdata/test1.yml') == '@testdata/test1.yml'
    assert maybe_unfrack_path2('@testdata/test2.yml') == '@testdata/test2.yml'
    assert maybe_unfrack_path2('@testdata/test3.yml') == '@testdata/test3.yml'


# Generated at 2022-06-12 20:21:19.445869
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    assert maybe_unfrack_path(u'@')('@foo') == u'@' + unfrackpath('foo')
    assert maybe_unfrack_path(u'@')('foo') == 'foo'
    assert maybe_unfrack_path(u'@@')('@@foo') == u'@@' + unfrackpath('foo')



# Generated at 2022-06-12 20:21:27.690173
# Unit test for function maybe_unfrack_path
def test_maybe_unfrack_path():
    test_string = '@/etc/ansible/ansible.cfg'
    result = maybe_unfrack_path('@')(test_string)
    assert '@' + unfrackpath('/etc/ansible/ansible.cfg') == result
    test_string = '@~/playbooks/playbook.yml'
    result = maybe_unfrack_path('@')(test_string)
    assert '@' + unfrackpath('~/playbooks/playbook.yml') == result
    test_string = '~/playbooks/playbook.yml'
    result = maybe_unfrack_path('@')(test_string)
    assert '~/playbooks/playbook.yml' == result


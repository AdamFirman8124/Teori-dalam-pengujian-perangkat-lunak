

# Generated at 2022-06-12 20:22:46.597405
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    os.chdir(CWD)

    # Testing the module / class
    test_answer = 'test_do_cd'
    test_args = ''
    console = ConsoleCLI(test_answer, test_args)
    console.do_cd('')
    assert console.cwd == 'test_do_cd'

    test_answer = 'test_do_cd'
    test_args = ''
    console = ConsoleCLI(test_answer, test_args)
    console.do_cd('*')
    assert console.cwd == 'all'

    test_answer = 'test_do_cd'
    test_args = ''
    console = ConsoleCLI(test_answer, test_args)
    console.do_cd('no_host_matched')

# Generated at 2022-06-12 20:22:49.687471
# Unit test for method cmdloop of class ConsoleCLI

# Generated at 2022-06-12 20:22:51.336085
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    C = AnsibleConsoleCLI()
    C.cmdloop()

# Generated at 2022-06-12 20:23:00.132571
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    # this hack is to import module from upper dir
    sys.path.append("../ansible_collections/ansible/netcommon")

    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import load_provider

    # this is a hack to get ansible ConsoleCLI working
    # ansible.config.load_config_file("../ansible.cfg")
    ansible.config.load_config_file("../ansible.cfg")
    ansible.config.CFG._config_cache['inventory'] = ansible.inventory.Inventory("../hosts_different_group")

    # clean the history file
    histfile = os.path.join(os.path.expanduser("~"), ".ansible-console_history")

# Generated at 2022-06-12 20:23:05.580863
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    ConsoleCLI = console.ConsoleCLI()
    ConsoleCLI.inventory = MagicMock()
    ConsoleCLI.selected = MagicMock()
    ConsoleCLI.groups = ["backup", "db", "lb"]
    ConsoleCLI.do_list("groups")
    ConsoleCLI.do_list("")


# Generated at 2022-06-12 20:23:11.877492
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    args = context.CLIARGS
    args['verbosity'] = 5
    cli = ConsoleCLI(args)

# Generated at 2022-06-12 20:23:15.043254
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    '''Test ConsoleCLI do_list method'''
    consoleCLI = ConsoleCLI()
    assert consoleCLI is not None
    print("passed test: test_ConsoleCLI_do_list")



# Generated at 2022-06-12 20:23:24.568857
# Unit test for method run of class ConsoleCLI
def test_ConsoleCLI_run():
    # Let's fake readline functionality
    class readline:
        def __init__(self):
            self.history_file = '~/.ansible-console_history'
        def read_history_file(self, histfile):
            pass
        def write_history_file(self, histfile):
            pass

    # Let's fake sys.stdout as well
    class stdout:
        def __init__(self):
            self.str = ''

        def write(self, text):
            self.str = text

        def flush(self):
            pass

    # Let's make the test
    from collections import namedtuple
    import sys
    import os
    from contextlib import contextmanager
    from ansible.cli import CLI
    from ansible.plugins.loader import module_loader, fragment_loader

# Generated at 2022-06-12 20:23:25.235894
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    pass

# Generated at 2022-06-12 20:23:32.194543
# Unit test for method post_process_args of class ConsoleCLI
def test_ConsoleCLI_post_process_args():
    cli_args = [
        "ansible-console",
        "--timeout", "10"
    ]
    config = context.CLIARGS = cli.parse(cli_args)
    ConsoleCLI().post_process_args()

    assert context.CLIARGS['inventory'] == '/etc/ansible/hosts'
    assert context.CLIARGS['module_path'] == '~/.ansible/plugins/modules/:/usr/share/ansible/plugins/modules'
    assert context.CLIARGS['connection'] == 'smart'
    assert context.CLIARGS['forks'] == 5
    assert context.CLIARGS['remote_user'] == 'root'
    assert context.CLIARGS['private_key_file'] == None

# Generated at 2022-06-12 20:24:00.121026
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    cli = ConsoleCLI()
    # without argument: 
    assert cli.do_cd('') == False
    # actual condition won't get this value
    # assert cli.do_cd('#') == False
    # assert cli.do_cd(' ') == False
    # assert cli.do_cd('/') == False
    # assert cli.do_cd('//') == False
    # assert cli.do_cd('///') == False
    # assert cli.do_cd('////') == False
    # assert cli.do_cd('/////') == False
    # assert cli.do_cd('//////') == False
    # assert cli.do_cd('///////') == False
    # assert cli.do_cd('////////') == False
    # assert cli.

# Generated at 2022-06-12 20:24:07.441722
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    """Unit test for function completedefault of class ConsoleCLI"""
    with patch('sys.stdout', new=StringIO()) as mock_stdout, \
        patch('sys.stderr', new=StringIO()) as mock_stderr, \
        patch('ansible.cli.console.ReadlineConsole.completedefault') as mock_completedefault:
        consolecli = ConsoleCLI(args=['ansible-console', '-i', 'test-inventory'])
        consolecli.parsed = True
        name = 'test-command'
        line = ' test-command test-param'
        begidx = 15
        endidx = 15
        consolecli.completedefault(name, line, begidx, endidx)
        assert mock_completedefault.called
        assert mock_com

# Generated at 2022-06-12 20:24:14.463605
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    # The test instance of ConsoleCLI class
    console_cli = ConsoleCLI()
    console_cli.module_finder = MagicMock()
    console_cli.module_finder.modules = [
        'test_module_a',
        'test_module_b',
        'test_module_c',
    ]
    # Test
    assert console_cli.list_modules() == [
        'a',
        'b',
        'c',
    ]


# Generated at 2022-06-12 20:24:18.241962
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    console_cli_obj = ConsoleCLI()
    # Asserting method default is correctly working
    assert console_cli_obj.default("hi") == False
    # Asserting method do_cd is correctly working
    assert console_cli_obj.do_cd("hi") == None

# Generated at 2022-06-12 20:24:28.698002
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    import tempfile
    from xml.dom.minidom import parseString
    import pwd
    import os
    import shutil

    CWD = os.getcwd()
    TMP = tempfile.mkdtemp()
    os.chdir(TMP)
    print(TMP)

    module_name = 'my_module_name'


    def cleanup():
        shutil.rmtree(TMP)
        os.chdir(CWD)


    atexit.register(cleanup)
    # Setup working directory
    os.makedirs('../module_utils')
    os.makedirs('library')
    os.makedirs('filter_plugins')
    #
    # Create a my_module_name
    #

# Generated at 2022-06-12 20:24:32.953601
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    console_cli = ConsoleCLI()
    console_cli.cwd = '*'
    console_cli.remote_user = 'test'
    console_cli.set_prompt()
    assert console_cli.prompt == 'test@* [\#] '



# Generated at 2022-06-12 20:24:34.987743
# Unit test for method run of class ConsoleCLI
def test_ConsoleCLI_run():
    res = Shell(loader=None, variable_manager=None, commands=None, exitmethod=None)
    res.run()
    pass

# Generated at 2022-06-12 20:24:39.685036
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    consolecli = ConsoleCLI()
    consolecli.groups = ['test']
    consolecli.selected = ['test1', 'test2']
    consolecli.do_list('')
    # FIXME - Use real host objects
    #assert consolecli.do_list('') == None


# Generated at 2022-06-12 20:24:47.753363
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    plugin = module_loader.find_plugin('setup')
    oc, a, _, _ = plugin_docs.get_docstring(plugin, fragment_loader, is_module=True)
    list_module_args = list(oc['options'].keys())

    # Create a ConsoleCLI object
    console = ConsoleCLI(args=['setup'])
    console.module_args = lambda x: list_module_args

    # Test if completedefault returns the expected result
    result = console.completedefault('', 'setup ', 5, 9)
    assert(result == ['gather_facts=', 'filter=', 'gather_subset='])



# Generated at 2022-06-12 20:24:53.803213
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    # JenkinsWorker.create_datadir_file(datadir_path)
    cli = ConsoleCLI()
    cli.inventory = MagicMock()
    cli.inventory.list_groups.return_value = ['foo', 'bar']
    cli.cwd = '*'

    cli.selected = ['fake']
    cli.do_list('')
    cli.inventory.list_hosts.assert_called_once_with(None)

    cli.do_list('groups')
    cli.inventory.list_groups.assert_called_with()
    assert cli.inventory.list_hosts.call_count == 1


# Generated at 2022-06-12 20:26:19.462601
# Unit test for method do_list of class ConsoleCLI

# Generated at 2022-06-12 20:26:26.983370
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    # Test for method completedefault(self, text, line, begidx, endidx)
    # This method tests if the completedefault method of the ConsoleCLI class will return the list of modules found in the ansible library
    # Parameters
    # text -> string - text, line -> string - line, begidx -> int - begidx, endidx -> int - endidx
    # Returns
    # list - list of modules found in the ansible library
    print ("Testing method completedefault of class ConsoleCLI")
    text = ''
    line = 'accelerate'
    begidx = 0
    endidx = 1
    cli = ConsoleCLI()
    assert cli.completedefault(text, line, begidx, endidx) == ['accelerate']


# Generated at 2022-06-12 20:26:30.337602
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():

    host = 'localhost'
    con = ConsoleCLI()
    arg = 'groups'
    con.do_list(arg)

    with pytest.raises(Exception):
        arg = 'test'
        con.do_list(arg)



# Generated at 2022-06-12 20:26:31.080566
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    pass


# Generated at 2022-06-12 20:26:40.195144
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    """Test for console cli default."""

    import unittest

    class TestConsoleCLI(unittest.TestCase):
        """Convenience class to test ConsoleCLI default."""

        def test_class_attributes(self, cls_attr):
            """Tests if ConsoleCLI class has given attributes."""

            self.assertTrue(hasattr(ConsoleCLI, cls_attr))

        def test_default(self):
            """Tests method default of class ConsoleCLI."""

            console = ConsoleCLI()
            self.assertRaises(Exception, console.default, 'test')

    suite = unittest.makeSuite(TestConsoleCLI)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-12 20:26:48.568321
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    """
    Test completedefault method of class ConsoleCLI using pytest.
    """
    import pytest

    def backup_ConsoleCLI_completedefault(self, text, line, begidx, endidx):
        return 'foo'

    ConsoleCLI.completedefault = backup_ConsoleCLI_completedefault

    test_ConsoleCLI = ConsoleCLI(['--check'])
    assert test_ConsoleCLI.completedefault() == 'foo'

# Generated at 2022-06-12 20:26:53.120987
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    # test data
    module_name = "ansible.plugins.shell"
    in_path = False
    # perform test
    cmd = ConsoleCLI()
    result = cmd.helpdefault(module_name)
    # assert results
    assert result is None


# Generated at 2022-06-12 20:26:54.103857
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    pass  # TODO Write test

# Generated at 2022-06-12 20:26:56.752180
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    cli = create_ConsoleCLI()
    cli.list_modules()


# Generated at 2022-06-12 20:26:58.361387
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    # TODO: Test me!
    raise Exception('Test not implemented!')

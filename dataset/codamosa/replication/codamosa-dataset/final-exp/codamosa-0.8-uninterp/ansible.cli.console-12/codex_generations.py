

# Generated at 2022-06-12 20:23:05.411669
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    c = ConsoleCLI()
    c._play_prereqs = mock.MagicMock()
    c._play_prereqs.return_value.__getitem__().list_hosts.return_value = []
    c.list_modules = mock.MagicMock()
    c.list_modules.return_value = ['module1']
    c.module_args = mock.MagicMock()
    plugin_docs.get_docstring = mock.MagicMock()
    plugin_docs.get_docstring.return_value = ({'short_description': 'short description', 'options': {'arg': {'description': ['long description']}}}, {})

    display.display = mock.MagicMock()

# Generated at 2022-06-12 20:23:09.652792
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():

    #setup
    console=ConsoleCLI()

    #create mock data
    ConsoleCLI.become=True
    ConsoleCLI.become_user='bob'
    ConsoleCLI.cwd='mockhost1'
    ConsoleCLI.forks=666
    ConsoleCLI.check_mode=True
    ConsoleCLI.diff=False
    ConsoleCLI.remote_user='alice'
    ConsoleCLI.task_timeout=10

    #call method
    console.set_prompt()

    #assert
    assert console.prompt == '[alice@mockhost1] >> '
    assert console.test_prompt == '[alice@mockhost1] >> '


# Generated at 2022-06-12 20:23:16.800901
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    # Testing with no group/host name.
    shell = ConsoleCLI()
    with patch.object(shell, 'set_prompt') as set_prompt_function:
        shell.do_cd('')
        set_prompt_function.assert_not_called()
        assert shell.cwd == '*'

    # Testing with all group/host.
    shell = ConsoleCLI()
    with patch.object(shell, 'set_prompt') as set_prompt_function:
        shell.do_cd('/*')
        set_prompt_function.assert_called_with()
        assert shell.cwd == 'all'


# Generated at 2022-06-12 20:23:22.822269
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    # Create an instance of 'ConsoleCLI' with arguments
    console_cli = ConsoleCLI()

# Generated at 2022-06-12 20:23:24.917946
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    instance = ConsoleCLI()
    assert instance.default('ping') == None


# Generated at 2022-06-12 20:23:27.967399
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    print('Testing method list_modules of class ConsoleCLI')
    consoleCLI = ConsoleCLI()
    consoleCLI.list_modules()


# Generated at 2022-06-12 20:23:32.258635
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    assert hasattr(ConsoleCLI, 'completedefault')
    cli = ConsoleCLI()
    text = "file"
    line = "file"
    begidx = 0
    endidx = 0
    assert cli.completedefault(text, line, begidx, endidx) == None

# Generated at 2022-06-12 20:23:39.341200
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    console = ConsoleCLI()
    ansible_module_path = C.DEFAULT_MODULE_PATH
    ansible_module_path += os.pathsep + os.path.join(os.path.dirname(__file__), '..', '..', '..', 'plugins', 'modules')
    module_paths = ansible_module_path.split(os.pathsep)
    modules = []

    for p in module_paths:
        if os.path.isdir(p):
            modules += find_module_paths(p)
        else:
            modules += find_module_paths(p, True)

    assert console.list_modules() == modules


# Generated at 2022-06-12 20:23:45.314901
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    console_instance = ConsoleCLI()
    console_instance.cwd = 'test_hosts'
    console_instance.variable_manager = DictData(dict())
    console_instance.inventory = Inventory(loader=DictData(dict()))
    console_instance.inventory.add_host(console_instance.cwd)
    console_instance.inventory.get_groups_dict()[console_instance.cwd] = Group(console_instance.cwd)
    console_instance.loader = DataLoader()
    console_instance.selected = console_instance.inventory.get_groups_dict()[console_instance.cwd]
    console_instance.inventory.get_groups_dict()[console_instance.cwd].add_host(console_instance.inventory.get_host(console_instance.cwd))
    # Real code starts here

# Generated at 2022-06-12 20:23:47.884792
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    # ./test/units/test_console.py
    test_ConsoleCLI().do_cd('./test/units/test_console.py')


# Generated at 2022-06-12 20:24:08.251658
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    """Test default"""
    # Setup

    # Command line arguments

# Generated at 2022-06-12 20:24:18.284972
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    cli = ConsoleCLI()
    cli.inventory = MagicMock()
    cli.cwd = "some string"

    cli.do_list("some string")
    cli.inventory.list_hosts.assert_called_with(cli.cwd)

    cli.do_list("")
    cli.inventory.list_groups.assert_called_with()
    
    
import unittest
unittest.main(argv=['first-arg-is-ignored'], exit=False)


# Generated at 2022-06-12 20:24:20.547627
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    # get an instance of ConsoleCLI class
    mycli = ConsoleCLI()
    # do some fake data for args for the method
    args = "."
    # execute the method
    mycli.do_cd(args)
    # tests


# Generated at 2022-06-12 20:24:30.155078
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    """
    Unit test for method completedefault of class ConsoleCLI
    """
    args = {}
    args['pattern'] = 'my patterns'
    args['inventory'] = 'my inventory'
    args['listhosts'] = 'my listhosts'
    args['subset'] = 'my subset'
    args['module_path'] = 'my module_path'
    args['flush_cache'] = 'my flush_cache'
    args['forks'] = 'my forks'
    args['remote_user'] = 'my remote_user'
    args['private_key_file'] = 'my private_key_file'
    args['ssh_common_args'] = 'my ssh_common_args'
    args['ssh_extra_args'] = 'my ssh_extra_args'
    args['sftp_extra_args']

# Generated at 2022-06-12 20:24:38.975687
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    d = dict(a=dict(hosts=['host1'], vars={'name': 'value'}), b=dict(hosts=['host2'], vars={'name': 'value'}))
    i = InventoryManager(loader=DataLoader())
    i.add_group('all')
    i.add_group('ungrouped')
    i.add_host('host1')
    i.add_host('host2')
    i.get_group('all').add_host('host1')
    i.get_group('all').add_host('host2')

    c = ConsoleCLI(i)
    assert c.complete_cd('', '', 0, 0) == ['host1', 'host2', 'all', 'ungrouped']

# Generated at 2022-06-12 20:24:40.867870
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    # FIXME: @mock.patch
    # FIXME: self.run()
    pass


# Generated at 2022-06-12 20:24:50.222657
# Unit test for method complete_cd of class ConsoleCLI

# Generated at 2022-06-12 20:24:51.478423
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    cli = ConsoleCLI()
    cli.cmdloop()
    assert True

# Generated at 2022-06-12 20:24:57.409800
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    module_name = 'setup'
    instance = ConsoleCLI()
    arg = '''
    '''
    instance.do_cd('webservers')
    check_raw = module_name in C._ACTION_ALLOWS_RAW_ARGS
    task = dict(action=dict(module=module_name, args=parse_kv(arg, check_raw=check_raw)), timeout=instance.task_timeout)
    play_ds = dict(name="Ansible Shell", hosts=instance.cwd, gather_facts='no', tasks=[task], remote_user=instance.remote_user, become=instance.become, become_user=instance.become_user, become_method=instance.become_method, check_mode=instance.check_mode, diff=instance.diff)

# Generated at 2022-06-12 20:25:08.774714
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    obj = ConsoleCLI()
    assert obj.set_prompt()
    assert obj.check_mode == context.CLIARGS['check']
    assert obj.task_timeout == context.CLIARGS['task_timeout']
    assert obj.diff == context.CLIARGS['diff']
    assert obj.passwords == {'conn_pass': sshpass, 'become_pass': becomepass}
    assert obj.inventory
    assert obj.modules
    assert obj.variable_manager
    assert obj.cwd == obj.pattern
    assert obj.become == context.CLIARGS['become']
    assert obj.check_mode == context.CLIARGS['check']
    assert obj.cwd == obj.pattern
    assert obj.diff == context.CLIARGS['diff']
    assert obj.loader
   

# Generated at 2022-06-12 20:25:26.570961
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    console_cli = ConsoleCLI()
    assert console_cli.list_modules() == ['setup']



# Generated at 2022-06-12 20:25:28.690209
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
   CLI = ConsoleCLI()
   CLI.do_cd("localhost")
   assert CLI.cwd == "localhost"
   return True


# Generated at 2022-06-12 20:25:31.430273
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    o = ConsoleCLI()
    o.modules = ['ping', 'setup']
    o.helpdefault('ping')
    o.helpdefault('setup')
    o.helpdefault('apt')
    o.helpdefault('not_a_module')

# Generated at 2022-06-12 20:25:33.681318
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    instance = ConsoleCLI()
    module_name = 'ping'
    # We are just checking for the display of the values. No validation of display possible.
    instance.helpdefault(module_name)

# Generated at 2022-06-12 20:25:39.120807
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    """Unit tests for console CLI"""
    ansible_console = ConsoleCLI()
    ansible_console.setup()
    with patch('ansible.cli.console.ConsoleCLI.set_prompt', return_value=True) as mock_method1:
        with patch('ansible.cli.console.ConsoleCLI.cmdloop', return_value=True) as mock_method2:
            ansible_console.run()
            assert mock_method1.called == True
            assert mock_method2.called == True

"""
Console script entry point
"""

# Generated at 2022-06-12 20:25:44.236189
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    from ansible_test._internal.test_test import get_all_subclasses
    classes = get_all_subclasses(ConsoleCLI)
    for cls in classes:
        if cls.__name__.startswith('__'):
            assert False, "name %s should not start with __" % cls.__name__
    assert set(ConsoleCLI.completedefault.__code__.co_names).issuperset(set(['mline', 'offs']))

# Generated at 2022-06-12 20:25:45.781865
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    pass


# Generated at 2022-06-12 20:25:51.840667
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    runner = CliRunner()
    module_dir = os.path.dirname(os.path.dirname(__file__))
    test_dir = os.path.join(module_dir, 'test', 'units', 'agilelib')
    result = runner.invoke(console.main, ["--module-path", test_dir, "--list"])
    assert result.exit_code == 0
    assert result.output == './\n'


# Generated at 2022-06-12 20:25:56.552557
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    """ Test default method of ConsoleCLI class. """
    # Test variables
    self = ConsoleCLI()
    module_name = 'setup'
    arg = 'args'
    forceshell = False

    # Test with variables defined
    # Expected result:
    #   An empty string
    result = self.default(arg, module_name)
    assert result == '', 'Expected empty string not found'


# Generated at 2022-06-12 20:25:57.401050
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    assert False



# Generated at 2022-06-12 20:26:16.330143
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    test_instance = ConsoleCLI()
    module_name = 'ansible.modules.network.network_cli'
    test_instance.helpdefault(module_name)

if __name__ == '__main__':
    test_ConsoleCLI_helpdefault()
    pass

# Generated at 2022-06-12 20:26:17.099690
# Unit test for method do_list of class ConsoleCLI

# Generated at 2022-06-12 20:26:24.431118
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    "Validate the module_args method"
    console_cli = ConsoleCLI()
    console_cli.module_args('copy')
    assert console_cli.module_args('copy') == ['content','dest','force','remote_src','selevel','serole','setype','seuser','src','validate','original_basename']
    assert console_cli.module_args('command') == ['chdir','creates','executable','removes','warn','_raw_params','_uses_shell','argv','creates','removes','stdin']
    assert console_cli.module_args('setup') == ['filter','gather_subset','gather_timeout','no_log']


# Generated at 2022-06-12 20:26:32.933187
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    # Test with bogus module name
    TestConsoleCLI = ConsoleCLI()
    TestConsoleCLI.modules = ['setup', 'ping']
    TestConsoleCLI.do_ping = lambda arg: TestConsoleCLI.default('ping ' + arg)
    TestConsoleCLI.helpdefault('bogus')

    # Test with real module, setup
    TestConsoleCLI = ConsoleCLI()
    TestConsoleCLI.modules = ['setup', 'ping']
    TestConsoleCLI.do_setup = lambda arg: TestConsoleCLI.default('setup ' + arg)
    TestConsoleCLI.helpdefault('setup')

# Generated at 2022-06-12 20:26:41.802150
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():

    #FIXME: make this is a test class with a proper setUp
    #before the first test
    #ansible_console.console.C.REJECT_EXTS = ['.swp']
    #ansible_console.console.C.IGNORE_FILES = ['ignoreme', 'ignoreme.exe']

    try:
        import ansible_console
        ansible_console_installed = True
    except ImportError:
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir)))
        ansible_console_installed=False

    from ansible_console.console import ConsoleCLI
    cli = ConsoleCLI()

    # Test module with spaces
    module

# Generated at 2022-06-12 20:26:53.933730
# Unit test for method complete_cd of class ConsoleCLI

# Generated at 2022-06-12 20:26:57.852493
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    '''
    Run the package unit tests if called from command line
    '''
    import sys
    import doctest

    results = doctest.testmod()
    if results.failed == 0:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    test_ConsoleCLI_do_list()

# Generated at 2022-06-12 20:27:01.614812
# Unit test for method do_verbosity of class ConsoleCLI
def test_ConsoleCLI_do_verbosity():
    console_cli = ConsoleCLI()
    console_cli.do_verbosity("1")
    console_cli.do_verbosity("2")
    assert console_cli.do_verbosity("3") is None
    assert console_cli.do_verbosity("a") is None
    

# Generated at 2022-06-12 20:27:08.946565
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    console_cli = ConsoleCLI(args=['ansible-console', './test/units/', '-i', './test/units/inventory.yml', '-u', 'mimaher'])
    p = Mock()
    p.name = 'localhost'
    p.port = 1234
    p.vars = {}
    p.groups = ['test_group']
    p.get_vars.return_value = {}
    Host = Mock()
    Host.return_value = p
    console_cli.inventory.get_host.return_value = p
    console_cli.inventory.list_hosts.return_value = [Host]
    console_cli.groups = ['test_group']
    console_cli.hosts = [p]
    console_cli.selected = [p]

# Generated at 2022-06-12 20:27:09.519507
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    pass

# Generated at 2022-06-12 20:28:35.907775
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    print('')
    print('Testing ConsoleCLI set_prompt method')
    print('-------------------------------------')
    # Set up arguments
    from ansible.cli import CLI
    from ansible.utils.display import Display
    from ansible import context
    
    display = Display()

# Generated at 2022-06-12 20:28:43.364507
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    cli = ConsoleCLI()
    cli.modules = ['setup', 'command', 'get_url']
    # check each module plus a non-module
    for module in cli.modules + ['bogus']:
        # should always return a list
        assert isinstance(cli.module_args(module), list)
        # no test I know of to validate the returned content is all valid options
        # if the module doesn't exist, an empty list should be returned
        if module == 'bogus':
            assert cli.module_args(module) == []



# Generated at 2022-06-12 20:28:50.877812
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    console = ConsoleCLI()

# Generated at 2022-06-12 20:28:56.711378
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    console = ConsoleCLI(['console', '-e', 'foo=bar'])

    console.set_prompt('test')
    console.prompt = 'test'

    display.v = mock.Mock()
    console.loader = mock.Mock()
    console.loader.module_loader = mock.Mock()
    console.loader.module_loader.get_all_plugin_loaders = lambda: [PlaybookCLI.module_loader, AnsibleModuleCLI.module_loader]
    console.loader.module_loader.find_plugin = lambda x, check_aliases=True: '/path/to/module'

# Generated at 2022-06-12 20:29:06.774692
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    import __main__
    import sys
    import mock

    # The required args for init of ConsoleCLI
    context.CLIARGS = mock.Mock()
    context.CLIARGS.connection = 'smart'
    context.CLIARGS.module_path = None
    context.CLIARGS.forks = 5
    context.CLIARGS.become = False
    context.CLIARGS.become_method = 'sudo'
    context.CLIARGS.become_user = 'root'
    context.CLIARGS.check = False
    context.CLIARGS.diff = False
    context.CLIARGS.private_key_file = None
    context.CLIARGS.remote_user = None
    context.CLIARGS.subset = None
    context.CL

# Generated at 2022-06-12 20:29:15.414210
# Unit test for method do_verbosity of class ConsoleCLI
def test_ConsoleCLI_do_verbosity():
    """
    Test method do_verbosity of ConsoleCLI
    """
    cli = ConsoleCLI()
    # Test case where there is no arg
    # Mock the response to display.display()
    with patch.object(display, 'display'):
        cli.do_verbosity("")
        display.display.assert_called_with("Usage: verbosity <number>")
    # Test case where there is an arg
    # Mock the response to display.verbosity
    with patch.object(display, 'verbosity') as mock_verbosity:
        cli.do_verbosity("2")
        cli.display.v("verbosity level set to 2")
        mock_verbosity.assert_called_with(2)


# Generated at 2022-06-12 20:29:17.354390
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    # Prepare test data
    console = ConsoleCLI()
    module = 'ping'
    # Execute the function under test
    console.helpdefault(module)
    # Check the result
    assert True

# Generated at 2022-06-12 20:29:18.451557
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    obj = ConsoleCLI()


# Unit test of function doc_callbacks of module console

# Generated at 2022-06-12 20:29:22.381247
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    console_cli = ConsoleCLI()
    console_cli.modules='[module_name]'
    console_cli.selected='selected'
    console_cli.module_args=MagicMock()
    console_cli.helpdefault('module_name')
    console_cli.module_args.assert_called_once_with('module_name')

# Generated at 2022-06-12 20:29:32.642001
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    import os
    import sys
    import imp
    import ctypes
    """
    :param module_name: the name of the module that we want to look for.
    :type module_name: String
    """
    try:
        if sys.version_info[:2] < (2, 7):
            import unittest2 as unittest
        else:
            import unittest
    except:
        import unittest
    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict


# Generated at 2022-06-12 20:31:18.774903
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    """This call tests the cmdloop method of ConsoleCLI"""

    cli = ConsoleCLI()

    c_pid = ConsoleCLI()
    c_pid.do_shell('ps -ef')
    c_pid.do_exit('')
    c_pid.do_EOF('')
    c_pid.do_forks('1')
    c_pid.do_serial('1')
    c_pid.do_verbosity('1')
    c_pid.do_cd('1')
    c_pid.do_list('1')
    c_pid.do_become('1')
    c_pid.do_become_user('1')
    c_pid.do_become_method('1')
    c_pid.do_check('1')

# Generated at 2022-06-12 20:31:27.728112
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    def mock_load_resources_from_cwd():
        return (None, None, None)

    def mock_do_shell(arg):
        return

    patch_do_shell = patch.object(ConsoleCLI, 'do_shell', mock_do_shell)
    patch_load_resources_from_cwd = patch.object(ConsoleCLI, 'load_resources_from_cwd', mock_load_resources_from_cwd)

    with patch_do_shell, patch_load_resources_from_cwd:
        # Test with no input
        display = Display()
        console_cli = ConsoleCLI(display)
        console_cli.cmdloop()

        # Test with input
        display = Display()
        console_cli = ConsoleCLI(display)
        console_cli.cmdqueue.append('arg')
       

# Generated at 2022-06-12 20:31:34.829456
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    consolecli = ConsoleCLI()
    consolecli.modules = ['ping']
    consolecli.do_ping = lambda arg: consolecli.default('ping ' + arg)
    consolecli.help_ping = lambda: consolecli.helpdefault('ping')
    tempfile = tempfile_builder.mktemp()
    try:
        consolecli.cmdqueue = ['ping', 'os_server', 'os_server']
        with open(tempfile.name, "w") as f:
            consolecli.stdout = f
            consolecli.cmdloop()
    finally:
        tempfile.close()
    with open(tempfile.name, 'r') as myfile:
        output = myfile.read()
    assert '''Run a connectivity test''' in output
    assert '''Parameters:''' in output

# Generated at 2022-06-12 20:31:43.906095
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    args = context.CLIARGS
    args['listhosts'] = False
    args['listtasks'] = False
    args['listtags'] = False
    args['syntax'] = False
    cli = ConsoleCLI(args=args)

    module_name = 'command'

# Generated at 2022-06-12 20:31:44.620951
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    pass

# Generated at 2022-06-12 20:31:57.568497
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    host = "ubuntu"
    pattern = "*"
    remote_user = "root"
    become_user = "root"
    become = True
    become_method = "sudo"
    check_mode = False
    diff = False
    inventory = InventoryManager("")
    loader = DictDataLoader({})
    variable_manager = VariableManager(loader=loader, inventory=inventory)
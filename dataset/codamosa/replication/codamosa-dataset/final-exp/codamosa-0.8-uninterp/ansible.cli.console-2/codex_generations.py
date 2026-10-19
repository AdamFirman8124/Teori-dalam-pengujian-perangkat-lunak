

# Generated at 2022-06-12 20:23:55.665492
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    print('Testing ConsoleCLI.cmdloop()...'),
    test_cli = ConsoleCLI([])
    test_cli.module_args = lambda module: ['module1_arg1=', 'module1_arg2=']
    test_cli.list_modules = lambda: ['module1', 'module2']
    test_cli.modules = test_cli.list_modules()
    for module in test_cli.modules:
        setattr(test_cli, 'do_' + module, lambda arg, module=module: test_cli.default(module + ' ' + arg))
        setattr(test_cli, 'help_' + module, lambda module=module: test_cli.helpdefault(module))
    test_cli.inventory = Mock()

# Generated at 2022-06-12 20:23:58.810100
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    cli = ConsoleCLI()
    modules = cli.list_modules()
    assert('ping' in modules)


# Generated at 2022-06-12 20:23:59.828134
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    console = ConsoleCLI()
    console.cmdloop()

# Generated at 2022-06-12 20:24:04.988530
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    import ansible.plugins.loader
    test_plugin = ansible.plugins.loader.PluginLoader.find_plugin("cron")
    assert test_plugin.endswith("/ansible/modules/system/cron.py")
    oc, a, _, _ = plugin_docs.get_docstring(test_plugin, fragment_loader, is_module=True)
    assert "name" in oc['options']
    assert "minute" in oc['options']
    assert "hour" in oc['options']

    # TODO: It would be better to use mock from the standard library to mock readline
    class MockReadline():
        def __init__(self, line):
            self.line = line
        def readline(self):
            return self.line

    console_cli = ConsoleCLI()
    console_

# Generated at 2022-06-12 20:24:10.894583
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    console = ConsoleCLI()
    assert console.module_args('copy') == ['content', 'dest', 'directory_mode', 'follow', 'force', 'mode', 'owner', 'regexp', 'remote_src', 'selevel', 'serole', 'setype', 'seuser', 'src', 'validate']

# Generated at 2022-06-12 20:24:21.776568
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    """
    [console/console.py]::ConsoleCLI::helpdefault
    """
    # from console.console import ConsoleCLI
    module_name = 'setup' # type: str
    c = ConsoleCLI()

    c.module_loader = mock.Mock()
    
    c.module_loader.find_plugin.return_value = 'setup'
    
    c.fragment_loader = mock.Mock()
    c.fragment_loader.load.return_value = {'doc': {
        'options': {
            'simple_option': {'description': ['description'], 'required': False, 'type': 'str'}
        },
        'module': True,
        'short_description': 'module description'
    }}

    c.helpdefault(module_name)
    assert True

# Generated at 2022-06-12 20:24:25.087966
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    # Test for no params
    # Test for one param
    # Test for multiple params
    # Test for error processing
    pass

# Test for method __init__ of class ConsoleCLI

# Generated at 2022-06-12 20:24:32.091154
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    """
    ConsoleCLI.do_cd()
    """
    consol = ConsoleCLI()
    consol.do_cd('host1')
    assert consol.cwd == 'host1'
    consol.do_cd('host2')
    assert consol.cwd == 'host2'
    consol.do_cd('host*')
    assert consol.cwd == 'host*'


# Generated at 2022-06-12 20:24:40.271165
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    cli = ansible_console.ConsoleCLI()
    cli.inventory = dict(hosts=dict(k1=hostvars(dict(b=1)), k2=hostvars(dict(b=1)), k3=hostvars(dict(b=1))))
    cli.groups = dict(group1=dict(hosts=dict(k1=hostvars(dict(b=1)), k2=hostvars(dict(b=1)), k3=hostvars(dict(b=1)))))
    r = cli.complete_cd('', 'cd ', 0, 0)
    assert r == ['group1', 'k1', 'k2', 'k3']
    r = cli.complete_cd('', 'cd g', 0, 0)
    assert r == ['group1']
    r = cl

# Generated at 2022-06-12 20:24:48.972011
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    stdout_save = sys.stdout
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    m = None
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        m = ConsoleCLI()
        m.do_exit = MagicMock(return_value=-1)
        m.cmdloop()

    sys.stdout = stdout_save
    stdout = capturedOutput.getvalue()
    assert 'Ansible-console was exited.' in stdout
    m.do_exit.assert_called_with('')
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == -1


# Generated at 2022-06-12 20:25:21.732085
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    # create a new object for class ConsoleCLI
    object_ConsoleCLI = ConsoleCLI()
    # create a parameter 'arg' for method do_list
    arg = None
    # call method do_list of class ConsoleCLI with parameter 'arg'
    result = object_ConsoleCLI.do_list(arg)
    assert result is None


# Generated at 2022-06-12 20:25:22.878396
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    cli = ConsoleCLI()
    assert cli.list_modules() is not None



# Generated at 2022-06-12 20:25:31.716541
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    #Args:
    #    param: name of module for which to show help
    #Return:
    #    None
    #Raises:
    #    None
    #Succeed:
    #    The name of the module is present in the list of modules.
    #    The module has documentation.
    #    The method runs without exception.
    #Fail:
    #    The name of the module is not present in the list of modules.
    #    The module does not have documentation.
    #    The method runs with an exception.
    #    The method displays output.
    #TODO: This method needs to be more thoroughly tested
    consoleCLI = ConsoleCLI()
    module_name = 'ping'
    consoleCLI.modules = [module_name]
    consoleCLI.modules.append('shell')
    in_

# Generated at 2022-06-12 20:25:39.213514
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    import os
    from collections import namedtuple

    argv = namedtuple('argv', ['connection'])
    options = argv(connection='ssh')
    args = os.environ
    args['inventory'] = "test/test_console/hosts"
    args['listhosts'] = None
    args['listtasks'] = None
    args['listtags'] = None
    args['syntax'] = None
    args['module_path'] = None
    args['forks'] = None
    args['remote_user'] = None
    args['private_key_file'] = None
    args['ssh_common_args'] = None
    args['ssh_extra_args'] = None
    args['sftp_extra_args'] = None
    args['scp_extra_args'] = None

# Generated at 2022-06-12 20:25:46.151448
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    from ansible.errors import AnsibleError
    from ansible.cli.console import ConsoleCLI
    from six import StringIO
    from unit.mock.loader import DictDataLoader
    from unit.mock.path import mock_unfrackpath_noop
    from unit.mock.plugins import MockModuleCollector
    from unit.mock.plugins import MockModuleUtilsPlugin
    from unit.mock.plugins import MockPluginLoader
    from unit.modules.fake_modules import AnsibleExitJson
    from unit.modules.fake_modules import AnsibleFailJson
    from unit.modules.fake_modules import ModuleTestCase
    from shutil import rmtree

    def setUpModule():
        module_loader.add_directory('')
        display.verbosity = 4

# Generated at 2022-06-12 20:25:55.404714
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    global consoleCLI
    consoleCLI.inventory = FakeInventory()

    # No argument
    consoleCLI.cwd = 'foo'
    consoleCLI.do_cd('')
    assert consoleCLI.cwd == '*'

    # With argument
    consoleCLI.do_cd('all')
    assert consoleCLI.cwd == 'all'

    # Bad group
    consoleCLI.do_cd('somebadgroup')
    assert consoleCLI.cwd == 'all'

    # Good group
    consoleCLI.do_cd('somegroup')
    assert consoleCLI.cwd == 'somegroup'

    # Good host
    consoleCLI.do_cd('somehost')
    assert consoleCLI.cwd == 'somehost'



# Generated at 2022-06-12 20:26:00.600428
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    console_cli = ConsoleCLI()
    console_cli.default(
        {'ansible_connection': 'winrm'},
        {'host_list': ['127.0.0.1'], 'module_path': 'test_path'},
        {'connection': 'winrm', 'remote_user': 'test_user', 'become_user': 'test_become_user',
         'become_method': 'test_become_method', 'check_mode': False, 'diff': False}
    )

# Generated at 2022-06-12 20:26:02.987253
# Unit test for method run of class ConsoleCLI
def test_ConsoleCLI_run():
    # Unit test doesn't catch the KeyboardInterrupt exception raised inside cmdloop method.
    # So, we need to exit after cmdloop is finished.
    sys.exit = lambda: None
    console_cli = ConsoleCLI()
    console_cli.run()


# Generated at 2022-06-12 20:26:07.231992
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    consolecli = ConsoleCLI()
    consolecli.get_plugins = lambda x: ['plug1', 'plug2']
    assert consolecli.list_modules() == ['plug1', 'plug2']

# Generated at 2022-06-12 20:26:18.869981
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    consolecli = ConsoleCLI()
    assert consolecli.module_args('add_host') == ['name', 'groups', 'host_vars']
    assert consolecli.module_args('ansible') == ['host_pattern', 'module_name', 'module_args', 'forks', 'become', 'become_method', 'become_user', 'check']
    assert consolecli.module_args('apt_key') == ['id', 'keyserver', 'data', 'state', 'absent_keyserver', 'absent_id']

# Generated at 2022-06-12 20:27:12.352031
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    global console_runner
    console_runner = ConsoleCLI('','','','','','','','','','','','','','','','','','','','','')
    console_runner.default('arg')


# Generated at 2022-06-12 20:27:22.427421
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    from unittest.mock import patch, call

    class FakeSelf(object):
        def __init__(self):
            self.line = ''
            self.blah = False

    console_cli = ConsoleCLI()

    with patch.object(console_cli, 'cmdloop') as cmdloop:
        console_cli.cmdloop()
        assert cmdloop.call_count == 1

    with patch.object(console_cli, 'onecmd') as onecmd:
        console_cli.cmdloop(fake=True)
        assert onecmd.call_count == 1

    with patch.object(console_cli, 'emptyline') as emptyline:
        console_cli.cmdloop(fake=True)
        assert emptyline.call_count == 1

# Generated at 2022-06-12 20:27:24.018363
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    ConsoleCLI().cmdloop()

# Generated at 2022-06-12 20:27:25.791312
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    console = ConsoleCLI()
    assert console.do_list('groups') == None

# Generated at 2022-06-12 20:27:28.542699
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():

    class Args(object):
        pass

    c = ConsoleCLI(args=Args())
    c.completedefault(text='', line='', begidx=0, endidx=0)


# Generated at 2022-06-12 20:27:32.164374
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    module_name = "something"
    text = ''
    line = module_name + " arg=val"
    begidx = len(module_name) + 1
    endidx = len(line)
    res = ConsoleCLI.module_args(module_name)
    res = list(res)
    assert res == ['arg']


# Generated at 2022-06-12 20:27:39.228811
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    cli = ConsoleCLI()
    cli.pattern = 'all'
    cli.inventory = mock.MagicMock()
    cli.inventory.list_hosts.return_value = [mock.MagicMock()]
    cli.inventory.list_groups.return_value = [mock.MagicMock()]
    cli.inventory.groups = [mock.MagicMock()]
    cli.inventory.groups[0].name = 'example'
    cli.inventory.list_hosts.return_value[0].name = 'example'
    cli.loader = mock.MagicMock()
    cli.loader.get_basedir.return_value = '/example'
    cli.loader.find_plugin.return_value = '/example'
    cli.variable_manager = mock.Magic

# Generated at 2022-06-12 20:27:45.240444
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    #args = defaultdict(list)
    #args = {'base_dir': os.environ.get('PYTHONPATH'), 'debug': True}
    args = {}

    context.CLIARGS = args
    ansible_base = BaseCLI()
    cli = ConsoleCLI.load(ansible_base)

    text = 'text'
    line = 'line'
    begidx = 0
    endidx = 5
    result = cli.completedefault(text, line, begidx, endidx)
    assert result == []


# Generated at 2022-06-12 20:27:51.978665
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    from ansible.errors import AnsibleOptionsError
    cli = ConsoleCLI(args=[])
    try:
        cli.helpdefault("ping")
    except AnsibleOptionsError as e:
        assert e.message == "Missing required 'inventory' parameter"

# Generated at 2022-06-12 20:27:57.327831
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    cli = ConsoleCLI(args=['ansible', 'all', '--tree', '/tmp/debug_tree'])
    assert cli.module_args('shell') == ['chdir', 'creates', 'executable', 'removes', 'warn']
    assert cli.module_args('command') == ['chdir', 'creates', 'executable', 'removes', 'warn']

# Generated at 2022-06-12 20:28:56.478223
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
  module_name = 'setup' # a valid ansible module
  c = ConsoleCLI()
  c.cwd = 'all'
  c.selected = ['localhost']
  #
  # set up the shell to support tasks
  c._play_prereqs()
  #
  # the task is to run a module command without arguments
  task = dict(action=dict(module=module_name))
  #
  # set up the play to run the task
  play_ds = dict(
    name="Ansible Shell",
    hosts=c.cwd,
    gather_facts='no',
    tasks=[task],
  )
  play = Play().load(play_ds, variable_manager=c.variable_manager, loader=c.loader)
  #
  # run the play
  cb = 'minimal'

# Generated at 2022-06-12 20:29:01.938263
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    console_cli = ConsoleCLI()
    f = open('./test_console_cli_completedefault.data', 'r')
    if f.mode == 'r':
        line = f.readline().rstrip('\n')
        while line != '':
            l = line.split(' ')
            print(console_cli.completedefault(l[0], line, 1, len(l[0])))
            line = f.readline().rstrip('\n')


# Generated at 2022-06-12 20:29:06.384882
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    #consoleCLI, args = mock_consoleCLI()
    hosts = """
    [testgroup1]
    localhost
    127.0.0.3

    [testgroup2]
    127.0.0.1
    127.0.0.4
    """
    inventory = Inventory(Loader=DataLoader())
    inventory_source = InventorySource(host_list=hosts)
    inventory.add_source('hosts', inventory_source)   
    args = dict(connection='local', host_list=hosts, pattern='localhost', forks=10, remote_user='root', become=False, become_method='sudo', become_user='root', check=False, diff=False, verbosity=3, inventory=inventory)
    consoleCLI = ConsoleCLI(args)

# Generated at 2022-06-12 20:29:15.772611
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    ConsoleCLI.do_list = lambda self, arg: None
    ConsoleCLI.groups = []
    ConsoleCLI.selected = []

    # Test 1
    ConsoleCLI.groups = [
        {'hosts': ['host1', 'host2'], 'vars': {}, 'name': 'group1'},
        {'hosts': ['host3', 'host4'], 'vars': {}, 'name': 'group2'}]

# Generated at 2022-06-12 20:29:22.004808
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    # Check for group
    for group in hosts:
        # Check for all hosts in group
        for host in group.hosts:
            # Create ConsoleCLI
            cli = ConsoleCLI()
            # Create line with the host address
            test_line = 'cd '+host.name
            # split the line
            test_line = test_line.split()
            # Set begin and end index
            begidx = 0
            endidx = len(test_line)
            # Call method complete_cd
            result = cli.complete_cd(test_line[1], test_line, begidx, endidx)
            # Result must be a list
            assert isinstance(result, list)
            # Result must contain the one host
            assert host.name in result
            # The length of the result must be 1
           

# Generated at 2022-06-12 20:29:32.277946
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    import sys
    import StringIO
    from ansible.module_utils.six.moves import reload_module

    # Load config file
    config_file = '/etc/ansible/ansible.cfg'
    if os.path.exists(config_file):
        import __main__
        __main__.CLI = AnsibleCLI([])
        context._init_global_context(__main__.CLI)
        context.CLIARGS = {'config': config_file}
        config.load_config_file()

    # Load console_cli class
    reload_module(console_cli)
    cli = console_cli.ConsoleCLI()

    # Set test environment
    argv_org = sys.argv
    stdout_org = sys.stdout

# Generated at 2022-06-12 20:29:37.976254
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():

    import os

    # make sure the history file does not exist
    histfile = os.path.join(os.path.expanduser("~"), ".ansible-console_history")
    try:
        os.remove(histfile)
    except OSError:
        pass

    # Create a prompt and start the command loop
    prompt = ConsoleCLI('ansible-console')

    # Make sure the history file exists
    assert os.path.exists(histfile)

    # Make sure the history file is empty
    assert os.stat(histfile).st_size == 0

# Generated at 2022-06-12 20:29:41.528887
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    mock_module_finder = Mock(return_value=['testmodule'])
    cli = ConsoleCLI(connection=None, module_finder=mock_modules_finder)
    assert cli.list_modules() == ['testmodule']
    mock_modules_finder.assert_called_once_with()

# Generated at 2022-06-12 20:29:42.385715
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
  result = True
  return result

# Generated at 2022-06-12 20:29:46.983001
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    config_file = './config/ansible.cfg'
    if not os.path.isfile(config_file):
        print('configuration file not found, config file should be located in ./config/ansible.cfg')
    config.load_config_file(config_file)
    # mock an inventory
    groups = dict()
    groups['all'] = dict()
    groups['all']['hosts'] = ['localhost']
    groups['subset'] = dict()
    groups['subset']['hosts'] = ['localhost']

    # Test class attributes
    cli = ConsoleCLI()
    cli.selected = ['localhost']
    cli.inventory =  Mock(get_groups_dict=Mock(return_value=groups))
    cli.do_list('subset')
